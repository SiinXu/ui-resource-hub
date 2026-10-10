#!/usr/bin/env python3
"""从 /workspace/ui/gen.py 导入资源清单，生成 data.json 和 data.js（data.js 让 file:// 直接打开也能用）。
用法：python3 build.py [gen.py 路径]"""
import json, re, sys, hashlib, os
SRC = sys.argv[1] if len(sys.argv) > 1 else '/workspace/ui/gen.py'
HERE = os.path.dirname(os.path.abspath(__file__))
code = open(SRC, encoding='utf-8').read()
code = code[:code.index('\nh=[')]          # 只取数据部分 S=[...]
ns = {}; exec(code, ns); S = ns['S']

# ---- 分类映射 ----
SEC_TYPE = {1:'component',2:'skill',3:'component',4:'component',5:'component',6:'inspiration',7:'template',8:'generator',9:'skill'}
EFFECT = {'Transitions','Thinking Orbs','Motion+','Paper Shaders 全集','Rive','ShaderGradient','NEAT','Liquid Glass React',
  'Codrops','Libraries.dev（你订阅了 Pro）','Paper Shaders 液态金属','React Bits 金属漆','Canvas UI','Border Beam','Liquid Metal'}
OVERRIDE = {'Unicorn Studio':'generator','UI 问题盘点可视化（@Linmiv）':'guide'}
SEC_SOURCE = {1:'@lumxss',2:'@kail_designs',9:'ui-skills.com'}
SEC_SHORT = {1:'最初推荐',2:'设计 Skills',3:'海外 AI 组件',4:'国内大厂 AI 组件',5:'动效与通用组件',6:'AI 产品灵感',7:'开源 AI 聊天应用',8:'AI 生成界面',9:'更多 UI Skills'}

TAG_RULES = [
 ('AI 聊天', r'聊天|对话|Chat|chat|助手|Copilot'), ('语音', r'语音|声波|Voice|LiveKit'),
 ('动效', r'动效|动画|过渡|Motion|animat|Transition|spring|Lottie'), ('WebGL/着色器', r'着色器|WebGL|Shader|shader|GLSL|3D'),
 ('shadcn', r'shadcn'), ('React', r'React'), ('Python', r'Python'), ('中文', r'中文|蚂蚁|腾讯|Lobe'),
 ('落地页', r'落地页|Land'), ('移动端', r'移动端|App|手机'), ('配色', r'配色|颜色|color'), ('字体', r'字体|typograph'),
 ('无障碍', r'无障碍|accessib|对比度'), ('原型', r'原型|线框|设计稿'), ('开源', r'开源|github\.com'),
 ('液态金属', r'金属|metal|Metal'), ('背景', r'背景|渐变|Gradient'), ('审查走查', r'审查|走查|review|critique|打分|反馈'),
 ('去 AI 味', r'AI 味|套路|千篇一律|高级感|taste'), ('智能体', r'智能体|Agent|agent'),
]
def pricing(name, note):
    t = name + note
    if 'Pro' in t and '免费' in t: return 'freemium'
    if '付费' in t or '买断' in t: return 'paid'
    if '免费' in t or '开源' in t or 'github.com' in t: return 'free'
    return 'unknown'

items = []; seen = {}
for si,(title,desc,lst) in enumerate(S, 1):
    for name,url,note in lst:
        t = OVERRIDE.get(name) or ('effect' if name in EFFECT else SEC_TYPE[si])
        m = re.findall(r'@[A-Za-z0-9_]+', title+name+note)
        src = m[0] if m else SEC_SOURCE.get(si, '')
        hay = name+' '+note+' '+url
        tags = [tg for tg,rx in TAG_RULES if re.search(rx, hay)]
        rid = re.sub(r'[^a-z0-9]+','-', (url.split('//')[1]).lower()).strip('-')[:60]
        if rid in seen: rid += '-' + hashlib.md5(name.encode()).hexdigest()[:4]
        seen[rid] = 1
        items.append(dict(id=rid, name=name, url=url, note=note, type=t, section=SEC_SHORT[si],
                          sectionTitle=title, sectionDesc=desc, source=src, pricing=pricing(name,note), tags=tags))

byname = {i['name']: i['id'] for i in items}
guides = json.load(open(os.path.join(HERE,'guides.src.json'), encoding='utf-8'))
for g in guides:
    for r in g['picks']:
        if r['name'] not in byname: sys.exit(f'指南引用了清单里不存在的资源: {r["name"]}')
        r['id'] = byname[r['name']]
data = dict(generated='2026-10-10', count=len(items), items=items, guides=guides)
json.dump(data, open(os.path.join(HERE,'data.json'),'w',encoding='utf-8'), ensure_ascii=False, indent=1)
open(os.path.join(HERE,'data.js'),'w',encoding='utf-8').write('window.UI_DATA=' + json.dumps(data, ensure_ascii=False) + ';\n')
from collections import Counter
print(len(items), dict(Counter(i['type'] for i in items)), dict(Counter(i['pricing'] for i in items)))
