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
]
