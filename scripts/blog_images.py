#!/usr/bin/env python3
"""Captures real screenshots of sites discussed in each post + renders diagrams/covers (HTML->PNG->WebP). Run on a box with Chrome."""
import os, sys, io, json, html
from PIL import Image
from playwright.sync_api import sync_playwright
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); OUT=os.path.join(ROOT,'blog','img')
sys.path.insert(0,os.path.join(ROOT,'blog_src')); from images import IMAGES
from posts import POSTS
T={p['slug']:p for p in POSTS}
E=html.escape
def save(png, name, w):
    im=Image.open(io.BytesIO(png)).convert('RGB')
    if im.width>w: im=im.resize((w,round(im.height*w/im.width)),Image.LANCZOS)
    im.save(os.path.join(OUT,name+'.webp'),'WEBP',quality=80,method=6)
    if name.endswith('-cover'): im.save(os.path.join(OUT,name+'.jpg'),quality=82,optimize=True)  # og:image (webp poorly supported by some crawlers)
BASECSS="""*{box-sizing:border-box;margin:0}body{width:1200px;height:%dpx;background:#07080d;color:#eef1f8;font-family:Geist,'Noto Sans CJK SC',system-ui,sans-serif;overflow:hidden;position:relative}
body:before{content:"";position:absolute;inset:0;background:radial-gradient(45%% 60%% at 12%% 0%%,rgba(56,189,248,.28),transparent 70%%),radial-gradient(40%% 55%% at 92%% 10%%,rgba(129,140,248,.26),transparent 70%%),radial-gradient(35%% 45%% at 70%% 110%%,rgba(244,114,182,.16),transparent 70%%)}
body:after{content:"";position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.07) 1px,transparent 1px);background-size:22px 22px;mask:linear-gradient(#000,transparent 85%%)}
.w{position:relative;z-index:1;padding:56px 64px;height:100%%;display:flex;flex-direction:column}
.eb{font:500 15px ui-monospace,monospace;letter-spacing:.12em;text-transform:uppercase;color:#8b93a7}.eb b{color:#67e8f9;font-weight:500}
h1{font:400 64px/1.04 'Instrument Serif',Georgia,serif;letter-spacing:-.02em;margin-top:18px;max-width:900px}
h1 em{font-style:italic;background:linear-gradient(100deg,#67e8f9,#a5b4fc,#f9a8d4);-webkit-background-clip:text;color:transparent}
.box{border:1px solid rgba(255,255,255,.12);background:rgba(16,19,27,.82);border-radius:16px;padding:20px 22px}
.k{font:500 13px ui-monospace,monospace;color:#67e8f9;letter-spacing:.06em;text-transform:uppercase}.t{font-size:22px;font-weight:600;margin-top:6px}.d{font-size:16px;color:#a6adbf;margin-top:6px;line-height:1.45}
.row{display:flex;gap:16px;align-items:stretch}.row>*{flex:1}.ar{flex:0 0 28px!important;display:grid;place-items:center;color:#687086;font-size:26px}
.foot{margin-top:auto;display:flex;justify-content:space-between;font:500 14px ui-monospace,monospace;color:#687086}"""
def page(body,h): return f"<html><head><style>{BASECSS%h}</style></head><body><div class=w>{body}</div></body></html>"
def cover(slug,c):
    p=T[slug]; t=p['t']['en']; a,_,b=t.partition(':')
    motif=''.join(f'<div class=box style="flex:1"><div class=k>{E(k)}</div><div class=t>{E(v)}</div></div>' for k,v in c['chips'])
    return page(f"""<div class=eb><b>UI Hub</b> · Blog · AI design</div><h1>{E(a)}{':' if b else ''} <em>{E(b.strip())}</em></h1>
<div class=row style="margin-top:auto">{motif}</div><div class=foot style="margin-top:22px"><span>siinxu.github.io/ui-resource-hub</span><span>{E(' · '.join(p['tags']))}</span></div>""",630)
def diagram(d):
    if d['kind']=='flow':
        cells=[]
        for i,(k,t,ds) in enumerate(d['steps']):
            if i: cells.append('<div class=ar>→</div>')
            cells.append(f'<div class=box><div class=k>{E(k)}</div><div class=t>{E(t)}</div><div class=d>{E(ds)}</div></div>')
        body=f'<div class=row style="flex:1">{"".join(cells)}</div>'
    elif d['kind']=='stack':
        body='<div style="display:flex;flex-direction:column;gap:12px;flex:1">'+''.join(f'<div class=box style="flex:1;display:flex;align-items:center;gap:24px;margin-left:{i*36}px"><div class=k style="width:150px">{E(k)}</div><div><div class=t>{E(t)}</div><div class=d>{E(ds)}</div></div></div>' for i,(k,t,ds) in enumerate(d['steps']))+'</div>'
    elif d['kind']=='code':
        body='<div class=box style="flex:1;font:19px/1.75 ui-monospace,monospace">'+''.join(f'<div><span style="color:#67e8f9;display:inline-block;width:130px">{E(k)}</span><span style="color:#d6dbe7">{E(v)}</span></div>' for k,v in d['lines'])+'</div>'
    elif d['kind']=='curves':
        def path(f): return 'M0,200 '+' '.join(f'L{x*3},{200-200*f(x/100):.1f}' for x in range(101))
        cs=[('linear',lambda x:x,'#687086'),('ease-in',lambda x:x**2.4,'#f9a8d4'),('ease-out',lambda x:1-(1-x)**2.4,'#67e8f9')]
        svg=''.join(f'<div class=box style="flex:1"><div class=k style="color:{c}">{n}</div><svg viewBox="-10 -10 320 220" style="width:100%;height:230px;margin-top:10px"><path d="M0,200H300M0,0V200" stroke="#2a2f3d" fill="none"/><path d="{path(f)}" stroke="{c}" stroke-width="4" fill="none"/></svg><div class=d>{E(dd)}</div></div>' for (n,f,c),dd in zip(cs,d['notes']))
        body=f'<div class=row style="flex:1">{svg}</div>'
    elif d['kind']=='swatch':
        def col(name,bg,surf,ink,ink2,acc):
            return f'<div class=box style="flex:1;background:{bg};border-color:rgba(128,128,128,.25)"><div class=k style="color:{acc}">{name}</div><div style="background:{surf};border-radius:12px;padding:18px;margin-top:14px;box-shadow:0 0 0 1px rgba(128,128,128,.2)"><div style="color:{ink};font-size:22px;font-weight:600">Card title</div><div style="color:{ink2};font-size:16px;margin-top:6px">Secondary text at 4.5:1 or better</div><div style="display:inline-block;margin-top:14px;background:{acc};color:{bg};padding:8px 14px;border-radius:9px;font-weight:600">Action</div></div>'+''.join(f'<div style="display:flex;gap:10px;align-items:center;margin-top:10px;color:{ink2};font:14px ui-monospace,monospace"><span style="width:22px;height:22px;border-radius:6px;background:{v};box-shadow:0 0 0 1px rgba(128,128,128,.3)"></span>{k} {v}</div>' for k,v in [('--bg',bg),('--surface',surf),('--ink',ink),('--accent',acc)])+'</div>'
        body='<div class=row style="flex:1">'+col('light','#f5f6fa','#ffffff','#0a0c14','#4a5164','#2563eb')+col('dark','#06070b','#141822','#f3f5fb','#a6adbf','#67e8f9')+'</div>'
    elif d['kind']=='checks':
        body='<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;flex:1">'+''.join(f'<div class=box><div class=k>{E(k)}</div><div class=t>{E(t)}</div><div class=d>{E(ds)}</div></div>' for k,t,ds in d['steps'])+'</div>'
    return page(f'<div class=eb><b>Diagram</b> · {E(d["title"])}</div><div style="height:26px"></div>{body}<div class=foot style="margin-top:20px"><span>UI Hub</span><span>CC BY 4.0</span></div>',675)
if __name__=='__main__':
    only=sys.argv[1:]
    with sync_playwright() as p:
        b=p.chromium.launch(executable_path='/usr/bin/google-chrome')
        ctx=b.new_context(viewport=dict(width=1200,height=675),device_scale_factor=1)
        for slug,spec in IMAGES.items():
            if only and slug not in only and not any(o.startswith(slug+'-') for o in only): continue  # argv = slugs or image names; skip everything else
            pg=ctx.new_page(); pg.set_viewport_size(dict(width=1200,height=630)); pg.set_content(cover(slug,spec['cover'])); pg.wait_for_timeout(200)
            save(pg.screenshot(),f'{slug}-cover',1200); pg.close()
            for n,im in enumerate(spec['inline']):
                name=f'{slug}-{n+1}'
                if only and slug not in only and name not in only: continue
                pg=ctx.new_page()
                try:
                    if im['type']=='shot':
                        pg.set_viewport_size(dict(width=1280,height=800)); pg.goto(im['url'],wait_until='domcontentloaded',timeout=45000); pg.wait_for_timeout(3500)
                        for sel in im.get('dismiss',[]):
                            try: pg.click(sel,timeout=1500)
                            except Exception: pass
                        if im.get('scroll'): pg.mouse.wheel(0,im['scroll']); pg.wait_for_timeout(1200)
                        save(pg.screenshot(),name,1280)
                    else:
                        pg.set_content(diagram(im)); pg.wait_for_timeout(200); save(pg.screenshot(),name,1200)
                    print('ok',name)
                except Exception as e: print('FAIL',name,e)
                pg.close()
