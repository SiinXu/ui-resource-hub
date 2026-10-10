#!/usr/bin/env python3
"""v3e 封面规则：非组件样式卡的预览必须是「真实组件」或「产品真实工作界面」，不再用营销首图 / logo / og 封面 / 只有文档框架的截图。
优先级：1) 人工复核选中的真实界面截图（_covers/pick.json，来自 /workspace/cap/covers.py 或 README 里的产品截图）
        2) 同一个库在本站的组件样式卡（官方文档演示截图）
        3) 都没有 → 不放图，前端显示「自制示意」占位
在 build_styles.py 之后运行。"""
import json, os, shutil
from urllib.parse import urlparse
H = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(H, 'data.json'), encoding='utf-8'))
mt = open(os.path.join(H, 'media.js'), encoding='utf-8').read(); media = json.loads(mt[len('window.UI_MEDIA='):-2])
pick = json.load(open(os.path.join(H, '_covers', 'pick.json'), encoding='utf-8'))
os.makedirs(os.path.join(H, 'previews', 'cover'), exist_ok=True)
PRI = ['chat','button','card','dialog','table','date','input','select','tabs','chart','toast','menu','form','carousel','background','motion','nav','avatar','loader']
host = lambda u: urlparse(u).netloc.replace('www.', '')
styles = {}
for i in d['items']:
    if i['type'] == 'style': styles.setdefault(i['lib'], []).append(i)
byhost = {}
for lib, lst in styles.items():
    L = next((x for x in d['items'] if x['id'] == lib), None)
    if L: byhost.setdefault(host(L['url']), lib)
SC = {r[0]: r[2] for r in json.load(open('/workspace/cap/scores.json'))} if os.path.exists('/workspace/cap/scores.json') else {}
def best(lib):
    '''优先挑色彩/实心元素多的演示截图（更像组件本身，少文档文字）'''
    lst = styles[lib]
    def key(x):
        sc = SC.get(x['id'], {}); vis = sc.get('col', 0) * 3 + sc.get('solid', 0)
        return (0 if vis > 0.03 else 1, PRI.index(x['kind']) if x['kind'] in PRI else 99, -vis)
    return sorted(lst, key=key)[0]
LIVEPOSTER = {'orbs-jakubantalik-com': 'previews/live-orbs.webp'}  # 组件本体的实时渲染截图
stat = {'pick': 0, 'lib_style': 0, 'host_style': 0, 'placeholder': 0}
for i in d['items']:
    if i['type'] in ('style', 'skill'): continue
    rid = i['id']; m = media.get(rid, {}); m.pop('img', None); m.pop('src', None); m.pop('from', None)
    if rid in LIVEPOSTER:
        m['img'] = LIVEPOSTER[rid]; m['src'] = 'comp'; stat['pick'] += 1
    elif rid in pick and pick[rid]:
        p = pick[rid]; dst = f'previews/cover/{rid}.webp'
        shutil.copyfile(p['file'], os.path.join(H, dst)); m['img'] = dst; m['src'] = p.get('src', 'app'); stat['pick'] += 1
    elif rid in styles:
        b = best(rid); m['img'] = media[b['id']]['img']; m['src'] = 'comp'; m['from'] = b['id']; stat['lib_style'] += 1
    elif i['type'] == 'library' and host(i['url']) in byhost:
        b = best(byhost[host(i['url'])]); m['img'] = media[b['id']]['img']; m['src'] = 'comp'; m['from'] = b['id']; stat['host_style'] += 1
    else: stat['placeholder'] += 1
    if m: media[rid] = m
    elif rid in media: del media[rid]
open(os.path.join(H, 'media.js'), 'w', encoding='utf-8').write('window.UI_MEDIA=' + json.dumps(media, ensure_ascii=False) + ';\n')
print(stat)
