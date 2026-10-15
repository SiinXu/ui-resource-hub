"""Knowledge base (/kb/): skills, specs, notes (+ blog). Each entry: /kb/<type>/<slug>/ (HTML) + /kb/<type>/<slug>.md (raw).
Also writes api/kb.json, api/search-index.json, context-bundle.md. Called from build_extras.py."""
import os, re, json, glob, shutil
import markdown
SK_SRC = '/workspace/web-bot-skills'
# licence-checked: full text only where the skill or its upstream repo is MIT / Apache-2.0
FULL = {'accessibility':('MIT',None),'composition-patterns':('MIT','https://github.com/vercel-labs/agent-skills'),'performance':('MIT','https://github.com/addyosmani/web-quality-skills'),
 'react-best-practices':('MIT','https://github.com/vercel-labs/agent-skills'),'web-quality-audit':('MIT','https://github.com/addyosmani/web-quality-skills'),
 'frontend-design':('Apache-2.0','https://github.com/anthropics/skills'),'mcp-builder':('Apache-2.0','https://github.com/anthropics/skills'),'webapp-testing':('Apache-2.0','https://github.com/anthropics/skills'),
 'taste-skill':('MIT','https://github.com/Leonxlnx/taste-skill'),'impeccable':('Apache-2.0','https://github.com/pbakaus/impeccable'),
 'emil-design-eng':('MIT','https://github.com/emilkowalski/skills'),'baseline-ui':('MIT','https://github.com/ibelick/ui-skills')}
DIGEST_UP = {'web-design-guidelines':'https://github.com/vercel-labs/web-interface-guidelines','redesign-skill':'https://github.com/Leonxlnx/taste-skill'}
PRIVATE = {'workflow-ship-change','iterate-until-verified','secrets-management','deploy-to-vercel'}  # internal/ops, not published
def build(g):
    E, w, ml, U, BASE, ITEMS, UPD, ROOT, head, topbar, foot, SCRIPT, POSTS = [g[k] for k in 'E w ml U BASE ITEMS UPD ROOT head topbar foot SCRIPT POSTS'.split()]
    import sys; sys.path.insert(0, os.path.join(ROOT,'kb_src')); from specs import SPECS, NOTES
    src = os.path.join(ROOT,'kb_src','skills'); os.makedirs(src, exist_ok=True)
    if os.path.isdir(SK_SRC):
        for f in glob.glob(SK_SRC+'/*/SKILL.md'):
            n = f.split('/')[-2]
            if n in PRIVATE: continue
            if n in FULL: shutil.copy(f, os.path.join(src, n+'.md')); continue
            t = open(f, encoding='utf-8').read(); m = re.match(r'^---\n(.*?)\n---\n', t, re.S)
            fm = m.group(0) if m else ''; heads = re.findall(r'^#{2,3} .+$', t[len(fm):], re.M)[:24]
            open(os.path.join(src, n+'.md'),'w',encoding='utf-8').write(fm + '\n'.join(heads) + '\n')  # digest only: no full text stored
    entries = []
    for f in sorted(glob.glob(src+'/*.md')):
        n = os.path.basename(f)[:-3]; t = open(f, encoding='utf-8').read()
        m = re.match(r'^---\n(.*?)\n---\n', t, re.S); fm = m.group(1) if m else ''; body = t[m.end():] if m else t
        d = re.search(r'^description:\s*(.+)$', fm, re.M); desc = d.group(1).strip().strip('"\'') if d else ''
        if desc in ('|','>','|-','>-',''):
            d2 = re.search(r'^description:\s*[|>]-?\s*\n((?:[ \t]+.+\n?)+)', fm, re.M); desc = ' '.join(d2.group(1).split()) if d2 else ''
        if n in FULL:
            lic, up = FULL[n]
            md = f"# Skill: {n}\n\n> {desc}\n\n*Licence: {lic}" + (f" · Upstream: {up}" if up else '') + " · Redistributed unmodified below.*\n\n" + body
            full = True
        else:
            up = DIGEST_UP.get(n); heads = re.findall(r'^#{2,3} (.+)$', body, re.M)[:24]
            md = f"# Skill: {n}\n\n> {desc}\n\n*Digest only: full text not redistributed here" + (f"; see upstream {up}" if up else '') + ".*\n\n## Outline\n" + '\n'.join(f'- {h}' for h in heads) + '\n'
            full = False; lic = None
        cat = 'design' if n in ('frontend-design','taste-skill','impeccable','emil-design-eng','redesign-skill','baseline-ui','web-design-guidelines','accessibility') else 'engineering'
        entries.append(dict(type='skill', slug=n, title=n, summary=desc[:300], tags=[cat]+(['full-text'] if full else ['digest']), md=md, license=lic, upstream=up))
    for slug,title,summ,tags,body,refs in SPECS:
        md = f"# {title}\n\n> {summ}\n" + body + ("\n## Sources\n" + '\n'.join(f'- [{a}]({u})' for a,u in refs) if refs else '')
        entries.append(dict(type='spec', slug=slug, title=title, summary=summ, tags=tags, md=md))
    for slug,title,summ,tags,body,refs in NOTES:
        md = f"# {title}\n\n> {summ}\n" + body + ("\n## References\n" + '\n'.join(f'- [{a}]({u})' for a,u in refs) if refs else '')
        entries.append(dict(type='note', slug=slug, title=title, summary=summ, tags=tags, md=md))
    for p in POSTS:
        txt = re.sub(r'<h2>(.*?)</h2>', r'\n## \1\n', p['en']); txt = re.sub(r'<li>', '- ', txt); txt = re.sub(r'<pre><code>(.*?)</code></pre>', lambda m: '\n```\n'+m.group(1)+'\n```\n', txt, flags=re.S)
        txt = re.sub(r'<strong>(.*?)</strong>', r'**\1**', txt); txt = re.sub(r'<code>(.*?)</code>', r'`\1`', txt); txt = re.sub(r'<[^>]+>', '\n', txt)
        txt = re.sub(r'\n{3,}', '\n\n', txt).replace('&lt;','<').replace('&gt;','>').replace('&amp;','&').strip()
        md = f"# {p['t']['en']}\n\n> {p['s']['en']}\n\nBlog post: <{BASE}blog/{p['slug']}/>\n\n{txt}\n\n## References\n" + '\n'.join(f'- [{t}]({u}) — {a}' for t,a,u in p['refs'])
        entries.append(dict(type='note', slug='blog-'+p['slug'], title=p['t']['en'], summary=p['s']['en'], tags=['blog']+p['tags'], md=md))
    for e in entries:
        e['url'] = f"{BASE}kb/{e['type']}/{e['slug']}/"; e['raw'] = f"{BASE}kb/{e['type']}/{e['slug']}.md"
    U.update({'kb':dict(zh='百科',zht='百科',en='Encyclopedia',ja='百科',ko='백과',ms='Ensiklopedia',vi='Bách khoa',fr='Encyclopédie',es='Enciclopedia',de='Enzyklopädie'),
      'kb_title':dict(zh='UI 设计百科',zht='UI 設計百科',en='UI design encyclopedia',ja='UIデザイン百科',ko='UI 디자인 백과',ms='Ensiklopedia reka bentuk UI',vi='Bách khoa thiết kế UI',fr='Encyclopédie du design UI',es='Enciclopedia de diseño UI',de='UI-Design-Enzyklopädie'),
      'kb_lede':dict(zh='组件、资源、skill、设计规范与经验，一处搜索；每条都有固定链接和原始 Markdown，可直接作为 AI Agent 的上下文。',zht='元件、資源、skill、設計規範與經驗，一處搜尋；每條都有固定連結和原始 Markdown，可直接作為 AI Agent 的上下文。',en='Components, resources, skills, design specs and lessons in one search. Every entry has a stable URL and raw Markdown you can feed to an AI agent as context.',ja='コンポーネント、リソース、スキル、デザイン仕様、知見をひとつの検索で。各項目に固定URLと生Markdownがあり、AIエージェントの文脈にそのまま使えます。',ko='컴포넌트, 리소스, 스킬, 디자인 규범, 경험을 한 번에 검색. 모든 항목에 고정 URL과 원본 Markdown이 있어 AI 에이전트 컨텍스트로 쓸 수 있습니다.',ms='Komponen, sumber, kemahiran, spesifikasi reka bentuk dan pengajaran dalam satu carian. Setiap entri ada URL tetap dan Markdown mentah untuk konteks ejen AI.',vi='Component, tài nguyên, skill, quy chuẩn thiết kế và kinh nghiệm trong một ô tìm kiếm. Mỗi mục có URL cố định và Markdown gốc để làm ngữ cảnh cho AI agent.',fr='Composants, ressources, skills, specs de design et leçons dans une seule recherche. Chaque entrée a une URL stable et un Markdown brut utilisable comme contexte d’agent IA.',es='Componentes, recursos, skills, especificaciones de diseño y lecciones en una sola búsqueda. Cada entrada tiene URL estable y Markdown en bruto para usar como contexto de un agente de IA.',de='Komponenten, Ressourcen, Skills, Design-Specs und Erfahrungen in einer Suche. Jeder Eintrag hat eine feste URL und rohes Markdown als Kontext für KI-Agents.'),
      'kb_ph':dict(zh='搜索组件、skill、规范、经验…',zht='搜尋元件、skill、規範、經驗…',en='Search components, skills, specs, lessons…',ja='コンポーネント・スキル・仕様・知見を検索…',ko='컴포넌트, 스킬, 규범, 경험 검색…',ms='Cari komponen, kemahiran, spesifikasi…',vi='Tìm component, skill, quy chuẩn, kinh nghiệm…',fr='Rechercher composants, skills, specs…',es='Buscar componentes, skills, especificaciones…',de='Komponenten, Skills, Specs suchen…'),
      'kb_bundle':dict(zh='复制上下文包',zht='複製上下文包',en='Copy context bundle',ja='コンテキスト一式をコピー',ko='컨텍스트 번들 복사',ms='Salin himpunan konteks',vi='Sao chép gói ngữ cảnh',fr='Copier le pack de contexte',es='Copiar paquete de contexto',de='Kontext-Paket kopieren'),
      'kb_dl':dict(zh='下载上下文包 .md',zht='下載上下文包 .md',en='Download context bundle .md',ja='コンテキスト一式 .md',ko='컨텍스트 번들 .md 다운로드',ms='Muat turun himpunan .md',vi='Tải gói ngữ cảnh .md',fr='Télécharger le pack .md',es='Descargar paquete .md',de='Kontext-Paket .md laden'),
      'kb_raw':dict(zh='原始 Markdown',zht='原始 Markdown',en='Raw Markdown',ja='生Markdown',ko='원본 Markdown',ms='Markdown mentah',vi='Markdown gốc',fr='Markdown brut',es='Markdown en bruto',de='Rohes Markdown'),
      'kb_copy':dict(zh='复制 .md',zht='複製 .md',en='Copy .md',ja='.md をコピー',ko='.md 복사',ms='Salin .md',vi='Sao chép .md',fr='Copier le .md',es='Copiar .md',de='.md kopieren'),
      'kb_en':dict(zh='本条目正文为英文，作为 AI Agent 上下文使用。',zht='本條目正文為英文，作為 AI Agent 上下文使用。',en='',ja='この項目の本文は英語です（AIエージェントの文脈用）。',ko='이 항목의 본문은 영어입니다(AI 에이전트 컨텍스트용).',ms='Kandungan entri ini dalam bahasa Inggeris (untuk konteks ejen AI).',vi='Nội dung mục này bằng tiếng Anh (dùng làm ngữ cảnh cho AI agent).',fr='Le contenu de cette entrée est en anglais (contexte pour agents IA).',es='El contenido de esta entrada está en inglés (contexto para agentes de IA).',de='Der Inhalt dieses Eintrags ist auf Englisch (Kontext für KI-Agents).'),
      'kb_post':dict(zh='阅读博客原文',zht='閱讀部落格原文',en='Read the blog post',ja='ブログ記事を読む',ko='블로그 글 읽기',ms='Baca artikel blog',vi='Đọc bài blog',fr='Lire l’article',es='Leer el artículo',de='Blogbeitrag lesen'),
      'ty_skill':dict(zh='Skill',zht='Skill',en='Skill',ja='スキル',ko='스킬',ms='Kemahiran',vi='Skill',fr='Skill',es='Skill',de='Skill'),
      'ty_spec':dict(zh='设计规范',zht='設計規範',en='Spec',ja='仕様',ko='규범',ms='Spesifikasi',vi='Quy chuẩn',fr='Spécification',es='Especificación',de='Spezifikation'),
      'ty_note':dict(zh='笔记',zht='筆記',en='Note',ja='ノート',ko='노트',ms='Nota',vi='Ghi chú',fr='Note',es='Nota',de='Notiz'),
      'kb_all':dict(zh='全部',zht='全部',en='All',ja='すべて',ko='전체',ms='Semua',vi='Tất cả',fr='Tout',es='Todo',de='Alle')})
    css = """<style>.kbs{display:flex;gap:8px;align-items:center;padding:12px 14px;border-radius:14px;background:var(--surf);border:1px solid var(--line2);margin:6px 0 10px}.kbs input{flex:1;font:inherit;font-size:16px;border:0;background:none;color:var(--ink);outline:none}
.chips{display:flex;gap:6px;flex-wrap:wrap;margin:0 0 14px}.chips button{font:500 12.5px var(--sans);color:var(--ink2);background:var(--surf);border:1px solid var(--line);border-radius:99px;padding:5px 11px;cursor:pointer}.chips button.on{color:var(--bg);background:var(--ink);border-color:var(--ink)}
.res{display:grid;gap:10px;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));padding-bottom:30px}.r{display:flex;flex-direction:column;gap:6px;padding:14px 16px;border-radius:14px;background:var(--surf);border:1px solid var(--line);text-decoration:none}.r:hover{border-color:var(--acc)}
.r .k{font:500 11px var(--mono);text-transform:uppercase;letter-spacing:.06em;color:var(--acc)}.r b{font-size:15px}.r p{margin:0;color:var(--ink2);font-size:13px;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}.cnt{font:500 12px var(--mono);color:var(--ink3);margin:0 0 10px}
.acts{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 14px}.btn{font:500 13.5px var(--sans);text-decoration:none;color:var(--ink);background:var(--surf);border:1px solid var(--line2);border-radius:10px;padding:8px 13px;cursor:pointer}.btn.pri{background:var(--ink);color:var(--bg)}
.md table{border-collapse:collapse;width:100%;font-size:13.5px;display:block;overflow:auto}.md th,.md td{border:1px solid var(--line);padding:6px 9px;text-align:left}.md blockquote{margin:0;padding:2px 14px;border-left:3px solid var(--acc);color:var(--ink2)}.md a{color:var(--acc)}.md img{max-width:100%}.kba{margin:4px 0 18px}.kba .btn{font-size:13px;padding:7px 12px}.kbn{font-size:13px;color:var(--ink3);margin:0 0 14px;padding:8px 12px;border-radius:10px;background:var(--mat)}</style>"""
    copyjs = """<script>function cpx(t,b){(navigator.clipboard?navigator.clipboard.writeText(t):Promise.reject()).catch(function(){var a=document.createElement('textarea');a.value=t;document.body.appendChild(a);a.select();document.execCommand('copy');a.remove()}).finally(function(){if(b){var o=b.innerHTML;b.textContent='✓';setTimeout(function(){b.innerHTML=o},1200)}})}</script>"""
    # entry pages
    for e in entries:
        p = f"kb/{e['type']}/{e['slug']}"
        w(p+'.md', e['md'])
        html_body = markdown.markdown(e['md'], extensions=['fenced_code','tables'])
        h1m = re.match(r'\s*(<h1>.*?</h1>)', html_body, re.S); h1 = h1m.group(1) if h1m else ''; rest = html_body[h1m.end():] if h1m else html_body
        if e['slug'].startswith('blog-'):
            rest = re.sub(r'<p>Blog post: <a href="([^"]+)">[^<]*</a></p>', '', rest, count=1)
            postlink = f'<a class="btn" href="../../../blog/{e["slug"][5:]}/">{ml("kb_post")} →</a>'
        else: postlink = ''
        note = ''.join(f'<p class="kbn" data-l="{c}">{E(U["kb_en"][k])}</p>' for c,_,k in g['LANGS'] if U['kb_en'][k])
        ld = {'@context':'https://schema.org','@type':'TechArticle','headline':e['title'],'description':e['summary'],'url':e['url'],'dateModified':UPD[:10],'isPartOf':{'@type':'CollectionPage','name':'UI Hub encyclopedia','url':BASE+'kb/'},'encoding':{'@type':'MediaObject','contentUrl':e['raw'],'encodingFormat':'text/markdown'}}
        w(p+'/index.html', head(f"{e['title']} · UI Hub encyclopedia", e['summary'][:160] or e['title'], p+'/', ld, '../../../') + css + copyjs + f"""<body>{topbar('../../../','kb')}<article class="md"><p class="meta"><a href="../../">← {ml('kb')}</a> · {ml('ty_'+e['type'])} · {' · '.join(E(t) for t in e['tags'])}</p>
{h1}<div class="acts kba">{postlink}<a class="btn" href="../{e['slug']}.md">{ml('kb_raw')}</a><button class="btn" type="button" onclick="fetch('../{e['slug']}.md').then(r=>r.text()).then(t=>cpx(t,this))">{ml('kb_copy')}</button></div>{note}{rest}</article>{foot('../../../')}{SCRIPT}</body></html>""")
    # api
    kbj = [{k:e.get(k) for k in ('type','slug','title','summary','tags','url','raw','license','upstream','md')} for e in entries]
    w('api/kb.json', json.dumps({'updated':UPD,'count':len(kbj),'types':['skill','spec','note'],'entries':kbj}, ensure_ascii=False))
    idx = [{'t':e['title'],'k':e['type'],'u':f"kb/{e['type']}/{e['slug']}/",'r':f"kb/{e['type']}/{e['slug']}.md",'d':e['summary'][:200],'g':e['tags']} for e in entries]
    for i in ITEMS:
        idx.append({'t':i['name'],'k':'component' if i['type']=='style' else 'resource','u':i['url'],'d':(i.get('noteEn') or i.get('note') or '')[:160],'g':(i.get('ct') or [])+(i.get('vs') or [])+[i['type']]})
    w('api/search-index.json', json.dumps({'updated':UPD,'fields':{'t':'title','k':'kind: skill|spec|note|resource|component','u':'url (relative = on this site)','r':'raw markdown (kb only)','d':'description','g':'tags'},'items':idx}, ensure_ascii=False, separators=(',',':')))
    # context bundle
    agents = open(os.path.join(ROOT,'AGENTS.md'),encoding='utf-8').read()
    bundle = f"# UI Hub context bundle ({UPD})\n\nSource: {BASE}kb/ · Full skills: {BASE}api/kb.json\n\n" + agents + "\n\n---\n\n# Design specs\n\n" + '\n\n'.join(e['md'] for e in entries if e['type']=='spec') + \
             "\n\n---\n\n# House style & lessons\n\n" + '\n\n'.join(e['md'] for e in entries if e['type']=='note' and not e['slug'].startswith('blog-')) + \
             "\n\n---\n\n# Skills index (fetch raw .md for full text)\n\n" + '\n'.join(f"- **{e['title']}** ({', '.join(e['tags'])}): {e['summary'][:180]} — {e['raw']}" for e in entries if e['type']=='skill') + \
             "\n\n# Blog notes\n\n" + '\n'.join(f"- {e['title']} — {e['raw']}" for e in entries if e['slug'].startswith('blog-')) + "\n"
    w('context-bundle.md', bundle)
    # index page
    from collections import Counter
    cnt = Counter(e['type'] for e in entries)
    chips = ''.join(f'<button type="button" data-k="{k}"{" class=on" if k=="" else ""}>{lab}</button>' for k,lab in [('',ml('kb_all')),('skill','Skills'),('spec','Specs'),('note','Notes'),('component','Components'),('resource','Resources')])
    ld = {'@context':'https://schema.org','@graph':[{'@type':'CollectionPage','name':'UI Hub design encyclopedia','url':BASE+'kb/','dateModified':UPD[:10]},
          {'@type':'ItemList','itemListElement':[{'@type':'ListItem','position':n+1,'url':e['url'],'name':e['title']} for n,e in enumerate(entries)]}],
          'potentialAction':{'@type':'SearchAction','target':BASE+'kb/?q={search_term_string}','query-input':'required name=search_term_string'}}
    static = ''.join(f'<a class="r" href="{e["type"]}/{e["slug"]}/"><span class="k">{e["type"]}</span><b>{E(e["title"])}</b><p>{E(e["summary"])}</p></a>' for e in entries)
    w('kb/index.html', head('UI design encyclopedia · UI Hub', U['kb_lede']['en'], 'kb/', ld, '../') + css + copyjs + f"""<body>{topbar('../','kb')}<main class="wrap"><section class="hero" style="padding-bottom:16px"><p class="eb">KB · {cnt['skill']} skills · {cnt['spec']} specs · {cnt['note']} notes · {len(ITEMS)} resources</p><h1>{ml('kb_title')}</h1><p class="lede">{ml('kb_lede')}</p></section>
<div class="acts"><button class="btn pri" type="button" id="cb">{ml('kb_bundle')}</button><a class="btn" href="../context-bundle.md" download="ui-hub-context.md">{ml('kb_dl')}</a><a class="btn" href="../api/kb.json">api/kb.json</a><a class="btn" href="../api/search-index.json">api/search-index.json</a></div>
<label class="kbs"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg><input id="q" type="search" autocomplete="off">{''.join(f'<span data-l="{c}" hidden></span>' for c,_,_ in g['LANGS'])}</label>
<div class="chips" id="chips">{chips}</div><p class="cnt" id="cnt"></p><div class="res" id="res">{static}</div></main>{foot('../')}{SCRIPT}
<script>(function(){{var PH={json.dumps(U['kb_ph'],ensure_ascii=False)},M={{'zh-Hans':'zh','zh-Hant':'zht'}};function ph(){{var l=document.documentElement.lang;q.placeholder=PH[M[l]||l]||PH.en}}var q=document.getElementById('q'),res=document.getElementById('res'),cnt=document.getElementById('cnt'),K='',D=null;ph();document.getElementById('ls').addEventListener('change',ph);
var p=new URLSearchParams(location.search);if(p.get('q'))q.value=p.get('q');
function esc(s){{return String(s).replace(/[&<>"]/g,function(c){{return{{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}}[c]}})}}
function run(){{if(!D)return;var t=q.value.trim().toLowerCase().split(/\\s+/).filter(Boolean),out=[];for(var i=0;i<D.length;i++){{var x=D[i];if(K&&x.k!==K)continue;var h=(x.t+' '+x.d+' '+(x.g||[]).join(' ')).toLowerCase(),ok=true,s=0;for(var j=0;j<t.length;j++){{var at=h.indexOf(t[j]);if(at<0){{ok=false;break}}s+=x.t.toLowerCase().indexOf(t[j])>=0?3:1}}if(ok)out.push([s+(x.r?2:0),x])}}
out.sort(function(a,b){{return b[0]-a[0]}});cnt.textContent=out.length+' results';res.innerHTML=out.slice(0,120).map(function(o){{var x=o[1],ext=!x.r&&/^https?:/.test(x.u);return '<a class="r" href="'+esc(x.r?'../'+x.u:x.u)+'"'+(ext?' target="_blank" rel="noopener"':'')+'><span class="k">'+x.k+(x.r?' · md':'')+'</span><b>'+esc(x.t)+'</b><p>'+esc(x.d)+'</p></a>'}}).join('')}}
fetch('../api/search-index.json').then(function(r){{return r.json()}}).then(function(j){{D=j.items;run()}});q.addEventListener('input',run);
document.querySelectorAll('#chips button').forEach(function(b){{b.addEventListener('click',function(){{K=b.dataset.k;document.querySelectorAll('#chips button').forEach(function(x){{x.classList.toggle('on',x===b)}});run()}})}});
document.getElementById('cb').addEventListener('click',function(){{var b=this;fetch('../context-bundle.md').then(function(r){{return r.text()}}).then(function(t){{cpx(t,b)}})}})}})();</script></body></html>""")
    return entries
