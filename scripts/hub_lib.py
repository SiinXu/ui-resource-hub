"""Append-only helpers for data.json / data.js. Never deletes items."""
import json, os, re, datetime
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DJ = os.path.join(ROOT, 'data.json')

def norm(u):
    u = u.lower().split('#')[0].split('?')[0]
    u = re.sub(r'^https?://(www\.)?', '', u)
    return u.rstrip('/')

def load():
    return json.load(open(DJ, encoding='utf-8'))

def append(new_items, stamp=None):
    d = load()
    have_u = {norm(i['url']) for i in d['items'] if i.get('url')}
    have_id = {i['id'] for i in d['items']}
    added = []
    from content_filter import blocked
    for it in new_items:
        if blocked(it): continue   # content policy: data/denylist.json
        if norm(it['url']) in have_u or it['id'] in have_id: continue
        it.setdefault('added', datetime.date.today().isoformat())
        d['items'].append(it); have_u.add(norm(it['url'])); have_id.add(it['id']); added.append(it)
    d['count'] = len(d['items'])
    d['generated'] = stamp or datetime.date.today().isoformat()
    d['updatedAt'] = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%MZ')
    json.dump(d, open(DJ, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    open(os.path.join(ROOT, 'data.js'), 'w', encoding='utf-8').write('window.UI_DATA=' + json.dumps(d, ensure_ascii=False) + ';\n')
    return added

def lib_item(id, name, url, note, ct, fw, pricing='free', tags=(), rt=('component-library',), vs=('minimal',), source='', section='开源组件库 · 2026-10 补全', type='library'):
    return dict(id=id, name=name, url=url, note=note, type=type, section=section, sectionTitle='开源组件库与组件注册表 · 补全',
                sectionDesc='', source=source, pricing=pricing, tags=list(fw) + list(tags), ct=list(ct), rt=list(rt), vs=list(vs))
