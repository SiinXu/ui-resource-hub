#!/usr/bin/env python3
"""Discovery feed: recent.design (robots.txt: Allow /; no published terms). METADATA ONLY.
For every new /i/ entry in https://recent.design/sitemap.xml we trace the ORIGINAL source:
  - X posts -> resolved via public APIs (api.fxtwitter.com, fallback publish.twitter.com/oembed) for author, text and
    the official link the creator posted; url = official site/repo when one exists, else the X post itself.
  - Website / App Store / GitHub entries -> url = that original link.
recent.design is kept only as `discovered_via` (+ `via` attribution link). Preview = official og:image hotlink, never copied.
No files are downloaded from recent.design's CDN. State: data/recent_design.json (processed entries)."""
import json, os, re, sys, time, html, datetime, urllib.request, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hub_lib import append, load, norm, ROOT
from content_filter import blocked
UA = 'Mozilla/5.0 (compatible; ui-hub-bot/1.0; +https://siinxu.github.io/ui-resource-hub/)'
MAX = int(os.environ.get('RD_MAX_NEW', '60'))
STATE = os.path.join(ROOT, 'data', 'recent_design.json')
RAW = os.environ.get('RD_RAW')          # optional local cache of parsed pages (initial import)
SECTION = '设计灵感 · 原作'

def get(url, timeout=25, limit=None):
    r = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': UA, 'Accept-Language': 'en'}), timeout=timeout)
    b = r.read(limit) if limit else r.read()
    return b.decode('utf-8', 'replace'), r.geturl()

def parse(h):
    g = lambda p: (re.search(p, h, re.S) or [None, None])[1]
    out = {'title': html.unescape(g(r'<meta property="og:title" content="([^"]*)"') or '').replace(' — Recent', ''),
           'desc': html.unescape(g(r'<meta name="description" content="([^"]*)"') or ''),
           'date': g(r'<time dateTime="([^"]+)"'),
           'kind': html.unescape(g(r'<p class="x1tz6pr4 x1gqxoa5 x176fvq0">([^<]*)</p>') or '')}
    for k, v in re.findall(r'<p class="x1tz6pr4 x2lah0s xlb5dbd">([^<]+)</p><div[^>]*>(.*?)</div></div>', h, re.S):
        out[k.lower()] = {'links': re.findall(r'href="([^"]+)"', v),
                          'vals': [html.unescape(x).strip() for x in re.findall(r'>([^<>]+)<', v) if x.strip()]}
    return out

def sitemap():
    xml, _ = get('https://recent.design/sitemap.xml')
    return re.findall(r'<loc>(https://recent\.design/i/[^<]+)</loc>', xml)

SOCIAL = re.compile(r'^(https?://)?([a-z0-9-]+\.)?(x\.com|twitter\.com|t\.co|instagram\.com|threads\.net|threads\.com|linkedin\.com|bsky\.app|youtube\.com|youtu\.be|tiktok\.com|facebook\.com|recent\.design|pic\.x\.com)(/|$)', re.I)
def clean(u):
    p = urllib.parse.urlsplit(u)
    q = [(k, v) for k, v in urllib.parse.parse_qsl(p.query) if not re.match(r'utm_|ref$|uo$|s$|t$|via$', k)]
    return urllib.parse.urlunsplit((p.scheme or 'https', p.netloc, p.path, urllib.parse.urlencode(q), ''))

def xpost(url):
    m = re.search(r'(?:x|twitter)\.com/([^/]+)/status/(\d+)', url)
    if not m: return None
    h, sid = m.groups()
    try:
        t = json.loads(get(f'https://api.fxtwitter.com/{h}/status/{sid}')[0])['tweet']
        links = [f.get('replacement') for f in (t.get('raw_text') or {}).get('facets', []) if f.get('type') == 'url' and f.get('replacement')]
        a = t.get('author') or {}
        return {'post': t.get('url') or url, 'handle': a.get('screen_name') or h, 'name': a.get('name') or '', 'text': t.get('text') or '',
                'links': links, 'likes': t.get('likes'), 'reposts': t.get('retweets'), 'bookmarks': t.get('bookmarks'),
                'impressions': (t.get('views') or None), 'date': (t.get('created_timestamp') and datetime.datetime.utcfromtimestamp(t['created_timestamp']).strftime('%Y-%m-%d')) or ''}
    except Exception as e:
        print('fxtwitter fail', url, e); dead = '404' in str(e)
    else: dead = False
    try:   # fallback: official oEmbed (author + text only)
        o = json.loads(get('https://publish.twitter.com/oembed?omit_script=1&url=' + urllib.parse.quote(url))[0])
        txt = html.unescape(re.sub(r'<[^>]+>', ' ', (re.search(r'<p[^>]*>(.*?)</p>', o.get('html', ''), re.S) or [None, ''])[1]))
        links = [l for l in re.findall(r'href="(https://t\.co/[^"]+)"', o.get('html', ''))]
        out = []
        for l in links[:3]:
            try: out.append(get(l, timeout=15, limit=2048)[1])
            except Exception: pass
        return {'post': url, 'handle': o.get('author_url', '').rstrip('/').split('/')[-1] or h, 'name': o.get('author_name', ''), 'text': txt.strip(), 'links': out}
    except Exception as e:
        print('oembed fail', url, e)
        if dead and '404' in str(e): return {'dead': True, 'post': url}
    return {'post': url, 'handle': h, 'name': '', 'text': '', 'links': []}

def img_ok(u):   # hotlinked preview must actually load (skip 404 / non-image og:image)
    try:
        r = urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': UA, 'Range': 'bytes=0-1023'}), timeout=20)
        return r.status in (200, 206) and (r.headers.get('content-type', '').startswith('image/') or bool(re.search(r'\.(png|jpe?g|webp|gif|avif)(\?|$)', u, re.I)))
    except Exception:
        return False

def og_image(url):
    try:
        h, final = get(url, timeout=15, limit=400000)
    except Exception as e:
        return None
    for p in [r'<meta[^>]+property=["\']og:image(?::secure_url)?["\'][^>]+content=["\']([^"\']+)', r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']',
              r'<meta[^>]+name=["\']twitter:image(?::src)?["\'][^>]+content=["\']([^"\']+)']:
        m = re.search(p, h, re.I)
        if m:
            u = urllib.parse.urljoin(final, html.unescape(m.group(1)).strip())
            if u.startswith('https://') and 'recent.design' not in u and img_ok(u): return u
    return None

CT = {'Motion': ['motion'], 'Web': ['layout'], 'Mobile': ['mobile'], 'App Icons': ['icon'], 'Icons': ['icon'], 'Branding': [], 'Illustration': [], 'AI': ['chat']}
VS = {'Minimal': 'minimal', 'Playful': 'playful', '3D': '3d', 'Retro': 'retro', 'Editorial': 'editorial', 'Brutalist': 'brutalist', 'Glassmorphism': 'glass', 'Glass': 'glass',
      'Skeuomorphic': 'skeuomorphic', 'Swiss': 'swiss', 'Gradient': 'gradient', 'Corporate': 'enterprise', 'Soft': 'soft', 'Futuristic': 'dark-tech', 'Industrial': 'industrial'}
def origin_of(u):
    hst = urllib.parse.urlsplit(u).netloc.lower().replace('www.', '')
    if hst in ('x.com', 'twitter.com'): return 'X'
    if hst == 'github.com': return 'GitHub'
    if hst == 'apps.apple.com': return 'App Store'
    return 'site'

def build(rd_url, p):
    if p.get('error') or not p.get('title'): return None, 'parse'
    src = (p.get('source') or {}).get('links') or []
    if not src: return None, 'nosource'
    s0 = src[0]; kind = p.get('kind') or ''
    cre = p.get('creator') or {}; cre_link = (cre.get('links') or [''])[0]; cre_name = (cre.get('vals') or [''])[0]
    code = rd_url.rsplit('/', 1)[-1]
    x = xpost(s0) if re.search(r'(x|twitter)\.com/[^/]+/status/', s0) else None
    official = None
    if x and x.get('dead'): return None, 'x-deleted'   # post removed by its author: don't list a dead link
    if x:
        for l in x['links']:
            if l and not SOCIAL.match(l): official = clean(l); break
    else:
        official = clean(s0) if not SOCIAL.match(s0) else None
    url = official or (x and x['post']) or s0
    handle = (re.search(r'(?:x|twitter)\.com/([A-Za-z0-9_]+)/?$', cre_link or '') or [None, None])[1] or (x and x['handle'])
    cat = ((p.get('category') or {}).get('vals') or [''])[0]
    styles = (p.get('style') or {}).get('vals') or []
    colors = (p.get('color') or {}).get('vals') or []
    vs = list(dict.fromkeys([VS[s] for s in styles + colors if s in VS])) or ['minimal']
    typ = {'Tools': 'tool', 'Skills': 'skill', 'Resources': 'collection'}.get(kind, 'inspiration')
    rt = {'tool': ['tool'], 'skill': ['skill'], 'collection': ['assets']}.get(typ, ['inspiration'])
    if cat in ('Icons', 'Fonts', 'Typefaces'): rt = ['assets']
    ct = CT.get(cat, []) + (['mobile'] if kind in ('App Icons', 'App Screenshots') and 'mobile' not in CT.get(cat, []) else [])
    if kind == 'App Icons' and 'icon' not in ct: ct.append('icon')
    desc = p.get('desc', '').strip()
    it = dict(id='rd-' + code, name=p['title'][:80], url=url, note=desc, noteEn=desc, type=typ, section=SECTION,
              sectionTitle=SECTION, sectionDesc='',
              source=('@' + handle) if handle else origin_of(url).replace('site', urllib.parse.urlsplit(url).netloc.replace('www.', '')),
              pricing='free' if typ == 'inspiration' else 'unknown', tags=[], ct=ct, rt=rt, vs=vs,
              origin='X' if (x and not official) else origin_of(url), discovered_via='recent.design', via=rd_url,
              rdkind=kind, rdcat=cat, rdstyle=styles + colors)
    if handle or cre_name: it['author'] = {k: v for k, v in {'name': (x and x.get('name')) or cre_name, 'handle': ('@' + handle) if handle else '', 'url': cre_link}.items() if v}
    if x:
        it['x_post'] = x['post']
        it['xsrc'] = {k: v for k, v in {'post': x['post'], 'author': '@' + x['handle'], 'likes': x.get('likes'), 'bookmarks': x.get('bookmarks'),
                                        'reposts': x.get('reposts'), 'impressions': x.get('impressions'), 'date': x.get('date')}.items() if v not in (None, '')}
    if official: it['official'] = official
    if p.get('date'): it['pub'] = p['date'][:10]
    return it, 'ok'

def jsload(f):
    s = open(os.path.join(ROOT, f), encoding='utf-8').read(); m = re.match(r'\s*(window\.\w+)\s*=\s*', s)
    return m.group(1), json.loads(s[m.end():].rstrip().rstrip(';'))

if __name__ == '__main__':
    st = json.load(open(STATE)) if os.path.exists(STATE) else {'seen': {}}
    raw = json.load(open(RAW)) if RAW and os.path.exists(RAW) else {}
    urls = sitemap(); todo = [u for u in urls if u not in st['seen']]
    print(f'sitemap={len(urls)} new={len(todo)} max={MAX}')
    have = {norm(i['url']) for i in load()['items']}
    cands, n = [], 0
    for u in todo:
        if n >= MAX: break
        n += 1
        try:
            p = raw.get(u) if u in raw and not raw[u].get('error') else parse(get(u)[0]); time.sleep(0.0 if u in raw else 1.0)
        except Exception as e:
            print('fetch fail', u, e); continue
        it, why = build(u, p)
        if not it: st['seen'][u] = {'status': why}; continue
        k = norm(it['url'])
        if k in have and it.get('x_post') and norm(it['x_post']) not in have:   # same official site already listed -> keep this distinct work via its X post
            it['url'] = it['x_post']; it['origin'] = 'X'; k = norm(it['url'])
        if k in have: st['seen'][u] = {'status': 'dup', 'url': it['url']}; continue
        r = blocked(it)
        if r: st['seen'][u] = {'status': 'blocked', 'why': r}; continue
        img = og_image(it['official']) if it.get('official') else None
        if img: it['_img'] = img
        have.add(k); cands.append(it); st['seen'][u] = {'status': 'added', 'id': it['id']}
        print(' +', it['id'], it['origin'], it.get('source'), it['url'], 'img' if img else '')
    mv, MD = jsload('media.js')
    for it in cands:
        img = it.pop('_img', None)
        if img: MD[it['id']] = {'img': img, 'src': 'og'}
    added = append(cands)
    open(os.path.join(ROOT, 'media.js'), 'w', encoding='utf-8').write(mv + '=' + json.dumps(MD, ensure_ascii=False) + ';\n')
    st['updated'] = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%MZ')
    json.dump(st, open(STATE, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    c = lambda f: sum(1 for i in added if f(i))
    print(f'added={len(added)} x_author={c(lambda i: i.get("xsrc"))} official={c(lambda i: i.get("official"))} x_only={c(lambda i: i["origin"]=="X")} og={c(lambda i: i["id"] in MD)}')
    if os.environ.get('RD_BUILD', '1') == '1':
        os.system(f'{sys.executable} {os.path.join(os.path.dirname(__file__), "build_extras.py")}')
