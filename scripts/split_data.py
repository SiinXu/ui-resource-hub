#!/usr/bin/env python3
"""Split the canonical data bundle into small first-screen files + lazily loaded parts (perf, 2026-10-17).

Canonical sources stay unchanged and are still written by every pipeline script:
  data.js / data.json (items), media.js, legal.js, notes.js, names_en.js, orig.js.
This script is a deterministic post-step (same inputs -> byte-identical outputs). It writes:
  split/first-<lang>.js   window.UI_FIRST: Featured + "more" + first grid page (96 cards) with card fields only,
                          precomputed facet counts/stats, and the media/legal/names/notes rows those cards need.
  split/core.js           window.UI_CORE: all items, card + filter + search fields, plus guides.
  split/detail.js         window.UI_DETAIL: {id: {detail-only fields}} merged into items before a detail sheet opens.
  split/i18n-<lang>.js    window.UI_I18N for ONE locale (perf 2026-10-17d): {langs (all 10 autonyms), <lang>: dict already
                          resolved through app.js t()'s fallback chain (lang -> en for non-zh -> zh-CN)} plus UI_CT_ORDER /
                          UI_SEC_ORDER. Built by evaluating the canonical i18n.js with node (it is code: many patch IIFEs).
                          i18n.js itself stays canonical and is still used by mobile/.
and rewrites the version map in index.html (/*UHV*/{...}/*/UHV*/) with content hashes so every data change
gets a new URL (cache-busting) without anyone bumping ?v= by hand.

Run it at the end of every workflow that touches data, and locally:  python3 scripts/split_data.py
`--check` exits 1 if the committed split files / index.html are stale (used by the split-data guard workflow).
"""
import hashlib, json, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(ROOT, *a)
LANGS = ['zh-CN', 'zh-TW', 'en', 'ja', 'ko', 'ms', 'vi', 'fr', 'es', 'de']
CT_MAX = 200           # ?ct=<kind> deep-link files only for kinds up to this many items
FIRST_GRID = 96          # app.js moreGrid(): first page = 96 cards
# fields app.js needs to render cards, filter, sort and search (everything else is detail-only)
CORE_F = ['id', 'name', 'note', 'noteTw', 'noteEn', 'url', 'type', 'pricing', 'tags', 'ct', 'rt', 'vs', 'source', 'section',
          'libName', 'kind', 'var', 'lib', 'discovered_via', 'origin', 'xsrc', 'sponsored']
VISUAL = {'style', 'library', 'component', 'effect', 'template', 'generator', 'inspiration', 'guide', 'system', 'spec',
          'tutorial', 'tool', 'collection'}
SRCO = ['recent.design', 'awwwards', 'x', 'github', 'site']
CJK = re.compile(r'[\u3400-\u9fff\uf900-\ufaff]')


def jsload(fn):
    s = open(P(fn), encoding='utf-8').read()
    s = s[s.index('window.'):]
    return json.loads(s[s.index('=') + 1:].rstrip().rstrip(';'))


def dumps(o):
    return json.dumps(o, ensure_ascii=False, separators=(',', ':'))


def core_rec(i):
    r = {k: i[k] for k in CORE_F if k in i}
    if 'xsrc' in r:            # card/filter code only tests truthiness (ORG); the full object lives in detail.js
        r['xsrc'] = 1
    return r


def org(i):  # mirrors app.js ORG()
    if i.get('origin'):
        return 'x' if i['origin'] == 'X' else 'github' if i['origin'] == 'GitHub' else 'site'
    if i.get('xsrc') or i.get('source') == 'X' or str(i.get('source') or '').startswith('@'):
        return 'x'
    return 'github' if re.match(r'^https?://(www\.)?github\.com/', i.get('url') or '') else 'site'


def src_ok(i, k):  # mirrors app.js srcOk()
    if k == 'recent.design':
        return i.get('discovered_via') == 'recent.design'
    if k == 'awwwards':
        return i.get('discovered_via') == 'awwwards.withseismic.com'
    return org(i) == k


def parse_app():
    a = open(P('app.js'), encoding='utf-8').read()
    feat = a[a.index('var FEAT = ['):]
    feat = feat[:feat.index('\n];')]
    fids, live = [], set()
    ms = list(re.finditer(r"\{id:'([^']+)'", feat))
    for n, m in enumerate(ms):
        fids.append(m.group(1))
        seg = feat[m.end():ms[n + 1].start() if n + 1 < len(ms) else len(feat)]
        if 'live:' in seg:
            live.add(m.group(1))
    more = re.findall(r"'([^']+)'", re.search(r'var MORE = \[([^\]]*)\]', a).group(1))
    if not fids:
        sys.exit('split_data: could not parse FEAT from app.js')
    return fids, live, more


def build():
    D = jsload('data.js')
    try:
        J = json.load(open(P('data.json'), encoding='utf-8'))
        if J.get('items') != D.get('items'):
            print('split_data: WARNING data.json and data.js differ; data.js is canonical for the site', file=sys.stderr)
    except FileNotFoundError:
        pass
    M, LG, NOTES, EN = jsload('media.js'), jsload('legal.js'), jsload('notes.js'), jsload('names_en.js')
    items = D['items']
    fids, live, more = parse_app()

    # ---- grid order (mirrors app.js renderGrid sort with no filters): style first, then visual with image, ...
    def grp(i):
        if i['type'] == 'style':
            return -1
        m = M.get(i['id']) or {}
        vis = i['type'] in VISUAL and (i['id'] in live or bool(m.get('img')))
        if vis:
            return 0 if (m.get('img') or i['id'] in live) else 1
        return 2
    order = sorted(range(len(items)), key=lambda k: (grp(items[k]), k))
    first_ids = set(items[k]['id'] for k in order[:FIRST_GRID]) | set(fids) | set(more)
    first_items = [core_rec(i) for i in items if i['id'] in first_ids]   # keep catalog order (client sort is stable)

    # ---- precomputed facets for the default (unfiltered) state, mirrors renderChips() + applyStatic()
    def cnt(f):
        c = {}
        for i in items:
            for x in i.get(f) or []:
                c[x] = c.get(x, 0) + 1
        return c
    tags = {}
    for i in items:
        for x in i['tags']:
            tags[x] = tags.get(x, 0) + 1
    src = {k: sum(1 for i in items if src_ok(i, k)) for k in SRCO}
    facets = {'n': len(items), 'rt': cnt('rt'), 'vs': cnt('vs'), 'ct': cnt('ct'), 'src': src, 'tag': tags}
    stats = {'rt': len(facets['rt']), 'vs': len(facets['vs'])}

    # ---- media / legal rows the first screen needs
    fm = {i['id']: M[i['id']] for i in first_items if i['id'] in M}
    fl = {}
    for i in first_items:
        for k in (i['id'], i.get('lib')):
            if k and k in LG:
                fl[k] = LG[k]

    meta = {'generated': D.get('generated'), 'updatedAt': D.get('updatedAt'), 'count': len(items)}
    out = {}
    blob = dumps(first_items) + dumps(fl)
    top_tags = sorted(tags, key=lambda x: -tags[x])[:40]
    for L in LANGS:
        f = dict(meta, stats=stats, facets=facets, items=first_items, media=fm, legal=fl)
        if not L.startswith('zh'):
            ids = [i['id'] for i in first_items]
            strs = set()
            for i in first_items:
                for k in ('name', 'var', 'source', 'libName', 'kind'):
                    if isinstance(i.get(k), str):
                        strs.add(i[k])
                strs.update(i['tags'])
            for r in fl.values():
                for k in ('lic', 'pro'):
                    if isinstance(r.get(k), str):
                        strs.add(r[k])
            en = {'name': {}, 'var': {}, 'note': {}, 'tag': {}, 'misc': {}}
            for g in ('name', 'var', 'misc'):
                en[g] = {k: v for k, v in EN.get(g, {}).items() if k in strs or k in blob}
            en['note'] = {k: EN['note'][k] for k in ids if k in EN.get('note', {})}
            tg = set(top_tags) | set(x for i in first_items for x in i['tags'])
            for tl in (L, 'en'):
                if tl in EN.get('tag', {}):
                    en['tag'][tl] = {k: v for k, v in EN['tag'][tl].items() if k in tg}
            notes = {'notes': {}, 'why': {}}
            for nl in (L, 'en'):
                if nl in NOTES.get('notes', {}):
                    notes['notes'][nl] = {k: NOTES['notes'][nl][k] for k in ids if k in NOTES['notes'][nl]}
            f['en'], f['notes'] = en, notes
        out[f'split/first-{L}.js'] = '/* generated by scripts/split_data.py from data.js — do not edit */\nwindow.UI_FIRST=' + dumps(f) + ';\n'
    core = dict(meta, items=[core_rec(i) for i in items], guides=D.get('guides', []))
    out['split/core.js'] = '/* generated by scripts/split_data.py from data.js — do not edit */\nwindow.UI_CORE=' + dumps(core) + ';\n'
    det = {}
    for i in items:
        r = {k: v for k, v in i.items() if k not in CORE_F or k == 'xsrc'}
        if r:
            det[i['id']] = r
    # ---- perf 2026-10-26: ?ct=<kind> deep links (e.g. /?ct=pricing) render from split/ct-<kind>.js (UI_CTX: that kind's
    # card rows + media/legal + Latin names/notes for every non-zh locale) instead of waiting for the 2.6 MB core.js.
    # Only kinds with <= CT_MAX items get a file; bigger kinds keep the core.js path. ix = catalog index (stable sort order).
    ixm = {i['id']: k for k, i in enumerate(items)}
    for kind in sorted(facets['ct']):
        if facets['ct'][kind] > CT_MAX:
            continue
        ks = [i for i in items if kind in (i.get('ct') or [])]
        ids = [i['id'] for i in ks]
        cl = {}
        for i in ks:
            for k in (i['id'], i.get('lib')):
                if k and k in LG:
                    cl[k] = LG[k]
        strs = set()
        for i in ks:
            for k in ('name', 'var', 'source', 'libName', 'kind'):
                if isinstance(i.get(k), str):
                    strs.add(i[k])
            strs.update(i['tags'])
        for r in cl.values():
            for k in ('lic', 'pro'):
                if isinstance(r.get(k), str):
                    strs.add(r[k])
        en = {g: {k: v for k, v in EN.get(g, {}).items() if k in strs} for g in ('name', 'var', 'misc')}
        en['note'] = {k: EN['note'][k] for k in ids if k in EN.get('note', {})}
        tg = set(x for i in ks for x in i['tags'])
        en['tag'] = {tl: {k: v for k, v in d.items() if k in tg} for tl, d in EN.get('tag', {}).items()}
        notes = {'notes': {nl: {k: d[k] for k in ids if k in d} for nl, d in NOTES.get('notes', {}).items()}, 'why': {}}
        c = {'ct': kind, 'items': [core_rec(i) for i in ks], 'media': {k: M[k] for k in ids if k in M}, 'legal': cl,
             'en': en, 'notes': notes, 'ix': {i: ixm[i] for i in sorted(set(ids) | first_ids) if i in ixm}}
        out[f'split/ct-{kind}.js'] = '/* generated by scripts/split_data.py from data.js — do not edit */\nwindow.UI_CTX=' + dumps(c) + ';\n'
    out['split/detail.js'] = '/* generated by scripts/split_data.py from data.js — do not edit */\nwindow.UI_DETAIL=' + dumps(det) + ';\n'
    return out


I18N_EVAL = r"""
const vm=require('vm'),fs=require('fs');const w={};w.window=w;vm.createContext(w);
vm.runInContext(fs.readFileSync(process.argv[1],'utf8'),w);
process.stdout.write(JSON.stringify({i18n:w.UI_I18N,ct:w.UI_CT_ORDER||null,sec:w.UI_SEC_ORDER||null}));
"""


def build_i18n():
    r = subprocess.run(['node', '-e', I18N_EVAL, P('i18n.js')], capture_output=True, text=True, encoding='utf-8')
    if r.returncode:
        sys.exit('split_data: evaluating i18n.js failed\n' + r.stderr)
    o = json.loads(r.stdout)
    I = o['i18n']
    langs = I['langs']
    have = [l[0] for l in langs]
    if sorted(have) != sorted(LANGS):
        sys.exit(f'split_data: i18n.js langs {have} != {LANGS}')
    out = {}
    for L in LANGS:
        chain = [L] + (['en'] if L not in ('zh-CN', 'zh-TW') else []) + ['zh-CN']
        d = {}
        for c in reversed(chain):  # later (higher priority) overrides, null never wins (t() uses != null)
            for k, v in I.get(c, {}).items():
                if v is not None:
                    d[k] = v
        # keep the canonical key order of the locale itself first, then fallbacks (deterministic)
        keys = []
        seen = set()
        for c in chain:
            for k in I.get(c, {}):
                if k in d and k not in seen:
                    seen.add(k); keys.append(k)
        d = {k: d[k] for k in keys}
        js = ('/* generated by scripts/split_data.py from i18n.js — do not edit */\n'
              '(function(w){var I=w.UI_I18N=w.UI_I18N||{};I.langs=' + dumps(langs) + ';I[' + dumps(L) + ']=' + dumps(d) + ';')
        if o['ct'] is not None:
            js += 'w.UI_CT_ORDER=' + dumps(o['ct']) + ';'
        if o['sec'] is not None:
            js += 'w.UI_SEC_ORDER=' + dumps(o['sec']) + ';'
        js += '})(window);\n'
        out[f'split/i18n-{L}.js'] = js
    return out


def h8(b):
    return hashlib.sha256(b).hexdigest()[:10]


def version_map(out):
    v = {}
    v['first'] = h8(''.join(out[f'split/first-{L}.js'] for L in LANGS).encode())
    v['core'] = h8(out['split/core.js'].encode())
    v['detail'] = h8(out['split/detail.js'].encode())
    v['i18n'] = h8(''.join(out[f'split/i18n-{L}.js'] for L in LANGS).encode())
    cts = sorted(fn[9:-3] for fn in out if fn.startswith('split/ct-'))
    v['ctx'] = h8(''.join(out[f'split/ct-{k}.js'] for k in cts).encode())
    v['cts'] = ','.join(cts)
    for k, fn in (('media', 'media.js'), ('legal', 'legal.js'), ('notes', 'notes.js'), ('en', 'names_en.js'), ('orig', 'orig.js')):
        v[k] = h8(open(P(fn), 'rb').read())
    return v


def main():
    check = '--check' in sys.argv
    out = build()
    out.update(build_i18n())
    v = version_map(out)
    ip = P('index.html')
    html = open(ip, encoding='utf-8').read()
    if '/*UHV*/' not in html:
        sys.exit('split_data: index.html has no /*UHV*/ version map')
    new_html = re.sub(r'/\*UHV\*/.*?/\*/UHV\*/', '/*UHV*/' + dumps(v) + '/*/UHV*/', html, count=1, flags=re.S)
    stale = []
    for fn, s in out.items():
        cur = open(P(fn), encoding='utf-8').read() if os.path.exists(P(fn)) else None
        if cur != s:
            stale.append(fn)
            if not check:
                os.makedirs(os.path.dirname(P(fn)), exist_ok=True)
                open(P(fn), 'w', encoding='utf-8').write(s)
    if new_html != html:
        stale.append('index.html')
        if not check:
            open(ip, 'w', encoding='utf-8').write(new_html)
    sizes = {fn: len(s.encode()) for fn, s in out.items()}
    print('split_data:', 'stale' if stale else 'up to date', stale, '| versions', v, '| bytes first-en', sizes['split/first-en.js'],
          'core', sizes['split/core.js'], 'detail', sizes['split/detail.js'])
    if check and stale:
        sys.exit(1)


if __name__ == '__main__':
    main()
