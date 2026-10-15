"""Analytics + GEO + newsletter injection for every UI Hub page (idempotent; runs at the end of build_extras.py).
- Cloudflare Web Analytics (siinxu.github.io site tag) + stats.incidental.site events.js (site=ui-hub, conversion = copy) + subscribe.js
- Organization (Incidental AI) + BreadcrumbList JSON-LD, GEO intro (what / who / numbers) in 10 languages, inline newsletter block
- robots.txt with AI crawlers, sitemap index + per-locale sitemaps"""
import os, re, json, glob
from collections import Counter
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = 'https://siinxu.github.io/ui-resource-hub/'
LC = ['zh-Hans','zh-Hant','en','ja','ko','ms','vi','fr','es','de']
D = json.load(open(os.path.join(ROOT, 'data.json'), encoding='utf-8'))
ITEMS = D['items']; tc = Counter(i['type'] for i in ITEMS); N = len(ITEMS); LIB = tc.get('library', 0); STY = tc.get('style', 0)
f = lambda n: f'{n:,}'
INTRO = {
 'zh-Hans': f'UI Hub 是一个每日更新的免费 UI 资源目录，给设计师、前端开发者和做界面的 AI Agent 用：共 {f(N)} 条资源，其中 {f(LIB)} 个组件库、{f(STY)} 个带明暗预览的组件样式示例，另有设计 skill 与 AI 设计技巧文章。',
 'zh-Hant': f'UI Hub 是一個每日更新的免費 UI 資源目錄，給設計師、前端開發者和做介面的 AI Agent 用：共 {f(N)} 條資源，其中 {f(LIB)} 個元件庫、{f(STY)} 個附明暗預覽的元件樣式示例，另有設計 skill 與 AI 設計技巧文章。',
 'en': f'UI Hub is a free, daily-updated directory of UI resources for designers, front-end developers and AI agents that build interfaces: {f(N)} resources, including {f(LIB)} component libraries and {f(STY)} component style demos with light/dark previews, plus design skills and AI design articles.',
 'ja': f'UI Hub は、デザイナー・フロントエンド開発者・UI を作る AI エージェント向けの、毎日更新される無料の UI リソース集です。全 {f(N)} 件（コンポーネントライブラリ {f(LIB)} 件、ライト/ダーク対応のスタイルデモ {f(STY)} 件）に加え、デザインスキルと AI デザイン記事を掲載しています。',
 'ko': f'UI Hub는 디자이너, 프론트엔드 개발자, 인터페이스를 만드는 AI 에이전트를 위한 매일 업데이트되는 무료 UI 리소스 디렉터리입니다. 총 {f(N)}개 리소스(컴포넌트 라이브러리 {f(LIB)}개, 라이트/다크 미리보기가 있는 스타일 데모 {f(STY)}개)와 디자인 스킬, AI 디자인 글을 제공합니다.',
 'ms': f'UI Hub ialah direktori sumber UI percuma yang dikemas kini setiap hari untuk pereka, pembangun front-end dan ejen AI yang membina antara muka: {f(N)} sumber, termasuk {f(LIB)} pustaka komponen dan {f(STY)} demo gaya komponen dengan pratonton terang/gelap, serta kemahiran reka bentuk dan artikel reka bentuk AI.',
 'vi': f'UI Hub là danh mục tài nguyên UI miễn phí, cập nhật hằng ngày, dành cho nhà thiết kế, lập trình viên front-end và AI agent dựng giao diện: {f(N)} tài nguyên, gồm {f(LIB)} thư viện component và {f(STY)} mẫu phong cách component có xem trước sáng/tối, cùng skill thiết kế và bài viết về thiết kế với AI.',
 'fr': f'UI Hub est un annuaire gratuit de ressources UI, mis à jour chaque jour, pour designers, développeurs front-end et agents IA qui construisent des interfaces : {f(N)} ressources, dont {f(LIB)} bibliothèques de composants et {f(STY)} démos de styles avec aperçus clair/sombre, plus des skills de design et des articles sur le design avec l’IA.',
 'es': f'UI Hub es un directorio gratuito de recursos de UI, actualizado a diario, para diseñadores, desarrolladores front-end y agentes de IA que construyen interfaces: {f(N)} recursos, incluidas {f(LIB)} bibliotecas de componentes y {f(STY)} demos de estilos con vista clara/oscura, además de skills de diseño y artículos de diseño con IA.',
 'de': f'UI Hub ist ein kostenloses, täglich aktualisiertes Verzeichnis von UI-Ressourcen für Designer, Frontend-Entwickler und KI-Agents, die Oberflächen bauen: {f(N)} Ressourcen, darunter {f(LIB)} Komponentenbibliotheken und {f(STY)} Komponenten-Stildemos mit Hell/Dunkel-Vorschau, dazu Design-Skills und Artikel zu KI-Design.'}
ALIAS = {'zh-Hans': ['zh-Hans', 'zh-CN', 'zh'], 'zh-Hant': ['zh-Hant', 'zh-TW']}
css_show = ','.join(f'html[lang="{a}"] .geo-intro [data-gl="{c}"]' for c in LC for a in ALIAS.get(c, [c]))
STYLE = ('<style id="ia-growth">.geo-intro{max-width:var(--max,1120px);margin:10px auto 0;padding:0 20px;font-size:12.5px;line-height:1.55;color:var(--ink3,#878da0)}@media(min-width:900px){.geo-intro{padding:0 40px}}'
         '.geo-intro [data-gl]{display:none}' + css_show + '{display:inline}'
         '.sub-band{max-width:var(--max,1120px);margin:0 auto;padding:0 20px;--ie-acc:var(--acc,#2563eb);--ie-acc-ink:var(--bg,#fff)}@media(min-width:900px){.sub-band{padding:0 40px}}'
         + open(os.path.join(os.path.dirname(__file__), 'subscribe.css')).read().replace('\n', '') + '</style>')
TOKEN = '41d8abdb6f1247c08f2412afcd5f2143'
ORG = {'@type': 'Organization', '@id': 'https://incidental.site/#org', 'name': 'Incidental AI', 'alternateName': '偶然 AI', 'url': 'https://incidental.site/'}
SEC = {'blog': 'Blog', 'kb': 'Encyclopedia', 'agents': 'For agents'}
def crumbs(rel, title):
    if not rel: return None
    parts = rel.strip('/').split('/'); L = [('UI Hub', BASE)]
    if parts[0] in SEC and len(parts) > 1: L.append((SEC[parts[0]], BASE + parts[0] + '/'))
    L.append((title, BASE + rel))
    return {'@type': 'BreadcrumbList', 'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': u} for i, (n, u) in enumerate(L)]}
def inject(path):
    rel = os.path.relpath(path, ROOT).replace(os.sep, '/'); rel = re.sub(r'(^|/)index\.html$', r'\1', rel)
    s = open(path, encoding='utf-8').read()
    s = re.sub(r'<!--IA-->.*?<!--/IA-->', '', s, flags=re.S)
    title = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', (re.search(r'<title>(.*?)</title>', s, re.S) or [None, 'UI Hub'])[1])).replace('&amp;', '&').split(' — ')[0].split(' · ')[0].strip()
    g = [ORG]; c = crumbs(rel, title)
    if c: g.append(c)
    ld = json.dumps({'@context': 'https://schema.org', '@graph': g}, ensure_ascii=False).replace('<', '\\u003c')
    head = (f'<!--IA--><script type="application/ld+json">{ld}</script>{STYLE}'
            f'<script defer src="https://static.cloudflareinsights.com/beacon.min.js" data-cf-beacon=\'{{"token":"{TOKEN}"}}\'></script>'
            '<script defer src="https://stats.incidental.site/events.js" data-site="ui-hub" data-goal="copy"></script><script defer src="https://stats.incidental.site/subscribe.js"></script><!--/IA-->')
    s = s.replace('</head>', head + '</head>', 1)
    intro = '<!--IA--><p class="geo-intro">' + ''.join(f'<span data-gl="{k}" lang="{k}">{v}</span>' for k, v in INTRO.items()) + '</p><!--/IA-->'
    s = s.replace('</header>', '</header>' + intro, 1)
    sub = f'<!--IA--><aside class="sub-band" aria-label="Newsletter"><div data-ie-sub data-site="ui-hub" data-source="{rel or "home"}"></div></aside><!--/IA-->'
    s = s.replace('<footer', sub + '<footer', 1) if '<footer' in s else s.replace('</body>', sub + '</body>', 1)
    open(path, 'w', encoding='utf-8').write(s)
def run():
    pages = [os.path.join(ROOT, 'index.html')] + [p for d in ('blog', 'kb', 'agents') for p in glob.glob(os.path.join(ROOT, d, '**', 'index.html'), recursive=True)]
    for p in pages: inject(p)
    # robots + sitemaps
    sm = open(os.path.join(ROOT, 'sitemap.xml'), encoding='utf-8').read()
    if '<sitemapindex' not in sm: open(os.path.join(ROOT, 'sitemap-default.xml'), 'w', encoding='utf-8').write(sm)
    dm = open(os.path.join(ROOT, 'sitemap-default.xml'), encoding='utf-8').read()
    locs = re.findall(r'<url><loc>([^<]+)</loc><lastmod>([^<]+)</lastmod>', dm)
    names = ['sitemap-default.xml']
    for c in LC:
        n = f'sitemap-{c}.xml'; names.append(n)
        open(os.path.join(ROOT, n), 'w', encoding='utf-8').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + '\n'.join(f'<url><loc>{u}?lang={c}</loc><lastmod>{d}</lastmod></url>' for u, d in locs) + '\n</urlset>\n')
    open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8').write('<?xml version="1.0" encoding="UTF-8"?>\n<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + '\n'.join(f'<sitemap><loc>{BASE}{n}</loc></sitemap>' for n in names) + '\n</sitemapindex>\n')
    bots = ['GPTBot', 'OAI-SearchBot', 'ChatGPT-User', 'ClaudeBot', 'Claude-Web', 'PerplexityBot', 'Google-Extended', 'Applebot-Extended']
    open(os.path.join(ROOT, 'robots.txt'), 'w').write('User-agent: *\nAllow: /\n\n# AI / generative search crawlers are welcome\n' + '\n'.join(f'User-agent: {b}\nAllow: /' for b in bots) + f'\n\nSitemap: {BASE}sitemap.xml\n# LLM-friendly index: {BASE}llms.txt\n')
    print('growth: injected', len(pages), 'pages')
if __name__ == '__main__': run()
