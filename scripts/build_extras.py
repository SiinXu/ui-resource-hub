#!/usr/bin/env python3
"""Generates blog/, agents/, llms.txt, llms-full.txt, AGENTS.md, api/*.json, .well-known/agent.json, sitemap.xml, robots.txt
and injects SEO head + nav into index.html. Idempotent; safe to run daily."""
import json, os, re, sys, html, datetime, glob
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'blog_src'))
from posts import POSTS
from images import IMAGES
BASE = 'https://siinxu.github.io/ui-resource-hub/'
LANGS = [('zh-Hans','简体中文','zh'),('zh-Hant','繁體中文','zht'),('en','English','en'),('ja','日本語','ja'),('ko','한국어','ko'),('ms','Bahasa Melayu','ms'),('vi','Tiếng Việt','vi'),('fr','Français','fr'),('es','Español','es'),('de','Deutsch','de')]
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
from content_filter import purge as _policy_purge
_pp = _policy_purge()   # content policy (data/denylist.json): never publish adult/NSFW/piracy/gambling items
if _pp: print('policy purge', _pp)
D = json.load(open(os.path.join(ROOT,'data.json'), encoding='utf-8'))
ITEMS = D['items']; UPD_ISO = re.sub(r'T(\d\d:\d\d)Z$', r'T\1:00Z', D.get('updatedAt') or D['generated']); UPD = (D.get('updatedAt') or D['generated']).replace('T',' ').replace('Z',' UTC'); TODAY = D['generated']
E = html.escape
def w(path, s):
    p = os.path.join(ROOT, path); os.makedirs(os.path.dirname(p), exist_ok=True); open(p,'w',encoding='utf-8').write(s)

# ---------- UI strings for extras pages (10 langs) ----------
U = {
 'blog_title': dict(zh='AI 设计技巧博客',zht='AI 設計技巧部落格',en='AI Design Techniques Blog',ja='AIデザインテクニック ブログ',ko='AI 디자인 기법 블로그',ms='Blog Teknik Reka Bentuk AI',vi='Blog kỹ thuật thiết kế AI',fr='Blog des techniques de design IA',es='Blog de técnicas de diseño con IA',de='Blog: KI-Designtechniken'),
 'blog_lede': dict(zh='原创分析：综合多方公开资料，用我们自己的话重写，并给出观点与清单。每篇文末列出全部引用来源。',zht='原創分析：綜合多方公開資料，用我們自己的話重寫，並給出觀點與清單。每篇文末列出全部引用來源。',en='Original analysis: we synthesise multiple public sources in our own words and add our take and checklists. Every post ends with full references.',ja='オリジナル分析：複数の公開資料を独自の言葉でまとめ、見解とチェックリストを加えています。各記事末尾に出典を掲載。',ko='독자적 분석: 여러 공개 자료를 우리 말로 종합하고 견해와 체크리스트를 더했습니다. 모든 글 끝에 출처를 밝힙니다.',ms='Analisis asli: kami sintesis pelbagai sumber awam dengan kata-kata sendiri. Setiap artikel disertakan rujukan penuh.',vi='Phân tích gốc: tổng hợp nhiều nguồn công khai bằng lời của chúng tôi, kèm quan điểm và checklist. Mỗi bài đều ghi nguồn đầy đủ.',fr='Analyses originales : nous synthétisons plusieurs sources publiques avec nos mots. Chaque article cite toutes ses références.',es='Análisis original: sintetizamos varias fuentes públicas con nuestras palabras. Cada artículo cita todas sus referencias.',de='Eigene Analysen: Wir fassen mehrere öffentliche Quellen in eigenen Worten zusammen. Jeder Beitrag nennt alle Quellen.'),
 'refs': dict(zh='引用来源',zht='引用來源',en='References',ja='参考文献',ko='참고 자료',ms='Rujukan',vi='Nguồn tham khảo',fr='Références',es='Referencias',de='Quellen'),
 'body_note': dict(zh='',zht='正文以簡體中文顯示。',en='',ja='本文は英語で表示しています。',ko='본문은 영어로 표시됩니다.',ms='Kandungan dipaparkan dalam bahasa Inggeris.',vi='Nội dung hiển thị bằng tiếng Anh.',fr='Le corps de l’article est en anglais.',es='El cuerpo del artículo está en inglés.',de='Der Beitragstext ist auf Englisch.'),
 'back': dict(zh='返回博客',zht='返回部落格',en='Back to blog',ja='ブログへ戻る',ko='블로그로',ms='Kembali ke blog',vi='Về blog',fr='Retour au blog',es='Volver al blog',de='Zurück zum Blog'),
 'home': dict(zh='资源',zht='資源',en='Resources',ja='リソース',ko='리소스',ms='Sumber',vi='Tài nguyên',fr='Ressources',es='Recursos',de='Ressourcen'),
 'agents': dict(zh='给 Agent',zht='給 Agent',en='For agents',ja='エージェント向け',ko='에이전트용',ms='Untuk ejen',vi='Cho Agent',fr='Pour agents',es='Para agentes',de='Für Agents'),
 'blog': dict(zh='博客',zht='部落格',en='Blog',ja='ブログ',ko='블로그',ms='Blog',vi='Blog',fr='Blog',es='Blog',de='Blog'),
 'upd': dict(zh='数据更新于',zht='資料更新於',en='Data updated',ja='データ更新',ko='데이터 업데이트',ms='Data dikemas kini',vi='Dữ liệu cập nhật',fr='Données mises à jour',es='Datos actualizados',de='Daten aktualisiert'),
 'ag_title': dict(zh='给 AI Agent 的使用指南',zht='給 AI Agent 的使用指南',en='Guide for AI agents',ja='AIエージェント向けガイド',ko='AI 에이전트 가이드',ms='Panduan untuk ejen AI',vi='Hướng dẫn cho AI agent',fr='Guide pour agents IA',es='Guía para agentes de IA',de='Leitfaden für KI-Agents'),
 'ag_lede': dict(zh='把本站交给你的 AI 助手：它可以读取机器可读索引，按风格和类型挑组件，复制代码和 Prompt，并按设计 skill 的流程做出好看的界面。',zht='把本站交給你的 AI 助手：它可以讀取機器可讀索引，按風格和類型挑元件，複製程式碼和 Prompt，並按設計 skill 的流程做出好看的介面。',en='Hand this site to your AI assistant: it can read the machine-readable index, pick components by style and type, copy code and prompts, and follow design skills to build good-looking UIs.',ja='このサイトをAIアシスタントに渡すと、機械可読インデックスを読み、スタイルと種類でコンポーネントを選び、コードとプロンプトをコピーし、デザインスキルに沿って美しいUIを作れます。',ko='이 사이트를 AI 어시스턴트에게 주면 기계 판독 인덱스를 읽고, 스타일·유형별로 컴포넌트를 고르고, 코드와 프롬프트를 복사하며, 디자인 스킬에 따라 UI를 만들 수 있습니다.',ms='Serahkan laman ini kepada pembantu AI anda: ia boleh membaca indeks mesin, memilih komponen mengikut gaya dan jenis, menyalin kod dan prompt, serta mengikut kemahiran reka bentuk.',vi='Đưa trang này cho trợ lý AI: nó đọc chỉ mục máy, chọn component theo phong cách và loại, sao chép code và prompt, rồi làm theo skill thiết kế.',fr='Confiez ce site à votre assistant IA : il lit l’index machine, choisit des composants par style et type, copie code et prompts, et suit les skills de design.',es='Dale este sitio a tu asistente de IA: lee el índice legible por máquina, elige componentes por estilo y tipo, copia código y prompts y sigue los skills de diseño.',de='Geben Sie diese Seite Ihrem KI-Assistenten: Er liest den maschinenlesbaren Index, wählt Komponenten nach Stil und Typ, kopiert Code und Prompts und folgt Design-Skills.'),
}
U['kb']=dict(zh='百科',zht='百科',en='Encyclopedia',ja='百科',ko='백과',ms='Ensiklopedia',vi='Bách khoa',fr='Encyclopédie',es='Enciclopedia',de='Enzyklopädie')
def L(k, code): return U[k].get(code) or U[k]['en']

CSS = """@font-face{font-family:Geist;src:url(%(r)sfonts/geist.woff2) format('woff2');font-weight:100 900;font-display:swap}
@font-face{font-family:'Instrument Serif';src:url(%(r)sfonts/instrument-serif.woff2) format('woff2');font-display:swap}
@font-face{font-family:'Instrument Serif';font-style:italic;src:url(%(r)sfonts/instrument-serif-italic.woff2) format('woff2');font-display:swap}
:root{--sans:Geist,"PingFang SC","Hiragino Sans","Apple SD Gothic Neo","Noto Sans CJK SC","Microsoft YaHei",system-ui,sans-serif;--serif:"Instrument Serif","Songti SC","Noto Serif SC",Georgia,serif;--mono:ui-monospace,SFMono-Regular,Menlo,monospace;--max:1120px}
[data-theme=dark]{color-scheme:dark;--bg:#06070b;--surf:#0d0f15;--mat:#10131a;--ink:#f3f5fb;--ink2:#a6adbf;--ink3:#687086;--acc:#67e8f9;--g1:#67e8f9;--g2:#a5b4fc;--g3:#f9a8d4;--line:rgba(255,255,255,.08);--line2:rgba(255,255,255,.14);--hdr:rgba(6,7,11,.66);--glow1:rgba(56,189,248,.18);--glow2:rgba(129,140,248,.16)}
[data-theme=light]{color-scheme:light;--bg:#f5f6fa;--surf:#fff;--mat:#eef0f6;--ink:#0a0c14;--ink2:#4a5164;--ink3:#878da0;--acc:#2563eb;--g1:#06b6d4;--g2:#6366f1;--g3:#ec4899;--line:rgba(10,12,20,.08);--line2:rgba(10,12,20,.14);--hdr:rgba(245,246,250,.72);--glow1:rgba(6,182,212,.12);--glow2:rgba(99,102,241,.12)}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.65 var(--sans);-webkit-font-smoothing:antialiased}
body:before{content:"";position:fixed;inset:-20% -10% auto;height:70vh;z-index:-1;background:radial-gradient(40% 50% at 20% 20%,var(--glow1),transparent 70%),radial-gradient(40% 50% at 80% 10%,var(--glow2),transparent 70%);pointer-events:none}
a{color:inherit}.wrap{max-width:var(--max);margin:0 auto;padding:0 20px}@media(min-width:900px){.wrap{padding:0 40px}}
.top{position:sticky;top:0;z-index:9;background:var(--hdr);backdrop-filter:blur(14px) saturate(1.4);-webkit-backdrop-filter:blur(14px) saturate(1.4);border-bottom:1px solid var(--line)}
.bar{display:flex;align-items:center;gap:14px;height:58px}.logo{font-weight:600;text-decoration:none;display:flex;gap:8px;align-items:center;letter-spacing:-.01em}
.logo i{width:18px;height:18px;border-radius:5px;background:linear-gradient(135deg,var(--g1),var(--g2));display:inline-block}
nav.tb{display:flex;gap:2px;margin-left:8px}nav.tb a{padding:6px 10px;border-radius:8px;text-decoration:none;color:var(--ink2);font-size:13.5px}nav.tb a:hover,nav.tb a.on{color:var(--ink);background:var(--mat)}
.sp{flex:1}select,button.th{font:inherit;font-size:13px;color:var(--ink);background:var(--surf);border:1px solid var(--line2);border-radius:8px;padding:5px 8px;cursor:pointer}
.hero{padding:64px 0 28px}.eb{font:500 12px/1 var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--ink3);display:flex;gap:8px;align-items:center}.eb:before{content:"";width:6px;height:6px;border-radius:9px;background:var(--acc);box-shadow:0 0 12px var(--acc)}
h1{font:400 clamp(36px,6vw,64px)/1.02 var(--serif);letter-spacing:-.02em;margin:14px 0 14px;max-width:18ch}h1 em{background:linear-gradient(100deg,var(--g1),var(--g2),var(--g3));-webkit-background-clip:text;background-clip:text;color:transparent}
.lede{color:var(--ink2);max-width:62ch;font-size:16.5px;margin:0}
.posts{display:grid;gap:14px;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));padding:20px 0 60px}
.pc{position:relative;display:flex;flex-direction:column;overflow:hidden;padding:0;border-radius:16px;background:var(--surf);border:1px solid var(--line);text-decoration:none;transition:border-color .2s,transform .2s}
.pc:hover{border-color:var(--line2);transform:translateY(-2px)}.pb{display:flex;flex-direction:column;gap:8px;padding:16px 18px 18px;flex:1}.cv{width:100%;height:auto;flex:none;aspect-ratio:1200/630;object-fit:cover;border-bottom:1px solid var(--line);background:#07080d}
@media(min-width:900px){.pc:first-child{grid-column:1/-1;flex-direction:row;align-items:center}.pc:first-child .cv{width:58%;height:auto;flex:none;border-bottom:0;border-right:1px solid var(--line)}.pc:first-child .pb{justify-content:center;padding:28px}.pc:first-child h2{font-size:34px}}
.posts{grid-template-columns:repeat(auto-fill,minmax(290px,1fr))!important}
figure{margin:26px 0}figure img{width:100%;height:auto;border-radius:14px;border:1px solid var(--line2);background:var(--mat);display:block}figcaption{font-size:12.5px;color:var(--ink3);margin-top:8px;line-height:1.5}figcaption a{color:var(--acc)}.hc{margin:22px 0 8px}
.pc .no{font:500 12px var(--mono);color:var(--ink3)}.pc h2{font:400 23px/1.15 var(--serif);margin:0;letter-spacing:-.01em}.pc p{margin:0;color:var(--ink2);font-size:14px}
.tg{display:flex;gap:6px;flex-wrap:wrap}.tg span{font:500 11px var(--mono);color:var(--ink3);border:1px solid var(--line);padding:2px 7px;border-radius:99px}
article{max-width:720px;margin:0 auto;padding:48px 20px 72px}article h1{max-width:none;font-size:clamp(32px,5vw,50px)}
article h2{font:400 26px/1.2 var(--serif);margin:36px 0 10px}article p,article li{color:var(--ink2)}article strong{color:var(--ink)}
pre{background:var(--mat);border:1px solid var(--line);border-radius:12px;padding:14px 16px;overflow:auto;font:12.5px/1.6 var(--mono)}code{font-family:var(--mono);font-size:.9em}
.refs{margin-top:40px;padding-top:18px;border-top:1px solid var(--line)}.refs li{margin:4px 0}.refs a{color:var(--acc)}
.meta{font:500 12px var(--mono);color:var(--ink3);margin:0 0 6px}.meta a{display:inline-block;padding:7px 0}@media(max-width:600px){.tg span{padding:5px 9px}}.note{font-size:13px;color:var(--ink3)}
.grid2{display:grid;gap:14px;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));margin:18px 0}
.box{padding:20px;border-radius:16px;background:var(--surf);border:1px solid var(--line)}.box h3{margin:0 0 6px;font-size:16px}.box p{margin:0;color:var(--ink2);font-size:14px}
.box code,.sec code{background:var(--mat);padding:1px 6px;border-radius:6px}.sec{padding:8px 0 30px}.sec h2{font:400 30px var(--serif);margin:26px 0 8px}
details{border-bottom:1px solid var(--line);padding:12px 0}summary{cursor:pointer;font-weight:500}details p{color:var(--ink2);margin:8px 0 0}
.foot{border-top:1px solid var(--line);padding:24px 0 40px;color:var(--ink3);font-size:13px}
[data-l]{display:none}
@media(max-width:600px){.bar{gap:6px}nav.tb{overflow-x:auto;min-width:0;flex:1;scrollbar-width:none}.sp{display:none}select{max-width:70px!important}.logo{font-size:0;gap:0}nav.tb{margin-left:0}nav.tb a{padding:6px 7px;font-size:13px;white-space:nowrap}select{max-width:92px}.hero{padding:40px 0 20px}}"""

def head(title, desc, path, extra_ld, root, img='og.png'):
    url = BASE + path
    alt = ''.join(f'<link rel="alternate" hreflang="{c}" href="{url}?lang={c}">' for c,_,_ in LANGS) + f'<link rel="alternate" hreflang="x-default" href="{url}">'
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}"><link rel="canonical" href="{url}">{alt}
<meta property="og:type" content="{'article' if 'blog/' in path and path!='blog/' else 'website'}"><meta property="og:site_name" content="UI Hub"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{BASE}{img}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{E(title)}"><meta name="twitter:description" content="{E(desc)}"><meta name="twitter:image" content="{BASE}{img}">
<link rel="alternate" type="text/plain" title="llms.txt" href="{BASE}llms.txt">
<script>try{{document.documentElement.dataset.theme=localStorage.getItem('uihub.theme5')||(matchMedia('(prefers-color-scheme: light)').matches?'light':'dark')}}catch(e){{document.documentElement.dataset.theme='dark'}}</script>
<style>{CSS.replace('%(r)s', root)}</style>
<script type="application/ld+json">{json.dumps(extra_ld, ensure_ascii=False)}</script></head>"""

def ml(key_or_dict, tag='span'):
    d = U[key_or_dict] if isinstance(key_or_dict,str) else key_or_dict
    return ''.join(f'<{tag} data-l="{c}">{E(d.get(k) or d["en"])}</{tag}>' for c,_,k in LANGS)

def topbar(root, on):
    opts = ''.join(f'<option value="{c}">{n}</option>' for c,n,_ in LANGS)
    def a(href, key, v): return f'<a href="{root}{href}"{" class=on" if on==v else ""}>{ml(key)}</a>'
    return f"""<header class="top"><div class="bar wrap"><a class="logo" href="{root}"><i></i>UI Hub</a><nav class="tb">{a('','home','home')}{a('kb/','kb','kb')}{a('blog/','blog','blog')}{a('agents/','agents','agents')}</nav><span class="sp"></span>
<select id="ls" aria-label="Language">{opts}</select><button class="th" id="th" aria-label="Theme">◐</button></div></header>"""

SCRIPT = """<script>(function(){var M={'zh-cn':'zh-Hans','zh-sg':'zh-Hans','zh-tw':'zh-Hant','zh-hk':'zh-Hant','zh-mo':'zh-Hant'},A=['zh-Hans','zh-Hant','en','ja','ko','ms','vi','fr','es','de'],APP={'zh-Hans':'zh-CN','zh-Hant':'zh-TW'};
function pick(){var q=(location.search.match(/[?&]lang=([\\w-]+)/)||[])[1];if(q&&A.indexOf(q)>=0)return q;try{var s=localStorage.getItem('uihub.lang');if(s){s={'zh-CN':'zh-Hans','zh-TW':'zh-Hant'}[s]||s;if(A.indexOf(s)>=0)return s}}catch(e){}
var n=(navigator.language||'en').toLowerCase();if(M[n])return M[n];if(/^zh-hant/.test(n))return 'zh-Hant';if(n.slice(0,2)==='zh')return 'zh-Hans';var b=n.slice(0,2);return A.indexOf(b)>=0?b:'en'}
function set(l){document.documentElement.lang=l;var st=document.getElementById('lst');if(!st){st=document.createElement('style');st.id='lst';document.head.appendChild(st)}st.textContent='[data-l="'+l+'"]{display:revert}';document.getElementById('ls').value=l;try{localStorage.setItem('uihub.lang',APP[l]||l)}catch(e){}}
function lt(){var L=document.documentElement.lang,loc=APP[L]||L;document.querySelectorAll('time.lt').forEach(function(t){var d=new Date(t.getAttribute('datetime'));if(isNaN(d))return;try{t.textContent=d.toLocaleString(loc,{year:'numeric',month:'short',day:'numeric',hour:'2-digit',minute:'2-digit',timeZoneName:'short'})}catch(e){}})}
set(pick());lt();document.getElementById('ls').onchange=function(){set(this.value);lt();document.dispatchEvent(new Event('uihub:lang'))};
document.getElementById('th').onclick=function(){var r=document.documentElement,n=r.dataset.theme==='dark'?'light':'dark';r.dataset.theme=n;try{localStorage.setItem('uihub.theme5',n)}catch(e){}}})();</script>"""

def foot(root):
    return f'<footer class="foot wrap">{ml("upd")} <time class="lt" datetime="{E(UPD_ISO)}">{E(UPD)}</time> · <a href="{root}llms.txt">llms.txt</a> · <a href="{root}api/resources.json">API</a> · <a href="{root}sitemap.xml">sitemap</a></footer>'

try: IMG_SIZES = json.load(open(os.path.join(ROOT,'blog_src','img_sizes.json')))
except Exception: IMG_SIZES = {}
ORG = {'@type':'Organization','name':'UI Hub','url':BASE}
def fig(slug, n, im, k, root):
    zh = k in ('zh','zht'); alt = im['alt']['zh' if zh else 'en']; src = f'{root}blog/img/{slug}-{n}.webp'
    if im['type']=='shot':
        host = im['url'].split('/')[2]
        cap = (f'截图：{E(im["site"])}（<a href="{E(im["url"])}" rel="noopener" target="_blank">{E(host)}</a>），2026-10-14 截取，版权归原站所有' if zh else
               f'Screenshot: {E(im["site"])} (<a href="{E(im["url"])}" rel="noopener" target="_blank">{E(host)}</a>), captured 2026-10-14. © the original site.')
    else:
        cap = ('示意图：UI Hub 原创，CC BY 4.0' if zh else 'Diagram: original by UI Hub, CC BY 4.0')
    iw, ih = IMG_SIZES.get(f'{slug}-{n}') or (None, None)
    if not iw:
        try:
            from PIL import Image as _I; iw, ih = _I.open(os.path.join(ROOT,'blog','img',f'{slug}-{n}.webp')).size
        except Exception: iw, ih = 1200, 675
    return f'<figure><img src="{src}" alt="{E(alt)}" loading="lazy" decoding="async" width="{iw}" height="{ih}"><figcaption>{E(alt)} · {cap}</figcaption></figure>'
def with_figs(body, slug, k, root):
    ims = IMAGES[slug]['inline']; F = [fig(slug, i+1, im, k, root) for i, im in enumerate(ims)]
    a = body.index('</p>')+4; body = body[:a]+F[0]+body[a:]
    m = min([x for x in (body.find(t, a+len(F[0])) for t in ('</ol>','</ul>','</pre>')) if x>0]); m = body.index('>', m)+1
    body = body[:m]+F[1]+body[m:]
    if len(F)>2:
        l = body.rfind('<h2>'); l = l if l>m else len(body); body = body[:l]+F[2]+body[l:]
    return body
# ---------- blog (v2, see blog_v2.py) ----------
import blog_v2; blog_v2.build(globals())

# ---------- skills ----------
SK = '/workspace/web-bot-skills'
DESIGN = ['frontend-design','taste-skill','impeccable','emil-design-eng','redesign-skill','baseline-ui','web-design-guidelines','accessibility','web-quality-audit','performance','composition-patterns','react-best-practices','iterate-until-verified','playwright-cli','webapp-testing']
UPSTREAM = {'taste-skill':'https://github.com/Leonxlnx/taste-skill','impeccable':'https://github.com/pbakaus/impeccable','frontend-design':'https://github.com/anthropics/skills','webapp-testing':'https://github.com/anthropics/skills','mcp-builder':'https://github.com/anthropics/skills'}
skills_p = os.path.join(ROOT,'blog_src','skills.json')
if os.path.isdir(SK):
    skills = []
    for f in sorted(glob.glob(SK+'/*/SKILL.md')):
        folder = f.split('/')[-2]; t = open(f,encoding='utf-8').read()
        m = re.search(r'^description:\s*(.+)$', t, re.M); desc = (m.group(1).strip().strip('"') if m else '')
        if not desc or desc in ('|','>'):
            m2 = re.search(r'^description:\s*[|>]-?\s*\n((?:\s+.+\n)+)', t, re.M); desc = ' '.join(m2.group(1).split()) if m2 else ''
        cat = 'design' if folder in DESIGN[:9] else ('engineering-ui' if folder in DESIGN else 'engineering')
        skills.append(dict(id=folder, description=desc[:400], category=cat, upstream=UPSTREAM.get(folder)))
    json.dump(skills, open(skills_p,'w'), ensure_ascii=False, indent=1)
skills = json.load(open(skills_p))
hub_skills = [dict(id=i['id'],name=i['name'],url=i['url'],note=i.get('noteEn') or i['note']) for i in ITEMS if i['type']=='skill']

# ---------- api ----------
def slim(i): 
    o = {k:i[k] for k in ('id','name','url','type','pricing','tags','ct','vs','rt','section','libName','kind','page','added') if i.get(k) not in (None,'',[])}
    o['note'] = i.get('noteEn') or i['note']
    if i.get('noteEn'): o['note_zh'] = i['note']
    for k in ('gold','why','flag','xsrc','source'):
        if i.get(k): o[k] = i[k]
    return o
w('api/resources.json', json.dumps({'name':'UI Hub resources','updated':UPD,'count':len(ITEMS),'license_note':'Links and metadata only; each resource keeps its own license. Preview images © original sites.',
   'fields':{'type':'library|component|style|skill|effect|template|generator|inspiration|system|spec|tool|tutorial|collection|guide','ct':'component kind, e.g. button,input,dialog,chart,table,chat,motion,background,layout','vs':'visual style, e.g. minimal,enterprise,material,soft,playful,motion,dark-tech,gradient,3d,apple,editorial,brutalist,glass','pricing':'free|freemium|paid|unknown','gold':'true = curated 精选 tier (start here); why = reason','flag':'quality flags: blank-preview | dup-preview (avoid as visual reference)','xsrc':'X/Twitter source post, author and engagement'},
   'items':[slim(i) for i in ITEMS]}, ensure_ascii=False, separators=(',',':')))
w('api/skills.json', json.dumps({'updated':UPD,'workflow':['Read the brief and pick ONE direction skill (frontend-design or taste-skill)','Search api/resources.json for components matching style (vs) and kind (ct)','Build with emil-design-eng for motion/interaction details','Audit with impeccable + baseline-ui + web-design-guidelines + accessibility','Verify in a real browser (playwright-cli / webapp-testing), light+dark, mobile'],
   'agent_skills':skills,'hub_skill_entries':hub_skills}, ensure_ascii=False, indent=1))
w('.well-known/agent.json', json.dumps({'name':'UI Hub','description':'Curated directory of UI component libraries, component style demos, design skills and AI design techniques.','url':BASE,
   'documentation':BASE+'agents/','llms_txt':BASE+'llms.txt','llms_full_txt':BASE+'llms-full.txt','agents_md':BASE+'AGENTS.md',
   'endpoints':{'resources':BASE+'api/resources.json','skills':BASE+'api/skills.json','sitemap':BASE+'sitemap.xml'},'updated':UPD,'auth':'none','rate_limit':'static files, be polite'}, indent=1))

# ---------- llms.txt / AGENTS.md ----------
from collections import Counter
tc = Counter(i['type'] for i in ITEMS)
libs = [i for i in ITEMS if i['type']=='library']
FAQ = [('What is UI Hub?','A free, curated directory of %d public UI resources: %d component libraries, %d component style demos with light/dark screenshots, %d design skills for AI agents, plus effects, templates, specs and tutorials. It links to original sites and never hosts paid source code.'%(len(ITEMS),tc['library'],tc['style'],tc['skill'])),
 ('How do I find a component in a given style?','Load %sapi/resources.json and filter by ct (component kind, e.g. "dialog") and vs (visual style, e.g. "minimal" or "motion"). type="style" entries are concrete component demos with a libName and page URL; type="library" entries are whole libraries with install info on the site.'%BASE),
 ('Which skills should an agent use for good UI?','One direction skill (frontend-design or taste-skill), emil-design-eng for motion and interaction polish, then impeccable, baseline-ui, web-design-guidelines and accessibility as an audit pass. See %sapi/skills.json.'%BASE),
 ('Can I copy the code?','Open-source libraries can be used under their own licenses (MIT, Apache-2.0 etc.); the card shows the original link. Paid tiers (marked paid/freemium) must be bought from the original vendor.'),
 ('How often is it updated?','Daily via a GitHub Actions job that adds new UI repositories and tools from GitHub, awesome-shadcn-ui and Hacker News. Nothing is deleted. Last update: %s.'%UPD)]
blog_lines = '\n'.join(f'- [{p["t"]["en"]}]({BASE}blog/{p["slug"]}/): {p["s"]["en"]}' for p in POSTS)
llms = f"""# UI Hub

> Curated, multilingual directory of {len(ITEMS)} public UI resources (component libraries, component style demos, effects, design systems, design skills for AI agents) plus original blog analysis of AI design techniques. Data updated {UPD}.

Use the JSON endpoints, not the SPA, when acting as an agent. Every entry links to its original site; licenses belong to the original authors.

## Design encyclopedia (query this first)
- [Encyclopedia]({BASE}kb/): skills (full SKILL.md where licensed), design specs (spacing, typography, colour, motion, accessibility, dark mode, mobile), house style & lessons, blog notes
- [KB JSON]({BASE}api/kb.json): every entry with type, tags, url, raw .md URL and full markdown
- [Search index]({BASE}api/search-index.json): kb entries + all resources/components, fields t,k,u,r,d,g
- Raw entry pattern: {BASE}kb/<type>/<slug>.md  (type = skill | spec | note), e.g. {BASE}kb/spec/motion.md, {BASE}kb/skill/taste-skill.md
- [Context bundle]({BASE}context-bundle.md): AGENTS.md + all specs + house style + skills index in one file

## Machine-readable
- [Resources JSON]({BASE}api/resources.json): all items with type, ct (component kind), vs (visual style), pricing, url
- [Skills JSON]({BASE}api/skills.json): design + engineering agent skills and the recommended workflow
- [Agent guide]({BASE}agents/): how to search, pick, copy and verify
- [AGENTS.md]({BASE}AGENTS.md)
- [Full text for LLMs]({BASE}llms-full.txt)

## Blog
- [Blog RSS feed]({BASE}blog/rss.xml) · [Blog JSON]({BASE}api/blog.json)
{blog_lines}

## Top component libraries
""" + '\n'.join(f'- [{i["name"]}]({i["url"]}): {i.get("noteEn") or i["note"]}' for i in libs[:60]) + "\n\n## FAQ\n" + '\n'.join(f'- **{q}** {a}' for q,a in FAQ) + "\n"
w('llms.txt', llms)
full = llms + "\n\n# Blog posts (full text, English)\n\n" + '\n\n'.join(f"## {p['t']['en']}\n\n{re.sub(r'<[^>]+>','',p['en']).strip()}\n\nReferences:\n"+'\n'.join(f'- {t} — {a}: {u}' for t,a,u in p['refs']) for p in POSTS)
full += "\n\n# All resources (name | type | url | note)\n\n" + '\n'.join(f"- {i['name']} | {i['type']} | {i['url']} | {(i.get('noteEn') or i['note'])[:160]}" for i in ITEMS if i['type']!='style')
full += "\n\n# Component style demos: %d entries, see api/resources.json (type=style)\n" % tc['style']
full_holder=[full]
AG = f"""# AGENTS.md — using UI Hub as a design source

You are an AI coding/design agent. UI Hub ({BASE}) is a curated index of UI libraries, component demos and design skills.

## Steps
1. Fetch `{BASE}api/resources.json` (≈{len(ITEMS)} items, updated {UPD}).
2. Filter: `type` (library | style | effect | template | skill …), `ct` (button, input, dialog, table, chart, chat, motion, background, layout …), `vs` (minimal, enterprise, soft, playful, motion, dark-tech, gradient, 3d, apple, editorial, brutalist …), `pricing` (prefer free).
3. Prefer `type=library` with an open license for production code; use `type=style` entries (component demos with `libName`, `page`) to choose a concrete look.
4. Open the original `url` for the install command and source. Respect each license; never copy paid/pro source.
5. Load skills from `{BASE}api/skills.json`: one direction skill (frontend-design | taste-skill) → build → emil-design-eng for motion → audit with impeccable, baseline-ui, web-design-guidelines, accessibility.
6. Verify in a real browser: light + dark, 375px mobile, keyboard focus, reduced motion.

## Rules
- Pick ONE visual style per product and lock it into tokens (CSS variables) before building pages.
- At most one "hero" effect (beams/spotlight/marquee) per page.
- Cite the resources you used (name + URL) in your PR/description.
"""
w('AGENTS.md', AG)

# ---------- agents page ----------
fq = ''.join(f'<details><summary>{E(q)}</summary><p>{E(a)}</p></details>' for q,a in FAQ)
sk_html = ''.join(f'<div class="box"><h3>{E(s["id"])} <span class="note">· {E(s["category"])}</span></h3><p>{E(s["description"][:220])}</p></div>' for s in skills if s['category']!='engineering')
ld = {'@context':'https://schema.org','@graph':[{'@type':'WebPage','name':'UI Hub guide for AI agents','url':BASE+'agents/'},{'@type':'FAQPage','mainEntity':[{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}} for q,a in FAQ]}]}
w('agents/index.html', head('Guide for AI agents · UI Hub', U['ag_lede']['en'], 'agents/', ld, '../') + f"""<body>{topbar('../','agents')}<main class="wrap"><section class="hero"><p class="eb">Agents · GEO</p><h1>{ml('ag_title')}</h1><p class="lede">{ml('ag_lede')}</p></section>
<div class="grid2"><a class="box" href="../api/resources.json" style="text-decoration:none"><h3>/api/resources.json</h3><p>{len(ITEMS)} items · type / ct / vs / pricing</p></a><a class="box" href="../api/skills.json" style="text-decoration:none"><h3>/api/skills.json</h3><p>{len(skills)} agent skills + workflow</p></a><a class="box" href="../llms.txt" style="text-decoration:none"><h3>/llms.txt</h3><p>llms-full.txt · AGENTS.md · .well-known/agent.json</p></a></div>
<section class="sec"><h2>Workflow</h2><ol>
<li>Fetch <code>api/resources.json</code>; filter by <code>ct</code> (component kind) and <code>vs</code> (visual style), prefer <code>pricing: free</code>.</li>
<li>Pick one direction skill (<code>frontend-design</code> or <code>taste-skill</code>) and lock tokens: font, spacing scale, radius, one accent, light + dark.</li>
<li>Choose components: <code>type: library</code> for code, <code>type: style</code> demos for the concrete look; open the original URL for install and source.</li>
<li>Use the card's copyable Prompt as a starting spec; add layout, states, real content and an "avoid" list.</li>
<li>Polish motion with <code>emil-design-eng</code>; audit with <code>impeccable</code>, <code>baseline-ui</code>, <code>web-design-guidelines</code>, <code>accessibility</code>.</li>
<li>Verify in a browser: light/dark, 375 px, keyboard, reduced motion. Cite the resources you used.</li></ol>
<pre><code>// example: minimal dialogs from free libraries
const r = await fetch('{BASE}api/resources.json').then(r=&gt;r.json());
r.items.filter(i =&gt; i.ct?.includes('dialog') &amp;&amp; i.vs?.includes('minimal') &amp;&amp; i.pricing==='free')</code></pre></section>
<section class="sec"><h2>Design &amp; UI engineering skills</h2><div class="grid2">{sk_html}</div></section>
<section class="sec"><h2>FAQ</h2>{fq}</section></main>{foot('../')}{SCRIPT}</body></html>""")

import agents_page; agents_page.build(globals())
import kb; KB = kb.build(globals())
w('llms-full.txt', full_holder[0] + '\n\n# Design encyclopedia entries (specs + notes, full; skills: see raw URLs)\n\n' + '\n\n'.join(e['md'] for e in KB if e['type'] in ('spec','note') and not e['slug'].startswith('blog-')) + '\n\n# Skill raw URLs\n' + '\n'.join(f"- {e['title']}: {e['raw']}" for e in KB if e['type']=='skill'))
# ---------- sitemap / robots ----------
urls = [('',UPD[:10]),('blog/',TODAY),('agents/',TODAY)] + [(f'blog/{p["slug"]}/',p['date']) for p in POSTS] + [('kb/',TODAY)] + [(f'kb/{e["type"]}/{e["slug"]}/',TODAY) for e in KB]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
for u,d in urls:
    sm += f'<url><loc>{BASE}{u}</loc><lastmod>{d}</lastmod>' + ''.join(f'<xhtml:link rel="alternate" hreflang="{c}" href="{BASE}{u}?lang={c}"/>' for c,_,_ in LANGS) + f'<xhtml:link rel="alternate" hreflang="x-default" href="{BASE}{u}"/></url>\n'
w('sitemap.xml', sm + '</urlset>\n')
w('robots.txt', f'User-agent: *\nAllow: /\n\nSitemap: {BASE}sitemap.xml\n# LLM-friendly index: {BASE}llms.txt\n')
w('.nojekyll', '')

img = 'og.png'
# ---------- index.html SEO head + nav ----------
ip = os.path.join(ROOT,'index.html'); s = open(ip,encoding='utf-8').read()
# Impact affiliate site verification (must stay in the homepage <head>)
IMPACT_META = "<meta name='impact-site-verification' value='15b17138-ddc6-446b-9829-a0aa087f726a'>"
if '15b17138-ddc6-446b-9829-a0aa087f726a' not in s: s = s.replace('<head>', '<head>\n'+IMPACT_META, 1)
desc = f'UI Hub: curated directory of {len(ITEMS)} UI resources — {tc["library"]} component libraries, {tc["style"]} component style demos with light/dark previews, design skills for AI agents, and AI design technique articles. 10 languages, updated daily.'
ld = {'@context':'https://schema.org','@graph':[{'@type':'WebSite','name':'UI Hub','url':BASE,'inLanguage':[c for c,_,_ in LANGS],'description':desc},
 {'@type':'CollectionPage','name':'UI Hub — UI components, libraries & design skills','url':BASE,'dateModified':UPD[:10],'about':['UI components','design systems','AI design']},
 {'@type':'ItemList','name':'Component libraries','numberOfItems':len(libs),'itemListElement':[{'@type':'ListItem','position':n+1,'name':i['name'],'url':i['url']} for n,i in enumerate(libs[:50])]}]}
alt = ''.join(f'<link rel="alternate" hreflang="{c}" href="{BASE}?lang={c}">' for c,_,_ in LANGS)
seo = f"""<!--SEO-->
<meta name="description" content="{E(desc)}"><link rel="canonical" href="{BASE}">{alt}<link rel="alternate" hreflang="x-default" href="{BASE}">
<meta property="og:type" content="website"><meta property="og:site_name" content="UI Hub"><meta property="og:title" content="UI Hub — UI components, libraries &amp; design skills"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{BASE}"><meta property="og:image" content="{BASE}{img}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="UI Hub — UI components, libraries &amp; design skills"><meta name="twitter:description" content="{E(desc)}"><meta name="twitter:image" content="{BASE}{img}">
<link rel="alternate" type="text/plain" title="llms.txt" href="llms.txt"><link rel="sitemap" type="application/xml" href="sitemap.xml">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<!--/SEO-->"""
s = re.sub(r'<!--SEO-->.*?<!--/SEO-->\n?', '', s, flags=re.S)
s = s.replace('<title>UI Hub</title>', '<title>UI Hub — UI components, libraries &amp; design skills</title>')
s = s.replace('</title>\n', '</title>\n'+seo+'\n', 1)
if 'class="bblog"' not in s:
    s = s.replace('<a href="#/fav" data-v="fav"><svg', '<a href="blog/" class="bblog"><svg viewBox="0 0 24 24"><path d="M5 4h10l4 4v12H5z"/><path d="M9 12h6M9 16h6M9 8h3"/></svg><span data-i18n="nav_blog">Blog</span></a><a href="#/fav" data-v="fav"><svg', 1)
if 'href="kb/" data-i18n' not in s:
    s = s.replace('<a href="blog/" data-i18n="nav_blog">', '<a href="kb/" data-i18n="nav_kb">Encyclopedia</a><a href="blog/" data-i18n="nav_blog">', 1)
if 'href="blog/" data-i18n' not in s:
    s = s.replace('<a href="#/fav" data-v="fav"><span data-i18n="nav_fav">', '<a href="blog/" data-i18n="nav_blog">Blog</a><a href="agents/" data-i18n="nav_agents">Agents</a><a href="#/fav" data-v="fav"><span data-i18n="nav_fav">', 1)
if 'id="upd"' not in s:
    pass
if 'function updTxt' not in s:
    s = s.replace('<dl class="hstats" id="hstats"></dl>', '<dl class="hstats" id="hstats"></dl>\n      <p class="upd" id="upd" style="margin:14px 0 0;font:500 12px/1 var(--mono);color:var(--ink3)"></p>', 1)
    s = s.replace('</script>\n</body>', "function updTxt(){var e=document.getElementById('upd');if(!e||!window.UI_DATA)return;var I=window.UI_I18N||{},l=document.documentElement.lang,d=I[l]||I.en||{};var r=UI_DATA.updatedAt||UI_DATA.generated,x=new Date(r.length===17&&r.slice(-1)==='Z'?r.slice(0,16)+':00Z':r),z={'zh-Hans':'zh-CN','zh-Hant':'zh-TW'}[l]||l,v=isNaN(x)?r:x.toLocaleString(z,{year:'numeric',month:'short',day:'numeric',hour:'2-digit',minute:'2-digit',timeZoneName:'short'});e.textContent=(d.updated||'Updated')+' '+v}updTxt();var _ls=document.getElementById('langSel');_ls&&_ls.addEventListener('change',function(){setTimeout(updTxt,0)});\n</script>\n</body>", 1)
s = s.replace("e.textContent=(d.updated||'Updated')+' '+(UI_DATA.updatedAt||UI_DATA.generated).replace('T',' ').replace('Z',' UTC')}", "var r=UI_DATA.updatedAt||UI_DATA.generated,x=new Date(r.length===17&&r.slice(-1)==='Z'?r.slice(0,16)+':00Z':r),z={'zh-Hans':'zh-CN','zh-Hant':'zh-TW'}[l]||l,v=isNaN(x)?r:x.toLocaleString(z,{year:'numeric',month:'short',day:'numeric',hour:'2-digit',minute:'2-digit',timeZoneName:'short'});e.textContent=(d.updated||'Updated')+' '+v}")
s = re.sub(r'\?v=5"', '?v=6"', s)
open(ip,'w',encoding='utf-8').write(s)

# CJK-friendly headings on agents + kb (keep-all + balanced wrap, phrase breaks)
CJK_CSS = '<style>h1,h2,h3,.lede{text-wrap:balance}:lang(ja) :is(h1,h2,h3,.eb2),:lang(zh-Hans) :is(h1,h2,h3),:lang(zh-Hant) :is(h1,h2,h3),:lang(ko) :is(h1,h2,h3,p,li,summary){word-break:keep-all;line-break:strict}@media(max-width:560px){.cb pre{padding-right:14px!important;padding-top:44px!important}}</style>'
for fp in ['agents/index.html','kb/index.html']:
    full = os.path.join(ROOT, fp)
    if not os.path.exists(full): continue
    t = open(full, encoding='utf-8').read()
    t = t.replace('AIエージェント向けガイド</span>', 'AIエージェント<wbr>向けガイド</span>').replace('UIデザイン百科</span>', 'UIデザイン<wbr>百科</span>')
    if 'CJK-wrap' not in t: t = t.replace('</head>', '<!--CJK-wrap-->'+CJK_CSS+'</head>', 1)
    open(full,'w',encoding='utf-8').write(t)
import importlib.util as _u
_sp=_u.spec_from_file_location('growth', os.path.join(os.path.dirname(os.path.abspath(__file__)),'growth.py'));_g=_u.module_from_spec(_sp);_sp.loader.exec_module(_g);_g.run()
print('extras built:', len(POSTS), 'posts,', len(ITEMS), 'items,', len(skills), 'skills, updated', UPD)
