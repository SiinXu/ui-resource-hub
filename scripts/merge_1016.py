"""Merge the 2026-10-16 curated expansion into data.json / media.js / legal.js / orig.js, set gold tier and quality flags."""
import json, os, re, sys, datetime, html, urllib.request
sys.path.insert(0, os.path.dirname(__file__))
from expand_spec_1016 import *
from hub_lib import norm
import numpy as np
from PIL import Image
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=lambda *a: os.path.join(ROOT,*a)
TODAY='2026-10-16'
def jsload(f):
    s=open(P(f),encoding='utf-8').read(); m=re.match(r'\s*(window\.\w+)\s*=\s*',s); return m.group(1), json.loads(s[m.end():].rstrip().rstrip(';'))
def jssave(f,var,obj): open(P(f),'w',encoding='utf-8').write(var+'='+json.dumps(obj,ensure_ascii=False)+';\n')
D=json.load(open(P('data.json'),encoding='utf-8')); items=D['items']; before=len(items)
mv,MD=jsload('media.js'); lv,LG=jsload('legal.js'); ov,OG=jsload('orig.js')
cap=json.load(open(P('_cap1016.json'))) if os.path.exists(P('_cap1016.json')) else {}
xp={p['id']:p for p in json.load(open('/workspace/reports/ui-hub-audit/tmp/xposts.json'))}
REJECT=set(json.load(open(P('_reject1016.json')))) if os.path.exists(P('_reject1016.json')) else set()
EXTRA=json.load(open(P('_extra1016.json'),encoding='utf-8')) if os.path.exists(P('_extra1016.json')) else []
def content(path):
    a=np.asarray(Image.open(path).convert('RGB').resize((160,100))).astype(int)
    b=np.concatenate([a[0],a[-1],a[:,0],a[:,-1]]); v,c=np.unique(b,axis=0,return_counts=True); bg=v[c.argmax()]
    return float((np.abs(a-bg).sum(axis=2)>40).mean())
def meta_desc(url):
    r=cap.get(cid_of.get(url,''),{})
    if r.get('desc'): return r['desc']
    try:
        h=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=15).read(300000).decode('utf-8','replace')
        m=re.search(r'<meta[^>]+(?:name="description"|property="og:description")[^>]+content="([^"]*)"',h) or re.search(r'<meta[^>]+content="([^"]*)"[^>]+(?:name="description"|property="og:description")',h)
        return html.unescape(m.group(1))[:300] if m else ''
    except Exception: return ''
cid_of={}
have_u={norm(i['url']) for i in items}; have_id={i['id'] for i in items}
new=[]; skipped=[]
def add(it, img, legal=None, orig_code=None):
    if it['id'] in REJECT: skipped.append((it['id'],'visual-review reject')); return
    if norm(it['url']) in have_u or it['id'] in have_id: skipped.append((it['id'],'duplicate url')); return
    if not img or not os.path.exists(P(img)): skipped.append((it['id'],'no preview')); return
    c=content(P(img))
    if c<0.02: skipped.append((it['id'],'blank preview %.3f'%c)); return
    st=cap.get(it['id'],{}).get('status')
    if st and st>=400 and st not in (403,): skipped.append((it['id'],'http %s'%st)); return
    it.setdefault('added',TODAY); it['cur']=1
    items.append(it); have_u.add(norm(it['url'])); have_id.add(it['id']); new.append(it)
    from PIL import ImageStat
    MD[it['id']]={'img':img,'src':'shot','tone':'l' if ImageStat.Stat(Image.open(P(img)).convert('L')).mean[0]>128 else 'd'}
    if legal: LG[it['id']]=legal
    d=meta_desc(it['url']); o={'ds':it['url']}
    if d: o['d']=d
    if orig_code: o['c']=orig_code; o['cs']=legal.get('gh','') if legal else ''
    if d or orig_code: OG[it['id']]=o
GOLDOFF=set(json.load(open(P('_goldoff1016.json')))) if os.path.exists(P('_goldoff1016.json')) else set()
def gold(it,why):
    if why and it['id'] not in GOLDOFF: it['gold']=True; it['why']=why
def style(cid,lib,libName,slug,title,kind,vs,note,why,url,source,legal=None,code=None,pricing='free'):
    cid_of[url]=cid
    it=dict(id=cid,type='style',lib=lib,libName=libName,kind=kind,var=title,name=f'{kind} · {libName} · {title}',url=url,page=url,note=note,
            section='精选扩充 · 2026-10-16',sectionTitle='精选扩充（2026-10-16）',sectionDesc='',source=source,pricing=pricing,
            tags=[libName],ct=[kind],rt=['component-demo'],vs=vs)
    gold(it,why); add(it,'previews/site/'+cid+'.webp',legal,code)
GH={'magicui-design':'https://github.com/magicuidesign/magicui','www-cult-ui-com':'https://github.com/nolly-studio/cult-ui','motion-primitives-com':'https://github.com/ibelick/motion-primitives','ui-shadcn-com':'https://github.com/shadcn-ui/ui'}
def mit(lib,cmd,url): return {'k':'oss','lic':'MIT','code':cmd,'gh':GH[lib]}, f'# ① 安装 Install — {url}\n{cmd}'
for s,t,k,vs,n,w in ACE:
    u='https://ui.aceternity.com/components/'+s
    style('x16-aceternity-'+s,'ui-aceternity-com','Aceternity UI',s,t,k,vs,n,w,u,'Aceternity UI',{'k':'lic','lic':'Aceternity UI 许可（免费组件，代码请从原站复制）'})
for s,t,k,vs,n,w in MAGIC:
    u='https://magicui.design/docs/components/'+s; lg,c=mit('magicui-design',f'npx shadcn@latest add "https://magicui.design/r/{s}.json"',u)
    style('x16-magicui-'+s,'magicui-design','Magic UI',s,t,k,vs,n,w,u,'Magic UI',lg,c)
for s,t,k,vs,n,w in CULT:
    u='https://www.cult-ui.com/docs/components/'+s; lg,c=mit('www-cult-ui-com',f'npx shadcn@latest add "https://www.cult-ui.com/r/{s}.json"',u)
    style('x16-cultui-'+s,'www-cult-ui-com','Cult UI',s,t,k,vs,n,w,u,'Cult UI',lg,c)
for s,t,k,vs,n,w in MP:
    u='https://motion-primitives.com/docs/'+s; lg,c=mit('motion-primitives-com',f'npx motion-primitives@latest add {s}',u)
    style('x16-motion-primitives-'+s,'motion-primitives-com','Motion Primitives',s,t,k,vs,n,w,u,'Motion Primitives',lg,c)
def simple(cid,name,url,typ,vs,ct,note,why,source,pricing='free',rt=None,extra=None,legal=None,code=None):
    cid_of[url]=cid
    it=dict(id=cid,name=name,url=url,note=note,type=typ,section='精选扩充 · 2026-10-16',sectionTitle='精选扩充（2026-10-16）',sectionDesc='',
            source=source,pricing=pricing,tags=[],ct=ct,rt=rt or {'inspiration':['inspiration'],'template':['template'],'tool':['tool'],'skill':['skill'],'tutorial':['tutorial'],'system':['design-system'],'library':['component-library'],'component':['component-library']}.get(typ,['tool']),vs=vs)
    if extra: it.update(extra)
    gold(it,why); add(it,'previews/site/'+cid+'.webp',legal,code)
for s,t,n,w in ACE_BLOCKS: simple('x16-aceternity-blocks-'+s,t,'https://ui.aceternity.com/blocks/'+s,'template',['dark-tech','motion'],['layout'],n,w,'Aceternity UI','freemium')
for s,t,n,w in ACE_TPL: simple('x16-aceternity-tpl-'+s,t,'https://ui.aceternity.com/templates/'+s,'template',['dark-tech','minimal'],['layout'],n,w,'Aceternity UI','paid')
for s,t,k,n,w in SHADCN:
    u='https://ui.shadcn.com/view/new-york-v4/'+s; lg,c=mit('ui-shadcn-com',f'npx shadcn@latest add {s}',u)
    simple('x16-shadcn-'+s,t,u,'template',['minimal','enterprise'],[k],n,w,'shadcn/ui','free',legal=lg,code=c)
for i,n,u,typ,vs,note,w in INSP: simple('x16-'+i,n,u,typ,vs,[],note,w,host:=re.sub(r'^https?://(www\.)?','',u).split('/')[0],'freemium' if typ=='tool' else 'free',rt=['mcp','tool'] if 'mcp' in i else None)
for i,n,u,vs,note,w in BENCH: simple('x16-'+i,n,u,'inspiration',vs,['layout'],note,w,'标杆站点',rt=['inspiration'])
for r in X:
    cid,name,url,typ,vs,ct,note,why,pid,author=r
    p=xp.get(pid,{})
    ex={'xsrc':{'post':f'https://x.com/{author}/status/{pid}','author':'@'+author,'likes':p.get('likes'),'bookmarks':p.get('bm'),'reposts':p.get('rt'),'impressions':p.get('imp'),'date':p.get('date')}}
    simple(cid,name,url,typ,vs,ct,note+f'（X 来源：@{author}，{p.get("likes","?")} 赞 / {p.get("bm","?")} 收藏，{p.get("date","")}）',why,'X',extra=ex)
for e in EXTRA:  # visually-approved Awwwards SOTD / Framer templates
    simple(e['id'],e['name'],e['url'],'inspiration',e['vs'],['layout'],e['note'],e.get('why'),e['source'],e.get('pricing','free'),rt=['inspiration'])
# ---- gold for existing items ----
OLD_GOLD={
 'shaders-paper-design-liquid-metal':'着色器做主视觉的高级样本：单一材质、光感细腻',
 'canvasui-dev':'雾面玻璃 + 颗粒 + 大数字，安静但有氛围',
 'backgrounds-supply':'无衬线 + 衬线斜体混排、只一块粉色，克制的配色范本',
 'www-shadergradient-co':'颗粒暖渐变 + 细衬线，电影感单色场',
 'lib-gsap-com':'字体主导的品牌页：近黑 + 骨白 + 一个荧光绿',
 'lib-lenis-darkroom-engineering':'海报式哥特字标题，极具记忆点的排版',
 'lib-motion-dev':'整块高饱和黄 + 黑色等宽字，瑞士海报的能量',
 'skiper-ui-com':'超大压缩无衬线标题，大胆而留白',
 'ui-lukacho-com':'超大黑色无衬线 + 一条虹彩丝带，“一处惊艳”的典型',
 'cs2-reactbits-dev--background--backgrounds-threads--v0':'黑底白色细线流场，优雅的单色动态背景',
 'cs2-reactbits-dev--background--backgrounds-liquid-chrome--v0':'单色液态金属流动，戏剧性强',
 'cs2-reactbits-dev--layout--components-masonry--v0':'黑白纪实照片瀑布流，编辑感',
 'ued-design-spells':'纸感底 + 优雅衬线标题，策展式陈列',
 'ued-utopia-fyi':'藏蓝 + 奶白，清晰的编辑字号阶梯',
 'lib-component-gallery':'大衬线标题 + 纸感，信息型站点也能有品味',
 'ued-practical-typography':'经典书籍排版，正文可读性的标准',
 'ui-shadcn-com':'所有现代 React 组件的底座，中性、可定制',
 'transitions-dev':'页面过渡的高质量合集',
}
for i in items:
    if i['id'] in OLD_GOLD: i['gold']=True; i['why']=OLD_GOLD[i['id']]
# ---- quality flags on existing items ----
flags={}
lc=[l.split(' ',1) for l in open('/workspace/reports/ui-hub-audit/tmp/linkcheck.txt').read().split('\n')+open('/workspace/reports/ui-hub-audit/tmp/linkcheck2.txt').read().split('\n') if ' ' in l]
dead={norm(u) for c,u in lc if c in ('404','410') and 'naiveui.com' not in u}   # Naive UI is an SPA: HTTP 404 but renders fine in a browser
pruned=[]
keep=[]
for i in items:
    if not i.get('cur') and norm(i.get('page') or i['url']) in dead and norm(i['url']) in dead: pruned.append(i['id']); flags.setdefault(i['id'],[]).append('dead-link')
    keep.append(i)
items[:]=keep
import hashlib, collections
groups=collections.defaultdict(list)
for i in items:
    m=MD.get(i['id'],{})
    if i.get('cur') or not m.get('img') or not os.path.exists(P(m['img'])): continue
    groups[m['img']].append(i['id'])
    if i['type']=='style' and content(P(m['img']))<0.01: flags.setdefault(i['id'],[]).append('blank-preview')
hgroups=collections.defaultdict(list)
for img,ids in groups.items():
    hgroups[hashlib.md5(open(P(img),'rb').read()).hexdigest()]+=ids
for h,ids in hgroups.items():
    if len(ids)>1:
        for x in ids[1:]: flags.setdefault(x,[]).append('dup-preview')
for i in items:
    if i['id'] in flags: i['flag']=sorted(set(flags[i['id']]))
    elif 'flag' in i and not i.get('cur'): del i['flag']
D['count']=len(items); D['generated']=TODAY; D['updatedAt']=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%MZ')
json.dump(D,open(P('data.json'),'w',encoding='utf-8'),ensure_ascii=False,indent=1)
open(P('data.js'),'w',encoding='utf-8').write('window.UI_DATA='+json.dumps(D,ensure_ascii=False)+';\n')
fixed=0
byid={i['id']:i for i in items}
for k,o in OG.items():
    it=byid.get(k)
    if it and 'magicui.design/docs/components/' in (it.get('page') or it['url']) and o.get('c') and 'r/marquee.json' in o['c']:
        slug=(it.get('page') or it['url']).split('/docs/components/')[1].split('#')[0].split('?')[0]
        if slug and slug!='marquee': o['c']=o['c'].replace('r/marquee.json','r/%s.json'%slug); fixed+=1
print('magicui install fixed',fixed)
jssave('media.js',mv,MD); jssave('legal.js',lv,LG); jssave('orig.js',ov,OG)
src=collections.Counter(i['source'] for i in new)
rep={'before':before,'after':len(items),'new':len(new),'new_by_source':dict(src),'gold':sum(1 for i in items if i.get('gold')),
     'pruned':pruned,'flagged':collections.Counter(f for v in flags.values() for f in set(v)),'flagged_items':len(flags),'magicui_install_fixed':fixed,'skipped':skipped}
json.dump(rep,open('/workspace/reports/ui-hub-audit/merge-result.json','w'),ensure_ascii=False,indent=1,default=dict)
print(json.dumps({k:v for k,v in rep.items() if k!='skipped'},ensure_ascii=False,default=dict)); print('skipped',len(skipped),skipped[:40])

# perf: regenerate split/ first-screen + lazy data files and the index.html hash map from the canonical data (deterministic)
import subprocess as _sp2, sys as _sys2
_sp2.run([_sys2.executable, __import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), 'split_data.py')], check=True)
