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
    U.update({
     'x_filter': H('Find references','查找参考','查找參考','参考を探す','레퍼런스 찾기','Cari rujukan','Tìm tham khảo','Trouver des références','Buscar referencias','Referenzen finden'),
     'x_choose': H('Pick components','选用组件','選用元件','コンポーネントを選ぶ','컴포넌트 선택','Pilih komponen','Chọn thành phần','Choisir les composants','Elegir componentes','Komponenten wählen'),
     'x_tokens': H('Design tokens','设计 token','設計 token','デザイントークン','디자인 토큰','Token reka bentuk','Design token','Tokens de design','Tokens de diseño','Design-Tokens'),
     'x_skills': H('Skills, in order','按顺序加载 skill','依序載入 skill','スキルの順番','스킬 순서','Kemahiran, mengikut urutan','Skill theo thứ tự','Skills, dans l’ordre','Skills, en orden','Skills der Reihe nach'),
     'x_verify': H('Check before shipping','上线前检查','上線前檢查','公開前チェック','출시 전 점검','Semak sebelum terbit','Kiểm tra trước khi phát hành','À vérifier avant de publier','Comprobar antes de publicar','Vor dem Livegang prüfen'),
     'x_open': H('Open in encyclopedia','在百科里打开','在百科裡打開','百科で開く','백과에서 열기','Buka dalam ensiklopedia','Mở trong bách khoa','Ouvrir dans l’encyclopédie','Abrir en la enciclopedia','In der Enzyklopädie öffnen'),
    })
    import sys; sys.path.insert(0, os.path.dirname(__file__)); import agents_i18n as I
    REV = {v['en']: v for v in list(I.X.values())+list(I.S.values())}
    def T(en, zh=None, zht=None): return REV[en]
    def LS(k, **kw): return {l: v.format(**kw) for l, v in I.S[k].items()}
    EXS = [
     dict(title=T('Build a dark SaaS pricing page','做一个深色 SaaS 定价页','做一個深色 SaaS 定價頁'), q='pricing',
      jq="curl -s %sapi/resources.json | jq '.items[] | select(.type==\"library\" and .pricing==\"free\" and (.tags|index(\"React\")) and ((.ct//[]) | index(\"card\") or index(\"button\") or index(\"layout\"))) | {name,url}'" % BASE,
      choose=[('shadcn/ui',T('base components','基础组件','基礎元件')),('shadcn/ui Blocks',T('pricing section','定价区块','定價區塊')),('Radix Primitives',T('underneath','底层交互','底層互動')),('Magic UI Number Ticker',T('the one accent moment','唯一的点睛动效','唯一的點睛動效'))],
      tokens=[('bg','#06070b'),('surface','#10131a'),('ink','#f3f5fb'),('accent','#67e8f9'),('radius','12px'),('font','Geist 14/20'),('numbers','tabular-nums')],
      skills=[('taste-skill',T('set the direction','定方向','定方向')),('emil-design-eng',T('toggle and hover motion, 200ms or less, ease-out','开关与悬停动效，不超过 200ms，ease-out','開關與懸停動效，不超過 200ms，ease-out')),('impeccable + baseline-ui + accessibility',T('final audit','最后审查','最後審查'))],
      verify=[T('Monthly / annual toggle works with the keyboard','月付 / 年付切换能用键盘操作','月付 / 年付切換能用鍵盤操作'),T('Visible focus ring on every CTA','每个 CTA 都有可见的焦点框','每個 CTA 都有可見的焦點框'),T('Muted text reaches 4.5:1 contrast','次要文字对比度达到 4.5:1','次要文字對比度達到 4.5:1'),T('At 375px the tiers stack vertically','375px 手机宽度下价格档位纵向排列','375px 手機寬度下價格檔位縱向排列'),T('Reduced motion turns the ticker off','开启“减少动效”时数字滚动关闭','開啟「減少動效」時數字滾動關閉'),T('Light theme still looks right','亮色主题同样正常','亮色主題同樣正常')]),
     dict(title=T('Add a fancy but restrained landing hero','做一个精致但克制的首屏','做一個精緻但克制的首屏'), q='hero',
      jq="curl -s %sapi/resources.json | jq '.items[] | select((.type==\"effect\" or .type==\"library\") and .pricing==\"free\" and ((.vs//[])|index(\"motion\")) and ((.ct//[])|index(\"background\"))) | {name,url}'" % BASE,
      choose=[('Aceternity Spotlight',T('pick one of these two','与下一项二选一','與下一項二選一')),('Magic UI Beams',T('or this one','或上一项','或上一項')),('Motion',T('entrance only','只做入场','只做入場'))],
      tokens=[], note=T('Only one effect on the whole page.','整页只放一个特效。','整頁只放一個特效。'),
      skills=[('frontend-design',T('set the direction','定方向','定方向')),('emil-design-eng',T('motion polish','打磨动效','打磨動效')),('web-design-guidelines + performance',T('audit','审查','審查'))],
      verify=[T('LCP under 2.5s','LCP 小于 2.5 秒','LCP 小於 2.5 秒'),T('Effect pauses when reduced motion is on','系统开启减少动效时特效暂停','系統開啟減少動效時特效暫停'),T('Text stays readable over the effect in both themes','亮暗两种主题下文字都清晰可读','亮暗兩種主題下文字都清晰可讀')]),
     dict(title=T('Audit an existing admin dashboard','审查一个现有的后台仪表盘','審查一個現有的後台儀表板'), q='dashboard',
      jq="curl -s %sapi/resources.json | jq '[.items[] | select(.type==\"style\" and ((.vs//[])|index(\"enterprise\")) and ((.ct//[]) | index(\"table\") or index(\"nav\") or index(\"form\")))] | .[:20] | map({name,libName,page})'" % BASE,
      choose=[], tokens=[],
      skills=[('redesign-skill',T('find the problems','找问题','找問題')),('baseline-ui',T('fix the basics','补基础','補基礎')),('accessibility',T('accessibility pass','无障碍检查','無障礙檢查')),('web-quality-audit',T('final score','最终评分','最終評分'))],
      verify=[T('Table header stays sticky','表头吸顶','表頭吸頂'),T('Rows can be focused with the keyboard','表格行可用键盘聚焦','表格列可用鍵盤聚焦'),T('Empty, loading and error states exist','有空状态、加载中和出错状态','有空狀態、載入中和出錯狀態'),T('Click targets are at least 24px','点击区域至少 24px','點擊區域至少 24px'),T('Dark mode matches light mode','暗色模式与亮色一致','暗色模式與亮色一致')])]
    def _flat(x):
        st=[('Filter', x['jq'])]
        if x['choose']: st.append(('Choose', '; '.join(f"{n} ({d['en']})" for n,d in x['choose'])))
        if x['tokens']: st.append(('Tokens', ', '.join(f'{k} {v}' for k,v in x['tokens'])))
        st.append(('Skills order', ', then '.join(f"{n} ({d['en']})" for n,d in x['skills'])))
        st.append(('Verify', '; '.join(v['en'] for v in x['verify'])))
        return (x['title']['en'], st)
    EX = [_flat(x) for x in EXS]
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
1. Fetch resources.json; start from `gold==true` (curated 精选 tier), skip items with `flag`; then filter by `ct`, `vs`, `pricing=free`. Pick ONE primary page-level reference (gold) + at most TWO supporting component references, and match the primary closely.
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
    INK = ['in_claude','in_cursor','in_codex']
    inst = ''.join(f'<tr><td><b>{a}</b></td><td><code>{E(b)}</code></td><td>{ml(I.S[INK[i]])}</td></tr>' for i,(a,b,c) in enumerate(INST))
    unzip = code('curl -L -o ui-hub-skill.zip %sui-hub-skill.zip\nunzip -o ui-hub-skill.zip -d ~/.claude/skills/   # or ~/.cursor/skills/ , ~/.codex/skills/' % BASE)
    def sec(k, body): return f'<div class="xs"><div class="xl">{ml(k)}</div>{body}</div>'
    def exhtml(x):
        b = sec('x_filter', code(x['jq']) + f'<a class="xk" href="../kb/?q={x["q"]}">{ml("x_open")} · /kb/?q={x["q"]} →</a>')
        if x['choose']: b += sec('x_choose', '<div class="chips">'+''.join(f'<span class="chip"><b>{E(n)}</b>{ml(d)}</span>' for n,d in x['choose'])+'</div>' + (f'<p class="xn">{ml(x["note"])}</p>' if x.get('note') else ''))
        elif x.get('note'): b += f'<p class="xn">{ml(x["note"])}</p>'
        if x['tokens']: b += sec('x_tokens', '<div class="toks">'+''.join(f'<span class="tok">'+(f'<i style="background:{v}"></i>' if v.startswith('#') else '')+f'<span>{E(k)}</span><code>{E(v)}</code></span>' for k,v in x['tokens'])+'</div>')
        b += sec('x_skills', '<ol class="steps">'+''.join(f'<li><code>{E(n)}</code><span>{ml(d)}</span></li>' for n,d in x['skills'])+'</ol>')
        b += sec('x_verify', '<ul class="chk">'+''.join(f'<li>{ml(v)}</li>' for v in x['verify'])+'</ul>')
        return f'<article class="box ex"><h3>{ml(x["title"])}</h3>{b}</article>'
    ex = ''.join(exhtml(x) for x in EXS)
    swh = '<p class="swh">'+ml({'zh':'← 左右滑动查看整张表 →','zht':'← 左右滑動查看整張表 →','en':'← Swipe to see the full table →','ja':'← 横にスワイプして表全体を表示 →','ko':'← 좌우로 밀어 전체 표 보기 →','ms':'← Leret untuk lihat jadual penuh →','vi':'← Vuốt ngang để xem cả bảng →','fr':'← Faites défiler pour voir le tableau →','es':'← Desliza para ver la tabla completa →','de':'← Wischen, um die ganze Tabelle zu sehen →'})+'</p>'
    tab = swh+'<div class="tw"><table><thead><tr><th>'+ml(I.S['th_prod'])+'</th><th>'+ml(I.S['th_vs'])+'</th><th>'+ml(I.S['th_lib'])+'</th><th>'+ml(I.S['th_rule'])+'</th></tr></thead><tbody>'+''.join(f'<tr><td>{ml(I.S["t%da"%(i+1)])}</td><td><code>{E(b)}</code></td><td>{E(c)}</td><td>{ml(I.S["t%dd"%(i+1)])}</td></tr>' for i,(a,b,c,d) in enumerate(TAB))+'</tbody></table></div>'
    dodont = '<div class="grid2"><div class="box do"><h3>✓ '+ml(I.S['do'])+'</h3><ul>'+''.join(f'<li>{ml(I.S["d%d"%(i+1)])}</li>' for i in range(len(DO)))+'</ul></div><div class="box dont"><h3>✕ '+ml(I.S['dont'])+'</h3><ul>'+''.join(f'<li>{ml(I.S["n%d"%(i+1)])}</li>' for i in range(len(DONT)))+'</ul></div></div>'
    uses = '<div class="grid2">'+''.join(f'<div class="box"><h3>{ml(I.S["u%dt"%(i+1)])}</h3><p>{ml(LS("u%db"%(i+1), n=len(skills)))}</p></div>' for i in range(len(USES)))+'</div>'
    snips = ''.join(f'<h3 class="sh">{ml(I.S["j%d"%(i+1)])}</h3>'+code(c) for i,(t,c) in enumerate(JQ))
    wf = '<ol class="steps wf">'+''.join(f'<li><span>{ml(I.S["w%d"%k])}</span></li>' for k in range(1,7))+'</ol>'
    sk = ''.join(f'<div class="box"><h3>{E(s["id"])} <span class="note">· {E(s["category"])}</span></h3><p>{E(s["description"][:200])}</p></div>' for s in skills if s['category']!='engineering')
    tc = {}
    for it in ITEMS: tc[it.get('type')] = tc.get(it.get('type'),0)+1
    fkw = dict(n=N, lib=tc.get('library',0), sty=tc.get('style',0), sk=tc.get('skill',0), upd=UPD)
    fq = ''.join(f'<details><summary>{ml(q)}</summary><p>{ml({l:v.format(**fkw) for l,v in a.items()})}</p></details>' for q,a in I.FAQI)
    PL = LS('prompt', B=BASE)
    one = f'<div class="one"><div class="oh"><span class="eb2">{ml("a_one")}</span><label class="tg"><input type="checkbox" id="pEn"> {ml(I.S["en_toggle"])}</label></div>' + ''.join(f'<div class="cb pl" data-l="{c}"><button class="cp" type="button">{ml("a_copy")}</button><pre class="pr"><code>{E(PL[k])}</code></pre></div>' for c,_,k in LANGS) + f'<div class="cb" id="pEnBox" hidden><button class="cp" type="button">{ml("a_copy")}</button><pre class="pr"><code>{E(PL["en"])}</code></pre></div></div>'
    acts = f'<div class="acts"><button class="btn pri" id="copyAll" type="button">{ml("a_copyall")}</button><a class="btn" href="../AGENTS.md" download="AGENTS.md">{ml("a_md")}</a><a class="btn" href="../ui-hub-skill.zip" download>{ml("a_skill")}</a><a class="btn" href="../ui-hub-skill/SKILL.md" download="SKILL.md">SKILL.md</a></div>'
    css = """<style>.one{margin:6px 0 18px;padding:18px;border-radius:18px;background:linear-gradient(var(--surf),var(--surf)) padding-box,linear-gradient(100deg,var(--g1),var(--g2),var(--g3)) border-box;border:1px solid transparent}
.oh{display:flex;align-items:center;gap:10px;margin-bottom:10px}.eb2{font:600 15px var(--sans)}.tabs2{display:flex;gap:2px;background:var(--mat);padding:3px;border-radius:9px}.tabs2 button{font:inherit;font-size:12.5px;border:0;background:none;color:var(--ink2);padding:4px 10px;border-radius:7px;cursor:pointer}.tabs2 .on{background:var(--surf);color:var(--ink);box-shadow:0 0 0 1px var(--line2)}
.cb{position:relative}.cb pre{margin:0 0 12px;padding-right:76px;white-space:pre-wrap;word-break:break-word}.pr,.pr code{font:13.5px/1.65 var(--sans)!important}.tabs2 button{white-space:nowrap}.oh .eb2{flex:1}
.cp{position:absolute;top:8px;right:8px;font:500 12px var(--sans);color:var(--ink);background:var(--surf);border:1px solid var(--line2);border-radius:7px;padding:4px 9px;cursor:pointer}.cp:hover{border-color:var(--acc)}.cp.ok{color:var(--acc)}
.acts{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 8px}.btn{font:500 13.5px var(--sans);text-decoration:none;color:var(--ink);background:var(--surf);border:1px solid var(--line2);border-radius:10px;padding:8px 13px;cursor:pointer}.btn:hover{border-color:var(--acc)}.btn.pri{background:var(--ink);color:var(--bg);border-color:var(--ink)}
.tw{overflow-x:auto;-webkit-overflow-scrolling:touch;border:1px solid var(--line);border-radius:14px;background:linear-gradient(90deg,var(--surf) 30%,transparent) left/40px 100% no-repeat local,linear-gradient(270deg,var(--surf) 30%,transparent) right/40px 100% no-repeat local,radial-gradient(farthest-side at 0 50%,rgba(127,127,127,.28),transparent) left/12px 100% no-repeat scroll,radial-gradient(farthest-side at 100% 50%,rgba(127,127,127,.28),transparent) right/12px 100% no-repeat scroll,var(--surf)}.swh{display:none;font:500 12px var(--sans);color:var(--ink3);margin:0 0 6px}@media(max-width:700px){.swh{display:block}.tw table{min-width:620px}.tw td,.tw th{padding:9px 10px}}table{border-collapse:collapse;width:100%;font-size:13.5px}th,td{text-align:left;padding:10px 12px;border-bottom:1px solid var(--line);vertical-align:top}th{font:500 12px var(--mono);color:var(--ink3);text-transform:uppercase;letter-spacing:.05em}tr:last-child td{border-bottom:0}td{color:var(--ink2)}
.exs{display:grid;grid-template-columns:1fr;gap:16px}@media(min-width:1100px){.exs{grid-template-columns:1fr 1fr}.exs .ex:first-child{grid-column:1/-1}}
.ex{padding:20px 22px}.ex h3{font-size:17px;margin:0 0 4px}.xs{margin-top:16px;padding-top:14px;border-top:1px solid var(--line)}.xl{font:600 11.5px var(--sans);letter-spacing:.06em;text-transform:uppercase;color:var(--ink3);margin-bottom:8px}
.ex .cb pre{margin:0 0 6px;font-size:12.5px}.xk{font-size:13px;color:var(--acc);text-decoration:none}.xk:hover{text-decoration:underline}.xn{margin:8px 0 0;font-size:13.5px;color:var(--ink2)}
.chips{display:flex;flex-wrap:wrap;gap:8px}.chip{display:inline-flex;align-items:baseline;gap:6px;padding:6px 11px;border:1px solid var(--line2);border-radius:999px;font-size:13px;color:var(--ink2);background:var(--mat)}.chip b{color:var(--ink);font-weight:600}
.toks{display:flex;flex-wrap:wrap;gap:8px}.tok{display:inline-flex;align-items:center;gap:7px;padding:5px 10px;border:1px solid var(--line);border-radius:9px;font-size:12.5px;color:var(--ink3)}.tok i{width:14px;height:14px;border-radius:4px;box-shadow:inset 0 0 0 1px rgba(127,127,127,.35)}.tok code{color:var(--ink);font:12.5px var(--mono)}
.steps{list-style:none;counter-reset:s;margin:0;padding:0;display:grid;gap:8px}.steps li{counter-increment:s;display:flex;flex-wrap:wrap;align-items:baseline;gap:4px 10px;font-size:13.5px;color:var(--ink2)}.steps li:before{content:counter(s);flex:none;width:22px;height:22px;border-radius:50%;display:inline-grid;place-items:center;font:600 12px var(--sans);color:var(--bg);background:var(--ink)}.steps code{font:13px var(--mono);color:var(--ink)}
.chk{list-style:none;margin:0;padding:0;display:grid;gap:6px;font-size:13.5px;color:var(--ink2)}@media(min-width:700px){.chk{grid-template-columns:1fr 1fr;gap:6px 18px}}.chk li{position:relative;padding-left:24px}.chk li:before{content:"";position:absolute;left:0;top:3px;width:14px;height:14px;border-radius:4px;border:1.5px solid var(--acc)}
.do h3{color:var(--live,#34d399)}.dont h3{color:#fb7185}.box ul{margin:6px 0 0;padding-left:18px;color:var(--ink2);font-size:14px}.sh{font-size:14px;margin:16px 0 6px}.sec>p{color:var(--ink2)}
.tg{display:inline-flex;align-items:center;gap:6px;font-size:12.5px;color:var(--ink2);cursor:pointer;white-space:nowrap}.one .pl.off{display:none!important}.wf li:before{background:var(--acc)}
h1,h2,h3,.lede{text-wrap:balance}:lang(ja) h1,:lang(ja) h2,:lang(ja) h3,:lang(zh) h1,:lang(zh) h2,:lang(ko) h1,:lang(ko) h2,:lang(ko) h3,:lang(ko) p,:lang(ko) li{word-break:keep-all;overflow-wrap:anywhere}
.toast2{position:fixed;left:50%;bottom:24px;transform:translateX(-50%);background:var(--ink);color:var(--bg);padding:8px 14px;border-radius:10px;font-size:13px;opacity:0;transition:opacity .2s;pointer-events:none}.toast2.on{opacity:1}</style>"""
    js = """<div class="toast2" id="t2">✓</div><script>(function(){function cp(t,b){(navigator.clipboard?navigator.clipboard.writeText(t):Promise.reject()).catch(function(){var a=document.createElement('textarea');a.value=t;document.body.appendChild(a);a.select();document.execCommand('copy');a.remove()}).finally(function(){if(b){b.classList.add('ok');setTimeout(function(){b.classList.remove('ok')},1200)}var e=document.getElementById('t2');e.classList.add('on');setTimeout(function(){e.classList.remove('on')},1200)})}
document.querySelectorAll('pre').forEach(function(p){if(p.parentNode.classList.contains('cb'))return;var w=document.createElement('div');w.className='cb';p.parentNode.insertBefore(w,p);w.appendChild(p);var b=document.querySelector('.cp').cloneNode(true);w.insertBefore(b,p)});
document.querySelectorAll('.cp').forEach(function(b){b.addEventListener('click',function(){cp(b.parentNode.querySelector('pre').innerText,b)})});
document.getElementById('copyAll').addEventListener('click',function(){var b=this;fetch('../AGENTS.md').then(function(r){return r.text()}).then(function(t){cp(t,b)})});
var t=document.getElementById('pEn');t.addEventListener('change',function(){document.getElementById('pEnBox').hidden=!t.checked;document.querySelectorAll('.one .pl').forEach(function(x){x.classList.toggle('off',t.checked)})});})();</script>"""
    ld = {'@context':'https://schema.org','@graph':[{'@type':'TechArticle','headline':'UI Hub guide for AI agents','url':BASE+'agents/','dateModified':UPD[:10]},
          {'@type':'FAQPage','mainEntity':[{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}} for q,a in FAQ]},
          {'@type':'HowTo','name':'Build a dark SaaS pricing page with UI Hub','step':[{'@type':'HowToStep','name':k,'text':v} for k,v in EX[0][1]]}]}
    w('agents/index.html', head('Guide for AI agents · UI Hub', U['ag_lede']['en'], 'agents/', ld, '../') + css + f"""<body>{topbar('../','agents')}<main class="wrap"><section class="hero" style="padding-bottom:18px"><p class="eb">Agents · GEO · Skill</p><h1>{ml('ag_title')}</h1><p class="lede">{ml('ag_lede')}</p></section>
{one}{acts}
<div class="grid2"><a class="box" href="../api/resources.json" style="text-decoration:none"><h3>/api/resources.json</h3><p>{ml(LS('c_res', n=N))}</p></a><a class="box" href="../api/skills.json" style="text-decoration:none"><h3>/api/skills.json</h3><p>{ml(LS('c_sk', n=len(skills)))}</p></a><a class="box" href="../llms.txt" style="text-decoration:none"><h3>/llms.txt</h3><p>{ml(I.S['c_llms'])}</p></a></div>
<section class="sec"><h2>{ml('a_install')}</h2>{swh}<div class="tw"><table><thead><tr><th>{ml(I.S['th_tool'])}</th><th>{ml(I.S['th_global'])}</th><th>{ml(I.S['th_proj'])}</th></tr></thead><tbody>{inst}</tbody></table></div><div style="height:12px"></div>{unzip}</section>
<section class="sec"><h2>{ml('a_for')}</h2>{uses}</section>
<section class="sec"><h2>{ml('a_wf')}</h2>{wf}</section>
<section class="sec"><h2>{ml('a_ex')}</h2><div class="exs">{ex}</div></section>
<section class="sec"><h2>{ml('a_snip')}</h2>{snips}</section>
<section class="sec"><h2>{ml('a_tab')}</h2>{tab}</section>
<section class="sec"><h2>{ml('a_do')}</h2>{dodont}</section>
<section class="sec"><h2>{ml('a_sk')}</h2><div class="grid2">{sk}</div></section>
<section class="sec"><h2>FAQ</h2>{fq}</section></main>{foot('../')}{SCRIPT}{js}</body></html>""")
