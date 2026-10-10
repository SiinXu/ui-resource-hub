#!/usr/bin/env python3
"""notes_src/notes_i18n.json（按资源 id 存的 7 种语言说明，人工撰写）-> notes.js。中文说明来自 data.json。"""
import json, os
H = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(H,'data.json'), encoding='utf-8'))
o = json.load(open(os.path.join(H,'notes_src','notes_i18n.json'), encoding='utf-8'))
for lang, m in o['notes'].items():
    miss = [i['id'] for i in d['items'] if i['note'] and i['id'] not in m]
    if miss: print('缺少', lang, miss)
open(os.path.join(H,'notes.js'),'w',encoding='utf-8').write('window.UI_NOTES='+json.dumps(o,ensure_ascii=False)+';\n')
