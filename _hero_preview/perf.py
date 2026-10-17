import asyncio,json,statistics,sys
from playwright.async_api import async_playwright
INIT="""
window.__m={cls:0,lcp:0};
new PerformanceObserver(l=>{for(const e of l.getEntries()){if(!e.hadRecentInput)window.__m.cls+=e.value}}).observe({type:'layout-shift',buffered:true});
new PerformanceObserver(l=>{const e=l.getEntries();window.__m.lcp=e[e.length-1].startTime}).observe({type:'largest-contentful-paint',buffered:true});
(function poll(){const f=document.querySelector('#feat .fc'),g=document.querySelector('#grid article');
 if(f&&!window.__m.feat&&f.getBoundingClientRect().height>0)window.__m.feat=performance.now();
 if(g&&!window.__m.grid)window.__m.grid=performance.now();
 if(!(window.__m.feat&&window.__m.grid))requestAnimationFrame(poll)})();
"""
URLS={'live':'https://ui.incidental.site/','A':'https://uihub-hero-gallery.sinxu-xsy.workers.dev/','B':'https://uihub-hero-collage.sinxu-xsy.workers.dev/'}
async def run(b,url,vp,mob):
    c=await b.new_context(viewport=vp,is_mobile=mob,has_touch=mob)
    await c.add_init_script(INIT);pg=await c.new_page()
    await pg.goto(url,wait_until='load');await pg.wait_for_timeout(6000)
    m=await pg.evaluate('({...window.__m,fcp:(performance.getEntriesByName("first-contentful-paint")[0]||{}).startTime,load:performance.timing.loadEventEnd-performance.timing.navigationStart,bytes:performance.getEntriesByType("resource").reduce((a,e)=>a+(e.transferSize||0),0)+(performance.getEntriesByType("navigation")[0].transferSize||0)})')
    await c.close();return m
async def main():
    out={}
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for dev,vp,mob in [('desktop',{'width':1440,'height':900},False),('mobile',{'width':390,'height':844},True)]:
            for k,u in URLS.items():
                rs=[]
                for i in range(3):
                    rs.append(await run(b,u+'?lang=en',vp,mob))
                med=lambda f: round(statistics.median([r.get(f) or 0 for r in rs]),3 if f=='cls' else 0)
                out[f'{dev}-{k}']={f:med(f) for f in ('feat','grid','fcp','lcp','cls','load','bytes')}
                out[f'{dev}-{k}']['cls_max']=round(max(r['cls'] for r in rs),3)
                print(dev,k,out[f'{dev}-{k}'],flush=True)
        await b.close()
    json.dump(out,open('/workspace/reports/uihub-hero-1017/perf.json','w'),indent=1)
asyncio.run(main())
