import { cpSync,existsSync,mkdirSync,readFileSync,rmSync,statSync,writeFileSync } from 'node:fs';
import path from 'node:path';
const base=process.cwd();
const origin=(process.env.CASTELEIN_SITE_ORIGIN||'https://castelein.eu.com').replace(/\/+$/,'');
const indexable=['https://castelein.eu.com','https://www.castelein.eu.com'].includes(origin)&&['','production'].includes(process.env.VERCEL_ENV||'');
const pages=JSON.parse(readFileSync('content/public-pages.json','utf8'));
const locales=['en','pt','es'].map(lang=>JSON.parse(readFileSync(`content/locales/${lang}.json`,'utf8')));
function shape(a,b,at=''){
 if(Array.isArray(a)){if(!Array.isArray(b)||a.length!==b.length)throw Error('Locale array mismatch '+at);a.forEach((v,i)=>shape(v,b[i],at+'.'+i));}
 else if(a&&typeof a==='object'){if(!b||Object.keys(a).sort().join()!==Object.keys(b).sort().join())throw Error('Locale keys mismatch '+at);for(const k in a)shape(a[k],b[k],at+'.'+k);}
 else if(typeof a!==typeof b)throw Error('Locale type mismatch '+at);
}
for(const locale of locales.slice(1))shape(locales[0],locale);
const contentPages=pages.filter(page=>!readFileSync(page,'utf8').includes('http-equiv="refresh"'));
for(const page of pages){
 const html=readFileSync(page,'utf8'),redirect=html.includes('http-equiv="refresh"');
 if(!redirect&&(html.match(/<h1\b/g)||[]).length!==1)throw Error('Expected one h1: '+page);
 const expectedRobots=indexable&&!redirect&&!page.endsWith('404.html')?'index,follow':'noindex,nofollow';
 if(!html.includes(`<meta name="robots" content="${expectedRobots}">`))throw Error('Incorrect indexing rule: '+page);
 if(!redirect&&(html.match(/hreflang="x-default"/g)||[]).length!==1)throw Error('Missing alternate languages: '+page);
 for(const [,src] of html.matchAll(/(?:src|href)="(\/[^"#?]*)[^"]*"/g)){
  let file=path.join(base,src);
  if(existsSync(file)&&statSync(file).isDirectory())file=path.join(file,'index.html');
  if(!existsSync(file))throw Error('Missing local resource: '+page+' '+src);
 }
 for(const [,json] of html.matchAll(/<script type="application\/(?:ld\+)?json"[^>]*>([\s\S]*?)<\/script>/g))JSON.parse(json);
 if(/[—–]/u.test(html))throw Error('Unexpected dash character in '+page);
 if(/past credentials|past resume|unsolicited pitches|PPTX\+|DOCX\+/i.test(html))throw Error('Removed copy remains in '+page);
 if(/(?:^|\/)contact\/index\.html$/.test(page)){
  if(/mailto:|paul@skaler\.pt|copy-email|draft-fallback/.test(html))throw Error('Removed public contact email/draft remains: '+page);
  if(!html.includes('action="/api/enquiry"')||!html.includes('id="form-status"'))throw Error('Contact submission markup missing: '+page);
 }
 // Owner-marked presentation text must stay removed in every language rebuild.
 if(!redirect&&!html.includes('<span class="reference-wordmark">Castelein.</span>'))throw Error('Approved Castelein wordmark missing: '+page);
 const footer=html.match(/<footer class="reference-footer"[^>]*>[\s\S]*?<\/footer>/)?.[0]||'';
 if(/(?:Founder of|Fundador da|Fundador de) Skaler\.pt/i.test(footer))throw Error('Removed footer founder clause remains: '+page);
 if(/Dutch founder|fundador(?: e criador de empresas)? neerlandês|fundador(?: y creador de empresas)? neerlandés/i.test(html))throw Error('Superseded profile wording remains in '+page);
 if(/reference-identity|(?:The Architect|O Arquiteto|El Arquitecto) · Castelein\.eu\.com · Portugal|Skaler · Venture Studio/i.test(html))throw Error('Removed presentation label remains in '+page);
 for(const [figure] of html.matchAll(/<figure\b[^>]*>[\s\S]*?<\/figure>/g)){
  if(figure.includes('class="native-diagram"')&&figure.includes('<figcaption'))throw Error('Removed diagram caption remains in '+page);
 }
 const ids=[...html.matchAll(/\bid="([^"]+)"/g)].map(m=>m[1]);
 if(new Set(ids).size!==ids.length)throw Error('Duplicate id: '+page);
}
const expectedRobotsTxt=indexable?`User-agent: *\nAllow: /\nDisallow: /api/\n\nSitemap: ${origin}/sitemap.xml\n`:'User-agent: *\nDisallow: /\n';
if(readFileSync('robots.txt','utf8')!==expectedRobotsTxt)throw Error('Incorrect robots.txt policy');
const out=path.join(base,'dist');rmSync(out,{recursive:true,force:true});mkdirSync(out,{recursive:true});
const nativeFigureFiles=["assets/fonts/native-instrument-serif-italic-latin-ext.woff2","assets/fonts/native-instrument-serif-italic-latin.woff2","assets/fonts/native-instrument-serif-normal-latin-ext.woff2","assets/fonts/native-instrument-serif-normal-latin.woff2","assets/fonts/native-inter-normal-latin-ext.woff2","assets/fonts/native-inter-normal-latin.woff2","assets/fonts/native-jetbrains-mono-normal-latin-ext.woff2","assets/fonts/native-jetbrains-mono-normal-latin.woff2","assets/fonts/native-Instrument-Serif-OFL.txt","assets/fonts/native-Inter-OFL.txt","assets/fonts/native-JetBrains-Mono-OFL.txt","assets/fonts/native-fonts.css","assets/native-figures.css"];
const publicFiles=[...pages,...nativeFigureFiles,'styles.css','main.js','favicon.svg','og.jpg','robots.txt','sitemap.xml','llms.txt','vercel.json','assets/portrait.webp','assets/reference.css','assets/reference-interior.css','assets/fonts/reference-fonts.css','assets/fonts/playfair-display-latin.woff2','assets/fonts/playfair-display-latin-ext.woff2','assets/fonts/instrument-sans-latin.woff2','assets/fonts/instrument-sans-latin-ext.woff2','assets/fonts/playfair-display-OFL.txt','assets/fonts/instrument-sans-OFL.txt'];
for(const file of publicFiles){mkdirSync(path.dirname(path.join(out,file)),{recursive:true});cpSync(file,path.join(out,file));}
// Static files need routing only. Deploy the source api/enquiry.py separately;
// uploading this static directory alone does not provide contact submission.
const sourceConfig=JSON.parse(readFileSync('vercel.json','utf8'));
writeFileSync(path.join(out,'vercel.json'),JSON.stringify({redirects:sourceConfig.redirects},null,2)+'\n');
console.log(`Validated ${contentPages.length} content/error pages in 3 languages, ${pages.length-contentPages.length} legacy destinations and ${publicFiles.length} public files. Source manuscripts and QA excluded.`);
