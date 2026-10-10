#!/usr/bin/env python3
"""给新卡抓「原站原文」：GitHub 仓库描述 + 许可；宽松许可的 Skill 仓库抓 SKILL.md 原文与 README 里的安装命令；其他站抓 meta description。
输出 _ued/orig_new.json {key: {d, ds, p?, ps?, lic?}}"""
import json, os, re, subprocess, html, hashlib, urllib.request, concurrent.futures as cf
H = os.path.dirname(os.path.abspath(__file__))
ns = {}
for f in ('items_a.py','items_b.py','items_c.py','items_d.py'): exec(open(os.path.join(H,f)).read(), ns)
ITEMS = ns['A']+ns['B']+ns['C']+ns['D']
CACHE = os.path.join(H,'cache'); os.makedirs(CACHE, exist_ok=True)
OK = re.compile(r'^(MIT|Apache-2\.0|BSD-[23]-Clause|ISC|CC-BY-4\.0|CC0-1\.0|Unlicense|MPL-2\.0)$')
def get(url, n=600000):
    fn = os.path.join(CACHE, hashlib.md5(url.encode()).hexdigest())
    if os.path.exists(fn): return open(fn, encoding='utf-8').read()
    try:
        s = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/128 Safari/537.36','Accept-Language':'en,zh;q=0.8'}), timeout=25).read(n).decode('utf-8','replace')
    except Exception as e: s = ''
    open(fn,'w',encoding='utf-8').write(s); return s
def gh(path):
    fn = os.path.join(CACHE, 'gh_'+hashlib.md5(path.encode()).hexdigest())
    if os.path.exists(fn): return json.load(open(fn))
    r = subprocess.run(['gh','api',path], capture_output=True, text=True)
    try: j = json.loads(r.stdout)
    except Exception: j = {}
    json.dump(j, open(fn,'w')); return j
def meta(s):
    for p in (r'<meta[^>]+property=["\']og:description["\'][^>]*content=["\']([^"\']+)', r'<meta[^>]+content=["\']([^"\']+)["\'][^>]*property=["\']og:description',
              r'<meta[^>]+name=["\']description["\'][^>]*content=["\']([^"\']+)', r'<meta[^>]+content=["\']([^"\']+)["\'][^>]*name=["\']description'):
        m = re.search(p, s, re.I)
        if m: return html.unescape(m.group(1)).strip()
    return ''
def fm(md, k):
    m = re.search(r'^'+k+r':\s*(.+)$', md, re.M); return m.group(1).strip().strip('"\'') if m else ''
INSTALL = re.compile(r'^\s*(?:\$\s*)?((?:npx|pnpm dlx|bunx) skills add .+|/plugin (?:marketplace add|install) .+|npx @?[\w\-/]+ (?:add|install|init|setup).+|claude mcp add .+|npm (?:i|install) -g .+)$', re.M)
def one(it):
    key, url, typ = it[0], it[4], it[2]
    m = re.match(r'https://github\.com/([^/]+/[^/#?]+)', url)
    o = {}
    if m:
        repo = m.group(1); r = gh('repos/'+repo)
        if not r.get('full_name'): return key, o
        lic = (r.get('license') or {}).get('spdx_id') or ''
        o['d'] = r.get('description') or ''; o['ds'] = 'https://github.com/'+r['full_name']; o['lic'] = lic; o['stars'] = r.get('stargazers_count')
        br = r.get('default_branch','main')
        readme = get(f'https://raw.githubusercontent.com/{r["full_name"]}/{br}/README.md')
        cmds = list(dict.fromkeys(x.strip() for x in INSTALL.findall(readme)))[:6]
        if OK.match(lic) and (typ=='skill' or key in ('vercel-guidelines-repo','google-design-md','cc-frontend-toolkit','awesome-design-md')):
            tree = gh(f'repos/{r["full_name"]}/git/trees/{br}?recursive=1').get('tree', [])
            sk = sorted([x['path'] for x in tree if x['path'].endswith('SKILL.md')], key=lambda p:(p.count('/'), p))
            parts = []
            if cmds: parts.append('# 官方安装命令 Install（README 原文）\n' + '\n'.join(cmds))
            if len(sk) > 1:
                idx = []
                for p in sk[:40]:
                    md = get(f'https://raw.githubusercontent.com/{r["full_name"]}/{br}/{p}')
                    idx.append(f'- {fm(md,"name") or p.split("/")[-2]}: {fm(md,"description")}  ({p})')
                parts.append(f'# 仓库内 {len(sk)} 个 SKILL.md（name / description 原文）· License: {lic}\n' + '\n'.join(idx))
            if sk:
                md = get(f'https://raw.githubusercontent.com/{r["full_name"]}/{br}/{sk[0]}')
                if len(md) > 30000: md = md[:30000] + '\n\n…（篇幅过长已截断，完整内容见原文链接）'
                parts.append(f'# SKILL.md 全文 · https://github.com/{r["full_name"]}/blob/{br}/{sk[0]} · License: {lic}\n{md}')
                o['ps'] = f'https://github.com/{r["full_name"]}/blob/{br}/{sk[0]}'
            elif readme:
                rd = readme if len(readme) <= 30000 else readme[:30000] + '\n\n…（篇幅过长已截断，完整内容见原文链接）'
                parts.append(f'# README 全文 · https://github.com/{r["full_name"]}/blob/{br}/README.md · License: {lic}\n{rd}')
                o['ps'] = f'https://github.com/{r["full_name"]}/blob/{br}/README.md'
            if parts and o.get('ps'): o['p'] = '\n\n'.join(parts)
        elif cmds and typ in ('skill','tool'):
            o['p'] = '# 官方安装命令 Install（README 原文）\n' + '\n'.join(cmds); o['ps'] = 'https://github.com/'+r['full_name']+'#readme'
    elif 'x.com/' not in url:
        d = meta(get(url))
        if d: o['d'] = d; o['ds'] = url
    return key, o
out = {}
with cf.ThreadPoolExecutor(12) as ex:
    for k, o in ex.map(one, ITEMS): out[k] = o
json.dump(out, open(os.path.join(H,'orig_new.json'),'w',encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'd:', sum(1 for v in out.values() if v.get('d')), 'p:', sum(1 for v in out.values() if v.get('p')))
for k,v in out.items():
    if v.get('lic') is not None: print(k, v.get('lic'), v.get('stars'), 'P' if v.get('p') else '-', len(v.get('p','')))
