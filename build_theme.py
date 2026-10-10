"""v5: theme metadata for previews. Run after build_media.py.
- tone: 'l' / 'd' for every screenshot (mean luminance), so the UI can say which theme a single shot is.
- imgL/imgD: light+dark captures (prefers-color-scheme emulation) for key sites where the two differ.
  Raw captures: /workspace/cap/theme/raw/<id>-light.png|-dark.png ; outputs previews/theme/<id>-l.webp|-d.webp
Never tints a shot to fake the other theme."""
import json,os,sys
from PIL import Image,ImageStat
ROOT=sys.argv[1] if len(sys.argv)>1 else '.'
RAW='/workspace/cap/theme/raw'
SKIP={'lovable-dev'}  # captured a bot-check page, not the site
mp=os.path.join(ROOT,'media.js'); s=open(mp).read()
M=json.loads(s[s.index('=')+1:].rstrip().rstrip(';'))
def lum(path):
    im=Image.open(path).convert('L'); im.thumbnail((200,200)); return ImageStat.Stat(im).mean[0]
n=0
for k,v in M.items():
    v.pop('tone',None)
    p=os.path.join(ROOT,v.get('img',''))
    if v.get('img') and os.path.exists(p):
        L=lum(p); v['tone']='l' if L>=140 else ('d' if L<=95 else None)
        if v['tone'] is None: v.pop('tone')
dual=0; os.makedirs(os.path.join(ROOT,'previews/theme'),exist_ok=True)
for k,v in M.items():
    v.pop('imgL',None); v.pop('imgD',None)
    a,b=os.path.join(RAW,k+'-light.png'),os.path.join(RAW,k+'-dark.png')
    if k in SKIP or not(os.path.exists(a) and os.path.exists(b)): continue
    la,lb=lum(a),lum(b)
    if la-lb<45 or la<120 or lb>110: continue   # not a real light/dark pair
    for src,suf in ((a,'l'),(b,'d')):
        im=Image.open(src).convert('RGB').resize((800,500),Image.LANCZOS)
        im.save(os.path.join(ROOT,'previews/theme',f'{k}-{suf}.webp'),quality=82)
    v['imgL']=f'previews/theme/{k}-l.webp'; v['imgD']=f'previews/theme/{k}-d.webp'; dual+=1
open(mp,'w').write('window.UI_MEDIA='+json.dumps(M,ensure_ascii=False,separators=(',',':'))+';\n')
from collections import Counter
print('tone',Counter(v.get('tone') for v in M.values()),'dual',dual)
