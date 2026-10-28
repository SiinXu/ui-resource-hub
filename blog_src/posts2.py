# Blog v2 (2026-10-14): 17 more original posts. Same schema as posts.py + optional cat/series/featured.
# Daily routine: append a new dict to POSTS2 (slug,date,cat,series|None,featured,tags,t,s[10 langs],en,zh,refs) and a matching IMAGES2 entry in images2.py; body needs <p>, a list/pre, and <h2>.
# Written in our own words; every factual claim is backed by the refs list. No invented stats.
def T(en,zh,zht,ja,ko,ms,vi,fr,es,de): return dict(en=en,zh=zh,zht=zht,ja=ja,ko=ko,ms=ms,vi=vi,fr=fr,es=es,de=de)
D='2026-10-14'
POSTS2 = [
dict(slug='v0-prompt-to-shadcn', date=D, cat='tools', series='prompt-to-ui', featured=True, tags=['v0','shadcn','prompt-to-UI'],
 t=T('v0 in practice: from a prompt to shadcn code you can keep','v0 实战：从一句提示到能留下来的 shadcn 代码','v0 實戰：從一句提示到能留下來的 shadcn 程式碼','v0実践：プロンプトから残せるshadcnコードへ','v0 실전: 프롬프트에서 남길 수 있는 shadcn 코드까지','v0 secara praktikal: dari prompt ke kod shadcn yang boleh disimpan','v0 thực chiến: từ một prompt đến mã shadcn giữ lại được',"v0 en pratique : d'un prompt à du code shadcn qu'on garde",'v0 en la práctica: de un prompt a código shadcn que puedes conservar','v0 in der Praxis: vom Prompt zu shadcn-Code, den man behält'),
 s=T('v0 is strongest when you treat it as a shadcn/Tailwind code generator, not a design oracle. Brief it like an engineer, then pull the code into your repo.','v0 最强的用法是把它当 shadcn/Tailwind 代码生成器，而不是设计神谕。像给工程师写需求一样写提示，然后把代码拉进自己的仓库。','v0 最強的用法是把它當 shadcn/Tailwind 程式碼產生器，而不是設計神諭。像給工程師寫需求一樣寫提示，再把程式碼拉進自己的倉庫。','v0はデザインの神託ではなくshadcn/Tailwindのコード生成器として使うと最強。エンジニア向けに指示し、コードを自分のリポジトリへ。','v0는 디자인 신탁이 아니라 shadcn/Tailwind 코드 생성기로 쓸 때 가장 강하다. 엔지니어에게 하듯 지시하고 코드를 저장소로 가져오자.','v0 paling kuat sebagai penjana kod shadcn/Tailwind. Beri arahan seperti kepada jurutera, kemudian bawa kod ke repo anda.','v0 mạnh nhất khi coi là trình sinh mã shadcn/Tailwind. Viết yêu cầu như cho kỹ sư rồi kéo mã về repo.',"v0 brille comme générateur de code shadcn/Tailwind. Briefez-le comme un ingénieur puis rapatriez le code.",'v0 rinde mejor como generador de código shadcn/Tailwind. Instrúyelo como a un ingeniero y lleva el código a tu repo.','v0 glänzt als shadcn/Tailwind-Codegenerator. Briefen Sie es wie einen Engineer und holen Sie den Code ins Repo.'),
 en="""<p>v0 by Vercel generates React components built on shadcn/ui and Tailwind CSS. That stack choice is the whole point: the output is ordinary, readable code using primitives many teams already ship, so the result can leave the tool. Treat v0 as a fast pair-programmer for UI, and judge it by whether you would merge its code.</p>
<h2>A brief that works</h2>
<ul><li><strong>Name the components.</strong> "Use Card, Tabs and a Table with a sticky header" beats "make a nice dashboard". v0 knows the shadcn vocabulary, so use it.</li>
<li><strong>Give tokens, not adjectives.</strong> Radius, one accent colour, font, density. "Modern" means nothing to a model; <code>--radius: 0.5rem</code> does.</li>
<li><strong>List the states.</strong> Empty, loading, error, long text. Generators default to the happy path.</li>
<li><strong>Paste real content.</strong> Lorem ipsum hides layout bugs; real names and prices expose them.</li></ul>
<h2>Iterate in small, named steps</h2>
<p>Ask for one change per turn ("tighten the table to 40px rows; keep everything else"). Big rewrites tend to regress parts you already liked. When something is right, say so explicitly so it stays.</p>
<h2>Getting the code out</h2>
<p>v0 lets you add generated code to a project through the shadcn CLI or download it, and it deploys to Vercel. Whichever path you take, review it like a PR: check that colours come from CSS variables rather than hard-coded hex, that interactive elements are real buttons and links, and that focus styles exist.</p>
<h2>Our take</h2>
<p>v0's ceiling is your brief and your design system. Teams that already use shadcn get the most out of it because the output drops straight into their codebase. Pair it with a taste skill or the guidelines in our encyclopedia to avoid the generic "centred hero + three cards" result.</p>""",
 zh="""<p>Vercel 的 v0 生成的是基于 shadcn/ui 和 Tailwind CSS 的 React 组件。这个技术栈选择就是它的核心价值：产出是普通、可读的代码，用的是很多团队本来就在用的组件，所以结果能离开这个工具。把 v0 当作写界面的快速结对程序员，评判标准只有一个：这段代码你愿不愿意合并。</p>
<h2>好用的提示怎么写</h2>
<ul><li><strong>直接点名组件。</strong>「用 Card、Tabs，表格表头吸顶」比「做个好看的仪表盘」有效得多。v0 懂 shadcn 的词汇，就用这些词。</li>
<li><strong>给 Token，不给形容词。</strong>圆角、一个强调色、字体、密度。「现代感」对模型毫无意义，<code>--radius: 0.5rem</code> 才有。</li>
<li><strong>列出状态。</strong>空、加载中、出错、超长文本。生成器默认只做一切顺利的情况。</li>
<li><strong>贴真实内容。</strong>假文会掩盖排版问题，真实的人名和价格会把问题暴露出来。</li></ul>
<h2>小步、明确地迭代</h2>
<p>每轮只提一个改动（「表格行高收到 40px，其他不动」）。大改容易把你已经满意的部分改坏。某处对了，要明确说出来让它保留。</p>
<h2>把代码拿出来</h2>
<p>v0 支持通过 shadcn CLI 把生成的代码加进项目，也可以下载，或者直接部署到 Vercel。无论走哪条路，都要像审 PR 一样审：颜色是否来自 CSS 变量而不是写死的十六进制，可交互元素是不是真正的 button 和链接，焦点样式有没有。</p>
<h2>我们的看法</h2>
<p>v0 的上限取决于你的需求描述和设计系统。已经在用 shadcn 的团队收益最大，因为产出能直接放进代码库。配合审美 skill 或本站百科里的规范使用，才能避开「居中大标题 + 三张卡片」的平庸结果。</p>""",
 refs=[('v0 by Vercel','Vercel','https://v0.app/'),('v0 documentation','Vercel','https://v0.app/docs'),('shadcn/ui','shadcn','https://ui.shadcn.com/'),('shadcn CLI docs','shadcn','https://ui.shadcn.com/docs/cli')]),

dict(slug='lovable-bolt-prompt-to-app', date=D, cat='tools', series='prompt-to-ui', tags=['Lovable','Bolt','full-stack'],
 t=T('Lovable and Bolt: when prompt-to-UI becomes prompt-to-app','Lovable 与 Bolt：当「提示生成界面」变成「提示生成应用」','Lovable 與 Bolt：當「提示產生介面」變成「提示產生應用」','LovableとBolt：プロンプトからUIがアプリになるとき','Lovable과 Bolt: 프롬프트-UI가 프롬프트-앱이 될 때','Lovable dan Bolt: apabila prompt-ke-UI menjadi prompt-ke-apl','Lovable và Bolt: khi prompt-to-UI thành prompt-to-app',"Lovable et Bolt : quand le prompt-to-UI devient prompt-to-app",'Lovable y Bolt: cuando prompt-to-UI se vuelve prompt-to-app','Lovable und Bolt: wenn Prompt-to-UI zu Prompt-to-App wird'),
 s=T('Both tools build whole apps, so design quality now competes with data, auth and deploys for attention. How to keep the look from being an afterthought.','两者都能生成完整应用，于是设计质量要和数据、登录、部署抢注意力。如何不让视觉沦为事后补丁。','兩者都能產生完整應用，於是設計品質要和資料、登入、部署搶注意力。如何不讓視覺淪為事後補丁。','どちらもアプリ全体を作るため、デザイン品質はデータや認証と注意を奪い合う。見た目を後回しにしない方法。','둘 다 앱 전체를 만들기에 디자인 품질이 데이터·인증·배포와 경쟁한다. 외관을 뒷전으로 두지 않는 법.','Kedua-duanya membina apl penuh; reka bentuk bersaing dengan data dan auth. Cara elak visual jadi hal kemudian.','Cả hai dựng app hoàn chỉnh nên thiết kế phải tranh chú ý với dữ liệu, đăng nhập. Cách để giao diện không bị bỏ quên.',"Les deux construisent des apps entières : le design rivalise avec données et auth. Comment ne pas le reléguer.",'Ambos construyen apps completas: el diseño compite con datos y auth. Cómo evitar que quede para después.','Beide bauen ganze Apps – Design konkurriert mit Daten und Auth. So bleibt die Optik keine Nebensache.'),
 en="""<p>Lovable and Bolt (by StackBlitz) sit one step beyond component generators: you describe an app and they scaffold front end, routing and, through integrations such as Supabase, a backend. Bolt runs the dev environment in the browser on StackBlitz's WebContainers. The design question changes accordingly: the model is juggling schema, auth and deploys, so visual decisions get made by default unless you make them first.</p>
<h2>A notable change this month</h2>
<p>On 8 October 2026 Lovable's changelog removed the three "design directions" it used to show before the first build of a visually open-ended prompt. It now derives the look from your description and asks about colour, typography and layout only when the prompt leaves them open. In practice: <strong>your prompt is now the art brief</strong>. If you don't write one, you get the default.</p>
<h2>Front-load the look</h2>
<ol><li>Open with a style paragraph before any feature list: palette, type, radius, density, one reference site.</li>
<li>Ask for a static UI pass first, with fake data, and approve it before wiring the backend.</li>
<li>Keep a <code>design.md</code> or similar guideline file in the project and tell the tool to follow it on every change.</li>
<li>After each feature, check the new screens against that file; drift creeps in one screen at a time.</li></ol>
<h2>When to pick which</h2>
<p>Use these tools when you need a working prototype with real data paths fast. Use a component generator (v0, Magic Patterns) or hand-built code when the deliverable is a polished interface inside an existing codebase. Many teams do both: prototype the flow in an app builder, rebuild the final UI with their own system.</p>""",
 zh="""<p>Lovable 和 StackBlitz 的 Bolt 比组件生成器更进一步：你描述一个应用，它们会搭出前端、路由，并通过 Supabase 等集成搭出后端。Bolt 借助 StackBlitz 的 WebContainers 在浏览器里运行开发环境。设计问题也随之改变：模型同时在处理数据结构、登录和部署，你不先做视觉决定，它就会按默认值替你做。</p>
<h2>本月一个值得注意的变化</h2>
<p>2026 年 10 月 8 日，Lovable 的更新日志写明：对视觉要求开放的提示，首次构建前不再给出三个「设计方向」供选择。现在它直接从你的描述推导外观，只有在提示没说清颜色、字体和布局时才会追问。换句话说：<strong>你的提示词现在就是美术需求</strong>，不写就是默认样式。</p>
<h2>把视觉要求放在最前面</h2>
<ol><li>功能列表之前先写一段风格说明：配色、字体、圆角、密度、一个参考网站。</li>
<li>先要一版只有假数据的静态界面，确认后再接后端。</li>
<li>在项目里放一个 <code>design.md</code> 之类的规范文件，要求每次改动都遵守。</li>
<li>每做完一个功能，对照这个文件检查新页面；风格跑偏总是一页一页累积的。</li></ol>
<h2>怎么选</h2>
<p>需要快速做出接通真实数据的可用原型时，用这类工具。交付物是要放进现有代码库的精致界面时，用组件生成器（v0、Magic Patterns）或手写。很多团队两者并用：在应用生成器里跑通流程，再用自己的设计系统重做最终界面。</p>""",
 refs=[('Lovable changelog (8 Oct 2026)','Lovable','https://docs.lovable.dev/changelog'),('Lovable cut its pick-a-look step','Art Direction Daily','https://artdirectiondaily.com/issues/2026-10-12-lovable-cut-pick-look-step.html'),('Bolt.new','StackBlitz','https://bolt.cello.so/ByQ3siiRkMz'),('WebContainers','StackBlitz','https://webcontainers.io/'),('Lovable Supabase integration','Lovable','https://docs.lovable.dev/integrations/supabase')]),

dict(slug='figma-make-and-figma-agent', date=D, cat='tools', series='prompt-to-ui', tags=['Figma','Figma Make','agent'],
 t=T('Figma Make and the Figma agent: AI moves onto the canvas','Figma Make 与 Figma 智能体：AI 搬上画布','Figma Make 與 Figma 智慧體：AI 搬上畫布','Figma MakeとFigmaエージェント：AIがキャンバスへ','Figma Make와 Figma 에이전트: AI가 캔버스로','Figma Make dan ejen Figma: AI pindah ke kanvas','Figma Make và agent của Figma: AI lên canvas',"Figma Make et l'agent Figma : l'IA arrive sur le canevas",'Figma Make y el agente de Figma: la IA llega al lienzo','Figma Make und der Figma-Agent: KI zieht auf die Canvas'),
 s=T('Figma Make turns prompts into working prototypes; the Figma agent, generally available since 6 Oct 2026, reads team guideline files. Why the guideline file matters most.','Figma Make 把提示变成可交互原型；Figma 智能体自 2026-10-06 正式可用，能读取团队规范文件。为什么规范文件才是关键。','Figma Make 把提示變成可互動原型；Figma 智慧體自 2026-10-06 正式可用，能讀取團隊規範檔。為什麼規範檔才是關鍵。','Figma Makeはプロンプトを動くプロトタイプに。2026/10/6 GAのエージェントはガイドラインを読む。肝はガイドライン。','Figma Make는 프롬프트를 프로토타입으로, 2026-10-06 정식 출시된 에이전트는 가이드라인 파일을 읽는다.','Figma Make jadikan prompt prototaip; ejen Figma (GA 6 Okt 2026) membaca fail garis panduan pasukan.','Figma Make biến prompt thành prototype; agent Figma (GA 6/10/2026) đọc file hướng dẫn của nhóm.',"Figma Make transforme des prompts en prototypes ; l'agent (GA le 6/10/2026) lit les guides d'équipe.",'Figma Make convierte prompts en prototipos; el agente (GA 6/10/2026) lee las guías del equipo.','Figma Make macht Prompts zu Prototypen; der Agent (GA 6.10.2026) liest Team-Guidelines.'),
 en="""<p>Figma Make, introduced at Config 2025, generates interactive prototypes and simple apps from a prompt, and can start from an existing Figma frame. It answered the question designers kept asking about v0-style tools: "can I do this where my designs already live?"</p>
<h2>The agent goes GA</h2>
<p>On 6 October 2026 Figma made its product-design agent generally available, after a beta that began in May. Two additions stand out in the coverage: library owners can supply guidelines (markdown files) that the agent reads whenever that library is enabled, and teammates can watch the agent's activity live on the canvas.</p>
<h2>Why the guideline file is the real feature</h2>
<ul><li>It moves art direction from a per-session prompt into a file the team maintains and reviews.</li>
<li>It makes AI output consistent across people, not just across one person's sessions.</li>
<li>It is the same pattern as SKILL.md, Cursor rules and Lovable project knowledge: <strong>durable, versioned design context</strong>.</li></ul>
<h2>What to put in yours</h2>
<p>Token names and when to use each; spacing and type scales; component do/don't pairs; voice and tone for UI copy; a short "never" list (no text gradients, no emoji icons, no centred body text). Keep it short enough that a reviewer actually reads it, and link to examples rather than describing them. Our encyclopedia's spec digests are a reasonable starting template.</p>""",
 zh="""<p>Figma Make 在 Config 2025 上推出，能根据提示生成可交互原型和简单应用，也可以从现有的 Figma 画框开始。它回答了设计师对 v0 这类工具一直在问的问题：「能不能在我的设计稿所在的地方做？」</p>
<h2>智能体正式可用</h2>
<p>2026 年 10 月 6 日，Figma 的产品设计智能体结束 5 月开始的测试，正式可用。报道中有两点特别值得注意：组件库所有者可以提供规范文件（Markdown），启用该库时智能体就会读取；队友可以在画布上实时看到智能体在做什么。</p>
<h2>为什么规范文件才是真正的功能</h2>
<ul><li>它把美术方向从每次会话的提示词，变成团队维护和审阅的文件。</li>
<li>它让 AI 产出在不同人之间保持一致，而不只是在一个人的多次会话之间。</li>
<li>它和 SKILL.md、Cursor rules、Lovable 项目知识是同一种模式：<strong>持久、有版本的设计上下文</strong>。</li></ul>
<h2>规范文件里写什么</h2>
<p>Token 名称及各自的用途；间距和字号阶梯；组件的「该做/不该做」对照；界面文案的语气；一份简短的「禁止」清单（不用渐变文字、不用 emoji 当图标、正文不居中）。写得足够短，审阅的人才会真的读；能放示例链接就别用文字描述。本站百科里的规范摘要可以当起步模板。</p>""",
 refs=[('Figma Make','Figma','https://www.figma.com/make/'),("Figma's AI agent for product design is now generally available",'The Verge','https://www.theverge.com/tech/1004953/figmas-ai-agent-for-product-design-is-now-generally-available'),('Figma release notes','Figma','https://www.figma.com/release-notes/'),('Lovable cut its pick-a-look step (Figma section)','Art Direction Daily','https://artdirectiondaily.com/issues/2026-10-12-lovable-cut-pick-look-step.html')]),

dict(slug='magic-patterns-magicos', date=D, cat='tools', series='prompt-to-ui', featured=True, tags=['Magic Patterns','MagicOS','canvas'],
 t=T('MagicOS: Magic Patterns bets on an infinite canvas of AI threads','MagicOS：Magic Patterns 押注「无限画布 + 并行 AI 线程」','MagicOS：Magic Patterns 押注「無限畫布 + 並行 AI 執行緒」','MagicOS：Magic Patternsは無限キャンバス＋並列AIスレッドに賭ける','MagicOS: Magic Patterns, 무한 캔버스와 병렬 AI 스레드에 베팅','MagicOS: Magic Patterns bertaruh pada kanvas tanpa had','MagicOS: Magic Patterns đặt cược vào canvas vô hạn và luồng AI song song',"MagicOS : Magic Patterns parie sur un canevas infini de fils IA",'MagicOS: Magic Patterns apuesta por un lienzo infinito de hilos de IA','MagicOS: Magic Patterns setzt auf eine unendliche Canvas mit KI-Threads'),
 s=T('Launched 13 Oct 2026: one coordinator chat spawns parallel design threads on a shared canvas. What it fixes (lost context) and when a single design is still better.','2026-10-13 发布：一个协调者对话在共享画布上派生多个并行设计线程。它解决了什么（上下文丢失），什么时候单个设计仍更合适。','2026-10-13 發布：一個協調者對話在共享畫布上派生多個並行設計執行緒。它解決了什麼，何時單一設計仍更合適。','2026/10/13公開：1つのコーディネーターが共有キャンバス上で並列スレッドを起動。解決すること、単一デザインが良い場面。','2026-10-13 출시: 하나의 코디네이터 채팅이 공유 캔버스에서 병렬 스레드를 만든다. 무엇을 해결하고 언제 단일 디자인이 나은가.','Dilancar 13 Okt 2026: satu sembang penyelaras menjana bebenang reka bentuk selari pada kanvas.','Ra mắt 13/10/2026: một chat điều phối tạo nhiều luồng thiết kế song song trên canvas chung.',"Lancé le 13/10/2026 : un chat coordinateur lance des fils de design parallèles sur un canevas partagé.",'Lanzado el 13/10/2026: un chat coordinador lanza hilos de diseño paralelos en un lienzo compartido.','Start am 13.10.2026: ein Koordinator-Chat startet parallele Design-Threads auf einer Canvas.'),
 en="""<p>Magic Patterns started as a prompt-to-UI tool aimed at product teams (it launched on Hacker News as YC W23, intentionally front-end only). On 13 October 2026 it introduced MagicOS, which reorganises the product around an infinite canvas rather than one chat and one preview.</p>
<h2>How it is structured</h2>
<ul><li><strong>Canvas:</strong> everything is a file on it: designs, documents, images, GitHub repos, notes.</li>
<li><strong>Coordinator:</strong> the chat you talk to. It answers small questions and turns real work into threads.</li>
<li><strong>Threads:</strong> each is an agent doing one piece of work; they run in parallel and report back.</li>
<li><strong>Sidebar:</strong> threads by status, so you see what is waiting on you.</li></ul>
<h2>What problem it targets</h2>
<p>Anyone who has explored five directions in five chat tabs knows the pain: you repeat the brief in each, lose rejected options, and forget why you picked one. MagicOS keeps PRDs, references, variants and rejected directions side by side, and the coordinator reads the canvas so you explain less. It also offers real-time voice and an MCP server so Claude, Cursor or Codex can build from what is on the canvas.</p>
<h2>When not to use it</h2>
<p>Magic Patterns' own docs say a single design still fits better for one page or a quick prototype, and that some features (Plan Mode, Controls, forking, merging, inline comments) were single-design only at launch. Our take: use the canvas for exploration-heavy work, keep the single design for focused polish.</p>""",
 zh="""<p>Magic Patterns 起初是面向产品团队的「提示生成界面」工具（以 YC W23 身份在 Hacker News 发布，刻意只做前端）。2026 年 10 月 13 日它推出 MagicOS，把产品从「一个对话 + 一个预览」重组为一块无限画布。</p>
<h2>它的结构</h2>
<ul><li><strong>画布：</strong>上面的一切都是文件：设计、文档、图片、GitHub 仓库、笔记。</li>
<li><strong>协调者：</strong>你对话的那个聊天。小问题它直接回答，真正的工作它拆成线程。</li>
<li><strong>线程：</strong>每个线程是一个负责一项工作的智能体，并行运行，完成或需要你时会汇报。</li>
<li><strong>侧栏：</strong>按状态列出所有线程，一眼看到哪些在等你。</li></ul>
<h2>它要解决的问题</h2>
<p>在五个聊天标签页里探索五个方向的人都懂这种痛：每个标签都要重复需求，被否掉的方案找不回来，也忘了当初为什么选了某一个。MagicOS 把 PRD、参考图、变体和被否掉的方向并排放着，协调者能读懂画布，你需要解释的就少了。它还支持实时语音，并提供 MCP 服务，让 Claude、Cursor 或 Codex 可以根据画布上的内容写代码。</p>
<h2>什么时候不用它</h2>
<p>Magic Patterns 自己的文档说，只做一个页面或快速原型时，单个设计仍然更合适；发布时 Plan Mode、Controls、分叉、合并、行内评论等功能也只在单个设计里有。我们的看法：探索多的工作用画布，专注打磨用单个设计。</p>""",
 refs=[('Introducing MagicOS','Magic Patterns','https://www.magicpatterns.com/blog/introducing-magicos'),('What is MagicOS','Magic Patterns docs','https://www.magicpatterns.com/docs/documentation/magic-os/overview'),('MagicOS vs. Designs','Magic Patterns docs','https://www.magicpatterns.com/docs/documentation/magic-os/when-to-use-magicos'),('Launch HN: Magic Patterns (YC W23)','Hacker News','https://news.ycombinator.com/item?id=43752176')]),

dict(slug='prompt-to-ui-tools-compared', date=D, cat='tools', series='prompt-to-ui', featured=True, tags=['comparison','v0','Lovable','Bolt','Figma Make','Magic Patterns'],
 t=T('Prompt-to-UI tools compared: v0, Lovable, Bolt, Figma Make, Magic Patterns','提示生成界面工具横评：v0、Lovable、Bolt、Figma Make、Magic Patterns','提示產生介面工具橫評：v0、Lovable、Bolt、Figma Make、Magic Patterns','プロンプトUIツール比較：v0・Lovable・Bolt・Figma Make・Magic Patterns','프롬프트-UI 도구 비교: v0, Lovable, Bolt, Figma Make, Magic Patterns','Perbandingan alat prompt-ke-UI','So sánh công cụ prompt-to-UI: v0, Lovable, Bolt, Figma Make, Magic Patterns','Comparatif des outils prompt-to-UI','Comparativa de herramientas prompt-to-UI','Prompt-to-UI-Tools im Vergleich'),
 s=T('Not a leaderboard: a decision guide by what you are shipping, where the output lives, and how much design control you need.','不是排行榜，而是决策指南：按你要交付什么、产出放在哪里、需要多少设计控制来选。','不是排行榜，而是決策指南：按你要交付什麼、產出放在哪裡、需要多少設計控制來選。','ランキングではなく判断ガイド：何を出すか、成果物の置き場所、必要なデザイン制御で選ぶ。','순위표가 아닌 결정 가이드: 무엇을 출시하는지, 산출물 위치, 필요한 디자인 통제로 고르자.','Bukan senarai kedudukan: panduan memilih mengikut apa yang dihantar dan kawalan reka bentuk.','Không phải bảng xếp hạng: hướng dẫn chọn theo thứ bạn giao, nơi đặt sản phẩm và mức kiểm soát thiết kế.',"Pas un classement : un guide de choix selon le livrable, l'emplacement du code et le contrôle du design.",'No es un ranking: una guía según lo que entregas, dónde vive el resultado y el control de diseño.','Kein Ranking: eine Entscheidungshilfe nach Ergebnis, Ablageort und Designkontrolle.'),
 en="""<p>All five tools turn words into interface, but they are built for different jobs. Comparing them on "which looks best" is unreliable because output depends mostly on your prompt. Compare them on what they produce and where it goes.</p>
<h2>By deliverable</h2>
<ul><li><strong>Components for an existing React codebase:</strong> v0 (shadcn/Tailwind output, CLI install).</li>
<li><strong>A working full-stack prototype:</strong> Lovable or Bolt (backend integrations, in-browser dev env for Bolt).</li>
<li><strong>Prototypes next to your design files:</strong> Figma Make; the Figma agent for edits on the canvas with team guidelines.</li>
<li><strong>Product-team exploration across many directions:</strong> Magic Patterns, now with the MagicOS canvas and an MCP server for coding agents.</li></ul>
<h2>Questions that decide it</h2>
<ol><li>Will engineers keep the code, or is this throwaway?</li>
<li>Do you need to match an existing design system? (Check whether the tool can import components or guideline files.)</li>
<li>Who iterates: a designer on a canvas, or a developer in a repo?</li>
<li>Where does the design context live, and can every teammate's session read it?</li></ol>
<h2>Our take</h2>
<p>The 2026 trend across all five is the same: durable context (guideline files, design systems, MCP) beats clever prompting. Pick the tool whose context mechanism fits your team, and invest in that file. Pricing and limits change often, so check each vendor's current page rather than any comparison table, including ours.</p>""",
 zh="""<p>五个工具都能把文字变成界面，但它们是为不同的活设计的。比「谁生成得好看」并不可靠，因为效果主要取决于你的提示。应该比它们产出什么、产出去哪里。</p>
<h2>按交付物选</h2>
<ul><li><strong>给现有 React 代码库的组件：</strong>v0（产出 shadcn/Tailwind 代码，可用 CLI 安装）。</li>
<li><strong>能跑的全栈原型：</strong>Lovable 或 Bolt（有后端集成，Bolt 在浏览器里跑开发环境）。</li>
<li><strong>紧挨设计稿的原型：</strong>Figma Make；要在画布上按团队规范修改，用 Figma 智能体。</li>
<li><strong>产品团队多方向探索：</strong>Magic Patterns，现在有 MagicOS 画布和给编程智能体用的 MCP 服务。</li></ul>
<h2>决定选择的几个问题</h2>
<ol><li>工程师会保留这些代码，还是用完即弃？</li>
<li>需要匹配现有设计系统吗？（看工具能否导入组件或规范文件。）</li>
<li>谁来迭代：画布上的设计师，还是仓库里的开发者？</li>
<li>设计上下文放在哪里，每个队友的会话都能读到吗？</li></ol>
<h2>我们的看法</h2>
<p>2026 年这五个工具的趋势一致：持久的上下文（规范文件、设计系统、MCP）比花哨的提示词更重要。选上下文机制最适合你团队的那个，然后把功夫花在那份文件上。价格和额度经常变，请以各家当前官网为准，任何对比表（包括我们这张）都不如官网可靠。</p>""",
 refs=[('v0','Vercel','https://v0.app/'),('Lovable docs','Lovable','https://docs.lovable.dev/'),('Bolt.new','StackBlitz','https://bolt.cello.so/ByQ3siiRkMz'),('Figma Make','Figma','https://www.figma.com/make/'),('Magic Patterns','Magic Patterns','https://www.magicpatterns.com/')]),
]
POSTS2 += [
dict(slug='aceternity-ui-deep-dive', date=D, cat='components', series='library-deep-dive', featured=True, tags=['Aceternity UI','motion','components'],
 t=T('Aceternity UI deep dive: spectacle, used sparingly','Aceternity UI 深读：惊艳效果，要省着用','Aceternity UI 深讀：驚豔效果，要省著用','Aceternity UI徹底解説：派手さは控えめに','Aceternity UI 심층 분석: 화려함은 아껴서','Aceternity UI mendalam: kemewahan, guna dengan jimat','Aceternity UI chuyên sâu: hiệu ứng ấn tượng, dùng tiết kiệm',"Aceternity UI en profondeur : du spectacle, avec parcimonie",'Aceternity UI a fondo: espectáculo, con moderación','Aceternity UI im Detail: Spektakel, sparsam eingesetzt'),
 s=T('Copy-paste React + Tailwind + Motion effects that made the "fancy" landing look popular. Which pieces carry a page and which turn it into a demo reel.','可复制粘贴的 React + Tailwind + Motion 特效，带火了「fancy」落地页风格。哪些能撑起页面，哪些会把页面变成特效合集。','可複製貼上的 React + Tailwind + Motion 特效，帶紅了「fancy」落地頁風格。哪些能撐起頁面，哪些會讓頁面變成特效合輯。','React+Tailwind+Motionのコピペ演出。ページを支える部品と、デモリールにしてしまう部品。','복사-붙여넣기 React+Tailwind+Motion 효과. 페이지를 받쳐 주는 것과 데모 릴로 만드는 것.','Kesan React+Tailwind+Motion salin-tampal. Mana yang menyokong halaman, mana yang jadi demo.','Hiệu ứng React+Tailwind+Motion copy-paste. Phần nào nâng trang, phần nào biến trang thành demo.',"Effets React+Tailwind+Motion à copier-coller : ce qui porte une page, ce qui en fait une démo.",'Efectos React+Tailwind+Motion para copiar: lo que sostiene una página y lo que la vuelve demo.','Copy-paste-Effekte mit React+Tailwind+Motion: was eine Seite trägt, was sie zur Demo macht.'),
 en="""<p>Aceternity UI, created by Manu Arora, is a collection of copy-paste components built with React, Tailwind CSS and Motion (formerly Framer Motion). It is known for showpiece effects: spotlight and beam backgrounds, 3D cards, animated grids, parallax hero scrolls. Free components are open to copy; there is also a paid tier of templates and blocks.</p>
<h2>What works on real pages</h2>
<ul><li><strong>One ambient background</strong> behind the hero (grid, dots, a soft spotlight). It adds depth without competing with copy.</li>
<li><strong>Bento grids and feature sections</strong> with restrained hover motion.</li>
<li><strong>Text reveal or typewriter</strong> for a single headline, not for paragraphs.</li></ul>
<h2>What to avoid</h2>
<p>Stacking three effects in one viewport, animating body text, and 3D tilt on cards that hold data. These read as a demo reel and cost performance on low-end phones. Always respect <code>prefers-reduced-motion</code>, which several effects do not handle by default, so wrap them yourself.</p>
<h2>How we use it in UI Hub</h2>
<p>Aceternity is one of the references behind the user's "restrained fancy" house style: borrow one signature effect per page, keep typography and spacing doing the heavy lifting. Search "aceternity" in the hub to see every Aceternity component we index with a live preview.</p>""",
 zh="""<p>Aceternity UI 由 Manu Arora 创建，是一套用 React、Tailwind CSS 和 Motion（原 Framer Motion）写的可复制组件。它以炫目的特效出名：聚光灯和光束背景、3D 卡片、动态网格、视差滚动首屏。免费组件可以直接复制，另有付费的模板和区块。</p>
<h2>在真实页面上好用的部分</h2>
<ul><li><strong>首屏后面放一个氛围背景</strong>（网格、点阵、柔和聚光灯）。增加层次，又不和文案抢戏。</li>
<li><strong>Bento 网格和功能区块</strong>，配克制的悬停动效。</li>
<li><strong>文字渐显或打字机效果</strong>只用在一句主标题上，不要用在段落上。</li></ul>
<h2>要避免的用法</h2>
<p>一屏叠三个特效、给正文加动画、给装数据的卡片加 3D 倾斜。这样看起来像特效合集，在低端手机上也很耗性能。一定要尊重 <code>prefers-reduced-motion</code>，有些特效默认不处理，需要自己包一层。</p>
<h2>UI Hub 怎么用它</h2>
<p>Aceternity 是「克制的 fancy」这一风格的参考之一：每页借一个标志性特效，排版和间距承担主要工作。在本站搜索「aceternity」，可以看到我们收录的所有 Aceternity 组件及实时预览。</p>""",
 refs=[('Aceternity UI','Manu Arora','https://ui.aceternity.com/'),('Aceternity UI components','Aceternity','https://ui.aceternity.com/components'),('Motion for React','Motion','https://motion.dev/'),('prefers-reduced-motion','MDN','https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion')]),

dict(slug='magic-ui-deep-dive', date=D, cat='components', series='library-deep-dive', tags=['Magic UI','shadcn','motion'],
 t=T('Magic UI deep dive: animated components that install like shadcn','Magic UI 深读：像 shadcn 一样安装的动效组件','Magic UI 深讀：像 shadcn 一樣安裝的動效元件','Magic UI徹底解説：shadcnのように入るアニメ部品','Magic UI 심층 분석: shadcn처럼 설치되는 애니메이션 컴포넌트','Magic UI mendalam: komponen animasi dipasang seperti shadcn','Magic UI chuyên sâu: component động cài như shadcn',"Magic UI en profondeur : des composants animés qui s'installent comme shadcn",'Magic UI a fondo: componentes animados que se instalan como shadcn','Magic UI im Detail: animierte Komponenten, installiert wie shadcn'),
 s=T('An open-source (MIT) set of motion components distributed through the shadcn registry. Best picks for SaaS pages and how to keep them accessible.','一套开源（MIT）的动效组件，通过 shadcn registry 分发。SaaS 页面最值得用的几个，以及如何保持无障碍。','一套開源（MIT）的動效元件，透過 shadcn registry 分發。SaaS 頁面最值得用的幾個，以及如何維持無障礙。','shadcnレジストリで配布されるMITのモーション部品。SaaSページ向けの選び方とアクセシビリティ。','shadcn 레지스트리로 배포되는 MIT 모션 컴포넌트. SaaS 페이지 추천과 접근성 유지법.','Komponen gerakan sumber terbuka (MIT) melalui registry shadcn.','Bộ component chuyển động MIT phân phối qua shadcn registry.',"Composants animés open source (MIT) distribués via le registre shadcn.",'Componentes animados open source (MIT) distribuidos por el registro de shadcn.','Open-Source-Motion-Komponenten (MIT) über die shadcn-Registry.'),
 en="""<p>Magic UI is an open-source library of animated components (MIT licence) designed as a companion to shadcn/ui. Components are added with the shadcn CLI from Magic UI's registry, so the source lands in your repo where you can edit it, rather than living in a dependency.</p>
<h2>Picks that earn their place</h2>
<ul><li><strong>Marquee</strong> for logo walls and testimonials: motion that carries information.</li>
<li><strong>Number ticker</strong> for a single headline metric.</li>
<li><strong>Animated beam / orbiting circles</strong> to show integrations, one per page.</li>
<li><strong>Shimmer or border-beam buttons</strong> for exactly one primary CTA.</li></ul>
<h2>Accessibility and performance</h2>
<p>Continuous motion (marquees, orbits) should pause on hover and stop under <code>prefers-reduced-motion</code>; WCAG 2.2.2 asks for a way to pause anything that moves for more than five seconds. Prefer transform and opacity animations, which browsers can composite cheaply.</p>
<h2>Our take</h2>
<p>Magic UI is the easiest way to add motion to a shadcn project because it shares the install model and the token variables. The risk is the same as any effects library: use one or two components per page, and let the rest of the UI stay calm.</p>""",
 zh="""<p>Magic UI 是一套开源（MIT 许可）的动效组件库，定位是 shadcn/ui 的搭档。组件用 shadcn CLI 从 Magic UI 的 registry 添加，源码直接落在你的仓库里可以随便改，而不是藏在依赖包里。</p>
<h2>值得用的几个</h2>
<ul><li><strong>Marquee 跑马灯</strong>用于 Logo 墙和用户评价：动效本身在传递信息。</li>
<li><strong>Number ticker 数字滚动</strong>只用于一个核心指标。</li>
<li><strong>Animated beam / Orbiting circles</strong>展示集成关系，每页一个。</li>
<li><strong>Shimmer 或 border-beam 按钮</strong>只给唯一的主 CTA。</li></ul>
<h2>无障碍与性能</h2>
<p>持续运动的元素（跑马灯、环绕动画）应在悬停时暂停，并在 <code>prefers-reduced-motion</code> 下停止；WCAG 2.2.2 要求超过五秒的运动内容必须能暂停。优先用 transform 和 opacity 做动画，浏览器可以低成本合成。</p>
<h2>我们的看法</h2>
<p>给 shadcn 项目加动效，Magic UI 是最省事的，因为安装方式和 Token 变量都一致。风险和所有特效库一样：每页用一两个，其他部分保持安静。</p>""",
 refs=[('Magic UI','Magic UI','https://magicui.design/'),('magicuidesign/magicui (MIT)','GitHub','https://github.com/magicuidesign/magicui'),('Understanding SC 2.2.2: Pause, Stop, Hide','W3C','https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html'),('shadcn registry docs','shadcn','https://ui.shadcn.com/docs/registry')]),

dict(slug='cult-ui-deep-dive', date=D, cat='components', series='library-deep-dive', tags=['Cult UI','shadcn','components'],
 t=T('Cult UI deep dive: tactile components with personality','Cult UI 深读：有手感、有个性的组件','Cult UI 深讀：有手感、有個性的元件','Cult UI徹底解説：触感と個性のある部品','Cult UI 심층 분석: 촉감과 개성이 있는 컴포넌트','Cult UI mendalam: komponen taktil berperibadi','Cult UI chuyên sâu: component có cảm giác và cá tính',"Cult UI en profondeur : des composants tactiles avec du caractère",'Cult UI a fondo: componentes táctiles con personalidad','Cult UI im Detail: taktile Komponenten mit Charakter'),
 s=T('shadcn-compatible components that feel physical: dynamic islands, textured buttons, expandable cards. How to borrow personality without breaking consistency.','兼容 shadcn、带物理手感的组件：灵动岛、质感按钮、可展开卡片。如何借来个性而不破坏一致性。','相容 shadcn、帶物理手感的元件：動態島、質感按鈕、可展開卡片。如何借來個性而不破壞一致性。','shadcn互換で物理的な触感の部品。一貫性を壊さずに個性を借りる方法。','shadcn 호환, 물리적 촉감의 컴포넌트. 일관성을 해치지 않고 개성을 빌리는 법.','Komponen serasi shadcn yang terasa fizikal.','Component tương thích shadcn có cảm giác vật lý.',"Composants compatibles shadcn au toucher physique.",'Componentes compatibles con shadcn con tacto físico.','shadcn-kompatible Komponenten mit physischem Gefühl.'),
 en="""<p>Cult UI is an open-source collection of shadcn-compatible components with a distinctly tactile feel: a dynamic-island style container, textured and "neumorphic-lite" buttons, expandable cards, and playful toolbars. Where Aceternity leans on spectacle, Cult UI leans on <strong>interaction feel</strong>: springs, squish and layout animation.</p>
<h2>Where it shines</h2>
<ul><li>Small product surfaces (toolbars, popovers, status pills) that benefit from springy layout transitions.</li>
<li>Portfolio and indie-product pages where personality is the point.</li>
<li>Learning material: reading the source is a good way to learn layout animation with Motion.</li></ul>
<h2>Keeping consistency</h2>
<p>Personality components drift from your system fast. Before adopting one, map its colours and radii onto your tokens, match its spring settings across components so motion feels like one family, and check keyboard support: custom toggles and islands need visible focus and proper roles.</p>
<h2>Our take</h2>
<p>Cult UI is a reference for the "Cult" in the house style list: tactile micro-interaction over loud backgrounds. Pick one signature interaction per product and let it recur, rather than mixing every clever component on one page.</p>""",
 zh="""<p>Cult UI 是一套开源、兼容 shadcn 的组件集，手感特别强：灵动岛式容器、带质感的「轻拟物」按钮、可展开卡片、俏皮的工具栏。Aceternity 靠视觉奇观，Cult UI 靠<strong>交互手感</strong>：弹簧、挤压和布局动画。</p>
<h2>它擅长的地方</h2>
<ul><li>小型产品界面（工具栏、弹出层、状态胶囊），适合有弹性的布局过渡。</li>
<li>作品集和独立产品页，个性本身就是卖点。</li>
<li>学习材料：读它的源码是学 Motion 布局动画的好方法。</li></ul>
<h2>保持一致性</h2>
<p>有个性的组件很容易偏离你的设计系统。采用前，把它的颜色和圆角映射到你的 Token 上，统一各组件的弹簧参数让动效像一家人，再检查键盘支持：自定义开关和灵动岛需要可见的焦点和正确的 role。</p>
<h2>我们的看法</h2>
<p>Cult UI 就是风格清单里「Cult」的出处：用有手感的微交互，而不是喧闹的背景。每个产品选一个标志性交互反复出现，而不是把所有巧妙组件堆在同一页。</p>""",
 refs=[('Cult UI','Cult UI','https://www.cult-ui.com/'),('nolly-studio/cult-ui','GitHub','https://github.com/nolly-studio/cult-ui'),('Layout animations','Motion','https://motion.dev/docs/react-layout-animations'),('ARIA Authoring Practices Guide','W3C','https://www.w3.org/WAI/ARIA/apg/')]),

dict(slug='shadcn-blocks-deep-dive', date=D, cat='components', series='library-deep-dive', tags=['shadcn','blocks','registry'],
 t=T('shadcn blocks and registries: page sections as source code','shadcn Blocks 与 Registry：把页面区块当源码','shadcn Blocks 與 Registry：把頁面區塊當原始碼','shadcnブロックとレジストリ：ページ部品をソースとして','shadcn 블록과 레지스트리: 페이지 섹션을 소스 코드로','Blok dan registry shadcn: bahagian halaman sebagai kod sumber','shadcn blocks và registry: khối trang dưới dạng mã nguồn',"Blocs et registres shadcn : des sections de page en code source",'Bloques y registros de shadcn: secciones como código fuente','shadcn-Blocks und Registries: Seitenabschnitte als Quellcode'),
 s=T('Blocks (dashboards, sidebars, login pages) install with one CLI command, and any team can publish its own registry. Why this is the best substrate for AI agents.','Blocks（仪表盘、侧栏、登录页）一条 CLI 命令就能装，任何团队都能发布自己的 registry。为什么这是 AI 智能体最好的底座。','Blocks（儀表板、側欄、登入頁）一條 CLI 指令就能裝，任何團隊都能發布自己的 registry。為何這是 AI 智慧體最好的底座。','ブロックはCLI一発で導入、どのチームも独自レジストリを公開可能。AIエージェントに最適な土台の理由。','블록은 CLI 한 줄로 설치, 누구나 레지스트리 공개 가능. AI 에이전트에 최적인 이유.','Blok dipasang dengan satu arahan CLI; mana-mana pasukan boleh terbitkan registry.','Block cài bằng một lệnh CLI; nhóm nào cũng có thể phát hành registry riêng.',"Les blocs s'installent en une commande ; chaque équipe peut publier son registre.",'Los bloques se instalan con un comando; cualquier equipo puede publicar su registro.','Blocks per CLI-Befehl; jedes Team kann eine eigene Registry veröffentlichen.'),
 en="""<p>shadcn/ui is not a package you install; it is a set of components whose source you copy into your project. Blocks extend the idea to whole sections: dashboards, sidebars, login and signup pages, charts. Each is added with the CLI, for example <code>npx shadcn@latest add dashboard-01</code>, and lands as editable files.</p>
<h2>Registries: everyone can publish</h2>
<p>The shadcn registry format lets any team publish components, blocks, hooks and theme files as JSON that the CLI understands. Magic UI, Cult UI and many others distribute this way, and you can run a private registry for your own design system.</p>
<pre><code>npx shadcn@latest add https://your-registry.example/r/pricing-01.json</code></pre>
<h2>Why agents love this model</h2>
<ul><li>The code is local, so an agent can read and edit it like any file.</li>
<li>Names are stable and documented, so prompts can reference them ("add sidebar-07").</li>
<li>Theme lives in CSS variables, so one token change restyles everything the agent generated.</li></ul>
<h2>Our take</h2>
<p>If you want AI-generated UI to stay consistent, give the agent a registry, not a style adjective. Start from official blocks, restyle via tokens, and publish your modified versions to a private registry so every future session builds from your system.</p>""",
 zh="""<p>shadcn/ui 不是一个要安装的依赖包，而是一套你把源码复制进项目的组件。Blocks 把这个思路扩展到整个区块：仪表盘、侧栏、登录注册页、图表。每个都用 CLI 添加，例如 <code>npx shadcn@latest add dashboard-01</code>，落地为可编辑的文件。</p>
<h2>Registry：人人都能发布</h2>
<p>shadcn 的 registry 格式让任何团队都能把组件、区块、hooks 和主题文件发布成 CLI 能读的 JSON。Magic UI、Cult UI 等很多库都这样分发，你也可以给自己的设计系统搭一个私有 registry。</p>
<pre><code>npx shadcn@latest add https://your-registry.example/r/pricing-01.json</code></pre>
<h2>为什么智能体喜欢这种模式</h2>
<ul><li>代码在本地，智能体可以像读写普通文件一样读写它。</li>
<li>名字稳定且有文档，提示里可以直接引用（「加上 sidebar-07」）。</li>
<li>主题放在 CSS 变量里，改一个 Token 就能给智能体生成的所有界面换装。</li></ul>
<h2>我们的看法</h2>
<p>想让 AI 生成的界面保持一致，就给智能体一个 registry，而不是一个风格形容词。从官方 blocks 起步，用 Token 换风格，再把改过的版本发布到私有 registry，之后每次会话都从你的系统出发。</p>""",
 refs=[('Blocks','shadcn/ui','https://ui.shadcn.com/blocks'),('Registry','shadcn/ui','https://ui.shadcn.com/docs/registry'),('CLI','shadcn/ui','https://ui.shadcn.com/docs/cli'),('Theming','shadcn/ui','https://ui.shadcn.com/docs/theming')]),

dict(slug='typography-for-ai-generated-ui', date=D, cat='craft', tags=['typography','tokens'],
 t=T('Typography for AI-generated UI: the fastest way to look less generic','AI 生成界面的字体排印：摆脱平庸感最快的办法','AI 產生介面的字體排印：擺脫平庸感最快的辦法','AI生成UIのタイポグラフィ：没個性から抜け出す最短路','AI 생성 UI의 타이포그래피: 평범함을 벗는 가장 빠른 길','Tipografi untuk UI jana AI','Typography cho UI do AI tạo: cách nhanh nhất để bớt tầm thường',"La typographie des UI générées par IA",'Tipografía para UI generada por IA','Typografie für KI-generierte UIs'),
 s=T('Generators default to one sans at three sizes. A type scale, a second typeface, tighter tracking on display sizes and real line lengths fix most of it.','生成器默认一种无衬线、三个字号。一套字号阶梯、第二种字体、大字号收紧字距和合理行长，能解决大部分问题。','產生器預設一種無襯線、三個字級。一套字級階梯、第二種字體、大字收緊字距和合理行長，能解決大部分問題。','生成器は1書体3サイズが既定。スケール、第2書体、見出しの字詰め、行長で大半が直る。','생성기는 산세리프 하나에 크기 셋. 스케일, 두 번째 서체, 자간, 줄 길이로 대부분 해결.','Skala jenis, muka taip kedua, jarak huruf dan panjang baris menyelesaikan kebanyakannya.','Thang cỡ chữ, font thứ hai, giãn chữ và độ dài dòng giải quyết phần lớn.',"Une échelle, une seconde police, l'approche et la longueur de ligne règlent l'essentiel.",'Una escala, una segunda fuente, el tracking y la longitud de línea resuelven casi todo.','Skala, zweite Schrift, Laufweite und Zeilenlänge lösen das meiste.'),
 en="""<p>Ask any generator for a landing page and you will usually get one sans-serif at body, heading and caption sizes. Typography is the cheapest lever to move a page away from that default, and it is easy to specify precisely in a prompt.</p>
<h2>Five rules to put in the brief</h2>
<ol><li><strong>Use a modular scale.</strong> Pick a ratio (1.2 for dense apps, 1.25–1.333 for marketing) and name the steps as tokens.</li>
<li><strong>Pair two typefaces with a job each.</strong> A display face for headlines (a serif such as Instrument Serif, or a tight grotesk) and a workhorse sans for UI.</li>
<li><strong>Tighten large text.</strong> Negative letter-spacing (around −0.02em) on display sizes; leave body text at default.</li>
<li><strong>Constrain line length.</strong> Roughly 45–75 characters for Latin body text; use <code>max-width: 65ch</code>.</li>
<li><strong>Fluid sizes.</strong> <code>clamp()</code> for headlines so mobile does not inherit desktop sizes.</li></ol>
<h2>CJK needs its own settings</h2>
<p>For Chinese and Japanese, use a slightly larger line-height (about 1.7), avoid negative tracking, and use <code>word-break: keep-all</code> or <code>text-wrap: balance</code> on headings so short phrases are not orphaned, the fix we applied to our own Japanese headings.</p>
<h2>Our take</h2>
<p>If you only change one thing in AI output, change the type scale and the display face. It is a two-line token edit with a visible payoff.</p>""",
 zh="""<p>让任何生成器做一个落地页，你通常会得到一种无衬线字体，分成正文、标题和说明三个字号。字体排印是把页面拉离默认样式最便宜的杠杆，而且在提示里很容易说精确。</p>
<h2>写进需求的五条规则</h2>
<ol><li><strong>用模数字号阶梯。</strong>选一个比例（紧凑应用 1.2，营销页 1.25–1.333），每一级起个 Token 名。</li>
<li><strong>两种字体，各司其职。</strong>标题用展示字体（Instrument Serif 这类衬线，或紧凑的怪诞体），界面用耐用的无衬线。</li>
<li><strong>大字收紧字距。</strong>展示字号用负字距（约 −0.02em），正文保持默认。</li>
<li><strong>限制行长。</strong>拉丁文正文大约每行 45–75 个字符，用 <code>max-width: 65ch</code>。</li>
<li><strong>流式字号。</strong>标题用 <code>clamp()</code>，别让手机继承桌面字号。</li></ol>
<h2>中日韩文字要单独设置</h2>
<p>中文和日文的行高要稍大（约 1.7），不要用负字距；标题用 <code>word-break: keep-all</code> 或 <code>text-wrap: balance</code>，避免短语被拆到下一行孤零零一个字。我们自己的日语标题就是这样修好的。</p>
<h2>我们的看法</h2>
<p>如果 AI 产出只改一处，就改字号阶梯和展示字体。两行 Token 的改动，效果立竿见影。</p>""",
 refs=[('Practical Typography: line length','Matthew Butterick','https://practicaltypography.com/line-length.html'),('text-wrap','MDN','https://developer.mozilla.org/en-US/docs/Web/CSS/text-wrap'),('clamp()','MDN','https://developer.mozilla.org/en-US/docs/Web/CSS/clamp'),('Utopia fluid type scale','Utopia','https://utopia.fyi/type/calculator/'),('Requirements for Chinese Text Layout','W3C','https://www.w3.org/TR/clreq/')]),

dict(slug='oklch-color-and-dark-mode', date=D, cat='craft', tags=['color','OKLCH','dark mode'],
 t=T('OKLCH colour systems: palettes that survive dark mode','OKLCH 色彩系统：经得起暗色模式的调色板','OKLCH 色彩系統：經得起暗色模式的調色盤','OKLCHカラー：ダークモードに耐えるパレット','OKLCH 색 체계: 다크 모드에서도 버티는 팔레트','Sistem warna OKLCH: palet yang tahan mod gelap','Hệ màu OKLCH: bảng màu sống sót trong dark mode',"Couleurs OKLCH : des palettes qui tiennent en mode sombre",'Color OKLCH: paletas que sobreviven al modo oscuro','OKLCH-Farben: Paletten, die den Dark Mode überstehen'),
 s=T('OKLCH keeps perceived lightness consistent across hues, so you can generate scales and dark themes by math instead of eyeballing. Tailwind v4 uses it by default.','OKLCH 让不同色相的感知亮度保持一致，色阶和暗色主题可以靠计算而不是靠肉眼。Tailwind v4 默认就用它。','OKLCH 讓不同色相的感知亮度保持一致，色階與暗色主題可以靠計算而非肉眼。Tailwind v4 預設就用它。','OKLCHは色相間で知覚明度を揃え、計算でスケールとダークテーマを作れる。Tailwind v4の既定。','OKLCH는 색상 간 지각 명도를 맞춰 계산으로 스케일과 다크 테마를 만든다. Tailwind v4 기본값.','OKLCH mengekalkan kecerahan persepsi; Tailwind v4 menggunakannya secara lalai.','OKLCH giữ độ sáng cảm nhận đồng đều; Tailwind v4 dùng mặc định.',"OKLCH garde une luminosité perçue constante ; Tailwind v4 l'utilise par défaut.",'OKLCH mantiene la luminosidad percibida; Tailwind v4 lo usa por defecto.','OKLCH hält die wahrgenommene Helligkeit konstant; Standard in Tailwind v4.'),
 en="""<p>OKLCH is a CSS colour space (CSS Color Level 4) defined by lightness, chroma and hue. Its lightness channel tracks perceived brightness far better than HSL's, so a yellow and a blue at the same L actually look similarly light. Tailwind CSS v4 switched its default palette to OKLCH, and all modern browsers support <code>oklch()</code>.</p>
<h2>Building a scale</h2>
<pre><code>--brand-50:  oklch(97% 0.02 250);
--brand-500: oklch(62% 0.17 250);
--brand-900: oklch(30% 0.09 250);</code></pre>
<p>Keep hue fixed, step lightness evenly, and reduce chroma at the extremes, where sRGB screens cannot display high chroma anyway.</p>
<h2>Dark mode by lightness, not inversion</h2>
<ul><li>Surfaces: very low L (around 14–20%) with a hint of the brand hue instead of pure black.</li>
<li>Text: high L but not 100%, to reduce glare.</li>
<li>Accent: raise L and lower chroma slightly so it does not vibrate on dark backgrounds.</li>
<li>Re-check contrast: equal OKLCH lightness differences do not guarantee WCAG ratios, so test with a contrast checker.</li></ul>
<h2>Our take</h2>
<p>Give agents colour tokens in OKLCH with light and dark values side by side. It makes "make it darker" or "add a success colour" a predictable edit instead of a guess.</p>""",
 zh="""<p>OKLCH 是 CSS Color Level 4 里的色彩空间，由亮度（L）、彩度（C）和色相（H）定义。它的亮度通道比 HSL 更贴近人眼感知，同样 L 值的黄色和蓝色看起来亮度确实接近。Tailwind CSS v4 已把默认调色板换成 OKLCH，所有现代浏览器都支持 <code>oklch()</code>。</p>
<h2>做一套色阶</h2>
<pre><code>--brand-50:  oklch(97% 0.02 250);
--brand-500: oklch(62% 0.17 250);
--brand-900: oklch(30% 0.09 250);</code></pre>
<p>固定色相，亮度均匀递进，两端降低彩度，反正 sRGB 屏幕在两端也显示不出高彩度。</p>
<h2>暗色模式靠调亮度，不靠反色</h2>
<ul><li>背景：很低的 L（约 14–20%），带一点品牌色相，而不是纯黑。</li>
<li>文字：高 L 但不到 100%，减少刺眼。</li>
<li>强调色：L 稍升、彩度稍降，避免在深色背景上「发颤」。</li>
<li>重新检查对比度：OKLCH 亮度差相等并不保证符合 WCAG 对比度，要用对比度工具实测。</li></ul>
<h2>我们的看法</h2>
<p>给智能体的颜色 Token 用 OKLCH，亮色和暗色值并排写。这样「再暗一点」「加一个成功色」就成了可预期的改动，而不是瞎猜。</p>""",
 refs=[('oklch()','MDN','https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/oklch'),('OKLCH in CSS: why we moved from RGB and HSL','Evil Martians','https://evilmartians.com/chronicles/oklch-in-css-why-quit-rgb-hsl'),('OKLCH Color Picker','oklch.com','https://oklch.com/'),('Tailwind CSS v4.0','Tailwind Labs','https://tailwindcss.com/blog/tailwindcss-v4'),('WebAIM Contrast Checker','WebAIM','https://webaim.org/resources/contrastchecker/')]),
]
POSTS2 += [
dict(slug='landing-page-teardown-linear-vercel', date=D, cat='teardown', tags=['landing page','teardown','case study'],
 t=T('Landing page teardown: what Linear and Vercel get right','落地页拆解：Linear 和 Vercel 做对了什么','落地頁拆解：Linear 和 Vercel 做對了什麼','LP分解：LinearとVercelが正しくやっていること','랜딩 페이지 해부: Linear와 Vercel이 잘하는 것','Bedah halaman pendaratan: Linear dan Vercel','Mổ xẻ landing page: Linear và Vercel làm đúng gì',"Décorticage de landing pages : ce que Linear et Vercel réussissent",'Desmontando landings: lo que Linear y Vercel hacen bien','Landingpage-Analyse: was Linear und Vercel richtig machen'),
 s=T('Two widely copied developer-tool homepages, read as a list of decisions: one message, product as hero image, dark restraint, and proof placed right after the promise.','两个被大量模仿的开发者工具首页，拆成一串决策：一句主张、产品即首图、克制的深色、承诺之后紧跟证据。','兩個被大量模仿的開發者工具首頁，拆成一串決策：一句主張、產品即首圖、克制的深色、承諾之後緊跟證據。','模倣される2つのトップページを決定の連続として読む。','많이 모방되는 두 홈페이지를 결정 목록으로 읽는다.','Dua laman utama yang banyak ditiru, dibaca sebagai senarai keputusan.','Hai trang chủ bị bắt chước nhiều, đọc như chuỗi quyết định.',"Deux pages d'accueil très copiées, lues comme une liste de décisions.",'Dos homes muy copiadas, leídas como una lista de decisiones.','Zwei oft kopierte Startseiten als Liste von Entscheidungen gelesen.'),
 en="""<p>Linear's and Vercel's homepages are among the most imitated in software. Copying their gradients misses the point; what is worth copying is a set of decisions you can see by reading the pages carefully. Screenshots below were captured on 14 October 2026; both sites change often.</p>
<h2>Decisions worth stealing</h2>
<ol><li><strong>One sentence of positioning</strong> in the hero, large, with a short supporting line. No feature list above the fold.</li>
<li><strong>The product is the hero image.</strong> Real UI (or a faithful render of it) instead of an illustration, so the visitor sees what they would use.</li>
<li><strong>Restraint in colour.</strong> Mostly neutral surfaces; accent colour reserved for action and emphasis.</li>
<li><strong>Proof straight after the promise:</strong> customer logos or concrete product capabilities right below the hero.</li>
<li><strong>Sections with one idea each,</strong> each with a short heading and a visual that demonstrates it.</li></ol>
<h2>What not to copy</h2>
<ul><li>Their brand recognition: a minimal hero works when people already know the name; a new product may need a more explicit line.</li>
<li>Heavy custom motion and 3D renders that took dedicated teams; a static, sharp product shot beats a mediocre animation.</li></ul>
<h2>Checklist for your page</h2>
<p>Can a stranger say what you sell after five seconds? Is the first image your actual product? Is there exactly one primary CTA? Does every section prove one claim? If yes, the gradient is optional.</p>""",
 zh="""<p>Linear 和 Vercel 的首页是软件行业被模仿最多的页面之一。照抄它们的渐变没抓到重点；值得学的是一组决策，仔细读页面就能看出来。下方截图于 2026 年 10 月 14 日截取，两个网站都经常改版。</p>
<h2>值得偷的决策</h2>
<ol><li><strong>首屏只有一句定位，</strong>字很大，配一行简短说明。首屏不放功能列表。</li>
<li><strong>产品就是首图。</strong>用真实界面（或忠实的渲染）代替插画，访客一眼看到自己将要用什么。</li>
<li><strong>颜色克制。</strong>大面积中性色，强调色只留给操作和重点。</li>
<li><strong>承诺之后紧跟证据：</strong>首屏下方就是客户 Logo 或具体的产品能力。</li>
<li><strong>每个区块只讲一件事，</strong>一个短标题加一张能证明它的图。</li></ol>
<h2>不要照抄的部分</h2>
<ul><li>它们的品牌知名度：大家已经认识这个名字，极简首屏才行得通；新产品可能需要说得更直白。</li>
<li>需要专门团队才能做出的重度动效和 3D 渲染；一张清晰的静态产品图胜过一个平庸的动画。</li></ul>
<h2>给你自己页面的检查清单</h2>
<p>陌生人五秒内能说出你卖什么吗？第一张图是你真实的产品吗？主 CTA 是不是只有一个？每个区块是否都在证明一个观点？都做到了，渐变可有可无。</p>""",
 refs=[('Linear homepage','Linear','https://linear.app/'),('Vercel homepage','Vercel','https://vercel.com/'),('The 5-second test','Nielsen Norman Group','https://www.nngroup.com/articles/first-impressions-human-automaticity/'),('Landing page design best practices','Nielsen Norman Group','https://www.nngroup.com/articles/homepage-design-principles/')]),

dict(slug='dashboard-design-patterns', date=D, cat='craft', tags=['dashboard','data','patterns'],
 t=T('Dashboard patterns that hold up: from KPI strip to drill-down table','经得起用的仪表盘模式：从指标条到下钻表格','經得起用的儀表板模式：從指標條到下鑽表格','使えるダッシュボードの型：KPIからドリルダウン表まで','버티는 대시보드 패턴: KPI 띠부터 드릴다운 표까지','Corak papan pemuka yang tahan','Mẫu dashboard bền vững: từ dải KPI đến bảng drill-down',"Des patterns de dashboard qui tiennent",'Patrones de dashboard que funcionan','Dashboard-Muster, die halten'),
 s=T('AI tools love to generate twelve charts. Good dashboards answer three questions in order: is it OK, what changed, why. A layout and a component list for each.','AI 工具爱生成十二张图表。好的仪表盘按顺序回答三个问题：正常吗、变了什么、为什么。每一层对应的布局和组件。','AI 工具愛產生十二張圖表。好的儀表板依序回答三個問題：正常嗎、變了什麼、為什麼。每層對應的版面與元件。','良いダッシュボードは「大丈夫か・何が変わったか・なぜか」の順に答える。','좋은 대시보드는 괜찮은가, 무엇이 바뀌었나, 왜인가 순으로 답한다.','Papan pemuka yang baik menjawab tiga soalan mengikut urutan.','Dashboard tốt trả lời ba câu theo thứ tự: ổn không, đổi gì, tại sao.',"Un bon dashboard répond dans l'ordre : ça va ? qu'est-ce qui change ? pourquoi ?",'Un buen dashboard responde: ¿va bien?, ¿qué cambió?, ¿por qué?','Gute Dashboards beantworten: Läuft es? Was hat sich geändert? Warum?'),
 en="""<p>Ask a generator for an "analytics dashboard" and you will likely get a sidebar, four stat cards and a grid of charts of equal weight. It looks complete and answers nothing. A better structure follows the questions a user actually asks, in order.</p>
<h2>Three layers</h2>
<ol><li><strong>Is everything OK?</strong> A KPI strip of 3–5 numbers, each with the comparison period and a direction, not a sparkline zoo.</li>
<li><strong>What changed?</strong> One primary time-series chart with a range selector, annotated where something happened.</li>
<li><strong>Why?</strong> A sortable, filterable table that drills into detail. Tables are where people actually work.</li></ol>
<h2>Details generators skip</h2>
<ul><li>Tabular figures (<code>font-variant-numeric: tabular-nums</code>) so numbers align.</li>
<li>Right-aligned numeric columns, left-aligned text.</li>
<li>Empty, loading (skeleton) and error states for every widget.</li>
<li>Units and time zone in labels; a "last updated" timestamp.</li>
<li>Colour used for status only, with a non-colour cue (icon or text) for colour-blind users.</li></ul>
<h2>Components to start from</h2>
<p>shadcn's dashboard blocks and its charts (built on Recharts) give you the scaffolding; Tremor offers dashboard-focused React components. Specify the three layers in your prompt and you get a page people can use, not just screenshot.</p>""",
 zh="""<p>让生成器做一个「数据分析仪表盘」，大概率得到一个侧栏、四张数字卡和一堆同样大小的图表。看起来很完整，却什么也没回答。更好的结构是按用户真正会问的问题依次排布。</p>
<h2>三个层次</h2>
<ol><li><strong>一切正常吗？</strong>3–5 个数字组成的指标条，每个带对比周期和涨跌方向，而不是一堆迷你折线图。</li>
<li><strong>变了什么？</strong>一张主时序图配时间范围选择，在发生事情的地方加标注。</li>
<li><strong>为什么？</strong>可排序、可筛选、能下钻的表格。表格才是用户真正干活的地方。</li></ol>
<h2>生成器常漏掉的细节</h2>
<ul><li>等宽数字（<code>font-variant-numeric: tabular-nums</code>），让数字对齐。</li>
<li>数字列右对齐，文字列左对齐。</li>
<li>每个组件都有空状态、加载骨架和错误状态。</li>
<li>标签里写单位和时区，再加一个「最后更新时间」。</li>
<li>颜色只表示状态，同时配非颜色提示（图标或文字），照顾色弱用户。</li></ul>
<h2>从哪些组件起步</h2>
<p>shadcn 的仪表盘区块和图表（基于 Recharts）提供骨架；Tremor 提供专为仪表盘设计的 React 组件。在提示里写明这三个层次，你得到的就是能用的页面，而不只是好截图。</p>""",
 refs=[('Dashboard blocks','shadcn/ui','https://ui.shadcn.com/blocks'),('Charts','shadcn/ui','https://ui.shadcn.com/charts'),('Tremor','Tremor','https://tremor.so/'),('Dashboards: making charts and graphs easier to understand','Nielsen Norman Group','https://www.nngroup.com/articles/dashboards-preattentive/'),('font-variant-numeric','MDN','https://developer.mozilla.org/en-US/docs/Web/CSS/font-variant-numeric')]),

dict(slug='design-tokens-for-agents', date=D, cat='agents', series='agent-context', featured=True, tags=['design tokens','DTCG','agents'],
 t=T('Design tokens for agents: the file that makes AI output on-brand','给智能体的设计 Token：让 AI 产出符合品牌的那份文件','給智慧體的設計 Token：讓 AI 產出符合品牌的那份檔案','エージェントのためのデザイントークン','에이전트를 위한 디자인 토큰','Token reka bentuk untuk ejen','Design token cho agent: file giúp AI ra đúng thương hiệu',"Des design tokens pour les agents",'Design tokens para agentes','Design Tokens für Agents'),
 s=T('A machine-readable token file (the W3C DTCG format) plus a short usage note beats any adjective in a prompt. Structure, naming, and how to hand it to an agent.','一份机器可读的 Token 文件（W3C DTCG 格式）加一段简短用法说明，胜过提示里任何形容词。结构、命名和交给智能体的方法。','一份機器可讀的 Token 檔（W3C DTCG 格式）加一段簡短用法說明，勝過提示裡任何形容詞。結構、命名與交給智慧體的方法。','機械可読なトークン(W3C DTCG)と短い使い方メモはどんな形容詞にも勝る。','기계가 읽는 토큰 파일(W3C DTCG)과 짧은 사용법이 어떤 형용사보다 낫다.','Fail token boleh dibaca mesin (DTCG) mengatasi kata sifat dalam prompt.','File token máy đọc được (DTCG) cùng ghi chú ngắn hơn mọi tính từ trong prompt.',"Un fichier de tokens lisible par machine (DTCG) vaut mieux que tout adjectif.",'Un archivo de tokens legible por máquina (DTCG) supera a cualquier adjetivo.','Eine maschinenlesbare Token-Datei (DTCG) schlägt jedes Adjektiv.'),
 en="""<p>Agents follow concrete values far more reliably than descriptions. A design token file turns "clean, premium, a bit playful" into numbers the agent can apply everywhere. The W3C Design Tokens Community Group (DTCG) publishes a vendor-neutral JSON format for this, supported by tools such as Style Dictionary and Tokens Studio.</p>
<h2>A minimal structure</h2>
<pre><code>{
  "color": { "accent": { "$type": "color", "$value": "oklch(62% 0.17 250)" } },
  "radius": { "md": { "$type": "dimension", "$value": "10px" } },
  "space": { "4": { "$type": "dimension", "$value": "16px" } }
}</code></pre>
<h2>Three tiers of naming</h2>
<ul><li><strong>Primitive:</strong> raw values (<code>blue-500</code>, <code>space-4</code>).</li>
<li><strong>Semantic:</strong> intent (<code>surface</code>, <code>text-muted</code>, <code>accent</code>, <code>danger</code>). Agents should mostly use these.</li>
<li><strong>Component:</strong> optional overrides (<code>button-radius</code>).</li></ul>
<h2>Handing it to an agent</h2>
<ol><li>Export tokens to CSS variables and commit them; tell the agent "never hard-code colours or spacing, use these variables".</li>
<li>Add a one-page usage note: which token for which job, plus three do/don't pairs.</li>
<li>Reference both from your AGENTS.md, Cursor rules or skill so every session loads them.</li>
<li>Verify: grep generated code for raw hex values as a cheap lint.</li></ol>
<p>Our encyclopedia's colour, spacing and type spec digests are written to be pasted into exactly this kind of usage note.</p>""",
 zh="""<p>智能体遵循具体数值远比遵循描述可靠。设计 Token 文件把「干净、高级、带点俏皮」变成智能体能处处套用的数字。W3C 设计 Token 社区组（DTCG）为此发布了一种与厂商无关的 JSON 格式，Style Dictionary、Tokens Studio 等工具都支持。</p>
<h2>最小结构</h2>
<pre><code>{
  "color": { "accent": { "$type": "color", "$value": "oklch(62% 0.17 250)" } },
  "radius": { "md": { "$type": "dimension", "$value": "10px" } },
  "space": { "4": { "$type": "dimension", "$value": "16px" } }
}</code></pre>
<h2>三层命名</h2>
<ul><li><strong>基础层：</strong>原始值（<code>blue-500</code>、<code>space-4</code>）。</li>
<li><strong>语义层：</strong>表达意图（<code>surface</code>、<code>text-muted</code>、<code>accent</code>、<code>danger</code>）。智能体应主要用这一层。</li>
<li><strong>组件层：</strong>可选的覆盖值（<code>button-radius</code>）。</li></ul>
<h2>交给智能体</h2>
<ol><li>把 Token 导出成 CSS 变量并提交；告诉智能体「颜色和间距一律不许写死，用这些变量」。</li>
<li>附一页用法说明：哪个 Token 用在哪里，再加三组该做/不该做。</li>
<li>在 AGENTS.md、Cursor rules 或 skill 里引用这两份文件，让每次会话都加载。</li>
<li>验证：在生成的代码里搜索裸十六进制色值，这是最便宜的检查。</li></ol>
<p>本站百科里的颜色、间距、字体规范摘要，就是按能直接贴进这类用法说明的格式写的。</p>""",
 refs=[('Design Tokens Community Group','W3C','https://www.w3.org/community/design-tokens/'),('Design Tokens Format Module','DTCG','https://www.designtokens.org/'),('Style Dictionary','Style Dictionary','https://styledictionary.com/'),('Tokens Studio','Tokens Studio','https://tokens.studio/')]),

dict(slug='claude-cursor-design-skills', date=D, cat='agents', series='agent-context', tags=['skills','Claude','Cursor','rules'],
 t=T('Design skills for Claude and Cursor: SKILL.md, rules and AGENTS.md','Claude 与 Cursor 的设计技能：SKILL.md、rules 和 AGENTS.md','Claude 與 Cursor 的設計技能：SKILL.md、rules 和 AGENTS.md','ClaudeとCursorのデザインスキル：SKILL.md・rules・AGENTS.md','Claude와 Cursor의 디자인 스킬: SKILL.md, rules, AGENTS.md','Kemahiran reka bentuk untuk Claude dan Cursor','Skill thiết kế cho Claude và Cursor: SKILL.md, rules, AGENTS.md',"Compétences design pour Claude et Cursor",'Skills de diseño para Claude y Cursor','Design-Skills für Claude und Cursor'),
 s=T('Three file formats, one idea: durable instructions an agent loads when relevant. How to write a design skill that changes output, with a template.','三种文件格式，一个思路：智能体在相关时加载的持久指令。怎样写一个真正改变产出的设计技能，附模板。','三種檔案格式，一個思路：智慧體在相關時載入的持久指令。怎樣寫一個真正改變產出的設計技能，附範本。','3つの形式、1つの考え方。出力を変えるデザインスキルの書き方とテンプレート。','세 가지 형식, 하나의 아이디어. 출력을 바꾸는 디자인 스킬 작성법과 템플릿.','Tiga format fail, satu idea. Cara menulis kemahiran reka bentuk, dengan templat.','Ba định dạng, một ý tưởng. Cách viết skill thiết kế thật sự thay đổi kết quả, kèm mẫu.',"Trois formats, une idée. Comment écrire une compétence design efficace, avec modèle.",'Tres formatos, una idea. Cómo escribir un skill de diseño eficaz, con plantilla.','Drei Formate, eine Idee. So schreibt man einen wirksamen Design-Skill, mit Vorlage.'),
 en="""<p>Anthropic's Agent Skills are folders with a <code>SKILL.md</code> file: YAML front matter (a name and a description) followed by instructions, optionally with scripts and assets. The agent sees the descriptions and loads a skill's full body only when it is relevant. Cursor offers project rules in <code>.cursor/rules</code>, and many coding agents read an <code>AGENTS.md</code> at the repo root. Different files, same idea: durable, scoped instructions.</p>
<h2>What makes a design skill work</h2>
<ul><li><strong>A precise description</strong>, because it decides when the skill loads ("Use when building or restyling web UI").</li>
<li><strong>Bans before wishes.</strong> Models respond well to a short list of things never to do (text gradients, emoji icons, centred paragraphs, more than one accent).</li>
<li><strong>Concrete values:</strong> tokens, scales, a reference to the token file.</li>
<li><strong>A verification step:</strong> "render in a browser at 390px and 1440px, light and dark, before saying done".</li></ul>
<h2>A template</h2>
<pre><code>---
name: house-ui
description: Use when creating or restyling any web page or component.
---
1. Load tokens from styles/tokens.css. Never hard-code colour/spacing.
2. Type: Instrument Serif display, Geist UI, scale 1.25.
3. Never: text gradients, emoji icons, glassmorphism stacks.
4. One signature effect per page (see /kb/ house style).
5. Verify in a browser: 390/1440px, light/dark, keyboard focus.</code></pre>
<h2>Where to find good ones</h2>
<p>Anthropic's public skills repository includes a frontend-design skill; community skills such as taste-skill and impeccable focus on aesthetics. Our encyclopedia indexes the ones we use, with full text where the licence allows.</p>""",
 zh="""<p>Anthropic 的 Agent Skills 是带 <code>SKILL.md</code> 文件的文件夹：开头是 YAML 元数据（名称和描述），后面是指令，可以附带脚本和素材。智能体先看到所有描述，只有相关时才加载完整内容。Cursor 提供放在 <code>.cursor/rules</code> 里的项目规则，很多编程智能体会读取仓库根目录的 <code>AGENTS.md</code>。文件不同，思路一样：持久、有作用范围的指令。</p>
<h2>好的设计技能有什么特点</h2>
<ul><li><strong>描述要精确</strong>，因为它决定什么时候加载（「在构建或改造网页界面时使用」）。</li>
<li><strong>先写禁令，再写愿望。</strong>模型对简短的「绝不做」清单反应很好（渐变文字、emoji 图标、段落居中、多于一个强调色）。</li>
<li><strong>具体数值：</strong>Token、阶梯、指向 Token 文件的引用。</li>
<li><strong>验证步骤：</strong>「宣布完成前，在浏览器里以 390px 和 1440px、亮色和暗色渲染检查」。</li></ul>
<h2>模板</h2>
<pre><code>---
name: house-ui
description: Use when creating or restyling any web page or component.
---
1. Load tokens from styles/tokens.css. Never hard-code colour/spacing.
2. Type: Instrument Serif display, Geist UI, scale 1.25.
3. Never: text gradients, emoji icons, glassmorphism stacks.
4. One signature effect per page (see /kb/ house style).
5. Verify in a browser: 390/1440px, light/dark, keyboard focus.</code></pre>
<h2>去哪找好的技能</h2>
<p>Anthropic 的公开 skills 仓库里有 frontend-design 技能；社区的 taste-skill、impeccable 等专注审美。本站百科收录了我们在用的技能，许可证允许的附全文。</p>""",
 refs=[('Agent Skills overview','Anthropic','https://docs.anthropic.com/en/docs/agents-and-tools/agent-skills/overview'),('anthropics/skills','GitHub','https://github.com/anthropics/skills'),('Rules','Cursor docs','https://docs.cursor.com/context/rules'),('AGENTS.md','agents.md','https://agents.md/'),('taste-skill','GitHub','https://github.com/Leonxlnx/taste-skill')]),

dict(slug='weekly-roundup-2026-w42', date=D, cat='news', series='weekly', featured=True, tags=['news','weekly','Figma','Lovable','MagicOS'],
 t=T('Weekly roundup, 14 Oct 2026: guideline files go mainstream','设计周报 2026-10-14：规范文件成为主流','設計週報 2026-10-14：規範檔成為主流','週刊まとめ 2026/10/14：ガイドラインファイルが主流に','주간 정리 2026-10-14: 가이드라인 파일이 대세로','Ringkasan mingguan 14 Okt 2026','Tổng hợp tuần 14/10/2026: file hướng dẫn thành xu hướng',"Revue hebdo du 14/10/2026 : les fichiers de guidelines s'imposent",'Resumen semanal 14/10/2026: los archivos de guías se imponen','Wochenrückblick 14.10.2026: Guideline-Dateien setzen sich durch'),
 s=T('Figma agent GA with team guidelines, Lovable drops its pick-a-look step, Magic Patterns launches MagicOS, Chrome iterates on HTML-in-Canvas. What it means for your workflow.','Figma 智能体正式可用并支持团队规范，Lovable 取消「先选风格」步骤，Magic Patterns 推出 MagicOS，Chrome 迭代 HTML-in-Canvas。对你的工作流意味着什么。','Figma 智慧體正式可用並支援團隊規範，Lovable 取消「先選風格」，Magic Patterns 推出 MagicOS，Chrome 迭代 HTML-in-Canvas。','Figmaエージェント正式版、Lovableのルック選択廃止、MagicOS登場、ChromeのHTML-in-Canvas。','Figma 에이전트 정식, Lovable 룩 선택 제거, MagicOS 출시, Chrome HTML-in-Canvas.','Ejen Figma GA, Lovable buang langkah pilih rupa, MagicOS dilancar, HTML-in-Canvas Chrome.','Agent Figma GA, Lovable bỏ bước chọn phong cách, MagicOS ra mắt, Chrome HTML-in-Canvas.',"Agent Figma en GA, Lovable supprime le choix de style, MagicOS, HTML-in-Canvas dans Chrome.",'Agente de Figma GA, Lovable quita el paso de estilo, MagicOS, HTML-in-Canvas en Chrome.','Figma-Agent GA, Lovable streicht Stilwahl, MagicOS, HTML-in-Canvas in Chrome.'),
 en="""<p>This week's design-tool news shares one theme: the art brief is moving out of the chat box and into files and canvases that persist. Dates are from each vendor's own announcement.</p>
<h2>The news</h2>
<ul><li><strong>6 Oct · Figma:</strong> the product-design agent is generally available after a beta that began in May. Library owners can attach markdown guideline files the agent reads; teammates can watch agent activity on the canvas.</li>
<li><strong>8 Oct · Lovable:</strong> the three pre-build design directions are gone; the look now comes from your prompt, with clarifying questions only when it is open. Same day: nine new app and chat connectors (including Zendesk, Neon and Metabase) and a Loom chat connector.</li>
<li><strong>13 Oct · Magic Patterns:</strong> MagicOS, an infinite canvas with a coordinator chat that runs parallel design threads, real-time voice, and an MCP server for coding agents.</li>
<li><strong>Chrome:</strong> the team posted an update on the HTML-in-Canvas API, which lets canvas and WebGL draw real DOM and CSS; an origin trial is running.</li></ul>
<h2>What to do with it</h2>
<ol><li>Write (or tidy) your design guideline file now; three tools in one week started reading one.</li>
<li>Put the style paragraph first in every app-builder prompt.</li>
<li>If you explore many directions, try a canvas tool; if you polish one screen, stay in a single design.</li></ol>
<p>Next week's roundup will be generated from the hub's daily feed and posted here.</p>""",
 zh="""<p>本周设计工具新闻有一个共同主题：美术需求正从聊天框搬进能长期保存的文件和画布。日期均以各厂商自己的公告为准。</p>
<h2>本周新闻</h2>
<ul><li><strong>10/6 · Figma：</strong>产品设计智能体结束 5 月开始的测试，正式可用。组件库所有者可以附加 Markdown 规范文件供智能体读取；队友可以在画布上看到智能体的操作。</li>
<li><strong>10/8 · Lovable：</strong>取消了首次构建前的三个设计方向选项，外观直接来自你的提示，只有没说清时才追问。同一天还上线了九个应用和聊天连接器（包括 Zendesk、Neon、Metabase）以及 Loom 聊天连接器。</li>
<li><strong>10/13 · Magic Patterns：</strong>推出 MagicOS：无限画布，由协调者对话并行运行多个设计线程，支持实时语音，并提供给编程智能体用的 MCP 服务。</li>
<li><strong>Chrome：</strong>团队发布了 HTML-in-Canvas API 的进展，让 canvas 和 WebGL 能绘制真实的 DOM 和 CSS，目前处于源试用（origin trial）阶段。</li></ul>
<h2>你可以做什么</h2>
<ol><li>现在就写（或整理）你的设计规范文件；一周内三个工具开始读这种文件。</li>
<li>在每个应用生成器的提示里，把风格段落放在最前面。</li>
<li>需要探索很多方向，试试画布类工具；只打磨一个页面，继续用单个设计。</li></ol>
<p>下周的周报会根据本站每日更新的内容生成并发布在这里。</p>""",
 refs=[("Figma's AI agent for product design is now generally available",'The Verge','https://www.theverge.com/tech/1004953/figmas-ai-agent-for-product-design-is-now-generally-available'),('Lovable changelog','Lovable','https://docs.lovable.dev/changelog'),('Introducing MagicOS','Magic Patterns','https://www.magicpatterns.com/blog/introducing-magicos'),('Lovable cut its pick-a-look step (incl. HTML-in-Canvas)','Art Direction Daily','https://artdirectiondaily.com/issues/2026-10-12-lovable-cut-pick-look-step.html'),('HTML-in-Canvas explainer','WICG','https://github.com/WICG/html-in-canvas')]),

dict(slug='tutorial-agent-builds-landing-with-ui-hub', date=D, cat='tutorial', series='agent-context', tags=['tutorial','agents','UI Hub'],
 t=T('Tutorial: have an agent build a landing page using UI Hub as context','教程：让智能体以 UI Hub 为上下文搭一个落地页','教學：讓智慧體以 UI Hub 為上下文搭一個落地頁','チュートリアル：UI Hubを文脈にエージェントでLPを作る','튜토리얼: UI Hub를 컨텍스트로 에이전트가 랜딩 페이지 만들기','Tutorial: ejen bina halaman pendaratan dengan UI Hub','Hướng dẫn: để agent dựng landing page với UI Hub làm ngữ cảnh',"Tutoriel : un agent construit une landing avec UI Hub comme contexte",'Tutorial: un agente crea una landing con UI Hub como contexto','Tutorial: ein Agent baut eine Landingpage mit UI Hub als Kontext'),
 s=T('Six steps from an empty folder to a verified page: load AGENTS.md, search the encyclopedia, pick components, load skills, build, verify in a browser.','从空文件夹到验证通过的页面六步走：加载 AGENTS.md、搜索百科、挑组件、加载技能、构建、浏览器验证。','從空資料夾到驗證通過的頁面六步：載入 AGENTS.md、搜尋百科、挑元件、載入技能、建置、瀏覽器驗證。','空フォルダから検証済みページまで6ステップ。','빈 폴더에서 검증된 페이지까지 6단계.','Enam langkah dari folder kosong ke halaman disahkan.','Sáu bước từ thư mục trống đến trang đã kiểm chứng.',"Six étapes du dossier vide à la page vérifiée.",'Seis pasos de una carpeta vacía a una página verificada.','Sechs Schritte vom leeren Ordner zur geprüften Seite.'),
 en="""<p>UI Hub is built to be read by agents: a JSON API, a design encyclopedia with raw Markdown per entry, and an AGENTS.md. This walkthrough shows the loop we use ourselves. Paste the prompts into Claude Code, Cursor, Codex or any agent that can fetch URLs.</p>
<h2>Six steps</h2>
<ol><li><strong>Load the guide.</strong> "Read https://siinxu.github.io/ui-resource-hub/AGENTS.md and follow it."</li>
<li><strong>Search the encyclopedia</strong> for the house style and the specs you need: <code>/kb/?q=house style</code>, <code>/kb/?q=typography</code>.</li>
<li><strong>Pick components</strong> from <code>/api/resources.json</code>, filtered by type and licence; prefer open-source libraries you can copy.</li>
<li><strong>Load skills</strong> in order: a taste or frontend-design skill first, then accessibility and quality checks.</li>
<li><strong>Build</strong> with tokens in CSS variables, one signature effect, real copy.</li>
<li><strong>Verify in a browser</strong> at 390px and 1440px, light and dark, and fix what you see before reporting done.</li></ol>
<h2>A prompt you can copy</h2>
<pre><code>Use UI Hub as design context: read /AGENTS.md, search /kb/ for
"house style", "typography", "colour". Build a landing page for
[product] with shadcn + one Aceternity background. Tokens in CSS
variables, 10-language-ready copy, then screenshot 390/1440 light/dark.</code></pre>
<h2>Why this works</h2>
<p>Each step replaces a vague instruction with a document the agent can read. The <a href="../../agents/">Agents guide</a> has a one-click copy of this prompt in 10 languages, plus a downloadable skill bundle.</p>""",
 zh="""<p>UI Hub 本来就是为智能体阅读而建的：有 JSON API、每条都有原始 Markdown 的设计百科，还有 AGENTS.md。下面是我们自己在用的流程。把提示贴进 Claude Code、Cursor、Codex 或任何能抓取网址的智能体即可。</p>
<h2>六步</h2>
<ol><li><strong>加载指南。</strong>「阅读 https://siinxu.github.io/ui-resource-hub/AGENTS.md 并照做。」</li>
<li><strong>搜索百科，</strong>找到风格要求和需要的规范：<code>/kb/?q=house style</code>、<code>/kb/?q=typography</code>。</li>
<li><strong>挑组件：</strong>从 <code>/api/resources.json</code> 按类型和许可证筛选；优先可复制的开源库。</li>
<li><strong>按顺序加载技能：</strong>先审美或 frontend-design 技能，再加无障碍和质量检查。</li>
<li><strong>构建：</strong>Token 放在 CSS 变量里，一个标志性特效，真实文案。</li>
<li><strong>浏览器验证：</strong>390px 和 1440px、亮色和暗色都看一遍，发现问题先修好再报告完成。</li></ol>
<h2>可直接复制的提示</h2>
<pre><code>Use UI Hub as design context: read /AGENTS.md, search /kb/ for
"house style", "typography", "colour". Build a landing page for
[product] with shadcn + one Aceternity background. Tokens in CSS
variables, 10-language-ready copy, then screenshot 390/1440 light/dark.</code></pre>
<h2>为什么有效</h2>
<p>每一步都把一句模糊的指令换成智能体能读的文档。<a href="../../agents/">Agent 指南</a>里有这段提示的 10 种语言一键复制版，以及可下载的技能包。</p>""",
 refs=[('UI Hub AGENTS.md','UI Hub','https://siinxu.github.io/ui-resource-hub/AGENTS.md'),('UI Hub design encyclopedia','UI Hub','https://siinxu.github.io/ui-resource-hub/kb/'),('AGENTS.md convention','agents.md','https://agents.md/'),('anthropics/skills','GitHub','https://github.com/anthropics/skills')]),
dict(slug='claude-design-everywhere', date=D, cat='tools', series=None, featured=True, tags=['Claude','Design','Artifacts','Dashboards'],
 t=T('Claude Design everywhere: out of beta, into every chat','Claude Design 全面开放：退出测试，进入每一场对话','Claude Design 全面開放：退出測試，進入每一場對話','Claude Designが正式版に：すべての会話で使える','Claude Design 정식 출시: 모든 대화에서 사용','Claude Design di mana-mana: keluar beta, masuk setiap sembang','Claude Design mọi nơi: hết beta, vào mọi cuộc trò chuyện',"Claude Design partout : fin du bêta, dans chaque chat",'Claude Design en todas partes: fuera de beta, en cada chat','Claude Design überall: aus der Beta, in jedem Chat'),
 s=T('Anthropic took Docs, Slides and Design out of beta on every plan, launched Dashboards and Motion in beta, and will close the standalone Design site on 14 Dec 2026. For UI builders the practical move is to migrate the design system now.','Anthropic 让 Docs、Slides、Design 在所有套餐正式可用，推出 Dashboards 与 Motion 测试版，并宣布独立 Design 站点将于 2026-12-14 关闭。界面构建者现在就该迁移设计系统。','Anthropic 讓 Docs、Slides、Design 在所有方案正式可用，推出 Dashboards 與 Motion 測試版，並宣布獨立 Design 站點將於 2026-12-14 關閉。介面建構者現在就該遷移設計系統。','AnthropicはDocs/Slides/Designを全プランで正式化し、DashboardsとMotionのベータを開始。スタンドアロンDesignは2026-12-14閉鎖。UI制作者は今すぐデザインシステムを移行すべき。','Anthropic이 Docs·Slides·Design을 전 요금제에서 정식 출시하고 Dashboards·Motion 베타를 열었으며, 단독 Design 사이트는 2026-12-14에 닫힌다. UI 제작자는 지금 디자인 시스템을 옮겨야 한다.','Anthropic keluarkan Docs, Slides dan Design dari beta pada semua pelan, lancar Dashboards dan Motion beta, dan tutup tapak Design berasingan pada 14 Dis 2026. Pembina UI patut pindahkan sistem reka bentuk sekarang.','Anthropic đưa Docs, Slides và Design ra khỏi beta trên mọi gói, mở beta Dashboards và Motion, và đóng site Design độc lập vào 14/12/2026. Người dựng UI nên migrate design system ngay.',"Anthropic sort Docs, Slides et Design du bêta sur tous les forfaits, lance Dashboards et Motion en bêta, et fermera le site Design autonome le 14 déc. 2026. Les builders UI doivent migrer le design system maintenant.",'Anthropic saca Docs, Slides y Design de beta en todos los planes, lanza Dashboards y Motion en beta, y cerrará el sitio Design independiente el 14 dic 2026. Quien construye UI debe migrar el design system ya.','Anthropic nimmt Docs, Slides und Design auf allen Plänen aus der Beta, startet Dashboards und Motion in Beta und schließt die eigenständige Design-Site am 14. Dez. 2026. UI-Builder sollten das Design System jetzt migrieren.'),
 en="""<p>On 8 October 2026 Anthropic published a product update that matters more for design-and-code workflows than the headline tools might suggest. Claude Dashboards and Claude Motion entered beta; Claude Docs, Slides and Design left beta and are available on every Claude plan, including Free. The same post says the standalone Claude Design site at claude.ai/design stays open only until 14 December 2026, after which design work lives inside ordinary Claude conversations, Claude Code and the Artifacts tab.</p>
<h2>What actually shipped</h2>
<ul><li><strong>Design in every chat.</strong> Anthropic’s product page and help centre describe Claude Design as an artifact template: describe a visual, get a canvas beside the conversation, then refine with chat, inline comments and on-canvas edits. It works in Claude Code via <code>/design</code> and <code>/design-sync</code>, and on mobile for viewing and editing (sharing settings stay on web/desktop).</li>
<li><strong>Design systems travel with you.</strong> Systems can be imported from GitHub, design files or a local codebase. Teams that used the standalone site can click “Migrate team design systems” on the Artifacts page; Anthropic notes migrated systems may need a “Let Claude clean it up” pass.</li>
<li><strong>Dashboards (beta, paid).</strong> Connect Redshift, BigQuery, ClickHouse, Databricks, Snowflake or Salesforce-style connectors, ask in plain language, and get a live dashboard. Each number exposes the query behind it and a refresh time; deeper analysis can be sent to tools such as Amplitude, Grafana, Hex, Mixpanel, Omni, Perplexity, PostHog or Sigma.</li>
<li><strong>Motion (beta, Team/Enterprise).</strong> Claude writes code that animates your own text, charts, shapes and images into a short explainer you can edit and export as MP4. Anthropic states it does not use a video-generation model and does not invent footage or people.</li>
<li><strong>Enterprise defaults.</strong> Docs, Slides and Design turn on by default on 15 October 2026 (except HIPAA-enabled orgs). Dashboards and Motion stay off until an admin enables them under Organization settings → Artifacts.</li></ul>
<h2>Why it matters for UI builders</h2>
<p>The useful shift is not “another AI design toy”. It is that the brief, the design system and the coding agent share one conversation surface. A prototype can start next to a requirements thread, inherit components via <code>/design-sync</code>, and hand off to Claude Code without screenshot archaeology. Connectors listed on the product page (Adobe, Canva, Gamma, Lovable, Miro, Replit, Vercel, Wix and others) push the same artifact into the tools you already ship from.</p>
<p>Anthropic’s own announcement claims more than 45 million docs, decks and designs since those templates arrived in every conversation. Treat that as a usage signal, not a quality guarantee: the ceiling is still your tokens, your refuse-list and whether an admin locked a single approved system.</p>
<h2>Our take</h2>
<p>Migrate the design system before December, not the day the standalone URL dies. Enterprise teams should treat 15 October as the day Design becomes ambient for everyone who can open Claude—so lock publishing rights and a default system first, or you will get fast, on-brand-looking noise. Prefer Motion when the story is your own data and copy; reach for a dedicated video model when you need filmed scenes. Prefer Dashboards for exploratory questions where seeing the SQL builds trust; keep your BI stack for governed reporting.</p>
<h2>Practical checklist</h2>
<ol><li>Open Artifacts → migrate team design systems; run the clean-up pass on each.</li>
<li>In Claude Code, run <code>/design-sync</code> against the repo that owns tokens and components.</li>
<li>Write a short house guideline (tokens, type scale, never-list) the same way you would for Figma’s agent or a SKILL.md—Claude Design still needs a file it can obey.</li>
<li>Enterprise admins: decide before 15 October whether Docs/Slides/Design should stay default-on; enable Dashboards/Motion only after data connectors are reviewed.</li>
<li>Export path: HTML / PDF / PPTX for stakeholders; hand off to Claude Code or a connector (v0, Vercel, Lovable, Replit…) when the next step is production UI.</li>
<li>Verify like any generated UI: real content, focus rings, light/dark, 390px and 1440px—not only the canvas preview.</li></ol>""",
 zh="""<p>2026 年 10 月 8 日，Anthropic 发了一则对「设计 + 代码」工作流比标题工具更要紧的产品更新：Claude Dashboards 与 Claude Motion 进入测试；Claude Docs、Slides、Design 退出测试，并在包括免费版在内的所有 Claude 套餐可用。同一篇文章写明，独立站点 claude.ai/design 只开放到 2026 年 12 月 14 日，之后设计工作落在普通对话、Claude Code 和 Artifacts 页签里。</p>
<h2>到底上线了什么</h2>
<ul><li><strong>每场对话里的 Design。</strong>产品页与帮助中心把 Claude Design 描述成一种 Artifact 模板：描述视觉效果，对话旁出现画布，再用聊天、行内评论和画布编辑迭代。Claude Code 里可用 <code>/design</code> 与 <code>/design-sync</code>；移动端可查看和编辑（分享设置仍在网页/桌面）。</li>
<li><strong>设计系统跟着走。</strong>可从 GitHub、设计文件或本地代码库导入。用过独立站点的团队可在 Artifacts 页点击「Migrate team design systems」；Anthropic 提示迁移后的系统可能需要「Let Claude clean it up」。</li>
<li><strong>Dashboards（测试版，付费）。</strong>连接 Redshift、BigQuery、ClickHouse、Databricks、Snowflake 或 Salesforce 类连接器，用自然语言提问，得到会随数据更新的仪表盘。每个数字可查看背后的查询与刷新时间；更深分析可送到 Amplitude、Grafana、Hex、Mixpanel、Omni、Perplexity、PostHog、Sigma 等。</li>
<li><strong>Motion（测试版，Team/Enterprise）。</strong>Claude 写代码来动画化你自己的文字、图表、形状与图片，导出 MP4。Anthropic 明确说它不用视频生成模型，也不捏造镜头或人物。</li>
<li><strong>企业默认。</strong>Docs、Slides、Design 于 2026 年 10 月 15 日默认开启（HIPAA 组织除外）。Dashboards 与 Motion 需管理员在 Organization settings → Artifacts 打开。</li></ul>
<h2>对界面构建者为什么重要</h2>
<p>真正有用的变化不是「又一个 AI 画图玩具」，而是简报、设计系统和编码智能体共享同一对话面。原型可以紧挨需求线程开始，经 <code>/design-sync</code> 继承组件，再交给 Claude Code，少做截图考古。产品页列出的连接器（Adobe、Canva、Gamma、Lovable、Miro、Replit、Vercel、Wix 等）把同一份产物推进你本来就在用的发布工具。</p>
<p>官方公告称，这些模板进入每场对话以来，已有超过 4500 万份文档、幻灯片与设计。把它当作用量信号，而不是质量保证：上限仍取决于你的 Token、禁止清单，以及管理员是否锁定了唯一批准的系统。</p>
<h2>我们的看法</h2>
<p>在 12 月独立 URL 失效前迁移设计系统，不要拖到最后一天。企业团队应把 10 月 15 日当成 Design 对所有能打开 Claude 的人「默认存在」的日子——先锁定发布权限与默认系统，否则只会得到又快又像品牌的噪声。故事是你自己的数据与文案时用 Motion；需要实拍场景时再用专用视频模型。探索性问题、且希望看见 SQL 以建立信任时用 Dashboards；受治理的报表仍留给 BI 栈。</p>
<h2>实操清单</h2>
<ol><li>打开 Artifacts → 迁移团队设计系统；对每个系统跑清理。</li>
<li>在 Claude Code 对拥有 Token 与组件的仓库执行 <code>/design-sync</code>。</li>
<li>写一份短的家规（Token、字号阶梯、禁止清单），写法同给 Figma 智能体或 SKILL.md——Claude Design 同样需要可读的约束文件。</li>
<li>企业管理员：在 10 月 15 日前决定 Docs/Slides/Design 是否保持默认开启；审过数据连接器后再开 Dashboards/Motion。</li>
<li>导出路径：给干系人用 HTML / PDF / PPTX；下一步是生产界面时交给 Claude Code 或连接器（v0、Vercel、Lovable、Replit…）。</li>
<li>像验证任何生成界面一样验收：真实内容、焦点环、亮/暗色、390px 与 1440px——不要只看画布预览。</li></ol>""",
 refs=[('Build live dashboards and animate explainers with Claude','Anthropic','https://claude.com/resources/articles/dashboards-and-motion'),('Claude Design product page','Anthropic','https://claude.com/product/design'),('Get started with Claude Design','Claude Help Center','https://support.claude.com/en/articles/14604416-get-started-with-claude-design'),('Claude Design admin guide for Team and Enterprise','Claude Help Center','https://support.claude.com/en/articles/14604406-claude-design-admin-guide-for-team-and-enterprise-plans'),('Claude Dashboards and Claude Motion: Anthropic’s new beta tools','Mad Robot','https://madrobot.blog/2026/10/08/claude-dashboards-motion-beta-docs-slides-design-free-plan/')]),
dict(slug='figma-code-layers-and-specs', date='2026-10-15', cat='tools', series=None, featured=True, tags=['Figma','Code Layers','Specs','MCP','design systems'],
 t=T('Figma code layers and Specs: the canvas becomes the shared context again','Figma 代码图层与 Specs：画布重新成为共享上下文','Figma 程式碼圖層與 Specs：畫布重新成為共享脈絡','Figmaのコードレイヤーと Specs：キャンバスが再び共有コンテキストに','Figma 코드 레이어와 Specs: 캔버스가 다시 공유 컨텍스트가 되다','Lapisan kod dan Specs Figma: kanvas kembali menjadi konteks bersama','Code layers và Specs của Figma: canvas lại là ngữ cảnh chung',"Code layers et Specs dans Figma : le canevas redevient le contexte partagé",'Code layers y Specs en Figma: el lienzo vuelve a ser el contexto compartido','Figma Code Layers und Specs: Die Canvas wird wieder zum gemeinsamen Kontext'),
 s=T('At Config India (15 Oct 2026) Figma moved code layers into open beta, launched Specs as a Markdown home on the canvas, and let libraries carry guidelines and code sources. The lesson for UI builders: agents are short of constraint files, not generators.',
     '在 Config India（2026-10-15）上，Figma 让代码图层进入公开测试，推出把 Markdown 放上画布的 Specs，并让组件库携带规范与代码源。给界面构建者的结论：智能体缺的不是生成器，而是约束文件。',
     '在 Config India（2026-10-15）上，Figma 讓程式碼圖層進入公開測試，推出把 Markdown 放上畫布的 Specs，並讓元件庫攜帶規範與程式碼來源。給介面建構者的結論：智慧體缺的不是產生器，而是約束檔案。',
     'Config India（2026-10-15）でFigmaはコードレイヤーをオープンベータにし、Markdownをキャンバスに置くSpecsを公開、ライブラリにガイドラインとコードソースを持たせた。UI制作者への教訓：エージェントに足りないのは生成器ではなく制約ファイルだ。',
     'Config India(2026-10-15)에서 Figma는 코드 레이어를 오픈 베타로 전환하고, Markdown을 캔버스에 두는 Specs를 출시했으며, 라이브러리에 가이드라인과 코드 소스를 붙였다. UI 제작자에게 주는 교훈: 에이전트에게 부족한 것은 생성기가 아니라 제약 파일이다.',
     'Di Config India (15 Okt 2026) Figma membawa lapisan kod ke beta terbuka, melancarkan Specs sebagai rumah Markdown di kanvas, dan membenarkan pustaka membawa garis panduan serta sumber kod. Pengajaran: ejen kekurangan fail kekangan, bukan penjana.',
     'Tại Config India (15/10/2026), Figma đưa code layers vào beta mở, ra mắt Specs làm nơi đặt Markdown trên canvas, và cho thư viện mang theo guidelines cùng code sources. Bài học: agent thiếu file ràng buộc, không thiếu trình sinh.',
     "À Config India (15 oct. 2026), Figma passe les code layers en bêta ouverte, lance Specs pour le Markdown sur le canevas et laisse les bibliothèques porter guidelines et sources de code. Leçon : les agents manquent de fichiers de contraintes, pas de générateurs.",
     'En Config India (15 oct 2026) Figma llevó los code layers a beta abierta, lanzó Specs como hogar del Markdown en el lienzo y dejó que las bibliotecas lleven guidelines y fuentes de código. Lección: a los agentes les faltan archivos de restricciones, no generadores.',
     'Auf der Config India (15. Okt. 2026) brachte Figma Code Layers in die offene Beta, startete Specs als Markdown-Ort auf der Canvas und ließ Bibliotheken Guidelines und Code-Quellen tragen. Die Lehre: Agenten fehlen Constraint-Dateien, nicht Generatoren.'),
 en="""<p>On 15 October 2026, at Config India in Bengaluru, Figma shipped a set of updates that are easy to read as “more AI features” and more useful to read as a single idea: put the code, the written intent and the design-system rules on the same canvas, so people and agents work from one context instead of five tabs. Dylan Field’s recap post frames the problem bluntly. AI made code cheap, so teams “build to think”, but that vibe-coding loop is usually single-player; one customer is quoted describing it as “fast, fast, fast… then slow”.</p>
<h2>What launched</h2>
<ul><li><strong>Code layers, open beta on all plans.</strong> A code layer is a running, interactive prototype that sits on the canvas. You can start one from scratch (Code tool or <kbd>B</kbd>), convert selected frames with <em>Build selection</em>, clone a connected GitHub repo, upload a local folder, push a prototype in from your coding tool through the Figma MCP server, or capture a live page with the Chrome extension. Teammates can duplicate a layer to try another direction, comment and annotate it, edit the code, ask the agent to merge the best parts of two versions, pull screens back out with <em>Extract designs</em>, and push to a branch and open a pull request.</li>
<li><strong>Specs, open beta on paid plans.</strong> A multiplayer Markdown container that lives as its own file or next to designs in Figma Design and FigJam (press <kbd>D</kbd>, or drop any <code>.md</code> file on the canvas). A spec can embed frames, FigJam boards and other canvas nodes, the Figma agent can read and reply to comments, and connectors such as GitHub and Hex can pull outside context in. Paste a spec link into a coding agent’s prompt and, according to Figma, the Markdown, frame references, diagrams, code layers and Code Connect snippets travel with it.</li>
<li><strong>Design systems that carry rules and code.</strong> Guidelines attached to published libraries (open beta, Professional and above) are handed to the agent automatically whenever someone builds with that library. Code sources (closed beta) attach a GitHub repo or npm package to a library so code layers pull from real components. A centralised design-system space with a system map and a “system check” for gaps such as missing descriptions or interactive states is preview only.</li>
<li><strong>Figma MCP.</strong> Figma says the server is now faster and uses fewer tokens; it can create code layers, read and write Specs, generate images and run Weave workflows, and adds tools such as <code>html_to_figma</code> and <code>generate_image</code>, plus 20 new partner integrations (OpenCode, Dia, Junie, Meta Muse and others).</li>
<li><strong>Payload in Figma Make.</strong> Make now scaffolds a Payload backend (CMS, database, auth, APIs, admin panel) as its native backend; Supabase stays available as a third-party connection.</li></ul>
<h2>Why it matters: three shifts</h2>
<p><strong>Prototypes go back to multiplayer.</strong> The real cost of coding-agent prototypes has not been generation; it has been review. A link to a running demo shows the result but hides the alternatives and the reasoning. Putting several running versions side by side on a canvas, with comments pinned to them, restores the critique loop design teams already know. The branch-and-PR exit matters too: the prototype has a route into the repo rather than being rebuilt.</p>
<p><strong>Markdown finally gets an address.</strong> Most teams working with agents already keep PRDs, <code>AGENTS.md</code> files and prompt notes in Markdown, scattered across laptops and repos with no link to the screens they describe. Specs is Figma’s bet that the brief should sit beside the frames, be editable by both humans and agents, and be passable to a coding agent by URL. Whether or not you adopt Specs, the pattern is right: one canonical brief, versioned with the work.</p>
<p><strong>Design systems become agent-readable.</strong> Guidelines and code sources are the most consequential part of the launch and the least flashy. A library that ships its own do/don’t rules and points at the real npm package turns “please match our design system” from a hope into an input the agent receives every time.</p>
<h2>Our take</h2>
<p>The scarce input in AI-assisted UI is still the constraint file. Every tool this month, from Claude Design’s design systems to the Figma agent’s guideline files, has converged on the same lesson: generation is abundant, and quality comes from short, explicit rules about tokens, states and what never to do. Figma is now giving those rules a native place to live and an automatic route to the agent. Teams that already wrote a tight guideline file will see the benefit immediately; teams that skipped it will get faster, on-brand-looking noise.</p>
<p>Two caveats. First, these are betas with staggered rollouts, so features may appear for one teammate before another. Second, cost: code layers use AI credits, free for creating and editing on paid plans only until 4 November 2026, and guidelines can make a prompt more expensive because they add context. Figma’s customer numbers (for example, Merkle reporting 30% faster iteration) are vendor-published snapshots, not independent benchmarks.</p>
<h2>How to try it this week</h2>
<ol><li><strong>Pick one flow, not a product.</strong> Convert a single real flow (sign-up, checkout, settings) into a code layer from existing frames or a lightweight prototype repo. Duplicate it once to compare two directions.</li>
<li><strong>Write a short Spec next to it.</strong> Tokens to use, states that must exist, content rules and a never-list. Keep it to one screen of text so it is actually read.</li>
<li><strong>Add guidelines to the library.</strong> Move your do/don’t pairs onto the published library so every agent prompt against it inherits them. If you are in the code-sources beta, attach the npm package your product really ships.</li>
<li><strong>Wire MCP from your coding agent.</strong> Connect Claude Code, Cursor, Codex or similar to the Figma MCP server, paste the spec link into the prompt, and let the agent create or update the code layer.</li>
<li><strong>Review on canvas like a pull request.</strong> Check empty, loading and error states, long text, keyboard focus and contrast, at 390px and 1440px, before anyone says “ship it”. Then push to a branch.</li></ol>
<pre><code># Spec: Checkout v2
## Tokens
surface / text-muted / accent only; radius 10; Geist 14/20
## States (must exist)
empty cart · loading · card declined · success · long names
## Content
real prices, real error copy; sentence case
## Never
text gradients · emoji icons · placeholder-only labels · raw hex
## Done when
390 + 1440 · light + dark · focus visible · AA contrast</code></pre>
<h2>Where UI Hub fits</h2>
<p>If you are writing that guideline file or Spec from scratch, start from the design skills and agent guides already collected on UI Hub: filter the resource list by <em>skills</em> for SKILL.md-style rule files, and see the <a href="../../agents/">Agents guide</a> for the search, pick and verify loop that pairs well with an MCP-connected coding agent. The point is the same whichever canvas you use: give the agent the rules before you ask it for pixels.</p>""",
 zh="""<p>2026 年 10 月 15 日，Figma 在班加罗尔的 Config India 上发布了一组更新。表面看是「又多了几个 AI 功能」，但更有用的读法是一个统一的思路：把代码、文字意图和设计系统规则放到同一张画布上，让人和智能体共用一份上下文，而不是在五个标签页之间来回切。Dylan Field 的汇总文章说得很直白：AI 让写代码变便宜，团队开始「边做边想」，但这种 vibe coding 往往是单人游戏——一位客户的原话是「快、快、快……然后变慢」。</p>
<h2>发布了什么</h2>
<ul><li><strong>代码图层（Code layers），所有套餐公开测试。</strong>代码图层是一段放在画布上、可交互、真正在运行的原型。可以从零开始（Code 工具或按 <kbd>B</kbd>），选中画框后点 <em>Build selection</em> 转换，克隆已连接的 GitHub 仓库，上传本地文件夹，通过 Figma MCP 服务器从编码工具推进来，或用 Chrome 扩展抓取线上页面。队友可以复制一层去试别的方向、评论和标注、直接改代码、让智能体合并两个版本的优点，用 <em>Extract designs</em> 把画面拆回可编辑图层，最后推到分支并开 Pull Request。</li>
<li><strong>Specs，付费套餐公开测试。</strong>一个多人协作的 Markdown 容器，可以是独立文件，也可以放在 Figma Design 与 FigJam 的设计旁边（按 <kbd>D</kbd>，或把任意 <code>.md</code> 文件拖到画布上）。Spec 可嵌入画框、FigJam 白板和其他画布节点；Figma 智能体能读取并回复评论；GitHub、Hex 等连接器可以把外部上下文拉进来。按 Figma 的说法，把 Spec 链接粘进编码智能体的提示里，Markdown、画框引用、图表、代码图层和 Code Connect 片段都会一起带过去。</li>
<li><strong>携带规则与代码的设计系统。</strong>挂在已发布组件库上的 Guidelines（公开测试，Professional 及以上）会在有人用该库构建时自动交给智能体。Code sources（封闭测试）把 GitHub 仓库或 npm 包挂到组件库上，让代码图层使用真实组件。集中式设计系统空间（含系统图谱，以及检查缺少描述、交互状态等缺口的 system check）目前仅为预览。</li>
<li><strong>Figma MCP。</strong>Figma 称服务器更快、更省 Token；可以创建代码图层、读写 Specs、生成图片、运行 Weave 工作流，新增 <code>html_to_figma</code>、<code>generate_image</code> 等工具，并新增 20 个合作集成（OpenCode、Dia、Junie、Meta Muse 等）。</li>
<li><strong>Figma Make 接入 Payload。</strong>Make 现在会把 Payload（CMS、数据库、认证、API、管理后台）作为原生后端脚手架；Supabase 继续作为第三方连接可用。</li></ul>
<h2>为什么重要：三个转变</h2>
<p><strong>原型回到多人协作。</strong>编码智能体做原型，真正的成本从来不是生成，而是评审。一个运行中的演示链接只给出结果，却藏起了备选方案和推理过程。把几个运行版本并排放在画布上、评论钉在旁边，就恢复了设计团队熟悉的评审循环。分支 + PR 的出口同样关键：原型有了进入代码仓库的路径，而不是推倒重写。</p>
<p><strong>Markdown 终于有了地址。</strong>和智能体协作的团队，PRD、<code>AGENTS.md</code>、提示词笔记大多已经是 Markdown，却散落在各自电脑和仓库里，和它们描述的界面毫无关联。Specs 押注的是：需求应该挨着画框、人和智能体都能编辑、并能用一个 URL 交给编码智能体。不管你用不用 Specs，这个模式是对的——一份权威需求，与作品一起版本化。</p>
<p><strong>设计系统变得「智能体可读」。</strong>Guidelines 和 Code sources 是这次发布里最不起眼、却影响最大的部分。一个自带该做/不该做规则、并指向真实 npm 包的组件库，会把「请符合我们的设计系统」从一句愿望变成智能体每次都会收到的输入。</p>
<h2>我们的看法</h2>
<p>AI 辅助界面里最稀缺的输入，仍然是约束文件。这个月的每个工具——从 Claude Design 的设计系统到 Figma 智能体的规范文件——都收敛到同一个结论：生成能力过剩，质量来自关于 Token、状态和「绝不做什么」的简短明确规则。Figma 现在给这些规则提供了原生的存放位置和自动送达智能体的通道。已经写好精炼规范文件的团队会立刻受益；跳过这一步的团队，只会得到更快、看起来很像品牌的噪声。</p>
<p>两点提醒。第一，这些都是分批灰度的测试版，队友之间可能先后看到功能。第二，成本：代码图层消耗 AI 积分，付费套餐里创建和编辑仅在 2026 年 11 月 4 日前免费；Guidelines 会增加上下文，也可能让单次提示更贵。Figma 公布的客户数据（如 Merkle 称迭代快 30%）是厂商发布的案例快照，不是独立基准测试。</p>
<h2>本周就能试的做法</h2>
<ol><li><strong>选一条流程，而不是整个产品。</strong>把一条真实流程（注册、结账、设置）从现有画框或轻量原型仓库转成代码图层，再复制一份比较两个方向。</li>
<li><strong>在旁边写一份短 Spec。</strong>写清要用的 Token、必须存在的状态、内容规则和禁止清单。控制在一屏以内，才会真的被读。</li>
<li><strong>给组件库加 Guidelines。</strong>把该做/不该做的规则放到已发布组件库上，让所有基于它的智能体提示自动继承。如果你在 Code sources 测试里，挂上产品真正发布的 npm 包。</li>
<li><strong>从编码智能体接入 MCP。</strong>把 Claude Code、Cursor、Codex 等连到 Figma MCP 服务器，把 Spec 链接粘进提示，让智能体创建或更新代码图层。</li>
<li><strong>像审 Pull Request 一样在画布上验收。</strong>在任何人说「可以上线」之前，检查空状态、加载、报错、长文本、键盘焦点和对比度，分别看 390px 与 1440px。然后推到分支。</li></ol>
<pre><code># Spec: 结账 v2
## Token
只用 surface / text-muted / accent；圆角 10；Geist 14/20
## 必须存在的状态
空购物车 · 加载中 · 卡被拒 · 成功 · 超长名称
## 内容
真实价格、真实报错文案；句首大写
## 禁止
文字渐变 · emoji 图标 · 只有占位符没有标签 · 裸 hex 色值
## 完成标准
390 + 1440 · 亮色 + 暗色 · 焦点可见 · AA 对比度</code></pre>
<h2>UI Hub 能帮什么</h2>
<p>如果你要从零写这份规范文件或 Spec，可以从 UI Hub 已收集的设计技能和智能体指南起步：在资源列表里按 <em>skills</em> 筛选 SKILL.md 风格的规则文件，再看 <a href="../../agents/">Agent 指南</a> 里「搜索、挑选、验证」的循环，它和接入 MCP 的编码智能体很搭。不管用哪张画布，道理都一样：先把规则交给智能体，再让它出像素。</p>""",
 refs=[('Build by design: New workflows for new ways of building','Figma (Dylan Field)','https://www.figma.com/blog/build-by-design/'),('Design together with code layers on the canvas','Figma','https://www.figma.com/blog/design-together-with-code-layers/'),('Introducing Specs: Markdown as a medium','Figma','https://www.figma.com/blog/introducing-figma-specs/'),("What's new from Config India 2026",'Figma Help Center','https://help.figma.com/hc/en-us/articles/43663368947863-What-s-new-from-Config-India-2026'),('Code layers in Figma Design','Figma Help Center','https://help.figma.com/hc/en-us/articles/44193259600535-Code-layers-in-Figma-Design'),('Guide to Specs in Figma','Figma Help Center','https://help.figma.com/hc/en-us/articles/44049066011671-Guide-to-Specs-in-Figma'),('Guide to the Figma MCP server','Figma Help Center','https://help.figma.com/hc/en-us/articles/32132100833559-Guide-to-the-Figma-MCP-server'),("Here's everything from Config India 2026",'Figma Forum','https://forum.figma.com/product-updates-3/here-s-everything-from-config-india-2026-59008'),('Figma deepens investment in India with largest international Config yet','Figma','https://www.figma.com/blog/figma-deepens-investment-in-india/')]),
dict(slug='shadcn-trace-and-ai-elements', date='2026-10-16', cat='components', series='library-deep-dive', featured=True, tags=['shadcn/ui','Trace','AI Elements','agent UI','AI SDK'],
 t=T('shadcn Trace and AI Elements: one shape for every step an agent takes','shadcn 的 Trace 与 AI Elements：让智能体的每一步都长一个样','shadcn 的 Trace 與 AI Elements：讓智慧體的每一步都長一個樣','shadcn の Trace と AI Elements：エージェントのすべてのステップを同じ形に','shadcn Trace와 AI Elements: 에이전트의 모든 단계를 같은 모양으로','Trace dan AI Elements shadcn: satu bentuk untuk setiap langkah ejen','Trace và AI Elements của shadcn: một hình dạng cho mọi bước của agent',"Trace et AI Elements de shadcn : une seule forme pour chaque étape d’un agent",'Trace y AI Elements de shadcn: una sola forma para cada paso de un agente','shadcn Trace und AI Elements: eine Form für jeden Schritt eines Agenten'),
 s=T('On 14 Oct 2026 shadcn/ui shipped Trace, Code Block and 21 copy-in AI Elements patterns that replace AI SDK Elements. The design lesson: reasoning, tool calls, sources and subagents are all one line with an icon, a title and a status, so agent UIs stop looking like debug logs.',
     '2026 年 10 月 14 日，shadcn/ui 发布 Trace、Code Block 和 21 个可直接复制的 AI Elements 模式，取代 AI SDK Elements。设计上的启发：推理、工具调用、来源和子智能体都是同一种「一行」——图标、标题加状态，智能体界面从此不再像调试日志。',
     '2026 年 10 月 14 日，shadcn/ui 發布 Trace、Code Block 和 21 個可直接複製的 AI Elements 模式，取代 AI SDK Elements。設計上的啟發：推理、工具呼叫、來源和子智慧體都是同一種「一行」——圖示、標題加狀態，智慧體介面從此不再像除錯日誌。',
     '2026年10月14日、shadcn/ui は Trace、Code Block、そしてコピーして使う21の AI Elements パターンを公開し、AI SDK Elements を置き換えた。デザイン上の教訓：推論、ツール呼び出し、ソース、サブエージェントはすべて「アイコン・タイトル・状態」を持つ1行であり、エージェントUIはもうデバッグログのように見える必要はない。',
     '2026년 10월 14일 shadcn/ui는 Trace, Code Block, 그리고 복사해서 쓰는 21개의 AI Elements 패턴을 공개해 AI SDK Elements를 대체했다. 디자인 교훈: 추론, 도구 호출, 출처, 서브에이전트는 모두 아이콘·제목·상태를 가진 한 줄이며, 에이전트 UI가 더 이상 디버그 로그처럼 보일 필요가 없다.',
     'Pada 14 Okt 2026 shadcn/ui melancarkan Trace, Code Block dan 21 corak AI Elements yang disalin terus ke projek, menggantikan AI SDK Elements. Pengajaran reka bentuk: penaakulan, panggilan alat, sumber dan subejen semuanya satu baris dengan ikon, tajuk dan status, jadi UI ejen tidak lagi kelihatan seperti log nyahpepijat.',
     'Ngày 14/10/2026, shadcn/ui ra mắt Trace, Code Block và 21 mẫu AI Elements sao chép thẳng vào dự án, thay thế AI SDK Elements. Bài học thiết kế: suy luận, gọi công cụ, nguồn và subagent đều là một dòng có biểu tượng, tiêu đề và trạng thái, nên giao diện agent không còn trông như log gỡ lỗi.',
     "Le 14 oct. 2026, shadcn/ui a publié Trace, Code Block et 21 patterns AI Elements à copier dans le projet, qui remplacent AI SDK Elements. Leçon de design : raisonnement, appels d’outils, sources et sous-agents sont tous une ligne avec icône, titre et statut, et les interfaces d’agents cessent de ressembler à des logs de débogage.",
     'El 14 oct 2026 shadcn/ui lanzó Trace, Code Block y 21 patrones de AI Elements que se copian al proyecto y sustituyen a AI SDK Elements. La lección de diseño: razonamiento, llamadas a herramientas, fuentes y subagentes son todos una línea con icono, título y estado, y las interfaces de agentes dejan de parecer logs de depuración.',
     'Am 14. Okt. 2026 veröffentlichte shadcn/ui Trace, Code Block und 21 kopierbare AI-Elements-Patterns, die AI SDK Elements ablösen. Die Designlehre: Reasoning, Tool-Calls, Quellen und Subagenten sind alle eine Zeile mit Icon, Titel und Status, und Agenten-UIs sehen nicht mehr wie Debug-Logs aus.'),
 en="""<p>On 14 October 2026 shadcn published <strong>Trace</strong>, a component for agent activity, together with <strong>Code Block</strong> and <strong>AI Elements</strong>, a set of patterns for agentic interfaces built entirely from shadcn/ui components. The announcement post passed 4,500 likes on X within two days, and shadcn-svelte followed with its own AI Elements a day later. The interesting part is not that there are new components. It is the design claim underneath them: reasoning, tool calls, sources, plans and subagent runs all have the same shape, so they should look and behave the same.</p>
<h2>What shipped</h2>
<ul><li><strong>Trace.</strong> A list of lines for the steps an agent takes. The shadcn team says it was distilled from studying hundreds of components in agentic interfaces. Each line has an icon, a title, an optional description and a status (<code>running</code>, <code>error</code> or <code>pending</code>, with a shimmer while a step runs). A line can expand, link to a page, or open a dialog, sheet, drawer or popover, and lines can nest, so a summary opens into steps and a step into its output. It reads the reasoning, tool and source parts that the AI SDK streams.</li>
<li><strong>Code Block.</strong> Displays code, terminal output, logs and diffs, with a header for a title and actions, line numbers, wrapping, highlighted and diff lines, and a small size (<code>size="sm"</code>) meant for tool output inside a Trace.</li>
<li><strong>AI Elements, 21 patterns.</strong> Chat, Prompt Input, Reasoning, Tool, Plan, Subagent, Confirmation, Context, Sources, File Tree, Terminal, Test Results and more. There is no package: each pattern is a composition you copy into your repo, and every docs page also exists as Markdown so a coding agent can read it directly.</li>
<li><strong>Every base and style.</strong> Trace and Code Block are available for Base UI, React Aria and Radix across all eight shadcn/ui styles, and they join the chat components released in June: Message Scroller, Message, Bubble, Marker, Attachment and Questionnaire.</li>
<li><strong>AI SDK Elements is being deprecated.</strong> Code you already copied from elements.ai-sdk.dev keeps working. Each pattern page has a migration prompt that rebuilds the wrapper in <code>components/ai-elements</code> on the new components while keeping every export and its props. A few low-usage elements (artifact, audio player, the React Flow canvas pieces, JSX preview, voice and mic selectors) were not rebuilt; the docs list which existing components to compose them from.</li></ul>
<h2>Why it matters: agent UIs get a grammar</h2>
<p>Until now most agent interfaces have been assembled one part type at a time: a reasoning accordion here, a tool-call card there, a sources popover somewhere else, each with its own spacing, icon logic and loading state. The result is the familiar “debug log” look, where every turn is a pile of unrelated widgets. Trace replaces that with one row grammar. What changes between a thought, a shell command and a subagent is only the icon, the title and what happens when you open the line.</p>
<p>That grammar also forces good copy. The accessibility notes are unusually specific: the icon is hidden from assistive tech, so the title is the accessible name and should be a sentence that says what happened (“Edited trace.tsx”, not “trace.tsx”). Because status is shown with colour and motion, it also belongs in the words: “Running pnpm build” while it runs, “Failed to run pnpm build” when it errors. The shimmer stops for readers who prefer reduced motion, and inside a Message Scroller each new line is announced once.</p>
<p>The Confirmation pattern adds one more useful rule. A pending approval is a prompt, not activity, so it sits outside the Trace as an item with Deny and Approve buttons, and only becomes a Tool line once the person answers. Asking and doing are visually different things.</p>
<h2>Our take</h2>
<p>This is the same move the whole field made this month, from Figma Specs to Claude Design: the useful unit is not a generator but a shared, explicit shape that people and agents can both follow. For agent UIs, Trace is that shape. Teams building copilots, coding agents or research tools should adopt the grammar even if they never install the component, because users judge trust from whether they can see what the agent did, in order, with honest status.</p>
<p>Three caveats. The patterns are written around AI SDK message parts; if you stream from another SDK you will write the mapping yourself. The release is days old, so expect APIs and examples to move, and remember that copied code does not update on its own. And showing raw reasoning is a product decision as well as a design one: the shadcn Reasoning demo collapses the text into “Thought for 5s” once the step finishes, which is a sensible default.</p>
<h2>How to adopt it this week</h2>
<ol><li><strong>List every step type your agent emits.</strong> Reasoning, tool calls, sources, plans, subagents, errors, approvals. If one does not fit “icon + title + status + optional detail”, question it before designing a new widget.</li>
<li><strong>Write titles as past-tense sentences.</strong> Present tense while running, past tense when done, and say the failure in words. That one rule fixes most screen-reader and scanning problems.</li>
<li><strong>Open while running, collapse when done.</strong> The demos open a line while the step streams and fold it afterwards; the person can still expand it.</li>
<li><strong>Put output in a small Code Block, never in the sentence.</strong> Commands, logs and diffs go inside the line’s expanded content at <code>size="sm"</code>.</li>
<li><strong>Keep approvals out of the trace.</strong> Ask with an explicit Deny / Approve item; record the decision as a normal line afterwards.</li>
<li><strong>Test the states, not just the happy path.</strong> Running, error, pending, nested, a very long title, keyboard-only, reduced motion, light and dark.</li></ol>
<pre><code># install
pnpm dlx shadcn@latest add trace
pnpm dlx shadcn@latest add code-block

# let your coding agent read the pattern
Add the Reasoning pattern from https://ui.shadcn.com/docs/ai-elements/base/reasoning.md to my chat.

# map message parts to lines
reasoning  → "Thinking" / "Thought for 5s", collapsible
tool call  → "Running &lt;cmd&gt;" / "Ran &lt;cmd&gt;" / "Failed to run &lt;cmd&gt;", output in Code Block sm
source     → link line, "(opens in a new tab)" in sr-only text
approval   → Confirmation item outside Trace, then a Tool line</code></pre>
<h2>Where UI Hub fits</h2>
<p>Trace and Code Block cover the activity inside a turn; the rest of the page still needs a direction. Browse the <em>chat</em> component kind in the UI Hub resource list for other agent and chat libraries to compare against, and pair them with the restrained look in our <a href="../shadcn-blocks-deep-dive/">shadcn Blocks deep dive</a>. If your agent also restyles your system, the same week shadcndesign turned its DS Manager into an MCP server, so a coding agent can change a shadcn theme while respecting locked values.</p>""",
 zh="""<p>2026 年 10 月 14 日，shadcn 发布了 <strong>Trace</strong>——一个专门展示智能体活动的组件，同时发布的还有 <strong>Code Block</strong> 和 <strong>AI Elements</strong>：一组完全用 shadcn/ui 组件拼成的智能体界面模式。这条公告在 X 上两天内超过 4500 个赞，第二天 shadcn-svelte 也上线了自己的 AI Elements。真正值得关注的不是「又多了几个组件」，而是背后的设计主张：推理、工具调用、来源、计划、子智能体运行，本质上是同一种形状，所以它们应该长得一样、用起来也一样。</p>
<h2>发布了什么</h2>
<ul><li><strong>Trace。</strong>一列「行」，每行是智能体走的一步。shadcn 团队说它是研究了数百个智能体界面里的组件后提炼出来的。每行有图标、标题、可选描述和状态（<code>running</code>、<code>error</code>、<code>pending</code>，运行中会有微光动效）。一行可以展开、链接到页面，或打开对话框、侧边面板、抽屉、气泡；行还能嵌套——摘要展开成步骤，步骤再展开成输出。它直接读取 AI SDK 流式输出的 reasoning、tool、source 等消息片段。</li>
<li><strong>Code Block。</strong>展示代码、终端输出、日志和 diff，带标题与操作按钮的页头、行号、换行、高亮行和 diff 行，还有专为 Trace 里工具输出准备的小尺寸（<code>size="sm"</code>）。</li>
<li><strong>AI Elements，21 个模式。</strong>Chat、Prompt Input、Reasoning、Tool、Plan、Subagent、Confirmation、Context、Sources、File Tree、Terminal、Test Results 等。没有 npm 包：每个模式都是一段组合代码，复制进你的仓库就归你；每个文档页还有 Markdown 版本，编码智能体可以直接读。</li>
<li><strong>覆盖所有底层与风格。</strong>Trace 和 Code Block 支持 Base UI、React Aria、Radix 三种底层，以及 shadcn/ui 全部八种风格；它们和 6 月发布的聊天组件（Message Scroller、Message、Bubble、Marker、Attachment、Questionnaire）配套使用。</li>
<li><strong>AI SDK Elements 将被弃用。</strong>你已经从 elements.ai-sdk.dev 复制的代码照常可用。每个模式页都附有迁移提示词，会在 <code>components/ai-elements</code> 里用新组件重建封装，同时保留所有导出名和 props。少数使用率低的元素（artifact、音频播放器、React Flow 画布相关组件、JSX 预览、语音和麦克风选择器）没有重做，文档列出了可以用哪些现有组件自己拼。</li></ul>
<h2>为什么重要：智能体界面有了「语法」</h2>
<p>此前大多数智能体界面都是按片段类型一块块拼的：这里一个推理折叠面板，那里一张工具调用卡片，别处再来一个来源气泡，各自的间距、图标逻辑和加载状态都不一样。结果就是熟悉的「调试日志」观感——每一轮回复都是一堆互不相干的小部件。Trace 用一套统一的行语法取代了它：一次思考、一条命令、一个子智能体之间，变化的只有图标、标题，以及点开这一行之后发生什么。</p>
<p>这套语法还逼着你把文案写好。它的无障碍说明写得非常具体：图标对辅助技术隐藏，所以标题就是可访问名称，应该写成一句说明发生了什么的话（「已编辑 trace.tsx」，而不是「trace.tsx」）。状态靠颜色和动效表达，所以也要写进文字里：运行时写「正在运行 pnpm build」，失败时写「pnpm build 运行失败」。偏好减少动效的用户看不到微光；放在 Message Scroller 里时，每新增一行只会被朗读一次。</p>
<p>Confirmation 模式还给出了一条很实用的规则：等待批准是一个「提问」，不是「活动」，所以它放在 Trace 之外，是一个带「拒绝 / 批准」按钮的条目；用户回答之后，它才变成一行 Tool 记录。「问」和「做」在视觉上是两回事。</p>
<h2>我们的看法</h2>
<p>这和本月整个行业的动作是一致的——从 Figma Specs 到 Claude Design：真正有用的单位不是生成器，而是一个人和智能体都能遵循的、共享且明确的形状。对智能体界面来说，Trace 就是这个形状。做 Copilot、编码智能体或研究工具的团队，即使不装这个组件，也应该采用这套语法，因为用户判断能不能信任智能体，靠的是能否按顺序看到它做了什么、状态是否诚实。</p>
<p>三点提醒。第一，这些模式是围绕 AI SDK 的消息片段写的；如果你用别的 SDK 做流式输出，映射得自己写。第二，发布才几天，API 和示例还会变，而复制进来的代码不会自己更新。第三，展示原始推理过程既是设计问题也是产品决策：shadcn 的 Reasoning 示例在步骤结束后会把内容收起成「Thought for 5s」，这是个合理的默认。</p>
<h2>本周就能用上的做法</h2>
<ol><li><strong>列出智能体会输出的每一种步骤。</strong>推理、工具调用、来源、计划、子智能体、报错、审批。如果某种步骤套不进「图标 + 标题 + 状态 + 可选详情」，先质疑它，再考虑设计新部件。</li>
<li><strong>标题写成完整的句子。</strong>运行中用进行时，完成后用完成时，失败要用文字说出来。这一条就能解决大部分读屏和快速浏览的问题。</li>
<li><strong>运行时展开，完成后收起。</strong>示例里步骤流式输出时自动展开，结束后折叠，用户仍可手动展开。</li>
<li><strong>输出放进小号 Code Block，别塞进句子里。</strong>命令、日志、diff 都放在这一行的展开内容里，用 <code>size="sm"</code>。</li>
<li><strong>审批不要放进 Trace。</strong>用明确的「拒绝 / 批准」条目来问，决定之后再记成普通的一行。</li>
<li><strong>测状态，而不只测顺利路径。</strong>运行中、报错、等待、嵌套、超长标题、纯键盘、减少动效、亮色和暗色。</li></ol>
<pre><code># 安装
pnpm dlx shadcn@latest add trace
pnpm dlx shadcn@latest add code-block

# 让编码智能体直接读模式文档
Add the Reasoning pattern from https://ui.shadcn.com/docs/ai-elements/base/reasoning.md to my chat.

# 消息片段 → 行
reasoning  → 「思考中」/「思考了 5 秒」，可折叠
tool call  → 「正在运行 &lt;命令&gt;」/「已运行」/「运行失败」，输出放 Code Block sm
source     → 链接行，sr-only 文本注明「在新标签页打开」
approval   → Trace 之外的 Confirmation 条目，回答后变成 Tool 行</code></pre>
<h2>UI Hub 能帮什么</h2>
<p>Trace 和 Code Block 解决的是一轮回复「内部」的活动展示，页面其余部分仍然需要一个视觉方向。可以在 UI Hub 资源列表里按 <em>chat</em> 组件类型筛选，对比其他智能体与聊天组件库，再参考我们的 <a href="../shadcn-blocks-deep-dive/">shadcn Blocks 深读</a> 里的克制风格。如果你的智能体还要改你的设计系统：同一周 shadcndesign 把 DS Manager 做成了 MCP 服务器，编码智能体可以在遵守锁定值的前提下修改 shadcn 主题。</p>""",
 refs=[('October 2026 - Trace, Code Block and AI Elements','shadcn/ui changelog','https://ui.shadcn.com/docs/changelog/2026-10-ai-elements'),('AI Elements: patterns for agentic interfaces','shadcn/ui docs','https://ui.shadcn.com/docs/ai-elements'),('Trace','shadcn/ui docs','https://ui.shadcn.com/docs/components/base/trace'),('Code Block','shadcn/ui docs','https://ui.shadcn.com/docs/components/base/code-block'),('Confirmation pattern','shadcn/ui docs','https://ui.shadcn.com/docs/ai-elements/base/confirmation'),('Reasoning pattern (Markdown for coding agents)','shadcn/ui docs','https://ui.shadcn.com/docs/ai-elements/base/reasoning.md'),('“I just published Trace, a new component for agent activity”','shadcn on X','https://x.com/shadcn/status/2110410655165779985'),('AI Elements for Svelte','shadcn-svelte docs','https://shadcn-svelte.com/docs/ai-elements'),('AI SDK Elements (being deprecated)','Vercel','https://elements.ai-sdk.dev/'),('Chatbot: message parts with useChat','AI SDK docs','https://ai-sdk.dev/docs/ai-sdk-ui/chatbot'),('shadcn chatbot template','shadcn-ui on GitHub','https://github.com/shadcn-ui/chatbot-template'),('Connect your coding agent to your design system','shadcndesign (Matt Wierzbicki)','https://www.shadcndesign.com/blog/ds-manager-mcp-server')]),
dict(slug='lovart-arti-design-agent-memory', date='2026-10-20', cat='agents', series=None, featured=True, tags=['Lovart','Arti','design agents','memory','review'],
 t=T('Lovart 2.0 and Arti: design agents learn to remember, run and review','Lovart 2.0 与 Arti：设计智能体学会了记忆、代跑和自查','Lovart 2.0 與 Arti：設計智慧體學會了記憶、代跑和自查','Lovart 2.0 と Arti：デザインエージェントが記憶し、任され、自ら見直す','Lovart 2.0과 Arti: 디자인 에이전트가 기억하고, 맡아서 하고, 스스로 검토한다','Lovart 2.0 dan Arti: ejen reka bentuk belajar mengingat, menjalankan dan menyemak','Lovart 2.0 và Arti: agent thiết kế biết ghi nhớ, tự chạy và tự rà soát',"Lovart 2.0 et Arti : les agents de design apprennent à se souvenir, à travailler seuls et à se relire",'Lovart 2.0 y Arti: los agentes de diseño aprenden a recordar, ejecutar y revisar','Lovart 2.0 und Arti: Design-Agenten lernen erinnern, selbst arbeiten und prüfen'),
 s=T('Lovart 2.0 adds an editable taste memory, scheduled design delegation and a background consistency check. Read alongside two other launches from 19 Oct, it shows where design agents are heading, and what you should write down before you hand one the work.',
     'Lovart 2.0 加入了可编辑的审美记忆、可定时的设计委托和后台一致性检查。和 10 月 19 日另外两项发布放在一起看，能看出设计智能体的走向，也能看出把活交出去之前你该先写清楚什么。',
     'Lovart 2.0 加入了可編輯的審美記憶、可排程的設計委託和背景一致性檢查。和 10 月 19 日另外兩項發布放在一起看，能看出設計智慧體的走向，也能看出把工作交出去之前你該先寫清楚什麼。',
     'Lovart 2.0は編集可能な好みの記憶、定期実行できるデザイン委任、バックグラウンドの一貫性チェックを追加。10月19日の他の2つの発表と並べると、デザインエージェントの方向性と、任せる前に書き出すべきことが見えてくる。',
     'Lovart 2.0은 편집 가능한 취향 메모리, 예약 가능한 디자인 위임, 백그라운드 일관성 검사를 추가했다. 10월 19일의 다른 두 발표와 함께 보면 디자인 에이전트의 방향과, 일을 맡기기 전에 적어 둘 것이 보인다.',
     'Lovart 2.0 menambah memori citarasa yang boleh disunting, delegasi reka bentuk berjadual dan semakan konsistensi di latar. Dibaca bersama dua pelancaran lain pada 19 Okt, ia menunjukkan hala tuju ejen reka bentuk.',
     'Lovart 2.0 thêm bộ nhớ gu thẩm mỹ chỉnh sửa được, giao việc thiết kế theo lịch và kiểm tra nhất quán chạy nền. Đặt cạnh hai bản phát hành khác ngày 19/10, ta thấy hướng đi của agent thiết kế.',
     "Lovart 2.0 ajoute une mémoire de goût modifiable, une délégation planifiée et une vérification de cohérence en arrière-plan. Lu avec deux autres lancements du 19 octobre, il montre où vont les agents de design.",
     'Lovart 2.0 añade una memoria de gusto editable, delegación programada y una revisión de coherencia en segundo plano. Junto a otros dos lanzamientos del 19 de octubre, muestra hacia dónde van los agentes de diseño.',
     'Lovart 2.0 bringt ein editierbares Geschmacksgedächtnis, geplante Design-Delegation und eine Konsistenzprüfung im Hintergrund. Zusammen mit zwei weiteren Launches vom 19. Oktober zeigt es, wohin Design-Agenten gehen.'),
 en="""<p>On 19 October Lovart shipped version 2.0 of its design agent, built around a new personal agent called Arti. The pitch is not a better image model. Lovart already routes to several third-party image and video models. The change is everything around generation: Arti keeps a memory of how you work, takes whole jobs on a schedule, researches before you start and checks the canvas while you work. It is a useful snapshot of where design agents are going, and of what you have to write down before you can trust one with real work.</p>
<h2>What actually shipped</h2>
<ul><li><strong>Memory you can read and edit.</strong> Lovart splits memory into four groups: basic information, collaboration style, aesthetic preferences and frequently used assets. Each entry can be viewed, edited or deleted, you choose whether it applies across projects, and you can seed it by chatting, from past projects, or by uploading a portfolio or a Markdown or memory file from another AI tool.</li>
<li><strong>Design delegation.</strong> Instead of a chain of prompts you write a brief (what to make, what to watch for, what done looks like), pick the target project, then run it once or daily, weekly or monthly. Each run has a credit limit, there is a Test run before you commit, and results land on a new canvas page. Lovart's own example: 168 product images for 42 SKUs in four sizes, run overnight after a four-SKU test.</li>
<li><strong>Design Research and Design Review.</strong> Research gathers references from sources such as Google, Pinterest and Behance into a report with a mood board. Review checks the canvas against the project's constraints in the background and only changes anything after you confirm. Lovart's example is a hand-drawn storyboard with one oil-paint frame that slipped through.</li>
<li><strong>Self-evolving skills.</strong> When you repeat the same workflow across projects more than three times, Lovart offers to save it as a reusable skill. You can switch this off.</li></ul>
<h2>The same week, the same idea elsewhere</h2>
<p>Two smaller launches on the same day point the same way. Gemini Notebook added a Review toggle so you can read and edit the outline or producer notes for slides and video overviews <em>before</em> anything renders. Automo's design engine now has a creative-director judge that looks at several rendered candidates and keeps the strongest, and its thumbs-up and thumbs-down now attach to the exact design you rated. Put together, the pattern is clear. The value is moving from "generate" to three other steps: remember what the person likes, show the plan before spending compute, and judge the output against something other than the average of the training data.</p>
<h2>Our take</h2>
<p>Memory is only as good as what is in it. A vague "I like clean, modern design" in memory produces the same generic result as a vague prompt, now on every project. The strongest line in Lovart's announcement is its own example memory: show three clearly different directions first, then build out the one I pick. That is a process rule, and process rules are what agents follow well. Treat the memory panel the way we treat a guideline file: short, specific and testable. The Review step is promising for the same reason. A consistency check needs explicit constraints to check against, so write them down at the start of the project rather than hoping the agent infers them.</p>
<p>Delegation is where the real risk is. A weekly job that quietly drifts off-brand is worse than no job. Lovart's guardrails (test run, credit limit, results on a separate canvas page, run history, pause) are the right shape, and you should use all of them.</p>
<h2>Checklist: before you hand a design agent the work</h2>
<ol><li><strong>Write the taste memory by hand.</strong> Three to six lines: palette in named values, type pairing, density, two or three references, and a never-list. Upload it as Markdown instead of letting the agent guess from old projects.</li>
<li><strong>Add one process rule.</strong> For example "three distinct directions first, then build out the chosen one", or "always show the outline before rendering".</li>
<li><strong>State constraints the reviewer can check.</strong> Style, aspect ratios, logo clear space, text-on-image contrast. If it is not written, no background check can catch it.</li>
<li><strong>Test before you schedule.</strong> Run a small batch (Lovart's own example used 4 of 42 SKUs), read every output, then set the schedule and a credit cap.</li>
<li><strong>Read the memory panel monthly.</strong> Delete anything stale or wrong. Learned preferences are guesses until you confirm them.</li>
<li><strong>Keep the final call.</strong> Accept fixes one by one, the way Lovart's Review asks you to, and never let a scheduled run publish straight to a live channel.</li></ol>
<pre><code># taste.md (upload as memory)
palette: cream #f6f1e7 · ink #1d1a16 · one accent, warm brown #8a5a3b
type: serif headlines + neutral sans body; no more than two weights
density: generous white space; one focal image per layout
process: show 3 clearly different directions first, then build the chosen one
never: neon gradients · stock 3D blobs · emoji as icons · text over busy photos
check: same illustration style on every frame · logo clear space ≥ 1× cap height</code></pre>
<h2>How UI Hub helps</h2>
<p>If you are writing that taste file from scratch, start from the house-style notes and specs in the <a href="../../kb/">UI Hub encyclopedia</a>, and our earlier piece on <a href="../taste-and-skills-for-agents/">teaching agents taste</a>. The format is the same whether the agent is Lovart, Claude, Cursor or Figma's: short rules first, pixels second.</p>""",
 zh="""<p>10 月 19 日，Lovart 发布了设计智能体 2.0 版本，核心是一个叫 Arti 的个人设计智能体。卖点不是更强的出图模型，Lovart 本来就接入了多家第三方的图像和视频模型。变化在生成之外：Arti 会记住你的工作方式，能按计划接下整件活，开工前先做调研，干活时在后台检查画布。它很好地说明了设计智能体正在往哪走，也说明了要放心把真活交给它之前，你得先写清楚什么。</p>
<h2>这次到底发布了什么</h2>
<ul><li><strong>能看、能改的记忆。</strong>Lovart 把记忆分成四组：基本信息、协作方式、审美偏好和常用素材。每一条都能查看、修改或删除，由你决定是否跨项目使用；可以通过对话告诉它，可以让它从过去的项目里学，也可以上传作品集、Markdown 文档或其他 AI 工具导出的记忆文件。</li>
<li><strong>设计委托。</strong>不再是一串提示词，而是写一份需求（做什么、注意什么、做成什么样算完成），选好结果放进哪个项目，然后选择只跑一次，或者按天、周、月定时跑。每次运行有积分上限，正式创建前可以先试跑，结果落在新的画布页里。Lovart 自己举的例子：主视觉定稿后，先用 4 个 SKU 试跑，再通宵跑完 42 个 SKU、4 种尺寸共 168 张图。</li>
<li><strong>设计调研与设计检查。</strong>调研会从 Google、Pinterest、Behance 等来源收集参考，整理成带情绪板的报告。检查会在后台对照项目约束扫一遍画布，只有你确认后才会改动。Lovart 的例子是：一组本该统一手绘动画风格的分镜里，混进了一帧油画质感，被检查出来了。</li>
<li><strong>自我进化的技能。</strong>同一套流程在不同项目里用了三次以上，Lovart 会提议把它存成可复用的技能。这个功能可以关掉。</li></ul>
<h2>同一天，别处也在做同一件事</h2>
<p>同一天还有两项较小的发布，方向一致。Gemini Notebook 给幻灯片和视频概览加了一个 Review 开关，可以在任何内容渲染<em>之前</em>先看、先改大纲或制作说明。Automo 的设计引擎加入了一个「创意总监」评审，会看多个渲染好的候选稿，只留下最强的那张；你的点赞和点踩也会精确对应到你评价的那一稿。放在一起看，规律很清楚：价值正在从「生成」转向另外三步——记住这个人喜欢什么，在花算力之前先给出方案，用训练数据平均值以外的标准来评判结果。</p>
<h2>我们的看法</h2>
<p>记忆的质量取决于里面写了什么。如果记忆里只有一句模糊的「我喜欢简洁现代」，结果就和模糊的提示一样平庸，而且会出现在每一个项目里。Lovart 公告里最有用的一句，其实是它自己举的记忆示例：先给三个明显不同的方向，等我选定一个再做全套。这是一条流程规则，而流程规则恰恰是智能体最能遵守的。对待记忆面板，就像对待规范文件一样：短、具体、可检验。设计检查值得期待也是同样的道理：一致性检查需要明确的约束才能对照，所以要在项目一开始就写下来，而不是指望智能体自己猜。</p>
<p>真正的风险在委托。一个每周悄悄跑偏品牌的定时任务，比没有任务更糟。Lovart 给的护栏（试跑、积分上限、结果放在单独的画布页、运行历史、随时暂停）方向是对的，每一项都应该用上。</p>
<h2>清单：把活交给设计智能体之前</h2>
<ol><li><strong>亲手写审美记忆。</strong>三到六行：用具体色值写配色、字体搭配、疏密、两三个参考，加一份禁止清单。以 Markdown 上传，不要让智能体从旧项目里猜。</li>
<li><strong>加一条流程规则。</strong>比如「先给三个不同方向，再把选中的做完整」，或者「渲染前一定先给大纲」。</li>
<li><strong>写出检查得了的约束。</strong>风格、画幅比例、Logo 安全区、图上文字的对比度。没写下来的，任何后台检查都抓不到。</li>
<li><strong>先试跑再定时。</strong>先跑一小批（Lovart 的例子是 42 个 SKU 里先跑 4 个），每一张都看过，再设定计划和积分上限。</li>
<li><strong>每月看一次记忆面板。</strong>删掉过时或错误的条目。学来的偏好在你确认之前都只是猜测。</li>
<li><strong>最终决定留在自己手里。</strong>像 Lovart 的检查流程要求的那样逐条确认修改，绝不让定时任务直接发布到线上渠道。</li></ol>
<pre><code># taste.md（作为记忆上传）
配色：奶油白 #f6f1e7 · 墨色 #1d1a16 · 只有一个强调色，暖棕 #8a5a3b
字体：衬线标题 + 中性无衬线正文；最多两种字重
疏密：留白充足；每个版面只有一个视觉焦点
流程：先给 3 个明显不同的方向，再把选中的做完整
禁止：霓虹渐变 · 图库 3D 软泡 · 用 emoji 当图标 · 文字压在杂乱照片上
检查：每一帧插画风格一致 · Logo 安全区 ≥ 1 倍大写字母高度</code></pre>
<h2>UI Hub 能帮什么</h2>
<p>如果要从零写这份审美文件，可以从 <a href="../../kb/">UI Hub 设计百科</a> 里的风格笔记和规范起步，再看我们之前那篇<a href="../taste-and-skills-for-agents/">教智能体审美</a>。无论智能体是 Lovart、Claude、Cursor 还是 Figma 的，格式都一样：先写短规则，再出像素。</p>""",
 refs=[('Lovart 2.0: Meet Arti, your personal design agent','Lovart','https://www.lovart.ai/news/lovart-2-0-arti'),('Lovart','Lovart','https://www.lovart.ai/'),('How to shape your slides and videos with Gemini Notebook','Google (Viraj Doshi, Shan Wang)','https://blog.google/innovation-and-ai/products/gemini-notebook/co-create-slides-videos/'),('Designs chosen by taste, not just by rule','Automo.ai','https://automo.ai/releases/designs-chosen-by-taste-not-just-by-rule'),('Teaching agents taste: how design skills de-slop AI interfaces','UI Hub','https://siinxu.github.io/ui-resource-hub/blog/taste-and-skills-for-agents/')]),
dict(slug='layers-brand-kits-json-ai-visuals', date='2026-10-21', cat='tools', series=None, featured=True, tags=['Vyb','Gemini','Fibo 2','layers','brand kit'],
 t=T('Layers, brand kits and JSON: three ways AI visuals stop looking generic','图层、品牌包和 JSON：让 AI 视觉不再千篇一律的三条路','圖層、品牌包和 JSON：讓 AI 視覺不再千篇一律的三條路','レイヤー、ブランドキット、JSON：AIビジュアルが没個性から抜け出す3つの方法','레이어, 브랜드 키트, JSON: AI 비주얼이 뻔해지지 않는 세 가지 방법','Lapisan, kit jenama dan JSON: tiga cara visual AI berhenti kelihatan generik','Layer, bộ nhận diện và JSON: ba cách để hình ảnh AI hết rập khuôn',"Calques, kits de marque et JSON : trois façons de rendre les visuels IA moins génériques",'Capas, kits de marca y JSON: tres formas de que los visuales con IA dejen de parecer genéricos','Ebenen, Brand-Kits und JSON: drei Wege, wie KI-Visuals nicht mehr generisch wirken'),
 s=T('On 20 October Coco Labs launched Vyb, a design model that builds in layers; Gemini started remembering an uploaded brand style; and Bria shipped Fibo 2, which turns every edit into editable JSON. Three different answers to the same problem, and a checklist for using them.',
     '10 月 20 日，Coco Labs 发布了按图层构建设计的模型 Vyb，Gemini 开始记住你上传的品牌风格，Bria 推出了把每次编辑都变成可改 JSON 的 Fibo 2。同一个问题的三种解法，附一份实用清单。',
     '10 月 20 日，Coco Labs 發布了按圖層建構設計的模型 Vyb，Gemini 開始記住你上傳的品牌風格，Bria 推出了把每次編輯都變成可改 JSON 的 Fibo 2。同一個問題的三種解法，附一份實用清單。',
     '10月20日、Coco Labsはレイヤーで組み立てるデザインモデルVybを発表し、Geminiはアップロードしたブランドスタイルを記憶し始め、BriaはすべてのEditを編集可能なJSONにするFibo 2を公開。同じ課題への3つの答えと実践チェックリスト。',
     '10월 20일 Coco Labs는 레이어로 디자인을 만드는 모델 Vyb를, Gemini는 업로드한 브랜드 스타일 기억 기능을, Bria는 모든 편집을 수정 가능한 JSON으로 바꾸는 Fibo 2를 내놓았다. 같은 문제에 대한 세 가지 답과 체크리스트.',
     'Pada 20 Okt, Coco Labs melancarkan Vyb yang membina reka bentuk secara berlapis, Gemini mula mengingati gaya jenama yang dimuat naik, dan Bria melancarkan Fibo 2 yang menjadikan setiap suntingan JSON boleh diubah. Tiga jawapan dan satu senarai semak.',
     'Ngày 20/10, Coco Labs ra mắt Vyb, mô hình thiết kế dựng theo layer; Gemini bắt đầu ghi nhớ phong cách thương hiệu bạn tải lên; Bria phát hành Fibo 2, biến mỗi lần chỉnh sửa thành JSON sửa được. Ba lời giải và một checklist.',
     "Le 20 octobre, Coco Labs a lancé Vyb, un modèle qui construit en calques ; Gemini mémorise désormais un style de marque importé ; Bria a publié Fibo 2, qui transforme chaque retouche en JSON modifiable. Trois réponses et une checklist.",
     'El 20 de octubre Coco Labs lanzó Vyb, un modelo que diseña por capas; Gemini empezó a recordar un estilo de marca subido; y Bria publicó Fibo 2, que convierte cada edición en JSON editable. Tres respuestas y una lista de control.',
     'Am 20. Oktober brachte Coco Labs Vyb, ein Modell, das in Ebenen gestaltet; Gemini merkt sich jetzt einen hochgeladenen Markenstil; Bria veröffentlichte Fibo 2, das jede Bearbeitung in editierbares JSON verwandelt. Drei Antworten und eine Checkliste.'),
 en="""<p>The most common complaint about AI-made graphics is not that they look bad. It is that they all look the same: the right mood, the wrong font, a brand colour that is almost but not quite yours, and a headline that melts when you try to change one word. Three launches on 20 October attack that problem from three different directions, and together they make a useful map of what to ask from any visual AI tool you adopt.</p>
<h2>Three launches, three answers</h2>
<ul><li><strong>Vyb (Coco Labs): build in layers.</strong> Vyb is pitched as a design model, not an image generator. It assembles your own images, fonts and colours layer by layer, so text stays text, graphics stay vectors and photos stay pixels, and it calls image generators only to fill gaps. Under the hood is a new design language, Cocolang, which Coco Labs says is compact enough for a model's context window and exports losslessly to tools such as Figma. It is in early access behind a waitlist.</li>
<li><strong>Gemini: remember the brand.</strong> Google's new business hub in Gemini lets you define a brand style by uploading your website, brand kit, fonts or colour palettes. Paired with its Nano Banana 2.1 image model, Gemini keeps that style for later requests, so you do not have to re-upload guidelines for every campaign. Google says it rolls out globally over the coming days.</li>
<li><strong>Fibo 2 (Bria): make the edit inspectable.</strong> Bria's new open-weights model, trained on licensed data, turns a plain-language edit into a structured JSON instruction (objects, lighting, background, text and the edit itself), then applies that JSON. You can generate the JSON separately, review or change it, and pass your own. With the same images, JSON and seed you can recreate a result. Edits can combine up to four reference images, or use a mask on a single image to protect everything outside it.</li></ul>
<h2>What the numbers do and do not say</h2>
<p>Coco Labs published its own benchmarks. On 145 Google fonts, Vyb matched the reference letter shapes 90.3% of the time against 76.0% for the next model it tested; on exact hex colours its average error was zero; and over 200 edits it changed 11.9% of pixels on average, while the image models it compared changed more than 90%. Those are vendor tests on public fonts, not independent results, but the last figure is the one that matters for daily work. A model that repaints the whole image to change one word slowly erodes everything you liked about the first version. Vyb's approval rate was also slightly lower than its best rival's, which Coco Labs puts down to the model declining edits that would hurt legibility.</p>
<h2>Our take</h2>
<p>All three are moving taste out of the prompt and into something you can check. Layers make your fonts and colours facts rather than suggestions. A stored brand style turns guidelines into a reusable asset. Structured JSON turns an edit into a diff you can review before it renders. The common failure they target is the same one we see in generated interfaces: the model drifts toward the average of its training data unless your choices are pinned down in a form it cannot reinterpret.</p>
<p>Two cautions. First, a remembered brand style is only as good as the kit you upload. A logo and a vague palette will give you consistent mediocrity. Second, do not mistake a layered export for a design system. If the tool outputs editable text in your font but ignores your spacing and hierarchy rules, you still have cleanup work. Ask for the layers, and still check the layout.</p>
<h2>Checklist: making AI visuals look like yours</h2>
<ol><li><strong>Prepare a real brand kit before you start.</strong> Fonts as files, colours as hex values, logo in vector, two or three approved reference layouts, and a short list of things you never do.</li>
<li><strong>Test fidelity with one boring asset.</strong> Ask for a plain banner with your headline font and primary colour, then check the font and pick the colour with an eyedropper. If either is off, the tool is guessing.</li>
<li><strong>Test edit drift.</strong> Change one word or one colour and compare before and after. Anything else that moved is a warning sign for multi-round work.</li>
<li><strong>Prefer outputs you can open.</strong> Layered files or Figma export for anything that will be edited again; flat images only for one-off use.</li>
<li><strong>Keep the instruction, not just the image.</strong> When a tool exposes structured instructions and seeds, as Fibo 2 does, save them next to the asset so a variant next month starts from the same spec.</li>
<li><strong>Protect what must not change.</strong> Use masks, locked layers or explicit "keep everything else" rules for product photos, faces and logos.</li></ol>
<pre><code>{
  "brand": "Northwind Tea",
  "fonts": { "display": "Fraunces 600", "body": "Inter 400" },
  "colors": { "ink": "#1d1a16", "paper": "#f6f1e7", "accent": "#8a5a3b" },
  "logo": "logo.svg  (clear space ≥ 1× cap height)",
  "layout": "one focal photo · headline top-left · max 2 text blocks",
  "never": ["gradients on text", "stock 3D", "more than one accent"],
  "keep": "product photo pixels untouched; edit text and colour only"
}</code></pre>
<h2>How UI Hub helps</h2>
<p>The brand kit above is the visual sibling of a token file. If you are setting one up for a product, our posts on <a href="../design-tokens-for-agents/">design tokens for agents</a> and <a href="../oklch-color-and-dark-mode/">OKLCH colour</a> cover naming and colour choices, and yesterday's piece on <a href="../lovart-arti-design-agent-memory/">Lovart's taste memory</a> shows the same idea from the agent side: write your taste down in a form a machine can check.</p>""",
 zh="""<p>人们对 AI 生成图形最常见的抱怨，不是难看，而是都长一个样：氛围对了，字体不对；品牌色差一点点；想改标题里一个字，整行字就糊了。10 月 20 日的三项发布从三个方向处理这个问题，放在一起看，正好是一张选择任何视觉 AI 工具时该问什么的地图。</p>
<h2>三项发布，三种答案</h2>
<ul><li><strong>Vyb（Coco Labs）：按图层构建。</strong>Vyb 的定位是设计模型，不是出图模型。它把你自己的图片、字体和颜色一层一层组合起来：文字保持为文字，图形保持为矢量，照片保持为像素，只在需要补位时才调用图像生成器。底层是一种新的设计语言 Cocolang，Coco Labs 说它足够紧凑、适合模型的上下文窗口，并能无损导出到 Figma 等工具。目前需要加入候补名单抢先体验。</li>
<li><strong>Gemini：记住品牌。</strong>Google 在 Gemini 里推出了面向小企业的新入口，可以上传网站、品牌包、字体或配色来定义品牌风格。配合 Nano Banana 2.1 图像模型，Gemini 会在之后的请求里沿用这套风格，不必每次做活动都重新上传规范。Google 表示会在未来几天全球陆续上线。</li>
<li><strong>Fibo 2（Bria）：让每次编辑可检查。</strong>Bria 的新开放权重模型使用授权数据训练，会先把一句自然语言修改翻译成结构化 JSON 指令（对象、光线、背景、文字和修改本身），再按这份 JSON 执行。你可以单独生成这份 JSON，审阅或修改后再传回去，也可以直接传自己写的。用同样的图片、JSON 和种子就能复现结果。一次编辑最多可组合四张参考图，单图编辑还能用蒙版保护蒙版外的全部内容。</li></ul>
<h2>这些数字说明了什么、没说明什么</h2>
<p>Coco Labs 公布了自家基准测试：在 145 款 Google 字体上，Vyb 的字形吻合度为 90.3%，它测试的次优模型为 76.0%；指定十六进制颜色时平均误差为零；在 200 次编辑中，Vyb 平均只改动 11.9% 的像素，而对比的图像模型都超过 90%。这些是厂商用公开字体做的测试，不是独立结果，但最后一个数字对日常工作最关键：为了改一个字而重画整张图的模型，会一点点磨掉你喜欢第一版的所有理由。另外，Vyb 的通过率略低于最强对手，Coco Labs 的解释是模型会拒绝会损害可读性的修改。</p>
<h2>我们的看法</h2>
<p>三者都在把「审美」从提示词里搬出来，放进可以检查的东西里。图层让你的字体和颜色成为事实而不是建议；存下来的品牌风格把规范变成可复用的资产；结构化 JSON 把一次修改变成渲染前可以审阅的差异。它们针对的失败，和我们在 AI 生成界面里看到的是同一种：除非你的选择以模型无法重新诠释的形式固定下来，否则模型总会滑向训练数据的平均值。</p>
<p>两点提醒。第一，记住的品牌风格只和你上传的品牌包一样好。只有一个 Logo 和一套模糊的配色，得到的就是稳定的平庸。第二，别把分层导出当成设计系统。如果工具输出了你字体的可编辑文字，却无视你的间距和层级规则，后面还是要返工。图层要争取，版式也照样要检查。</p>
<h2>清单：让 AI 视觉看起来像你的</h2>
<ol><li><strong>开工前准备真正的品牌包。</strong>字体用文件、颜色用十六进制值、Logo 用矢量，再加两三个认可的参考版式和一份「绝不做」清单。</li>
<li><strong>用一张最无聊的图测保真度。</strong>让它做一张只有标题字体和主色的简单横幅，核对字体，再用取色器吸一下颜色。任何一项不对，说明工具在猜。</li>
<li><strong>测编辑漂移。</strong>只改一个词或一个颜色，对比前后。其他地方也动了，就是多轮修改的危险信号。</li>
<li><strong>优先选能打开的输出。</strong>还要再改的素材用分层文件或 Figma 导出；平面图只用于一次性场景。</li>
<li><strong>保存指令，而不只是图片。</strong>工具像 Fibo 2 那样提供结构化指令和种子时，把它们和素材存在一起，下个月做变体就能从同一份规格出发。</li>
<li><strong>保护不能改的部分。</strong>产品照片、人脸和 Logo 用蒙版、锁定图层或明确的「其他全部保持不变」规则保护。</li></ol>
<pre><code>{
  "brand": "Northwind Tea",
  "fonts": { "display": "Fraunces 600", "body": "Inter 400" },
  "colors": { "ink": "#1d1a16", "paper": "#f6f1e7", "accent": "#8a5a3b" },
  "logo": "logo.svg（安全区 ≥ 1 倍大写字母高度）",
  "layout": "一张焦点照片 · 标题在左上 · 最多 2 段文字",
  "never": ["文字渐变", "图库 3D", "超过一个强调色"],
  "keep": "产品照片像素不动，只改文字和颜色"
}</code></pre>
<h2>UI Hub 能帮什么</h2>
<p>上面的品牌包，相当于视觉版的 Token 文件。如果要为产品建一份，可以看我们的<a href="../design-tokens-for-agents/">给智能体的设计 Token</a>和 <a href="../oklch-color-and-dark-mode/">OKLCH 配色</a>，讲命名和选色；昨天那篇 <a href="../lovart-arti-design-agent-memory/">Lovart 审美记忆</a>则是从智能体一侧讲同一件事：把你的审美写成机器能检查的形式。</p>""",
 refs=[('Introducing Vyb - Our First Design Model That Understands Taste','Coco Labs (David Zats, Anusha Ramesh)','https://cocolabs.ai/blog/introducing-vyb'),('Coco Labs','Coco Labs','https://cocolabs.ai/'),('New Gemini tools for small business owners','Google (Vishnu Sivaji)','https://blog.google/innovation-and-ai/products/gemini-app/new-tools-small-business-owners/'),('Fibo 2 is live','Bria AI docs','https://docs.bria.ai/whats-new/fibo-2'),('Generate Structured Instruction','Bria AI docs','https://docs.bria.ai/image-editing/editing/generate-structured-instruction'),('Image Edit by Text','Bria AI docs','https://docs.bria.ai/image-editing/editing/edit-image'),('Bria AI models','Hugging Face','https://huggingface.co/briaai'),('Qwen-Image-Layered','QwenLM on GitHub','https://github.com/QwenLM/Qwen-Image-Layered'),('Design tokens for agents','UI Hub','https://siinxu.github.io/ui-resource-hub/blog/design-tokens-for-agents/')]),
dict(slug='lint-agents-onto-your-design-system', date='2026-10-22', cat='agents', series=None, featured=True, tags=['onsystem','@shadcn/lint','Figma Guidelines','design systems','linting'],
 t=T('Lint the agent: keeping AI-written UI on your design system','给智能体上 Lint：让 AI 写的界面守住你的设计系统','給智能體上 Lint：讓 AI 寫的介面守住你的設計系統','エージェントにLintを：AIが書くUIをデザインシステムに留める','에이전트에 린트를: AI가 쓴 UI를 디자인 시스템 안에 묶어 두기','Lint untuk ejen: memastikan UI tulisan AI kekal dalam sistem reka bentuk anda','Lint cho agent: giữ UI do AI viết bám đúng design system','Linter l’agent : garder l’UI écrite par l’IA dans votre design system','Lintear al agente: mantener la UI escrita por IA dentro de tu design system','Den Agenten linten: KI-geschriebene UI im eigenen Design-System halten'),
 s=T('On 22 October the open-source onsystem went public, joining shadcn’s agent-first linter and Figma’s new Guidelines and system check. The shared idea: stop asking agents to follow your design system and start checking every edit. What the benchmark shows, and a setup checklist.',
     '10 月 22 日，开源工具 onsystem 公开发布，与 shadcn 面向智能体的 Lint 工具、Figma 新推出的 Guidelines 和系统检查站到了一起。共同思路是：别再只“请”智能体遵守设计系统，而是检查每一次编辑。基准测试说明了什么，附一份配置清单。',
     '10 月 22 日，開源工具 onsystem 公開發布，與 shadcn 面向智能體的 Lint 工具、Figma 新推出的 Guidelines 和系統檢查站到了一起。共同思路是：別再只「請」智能體遵守設計系統，而是檢查每一次編輯。基準測試說明了什麼，附一份設定清單。',
     '10月22日、オープンソースのonsystemが公開され、shadcnのエージェント向けリンターやFigmaの新しいGuidelines・システムチェックに加わった。共通の考え方は、デザインシステムを守るよう頼むのではなく、すべての編集を検査すること。ベンチマークの読み方と導入チェックリスト。',
     '10월 22일 오픈소스 onsystem이 공개되며 shadcn의 에이전트용 린터, Figma의 새 Guidelines·시스템 체크와 나란히 섰다. 공통된 생각은 디자인 시스템을 지켜 달라고 부탁하지 말고 모든 편집을 검사하라는 것. 벤치마크가 말하는 것과 설정 체크리스트.',
     'Pada 22 Okt, onsystem sumber terbuka dilancarkan, menyertai linter shadcn untuk ejen serta Guidelines dan semakan sistem baharu Figma. Idea yang sama: berhenti meminta ejen mematuhi sistem reka bentuk, mula menyemak setiap suntingan. Apa kata penanda arasnya, dan senarai semak persediaan.',
     'Ngày 22/10, công cụ mã nguồn mở onsystem ra mắt, đứng cạnh linter dành cho agent của shadcn và Guidelines cùng system check mới của Figma. Ý chung: đừng chỉ nhờ agent tuân thủ design system, hãy kiểm tra từng lần sửa. Benchmark nói gì và checklist thiết lập.',
     "Le 22 octobre, l’outil open source onsystem est sorti, rejoignant le linter pour agents de shadcn et les nouvelles Guidelines et vérifications système de Figma. L’idée commune : ne plus demander à l’agent de respecter le design system, mais vérifier chaque modification. Ce que dit le benchmark, et une checklist.",
     'El 22 de octubre se publicó onsystem, de código abierto, junto al linter para agentes de shadcn y las nuevas Guidelines y comprobaciones de sistema de Figma. La idea común: dejar de pedir al agente que respete el design system y empezar a revisar cada edición. Qué dice el benchmark y una lista de configuración.',
     'Am 22. Oktober erschien das Open-Source-Tool onsystem, neben shadcns Linter für Agenten und Figmas neuen Guidelines und System-Checks. Die gemeinsame Idee: Agenten nicht mehr bitten, das Design-System einzuhalten, sondern jede Änderung prüfen. Was der Benchmark zeigt, plus Setup-Checkliste.'),
 en="""<p>Ask a coding agent for a settings card in a shadcn/ui project and you often get something that type-checks and still looks wrong: a hex red instead of the destructive token, <code>p-[13px]</code> instead of the spacing scale, a native <code>&lt;button&gt;</code> with hand-rolled classes next to your real Button, and a <code>variant="danger"</code> your Button has never heard of. The agent is not careless. It writes from its training data, and it cannot see your Storybook. This week the tooling around that gap got noticeably more serious.</p>
<h2>Three tools, one shift</h2>
<ul><li><strong>onsystem (22 October).</strong> Diogo Esteves made public an MIT-licensed checker that reads your design system from source and flags agent-written React that strays from it. Its eight rules cover hard-coded colours, spacing and radius, native elements your system already wraps, invented components, unknown props, unknown variant values, and icon buttons without an accessible name. Each finding comes with the replacement to write. It runs in three places: an MCP server the agent can call (<code>check_ui</code>) to see your components and tokens, a hook that checks each file right after the agent edits it in Claude Code, and a CLI, ESLint plugin and GitHub Action for pull requests. It makes no model calls.</li>
<li><strong>@shadcn/lint.</strong> shadcn's own "agent-first linter for Tailwind design systems" takes the policy route. You declare what may change, for example that a Button accepts margin and width but owns its padding, and when an agent breaks the rule the error explains why and points to an existing size or variant. It works with Tailwind v4 in React, Svelte and Vue, through ESLint or Oxlint, and does not require shadcn/ui.</li>
<li><strong>Figma Guidelines and system check.</strong> Announced at Config India on 15 October, Guidelines (open beta) let you attach written rules to a published library so agents reading it through Figma's MCP server follow the patterns your team set. A previewed system check scans the library itself for gaps such as missing descriptions and interactive states. That is the same idea one layer up: lint the source of truth, not only the code.</li></ul>
<h2>What the benchmark says</h2>
<p>onsystem ships with a public benchmark run on 12 October: six models from three providers each wrote the same 20 UI components in five open-source repositories, 240 runs per configuration. Measured by onsystem's own check, design-system errors fell from 0.85 per run with no help to 0.00 with its skill, MCP server and hook together, with type-check pass rates (93% vs 92%) and cost per run essentially unchanged. Scored by @shadcn/lint, a linter it does not control, findings per run went from 4.97 to 2.64.</p>
<p>Two readings matter more than the headline. First, the tool under test scores the headline, which the author states openly, so the independent number is the one to quote: roughly half the problems gone, not all of them. Second, the breakdown by part is the real lesson. The written skill alone, a set of instructions in the prompt, cut errors to 0.42 per run. The MCP server alone reached 0.01 and the hook alone 0.05. Telling the agent the rules helps; giving it something to query and something that pushes back helps far more.</p>
<h2>Our take</h2>
<p>For two years the answer to off-brand AI UI has been better context: tokens files, AGENTS.md, taste skills, guideline documents. Those still matter, because they tell the agent what good looks like. But context is a request, and a linter is a contract. The pattern emerging this month is a loop of read, write, check, fix: the agent reads your components and tokens, writes, gets a precise error with the fix, and corrects itself before you ever review it. Designers should care, because the rules in that loop are design decisions. Which props may be overridden, which spacing values are legal, which elements need a label: someone has to write those down, and it should be the people who own the system.</p>
<p>A caution: static checks only see what they can read. onsystem documents that classes built at runtime, such as <code>bg-${color}-500</code>, or values passed in from another file are not followed. @shadcn/lint's <code>require-static-classes</code> rule exists to flag exactly those cases. Linting also says nothing about hierarchy, rhythm or taste, so it shrinks review work rather than replacing it.</p>
<h2>Checklist: putting a design-system check in the agent loop</h2>
<ol><li><strong>Run a baseline first.</strong> Check your current app with no setup (<code>npx -y onsystem check .</code> for React, or the @shadcn/lint quickstart) and count findings by rule. That tells you where agents and people already drift.</li>
<li><strong>Write policies, not just tokens.</strong> For each core component, decide what callers may change (layout, margin, width) and what the component owns (padding, radius, colour). Put that in lint config, where an agent gets an error, not in a wiki.</li>
<li><strong>Make every error teach.</strong> Prefer rules whose message names the token, size or variant to use instead. An error that only says "not allowed" sends the agent guessing again.</li>
<li><strong>Check at edit time and at merge time.</strong> A hook or MCP tool keeps the agent honest while it works; the same rules in CI catch anything that slips through, including human edits.</li>
<li><strong>Forbid what you cannot read.</strong> Turn on a rule that rejects dynamically built class names, so the linter's blind spots do not become the agent's favourite escape hatch.</li>
<li><strong>Fix the system when the lint is noisy.</strong> If agents keep reaching for a missing variant, that is a gap in your design system. Add it on purpose, as both tools suggest, rather than loosening the rule.</li>
<li><strong>Still review the pixels.</strong> Clean lint means the parts are legal, not that the screen is good. Keep a visual check for hierarchy, density and states.</li></ol>
<pre><code># 1. see what drifts today (React, no install)
npx -y onsystem check .

# 2. or ask your agent to set up shadcn's linter
"Read https://github.com/shadcn-ui/lint/blob/main/SETUP.md
 and set up @shadcn/lint in this project."

# 3. a policy: Button keeps its own size and shape
"shadcn/no-restyle": ["error", { allow: ["layout"] }]

# 4. the same rules on every pull request
- uses: dgesteves/onsystem@v0</code></pre>
<h2>How UI Hub helps</h2>
<p>A linter can only enforce choices that exist. If you are still defining them, start with our posts on <a href="../design-tokens-for-agents/">design tokens for agents</a> and <a href="../component-composition/">component composition</a>, then use <a href="../claude-cursor-design-skills/">design skills for Claude and Cursor</a> for the instruction layer. This post is the missing third step: once the agent knows the rules, check that it kept them.</p>""",
 zh="""<p>在 shadcn/ui 项目里让编码智能体写一张设置卡片，常常得到能通过类型检查、看起来却不对的东西：用十六进制红色代替 destructive Token，用 <code>p-[13px]</code> 代替间距阶梯，在你真正的 Button 旁边写一个手搓样式的原生 <code>&lt;button&gt;</code>，再加一个你的 Button 根本没有的 <code>variant="danger"</code>。智能体不是不认真，而是凭训练数据写代码，它看不到你的 Storybook。这周，围绕这道缝隙的工具明显成熟了一截。</p>
<h2>三个工具，一个转向</h2>
<ul><li><strong>onsystem（10 月 22 日）。</strong>Diogo Esteves 公开了一款 MIT 许可的检查工具：它从源码读取你的设计系统，标出智能体写的、偏离系统的 React 代码。八条规则覆盖写死的颜色、间距和圆角，系统已封装却仍用原生元素，凭空捏造的组件、不存在的属性、不存在的变体值，以及没有无障碍名称的图标按钮。每条问题都附上应该改成什么。它在三个位置运行：智能体可调用的 MCP 服务（<code>check_ui</code>），让它看到你的组件和 Token；在 Claude Code 里每次编辑后立即检查该文件的钩子；以及用于拉取请求的命令行、ESLint 插件和 GitHub Action。全程不调用模型。</li>
<li><strong>@shadcn/lint。</strong>shadcn 官方这款「面向智能体的 Tailwind 设计系统 Lint 工具」走的是策略路线：由你声明什么能改，例如 Button 可以接受外边距和宽度，但内边距归它自己管。智能体违规时，报错会解释原因，并指向现有的尺寸或变体。它支持 React、Svelte 和 Vue 中的 Tailwind v4，可接入 ESLint 或 Oxlint，不要求使用 shadcn/ui。</li>
<li><strong>Figma Guidelines 与系统检查。</strong>10 月 15 日在 Config India 上发布的 Guidelines（公开测试）可以把书面规则挂在已发布的组件库上，智能体通过 Figma 的 MCP 服务读取时，就会遵循团队定下的模式。预览中的系统检查则扫描组件库本身，找出缺少描述、缺少交互状态之类的漏洞。这是同一思路往上一层：不只检查代码，也检查事实来源。</li></ul>
<h2>基准测试说明了什么</h2>
<p>onsystem 附带一份 10 月 12 日跑的公开基准测试：来自三家厂商的六个模型，在五个开源仓库里各写同样的 20 个界面组件，每种配置 240 次运行。按 onsystem 自己的检查计数，设计系统错误从无辅助时每次 0.85 个，降到技能、MCP 服务和钩子齐上时的 0.00 个，类型检查通过率（93% 对 92%）和每次成本基本不变。换用它控制不了的 @shadcn/lint 打分，每次的问题数从 4.97 降到 2.64。</p>
<p>比标题数字更重要的有两点。第一，标题数字是被测工具自己打的分，作者也明说了，所以该引用的是独立那组：问题大约少了一半，而不是全部消失。第二，按组件拆开的结果才是真正的教训。只给书面技能（也就是写在提示里的一套说明），错误降到每次 0.42；只用 MCP 服务降到 0.01，只用钩子降到 0.05。把规则告诉智能体有用；给它可以查询的东西、会反驳它的东西，有用得多。</p>
<h2>我们的看法</h2>
<p>两年来，解决 AI 界面不合品牌的答案一直是更好的上下文：Token 文件、AGENTS.md、审美技能、规范文档。这些仍然重要，因为它们告诉智能体什么是好的。但上下文只是请求，Lint 才是契约。这个月浮现的模式是一个「读、写、查、改」的循环：智能体读取你的组件和 Token，写代码，拿到附带修法的精确报错，在你审阅之前就自己改好。设计师应该关心这件事，因为循环里的规则本身就是设计决策：哪些属性可以覆盖，哪些间距值合法，哪些元素必须有标签，总得有人把它们写下来，而这个人应该是系统的负责人。</p>
<p>一点提醒：静态检查只看得见它读得懂的东西。onsystem 文档写明，运行时拼出来的类名（如 <code>bg-${color}-500</code>）或从别的文件传进来的值不会被追踪；@shadcn/lint 的 <code>require-static-classes</code> 规则正是为了标出这类情况。Lint 也管不了层级、节奏和审美，所以它是减少审阅工作，而不是取代审阅。</p>
<h2>清单：把设计系统检查放进智能体循环</h2>
<ol><li><strong>先跑一次基线。</strong>不做任何配置先检查现有应用（React 项目用 <code>npx -y onsystem check .</code>，或按 @shadcn/lint 的快速上手），按规则统计问题数，就知道智能体和人已经在哪里跑偏。</li>
<li><strong>写策略，而不只是 Token。</strong>为每个核心组件决定调用方能改什么（布局、外边距、宽度），什么归组件自己（内边距、圆角、颜色）。把它写进 Lint 配置，让智能体收到报错，而不是写在没人看的 Wiki 里。</li>
<li><strong>让每条报错都能教人。</strong>优先选报错里直接点名该用哪个 Token、尺寸或变体的规则。只说「不允许」的报错，只会让智能体再猜一次。</li>
<li><strong>编辑时查，合并时也查。</strong>钩子或 MCP 工具让智能体在工作中守规矩；同样的规则放进 CI，兜住漏网的修改，包括人写的。</li>
<li><strong>禁止读不懂的写法。</strong>打开拒绝动态拼接类名的规则，别让 Lint 的盲区变成智能体最爱的后门。</li>
<li><strong>Lint 太吵时，修系统。</strong>智能体反复去找一个不存在的变体，说明设计系统有缺口。照两款工具的建议，有意识地补上它，而不是放宽规则。</li>
<li><strong>像素还是要看。</strong>Lint 全绿只说明零件合法，不说明画面好看。层级、疏密和各种状态，仍要留一道视觉检查。</li></ol>
<pre><code># 1. 先看现在哪里跑偏（React，无需安装）
npx -y onsystem check .

# 2. 或让智能体配置 shadcn 的 Lint 工具
"Read https://github.com/shadcn-ui/lint/blob/main/SETUP.md
 and set up @shadcn/lint in this project."

# 3. 一条策略：Button 自己管尺寸和形状
"shadcn/no-restyle": ["error", { allow: ["layout"] }]

# 4. 每个拉取请求跑同样的规则
- uses: dgesteves/onsystem@v0</code></pre>
<h2>UI Hub 能帮什么</h2>
<p>Lint 只能执行已经存在的选择。如果你还在定义这些选择，可以先看<a href="../design-tokens-for-agents/">给智能体的设计 Token</a>和<a href="../component-composition/">组件组合</a>，再用<a href="../claude-cursor-design-skills/">Claude 和 Cursor 的设计技能</a>搭好说明层。这篇补上缺失的第三步：智能体知道规则之后，检查它有没有守住。</p>""",
 refs=[('I built three open-source tools for coding agents: onsystem, ondocs and signoff-ui','Diogo Esteves, DEV Community','https://dev.to/dgesteves/i-built-three-open-source-tools-for-coding-agents-onsystem-ondocs-and-signoff-ui-2ho7'),('onsystem: keeps coding agents on your design system','onsystem','https://onsystem.vercel.app/'),('Benchmark: coding agents with and without onsystem','onsystem','https://onsystem.vercel.app/benchmark'),('Rules','onsystem','https://onsystem.vercel.app/rules'),('onsystem repository','GitHub (dgesteves)','https://github.com/dgesteves/onsystem'),('@shadcn/lint: write design system rules that agents can verify','shadcn (GitHub)','https://github.com/shadcn-ui/lint'),('Build by design: New workflows for new ways of building','Figma (Dylan Field)','https://www.figma.com/blog/build-by-design/'),("What's new from Config India 2026",'Figma Learn','https://help.figma.com/hc/en-us/articles/43663368947863-What-s-new-from-Config-India-2026'),("Figma's new system check finds the hover state nobody drew",'Art Direction Daily','https://artdirectiondaily.com/issues/2026-10-16-figma-check-finds-missing-hover.html')]),
dict(slug='ai-svg-for-ui-ideogram-vector', date='2026-10-23', cat='tools', series=None, featured=True, tags=['Ideogram Vector 1.0','Recraft','QuiverAI Arrow','SVG','icons'],
 t=T('AI vectors for UI: what Ideogram Vector 1.0 changes, and the checks before an SVG ships','给界面用的 AI 矢量图：Ideogram Vector 1.0 改变了什么，SVG 上线前要查什么','給介面用的 AI 向量圖：Ideogram Vector 1.0 改變了什麼，SVG 上線前要查什麼','UIのためのAIベクター：Ideogram Vector 1.0で何が変わり、SVGを出す前に何を確認するか','UI를 위한 AI 벡터: Ideogram Vector 1.0이 바꾼 것과 SVG 배포 전 점검할 것','Vektor AI untuk UI: apa yang diubah Ideogram Vector 1.0, dan semakan sebelum SVG dihantar','Vector AI cho UI: Ideogram Vector 1.0 thay đổi gì và cần kiểm tra gì trước khi đưa SVG lên','Des vecteurs IA pour l’UI : ce que change Ideogram Vector 1.0, et les vérifications avant de livrer un SVG','Vectores con IA para la UI: qué cambia Ideogram Vector 1.0 y qué revisar antes de publicar un SVG','KI-Vektoren für UI: was Ideogram Vector 1.0 ändert und was vor dem Ausliefern einer SVG zu prüfen ist'),
 s=T('On 22 October Ideogram shipped Vector 1.0, a model that writes editable SVG from a prompt or traces an image, joining Recraft V4.1 and QuiverAI Arrow 2. Editable is not the same as ready for an interface: what the three tools actually return, and a checklist for icons and illustrations.',
     '10 月 22 日，Ideogram 发布 Vector 1.0：根据提示词直接生成可编辑的 SVG，也能把图片描成矢量，与 Recraft V4.1、QuiverAI Arrow 2 站到了一起。可编辑不等于能直接放进界面：三款工具实际给出什么，附一份图标和插画的检查清单。',
     '10 月 22 日，Ideogram 發布 Vector 1.0：根據提示詞直接生成可編輯的 SVG，也能把圖片描成向量，與 Recraft V4.1、QuiverAI Arrow 2 站到了一起。可編輯不等於能直接放進介面：三款工具實際給出什麼，附一份圖示和插畫的檢查清單。',
     '10月22日、IdeogramはVector 1.0を公開した。プロンプトから編集可能なSVGを生成し、画像をベクター化もできるモデルで、Recraft V4.1やQuiverAI Arrow 2に並ぶ。編集可能とUIにそのまま使えるは別物。3つのツールが実際に返すものと、アイコン・イラスト用チェックリスト。',
     '10월 22일 Ideogram이 Vector 1.0을 내놓았다. 프롬프트로 편집 가능한 SVG를 만들고 이미지를 벡터로 변환하는 모델로, Recraft V4.1·QuiverAI Arrow 2와 나란히 섰다. 편집 가능하다는 것과 UI에 바로 쓸 수 있다는 것은 다르다. 세 도구가 실제로 내놓는 것과 아이콘·일러스트 체크리스트.',
     'Pada 22 Okt, Ideogram melancarkan Vector 1.0, model yang menulis SVG boleh sunting daripada prompt atau menjejak imej, menyertai Recraft V4.1 dan QuiverAI Arrow 2. Boleh disunting tidak sama dengan sedia untuk antara muka: apa yang sebenarnya dihasilkan ketiga-tiga alat, dan senarai semak untuk ikon dan ilustrasi.',
     'Ngày 22/10, Ideogram ra mắt Vector 1.0, mô hình tạo SVG chỉnh sửa được từ prompt hoặc chuyển ảnh thành vector, đứng cạnh Recraft V4.1 và QuiverAI Arrow 2. Chỉnh sửa được chưa có nghĩa là dùng ngay trong giao diện: ba công cụ thực sự trả về gì, kèm checklist cho icon và minh hoạ.',
     'Le 22 octobre, Ideogram a lancé Vector 1.0, un modèle qui produit un SVG modifiable à partir d’un prompt ou vectorise une image, aux côtés de Recraft V4.1 et QuiverAI Arrow 2. Modifiable ne veut pas dire prêt pour une interface : ce que renvoient vraiment les trois outils, et une checklist pour icônes et illustrations.',
     'El 22 de octubre Ideogram lanzó Vector 1.0, un modelo que genera SVG editable a partir de un prompt o vectoriza una imagen, junto a Recraft V4.1 y QuiverAI Arrow 2. Editable no significa listo para una interfaz: qué devuelven de verdad las tres herramientas y una lista de revisión para iconos e ilustraciones.',
     'Am 22. Oktober brachte Ideogram Vector 1.0 heraus, ein Modell, das aus einem Prompt editierbare SVG erzeugt oder Bilder vektorisiert, neben Recraft V4.1 und QuiverAI Arrow 2. Editierbar heißt nicht fertig für eine Oberfläche: was die drei Tools wirklich liefern, plus Checkliste für Icons und Illustrationen.'),
 en="""<p>Most AI images reach an interface as a flat PNG: fine for a hero photo, useless for an icon that has to follow your theme colour, an empty-state illustration that must stay sharp on a 3x screen, or a logo you will resize forty times. On 22 October Ideogram launched Vector 1.0, its first model that returns SVG instead of pixels. It joins Recraft V4.1 and QuiverAI's Arrow 2, which already generate vectors. With three serious options, the question for UI work is no longer whether AI can draw a vector, but what it takes to make one ship.</p>
<h2>What shipped, and what the three tools return</h2>
<ul><li><strong>Ideogram Vector 1.0 (22 October).</strong> Two jobs under one model: text-to-vector, with optional reference images, three quality levels and a seed, and image-to-vector, which traces a JPEG, PNG or WebP up to 50 MB. It runs in the Ideogram app, through the API, and on partner platforms such as fal from day one. Ideogram pitches it for logos, wordmarks, print, labels, stickers and illustrations, and says each shape arrives as its own element you can recolour, move or resize. API prices on the product page run from $0.13 to $0.20 per SVG by quality ($0.32 at high quality with references) and $0.10 per image-to-vector conversion. One caveat from an early reading of the API reference: the vectorizer's layer-grouping option is listed as not yet available, so a traced image comes back as paths rather than neatly named groups. Its two modes trade fidelity against shape count: default keeps fine detail, simple draws fewer, cleaner shapes.</li>
<li><strong>Recraft V4.1.</strong> Generates SVG from a prompt for logos, icons and illustrations, converts raster images, and has a vector editor in Recraft Studio where you can move points, add tangents and recolour without leaving the canvas. Its docs note that the vector generation type does not take reference images.</li>
<li><strong>QuiverAI Arrow 2.</strong> A generally available model that does SVG generation, vectorization, editing and animation in one place, priced per token ($4 input and $20 output per million), with a larger Arrow 2 Telos at 50% higher rates. A third-party guide to it recommends prompts that name hex colours and one outline weight, say the drawing must read at 32 px, and rule out gradients, text and shadows, and notes that it is not meant for photographs.</li></ul>
<p>The same day, Canva released Craft, its first image model, which writes a plan of the composition before rendering and uses that plan to turn images into editable layers. It still outputs pixels, but it points the same way: generated visuals are starting to arrive as structure you can edit, not a picture you have to redraw.</p>
<h2>Our take</h2>
<p>For interfaces, editable is necessary but not enough. An icon that works in a product is a contract: a fixed grid (usually 24 by 24), one stroke weight across the set, colour taken from the surrounding text so it follows light and dark themes, a small file, and a clear role for screen readers. Generators optimise for a picture that looks good at full size. Nothing in the launches suggests they target those rules, so treat their output like a strong first draft from an illustrator who has never seen your icon set. The biggest win is in the middle of the range: empty states, onboarding spots, marketing illustrations and logo exploration, where a vector you can recolour to your tokens beats a PNG you cannot. For the core icon set, a maintained open library is still the safer default, with AI filling the gaps it does not cover.</p>
<p>Two practical warnings. Traced artwork can carry thousands of anchor points, which bloats pages and makes hand edits painful, so prefer the simple mode or a fresh generation for UI assets. And check the licence and output privacy for your plan before you put a generated mark into a product; Ideogram's docs say outputs are private by default, but terms differ between tools and tiers.</p>
<h2>Checklist: getting an AI SVG ready for an interface</h2>
<ol><li><strong>Prompt for the system, not the picture.</strong> Give the grid size, stroke weight, cap style, fill or no fill, the exact hex values from your tokens, and the smallest size it must read at. Ban gradients, text and shadows for icons.</li>
<li><strong>Generate the set together.</strong> Ask for several icons in one prompt, or reuse the seed and a reference, so weights and corner radii match. Mixed weights are the first thing users notice.</li>
<li><strong>Prefer generation over tracing for UI.</strong> Trace only when you must keep an existing drawing, and use the simplest mode that still looks right.</li>
<li><strong>Clean the file.</strong> Run it through an optimizer such as SVGO, keep the <code>viewBox</code>, drop editor metadata, and look at the path count before and after.</li>
<li><strong>Hand colour to CSS.</strong> For single-colour icons, replace fixed fills and strokes with <code>currentColor</code> so the icon follows text colour in both themes. For multicolour illustrations, map each colour to a CSS variable from your tokens.</li>
<li><strong>Give it the right role.</strong> Decorative icons next to a text label get <code>aria-hidden="true"</code>; a standalone meaningful graphic gets <code>role="img"</code> and a <code>&lt;title&gt;</code> or an accessible name on its button.</li>
<li><strong>Check it small and in both themes.</strong> View it at 16 and 24 px on light and dark backgrounds before you merge. If it only works large, it is an illustration, not an icon.</li></ol>
<pre><code># 1. prompt for a UI icon, not a poster
"Six 24 px line icons for a finance app: wallet, card,
 receipt, chart, bell, lock. 2 px stroke, round caps,
 no fill, one colour #111827, no text, no gradients.
 Each must read at 16 px."

# 2. clean the file
npx svgo wallet.svg -o wallet.min.svg

# 3. let CSS own the colour and the role
&lt;svg viewBox="0 0 24 24" fill="none"
     stroke="currentColor" aria-hidden="true"&gt;…&lt;/svg&gt;</code></pre>
<h2>How UI Hub helps</h2>
<p>A generated vector only fits if your tokens exist first. Our posts on <a href="../design-tokens-for-agents/">design tokens for agents</a> and <a href="../oklch-color-and-dark-mode/">OKLCH colour and dark mode</a> cover the colour side, and <a href="../layers-brand-kits-json-ai-visuals/">layers, brand kits and JSON</a> covers the same "editable, not flat" shift for raster images. For accessible names and roles, see <a href="../accessibility-in-ai-generated-ui/">accessibility in AI-generated UI</a>.</p>""",
 zh="""<p>大多数 AI 图片进入界面时都是一张扁平的 PNG：放首屏照片没问题，但要做一个跟随主题色变化的图标、一张在 3 倍屏上也要清晰的空状态插画，或者一个要缩放几十次的 Logo，就派不上用场。10 月 22 日，Ideogram 发布 Vector 1.0，这是它第一个直接输出 SVG、而不是像素的模型。在它之前，Recraft V4.1 和 QuiverAI 的 Arrow 2 已经能生成矢量图。三个像样的选择摆在一起，对界面设计来说，问题已经不是 AI 能不能画矢量，而是怎样才能让它真正上线。</p>
<h2>发布了什么，三款工具实际给出什么</h2>
<ul><li><strong>Ideogram Vector 1.0（10 月 22 日）。</strong>一个模型做两件事：文生矢量，可附参考图，有三档质量和种子；图转矢量，可描摹 50 MB 以内的 JPEG、PNG 或 WebP。可以在 Ideogram 应用、API 里用，首日也上了 fal 等合作平台。Ideogram 主打 Logo、字标、印刷品、标签、贴纸和插画，并称每个形状都是独立元素，可以单独改色、移动或缩放。产品页上的 API 价格按质量为每张 SVG 0.13 到 0.20 美元（高质量加参考图 0.32 美元），图转矢量每张 0.10 美元。有一点要留意：按早期对 API 文档的解读，描摹接口的图层分组选项标为「暂不可用」，所以描出来的是一堆路径，而不是命名好的分组。它的两种模式在细节和形状数量之间取舍：默认模式保留细节，简洁模式画得更少、更干净。</li>
<li><strong>Recraft V4.1。</strong>可根据提示词为 Logo、图标和插画生成 SVG，也能把位图转成矢量；Recraft Studio 里有矢量编辑器，可以直接在画布上移动锚点、加切线、改颜色。文档注明，矢量生成类型不支持参考图。</li>
<li><strong>QuiverAI Arrow 2。</strong>已正式可用，一个模型同时做 SVG 生成、矢量化、编辑和动画，按 token 计价（每百万输入 4 美元、输出 20 美元），更强的 Arrow 2 Telos 费率高 50%。一份第三方使用指南建议：提示词里写明十六进制颜色和统一描边粗细，说明要在 32 px 下仍能看清，并排除渐变、文字和阴影；也提到它不适合照片类内容。</li></ul>
<p>同一天，Canva 发布了第一个自研图像模型 Craft：先写出画面构图的规划，再渲染，并借助这份规划把图片转成可编辑图层。它输出的仍是像素，但方向一致：生成的视觉开始以「可编辑的结构」交到你手上，而不是一张只能重画的图。</p>
<h2>我们的看法</h2>
<p>对界面来说，可编辑是必要条件，但不够。产品里能用的图标是一份契约：固定网格（通常 24×24），整套统一的描边粗细，颜色取自周围文字以便跟随亮暗主题，文件小，并且对读屏软件有明确的角色。生成器优化的是「全尺寸下好看的一张图」，从发布信息看，它们并没有瞄准这些规则。所以要把它们的产出当成一位没见过你图标库的插画师交来的好初稿。收益最大的是中间地带：空状态、引导页插画、营销插画和 Logo 探索，在这些地方，能按 Token 改色的矢量图远胜一张改不了的 PNG。至于核心图标集，持续维护的开源图标库仍是更稳的默认选择，AI 用来补它没有的那几个。</p>
<p>两点实际提醒。描摹出来的图可能带着成千上万个锚点，既拖慢页面，也让手动修改很痛苦；界面素材优先用简洁模式，或者干脆重新生成。另外，把生成的标志放进产品之前，先确认你所用套餐的授权和输出隐私条款；Ideogram 文档说输出默认私有，但各工具、各档位的条款并不相同。</p>
<h2>清单：让 AI 生成的 SVG 能放进界面</h2>
<ol><li><strong>按系统写提示词，而不是按画面。</strong>写明网格尺寸、描边粗细、端点样式、填充与否、Token 里的准确十六进制色值，以及最小要在多大尺寸下看清。图标要禁止渐变、文字和阴影。</li>
<li><strong>整套一起生成。</strong>在一条提示里要多个图标，或复用同一个种子和参考图，让粗细和圆角一致。粗细不统一是用户最先注意到的问题。</li>
<li><strong>界面素材优先生成，少用描摹。</strong>只有必须保留现有画稿时才描摹，并选仍然好看的最简模式。</li>
<li><strong>清理文件。</strong>用 SVGO 之类的优化器跑一遍，保留 <code>viewBox</code>，删掉编辑器元数据，对比清理前后的路径数。</li>
<li><strong>把颜色交给 CSS。</strong>单色图标把写死的 fill 和 stroke 换成 <code>currentColor</code>，让它在两套主题里都跟随文字颜色；多色插画把每种颜色映射到 Token 里的 CSS 变量。</li>
<li><strong>给它正确的角色。</strong>旁边有文字标签的装饰性图标加 <code>aria-hidden="true"</code>；单独表达含义的图形加 <code>role="img"</code> 和 <code>&lt;title&gt;</code>，或给所在按钮一个无障碍名称。</li>
<li><strong>小尺寸、双主题都看一遍。</strong>合并前在亮色和暗色背景上，分别以 16 px 和 24 px 查看。只有放大才好看的，是插画，不是图标。</li></ol>
<pre><code># 1. 按界面图标写提示词，而不是海报
"Six 24 px line icons for a finance app: wallet, card,
 receipt, chart, bell, lock. 2 px stroke, round caps,
 no fill, one colour #111827, no text, no gradients.
 Each must read at 16 px."

# 2. 清理文件
npx svgo wallet.svg -o wallet.min.svg

# 3. 让 CSS 管颜色和角色
&lt;svg viewBox="0 0 24 24" fill="none"
     stroke="currentColor" aria-hidden="true"&gt;…&lt;/svg&gt;</code></pre>
<h2>UI Hub 能帮什么</h2>
<p>生成的矢量图要先有 Token 才对得上。配色部分可以看<a href="../design-tokens-for-agents/">给智能体的设计 Token</a>和 <a href="../oklch-color-and-dark-mode/">OKLCH 配色与暗色模式</a>；<a href="../layers-brand-kits-json-ai-visuals/">图层、品牌包与 JSON</a> 讲的是位图领域同样的「可编辑而非扁平」转向。无障碍名称和角色，参见 <a href="../accessibility-in-ai-generated-ui/">AI 生成界面的无障碍</a>。</p>""",
 refs=[('Ideogram Vector: ready-to-use SVG artwork','Ideogram','https://ideogram.ai/models/vector/'),('Ideogram launches its first vector model for editable SVG design','Ryan Merket, Runtime Wire','https://runtimewire.com/article/ideogram-vector-1-svg-model-launch'),('Ideogram Vector 1.0: Editable SVGs with an API layer caveat','OrcaRouter blog','https://www.orcarouter.ai/blog/ideogram-vector-1-0-release-editable-svg'),('Ideogram Vector 1.0: Editable SVGs from a prompt','ArtRealmAI','https://artrealmai.com/article/ideogram-vector-1-0-editable-svg-text-image-to-vector'),('Ideogram Vector text-to-vector API','fal','https://fal.ai/models/ideogram/vector/text-to-vector/api'),('AI vector generator: text to SVG','Recraft','https://www.recraft.ai/ai-vector-generator'),('Vector Editor','Recraft docs','https://www.recraft.ai/docs/recraft-studio/image-editing/vector-editor'),('Arrow 2','QuiverAI','https://quiver.ai/models/arrow-2/'),('Models','QuiverAI docs','https://docs.quiver.ai/developers/models'),('Arrow','Batch Banana docs','https://batchbanana.com/docs/models/arrow'),('Introducing Canva Craft','Canva Newsroom','https://www.canva.com/newsroom/news/canva-craft/'),('Canva releases its first image generation model','Ivan Mehta, TechCrunch','https://techcrunch.com/2026/10/22/canva-releases-its-first-image-generation-model/'),('SVGO','SVGO','https://svgo.dev/'),('Decorative images','W3C WAI','https://www.w3.org/WAI/tutorials/images/decorative/')]),
dict(slug='agent-approval-ui-budgets-interruptions', date='2026-10-26', cat='agents', series=None, featured=True, tags=['agent UX','approvals','Walmart Agent Profiles','Claude Duet','1Password for Agents'],
 t=T('Designing approvals for agents that act for people: budgets, previews and when to interrupt','为替人办事的智能体设计审批：预算、预览，以及什么时候打扰用户','為替人辦事的智慧體設計審批：預算、預覽，以及什麼時候打擾使用者','人の代わりに動くエージェントの承認設計：予算、プレビュー、そして割り込むタイミング','사람 대신 일하는 에이전트의 승인 설계: 예산, 미리보기, 그리고 끼어들 때','Mereka bentuk kelulusan untuk ejen yang bertindak bagi pihak orang: bajet, pratonton dan bila perlu mengganggu','Thiết kế phê duyệt cho agent làm thay người dùng: ngân sách, xem trước và khi nào nên làm phiền','Concevoir les validations des agents qui agissent pour nous : budgets, aperçus et moment d’interrompre','Diseñar aprobaciones para agentes que actúan por las personas: presupuestos, vistas previas y cuándo interrumpir','Freigaben für Agents gestalten, die für Menschen handeln: Budgets, Vorschauen und wann man stört'),
 s=T('In one week Walmart announced Agent Profiles with spending limits, Anthropic opened Claude Duet, which asks before it sends, pays, signs or deletes, and 1Password shipped approvals for agent sign-ins. Together they sketch a shared pattern for agent permission UI: what each one shipped, our take, and a checklist for your own product.',
     '一周之内，Walmart 公布了带消费上限的 Agent Profiles，Anthropic 开放了在发送、付款、签署或删除前都会先问你的 Claude Duet，1Password 也上线了智能体登录审批。三者拼出了一套智能体授权界面的共同模式：它们各自发布了什么，我们的看法，以及一份可用于你自己产品的清单。',
     '一週之內，Walmart 公布了帶消費上限的 Agent Profiles，Anthropic 開放了在傳送、付款、簽署或刪除前都會先問你的 Claude Duet，1Password 也上線了智慧體登入審批。三者拼出了一套智慧體授權介面的共同模式：它們各自發布了什麼，我們的看法，以及一份可用於你自己產品的清單。',
     '1週間のうちに、Walmartは支出上限付きのAgent Profilesを発表し、Anthropicは送信・支払い・署名・削除の前に必ず確認するClaude Duetを公開し、1Passwordはエージェントのサインイン承認を出した。3つを並べるとエージェント権限UIの共通パターンが見える。各社の内容、私たちの見解、自社プロダクト用チェックリスト。',
     '일주일 사이에 Walmart는 지출 한도가 있는 Agent Profiles를 발표했고, Anthropic은 보내기·결제·서명·삭제 전에 먼저 묻는 Claude Duet을 열었으며, 1Password는 에이전트 로그인 승인을 내놓았다. 셋을 합치면 에이전트 권한 UI의 공통 패턴이 보인다. 각자 내놓은 것, 우리의 견해, 내 제품용 체크리스트.',
     'Dalam seminggu, Walmart mengumumkan Agent Profiles dengan had perbelanjaan, Anthropic membuka Claude Duet yang bertanya sebelum menghantar, membayar, menandatangani atau memadam, dan 1Password melancarkan kelulusan log masuk ejen. Bersama-sama ia melakar corak UI kebenaran ejen: apa yang dilancarkan, pandangan kami dan senarai semak untuk produk anda.',
     'Trong một tuần, Walmart công bố Agent Profiles có hạn mức chi tiêu, Anthropic mở Claude Duet luôn hỏi trước khi gửi, thanh toán, ký hay xoá, và 1Password ra mắt phê duyệt đăng nhập cho agent. Gộp lại, chúng phác ra một mẫu chung cho UI cấp quyền agent: mỗi bên ra mắt gì, nhận định của chúng tôi và checklist cho sản phẩm của bạn.',
     'En une semaine, Walmart a annoncé Agent Profiles avec plafonds de dépense, Anthropic a ouvert Claude Duet, qui demande avant d’envoyer, payer, signer ou supprimer, et 1Password a lancé la validation des connexions d’agents. Ensemble, ils dessinent un modèle commun d’UI de permissions : ce que chacun a lancé, notre avis et une checklist pour votre produit.',
     'En una semana, Walmart anunció Agent Profiles con límites de gasto, Anthropic abrió Claude Duet, que pregunta antes de enviar, pagar, firmar o borrar, y 1Password lanzó aprobaciones para los inicios de sesión de agentes. Juntos esbozan un patrón común de UI de permisos: qué lanzó cada uno, nuestra opinión y una lista de revisión para tu producto.',
     'Innerhalb einer Woche kündigte Walmart Agent Profiles mit Ausgabenlimits an, Anthropic öffnete Claude Duet, das vor Senden, Bezahlen, Unterschreiben oder Löschen fragt, und 1Password brachte Freigaben für Agent-Logins. Zusammen skizzieren sie ein gemeinsames Muster für Agent-Berechtigungs-UI: was jeweils kam, unsere Einschätzung und eine Checkliste für dein Produkt.'),
 en="""<p>Most agent interfaces still have one permission model: the agent can do everything the person can, because it signs in as them. That worked while agents mostly read and drafted. It stops working the moment they buy, send and sign. In the week of 21 October three launches, from a retailer, a model lab and a password manager, each shipped a different piece of the same answer. Read together, they are the clearest picture yet of what a permission screen for an agent should look like.</p>
<h2>What shipped</h2>
<ul><li><strong>Walmart Agent Profiles (announced 21 October, launching within a month).</strong> Today an agent shopping on Walmart signs in with the customer's account, so its orders are mixed in with theirs. Agent Profiles give each agent its own profile inside the account, with its purchases listed separately. By default every agent purchase needs approval; the customer can instead allow spending up to a limit such as $50, $100 or $200, and Walmart says it may still ask for approval inside that limit. Profiles can be turned off or deleted at any time. Under the new terms, agents never receive card details, cannot add or change payment methods, and may only use the information a task needs. A beta Agent Gateway connects agents over MCP and, in Walmart's example, helps an agent find your usual milk without handing over your whole shopping history.</li>
<li><strong>Claude Duet (research preview, 21 October).</strong> Anthropic's proactive agent sends a morning brief, checks connected apps every few hours rather than continuously, and messages you only when something needs your attention; you can tell it what you want to hear about and how often. It reads, drafts and prepares work on its own, but before it sends a message, makes a payment, signs a document or deletes anything, it shows exactly what it is about to do and waits. Some actions, such as trading securities or moving money between accounts, stay off-limits even with approval, and any connected app can be disconnected. Anthropic says the preview may still misjudge what is urgent and cannot yet show you its browser.</li>
<li><strong>1Password for Agents (October).</strong> When an agent hits a sign-in form, 1Password shows a prompt naming which agent is asking and suggesting a login; you approve on your own device, and 1Password fills the form without the credential ever reaching the agent. Its Claude integration goes further: there are no standing approvals, so a new agent session means a new prompt, and released credentials expire with the session.</li></ul>
<p>One early hands-on review of Duet, by Claire Vo and summarised in the FocusHeron <em>AI and Designers</em> newsletter, adds the human side: a proactive agent needs a deliberate rule for when it may interrupt, and slow responses quickly erode the willingness to work with it in real time.</p>
<h2>Our take</h2>
<p>The three launches agree on more than they differ, and the agreement is a design pattern rather than a security feature. Autonomy is not one switch; it is a setting per action type, with four rungs. Some actions are <strong>never</strong> allowed. Consequential ones are <strong>asked every time</strong> by default. Routine ones can run <strong>within a budget</strong> the person chose. Everything the agent did is <strong>visible afterwards</strong> in its own ledger, separate from what the person did. The approval itself has to be a preview of the exact action, not a generic "Allow?" dialog: Duet's "shows you exactly what it is about to do" and 1Password's "which agent is asking, for which login" are the two halves of a good approval card.</p>
<p>The quieter lesson is about attention. A permission model that asks for everything trains people to tap Approve without reading, which is worse than no approval at all. Duet's few-hours check-in and per-topic notification settings, and Walmart's budget tier, both exist to reduce how often the person is asked, so that the remaining questions get read. If your product adds agent actions, design the interruption budget at the same time as the spending budget.</p>
<h2>Checklist: an approval UI for agent actions</h2>
<ol><li><strong>Give each agent its own identity.</strong> Show its name and icon on every request and on every action in history, never the person's avatar.</li>
<li><strong>Classify actions before you design screens.</strong> Read, draft, act within budget, act with approval, never. Write the list down; it is your permission spec.</li>
<li><strong>Default consequential actions to "ask".</strong> Sending, paying, signing, deleting and changing account settings start in the ask tier; the person can loosen it later, per agent.</li>
<li><strong>Make the approval card a preview.</strong> Show the exact recipient and text, item and price, or file and change, plus who is asking and why. Offer Approve, Edit and Deny, and make Deny as easy to hit as Approve.</li>
<li><strong>Budgets in the person's units.</strong> Money per purchase or per week, messages per day, or recipients outside the team. Show the remaining budget on the card and in settings.</li>
<li><strong>Keep a separate ledger.</strong> Agent actions get their own list with filters, an undo or return path where one exists, and a one-tap way to pause or remove the agent.</li>
<li><strong>Set an interruption rule.</strong> Batch low-stakes items into a brief, interrupt only for blocked or time-critical work, and let people choose topics and frequency.</li>
<li><strong>No standing secrets.</strong> Never paste credentials into the agent's context; hand sign-in to a credential manager and expire access with the session.</li>
<li><strong>Make the approval accessible.</strong> A blocking approval is an <code>alertdialog</code> with a clear title, focus on the safest option, and text a screen reader can read in full.</li></ol>
<pre><code># agent-permissions.yml: a starting spec
agent: "Shopping assistant"
never:    [change_payment_method, move_money, trade]
ask:      [send_message, purchase_over_budget, sign, delete]
budget:   { purchase: "$100 / week", messages: "10 / day" }
auto:     [read, search, draft, add_to_cart]
notify:   { brief: "08:00", interrupt: [blocked, deadline_today] }
ledger:   separate_from_owner
session:  { credentials: via_password_manager, expire: on_end }</code></pre>
<h2>How UI Hub helps</h2>
<p>The building blocks for this UI already exist. Our post on <a href="../shadcn-trace-and-ai-elements/">shadcn Trace and AI Elements</a> covers the Confirmation and Tool patterns that an approval card can be built from, and <a href="../accessibility-in-ai-generated-ui/">accessibility in AI-generated UI</a> covers focus and dialog roles. For making the agent itself follow your rules while it builds screens like these, see <a href="../lint-agents-onto-your-design-system/">linting agents onto your design system</a>.</p>""",
 zh="""<p>大多数智能体界面至今只有一种授权方式：智能体用你的账号登录，所以你能做的它全都能做。在智能体主要负责阅读和起草时，这样还行；一旦它开始买东西、发消息、签文件，就不行了。10 月 21 日那一周，一家零售商、一家模型公司和一家密码管理器各自发布了同一个答案的不同部分。把三者放在一起看，是迄今最清楚的一张图：给智能体的授权界面应该长什么样。</p>
<h2>发布了什么</h2>
<ul><li><strong>Walmart Agent Profiles（10 月 21 日公布，一个月内上线）。</strong>现在智能体在 Walmart 购物时用的是顾客的账号，它下的单和顾客自己的订单混在一起。Agent Profiles 让每个智能体在账号里拥有自己的资料页，它的购买记录单独列出。默认情况下智能体每次购买都需要批准；顾客也可以改成允许它在某个额度内消费，例如 50、100 或 200 美元，Walmart 表示即便在额度内也可能再要求确认。资料页可以随时关闭或删除。按新条款，智能体拿不到银行卡信息，不能添加或修改支付方式，只能使用任务所需的信息。测试中的 Agent Gateway 通过 MCP 连接智能体；按 Walmart 举的例子，它能帮智能体找到你常买的牛奶，而不把你的全部购物记录交出去。</li>
<li><strong>Claude Duet（10 月 21 日开放研究预览）。</strong>Anthropic 的主动型智能体每天早上发一份简报，每隔几小时（而不是持续不断地）检查已连接的应用，只在有事需要你处理时才发消息；你可以告诉它想听哪些事、多久一次。它会自己阅读、起草和准备工作，但在发送消息、付款、签署文件或删除任何东西之前，会把它准备做的事原样展示给你，等你批准。有些操作即使你批准也不允许，比如交易证券或在账户之间转账；任何已连接的应用都可以断开。Anthropic 也说明，预览版仍可能误判轻重缓急，暂时还不能让你看到它的浏览器。</li>
<li><strong>1Password for Agents（10 月）。</strong>智能体遇到登录表单时，1Password 会弹出提示，写明是哪个智能体在请求，并推荐一条登录项；你在自己的设备上批准，1Password 直接填表，凭据从不经过智能体。它与 Claude 的集成更进一步：没有长期有效的批准，新的智能体会话就要重新确认，放出的凭据随会话结束而失效。</li></ul>
<p>FocusHeron 的《AI and Designers》通讯汇总了 Claire Vo 对 Duet 的早期上手评测，补上了人的一面：主动型智能体需要一条明确的「什么时候可以打扰」规则，而响应慢会迅速消磨人们实时与它协作的意愿。</p>
<h2>我们的看法</h2>
<p>这三次发布的共同点比分歧多，而且共同点是一种设计模式，不只是安全功能。自主权不是一个开关，而是按操作类型分别设置的四级阶梯：有些操作<strong>永不允许</strong>；有后果的操作默认<strong>每次都问</strong>；日常操作可以在用户选定的<strong>预算内自动执行</strong>；智能体做过的一切都要在它自己的记录里<strong>事后可查</strong>，和用户本人的操作分开。审批本身必须是对具体操作的预览，而不是一个笼统的「允许吗？」对话框：Duet 的「把准备做的事原样展示给你」和 1Password 的「哪个智能体、要用哪条登录」，正好是一张好审批卡片的两半。</p>
<p>更安静的一课关于注意力。什么都要问的授权模型，会把人训练成不看内容就点「批准」，这比没有审批还糟。Duet 几小时一次的检查、按话题设置的通知，以及 Walmart 的预算档位，都是为了减少打扰次数，让剩下的那些问题真正被读到。如果你的产品要加智能体操作，请把「打扰预算」和「消费预算」一起设计。</p>
<h2>清单：为智能体操作设计审批界面</h2>
<ol><li><strong>给每个智能体独立身份。</strong>每次请求、历史里的每条操作，都显示它的名字和图标，而不是用户本人的头像。</li>
<li><strong>先给操作分级，再画界面。</strong>阅读、起草、预算内执行、需批准执行、永不允许。把这份清单写下来，它就是你的授权规格。</li>
<li><strong>有后果的操作默认「先问」。</strong>发送、付款、签署、删除、修改账号设置都从「先问」档开始，之后用户可以按智能体逐个放宽。</li>
<li><strong>审批卡片要做成预览。</strong>写明确切的收件人和正文、商品和价格，或文件和改动，以及是谁在请求、为什么。提供批准、编辑、拒绝三个选项，拒绝要和批准一样容易点到。</li>
<li><strong>预算用用户熟悉的单位。</strong>每笔或每周金额、每天消息数、团队外收件人数量。在卡片和设置里都显示剩余额度。</li>
<li><strong>单独的操作记录。</strong>智能体的操作单独成列，可筛选；能撤销或退货的提供入口，并提供一键暂停或移除该智能体。</li>
<li><strong>定一条打扰规则。</strong>低风险事项合并进简报，只在受阻或有时效时打断，并让用户自己选择话题和频率。</li>
<li><strong>不留长期密钥。</strong>永远不要把凭据贴进智能体的上下文；登录交给密码管理器，访问权限随会话结束失效。</li>
<li><strong>审批要无障碍。</strong>阻断式审批用 <code>alertdialog</code>，标题清楚，焦点落在最安全的选项上，正文读屏软件能完整读出。</li></ol>
<pre><code># agent-permissions.yml：一份起步规格
agent: "Shopping assistant"
never:    [change_payment_method, move_money, trade]
ask:      [send_message, purchase_over_budget, sign, delete]
budget:   { purchase: "$100 / week", messages: "10 / day" }
auto:     [read, search, draft, add_to_cart]
notify:   { brief: "08:00", interrupt: [blocked, deadline_today] }
ledger:   separate_from_owner
session:  { credentials: via_password_manager, expire: on_end }</code></pre>
<h2>UI Hub 能帮什么</h2>
<p>搭这种界面的积木已经有了。<a href="../shadcn-trace-and-ai-elements/">shadcn Trace 与 AI Elements</a> 一文介绍了可用来拼审批卡片的 Confirmation 和 Tool 模式；<a href="../accessibility-in-ai-generated-ui/">AI 生成界面的无障碍</a>讲了焦点和对话框角色。想让智能体在搭这类界面时遵守你的规范，可以看<a href="../lint-agents-onto-your-design-system/">用 Lint 把智能体拉回你的设计系统</a>。</p>""",
 refs=[('Making it possible for agents to shop on behalf of customers','Walmart','https://corporate.walmart.com/news/2026/10/Making-It-Possible-for-Agents-to-Shop-on-Behalf-of-Customers'),('Walmart is inviting AI agents to shop for you','The Verge','https://www.theverge.com/ai-artificial-intelligence/1015715/walmart-ai-shopping-agents'),('Walmart will let AI agents shop for you, with their own spending limits','The Next Web','https://thenextweb.com/news/walmart-ai-agents-shop-agent-profiles'),('Walmart AI agent shopping: new controls and spending limits','Digital Commerce 360','https://www.digitalcommerce360.com/2026/10/23/walmart-unveils-ai-agent-shopping-controls-spending-limits/'),('Introducing Claude Duet','Anthropic','https://claude.com/resources/articles/claude-duet'),('Get started with Claude Duet','Claude Help Center','https://support.claude.com/en/articles/17631495-get-started-with-claude-duet'),('Anthropic announces preview of Claude Duet','Ashley Capoot, CNBC','https://www.cnbc.com/2026/10/21/anthropic-preview-of-claude-duet-personal-ai-agent-take-on-muse-dots.html'),('Use 1Password to sign in to sites with supported agents','1Password Support','https://support.1password.com/1password-for-agents/'),('1Password for Agents launches as the trust layer for personal AI agents','1Password','https://1password.com/press/2026/october/1password-for-agents-trust-layer-personal-ai-agents'),('About the security of 1Password for Claude','1Password Support','https://support.1password.com/1password-claude-security/'),('AI and Designers, issue 2 (25 October 2026)','FocusHeron','https://focusheron.com/n/agentic-for-designers/i/iss_974440f090eb494aaff677d12748be1e'),('AI Elements','shadcn/ui','https://ui.shadcn.com/docs/ai-elements'),('Alert and message dialogs pattern','W3C WAI-ARIA APG','https://www.w3.org/WAI/ARIA/apg/patterns/alertdialog/')]),
dict(slug='agents-drive-design-tools-framer-weave-app-studio', date='2026-10-27', cat='agents', series=None, featured=True, tags=['Framer MCP','Figma Weave','Runway App Studio','MCP','creative workflows'],
 t=T('Your design tools now take orders from agents: Framer MCP, Figma Weave and Runway App Studio','设计工具开始听智能体指挥：Framer MCP、Figma Weave 与 Runway App Studio','設計工具開始聽智慧體指揮：Framer MCP、Figma Weave 與 Runway App Studio','デザインツールがエージェントの指示で動き出す：Framer MCP、Figma Weave、Runway App Studio','디자인 도구가 에이전트의 지시를 받기 시작했다: Framer MCP, Figma Weave, Runway App Studio','Alat reka bentuk kini menerima arahan ejen: Framer MCP, Figma Weave dan Runway App Studio','Công cụ thiết kế bắt đầu nhận lệnh từ agent: Framer MCP, Figma Weave và Runway App Studio','Vos outils de design obéissent désormais aux agents : Framer MCP, Figma Weave et Runway App Studio','Tus herramientas de diseño ya reciben órdenes de agentes: Framer MCP, Figma Weave y Runway App Studio','Deine Design-Tools nehmen jetzt Aufträge von Agents an: Framer MCP, Figma Weave und Runway App Studio'),
 s=T('In five days Framer opened its canvas and CMS to outside agents over MCP, Figma made every Weave image and video model callable from the Figma MCP, and Runway turned plain-language descriptions into shareable creative apps. Three different ways to put a creative tool behind an agent, what each one gates, our take, and a checklist for setting it up safely.',
     '五天之内，Framer 通过 MCP 把画布和 CMS 开放给外部智能体，Figma 让 Weave 的所有图像和视频模型都能从 Figma MCP 调用，Runway 则能把一段自然语言描述变成可分享的创作应用。这是把创作工具交给智能体的三种不同方式：各自在哪里设了关卡，我们的看法，以及一份安全上手清单。',
     '五天之內，Framer 透過 MCP 把畫布和 CMS 開放給外部智慧體，Figma 讓 Weave 的所有圖像和影片模型都能從 Figma MCP 呼叫，Runway 則能把一段自然語言描述變成可分享的創作應用。這是把創作工具交給智慧體的三種不同方式：各自在哪裡設了關卡，我們的看法，以及一份安全上手清單。',
     '5日間で、FramerはMCP経由でキャンバスとCMSを外部エージェントに開放し、FigmaはWeaveの画像・動画モデルをすべてFigma MCPから呼べるようにし、Runwayは自然文の説明を共有できるクリエイティブアプリに変えた。クリエイティブツールをエージェントに任せる3つの方法、それぞれの関門、私たちの見解、安全に始めるチェックリスト。',
     '닷새 사이에 Framer는 MCP로 캔버스와 CMS를 외부 에이전트에 열었고, Figma는 Weave의 모든 이미지·동영상 모델을 Figma MCP에서 호출할 수 있게 했으며, Runway는 자연어 설명을 공유 가능한 크리에이티브 앱으로 바꿨다. 크리에이티브 도구를 에이전트에 맡기는 세 가지 방식, 각각의 관문, 우리의 견해, 안전한 설정 체크리스트.',
     'Dalam lima hari, Framer membuka kanvas dan CMS kepada ejen luar melalui MCP, Figma menjadikan setiap model imej dan video Weave boleh dipanggil dari Figma MCP, dan Runway menukar penerangan bahasa biasa kepada aplikasi kreatif yang boleh dikongsi. Tiga cara meletakkan alat kreatif di belakang ejen, apa yang dikawal setiap satu, pandangan kami dan senarai semak persediaan yang selamat.',
     'Trong năm ngày, Framer mở canvas và CMS cho agent bên ngoài qua MCP, Figma cho phép gọi mọi mô hình ảnh và video của Weave từ Figma MCP, còn Runway biến mô tả bằng ngôn ngữ tự nhiên thành ứng dụng sáng tạo có thể chia sẻ. Ba cách đặt công cụ sáng tạo sau một agent, mỗi cách chặn ở đâu, nhận định của chúng tôi và checklist thiết lập an toàn.',
     'En cinq jours, Framer a ouvert son canevas et son CMS aux agents externes via MCP, Figma a rendu tous les modèles image et vidéo de Weave accessibles depuis le Figma MCP, et Runway transforme une description en langage courant en app créative partageable. Trois façons de confier un outil créatif à un agent, ce que chacune verrouille, notre avis et une checklist pour s’y mettre sans risque.',
     'En cinco días, Framer abrió su lienzo y su CMS a agentes externos por MCP, Figma hizo que todos los modelos de imagen y vídeo de Weave se puedan llamar desde el Figma MCP, y Runway convierte una descripción en lenguaje natural en una app creativa que se puede compartir. Tres formas de poner una herramienta creativa detrás de un agente, qué controla cada una, nuestra opinión y una lista para configurarlo con seguridad.',
     'Innerhalb von fünf Tagen öffnete Framer Canvas und CMS per MCP für externe Agents, Figma machte alle Bild- und Videomodelle von Weave über den Figma MCP aufrufbar, und Runway macht aus einer Beschreibung in Alltagssprache eine teilbare Kreativ-App. Drei Wege, ein Kreativ-Tool hinter einen Agent zu stellen, was jeder absichert, unsere Einschätzung und eine Checkliste für ein sicheres Setup.'),
 en="""<p>Until recently, an AI agent that wanted to change a website or produce a campaign image had two options: write code from scratch, or ask you to open the design tool yourself. Between 22 and 26 October three creative tools removed that gap in three different ways. Framer let outside agents edit its canvas and CMS, Figma let agents call Weave's image and video models through the Figma MCP, and Runway let anyone describe a creative app and get a working one. Each answers the same question, <em>what may an agent do inside my creative tool?</em>, with a different gate.</p>
<h2>What shipped</h2>
<ul><li><strong>Framer MCP (22 October).</strong> Any client that supports remote MCP servers and OAuth, such as Codex, Claude or Cursor, can connect to <code>https://mcp.framer.com/mcp</code>. After you approve the connection, the agent can create pages and edit layouts across desktop, tablet and phone breakpoints using the project's existing styles and components, manage CMS collections and items, and review metadata, headings and alt text. It acts with your account's permissions. Changes stay in the project, or on a branch, until someone publishes; the agent can publish, but only if you explicitly ask. Framer's branches show a diff under Review Changes, and applying a branch to main is a separate step from publishing main.</li>
<li><strong>Figma Weave through the Figma MCP (26 October).</strong> With a paid standalone Weave account linked to Figma, an external agent can run a Weave model such as Seedance, Kling or Nano Banana directly, or run a published Weave tool, which is Weave's word for a published workflow such as a product-mockup generator. Runs spend Weave credits, not Figma AI credits. Before a paid run the tool returns a cost-confirmation status and the agent must show you the credit cost and get a yes; workflows whose cost depends on a dynamic iterator say up front that the cost can't be quoted. Private tools are invisible to agents, and creating or editing workflows over MCP is not supported yet.</li>
<li><strong>Runway App Studio (26 October).</strong> You describe a tool in plain language and Runway's builder agent plans, designs and deploys an app with its own interface that generates images, video and audio from your Brand Kits, Workflows and assets. Early in the build it asks you to pick one of three colour schemes and can take your logo. An app is a private preview until you publish it to yourself, your workspace or specific people; you can roll back to earlier versions, the code stays inspectable, and each app shows its own credit usage. Launch examples include Precise Edit, which retouches only the region you mark, and AutoComp, which swaps a product into existing footage.</li></ul>
<h2>Our take</h2>
<p>These are three rungs of the same ladder. At the bottom, the <strong>agent drives the canvas</strong> (Framer): it can touch anything you can, so the safety comes from where its work lands, a branch with a reviewable diff, and from publishing being a separate, explicit act. In the middle, the <strong>agent calls a published workflow</strong> (Weave): it cannot change how the asset is made, only fill in the inputs someone else designed, and every paid run passes a price check. At the top, the <strong>workflow becomes an app for people</strong> (App Studio): the agent's work is the tool itself, and the guardrails are the Brand Kit it reads, the audience it is published to and the version you can roll back to.</p>
<p>The practical lesson for design teams is that the valuable artefact is moving from the prompt to the published workflow. A prompt that produced a good hero image once is a note; a published Weave tool or App Studio app with fixed references, brand colours and a known cost is something an agent can be trusted to run a hundred times. Framer's version of the same idea is the project's own styles and components, which its agent is told to reuse. If your system is not packaged in one of those forms, outside agents will improvise, and that is where off-brand output comes from.</p>
<p>Two cautions. Framer's agent works with your account's permissions, so an agent connected to a personal account can reach every project that account can. And cost confirmation only protects you if someone reads it: batch runs (Weave allows one to ten per call) multiply quickly.</p>
<h2>Checklist: letting an agent into your creative tools</h2>
<ol><li><strong>Pick the rung on purpose.</strong> Use canvas access for layout and content edits, published workflows for repeatable assets, and an app when non-designers need to run the workflow themselves.</li>
<li><strong>Branch by default.</strong> Tell the agent to create a branch before every Framer task, turn on automatic branching to protect main, and review the diff and a branch preview URL before you apply.</li>
<li><strong>Keep publish human.</strong> Never include "and publish" in a standing instruction; publish main yourself after review.</li>
<li><strong>Connect the narrowest account.</strong> Use a workspace or account that only holds the projects the agent should touch, since it inherits that account's permissions.</li>
<li><strong>Publish workflows, not prompts.</strong> Wrap your best image or video recipe as a Weave tool or App Studio app with fixed references, Brand Kit and named inputs, so agents fill in blanks instead of inventing styles.</li>
<li><strong>Set a credit ceiling.</strong> Decide a per-run and per-week credit budget, keep <code>numberOfRuns</code> low until the output is proven, and treat "cost can't be quoted" as a reason to run once first.</li>
<li><strong>Review assets like code.</strong> Check every generated image or page in light and dark themes, at 375 px, for alt text and contrast, before it enters a library or CMS.</li>
<li><strong>Log what the agent made.</strong> Keep a list of agent-generated pages, CMS items and assets with the prompt, workflow version and credit cost, so you can find and replace them later.</li></ol>
<pre><code># creative-agent-policy.yml: a starting spec
framer:
  connect: https://mcp.framer.com/mcp   # OAuth, workspace account only
  always_branch: true
  publish: human_only
  review: [diff, branch_preview_url, 375px, dark_mode]
weave:
  allow: published_tools_only           # no raw model runs in production
  confirm_cost: always
  max_runs_per_call: 2
  weekly_credit_budget: 500
app_studio:
  audience_default: only_me             # widen after review
  brand_kit: required
log: [page, cms_item, asset, prompt, workflow_version, credits]</code></pre>
<h2>How UI Hub helps</h2>
<p>An agent can only reuse styles that are written down. Our posts on <a href="../design-tokens-for-agents/">design tokens for agents</a> and <a href="../lint-agents-onto-your-design-system/">linting agents onto your design system</a> cover how to package them, and <a href="../layers-brand-kits-json-ai-visuals/">layers, brand kits and JSON for AI visuals</a> covers the brand-kit side of generated images. For the approval step itself, see <a href="../agent-approval-ui-budgets-interruptions/">designing approvals for agents</a>; for Figma's other agent features, see <a href="../figma-code-layers-and-specs/">Figma code layers and Specs</a>.</p>""",
 zh="""<p>不久之前，一个想改网站或做一张活动图的 AI 智能体只有两条路：从零写代码，或者请你自己打开设计工具。10 月 22 日到 26 日，三款创作工具用三种不同方式填上了这道缝：Framer 让外部智能体编辑它的画布和 CMS，Figma 让智能体通过 Figma MCP 调用 Weave 的图像和视频模型，Runway 让任何人描述一个创作应用就能得到能用的成品。它们回答的是同一个问题——<em>智能体在我的创作工具里能做什么？</em>——只是关卡设在不同的地方。</p>
<h2>发布了什么</h2>
<ul><li><strong>Framer MCP（10 月 22 日）。</strong>任何支持远程 MCP 服务器和 OAuth 的客户端，比如 Codex、Claude 或 Cursor，都能连接 <code>https://mcp.framer.com/mcp</code>。你批准连接后，智能体可以用项目已有的样式和组件新建页面、在桌面/平板/手机断点上改布局，管理 CMS 集合与条目，检查元数据、标题层级和替代文本。它使用你账号的权限。改动会留在项目或分支里，直到有人发布；智能体也能发布，但只在你明确要求时。Framer 的分支在 Review Changes 里显示差异，把分支应用到 main 和发布 main 是两个独立步骤。</li>
<li><strong>通过 Figma MCP 使用 Figma Weave（10 月 26 日）。</strong>只要有一个与 Figma 关联的付费独立 Weave 账号，外部智能体就能直接运行 Seedance、Kling、Nano Banana 等 Weave 模型，或者运行已发布的 Weave tool——这是 Weave 对「已发布工作流」的叫法，比如一个产品样机生成器。运行消耗的是 Weave 积分，不是 Figma AI 积分。付费运行前，工具会返回需确认费用的状态，智能体必须把积分花费告诉你并得到同意；费用取决于动态迭代器的工作流，会事先说明无法报价。私有工具对智能体不可见，目前也还不支持通过 MCP 创建或编辑工作流。</li>
<li><strong>Runway App Studio（10 月 26 日）。</strong>你用自然语言描述一个工具，Runway 的构建智能体就会规划、设计并部署一个有独立界面的应用，用你的 Brand Kit、Workflow 和素材生成图像、视频和音频。构建早期它会让你从三套配色里选一套，也可以放入你的 Logo。应用在发布前只是你自己能看的私有预览，发布时可选仅自己、整个工作区或指定的人；可以回滚到旧版本，代码可查看，每个应用单独显示积分用量。首发示例里有只修你圈出区域的 Precise Edit，以及把产品换进现有视频画面的 AutoComp。</li></ul>
<h2>我们的看法</h2>
<p>这是同一架梯子的三级。最低一级是<strong>智能体直接操作画布</strong>（Framer）：你能碰的它都能碰，所以安全来自它的成果落在哪里——一个能看差异的分支——以及发布是一个单独、明确的动作。中间一级是<strong>智能体调用已发布的工作流</strong>（Weave）：它改不了素材的做法，只能填别人设计好的输入，而且每次付费运行都要过一道价格确认。最高一级是<strong>工作流变成给人用的应用</strong>（App Studio）：智能体的产出就是工具本身，护栏是它读取的 Brand Kit、发布对象和可以回滚的版本。</p>
<p>对设计团队来说，最实际的一课是：有价值的资产正在从「提示词」变成「已发布的工作流」。一条曾经出过一张好首屏图的提示词只是笔记；一个固定了参考图、品牌色和已知费用的 Weave tool 或 App Studio 应用，才是能放心让智能体跑一百次的东西。Framer 版本的同一思路，是项目自己的样式和组件，它的智能体被要求优先复用。如果你的设计系统没有被打包成这类形式，外部智能体就会即兴发挥，跑偏的产出就是这么来的。</p>
<p>两点提醒：Framer 的智能体使用你账号的权限，接在个人账号上的智能体能碰到该账号的所有项目；费用确认只有在有人认真看时才有用，批量运行（Weave 每次调用可跑 1 到 10 次）会让花费迅速翻倍。</p>
<h2>清单：让智能体进入你的创作工具</h2>
<ol><li><strong>有意识地选层级。</strong>布局和内容修改用画布权限，可重复的素材用已发布工作流，需要非设计师自己跑流程时做成应用。</li>
<li><strong>默认开分支。</strong>每个 Framer 任务都让智能体先建分支，打开自动分支保护 main，应用前先看差异和分支预览链接。</li>
<li><strong>发布留给人。</strong>长期指令里不要写「然后发布」；审完之后由你自己发布 main。</li>
<li><strong>连接权限最小的账号。</strong>用只包含智能体该碰项目的工作区或账号，因为它继承的是这个账号的全部权限。</li>
<li><strong>发布工作流，而不是提示词。</strong>把最好的图像或视频做法封装成 Weave tool 或 App Studio 应用，固定参考图、Brand Kit 和命名输入，让智能体填空而不是自创风格。</li>
<li><strong>设积分上限。</strong>定好单次和每周的积分预算，效果没验证前把 <code>numberOfRuns</code> 设小，遇到「无法报价」就先跑一次再说。</li>
<li><strong>像审代码一样审素材。</strong>生成的每张图、每个页面，进素材库或 CMS 之前都在亮色和暗色、375 px 宽度下检查，看替代文本和对比度。</li>
<li><strong>记录智能体产出。</strong>把智能体生成的页面、CMS 条目和素材列成清单，附上提示词、工作流版本和积分花费，方便以后查找和替换。</li></ol>
<pre><code># creative-agent-policy.yml：一份起步规格
framer:
  connect: https://mcp.framer.com/mcp   # OAuth，只用工作区账号
  always_branch: true
  publish: human_only
  review: [diff, branch_preview_url, 375px, dark_mode]
weave:
  allow: published_tools_only           # 生产环境不直接跑原始模型
  confirm_cost: always
  max_runs_per_call: 2
  weekly_credit_budget: 500
app_studio:
  audience_default: only_me             # 审过再扩大
  brand_kit: required
log: [page, cms_item, asset, prompt, workflow_version, credits]</code></pre>
<h2>UI Hub 能帮什么</h2>
<p>智能体只能复用写下来的样式。<a href="../design-tokens-for-agents/">给智能体的设计 Token</a>和<a href="../lint-agents-onto-your-design-system/">用 Lint 把智能体拉回你的设计系统</a>讲了怎么打包；<a href="../layers-brand-kits-json-ai-visuals/">图层、品牌包与 JSON</a>讲了生成图片的品牌包这一侧。审批环节本身见<a href="../agent-approval-ui-budgets-interruptions/">为替人办事的智能体设计审批</a>；Figma 其他智能体功能见 <a href="../figma-code-layers-and-specs/">Figma Code Layers 与 Specs</a>。</p>""",
 refs=[('Framer MCP','Framer Updates','https://www.framer.com/updates/framer-mcp'),('Connect Claude, Codex and Cursor to Framer with MCP','Framer','https://www.framer.com/mcp/'),('Getting started with Framer MCP','Framer Help','https://www.framer.com/help/articles/getting-started-with-framer-mcp/'),('What you can do with Framer MCP','Framer Help','https://www.framer.com/help/articles/what-you-can-do-with-framer-mcp/'),('How to use branches in Framer','Framer Help','https://www.framer.com/help/articles/how-to-use-branches-in-framer/'),('Review Agent changes safely with Branching','Framer Academy','https://www.framer.com/academy/lessons/branching-explore-variations-safely'),('Access video and image models from Figma Weave via the Figma MCP','Figma release notes','https://www.figma.com/release-notes/'),('Figma MCP server FAQs','Figma Learn','https://help.figma.com/hc/en-us/articles/39252411778583-Figma-MCP-server-FAQs'),('Tools and example prompts','Figma Learn','https://help.figma.com/hc/en-us/articles/42495147242903-Tools-and-example-prompts'),('Running Weave tools and models from external agents (MCP)','Figma Weave Knowledge Center','https://help.weavy.ai/en/articles/16202764-running-weave-tools-and-models-from-external-agents-mcp'),('Introducing Runway App Studio','Runway','https://runway.com/news/company-news/introducing-runway-app-studio'),('App Studio: build your own creative apps','Runway','https://runway.com/product/app-studio'),('Runway App Studio brings no-code app building to AI filmmaking','Bottle Rocket Content','https://www.bottlerocketcontent.com/runway-app-studio-no-code-creative-apps/'),('Tools','Model Context Protocol specification','https://modelcontextprotocol.io/specification/2025-06-18/server/tools')]),
]
POSTS2 += [
dict(slug='annotate-dont-describe-visual-prompts', date='2026-10-28', cat='workflow', series=None, featured=True, tags=['Cursor Design Mode','Annotate','v0 Design mode','Lovable','visual prompts'],
 t=T('Point, don’t describe: visual prompts for UI edits in Cursor, v0 and Lovable','别再描述，直接指：Cursor、v0 与 Lovable 里用「可视化提示」改界面','別再描述，直接指：Cursor、v0 與 Lovable 裡用「視覺化提示」改介面','説明より指さし：Cursor・v0・Lovable のビジュアルプロンプトでUIを直す','설명 대신 가리키기: Cursor, v0, Lovable의 시각적 프롬프트로 UI 고치기','Tunjuk, jangan terangkan: prompt visual untuk suntingan UI dalam Cursor, v0 dan Lovable','Chỉ vào, đừng mô tả: prompt trực quan để sửa UI trong Cursor, v0 và Lovable','Montrer plutôt que décrire : les prompts visuels pour retoucher une UI dans Cursor, v0 et Lovable','Señala, no describas: prompts visuales para editar UI en Cursor, v0 y Lovable','Zeigen statt beschreiben: visuelle Prompts für UI-Änderungen in Cursor, v0 und Lovable'),
 s=T('On 27 October Cursor added Annotate to Design Mode: click, box, draw, edit text or CSS on your running app and the agent gets the element’s identity plus a cropped screenshot. v0 and Lovable already let you point at a preview. What each one actually sends to the model, where pointing beats a paragraph, where it quietly breaks your design system, and a checklist for notes that land first time.',
     '10 月 27 日，Cursor 给 Design Mode 加上了 Annotate：在运行中的应用上点选、框选、涂画、改文字或改 CSS，智能体就能拿到元素身份信息和一张裁好的截图。v0 和 Lovable 也早已支持在预览上直接指。本文拆解三者到底把什么交给模型、什么时候「指」比一段话更好用、什么时候它会悄悄绕开你的设计系统，以及一份让批注一次命中的清单。',
     '10 月 27 日，Cursor 為 Design Mode 加上了 Annotate：在執行中的應用上點選、框選、塗畫、改文字或改 CSS，智慧體就能拿到元素身分資訊和一張裁好的截圖。v0 和 Lovable 也早已支援在預覽上直接指。本文拆解三者到底把什麼交給模型、什麼時候「指」比一段話更好用、什麼時候它會悄悄繞開你的設計系統，以及一份讓批註一次命中的清單。',
     '10月27日、CursorはDesign ModeにAnnotateを追加した。動いているアプリ上でクリック、範囲指定、描き込み、テキストやCSSの編集をすると、エージェントは要素の識別情報と切り抜いたスクリーンショットを受け取る。v0とLovableもプレビューを指さす機能を持つ。3つが実際にモデルへ渡すもの、指さしが文章に勝つ場面、デザインシステムを静かに崩す場面、一度で通るメモのチェックリスト。',
     '10월 27일 Cursor는 Design Mode에 Annotate를 추가했다. 실행 중인 앱에서 클릭, 영역 지정, 그리기, 텍스트나 CSS 편집을 하면 에이전트는 요소의 식별 정보와 잘라낸 스크린샷을 받는다. v0와 Lovable도 이미 미리보기를 가리킬 수 있다. 세 도구가 모델에 실제로 넘기는 것, 가리키기가 문장보다 나은 경우, 디자인 시스템을 조용히 깨는 경우, 한 번에 통하는 메모 체크리스트.',
     'Pada 27 Oktober Cursor menambah Annotate pada Design Mode: klik, kotakkan, lukis, sunting teks atau CSS pada aplikasi yang sedang berjalan dan ejen menerima identiti elemen serta tangkapan skrin yang dipotong. v0 dan Lovable sudah membolehkan anda menunjuk pada pratonton. Apa yang setiap satu hantar kepada model, bila menunjuk lebih baik daripada perenggan, bila ia diam-diam memecahkan sistem reka bentuk, dan senarai semak untuk nota yang tepat kali pertama.',
     'Ngày 27/10, Cursor thêm Annotate vào Design Mode: bấm, khoanh vùng, vẽ, sửa chữ hoặc CSS trên ứng dụng đang chạy và agent nhận được danh tính phần tử cùng ảnh chụp đã cắt. v0 và Lovable vốn đã cho phép chỉ vào bản xem trước. Mỗi công cụ thực sự gửi gì cho mô hình, khi nào chỉ tay hơn một đoạn văn, khi nào nó âm thầm phá design system, và checklist để ghi chú trúng ngay lần đầu.',
     'Le 27 octobre, Cursor a ajouté Annotate à Design Mode : cliquez, encadrez, dessinez, modifiez un texte ou du CSS sur l’app en cours d’exécution, et l’agent reçoit l’identité de l’élément et une capture recadrée. v0 et Lovable permettaient déjà de pointer l’aperçu. Ce que chacun envoie vraiment au modèle, quand pointer vaut mieux qu’un paragraphe, quand cela contourne en silence votre design system, et une checklist pour des notes qui passent du premier coup.',
     'El 27 de octubre Cursor añadió Annotate a Design Mode: haz clic, enmarca, dibuja o edita texto o CSS sobre tu app en marcha y el agente recibe la identidad del elemento y una captura recortada. v0 y Lovable ya permitían señalar la vista previa. Qué envía cada uno al modelo, cuándo señalar gana a un párrafo, cuándo rompe en silencio tu sistema de diseño y una lista para notas que acierten a la primera.',
     'Am 27. Oktober hat Cursor Design Mode um Annotate erweitert: Klicke, rahme ein, zeichne oder ändere Text und CSS in der laufenden App, und der Agent erhält die Identität des Elements plus einen zugeschnittenen Screenshot. v0 und Lovable können schon länger auf die Vorschau zeigen. Was jedes Tool wirklich ans Modell schickt, wann Zeigen einen Absatz schlägt, wann es dein Design-System leise umgeht, und eine Checkliste für Notizen, die beim ersten Mal sitzen.'),
 en="""<p>“Make the second card match the first, but tighter” is a hard sentence for a coding agent. Which second card? Tighter how? The agent has to search the code for something that looks like your description, and when it guesses wrong you write a correction that is longer than the original request. On 27 October Cursor shipped Annotate, a reworked version of its browser Design Mode that lets you answer those questions by pointing at the running app. v0 and Lovable offer their own version of the same idea. Taken together they show that, for interface work, the useful prompt is becoming <em>a pointer plus a small change</em> rather than a paragraph.</p>
<h2>What each tool sends to the model</h2>
<ul><li><strong>Cursor Design Mode with Annotate (27 October, Cursor 3.24.18 or later).</strong> It lives in the browser inside the Agents Window; click Annotate or press <code>Cmd/Ctrl + Shift + D</code>. You click an element (arrow keys move the highlight to its parent or child), Shift-click to add more elements to the same note, drag to box an area and draw with pen, ellipse, rectangle or arrow, double-click text to edit it in place, open a CSS inspector on a single element, or dictate. For every picked element the agent receives the tag, id, classes, attributes, a selector path, the first 200 characters of visible text, size and position, six computed styles (colour, background, font size, font family, display, position) and, in React, Vue and Svelte apps, the component name and component stack. It also gets a screenshot cropped to the element or to your marked-up area. Notes go out one at a time by default; a <em>Batch edits</em> switch collects them as numbered pins and sends them as one message. Cursor recommends a fast UI-capable model for this loop, naming Composer 2.5.</li>
<li><strong>v0 Design mode.</strong> You select an element in the live preview and either adjust it in a panel (typography, colour, background, margin and padding, border, opacity and radius, shadow, text) or type an instruction, and v0 attaches a screenshot of the element to it. When the project uses Tailwind, the panel offers Tailwind-compatible values. Edits stay pending, with undo, reset and a before-and-after toggle, until you press Apply; Apply sends everything to the chat and produces a normal new version you can diff or revert. A Design Mode API lets teams embed the same editor in their own product.</li>
<li><strong>Lovable preview toolbar.</strong> It replaced the older Visual edits panel with four modes: select elements (Cmd/Ctrl-click for several), edit text inline, draw an annotation that is sent as a marked-up screenshot (rough shapes are cleaned up), and pinned comments for teammates. Comments are free; sending one to Lovable, selecting, and drawing use build credits. Each account gets 100 free inline text edits per rolling 24 hours, with a shared workspace cap of 2,000.</li></ul>
<h2>Our take</h2>
<p>The three tools split along one line: <strong>does the tool apply your visual change itself, or translate it for the agent?</strong> v0 sits closest to a design tool: panel edits are concrete values, the result is a reviewable version, and the model mainly turns them into source. Cursor and Lovable treat your mark as context: the agent still decides what code to change, but it starts from the right component instead of a guess. Cursor sends the richest context, structured element data and the component stack as well as pixels, which is why it can work inside large existing codebases rather than only in a generated project.</p>
<p>Pointing has two blind spots. First, a note captures one frozen state at one width. The agent sees the hover you circled at 1440 px, not the empty state, the error state or the 375 px layout, and will happily fix only what it saw. Cursor’s announcement mentions reviewing designs at different screen sizes, but the check is still yours. Second, direct manipulation produces raw values. Drag a padding to 18 px or pick <code>#3b82f6</code> in an inspector and you have just written a one-off that your design system doesn’t know about. v0’s Tailwind-aware values help, but none of these tools promise to map an edit to your tokens. Tell the agent to do it, and lint for it afterwards.</p>
<p>Our rule of thumb: <strong>point for <em>where</em>, write for <em>why</em>.</strong> The mark gives location, the sentence gives intent and limits. “Match this card’s spacing to the one on the left, use our space tokens, don’t change the copy” is a better note than either a drawing or a paragraph on its own.</p>
<h2>Checklist: visual notes that land first time</h2>
<ol><li><strong>Pick the smallest target.</strong> Use the parent and child highlight (arrow keys in Cursor) until the box is the component you mean, not its wrapper or one span inside it.</li>
<li><strong>Use multi-select for relationships.</strong> Select both elements when the change is “make A match B”, “remove the duplicate” or “align these”. A single selection makes the agent hunt for the other one.</li>
<li><strong>Draw only for areas.</strong> Box or circle when the change is about a region (crowding, a gap, where a new element goes), not to point at a single button.</li>
<li><strong>Write intent and limits in one line.</strong> Say what should change, the token or component to use, and what must not change.</li>
<li><strong>Translate raw values into tokens.</strong> After a CSS-inspector or panel tweak, add “use the nearest existing token” and let your design-system lint fail on hard-coded colours and spacing.</li>
<li><strong>Batch related notes, send unrelated ones alone.</strong> A round of spacing fixes on one screen is one batch; a copy fix and a layout change on different pages are separate notes the agent can run in parallel.</li>
<li><strong>Re-check the other states.</strong> After each round, look at 375 px, dark mode, empty, loading, error and keyboard focus. The note only showed one of them.</li>
<li><strong>Review the diff, not just the preview.</strong> Hot reload shows that it looks right. The diff shows whether the agent changed a shared component that ten other pages use.</li></ol>
<pre><code># a visual note that works (target + intent + limits)
target:  PricingCard[plan="Pro"]  + PricingCard[plan="Team"]   # multi-select
change:  make Team match Pro: same padding, same badge position
use:     --space-6 for padding, Badge variant="outline"
keep:    copy, prices, button labels
check:   375px stack, dark mode, focus ring on CTA</code></pre>
<h2>How UI Hub helps</h2>
<p>Pointing only stays on-brand if the agent has tokens to map onto. Our post on <a href="../design-tokens-for-agents/">design tokens for agents</a> covers how to write them down, and <a href="../lint-agents-onto-your-design-system/">linting agents onto your design system</a> covers catching the one-off values that visual edits produce. For the tools themselves, see <a href="../v0-prompt-to-shadcn/">v0 in practice</a> and <a href="../lovable-bolt-prompt-to-app/">Lovable and Bolt</a>; for the states a single note won’t show, see <a href="../accessibility-in-ai-generated-ui/">accessibility in AI-generated UI</a>.</p>""",
 zh="""<p>「把第二张卡片改得和第一张一样，但更紧凑一点」——这句话对编码智能体来说很难。哪张是第二张？怎么个紧凑法？智能体只能在代码里找一个长得像你描述的东西，猜错了，你写的纠正往往比原来的请求还长。10 月 27 日，Cursor 推出了 Annotate，这是它浏览器里 Design Mode 的改版：你可以直接在运行中的应用上「指」来回答这些问题。v0 和 Lovable 也有各自的版本。放在一起看，可以发现：做界面时，好用的提示正在从「一段话」变成<em>「一个指向 + 一个小改动」</em>。</p>
<h2>三个工具分别把什么交给模型</h2>
<ul><li><strong>Cursor Design Mode + Annotate（10 月 27 日，需 Cursor 3.24.18 或更高）。</strong>它在 Agents Window 内置浏览器里，点 Annotate 或按 <code>Cmd/Ctrl + Shift + D</code> 打开。你可以点选元素（方向键可把高亮移到父级或子级），Shift 点击把更多元素加进同一条批注，拖拽框选区域并用画笔、椭圆、矩形或箭头标注，双击文字原地修改，对单个元素打开 CSS 检查器，或者直接语音口述。每个被选中的元素，智能体都会收到：标签、id、class、属性、选择器路径、前 200 个可见字符、尺寸与位置、六项计算样式（颜色、背景色、字号、字体、display、position）；在 React、Vue、Svelte 应用里还有组件名和组件栈。另外还有一张裁到该元素或你标注区域的截图。批注默认逐条发送；打开 <em>Batch edits</em> 开关后，批注会以编号图钉的形式攒起来，一次作为一条消息发出。Cursor 建议这类循环用速度快、擅长界面的模型，点名了 Composer 2.5。</li>
<li><strong>v0 Design mode。</strong>在实时预览里选中元素，要么在面板里调（字体排印、颜色、背景、内外边距、边框、透明度与圆角、阴影、文字），要么输入一句指令，v0 会自动附上该元素的截图。项目用 Tailwind 时，面板会给出兼容 Tailwind 的取值。改动先挂起，可撤销、重置、对比前后，按 Apply 才会发到对话里，生成一个可看差异、可回退的新版本。团队还能通过 Design Mode API 把同一套编辑器嵌进自己的产品。</li>
<li><strong>Lovable 预览工具栏。</strong>它取代了旧的 Visual edits 面板，分四种模式：选择元素（Cmd/Ctrl 点击可多选）、原地改文字、画批注（作为带标注的截图发送，随手画的形状会被自动规整）、给队友留的图钉评论。评论免费；把评论发给 Lovable、选择元素和画批注都消耗构建积分。每个账号每滚动 24 小时有 100 次免费原地改字，工作区共享上限 2000 次。</li></ul>
<h2>我们的看法</h2>
<p>三者的分界线是：<strong>工具是自己执行你的视觉改动，还是把它翻译给智能体？</strong>v0 最接近设计工具：面板改的是具体数值，结果是一个可审阅的版本，模型主要负责把它写进源码。Cursor 和 Lovable 把你的标注当作上下文：改哪段代码仍由智能体决定，但它从正确的组件出发，而不是靠猜。Cursor 给的上下文最丰富——除了像素还有结构化的元素数据和组件栈——所以它能在大型现有代码库里工作，而不只是在生成出来的项目里。</p>
<p>「指」有两个盲区。第一，一条批注只记录某个宽度下的一个定格状态。智能体看到的是你在 1440 px 下圈出的悬停态，看不到空状态、错误态或 375 px 布局，而且会很乐意只修它看到的那一个。Cursor 的发布说明提到可以在不同屏幕尺寸下检查设计，但检查这件事仍然是你的。第二，直接操作产生的是裸数值。在检查器里把内边距拖到 18 px、选了 <code>#3b82f6</code>，你就写下了一个设计系统不认识的一次性值。v0 的 Tailwind 取值有帮助，但这几个工具都没有承诺把改动映射到你的 Token。要明确告诉智能体这么做，事后再用 Lint 查。</p>
<p>我们的经验法则：<strong>用「指」说明在哪里，用文字说明为什么。</strong>标注给位置，句子给意图和边界。「把这张卡片的间距改成和左边那张一致，用我们的间距 Token，文案别动」比单独一幅涂鸦或一段话都好。</p>
<h2>清单：让可视化批注一次命中</h2>
<ol><li><strong>选最小的目标。</strong>用父级/子级高亮（Cursor 里是方向键）调到你真正想改的组件，而不是它的外层容器或里面的某个 span。</li>
<li><strong>涉及关系就多选。</strong>「让 A 和 B 一致」「删掉重复的」「把这些对齐」时，把两个元素都选上。只选一个，智能体就得自己去找另一个。</li>
<li><strong>只在说区域时才画。</strong>改动关乎一块区域（太挤、有空隙、新元素放哪）时才框或圈，别用来指一个按钮。</li>
<li><strong>一句话写清意图和边界。</strong>说明要改什么、用哪个 Token 或组件、什么不能动。</li>
<li><strong>把裸数值换成 Token。</strong>用过 CSS 检查器或面板微调后，补一句「用最接近的现有 Token」，并让设计系统 Lint 在硬编码颜色和间距上报错。</li>
<li><strong>相关的批注打包，不相关的单发。</strong>同一屏的一轮间距修正是一批；不同页面上的一处文案和一处布局是两条独立批注，智能体可以并行处理。</li>
<li><strong>回头检查其他状态。</strong>每轮之后看一遍 375 px、暗色模式、空状态、加载、错误和键盘焦点。批注只展示了其中一种。</li>
<li><strong>看差异，而不只是看预览。</strong>热更新告诉你「看起来对」；差异告诉你智能体是不是改了一个另外十个页面都在用的共享组件。</li></ol>
<pre><code># 一条好用的可视化批注（目标 + 意图 + 边界）
target:  PricingCard[plan="Pro"]  + PricingCard[plan="Team"]   # 多选
change:  让 Team 和 Pro 一致：相同内边距、相同徽章位置
use:     内边距用 --space-6，Badge variant="outline"
keep:    文案、价格、按钮文字
check:   375px 堆叠、暗色模式、CTA 焦点环</code></pre>
<h2>UI Hub 能帮什么</h2>
<p>只有当智能体有 Token 可映射时，「指」出来的改动才不会跑偏。<a href="../design-tokens-for-agents/">给智能体的设计 Token</a> 讲了怎么把它们写下来，<a href="../lint-agents-onto-your-design-system/">用 Lint 把智能体拉回你的设计系统</a> 讲了怎么抓住可视化编辑产生的一次性数值。工具本身见 <a href="../v0-prompt-to-shadcn/">v0 实战</a> 和 <a href="../lovable-bolt-prompt-to-app/">Lovable 与 Bolt</a>；单条批注看不到的那些状态，见 <a href="../accessibility-in-ai-generated-ui/">AI 生成界面的无障碍</a>。</p>""",
 refs=[('Design Mode','Cursor Docs','https://cursor.com/docs/agent/design-mode'),('Direct agents with visual prompts in Design Mode','Erik Nilsson, Ian Huang & Ryo Lu, Cursor','https://cursor.com/blog/design-mode'),('Release notes','Cursor Docs','https://cursor.com/docs/release-notes'),('New in Cursor design mode: Annotate','@cursor_ai on X','https://x.com/cursor_ai/status/2115159585548021814'),('Cursor’s Design Mode adds Annotate: point and draw instead of describing UI changes to agents','Automater News','https://automater.ai/news/cursor-design-mode-annotate-point-draw-agents/'),('Cursor adds Annotate to Design mode','daily.dev','https://daily.dev/posts/cursor-adds-annotate-to-design-mode-t6xlmktyu'),('Design mode','v0 Docs','https://v0.app/docs/design-mode'),('Edit from the preview','Lovable Documentation','https://docs.lovable.dev/features/visual-edit')]),
]
