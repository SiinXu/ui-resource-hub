import asyncio,sys
from playwright.async_api import async_playwright
INIT="""window.__ls=[];new PerformanceObserver(l=>{for(const e of l.getEntries()){if(e.hadRecentInput)continue;window.__ls.push({v:+e.value.toFixed(4),t:Math.round(e.startTime),src:(e.sources||[]).map(s=>{const n=s.node;return (n&&n.nodeType===1?(n.tagName+'#'+n.id+'.'+String(n.className).slice(0,40)):String(n&&n.nodeName))+' '+JSON.stringify([Math.round(s.previousRect.y),Math.round(s.currentRect.y),Math.round(s.previousRect.height),Math.round(s.currentRect.height)])})})}}).observe({type:'layout-shift',buffered:true});"""
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for u in sys.argv[1:]:
            c=await b.new_context(viewport={'width':1440,'height':900});await c.add_init_script(INIT);pg=await c.new_page()
            await pg.goto(u,wait_until='load');await pg.wait_for_timeout(5000)
            print(u);[print('  ',x) for x in await pg.evaluate('window.__ls')]
            await c.close()
        await b.close()
asyncio.run(main())
