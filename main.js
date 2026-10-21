/* Local navigation and same-origin introduction submission. */
(() => {
 const menus=document.querySelectorAll('.mobile-menu');
 document.addEventListener('keydown',event=>{
  if(event.key!=='Escape')return;
  for(const menu of menus)if(menu.open){menu.open=false;menu.querySelector('summary').focus();}
 });
 document.addEventListener('click',event=>{for(const menu of menus)if(menu.open&&(!menu.contains(event.target)||event.target.closest('a')))menu.open=false;});
 if(location.pathname==='/'){
  const legacy={'#approach':'/thesis/','#vision':'/thesis/','#principles':'/thesis/','#insights':'/memos/'};
  if(legacy[location.hash])location.replace(legacy[location.hash]);
 }
 for(const a of document.querySelectorAll('.language-nav a')){const target=new URL(a.href);target.search=location.search;target.hash=location.hash;a.href=target.href;}
 const form=document.querySelector('#introduction-form');if(!form)return;
 const copy=JSON.parse(document.querySelector('#form-copy').textContent);
 const fields=Object.fromEntries(['name','email','organisation','startingPoint','startingPointOther','opportunity','contribution'].map(key=>[key,document.getElementById(key)]));
 const status=document.querySelector('#form-status'),fieldset=document.querySelector('#introduction-fields'),submit=form.querySelector('[type="submit"]');
 const query=new URLSearchParams(location.search),start=query.get('starting-point');
 if(Object.hasOwn(copy.options,start))fields.startingPoint.value=start;
 if(query.get('subject')==='estateos'){fields.startingPoint.value='other';fields.startingPointOther.value=copy.estateSubject;fields.opportunity.value=copy.estateSubject;}
 function showError(key,message){document.getElementById(`${key}-error`).textContent=message;if(message)fields[key].setAttribute('aria-invalid','true');else fields[key].removeAttribute('aria-invalid');}
 function syncOther(){const active=fields.startingPoint.value==='other';document.querySelector('#startingPointOther-field').hidden=!active;fields.startingPointOther.disabled=!active;fields.startingPointOther.required=active;if(!active)showError('startingPointOther','');}
 fields.startingPoint.addEventListener('change',syncOther);
 for(const field of Object.values(fields))field.addEventListener('input',()=>{if(Object.hasOwn(copy.errors,field.id))showError(field.id,'');status.textContent='';});
 let sending=false;
 form.addEventListener('submit',async event=>{
  event.preventDefault();if(sending)return;let invalid;
  for(const key of Object.keys(copy.errors)){const valid=(key==='startingPointOther'&&fields.startingPoint.value!=='other')||(fields[key].value.trim()&&(key!=='email'||fields.email.validity.valid));showError(key,valid?'':copy.errors[key]);if(!valid&&!invalid)invalid=fields[key];}
  if(invalid){status.textContent='';invalid.focus();return;}
  const payload=Object.fromEntries(Object.entries(fields).filter(([key])=>key!=='startingPointOther'||fields.startingPoint.value==='other').map(([key,field])=>[key,field.value.trim()]));
  payload.locale=document.documentElement.lang.split('-')[0];payload.website=document.querySelector('#website').value;
  sending=true;fieldset.disabled=true;submit.textContent=copy.sending;form.setAttribute('aria-busy','true');status.textContent=copy.sending;
  const controller=new AbortController(),timeout=setTimeout(()=>controller.abort(),55000);
  try{
   const response=await fetch(form.action,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(payload),credentials:'same-origin',signal:controller.signal});
   const result=await response.json();
   if(!response.ok||result.ok!==true||result.code!=='sent')throw new Error(result.code==='unavailable'?'unavailable':result.code==='invalid'?'invalid':'failed');
   form.reset();syncOther();status.textContent=copy.sent;
  }catch(error){status.textContent=error.message==='unavailable'?copy.unavailable:error.message==='invalid'?copy.invalid:copy.failed;}
  finally{clearTimeout(timeout);sending=false;fieldset.disabled=false;submit.textContent=copy.action;form.removeAttribute('aria-busy');}
 });
 syncOther();fieldset.disabled=false;
})();
