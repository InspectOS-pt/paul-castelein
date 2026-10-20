"""Inert, localized recreation of Paul's selected Meta personal-site layout.

The template retains the supplied section markup and compiled utility styles.
No source JavaScript, network embeds, or source instructions are executed.
"""
from html import escape
from pathlib import Path
import re
from reference_figures import reference_figure
ROOT = Path(__file__).resolve().parent.parent
LABELS = {
 'en': {
  'principle':'Principle','livingProof':'Living Proof','portfolio':'Active Portfolio Ventures','assets':'Asset Owners','capital':'Capital','experts':'Experts','thesisMeta':'Thesis / Operating Model · Business Model of 2030','model':'Business Model of 2030','modelTitle':'Verified Reality and Permissioned Distribution','compounds':'Compounds with every transaction','flywheelPractice':'How the Vertical Flywheel Compounds in Practice:','profile':'Operator · Company builder · Based in Oeiras, Portugal','ownedDistribution':'Owned Distribution','talentFlywheel':'Skaler Talent Flywheel','engine':'Skaler.pt · The Engine','engineDescription':'AI-native venture studio · 9 capability tracks · 3 pod clusters','location':'Oeiras · Portugal','contactNote':'Your introduction comes directly to me. Start with a clear summary. No deck required.'},
 'pt': {
  'principle':'Princípio','livingProof':'Prova concreta','portfolio':'Empresas do portefólio em atividade','assets':'Proprietários de ativos','capital':'Capital','experts':'Especialistas','thesisMeta':'Tese / Modelo operacional · Modelo de negócio de 2030','model':'Modelo de negócio de 2030','modelTitle':'Realidade verificada e distribuição permissionada','compounds':'Reforça-se a cada transação','flywheelPractice':'Como o ciclo vertical se reforça na prática:','profile':'Operador · Criador de empresas · Sediado em Oeiras, Portugal','ownedDistribution':'Distribuição própria','talentFlywheel':'O ciclo de talento da Skaler','engine':'Skaler.pt · O motor','engineDescription':'Venture studio nativo de IA · 9 áreas de competência · 3 grupos de pods','location':'Oeiras · Portugal','contactNote':'A sua mensagem chega diretamente a mim. Comece com um resumo claro. Não é necessário enviar uma apresentação em diapositivos.'},
 'es': {
  'principle':'Principio','livingProof':'Prueba tangible','portfolio':'Empresas activas de la cartera','assets':'Propietarios de activos','capital':'Capital','experts':'Expertos','thesisMeta':'Tesis / Modelo operativo · Modelo de negocio de 2030','model':'Modelo de negocio de 2030','modelTitle':'Realidad verificada y distribución con permisos','compounds':'Se refuerza con cada transacción','flywheelPractice':'Cómo se refuerza el ciclo vertical en la práctica:','profile':'Operador · Creador de empresas · En Oeiras, Portugal','ownedDistribution':'Distribución propia','talentFlywheel':'El ciclo de talento de Skaler','engine':'Skaler.pt · El motor','engineDescription':'Venture studio nativo de IA · 9 áreas de capacidad · 3 grupos de pods','location':'Oeiras · Portugal','contactNote':'Su mensaje me llega directamente. Comience con un resumen claro. No es necesario enviar una presentación de diapositivas.'}
}
def route(key,lang):return ('' if lang=='en' else '/'+lang)+'/'+(key.strip('/')+'/' if key.strip('/') else '')
def render_reference(d,lang):
 template=(ROOT/'scripts/templates/reference-home.html').read_text()
 venture_urls=[v['url'] if not v['url'].startswith('/') else ('' if lang=='en' else '/'+lang)+v['url'] for v in d['home']['ventures']]
 context={**d,'ventureUrl':venture_urls,'labels':LABELS[lang], 'status':[d['ui']['status']+': '+v['status'] for v in d['home']['ventures']], 'step':[v['title']+' '+v['text'] for v in d['thesis']['sections'][3]['steps']], 'memoTitle':[re.sub(r'^[IVX]+\.\s*','',v['title']) for v in d['memos']['sections']], 'contactIntro':' '.join(d['contact']['intro']), 'contactRoute':route('contact',lang)}
 def replace(m):
  value=context
  for key in m[1].split('.'):value=value[int(key)] if isinstance(value,list) else value[key]
  return escape(str(value),quote=True)
 template=re.sub(r'\{\{([\w.]+)\}\}',replace,template)
 for n in range(1,6):template=template.replace('__FIG_'+str(n)+'__',reference_figure(n,lang,dark=n in [2,3,4]))
 return template

def reference_header(d,lang,key):
 nav=''.join(f'<a href="{route("",lang)}#{slug}" class="reference-nav-link">{escape(label)}</a>' for slug,label in d['ui']['nav'].items())
 languages=''.join(f'<a href="{route(key,code)}" lang="{tag}" hreflang="{tag}" aria-label="{name}"'+(' aria-current="page"' if code==lang else '')+'>'+code.upper()+'</a>' for code,tag,name in [('en','en','English'),('pt','pt-PT','Português'),('es','es','Español')])
 return f'''<header class="reference-header"><div class="reference-header-row"><a class="reference-brand" href="{route('',lang)}"><span class="reference-wordmark">Castelein.</span></a><nav class="reference-desktop-nav" aria-label="{escape(d['ui']['menu'])}">{nav}</nav><nav class="language-nav reference-language-nav" aria-label="{escape(d['ui']['language'])}">{languages}</nav><details class="mobile-menu reference-menu"><summary aria-label="{escape(d['ui']['menu'])}"><span></span><span></span><span></span></summary><nav aria-label="{escape(d['ui']['menu'])}">{nav}</nav></details></div></header>'''

def reference_footer(d,lang):
 return f'''<footer class="reference-footer"><div class="reference-footer-row"><p>{escape(d['ui']['footer'])}</p><div><a href="https://www.skaler.pt/">Skaler.pt</a><a href="{route('privacy',lang)}">{escape(d['ui']['privacy'])}</a><span>{escape(d['ui']['copyright'])}</span></div></div></footer>'''
