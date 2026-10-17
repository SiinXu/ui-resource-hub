"""Build preview index.html for A (gallery) / B (collage) from the main index.html. Usage: build.py a|b"""
import json, re, sys, html as H
key = sys.argv[1]
ROOT = f'/workspace/uihub-hero/{key}'
base = open('/workspace/ui-hub-pages/index.html', encoding='utf-8').read()  # main @ 4f0dcd2
wall = json.load(open('/workspace/uihub-hero/wall.json'))[key]
css = open(f'/workspace/uihub-hero/src/{key}.css', encoding='utf-8').read()
css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
css = re.sub(r'\s*\n\s*', '', css)
h = base
# 1) preview-only head tweaks
h = h.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n<meta name="robots" content="noindex,nofollow">', 1)
h = h.replace('data-site="ui-hub" data-goal="copy"', 'data-site="ui-hub-preview" data-goal="copy"', 1)
import sys as _s; _s.path.insert(0,'/workspace/uihub-hero/src'); from decolor import decolor, audit
WH, WS = (35, 0.06) if key == 'a' else (0, 0.0)
import decolor as _d; _d.FAV = 'd95151' if key == 'a' else 'f2f2f2'
tok = open(f'/workspace/uihub-hero/src/tokens-{key}.css', encoding='utf-8').read()
st = decolor(open('/workspace/ui-hub-pages/styles.css', encoding='utf-8').read(), WH, WS) + '\n' + tok
open(f'{ROOT}/styles.hx.css', 'w', encoding='utf-8').write(st)
h = h.replace('<link rel="stylesheet" href="styles.css?v=15">', '<link rel="stylesheet" href="styles.hx.css?v=2">\n<style id="hx-css">' + css + '</style>', 1)
# 2) cut existing hero + chipsBar
m = re.search(r'    <div class="hero wrap" id="hero" data-n="(\d+)">(.*?)\n    </div>\n', h, re.S)
hero_inner, n = m.group(2), m.group(1)
cb = re.search(r'    <div class="filters wrap" id="chipsBar">.*?</div></div>\n', h, re.S)
# the chipsBar div ends with '</p></div>' — find exact
cbm = re.search(r'<div class="filters wrap" id="chipsBar">.*?<p class="fnote"[^>]*>[^<]*</p></div>', h, re.S)
chips = cbm.group(0).replace('class="filters wrap"', 'class="filters"')
h = h.replace(cbm.group(0) + '\n', '', 1) if (cbm.group(0) + '\n') in h else h.replace(cbm.group(0), '', 1)
ILL = ('<div class="hx-ill hx-i1" aria-hidden="true"><svg viewBox="0 0 120 120"><circle class="f" cx="70" cy="64" r="44"/><circle class="s" cx="62" cy="58" r="44"/><circle class="s" cx="62" cy="46" r="13"/><path class="s n" d="M36 86c6-16 46-16 52 0"/></svg></div>'
       '<div class="hx-ill hx-i2" aria-hidden="true"><svg viewBox="0 0 150 100"><path class="f" transform="translate(6 6)" d="M14 10h120a8 8 0 0 1 8 8v44a8 8 0 0 1-8 8H74l-14 16-4-16H14a8 8 0 0 1-8-8V18a8 8 0 0 1 8-8z"/><path class="s" d="M14 10h120a8 8 0 0 1 8 8v44a8 8 0 0 1-8 8H74l-14 16-4-16H14a8 8 0 0 1-8-8V18a8 8 0 0 1 8-8z"/><path class="s n" d="M26 40c8-10 14 10 22 0s14 10 22 0 14 10 22 0 14 10 22 0"/></svg></div>'
       '<div class="hx-ill hx-i3" aria-hidden="true"><svg viewBox="0 0 120 150"><rect class="f" x="16" y="14" width="96" height="132" rx="10"/><rect class="s" x="8" y="6" width="96" height="132" rx="10"/><path class="s" d="M8 70h96"/><circle class="s" cx="70" cy="30" r="9" style="fill:var(--fi)"/><path class="s" d="M20 62l22-24 18 18 12-10 24 16" style="fill:var(--fi)"/><path class="s n" d="M22 94c6-6 10 6 16 0s10 6 16 0 10 6 16 0 10 6 16 0M22 112c6-6 10 6 16 0s10 6 16 0 10 6 16 0"/></svg></div>')
def esc(s): return H.escape(s, quote=True)
if key == 'a':
    tiles = ''.join(
        f'<a class="hx-p" href="#/r/{esc(t["id"])}" data-cap="{esc(t["name"])}" aria-label="{esc(t["name"])}"><span class="fr"><img src="{t["src"]}" alt="" width="{t["w"]}" height="{t["h"]}" decoding="async" '
        + ('fetchpriority="low"' if k < 4 else 'loading="lazy"') + f'></span><span class="lb">No.{k+1:02d}<b>{esc(t["name"])}</b></span></a>'
        for k, t in enumerate(wall))
    wall_html = f'<div class="hx-wall">{tiles}</div><div class="hx-tip" id="hxTip" aria-hidden="true"></div>'
    main = f'<div class="hx-main">{ILL}<div class="hero" id="hero" data-n="{n}">{hero_inner}\n    </div>{wall_html}</div>'
else:
    AR = ['4/5', '16/10', '1/1', '3/4', '16/11', '4/5', '16/10', '3/4', '1/1', '16/10', '4/5', '16/11']
    cols = [[], [], []]
    order = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    # mobile shows cols 1-2 → put the 6 strongest there first
    for k, t in enumerate(wall):
        cols[k % 3].append((k, t))
    def tile(k, t):
        return (f'<a class="hx-t" href="#/r/{esc(t["id"])}" style="aspect-ratio:{AR[k]};--d:{0.05*k:.2f}s" aria-label="{esc(t["name"])}"><img src="{t["src"]}" alt="" width="{t["w"]}" height="{t["h"]}" decoding="async" '
                + ('fetchpriority="low"' if k < 6 else 'loading="lazy"') + f'><span class="cp"><small>{esc(t["type"])}</small><b>{esc(t["name"])}</b></span></a>')
    wall_html = '<div class="hx-wall">' + ''.join('<div class="hx-col">' + ''.join(tile(k, t) for k, t in c) + '</div>' for c in cols) + '</div>'
    main = f'<div class="hx-main"><div class="hero" id="hero" data-n="{n}">{hero_inner}\n    </div>{wall_html}</div>'
rail = f'<aside class="hx-rail" id="hxRail">{chips}<button class="hx-go" id="hxGo" type="button"></button></aside>'
section = f'    <section class="hx hx-{key}" id="hx"><div class="hx-in">{rail}{main}</div></section>\n'
h = h.replace(m.group(0), section, 1)
JS = open('/workspace/uihub-hero/src/hx.js', encoding='utf-8').read()
h = h.replace('<div class="toast" id="toast"></div>', '<div class="toast" id="toast"></div>\n<script>' + JS + '</script>', 1)
h = decolor(h, WH, WS).replace('<meta name="theme-color" content="#06070b">', '<meta name="theme-color" content="' + ('#292827' if key=='a' else '#0b0b0b') + '">')
open(f'{ROOT}/index.html', 'w', encoding='utf-8').write(h)
print('audit index', audit(h), 'audit css', audit(st))
print(key, 'index.html', len(h), 'bytes; css', len(css), 'js', len(JS))
