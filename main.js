/* Only local UI and local email drafts. No requests or form submissions. */
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
 const fields=Object.fromEntries(['name','email','organisation','startingPoint','opportunity','contribution'].map(key=>[key,document.getElementById(key)]));
 const status=document.querySelector('#draft-status'),fallback=document.querySelector('#draft-fallback'),copyArea=document.querySelector('#draft-copy');
 const query=new URLSearchParams(location.search),start=query.get('starting-point');
 if(Object.hasOwn(copy.options,start))fields.startingPoint.value=start;
 const estate=query.get('subject')==='estateos';
 if(estate){fields.startingPoint.value='other';fields.opportunity.value=copy.estateSubject;}
 async function copyText(text,area){try{await navigator.clipboard.writeText(text);return true;}catch{if(area){area.focus();area.select();}return false;}}
 document.querySelector('#copy-email').addEventListener('click',async()=>{document.querySelector('#copy-status').textContent=await copyText('paul@skaler.pt')?copy.copiedEmail:'paul@skaler.pt';});
 function showError(key,message){document.getElementById(`${key}-error`).textContent=message;if(message)fields[key].setAttribute('aria-invalid','true');else fields[key].removeAttribute('aria-invalid');}
 let draft='';
 function prepare(){
  const subject=estate?copy.estateSubject:copy.subject;
  const body=[`${copy.name}: ${fields.name.value.trim()}`,`${copy.email}: ${fields.email.value.trim()}`,`${copy.organisation}: ${fields.organisation.value.trim()}`,`${copy.startingPoint}: ${copy.options[fields.startingPoint.value]}`,'',`${copy.opportunity}:\n${fields.opportunity.value.trim()}`,'',`${copy.contribution}:\n${fields.contribution.value.trim()}`].join('\n');
  draft=`${subject}\n\n${body}`;form.dataset.draftHref=`mailto:paul@skaler.pt?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;copyArea.value=draft;
 }
 for(const field of Object.values(fields))field.addEventListener('input',()=>{if(Object.hasOwn(copy.errors,field.id))showError(field.id,'');prepare();});
 form.addEventListener('submit',event=>{
  event.preventDefault();let invalid;
  for(const key of Object.keys(copy.errors)){const valid=fields[key].value.trim()&&(key!=='email'||fields.email.validity.valid);showError(key,valid?'':copy.errors[key]);if(!valid&&!invalid)invalid=fields[key];}
  if(invalid){status.textContent='';invalid.focus();return;}
  prepare();fallback.hidden=false;status.textContent=copy.draftReady;location.href=form.dataset.draftHref;
 });
 document.querySelector('#copy-introduction').addEventListener('click',async()=>{if(await copyText(draft,copyArea))status.textContent=copy.copiedIntroduction;});
 prepare();document.querySelector('#introduction-fields').disabled=false;
})();
