#!/usr/bin/env python3
"""Daily UI resource harvester (append-only).
Sources (all public, legal): GitHub Search API (UI/component repos), awesome-shadcn-ui list (GitHub README),
Hacker News Algolia API (Show HN design/UI tools). Product Hunt needs an API token -> used only if PH_TOKEN is set.
Dedupes against data.json by normalised URL and id, appends max N items, then rebuilds site extras."""
import json, os, re, sys, datetime, urllib.request, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hub_lib import append, load, norm, lib_item
MAX = int(os.environ.get('MAX_NEW', '15'))
OK_LIC = {'MIT','Apache-2.0','BSD-3-Clause','BSD-2-Clause','ISC','MPL-2.0','0BSD','Unlicense','CC0-1.0'}
TOK = os.environ.get('GITHUB_TOKEN') or os.environ.get('GH_TOKEN')
def get(url, gh=False):
    h = {'User-Agent': 'ui-resource-hub-bot', 'Accept': 'application/vnd.github+json' if gh else '*/*'}
    if gh and TOK: h['Authorization'] = 'Bearer ' + TOK
    with urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=30) as r:
        return r.read().decode('utf-8', 'replace')
CT = [('chat',r'chat|assistant|ai'),('motion',r'animat|motion|transition'),('background',r'background|shader|gradient'),('chart',r'chart|graph|visuali'),
      ('table',r'table|grid'),('form',r'form|input'),('layout',r'block|landing|template|section'),('icon',r'icon'),('editor',r'editor'),('dialog',r'modal|dialog|drawer')]
def cts(t): return [k for k,rx in CT if re.search(rx, t, re.I)]
def fws(t):
    out=[f for f,rx in [('React',r'react|next\.?js|shadcn'),('Vue',r'\bvue|nuxt'),('Svelte',r'svelte'),('Angular',r'angular'),('HTML',r'tailwind|css')] if re.search(rx,t,re.I)]
    return out or ['HTML']
def from_repo(r, why):
    lic = (r.get('license') or {}).get('spdx_id')
    if lic not in OK_LIC or r.get('fork') or r.get('archived') or not r.get('description'): return None
    desc = r['description'].strip()[:180]
    if not re.search(r'\bui\b|component|design|tailwind|shadcn|css|interface|animation|theme', desc+' '+' '.join(r.get('topics',[])), re.I): return None
    hay = r['full_name']+' '+desc+' '+' '.join(r.get('topics',[]))
    url = r.get('homepage') if (r.get('homepage') or '').startswith('https://') else r['html_url']
    return lib_item('gh-'+re.sub(r'[^a-z0-9]+','-',r['full_name'].lower()), r['name'], url,
        f"{why}：{desc}（GitHub ★{r['stargazers_count']}，{lic} 许可，仓库 {r['full_name']}）", cts(hay), fws(hay),
        tags=['开源','自动收录'], section='每日新收录', source='GitHub') | {'noteEn': f"New GitHub UI repo: {desc} (★{r['stargazers_count']}, {lic}, {r['full_name']})"}
def github():
    since = (datetime.date.today()-datetime.timedelta(days=120)).isoformat()
    qs = [f'topic:ui-components created:>{since} stars:>150', f'topic:shadcn-ui created:>{since} stars:>150',
          f'topic:tailwind-components created:>{since} stars:>100', f'topic:design-system created:>{since} stars:>200',
          f'"component library" in:description created:>{since} stars:>300', f'topic:react-components pushed:>{since} stars:>2000']
    out=[]
    for q in qs:
        try: js=json.loads(get('https://api.github.com/search/repositories?sort=stars&per_page=30&q='+urllib.parse.quote(q), gh=True))
        except Exception as e: print('gh fail', q, e); continue
        out += [x for x in (from_repo(r,'GitHub 新晋 UI 仓库') for r in js.get('items',[])) if x]
    return out
def awesome():
    out=[]
    try: md=get('https://raw.githubusercontent.com/birobirobiro/awesome-shadcn-ui/main/README.md')
    except Exception as e: print('awesome fail', e); return out
    rows = re.findall(r'^\|\s*([^|\[]{2,60}?)\s*\|\s*([^|]{10,300}?)\s*\|\s*\[Link\]\((https://[^)]+)\)\s*\|\s*(\d{4}-\d\d-\d\d)', md, re.M)
    rows.sort(key=lambda r: r[3], reverse=True)   # newest additions first
    for name,desc,url,_ in rows[:200]:
        desc = desc[:200]
        out.append(lib_item('aw-'+re.sub(r'[^a-z0-9]+','-',norm(url))[:60], name.strip(), url, f'awesome-shadcn-ui 收录：{desc.strip()}',
            cts(name+desc), ['React'], pricing='unknown', tags=['shadcn','自动收录'], section='每日新收录', source='awesome-shadcn-ui', type='collection' if 'github.com' not in url else 'library') | {'noteEn': 'Listed in awesome-shadcn-ui: '+desc.strip()})
    return out
def hn():
    out=[]; ts=int((datetime.datetime.now()-datetime.timedelta(days=3)).timestamp())
    for q in ['UI components','design tool','tailwind','shadcn','design system']:
        try: js=json.loads(get('https://hn.algolia.com/api/v1/search?tags=show_hn&numericFilters=created_at_i>%d,points>25&query=%s'%(ts,urllib.parse.quote(q))))
        except Exception as e: print('hn fail', e); continue
        for h in js.get('hits',[]):
            u=h.get('url') or ''
            if not u.startswith('https://'): continue
            t=re.sub(r'^Show HN:\s*','',h['title'])
            if not re.search(r'\bUI\b|design|component|tailwind|shadcn|css|figma|icon|font|animation', t, re.I): continue
            out.append(lib_item('hn-'+str(h['objectID']), t[:60], u, f"Hacker News「Show HN」近期热门设计/UI 工具（{h.get('points')} 分）：{t}", cts(t), fws(t),
                pricing='unknown', tags=['自动收录'], section='每日新收录', source='Hacker News', type='tool', rt=('tool',)) | {'noteEn': f"Trending Show HN design/UI tool ({h.get('points')} pts): {t}"})
    return out
def producthunt():
    tok=os.environ.get('PH_TOKEN'); out=[]
    if not tok: return out
    q='{"query":"{ posts(first:20, topic:\\"design-tools\\", order:VOTES){ edges{ node{ id name tagline website votesCount } } } }"}'
    try:
        req=urllib.request.Request('https://api.producthunt.com/v2/api/graphql',data=q.encode(),headers={'Authorization':'Bearer '+tok,'Content-Type':'application/json'})
        js=json.loads(urllib.request.urlopen(req,timeout=30).read())
        for e in js['data']['posts']['edges']:
            n=e['node']; out.append(lib_item('ph-'+n['id'], n['name'], n['website'], f"Product Hunt 设计工具：{n['tagline']}（{n['votesCount']} 票）", cts(n['tagline']), ['HTML'], pricing='unknown', tags=['自动收录'], section='每日新收录', source='Product Hunt', type='tool', rt=('tool',)))
    except Exception as e: print('ph fail', e)
    return out
if __name__ == '__main__':
    cands = github() + hn() + awesome() + producthunt()
    have = {norm(i['url']) for i in load()['items']}
    fresh, seen = [], set()
    for c in cands:
        k=norm(c['url'])
        if k in have or k in seen: continue
        seen.add(k); fresh.append(c)
    added = append(fresh[:MAX])
    print(f'candidates={len(cands)} fresh={len(fresh)} added={len(added)}')
    for a in added: print(' +', a['name'], a['url'])
    os.system(f'{sys.executable} {os.path.join(os.path.dirname(__file__),"build_extras.py")}')
