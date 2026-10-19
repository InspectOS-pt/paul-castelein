import { cpSync,existsSync,mkdirSync,readFileSync,rmSync,statSync,writeFileSync } from 'node:fs';
import path from 'node:path';
const base=process.cwd();
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
 if(!html.includes('noindex,nofollow'))throw Error('Preview indexing rule missing: '+page);
 if(!redirect&&(html.match(/hreflang="x-default"/g)||[]).length!==1)throw Error('Missing alternate languages: '+page);
 for(const [,src] of html.matchAll(/(?:src|href)="(\/[^"#?]*)[^"]*"/g)){
  let file=path.join(base,src);
  if(existsSync(file)&&statSync(file).isDirectory())file=path.join(file,'index.html');
  if(!existsSync(file))throw Error('Missing local resource: '+page+' '+src);
 }
 for(const [,json] of html.matchAll(/<script type="application\/(?:ld\+)?json"[^>]*>([\s\S]*?)<\/script>/g))JSON.parse(json);
 if(/[—–]/u.test(html))throw Error('Unexpected dash character in '+page);
 if(/past credentials|past resume|unsolicited pitches|PPTX\+|DOCX\+/i.test(html))throw Error('Removed copy remains in '+page);
 const ids=[...html.matchAll(/\bid="([^"]+)"/g)].map(m=>m[1]);
 if(new Set(ids).size!==ids.length)throw Error('Duplicate id: '+page);
}
const out=path.join(base,'dist');rmSync(out,{recursive:true,force:true});mkdirSync(out,{recursive:true});
const publicFiles=[...pages,'styles.css','main.js','favicon.svg','og.jpg','robots.txt','sitemap.xml','llms.txt','vercel.json','assets/portrait.webp','assets/reference.css','assets/reference-interior.css','assets/infographics/replacing-trust-with-proof.webp','assets/infographics/business-model-2030.webp','assets/infographics/information-asymmetry-collapse.webp','assets/infographics/vertical-data-flywheel.webp','assets/infographics/five-moats.webp','assets/fonts/reference-fonts.css','assets/fonts/playfair-display-latin.woff2','assets/fonts/playfair-display-latin-ext.woff2','assets/fonts/instrument-sans-latin.woff2','assets/fonts/instrument-sans-latin-ext.woff2','assets/fonts/playfair-display-OFL.txt','assets/fonts/instrument-sans-OFL.txt'];
for(const file of publicFiles){mkdirSync(path.dirname(path.join(out,file)),{recursive:true});cpSync(file,path.join(out,file));}
// A prebuilt public bundle needs routing only, not commands referring to source files.
const sourceConfig=JSON.parse(readFileSync('vercel.json','utf8'));
writeFileSync(path.join(out,'vercel.json'),JSON.stringify({redirects:sourceConfig.redirects},null,2)+'\n');
console.log(`Validated ${contentPages.length} content/error pages in 3 languages, ${pages.length-contentPages.length} legacy destinations and ${publicFiles.length} public files. Source manuscripts and QA excluded.`);
