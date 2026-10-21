"""Render Paul's October 19 personal master and its review translations."""
from html import escape
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit
import json
import os
import re
from reference_figures import reference_figure
from reference_layout import render_reference, reference_header, reference_footer
ROOT=Path(__file__).resolve().parent.parent
ORIGIN=os.environ.get('CASTELEIN_SITE_ORIGIN','https://castelein.eu.com').rstrip('/')
o=urlsplit(ORIGIN)
if o.scheme!='https' or not o.netloc or o.path or o.query or o.fragment or o.username or o.password: raise ValueError('Expected HTTPS origin')
LANGS={'en':('en','English',''),'pt':('pt-PT','Português','/pt'),'es':('es','Español','/es')}
PAGES=['','thesis','partnerships','memos','about','contact','privacy']
FILES=[]
def e(v):return escape(str(v),quote=True)
def ps(v):return ''.join('<p>'+e(x)+'</p>' for x in ([v] if isinstance(v,str) else v))
def route(key,lang):return LANGS[lang][2]+'/'+(key.strip('/')+'/' if key.strip('/') else '')
def local(href,lang):
 if not href.startswith('/'):return href
 u=urlsplit(href);return urlunsplit(('','',route(u.path,lang),u.query,u.fragment))
def a(label,href,cls='',**attrs):
 extra=''.join(' '+k.replace('_','-')+'="'+e(v)+'"' for k,v in attrs.items())
 return '<a href="'+e(href)+'" class="'+e(cls)+'"'+extra+'>'+e(label)+'</a>'
def button(label,href,secondary=False):return a(label,href,'button secondary' if secondary else 'button')
def desc(key,d):
 p=d[key or 'home'];t=p.get('intro',p.get('lead',d['home']['intro']));return (t[0] if isinstance(t,list) else t)[:220]
def shell(key,d,lang,body,error=False):
 ui=d['ui'];url=ORIGIN+route(key,lang)
 title=ui['notFound'] if error else ((d[key]['title'] if key else ui['identity'].split(' · ')[0])+' | Pieter Paul Castelein')
 description=ui['notFoundText'] if error else desc(key,d)
 alternates=''.join(f'<link rel="alternate" hreflang="{tag}" href="{ORIGIN}{route(key,code)}">' for code,(tag,_,_) in LANGS.items())+f'<link rel="alternate" hreflang="x-default" href="{ORIGIN}{route(key,"en")}">'
 schema={'@context':'https://schema.org','@type':'Article' if key=='memos' else 'WebPage','name':title,'url':url,'description':description,'inLanguage':LANGS[lang][0]}
 if key=='memos':schema.update(headline=d['memos']['articleTitle'],author={'@type':'Person','name':'Pieter Paul Castelein'},datePublished='2026-10-19')
 if not key:schema.update({'@type':'ProfilePage','mainEntity':{'@type':'Person','name':'Pieter Paul Castelein','jobTitle':ui['identity'].split(' · ')[0],'sameAs':['https://www.linkedin.com/in/pieter-paul-castelein/'],'worksFor':{'@type':'Organization','name':'Skaler','url':'https://www.skaler.pt/'}}})
 structured=json.dumps(schema,ensure_ascii=False).replace('</','<\\/')
 figure_styles='<link rel="stylesheet" href="/assets/fonts/native-fonts.css"><link rel="stylesheet" href="/assets/native-figures.css">' if key in ['', 'thesis', 'memos'] and not error else ''
 return f'''<!doctype html><html lang="{LANGS[lang][0]}"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title><meta name="description" content="{e(description)}"><meta name="author" content="Pieter Paul Castelein">
<meta name="robots" content="noindex,nofollow"><meta name="color-scheme" content="light"><meta name="theme-color" content="#fafaf8">
<link rel="canonical" href="{e(url)}">{alternates}<meta property="og:type" content="{'article' if key=='memos' else 'website'}">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(description)}"><meta property="og:url" content="{e(url)}">
<meta property="og:image" content="{ORIGIN}/og.jpg?v=20261019-editorial"><meta property="og:image:alt" content="Pieter Paul Castelein. {e(ui['identity'])}">
<meta name="twitter:card" content="summary_large_image"><link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preload" href="/assets/fonts/playfair-display-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/fonts/reference-fonts.css"><link rel="stylesheet" href="/assets/reference.css">{chr(60)+'link rel="stylesheet" href="/styles.css"><link rel="stylesheet" href="/assets/reference-interior.css">' if key or error else ''}{figure_styles}<script src="/main.js" defer></script><script type="application/ld+json">{structured}</script>
</head><body class="{'reference-home' if not key and not error else 'reference-interior'}"><a class="skip-link" href="#main">{e(ui['skip'])}</a>
{reference_header(d,lang,key)}
<main id="main">{body}</main>{reference_footer(d,lang)}</body></html>'''
def intro(key,d,lang):
 p=d[key];label=d['ui']['nav'].get(key,p['title']);lead=[] if key=='memos' else p.get('intro',p.get('lead',[]))
 return f'<header class="wrap page-heading"><p class="eyebrow">{e(label)}</p><h1>{e(p["title"])}</h1><div class="lead">{ps(lead)}</div></header>'
def home(d,lang):
 return render_reference(d,lang)

def blocks(sections,d=None,lang=None,context=''):
 result=''
 for n,b in enumerate(sections,1):
  result+=f'<section class="reading-section" id="section-{n}"><h2>{e(b["title"])}</h2>{ps(b["text"])}'
  if context=='thesis' and b.get('items'):result+=reference_figure(2,lang)
  if context=='thesis' and n==2:result+=reference_figure(3,lang)
  if b.get('items'):result+='<div class="thesis-pair">'+''.join(f'<div><h3>{e(i["title"])}</h3>{ps(i["text"])}</div>' for i in b['items'])+'</div>'
  if b.get('steps'):
   if d is not None:result+=reference_figure(4,lang)
   result+='<ol class="flywheel">'+''.join(f'<li><span class="index">0{j}</span><div><h3>{e(i["title"])}</h3>{ps(i["text"])}</div></li>' for j,i in enumerate(b['steps'],1))+'</ol>'
  if b.get('closing'):result+=ps(b['closing'])
  result+='</section>'
 return result
def reading(key,d,lang):
 p=d[key];extra=f'<h2 class="memo-title">{e(p["articleTitle"])}</h2>{ps(p["lead"])}{reference_figure(5,lang)}' if key=='memos' else ''
 return intro(key,d,lang)+f'<div class="wrap reading-layout"><aside class="reading-rail"><p>Pieter Paul Castelein</p>{a(d["ui"]["contactAction"],route("contact",lang),"text-link")}</aside><article class="reading">{extra}{blocks(p["sections"],d,lang,key)}<div class="actions">{button(d["ui"]["contactAction"],route("contact",lang))}</div></article></div>'
def partnerships(d,lang):
 p=d['partnerships'];ui=d['ui']
 rows=''.join(f'<section class="partner-row" id="{slug}"><h2>{e(partner["title"])}</h2><div>{ps(partner["text"])}{a(ui["contactAction"],route("contact",lang)+"?starting-point="+point,"text-link")}</div></section>' for partner,slug,point in zip(d['home']['partners'],['assets','capital','experts'],['assets','capital','expertise']))
 return intro('partnerships',d,lang)+f'<div class="wrap partnership-content">{rows}<section class="economics"><div class="section-heading"><h2>{e(p["sectionTitle"])}</h2>{ps(p["sectionIntro"])}</div><div class="economics-pair"><div><h3>{e(p["ownerTitle"])}</h3>{ps(p["ownerText"])}</div><div><h3>{e(p["operatingTitle"])}</h3>{ps(p["operatingText"])}</div></div></section><div class="actions">{button(p["action"],route("contact",lang))}</div></div>'
def about(d,lang):
 return intro('about',d,lang)+f'<div class="wrap about-layout"><figure><img src="/assets/portrait.webp" alt="{e(d["ui"]["portraitAlt"])}" width="400" height="400"><figcaption>Pieter Paul Castelein</figcaption></figure><article class="reading">{blocks(d["about"]["sections"])}<div class="actions">{button(d["ui"]["contactAction"],route("contact",lang))}{a("Skaler.pt","https://www.skaler.pt/","text-link")}</div></article></div>'
def contact(d,lang):
 p=d['contact'];f=d['form'];config=json.dumps(f,ensure_ascii=False).replace('</','<\\/')
 def field(key,label,t='text'):
  autocomplete='name' if key=='name' else 'email'
  maximum=120 if key=='name' else 254
  return f'<div class="form-field"><label for="{key}">{e(label)}</label><input id="{key}" name="{key}" type="{t}" autocomplete="{autocomplete}" maxlength="{maximum}" required aria-describedby="{key}-error"><span class="field-error" id="{key}-error"></span></div>'
 options=''.join(f'<option value="{key}">{e(value)}</option>' for key,value in f['options'].items())
 return f'''<section class="wrap contact-layout"><header><p class="eyebrow">{e(d['ui']['nav']['contact'])}</p><h1>{e(p['title'])}</h1>{ps(p['intro'])}{a('LinkedIn','https://www.linkedin.com/in/pieter-paul-castelein/','text-link')}</header>
<form id="introduction-form" class="introduction-form" action="/api/enquiry" method="post" novalidate><h2>{e(p['summaryTitle'])}</h2><p class="muted">{e(p['summaryHelp'])}</p><fieldset id="introduction-fields" disabled><div class="form-pair">{field('name',f['name'])}{field('email',f['email'],'email')}</div><div class="form-field"><label for="startingPoint">{e(f['startingPoint'])}</label><select id="startingPoint" name="startingPoint">{options}</select></div><div class="form-field"><label for="opportunity">{e(f['opportunity'])}</label><textarea id="opportunity" name="opportunity" rows="5" maxlength="6000" required aria-describedby="opportunity-error"></textarea><span class="field-error" id="opportunity-error"></span></div>
<details class="additional-context"><summary>{e(f['organisation'])} / {e(f['contribution'])} ({e(f['optional'])})</summary><div class="form-field"><label for="organisation">{e(f['organisation'])}</label><input id="organisation" name="organisation" autocomplete="organization" maxlength="200"></div><div class="form-field"><label for="contribution">{e(f['contribution'])}</label><textarea id="contribution" name="contribution" rows="3" maxlength="3000"></textarea></div></details>
<div class="form-honeypot" aria-hidden="true"><label for="website">Website</label><input id="website" name="website" tabindex="-1" autocomplete="off"></div><button class="button" type="submit">{e(f['action'])}</button></fieldset><p class="field-help">{e(f['explanation'])} {a(f['privacy'],route('privacy',lang),'text-link')}</p><p id="form-status" class="status" role="status" aria-live="polite"></p><noscript><p>{e(f['fallback'])}</p></noscript></form><script type="application/json" id="form-copy">{config}</script></section>'''

def privacy(d,lang):
 p=d['privacy'];links=''.join('<p>'+a(link['label'],link['href'],'text-link')+'</p>' for link in p['links'])
 return f'<header class="wrap page-heading"><h1>{e(p["title"])}</h1><p class="lead">{e(p["intro"])}</p></header><div class="wrap narrow"><aside class="review-note"><h2>{e(p["noteTitle"])}</h2>{ps(p["note"])}</aside>{blocks(p["sections"])}<section class="reading-section"><h2>{e(p["linksTitle"])}</h2>{links}</section></div>'
def write(file,html):
 target=ROOT/file.lstrip('/');target.parent.mkdir(parents=True,exist_ok=True);target.write_text(html+'\n');FILES.append(file.lstrip('/'))
for lang in LANGS:
 d=json.loads((ROOT/'content/locales'/f'{lang}.json').read_text())
 for key in PAGES:
  if not key:body=home(d,lang)
  elif key in ['thesis','memos']:body=reading(key,d,lang)
  elif key=='partnerships':body=partnerships(d,lang)
  elif key=='about':body=about(d,lang)
  elif key=='contact':body=contact(d,lang)
  else:body=privacy(d,lang)
  write(route(key,lang)+'index.html',shell(key,d,lang,body))
 body=f'<section class="wrap page-heading"><h1>{e(d["ui"]["notFound"])}</h1>{ps(d["ui"]["notFoundText"])}{button(d["ui"]["backHome"],route("",lang))}</section>'
 write(LANGS[lang][2]+'/404.html',shell('',d,lang,body,True))
ALIASES={'how-we-build/':'/thesis/','vision/':'/thesis/','for-investors/':'/partnerships/#capital','for-asset-owners/':'/partnerships/#assets','build-with-me/':'/partnerships/','ventures/':'/#ventures','insights/':'/memos/','insights/building-a-company/':'/memos/','insights/distribution-business-model/':'/memos/#section-5','insights/finding-exceptional-people/':'/about/','insights/first-venture-brief/':'/contact/?starting-point=expertise','insights/assets-to-operating-business/':'/partnerships/#assets','insights/when-to-build-a-new-company/':'/memos/','insights/industry-expertise-to-business/':'/contact/?starting-point=expertise','insights/market-entry-business-model/':'/memos/#section-5','insights/beyond-investment/':'/partnerships/'}
for old,new in ALIASES.items():write(old+'index.html',f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="robots" content="noindex,nofollow"><meta http-equiv="refresh" content="0;url={e(new)}"><link rel="canonical" href="{e(ORIGIN+new)}"><title>Pieter Paul Castelein</title></head><body class="{'reference-home' if not key and not error else 'reference-interior'}">{a("Continue",new)}</body></html>')
(ROOT/'vercel.json').write_text(json.dumps({'$schema':'https://openapi.vercel.sh/vercel.json','framework':None,'buildCommand':'python3 scripts/build-site.py','installCommand':'','outputDirectory':'dist','functions':{'api/enquiry.py':{'maxDuration':60,'excludeFiles':'{assets/**,content/**,scripts/**,tests/**,qa/**,research/**,dist/**,**/*.html,**/*.md}'}},'redirects':[{'source':'/'+old.rstrip('/'),'destination':new,'permanent':True} for old,new in ALIASES.items()]},indent=2)+'\n')
urls=[ORIGIN+route(key,lang) for lang in LANGS for key in PAGES]
(ROOT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+e(u)+'</loc></url>' for u in urls)+'</urlset>\n')
(ROOT/'robots.txt').write_text('User-agent: *\nDisallow: /\n')
(ROOT/'llms.txt').write_text('# Pieter Paul Castelein\n\nPersonal thesis and partnership portal.\nPreview for content review.\n\n'+'\n'.join('- '+u for u in urls)+'\n')
(ROOT/'content/public-pages.json').write_text(json.dumps(FILES,indent=2)+'\n')
print(f'Generated 21 content pages, 3 error pages and {len(ALIASES)} legacy destinations.')
