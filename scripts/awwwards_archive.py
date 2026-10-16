#!/usr/bin/env python3
"""Discovery feed: awwwards.withseismic.com (Awwwards Archive). robots.txt: Allow / (Disallow /api/, which we never touch);
no published terms. METADATA ONLY, traced to the ORIGINAL sources:
  url = the winning website itself (official site), credit = studio/author (+ its Awwwards profile),
  awwwards = the work's page on awwwards.com (/sites/<slug>, verified, its og:description is the note).
awwwards.withseismic.com is kept only as `discovered_via` (+ `via` link back). Preview = official site's og:image hotlink,
validated to load; Awwwards/withseismic thumbnails are never used or copied.
Scope: Awwwards Site of the Day winners since AW_SINCE (default 2024-01-01). Honorable Mentions and the template
marketplace (/author/webflow--…, framer--…) are out of scope.
Modes: default = feed.xml (latest winners, used by the scheduled job); AW_INITIAL=1 = all studio pages updated since AW_SINCE."""
import json, os, re, sys, time, html, datetime, urllib.request, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hub_lib import append, load, norm, ROOT
from content_filter import blocked
BASE = 'https://awwwards.withseismic.com'
UA = 'Mozilla/5.0 (compatible; ui-hub-bot/1.0; +https://siinxu.github.io/ui-resource-hub/)'
BUA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36 ui-hub-bot'
SINCE = os.environ.get('AW_SINCE', '2024-01-01')
MAX = int(os.environ.get('AW_MAX_NEW', '40'))
STATE = os.path.join(ROOT, 'data', 'awwwards_archive.json')
SECTION = '整站灵感 · Awwwards 每日最佳'
PAUSE = float(os.environ.get('AW_PAUSE', '1.0'))

def get(url, ua=UA, timeout=25, limit=None):
    r = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': ua, 'Accept-Language': 'en'}), timeout=timeout)
    b = r.read(limit) if limit else r.read()
    return b.decode('utf-8', 'replace'), r.geturl()

def studio_page(url):
    """Parse a withseismic studio page -> studio info + its works."""
    h, _ = get(url)
    ld = {}
    for blk in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
        try:
            j = json.loads(blk)
            if j.get('@type') == 'ProfilePage': ld = j
        except Exception: pass
    me = ld.get('mainEntity') or {}
    name = me.get('name') or html.unescape((re.search(r'<title>([^<|—]+)', h) or [None, ''])[1]).strip()
    works = []
    for wid, href, body in re.findall(r'<li id="([^"]+)"[^>]*><a href="([^"]+)"[^>]*>(.*?)</a></li>', h, re.S):
        title = html.unescape((re.search(r'<h3[^>]*title="([^"]*)"', body) or re.search(r'<h3[^>]*>([^<]*)<', body) or [None, ''])[1])
        date = (re.search(r'(\d{4}-\d\d-\d\d)</span>', body) or [None, ''])[1]
        awards = [html.unescape(a) for a in re.findall(r'<span[^>]*color:var\(--muted\)"?[^>]*>([A-Za-z ]+)</span>', body) if a.strip() in ('Site of the Day', 'Honorable Mention', 'Developer Award', 'Site of the Month', 'Site of the Year')]
        works.append({'slug': wid, 'url': html.unescape(href), 'title': title, 'date': date, 'awards': awards})
    return {'name': name, 'profile': me.get('url') or '', 'page': url, 'works': works}

def awwwards_page(slug):
    try:
        h, final = get('https://www.awwwards.com/sites/' + urllib.parse.quote(slug), ua=BUA)
    except Exception:
        return None
    g = lambda p: (re.search(p, h) or [None, None])[1]
    desc = html.unescape(g(r'<meta property="og:description" content="([^"]*)"') or '').strip()
    tags = sorted(set(t.strip('/') for t in re.findall(r'href="/websites/([a-z0-9-]+/)"', h)) - {'nominees', 'sites_of_the_day', 'sites_of_the_month', 'sites_of_the_year', 'honorable'})
    return {'url': final.split('?')[0], 'desc': desc, 'tags': tags}

def img_ok(u):
    try:
        r = urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': BUA, 'Range': 'bytes=0-1023'}), timeout=20)
        return r.status in (200, 206) and (r.headers.get('content-type', '').startswith('image/') or bool(re.search(r'\.(png|jpe?g|webp|gif|avif)(\?|$)', u, re.I)))
    except Exception:
        return False

def og_image(url):
    try: h, final = get(url, ua=BUA, timeout=15, limit=500000)
    except Exception: return None
    for p in [r'<meta[^>]+property=["\']og:image(?::secure_url)?["\'][^>]+content=["\']([^"\']+)', r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']',
              r'<meta[^>]+name=["\']twitter:image(?::src)?["\'][^>]+content=["\']([^"\']+)']:
        m = re.search(p, h, re.I)
        if m:
            u = urllib.parse.urljoin(final, html.unescape(m.group(1)).strip())
            if u.startswith('https://') and not re.search(r'awwwards|withseismic', u) and img_ok(u): return u
            return None
    return None

VS = {'minimal': 'minimal', 'clean': 'minimal', 'typography': 'editorial', 'editorial': 'editorial', '3d': '3d', 'webgl': '3d', 'three-js': '3d', 'threejs': '3d',
      'animation': 'motion', 'transitions': 'motion', 'scrolling': 'motion', 'gradient': 'gradient', 'colorful': 'playful', 'illustration': 'playful', 'retro': 'retro',
      'brutalism': 'brutalist', 'brutalist': 'brutalist', 'swiss-design': 'swiss', 'grid': 'swiss', 'glassmorphism': 'glass'}

def build(w, st):
    slug = w['slug']; aw = awwwards_page(slug); time.sleep(PAUSE)
    tags = (aw or {}).get('tags', [])
    vs = list(dict.fromkeys(VS[t] for t in tags if t in VS)) or ['minimal']
    ct = ['layout'] + (['motion'] if 'animation' in tags or 'transitions' in tags else [])
    awards = [a for a in ['Site of the Day', 'Developer Award', 'Site of the Month', 'Site of the Year'] if a in w['awards']]
    desc = (aw or {}).get('desc') or f"Awwwards {' + '.join(awards) or 'Site of the Day'} ({w['date']}) by {st['name']}."
    it = dict(id='awd-' + slug[:70], name=w['title'][:80], url=w['url'], note=desc, noteEn=desc, type='inspiration', section=SECTION, sectionTitle=SECTION,
              sectionDesc='', source=st['name'], pricing='free', tags=[], ct=ct, rt=['inspiration'], vs=vs,
              origin='site', discovered_via='awwwards.withseismic.com', via=st['page'] + '#' + slug,
              author={k: v for k, v in {'name': st['name'], 'url': st['profile'] or ''}.items() if v},
              awwwards={k: v for k, v in {'page': (aw or {}).get('url'), 'awards': awards, 'date': w['date'], 'tags': tags}.items() if v})
    it['pub'] = w['date']
    return it

def feed_works():
    x, _ = get(BASE + '/feed.xml')
    out = {}
    for item in re.findall(r'<item>(.*?)</item>', x, re.S):
        link = (re.search(r'<link>([^<]+)</link>', item) or [None, ''])[1]
        desc = html.unescape((re.search(r'<description>([^<]*)</description>', item) or [None, ''])[1])
        if 'Site of the Day' not in desc: continue
        page, _, slug = link.partition('#')
        out.setdefault(page, set()).add(slug)
    return out

def initial_pages():
    x, _ = get(BASE + '/sitemap.xml')
    us = re.findall(r'<loc>(' + re.escape(BASE) + r'/author/[^<]+)</loc>.*?<lastmod>([^<]+)</lastmod>', x, re.S)
    return {u: None for u, d in us if d[:10] >= SINCE and '--' not in u.rsplit('/', 1)[-1]}

def jsload(f):
    s = open(os.path.join(ROOT, f), encoding='utf-8').read(); m = re.match(r'\s*(window\.\w+)\s*=\s*', s)
    return m.group(1), json.loads(s[m.end():].rstrip().rstrip(';'))

if __name__ == '__main__':
    st_all = json.load(open(STATE)) if os.path.exists(STATE) else {'seen': {}}
    seen = st_all['seen']
    pages = ({l.strip(): None for l in open(os.environ['AW_PAGES']) if l.strip()} if os.environ.get('AW_PAGES')   # retry list of studio pages
             else initial_pages() if os.environ.get('AW_INITIAL') == '1' else feed_works())
    print(f'mode={"initial" if os.environ.get("AW_INITIAL")=="1" else "feed"} studio_pages={len(pages)} since={SINCE} max={MAX}')
    have = {norm(i['url']) for i in load()['items']}
    cands, cnt = [], [0]
    import threading; lock = threading.Lock()
    def work(item):
        page, only = item
        if cnt[0] >= MAX: return
        if only is not None and all((page + '#' + s) in seen for s in only): return
        try: st = studio_page(page); time.sleep(PAUSE)
        except Exception as e: print('studio fail', page, e); return
        for w in st['works']:
            key = page + '#' + w['slug']
            with lock:
                if key in seen or cnt[0] >= MAX: continue
                if only is not None and w['slug'] not in only: continue
                if 'Site of the Day' not in w['awards'] or (w['date'] or '0') < SINCE: continue
                if not w['url'].startswith('http'): seen[key] = {'status': 'nourl'}; continue
                if norm(w['url']) in have: seen[key] = {'status': 'dup', 'url': w['url']}; continue
                cnt[0] += 1; have.add(norm(w['url']))
            it = build(w, st)
            r = blocked(it)
            if r:
                with lock: seen[key] = {'status': 'blocked', 'why': r}
                continue
            img = og_image(it['url'])
            if img: it['_img'] = img
            with lock:
                cands.append(it); seen[key] = {'status': 'added', 'id': it['id']}
            print(' +', it['id'], it['url'], '| aw' if it['awwwards'].get('page') else '| -', '| img' if img else '', flush=True)
    import concurrent.futures as cf
    with cf.ThreadPoolExecutor(int(os.environ.get('AW_WORKERS', '1'))) as ex: list(ex.map(work, pages.items()))
    cands.sort(key=lambda i: i.get('pub', ''), reverse=True)
    mv, MD = jsload('media.js')
    for it in cands:
        img = it.pop('_img', None)
        if img: MD[it['id']] = {'img': img, 'src': 'og'}
    added = append(cands)
    open(os.path.join(ROOT, 'media.js'), 'w', encoding='utf-8').write(mv + '=' + json.dumps(MD, ensure_ascii=False) + ';\n')
    st_all['updated'] = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%MZ')
    json.dump(st_all, open(STATE, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    c = lambda f: sum(1 for i in added if f(i))
    print(f'added={len(added)} awwwards_page={c(lambda i: i["awwwards"].get("page"))} credit={c(lambda i: i.get("author"))} og={c(lambda i: i["id"] in MD)}')
    if os.environ.get('AW_BUILD', '1') == '1':
        os.system(f'{sys.executable} {os.path.join(os.path.dirname(__file__), "build_extras.py")}')
