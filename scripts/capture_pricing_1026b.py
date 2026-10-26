"""Capture previews for the 2026-10-26 (b) pricing expansion -> previews/site/<id>.webp + _cap1026b.json. Same method as capture_1016 (1440x900 viewport -> 800x500 webp)."""
import asyncio, json, os, sys, io
from playwright.async_api import async_playwright
from PIL import Image
import numpy as np
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT=os.path.join(ROOT,'previews/site'); CJ=os.path.join(ROOT,'_cap1026b.json')
U={
'tailwind-plus':'https://tailwindcss.com/plus/ui-blocks/marketing/sections/pricing',
'bootstrap-example':'https://getbootstrap.com/docs/5.3/examples/pricing/',
'mdb':'https://mdbootstrap.com/docs/standard/extended/pricing/',
'tailwindcomponents':'https://tailwindcomponents.com/components/pricing',
'pricingpages-design':'https://www.pricingpages.design/',
'land-book':'https://land-book.com/?category=pricing',
'saaslandingpage':'https://saaslandingpage.com/pricing/',
'tailark':'https://tailark.com/pricing',
'magicui-pro':'https://pro.magicui.design/docs/sections/pricing',
'pagecollective':'https://www.pagecollective.com/pricing',
'saasframe':'https://www.saasframe.io/categories/pricing-page',
'landingfolio':'https://www.landingfolio.com/inspiration/section/pricing',
'webflow-made':'https://webflow.com/made-in-webflow/pricing',
'saasui':'https://www.saasui.design/pattern/pricing',
'lukacho':'https://ui.lukacho.com/components/pricing',
'freefrontend-css':'https://freefrontend.com/css-pricing-tables/',
'freefrontend-tw':'https://freefrontend.com/tailwind-pricing-tables/',
'markuptag':'https://www.markuptag.com/category/pricing-table/',
'wickedblocks':'https://wickedblocks.dev/groups/pricing',
'preline-examples':'https://preline.co/examples/pricing-sections.html',
'awwwards-pricing':'https://www.awwwards.com/websites/pricing/',
'tw-elements-comp':'https://tw-elements.com/docs/standard/components/pricing/',
}
for n in [1,3,4,5,6,7,8,9,10,11,12,13,14,15]: U['shadcnblocks-%d'%n]='https://www.shadcnblocks.com/block/pricing%d'%n
for p in ['Yaya12085/foolish-husky-65','Yaya12085/mean-vampirebat-50','Yaya12085/rotten-dolphin-86','Yaya12085/serious-eagle-83','Yaya12085/splendid-firefox-37','emmanuelh-dev/curvy-robin-66','emmanuelh-dev/orange-cougar-98','Cobp/old-cat-57','Cobp/popular-gecko-2','alexruix/loud-baboon-79','mi-series/splendid-eagle-61','seyed-mohsen-mousavi/swift-sloth-95','Admin12121/brown-bird-6','Li-Deheng/itchy-octopus-9']:
    U['uiverse-'+p.split('/')[1]]='https://uiverse.io/'+p
C=[('x1026b-pricing-'+k,v) for k,v in U.items()]
only=set(sys.argv[1:])
if only: C=[c for c in C if c[0] in only]
res=json.load(open(CJ)) if os.path.exists(CJ) else {}
def content(img):
    a=np.asarray(img.convert('RGB').resize((160,100))).astype(int)
    b=np.concatenate([a[0],a[-1],a[:,0],a[:,-1]]); v,c=np.unique(b,axis=0,return_counts=True); bg=v[c.argmax()]
    return float((np.abs(a-bg).sum(axis=2)>40).mean())
async def one(b,cid,url,sem):
    async with sem:
        rec={'url':url}
        for attempt in range(2):
            ctx=await b.new_context(viewport={'width':1440,'height':900},color_scheme='light',device_scale_factor=1,user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36')
            pg=await ctx.new_page()
            try:
                r=await pg.goto(url,wait_until='domcontentloaded',timeout=40000); rec['status']=r.status if r else 0
                try: await pg.wait_for_load_state('networkidle',timeout=12000)
                except Exception: pass
                await pg.wait_for_timeout(4000+attempt*3000)
                rec['title']=(await pg.title())[:160]
                rec['desc']=await pg.evaluate("()=>{const m=document.querySelector('meta[name=description],meta[property=\"og:description\"]');return m?m.content.slice(0,400):''}")
                rec['h']=await pg.evaluate("()=>[...document.querySelectorAll('h1,h2')].slice(0,4).map(e=>e.innerText.trim().slice(0,80)).join(' | ')")
                im=Image.open(io.BytesIO(await pg.screenshot())).convert('RGB').resize((800,500))
                rec['content']=round(content(im),4)
                if rec['content']>=0.03 or attempt==1:
                    im.save(os.path.join(OUT,cid+'.webp'),quality=82); await ctx.close(); break
            except Exception as e: rec['err']=str(e)[:160]
            await ctx.close()
        res[cid]=rec; print(cid,rec.get('status'),rec.get('content'),rec.get('title','')[:70],flush=True)
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); sem=asyncio.Semaphore(6)
        await asyncio.gather(*[one(b,*c,sem) for c in C]); await b.close()
    json.dump(res,open(CJ,'w'),ensure_ascii=False,indent=1)
asyncio.run(main())
