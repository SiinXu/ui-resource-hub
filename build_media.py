#!/usr/bin/env python3
"""生成 media.js：每条资源的预览图、预览来源、能否 iframe 嵌入。
数据来自 _probe/probe.json（curl 检查 X-Frame-Options / CSP frame-ancestors）和 previews/ 目录。"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, 'data.json'), encoding='utf-8'))
probe = {r[0]: r for r in json.load(open(os.path.join(HERE, '_probe/probe.json')))}
SHOT = {'www-beautifului-dev','beautiful-ui-five-vercel-app','ai-sdk-dev-elements','openai-github-io-chatkit-js','ui-elevenlabs-io',
        'chatscope-io','tdesign-tencent-com-chat','www-hover-dev','motion-primitives-com'}
ALIAS = {'orbs-jakubantalik-com': 'live-orbs', 'metal-jakubantalik-com': 'live-metal'}
media = {}
for it in d['items']:
    rid = it['id']; m = {}
    name = ALIAS.get(rid, rid)
    if os.path.exists(os.path.join(HERE, 'previews', name + '.webp')):
        m['img'] = 'previews/' + name + '.webp'
        m['src'] = 'shot' if (rid in SHOT or rid in ALIAS) else 'og'
    p = probe.get(rid)
    if p:
        code, xfo, fa = p[1], p[2], p[3]
        ok = code.startswith('200') and not xfo and (not fa or all('*' == f.strip() for f in fa))
        if ok and rid not in ('ui-elevenlabs-io',): m['frame'] = 1
    if m: media[rid] = m
open(os.path.join(HERE, 'media.js'), 'w', encoding='utf-8').write('window.UI_MEDIA=' + json.dumps(media, ensure_ascii=False) + ';\n')
print(len(media), 'with media;', sum(1 for v in media.values() if 'img' in v), 'images;', sum(1 for v in media.values() if v.get('frame')), 'frameable')
