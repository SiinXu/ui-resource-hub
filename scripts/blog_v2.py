"""Blog v2 builder: index with search, category filter, featured, series, reading time; post pages with series nav + related; RSS."""
import re, json
from email.utils import format_datetime
import datetime as _dt
CATS = {
 'all': dict(zh='全部',zht='全部',en='All',ja='すべて',ko='전체',ms='Semua',vi='Tất cả',fr='Tout',es='Todo',de='Alle'),
 'tools': dict(zh='工具评测',zht='工具評測',en='Tools',ja='ツール',ko='도구',ms='Alat',vi='Công cụ',fr='Outils',es='Herramientas',de='Tools'),
 'workflow': dict(zh='工作流',zht='工作流',en='Workflow',ja='ワークフロー',ko='워크플로',ms='Aliran kerja',vi='Quy trình',fr='Workflow',es='Flujo de trabajo',de='Workflow'),
 'components': dict(zh='组件库深读',zht='元件庫深讀',en='Component libraries',ja='コンポーネント',ko='컴포넌트',ms='Pustaka komponen',vi='Thư viện component',fr='Bibliothèques',es='Bibliotecas',de='Komponenten'),
 'craft': dict(zh='设计手艺',zht='設計手藝',en='Craft',ja='クラフト',ko='디자인 기본기',ms='Kemahiran',vi='Tay nghề',fr='Savoir-faire',es='Oficio',de='Handwerk'),
 'agents': dict(zh='Agent 上下文',zht='Agent 上下文',en='Agent context',ja='エージェント文脈',ko='에이전트 컨텍스트',ms='Konteks ejen',vi='Ngữ cảnh agent',fr='Contexte agent',es='Contexto de agentes',de='Agent-Kontext'),
 'teardown': dict(zh='案例拆解',zht='案例拆解',en='Teardowns',ja='分解',ko='해부',ms='Bedah kes',vi='Mổ xẻ',fr='Décorticages',es='Análisis',de='Analysen'),
 'news': dict(zh='周报动态',zht='週報動態',en='News',ja='ニュース',ko='뉴스',ms='Berita',vi='Tin tức',fr='Actus',es='Noticias',de='News'),
 'tutorial': dict(zh='教程',zht='教學',en='Tutorials',ja='チュートリアル',ko='튜토리얼',ms='Tutorial',vi='Hướng dẫn',fr='Tutoriels',es='Tutoriales',de='Tutorials'),
}
SERIES = {
 'prompt-to-ui': dict(zh='提示生成界面工具系列',zht='提示產生介面工具系列',en='Series: Prompt-to-UI tools',ja='シリーズ：プロンプトUIツール',ko='시리즈: 프롬프트-UI 도구',ms='Siri: Alat prompt-ke-UI',vi='Loạt bài: Công cụ prompt-to-UI',fr='Série : outils prompt-to-UI',es='Serie: herramientas prompt-to-UI',de='Serie: Prompt-to-UI-Tools'),
 'library-deep-dive': dict(zh='组件库深读系列',zht='元件庫深讀系列',en='Series: Library deep dives',ja='シリーズ：ライブラリ徹底解説',ko='시리즈: 라이브러리 심층 분석',ms='Siri: Pustaka mendalam',vi='Loạt bài: Thư viện chuyên sâu',fr='Série : bibliothèques en profondeur',es='Serie: bibliotecas a fondo',de='Serie: Bibliotheken im Detail'),
 'agent-context': dict(zh='给 Agent 的设计上下文系列',zht='給 Agent 的設計上下文系列',en='Series: Design context for agents',ja='シリーズ：エージェントのデザイン文脈',ko='시리즈: 에이전트용 디자인 컨텍스트',ms='Siri: Konteks reka bentuk untuk ejen',vi='Loạt bài: Ngữ cảnh thiết kế cho agent',fr='Série : contexte design pour agents',es='Serie: contexto de diseño para agentes',de='Serie: Designkontext für Agents'),
 'weekly': dict(zh='每周动态',zht='每週動態',en='Series: Weekly roundup',ja='シリーズ：週刊まとめ',ko='시리즈: 주간 정리',ms='Siri: Ringkasan mingguan',vi='Loạt bài: Tổng hợp tuần',fr='Série : revue hebdo',es='Serie: resumen semanal',de='Serie: Wochenrückblick'),
}
S2 = {
 'featured': dict(zh='精选',zht='精選',en='Featured',ja='注目',ko='추천',ms='Pilihan',vi='Nổi bật',fr='À la une',es='Destacados',de='Empfohlen'),
 'allposts': dict(zh='全部文章',zht='全部文章',en='All posts',ja='すべての記事',ko='모든 글',ms='Semua artikel',vi='Tất cả bài viết',fr='Tous les articles',es='Todos los artículos',de='Alle Beiträge'),
 'min': dict(zh='分钟阅读',zht='分鐘閱讀',en='min read',ja='分で読めます',ko='분 읽기',ms='min bacaan',vi='phút đọc',fr='min de lecture',es='min de lectura',de='Min. Lesezeit'),
 'search': dict(zh='搜索文章、标签、工具…',zht='搜尋文章、標籤、工具…',en='Search posts, tags, tools…',ja='記事・タグ・ツールを検索…',ko='글, 태그, 도구 검색…',ms='Cari artikel, tag, alat…',vi='Tìm bài, thẻ, công cụ…',fr='Rechercher articles, tags, outils…',es='Buscar artículos, etiquetas, herramientas…',de='Beiträge, Tags, Tools suchen…'),
 'none': dict(zh='没有匹配的文章',zht='沒有符合的文章',en='No matching posts',ja='該当する記事はありません',ko='일치하는 글이 없습니다',ms='Tiada artikel sepadan',vi='Không có bài phù hợp',fr='Aucun article correspondant',es='No hay artículos',de='Keine passenden Beiträge'),
 'related': dict(zh='相关文章',zht='相關文章',en='Related posts',ja='関連記事',ko='관련 글',ms='Artikel berkaitan',vi='Bài liên quan',fr='Articles liés',es='Artículos relacionados',de='Ähnliche Beiträge'),
 'inseries': dict(zh='本系列',zht='本系列',en='In this series',ja='このシリーズ',ko='이 시리즈',ms='Dalam siri ini',vi='Trong loạt bài',fr='Dans cette série',es='En esta serie',de='In dieser Serie'),
 'rss': dict(zh='RSS 订阅',zht='RSS 訂閱',en='RSS feed',ja='RSSフィード',ko='RSS 피드',ms='Suapan RSS',vi='Nguồn RSS',fr='Flux RSS',es='Feed RSS',de='RSS-Feed'),
 'posts_n': dict(zh='篇文章',zht='篇文章',en='posts',ja='件の記事',ko='개의 글',ms='artikel',vi='bài viết',fr='articles',es='artículos',de='Beiträge'),
}
OLDCAT = {'ai-assisted-ui-design-workflow':'workflow','prompts-for-ui':'workflow','design-to-code-with-ai':'workflow','taste-and-skills-for-agents':'agents',
          'component-composition':'components','motion-that-feels-right':'craft','dark-mode-done-right':'craft','accessibility-in-ai-generated-ui':'craft'}
OLDSERIES = {'taste-and-skills-for-agents':'agent-context'}
EXTRA_CSS = """.tools{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin:8px 0 6px}.q{flex:1 1 260px;font:inherit;font-size:14.5px;color:var(--ink);background:var(--surf);border:1px solid var(--line2);border-radius:12px;padding:10px 14px;outline:none}.q:focus{border-color:var(--acc)}
.chips{display:flex;flex-wrap:wrap;gap:6px;margin:6px 0 4px}.chip{font:inherit;font-size:13px;color:var(--ink2);background:transparent;border:1px solid var(--line2);border-radius:99px;padding:5px 12px;cursor:pointer}.chip.on,.chip:hover{color:var(--ink);background:var(--mat);border-color:var(--ink3)}
.chip b{font-weight:500;color:var(--ink3);margin-left:4px;font-size:11.5px}.rssb{font:500 12.5px var(--mono);color:var(--acc);text-decoration:none;border:1px solid var(--line2);border-radius:99px;padding:6px 12px}
.sh{font:400 30px/1.1 var(--serif);margin:34px 0 4px;letter-spacing:-.01em}.sh small{font:500 12px var(--mono);color:var(--ink3);margin-left:10px;letter-spacing:0}
.feat{display:grid;gap:14px;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));padding:14px 0 0}.feat .pc h2{font-size:21px}
.ser{display:grid;gap:14px;grid-template-columns:repeat(auto-fill,minmax(330px,1fr));padding:14px 0 0}.sbox{padding:18px 20px;border-radius:16px;background:var(--surf);border:1px solid var(--line)}.sbox h3{font:400 22px/1.15 var(--serif);margin:0 0 8px}
.sbox ol{margin:0;padding-left:20px}.sbox li{margin:5px 0;color:var(--ink2);font-size:14px}.sbox a{text-decoration:none}.sbox a:hover{color:var(--acc)}
.pc .mt{display:flex;gap:8px;flex-wrap:wrap;font:500 11.5px var(--mono);color:var(--ink3)}.pc .ct{color:var(--acc)}
#grid .pc:first-child{grid-column:auto;flex-direction:column}#grid .pc:first-child .cv{width:100%;border-right:0;border-bottom:1px solid var(--line)}#grid .pc:first-child h2{font-size:23px}#grid .pc:first-child .pb{padding:16px 18px 18px}
.feat .pc:first-child{grid-column:1/-1}@media(min-width:900px){.feat .pc:first-child{flex-direction:row;align-items:center}.feat .pc:first-child .cv{width:58%;border-bottom:0;border-right:1px solid var(--line)}.feat .pc:first-child h2{font-size:34px}.feat .pc:first-child .pb{padding:28px}}
.empty{color:var(--ink3);padding:30px 0;display:none}
.snav{margin:30px 0 0;padding:16px 18px;border-radius:14px;background:var(--surf);border:1px solid var(--line)}.snav h3{margin:0 0 6px;font:500 12px var(--mono);color:var(--ink3);text-transform:uppercase;letter-spacing:.06em}.snav ol{margin:0;padding-left:20px}.snav li{margin:3px 0;font-size:14px}.snav li.cur{color:var(--ink);font-weight:600}.snav a{color:var(--ink2)}
.rel{display:grid;gap:12px;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));margin-top:12px}.rel .pc h2{font-size:18px}.rel .pc p{display:none}"""
def build(G):
    POSTS, ml, E, w, head, topbar, foot, SCRIPT, BASE, LANGS, with_figs, U, L = (G[k] for k in 'POSTS ml E w head topbar foot SCRIPT BASE LANGS with_figs U L'.split())
    for p in POSTS:
        p.setdefault('cat', OLDCAT.get(p['slug'],'workflow')); p.setdefault('series', OLDSERIES.get(p['slug'])); p.setdefault('featured', False)
        zhc = len(re.sub(r'<[^>]+>|\s','',p['zh'])); enw = len(re.sub(r'<[^>]+>',' ',p['en']).split())
        p['mins_zh'] = max(2, round(zhc/400)); p['mins_en'] = max(2, round(enw/220))
    css = '<style>'+EXTRA_CSS+'</style>'
    def rt(p):  # reading time, localized
        return ''.join(f'<span data-l="{c}">{p["mins_zh"] if k in ("zh","zht") else p["mins_en"]} {E(S2["min"].get(k) or S2["min"]["en"])}</span>' for c,_,k in LANGS)
    def card(p, root='', eager=False):
        txt = ' '.join([p['t'][k] for k in p['t']] + [p['s']['en'], p['s']['zh']] + p['tags'] + [p['cat']]).lower()
        return (f'<a class="pc" href="{root}{p["slug"]}/" data-cat="{p["cat"]}" data-q="{E(txt)}"><img class="cv" src="{root}img/{p["slug"]}-cover.webp" alt="" loading="{"eager" if eager else "lazy"}" width="1200" height="630">'
                f'<div class="pb"><div class="mt"><span class="ct">{ml(CATS[p["cat"]])}</span><span>{p["date"]}</span><span>{rt(p)}</span></div><h2>{ml(p["t"])}</h2><p>{ml(p["s"])}</p><div class="tg">'+''.join(f'<span>{E(t)}</span>' for t in p['tags'])+'</div></div></a>')
    order = sorted(POSTS, key=lambda p:(p['date'], POSTS.index(p)), reverse=True)
    feat = [p for p in order if p['featured']][:4]
    counts = {c: sum(1 for p in POSTS if p['cat']==c) for c in CATS if c!='all'}
    chips = f'<button class="chip on" data-c="all">{ml(CATS["all"])}<b>{len(POSTS)}</b></button>' + ''.join(f'<button class="chip" data-c="{c}">{ml(CATS[c])}<b>{n}</b></button>' for c,n in counts.items() if n)
    ser = ''.join(f'<div class="sbox"><h3>{ml(SERIES[s])}</h3><ol>'+''.join(f'<li><a href="{p["slug"]}/">{ml(p["t"])}</a></li>' for p in POSTS if p['series']==s)+'</ol></div>' for s in SERIES if any(p['series']==s for p in POSTS))
    ph = json.dumps({c: S2['search'].get(k) or S2['search']['en'] for c,_,k in LANGS}, ensure_ascii=False)
    js = """<script>(function(){var q=document.getElementById('q'),cs=document.querySelectorAll('.chip'),cards=document.querySelectorAll('#grid .pc'),em=document.getElementById('empty'),cur='all',PH=%s;
function ph(){q.placeholder=PH[document.documentElement.lang]||PH.en}ph();document.getElementById('ls').addEventListener('change',ph);
var u=new URLSearchParams(location.search);if(u.get('q'))q.value=u.get('q');if(u.get('cat'))cur=u.get('cat');
function run(){var t=q.value.trim().toLowerCase(),n=0,f=!t&&cur==='all';document.querySelectorAll('.fx').forEach(function(e){e.style.display=f?'':'none'});
cards.forEach(function(c){var ok=(cur==='all'||c.dataset.cat===cur)&&(!t||t.split(/\\s+/).every(function(w){return c.dataset.q.indexOf(w)>=0}));c.style.display=ok?'':'none';if(ok)n++});
em.style.display=n?'none':'block';cs.forEach(function(b){b.classList.toggle('on',b.dataset.c===cur)})}
q.addEventListener('input',run);cs.forEach(function(b){b.onclick=function(){cur=b.dataset.c;run()}});run()})();</script>""" % ph
    ld = {'@context':'https://schema.org','@graph':[{'@type':'Blog','name':U['blog_title']['en'],'url':BASE+'blog/','inLanguage':[c for c,_,_ in LANGS]},
          {'@type':'ItemList','itemListElement':[{'@type':'ListItem','position':i+1,'url':BASE+f'blog/{p["slug"]}/','name':p['t']['en']} for i,p in enumerate(order)]}]}
    rsslink = f'<link rel="alternate" type="application/rss+xml" title="UI Hub Blog" href="{BASE}blog/rss.xml">'
    h = head('AI Design Techniques Blog · UI Hub', U['blog_lede']['en'], 'blog/', ld, '../').replace('</head>', rsslink+css+'</head>')
    w('blog/index.html', h + f"""<body>{topbar('../','blog')}<main class="wrap"><section class="hero"><p class="eb">Blog · {len(POSTS)} {ml(S2['posts_n'])}</p><h1>{ml('blog_title')}</h1><p class="lede">{ml('blog_lede')}</p></section>
<div class="tools"><input id="q" class="q" type="search" aria-label="Search"><a class="rssb" href="rss.xml">RSS · {ml(S2['rss'])}</a></div><div class="chips">{chips}</div>
<div class="fx"><h2 class="sh">{ml(S2['featured'])}</h2><div class="feat">{''.join(card(p, eager=i<3) for i,p in enumerate(feat))}</div>
<div class="ser">{ser}</div></div>
<h2 class="sh">{ml(S2['allposts'])}<small>{len(POSTS)}</small></h2><div class="posts" id="grid">{''.join(card(p) for p in order)}</div><p class="empty" id="empty">{ml(S2['none'])}</p></main>{foot('../')}{SCRIPT}{js}</body></html>""")
    # posts
    for p in POSTS:
        refs = '<ol>'+''.join(f'<li><a href="{E(u)}" rel="noopener" target="_blank">{E(t)}</a> — {E(a)}</li>' for t,a,u in p['refs'])+'</ol>'
        body = ''.join(f'<div data-l="{c}">' + (f'<p class="note">{E(L("body_note",k))}</p>' if L('body_note',k) else '') + with_figs(p['zh'] if k in ('zh','zht') else p['en'], p['slug'], k, '../../') + '</div>' for c,_,k in LANGS)
        snav = ''
        if p['series']:
            sp = [x for x in POSTS if x['series']==p['series']]
            snav = f'<nav class="snav"><h3>{ml(S2["inseries"])} · {ml(SERIES[p["series"]])}</h3><ol>'+''.join(f'<li class="cur">{ml(x["t"])}</li>' if x is p else f'<li><a href="../{x["slug"]}/">{ml(x["t"])}</a></li>' for x in sp)+'</ol></nav>'
        score = lambda x: (x['cat']==p['cat'])*2 + len(set(t.lower() for t in x['tags']) & set(t.lower() for t in p['tags'])) + (x['series']==p['series'] and p['series'] is not None)
        rel = sorted([x for x in POSTS if x is not p], key=lambda x:-score(x))[:3]
        relh = f'<section class="refs"><h2>{ml(S2["related"])}</h2><div class="rel">'+''.join(card(x,'../').replace('src="../img/','src="../img/') for x in rel)+'</div></section>'
        ld = {'@context':'https://schema.org','@type':'BlogPosting','headline':p['t']['en'],'alternativeHeadline':p['t']['zh'],'description':p['s']['en'],'datePublished':p['date'],'dateModified':p['date'],
              'inLanguage':['en','zh-Hans'],'author':{'@type':'Organization','name':'UI Hub','url':BASE},'publisher':{'@type':'Organization','name':'UI Hub','url':BASE},'mainEntityOfPage':BASE+f'blog/{p["slug"]}/','articleSection':CATS[p['cat']]['en'],'timeRequired':f'PT{p["mins_en"]}M',
              'citation':[{'@type':'CreativeWork','name':t,'author':a,'url':u} for t,a,u in p['refs']],'keywords':', '.join(p['tags']),'image':BASE+f'blog/img/{p["slug"]}-cover.webp'}
        h = head(p['t']['en']+' · UI Hub', p['s']['en'], f'blog/{p["slug"]}/', ld, '../../', f'blog/img/{p["slug"]}-cover.jpg').replace('</head>', rsslink+css+'</head>')
        w(f'blog/{p["slug"]}/index.html', h + f"""<body>{topbar('../../','blog')}<article><p class="meta"><a href="../">← {ml('back')}</a> · <a href="../?cat={p['cat']}">{ml(CATS[p['cat']])}</a> · {p['date']} · {rt(p)}</p>
<h1>{ml(p['t'])}</h1><p class="lede">{ml(p['s'])}</p><figure class="hc"><img src="../img/{p['slug']}-cover.webp" alt="{E(p['t']['en'])}" width="1200" height="630" fetchpriority="high"></figure>{body}{snav}<section class="refs"><h2>{ml('refs')}</h2>{refs}</section>{relh}</article>{foot('../../')}{SCRIPT}</body></html>""")
    w('api/blog.json', json.dumps({'count':len(POSTS),'rss':BASE+'blog/rss.xml','categories':{c:v['en'] for c,v in CATS.items() if c!='all'},'series':{c:v['en'] for c,v in SERIES.items()},
        'posts':[{'slug':p['slug'],'url':BASE+f'blog/{p["slug"]}/','date':p['date'],'category':p['cat'],'series':p['series'],'featured':p['featured'],'tags':p['tags'],'title':p['t'],'summary':p['s'],
                  'reading_minutes':{'en':p['mins_en'],'zh':p['mins_zh']},'cover':BASE+f'blog/img/{p["slug"]}-cover.webp','references':[{'title':t,'by':a,'url':u} for t,a,u in p['refs']]} for p in order]}, ensure_ascii=False, indent=1))
    # RSS
    def rfc(d): return format_datetime(_dt.datetime.fromisoformat(d+'T08:00:00+00:00'))
    items = ''.join(f"""<item><title>{E(p['t']['en'])}</title><link>{BASE}blog/{p['slug']}/</link><guid isPermaLink="true">{BASE}blog/{p['slug']}/</guid><pubDate>{rfc(p['date'])}</pubDate><category>{E(CATS[p['cat']]['en'])}</category><description>{E(p['s']['en']+' / '+p['s']['zh'])}</description><enclosure url="{BASE}blog/img/{p['slug']}-cover.jpg" type="image/jpeg" length="0"/></item>\n""" for p in order)
    w('blog/rss.xml', f"""<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom"><channel><title>UI Hub · AI Design Techniques Blog</title><link>{BASE}blog/</link><atom:link href="{BASE}blog/rss.xml" rel="self" type="application/rss+xml"/><description>{E(U['blog_lede']['en'])}</description><language>en</language><lastBuildDate>{rfc(order[0]['date'])}</lastBuildDate>\n{items}</channel></rss>\n""")
