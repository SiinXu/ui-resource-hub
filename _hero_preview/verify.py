import asyncio,re,json
from playwright.async_api import async_playwright
U={'A':'https://uihub-hero-gallery.sinxu-xsy.workers.dev/','B':'https://uihub-hero-collage.sinxu-xsy.workers.dev/'}
HAN=re.compile(r'[\u3400-\u9fff\uf900-\ufaff]')
ALLOW={'简体中文','繁體中文','日本語'}
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); res={}
        for k,u in U.items():
            # Han check all non-zh locales
            for L in ['en','ja','ko','ms','vi','fr','es','de']:
                c=await b.new_context(viewport={'width':1440,'height':900});pg=await c.new_page()
                await pg.goto(u+'?lang='+L,wait_until='load');await pg.wait_for_timeout(4500)
                txt=await pg.evaluate('''()=>{const o=[document.body.innerText];document.querySelectorAll('[alt],[aria-label],[title],[placeholder],[data-cap]').forEach(e=>['alt','aria-label','title','placeholder','data-cap'].forEach(a=>{const v=e.getAttribute(a);if(v)o.push(v)}));o.push(document.title);return o.join('\\n')}''')
                for a in ALLOW: txt=txt.replace(a,'')
                if L=='ja':
                    # Japanese legitimately uses kanji; only check hero wall captions + rail for Chinese-only strings is out of scope
                    res[f'{k}-{L}']='skipped (kanji are Japanese)';await c.close();continue
                hits=sorted(set(HAN.findall(txt)))
                res[f'{k}-{L}']=len(hits) and ''.join(hits[:40]) or 0
                await c.close()
            # interaction: click wall tile body (desktop + mobile), modal opens, Esc closes; rail chip filters grid
            for dev,vp,mob in [('desktop',{'width':1440,'height':900},False),('mobile',{'width':390,'height':844},True)]:
                c=await b.new_context(viewport=vp,is_mobile=mob,has_touch=mob);pg=await c.new_page();errs=[]
                pg.on('pageerror',lambda e: errs.append(str(e)))
                await pg.goto(u+'?lang=en',wait_until='load');await pg.wait_for_timeout(4000)
                sel='.hx-p' if k=='A' else '.hx-t'
                t=pg.locator(sel).first;await t.scroll_into_view_if_needed()
                box=await t.bounding_box()
                await (pg.touchscreen.tap(box['x']+box['width']/2,box['y']+box['height']*0.6) if mob else pg.mouse.click(box['x']+box['width']/2,box['y']+box['height']*0.6))
                await pg.wait_for_timeout(1200)
                st=await pg.evaluate('({hash:location.hash,open:document.getElementById("sheet").classList.contains("open"),w:Math.round(document.getElementById("sheet").getBoundingClientRect().width),title:(document.querySelector("#sheet h2,#sheet h1")||{}).textContent})')
                await pg.screenshot(path=f'/workspace/reports/uihub-hero-1017/{k.lower()}-modal-{dev}.png')
                if not mob: await pg.keyboard.press('Escape')
                else: await pg.go_back()
                await pg.wait_for_timeout(600)
                closed=await pg.evaluate('!document.getElementById("sheet").classList.contains("open")')
                # filter chip in rail
                before=await pg.evaluate('document.getElementById("meta").textContent')
                chip=pg.locator('#hxRail #chips .chip[data-rt]:not([data-rt=""])').first
                await chip.scroll_into_view_if_needed(); await chip.click(); await pg.wait_for_timeout(500)
                after=await pg.evaluate('document.getElementById("meta").textContent')
                go=await pg.evaluate('document.getElementById("hxGo").textContent')
                tap=await pg.evaluate('''()=>[...document.querySelectorAll('#hx a,#hx button')].filter(e=>{const r=e.getBoundingClientRect();return r.width>0&&r.height>0&&r.height<28}).length''')
                ov=await pg.evaluate('document.documentElement.scrollWidth-innerWidth')
                res[f'{k}-{dev}-interact']=dict(tile=st,closed=closed,filter_before=before,filter_after=after,go=go,small_targets=tap,overflow=ov,errors=errs)
                await c.close()
        await b.close()
        print(json.dumps(res,ensure_ascii=False,indent=1))
        json.dump(res,open('/workspace/reports/uihub-hero-1017/verify.json','w'),ensure_ascii=False,indent=1)
asyncio.run(main())
