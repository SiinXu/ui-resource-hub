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
    if o.get('c'): stat['code_orig'] += 1
    elif o.get('sup'): stat['code_sup_only'] += 1
    else: stat['code_off'] += 1
    if o.get('p'): stat['prompt_orig'] += 1
    elif o.get('d'): stat['prompt_desc'] += 1
    else: stat['prompt_sup_only'] += 1
    if o: out[rid] = o
open(os.path.join(H, 'orig.js'), 'w', encoding='utf-8').write('window.UI_ORIG=' + json.dumps(out, ensure_ascii=False) + ';\n')
print('items', len(d['items']), stat)
