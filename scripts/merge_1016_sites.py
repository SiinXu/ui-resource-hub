"""Data-only append: full-website / page-level UI references (2026-10-16 batch 2).
Appends to data.json + data.js + media.js only. No UI files, no new tag values (tags=[]),
types/styles/ct mapped onto existing values. Style 'look' / gold are invisible metadata."""
import json, os, re, sys, shutil, datetime, collections
from urllib.parse import urlparse
from PIL import Image, ImageStat
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); P=lambda *a: os.path.join(ROOT,*a)
SRC=sys.argv[1]  # final list json
TODAY='2026-10-16'
VS_OK={'minimal','enterprise','material','soft','motion','playful','dark-tech','gradient','utilitarian','3d','editorial','apple','swiss','skeuomorphic','glass','retro','brutalist','fluent','industrial','neumorphism'}
def jsload(f):
    s=open(P(f),encoding='utf-8').read(); m=re.match(r'\s*(window\.\w+)\s*=\s*',s); return m.group(1), json.loads(s[m.end():].rstrip().rstrip(';'))
D=json.load(open(P('data.json'),encoding='utf-8')); items=D['items']; before=len(items)
mv,MD=jsload('media.js')
H=lambda u:urlparse(u).netloc.lower().replace('www.','')
have_h={H(i['url']) for i in items}; have_id={i['id'] for i in items}
GENERIC={'home','homepage','index','about','my framer site','welcome','','portfolio'}
def clean_name(r):
    for t in [r.get('og') or '', r.get('title') or '']:
        t=re.sub(r'\s+',' ',t).strip()
        parts=[p.strip() for p in re.split(r'\s+[|–—·:\-]\s+|\s*\|\s*',t) if p.strip()]
        for p in parts:
            if p.lower() not in GENERIC and len(p)>=2: return p[:60]
    h=H(r['url']).split('.')[0]; return h[:1].upper()+h[1:]
new=[]; skipped=[]
for r in json.load(open(SRC,encoding='utf-8')):
    h=H(r['url'])
    if h in have_h: skipped.append((r['url'],'dup host')); continue
    cid='w16-'+re.sub(r'[^a-z0-9]+','-',(h+urlparse(r['url']).path).lower()).strip('-')[:60]
    if cid in have_id: skipped.append((r['url'],'dup id')); continue
    vs=[v for v in r['vs'] if v in VS_OK] or ['minimal']
    tpl=r['source']=='Framer Marketplace'
    price=r.get('price','')
    src_note={'X':None}.get(r['source'],r['source'])
    note=r['note']
    if r['source']=='X':
        note+=f"（X 来源：@{r['x_handle']}，{r['x_likes']} 赞 / {r['x_bm']} 收藏，{r['x_date']}）"
    else:
        note+=f"（收录自 {r['source']}）"
    it=dict(id=cid,name=clean_name(r),url=r['url'],note=note,type='template' if tpl else 'inspiration',
            section='整站灵感 · 2026-10-16',sectionTitle='整站灵感（2026-10-16）',sectionDesc='',source=r['source'],
            pricing=('paid' if price.startswith('$') else 'unknown') if tpl else 'free',
            tags=[],ct=['layout'],rt=['template'] if tpl else ['inspiration'],vs=vs,added=TODAY)
    if r.get('via'): it['via']=r['via']
    if r.get('look'): it['look']=r['look']
    if r['look'] in ('画廊线描','黑白拼贴'): it['gold']=True; it['why']=r['look']+'的代表样本'
    if r['source']=='X':
        it['xsrc']={'post':r['via'],'author':'@'+r['x_handle'],'likes':r['x_likes'],'bookmarks':r['x_bm'],'reposts':r['x_rt'],'impressions':r['x_views'],'date':r['x_date']}
    img=f'previews/site/{cid}.webp'
    shutil.copyfile(os.path.join('/workspace/harvest',r['img']),P(img))
    tone='l' if ImageStat.Stat(Image.open(P(img)).convert('L')).mean[0]>128 else 'd'
    MD[cid]={'img':img,'src':'shot','tone':tone}
    items.append(it); have_h.add(h); have_id.add(cid); new.append(it)
D['count']=len(items); D['generated']=TODAY; D['updatedAt']=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%MZ')
json.dump(D,open(P('data.json'),'w',encoding='utf-8'),ensure_ascii=False,indent=1)
open(P('data.js'),'w',encoding='utf-8').write('window.UI_DATA='+json.dumps(D,ensure_ascii=False)+';\n')
open(P('media.js'),'w',encoding='utf-8').write(mv+'='+json.dumps(MD,ensure_ascii=False)+';\n')
rep={'before':before,'after':len(items),'new':len(new),'by_source':collections.Counter(i['source'] for i in new),
     'look':collections.Counter(i.get('look','') for i in new),'x':sum(1 for i in new if i['source']=='X'),'skipped':skipped}
json.dump(rep,open('/workspace/harvest/merge_sites_result.json','w'),ensure_ascii=False,indent=1)
print(json.dumps(rep,ensure_ascii=False))

# perf: regenerate split/ first-screen + lazy data files and the index.html hash map from the canonical data (deterministic)
import subprocess as _sp2, sys as _sys2
_sp2.run([_sys2.executable, __import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), 'split_data.py')], check=True)
