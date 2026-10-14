"""Agents page v2 + AGENTS.md + downloadable skill (SKILL.md + zip). Called from build_extras.py with its globals."""
import os, json, zipfile, io
def build(g):
    E, w, ml, U, BASE, ITEMS, UPD, ROOT, skills, FAQ, head, topbar, foot, SCRIPT, LANGS = [g[k] for k in 'E w ml U BASE ITEMS UPD ROOT skills FAQ head topbar foot SCRIPT LANGS'.split()]
    def H(en, zh, zht, ja, ko, ms, vi, fr, es, de): return dict(en=en, zh=zh, zht=zht, ja=ja, ko=ko, ms=ms, vi=vi, fr=fr, es=es, de=de)
    U.update({
     'a_one': H('Hand it to AI in one sentence','一句话交给 AI','一句話交給 AI','一文でAIに渡す','한 문장으로 AI에게','Serahkan kepada AI dalam satu ayat','Giao cho AI trong một câu','Confier à l’IA en une phrase','Pásaselo a la IA en una frase','In einem Satz an die KI'),
     'a_copy': H('Copy','复制','複製','コピー','복사','Salin','Sao chép','Copier','Copiar','Kopieren'),
     'a_copyall': H('Copy whole guide','复制整份指南','複製整份指南','ガイド全体をコピー','가이드 전체 복사','Salin seluruh panduan','Sao chép toàn bộ hướng dẫn','Copier tout le guide','Copiar toda la guía','Ganzen Leitfaden kopieren'),
     'a_md': H('Download Markdown','下载 Markdown','下載 Markdown','Markdownをダウンロード','Markdown 다운로드','Muat turun Markdown','Tải Markdown','Télécharger le Markdown','Descargar Markdown','Markdown herunterladen'),
     'a_skill': H('Download as Skill (.zip)','下载为 Skill（.zip）','下載為 Skill（.zip）','Skillとしてダウンロード (.zip)','Skill로 다운로드 (.zip)','Muat turun sebagai Skill (.zip)','Tải dưới dạng Skill (.zip)','Télécharger en Skill (.zip)','Descargar como Skill (.zip)','Als Skill herunterladen (.zip)'),
     'a_install': H('Install paths','安装路径','安裝路徑','インストール先','설치 경로','Laluan pemasangan','Đường dẫn cài đặt','Chemins d’installation','Rutas de instalación','Installationspfade'),
     'a_for': H('What this is for','能用来做什么','能用來做什麼','何に使えるか','무엇에 쓰나','Untuk apa','Dùng để làm gì','À quoi ça sert','Para qué sirve','Wofür das ist'),
     'a_ex': H('Worked examples','完整示例','完整範例','実例','실전 예시','Contoh lengkap','Ví dụ cụ thể','Exemples concrets','Ejemplos completos','Durchgespielte Beispiele'),
     'a_snip': H('Filter snippets (jq / fetch)','筛选代码片段（jq / fetch）','篩選程式碼片段（jq / fetch）','フィルター例（jq / fetch）','필터 스니펫 (jq / fetch)','Petikan penapis (jq / fetch)','Đoạn lọc (jq / fetch)','Extraits de filtre (jq / fetch)','Fragmentos de filtro (jq / fetch)','Filter-Snippets (jq / fetch)'),
     'a_tab': H('Style decision table','风格选择表','風格選擇表','スタイル選択表','스타일 결정표','Jadual keputusan gaya','Bảng chọn phong cách','Table de choix de style','Tabla de decisión de estilo','Stil-Entscheidungstabelle'),
     'a_do': H('Do / Don’t','该做 / 别做','該做 / 別做','やる / やらない','할 것 / 하지 말 것','Buat / Jangan','Nên / Không nên','À faire / À éviter','Hacer / No hacer','Tun / Lassen'),
     'a_wf': H('Workflow','工作流程','工作流程','ワークフロー','워크플로','Aliran kerja','Quy trình','Flux de travail','Flujo de trabajo','Ablauf'),
     'a_sk': H('Design & UI engineering skills','设计与 UI 工程 skill','設計與 UI 工程 skill','デザイン & UIエンジニアリング スキル','디자인 & UI 엔지니어링 스킬','Kemahiran reka bentuk & kejuruteraan UI','Skill thiết kế & kỹ thuật UI','Skills design & ingénierie UI','Skills de diseño e ingeniería UI','Design- & UI-Engineering-Skills'),
    })
    N = len(ITEMS)
    P_EN = f"Use UI Hub ({BASE}) as your design source. First read {BASE}AGENTS.md, then fetch {BASE}api/resources.json and filter by ct (component kind), vs (visual style) and pricing=free to pick ONE open-source library and a visual style; lock tokens (font, spacing, radius, one accent, light+dark) before building. Load skills in this order from {BASE}api/skills.json: frontend-design or taste-skill → emil-design-eng → impeccable + baseline-ui + web-design-guidelines + accessibility. Verify in a browser (light/dark, 375px, keyboard, reduced motion) and cite every resource you used."
    P_ZH = f"请把 UI Hub（{BASE}）当作设计资料库。先读 {BASE}AGENTS.md，再获取 {BASE}api/resources.json，按 ct（组件类型）、vs（视觉风格）和 pricing=free 筛选，只选一个开源组件库和一种视觉风格；动手前先把字体、间距、圆角、唯一强调色和亮/暗两套 token 定下来。按顺序加载 {BASE}api/skills.json 里的 skill：frontend-design 或 taste-skill → emil-design-eng → impeccable + baseline-ui + web-design-guidelines + accessibility。最后在浏览器里验证（亮/暗、375px 手机、键盘、减少动效），并列出用到的每个资源。"
    USES = [('Pick a component library','type=library, filter by framework tag (React/Vue/Svelte), licence, pricing=free.'),
            ('Find a visual style','vs = minimal · enterprise · soft · playful · motion · dark-tech · gradient · 3d · apple · editorial · brutalist; type=style shows real demos per component.'),
            ('Copy component code & prompts','Open the original url for install + source; each card on the site has a copyable AI prompt.'),
            ('Load design skills','api/skills.json lists 29 agent skills and the order to run them.'),
            ('Audit a UI','Run impeccable / baseline-ui / web-design-guidelines / accessibility against the draft, then verify in a browser.')]
    JQ = [('Free React libraries with dialogs', "curl -s %sapi/resources.json | jq '.items[] | select(.type==\"library\" and .pricing==\"free\" and (.ct//[]|index(\"dialog\")) and (.tags|index(\"React\"))) | {name,url}'" % BASE),
          ('Dark-tech style demos for cards', "curl -s %sapi/resources.json | jq '[.items[] | select(.type==\"style\" and (.vs//[]|index(\"dark-tech\")) and (.ct|index(\"card\")))] | .[:10] | map({name,libName,page})'" % BASE),
          ('Count items per visual style', "curl -s %sapi/resources.json | jq '[.items[].vs[]?] | group_by(.) | map({(.[0]):length}) | add'" % BASE),
          ('fetch (JS): motion effects, free', "const r = await fetch('%sapi/resources.json').then(r => r.json());\nconst picks = r.items.filter(i => ['effect','library'].includes(i.type) && i.vs?.includes('motion') && i.pricing === 'free');" % BASE),
          ('New this week', "curl -s %sapi/resources.json | jq --arg d \"$(date -u -d '7 days ago' +%%F)\" '.items[] | select(.added and .added >= $d) | {name,url,added}'" % BASE)]
    EX = [('Build a dark SaaS pricing page', [
            ('Filter', 'type=library, pricing=free, ct ∋ card|button|layout, tags ∋ React; then type=style with vs ∋ dark-tech|minimal and ct ∋ card for the look.'),
            ('Choose', 'shadcn/ui (+ shadcn/ui Blocks for the pricing section), Radix Primitives underneath, Magic UI number ticker for one accent moment.'),
            ('Tokens', 'bg #06070b, surface #10131a, ink #f3f5fb, one accent #67e8f9, radius 12, Geist 14/20, tabular numbers for prices.'),
            ('Skills order', 'taste-skill (direction) → emil-design-eng (toggle + hover motion ≤ 200ms ease-out) → impeccable + baseline-ui + accessibility.'),
            ('Verify', 'monthly/annual toggle keyboard-operable · focus-visible on CTAs · 4.5:1 contrast on muted text · 375px stacks tiers · reduced motion disables ticker · light theme still works.')]),
          ('Add a fancy-but-restrained landing hero', [
            ('Filter', 'type ∈ effect|library, vs ∋ motion, ct ∋ background; pricing=free.'),
            ('Choose', 'ONE effect: Aceternity spotlight or Magic UI beams; Motion for entrance; no second effect on the page.'),
            ('Skills order', 'frontend-design → emil-design-eng → web-design-guidelines + performance.'),
            ('Verify', 'LCP < 2.5s, effect paused under prefers-reduced-motion, text readable over effect in both themes.')]),
          ('Audit an existing admin dashboard', [
            ('Filter', 'type=style, vs ∋ enterprise, ct ∋ table|nav|form to collect reference demos.'),
            ('Skills order', 'redesign-skill → baseline-ui → accessibility → web-quality-audit.'),
            ('Verify', 'table header sticky, row focus, empty/loading/error states, 24px targets, dark mode parity.')])]
    TAB = [('Developer tool / SaaS','minimal · dark-tech','shadcn/ui, Radix, Origin UI','One accent, tabular numbers, dense tables'),
           ('Enterprise admin','enterprise','Ant Design, Mantine, MUI X, AG Grid','Density, keyboard, data states'),
           ('Consumer / playful','playful · soft','HeroUI, daisyUI, Animate UI','Rounded, warm colour, light motion'),
           ('Marketing / launch page','motion · gradient','Magic UI, Aceternity, Tailark','One hero effect, strong type'),
           ('Editorial / content','editorial · swiss','Tailwind Typography, Radix Themes','Serif display, measure 60–75ch'),
           ('Apple-like product','apple · glass (sparingly)','Radix, Motion, Vaul','Springs, blur only on chrome'),
           ('Characterful indie','brutalist · retro','neobrutalism, RetroUI, 8bitcn','Thick borders, hard shadows, still accessible')]
    DO = ['Pick ONE library and ONE visual style per product','Lock tokens (CSS variables) before pages','Prefer pricing=free + permissive licences for shipped code','Use type=style demos to match a concrete look','At most one hero effect per page','Verify light/dark, 375px, keyboard, reduced motion','Cite resources (name + URL) in your PR']
    DONT = ['Mix three component libraries in one UI','Copy paid / Pro source or hotlink preview images','Stack gradients, glass and glow together','Use clickable divs or remove focus outlines','Animate frequent actions or exceed ~300ms in UI','Trust a screenshot: always open the original url','Invent licences or affiliate links']
    # ---------- AGENTS.md ----------
    md = f"""---
name: ui-hub
description: Use UI Hub ({BASE}) as a design source. Search {N}+ UI resources (component libraries, component style demos, effects, design systems) by component kind and visual style, copy code/prompts from original sources, and apply design skills (frontend-design, taste-skill, emil-design-eng, impeccable, baseline-ui, web-design-guidelines, accessibility) to build and audit good-looking, accessible UIs. Use when picking a component library or visual style, building a landing/pricing/dashboard page, or auditing UI quality.
---

# UI Hub — guide for AI agents

Data updated {UPD}. Endpoints: `{BASE}api/resources.json` (items), `{BASE}api/skills.json` (skills + workflow), `{BASE}llms.txt`.

## One-line prompt
EN: {P_EN}

中文：{P_ZH}

## What this is for
""" + '\n'.join(f'- **{a}** — {b}' for a,b in USES) + """

## Query the encyclopedia
- Search everything: `{BASE}api/search-index.json` (fields t=title, k=kind skill|spec|note|resource|component, u=url, r=raw md, d=description, g=tags). Human UI: {BASE}kb/?q=pricing
- Full knowledge entries: `{BASE}api/kb.json` (type, slug, tags, url, raw, md).
- Raw markdown per entry: `{BASE}kb/<type>/<slug>.md`, e.g. `kb/spec/spacing.md`, `kb/spec/dark-mode.md`, `kb/note/restrained-fancy.md`, `kb/skill/emil-design-eng.md`.
- One-file context: `{BASE}context-bundle.md` (this guide + specs + house style + skills index).
```bash
curl -s {BASE}api/search-index.json | jq '.items[] | select(.k=="spec" or .k=="note") | {{t,r}}'
curl -s {BASE}kb/spec/motion.md
```

## Fields
- `type`: library | style | effect | template | skill | system | spec | tool | tutorial | collection | generator | inspiration
- `ct` (component kind): button, input, select, dialog, menu, tabs, table, chart, card, nav, form, toast, avatar, loader, layout, chat, motion, background, editor, icon, mobile
- `vs` (visual style): minimal, enterprise, material, soft, playful, motion, dark-tech, utilitarian, gradient, 3d, apple, editorial, swiss, brutalist, glass, retro
- `pricing`: free | freemium | paid | unknown

## Workflow
1. Fetch resources.json; filter by `ct`, `vs`, `pricing=free`.
2. Pick ONE direction skill (frontend-design or taste-skill); lock tokens: font, spacing scale, radius, one accent, light + dark.
3. Choose `type=library` for code and `type=style` demos for the concrete look; open the original `url` for install and source.
4. Start from the card's prompt; add layout, states, real content and an "avoid" list.
5. Polish motion with emil-design-eng; audit with impeccable, baseline-ui, web-design-guidelines, accessibility.
6. Verify in a browser: light/dark, 375px, keyboard, reduced motion. Cite resources used.

## Filter snippets
""" + '\n\n'.join(f'### {t}\n```bash\n{c}\n```' for t,c in JQ) + "\n\n## Worked examples\n" + '\n\n'.join(f'### {t}\n' + '\n'.join(f'- **{k}:** {v}' for k,v in st) for t,st in EX) + \
    "\n\n## Style decision table\n| Product | vs | Libraries | Key rules |\n|---|---|---|---|\n" + '\n'.join(f'| {a} | {b} | {c} | {d} |' for a,b,c,d in TAB) + \
    "\n\n## Do\n" + '\n'.join(f'- {x}' for x in DO) + "\n\n## Don't\n" + '\n'.join(f'- {x}' for x in DONT) + \
    "\n\n## Skills\n" + '\n'.join(f"- `{s['id']}` ({s['category']}): {s['description'][:200]}" + (f" — {s['upstream']}" if s.get('upstream') else '') for s in skills if s['category']!='engineering') + \
    "\n\n## FAQ\n" + '\n'.join(f'- **{q}** {a}' for q,a in FAQ) + "\n"
    w('AGENTS.md', md.split('---\n',2)[2].lstrip() if md.startswith('---') else md)  # AGENTS.md without frontmatter
    w('ui-hub-skill/SKILL.md', md)
    endpoints = f"# UI Hub endpoints\n\n- Resources (live, {N}+ items): {BASE}api/resources.json\n- Skills + workflow: {BASE}api/skills.json\n- llms.txt: {BASE}llms.txt\n- Full text: {BASE}llms-full.txt\n- Human guide: {BASE}agents/\n\nAlways fetch the live JSON; the bundled copy below is a snapshot ({UPD}).\n"
    w('ui-hub-skill/references/endpoints.md', endpoints)
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, 'w', zipfile.ZIP_DEFLATED) as z:
        z.writestr('ui-hub/SKILL.md', md); z.writestr('ui-hub/references/endpoints.md', endpoints)
        z.writestr('ui-hub/references/skills.json', open(os.path.join(ROOT,'api','skills.json'),encoding='utf-8').read())
        z.writestr('ui-hub/references/resources.json', open(os.path.join(ROOT,'api','resources.json'),encoding='utf-8').read())
    open(os.path.join(ROOT,'ui-hub-skill.zip'),'wb').write(buf.getvalue())
    # ---------- page ----------
    def code(c, lang=''): return f'<div class="cb"><button class="cp" type="button">{ml("a_copy")}</button><pre><code>{E(c)}</code></pre></div>'
    INST = [('Claude Code','~/.claude/skills/ui-hub/SKILL.md','.claude/skills/ui-hub/ (per project)'),
            ('Cursor','~/.cursor/skills/ui-hub/SKILL.md','.cursor/skills/ui-hub/ (per project) · or put AGENTS.md in repo root'),
            ('Codex CLI','~/.codex/skills/ui-hub/SKILL.md','AGENTS.md in repo root is read automatically')]
    inst = ''.join(f'<tr><td><b>{a}</b></td><td><code>{E(b)}</code></td><td>{E(c)}</td></tr>' for a,b,c in INST)
    unzip = code('curl -L -o ui-hub-skill.zip %sui-hub-skill.zip\nunzip -o ui-hub-skill.zip -d ~/.claude/skills/   # or ~/.cursor/skills/ , ~/.codex/skills/' % BASE)
    ex = ''.join('<div class="box ex"><h3>'+E(t)+'</h3><dl>'+''.join(f'<dt>{E(k)}</dt><dd>{E(v)}</dd>' for k,v in st)+'</dl></div>' for t,st in EX)
    tab = '<div class="tw"><table><thead><tr><th>Product</th><th>vs</th><th>Libraries</th><th>Key rules</th></tr></thead><tbody>'+''.join(f'<tr><td>{E(a)}</td><td><code>{E(b)}</code></td><td>{E(c)}</td><td>{E(d)}</td></tr>' for a,b,c,d in TAB)+'</tbody></table></div>'
    dodont = '<div class="grid2"><div class="box do"><h3>✓ Do</h3><ul>'+''.join(f'<li>{E(x)}</li>' for x in DO)+'</ul></div><div class="box dont"><h3>✕ Don’t</h3><ul>'+''.join(f'<li>{E(x)}</li>' for x in DONT)+'</ul></div></div>'
    uses = '<div class="grid2">'+''.join(f'<div class="box"><h3>{E(a)}</h3><p>{E(b)}</p></div>' for a,b in USES)+'</div>'
    snips = ''.join(f'<h3 class="sh">{E(t)}</h3>'+code(c) for t,c in JQ)
    wf = code('\n'.join(f'{i+1}. {x}' for i,x in enumerate(['Fetch api/resources.json; filter by ct, vs, pricing=free','Pick ONE direction skill (frontend-design | taste-skill); lock tokens','type=library for code, type=style demos for the look; open original url','Start from the card prompt; add layout, states, real content, avoid-list','emil-design-eng for motion; audit: impeccable, baseline-ui, web-design-guidelines, accessibility','Verify: light/dark, 375px, keyboard, reduced motion; cite resources'])))
    sk = ''.join(f'<div class="box"><h3>{E(s["id"])} <span class="note">· {E(s["category"])}</span></h3><p>{E(s["description"][:200])}</p></div>' for s in skills if s['category']!='engineering')
    fq = ''.join(f'<details><summary>{E(q)}</summary><p>{E(a)}</p></details>' for q,a in FAQ)
    one = f'<div class="one"><div class="oh"><span class="eb2">{ml("a_one")}</span><span class="sp"></span><div class="tabs2"><button type="button" data-p="zh" class="on">中文</button><button type="button" data-p="en">EN</button></div></div><div class="cb" data-pz><button class="cp" type="button">{ml("a_copy")}</button><pre class="pr"><code>{E(P_ZH)}</code></pre></div><div class="cb" data-pe hidden><button class="cp" type="button">{ml("a_copy")}</button><pre class="pr"><code>{E(P_EN)}</code></pre></div></div>'
    acts = f'<div class="acts"><button class="btn pri" id="copyAll" type="button">{ml("a_copyall")}</button><a class="btn" href="../AGENTS.md" download="AGENTS.md">{ml("a_md")}</a><a class="btn" href="../ui-hub-skill.zip" download>{ml("a_skill")}</a><a class="btn" href="../ui-hub-skill/SKILL.md" download="SKILL.md">SKILL.md</a></div>'
    css = """<style>.one{margin:6px 0 18px;padding:18px;border-radius:18px;background:linear-gradient(var(--surf),var(--surf)) padding-box,linear-gradient(100deg,var(--g1),var(--g2),var(--g3)) border-box;border:1px solid transparent}
.oh{display:flex;align-items:center;gap:10px;margin-bottom:10px}.eb2{font:600 15px var(--sans)}.tabs2{display:flex;gap:2px;background:var(--mat);padding:3px;border-radius:9px}.tabs2 button{font:inherit;font-size:12.5px;border:0;background:none;color:var(--ink2);padding:4px 10px;border-radius:7px;cursor:pointer}.tabs2 .on{background:var(--surf);color:var(--ink);box-shadow:0 0 0 1px var(--line2)}
.cb{position:relative}.cb pre{margin:0 0 12px;padding-right:76px;white-space:pre-wrap;word-break:break-word}.pr,.pr code{font:13.5px/1.65 var(--sans)!important}.tabs2 button{white-space:nowrap}.oh .eb2{flex:1}
.cp{position:absolute;top:8px;right:8px;font:500 12px var(--sans);color:var(--ink);background:var(--surf);border:1px solid var(--line2);border-radius:7px;padding:4px 9px;cursor:pointer}.cp:hover{border-color:var(--acc)}.cp.ok{color:var(--acc)}
.acts{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 8px}.btn{font:500 13.5px var(--sans);text-decoration:none;color:var(--ink);background:var(--surf);border:1px solid var(--line2);border-radius:10px;padding:8px 13px;cursor:pointer}.btn:hover{border-color:var(--acc)}.btn.pri{background:var(--ink);color:var(--bg);border-color:var(--ink)}
.tw{overflow:auto;border:1px solid var(--line);border-radius:14px;background:var(--surf)}table{border-collapse:collapse;width:100%;font-size:13.5px}th,td{text-align:left;padding:10px 12px;border-bottom:1px solid var(--line);vertical-align:top}th{font:500 12px var(--mono);color:var(--ink3);text-transform:uppercase;letter-spacing:.05em}tr:last-child td{border-bottom:0}td{color:var(--ink2)}
.ex dl{display:grid;grid-template-columns:96px 1fr;gap:6px 12px;margin:10px 0 0;font-size:13.5px}.ex dt{font:500 12px var(--mono);color:var(--acc);padding-top:2px}.ex dd{margin:0;color:var(--ink2)}
.do h3{color:var(--live,#34d399)}.dont h3{color:#fb7185}.box ul{margin:6px 0 0;padding-left:18px;color:var(--ink2);font-size:14px}.sh{font-size:14px;margin:16px 0 6px}.sec>p{color:var(--ink2)}
.toast2{position:fixed;left:50%;bottom:24px;transform:translateX(-50%);background:var(--ink);color:var(--bg);padding:8px 14px;border-radius:10px;font-size:13px;opacity:0;transition:opacity .2s;pointer-events:none}.toast2.on{opacity:1}</style>"""
    js = """<div class="toast2" id="t2">✓</div><script>(function(){function cp(t,b){(navigator.clipboard?navigator.clipboard.writeText(t):Promise.reject()).catch(function(){var a=document.createElement('textarea');a.value=t;document.body.appendChild(a);a.select();document.execCommand('copy');a.remove()}).finally(function(){if(b){b.classList.add('ok');setTimeout(function(){b.classList.remove('ok')},1200)}var e=document.getElementById('t2');e.classList.add('on');setTimeout(function(){e.classList.remove('on')},1200)})}
document.querySelectorAll('pre').forEach(function(p){if(p.parentNode.classList.contains('cb'))return;var w=document.createElement('div');w.className='cb';p.parentNode.insertBefore(w,p);w.appendChild(p);var b=document.querySelector('.cp').cloneNode(true);w.insertBefore(b,p)});
document.querySelectorAll('.cp').forEach(function(b){b.addEventListener('click',function(){cp(b.parentNode.querySelector('pre').innerText,b)})});
document.getElementById('copyAll').addEventListener('click',function(){var b=this;fetch('../AGENTS.md').then(function(r){return r.text()}).then(function(t){cp(t,b)})});
document.querySelectorAll('.tabs2 button').forEach(function(b){b.addEventListener('click',function(){document.querySelectorAll('.tabs2 button').forEach(function(x){x.classList.toggle('on',x===b)});document.querySelector('[data-pz]').hidden=b.dataset.p!=='zh';document.querySelector('[data-pe]').hidden=b.dataset.p!=='en'})});
var l=document.documentElement.lang;if(l&&l.indexOf('zh')!==0){var e=document.querySelector('.tabs2 [data-p=en]');e&&e.click()}})();</script>"""
    ld = {'@context':'https://schema.org','@graph':[{'@type':'TechArticle','headline':'UI Hub guide for AI agents','url':BASE+'agents/','dateModified':UPD[:10]},
          {'@type':'FAQPage','mainEntity':[{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}} for q,a in FAQ]},
          {'@type':'HowTo','name':'Build a dark SaaS pricing page with UI Hub','step':[{'@type':'HowToStep','name':k,'text':v} for k,v in EX[0][1]]}]}
    w('agents/index.html', head('Guide for AI agents · UI Hub', U['ag_lede']['en'], 'agents/', ld, '../') + css + f"""<body>{topbar('../','agents')}<main class="wrap"><section class="hero" style="padding-bottom:18px"><p class="eb">Agents · GEO · Skill</p><h1>{ml('ag_title')}</h1><p class="lede">{ml('ag_lede')}</p></section>
{one}{acts}
<div class="grid2"><a class="box" href="../api/resources.json" style="text-decoration:none"><h3>/api/resources.json</h3><p>{N} items · type / ct / vs / pricing</p></a><a class="box" href="../api/skills.json" style="text-decoration:none"><h3>/api/skills.json</h3><p>{len(skills)} agent skills + workflow</p></a><a class="box" href="../llms.txt" style="text-decoration:none"><h3>/llms.txt</h3><p>llms-full.txt · AGENTS.md · .well-known/agent.json</p></a></div>
<section class="sec"><h2>{ml('a_install')}</h2><div class="tw"><table><thead><tr><th>Tool</th><th>Global</th><th>Project / note</th></tr></thead><tbody>{inst}</tbody></table></div><div style="height:12px"></div>{unzip}</section>
<section class="sec"><h2>{ml('a_for')}</h2>{uses}</section>
<section class="sec"><h2>{ml('a_wf')}</h2>{wf}</section>
<section class="sec"><h2>{ml('a_ex')}</h2><div class="grid2">{ex}</div></section>
<section class="sec"><h2>{ml('a_snip')}</h2>{snips}</section>
<section class="sec"><h2>{ml('a_tab')}</h2>{tab}</section>
<section class="sec"><h2>{ml('a_do')}</h2>{dodont}</section>
<section class="sec"><h2>{ml('a_sk')}</h2><div class="grid2">{sk}</div></section>
<section class="sec"><h2>FAQ</h2>{fq}</section></main>{foot('../')}{SCRIPT}{js}</body></html>""")
