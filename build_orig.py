#!/usr/bin/env python3
"""v3e：orig.js —— 每张卡的「原站原文」（说明 / 官方 Prompt / 官方示例代码）与「聚合站补充」分开存放。
原则：原站内容放在前面、原样保留（仅去掉多余空行），注明来源 URL 和许可；聚合站自己写的安装命令等只作为补充附在后面。
代码只给已核实为宽松开源许可（MIT / Apache-2.0 / ISC / BSD）的库；付费、专有、AGPL、Commons Clause 等一律禁用。
数据：_orig/pages.json（原站 meta 说明、ui-skills 安装命令）、_orig/readme_parsed.json（GitHub README 简介/安装/用法）、
_orig/pages_cap.json（组件文档页：页首说明、用法代码、每个演示块的源码，由 /workspace/cap/cap2.py 抓取）。
在 build_styles.py 和 build_legal.py 之后运行。"""
import json, os, re
H = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(H, 'data.json'), encoding='utf-8'))
lg = json.loads(open(os.path.join(H, 'legal.js'), encoding='utf-8').read()[len('window.UI_LEGAL='):-2])
P = json.load(open(os.path.join(H, '_orig', 'pages.json'), encoding='utf-8'))
R = json.load(open(os.path.join(H, '_orig', 'readme_parsed.json'), encoding='utf-8'))
C = json.load(open(os.path.join(H, '_orig', 'pages_cap.json'), encoding='utf-8')) if os.path.exists(os.path.join(H, '_orig', 'pages_cap.json')) else {}
OKLIC = re.compile(r'^(MIT|Apache-2\.0|ISC|BSD|0BSD|BSD-[23]-Clause)$')
by = {i['id']: i for i in d['items']}
DEMO = json.load(open(os.path.join(H, '_orig', 'democode.json'), encoding='utf-8')) if os.path.exists(os.path.join(H, '_orig', 'democode.json')) else {}
def tidy(s, n=2500):
    s = re.sub(r'\n{3,}', '\n\n', (s or '').replace('\r', '')).strip()
    return s[:n]
def ok_code(c):
    '''丢弃被页面折叠截断的片段：括号不配对或以 { ( 结尾的不算完整原文。'''
    if not c: return ''
    if abs(c.count('{') - c.count('}')) > 0 or abs(c.count('(') - c.count(')')) > 1 or c.rstrip()[-1:] in '{(,': return ''
    return c
def bad_desc(s):
    return (not s) or len(s) < 25 or re.search(r'help us keep running|cookie|sign in|javascript is required|just a moment', s, re.I)
def repo_of(l): return l['gh'].split('github.com/')[1].strip('/') if l.get('gh') else ''
# 每个库：从它任一文档页里找一段官方「用法」代码（import ...）
lib_usage = {}
for k, v in C.items():
    lib = k.split('|')[0]
    if ok_code(tidy(v.get('usage'))) and lib not in lib_usage: lib_usage[lib] = (tidy(v['usage']), v.get('final') or v['url'])
# v3f：官方仓库文档演示原文（_orig/fetch_full.py）+ 官方安装/配置原文，组成「安装 → 配置 → 引入 → 基础用法」
FULL = json.load(open(os.path.join(H, '_orig', 'fullcode.json'), encoding='utf-8')) if os.path.exists(os.path.join(H, '_orig', 'fullcode.json')) else {}
SETUP = FULL.pop('__setup__', {})
_F2 = os.path.join(H, '_orig', 'fullcode2.json')  # v3g：第二批官方完整代码（_orig/fetch_full2.py）
if os.path.exists(_F2): FULL.update(json.load(open(_F2, encoding='utf-8')))
_S2 = os.path.join(H, '_orig', 'setup2.json')  # v3g：CSS / Vue 库官方安装 + 引入原文（_orig/fetch_setup2.py）
if os.path.exists(_S2): SETUP.update(json.load(open(_S2, encoding='utf-8')))
# v3g：商业许可部分（MUI X Pro / Premium）不给代码，即使库本体是 MIT
PRO_URL = re.compile(r'mui\.com/x/react-date-pickers/date-range-picker|mui\.com/x/react-data-grid/#(pro|premium)-version')
GHR = lambda r, f='README.md', b='HEAD': f'https://github.com/{r}/blob/{b}/{f}'
INSTALL = {  # 官方 README / 官方入门文档里的安装命令原文（2026-10-10 核对）
 'lib-ant-design': [('Install', 'npm install antd', GHR('ant-design/ant-design'))],
 'lib-ng-ant-design': [('Install', 'ng add ng-zorro-antd', GHR('NG-ZORRO/ng-zorro-antd'))],
 'lib-www-naiveui-com': [('Install', 'npm i naive-ui', GHR('tusen-ai/naive-ui'))],
 'lib-quasar-dev': [('Install', 'pnpm create quasar@latest\n# or\nnpm init quasar@latest', GHR('quasarframework/quasar', 'docs/src/pages/start/quick-start.md'))],
 'lib-tdesign-tencent-com': [('Install', 'npm i tdesign-vue-next', GHR('Tencent/tdesign-vue-next'))],
 'lib-vuetifyjs-com': [('Install', 'npm create vuetify@latest', GHR('vuetifyjs/vuetify', 'packages/docs/src/pages/en/getting-started/installation.md'))],
 'lib-arco-design': [('Install', 'npm install @arco-design/web-react', GHR('arco-design/arco-design'))],
 'www-heroui-com': [('Install', 'npm i @heroui/styles @heroui/react', GHR('heroui-inc/heroui', 'apps/docs/content/docs/en/react/getting-started/(overview)/quick-start.mdx', 'v3')),
                    ('Setup · globals.css', '@import "tailwindcss";\n@import "@heroui/styles";', GHR('heroui-inc/heroui', 'apps/docs/content/docs/en/react/getting-started/(overview)/quick-start.mdx', 'v3'))],
}
STEP = {'Install': '① 安装 Install', 'Setup': '② 配置 Setup', 'Import': '③ 引入 Import'}
def hdr(h, src, code):
    k = h.split(' ')[0]
    lab = STEP.get(k, '④ 示例 Example · ' + h)
    if k == 'Setup': lab = '② 配置 ' + h
    txt = f'{lab} — {src}'
    if k == 'Install': return '# ' + txt
    if code.lstrip().startswith('<'): return '<!-- ' + txt + ' -->'
    if code.lstrip().startswith('@import'): return '/* ' + txt + ' */'
    return '// ' + txt
def compose(parts):
    return '\n\n'.join(hdr(p['h'], p['src'], p['code']) + '\n' + p['code'].strip() for p in parts)
def install_parts(i, L):
    lib = i.get('lib') or i['id']
    if lib in SETUP: return SETUP[lib]
    if lib in INSTALL: return [{'h': h, 'code': c, 'src': u} for h, c, u in INSTALL[lib]]
    if L.get('code') and L.get('gh'): return [{'h': 'Install', 'code': L['code'], 'src': L['gh'] + '#readme'}]
    return []
def sup_text(i, L, fw=None):
    s = f"# 聚合站补充 · Hub notes\n# 原站文档 Docs: {i['url']}\n# 许可 License: {L.get('lic')}" + (f" · 框架 Framework: {fw}" if fw else '')
    s += "\n# 以上「原站原文」逐字来自官方仓库/文档（每段标了来源）；完整变体与 API 请看原站。"
    if L.get('pro'): s += f"\n# 不含付费部分：{L['pro']}（请到原站购买）。"
    else: s += "\n# 本站不提供任何付费模板 / Pro 组件源码。"
    return s
FULLN = 0
# v3g：原站公开的 Prompt 全文（不截断）——Skill 的 SKILL.md 全文、README 里写明「给 coding agent 的 prompt」
SKMD = json.load(open(os.path.join(H, '_orig', 'skillmd.json'), encoding='utf-8')) if os.path.exists(os.path.join(H, '_orig', 'skillmd.json')) else {}
RPR = {k: [x for x in v if 'prompt' in x['h'].lower()] for k, v in (json.load(open(os.path.join(H, '_orig', 'readme_prompts.json'), encoding='utf-8')) if os.path.exists(os.path.join(H, '_orig', 'readme_prompts.json')) else {}).items()}
PAGE_PROMPTS = {  # 官网页面上公开列出的示例 Prompt（原文，2026-10-10 抓取）
 'libraries-dev-skill-html': ('Try it', 'https://libraries.dev/skill.html', ['Review my project and suggest where libraries.dev effects fit', 'Show a thinking orb while the chat reply is streaming', 'Add a border beam to the prompt input while it generates', 'Give each agent in the sidebar a bot avatar that follows its status']),
}
def skill_prompt(rid):
    k = SKMD[rid]
    t = f"# 官方安装命令 Install\n{k['install']}\n\n# SKILL.md 全文 · {k['src']} · License: {k['lic']}\n{k['md']}"
    if rid in PAGE_PROMPTS:
        h, u, ps = PAGE_PROMPTS[rid]; t += f"\n\n# 官网示例 Prompt（{h}）· {u}\n" + '\n'.join('- ' + x for x in ps)
    return t
DESCS = json.load(open(os.path.join(H, '_orig', 'descs.json'), encoding='utf-8')) if os.path.exists(os.path.join(H, '_orig', 'descs.json')) else {}  # v3g：缺说明的卡补官方文档原文（_orig/fetch_desc.py）
CSSLIB = {'lib-getbootstrap-com', 'lib-daisyui-com', 'lib-flowbite-com', 'lib-bulma-io', 'lib-picocss-com', 'lib-open-props-style', 'lib-www-hyperui-dev'}
out = {}; stat = dict(code_orig=0, code_sup_only=0, code_off=0, prompt_orig=0, prompt_desc=0, prompt_sup_only=0)
for i in d['items']:
    rid = i['id']; o = {}
    L = lg.get(rid) or (lg.get(i.get('lib')) if i.get('lib') else None) or {'k': 'unk'}
    oss = L.get('k') == 'oss' and OKLIC.match(L.get('lic', '') or '')
    if i['type'] == 'style':
        pg = C.get(f"{i['lib']}|{i.get('page', '')}") or {}
        desc = tidy(pg.get('lead') or '', 500)
        if bad_desc(desc): desc = tidy(pg.get('md') or '', 400)
        if not bad_desc(desc): o['d'] = desc; o['ds'] = pg.get('final') or i['url']
        if oss:
            code = ''
            if i.get('shot'):
                sh = next((s for s in pg.get('shots', []) if s['id'] == i['shot']), None)
                code = tidy(sh.get('code') if sh else '')
            elif pg.get('shots'):
                code = tidy(pg['shots'][0].get('code'))
            code = ok_code(code); use = ok_code(tidy(pg.get('usage')))
            if use and use not in code: code = (use + '\n\n' + code).strip() if code else use
            if code: o['c'] = code; o['cs'] = i['url']; o['cl'] = L['lic']
            if i.get('shot') in DEMO:  # 官方仓库里该演示的原样源码（按演示标题匹配）
                dm = DEMO[i['shot']]; o['c'] = tidy(dm['code'], 4000); o['cs'] = dm['src']; o['cl'] = dm['lic']
            lc = (lg.get(i['lib']) or {}).get('code')
            if lc and lc not in code: o['sup'] = lc
    else:
        pg = P.get(rid, {})
        if pg.get('install'):  # ui-skills.com：原站公开的安装命令 + SKILL 描述，原样作为 Prompt 主体
            o['p'] = pg['install'] + ('\n\n' + pg['skilldesc'] if pg.get('skilldesc') else ''); o['ps'] = i['url']
        rd = R.get(repo_of(L), {})
        desc = pg.get('skilldesc') or pg.get('md') or ''
        ds = i['url']
        if bad_desc(desc) and rd.get('intro'): desc, ds = rd['intro'], rd['src']
        if not bad_desc(desc): o['d'] = tidy(desc, 600); o['ds'] = ds
        if oss:
            code = '\n\n'.join(x for x in (rd.get('install'), rd.get('usage')) if x)
            src = rd.get('src') if code else ''
            if not code and i['id'] in lib_usage and ok_code(lib_usage[i['id']][0]): code, src = lib_usage[i['id']]
            if code: o['c'] = tidy(code); o['cs'] = src; o['cl'] = L['lic']
            if L.get('code') and L['code'].strip() not in (o.get('c') or ''): o['sup'] = L['code']
    if rid in SKMD: o['p'] = skill_prompt(rid); o['ps'] = SKMD[rid]['src']; o['pl'] = len(o['p'])
    elif repo_of(L) in RPR and RPR[repo_of(L)] and i['type'] != 'style':
        x = RPR[repo_of(L)][0]; o['p'] = f"# {x['h']}\n{x['p']}"; o['ps'] = x['src']
    if not o.get('d') and not o.get('p') and rid in DESCS: o['d'] = DESCS[rid]['d']; o['ds'] = DESCS[rid]['ds']
    # v3f：完整官方代码（安装 → 配置 → 引入 → 用法）
    if oss:
        fw = None
        fk = rid if rid in FULL else (next((k for k in (f'cs-{rid}-button', f'cs2-{rid}--button--button--v0', f'cs2-{rid}--button--button--v2') if k in FULL), None) if i['type'] == 'library' and rid in SETUP else None)
        if fk:
            fu = FULL[fk]; fw = fu.get('fw')
            parts = ([] if fu.get('noinst') else install_parts(i, L)) + fu['parts']
            o['c'] = compose(parts); o['cs'] = fu['parts'][-1]['src']; o['cl'] = fu.get('lic') or L['lic']; o['fw'] = fw; o['full'] = 1
        elif o.get('c') and i['type'] == 'style':
            ip = install_parts(i, L)
            if ip and ip[0]['code'] not in o['c']:
                o['c'] = compose(ip) + '\n\n' + hdr('官方文档示例', o.get('cs') or i['url'], o['c']) + '\n' + o['c']
            if ip and (re.search(r'^\s*import |@import|<script', o['c'], re.M) or i.get('lib') in CSSLIB): o['full'] = 1
        if o.get('c'): o['sup'] = sup_text(i, L, fw)
        if o.get('full') and not PRO_URL.search(i['url']): FULLN += 1
    if PRO_URL.search(i['url']):
        for k in ('c', 'cs', 'cl', 'full', 'fw', 'sup'): o.pop(k, None)
        o['nc'] = 'MUI X Pro / Premium 为商业许可，本站不提供代码 · Commercial license (MUI X Pro/Premium) — no code here'
    if o.get('c'): stat['code_orig'] += 1
    elif o.get('sup'): stat['code_sup_only'] += 1
    else: stat['code_off'] += 1
    if o.get('p'): stat['prompt_orig'] += 1
    elif o.get('d'): stat['prompt_desc'] += 1
    else: stat['prompt_sup_only'] += 1
    if o: out[rid] = o
open(os.path.join(H, 'orig.js'), 'w', encoding='utf-8').write('window.UI_ORIG=' + json.dumps(out, ensure_ascii=False) + ';\n')
stat['full_official'] = FULLN
print('items', len(d['items']), stat)
