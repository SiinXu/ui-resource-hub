import json
K = ['rt_h','rt_all','vs_h','vs_all','kv_rt','kv_vs','tag_site','code_doc','t_system','t_spec','t_tutorial','t_tool','t_collection',
 'sec_10','sec_11','sec_12','sec_13','sec_14','sec_15']
RT = ['design-system','component-library','component-demo','motion','skill','mcp','design-md','tokens-spec','a11y','anti-slop','tutorial','course','newsletter','inspiration','template','generator','tool','assets','directory']
VS = ['minimal','swiss','editorial','brutalist','glass','neumorphism','skeuomorphic','material','fluent','apple','enterprise','playful','soft','dark-tech','gradient','3d','motion','retro','industrial','utilitarian']
L = {
'zh-CN': (['资源类型','全部类型','页面风格','全部风格','资源类型','页面风格','网站首页截图','官方文档 / 规范 / 教程，没有可复制的源码；原站原文说明见上方','设计系统','规范','教程','工具','合集',
  'Agent 设计 Skills · 新增','大厂 UED / 设计系统','设计教程','组件风格与 Token 规范','UI 灵感站与素材 · 新增','AI Coding × 设计'],
  ['大厂设计系统','组件库','组件演示','动效特效','Agent Skill','MCP 接入','DESIGN.md / llms.txt','Token 与规范','无障碍','去 AI 味','教程文章','课程','资讯周刊','灵感图库','模板应用','AI 生成','设计工具','图标字体素材','合集目录'],
  ['极简','瑞士网格','杂志编辑','新粗野','玻璃拟态','新拟态','拟物质感','Material','Fluent','苹果 / iOS','中后台企业','活泼趣味','柔和圆润','暗黑科技','渐变光感','3D / WebGL','动感','复古游戏','工业单色','朴素实用']),
'en': (['Resource type','All types','Visual style','All styles','Resource type','Visual style','Homepage screenshot','Official docs / spec / tutorial — no source code to copy; the original description is above','Design system','Spec','Tutorial','Tool','Collection',
  'Agent design skills · new','Big-tech UED / design systems','Design tutorials','Component style & token specs','UI inspiration & assets · new','AI coding × design'],
  ['Design systems','Component libraries','Component demos','Motion & effects','Agent skills','MCP','DESIGN.md / llms.txt','Tokens & specs','Accessibility','Anti AI-slop','Tutorials','Courses','Newsletters','Inspiration','Templates','AI generators','Design tools','Icons, fonts & assets','Directories'],
  ['Minimal','Swiss grid','Editorial','Brutalist','Glassmorphism','Neumorphism','Skeuomorphic','Material','Fluent','Apple / iOS','Enterprise admin','Playful','Soft','Dark tech','Gradient glow','3D / WebGL','Motion-rich','Retro gaming','Industrial mono','Utilitarian']),
'ja': (['リソース種別','すべての種別','ビジュアルスタイル','すべてのスタイル','リソース種別','ビジュアルスタイル','トップページのスクリーンショット','公式ドキュメント／規約／チュートリアルのため、コピーできるソースコードはありません。元サイトの説明は上にあります','デザインシステム','規約','チュートリアル','ツール','まとめ',
  'エージェント向けデザイン Skill・新着','大手企業の UED／デザインシステム','デザインチュートリアル','コンポーネントスタイルとトークン規約','UI インスピレーションと素材・新着','AI コーディング × デザイン'],
  ['デザインシステム','コンポーネントライブラリ','コンポーネントデモ','モーション・エフェクト','エージェント Skill','MCP','DESIGN.md／llms.txt','トークンと規約','アクセシビリティ','AI っぽさ除去','チュートリアル','講座','ニュースレター','インスピレーション','テンプレート','AI 生成','デザインツール','アイコン・フォント素材','ディレクトリ'],
  ['ミニマル','スイスグリッド','エディトリアル','ブルータリズム','グラスモーフィズム','ニューモーフィズム','スキューモーフィズム','Material','Fluent','Apple／iOS','業務システム','ポップ','ソフト','ダークテック','グラデーション','3D／WebGL','モーション重視','レトロゲーム','インダストリアル','実用本位']),
'ko': (['리소스 유형','전체 유형','비주얼 스타일','전체 스타일','리소스 유형','비주얼 스타일','홈페이지 스크린샷','공식 문서/규범/튜토리얼로 복사할 소스 코드가 없습니다. 원문 설명은 위에 있습니다','디자인 시스템','규범','튜토리얼','도구','모음',
  '에이전트 디자인 Skill · 신규','빅테크 UED / 디자인 시스템','디자인 튜토리얼','컴포넌트 스타일과 토큰 규범','UI 영감 사이트와 소재 · 신규','AI 코딩 × 디자인'],
  ['디자인 시스템','컴포넌트 라이브러리','컴포넌트 데모','모션·이펙트','에이전트 Skill','MCP','DESIGN.md / llms.txt','토큰과 규범','접근성','AI 티 제거','튜토리얼','강의','뉴스레터','영감','템플릿','AI 생성','디자인 도구','아이콘·폰트 소재','디렉터리'],
  ['미니멀','스위스 그리드','에디토리얼','브루탈리즘','글래스모피즘','뉴모피즘','스큐어모피즘','Material','Fluent','Apple / iOS','기업용 관리','발랄','부드러움','다크 테크','그라데이션','3D / WebGL','모션 중심','레트로 게임','인더스트리얼','실용형']),
'ms': (['Jenis sumber','Semua jenis','Gaya visual','Semua gaya','Jenis sumber','Gaya visual','Tangkapan skrin laman utama','Dokumentasi rasmi / spesifikasi / tutorial — tiada kod sumber untuk disalin; penerangan asal ada di atas','Sistem reka bentuk','Spesifikasi','Tutorial','Alat','Koleksi',
  'Skill reka bentuk ejen · baharu','UED syarikat besar / sistem reka bentuk','Tutorial reka bentuk','Gaya komponen & spesifikasi token','Inspirasi UI & aset · baharu','Pengekodan AI × reka bentuk'],
  ['Sistem reka bentuk','Pustaka komponen','Demo komponen','Animasi & kesan','Skill ejen','MCP','DESIGN.md / llms.txt','Token & spesifikasi','Kebolehcapaian','Anti rasa AI','Tutorial','Kursus','Surat berita','Inspirasi','Templat','Penjana AI','Alat reka bentuk','Ikon, fon & aset','Direktori'],
  ['Minimalis','Grid Swiss','Editorial','Brutalis','Glassmorphism','Neumorphism','Skeuomorfik','Material','Fluent','Apple / iOS','Pentadbiran perusahaan','Ceria','Lembut','Teknologi gelap','Cahaya gradien','3D / WebGL','Kaya animasi','Permainan retro','Industri monokrom','Utilitarian']),
'es': (['Tipo de recurso','Todos los tipos','Estilo visual','Todos los estilos','Tipo de recurso','Estilo visual','Captura de la portada','Documentación oficial / especificación / tutorial: no hay código que copiar; la descripción original está arriba','Sistema de diseño','Especificación','Tutorial','Herramienta','Colección',
  'Skills de diseño para agentes · nuevo','UED de grandes empresas / sistemas de diseño','Tutoriales de diseño','Estilo de componentes y especificaciones de tokens','Inspiración UI y recursos · nuevo','Programación con IA × diseño'],
  ['Sistemas de diseño','Librerías de componentes','Demos de componentes','Animación y efectos','Skills de agente','MCP','DESIGN.md / llms.txt','Tokens y especificaciones','Accesibilidad','Anti “look IA”','Tutoriales','Cursos','Boletines','Inspiración','Plantillas','Generadores IA','Herramientas de diseño','Iconos, fuentes y recursos','Directorios'],
  ['Minimalista','Retícula suiza','Editorial','Brutalista','Glassmorphism','Neumorfismo','Esqueuomorfismo','Material','Fluent','Apple / iOS','Empresarial','Divertido','Suave','Tecnológico oscuro','Degradado luminoso','3D / WebGL','Con mucho movimiento','Retro gamer','Industrial monocromo','Utilitario']),
'de': (['Ressourcentyp','Alle Typen','Visueller Stil','Alle Stile','Ressourcentyp','Visueller Stil','Screenshot der Startseite','Offizielle Doku / Spezifikation / Tutorial – kein Quellcode zum Kopieren; die Originalbeschreibung steht oben','Designsystem','Spezifikation','Tutorial','Tool','Sammlung',
  'Design-Skills für Agenten · neu','UED großer Firmen / Designsysteme','Design-Tutorials','Komponentenstil & Token-Spezifikationen','UI-Inspiration & Assets · neu','KI-Coding × Design'],
  ['Designsysteme','Komponentenbibliotheken','Komponenten-Demos','Motion & Effekte','Agent-Skills','MCP','DESIGN.md / llms.txt','Tokens & Spezifikationen','Barrierefreiheit','Anti-KI-Look','Tutorials','Kurse','Newsletter','Inspiration','Vorlagen','KI-Generatoren','Design-Tools','Icons, Schriften & Assets','Verzeichnisse'],
  ['Minimal','Swiss Grid','Editorial','Brutalistisch','Glassmorphism','Neumorphism','Skeuomorph','Material','Fluent','Apple / iOS','Enterprise-Admin','Verspielt','Weich','Dark Tech','Verlaufsglanz','3D / WebGL','Bewegungsreich','Retro-Gaming','Industrial mono','Funktional']),
'fr': (['Type de ressource','Tous les types','Style visuel','Tous les styles','Type de ressource','Style visuel','Capture de la page d’accueil','Documentation officielle / spécification / tutoriel : pas de code source à copier ; la description d’origine est ci-dessus','Design system','Spécification','Tutoriel','Outil','Collection',
  'Skills de design pour agents · nouveau','UED des grands groupes / design systems','Tutoriels de design','Style de composants et spécifications de tokens','Inspiration UI et ressources · nouveau','Code IA × design'],
  ['Design systems','Bibliothèques de composants','Démos de composants','Animation et effets','Skills d’agent','MCP','DESIGN.md / llms.txt','Tokens et spécifications','Accessibilité','Anti « effet IA »','Tutoriels','Cours','Newsletters','Inspiration','Modèles','Générateurs IA','Outils de design','Icônes, polices et ressources','Annuaires'],
  ['Minimaliste','Grille suisse','Éditorial','Brutaliste','Glassmorphism','Neumorphisme','Skeuomorphisme','Material','Fluent','Apple / iOS','Back-office entreprise','Ludique','Doux','Tech sombre','Dégradé lumineux','3D / WebGL','Très animé','Rétro gaming','Industriel mono','Utilitaire']),
}
A = {}
for lang,(base,rt,vs) in L.items():
    assert len(base)==len(K) and len(rt)==len(RT) and len(vs)==len(VS), lang
    o = dict(zip(K,base)); o.update({'rt_'+k:v for k,v in zip(RT,rt)}); o.update({'vs_'+k:v for k,v in zip(VS,vs)}); A[lang]=o
js = '/* v3h：资源类型 / 页面样式风格 / 新分区 */\n(function(I){var A=' + json.dumps(A, ensure_ascii=False) + ';for(var l in A)if(I[l])for(var k in A[l])I[l][k]=A[l][k]})(window.UI_I18N);\n'
js += 'window.UI_SEC_ORDER=window.UI_SEC_ORDER.concat(["Agent 设计 Skills · 新增","大厂 UED / 设计系统","设计教程","组件风格与 Token 规范","UI 灵感站与素材 · 新增","AI Coding × 设计"]);\n'
s = open('i18n.js', encoding='utf-8').read()
if '/* v3h' in s: s = s[:s.index('/* v3h')]
open('i18n.js','w',encoding='utf-8').write(s + js)
print('ok')
