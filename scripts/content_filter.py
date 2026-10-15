"""Content policy for UI Hub auto-collection: rejects adult / NSFW / piracy / gambling items.
Rules live in data/denylist.json (repo-id/URL denylist + zh/en keywords). Used by daily_update.py
(before append) and hub_lib.append (defence in depth); purge() also removes already-stored hits."""
import json, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DENY = os.path.join(ROOT, 'data', 'denylist.json')

def _norm(u):
    u = (u or '').lower().split('#')[0].split('?')[0]
    return re.sub(r'^https?://(www\.)?', '', u).rstrip('/')

def rules():
    d = json.load(open(DENY, encoding='utf-8'))
    ids = {e['id'] for e in d.get('ids', [])}
    urls = {_norm(e['url']) for e in d.get('ids', []) if e.get('url')}
    kw = d.get('keywords', {})
    sub = [k.lower() for k in kw.get('substring', [])]
    # word-bounded: ascii letters/digits must not touch the match (works for zh too)
    word = [re.compile(r'(?<![a-z0-9])' + re.escape(k.lower()) + r'(?![a-z0-9])') for k in kw.get('word', [])]
    return ids, urls, sub, word

_R = None
def blocked(item, extra_text=''):
    """Return a reason string if the item violates the policy, else None.
    item: dict with id/name/url/note/noteEn/tags (+ optional 'topics'); extra_text: e.g. GitHub topics."""
    global _R
    if _R is None: _R = rules()
    ids, urls, sub, word = _R
    if item.get('id') in ids: return 'denylist id ' + item['id']
    if _norm(item.get('url')) in urls: return 'denylist url ' + item.get('url', '')
    hay = ' '.join(str(x) for x in [item.get('id', ''), item.get('name', ''), item.get('url', ''), item.get('note', ''),
                                     item.get('noteEn', ''), ' '.join(item.get('tags') or []), ' '.join(item.get('topics') or []), extra_text]).lower()
    for k in sub:
        if k in hay: return 'keyword ' + k
    for rx in word:
        m = rx.search(hay)
        if m: return 'keyword ' + m.group(0)
    return None

def purge():
    """Remove policy violations from data.json/data.js and notes_src/notes_i18n.json. Returns removed ids."""
    dj = os.path.join(ROOT, 'data.json')
    d = json.load(open(dj, encoding='utf-8'))
    bad = {i['id']: r for i in d['items'] if (r := blocked(i))}
    if not bad: return {}
    d['items'] = [i for i in d['items'] if i['id'] not in bad]; d['count'] = len(d['items'])
    json.dump(d, open(dj, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    open(os.path.join(ROOT, 'data.js'), 'w', encoding='utf-8').write('window.UI_DATA=' + json.dumps(d, ensure_ascii=False) + ';\n')
    nj = os.path.join(ROOT, 'notes_src', 'notes_i18n.json')
    if os.path.exists(nj):
        o = json.load(open(nj, encoding='utf-8'))
        for sec in o.values():
            if isinstance(sec, dict):
                for m in sec.values():
                    if isinstance(m, dict):
                        for k in bad: m.pop(k, None)
        json.dump(o, open(nj, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        open(os.path.join(ROOT, 'notes.js'), 'w', encoding='utf-8').write('window.UI_NOTES=' + json.dumps(o, ensure_ascii=False) + ';\n')
    return bad

if __name__ == '__main__':
    import sys
    d = json.load(open(os.path.join(ROOT, 'data.json'), encoding='utf-8'))
    hits = [(i['id'], i['name'], r) for i in d['items'] if (r := blocked(i))]
    for h in hits: print(*h, sep=' | ')
    print(len(hits), 'hits of', len(d['items']))
    if '--purge' in sys.argv: print('purged', purge())
