"""Capture real previews for the 2026-10-16 expansion. Writes previews/site/<id>.webp and _cap1016.json (status/title/desc/content)."""
import asyncio, json, os, sys, io
sys.path.insert(0, os.path.dirname(__file__))
from expand_spec_1016 import *
from playwright.async_api import async_playwright
from PIL import Image
import numpy as np
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT=os.path.join(ROOT,'previews/site'); CJ=os.path.join(ROOT,'_cap1016.json')
links=json.load(open('/workspace/reports/ui-hub-audit/tmp/links.json'))
C=[]  # (id,url,mode)
for s,*_ in ACE: C.append(('x16-aceternity-'+s,'https://ui.aceternity.com/components/'+s,'el'))
for s,*_ in ACE_BLOCKS: C.append(('x16-aceternity-blocks-'+s,'https://ui.aceternity.com/blocks/'+s,'page'))
for s,*_ in ACE_TPL: C.append(('x16-aceternity-tpl-'+s,'https://ui.aceternity.com/templates/'+s,'page'))
for s,*_ in MAGIC: C.append(('x16-magicui-'+s,'https://magicui.design/docs/components/'+s,'el'))
for s,*_ in CULT: C.append(('x16-cultui-'+s,'https://www.cult-ui.com/docs/components/'+s,'el'))
for s,*_ in MP: C.append(('x16-motion-primitives-'+s,'https://motion-primitives.com/docs/'+s,'el'))
for s,*_ in SHADCN: C.append(('x16-shadcn-'+s,'https://ui.shadcn.com/view/new-york-v4/'+s,'page'))
for i,n,u,*_ in INSP: C.append(('x16-'+i,u,'page'))
for i,n,u,*_ in BENCH: C.append(('x16-'+i,u,'page'))
for r in X: C.append((r[0],r[2],'page'))
for u in list(links['awwwards'])[:14]: C.append(('x16-awwwards-'+u.rstrip('/').split('/')[-1],u,'page'))
for u in list(links['framer'])[:14]: C.append(('x16-framer-'+u.rstrip('/').split('/')[-1],u,'page'))
only=set(sys.argv[1:])
if only: C=[c for c in C if c[0] in only]
import glob
done={os.path.basename(f)[:-5] for f in glob.glob(os.path.join(OUT,'x*.webp'))}
if not only: C=[c for c in C if c[0] not in done]
print('todo',len(C),flush=True)
res=json.load(open(CJ)) if os.path.exists(CJ) else {}
def content(img):
    a=np.asarray(img.convert('RGB').resize((160,100))).astype(int)
    b=np.concatenate([a[0],a[-1],a[:,0],a[:,-1]]); v,c=np.unique(b,axis=0,return_counts=True); bg=v[c.argmax()]
    return float((np.abs(a-bg).sum(axis=2)>40).mean())
JS_EL="""()=>{const c=[...document.querySelectorAll('[class*="preview" i],[data-preview],iframe')].filter(e=>{const r=e.getBoundingClientRect();return r.width>=480&&r.height>=260&&r.height<1400&&getComputedStyle(e).visibility!=='hidden'});
 c.sort((a,b)=>{const ra=a.getBoundingClientRect(),rb=b.getBoundingClientRect();return (ra.top+scrollY)-(rb.top+scrollY)});
 if(!c.length)return null;const e=c[0];e.setAttribute('data-cap16','1');return 1}"""
async def one(b,cid,url,mode,sem):
    async with sem:
      try:
        await asyncio.wait_for(_one(b,cid,url,mode),90)
      except Exception as e:
        res[cid]={'url':url,'err':'timeout '+str(e)[:80]}; print(cid,'TIMEOUT',flush=True)
      json.dump(res,open(CJ,'w'),ensure_ascii=False,indent=1)
async def _one(b,cid,url,mode):
    if True:
        for attempt in range(2):
            ctx=await b.new_context(viewport={'width':1440,'height':900},color_scheme='dark' if attempt==0 else 'light',device_scale_factor=1,user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36')
            pg=await ctx.new_page(); rec={'url':url}
            try:
                r=await pg.goto(url,wait_until='domcontentloaded',timeout=40000); rec['status']=r.status if r else 0
                try: await pg.wait_for_load_state('networkidle',timeout=12000)
                except Exception: pass
                await pg.wait_for_timeout(3500+attempt*3000)
                rec['title']=(await pg.title())[:140]
                rec['desc']=await pg.evaluate("()=>{const m=document.querySelector('meta[name=description],meta[property=\"og:description\"]');return m?m.content.slice(0,300):''}")
                png=None
                if mode=='el' and await pg.evaluate(JS_EL):
                    el=pg.locator('[data-cap16]').first; await el.scroll_into_view_if_needed(); await pg.wait_for_timeout(1500)
                    png=await el.screenshot(); rec['mode']='element'
                if png is None:
                    png=await pg.screenshot(); rec['mode']='viewport'
                im=Image.open(io.BytesIO(png)).convert('RGB')
                if rec['mode']=='viewport': im=im.resize((800,500))
                else:
                    im.thumbnail((800,800))
                rec['content']=round(content(im),4); rec['size']=im.size
                if rec['content']>=0.03 or attempt==1:
                    im.save(os.path.join(OUT,cid+'.webp'),quality=82); rec['img']='previews/site/'+cid+'.webp'
                    await ctx.close(); break
            except Exception as e:
                rec['err']=str(e)[:160]
            await ctx.close()
        res[cid]=rec; print(cid,rec.get('status'),rec.get('mode'),rec.get('content'),rec.get('err','')[:60],flush=True)
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); sem=asyncio.Semaphore(6)
        await asyncio.gather(*[one(b,*c,sem) for c in C])
        await b.close()
    json.dump(res,open(CJ,'w'),ensure_ascii=False,indent=1)
asyncio.run(main())
