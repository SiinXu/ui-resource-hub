#!/usr/bin/env python3
"""组件样式卡（v3d）：把 /workspace/cap 抓到的各库「官方文档公开演示」截图变成独立卡片。
每张卡 = 一个组件类型 × 一个来源库，深链到该组件的原站文档页。只存截图（识别/导航用），不存任何源码。
在 build.py、build_media.py 之后运行：python3 build_styles.py"""
import json, os, shutil, hashlib, re
import numpy as np
from PIL import Image
from collections import Counter

def focus(src, dst):
    '''把演示区里的组件本身放大居中：去掉大片留白和细边框线，再按 16:10 补底色。'''
    im = Image.open(src).convert('RGB'); a = np.asarray(im).astype(int); h, w, _ = a.shape
    edge = np.concatenate([a[0], a[-1], a[:, 0], a[:, -1]]); bg = np.median(edge, axis=0)
    m = (np.abs(a - bg).sum(axis=2) > 40)
    rf = m.mean(axis=1); cf = m.mean(axis=0)
    m[rf > 0.55, :] = False; m[:, cf > 0.55] = False      # 去掉横竖贯穿的边框/分隔线
    ys, xs = np.where(m)
    if len(ys) < 50: im.save(dst, 'WEBP', quality=84); return
    y0, y1 = np.percentile(ys, [0.5, 99.5]).astype(int); x0, x1 = np.percentile(xs, [0.5, 99.5]).astype(int)
    p = 28; x0 = max(0, x0 - p); y0 = max(0, y0 - p); x1 = min(w, x1 + p); y1 = min(h, y1 + p)
    c = im.crop((x0, y0, x1, y1)); cw, ch = c.size
    tw = max(cw, int(ch * 1.6), 340); th = max(ch, int(tw / 1.6))
    out = Image.new('RGB', (tw, th), tuple(int(v) for v in bg)); out.paste(c, ((tw - cw) // 2, (th - ch) // 2))
    if out.width < 640: out = out.resize((640, round(640 * out.height / out.width)), Image.LANCZOS)
    out.save(dst, 'WEBP', quality=84)

H = os.path.dirname(os.path.abspath(__file__)); CAP = '/workspace/cap'
d = json.load(open(os.path.join(H, 'data.json'), encoding='utf-8'))
mtxt = open(os.path.join(H, 'media.js'), encoding='utf-8').read(); media = json.loads(mtxt[len('window.UI_MEDIA='):-2])
caps = json.load(open(os.path.join(CAP, 'caps.json')))
REJECT = set(json.load(open(os.path.join(H, 'styles_reject.json')))) if os.path.exists(os.path.join(H, 'styles_reject.json')) else set()
KMAP = {'chip': 'badge', 'effect': 'background', 'code': 'editor'}
EN = {'button':'Button','dialog':'Dialog','select':'Select','table':'Table','toast':'Toast','tabs':'Tabs','date':'Date picker','menu':'Menu','input':'Input',
      'card':'Card','carousel':'Carousel','chart':'Chart','form':'Form','tooltip':'Tooltip','avatar':'Avatar','loader':'Loader','nav':'Navigation','upload':'Upload',
      'editor':'Editor','chat':'Chat','motion':'Motion','background':'Background','layout':'Layout','icon':'Icons','dnd':'Drag & drop','flow':'Flow',
      'switch':'Switch','checkbox':'Checkbox & radio','slider':'Slider','badge':'Badge & tag','progress':'Progress','accordion':'Accordion','pagination':'Pagination',
      'breadcrumb':'Breadcrumb','alert':'Alert','rating':'Rating','color':'Color picker','tree':'Tree','timeline':'Timeline','steps':'Steps','empty':'Empty & result','list':'List','data':'Data display'}
ZH = {'button':'按钮','dialog':'弹窗','select':'选择器','table':'表格','toast':'通知','tabs':'标签页','date':'日期','menu':'菜单','input':'输入框','card':'卡片',
      'carousel':'轮播','chart':'图表','form':'表单','tooltip':'气泡','avatar':'头像','loader':'加载','nav':'导航','upload':'上传','editor':'编辑器','chat':'聊天',
      'motion':'动效','background':'背景','layout':'区块','icon':'图标','dnd':'拖拽','flow':'流程图',
      'switch':'开关','checkbox':'复选单选','slider':'滑块','badge':'徽标标签','progress':'进度','accordion':'折叠面板','pagination':'分页','breadcrumb':'面包屑',
      'alert':'警告提示','rating':'评分','color':'取色器','tree':'树形','timeline':'时间轴','steps':'步骤条','empty':'空状态结果','list':'列表','data':'数据展示'}
by = {i['id']: i for i in d['items']}
d['items'] = [i for i in d['items'] if i['type'] != 'style']
for k in list(media):
    if k.startswith('cs-') or k.startswith('cs2-'): del media[k]
os.makedirs(os.path.join(H, 'previews', 'cs'), exist_ok=True)
seen = set(); n = 0; drop = {}
order = {s[0]: k for k, s in enumerate(json.load(open(os.path.join(CAP, 'order.json'))))} if os.path.exists(os.path.join(CAP,'order.json')) else {}
caps.sort(key=lambda c: -(c.get('std') or 0))
for c in caps:
    why = None
    if c.get('err'): why = 'err'
    elif (c.get('status') or 0) >= 400: why = 'http'
    elif re.search(r'404|not found|page not found', c.get('title', ''), re.I): why = '404'
    elif (c.get('std') or 0) < 5: why = 'blank'
    elif c['id'] in REJECT: why = 'reject'
    src = os.path.join(CAP, 'out', c['id'] + '.webp')
    if not why and not os.path.exists(src): why = 'nofile'
    if not why:
        hh = hashlib.md5(open(src, 'rb').read()).hexdigest()
        if hh in seen: why = 'dup'
        seen.add(hh)
    if why: drop[why] = drop.get(why, 0) + 1; continue
    L = by[c['lib']]; kind = KMAP.get(c['kind'], c['kind'])
    rid = 'cs-' + c['id'].replace('--', '-')
    focus(src, os.path.join(H, 'previews', 'cs', rid + '.webp'))
    d['items'].append(dict(id=rid, type='style', lib=L['id'], libName=c['name'], kind=kind, name=f"{EN.get(kind,kind)} · {c['name']}",
        url=c.get('final') or c['url'], page=c['url'], note=f"{c['name']} 官方文档里的「{ZH.get(kind,kind)}」公开演示", section='组件样式', sectionTitle='组件样式（官方文档演示截图）',
        sectionDesc='', source='', pricing=L['pricing'], tags=[t for t in L['tags'] if t != '开源'] + [c['name']], ct=[kind]))
    media[rid] = {'img': f'previews/cs/{rid}.webp', 'src': 'shot'}; n += 1
# ---- v3e：同一文档页的多个官方演示块（不同变体），dHash 去重 ----
def dh(p):
    im = Image.open(p).convert('L').resize((17, 16), Image.LANCZOS); a = np.asarray(im).astype(int)
    return int(''.join('1' if v else '0' for v in (a[:, 1:] > a[:, :-1]).flatten()), 2)
BADLAB = re.compile(r'^(props|styles api|design token|semantic dom|keyboard( interaction)?|methods|api|api reference|accessibility|events|slots|attributes|on this page|introduction|description|form props|root provider|command palette|components|buttons|forms|ui patterns|template|css variables|data attributes|types|parameters|properties|options|exposes|theming|changelog|faq)$', re.I)
GENERIC = re.compile(r'^(examples?|demos?|usage|preview|installation|overview|playground|code|api|import|anatomy|default|)$', re.I)
caps2 = list({r['page']: r for r in (json.loads(l) for l in open(os.path.join(CAP, 'caps2.jsonl')))}.values()) if os.path.exists(os.path.join(CAP, 'caps2.jsonl')) else []
REJ2 = set(json.load(open(os.path.join(H, 'styles_reject2.json')))) if os.path.exists(os.path.join(H, 'styles_reject2.json')) else set()
hashes = {}
for i in d['items']:
    if i['type'] == 'style': hashes.setdefault(i['lib'], []).append(dh(os.path.join(H, 'previews', 'cs', i['id'] + '.webp')))
PAGE = {}; drop2 = Counter(); n2 = 0
ids = {i['id'] for i in d['items']}
for pgr in caps2:
    PAGE[(pgr['lib'], pgr['url'])] = pgr
    if pgr.get('err') and not pgr['shots']: drop2['err'] += 1; continue
    st_ = pgr.get('status') or 0
    if (st_ >= 400 and pgr['lib'] != 'lib-www-naiveui-com') or re.search(r'404|not found', pgr.get('title', '') + ' ' + pgr.get('h1', ''), re.I):
        drop2['http'] += len(pgr['shots']) or 1; continue
    L = by[pgr['lib']]; kind = KMAP.get(pgr['kind'], pgr['kind'])
    for sh in pgr['shots']:
        src = os.path.join(CAP, 'out2', sh['id'] + '.webp')
        if sh['id'] in REJ2: drop2['reject'] += 1; continue
        if (sh.get('std') or 0) < 6 or not os.path.exists(src): drop2['blank'] += 1; continue
        w, h_ = sh['size']
        if w < 200 or h_ < 120: drop2['small'] += 1; continue
        hv = dh(src)
        if any(bin(hv ^ o).count('1') <= 10 for o in hashes.get(L['id'], [])): drop2['dup'] += 1; continue
        hashes.setdefault(L['id'], []).append(hv)
        rid = 'cs2-' + re.sub(r'[^a-z0-9-]+', '-', sh['id'].lower()).strip('-')
        if rid in ids: drop2['dupid'] += 1; continue
        ids.add(rid)
        dst = os.path.join(H, 'previews', 'cs', rid + '.webp')
        if not os.path.exists(dst) or os.path.getmtime(dst) < os.path.getmtime(src): focus(src, dst)
        lab = (sh.get('label') or '').replace('\u200b', '').split('\n')[0].strip().rstrip('#').strip()
        if BADLAB.search(lab): drop2['doclabel'] += 1; hashes[L['id']].pop(); ids.discard(rid); continue
        if len(lab.split()) > 4 or re.search(r'\d', lab): lab = ''
        if GENERIC.match(lab) or lab.lower() == (pgr.get('h1') or '').lower().strip(): lab = ''
        url = (pgr.get('final') or pgr['url']); anc = sh.get('anchor') or ''
        if anc and anc not in ('mainContent', 'examples', 'Demos') and '#' not in url: url = url + '#' + anc
        d['items'].append(dict(id=rid, type='style', lib=L['id'], libName=pgr['name'], kind=kind, var=lab[:40],
            name=f"{EN.get(kind,kind)} · {pgr['name']}" + (f" · {lab[:40]}" if lab else ''), url=url, page=pgr['url'], shot=sh['id'],
            note=f"{pgr['name']} 官方文档里的「{ZH.get(kind,kind)}」公开演示" + (f"（{lab[:40]}）" if lab else ''), section='组件样式',
            sectionTitle='组件样式（官方文档演示截图）', sectionDesc='', source='', pricing=L['pricing'],
            tags=[t for t in L['tags'] if t != '开源'] + [pgr['name']], ct=[kind]))
        media[rid] = {'img': f'previews/cs/{rid}.webp', 'src': 'shot'}; n2 += 1
print('v3e new style cards', n2, 'dropped', dict(drop2))
json.dump({f'{k[0]}|{k[1]}': v for k, v in PAGE.items()}, open(os.path.join(H, '_orig', 'pages_cap.json'), 'w'), ensure_ascii=False)
base = [i for i in d['items'] if i['type'] != 'style']; st = [i for i in d['items'] if i['type'] == 'style']
buckets = {}
for i in st: buckets.setdefault(i['lib'], []).append(i)
rr = []; ks = list(buckets)
while any(buckets.values()):
    for k in ks:
        if buckets[k]: rr.append(buckets[k].pop(0))
d['items'] = base + rr
d['count'] = len(d['items'])
json.dump(d, open(os.path.join(H, 'data.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
open(os.path.join(H, 'data.js'), 'w', encoding='utf-8').write('window.UI_DATA=' + json.dumps(d, ensure_ascii=False) + ';\n')
open(os.path.join(H, 'media.js'), 'w', encoding='utf-8').write('window.UI_MEDIA=' + json.dumps(media, ensure_ascii=False) + ';\n')
print('style cards', n, 'dropped', drop, 'total items', d['count'])
