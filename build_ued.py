#!/usr/bin/env python3
"""v3h：导入第二批（大厂 UED / Skills / 教程 / 规范 / 灵感站 / AI Coding×设计）资源，并给全部卡片加两个筛选维度：
  rt = 资源类型（多选标签），vs = 页面样式风格（多选标签）。
在 build.py → build_media.py → build_styles.py → build_covers.py → build_notes.py → build_legal.py → build_orig.py 之后运行；可重复运行（先删掉 batch=ued 再加）。
数据源：_ued/items_[a-d].py（8 语说明，人工撰写），_ued/orig_new.json（_ued/fetch.py 抓的原站原文），_ued/covers.json（网站首页截图封面）。"""
import json, os, re, shutil
H = os.path.dirname(os.path.abspath(__file__)); U = os.path.join(H, '_ued')
LANGS = ['en','ja','ko','ms','es','de','fr']
def rjs(f, pre):
    s = open(os.path.join(H, f), encoding='utf-8').read(); return json.loads(s[len(pre):].rstrip().rstrip(';'))
def wjs(f, pre, o): open(os.path.join(H, f), 'w', encoding='utf-8').write(pre + json.dumps(o, ensure_ascii=False) + ';\n')
ns = {}
for f in ('items_a.py','items_b.py','items_c.py','items_d.py'): exec(open(os.path.join(U, f), encoding='utf-8').read(), ns)
NEW = ns['A'] + ns['B'] + ns['C'] + ns['D']
SEC = {'S': ('Agent 设计 Skills · 新增', '十一、Agent 设计 Skills（Cursor / Claude Code / Codex）· 2026-10 新增'),
       'D': ('大厂 UED / 设计系统', '十二、大厂 UED 与官方设计系统'),
       'T': ('设计教程', '十三、设计教程：组件体系、token、字体、间距、动效、无障碍'),
       'N': ('组件风格与 Token 规范', '十四、组件风格与规范：token 标准、命名、无障碍硬规范'),
       'I': ('UI 灵感站与素材 · 新增', '十五、UI 灵感站、组件与素材 · 2026-10 新增'),
       'A': ('AI Coding × 设计', '十六、AI Coding × 设计：工作流、工具、DESIGN.md、课程与资讯')}
RT_TAG = {'skill':'Skill','mcp':'MCP','design-md':'DESIGN.md','tokens-spec':'Token','a11y':'无障碍','anti-slop':'去 AI 味','design-system':'大厂规范','motion':'动效'}

d = json.load(open(os.path.join(H, 'data.json'), encoding='utf-8'))
items = [i for i in d['items'] if i.get('batch') != 'ued']
urls = {i['url'].rstrip('/') for i in items}

# ---------- 现有卡片：资源类型 ----------
DS = {'lib-ant-design','lib-mobile-ant-design','lib-tdesign-tencent-com','lib-arco-design','lib-semi-design','lib-element-plus-org','lib-vant-ui-github-io-vant',
      'lib-react-fluentui-dev','lib-carbondesignsystem-com','lib-primer-style','lib-material-web-dev','lib-mui-com-material-ui','lib-material-angular-dev',
      'lib-react-aria-adobe-com','lib-ng-ant-design','x-ant-design','tdesign-tencent-com-chat','lib-g2-antv-antgroup-com'}
ASSETS = {'lib-lucide-dev','lib-heroicons-com','lib-tabler-io-icons','lib-phosphoricons-com','lib-icon-sets-iconify-design'}
A11Y = {'lib-react-aria-adobe-com','lib-www-radix-ui-com-primitives','lib-headlessui-com','lib-ark-ui-com','lib-base-ui-com','lib-reka-ui-com','lib-kobalte-dev','lib-bits-ui-com','lib-melt-ui-com'}
MOTIONLIB = {'lib-motion-dev','lib-motion-dev-examples','lib-www-react-spring-dev','lib-gsap-com','lib-auto-animate-formkit-com','lib-airbnb-io-lottie','lib-lenis-darkroom-engineering','lib-animate-style','lib-threejs-org','lib-r3f-docs-pmnd-rs','lib-drei-docs-pmnd-rs'}
BASE_RT = {'style':'component-demo','library':'component-library','component':'component-library','effect':'motion','skill':'skill','inspiration':'inspiration',
           'template':'template','generator':'generator','guide':'tutorial'}
def rt_of(i):
    if i['type'] == 'style': return ['component-demo'] + (['motion'] if i.get('kind') in ('motion', 'background', 'threed', 'loader') else [])
    s = [BASE_RT.get(i['type'], 'tool')]; k = (i.get('lib') or i['id']); n = (i['name'] + ' ' + i['id']).lower(); tags = i.get('tags', [])
    if k in DS: s.append('design-system')
    if k in ASSETS: s.append('assets')
    if k in A11Y or '无障碍' in tags or re.search(r'accessib|harden', n): s.append('a11y')
    if k in MOTIONLIB or 'motion' in i.get('ct', []) and i['type'] != 'style' or re.search(r'animat|spring|morphing|transition|lottie|libraries-dev-skill', n) or '动效' in tags and i['type'] != 'style': s.append('motion')
    if i['type'] == 'style' and i.get('kind') in ('motion', 'background', 'threed', 'loader'): s.append('motion')
    if k == 'lib-open-props-style': s.append('tokens-spec')
    if k == 'lib-component-gallery': s.append('directory')
    if i['type'] == 'skill' and (re.search(r'taste|impeccable|polish|critique|quieter|bolder|soft-skill|minimalist|redesign|baseline|improve-ui|ui-skills-root|rams|better-interface|make-interfaces|design-review', n) or '去 AI 味' in tags): s.append('anti-slop')
    if 'create-design-md' in n: s.append('design-md')
    if 'web-design-guidelines' in n: s += ['tokens-spec', 'a11y']
    if i['id'] in ('www-ui-skills-com-skills-jakubkrehel-better-typography', 'www-ui-skills-com-skills-jakubkrehel-better-colors'): s.append('tokens-spec')
    return list(dict.fromkeys(s))
# ---------- 现有卡片：页面样式风格 ----------
G = lambda *a: list(a)
LIBVS = {}
for k in ('lib-mui-com-material-ui','lib-mui-com-x','lib-material-angular-dev','lib-material-web-dev','lib-vuetifyjs-com','lib-reactnativepaper-com','lib-quasar-dev'): LIBVS[k] = G('material')
LIBVS['lib-react-fluentui-dev'] = G('fluent', 'enterprise')
for k in ('lib-ant-design','lib-g2-antv-antgroup-com','lib-tdesign-tencent-com','lib-arco-design','lib-semi-design','lib-www-naiveui-com','lib-element-plus-org','lib-primevue-org',
          'lib-primereact-org','lib-primeng-org','lib-ng-ant-design','lib-www-ag-grid-com','lib-fullcalendar-io','lib-echarts-apache-org','x-ant-design','tdesign-tencent-com-chat'): LIBVS[k] = G('enterprise')
LIBVS['lib-carbondesignsystem-com'] = G('enterprise', 'swiss'); LIBVS['lib-primer-style'] = G('minimal', 'enterprise')
LIBVS['lib-mobile-ant-design'] = G('minimal', 'enterprise'); LIBVS['lib-vant-ui-github-io-vant'] = G('playful', 'minimal')
for k in ('lib-konstaui-com','lib-ionicframework-com'): LIBVS[k] = G('apple', 'minimal')
LIBVS['lib-vaul-emilkowal-ski'] = G('apple', 'minimal'); LIBVS['lib-daisyui-com'] = G('playful', 'soft'); LIBVS['lib-animate-style'] = G('playful', 'motion')
LIBVS['lib-www-skeleton-dev'] = G('playful', 'gradient'); LIBVS['lib-chakra-ui-com'] = G('soft', 'minimal'); LIBVS['lib-mantine-dev'] = G('minimal', 'enterprise')
for k in ('lib-motion-dev','lib-motion-dev-examples','lib-www-react-spring-dev','lib-gsap-com','lib-auto-animate-formkit-com','lib-airbnb-io-lottie','lib-lenis-darkroom-engineering'): LIBVS[k] = G('motion')
for k in ('lib-threejs-org','lib-r3f-docs-pmnd-rs','lib-drei-docs-pmnd-rs'): LIBVS[k] = G('3d', 'dark-tech')
LIBVS['lib-www-eldoraui-site'] = G('dark-tech', 'motion'); LIBVS['lib-tremor-so'] = G('minimal', 'enterprise'); LIBVS['lib-getbootstrap-com'] = G('minimal', 'utilitarian')
LIBVS['lib-bulma-io'] = G('minimal', 'utilitarian'); LIBVS['lib-picocss-com'] = G('minimal', 'utilitarian')
IDVS = {
 'magicui-design': G('dark-tech','gradient','motion'), 'ui-aceternity-com': G('dark-tech','gradient','3d','motion'), 'reactbits-dev': G('dark-tech','motion','3d'),
 'animate-ui-com': G('minimal','motion'), 'skiper-ui-com': G('dark-tech','motion'), 'www-vengenceui-com': G('dark-tech','motion'), 'ui-lukacho-com': G('dark-tech','motion'),
 'www-cult-ui-com': G('dark-tech','skeuomorphic','motion'), 'kokonutui-com': G('minimal','motion'), 'smoothui-dev': G('minimal','motion'), 'animata-design': G('playful','motion'),
 'www-hover-dev': G('dark-tech','motion'), 'motion-primitives-com': G('minimal','motion'), 'originkit-dev': G('minimal','motion'), 'canvasui-dev': G('3d','gradient'),
 '21st-dev': G('minimal','dark-tech'), 'www-heroui-com': G('soft','playful'), 'coss-com-ui': G('minimal'), 'www-shadcnblocks-com': G('minimal'),
 'uiverse-io': G('playful','neumorphism','skeuomorphic'), 'www-beautifului-dev': G('minimal','soft'), 'beautiful-ui-five-vercel-app': G('minimal','soft'),
 'beui-dev': G('dark-tech','motion'), 'rareui-com': G('dark-tech','motion'), 'transitions-dev': G('motion','minimal'),
 'orbs-jakubantalik-com': G('skeuomorphic','gradient','3d'), 'beam-jakubantalik-com': G('gradient','dark-tech'), 'metal-jakubantalik-com': G('skeuomorphic','3d'),
 'shaders-paper-design-liquid-metal': G('skeuomorphic','3d'), 'reactbits-dev-animations-metallic-paint': G('skeuomorphic','3d'), 'libraries-dev': G('skeuomorphic','gradient','motion'),
 'shaders-paper-design': G('gradient','3d'), 'www-shadergradient-co': G('gradient','3d'), 'neat-firecms-co': G('gradient','3d'), 'www-unicorn-studio': G('3d','gradient','motion'),
 'github-com-rdev-liquid-glass-react': G('glass','apple'), 'rive-app': G('playful','motion'), 'motion-dev-plus': G('motion','minimal'), 'tympanus-net-codrops': G('editorial','motion','3d'),
 'www-aiverse-design': G('minimal','dark-tech'), 'mobbin-com': G('apple','minimal'), 'land-book-com': G('editorial','minimal'), 'refero-design': G('minimal','editorial'),
 '60fps-design': G('motion','apple'), 'inspora-design': G('editorial','minimal'), 'brandguidelines-net': G('editorial','swiss'), 'backgrounds-supply': G('gradient','3d'),
 'reelfolio-io': G('editorial','motion'), 'ui-elevenlabs-io': G('minimal','gradient'), 'www-thesys-dev': G('minimal','gradient'),
 'www-ui-skills-com-skills-emilkowalski-apple-design': G('apple','glass'), 'www-ui-skills-com-skills-mengto-beautiful-shadows': G('skeuomorphic','soft'),
 'www-ui-skills-com-skills-leonxlnx-soft-skill': G('soft'), 'www-ui-skills-com-skills-leonxlnx-minimalist-skill': G('minimal','swiss'),
 'www-ui-skills-com-skills-pbakaus-bolder': G('editorial','brutalist'), 'www-ui-skills-com-skills-pbakaus-quieter': G('minimal'), 'www-ui-skills-com-skills-pbakaus-overdrive': G('motion','3d'),
 'www-ui-skills-com-skills-pbakaus-delight': G('playful','motion'), 'www-ui-skills-com-skills-rams-rams': G('industrial','minimal'), 'www-ui-skills-com-skills-leonxlnx-taste-skill': G('editorial','minimal'),
 'www-ui-skills-com-skills-zarazhangrui-frontend-slides': G('editorial'), 'www-ui-skills-com-skills-anthropics-canvas-design': G('editorial'), 'www-ui-skills-com-skills-leonxlnx-redesign-skill': G('editorial','minimal'),
}
def vs_of(i):
    k = i.get('lib') or i['id']
    if k in IDVS: return IDVS[k]
    if k in LIBVS: return LIBVS[k]
    if i['type'] == 'style': return ['minimal']
    n = (i['name'] + ' ' + i['id']).lower()
    if re.search(r'animat|spring|morphing|transition|lottie', n): return ['motion', 'minimal']
    if i['type'] == 'effect': return ['gradient', 'motion']
    return ['minimal']
for i in items:
    i['rt'] = rt_of(i); i['vs'] = vs_of(i)

# ---------- 新卡片 ----------
orig_new = json.load(open(os.path.join(U, 'orig_new.json'), encoding='utf-8'))
new = []; dup = []
for x in NEW:
    key, sec, typ, name, url, rt, vs, price, src = x[:9]; zh = x[9]
    if url.rstrip('/') in urls: dup.append(name); continue
    rts = rt.split(); tags = [RT_TAG[r] for r in rts if r in RT_TAG]
    if 'github.com' in url: tags.append('开源')
    new.append(dict(id='ued-' + key, name=name, url=url, note=zh, type=typ, section=SEC[sec][0], sectionTitle=SEC[sec][1], sectionDesc='', source=src,
                    pricing=price, tags=list(dict.fromkeys(tags)), ct=[], rt=rts, vs=vs.split(), batch='ued'))
items = new + items
d['items'] = items; d['count'] = len(items); d['generated'] = '2026-10-10'
json.dump(d, open(os.path.join(H, 'data.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
wjs('data.js', 'window.UI_DATA=', d)

# ---------- 8 语说明 ----------
NI = json.load(open(os.path.join(H, 'notes_src', 'notes_i18n.json'), encoding='utf-8'))
NOTES = rjs('notes.js', 'window.UI_NOTES=')
for x in NEW:
    rid = 'ued-' + x[0]
    for k, lang in enumerate(LANGS):
        NI['notes'].setdefault(lang, {})[rid] = x[10 + k]; NOTES['notes'].setdefault(lang, {})[rid] = x[10 + k]
json.dump(NI, open(os.path.join(H, 'notes_src', 'notes_i18n.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
wjs('notes.js', 'window.UI_NOTES=', NOTES)

# ---------- 许可 / 复制代码说明 ----------
LG = rjs('legal.js', 'window.UI_LEGAL=')
for i in new:
    o = orig_new.get(i['id'][4:], {})
    if i['type'] == 'skill': L = {'k': 'skill'}
    elif i['pricing'] == 'paid': L = {'k': 'paid'}
    elif i['type'] in ('system', 'spec', 'tutorial'): L = {'k': 'doc'}
    elif i['type'] in ('inspiration', 'collection', 'generator', 'template'): L = {'k': 'svc'}
    else: L = {'k': 'unk'}
    if o.get('lic') and o['lic'] not in ('NOASSERTION', ''): L['lic'] = o['lic']
    if 'github.com' in i['url']: L['gh'] = o.get('ds') or i['url']
    LG[i['id']] = L
wjs('legal.js', 'window.UI_LEGAL=', LG)

# ---------- 原站原文（说明 / SKILL.md / 安装命令） ----------
O = rjs('orig.js', 'window.UI_ORIG=')
for i in new:
    o = orig_new.get(i['id'][4:], {}); e = {}
    if o.get('d'): e['d'] = o['d'][:600]; e['ds'] = o.get('ds') or i['url']
    if o.get('p'): e['p'] = o['p']; e['ps'] = o.get('ps') or i['url']; e['pl'] = len(o['p'])
    if e: O[i['id']] = e
    else: O.pop(i['id'], None)
wjs('orig.js', 'window.UI_ORIG=', O)

# ---------- 封面：网站首页真实截图 ----------
M = rjs('media.js', 'window.UI_MEDIA=')
CV = json.load(open(os.path.join(U, 'covers.json'))) if os.path.exists(os.path.join(U, 'covers.json')) else {}
os.makedirs(os.path.join(H, 'previews', 'site'), exist_ok=True)
for rid, mode in CV.items():
    if rid not in {i['id'] for i in items}: continue
    srcf = f'/workspace/cap/home2/{rid}.webp'; dst = f'previews/site/{rid}.webp'
    if not os.path.exists(srcf): continue
    shutil.copyfile(srcf, os.path.join(H, dst))
    m = M.get(rid, {}); m['img'] = dst; m['src'] = 'site'; m.pop('from', None); M[rid] = m
wjs('media.js', 'window.UI_MEDIA=', M)

from collections import Counter
print('new', len(new), 'dup-skipped', dup, 'total', len(items))
print('rt', dict(Counter(r for i in items for r in i['rt'])))
print('vs', dict(Counter(v for i in items for v in i['vs'])))
