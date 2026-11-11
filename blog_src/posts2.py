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
POSTS2 += [
dict(slug='github-replica-design-system-prototypes', date='2026-10-29', cat='tools', series='agent-context', featured=True, tags=['GitHub Replica','Copilot','design systems','AI prototyping','agent guidance'],
 t=T('GitHub Replica: AI prototypes that start from your design system, not a blank page','GitHub Replica：从你的设计系统出发、而不是从空白页出发的 AI 原型','GitHub Replica：從你的設計系統出發、而不是從空白頁出發的 AI 原型','GitHub Replica：白紙ではなく自社デザインシステムから始めるAIプロトタイプ','GitHub Replica: 빈 페이지가 아니라 내 디자인 시스템에서 시작하는 AI 프로토타입','GitHub Replica: prototaip AI yang bermula daripada sistem reka bentuk anda, bukan halaman kosong','GitHub Replica: prototype AI bắt đầu từ design system của bạn, không phải trang trắng','GitHub Replica : des prototypes IA qui partent de votre design system, pas d’une page blanche','GitHub Replica: prototipos con IA que parten de tu design system, no de una página en blanco','GitHub Replica: KI-Prototypen, die bei deinem Designsystem anfangen statt bei einer leeren Seite'),
 s=T('On 28 October GitHub open-sourced Replica, an MIT-licensed prototyping tool from GitHub Design and Microsoft CoreAI Design that runs in the Copilot app. Its real idea is not the canvas but the guidance: reviewed context files split by owner, drafts kept out of active use, missing evidence marked manual instead of passed. What it does, where it is heavy, and a checklist you can apply even without Replica.',
     '10 月 28 日，GitHub 开源了 Replica：一款由 GitHub Design 与 Microsoft CoreAI Design 打造、运行在 Copilot 应用里的原型工具，MIT 许可。它真正值得看的不是画布，而是「规范」的管法：按负责方拆分、经过评审的上下文文件，草稿不进入生效状态，缺证据就记为人工检查而不是默认通过。本文讲它能做什么、哪里偏重，以及一份即使不用 Replica 也能照做的清单。',
     '10 月 28 日，GitHub 開源了 Replica：一款由 GitHub Design 與 Microsoft CoreAI Design 打造、執行在 Copilot 應用裡的原型工具，MIT 授權。它真正值得看的不是畫布，而是「規範」的管法：按負責方拆分、經過審閱的上下文檔案，草稿不進入生效狀態，缺證據就記為人工檢查而不是預設通過。本文講它能做什麼、哪裡偏重，以及一份即使不用 Replica 也能照做的清單。',
     '10月28日、GitHubはReplicaをオープンソース化した。GitHub DesignとMicrosoft CoreAI Designが作った、Copilotアプリ上で動くMITライセンスのプロトタイピングツールだ。本当の見どころはキャンバスではなくガイダンスの扱い方にある。担当ごとに分けたレビュー済みのコンテキストファイル、有効化されない下書き、根拠がなければ合格ではなく手動確認。できること、重い部分、Replicaを使わなくても使えるチェックリスト。',
     '10월 28일 GitHub는 Replica를 오픈소스로 공개했다. GitHub Design과 Microsoft CoreAI Design이 만든, Copilot 앱에서 동작하는 MIT 라이선스 프로토타이핑 도구다. 진짜 핵심은 캔버스가 아니라 가이드를 다루는 방식이다. 담당별로 나눈 검토된 컨텍스트 파일, 활성화되지 않는 초안, 근거가 없으면 통과가 아니라 수동 확인. 무엇을 하는지, 어디가 무거운지, Replica 없이도 쓸 수 있는 체크리스트.',
     'Pada 28 Oktober GitHub menjadikan Replica sumber terbuka: alat prototaip berlesen MIT daripada GitHub Design dan Microsoft CoreAI Design yang berjalan dalam aplikasi Copilot. Idea sebenarnya bukan kanvas tetapi panduan: fail konteks yang disemak dan dipecahkan mengikut pemilik, draf tidak digunakan secara aktif, bukti yang tiada ditanda manual dan bukan lulus. Apa yang ia buat, di mana ia berat, dan senarai semak yang boleh digunakan walaupun tanpa Replica.',
     'Ngày 28/10, GitHub mở mã nguồn Replica: công cụ làm prototype giấy phép MIT do GitHub Design và Microsoft CoreAI Design xây dựng, chạy trong ứng dụng Copilot. Ý tưởng thật sự không nằm ở canvas mà ở cách quản lý hướng dẫn: các file ngữ cảnh đã duyệt, chia theo người phụ trách, bản nháp không được kích hoạt, thiếu bằng chứng thì đánh dấu kiểm tra thủ công chứ không phải đạt. Nó làm gì, nặng ở đâu, và checklist áp dụng được cả khi không dùng Replica.',
     'Le 28 octobre, GitHub a publié en open source Replica, un outil de prototypage sous licence MIT conçu par GitHub Design et Microsoft CoreAI Design, qui tourne dans l’app Copilot. Son idée forte n’est pas le canevas mais la gestion des consignes : des fichiers de contexte relus et répartis par responsable, des brouillons jamais actifs, une preuve manquante notée « manuel » plutôt que « validé ». Ce qu’il fait, où il est lourd, et une checklist applicable même sans Replica.',
     'El 28 de octubre GitHub liberó Replica, una herramienta de prototipado con licencia MIT creada por GitHub Design y Microsoft CoreAI Design que funciona dentro de la app de Copilot. Su idea de fondo no es el lienzo sino la guía: archivos de contexto revisados y repartidos por responsable, borradores que nunca quedan activos y evidencia ausente marcada como manual en vez de aprobada. Qué hace, dónde pesa y una checklist útil incluso sin Replica.',
     'Am 28. Oktober hat GitHub Replica als Open Source veröffentlicht: ein MIT-lizenziertes Prototyping-Tool von GitHub Design und Microsoft CoreAI Design, das in der Copilot-App läuft. Die eigentliche Idee ist nicht die Canvas, sondern der Umgang mit Vorgaben: geprüfte Kontextdateien nach Zuständigkeit getrennt, Entwürfe nie aktiv, fehlende Belege als manuell statt bestanden markiert. Was es kann, wo es schwer ist, und eine Checkliste, die auch ohne Replica funktioniert.'),
 en="""<p>Most prompt-to-UI tools start from a blank page and a model’s idea of what a “clean SaaS app” looks like. You get something polished and generic, and the first hour of review is spent explaining that your product doesn’t have that sidebar, that button style or that kind of empty state. On 28 October GitHub open-sourced <strong>Replica</strong>, a prototyping tool built by GitHub Design and Microsoft CoreAI Design, which tries to fix the order of operations: <em>designers write and approve the rules first, then anyone on the team prototypes inside them.</em></p>
<h2>What Replica is</h2>
<ul><li><strong>Where it runs.</strong> Inside the GitHub Copilot app. A plugin adds a Replica canvas that shows your running prototype next to the conversation, so you describe a change, try it, and refine it in one place. It is MIT-licensed and maintained by GitHub staff.</li>
<li><strong>Four parts.</strong> Starters (a <em>Minimal</em> app to adapt to your own system, or a <em>CoreAI Sandbox</em> with Microsoft’s CoreAI design system already wired in), the canvas plugin, an optional self-hosted <strong>Replica Hub</strong> for publishing and comments, and a GitHub build action that only matters once you publish.</li>
<li><strong>Local first.</strong> A local prototype needs the Copilot app, Git, Node.js and npm on macOS or Linux. No Hub, Docker, domain or GitHub repository is required. Hub needs a Linux server, a dedicated domain with wildcard DNS and HTTPS, and GitHub approvals, and your organisation runs it, not GitHub.</li>
<li><strong>Models.</strong> GitHub-hosted models with a Copilot plan, or your own model provider (public preview, provider’s terms apply). Viewing or reviewing a finished prototype needs no Copilot subscription.</li></ul>
<h2>The interesting part: guidance as a reviewed artifact</h2>
<p>You run <code>/setup-skills</code>, point Copilot at approved sources (product docs, design-system docs, component and token packages), and it drafts guidance. The docs are explicit that drafting does not activate anything: designers and design-system maintainers review the drafts, and activation is a separate approval. The result is a set of context files, each owning one concern: <code>DESIGN-SYSTEM.md</code> for components, tokens and patterns, <code>PRODUCT-DESIGN.md</code> for scenarios and state behaviour, <code>RESPONSIVE-DESIGN.md</code> for widths, plus accessibility, browser validation, seed data and repository rules.</p>
<p>The bundled skills are strict about how they use that context. The design-system review skill reads only the active folder, never drafts. A rule labelled <code>proposed-default</code> is treated as a proposal, not policy. And when required evidence is missing, the check is marked <em>manual, never pass</em>; the skill is told not to guess components or tokens. The template for <code>DESIGN-SYSTEM.md</code> also rejects lazy context: “TextInput exists” is not an answer to how validation errors are shown.</p>
<p>There is a feedback loop too. With Hub connected, <code>/review-hub-feedback</code> looks for recurring themes across prototype reviews, and <code>/prepare-feedback-proposals</code> turns chosen findings into proposed guidance edits, each shown before you approve it. Comments improve the rules, not just the one prototype that got them.</p>
<h2>Our take</h2>
<p>Replica is less a new generator than a workflow wrapped around one: branch per prototype, sample data only, ask before committing, never push or publish without approval. That is the right shape for teams where a PM or engineer prototypes alongside designers. The strongest idea is portable: <strong>split guidance by owner, separate draft from active, and make “I don’t know” visible</strong>. Most agent context files we see are one long, unreviewed <code>AGENTS.md</code> that nobody owns and every agent treats as gospel.</p>
<p>The costs are real. It assumes the Copilot app (macOS or Linux) and, for sharing, someone willing to operate a Hub with wildcard DNS. The canvas proxies the preview from a different origin, so apps that depend on their own origin for storage or sign-in may need extra work. And the docs themselves warn about the failure we see most often in AI-built UI: the agent using <em>similar-looking replacements</em> instead of your real components. Guidance lowers that risk; it does not remove it, so check imports, not screenshots.</p>
<h2>Checklist: design-system-first prototyping (with or without Replica)</h2>
<ol><li><strong>Split guidance into owned files.</strong> Design system, product behaviour, responsive widths, accessibility, seed data and repository rules each get one file and one owner.</li>
<li><strong>Give every rule a condition and evidence.</strong> “Use Banner for page-level errors, InlineMessage inside forms — see docs link” beats “use our components”.</li>
<li><strong>Keep drafts out of active context.</strong> Agent-written guidance goes to a drafts folder until a designer approves it; label unreviewed defaults as proposed.</li>
<li><strong>Make unknowns visible.</strong> If the agent can’t find evidence for a token or pattern, it should say so and leave the check manual, not invent a value.</li>
<li><strong>One prototype, one branch.</strong> Keep the default branch as the reviewed starting point; never let a prototype rewrite it.</li>
<li><strong>Sample data only.</strong> No production credentials or customer data in prototypes, ever.</li>
<li><strong>Verify the real components.</strong> Grep the prototype’s imports for your package and wrappers; a lookalike <code>&lt;button&gt;</code> is a failed check.</li>
<li><strong>Route feedback into the rules.</strong> When the same review comment appears twice, change the guidance file, not just the prototype.</li></ol>
<pre><code># .agents/context/  (one concern per file, reviewed before use)
DESIGN-SYSTEM.md      # imports, tokens, layout, forms, feedback — each with a docs link
PRODUCT-DESIGN.md     # scenarios, saving, empty / loading / error behaviour
RESPONSIVE-DESIGN.md  # required widths, what collapses at 375px
ACCESSIBILITY.md      # keyboard, contrast, screen-reader expectations
SEED-DATA.md          # sample data rules (no real customers)
REPOSITORY.md         # required wrappers, branch + commit rules
# drafts/ is never read as active; "proposed-default" ≠ policy</code></pre>
<h2>How UI Hub helps</h2>
<p>Replica only works as well as the guidance you feed it. Our posts on <a href="../design-tokens-for-agents/">design tokens for agents</a> and <a href="../claude-cursor-design-skills/">design skills for Claude and Cursor</a> cover how to write that context; <a href="../lint-agents-onto-your-design-system/">linting agents onto your design system</a> covers catching lookalike components after the fact. For how Replica sits next to v0, Lovable, Figma Make and Magic Patterns, see <a href="../prompt-to-ui-tools-compared/">prompt-to-UI tools compared</a>, and for Figma’s own library guidelines, <a href="../figma-make-and-figma-agent/">Figma Make and the Figma agent</a>.</p>""",
 zh="""<p>大多数「提示生成界面」工具都从一张空白页和模型心目中的「干净 SaaS 应用」开始。你会得到一个精致但千篇一律的结果，评审的第一个小时都花在解释「我们产品没有这种侧栏、不是这种按钮、空状态也不长这样」上。10 月 28 日，GitHub 开源了由 GitHub Design 与 Microsoft CoreAI Design 打造的原型工具 <strong>Replica</strong>，它想把顺序调过来：<em>先由设计师写好并批准规则，团队里的任何人再在规则之内做原型。</em></p>
<h2>Replica 是什么</h2>
<ul><li><strong>在哪里运行。</strong>在 GitHub Copilot 应用里。一个插件会加上 Replica 画布，把正在运行的原型显示在对话旁边：描述改动、试用、再迭代，都在一个地方完成。MIT 许可，由 GitHub 员工维护。</li>
<li><strong>四个部分。</strong>Starter（一个用来改造成你自己设计系统的 <em>Minimal</em> 应用，或已经接好微软 CoreAI 设计系统的 <em>CoreAI Sandbox</em>）、画布插件、可选的自托管 <strong>Replica Hub</strong>（用于发布与评论），以及只有在发布时才用得到的 GitHub 构建 Action。</li>
<li><strong>本地优先。</strong>本地原型只需要 macOS 或 Linux 上的 Copilot 应用、Git、Node.js 和 npm，不需要 Hub、Docker、域名或 GitHub 仓库。Hub 则需要一台 Linux 服务器、带通配符 DNS 和 HTTPS 的专用域名，以及 GitHub 侧的授权，并且由你的组织自己运维，不是 GitHub 托管。</li>
<li><strong>模型。</strong>可用 Copilot 套餐里 GitHub 托管的模型，也可接入自己的模型服务商（公开预览，按服务商条款计费）。查看或评审已完成的原型不需要 Copilot 订阅。</li></ul>
<h2>真正有意思的部分：把规范当作需要评审的产物</h2>
<p>你运行 <code>/setup-skills</code>，把 Copilot 指向经过批准的资料（产品文档、设计系统文档、组件和 Token 包），它会起草规范。文档写得很明确：起草不会让任何东西生效；设计师和设计系统维护者评审草稿，生效是另一次单独的批准。最终得到一组上下文文件，每个只管一件事：<code>DESIGN-SYSTEM.md</code> 管组件、Token 和模式，<code>PRODUCT-DESIGN.md</code> 管场景和状态行为，<code>RESPONSIVE-DESIGN.md</code> 管宽度，另外还有无障碍、浏览器验证、示例数据和仓库规则。</p>
<p>内置技能对这些上下文的用法很严格。设计系统评审技能只读生效目录，从不读草稿；标为 <code>proposed-default</code> 的规则只算提议，不算政策；缺少必要证据时，这项检查记为<em>人工检查，绝不算通过</em>，并且明确要求不要猜组件或 Token。<code>DESIGN-SYSTEM.md</code> 的模板也拒绝敷衍的上下文：「有 TextInput 组件」并不能回答「校验错误怎么展示」。</p>
<p>它还有反馈闭环。接上 Hub 后，<code>/review-hub-feedback</code> 会在多个原型的评审中找反复出现的主题，<code>/prepare-feedback-proposals</code> 把选中的发现变成对规范的修改提议，每条都先展示、再由你批准。评论改进的是规则，而不只是收到评论的那一个原型。</p>
<h2>我们的看法</h2>
<p>Replica 与其说是一个新的生成器，不如说是包在生成器外面的一套工作流：一个原型一个分支、只用示例数据、提交前先问、未经批准绝不推送或发布。对于产品经理、工程师和设计师一起做原型的团队，这个形态是对的。最有价值的想法可以直接带走：<strong>按负责方拆分规范、区分草稿和生效、让「不知道」显性化</strong>。我们见到的大多数智能体上下文文件，都是一份没人负责、没人评审、却被每个智能体奉为圣旨的长 <code>AGENTS.md</code>。</p>
<p>代价也是真实的。它默认你用 Copilot 应用（macOS 或 Linux）；要分享，还得有人愿意运维一个带通配符 DNS 的 Hub。画布从另一个源（origin）代理预览，所以依赖自身源做存储或登录的应用可能要额外处理。文档自己也提醒了 AI 生成界面里我们最常见的失败：智能体用<em>长得像的替代品</em>而不是你真正的组件。规范能降低这个风险，但不能消除它，所以要查 import，而不是看截图。</p>
<h2>清单：以设计系统为起点做原型（用不用 Replica 都适用）</h2>
<ol><li><strong>把规范拆成有人负责的文件。</strong>设计系统、产品行为、响应式宽度、无障碍、示例数据、仓库规则，各一个文件、各一个负责人。</li>
<li><strong>每条规则写清适用条件和依据。</strong>「页面级错误用 Banner，表单内用 InlineMessage，见文档链接」好过「用我们的组件」。</li>
<li><strong>草稿不进生效上下文。</strong>智能体写的规范先放草稿目录，设计师批准后才生效；没评审过的默认值标为「提议」。</li>
<li><strong>让未知可见。</strong>智能体找不到某个 Token 或模式的依据时，应该说出来，把检查留给人工，而不是编一个值。</li>
<li><strong>一个原型一个分支。</strong>默认分支保持为评审过的起点，绝不让原型改写它。</li>
<li><strong>只用示例数据。</strong>原型里永远不放生产凭据或客户数据。</li>
<li><strong>核对是不是真组件。</strong>在原型的 import 里搜你的组件包和封装层；一个长得像的 <code>&lt;button&gt;</code> 就算检查失败。</li>
<li><strong>把反馈导回规则。</strong>同一条评审意见出现两次，就去改规范文件，而不只是改原型。</li></ol>
<pre><code># .agents/context/  （一个文件管一件事，评审后才使用）
DESIGN-SYSTEM.md      # import、Token、布局、表单、反馈——每条附文档链接
PRODUCT-DESIGN.md     # 场景、保存、空 / 加载 / 错误状态行为
RESPONSIVE-DESIGN.md  # 必须支持的宽度，375px 下什么会折叠
ACCESSIBILITY.md      # 键盘、对比度、读屏要求
SEED-DATA.md          # 示例数据规则（不用真实客户）
REPOSITORY.md         # 必须使用的封装层、分支与提交规则
# drafts/ 永远不作为生效上下文读取；"proposed-default" ≠ 政策</code></pre>
<h2>UI Hub 能帮什么</h2>
<p>Replica 的效果取决于你喂给它的规范。<a href="../design-tokens-for-agents/">给智能体的设计 Token</a> 和 <a href="../claude-cursor-design-skills/">Claude 与 Cursor 的设计技能</a> 讲了怎么写这些上下文；<a href="../lint-agents-onto-your-design-system/">用 Lint 把智能体拉回你的设计系统</a> 讲了事后怎么抓住「长得像」的组件。Replica 和 v0、Lovable、Figma Make、Magic Patterns 的定位对比，见<a href="../prompt-to-ui-tools-compared/">提示生成界面工具横评</a>；Figma 自己的组件库规范，见 <a href="../figma-make-and-figma-agent/">Figma Make 与 Figma 智能体</a>。</p>""",
 refs=[('Introducing Replica, an open-source AI prototyping tool','GitHub Changelog','https://github.blog/changelog/2026-10-28-introducing-replica-an-open-source-ai-prototyping-tool/'),('github/replica','GitHub Design & Microsoft CoreAI Design, GitHub','https://github.com/github/replica'),('Create your first local prototype','Replica docs','https://github.com/github/replica/blob/main/docs/local-prototyping.md'),('Set up and configure your prototype environment','Replica docs','https://github.com/github/replica/blob/main/docs/prototype-environment.md'),('Replica setup and workflows (REPLICA.md)','Replica starters','https://github.com/github/replica/blob/main/starters/shared/REPLICA.md'),('Component design-system review skill','Replica starters','https://github.com/github/replica/blob/main/starters/shared/.agents/skills/component-design-system-review/SKILL.md'),('Design-system research template','Replica starters','https://github.com/github/replica/blob/main/starters/shared/.agents/context-templates/DESIGN-SYSTEM.md'),('GitHub open-sources Replica for prototypes built with your design system','Jordan Reid, ByteForward','https://bytefwd.com/github-replica-design-system-prototypes-local-hub/'),('GitHub Open-Sources Replica for On-Brand AI Prototypes','Nvdium','https://nvdium.com/en/articles/140006649'),('Figma product news and release notes','Figma','https://www.figma.com/release-notes/')]),
]
POSTS2 += [
dict(slug='canva-brush-edit-dont-regenerate', date='2026-10-30', cat='tools', series=None, featured=True, tags=['Canva Brush','Canva AI','AI editing','brand consistency','Krea'],
 t=T('Canva Brush: AI design moves from generating to editing',
     'Canva Brush：AI 设计正从「生成」走向「修改」',
     'Canva Brush：AI 設計正從「生成」走向「修改」',
     'Canva Brush：AIデザインは「生成」から「編集」へ',
     'Canva Brush: AI 디자인이 ‘생성’에서 ‘편집’으로 옮겨 간다',
     'Canva Brush: reka bentuk AI beralih daripada menjana kepada menyunting',
     'Canva Brush: thiết kế AI chuyển từ tạo mới sang chỉnh sửa',
     'Canva Brush : le design IA passe de la génération à l’édition',
     'Canva Brush: el diseño con IA pasa de generar a editar',
     'Canva Brush: KI-Design wechselt vom Generieren zum Bearbeiten'),
 s=T('On 29 October Canva Research launched Brush, a vision-language model trained to edit existing designs: it reads the layout, writes code to change elements, checks the page and keeps everything editable. Canva claims up to 69% faster and 46% cheaper edits than its previous agent. What it does, what the numbers do and don’t prove, how it compares with Krea’s brand-kit-first Ad Studio, and a checklist for edit prompts that change only what you meant.',
     '10 月 29 日，Canva Research 发布了 Brush：一个专门用来「修改现有设计」的视觉语言模型。它读懂版面结构，写代码改元素，再检查页面，结果全部保持可编辑。Canva 称它比自家上一代设计智能体快最多 69%、每次修改成本低 46%。本文讲它能做什么、这些数字能说明什么不能说明什么、它和 Krea 先抽品牌套件的 Ad Studio 有何不同，以及一份「只改你想改的」修改提示清单。',
     '10 月 29 日，Canva Research 發布了 Brush：一個專門用來「修改現有設計」的視覺語言模型。它讀懂版面結構，寫程式改元素，再檢查頁面，結果全部保持可編輯。Canva 稱它比自家上一代設計智慧體快最多 69%、每次修改成本低 46%。本文講它能做什麼、這些數字能說明什麼不能說明什麼、它和 Krea 先抽品牌套件的 Ad Studio 有何不同，以及一份「只改你想改的」修改提示清單。',
     '10月29日、Canva ResearchはBrushを発表した。既存デザインの編集に特化した視覚言語モデルで、レイアウトを読み取り、コードを書いて要素を変え、ページを確認し、結果はすべて編集可能なまま残る。Canvaは従来のエージェント比で最大69%速く、編集1回あたり46%安いとしている。何ができるか、数字が示すこと・示さないこと、ブランドキット先行のKrea Ad Studioとの違い、意図した部分だけを変える編集プロンプトのチェックリスト。',
     '10월 29일 Canva Research는 Brush를 공개했다. 기존 디자인 편집에 특화된 비전-언어 모델로, 레이아웃을 읽고 코드를 써서 요소를 바꾸고 페이지를 확인하며 결과는 모두 편집 가능한 상태로 남는다. Canva는 이전 에이전트보다 최대 69% 빠르고 편집당 비용이 46% 낮다고 말한다. 무엇을 하는지, 숫자가 증명하는 것과 아닌 것, 브랜드 키트부터 만드는 Krea Ad Studio와의 차이, 의도한 부분만 바꾸는 편집 프롬프트 체크리스트.',
     'Pada 29 Oktober Canva Research melancarkan Brush, model bahasa-visual yang dilatih untuk menyunting reka bentuk sedia ada: ia membaca susun atur, menulis kod untuk menukar elemen, menyemak halaman dan mengekalkan semuanya boleh disunting. Canva mendakwa suntingan sehingga 69% lebih pantas dan 46% lebih murah berbanding ejen sebelumnya. Apa yang ia buat, apa yang angka itu buktikan dan tidak, perbandingan dengan Ad Studio Krea yang bermula dengan kit jenama, dan senarai semak untuk prompt suntingan yang hanya mengubah apa yang anda maksudkan.',
     'Ngày 29/10, Canva Research ra mắt Brush, một mô hình thị giác-ngôn ngữ được huấn luyện để chỉnh sửa thiết kế có sẵn: nó đọc bố cục, viết code để thay đổi phần tử, kiểm tra trang và giữ mọi thứ có thể chỉnh sửa. Canva nói chỉnh sửa nhanh hơn tới 69% và rẻ hơn 46% so với agent trước. Nó làm gì, các con số chứng minh được gì và không, so sánh với Ad Studio của Krea (bắt đầu từ bộ nhận diện thương hiệu), và checklist cho prompt chỉnh sửa chỉ đổi đúng thứ bạn muốn.',
     'Le 29 octobre, Canva Research a lancé Brush, un modèle vision-langage entraîné à modifier des designs existants : il lit la mise en page, écrit du code pour changer les éléments, vérifie la page et garde tout modifiable. Canva annonce des modifications jusqu’à 69 % plus rapides et 46 % moins chères qu’avec son agent précédent. Ce qu’il fait, ce que ces chiffres prouvent ou non, la comparaison avec Ad Studio de Krea qui part d’un kit de marque, et une checklist de prompts d’édition qui ne changent que ce que vous vouliez.',
     'El 29 de octubre Canva Research lanzó Brush, un modelo de visión y lenguaje entrenado para editar diseños existentes: lee el layout, escribe código para cambiar elementos, revisa la página y deja todo editable. Canva afirma ediciones hasta un 69 % más rápidas y un 46 % más baratas que con su agente anterior. Qué hace, qué prueban y qué no esas cifras, cómo se compara con Ad Studio de Krea, que parte de un kit de marca, y una checklist de prompts de edición que cambian solo lo que querías.',
     'Am 29. Oktober hat Canva Research Brush vorgestellt, ein Vision-Language-Modell, das auf das Bearbeiten bestehender Designs trainiert ist: Es liest das Layout, schreibt Code, um Elemente zu ändern, prüft die Seite und lässt alles editierbar. Canva nennt bis zu 69 % schnellere und 46 % günstigere Bearbeitungen als mit dem bisherigen Agenten. Was es kann, was die Zahlen belegen und was nicht, der Vergleich mit Kreas Ad Studio, das beim Brand Kit beginnt, und eine Checkliste für Bearbeitungs-Prompts, die nur das ändern, was du meinst.'),
 en="""<p>The expensive moment in AI design is rarely the first prompt. It is the second one: “change only the headline”, and the tool rewrites the subtitle, moves the logo and picks a new blue. On 29 October Canva Research launched <strong>Brush</strong>, a vision-language model built for exactly that second prompt. Canva’s own framing is the useful part: generating a design is hard, but editing one is harder, because the model has to know what to change <em>and what must stay exactly as it is</em>.</p>
<h2>What Brush is</h2>
<ul><li><strong>An editing model, not an image model.</strong> Brush looks at an existing Canva design, works out how it is put together and applies the change you ask for, from one line of copy to every slide in a deck. It arrived a week after Canva Craft, the company’s image-generation model; Canva’s split is that Craft makes the image and Brush refines the design around it.</li>
<li><strong>It edits by writing code.</strong> Behind the chat, Brush runs an agentic loop: it writes and runs code that adjusts design elements, then inspects the rendered page to decide the next step. The result is ordinary Canva layers, so text, images, colours and layout stay editable by hand.</li>
<li><strong>How it was trained.</strong> Canva started from an open-weights model and post-trained it on real design and editing tasks, using design expertise and anonymised data from people who opted in, then large-scale reinforcement learning. The reward scores visual quality, whether the layout follows design principles and whether the task was actually done, with “good” defined by Canva’s professional designers.</li>
<li><strong>Availability.</strong> Canva Pro, for supported edits in Canva AI: open or attach a design and pick <em>Brush</em> in the Canva AI model dropdown. Wider access is promised but not dated. Still missing, by Canva’s own list: Brand Kit support, referencing attachments, and better handling of image-heavy layouts.</li></ul>
<h2>What the numbers do and don’t say</h2>
<p>Canva reports Brush as up to 69% faster on general editing tasks and 46% cheaper per edit task than its previous design agent, and says in internal testing it matched or beat that setup on most editing tasks, strongest at restyling and adapting designs to new formats. These are vendor numbers against Canva’s own earlier agent, not a public benchmark, and “up to” describes the best case. The more telling detail is why Canva cares: at hundreds of millions of users, a few cents per edit decides whether a feature can ship to everyone. A small specialised model that is cheap enough to run on every edit is a product decision as much as a research one.</p>
<h2>Two answers to the same problem</h2>
<p>The same evening, Krea launched <strong>Ad Studio</strong>, powered by its first Krea 3 “expert” model for advertising. You paste a brand’s website, it extracts a brand kit (logo, colours, typography) in a minute or two, then generates dozens of ads. Krea claims “full consistency” with the brand; no independent evaluation exists yet. Put side by side, the two launches show where AI design is heading: Krea gets consistency by <em>extracting rules first</em>, Canva by <em>starting from a design that already exists</em>. Both are moving away from the blank-canvas prompt, the same direction we saw with <a href="../annotate-dont-describe-visual-prompts/">visual prompts in Cursor, v0 and Lovable</a> and <a href="../layers-brand-kits-json-ai-visuals/">JSON brand kits for AI visuals</a>.</p>
<h2>Our take</h2>
<p>An edit model that works through code on real layers is the right architecture: edits become operations on named elements, which can be scoped, repeated across pages and undone, instead of a fresh image that only resembles your design. The catch for teams is the missing Brand Kit support. Today Brush can see your design but not your brand rules, so “keep it on-brand” is still your job, and the best way to do it is to put the values in the prompt. Treat “restyle” and “resize for Instagram” as the sweet spot Canva itself names, and be more careful with image-heavy layouts until the promised fix lands.</p>
<h2>Checklist: edit prompts that change only what you meant</h2>
<ol><li><strong>Name the scope.</strong> Which pages and which elements: “slide titles on pages 2–5”, not “the deck”.</li>
<li><strong>Name what must not move.</strong> Body copy, images, logo position, page order. An edit model is only as precise as its “keep” list.</li>
<li><strong>Give values, not adjectives.</strong> Hex colours, font names and sizes beat “more premium”, especially while the model can’t read your Brand Kit.</li>
<li><strong>One intent per prompt.</strong> Batch only uniform changes (every header); split mixed requests into separate turns so you can check each.</li>
<li><strong>For format remixes, say what to drop.</strong> A slide becoming a 1080×1350 post needs to lose text, not shrink it.</li>
<li><strong>Duplicate before sweeping edits.</strong> Multi-page changes are where unrequested drift hides; keep the original to compare.</li>
<li><strong>Check the pages you didn’t mention.</strong> Look for text overflow, contrast below 4.5:1, broken alignment and changes outside your scope.</li>
<li><strong>Finish by hand.</strong> The output is normal layers; the last 10% is faster in the editor than in another prompt.</li></ol>
<pre><code>scope:   pages 2–5 · slide titles only
change:  font → Playfair Display 40 · colour #1F2A44
keep:    body copy · images · logo position · page order
check:   titles ≤ 2 lines · contrast ≥ 4.5:1 · nothing else moved</code></pre>
<h2>How UI Hub helps</h2>
<p>The “keep” list works best when your values already have names. <a href="../design-tokens-for-agents/">Design tokens for agents</a> covers writing them down, and <a href="../lint-agents-onto-your-design-system/">linting agents onto your design system</a> covers catching one-off values after an AI edit. For pointing at elements instead of describing them, see <a href="../annotate-dont-describe-visual-prompts/">Point, don’t describe</a>; for how design tools are opening to outside agents, see <a href="../agents-drive-design-tools-framer-weave-app-studio/">agents that drive design tools</a>.</p>""",
 zh="""<p>AI 设计里最贵的往往不是第一条提示，而是第二条：「只改标题」，结果工具连副标题一起重写，把 Logo 挪了位置，还换了一种蓝。10 月 29 日，Canva Research 发布了 <strong>Brush</strong>，一个专门为这「第二条提示」打造的视觉语言模型。Canva 自己的说法很说明问题：生成设计已经很难，修改设计更难，因为模型既要知道改什么，<em>也要知道什么必须原封不动</em>。</p>
<h2>Brush 是什么</h2>
<ul><li><strong>是修改模型，不是图像模型。</strong>Brush 会看一份现有的 Canva 设计，弄清它的结构，再按你的要求修改，小到一行文案，大到整份演示文稿的每一页。它比 Canva 的图像生成模型 Canva Craft 晚一周推出；Canva 的分工是：Craft 负责生成图像，Brush 负责把图像周围的设计改好。</li>
<li><strong>它靠写代码来改。</strong>在对话背后，Brush 跑的是一个智能体循环：写代码、运行代码去调整设计元素，再检查渲染出来的页面，决定下一步。结果是普通的 Canva 图层，文字、图片、颜色和版式都还能手动编辑。</li>
<li><strong>怎么训练的。</strong>Canva 从一个开放权重模型出发，用真实的设计和修改任务做后训练，数据来自设计专业知识和自愿参与改进的用户的匿名数据，再加上大规模强化学习。奖励会评估视觉质量、版式是否符合设计原则、任务是否真的完成，而「好」的标准由 Canva 的专业设计师来定。</li>
<li><strong>可用范围。</strong>Canva Pro 用户，在 Canva AI 中用于支持的修改：打开或附上一份设计，在 Canva AI 的模型下拉菜单里选 <em>Brush</em>。更大范围开放已承诺，但没有日期。按 Canva 自己列的清单，目前还缺：品牌套件（Brand Kit）支持、引用附件，以及对图片密集版式的更好处理。</li></ul>
<h2>这些数字能说明什么</h2>
<p>Canva 称，Brush 在一般修改任务上比自家上一代设计智能体快最多 69%，每次修改成本低 46%；内部测试中，大多数修改任务的质量持平或更好，改风格和改尺寸适配新格式时表现最强。这些是厂商拿自己旧版智能体做的对比，不是公开基准，「最多」描述的是最好情况。更值得注意的是 Canva 为什么在意成本：用户以亿计，每次修改多几美分，就决定了一个功能能不能给所有人用。一个便宜到每次修改都能跑的小型专用模型，既是研究决定，也是产品决定。</p>
<h2>同一个问题的两种解法</h2>
<p>同一天晚上，Krea 发布了 <strong>Ad Studio</strong>，由它第一个面向广告的 Krea 3「专家」模型驱动。粘贴品牌官网链接，它会在一两分钟内抽出品牌套件（Logo、颜色、字体），然后生成几十张广告。Krea 声称与品牌「完全一致」，目前还没有独立评测。两次发布放在一起，能看出 AI 设计的走向：Krea 靠<em>先抽规则</em>来保证一致，Canva 靠<em>从已有设计出发</em>。两者都在离开「空白画布 + 一句提示」，和我们在 <a href="../annotate-dont-describe-visual-prompts/">Cursor、v0、Lovable 的可视化提示</a>、<a href="../layers-brand-kits-json-ai-visuals/">给 AI 视觉用的 JSON 品牌套件</a>里看到的方向一致。</p>
<h2>我们的看法</h2>
<p>在真实图层上、通过代码来改的修改模型，架构是对的：修改变成了对具名元素的操作，可以限定范围、跨页重复、可以撤销，而不是生成一张只是「长得像」你设计的新图。对团队来说，最大的问题是还不支持品牌套件。现在 Brush 能看到你的设计，却看不到你的品牌规则，所以「保持品牌一致」仍然是你的事，最好的办法是把具体数值写进提示。把「改风格」和「改成 Instagram 尺寸」当作 Canva 自己点名的强项；在承诺的改进上线之前，处理图片密集的版式要更小心。</p>
<h2>清单：只改你想改的修改提示</h2>
<ol><li><strong>写明范围。</strong>哪几页、哪些元素：「第 2–5 页的标题」，而不是「这份演示文稿」。</li>
<li><strong>写明哪些不能动。</strong>正文、图片、Logo 位置、页面顺序。修改模型有多精确，取决于你的「保持」清单。</li>
<li><strong>给数值，不给形容词。</strong>色值、字体名和字号，好过「更高级一点」，尤其是在模型还读不到你的品牌套件的时候。</li>
<li><strong>一条提示一个意图。</strong>只有统一的改动（所有标题）才批量做；混合需求拆成几轮，每轮都能检查。</li>
<li><strong>改格式时说清删什么。</strong>一页幻灯片改成 1080×1350 的帖子，应该删字，而不是把字缩小。</li>
<li><strong>大范围修改前先复制一份。</strong>多页修改最容易藏着没要求的偏移，留着原稿好对比。</li>
<li><strong>检查你没提到的页面。</strong>看有没有文字溢出、对比度低于 4.5:1、对齐被破坏，以及范围之外的改动。</li>
<li><strong>最后手动收尾。</strong>产出是普通图层，最后 10% 在编辑器里改比再写一条提示更快。</li></ol>
<pre><code>范围：  第 2–5 页 · 仅幻灯片标题
修改：  字体 → Playfair Display 40 · 颜色 #1F2A44
保持：  正文 · 图片 · Logo 位置 · 页面顺序
检查：  标题不超过 2 行 · 对比度 ≥ 4.5:1 · 其他都没动</code></pre>
<h2>UI Hub 能帮什么</h2>
<p>「保持」清单在你的数值已经有名字时最好用。<a href="../design-tokens-for-agents/">给智能体的设计 Token</a> 讲了怎么把它们写下来，<a href="../lint-agents-onto-your-design-system/">用 Lint 把智能体拉回你的设计系统</a> 讲了 AI 修改之后怎么抓住一次性数值。想用「指」代替「描述」，见<a href="../annotate-dont-describe-visual-prompts/">指出来，而不是描述</a>；设计工具如何向外部智能体开放，见<a href="../agents-drive-design-tools-framer-weave-app-studio/">驱动设计工具的智能体</a>。</p>""",
 refs=[('Introducing Canva Brush, a vision-language model for design','Canva Research Team, Canva Newsroom','https://www.canva.com/newsroom/news/canva-brush/'),('Introducing Canva Craft','Canva Newsroom','https://www.canva.com/newsroom/news/canva-craft/'),('Canva launches AI design editing model ‘Brush’','Capital Brief','https://www.capitalbrief.com/briefing/canva-launches-ai-design-editing-model-brush-48352e11-c62c-4319-973a-490efa945f92/'),('Canva launches Brush, an in-house vision-language model that edits existing designs','Aipolix','https://aipolix.com/en-us/news/canva-brush-vision-language-model-design-editing'),('Canva Research unveils Brush vision-language model for design editing','AI Compass','https://ashutoshai.com/ai-compass/2026/10/29/canva-brush/'),('Krea launches Ad Studio, powered by the first Krea 3 “expert” dedicated to advertising','Iris & Tomo, Neural Brew','https://neuralbrew.ai/en/articles/2026/10/krea-launches-ad-studio-first-expert/'),('Ad Studio','Krea','https://www.krea.ai/ad-studio'),('Canva AI','Canva','https://www.canva.com/ai/')]),
]
POSTS2 += [
dict(slug='generative-ui-catalogs-surfaces-a2ui', date='2026-10-31', cat='agents', series=None, featured=True, tags=['CopilotKit','A2UI','generative UI','component catalog','design systems'],
 t=T('Generative UI gets a design system: CopilotKit catalogs, surfaces and A2UI 1.0',
     '生成式界面有了设计系统：CopilotKit 的组件目录、页面区域与 A2UI 1.0',
     '生成式介面有了設計系統：CopilotKit 的元件目錄、頁面區域與 A2UI 1.0',
     '生成UIにデザインシステムが入る：CopilotKitのカタログ、サーフェス、A2UI 1.0',
     '생성형 UI에 디자인 시스템이 들어오다: CopilotKit 카탈로그, 서피스, A2UI 1.0',
     'UI generatif kini ada sistem reka bentuk: katalog, permukaan CopilotKit dan A2UI 1.0',
     'Generative UI có hệ thống thiết kế: catalog, surface của CopilotKit và A2UI 1.0',
     'L’UI générative a enfin un design system : catalogues, surfaces CopilotKit et A2UI 1.0',
     'La UI generativa ya tiene sistema de diseño: catálogos, superficies de CopilotKit y A2UI 1.0',
     'Generative UI bekommt ein Designsystem: CopilotKit-Kataloge, Surfaces und A2UI 1.0'),
 s=T('On 29 October CopilotKit shipped a 70-component catalog, page “surfaces” and a markdown mode for generative UI, all on Google’s A2UI 1.0 protocol; two days earlier Google added A2UI Express, a compact format that cuts tokens up to 3×. The shift for designers: when an agent builds screens, the component catalog becomes the design system’s contract. What changed, what it means for UI teams, and a checklist for a catalog agents can’t break.',
     '10 月 29 日，CopilotKit 为生成式界面发布了 70 个组件的标准目录、可放在页面任意位置的「surface 区域」和 Markdown 模式，全部基于 Google 的 A2UI 1.0 协议；两天前 Google 推出了 A2UI Express，一种最多省 3 倍 token 的紧凑格式。对设计师来说，变化在于：当智能体来搭界面，组件目录就成了设计系统的「合同」。本文讲改了什么、对 UI 团队意味着什么，以及一份让智能体「改不坏」的组件目录清单。',
     '10 月 29 日，CopilotKit 為生成式介面發布了 70 個元件的標準目錄、可放在頁面任意位置的「surface 區域」和 Markdown 模式，全部基於 Google 的 A2UI 1.0 協定；兩天前 Google 推出了 A2UI Express，一種最多省 3 倍 token 的緊湊格式。對設計師來說，變化在於：當智慧體來搭介面，元件目錄就成了設計系統的「合約」。本文講改了什麼、對 UI 團隊意味著什麼，以及一份讓智慧體「改不壞」的元件目錄清單。',
     '10月29日、CopilotKitは生成UI向けに70コンポーネントの標準カタログ、ページ上の「サーフェス」、マークダウンモードを公開した。いずれもGoogleのA2UI 1.0プロトコル上に構築されている。その2日前、Googleはトークンを最大3分の1にするコンパクト形式A2UI Expressを追加した。デザイナーにとっての変化は、エージェントが画面を組むとき、コンポーネントカタログがデザインシステムの契約になることだ。何が変わったか、UIチームへの意味、エージェントに壊されないカタログのチェックリスト。',
     '10월 29일 CopilotKit는 생성형 UI용 70개 컴포넌트 표준 카탈로그, 페이지 위의 ‘서피스’, 마크다운 모드를 내놓았다. 모두 Google의 A2UI 1.0 프로토콜 위에 만들어졌다. 이틀 전 Google은 토큰을 최대 3배 줄이는 간결한 형식 A2UI Express를 추가했다. 디자이너에게 달라지는 점은, 에이전트가 화면을 만들 때 컴포넌트 카탈로그가 디자인 시스템의 계약이 된다는 것이다. 무엇이 바뀌었는지, UI 팀에 주는 의미, 에이전트가 깨뜨릴 수 없는 카탈로그 체크리스트.',
     'Pada 29 Oktober CopilotKit melancarkan katalog 70 komponen, “permukaan” halaman dan mod markdown untuk UI generatif, semuanya di atas protokol A2UI 1.0 Google; dua hari sebelumnya Google menambah A2UI Express, format padat yang mengurangkan token sehingga 3×. Perubahan bagi pereka: apabila ejen membina skrin, katalog komponen menjadi kontrak sistem reka bentuk. Apa yang berubah, maksudnya bagi pasukan UI, dan senarai semak untuk katalog yang tidak boleh dirosakkan ejen.',
     'Ngày 29/10, CopilotKit ra mắt catalog 70 component, “surface” trên trang và chế độ markdown cho generative UI, tất cả dựa trên giao thức A2UI 1.0 của Google; hai ngày trước, Google thêm A2UI Express, định dạng gọn giúp giảm token tới 3 lần. Thay đổi với designer: khi agent dựng màn hình, catalog component trở thành hợp đồng của hệ thống thiết kế. Điều gì thay đổi, ý nghĩa với đội UI, và checklist cho một catalog mà agent không thể phá.',
     'Le 29 octobre, CopilotKit a publié un catalogue de 70 composants, des « surfaces » de page et un mode markdown pour l’UI générative, le tout sur le protocole A2UI 1.0 de Google ; deux jours plus tôt, Google ajoutait A2UI Express, un format compact qui divise les tokens jusqu’à 3. Le changement pour les designers : quand un agent construit les écrans, le catalogue de composants devient le contrat du design system. Ce qui change, ce que cela implique pour les équipes UI, et une checklist pour un catalogue que l’agent ne peut pas casser.',
     'El 29 de octubre CopilotKit lanzó un catálogo de 70 componentes, “superficies” en la página y un modo markdown para UI generativa, todo sobre el protocolo A2UI 1.0 de Google; dos días antes Google añadió A2UI Express, un formato compacto que reduce los tokens hasta 3×. El cambio para diseñadores: cuando un agente construye pantallas, el catálogo de componentes se convierte en el contrato del sistema de diseño. Qué cambió, qué significa para los equipos de UI y una checklist para un catálogo que el agente no pueda romper.',
     'Am 29. Oktober hat CopilotKit einen Katalog mit 70 Komponenten, Seiten-„Surfaces“ und einen Markdown-Modus für Generative UI veröffentlicht, alles auf Googles A2UI-1.0-Protokoll; zwei Tage zuvor brachte Google A2UI Express, ein kompaktes Format mit bis zu 3× weniger Tokens. Der Wandel für Designer: Wenn ein Agent Screens baut, wird der Komponentenkatalog zum Vertrag des Designsystems. Was sich geändert hat, was es für UI-Teams bedeutet und eine Checkliste für einen Katalog, den der Agent nicht kaputt machen kann.'),
 en="""<p>For two years “generative UI” mostly meant a chatbot that sometimes drew a chart inside its bubble. This week it grew up. On 29 October CopilotKit released a large upgrade to its generative UI layer: a standard catalog of 70 components, <strong>surfaces</strong> that let an agent render into named areas of your actual page, and a markdown mode where text and components stream in the same answer. Underneath sits <strong>A2UI</strong>, the open protocol Google started (with CopilotKit and others contributing), whose 1.0 spec is now a release candidate. Two days earlier Google’s A2UI team shipped a faster way for models to write it. Read together, these releases move an important decision from engineers to design-system owners: <em>which components an agent may use, where, and with what props</em>.</p>
<h2>What shipped this week</h2>
<ul><li><strong>A standard catalog of 70 components.</strong> Layout, text, form inputs, tables, images, video, charts (built on Recharts) and maps (built on MapLibre), plus ready-made blocks such as link previews, citations, product cards and follow-up suggestions. CopilotKit says 18 of them are A2UI’s basic components and 52 are its own.</li>
<li><strong>Your components, typed.</strong> You register your own with <code>createGenerativeUI</code>: each entry has a description the agent reads to decide when to use it, and a props schema (Zod, Valibot or ArkType). Three switches decide how your catalog sits next to the standard one: <code>extends</code> keeps both, <code>omit</code> removes components so the agent never sees them, and <code>overrides</code> replaces a standard component with yours.</li>
<li><strong>Surfaces outside the chat.</strong> Wrap any area in <code>GenerativeUISurface</code> with an id, a plain-language description of what belongs there, a list of allowed components and a fallback (your normal hand-built UI). The agent only sees a target while it is on screen; anything outside the allowed list is rejected and the agent is told why.</li>
<li><strong>Two streaming modes.</strong> Tool mode (the default) sends UI through a tool call and renders it piece by piece; markdown mode lets the agent write UI straight into its reply. Sliders, live values and form checks run in the browser, so interacting with generated UI costs no extra tokens.</li>
<li><strong>Guardrails and debugging.</strong> Every piece is checked against the catalog before it renders, generated UI never executes code on your page, each component gets its own error boundary, and a new Inspector pane shows what rendered, what was rejected and the exact prompt the model saw. CopilotKit labels all of this experimental until A2UI 1.0 is final.</li></ul>
<h2>Why A2UI matters to designers</h2>
<p>A2UI’s core idea is simple: an agent does not send HTML or code, it sends a <em>declarative description</em> of components from a catalog the client has approved, and the client renders them with its own native widgets (renderers exist for Angular, Flutter, Lit, React and markdown). That makes the catalog the only vocabulary the agent has. On 27 October Google added swappable “inference formats”: the model can write <strong>A2UI Express</strong>, a compact line-by-line syntax that the SDK compiles into standard A2UI messages. Google reports up to 3× fewer tokens and up to 3× lower latency than writing the JSON directly, and much bigger speed-ups when a small decision model only picks between layouts you designed in advance. The detail that matters for design quality: both the prompt and the compiler are generated from your catalog schema, so a format cannot describe a component or property your catalog does not have. On 30 October the project also published its first CLI, which generates typed builders from catalog schemas.</p>
<h2>Our take</h2>
<p>This is the right shape for agent-built interfaces, and it changes who owns the result. When an agent can only compose from a typed catalog, “on-brand” stops being a hope you put in a prompt and becomes a property of the system: the agent literally cannot emit a neon gradient button if no such variant exists. The flip side is that every weakness in the catalog becomes visible. A vague description (“a card”) makes the agent pick it for everything; a free-text <code>variant</code> prop invites invented styles; a surface without a good fallback leaves a hole when the model is slow or wrong. So the craft moves upstream: designers should write component descriptions like usage guidelines, keep prop types narrow, and design the empty, streaming and error states of every surface, because those are now part of the product. Two caveats: the CopilotKit API is explicitly experimental, and the speed numbers are vendor-reported best cases, so pin versions and measure on your own screens.</p>
<h2>Checklist: a catalog an agent can’t break</h2>
<ol><li><strong>Start narrow.</strong> Give each surface only the components it needs (<code>components</code> or <code>omit</code>); a product row should accept product cards, not sliders. Smaller lists also mean smaller prompts.</li>
<li><strong>Override the basics.</strong> Replace the standard Button, Card and Input with your own so tokens, radii and focus styles come from your system, not the library default.</li>
<li><strong>Write descriptions as rules.</strong> Say when to use a component, when not to, and what to use instead. The agent reads these on every run.</li>
<li><strong>Type props tightly.</strong> Enums for variants and tones, numbers for numbers, length limits for labels. Free strings are where invented styles come from.</li>
<li><strong>Design the fallback first.</strong> Every surface should render your real hand-designed UI until the agent takes over, and again after it lets go.</li>
<li><strong>Design the in-between states.</strong> Streaming skeletons, a per-component error fallback, and what the area looks like when the agent removes its surface.</li>
<li><strong>Keep user input sacred.</strong> Values the user typed should never be overwritten by the agent; check that your setup enforces it.</li>
<li><strong>Theme with tokens and test dark mode.</strong> Generated screens should pass the same contrast checks (4.5:1 for body text) as hand-built ones.</li>
<li><strong>Read the rejections.</strong> Review what the Inspector rejected each week: a repeated rejection means a missing component or a misleading description, not a bad model.</li>
<li><strong>Match the mode to the screen.</strong> Fixed layouts are faster as predefined templates chosen by the agent; reserve free composition for screens that really vary.</li></ol>
<pre><code>StatCard
  use when:  the user asks about one metric over a period
  not for:   more than 4 numbers (use Table) · trends (use LineChart)
  props:     label: string ≤ 24 · value: number · delta: number
             tone: "up" | "down" | "flat"
  tokens:    surface/raised · text/muted · accent only when tone = "up"</code></pre>
<h2>How UI Hub helps</h2>
<p>A good catalog starts from named values: <a href="../design-tokens-for-agents/">design tokens for agents</a> covers writing them down, and <a href="../lint-agents-onto-your-design-system/">linting agents onto your design system</a> covers catching one-off values afterwards. For the chat side of agent interfaces (steps, tool calls, code output), see <a href="../shadcn-trace-and-ai-elements/">shadcn Trace and AI Elements</a>; for approval and interruption patterns when an agent acts on a page, see <a href="../agent-approval-ui-budgets-interruptions/">agent approval UI</a>. The component pages on UI Hub are a useful shopping list when you decide what belongs in your catalog.</p>""",
 zh="""<p>两年来，「生成式界面」大多意味着一个偶尔在气泡里画张图表的聊天机器人。这周它长大了。10 月 29 日，CopilotKit 大幅升级了它的生成式界面层：一个 70 个组件的标准目录，让智能体把界面渲染到你真实页面上指定区域的 <strong>surface（页面区域）</strong>，以及让文字和组件在同一条回答里一起流式输出的 Markdown 模式。底层是 <strong>A2UI</strong>，由 Google 发起、CopilotKit 等参与贡献的开放协议，1.0 规范现在处于候选版本。两天前，Google 的 A2UI 团队还发布了一种让模型更快写出 A2UI 的方式。放在一起看，这几次发布把一个重要决定从工程师手里交给了设计系统的负责人：<em>智能体能用哪些组件、用在哪里、带什么属性</em>。</p>
<h2>这周发布了什么</h2>
<ul><li><strong>70 个组件的标准目录。</strong>布局、文字、表单输入、表格、图片、视频、图表（基于 Recharts）和地图（基于 MapLibre），外加链接预览、引用、商品卡片、追问建议等现成区块。CopilotKit 说其中 18 个是 A2UI 的基础组件，另外 52 个是它自己的。</li>
<li><strong>你自己的组件，带类型。</strong>用 <code>createGenerativeUI</code> 注册：每个组件有一段描述，智能体靠它决定什么时候用；还有一个属性 schema（Zod、Valibot 或 ArkType）。三个开关决定你的目录和标准目录怎么共存：<code>extends</code> 两者都保留，<code>omit</code> 移除组件、让智能体根本看不到，<code>overrides</code> 用你的组件替换标准组件。</li>
<li><strong>聊天框之外的 surface。</strong>用 <code>GenerativeUISurface</code> 包住页面上任意区域，给它一个 id、一段说明这里该放什么的文字、允许使用的组件列表，以及一个兜底内容（你平时手工做的界面）。智能体只有在该区域出现在屏幕上时才看得到它；不在允许列表里的组件会被拒绝，并告诉智能体原因。</li>
<li><strong>两种流式模式。</strong>工具模式（默认）通过工具调用发送界面，逐块渲染；Markdown 模式让智能体直接把界面写进回复。滑块、实时数值和表单校验都在浏览器里运行，所以和生成的界面交互不额外消耗 token。</li>
<li><strong>防护与调试。</strong>每一块在渲染前都会对照目录检查，生成的界面不会在你的页面上执行代码，每个组件有自己的错误边界，Inspector 新增的面板会显示渲染了什么、拒绝了什么、模型看到的完整提示。在 A2UI 1.0 定稿之前，CopilotKit 把这些都标为实验功能。</li></ul>
<h2>为什么 A2UI 和设计师有关</h2>
<p>A2UI 的核心思路很简单：智能体不发 HTML，也不发代码，而是发一份<em>声明式描述</em>，里面只能用客户端批准过的目录里的组件，客户端再用自己的原生组件渲染（已有 Angular、Flutter、Lit、React 和 Markdown 渲染器）。这样，目录就是智能体唯一的词汇表。10 月 27 日，Google 加入了可替换的「推理格式」：模型可以写 <strong>A2UI Express</strong>，一种逐行书写的紧凑语法，再由 SDK 编译成标准 A2UI 消息。Google 称它比直接写 JSON 最多少用 3 倍 token、延迟最多降 3 倍；如果只让一个小型决策模型在你预先设计好的版式之间挑选，速度还能快得多。对设计质量最关键的一点是：提示和编译器都从你的目录 schema 生成，所以这种格式描述不出目录里没有的组件或属性。10 月 30 日，项目还发布了第一个命令行工具，可以从目录 schema 生成带类型的构建器。</p>
<h2>我们的看法</h2>
<p>这是智能体搭界面的正确形态，而且它改变了「结果归谁负责」。当智能体只能从带类型的目录里组合，「符合品牌」就不再是写在提示里的愿望，而是系统本身的属性：如果目录里没有霓虹渐变按钮这个变体，智能体就根本输出不了。反过来，目录的每个弱点都会暴露出来。描述含糊（「一张卡片」），智能体就什么都用它；<code>variant</code> 属性是自由文本，就等于邀请它发明样式；surface 没有好的兜底，模型慢了或错了就会留下一个洞。所以手艺往上游移：设计师应该把组件描述写成使用规范，把属性类型收窄，并为每个 surface 设计空状态、加载中和出错状态，因为这些现在都是产品的一部分。两点提醒：CopilotKit 的 API 明确是实验性的，速度数字是厂商给出的最好情况，所以要锁定版本，在你自己的页面上实测。</p>
<h2>清单：让智能体改不坏的组件目录</h2>
<ol><li><strong>从窄开始。</strong>每个 surface 只给它需要的组件（<code>components</code> 或 <code>omit</code>）；商品行只接受商品卡片，不接受滑块。列表越短，提示也越短。</li>
<li><strong>替换基础组件。</strong>用你自己的 Button、Card、Input 替换标准组件，让 token、圆角和焦点样式来自你的系统，而不是库的默认值。</li>
<li><strong>把描述写成规则。</strong>写清什么时候用、什么时候不用、不用时换成什么。智能体每次运行都会读。</li>
<li><strong>收窄属性类型。</strong>变体和语气用枚举，数字用数字类型，标签限制长度。自由字符串正是「发明样式」的来源。</li>
<li><strong>先设计兜底内容。</strong>每个 surface 在智能体接手之前、以及放手之后，都应该显示你手工设计的真实界面。</li>
<li><strong>设计中间状态。</strong>流式加载骨架屏、单个组件的出错兜底，以及智能体移除 surface 后这块区域的样子。</li>
<li><strong>用户输入不能动。</strong>用户已经填写的值绝不能被智能体覆盖，确认你的配置做到了这一点。</li>
<li><strong>用 token 定主题，测暗色模式。</strong>生成的页面应该和手工页面通过同样的对比度检查（正文 4.5:1）。</li>
<li><strong>看被拒绝的记录。</strong>每周看一遍 Inspector 里被拒绝的内容：反复被拒，说明缺组件或描述有误导，而不是模型不行。</li>
<li><strong>按页面选模式。</strong>固定版式更适合预先设计好的模板、由智能体挑选；自由组合留给真正多变的页面。</li></ol>
<pre><code>StatCard（指标卡）
  何时用：  用户询问某个时间段内的单个指标
  不用于：  超过 4 个数字（改用 Table）· 趋势（改用 LineChart）
  属性：    label: string ≤ 24 · value: number · delta: number
            tone: "up" | "down" | "flat"
  token：   surface/raised · text/muted · 仅 tone = "up" 时用强调色</code></pre>
<h2>UI Hub 能帮什么</h2>
<p>好的组件目录从有名字的数值开始：<a href="../design-tokens-for-agents/">给智能体的设计 Token</a> 讲了怎么把它们写下来，<a href="../lint-agents-onto-your-design-system/">用 Lint 把智能体拉回你的设计系统</a> 讲了事后怎么抓住一次性数值。智能体界面里聊天那一侧（步骤、工具调用、代码输出），见 <a href="../shadcn-trace-and-ai-elements/">shadcn Trace 与 AI Elements</a>；智能体在页面上动手时的审批与打断模式，见<a href="../agent-approval-ui-budgets-interruptions/">智能体审批界面</a>。决定目录里该放什么组件时，UI Hub 的组件页面是一份好用的清单。</p>""",
 refs=[('New in Generative UI: Catalogs, Surfaces and Markdown Mode','Anmol Baranwal and Eli Berman, CopilotKit Blog','https://www.copilotkit.ai/blog/new-generative-ui'),('Surfaces','CopilotKit Docs','https://docs.copilotkit.ai/generative-ui/components/surfaces'),('Catalogs','CopilotKit Docs','https://docs.copilotkit.ai/generative-ui/components/catalogs'),('Standard catalog','CopilotKit Docs','https://docs.copilotkit.ai/generative-ui/components/standard-catalog'),('Generative UI shop example','CopilotKit, GitHub','https://github.com/CopilotKit/CopilotKit/tree/main/examples/v2/generative-ui-shop'),('A2UI: a generative UI protocol for cross-platform agentic experiences','A2UI project','https://a2ui.org/'),('Fast, reliable A2UI, with swappable inference formats','Vishal Motwani, Google Developers Blog','https://developers.googleblog.com/en/fast-reliable-a2ui/'),('A2UI Express technical specification','A2UI project','https://a2ui.org/specification/proposals/express/a2ui_express/'),('A2UI CLI v0.1.0 release','a2ui-project, GitHub','https://github.com/a2ui-project/a2ui/releases/tag/cli-v0.1.0'),('Generative UI timeline','AG-UI.AI','https://ag-ui.ai/en/timeline')]),
]
POSTS2 += [
dict(slug='ai-design-tool-shutdowns-keep-work-portable', date='2026-11-01', cat='workflow', series=None, featured=True, tags=['Motiff','Visily','export','design tokens','portability'],
 t=T('Two AI design tools closed on 31 October: how to keep your design work portable',
     '两款 AI 设计工具在 10 月 31 日关停：怎样让你的设计成果随时能带走',
     '兩款 AI 設計工具在 10 月 31 日關閉：怎樣讓你的設計成果隨時能帶走',
     '10月31日、2つのAIデザインツールが終了：デザイン資産を持ち出せる状態に保つ方法',
     '10월 31일 두 AI 디자인 도구가 문을 닫았다: 디자인 작업을 언제든 옮길 수 있게 지키는 법',
     'Dua alat reka bentuk AI ditutup pada 31 Oktober: cara memastikan kerja reka bentuk anda mudah dipindah',
     'Hai công cụ thiết kế AI đóng cửa ngày 31/10: cách giữ thành quả thiết kế luôn mang đi được',
     'Deux outils de design IA ont fermé le 31 octobre : comment garder votre travail portable',
     'Dos herramientas de diseño con IA cerraron el 31 de octubre: cómo mantener tu trabajo portable',
     'Zwei KI-Designtools schlossen am 31. Oktober: So bleibt deine Designarbeit portabel'),
 s=T('Motiff’s export window and Visily’s service both ended on 31 October 2026; Visily deletes all data on 30 November. Neither had an open file format, so what survived was whatever teams exported in time. What happened, why AI design tools are consolidating, the export ladder from code down to PNG, and a ten-point exit plan to set up before you adopt the next tool.',
     'Motiff 的数据导出窗口和 Visily 的服务都在 2026 年 10 月 31 日结束；Visily 会在 11 月 30 日删除全部数据。两者都没有开放的文件格式，最后留下来的只有团队及时导出的东西。本文讲发生了什么、AI 设计工具为什么在收缩、从代码到 PNG 的「导出阶梯」，以及一份在采用下一个工具之前就该定好的十条退出计划。',
     'Motiff 的資料匯出窗口和 Visily 的服務都在 2026 年 10 月 31 日結束；Visily 會在 11 月 30 日刪除全部資料。兩者都沒有開放的檔案格式，最後留下來的只有團隊及時匯出的東西。本文講發生了什麼、AI 設計工具為什麼在收縮、從程式碼到 PNG 的「匯出階梯」，以及一份在採用下一個工具之前就該定好的十條退出計畫。',
     'Motiffのデータエクスポート期間とVisilyのサービスは、どちらも2026年10月31日に終了した。Visilyは11月30日に全データを削除する。どちらにも公開ファイル形式はなく、残ったのはチームが期限内に書き出したものだけだった。何が起きたか、AIデザインツールが集約に向かう理由、コードからPNGまでの「エクスポートの階段」、次のツールを導入する前に用意したい10項目の撤退計画。',
     'Motiff의 데이터 내보내기 기간과 Visily의 서비스가 모두 2026년 10월 31일에 끝났고, Visily는 11월 30일에 모든 데이터를 삭제한다. 둘 다 공개 파일 형식이 없어서, 남은 것은 팀이 제때 내보낸 것뿐이었다. 무슨 일이 있었는지, AI 디자인 도구가 왜 정리되고 있는지, 코드에서 PNG까지의 ‘내보내기 사다리’, 다음 도구를 도입하기 전에 세워 둘 10가지 탈출 계획.',
     'Tetingkap eksport data Motiff dan perkhidmatan Visily kedua-duanya tamat pada 31 Oktober 2026; Visily memadam semua data pada 30 November. Tiada satu pun mempunyai format fail terbuka, jadi yang tinggal hanyalah apa yang sempat dieksport pasukan. Apa yang berlaku, mengapa alat reka bentuk AI semakin bergabung, tangga eksport dari kod hingga PNG, dan pelan keluar 10 perkara sebelum anda menggunakan alat seterusnya.',
     'Cửa sổ xuất dữ liệu của Motiff và dịch vụ Visily đều kết thúc ngày 31/10/2026; Visily xóa toàn bộ dữ liệu vào 30/11. Cả hai đều không có định dạng tệp mở, nên thứ còn lại chỉ là những gì đội ngũ kịp xuất ra. Chuyện gì đã xảy ra, vì sao công cụ thiết kế AI đang thu gọn, “bậc thang xuất” từ code đến PNG, và kế hoạch rút lui 10 điểm nên có trước khi dùng công cụ tiếp theo.',
     'La fenêtre d’export de Motiff et le service Visily ont tous deux pris fin le 31 octobre 2026 ; Visily supprime toutes les données le 30 novembre. Aucun n’avait de format de fichier ouvert : ce qui a survécu, c’est ce que les équipes ont exporté à temps. Ce qui s’est passé, pourquoi les outils de design IA se concentrent, l’échelle d’export du code jusqu’au PNG, et un plan de sortie en dix points à préparer avant d’adopter le prochain outil.',
     'La ventana de exportación de Motiff y el servicio de Visily terminaron el 31 de octubre de 2026; Visily borra todos los datos el 30 de noviembre. Ninguno tenía un formato de archivo abierto, así que lo que sobrevivió fue lo que los equipos exportaron a tiempo. Qué pasó, por qué las herramientas de diseño con IA se están concentrando, la escalera de exportación del código al PNG y un plan de salida de diez puntos para preparar antes de adoptar la siguiente herramienta.',
     'Motiffs Exportfenster und der Dienst von Visily endeten beide am 31. Oktober 2026; Visily löscht alle Daten am 30. November. Keines der Tools hatte ein offenes Dateiformat, also blieb nur, was Teams rechtzeitig exportiert hatten. Was passiert ist, warum sich KI-Designtools konsolidieren, die Export-Leiter vom Code bis zum PNG und ein Exit-Plan in zehn Punkten, den du vor dem nächsten Tool aufsetzen solltest.'),
 en="""<p>Yesterday, 31 October 2026, was a quiet deadline for two AI design tools. <strong>Motiff</strong>, the Figma-class editor that later pivoted to AI UI generation, closed its last export window: the service itself went offline on 23 June, and Motiff says all remaining data is deleted after 31 October. <strong>Visily</strong>, the AI wireframing tool, shut down the same day and says its data will be permanently deleted on 30 November. Neither event is dramatic on its own. Together they are a useful reminder that the files in a cloud design tool are often the only copy of your work, and that the market for these tools is changing fast.</p>
<h2>What happened</h2>
<ul><li><strong>Motiff.</strong> The shutdown was announced on 24 April 2026, when new sign-ups and renewals stopped. The editor went offline on 23 June, and export stayed open until 31 October, with every export option made free: PNG, JPEG, WebP, PDF, Copy to Figma, HTML code, React code and a project ZIP. The motiff.com home page now shows a “discontinued” banner, and the old editor survives only as an export page.</li>
<li><strong>Visily.</strong> Announced on 3 October, the team wrote that “the market for tools like Visily has changed substantially in the last couple of years.” Designs could be exported as images, PDF, code (React, Vue or HTML on paid plans, up to 10 screens per ZIP) or to Figma through a plugin, and assets could also be pulled through Visily’s MCP server. Free-plan image exports were limited to 1× scale.</li>
<li><strong>No open format.</strong> As the migration guide from Brilliant points out, Motiff never published a documented file format, so there was no file to hand to a converter later. The only way out was through the exports, before the deadline.</li></ul>
<h2>Why this keeps happening</h2>
<p>Generating a screen has become cheap, and the large platforms now bundle it. Figma, Canva, Framer and GitHub have all shipped agents or prototyping tools in the last month that work inside your existing design system. That squeezes standalone tools whose main feature was “a prompt that makes a screen.” Figma’s own pitch this week is telling: in a survey it cited in South Korea, 62% of respondents said AI output needed six to ten rounds of revision before it could ship, and its answer is an agent that reads a team’s design context. In other words, the value has moved from the generated pixels to the decisions behind them: tokens, components, specs and the reasons for each screen. Those decisions are exactly what gets lost when they only live inside one vendor’s canvas.</p>
<h2>Our take</h2>
<p>Treat every AI design tool, including the big ones, as a place where work <em>happens</em>, not where it <em>lives</em>. The source of truth should sit in formats you control: code in your repository, tokens in the open DTCG JSON format (its first stable version, 2025.10, is supported by Figma, Penpot, Sketch, Framer, Tokens Studio and others), and specs and briefs in plain markdown. Then a shutdown, a price change or a pivot costs you a migration weekend instead of your archive. The test is simple: if the tool vanished tomorrow, could you rebuild your three most important screens from what is on your own disk? If the honest answer is no, fix that before you design anything else in it.</p>
<h2>The export ladder</h2>
<p>When you export, take the highest rung the tool offers, and take the lower rungs too. <strong>Code</strong> you can run beats a <strong>design file</strong> another tool can open; both beat <strong>structured files</strong> such as SVG and token JSON; and those beat <strong>flat images and PDF</strong>, which are a faithful record but cannot be edited. Images are still worth keeping, named by screen and date, as proof of what was agreed.</p>
<h2>Checklist: an exit plan for any AI design tool</h2>
<ol><li><strong>Find the export page on day one.</strong> Before your team commits, export one real screen in every format offered and open it somewhere else.</li>
<li><strong>Check which exports are paywalled.</strong> At Visily, code and Figma exports needed a paid plan and free images were 1×. Know what you lose if you downgrade.</li>
<li><strong>Keep tokens outside the tool.</strong> Colours, type, spacing and radii belong in a DTCG JSON file in git that the tool imports, not the other way round.</li>
<li><strong>Put generated code in git straight away.</strong> A ZIP in a downloads folder is not a source of truth.</li>
<li><strong>Write down the brief.</strong> Save the prompt, the constraints and the reason you chose a direction for each key screen in a markdown file next to the code.</li>
<li><strong>Export on a schedule.</strong> Monthly, the richest format available, to storage your team owns. Batch limits (10 screens per ZIP at Visily) mean large boards take longer than you expect.</li>
<li><strong>Bring your fonts and assets.</strong> Code exports often lose custom fonts and licensed images; keep originals and licences separately.</li>
<li><strong>Prefer tools with an MCP server or API.</strong> Visily’s MCP server gave agents a second way to pull assets out. Programmatic access is an exit door.</li>
<li><strong>Watch the warning signs.</strong> Renewals paused, a home page that suddenly promotes a different product, or a support article titled “what you need to know.”</li>
<li><strong>If you just missed a deadline, ask today.</strong> Visily says data is deleted on 30 November and lists support@visily.ai for questions; it does not say whether export still works after 31 October, so ask now rather than assume.</li></ol>
<pre><code>design-exit.md
  tool:       &lt;name&gt; · plan: &lt;tier&gt; · owner: &lt;person&gt;
  source:     tokens/*.json (DTCG) · src/ (code) · specs/*.md
  exports:    monthly · code ZIP + Figma copy + PNG @2x
  last test:  2026-11-01 · opened in &lt;other tool&gt;: OK
  if closed:  export all · move tokens · rebuild top 3 screens</code></pre>
<h2>How UI Hub helps</h2>
<p>Getting values out of a tool starts with naming them: <a href="../design-tokens-for-agents/">design tokens for agents</a> covers writing tokens down in a form agents and tools can share. <a href="../figma-code-layers-and-specs/">Figma code layers and Specs</a> and <a href="../github-replica-design-system-prototypes/">GitHub Replica</a> show the platforms moving toward code and written context as the shared source. If you are choosing a replacement, <a href="../prompt-to-ui-tools-compared/">prompt-to-UI tools compared</a> is a starting point, and the tool pages on UI Hub list what each one exports.</p>""",
 zh="""<p>昨天，2026 年 10 月 31 日，是两款 AI 设计工具一个不太起眼的截止日。<strong>Motiff</strong>，一款对标 Figma、后来转向 AI 界面生成的编辑器，关闭了最后的导出窗口：服务本身已于 6 月 23 日下线，Motiff 表示 10 月 31 日之后剩余数据全部删除。<strong>Visily</strong>，一款 AI 线框图工具，同一天关停，并表示数据将于 11 月 30 日永久删除。单看每件事都不算大新闻，放在一起却是个有用的提醒：云端设计工具里的文件，往往是你作品唯一的一份；而这类工具的市场正在快速变化。</p>
<h2>发生了什么</h2>
<ul><li><strong>Motiff。</strong>2026 年 4 月 24 日宣布关停，同时停止新注册和续费。编辑器 6 月 23 日下线，导出一直开放到 10 月 31 日，并且所有导出选项都改为免费：PNG、JPEG、WebP、PDF、复制到 Figma、HTML 代码、React 代码和项目 ZIP。motiff.com 首页现在挂着「已停止服务」的横幅，旧编辑器只剩一个导出页面。</li>
<li><strong>Visily。</strong>10 月 3 日宣布，团队写道「像 Visily 这样的工具，市场在过去几年里发生了很大变化」。设计可以导出为图片、PDF、代码（付费方案支持 React、Vue 或 HTML，每个 ZIP 最多 10 个页面），或通过插件导入 Figma，素材还可以通过 Visily 的 MCP 服务器取出。免费方案的图片导出只有 1 倍尺寸。</li>
<li><strong>没有开放格式。</strong>Brilliant 的迁移指南指出，Motiff 从未公开过有文档的文件格式，所以事后没有一个文件可以交给转换器。唯一的出路就是在截止日前导出。</li></ul>
<h2>为什么这种事会反复发生</h2>
<p>生成一个页面已经很便宜，而大平台正在把它打包进来。过去一个月里，Figma、Canva、Framer 和 GitHub 都推出了能在你现有设计系统里工作的智能体或原型工具。这挤压了那些主打「一句提示做出一个页面」的独立工具。Figma 这周的说法很能说明问题：它引用的一项韩国调查中，62% 的受访者说 AI 产出要改六到十轮才能上线，而它给出的答案是一个读取团队设计上下文的智能体。换句话说，价值已经从生成的像素转移到背后的决定：Token、组件、规格说明，以及每个页面为什么这样做。这些决定如果只存在于某个厂商的画布里，正是最先丢掉的东西。</p>
<h2>我们的看法</h2>
<p>把每一款 AI 设计工具，包括大平台，都当成工作「发生」的地方，而不是作品「存放」的地方。真正的源头应该放在你自己掌控的格式里：代码放在你的仓库，Token 用开放的 DTCG JSON 格式（首个稳定版 2025.10 已被 Figma、Penpot、Sketch、Framer、Tokens Studio 等支持），规格和需求说明用普通 Markdown。这样一来，工具关停、涨价或转型，代价是一个周末的迁移，而不是你的整个存档。检验方法很简单：如果这个工具明天消失，你能不能只靠自己硬盘上的东西，重建最重要的三个页面？如果诚实的回答是不能，先把这件事解决，再在里面设计别的。</p>
<h2>导出阶梯</h2>
<p>导出时，拿工具提供的最高一级，也把低几级一起拿上。能运行的<strong>代码</strong>胜过其他工具能打开的<strong>设计文件</strong>；两者都胜过 SVG、Token JSON 这类<strong>结构化文件</strong>；而这些又胜过<strong>图片和 PDF</strong>，它们忠实记录了设计，但无法编辑。图片仍然值得保留，按页面和日期命名，作为当时达成一致的凭证。</p>
<h2>清单：任何 AI 设计工具的退出计划</h2>
<ol><li><strong>第一天就找到导出页面。</strong>团队正式采用之前，把一个真实页面按所有可选格式各导出一次，并在别的工具里打开。</li>
<li><strong>弄清哪些导出要付费。</strong>在 Visily，代码和 Figma 导出需要付费方案，免费图片只有 1 倍。要知道降级后会失去什么。</li>
<li><strong>Token 放在工具之外。</strong>颜色、字体、间距和圆角应该放在 git 里的 DTCG JSON 文件中，由工具导入，而不是反过来。</li>
<li><strong>生成的代码马上进 git。</strong>下载文件夹里的 ZIP 不是源头。</li>
<li><strong>把需求说明写下来。</strong>每个关键页面的提示词、约束和选择这个方向的理由，存成和代码放在一起的 Markdown 文件。</li>
<li><strong>定期导出。</strong>每月一次，用能拿到的最完整格式，存到团队自己的存储里。批量限制（Visily 每个 ZIP 最多 10 个页面）意味着大画板比你预想的更花时间。</li>
<li><strong>字体和素材自己保管。</strong>代码导出常常丢掉自定义字体和授权图片；原文件和授权要单独保存。</li>
<li><strong>优先选有 MCP 服务器或 API 的工具。</strong>Visily 的 MCP 服务器让智能体多了一条取出素材的路。可编程访问就是一扇出口。</li>
<li><strong>留意预警信号。</strong>续费暂停、首页突然主推另一个产品，或者出现一篇标题叫「你需要知道的事」的帮助文章。</li>
<li><strong>如果刚错过截止日，今天就去问。</strong>Visily 说数据在 11 月 30 日删除，并留了 support@visily.ai 作为咨询邮箱；它没有说 10 月 31 日之后还能不能导出，所以现在就问，不要想当然。</li></ol>
<pre><code>design-exit.md（退出计划）
  工具：     &lt;名称&gt; · 方案：&lt;档位&gt; · 负责人：&lt;姓名&gt;
  源头：     tokens/*.json（DTCG）· src/（代码）· specs/*.md
  导出：     每月 · 代码 ZIP + Figma 副本 + PNG @2x
  上次测试： 2026-11-01 · 在 &lt;其他工具&gt; 中打开：正常
  若关停：   全部导出 · 迁移 Token · 重建前三个页面</code></pre>
<h2>UI Hub 能帮什么</h2>
<p>把数值从工具里带出来，先要给它们起名字：<a href="../design-tokens-for-agents/">给智能体的设计 Token</a> 讲了怎么把 Token 写成智能体和工具都能共用的形式。<a href="../figma-code-layers-and-specs/">Figma 代码图层与 Specs</a> 和 <a href="../github-replica-design-system-prototypes/">GitHub Replica</a> 展示了大平台正在把代码和书面上下文当作共同的源头。如果你在挑替代工具，可以从<a href="../prompt-to-ui-tools-compared/">提示生成界面工具对比</a>开始，UI Hub 的工具页面也列出了每款工具能导出什么。</p>""",
 refs=[('Motiff is shutting down — what you need to know','Motiff Help Center','https://motiff.com/help/others/462390803479041'),('Motiff home page (discontinued banner)','Motiff','https://motiff.com/home'),('Moving from Motiff','Brilliant Docs','https://brilliant.design/docs/solutions/moving-from-motiff'),('Visily is shutting down','The Visily Team, Visily Blog','https://www.visily.ai/blog/visily-is-shutting-down'),('How to export designs to code','Visily Support','https://support.visily.ai/portal/en/kb/articles/how-to-export-designs-to-code'),('How to export designs as images','Visily Support','https://support.visily.ai/portal/en/kb/articles/how-to-export-designs-as-images'),('Visily shutdown: dates, export steps, alternatives','Shutdown Watch','https://shutdownwatch.com/shutdowns/visily/'),('Week of Oct 26 to Nov 1, 2026: what changed','Design Eng Index','https://designengindex.com/weekly/2026-44'),('Figma bets on design-specific AI agent as quality lags speed','GMAsia News','https://gmasia.ai/news/figma-bets-on-design-specific-ai-agent-as-quality-lags-speed'),('Design Tokens Community Group (DTCG), first stable version 2025.10','W3C Design Tokens Community Group','https://www.designtokens.org/')]),
dict(slug='best-animated-react-component-libraries-2026', date='2026-11-01', cat='components', series=None, featured=False, tags=['React','animation','Motion','Magic UI','React Bits','Aceternity UI'],
 t=T('Best animated React component libraries 2026: Motion, Magic UI, React Bits and more', '2026 年最值得用的 React 动效组件库：Motion、Magic UI、React Bits 等', '2026 年最值得用的 React 動效元件庫：Motion、Magic UI、React Bits 等', '2026年のReactアニメーションUIライブラリ比較：Motion、Magic UI、React Bitsなど', '2026년 애니메이션 React 컴포넌트 라이브러리 비교: Motion, Magic UI, React Bits 등', 'Pustaka komponen React beranimasi terbaik 2026: Motion, Magic UI, React Bits dan lain-lain', 'Thư viện component React có hiệu ứng chuyển động đáng dùng năm 2026: Motion, Magic UI, React Bits và hơn thế', 'Meilleures bibliothèques de composants React animés en 2026 : Motion, Magic UI, React Bits et plus', 'Mejores bibliotecas de componentes React animados en 2026: Motion, Magic UI, React Bits y más', 'Die besten animierten React-Komponentenbibliotheken 2026: Motion, Magic UI, React Bits und mehr'),
 s=T('Ten animated React libraries compared with numbers read from GitHub, npm and their own sites on 1 November 2026: engines you write motion with, copy-paste collections, and the licence catch to check before shipping.', '十个 React 动效库，数字均于 2026 年 11 月 1 日取自 GitHub、npm 和各自官网：自己写动效的引擎、复制即用的合集，以及上线前要查的许可证细节。', '十個 React 動效庫，數字均於 2026 年 11 月 1 日取自 GitHub、npm 與各自官網：自己寫動效的引擎、複製即用的合集，以及上線前要查的授權細節。', 'GitHub・npm・各公式サイトから2026年11月1日に読み取った数値で、10のReactアニメーションライブラリを比較。モーションを書くエンジン、コピペ集、公開前に確認すべきライセンスの注意点。', '2026년 11월 1일 GitHub·npm·각 공식 사이트에서 읽은 수치로 10개의 애니메이션 React 라이브러리를 비교합니다. 직접 모션을 쓰는 엔진, 복사해 쓰는 컬렉션, 배포 전 확인할 라이선스 함정까지.', 'Sepuluh pustaka React beranimasi dibandingkan dengan angka dari GitHub, npm dan laman rasmi pada 1 November 2026: enjin untuk menulis gerakan, koleksi salin-tampal, dan perangkap lesen sebelum dilancarkan.', 'So sánh mười thư viện React có hiệu ứng với số liệu đọc từ GitHub, npm và trang chính thức ngày 1/11/2026: engine để tự viết chuyển động, bộ sưu tập sao chép dùng ngay, và điểm cần kiểm tra về giấy phép trước khi phát hành.', 'Dix bibliothèques React animées comparées avec des chiffres lus sur GitHub, npm et leurs sites le 1er novembre 2026 : moteurs pour écrire le mouvement, collections à copier, et le piège de licence à vérifier avant de livrer.', 'Diez bibliotecas React animadas comparadas con cifras leídas en GitHub, npm y sus sitios el 1 de noviembre de 2026: motores para escribir movimiento, colecciones para copiar y la trampa de licencia que hay que revisar antes de publicar.', 'Zehn animierte React-Bibliotheken im Vergleich, mit Zahlen von GitHub, npm und den Projektseiten vom 1. November 2026: Engines zum Schreiben von Bewegung, Copy-Paste-Sammlungen und der Lizenzhaken vor dem Release.'),
 en='<p>This is a shortlist of animated React component libraries worth knowing in 2026, with the numbers read straight from GitHub, npm and each project’s own site on 1 November 2026. “Animated React component library” covers two different things: <strong>animation engines</strong> you write motion with, and <strong>copy-paste collections</strong> of ready-made animated components. They solve different problems, so they are listed separately. Stars and downloads move every day; treat them as a snapshot, not a ranking.</p>\n<h2>The short answer</h2>\n<ul><li><strong>Need to animate your own components:</strong> Motion (formerly Framer Motion). It is the most downloaded animation engine here and is MIT licensed.</li>\n<li><strong>Need physics-based springs:</strong> React Spring.</li>\n<li><strong>Need list add/remove animation with almost no code:</strong> AutoAnimate.</li>\n<li><strong>Need a landing page with animated sections today:</strong> Magic UI or Aceternity UI. Both are built on React, Tailwind CSS and Motion.</li>\n<li><strong>Need the largest pool of animated pieces:</strong> React Bits, but read its licence first (below).</li>\n<li><strong>Need animated components that sit on top of shadcn/ui:</strong> Cult UI, Kokonut UI, Motion Primitives or Animate UI.</li></ul>\n<h2>Animation engines: you write the motion</h2>\n<ul><li><strong>Motion</strong> — “An open source animation library for JavaScript, React and Vue.” MIT. 34,779 GitHub stars, last push 1 November 2026. Install with <code>npm install motion</code> and import from <code>motion/react</code>; its README states that Framer Motion is now Motion. The <code>motion</code> package was at version 14.9.0 and had about 33.9 million npm downloads in the week of 23–29 October 2026 (the older <code>framer-motion</code> package: about 66.9 million). Its README lists gestures, springs, layout transitions, scroll-linked effects and timelines. A separate paid tier, Motion+, exists; UI Hub lists it as paid, one-time purchase.</li>\n<li><strong>React Spring</strong> — “A spring physics based React animation library.” MIT. 29,261 stars. <code>@react-spring/web</code> was at 10.1.2 with about 7.2 million weekly downloads, and supports React 16.8 through 19.</li>\n<li><strong>AutoAnimate</strong> (FormKit) — “A zero-config, drop-in animation utility” for React, Vue or plain JavaScript. MIT. 13,954 stars; last push 10 July 2026. <code>@formkit/auto-animate</code> was at 0.10.0 with about 2.4 million weekly downloads. It animates elements entering, leaving and moving inside a parent, which is why it needs so little code.</li></ul>\n<h2>Copy-paste collections: you own the source</h2>\n<ul><li><strong>Magic UI</strong> — its homepage says “150+ free and open-source animated components and effects built with React, TypeScript, Tailwind CSS, and Motion”, as a companion to shadcn/ui. MIT. 23,026 stars.</li>\n<li><strong>Aceternity UI</strong> — its homepage lists 118+ free components, and separately 183+ blocks, 17 templates and 4 landing pages; blocks are described as included with its paid All-Access Pass. Built with React, Tailwind CSS and Motion. We did not find a public repository for it to read star counts from.</li>\n<li><strong>React Bits</strong> — described by its repository as “the largest open-source library of animated, interactive, and customizable React &amp; Next.js components”. 50,984 stars, the highest in this list. You choose JavaScript or TypeScript and plain CSS or Tailwind, then copy the source or install through its CLI. Licence: MIT + Commons Clause (see below).</li>\n<li><strong>Cult UI</strong> — “150+ free shadcn/ui components, built with Tailwind CSS and Motion. MIT licensed.” 6,899 stars; last push 29 October 2026.</li>\n<li><strong>Kokonut UI</strong> — an open-source collection of components built with Tailwind CSS, shadcn/ui and Motion. MIT. 2,259 stars.</li>\n<li><strong>Motion Primitives</strong> — a UI kit of animated interface pieces. MIT. 6,879 stars; last push 28 September 2026.</li>\n<li><strong>Animate UI</strong> — “fully animated, open-source component distribution built with React, TypeScript, Tailwind CSS, Motion, and Shadcn CLI”. 4,819 stars. Licence: MIT + Commons Clause. Its homepage also advertises an agent skill, installed with <code>npx skills add imskyleen/animate-ui</code>.</li></ul>\n<h2>Small libraries that animate one thing well</h2>\n<ul><li><strong>Sonner</strong> (toasts) and <strong>Vaul</strong> (mobile-style drawer), both by Emil Kowalski, had about 54.5 million and 31.2 million weekly npm downloads respectively in the same week.</li>\n<li><strong>Lenis</strong> (smooth scroll) had about 2.4 million weekly downloads, and <strong>GSAP</strong> about 8.3 million. GSAP is not React-only, and UI Hub notes it is free to use under its own licence rather than MIT.</li></ul>\n<h2>Read the licence before you ship</h2>\n<p>Two libraries above use “MIT + Commons Clause”. The React Bits licence says you may use the software, including commercially, as long as you do not sell, sublicense or redistribute the components themselves, whether alone, in a bundle or as a ported version. That is fine for a product or website you build; it rules out publishing the components as your own template pack. The Animate UI licence has the same Commons Clause name, so read its LICENSE file for the exact terms before reusing it. Motion, React Spring, AutoAnimate, Magic UI, Cult UI, Kokonut UI and Motion Primitives show plain MIT on GitHub. Aceternity UI’s free components and paid blocks follow the terms on its own site, and we did not check the licences of the small libraries.</p>\n<h2>How to choose</h2>\n<ol><li><strong>Start from the job, not the star count.</strong> Animating state changes in your own components calls for an engine (Motion, React Spring, AutoAnimate). A marketing page calls for a copy-paste collection.</li>\n<li><strong>Pick one engine.</strong> Most collections here are built on Motion, so using Motion for your own code means one dependency instead of two.</li>\n<li><strong>Copy only what you use.</strong> Collections install as source files you own, so remove unused components and check each one’s dependencies.</li>\n<li><strong>One hero effect per page.</strong> Stacked animated backgrounds hurt readability and performance more than they help.</li>\n<li><strong>Respect reduced motion.</strong> Test with the operating system’s reduce-motion setting on, in light and dark themes, at 375 px width and by keyboard.</li></ol>\n<pre><code># Free React libraries with the "motion" visual style in UI Hub\ncurl -s https://ui.incidental.site/api/resources.json \\\n | jq \'.items[] | select(.type=="library" and .pricing=="free"\n   and (.tags|index("React")) and ((.vs//[])|index("motion"))) | {name,url}\'</code></pre>\n<h2>What UI Hub adds</h2>\n<p>UI Hub lists 235 component libraries; on 1 November 2026, 11 of them were tagged React with the motion visual style, and 9 of those were marked free. The filter above reproduces that list from the public API. For deeper reading, see our notes on <a href="../motion-that-feels-right/">motion that feels right</a> (durations, easing and reduced motion), and the deep dives on <a href="../magic-ui-deep-dive/">Magic UI</a>, <a href="../aceternity-ui-deep-dive/">Aceternity UI</a> and <a href="../cult-ui-deep-dive/">Cult UI</a>.</p>',
 zh='<p>这是一份 2026 年值得了解的 React 动效组件库清单，所有数字都是 2026 年 11 月 1 日直接从 GitHub、npm 和各项目官网读到的。「React 动效组件库」其实包含两类东西：自己编写动画的<strong>动画引擎</strong>，以及可以直接复制使用的<strong>现成动效组件合集</strong>。它们解决的问题不同，所以分开列出。星标数和下载量每天都在变，请把它当作一张快照，而不是排名。</p>\n<h2>一句话结论</h2>\n<ul><li><strong>要给自己的组件加动画：</strong>Motion（原 Framer Motion）。它是这份清单里下载量最高的动画引擎，MIT 许可。</li>\n<li><strong>要基于物理的弹簧动画：</strong>React Spring。</li>\n<li><strong>要用几乎不写代码的方式做列表增删动画：</strong>AutoAnimate。</li>\n<li><strong>今天就要一个带动效区块的落地页：</strong>Magic UI 或 Aceternity UI，都基于 React、Tailwind CSS 和 Motion。</li>\n<li><strong>要最大的动效素材库：</strong>React Bits，但请先读下面的许可证说明。</li>\n<li><strong>要放在 shadcn/ui 之上的动效组件：</strong>Cult UI、Kokonut UI、Motion Primitives 或 Animate UI。</li></ul>\n<h2>动画引擎：由你来写动效</h2>\n<ul><li><strong>Motion</strong>——「面向 JavaScript、React 和 Vue 的开源动画库」。MIT。GitHub 34,779 星，最近一次推送是 2026 年 11 月 1 日。用 <code>npm install motion</code> 安装，从 <code>motion/react</code> 导入；其 README 明确说明 Framer Motion 现在就是 Motion。<code>motion</code> 包版本 14.9.0，2026 年 10 月 23–29 日这一周 npm 下载约 3394 万次（旧的 <code>framer-motion</code> 包约 6686 万次）。README 列出手势、弹簧、布局过渡、滚动联动和时间线。另有付费版 Motion+；UI Hub 把它标为付费、一次性买断。</li>\n<li><strong>React Spring</strong>——「基于弹簧物理的 React 动画库」。MIT。29,261 星。<code>@react-spring/web</code> 版本 10.1.2，周下载约 719 万次，支持 React 16.8 到 19。</li>\n<li><strong>AutoAnimate</strong>（FormKit）——「零配置、即插即用的动画工具」，可用于 React、Vue 或原生 JavaScript。MIT。13,954 星，最近一次推送是 2026 年 7 月 10 日。<code>@formkit/auto-animate</code> 版本 0.10.0，周下载约 238 万次。它为父元素内进入、离开和移动的元素加动画，所以需要的代码很少。</li></ul>\n<h2>复制即用的合集：源码归你</h2>\n<ul><li><strong>Magic UI</strong>——官网写的是「150+ 个免费开源、基于 React、TypeScript、Tailwind CSS 和 Motion 的动效组件与效果」，定位为 shadcn/ui 的搭档。MIT。23,026 星。</li>\n<li><strong>Aceternity UI</strong>——官网列出 118+ 个免费组件，另有 183+ 个区块、17 个模板和 4 个完整落地页；区块说明包含在付费的 All-Access Pass 中。基于 React、Tailwind CSS 和 Motion。我们没有找到可以读取星标数的公开代码仓库。</li>\n<li><strong>React Bits</strong>——仓库自述为「最大的开源动效、交互、可定制 React 与 Next.js 组件库」。50,984 星，是这份清单里最多的。可以选择 JavaScript 或 TypeScript、纯 CSS 或 Tailwind，然后复制源码或用它的 CLI 安装。许可证：MIT + Commons Clause（见下文）。</li>\n<li><strong>Cult UI</strong>——「150+ 个免费 shadcn/ui 组件，基于 Tailwind CSS 和 Motion，MIT 许可」。6,899 星，最近一次推送是 2026 年 10 月 29 日。</li>\n<li><strong>Kokonut UI</strong>——基于 Tailwind CSS、shadcn/ui 和 Motion 的开源组件合集。MIT。2,259 星。</li>\n<li><strong>Motion Primitives</strong>——一套动效界面组件包。MIT。6,879 星，最近一次推送是 2026 年 9 月 28 日。</li>\n<li><strong>Animate UI</strong>——「完全动效化、基于 React、TypeScript、Tailwind CSS、Motion 和 Shadcn CLI 的开源组件分发」。4,819 星。许可证：MIT + Commons Clause。官网还提供一个 agent skill，用 <code>npx skills add imskyleen/animate-ui</code> 安装。</li></ul>\n<h2>只把一件事做好的小库</h2>\n<ul><li><strong>Sonner</strong>（通知）和 <strong>Vaul</strong>（移动端风格抽屉），都出自 Emil Kowalski，同一周 npm 周下载分别约 5445 万和 3119 万次。</li>\n<li><strong>Lenis</strong>（平滑滚动）周下载约 238 万次，<strong>GSAP</strong> 约 826 万次。GSAP 并非只面向 React；UI Hub 注明它免费使用，但采用自有许可证而不是 MIT。</li></ul>\n<h2>上线前先读许可证</h2>\n<p>上面有两个库使用「MIT + Commons Clause」。React Bits 的许可证写明：可以使用该软件，包括商业用途，前提是不出售、转授权或再分发组件本身，无论单独、打包还是移植版本。用它做自己的产品或网站没有问题；把这些组件当作你自己的模板包发布则不行。Animate UI 的许可证名称相同，重用前请读它的 LICENSE 文件了解确切条款。Motion、React Spring、AutoAnimate、Magic UI、Cult UI、Kokonut UI 和 Motion Primitives 在 GitHub 上显示为普通 MIT；Aceternity UI 的免费组件和付费区块遵循官网上的自有条款；小型库的许可证我们没有逐一核对。</p>\n<h2>怎么选</h2>\n<ol><li><strong>从任务出发，不要看星标。</strong>给自己组件里的状态变化加动画，选引擎（Motion、React Spring、AutoAnimate）；做营销页，选复制即用的合集。</li>\n<li><strong>只选一个引擎。</strong>这里大多数合集都基于 Motion，所以自己的代码也用 Motion，依赖就只有一个而不是两个。</li>\n<li><strong>只复制用到的。</strong>合集是以源码文件的形式安装的，归你所有，所以要删掉不用的组件，并检查每个组件的依赖。</li>\n<li><strong>每页只放一个主视觉特效。</strong>堆叠动效背景对可读性和性能的伤害大于帮助。</li>\n<li><strong>尊重减少动态效果设置。</strong>在系统开启「减少动态效果」的情况下测试，同时测浅色和深色主题、375 px 宽度和键盘操作。</li></ol>\n<pre><code># UI Hub 里视觉风格为 "motion" 的免费 React 库\ncurl -s https://ui.incidental.site/api/resources.json \\\n | jq \'.items[] | select(.type=="library" and .pricing=="free"\n   and (.tags|index("React")) and ((.vs//[])|index("motion"))) | {name,url}\'</code></pre>\n<h2>UI Hub 能帮什么</h2>\n<p>UI Hub 收录了 235 个组件库；2026 年 11 月 1 日，其中 11 个带有 React 标签且视觉风格为 motion，这 11 个里 9 个标为免费。上面的筛选命令可以用公开 API 复现这份名单。想读得更深，可以看我们的<a href="../motion-that-feels-right/">让动效有手感</a>（时长、缓动和减少动态效果），以及 <a href="../magic-ui-deep-dive/">Magic UI</a>、<a href="../aceternity-ui-deep-dive/">Aceternity UI</a> 和 <a href="../cult-ui-deep-dive/">Cult UI</a> 的深度解读。</p>',
 refs=[('motiondivision/motion (README, licence, stars)', 'GitHub', 'https://github.com/motiondivision/motion'), ('Motion for React', 'Motion', 'https://motion.dev/docs/react'), ('pmndrs/react-spring', 'GitHub', 'https://github.com/pmndrs/react-spring'), ('formkit/auto-animate', 'GitHub', 'https://github.com/formkit/auto-animate'), ('Magic UI', 'Magic UI', 'https://magicui.design/'), ('magicuidesign/magicui', 'GitHub', 'https://github.com/magicuidesign/magicui'), ('Aceternity UI', 'Aceternity', 'https://ui.aceternity.com/'), ('React Bits', 'React Bits', 'https://reactbits.dev/'), ('DavidHDev/react-bits (LICENSE: MIT + Commons Clause)', 'GitHub', 'https://github.com/DavidHDev/react-bits/blob/main/LICENSE.md'), ('nolly-studio/cult-ui', 'GitHub', 'https://github.com/nolly-studio/cult-ui'), ('kokonut-labs/kokonutui', 'GitHub', 'https://github.com/kokonut-labs/kokonutui'), ('ibelick/motion-primitives', 'GitHub', 'https://github.com/ibelick/motion-primitives'), ('Animate UI', 'Animate UI', 'https://animate-ui.com/'), ('imskyleen/animate-ui', 'GitHub', 'https://github.com/imskyleen/animate-ui'), ('npm weekly downloads API (23–29 October 2026)', 'npm', 'https://api.npmjs.org/downloads/point/last-week/motion'), ('UI Hub resources API', 'UI Hub', 'https://ui.incidental.site/api/resources.json')]),
]
POSTS2 += [
dict(slug='stageshow-faux-product-ui-for-agents', date='2026-11-02', cat='agents', series=None, featured=True, tags=['Stageshow','faux UI','agent skills','product demos','motion'],
 t=T('Stageshow: teaching agents to make product demos that look real',
     'Stageshow：教智能体做出像真产品的界面演示',
     'Stageshow：教智能體做出像真產品的介面示範',
     'Stageshow：エージェントに本物らしい製品デモを作らせる方法',
     'Stageshow: 에이전트가 진짜 같은 제품 데모를 만들게 하는 법',
     'Stageshow: mengajar ejen membuat demo produk yang kelihatan sebenar',
     'Stageshow: dạy agent làm bản demo sản phẩm trông như thật',
     'Stageshow : apprendre aux agents à faire des démos produit crédibles',
     'Stageshow: enseñar a los agentes a crear demos de producto que parezcan reales',
     'Stageshow: Agents bringen, Produktdemos zu bauen, die echt wirken'),
 s=T('Benji Taylor’s open-source Stageshow skill, released on 31 October, writes down the judgment behind good faux product UI for coding agents: five ways mockups fail, a seven-step workflow, gold examples, a React kit and a script that films the result so the agent can check its own work. What is in it, what it gets right, the accessibility and honesty gaps you still have to close, and a ten-step checklist for your next hero demo.',
     'Benji Taylor 在 10 月 31 日开源的 Stageshow 技能，把做好「假产品界面」（faux UI）的判断力写成了智能体能读的规则：五种常见失败、七步工作流、标杆示例、一套 React 组件，以及一个把成品录下来让智能体自查的脚本。本文讲它包含什么、做对了什么、你仍需自己补上的无障碍与诚实问题，并给出一份做下一个首屏演示时可用的十步清单。',
     'Benji Taylor 在 10 月 31 日開源的 Stageshow 技能，把做好「假產品介面」（faux UI）的判斷力寫成了智能體能讀的規則：五種常見失敗、七步工作流程、標竿範例、一套 React 元件，以及一個把成品錄下來讓智能體自查的腳本。本文講它包含什麼、做對了什麼、你仍需自己補上的無障礙與誠實問題，並給出一份做下一個首屏示範時可用的十步清單。',
     'Benji Taylorが10月31日に公開したオープンソースのスキル「Stageshow」は、良いフェイク製品UIを作るための判断をコーディングエージェント向けに書き出したものだ。モックアップが失敗する5つのパターン、7ステップの手順、手本となる作例、Reactキット、そして完成品を撮影してエージェント自身に確認させるスクリプト。中身、優れている点、自分で埋めるべきアクセシビリティと誠実さの課題、次のヒーローデモ用の10項目チェックリストを紹介する。',
     'Benji Taylor가 10월 31일 공개한 오픈소스 스킬 Stageshow는 좋은 가짜 제품 UI를 만드는 판단을 코딩 에이전트가 읽을 수 있게 글로 옮겼다. 목업이 실패하는 다섯 가지 방식, 7단계 워크플로, 기준이 되는 예제, React 키트, 결과물을 촬영해 에이전트가 스스로 점검하게 하는 스크립트까지. 무엇이 들어 있는지, 무엇을 잘했는지, 직접 메워야 할 접근성과 정직성의 빈틈, 다음 히어로 데모를 위한 10단계 체크리스트를 정리했다.',
     'Kemahiran sumber terbuka Stageshow oleh Benji Taylor, dikeluarkan pada 31 Oktober, menulis pertimbangan di sebalik UI produk tiruan yang baik untuk ejen pengekodan: lima cara mockup gagal, aliran kerja tujuh langkah, contoh rujukan, kit React dan skrip yang merakam hasil supaya ejen boleh menyemak kerjanya sendiri. Apa isinya, apa yang betul, jurang kebolehcapaian dan kejujuran yang masih perlu anda tutup, serta senarai semak sepuluh langkah untuk demo hero seterusnya.',
     'Stageshow, skill mã nguồn mở của Benji Taylor ra mắt ngày 31/10, viết ra những phán đoán đằng sau một giao diện sản phẩm giả (faux UI) tốt để agent lập trình đọc được: năm kiểu mockup thất bại, quy trình bảy bước, ví dụ chuẩn, bộ kit React và một script quay lại kết quả để agent tự kiểm tra. Bài viết nói nó có gì, làm đúng điều gì, những lỗ hổng về khả năng tiếp cận và tính trung thực bạn vẫn phải tự lấp, cùng danh sách mười bước cho bản demo hero tiếp theo.',
     'Stageshow, le skill open source de Benji Taylor publié le 31 octobre, met par écrit pour les agents de code le jugement qui fait une bonne fausse interface produit : cinq façons dont les maquettes échouent, une méthode en sept étapes, des exemples de référence, un kit React et un script qui filme le résultat pour que l’agent vérifie son propre travail. Ce qu’il contient, ce qu’il réussit, les manques d’accessibilité et d’honnêteté à combler vous-même, et une liste en dix étapes pour votre prochaine démo de hero.',
     'Stageshow, el skill de código abierto que Benji Taylor publicó el 31 de octubre, pone por escrito para los agentes de código el criterio detrás de una buena interfaz de producto simulada: cinco formas en que fallan los mockups, un flujo de siete pasos, ejemplos de referencia, un kit de React y un script que graba el resultado para que el agente revise su propio trabajo. Qué incluye, qué hace bien, los huecos de accesibilidad y honestidad que aún debes cubrir tú, y una lista de diez pasos para tu próxima demo de portada.',
     'Benji Taylors Open-Source-Skill Stageshow, veröffentlicht am 31. Oktober, schreibt für Coding-Agents das Urteilsvermögen hinter guter Faux-Produkt-UI auf: fünf Arten, wie Mockups scheitern, ein Ablauf in sieben Schritten, Referenzbeispiele, ein React-Kit und ein Skript, das das Ergebnis filmt, damit der Agent seine Arbeit selbst prüft. Was drin ist, was es richtig macht, welche Lücken bei Barrierefreiheit und Ehrlichkeit du selbst schließen musst, und eine Checkliste in zehn Schritten für deine nächste Hero-Demo.'),
 en="""<p>On 31 October designer Benji Taylor open-sourced <strong>Stageshow</strong>, an agent skill for one narrow job: faux product UI. That means the miniature, simplified screens on a landing page, a feature card or a docs hero, either as a still or as a short looping demo with a cursor. His point is that good models can already draw these, but the results tend to look heavy and generated. Stageshow is his attempt to write down the hundred small decisions a designer makes by hand so an agent can make them too. The launch post on X passed 1.3 million views and 24,000 bookmarks within two days, which says how many teams are fighting the same problem.</p>
<h2>What is in the skill</h2>
<ul><li><strong>One idea and five failures.</strong> The demo should read as a real product, simplified to what the viewer needs, framed with intent, with a cause for every motion. It fails when it is <em>too much</em> (real text everywhere), a <em>wireframe</em> (two gray blobs and a button), <em>boxed</em> (a whole window shrunk into a card), <em>flat</em> (everything the same weight) or <em>bland</em> (a gray window whatever the brief asked for).</li>
<li><strong>A seven-step workflow.</strong> Medium and placement, look, story, start from an example, build the screen, choreograph, rehearse. Most of the quality is decided before code: where the demo sits, the focal object, the action, the payoff and what can be left out.</li>
<li><strong>Gold examples and teaching pairs.</strong> Dozens of reference scenes (hero demo, bento grids, chart scrub, drag to reorder, an AI answer streaming in), product studies, and bad and good versions side by side. The agent copies the closest gold example instead of starting blank.</li>
<li><strong>A small React kit.</strong> A <code>Stage</code> with a scripted <code>Act</code> API, windows and phones drawn from real geometry, and motion parts such as <code>Roll</code>, <code>Count</code> and <code>Fly</code>. It handles the hard parts but deliberately supplies no look; you map your own tokens onto it.</li>
<li><strong>Tools that film the result.</strong> <code>film.mjs</code> opens the page in headless Chrome and shoots a contact sheet; <code>layout.mjs</code> checks that text and controls fit their boxes. The agent looks at its own frames and fixes the largest fault first: framing, then hierarchy, then motion, then polish.</li></ul>
<h2>The numbers worth stealing</h2>
<p>The rules are concrete enough to check. Design at the size the demo is seen: about 720 × 340 for a hero beside copy, 900 to 1100 wide for a full-width hero, 400 × 300 for a card, plus a separate compact design for a 358px phone column. Budget words, not elements: usually 3 to 7 real strings, with placeholder bars for the rest. Crop 10 to 40% of the hero window off the stage and let it fill at least two thirds of the width. A story is three to five beats in 10 to 16 seconds; the payoff holds for about two seconds; data never rewinds in view. And the faux app’s title is a <code>div</code>, never a real heading, because the demo lives inside someone else’s page outline.</p>
<h2>Our take</h2>
<p>The kit is useful, but the real lesson is the shape of the skill. It pairs a short list of named failures with gold examples to copy and a way for the agent to <em>see</em> its own output. Most design skills only do the first. A rule like “avoid clutter” is easy to agree with and easy to ignore; a filmed frame next to the gold example is not. If you write design skills for your own team, copy that structure: failures with names, examples with numbers, and a check the agent can run.</p>
<p>Two things the skill leaves to you. First, <strong>accessibility</strong>: a 10 to 16 second loop that starts on its own and sits next to other content needs a way to pause it under WCAG 2.2.2, and readers who ask for reduced motion should get the poster frame, not the animation. Stageshow’s emphasis on a poster frame that tells the story on its own makes this easy, but you have to wire it up. Second, <strong>honesty</strong>: a polished faux screen can quietly become the spec, or promise a feature that does not exist yet. Show only what ships, label illustrations as illustrations, and re-film when the real product changes. Also note the licence: the code is MIT, but the bundled app icons and brand marks stay with their owners.</p>
<h2>Checklist: your next hero demo with an agent</h2>
<ol><li><strong>Install and look first.</strong> <code>npx skills add benjitaylor/skills --skill stageshow</code>, then run the playground and film the gold example closest to your idea.</li>
<li><strong>Write the plan before any code.</strong> Placement and size, focal object, the one action, the payoff, and what to leave out.</li>
<li><strong>Map your tokens.</strong> Font, accent, radius and light or dark ground from your real product, not the kit’s defaults.</li>
<li><strong>Set a word budget.</strong> Three to seven real strings on what the story is about; placeholder bars at the edges.</li>
<li><strong>Frame it.</strong> One hero, at most one satellite straddling its edge, the window bled off an edge, one consistent gutter.</li>
<li><strong>Script three to five beats.</strong> Ten to sixteen seconds, every cursor move explained, a payoff that holds, a loop that ends where it began.</li>
<li><strong>Choose the poster frame.</strong> The single frame that tells the story; serve it under <code>prefers-reduced-motion</code> and as the thumbnail.</li>
<li><strong>Add a pause control.</strong> Auto-playing loops over five seconds need one; give the demo an accessible name and keep its fake headings out of the outline.</li>
<li><strong>Film at both widths.</strong> Desktop and 390px; fix the largest visible fault first and re-film until the gate passes, then look again yourself.</li>
<li><strong>Run an honesty pass.</strong> Every feature shown exists today; the demo is captioned as an illustration; someone owns re-filming it after UI changes.</li></ol>
<pre><code>demo-plan.md
  place:    homepage hero, beside copy · 720×340 · compact 358
  focus:    the issue row being assigned
  beats:    open menu → pick teammate → avatar lands → status rolls
  payoff:   assigned row holds 2s · poster = this frame
  words:    issue title · teammate name · status   (3 real strings)
  a11y:     pause button · reduced motion → poster · role="img" + label
  honesty:  shipped feature only · caption "Illustration"</code></pre>
<h2>How UI Hub helps</h2>
<p>Stageshow is one of a growing set of design skills; <a href="../taste-and-skills-for-agents/">teaching agents taste</a> and <a href="../claude-cursor-design-skills/">design skills for Claude and Cursor</a> explain how to stack them. Its motion rules sit well next to <a href="../motion-that-feels-right/">motion that feels right</a>, and <a href="../landing-page-teardown-linear-vercel/">our Linear and Vercel teardown</a> shows why the first image on a landing page should be your real product. Before a demo ships, run the checks in <a href="../accessibility-in-ai-generated-ui/">accessibility in AI-generated UI</a>. The skill library on UI Hub lists Stageshow’s neighbours by role.</p>""",
 zh="""<p>10 月 31 日，设计师 Benji Taylor 开源了 <strong>Stageshow</strong>，一个只做一件事的智能体技能：假产品界面（faux UI）。也就是落地页、功能卡片或文档首屏上那些缩小、简化过的产品画面，可以是一张静帧，也可以是一段带光标的短循环演示。他的观点是，好模型已经能画出这类画面，但结果往往显得笨重、一看就是生成的。Stageshow 想做的，是把设计师手工做这类画面时的上百个小决定写下来，让智能体也能做出这些决定。这条发布帖在 X 上两天内超过 130 万次浏览、2.4 万次收藏，说明很多团队都卡在同一个问题上。</p>
<h2>技能里有什么</h2>
<ul><li><strong>一个核心观点和五种失败。</strong>演示应该看起来像真产品，简化到观众需要的程度，有意图地取景，每个动作都有原因。它会在这几种情况下失败：<em>太满</em>（每一行都是真实文字）、<em>线框图</em>（两个灰块加一个按钮）、<em>装箱</em>（整个窗口缩进一张卡片）、<em>扁平</em>（所有元素一样重）、<em>平淡</em>（不管需求要什么，都是一个灰窗口）。</li>
<li><strong>七步工作流。</strong>媒介与位置、外观、故事、从示例开始、搭画面、编排动作、彩排。大部分质量在写代码前就决定了：演示放在哪、焦点对象是什么、发生什么动作、结果是什么、哪些可以省掉。</li>
<li><strong>标杆示例与正反对照。</strong>几十个参考场景（首屏演示、Bento 网格、图表拖动、拖拽排序、AI 回答流式出现等）、真实产品研究，以及好坏两个版本并排对比。智能体从最接近的标杆示例复制起步，而不是从空白开始。</li>
<li><strong>一套小型 React 组件。</strong>带脚本化 <code>Act</code> API 的 <code>Stage</code>，按真实尺寸绘制的窗口和手机，以及 <code>Roll</code>、<code>Count</code>、<code>Fly</code> 等动效部件。它负责难做的部分，但刻意不提供外观，你要把自己的 Token 映射上去。</li>
<li><strong>把结果录下来的工具。</strong><code>film.mjs</code> 用无头 Chrome 打开页面，拍成一张联系表；<code>layout.mjs</code> 检查文字和控件是否装得下。智能体看自己拍下的画面，先修最大的问题：取景，其次层级，再次动效，最后细节。</li></ul>
<h2>值得直接借用的数字</h2>
<p>这些规则具体到可以检查。按演示实际显示的尺寸来设计：放在文案旁的首屏约 720 × 340，通栏首屏宽 900 到 1100，卡片 400 × 300，另外为 358px 宽的手机栏单独做一版紧凑设计。控制的是文字预算，而不是元素数量：通常 3 到 7 处真实文字，其余用占位条。让首屏窗口有 10% 到 40% 被裁出画面，并至少占画面宽度的三分之二。一个故事是三到五个节拍、10 到 16 秒；结果画面停留约两秒；数据不能在画面内倒退。另外，假应用的标题用 <code>div</code>，绝不用真正的标题标签，因为演示是嵌在别人页面的大纲里的。</p>
<h2>我们的看法</h2>
<p>组件包有用，但真正值得学的是这个技能的结构。它把一份有名字的失败清单、可复制的标杆示例，以及让智能体<em>看见</em>自己产出的方法放在一起。大多数设计技能只做到第一点。「避免杂乱」这种规则很容易同意，也很容易被忽略；但一张录下来的画面摆在标杆示例旁边，就很难忽略。如果你在给团队写设计技能，可以照搬这个结构：失败要有名字，示例要有数字，检查要能让智能体自己跑。</p>
<p>有两件事这个技能留给了你。第一是<strong>无障碍</strong>：一段自动播放、与其他内容并列、长达 10 到 16 秒的循环，按 WCAG 2.2.2 需要提供暂停方式；开启「减少动态效果」的读者应该看到海报帧，而不是动画。Stageshow 强调海报帧本身就要讲清故事，这让事情变简单，但接线要你自己做。第二是<strong>诚实</strong>：一张精致的假界面可能悄悄变成设计规格，或者承诺了一个还不存在的功能。只展示已经上线的东西，把示意图标注为示意图，真实产品变了就重新录。还要留意许可：代码是 MIT，但附带的应用图标和品牌标识仍归各自所有者。</p>
<h2>清单：用智能体做下一个首屏演示</h2>
<ol><li><strong>先安装，再看样例。</strong>运行 <code>npx skills add benjitaylor/skills --skill stageshow</code>，然后启动演示场，把和你想法最接近的标杆示例录一遍。</li>
<li><strong>写代码前先写计划。</strong>位置和尺寸、焦点对象、唯一的动作、结果，以及要省掉什么。</li>
<li><strong>映射你的 Token。</strong>字体、强调色、圆角、浅色或深色底，都取自你的真实产品，而不是组件包默认值。</li>
<li><strong>定文字预算。</strong>故事相关的地方用三到七处真实文字，边缘用占位条。</li>
<li><strong>取景。</strong>一个主体，最多一个跨在其边缘上的辅助对象，窗口从一侧出血，全画面统一一个边距。</li>
<li><strong>编三到五个节拍。</strong>十到十六秒，每次光标移动都有理由，结果画面要停住，循环回到起点。</li>
<li><strong>选定海报帧。</strong>能单独讲清故事的那一帧；在 <code>prefers-reduced-motion</code> 下和缩略图里都用它。</li>
<li><strong>加暂停控件。</strong>超过五秒的自动循环需要它；给演示一个可访问的名称，并让里面的假标题不进入页面大纲。</li>
<li><strong>两个宽度都录。</strong>桌面和 390px；先修最明显的问题，重录直到检查通过，然后自己再看一遍。</li>
<li><strong>做一遍诚实检查。</strong>展示的每个功能今天都已存在；演示标注为示意图；有人负责在界面改版后重录。</li></ol>
<pre><code>demo-plan.md（演示计划）
  位置：    首页首屏，文案旁 · 720×340 · 紧凑版 358
  焦点：    正在被指派的那一行任务
  节拍：    打开菜单 → 选同事 → 头像落位 → 状态滚动更新
  结果：    已指派的行停留 2 秒 · 海报帧 = 这一帧
  文字：    任务标题 · 同事姓名 · 状态   （3 处真实文字）
  无障碍：  暂停按钮 · 减少动态 → 海报帧 · role="img" + 名称
  诚实：    只展示已上线功能 · 标注「示意图」</code></pre>
<h2>UI Hub 能帮什么</h2>
<p>Stageshow 是越来越多设计技能中的一个；<a href="../taste-and-skills-for-agents/">教智能体审美</a>和 <a href="../claude-cursor-design-skills/">Claude 与 Cursor 的设计技能</a>讲了怎么把它们组合起来。它的动效规则可以和<a href="../motion-that-feels-right/">恰到好处的动效</a>对照着读，<a href="../landing-page-teardown-linear-vercel/">Linear 与 Vercel 落地页拆解</a>说明了为什么落地页的第一张图应该是你的真实产品。演示上线前，用 <a href="../accessibility-in-ai-generated-ui/">AI 生成界面的无障碍检查</a>过一遍。UI Hub 的技能库按角色列出了和 Stageshow 相邻的技能。</p>""",
 refs=[('Stageshow','Benji Taylor, benji.org','https://benji.org/stageshow'),('Stageshow launch post','Benji Taylor (@benjitaylor), X','https://x.com/benjitaylor/status/2116593247854453244'),('stageshow/SKILL.md','Benji Taylor, GitHub (benjitaylor/skills)','https://github.com/benjitaylor/skills/blob/main/stageshow/SKILL.md'),('Framing reference','Benji Taylor, GitHub (benjitaylor/skills)','https://github.com/benjitaylor/skills/blob/main/stageshow/references/framing.md'),('Craft reference','Benji Taylor, GitHub (benjitaylor/skills)','https://github.com/benjitaylor/skills/blob/main/stageshow/references/craft.md'),('Motion reference','Benji Taylor, GitHub (benjitaylor/skills)','https://github.com/benjitaylor/skills/blob/main/stageshow/references/motion.md'),('Rehearse reference (filming and checks)','Benji Taylor, GitHub (benjitaylor/skills)','https://github.com/benjitaylor/skills/blob/main/stageshow/references/rehearse.md'),('Notices: licence and third-party assets','Benji Taylor, GitHub (benjitaylor/skills)','https://github.com/benjitaylor/skills/blob/main/stageshow/NOTICE.md'),('Stageshow skill listing','agentools.sh','https://agentools.sh/skills/stageshow/'),('Reply on labelling faux UI as a mock','Muscle AI (@themuscleai), X','https://x.com/themuscleai/status/2116917325613908205'),('Understanding SC 2.2.2: Pause, Stop, Hide','W3C Web Accessibility Initiative','https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html'),('prefers-reduced-motion','MDN Web Docs','https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion'),('The open agent skills ecosystem','skills.sh','https://skills.sh/')]),
]

POSTS2 += [
dict(slug='figma-shaders-ga-ship-shader-backgrounds', date='2026-11-03', cat='tools', series=None, featured=True, tags=['Figma','shaders','code layers','WebGL','accessibility'],
 t=T('Figma shaders are generally available: how to ship shader backgrounds that stay fast and readable',
     'Figma 着色器全面开放：怎样上线既流畅又易读的着色器背景',
     'Figma 著色器全面開放：怎樣上線既流暢又易讀的著色器背景',
     'Figmaのシェーダーが一般提供に：速さと読みやすさを保ったシェーダー背景の出し方',
     'Figma 셰이더 정식 출시: 빠르고 읽기 쉬운 셰이더 배경을 내보내는 법',
     'Shader Figma kini tersedia umum: cara menghantar latar shader yang laju dan mudah dibaca',
     'Shader của Figma đã phát hành chính thức: cách đưa nền shader lên web mà vẫn nhanh và dễ đọc',
     'Les shaders de Figma sont disponibles pour tous : livrer des fonds shader rapides et lisibles',
     'Los shaders de Figma ya están disponibles para todos: cómo publicar fondos con shaders rápidos y legibles',
     'Figma-Shader sind allgemein verfügbar: Shader-Hintergründe ausliefern, die schnell und lesbar bleiben'),
 s=T('On 2 November Figma made shaders generally available, raised export to 4096 px and let shaders travel into code layers. That moves glowing gradients, grain and glass effects from mockups toward real pages. What changed, what is still unclear, and a checklist for shipping a shader without hurting contrast, motion comfort or battery life.',
     '11 月 2 日，Figma 把着色器（shader）开放给所有用户，导出上限提高到 4096 像素，并让着色器可以进入代码图层。发光渐变、颗粒和玻璃效果因此从设计稿更接近真实页面。本文讲改了什么、还有什么不清楚，以及一份在不牺牲对比度、动效舒适度和电量的前提下上线着色器的清单。',
     '11 月 2 日，Figma 把著色器（shader）開放給所有使用者，匯出上限提高到 4096 像素，並讓著色器可以進入程式碼圖層。發光漸層、顆粒和玻璃效果因此從設計稿更接近真實頁面。本文講改了什麼、還有什麼不清楚，以及一份在不犧牲對比度、動效舒適度和電量的前提下上線著色器的清單。',
     '11月2日、Figmaはシェーダーを全ユーザーに一般提供し、書き出しを最大4096pxに引き上げ、シェーダーをコードレイヤーに持ち込めるようにした。光るグラデーションやグレイン、ガラス表現がモックから実際のページに近づく。何が変わったか、まだ不明な点、そしてコントラスト・動きへの配慮・バッテリーを損なわずにシェーダーを出すためのチェックリスト。',
     'Figma는 11월 2일 셰이더를 모든 사용자에게 정식 제공하고, 내보내기 해상도를 4096px까지 올렸으며, 셰이더를 코드 레이어로 가져갈 수 있게 했다. 빛나는 그라데이션, 그레인, 유리 효과가 목업에서 실제 페이지로 한 걸음 다가섰다. 무엇이 바뀌었는지, 아직 불분명한 점, 그리고 대비·모션 편안함·배터리를 해치지 않고 셰이더를 출시하는 체크리스트.',
     'Pada 2 November Figma menjadikan shader tersedia umum, menaikkan eksport hingga 4096 px dan membolehkan shader dibawa ke lapisan kod. Kecerunan bercahaya, butiran dan kesan kaca kini lebih dekat ke halaman sebenar. Apa yang berubah, apa yang masih belum jelas, dan senarai semak untuk menghantar shader tanpa menjejaskan kontras, keselesaan gerakan atau bateri.',
     'Ngày 2/11, Figma phát hành chính thức shader cho mọi người dùng, nâng mức xuất lên 4096 px và cho phép đưa shader vào code layer. Gradient phát sáng, hạt nhiễu và hiệu ứng kính vì thế tiến gần hơn tới trang thật. Điều gì đã thay đổi, điều gì còn chưa rõ, và danh sách kiểm tra để đưa shader lên mà không làm hỏng độ tương phản, sự dễ chịu khi chuyển động hay thời lượng pin.',
     'Le 2 novembre, Figma a ouvert les shaders à tous, porté l’export à 4096 px et permis aux shaders de passer dans les code layers. Dégradés lumineux, grain et effets de verre se rapprochent ainsi des vraies pages. Ce qui change, ce qui reste flou, et une liste pour livrer un shader sans nuire au contraste, au confort de mouvement ni à la batterie.',
     'El 2 de noviembre Figma abrió los shaders a todos los usuarios, subió la exportación a 4096 px y permitió llevarlos a las code layers. Los degradados luminosos, el grano y los efectos de cristal quedan así más cerca de las páginas reales. Qué cambió, qué sigue sin estar claro y una lista para publicar un shader sin perjudicar el contraste, la comodidad con el movimiento ni la batería.',
     'Am 2. November hat Figma Shader für alle freigegeben, den Export auf 4096 px erhöht und Shader in Code-Layer übertragbar gemacht. Leuchtende Verläufe, Körnung und Glaseffekte rücken damit vom Mockup näher an echte Seiten. Was sich geändert hat, was noch offen ist, und eine Checkliste, um Shader auszuliefern, ohne Kontrast, Bewegungskomfort oder Akku zu opfern.'),
 en="""<p>On 2 November Figma shipped a short release note with a big consequence: <strong>shaders are now generally available to all users</strong>, they render and export at up to <strong>4096 px</strong>, and they can be included when you use “build this with code” to turn a design into a <strong>code layer</strong>. Inside a code layer the shader runs when the layer is set to Play. Figma says this part works in the browser on Chrome 157 and is rolling out this week. A week earlier, on 27 October, shaders also gained version history, with an agent-written description for each version.</p>
<p>Put together, a shader is no longer a canvas trick that ends up as a flat PNG or a looping MP4 at handoff. It can stay code. Designers replying to Figma’s announcement on X picked up on exactly that, and one asked the question nobody has answered yet: does the shader stay editable once it lands in code, or is it flattened? That is worth testing before you plan around it.</p>
<h2>What a Figma shader is</h2>
<ul><li><strong>Shader fills</strong> replace a layer’s fill with a generated visual: patterns, mesh gradients, noise, procedural textures such as marble or water. They can be static or animated, apply to fills and strokes, and stack with ordinary fills.</li>
<li><strong>Shader effects</strong> take the layer’s existing pixels as input and change them: grain, blur, distortion, halftone, dithering, colour shifts, even hover-triggered motion.</li>
<li><strong>You build them by prompting.</strong> Open the Figma agent and ask it to “build me a shader”, describe what you want to see, and name the controls you want, such as a slider for glow intensity. Figma’s own tips: say “shader” explicitly (“make me a mesh gradient” may give you a plain image fill), use real-world references (“like a risograph print”), and state what must survive, such as legible text, crisp edges or brand hues.</li>
<li><strong>They behave like design-system parts.</strong> Combinations of shader fills or effects can be saved as styles and published to a team library, and you can view the code behind each one.</li></ul>
<h2>What changed on 2 November, and what did not</h2>
<p>Three things changed: general availability, the 4096 px export ceiling, and the path into code layers. The higher export matters more than it sounds, because a sharp still is exactly what you need as the fallback for a live shader. The code layer path matters because it is the first official route from a Figma shader to running code rather than a video.</p>
<p>Some things did not change. On the canvas only one animated or interactive shader plays per page at a time. Code layers are still in open beta, and code layer generation is free on paid plans only through 4 November; after that it uses AI credits like other agent features. And a code layer is a prototype on the canvas, not your production stack, so treat it as a working reference for engineering, not the final component.</p>
<h2>Our take</h2>
<p>Shaders are the most “fancy” thing a design tool can hand to a developer, and that is the risk. The same properties that make them striking are the ones that break pages: they move behind text, they change brightness frame by frame, and they keep a GPU busy whether anyone is looking or not. A shader that looked fine in a Figma frame can fail contrast on its brightest frame, drain a phone battery, or run a full-screen loop for a reader who asked their system for reduced motion.</p>
<p>So treat a shader like a design token with rules attached, not like an image. Decide where it is allowed (hero backgrounds and illustrations, not behind body copy), how bright it may get, whether it may move, and what replaces it when it cannot run. If you code shaders directly instead of going through Figma, small libraries such as Paper Shaders (zero-dependency WebGL shaders for React and vanilla JavaScript, Apache-2.0, about 1.3 million npm downloads in the week to 2 November) make that easy, but their docs ask you to pin an exact version because breaking changes still ship under 0.0.x.</p>
<h2>Checklist: shipping a shader background</h2>
<ol><li><strong>Prompt for controls, not just a look.</strong> Ask the agent for named sliders (intensity, speed, scale) and for what must stay unchanged, so engineering can tune it without a new prompt.</li>
<li><strong>Save it as a style.</strong> Publish the shader to the team library so every screen uses the same one, and lean on version history when someone changes it.</li>
<li><strong>Export a 4096 px poster.</strong> Use the sharpest still as the fallback image, the social card and the first paint before WebGL starts.</li>
<li><strong>Check contrast on the worst frame.</strong> Body text needs 4.5:1 against the brightest moment of the animation, not the average. Add a scrim behind text if needed.</li>
<li><strong>Respect reduced motion.</strong> Under <code>prefers-reduced-motion: reduce</code>, show the poster or set speed to zero.</li>
<li><strong>Give long motion a pause.</strong> If it moves for more than five seconds next to other content, WCAG 2.2.2 asks for a way to pause, stop or hide it.</li>
<li><strong>Stop when nobody is looking.</strong> Pause the render loop when the canvas leaves the viewport (Intersection Observer) or the tab is hidden.</li>
<li><strong>Budget live canvases.</strong> One live shader per view; everything else uses its still. Browsers cap how many WebGL contexts a page can hold.</li>
<li><strong>Test the code layer handoff.</strong> Build one design with a shader into a code layer and check whether its controls survive, before a team depends on it.</li>
<li><strong>Pin and record.</strong> Pin the shader library version in <code>package.json</code> and note which Figma style version the code matches.</li></ol>
<pre><code>shader-spec.md
  name:      hero-glow (Figma style v3)
  where:     hero background only, never behind body copy
  controls:  intensity 0–1 · speed 0–0.4 · hue locked to brand
  poster:    hero-glow@4096.webp (first paint, og image, reduced motion)
  contrast:  headline + CTA ≥ 4.5:1 on brightest frame · scrim 40%
  motion:    pause button · stops offscreen and on hidden tab
  budget:    1 live canvas per view</code></pre>
<h2>How UI Hub helps</h2>
<p>For the code layer workflow itself, read <a href="../figma-code-layers-and-specs/">Figma code layers and Specs</a>. Motion rules from <a href="../motion-that-feels-right/">motion that feels right</a> apply to shaders too, and <a href="../oklch-color-and-dark-mode/">OKLCH colour and dark mode</a> helps you keep a shader inside your palette on both themes. Before shipping, run the checks in <a href="../accessibility-in-ai-generated-ui/">accessibility in AI-generated UI</a>, and if you would rather code the effect, compare options in <a href="../best-animated-react-component-libraries-2026/">the best animated React component libraries of 2026</a>.</p>""",
 zh="""<p>11 月 2 日，Figma 发布了一条篇幅很短、影响却不小的更新：<strong>着色器（shader）现已向所有用户正式开放</strong>，渲染和导出分辨率最高可达 <strong>4096 像素</strong>，并且在用「build this with code」把设计转换为<strong>代码图层</strong>时，可以把着色器一起带进去。在代码图层里，把图层设为 Play 后着色器就会运行。Figma 表示这一部分需要在浏览器中使用 Chrome 157，本周陆续上线。一周前的 10 月 27 日，着色器还加入了版本历史，每个版本都有一段由智能体写的说明。</p>
<p>把这些放在一起看，着色器不再是一个在交付时被压成静态 PNG 或循环 MP4 的画布技巧，它可以一直保持为代码。在 X 上回复 Figma 公告的设计师们注意到的正是这一点，其中一位提出了目前还没人回答的问题：着色器进入代码后还能继续编辑吗，还是会被拍平？在围绕它做规划之前，值得先自己测一下。</p>
<h2>Figma 的着色器是什么</h2>
<ul><li><strong>着色器填充</strong>用生成的画面替换图层的填充：图案、网格渐变、噪点，以及大理石、水面这类程序化纹理。可以是静态的，也可以是动画；可用于填充和描边，并能和普通填充叠加。</li>
<li><strong>着色器效果</strong>以图层现有的像素为输入并加以改变：颗粒、模糊、扭曲、半色调、抖动、色彩偏移，甚至是鼠标悬停时触发的动效。</li>
<li><strong>通过提示词来做。</strong>打开 Figma 智能体，输入「build me a shader」，描述你想看到的效果，并说出你需要的控件，比如一个调节发光强度的滑块。Figma 自己给的建议：明确说「shader」（只说「做一个网格渐变」可能只得到普通图片填充）；用现实中的参照（「像孔版印刷那样」）；说清楚哪些东西必须保留，比如文字可读、边缘清晰、品牌色相不变。</li>
<li><strong>它们像设计系统的一部分那样工作。</strong>着色器填充或效果的组合可以存成样式并发布到团队库，也可以查看每个着色器背后的代码。</li></ul>
<h2>11 月 2 日改了什么，没改什么</h2>
<p>改了三件事：全面开放、4096 像素的导出上限、进入代码图层的路径。更高的导出分辨率比听起来更重要，因为一张清晰的静帧正是实时着色器需要的备用图。进入代码图层的路径之所以重要，是因为这是 Figma 着色器第一次有官方途径变成可运行的代码，而不是一段视频。</p>
<p>也有没变的。在画布上，每个页面同一时间只能播放一个动画或交互着色器。代码图层仍是公开测试版，付费方案上生成代码图层只免费到 11 月 4 日，之后会像其他智能体功能一样消耗 AI 额度。另外，代码图层是画布上的原型，不是你的生产技术栈，应把它当作给工程师的可运行参考，而不是最终组件。</p>
<h2>我们的看法</h2>
<p>着色器大概是设计工具能交给开发者的最「炫」的东西，而这正是风险所在。让它们抢眼的那些特性，也正是会把页面弄坏的特性：它们在文字后面动，每一帧亮度都在变，而且无论有没有人在看，都让 GPU 一直忙着。一个在 Figma 画框里看起来没问题的着色器，可能在最亮的那一帧对比度不达标，可能耗光手机电量，也可能给一位在系统里开启了「减少动态效果」的读者播放全屏循环动画。</p>
<p>所以，要把着色器当成附带规则的设计 Token，而不是一张图片。决定它允许出现在哪里（首屏背景和插图，而不是正文后面）、最亮可以到多少、能不能动，以及它无法运行时用什么替代。如果你不经过 Figma、直接写着色器代码，Paper Shaders 这类小型库（面向 React 和原生 JavaScript 的零依赖 WebGL 着色器，Apache-2.0 许可，截至 11 月 2 日的一周 npm 下载约 130 万次）会让这件事变得简单，但它的文档要求锁定确切版本，因为 0.0.x 版本之间仍会有破坏性变更。</p>
<h2>清单：上线一个着色器背景</h2>
<ol><li><strong>要控件，而不只是要一个样子。</strong>让智能体提供有名字的滑块（强度、速度、缩放），并说明哪些东西必须保持不变，这样工程师不用重新写提示词就能调整。</li>
<li><strong>存为样式。</strong>把着色器发布到团队库，让每个页面用的都是同一个；有人改动时，借助版本历史追溯。</li>
<li><strong>导出 4096 像素的海报图。</strong>用最清晰的静帧作为备用图、社交分享图，以及 WebGL 启动前的首屏画面。</li>
<li><strong>在最差的那一帧检查对比度。</strong>正文需要在动画最亮的时刻也达到 4.5:1，而不是按平均值算。必要时在文字后面加一层遮罩。</li>
<li><strong>尊重「减少动态效果」。</strong>在 <code>prefers-reduced-motion: reduce</code> 下显示海报图，或把速度设为零。</li>
<li><strong>长时间动效要能暂停。</strong>如果它与其他内容并列、运动超过五秒，WCAG 2.2.2 要求提供暂停、停止或隐藏的方式。</li>
<li><strong>没人看时就停下。</strong>画布离开视口（Intersection Observer）或标签页被隐藏时，暂停渲染循环。</li>
<li><strong>控制实时画布的数量。</strong>每屏只保留一个实时着色器，其余都用静帧。浏览器对一个页面能同时持有的 WebGL 上下文数量有上限。</li>
<li><strong>先测代码图层的交接。</strong>在团队依赖它之前，先把一个带着色器的设计转成代码图层，检查它的控件是否保留下来。</li>
<li><strong>锁版本并记录。</strong>在 <code>package.json</code> 里锁定着色器库的确切版本，并记下代码对应的是哪个版本的 Figma 样式。</li></ol>
<pre><code>shader-spec.md（着色器规格）
  名称：      hero-glow（Figma 样式 v3）
  位置：      只用于首屏背景，绝不放在正文后面
  控件：      强度 0–1 · 速度 0–0.4 · 色相锁定为品牌色
  海报图：    hero-glow@4096.webp（首屏画面、分享图、减少动态效果）
  对比度：    标题和按钮在最亮帧 ≥ 4.5:1 · 遮罩 40%
  动效：      暂停按钮 · 离开视口和标签页隐藏时停止
  预算：      每屏 1 个实时画布</code></pre>
<h2>UI Hub 能帮什么</h2>
<p>代码图层本身的工作流程，请看 <a href="../figma-code-layers-and-specs/">Figma 代码图层与 Specs</a>。<a href="../motion-that-feels-right/">恰到好处的动效</a>里的规则同样适用于着色器，<a href="../oklch-color-and-dark-mode/">OKLCH 色彩与深色模式</a>能帮你让着色器在深浅两种主题下都留在品牌色板之内。上线前，用 <a href="../accessibility-in-ai-generated-ui/">AI 生成界面的无障碍检查</a>过一遍；如果你更想直接写代码实现效果，可以在 <a href="../best-animated-react-component-libraries-2026/">2026 年最值得用的 React 动效组件库</a>里比较选择。</p>""",
 refs=[('Release notes: Export shaders at higher resolutions and bring them into code layers (2 Nov 2026)','Figma','https://www.figma.com/release-notes/'),('Create shaders with the Figma agent','Figma Learn','https://help.figma.com/hc/en-us/articles/41147702210071-Create-shaders-with-the-Figma-agent'),('Use shaders in designs','Figma Learn','https://help.figma.com/hc/en-us/articles/41175721167767-Use-shaders-in-designs'),('Prompting tips for generative plugins and shaders','Figma Learn','https://help.figma.com/hc/en-us/articles/41408020198935-Prompting-tips-for-generative-plugins-and-shaders'),('Workflow lab: Figma Motion, Figma Weave and shaders','Figma Learn','https://help.figma.com/hc/en-us/articles/42847574436119-Workflow-lab-New-tools-more-expression-with-Figma-Motion-Figma-Weave-and-shaders'),('What’s new from Config India 2026 (code layers open beta and credits)','Figma Learn','https://help.figma.com/hc/en-us/articles/43663368947863-What-s-new-from-Config-India-2026'),('Reply asking whether shaders stay editable in code layers','Shaheryar Butt (@SheryButtUXUI), X','https://x.com/SheryButtUXUI/status/2117367128642687211'),('Reply on shaders reaching sites instead of an MP4','Loki (@lokidotdev), X','https://x.com/lokidotdev/status/2117311148962058335'),('paper-design/shaders','Paper, GitHub','https://github.com/paper-design/shaders'),('Paper Shaders gallery','Paper','https://shaders.paper.design/'),('Understanding SC 1.4.3: Contrast (Minimum)','W3C Web Accessibility Initiative','https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html'),('Understanding SC 2.2.2: Pause, Stop, Hide','W3C Web Accessibility Initiative','https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html'),('prefers-reduced-motion','MDN Web Docs','https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion'),('Intersection Observer API','MDN Web Docs','https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API'),('WebGL best practices','MDN Web Docs','https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/WebGL_best_practices')]),
]

POSTS2 += [
dict(slug='safari-adaptive-dark-mode-design-for-it', date='2026-11-04', cat='craft', series=None, featured=True, tags=['Safari','dark mode','color-scheme','CSS','accessibility'],
 t=T('Safari will darken light-only sites for you: design your own dark mode before Adaptive Dark Mode does',
     'Safari 会替你把纯浅色网站变暗：在「自适应深色模式」动手之前，先做好你自己的深色模式',
     'Safari 會替你把純淺色網站變暗：在「自適應深色模式」動手之前，先做好你自己的深色模式',
     'Safariがライト専用サイトを勝手にダークにする：Adaptive Dark Modeより先に自分のダークモードを設計しよう',
     'Safari가 라이트 전용 사이트를 대신 어둡게 만든다: Adaptive Dark Mode보다 먼저 직접 다크 모드를 설계하라',
     'Safari akan menggelapkan laman cerah untuk anda: reka mod gelap sendiri sebelum Adaptive Dark Mode melakukannya',
     'Safari sẽ tự làm tối các trang chỉ có giao diện sáng: hãy tự thiết kế chế độ tối trước khi Adaptive Dark Mode làm thay bạn',
     'Safari va assombrir les sites clairs à votre place : concevez votre mode sombre avant qu’Adaptive Dark Mode ne le fasse',
     'Safari oscurecerá por ti los sitios solo claros: diseña tu propio modo oscuro antes de que lo haga Adaptive Dark Mode',
     'Safari dunkelt helle Websites selbst ab: Gestalten Sie Ihren eigenen Dark Mode, bevor Adaptive Dark Mode es tut'),
 s=T('On 3 November WebKit announced Adaptive Dark Mode in the Safari 27.3 beta: when a reader turns it on, Safari recolours light websites as dark, and your site cannot tell. What it changes, what it skips, the opt-out trap in beta 1, and a checklist for choosing between a real dark theme, letting Safari adapt, or keeping parts light.',
     '11 月 3 日，WebKit 在 Safari 27.3 测试版中发布了「自适应深色模式」（Adaptive Dark Mode）：读者开启后，Safari 会把浅色网站重新着色成深色，而网站本身无法察觉。本文讲它改什么、不改什么、测试版 1 里的退出陷阱，以及一份清单，帮你在「自己做深色主题」「让 Safari 自动适配」「部分区域保持浅色」之间做选择。',
     '11 月 3 日，WebKit 在 Safari 27.3 測試版中發布了「自適應深色模式」（Adaptive Dark Mode）：讀者開啟後，Safari 會把淺色網站重新著色成深色，而網站本身無法察覺。本文講它改什麼、不改什麼、測試版 1 裡的退出陷阱，以及一份清單，幫你在「自己做深色主題」「讓 Safari 自動適配」「部分區域保持淺色」之間做選擇。',
     '11月3日、WebKitはSafari 27.3ベータでAdaptive Dark Modeを発表した。読者が有効にすると、Safariはライトなサイトをダークに塗り替え、サイト側はそれを検知できない。何が変わり何が変わらないか、ベータ1のオプトアウトの落とし穴、そして自前のダークテーマ・Safari任せ・一部をライトのまま残す、の選び方チェックリスト。',
     '11월 3일 WebKit은 Safari 27.3 베타에서 Adaptive Dark Mode를 발표했다. 사용자가 켜면 Safari가 밝은 웹사이트를 어둡게 다시 칠하고, 사이트는 이를 알 수 없다. 무엇을 바꾸고 무엇을 건너뛰는지, 베타 1의 옵트아웃 함정, 그리고 직접 다크 테마를 만들지·Safari에 맡길지·일부를 밝게 둘지 고르는 체크리스트.',
     'Pada 3 November WebKit mengumumkan Adaptive Dark Mode dalam beta Safari 27.3: apabila pembaca menghidupkannya, Safari mewarnakan semula laman cerah menjadi gelap, dan laman anda tidak dapat mengesannya. Apa yang diubah, apa yang dilangkau, perangkap pilihan keluar dalam beta 1, dan senarai semak untuk memilih antara tema gelap sendiri, membiarkan Safari menyesuaikan, atau mengekalkan sebahagian cerah.',
     'Ngày 3/11, WebKit công bố Adaptive Dark Mode trong bản beta Safari 27.3: khi người đọc bật, Safari tô lại các trang sáng thành tối và trang web không thể biết điều đó. Nó thay đổi gì, bỏ qua gì, cái bẫy khi muốn từ chối trong beta 1, và danh sách kiểm tra để chọn giữa tự làm giao diện tối, để Safari tự điều chỉnh, hay giữ một phần ở chế độ sáng.',
     'Le 3 novembre, WebKit a annoncé Adaptive Dark Mode dans la bêta de Safari 27.3 : quand un lecteur l’active, Safari recolore en sombre les sites clairs, sans que le site puisse le savoir. Ce qui change, ce qui est épargné, le piège de l’exclusion dans la bêta 1, et une liste pour choisir entre un vrai thème sombre, laisser Safari adapter ou garder certaines zones claires.',
     'El 3 de noviembre WebKit anunció Adaptive Dark Mode en la beta de Safari 27.3: cuando un lector lo activa, Safari recolorea en oscuro los sitios claros y tu sitio no puede detectarlo. Qué cambia, qué deja intacto, la trampa para excluirse en la beta 1 y una lista para elegir entre un tema oscuro propio, dejar que Safari adapte o mantener partes en claro.',
     'Am 3. November kündigte WebKit Adaptive Dark Mode in der Beta von Safari 27.3 an: Schalten Leser es ein, färbt Safari helle Websites dunkel um, und die Website kann das nicht erkennen. Was es ändert, was es auslässt, die Opt-out-Falle in Beta 1 und eine Checkliste für die Wahl zwischen eigenem Dark Theme, Safari anpassen lassen oder Teile hell halten.'),
 en="""<p>On 3 November the WebKit team announced <strong>Adaptive Dark Mode</strong> in the Safari 27.3 beta. If a reader has their system set to dark and lands on a bright page, Safari offers a preview and a “Try” button; MacRumors reports that after the first try it can be switched on for every site or site by site. Once it is on, Safari recolours light pages as dark. WebKit’s reason is a gap it measures itself: almost 40% of page loads come from people in dark mode, but only about 10% of page loads support it. Apple’s point releases that carry the feature are expected in December, according to MacRumors.</p>
<p>For designers the important line is not the feature but the condition. If your site does not declare dark mode support, a browser engine will now make a dark version of it for some of your readers, using its own rules, and you will not be able to see that it happened.</p>
<h2>What Safari changes, and what it leaves alone</h2>
<ul><li><strong>It skips sites that already declare dark support</strong> with the <code>color-scheme</code> meta tag or <code>color-scheme: light dark</code> in CSS, and pages that are already mostly dark with light text.</li>
<li><strong>On light pages it inverts lightness but keeps hue.</strong> Backgrounds go dark, dark text goes light, and transformed text aims for the WCAG 4.5:1 contrast ratio. Light CSS gradients become dark too.</li>
<li><strong>It tries to keep things usable:</strong> buttons keep contrast against their backgrounds, text stays readable over images, hover menus stay clear. MacRumors adds that it lifts raised surfaces and rebalances layered shadows.</li>
<li><strong>Images are mostly untouched.</strong> SVGs are inspected and recoloured when needed; for bitmaps Safari reads the pixel histogram and inverts simple black-and-white logos.</li>
<li><strong>Some effects get switched off.</strong> Masks and <code>mix-blend-mode</code> may be disabled on transformed elements, and <code>&lt;canvas&gt;</code> content is left as it is.</li>
<li><strong>Your site cannot detect it.</strong> To avoid adding a fingerprinting signal, JavaScript that reads CSS colours gets the authored colours, not the ones on screen.</li></ul>
<h2>The opt-out trap in beta 1</h2>
<p>WebKit’s documented way to keep a page or one element light is <code>color-scheme: light only</code> (or the meta tag with <code>light only</code>). In Safari 27.3 beta 1, the <code>only</code> keyword is not supported yet. That leaves a tempting shortcut: declare <code>light dark</code> so Safari leaves you alone. Don’t do it without real dark styles. That declaration tells every browser you handle dark mode, so built-in parts such as form controls, scrollbars and the default page background follow the reader’s dark preference, while your hard-coded light colours stay light. You trade Safari’s attempt at a dark page for a mixed one that you made yourself.</p>
<h2>Our take</h2>
<p>An automatic dark theme is a floor, not a design. It is probably better than a glaring white page at midnight, and WebKit clearly worked hard on contrast. But it makes decisions a designer would want to make: how light your brand colour becomes when its lightness flips, which surfaces sit above others, whether a photo with a baked-in white box looks pasted on. And because the change is invisible to scripts, you will not see it in analytics or in screenshots your monitoring takes; you will only see it if you open the page in Safari yourself.</p>
<p>The good news is that a real dark theme is cheaper than it used to be. <code>light-dark()</code> lets one token hold both values, <code>color-mix()</code> derives hover and border shades, and a coding agent can do most of the mechanical work of moving scattered hex values into tokens. The design work that remains is the part worth doing by hand: choosing the dark palette, checking contrast and deciding what must stay light.</p>
<h2>Checklist: decide before Safari decides for you</h2>
<ol><li><strong>Look at it first.</strong> In the Safari 27.3 beta, set the system to dark, open your key pages and tap Try. Screenshot the home page, a form, a table and anything with your logo.</li>
<li><strong>Pick a path per site.</strong> A real dark theme for products people use for long sessions; letting Safari adapt for simple content sites; light only for areas where colour is the content.</li>
<li><strong>If you go dark, use tokens.</strong> Put every colour in a token, write both values with <code>light-dark()</code>, and declare <code>color-scheme: light dark</code> in the HTML head, not later from JavaScript.</li>
<li><strong>Check contrast in both themes.</strong> Body text 4.5:1, large text and icons 3:1, including focus rings, disabled states and placeholder text.</li>
<li><strong>Fix the inputs Safari struggles with.</strong> Logos and icons as SVG, images with transparent backgrounds rather than a baked page colour, CSS colours instead of tiled background images or sprites.</li>
<li><strong>Mark what must stay light.</strong> Product photos, charts with semantic colours, brand artwork: plan <code>color-scheme: light only</code> on those elements and re-test when a later beta supports <code>only</code>.</li>
<li><strong>Remember canvas and blend modes.</strong> Shaders, charts drawn to canvas and <code>mix-blend-mode</code> effects will not be adapted, or may be switched off, so they need their own dark versions.</li>
<li><strong>Don’t fake support.</strong> Never ship <code>light dark</code> as an opt-out without dark styles behind it.</li></ol>
<pre><code>/* in &lt;head&gt;: &lt;meta name="color-scheme" content="light dark"&gt; */
:root {
  color-scheme: light dark;
  --bg:      light-dark(#f7f7f5, #0e0f13);
  --surface: light-dark(#ffffff, #171922);
  --ink:     light-dark(#111318, #eceef4);
  --muted:   light-dark(#4b5162, #a4abbd);
  --accent:  light-dark(#2453d6, #8aa8ff);
  --line:    color-mix(in oklch, var(--ink) 14%, transparent);
}
body { background: var(--bg); color: var(--ink); }
/* areas that must stay light (once Safari supports "only") */
.product-photos, .brand-art { color-scheme: light only; }</code></pre>
<h2>How UI Hub helps</h2>
<p>For the basics of a hand-made dark theme, start with <a href="../dark-mode-done-right/">dark mode done right</a>; for building the palette itself, read <a href="../oklch-color-and-dark-mode/">OKLCH colour and dark mode</a>, and keep the tokens where agents can read them with <a href="../design-tokens-for-agents/">design tokens for agents</a>. Run the contrast and focus checks in <a href="../accessibility-in-ai-generated-ui/">accessibility in AI-generated UI</a> on both themes. If your hero uses a canvas or shader, <a href="../figma-shaders-ga-ship-shader-backgrounds/">shipping shader backgrounds</a> covers the fallbacks you will need, since Safari leaves canvas content alone.</p>""",
 zh="""<p>11 月 3 日，WebKit 团队在 Safari 27.3 测试版中发布了<strong>自适应深色模式</strong>（Adaptive Dark Mode）。如果读者把系统设为深色，又打开了一个很亮的页面，Safari 会提供预览和一个「Try」按钮；据 MacRumors 报道，试用一次之后，可以选择对所有网站开启，或者逐个网站开启。开启后，Safari 会把浅色页面重新着色成深色。WebKit 给出的理由是它自己测到的差距：将近 40% 的页面加载来自使用深色模式的用户，但只有大约 10% 的页面加载支持深色模式。MacRumors 称，带有这项功能的系统更新预计在 12 月推出。</p>
<p>对设计师来说，关键不在功能本身，而在它的触发条件：如果你的网站没有声明支持深色模式，浏览器引擎现在会按它自己的规则，给你的部分读者生成一个深色版本，而你无法看到这件事发生了。</p>
<h2>Safari 改什么，不改什么</h2>
<ul><li><strong>已声明支持深色的网站会被跳过</strong>：用了 <code>color-scheme</code> meta 标签，或在 CSS 里写了 <code>color-scheme: light dark</code>；本来就以深色背景、浅色文字为主的页面也不受影响。</li>
<li><strong>对浅色页面，它反转明度但保留色相。</strong>背景变深，深色文字变浅，转换后的文字以 WCAG 4.5:1 的对比度为目标。浅色的 CSS 渐变也会变深。</li>
<li><strong>它会尽量保持可用：</strong>按钮和背景之间保持对比，图片上的文字保持可读，悬停菜单保持清晰。MacRumors 补充说，它还会把浮起的表面提亮，并重新平衡叠加的阴影。</li>
<li><strong>图片大多不动。</strong>SVG 会被检查，必要时重新着色；位图则会分析像素直方图，把简单的黑白 Logo 反色。</li>
<li><strong>部分效果会被关掉。</strong>被转换的元素上，遮罩和 <code>mix-blend-mode</code> 可能会被停用；<code>&lt;canvas&gt;</code> 里的内容保持原样。</li>
<li><strong>网站察觉不到。</strong>为了不增加可用于指纹追踪的信号，JavaScript 读取 CSS 颜色时拿到的是作者写的原始颜色，而不是屏幕上显示的颜色。</li></ul>
<h2>测试版 1 里的退出陷阱</h2>
<p>WebKit 文档里让页面或某个元素保持浅色的方法是 <code>color-scheme: light only</code>（或在 meta 标签里写 <code>light only</code>）。但在 Safari 27.3 测试版 1 中，<code>only</code> 关键字还不支持。于是出现一个诱人的捷径：声明 <code>light dark</code>，让 Safari 别管你。如果没有真正的深色样式，不要这样做。这个声明是在告诉所有浏览器「我自己处理深色模式」，于是表单控件、滚动条、默认页面背景这些浏览器自带的部分会跟随读者的深色偏好，而你写死的浅色仍然是浅色。你等于用一个自己造成的「深浅混搭」页面，换掉了 Safari 尝试生成的深色页面。</p>
<h2>我们的看法</h2>
<p>自动生成的深色主题是底线，不是设计。在半夜，它大概比一个刺眼的白页面好，WebKit 显然也在对比度上下了功夫。但它替你做了本该由设计师做的决定：品牌色在明度翻转后会变得多浅、哪些表面应该浮在其他表面之上、一张自带白底的图片会不会像贴上去的。而且这种变化对脚本不可见，你在数据分析里看不到，监控工具截的图里也看不到；只有你自己用 Safari 打开页面时才会看到。</p>
<p>好消息是，做一个真正的深色主题比以前便宜多了。<code>light-dark()</code> 让一个 Token 同时保存两种取值，<code>color-mix()</code> 可以推导出悬停色和边框色，把散落各处的十六进制颜色值整理成 Token 这类机械工作，大部分可以交给编程智能体。剩下的设计工作才是值得亲手做的：选定深色色板、检查对比度、决定哪些地方必须保持浅色。</p>
<h2>清单：在 Safari 替你决定之前，先做决定</h2>
<ol><li><strong>先亲眼看看。</strong>在 Safari 27.3 测试版里把系统设为深色，打开你的关键页面并点 Try。给首页、一个表单、一个表格和所有带 Logo 的地方截图。</li>
<li><strong>按网站选路线。</strong>用户长时间使用的产品，做真正的深色主题；简单的内容网站，可以让 Safari 自动适配；颜色本身就是内容的区域，保持浅色。</li>
<li><strong>如果做深色，就用 Token。</strong>把每个颜色都放进 Token，用 <code>light-dark()</code> 写出两种取值，并在 HTML head 里声明 <code>color-scheme: light dark</code>，不要等 JavaScript 稍后注入。</li>
<li><strong>两种主题都查对比度。</strong>正文 4.5:1，大字号文字和图标 3:1，包括焦点框、禁用状态和占位文字。</li>
<li><strong>修好 Safari 难处理的素材。</strong>Logo 和图标用 SVG；图片用透明背景，不要把页面底色烤进图片；用 CSS 颜色代替平铺背景图和雪碧图。</li>
<li><strong>标出必须保持浅色的部分。</strong>商品照片、带语义颜色的图表、品牌插画：计划在这些元素上用 <code>color-scheme: light only</code>，等后续测试版支持 <code>only</code> 后再测一遍。</li>
<li><strong>别忘了 canvas 和混合模式。</strong>着色器、画在 canvas 上的图表以及 <code>mix-blend-mode</code> 效果不会被适配，或者可能被关掉，它们需要自己的深色版本。</li>
<li><strong>不要假装支持。</strong>绝不要在没有深色样式的情况下，用 <code>light dark</code> 当作退出开关。</li></ol>
<pre><code>/* 在 &lt;head&gt; 中：&lt;meta name="color-scheme" content="light dark"&gt; */
:root {
  color-scheme: light dark;
  --bg:      light-dark(#f7f7f5, #0e0f13);   /* 页面背景 */
  --surface: light-dark(#ffffff, #171922);   /* 卡片表面 */
  --ink:     light-dark(#111318, #eceef4);   /* 正文 */
  --muted:   light-dark(#4b5162, #a4abbd);   /* 次要文字 */
  --accent:  light-dark(#2453d6, #8aa8ff);   /* 强调色 */
  --line:    color-mix(in oklch, var(--ink) 14%, transparent);
}
body { background: var(--bg); color: var(--ink); }
/* 必须保持浅色的区域（等 Safari 支持 "only" 后生效） */
.product-photos, .brand-art { color-scheme: light only; }</code></pre>
<h2>UI Hub 能帮什么</h2>
<p>亲手做深色主题的基础，先看<a href="../dark-mode-done-right/">把暗色模式做对</a>；搭建色板本身，请看 <a href="../oklch-color-and-dark-mode/">OKLCH 色彩与深色模式</a>；用 <a href="../design-tokens-for-agents/">面向智能体的设计 Token</a> 把 Token 放在智能体读得到的地方。在两种主题下都用 <a href="../accessibility-in-ai-generated-ui/">AI 生成界面的无障碍检查</a>过一遍对比度和焦点。如果你的首屏用了 canvas 或着色器，<a href="../figma-shaders-ga-ship-shader-backgrounds/">上线着色器背景</a>一文讲了你需要的备用方案，因为 Safari 不会改动 canvas 里的内容。</p>""",
 refs=[('Introducing Adaptive Dark Mode','Simon Fraser, Luming Yin, Lily Spiniolas, Joanne Pan, Veda Periwal and Jen Simmons, WebKit','https://webkit.org/blog/18541/introducing-adaptive-dark-mode/'),('iOS 27.3 Adds Vertical Tabs and Adaptive Dark Mode to Safari','Juli Clover, MacRumors','https://www.macrumors.com/2026/11/03/ios-27-3-safari/'),('Safari’s new dark mode repaints light websites without the sites knowing','PPC Land','https://ppc.land/safaris-new-dark-mode-repaints-light-websites-without-the-sites-knowing/'),('Safari 27.3 Beta Adds Adaptive Dark Mode for Light Websites','Technobezz','https://www.technobezz.com/news/safari-beta-adds-adaptive-dark-mode'),('Safari introduces Adaptive Dark Mode in 27.3 (discussion)','Hacker News','https://news.ycombinator.com/item?id=50358562'),('color-scheme','MDN Web Docs','https://developer.mozilla.org/en-US/docs/Web/CSS/color-scheme'),('light-dark()','MDN Web Docs','https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/light-dark'),('prefers-color-scheme','MDN Web Docs','https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme'),('color-mix()','MDN Web Docs','https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/color-mix'),('contrast-color()','MDN Web Docs','https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/contrast-color'),('Improved dark mode default styling with the color-scheme CSS property and the corresponding meta tag','web.dev','https://web.dev/articles/color-scheme'),('CSS Color Adjustment Module Level 1','W3C CSS Working Group (editor’s draft)','https://drafts.csswg.org/css-color-adjust-1/'),('Understanding SC 1.4.3: Contrast (Minimum)','W3C Web Accessibility Initiative','https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html')]),
]

POSTS2 += [
dict(slug='design-on-running-code-dessn-doop-code-canvas', date='2026-11-05', cat='workflow', series=None, featured=True, tags=['Dessn','Doop','Figma','code layers','MCP','agents','design systems'],
 t=T('Design on running code: Dessn, Doop and Figma turn the canvas into a place agents and designers share',
     '在运行中的代码上做设计：Dessn、Doop 和 Figma 正在把画布变成设计师与智能体共用的地方',
     '在執行中的程式碼上做設計：Dessn、Doop 和 Figma 正在把畫布變成設計師與智慧體共用的地方',
     '動くコードの上でデザインする：Dessn、Doop、Figmaがキャンバスをデザイナーとエージェントの共有の場に変える',
     '실행 중인 코드 위에서 디자인하기: Dessn, Doop, Figma가 캔버스를 디자이너와 에이전트가 함께 쓰는 곳으로 바꾼다',
     'Reka bentuk di atas kod yang sedang berjalan: Dessn, Doop dan Figma menjadikan kanvas ruang kongsi pereka dan ejen',
     'Thiết kế trên mã đang chạy: Dessn, Doop và Figma biến canvas thành nơi nhà thiết kế và agent cùng làm việc',
     'Concevoir sur du code qui tourne : Dessn, Doop et Figma font du canevas un espace partagé entre designers et agents',
     'Diseñar sobre código en ejecución: Dessn, Doop y Figma convierten el lienzo en un espacio compartido por diseñadores y agentes',
     'Auf laufendem Code gestalten: Dessn, Doop und Figma machen die Arbeitsfläche zum gemeinsamen Ort für Designer und Agents'),
 s=T('On 4 November Dessn launched a canvas that runs your real app from your repo, the open-source Doop canvas trended on GitHub, and a day earlier Figma’s code layers started reading prototype connections. Two kinds of agent canvas are emerging: frames that are your app, and frames that are loose HTML. How they differ, what to check before connecting a repo, and a checklist for designing on code.',
     '11 月 4 日，Dessn 发布了一个直接从你的代码仓库运行真实应用的画布；开源画布 Doop 登上 GitHub 趋势榜；前一天，Figma 的代码图层开始读取原型连线。智能体画布正在分成两类：画框就是你的应用，或者画框只是独立的 HTML。本文讲两者的区别、接入代码仓库前要检查什么，以及一份「在代码上做设计」的清单。',
     '11 月 4 日，Dessn 發布了一個直接從你的程式碼倉庫執行真實應用的畫布；開源畫布 Doop 登上 GitHub 趨勢榜；前一天，Figma 的程式碼圖層開始讀取原型連線。智慧體畫布正在分成兩類：畫框就是你的應用，或者畫框只是獨立的 HTML。本文講兩者的區別、接入程式碼倉庫前要檢查什麼，以及一份「在程式碼上做設計」的清單。',
     '11月4日、リポジトリから実際のアプリを動かすキャンバスDessnが公開され、オープンソースのキャンバスDoopがGitHubのトレンドに入り、その前日にはFigmaのコードレイヤーがプロトタイプの接続を読むようになった。エージェント向けキャンバスは「フレーム＝自分のアプリ」と「フレーム＝単独のHTML」の2種類に分かれつつある。違い、リポジトリ接続前の確認点、コード上でデザインするためのチェックリスト。',
     '11월 4일 저장소에서 실제 앱을 그대로 실행하는 캔버스 Dessn이 출시됐고, 오픈소스 캔버스 Doop이 GitHub 트렌딩에 올랐으며, 하루 전 Figma 코드 레이어는 프로토타입 연결을 읽기 시작했다. 에이전트용 캔버스는 ‘프레임이 곧 내 앱’인 것과 ‘프레임이 독립 HTML’인 것으로 나뉘고 있다. 차이점, 저장소 연결 전 확인할 점, 코드 위에서 디자인하기 위한 체크리스트.',
     'Pada 4 November Dessn melancarkan kanvas yang menjalankan aplikasi sebenar daripada repo anda, kanvas sumber terbuka Doop menjadi trending di GitHub, dan sehari sebelumnya lapisan kod Figma mula membaca sambungan prototaip. Dua jenis kanvas ejen sedang muncul: bingkai yang ialah aplikasi anda, dan bingkai HTML bebas. Perbezaannya, perkara untuk disemak sebelum menyambung repo, dan senarai semak.',
     'Ngày 4/11, Dessn ra mắt canvas chạy ứng dụng thật từ repo của bạn, canvas mã nguồn mở Doop lên xu hướng GitHub, và một ngày trước đó code layer của Figma bắt đầu đọc các liên kết prototype. Đang hình thành hai loại canvas cho agent: frame chính là ứng dụng của bạn, và frame là HTML rời. Khác biệt, những gì cần kiểm tra trước khi kết nối repo, và một checklist.',
     'Le 4 novembre, Dessn a lancé un canevas qui exécute votre vraie application depuis votre dépôt, le canevas open source Doop est apparu dans les tendances GitHub, et la veille les calques de code de Figma ont commencé à lire les connexions de prototype. Deux types de canevas pour agents émergent : des cadres qui sont votre application, et des cadres en HTML libre. Différences, vérifications avant de connecter un dépôt, et une checklist.',
     'El 4 de noviembre Dessn lanzó un lienzo que ejecuta tu aplicación real desde tu repositorio, el lienzo de código abierto Doop fue tendencia en GitHub y un día antes las capas de código de Figma empezaron a leer las conexiones del prototipo. Surgen dos tipos de lienzo para agentes: marcos que son tu aplicación y marcos de HTML suelto. En qué se diferencian, qué revisar antes de conectar un repositorio y una checklist.',
     'Am 4. November startete Dessn eine Arbeitsfläche, die Ihre echte App aus dem Repository ausführt, die Open-Source-Fläche Doop landete in den GitHub-Trends, und einen Tag zuvor begannen Figmas Code-Ebenen, Prototyp-Verbindungen zu lesen. Zwei Arten von Agent-Flächen entstehen: Frames, die Ihre App sind, und Frames aus losem HTML. Unterschiede, Prüfpunkte vor dem Verbinden eines Repos und eine Checkliste.'),
 en="""<p>Three releases in two days point the same way. On 4 November <strong>Dessn</strong> launched on Product Hunt with a simple pitch: connect GitHub, GitLab or Bitbucket, and it renders your frontend one to one on a design canvas, with the backend mocked, so the team and their agents look at what is actually live. The same day the open-source <strong>Doop</strong>, a multiplayer canvas where people and AI agents edit HTML frames together, showed up on GitHub’s trending list. And on 3 November <strong>Figma</strong> said that when you turn design frames into a code layer, its agent now reads the prototype connections and interactions between them; it also made repository cloning the default for new GitHub connections.</p>
<p>None of these is “AI generates a mockup”. They are about where the design and the agent meet: a shared canvas that an agent can write to over MCP (the Model Context Protocol that lets coding agents call tools) and that a person can click through.</p>
<h2>Two kinds of agent canvas</h2>
<ul><li><strong>Frames that are your app.</strong> In Dessn, a frame holds the app’s codebase. Its agent guidance says a new page, state or variation is a copy of the app’s frame whose code the agent writes, that components should be reused or modified rather than recreated, and that the change goes home as a patch, commits or a bundle. Dessn also exposes the components and tokens the app really uses, with file and line. Figma’s code layers sit nearby: you can import a GitHub repo or convert frames, and now the prototype wiring travels with them.</li>
<li><strong>Frames that are loose HTML.</strong> Doop frames render HTML in sandboxed iframes. Agents connect over MCP with OAuth and work as you; its README lists 42 tools, including streaming a design into a frame section by section and taking a screenshot so the agent can review its own work. A built-in agent runs on GPT, Claude, Gemini, DeepSeek, Kimi or Qwen models. It is AGPL-3.0, self-hostable with an embedded Postgres, and calls itself an open-source alternative to Paper.</li></ul>
<p>Dessn’s own docs draw the same line: real-app frames are what it is for, and HTML frames are for notes, annotations and visuals that are not a page of the app, such as an OG image or a moodboard.</p>
<h2>Our take</h2>
<p>The difference matters more than the brand names. An HTML frame is a fast sketch: great for exploring five directions, but every one of them still has to be translated into your components, and that translation is where design systems drift. A frame that runs your code skips the translation, because the variation is already a diff against your app. The cost moves elsewhere: you are now connecting a repository, deciding what data the mocked backend shows, and reviewing a code change rather than a picture.</p>
<p>That shift also changes what a designer reviews. On a code canvas the useful questions are no longer “is this pixel right” but “did the agent reuse our Button, did it handle the empty and error states, and does the diff touch anything it should not”. Figma reading prototype connections is a small version of the same idea: the flow you wired becomes input for the code, so wiring the flow carefully is now part of the spec.</p>
<p>We would not pick one canvas for everything. Use an HTML canvas to explore directions quickly and cheaply, then move the winner onto a frame that runs your code before anyone calls it done.</p>
<h2>Checklist: designing on running code</h2>
<ol><li><strong>Decide what the frame is.</strong> Your app (code-backed) for anything that will ship; loose HTML for exploration, moodboards and one-off visuals. Label exploration boards so nobody treats them as spec.</li>
<li><strong>Check repository access first.</strong> Know which repos are connected, whether the tool only reads or also clones, and who can see them. In Figma, new GitHub connections now clone by default; admins can turn it off per repository.</li>
<li><strong>Seed realistic mock data.</strong> If the backend is mocked, make sure the canvas shows real-looking names, long strings, empty lists and error responses, not just the happy path.</li>
<li><strong>Tell agents to reuse, not recreate.</strong> Put “reuse or modify existing components; never rebuild one” in your agent rules, and run your design-system lint on every diff.</li>
<li><strong>Wire the flow before you generate.</strong> In Figma, connect the prototype frames and interactions first, since the code layer agent now reads them.</li>
<li><strong>Review by clicking, then by diff.</strong> Click through every state on the canvas, then read the patch: changed files, new dependencies, hard-coded colours.</li>
<li><strong>Keep one source of truth.</strong> After the change merges, refresh the canvas from the repo so the next round starts from production, not from yesterday’s frame.</li>
<li><strong>Read the licence if you self-host.</strong> Doop is AGPL-3.0: if you modify it and let others use it over a network, you must offer them your modified source.</li></ol>
<pre><code># Brief for an agent working on a code-backed canvas
Goal:       add an empty state + error state to the Invoices page
Frame:      copy the live Invoices frame; do not start from blank HTML
Reuse:      EmptyState, Alert, Button from src/components (no new components)
Tokens:     colours and spacing from tokens.css only, no hex values
Data:       mock 0 invoices, 1 invoice, 240 invoices, and a 500 error
States:     loading · empty · error · long names · 375px width
Deliver:    playable frame + patch; list every changed file
Never:      touch API code, add dependencies, or change other pages</code></pre>
<h2>How UI Hub helps</h2>
<p>For the Figma side, read <a href="../figma-code-layers-and-specs/">Figma code layers and Specs</a>. Pointing at a running app instead of describing it is covered in <a href="../annotate-dont-describe-visual-prompts/">annotate, don’t describe</a>. To make agents reuse your components, use <a href="../lint-agents-onto-your-design-system/">lint agents onto your design system</a> and keep tokens readable with <a href="../design-tokens-for-agents/">design tokens for agents</a>. <a href="../github-replica-design-system-prototypes/">GitHub Replica</a> shows a related approach where reviewed design-system guidance drives prototypes.</p>""",
 zh="""<p>两天里的三个发布，指向同一个方向。11 月 4 日，<strong>Dessn</strong> 在 Product Hunt 上发布，卖点很直接：连上 GitHub、GitLab 或 Bitbucket，它就把你的前端一比一渲染到设计画布上，后端用模拟数据代替，让团队和他们的智能体看到的都是真正上线的东西。同一天，开源的 <strong>Doop</strong>（一个让人和 AI 智能体一起编辑 HTML 画框的多人画布）出现在 GitHub 趋势榜上。11 月 3 日，<strong>Figma</strong> 宣布：把设计画框转成代码图层时，它的智能体现在会读取画框之间的原型连线和交互；同时，新建的 GitHub 连接默认允许克隆代码仓库。</p>
<p>这些都不是「AI 生成一张效果图」。它们讨论的是设计和智能体在哪里相遇：一个智能体可以通过 MCP（让编程智能体调用外部工具的模型上下文协议）写入、人可以直接点着试用的共享画布。</p>
<h2>两类智能体画布</h2>
<ul><li><strong>画框就是你的应用。</strong>在 Dessn 里，一个画框装着整个应用的代码。它给智能体的指南写道：新页面、新状态或新变体，都是复制一份应用画框，再由智能体改写其中的代码；组件应该复用或修改，而不是重新造一个；改动以补丁、提交或代码包的形式带回本地。Dessn 还会列出应用真正在用的组件和 Token，并标明文件和行号。Figma 的代码图层与它相近：你可以导入 GitHub 仓库或转换画框，现在原型连线也会一起带过去。</li>
<li><strong>画框只是独立的 HTML。</strong>Doop 的画框在沙盒 iframe 里渲染 HTML。智能体通过带 OAuth 的 MCP 接入，以你的身份工作；它的 README 列出了 42 个工具，包括把设计一段一段流式写入画框，以及截图让智能体检查自己的作品。内置智能体可以用 GPT、Claude、Gemini、DeepSeek、Kimi 或 Qwen 模型。它采用 AGPL-3.0 许可，可以带着内嵌的 Postgres 自行部署，并自称是 Paper 的开源替代品。</li></ul>
<p>Dessn 自己的文档也划了同一条线：真实应用画框才是它的主业，HTML 画框用来放笔记、批注和不属于应用页面的视觉内容，比如 OG 分享图或情绪板。</p>
<h2>我们的看法</h2>
<p>两类画布的区别，比品牌名字更重要。HTML 画框是快速草图：适合同时探索五个方向，但每一个最终都得翻译成你的组件，而设计系统恰恰是在这一步跑偏的。运行你代码的画框省掉了翻译，因为变体本身就是针对你应用的一份代码差异。成本转移到了别处：你要接入代码仓库，要决定模拟后端展示什么数据，要审查的是代码改动，而不是一张图。</p>
<p>这也改变了设计师审查的内容。在代码画布上，有用的问题不再是「这个像素对不对」，而是「智能体有没有复用我们的 Button、有没有处理空状态和错误状态、这份差异有没有碰到不该碰的地方」。Figma 读取原型连线是同一思路的小版本：你连好的流程会成为生成代码的输入，所以认真连流程现在也是需求说明的一部分。</p>
<p>我们不建议用一种画布做所有事。用 HTML 画布又快又便宜地探索方向，选定之后，在有人宣布「完成」之前，把它搬到运行你代码的画框上。</p>
<h2>清单：在运行中的代码上做设计</h2>
<ol><li><strong>先决定画框是什么。</strong>要上线的东西用你的应用（代码支撑的画框）；探索、情绪板和一次性视觉用独立 HTML。给探索用的画板加上标注，免得有人把它当成需求。</li>
<li><strong>先查代码仓库权限。</strong>弄清楚连了哪些仓库、工具只是读取还是会克隆、谁能看到。在 Figma 里，新建的 GitHub 连接现在默认克隆；管理员可以按仓库关闭。</li>
<li><strong>准备真实感的模拟数据。</strong>如果后端是模拟的，确保画布上有像真的名字、超长字符串、空列表和报错返回，而不只是一切顺利的情况。</li>
<li><strong>让智能体复用，而不是重造。</strong>在智能体规则里写上「复用或修改现有组件，绝不重新造一个」，并对每份差异跑一遍设计系统检查。</li>
<li><strong>先连流程，再生成。</strong>在 Figma 里，先把原型画框和交互连好，因为代码图层的智能体现在会读取它们。</li>
<li><strong>先点着看，再读差异。</strong>在画布上把每个状态都点一遍，然后读补丁：改了哪些文件、新增了哪些依赖、有没有写死的颜色。</li>
<li><strong>只保留一个事实来源。</strong>改动合并后，从仓库刷新画布，让下一轮从线上版本开始，而不是从昨天的画框开始。</li>
<li><strong>自行部署就读许可证。</strong>Doop 采用 AGPL-3.0：如果你修改了它并让别人通过网络使用，就必须向他们提供修改后的源代码。</li></ol>
<pre><code># 给在代码画布上工作的智能体的任务说明
目标：     给发票页面加上空状态和错误状态
画框：     复制线上的发票页画框，不要从空白 HTML 开始
复用：     src/components 里的 EmptyState、Alert、Button（不新建组件）
Token：    颜色和间距只用 tokens.css，不写十六进制颜色
数据：     模拟 0 张、1 张、240 张发票，以及一次 500 错误
状态：     加载 · 空 · 错误 · 超长名称 · 375px 宽度
交付：     可点击的画框 + 补丁；列出所有改动的文件
禁止：     改 API 代码、加依赖、改其他页面</code></pre>
<h2>UI Hub 能帮什么</h2>
<p>Figma 这一侧，请看 <a href="../figma-code-layers-and-specs/">Figma 代码图层与 Specs</a>。直接指着运行中的应用说话、而不是用文字描述，见<a href="../annotate-dont-describe-visual-prompts/">标注，而不是描述</a>。想让智能体复用你的组件，用<a href="../lint-agents-onto-your-design-system/">用检查把智能体拉回设计系统</a>，并用<a href="../design-tokens-for-agents/">面向智能体的设计 Token</a> 让 Token 保持可读。<a href="../github-replica-design-system-prototypes/">GitHub Replica</a> 展示了一种相关做法：由审核过的设计系统指南驱动原型。</p>""",
 refs=[('Dessn: the design canvas that runs your real code (Product Hunt launch, 4 Nov 2026)','Hunted.space','https://hunted.space/product/dessn-2'),('Dessn','Dessn','https://www.dessn.ai/'),('We built what you wished Figma could be (launch video)','Dessn, via posts.design','https://posts.design/gabriella-we-built-what-you-wished-figma-could-2026-11-04'),('kgoedecke/doop','kgoedecke, GitHub','https://github.com/kgoedecke/doop'),('Get started','Doop','https://doop.design/docs/get-started'),('The design MCP for Claude Code','Doop','https://doop.design/design-mcp-for-claude-code'),('doop open-source canvas lets AI agents design live with humans','Marcello Babbili, Not a Tech Guy','https://www.notatechguy.com/doop-open-source-canvas-lets-ai-agents-design-live-with-humans/'),('Release notes: prototype connections as context for code layers; cloning by default (3 Nov 2026)','Figma','https://www.figma.com/release-notes/'),('What’s new from Config India 2026 (code layers open beta)','Figma Learn','https://help.figma.com/hc/en-us/articles/43663368947863-What-s-new-from-Config-India-2026'),('Paper','Paper','https://paper.design/'),('Authorization','Model Context Protocol specification','https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization'),('GNU Affero General Public License v3.0','choosealicense.com','https://choosealicense.com/licenses/agpl-3.0/')]),
dict(slug='figma-agent-vector-strokes-icons', date='2026-11-06', cat='tools', series=None, featured=True, tags=['Figma','vectors','icons','strokes','Figma Motion','agent'],
 t=T('Figma’s agent now draws icons as strokes: keep the line weight editable',
     'Figma 智能体开始用描边画图标：让线宽继续可改',
     'Figma 智慧體開始用描邊畫圖示：讓線寬繼續可改',
     'Figmaのエージェントがアイコンをストロークで描く：線幅を編集可能なままにする',
     'Figma 에이전트가 아이콘을 스트로크로 그린다: 선 굵기를 계속 편집 가능하게',
     'Ejen Figma kini melukis ikon sebagai strok: kekalkan tebal garisan boleh diedit',
     'Agent Figma giờ vẽ icon bằng stroke: giữ độ dày nét vẫn chỉnh được',
     'L’agent Figma dessine désormais les icônes en traits : gardez l’épaisseur éditable',
     'El agente de Figma ahora dibuja iconos con trazos: mantén el grosor editable',
     'Figmas Agent zeichnet Icons jetzt als Striche: die Strichstärke bleibt editierbar'),
 s=T('On 5 November 2026 Figma improved agent-generated vector illustrations and icons: line work comes as strokes (not filled outlines), layers are grouped for editing, you can attach style references, and the structure is ready for Figma Motion. Why that matters for icon systems, how to brief the agent, and a checklist from prompt to shipped SVG.',
     '2026 年 11 月 5 日，Figma 改进了智能体生成的矢量插画和图标：线条用描边而不是填色轮廓、图层按功能分组便于修改、可挂上风格参考，结构也适合用 Figma Motion 做动画。这对图标系统意味着什么、怎么给智能体写提示，以及从提示到上线 SVG 的一份清单。',
     '2026 年 11 月 5 日，Figma 改進了智慧體產生的向量插畫與圖示：線條用描邊而不是填色輪廓、圖層按功能分組便於修改、可掛上風格參考，結構也適合用 Figma Motion 做動畫。這對圖示系統意味著什麼、怎麼給智慧體寫提示，以及從提示到上線 SVG 的一份清單。',
     '2026年11月5日、Figmaはエージェントが生成するベクターイラストとアイコンを改善した。線は塗りつぶしではなくストローク、レイヤーは編集しやすいよう機能別にグループ化、スタイル参照を添付でき、Figma Motion向けの構造にもなる。アイコンシステムにとっての意味、エージェントへの指示の出し方、プロンプトから出荷用SVGまでのチェックリスト。',
     '2026년 11월 5일 Figma는 에이전트가 생성한 벡터 일러스트와 아이콘을 개선했다. 선은 채운 외곽선이 아니라 스트로크이고, 레이어는 편집하기 쉽게 기능별로 묶이며, 스타일 참조를 붙일 수 있고, Figma Motion용 구조도 갖춘다. 아이콘 시스템에 주는 의미, 에이전트 지시 방법, 프롬프트에서 배포 SVG까지의 체크리스트.',
     'Pada 5 November 2026 Figma menambah baik ilustrasi dan ikon vektor yang dijana ejen: kerja garisan datang sebagai strok (bukan outline terisi), lapisan dikumpulkan untuk suntingan, anda boleh lampirkan rujukan gaya, dan strukturnya sedia untuk Figma Motion. Mengapa penting untuk sistem ikon, cara memberi arahan, dan senarai semak dari prompt ke SVG.',
     'Ngày 5/11/2026 Figma cải thiện minh họa và icon vector do agent tạo: nét là stroke (không phải outline tô đặc), layer được nhóm để chỉnh sửa, có thể gắn tham chiếu phong cách, và cấu trúc sẵn sàng cho Figma Motion. Vì sao điều đó quan trọng với hệ icon, cách brief agent, và checklist từ prompt đến SVG đưa lên.',
     'Le 5 novembre 2026, Figma a amélioré les illustrations et icônes vectorielles générées par l’agent : les traits sont des strokes (pas des contours remplis), les calques sont groupés pour l’édition, on peut joindre des références de style, et la structure convient à Figma Motion. Pourquoi c’est important pour un système d’icônes, comment briefer l’agent, et une checklist du prompt au SVG livré.',
     'El 5 de noviembre de 2026 Figma mejoró las ilustraciones e iconos vectoriales generados por el agente: el trazo llega como stroke (no como contorno relleno), las capas se agrupan para editar, puedes adjuntar referencias de estilo y la estructura sirve para Figma Motion. Por qué importa para un sistema de iconos, cómo briefar al agente y una checklist del prompt al SVG publicado.',
     'Am 5. November 2026 hat Figma agentengenerierte Vektorillustrationen und Icons verbessert: Linien kommen als Strokes (nicht als gefüllte Outlines), Ebenen sind zum Editieren gruppiert, Stilreferenzen lassen sich anhängen, und die Struktur eignet sich für Figma Motion. Warum das für Icon-Systeme zählt, wie man den Agent briefed und eine Checkliste vom Prompt zum ausgelieferten SVG.'),
 en="""<p>On 5 November 2026 Figma’s release notes listed a quiet but useful change: the Figma agent now generates polished vector illustrations and icons that are easier to edit, match to a style, or animate. Four details matter for anyone who has inherited an AI icon set they could not finish: functional layer grouping, attachable style references, line work drawn as <strong>strokes instead of fills</strong>, and a layer tree clean enough for Figma Motion.</p>
<p>That is a different promise from “AI drew a nice picture”. A filled outline bakes the weight into the shape. A stroke keeps weight and end caps as settings, so you can drag them later without redrawing. Figma’s own help centre says the agent can generate illustrations and icon sets from a prompt or from reference images, with editable strokes and fills and an organised layer structure, and you can watch them appear live on the canvas.</p>
<h2>What actually changed</h2>
<ul><li><strong>Strokes for line work.</strong> Change stroke weight and end caps without redrawing the path. That is the difference between a one-off asset and a system you can still tune.</li>
<li><strong>Layers grouped by function.</strong> Independent layers that are grouped intuitively, so you can revise one part of an icon set without exploding the whole file.</li>
<li><strong>Style references.</strong> Attach your own illustrations so the agent generates more components or on-brand icons at scale, instead of inventing a new look every time.</li>
<li><strong>Motion-ready structure.</strong> The same clean tree is meant to animate in Figma Motion, by you or by the agent.</li></ul>
<p>The same week Figma also put code layers into open beta with a workflow lab (4 November) and earlier raised shader export to 4096 px and into code layers (2 November). Vectors, motion and code on one canvas are converging; this post stays on the vector side.</p>
<h2>Our take</h2>
<p>The useful unit is not “an illustration”, it is <strong>an editable line decision</strong>. Most prompt-to-image tools still hand you a raster or a flattened SVG that looks right until you need a 1.5 px hairline next to a 2 px icon. Drawing in strokes moves the decision back into the file. Keep that decision open all the way to production: export SVG with real <code>stroke</code> attributes, set <code>stroke="currentColor"</code>, hold width in a CSS custom property, and use <code>vector-effect: non-scaling-stroke</code> when the icon must keep one optical weight at every size.</p>
<p>Style references are the other half. An agent that has never seen your icon set will invent a second dialect. Attach three of your best icons, name the stroke weight and end cap in the prompt, and ask for three more in the same family before you commission a whole set. Open the layers panel before you admire the preview—generated art is only as useful as its structure.</p>
<p>We would still clean the SVG before shipping (SVGO, viewBox, aria-hidden or a title). Treat the agent like a junior illustrator who drafts in your file, not like a CDN of finished icons.</p>
<h2>Checklist: from prompt to a shipped stroke icon</h2>
<ol><li><strong>Brief the line, not the vibe.</strong> Name stroke weight, end caps (round / butt / square), corner joins, and whether fills are allowed.</li>
<li><strong>Attach style references.</strong> Two or three existing icons beat a paragraph of adjectives. Ask for a small batch first and compare strokes side by side.</li>
<li><strong>Open the layers panel.</strong> Confirm independent, sensibly grouped layers before you accept the result.</li>
<li><strong>Tune weight on the stroke.</strong> Adjust stroke weight and caps; if you have to redraw, the file is still a filled outline—reject it.</li>
<li><strong>Animate only if the tree is clean.</strong> Use Figma Motion on paths that already separate; do not animate a flattened blob.</li>
<li><strong>Export as live strokes.</strong> Keep <code>stroke</code> / <code>stroke-width</code> / <code>stroke-linecap</code> in the SVG. Outline only for logos that need a fixed silhouette.</li>
<li><strong>Tokenise on the page.</strong> One <code>--line</code> (or similar) for icons, rules and markers; <code>currentColor</code> for theme; check light and dark.</li>
<li><strong>Access and credits.</strong> Agent work uses Figma AI credits; check your plan before generating a large set.</li></ol>
<pre><code># Brief for the Figma agent (icon set)
Goal:       6 outline icons for a docs site (search, copy, link, warn, check, menu)
Style ref:  attach icons/search.svg + icons/copy.svg (our current set)
Stroke:     1.5 px, round caps, round joins, no filled outlines for line work
Grid:       24×24 viewBox, 2 px padding, optical centre
Colour:     single currentColor; no hard-coded greys
Deliver:    one frame per icon, layers grouped by path, ready for Motion if needed
Never:      drop shadows, gradients, emoji style, mismatched weights across the set
First pass: make only search / copy / link so we can compare strokes before the rest</code></pre>
<h2>How UI Hub helps</h2>
<p>For SVG workflows that start outside Figma, see <a href="../ai-svg-for-ui-ideogram-vector/">AI SVG for UI with Ideogram Vector</a>. Shaders that now travel into code layers are covered in <a href="../figma-shaders-ga-ship-shader-backgrounds/">Figma shaders GA</a>. Broader agent-on-canvas context sits in <a href="../figma-make-and-figma-agent/">Figma Make and the Figma agent</a> and <a href="../figma-code-layers-and-specs/">code layers and Specs</a>. When the destination is code you already ship, <a href="../design-on-running-code-dessn-doop-code-canvas/">design on running code</a> is the matching workflow post.</p>""",
 zh="""<p>2026 年 11 月 5 日，Figma 的更新日志写了一条看起来不大、但对做图标的人很有用的改动：智能体生成的矢量插画和图标更容易编辑、对齐风格，也更容易做动画。四个细节对「接手过一套没法改完的 AI 图标」的人都重要：按功能分组的图层、可挂上的风格参考、<strong>线条用描边而不是填色轮廓</strong>，以及干净到适合 Figma Motion 的图层树。</p>
<p>这和「AI 画了一张好看的图」不是一回事。填色轮廓把线宽烤进了形状里；描边则把线宽和端点样式留成设置，以后还能拖，不用重画。Figma 帮助中心也写明：智能体可以根据提示或参考图生成插画和图标集，带可编辑的描边与填色、条理清楚的图层，并且你可以看着它们在画布上实时长出来。</p>
<h2>到底改了什么</h2>
<ul><li><strong>线条用描边。</strong>改线宽和端点样式时不用重画路径。这是一次性素材和还能继续调的系统之间的差别。</li>
<li><strong>图层按功能分组。</strong>独立图层、分组合理，改图标集的某一部分时不必拆烂整个文件。</li>
<li><strong>风格参考。</strong>挂上你自己的插画，让智能体按同一套视觉再批量生成组件或品牌图标，而不是每次发明一种新画风。</li>
<li><strong>适合做动效的结构。</strong>同一棵干净的图层树，可以在 Figma Motion 里由你或智能体做动画。</li></ul>
<p>同一周，Figma 还用工作流实验把代码图层推进了开放测试（11 月 4 日），并更早把着色器导出提到 4096 像素、带进代码图层（11 月 2 日）。矢量、动效和代码在同一张画布上汇合；这篇只谈矢量这一侧。</p>
<h2>我们的看法</h2>
<p>真正有用的单位不是「一张插画」，而是<strong>一个还可编辑的线条决定</strong>。多数提示生成图像的工具，最后给你的是位图或已经压扁的 SVG——看着对，直到你要在 2 px 图标旁边放一根 1.5 px 的发丝线。用描边画，等于把决定留回文件里。把这个决定一直留到上线：导出带真实 <code>stroke</code> 属性的 SVG，设 <code>stroke="currentColor"</code>，线宽放进 CSS 自定义属性，需要光学线宽不随缩放变时再用 <code>vector-effect: non-scaling-stroke</code>。</p>
<p>另一半是风格参考。从没见过你图标集的智能体，会发明第二种方言。先挂上三枚最好的现有图标，在提示里写明线宽和端点，先要三枚同族新图标，再决定要不要整套。先打开图层面板，再欣赏预览——生成物的价值取决于它的结构。</p>
<p>上线前我们仍会清理 SVG（SVGO、viewBox、aria-hidden 或 title）。把智能体当成在你文件里起草的初级插画师，而不是成品图标 CDN。</p>
<h2>清单：从提示到上线的描边图标</h2>
<ol><li><strong>写清线条，而不是氛围。</strong>写明线宽、端点（圆 / 平 / 方）、转角连接、是否允许填色。</li>
<li><strong>挂上风格参考。</strong>两三枚现有图标胜过一整段形容词。先要一小批，并排对比描边。</li>
<li><strong>打开图层面板。</strong>确认图层独立、分组合理，再接受结果。</li>
<li><strong>在描边上改线宽。</strong>调 stroke weight 和 caps；若还得重画，说明文件仍是填色轮廓——退回。</li>
<li><strong>图层干净再做动画。</strong>只对已经拆开的路径用 Figma Motion，不要去动压扁的色块。</li>
<li><strong>导出成活的描边。</strong>SVG 里保留 <code>stroke</code> / <code>stroke-width</code> / <code>stroke-linecap</code>。只有需要固定剪影的 Logo 才转轮廓。</li>
<li><strong>在页面上做成 Token。</strong>图标、分隔线和标记共用一个 <code>--line</code>（或类似变量）；主题色用 <code>currentColor</code>；浅色和深色都要检查。</li>
<li><strong>权限和额度。</strong>智能体工作消耗 Figma AI 积分；大批量生成前先看清套餐。</li></ol>
<pre><code># 给 Figma 智能体的图标集说明
目标：     文档站用的 6 个线性图标（搜索、复制、链接、警告、完成、菜单）
风格参考： 挂上 icons/search.svg + icons/copy.svg（现有套件）
描边：     1.5 px，圆角端点，圆角连接，线条不用填色轮廓
网格：     24×24 viewBox，内边距 2 px，光学居中
颜色：     单一 currentColor；不写死灰色
交付：     每图标一帧，路径按图层分组，需要时可进 Motion
禁止：     投影、渐变、emoji 风、整套线宽不一致
第一轮：   只做搜索 / 复制 / 链接，对比描边后再生成其余</code></pre>
<h2>UI Hub 能帮什么</h2>
<p>从 Figma 之外起步的 SVG 流程，见 <a href="../ai-svg-for-ui-ideogram-vector/">用 Ideogram Vector 做界面 SVG</a>。已能进入代码图层的着色器，见 <a href="../figma-shaders-ga-ship-shader-backgrounds/">Figma 着色器正式可用</a>。更广的「智能体在画布上」背景，见 <a href="../figma-make-and-figma-agent/">Figma Make 与 Figma 智能体</a>以及 <a href="../figma-code-layers-and-specs/">代码图层与 Specs</a>。若最终落点是你已经在跑的代码，对应的工作流文章是<a href="../design-on-running-code-dessn-doop-code-canvas/">在运行中的代码上做设计</a>。</p>""",
 refs=[('Improvements to agent-generated vector illustrations and icons (5 Nov 2026)','Figma release notes','https://www.figma.com/release-notes/'),('Generate and edit vectors with Figma AI','Figma Learn','https://help.figma.com/hc/en-us/articles/38031452710807-Generate-and-edit-vectors-with-Figma-AI'),('Figma’s agent now draws in strokes, so the line weight stays yours','Art Direction Daily','https://artdirectiondaily.com/issues/2026-11-05-figma-agent-draws-in-strokes.html'),('AI Vector Illustrations in Figma: the agent finally draws clean','Mazette.co','https://www.mazette.co/en/blog/ai-vector-illustrations-in-figma-the-agent-finally-draws-clean'),('stroke-linecap','MDN Web Docs','https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/stroke-linecap'),('vector-effect','MDN Web Docs','https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/vector-effect'),('Workflow lab: Test ideas with code layers and the Figma agent (4 Nov 2026)','Figma Blog','https://www.figma.com/blog/workflow-lab-build-with-code-on-the-canvas-using-the-figma-agent-and-code-layers/'),('Design Tools news (RSS checked 6 Nov 2026)','designtools.fyi','https://designtools.fyi/news')]),

dict(slug='cursor-live-apps-off-localhost', date='2026-11-07', cat='tools', series=None, featured=True, tags=['Cursor','live apps','cloud agents','deployment','Postgres','SSO','security'],
 t=T('Cursor Live Apps: get the UI off localhost before the demo dies',
     'Cursor Live Apps：在演示凉掉之前，把界面拉出 localhost',
     'Cursor Live Apps：在示範涼掉之前，把介面拉出 localhost',
     'Cursor Live Apps：デモが死ぬ前にUIをlocalhostから出す',
     'Cursor Live Apps: 데모가 죽기 전에 UI를 localhost 밖으로',
     'Cursor Live Apps: keluarkan UI dari localhost sebelum demo mati',
     'Cursor Live Apps: đưa UI ra khỏi localhost trước khi demo chết',
     'Cursor Live Apps : sortez l’UI de localhost avant que la démo meure',
     'Cursor Live Apps: saca la UI de localhost antes de que muera la demo',
     'Cursor Live Apps: UI vor dem Demo-Tod von localhost holen'),
 s=T('On 5 November 2026 Cursor let cloud agents scaffold, host, and publish a live app with Postgres, SSO, and security checks. Why that changes the design loop, how it compares to Lovable and v0, and a checklist before you hit publish.',
     '2026 年 11 月 5 日，Cursor 让云端智能体搭脚手架、托管并发布带 Postgres、SSO 与安全检查的线上应用。这为什么改了设计循环、怎么和 Lovable、v0 比，以及点发布前的一份清单。',
     '2026 年 11 月 5 日，Cursor 讓雲端智慧體搭腳手架、託管並發布帶 Postgres、SSO 與安全檢查的線上應用。這為什麼改了設計循環、怎麼和 Lovable、v0 比，以及點發布前的一份清單。',
     '2026年11月5日、Cursorはクラウドエージェントにスキャフォールド・ホスティング・公開まで任せ、Postgres・SSO・セキュリティ検査付きのライブアプリを出せるようにした。デザインループへの影響、Lovableやv0との比較、公開前チェックリスト。',
     '2026년 11월 5일 Cursor는 클라우드 에이전트가 Postgres·SSO·보안 검사와 함께 라이브 앱을 스캐폴드·호스팅·게시하게 했다. 디자인 루프가 바뀌는 이유, Lovable·v0 비교, 게시 전 체크리스트.',
     'Pada 5 November 2026 Cursor benarkan ejen awan scaffold, hos dan terbitkan apl langsung dengan Postgres, SSO dan semakan keselamatan. Mengapa gelung reka bentuk berubah, banding dengan Lovable dan v0, serta senarai semak sebelum terbit.',
     'Ngày 5/11/2026 Cursor cho phép cloud agent dựng scaffold, host và publish app sống kèm Postgres, SSO và kiểm tra bảo mật. Vì sao vòng thiết kế đổi, so với Lovable và v0, và checklist trước khi bấm publish.',
     'Le 5 novembre 2026, Cursor a laissé les agents cloud scaffolder, héberger et publier une app live avec Postgres, SSO et contrôles de sécurité. Pourquoi la boucle de design change, comparaison avec Lovable et v0, checklist avant de publier.',
     'El 5 de noviembre de 2026 Cursor permitió que agentes en la nube andamien, alojen y publiquen una app en vivo con Postgres, SSO y comprobaciones de seguridad. Por qué cambia el bucle de diseño, comparación con Lovable y v0, y checklist antes de publicar.',
     'Am 5. November 2026 ließ Cursor Cloud-Agenten eine Live-App mit Postgres, SSO und Security-Checks scaffolden, hosten und veröffentlichen. Warum sich die Design-Schleife ändert, Vergleich mit Lovable und v0, Checkliste vor dem Publish.'),
 en="""<p>On 5 November 2026 Cursor’s changelog shipped <strong>Build Live Apps</strong>: tell a cloud agent you want an app, and it scaffolds the web app, spins up Postgres when needed, puts authentication behind Cursor SSO, provisions hosting, and hands you a shareable URL after you pick a domain. The company’s own framing is blunt—agents made writing code cheap, but most apps still die on localhost. The day after, on 6 November, Cursor also shipped Voice Chat with Agents (Grok Voice) so you can talk through a change while work is running; useful as a design-loop companion, not the main story here.</p>
<p>Coverage from The New Stack (Paul Sawers, 6 November) places the release next to Lovable and Replit’s prompt-to-app turf, and notes Vercel’s public reply that the hosting path sits on <strong>Vercel for Platforms</strong>—deploy without each teammate opening their own Vercel account or wiring deploy config by hand. Availability is on paid plans with cloud agents enabled. That is the product. The design problem underneath is older: demos that only run on one laptop are not products.</p>
<h2>What shipped, and how it works</h2>
<ul><li><strong>Cloud agent, not a localhost wizard.</strong> You kick off a cloud agent and say you want an app; Cursor scaffolds, optionally provisions Postgres, configures auth behind Cursor SSO, and hosts it.</li>
<li><strong>Secrets on demand.</strong> If the app must talk to your systems (for example a warehouse), Cursor asks for the secrets it needs instead of inventing them.</li>
<li><strong>Security checks before go-live.</strong> On publish, deterministic and agentic checks look for common failures such as secrets in app files. Failures block the ship until the agent can fix them and you explicitly publish.</li>
<li><strong>Share scope is a product decision.</strong> After checks pass you get the live URL; share with people, groups, or the whole team behind Cursor sign-in. On individual plans you can also share publicly. Team admins can see apps and secrets, add review rules, approve blocked publishes, and unpublish.</li>
<li><strong>Repos and git.</strong> Apps can come from new or existing repos on Cursor Origin and GitHub; other providers such as GitLab are listed as coming soon. Cursor also notes you can provision an API key so a script or Grok Bot can call the app.</li></ul>
<p>Cursor’s own examples lean internal: ops tools, customer multimedia decks, onboarding, sales dashboards, engineering-service portals. That is a clue. Live Apps are strongest when “share with the team behind SSO” is the point, not when you need a public brand site with a long design history.</p>
<h2>Our take: treat Live Apps like an internal product surface</h2>
<p>The design problem moved from <strong>“generate a screen”</strong> to <strong>“what ships past localhost”</strong>. A pretty preview that only you can open is still a localhost demo with better lighting. Live Apps collapse scaffold → host → auth → share into one publish path; that is useful, and it is also where taste and security both get decided by default if you do not decide first.</p>
<p>Lock tokens and components <em>before</em> the agent scaffolds. A cloud agent that has never seen your Button, radius, or type scale will invent a second UI dialect the moment Postgres comes up. Put a short design file (tokens, one accent, density, never-list) in the repo the agent reads, the same way you would for any coding agent. Decide auth and share scope <em>before</em> you hit publish: team-only behind SSO is a different product from a public link on an individual plan. Treat the security checks as a gate, not a vibe—The New Stack reminds readers that Semafor previously reported Replit employees finding sensitive exposure in a sample of Lovable-built apps, after which Lovable said it added further pre-publish checks. Cursor’s checks are addressing that class of failure; they are not a substitute for reviewing what the app can actually reach.</p>
<p>Know when adjacent tools still fit better. <strong>v0</strong> stays the component-oriented path: prompt into shadcn/Tailwind you pull into an existing repo, with Design mode and design-system hooks when the deliverable is UI inside code you already ship (see v0’s docs). <strong>Lovable</strong> remains a dedicated prompt-to-app surface with its own changelog cadence—recent entries such as GPT Image models for in-app AI features (6 November) and “Dreaming” memory tidy-ups (4 November) show it is still iterating as a full product builder, not a side feature of an IDE. Replit-style environments still win when the whole collaborative runtime is the product. Live Apps win when your team already lives in Cursor and the app’s natural home is “behind our SSO, shareable tomorrow”.</p>
<h2>Checklist before you hit publish</h2>
<ol><li><strong>Write the surface brief first.</strong> Audience (team / group / public), one job the app does, and a never-list for UI chrome.</li>
<li><strong>Lock tokens and components in the repo.</strong> Radius, type, accent, your Button/Card—before the scaffold, not after the first share link.</li>
<li><strong>Name the data boundary.</strong> Which secrets, which warehouse tables, which environments. Do not paste production keys into a chat because the agent asked politely.</li>
<li><strong>Choose share scope on purpose.</strong> SSO teammates vs public. Individual-plan public links are a different threat model from internal ops tools.</li>
<li><strong>Read every failed security check.</strong> Fix or accept with admin override only after a human understands the finding. Do not treat “agent said it fixed it” as a merge.</li>
<li><strong>Click the live URL like a stranger.</strong> Empty, loading, error, mobile width, and sign-out. Localhost habits hide all four.</li>
<li><strong>Decide ownership.</strong> Who can unpublish, who rotates secrets, which admin sees the app list—before the third teammate bookmarks it.</li>
<li><strong>Pick the right tool if Live Apps are wrong.</strong> Components for an existing React app → v0. Open-ended public product with Lovable’s own stack → Lovable. Cursor-native internal tool with SSO → Live Apps.</li></ol>
<pre><code># Live Apps publish brief (paste into the cloud agent first)
Surface:   internal ops tool for desk seating + event registration
Audience:  whole team behind Cursor SSO (not public)
Stack:     reuse our Button/Card; tokens in styles/tokens.css
Data:      read-only seat map from warehouse; ask before any write secret
Auth:      Cursor SSO only; no anonymous link
Never:     hard-coded API keys, second accent colour, emoji icons
Gate:      stop on any security-check failure; I review before Publish
Companion: Voice Chat OK for iteration talk-track; publish stays a click I make</code></pre>
<h2>When not to use Live Apps</h2>
<p>Skip them when the deliverable must merge into a mature design system with PR review as the only ship path—v0 or a hand PR still fit better. Skip them when you need Lovable’s (or Replit’s) full product surface and you are not standardising on Cursor. Skip them for customer-facing marketing sites that need brand art direction the agent has never seen. Use them when the pain is real: a useful internal UI that would otherwise die on someone’s laptop between the standup and the demo.</p>
<p>Related on UI Hub: <a href="../lovable-bolt-prompt-to-app/">Lovable and Bolt</a>, <a href="../v0-prompt-to-shadcn/">v0 to shadcn</a>, <a href="../prompt-to-ui-tools-compared/">prompt-to-UI tools compared</a>, and <a href="../annotate-dont-describe-visual-prompts/">annotate, don’t describe</a> for iterating on a running preview.</p>""",
 zh="""<p>2026 年 11 月 5 日，Cursor 的更新日志上线了 <strong>Build Live Apps</strong>：对云端智能体说你要做一个应用，它会搭好 Web 应用脚手架，需要时拉起 Postgres，把登录放在 Cursor SSO 后面，配好托管，你选好域名后拿到可分享的链接。官方说法很直白——智能体让写代码变便宜了，但多数应用还是死在 localhost。次日（11 月 6 日）Cursor 还上了 Voice Chat with Agents（Grok Voice），可以边跑任务边语音沟通；适合当设计循环的伴奏，不是这篇的主线。</p>
<p>The New Stack（Paul Sawers，11 月 6 日）把这次发布放在 Lovable、Replit 的「提示生成应用」赛道旁边，并提到 Vercel 在 X 上的公开回复：托管路径建在 <strong>Vercel for Platforms</strong> 上——团队成员不必各自开 Vercel 账号、也不必手写部署配置。功能面向已开启云端智能体的付费方案。产品是这样；底下的设计问题更老：只能在一台笔记本上跑的演示，还不是产品。</p>
<h2>上了什么、怎么跑</h2>
<ul><li><strong>云端智能体，不是本机向导。</strong>发起云端智能体并明确说要做应用；Cursor 搭脚手架，按需开 Postgres，配置 Cursor SSO 登录并托管。</li>
<li><strong>按需要密钥。</strong>若应用要连你的系统（例如数仓），Cursor 会向你要所需密钥，而不是自己编造。</li>
<li><strong>上线前的安全检查。</strong>发布时跑确定式与智能体安全检查，抓应用文件里写死密钥等常见问题；不过检就不能上线，修完且由你明确点发布才行。</li>
<li><strong>分享范围是产品决策。</strong>过检后拿到线上 URL；可分享给特定人、群组或整个团队，都在 Cursor 登录之后。个人方案也可公开分享。团队管理员能看到应用与密钥、加审查规则、批准被拦的发布、下线应用。</li>
<li><strong>仓库与 Git。</strong>可从 Cursor Origin 与 GitHub 上的新仓或已有仓部署；GitLab 等写明即将支持。也可开通 API key，让脚本或 Grok Bot 调用应用。</li></ul>
<p>Cursor 自己举的例子偏内部：运营工具、客户多媒体演示、入职培训、销售看板、工程服务门户。这是信号：Live Apps 最强的场景是「挂在团队 SSO 后面分享」，而不是要做有长久设计史的对外品牌站。</p>
<h2>我们的看法：把 Live Apps 当成内部产品界面</h2>
<p>设计问题已经从<strong>「生成一屏」</strong>变成<strong>「什么能活过 localhost」</strong>。只有你能打开的漂亮预览，不过是灯光更好的本机演示。Live Apps 把脚手架 → 托管 → 登录 → 分享压成一条发布路径；有用，但也意味着你不先决定，审美和安全都会被默认值替你决定。</p>
<p>在智能体搭脚手架<strong>之前</strong>锁死 Token 和组件。从没见过你的 Button、圆角、字号阶梯的云端智能体，一接到 Postgres 就会发明第二种界面方言。把简短的设计文件（Token、一个强调色、密度、禁止清单）放进智能体会读的仓库，和对待任何编程智能体一样。在点发布<strong>之前</strong>决定登录与分享范围：SSO 仅限团队，和个人方案上的公开链接，是两种产品。把安全检查当关卡，不当氛围——The New Stack 提醒读者：Semafor 曾报道 Replit 员工在一批 Lovable 应用样本里发现敏感信息暴露，此后 Lovable 称增加了发布前检查。Cursor 的检查对准的是这类问题；它不能代替你审应用到底能碰到什么。</p>
<p>也要知道相邻工具何时更合适。<strong>v0</strong> 仍是组件导向路径：提示生成可拉进现有仓库的 shadcn/Tailwind，并有 Design mode 与设计系统挂钩——交付物是已有代码里的界面时看 v0 文档。<strong>Lovable</strong> 仍是独立的提示生成应用产品，更新日志节奏自己的——例如 11 月 6 日为应用内 AI 功能接入 GPT Image 模型、11 月 4 日的「Dreaming」记忆整理，说明它还在当完整产品构建器迭代，而不是 IDE 的附属功能。整机协作运行时才是产品时，Replit 一类环境仍更合适。团队已经住在 Cursor、应用天生该「挂在我们的 SSO 后面、明天就能分享」时，Live Apps 才对。</p>
<h2>点发布前的清单</h2>
<ol><li><strong>先写界面简报。</strong>受众（团队 / 群组 / 公开）、应用只办一件什么事、界面 chrome 的禁止清单。</li>
<li><strong>在仓库里锁 Token 和组件。</strong>圆角、字体、强调色、你的 Button/Card——在搭脚手架之前，而不是出了分享链接之后。</li>
<li><strong>写清数据边界。</strong>哪些密钥、哪些数仓表、哪些环境。不要因为智能体礼貌地要，就把生产密钥贴进对话。</li>
<li><strong>有意选择分享范围。</strong>SSO 队友 vs 公开。个人方案公开链接，和内部运营工具，威胁模型不同。</li>
<li><strong>读完每一条失败的安全检查。</strong>只有人看懂发现后，才修复或走管理员覆盖。「智能体说修好了」不等于合并。</li>
<li><strong>像陌生人一样点开线上 URL。</strong>空态、加载、出错、窄屏、退出登录。localhost 习惯会把这四项都藏起来。</li>
<li><strong>定好所有权。</strong>谁能下线、谁轮换密钥、哪个管理员看应用列表——在第三个同事收藏链接之前。</li>
<li><strong>Live Apps 不合适就换工具。</strong>已有 React 应用里的组件 → v0；开放的对外产品且跟 Lovable 栈 → Lovable；Cursor 原生、要 SSO 的内部工具 → Live Apps。</li></ol>
<pre><code># Live Apps 发布简报（先贴进云端智能体）
界面：     工位与活动报名用的内部运营工具
受众：     整个团队，Cursor SSO 之后（不公开）
技术栈：   复用我们的 Button/Card；Token 在 styles/tokens.css
数据：     只读座位图来自数仓；任何写入密钥先问我
登录：     仅 Cursor SSO；不要匿名链接
禁止：     写死 API key、第二个强调色、emoji 图标
关卡：     安全检查失败就停；我审过再点 Publish
伴奏：     迭代讨论可用 Voice Chat；发布必须是我点的那一下</code></pre>
<h2>什么时候别用 Live Apps</h2>
<p>交付物必须合进成熟设计系统、且唯一上线路径是 PR 审查时，跳过——v0 或手写 PR 更合适。你需要 Lovable（或 Replit）的完整产品界面、又不以 Cursor 为标准时，跳过。要做智能体从未见过品牌美术方向的对外营销站时，跳过。真正痛的时候再用：一个本来有用的内部界面，若不去掉 localhost，会在站会和演示之间死在某台笔记本上。</p>
<p>UI Hub 相关阅读：<a href="../lovable-bolt-prompt-to-app/">Lovable 与 Bolt</a>、<a href="../v0-prompt-to-shadcn/">v0 到 shadcn</a>、<a href="../prompt-to-ui-tools-compared/">提示生成界面工具对比</a>，以及在运行中的预览上迭代的<a href="../annotate-dont-describe-visual-prompts/">标注，而不是描述</a>。</p>""",
 refs=[('Build Live Apps in Cursor (5 Nov 2026)','Cursor Changelog','https://cursor.com/changelog/build-live-apps'),('Voice Chat with Agents (6 Nov 2026)','Cursor Changelog','https://cursor.com/changelog'),('"Most apps never make it off localhost": Cursor takes on Lovable and Replit with fully managed app deployment','Paul Sawers / The New Stack','https://thenewstack.io/cursor-ai-app-deployment/'),('Lovable changelog','Lovable','https://docs.lovable.dev/changelog'),('What is v0?','v0 by Vercel','https://v0.app/docs'),('v0 by Vercel','Vercel','https://v0.app/')]),

dict(slug='twombly-shared-canvas-team-comments', date='2026-11-08', cat='tools', series=None, featured=True, tags=['Twombly','canvas','agents','collaboration','comments'],
 t=T('Twombly: pin comments on the agent’s frames so it iterates on the team’s feedback',
     'Twombly：把批注钉在智能体的画框上，让它按团队的反馈迭代',
     'Twombly：把批註釘在智慧體的畫框上，讓它按團隊的回饋迭代',
     'Twombly：エージェントのフレームにコメントをピンし、チームのフィードバックで次の案を出す',
     'Twombly: 에이전트 프레임에 댓글을 고정해 팀 피드백으로 다음 안을 만든다',
     'Twombly: semat komen pada bingkai ejen supaya ia mengulang berdasarkan maklum balas pasukan',
     'Twombly: ghim bình luận lên khung của agent để nó lặp theo phản hồi của cả nhóm',
     'Twombly : épinglez des commentaires sur les cadres de l’agent pour qu’il itère sur les retours de l’équipe',
     'Twombly: fija comentarios en los marcos del agente para que itere con el feedback del equipo',
     'Twombly: Kommentare an die Agent-Frames heften, damit die nächste Runde dem Team folgt'),
 s=T('On 7 November 2026 Jaytel showed Twombly on Hacker News: a localhost canvas where coding agents place each design version as a live frame, and a Share link adds live cursors, comments and voice huddles the agent can read. How that differs from Dessn, Doop and Cursor Live Apps, plus a checklist before you share.',
     '2026 年 11 月 7 日，Jaytel 在 Hacker News 展示了 Twombly：智能体把每个设计版本放成本机画布上的实时画框，点 Share 后团队可以用实时光标、批注和语音围聊，智能体也能读到这些反馈。它和 Dessn、Doop、Cursor Live Apps 有何不同，以及分享前的清单。',
     '2026 年 11 月 7 日，Jaytel 在 Hacker News 展示了 Twombly：智慧體把每個設計版本放成本機畫布上的即時畫框，點 Share 後團隊可以用即時光標、批註和語音圍聊，智慧體也能讀到這些回饋。它和 Dessn、Doop、Cursor Live Apps 有何不同，以及分享前的清單。',
     '2026年11月7日、JaytelはHacker NewsでTwomblyを紹介した。コーディングエージェントが各デザイン案をローカルホストのキャンバス上のライブフレームとして置き、Shareするとチームはライブカーソル・コメント・ボイスハドルを使え、エージェントもそれを読める。Dessn、Doop、Cursor Live Appsとの違いと、共有前のチェックリスト。',
     '2026년 11월 7일 Jaytel이 해커뉴스에 Twombly를 올렸다. 코딩 에이전트가 각 디자인 버전을 로컬호스트 캔버스의 라이브 프레임으로 올리고, Share 링크는 실시간 커서·댓글·보이스 허들을 더하며 에이전트도 이를 읽는다. Dessn·Doop·Cursor Live Apps와의 차이와 공유 전 체크리스트.',
     'Pada 7 November 2026 Jaytel mempamerkan Twombly di Hacker News: kanvas localhost di mana ejen pengekodan meletakkan setiap versi reka bentuk sebagai bingkai langsung, dan pautan Share menambah kursor langsung, komen dan huddle suara yang boleh dibaca ejen. Bezanya dengan Dessn, Doop dan Cursor Live Apps, serta senarai semak sebelum anda kongsi.',
     'Ngày 7/11/2026 Jaytel giới thiệu Twombly trên Hacker News: canvas localhost để coding agent đặt mỗi phiên bản thiết kế thành khung sống, và liên kết Share thêm con trỏ trực tiếp, bình luận cùng voice huddle mà agent có thể đọc. Khác gì Dessn, Doop và Cursor Live Apps, cùng checklist trước khi chia sẻ.',
     'Le 7 novembre 2026, Jaytel a présenté Twombly sur Hacker News : un canvas en localhost où l’agent de code pose chaque version comme un cadre vivant ; un lien Share ajoute curseurs, commentaires et huddles vocaux que l’agent peut lire. Différences avec Dessn, Doop et Cursor Live Apps, et une checklist avant de partager.',
     'El 7 de noviembre de 2026 Jaytel mostró Twombly en Hacker News: un lienzo en localhost donde el agente de código coloca cada versión como un marco en vivo, y un enlace Share añade cursores, comentarios y huddles de voz que el agente puede leer. Cómo se diferencia de Dessn, Doop y Cursor Live Apps, y una lista antes de compartir.',
     'Am 7. November 2026 zeigte Jaytel Twombly auf Hacker News: ein Localhost-Canvas, auf dem Coding-Agenten jede Designversion als Live-Frame ablegen; der Share-Link ergänzt Live-Cursor, Kommentare und Voice-Huddles, die der Agent lesen kann. Unterschiede zu Dessn, Doop und Cursor Live Apps sowie eine Checkliste vor dem Teilen.'),
 en="""<p>On 7 November 2026, software designer Jaytel posted a Show HN for <strong>Twombly</strong>: give your coding agent a skill, and it places each design version on one infinite canvas as a live frame. Click Share and the team gets a single link with live cursors, following, comments pinned to frames, and voice huddles. The loop he stressed is what happens next: the agent can read those comments and see which frame someone is looking at, so the next pass is steered by the team’s feedback, not only by the person who typed the prompt.</p>
<p>The npm package <code>twombly</code>, published by Materic, Inc. on 5 November and updated through version 0.4.12 on 7 November, matches that description. It works with Claude Code, Codex, Cursor, and any agent that can run a command, in any framework and any repo. You can install the skill with <code>npx skills add materic-inc/twombly-skill -g -y</code>, or run <code>npx -y twombly@latest guide</code> and hand the guide to the agent. The homepage, the project’s <code>llms.txt</code>, and the skill repository on GitHub all tell the same story. The interesting design claim is smaller than “another AI canvas”: explorations become addressable frames a group can stand around.</p>
<h2>What a frame is, and what stays local</h2>
<ul><li><strong>A frame is a folder of static files</strong> that should run with no server and no network: a Vite, Next.js, SvelteKit or Astro build, one component bundled with mock data, a frozen capture of a running page, or a picture.</li>
<li><strong>Nothing goes online until a person clicks Share.</strong> The canvas opens on localhost. Twombly’s own docs say the agent never shares unless asked.</li>
<li><strong>Gates check every frame</strong> for secrets, outside requests and server code, locally and again in the cloud, before it is placed.</li>
<li><strong>The agent has two machine-readable signals:</strong> <code>twombly context</code> returns what the person is looking at; <code>twombly comments</code> returns the feedback left on the frames. Output is JSON.</li>
<li><strong>Several agents can share one canvas</strong>, and a folder can hold any number of named canvases. Typical commands include <code>twombly init --name "Notification Explorations"</code> and <code>twombly add ./dist --title "V1" --width 1280 --height 800</code>.</li></ul>
<p>Sharing has a clearer privacy story than most prototype tools bother to write down. Twombly’s privacy page (updated 7 November) says an unshared canvas stays on your computer; once you share, anyone with the link can see the canvas, its comments and who is present, and can join the huddle. Links are hard to guess and search engines are asked not to index them, but they are not private. Huddle audio passes through the host and is not recorded or stored. Materic says it does not use canvases to train AI models. Account data for shared work comes from Google sign-in (name, email, picture and account ID).</p>
<h2>Our take: this is annotate-don’t-describe, made multiplayer</h2>
<p>A week of canvas news has been circling the same problem. <a href="../design-on-running-code-dessn-doop-code-canvas/">Dessn, Doop and Figma code layers</a> let people and agents design on something that actually runs. <a href="../cursor-live-apps-off-localhost/">Cursor Live Apps</a> take a different cut: get a useful internal UI off localhost and behind SSO. Twombly is neither a production runtime nor a hosted app. It is a review surface for versions. That is the gap many agent workflows still leave as a chat scroll—“try it again, but tighter”—with no one else able to point at the frame they mean.</p>
<p>The move that matters is making each exploration <em>addressable</em>. A comment pinned to “V2 — denser table” is a different artifact from a paragraph in a prompt. Combined with <code>twombly context</code>, the agent can see which frame a teammate is looking at. That is the same instinct as <a href="../annotate-dont-describe-visual-prompts/">annotate, don’t describe</a>, except the note lives where the whole team can add it, and the agent is expected to read it back.</p>
<p>Treat the frames as what they are. They are static folders—builds, captures, pictures—not your connected app. They are good for comparing layout, type, density and empty states; they are a weak place to judge auth, live data or anything that needs a server. Dessn (or a Figma code layer wired to the repo) is still the better canvas once you have picked a direction and need the real components. Cursor Live Apps are still the better path when the pain is “this demo dies on my laptop.” Twombly is for the messy middle: several directions on the table, several people talking, one agent that should hear all of them.</p>
<p>Two caveats follow from the docs themselves. First, a shared link is public to anyone who receives it; do not put customer data, unreleased work you would not email, or anything the gates might miss, on a frame you then Share. Second, the product is days old—the package appeared on 5 November—so command names and defaults may move. Read <code>twombly help</code> on the version you installed rather than memorising a blog post.</p>
<h2>Checklist before you share a canvas</h2>
<ol><li><strong>Name the canvas after the question.</strong> “Notification density” beats “Explorations”.</li>
<li><strong>Init on localhost first.</strong> Install the skill, run the guide, and do not click Share until you have looked at every frame yourself.</li>
<li><strong>Add frames from real builds with mock data.</strong> Include empty, loading, error and a long string—not only the happy-path screenshot.</li>
<li><strong>Title frames as directions, not as winners.</strong> “V1 dense table / V2 editorial cards,” never “Final”.</li>
<li><strong>Keep tokens and components in the repo the agent builds from.</strong> A pretty frame that invents a second accent is not an option; it is drift.</li>
<li><strong>Read the gate results.</strong> Secrets, outside requests and server code should fail closed. If something slips through, do not share.</li>
<li><strong>Treat the Share link as public.</strong> Anyone with it can see comments, presence and the huddle. Send it the way you would send a prototype link you are willing to forward.</li>
<li><strong>Comment on the frame you mean, with something checkable.</strong> “Tighten the header 8px and drop the second accent” beats “make it cleaner.”</li>
<li><strong>Have the agent read before it rebuilds.</strong> Run <code>twombly context</code> then <code>twombly comments</code>, then one change set—not a fresh prompt that ignores the board.</li>
<li><strong>When you pick a direction, leave the exploration canvas.</strong> Take the winner into the real repo, a code-backed canvas, or a pull request. Twombly is not the source of truth.</li></ol>
<pre><code># Paste this to your coding agent (after the skill is installed)
Put this project's main screens on a Twombly canvas named "Notification density".
Add three frames from a static build with mock data:
  V1 dense table — our current tokens, 8px density
  V2 editorial cards — same tokens, more whitespace
  V3 split inbox — list + preview, empty + error states included
Do not click Share. Do not invent a second accent or a new typeface.
After I (or the team) comment, run `twombly context` and `twombly comments`
and change only what those notes ask for. Rebuild the same frame titles.
When we pick a winner, stop exploring and open a PR in this repo.</code></pre>
<h2>When Twombly is the wrong surface</h2>
<p>Skip it when you already know the direction and need to edit the running product—use a code-backed canvas or a pull request. Skip it when the deliverable is a hosted internal tool behind SSO: that is Live Apps territory. Skip it when the only reviewer is you and a screenshot thread would do. Use it when several people need to stand around several live versions, and the agent should iterate on what they marked, not on a recap you typed from memory.</p>
<p>Related on UI Hub: <a href="../design-on-running-code-dessn-doop-code-canvas/">design on running code</a>, <a href="../cursor-live-apps-off-localhost/">Cursor Live Apps</a>, <a href="../annotate-dont-describe-visual-prompts/">annotate, don’t describe</a>, and <a href="../claude-cursor-design-skills/">design skills for Claude and Cursor</a>.</p>""",
 zh="""<p>2026 年 11 月 7 日，软件设计师 Jaytel 在 Hacker News 上发了一条 Show HN，介绍 <strong>Twombly</strong>：给你的编程智能体装上对应 skill，它就会把每个设计版本放进同一张无限画布，成为一个实时画框。点 Share，团队拿到一条链接，带实时光标、跟随、钉在画框上的批注，以及语音围聊。他强调的循环是接下来那一步：智能体可以读这些批注，也能看到有人正在看哪一框，于是下一轮由团队的反馈来开，而不只听那个敲提示词的人。</p>
<p>Materic, Inc. 在 11 月 5 日发布的 npm 包 <code>twombly</code>（到 11 月 7 日已更新至 0.4.12）和这套说法对得上。它适用于 Claude Code、Codex、Cursor，以及任何能跑命令的智能体，不限框架和仓库。安装方式是 <code>npx skills add materic-inc/twombly-skill -g -y</code>，或者自己跑 <code>npx -y twombly@latest guide</code> 再把指南交给智能体。官网、项目的 <code>llms.txt</code> 和 GitHub 上的 skill 仓库讲的是同一件事。真正有设计含量的主张，比「又一块 AI 画布」小得多：探索变成一组成员能围着看的、可寻址的画框。</p>
<h2>画框是什么，以及什么留在本机</h2>
<ul><li><strong>一个画框就是一夹静态文件</strong>，应当不靠服务器、也不联网就能跑：Vite、Next.js、SvelteKit 或 Astro 的构建产物，带模拟数据的单个组件，对正在运行页面的冻结抓取，或者一张图。</li>
<li><strong>在有人点 Share 之前，什么都不会上网。</strong>画布开在 localhost。Twombly 自己的文档写明：除非被要求，智能体不会去分享。</li>
<li><strong>关卡会检查每个画框</strong>：密钥、对外请求和服务器代码，先在本地查一遍，上云再查一遍，通过后才会放上去。</li>
<li><strong>智能体有两个可机读信号：</strong><code>twombly context</code> 返回此人正在看什么；<code>twombly comments</code> 返回钉在画框上的反馈。输出是 JSON。</li>
<li><strong>多个智能体可以共用一块画布</strong>，一个文件夹里也可以放任意多个命名画布。常见命令包括 <code>twombly init --name "Notification Explorations"</code> 和 <code>twombly add ./dist --title "V1" --width 1280 --height 800</code>。</li></ul>
<p>它对分享隐私的说明，比多数原型工具愿意写下来的更清楚。Twombly 的隐私页（11 月 7 日更新）写着：未分享的画布留在你的电脑上；一旦分享，任何拿到链接的人都能看到画布、批注和在场的人，也能加入围聊。链接不好猜，他们也请求搜索引擎不要收录，但链接本身并不是私密的。围聊音频经过托管方传递，不录音、不存储。Materic 称不会用画布内容训练 AI 模型。分享所需的账户信息来自 Google 登录（姓名、邮箱、头像和账户 ID）。</p>
<h2>我们的看法：这是「标注，而不是描述」的多人版</h2>
<p>这一周的画布新闻其实围着同一个问题转。<a href="../design-on-running-code-dessn-doop-code-canvas/">Dessn、Doop 和 Figma 代码图层</a>让人和智能体在真正能跑的东西上设计。<a href="../cursor-live-apps-off-localhost/">Cursor Live Apps</a> 切的是另一刀：把有用的内部界面拉出 localhost，挂到 SSO 后面。Twombly 既不是生产运行时，也不是托管应用。它是版本的审阅面。许多智能体工作流至今仍把这块留成一段聊天记录——「再试一次，紧一点」——别人无法指着他们说的那一框。</p>
<p>真正重要的动作，是让每一次探索都<strong>可寻址</strong>。钉在「V2 — 更密的表格」上的一条批注，和提示词里的一段话，不是同一种工件。再加上 <code>twombly context</code>，智能体能看到同事正在看哪一框。这和<a href="../annotate-dont-describe-visual-prompts/">标注，而不是描述</a>是同一直觉，只不过批注活在整个团队都能加的地方，并且智能体被要求读回去。</p>
<p>把画框当成它本来的样子。它们是静态文件夹——构建产物、抓取、图片——不是你连着后端的应用。用来比较布局、字体、密度和空状态很合适；用来判断登录、实时数据或任何需要服务器的东西就弱。一旦选定方向、需要真实组件，Dessn（或接到仓库的 Figma 代码图层）仍是更好的画布。痛点是「演示会死在我笔记本上」时，Cursor Live Apps 仍更合适。Twombly 适合中间那段乱：桌上有好几个方向，好几个人在说话，一个智能体应当听见所有人。</p>
<p>文档本身也带出两条提醒。第一，分享链接对任何收到它的人是公开的；客户数据、你不会发邮件的未发布稿，以及关卡可能漏掉的东西，都不要放上再点 Share。第二，这个产品才几天——包裹 11 月 5 日才出现——命令名和默认值都可能变。以你安装的那个版本的 <code>twombly help</code> 为准，不要背一篇博客。</p>
<h2>点分享前的清单</h2>
<ol><li><strong>用问题给画布起名。</strong>「通知密度」比「探索」好。</li>
<li><strong>先在 localhost 初始化。</strong>装 skill、跑指南，自己看完每一框再点 Share。</li>
<li><strong>用带模拟数据的真实构建来加画框。</strong>带上空态、加载、出错和一条很长的文案，不要只有快乐路径截图。</li>
<li><strong>把画框标成方向，而不是胜者。</strong>「V1 密表格 / V2 编辑风卡片」，不要写「Final」。</li>
<li><strong>Token 和组件留在智能体构建所用的仓库里。</strong>漂亮但是发明了第二种强调色的画框，不是选项，是跑偏。</li>
<li><strong>读关卡结果。</strong>密钥、对外请求和服务器代码应当直接拦下。有漏网的就不要分享。</li>
<li><strong>把 Share 链接当成公开的。</strong>任何拿到它的人都能看到批注、在场情况和围聊。发送方式，要像你愿意被转发的原型链接一样。</li>
<li><strong>批注钉在你指的那一框上，而且要能核对。</strong>「页头收紧 8px，去掉第二种强调色」比「做干净一点」有用。</li>
<li><strong>让智能体先读再改。</strong>先跑 <code>twombly context</code> 再跑 <code>twombly comments</code>，然后做一组改动——不要另开一段无视画板的新提示。</li>
<li><strong>选定方向后，离开这块探索画布。</strong>把赢家带回真实仓库、代码支撑的画布，或开一个 PR。Twombly 不是事实来源。</li></ol>
<pre><code># 技能装好后，把这段贴给你的编程智能体
把本项目的主界面放到名为「通知密度」的 Twombly 画布上。
用带模拟数据的静态构建加三个画框：
  V1 密表格 — 用我们现有 Token，8px 密度
  V2 编辑风卡片 — 同一套 Token，留白更多
  V3 分栏收件箱 — 列表 + 预览，包含空态和错误态
不要点 Share。不要发明第二种强调色或新字体。
等我（或团队）批注之后，运行 `twombly context` 和 `twombly comments`，
只改这些笔记要求的内容。重建时沿用原来的画框标题。
我们选定赢家后，停止探索，在本仓库开一个 PR。</code></pre>
<h2>什么时候 Twombly 不是合适的界面</h2>
<p>方向已经清楚、需要改正在运行的产品时，跳过——用代码支撑的画布或 pull request。交付物是挂在 SSO 后面的内部托管工具时，跳过——那是 Live Apps 的地盘。审阅者只有你、截图线程就够用时，也跳过。适合用它的时候是：好几个人需要围着好几个实时版本看，而智能体应当按他们标出来的东西迭代，而不是按你凭记忆重述的一句话。</p>
<p>UI Hub 相关阅读：<a href="../design-on-running-code-dessn-doop-code-canvas/">在运行中的代码上设计</a>、<a href="../cursor-live-apps-off-localhost/">Cursor Live Apps</a>、<a href="../annotate-dont-describe-visual-prompts/">标注，而不是描述</a>，以及<a href="../claude-cursor-design-skills/">给 Claude 和 Cursor 的设计技能</a>。</p>""",
 refs=[('Twombly: a canvas for your agent’s explorations','Twombly','https://twombly.app/'),('Twombly llms.txt','Twombly','https://twombly.app/llms.txt'),('Privacy (updated 7 November 2026)','Twombly / Materic, Inc.','https://twombly.app/privacy'),('twombly on npm','Materic, Inc.','https://www.npmjs.com/package/twombly'),('materic-inc/twombly-skill','GitHub','https://github.com/materic-inc/twombly-skill'),('Show HN: Twombly – A collaborative canvas for your agent’s design explorations','Hacker News (jaytel)','https://news.ycombinator.com/item?id=50405205'),('twombly skill listing','skills.sh','https://www.skills.sh/materic-inc/twombly-skill/twombly')]),

dict(slug='motion-pinch-press-gestures-with-fallbacks', date='2026-11-09', cat='craft', series=None, featured=True, tags=['Motion','gestures','pinch','long press','accessibility'],
 t=T('Motion’s new pinch and press gestures: ship them with a visible fallback',
     'Motion 新增双指缩放与按压手势：上线时务必配一个看得见的替代操作',
     'Motion 新增雙指縮放與按壓手勢：上線時務必配一個看得見的替代操作',
     'Motionの新しいピンチとプレスのジェスチャー：見える代替操作と一緒に出す',
     'Motion의 새 핀치·프레스 제스처: 눈에 보이는 대체 조작과 함께 내보내기',
     'Gerak isyarat pinch dan press baharu Motion: hantar bersama alternatif yang kelihatan',
     'Cử chỉ pinch và press mới của Motion: phát hành kèm một lựa chọn thay thế nhìn thấy được',
     'Les nouveaux gestes pinch et press de Motion : livrez-les avec une alternative visible',
     'Los nuevos gestos pinch y press de Motion: publícalos con una alternativa visible',
     'Motions neue Pinch- und Press-Gesten: nur mit sichtbarer Alternative ausliefern'),
 s=T('Motion 14.11 (9 November 2026) adds pinch for two-finger and trackpad zoom and rotate; 14.10 (5 November) gave press double press, long press and hold-to-repeat. What the new APIs do, where they quietly break scrolling and accessibility, and a checklist for shipping gestures with buttons that do the same job.',
     'Motion 14.11（2026 年 11 月 9 日）新增 pinch，支持双指和触控板缩放、旋转；14.10（11 月 5 日）让 press 支持双击、长按和按住连发。新 API 能做什么、会在哪里悄悄破坏滚动和无障碍，以及一份让手势与「做同一件事的按钮」一起上线的清单。',
     'Motion 14.11（2026 年 11 月 9 日）新增 pinch，支援雙指和觸控板縮放、旋轉；14.10（11 月 5 日）讓 press 支援雙擊、長按和按住連發。新 API 能做什麼、會在哪裡悄悄破壞捲動和無障礙，以及一份讓手勢與「做同一件事的按鈕」一起上線的清單。',
     'Motion 14.11（2026年11月9日）は2本指とトラックパッドでのズーム・回転を行うpinchを追加し、14.10（11月5日）はpressにダブルプレス、長押し、押し続けでの連続実行を加えた。新APIでできること、スクロールとアクセシビリティを静かに壊す場所、同じ操作ができるボタンと一緒に出すためのチェックリスト。',
     'Motion 14.11(2026년 11월 9일)은 두 손가락·트랙패드 확대와 회전을 위한 pinch를 추가했고, 14.10(11월 5일)은 press에 더블 프레스, 길게 누르기, 누르고 있으면 반복을 더했다. 새 API가 하는 일, 스크롤과 접근성을 조용히 깨는 지점, 같은 일을 하는 버튼과 함께 제스처를 내보내는 체크리스트.',
     'Motion 14.11 (9 November 2026) menambah pinch untuk zum dan putar dengan dua jari atau trackpad; 14.10 (5 November) memberi press tekan dua kali, tekan lama dan tahan untuk ulang. Apa yang dilakukan API baharu, di mana ia diam-diam merosakkan skrol dan kebolehcapaian, serta senarai semak untuk menghantar gerak isyarat bersama butang yang melakukan kerja sama.',
     'Motion 14.11 (9/11/2026) thêm pinch để phóng to và xoay bằng hai ngón tay hoặc trackpad; 14.10 (5/11) cho press nhấn đúp, nhấn giữ và giữ để lặp. API mới làm gì, chỗ nào nó âm thầm làm hỏng cuộn trang và khả năng tiếp cận, cùng checklist để phát hành cử chỉ kèm nút làm cùng việc.',
     'Motion 14.11 (9 novembre 2026) ajoute pinch pour zoomer et pivoter à deux doigts ou au trackpad ; 14.10 (5 novembre) a donné à press le double appui, l’appui long et la répétition au maintien. Ce que font ces API, où elles cassent discrètement le défilement et l’accessibilité, et une checklist pour livrer chaque geste avec un bouton qui fait la même chose.',
     'Motion 14.11 (9 de noviembre de 2026) añade pinch para hacer zoom y rotar con dos dedos o trackpad; 14.10 (5 de noviembre) dio a press doble pulsación, pulsación larga y repetir al mantener. Qué hacen las nuevas API, dónde rompen en silencio el scroll y la accesibilidad, y una lista para publicar cada gesto con un botón que haga lo mismo.',
     'Motion 14.11 (9. November 2026) bringt pinch für Zoomen und Drehen mit zwei Fingern oder Trackpad; 14.10 (5. November) gab press Doppeltippen, langes Drücken und Wiederholen beim Halten. Was die neuen APIs tun, wo sie unbemerkt Scrollen und Barrierefreiheit brechen, und eine Checkliste, um jede Geste mit einem Button auszuliefern, der dasselbe kann.'),
 en="""<p>Motion, the animation library that grew out of Framer Motion, shipped two gesture releases in five days. Version <strong>14.10.0</strong> on 5 November 2026 taught <code>press</code> to count, hold and repeat, so one function now covers double press, long press and press-and-hold steppers. Version <strong>14.11.0</strong> on 9 November added <code>pinch</code>: two-finger zoom and rotate, and a patch the same day (14.11.1) made rotation snapping use the release velocity and let you choose the pivot. For product teams this closes a gap that usually meant a second gesture library or a pile of pointer-event code. It also makes it very easy to ship interactions nobody can find, and some people cannot perform.</p>
<h2>What shipped</h2>
<ul><li><strong><code>pinch()</code> handles four kinds of input:</strong> two pointers, trackpads, <code>wheel</code> events with <code>ctrlKey</code>, and Safari’s own <code>gesturestart</code>/<code>gesturechange</code>/<code>gestureend</code> events. The element scales and rotates around the point between the fingers, or under the cursor on a trackpad.</li>
<li><strong>Limits, elasticity and snapping are options, not your maths.</strong> <code>scale</code> and <code>rotate</code> take <code>min</code>/<code>max</code>; <code>elastic</code> (default 0.35) controls how far you can overshoot; <code>rotate.snap: 90</code> lands on the nearest quarter turn; <code>snapToOrigin</code> springs back to 1× and upright. <code>origin</code> can be the pointer or a fixed point such as the centre.</li>
<li><strong>It plays well with the other gestures.</strong> With <code>drag</code> on the same element, lifting one finger continues as a drag without a jump, and a zoom does not end in a fling. A pinch is never a press: it cancels a running press with <code>success: false</code>.</li>
<li><strong><code>press()</code> gained <code>count</code>, <code>hold</code> and <code>repeat</code>.</strong> <code>count: 2</code> is a double press (with a 0.3-second default gap); <code>hold: 1</code> is a one-second long press with an <code>onHold</code> progress value from 0 to 1; <code>hold</code> plus <code>repeat</code> fires <code>onRepeat</code> while a stepper button is held. A long press cancels if the pointer moves more than a few pixels, so scrolling does not trigger it, and Motion suppresses the touch context menu.</li>
<li><strong>Keyboard support is built into <code>press</code>.</strong> Any element with a press gesture becomes focusable and responds to Enter. The 14.10 release also added Home and End keys to <code>Reorder</code> and a new <code>tap</code> prop on <code>motion</code> components.</li></ul>
<p>The pinch documentation shows a plain JavaScript function that takes an element, an array or a selector and returns a stop function. In a React component the natural shape is to call it on a ref inside an effect and return that stop function as the cleanup. That is our reading of the API, not a separate React prop, so check the docs for your installed version.</p>
<h2>Our take: a gesture is a shortcut, not a feature</h2>
<p>Pinch, double press and long press are invisible. Nothing on screen says “hold me” or “two fingers here”, and many people use a mouse, a keyboard, a switch or a single finger. WCAG 2.2 already draws the line. Success criterion 2.5.1 (Pointer Gestures, level A) says anything operated by a multipoint or path-based gesture must also work with a single pointer, unless the gesture is essential. 2.5.7 (Dragging Movements, AA) says the same for dragging. So the shippable pattern is always a pair: the gesture as a fast path for people who know it, and a visible control that does exactly the same thing.</p>
<p>The second trap is quieter. <code>pinch</code> sets <code>touch-action: none</code> on the element so the browser does not scroll or zoom the page underneath. That is correct inside a photo viewer. On a full-width image in a scrolling feed, it means a one-finger swipe that starts on the image no longer scrolls the page. The fix is a design decision, not a code tweak: make things pinchable inside a focused surface such as a lightbox, a map or a canvas, and keep inline media static.</p>
<p>Press variants need the same discipline. Do not stack a single press and a double press on one element unless you are happy for the single action to feel delayed or ambiguous; give each element one job. Long press is best for <em>hold to confirm</em> on destructive actions, where the <code>onHold</code> progress can draw a ring that fills as you hold, and the hold itself is the safety. It is a poor place to hide the only way to reach a menu. Hold-to-repeat belongs on stepper buttons that still change by one on a normal press, next to a field you can type into.</p>
<h2>Checklist before you ship a gesture</h2>
<ol><li><strong>Write the visible control first.</strong> Zoom buttons and a reset, a rotate button, a ⋯ menu, a delete button with confirmation. Then add the gesture as a shortcut for the same action.</li>
<li><strong>Pinch only inside a focused surface.</strong> Lightbox, map, editor canvas. Never a full-bleed image in a scrolling page, because <code>touch-action: none</code> takes over the swipe.</li>
<li><strong>Set limits that match the content.</strong> For photos, <code>scale: { min: 1, max: 4 }</code> with a low <code>elastic</code>; turn <code>rotate</code> off unless rotation means something.</li>
<li><strong>Snap to states the user can name.</strong> <code>rotate.snap: 90</code> for orientation, <code>snapToOrigin</code> for a “fit” reset, and show the current zoom as text.</li>
<li><strong>One press meaning per element.</strong> Do not combine single and double press on the same target.</li>
<li><strong>Use long press as hold-to-confirm, with progress.</strong> Draw <code>onHold</code> progress, cancel cleanly on early release, and offer a normal confirm dialog as the alternative.</li>
<li><strong>Hold-to-repeat starts slow.</strong> A short <code>hold</code> before <code>repeat</code>, so a quick tap still changes the value by one, and a text field for big jumps.</li>
<li><strong>Test with keyboard only.</strong> Tab to every pressable element and press Enter. Check that held-key behaviour matches what you expect rather than assuming.</li>
<li><strong>Test on a real phone and a trackpad.</strong> Ctrl-wheel on a desktop mouse, Safari on iOS, Android Chrome; confirm the page still scrolls around the gesture surface.</li>
<li><strong>Tell people once.</strong> A one-line hint (“Pinch or use + / − to zoom”) the first time the surface opens, then get out of the way.</li></ol>
<pre><code># Paste this to your coding agent
Add Motion gestures to our image viewer only (the lightbox, not the feed).
Use pinch() with scale { min: 1, max: 4 }, elastic 0.2, rotate off, and
a "Fit" button that animates scale, rotate, x and y back to their start.
Attach it in an effect on a ref and call the returned stop function on cleanup.
Every gesture needs a visible control that does the same thing:
  + / − zoom buttons, a Fit button, and the current zoom shown as text.
For "Delete photo", use press() with hold: 1 and draw onHold progress as a
ring; keep the normal confirm dialog as the alternative path.
Keep page scrolling working outside the lightbox. Test keyboard-only,
iOS Safari and a trackpad, and list anything you could not test.</code></pre>
<h2>When not to use it</h2>
<p>Skip pinch when the content is text: let the browser’s own zoom do its job, and never block it. Skip long press and double press for primary actions in a web app that most people will use with a mouse. Use these gestures where they match a physical expectation—photos, maps, canvases, steppers, hold-to-confirm—and treat them as shortcuts layered over controls everyone can see.</p>
<p>Related on UI Hub: <a href="../motion-that-feels-right/">motion that feels right</a>, <a href="../best-animated-react-component-libraries-2026/">animated React component libraries</a>, and <a href="../accessibility-in-ai-generated-ui/">accessibility in AI-generated UI</a>.</p>""",
 zh="""<p>从 Framer Motion 演变而来的动画库 Motion，五天内发了两次手势更新。2026 年 11 月 5 日的 <strong>14.10.0</strong> 让 <code>press</code> 学会了计数、按住和连发，一个函数就能覆盖双击、长按和按住不放的步进按钮。11 月 9 日的 <strong>14.11.0</strong> 新增 <code>pinch</code>：双指缩放和旋转；同一天的补丁 14.11.1 让旋转吸附参考松手时的速度，并允许你选择旋转与缩放的支点。对产品团队来说，这补上了过去常要另装一个手势库、或手写一堆 pointer 事件代码的缺口。同时，它也让人很容易做出没人找得到、甚至有些人根本做不出来的交互。</p>
<h2>这次发了什么</h2>
<ul><li><strong><code>pinch()</code> 支持四类输入：</strong>两个触点、触控板、带 <code>ctrlKey</code> 的 <code>wheel</code> 事件，以及 Safari 自己的 <code>gesturestart</code>/<code>gesturechange</code>/<code>gestureend</code> 事件。元素围绕两指之间的点缩放和旋转；在触控板上则围绕光标所在位置。</li>
<li><strong>限制、弹性和吸附都是选项，不用你自己算。</strong><code>scale</code> 和 <code>rotate</code> 接受 <code>min</code>/<code>max</code>；<code>elastic</code>（默认 0.35）控制能越界多远；<code>rotate.snap: 90</code> 会落到最近的 90 度；<code>snapToOrigin</code> 会弹回 1 倍并摆正。<code>origin</code> 可以是指尖位置，也可以是固定点，比如中心。</li>
<li><strong>和其他手势配合良好。</strong>同一元素加上 <code>drag</code> 时，抬起一根手指会无跳动地接着拖动，而缩放结束时不会被甩飞。pinch 永远不算 press：它会以 <code>success: false</code> 取消正在进行的 press。</li>
<li><strong><code>press()</code> 新增 <code>count</code>、<code>hold</code> 和 <code>repeat</code>。</strong><code>count: 2</code> 是双击（默认两次间隔 0.3 秒）；<code>hold: 1</code> 是一秒长按，并通过 <code>onHold</code> 给出 0 到 1 的进度；<code>hold</code> 加 <code>repeat</code> 会在按住步进按钮时持续触发 <code>onRepeat</code>。指针移动超过几个像素，长按就会取消，所以滚动不会误触；Motion 还会阻止触屏长按弹出的系统菜单。</li>
<li><strong><code>press</code> 自带键盘支持。</strong>任何带 press 手势的元素都会变得可聚焦，并响应 Enter。14.10 还给 <code>Reorder</code> 加上了 Home 和 End 键，并为 <code>motion</code> 组件新增 <code>tap</code> 属性。</li></ul>
<p>pinch 文档展示的是一个普通 JavaScript 函数：接受元素、元素数组或选择器，返回一个停止函数。在 React 组件里，顺手的写法是在 effect 中对 ref 调用它，再把停止函数作为清理函数返回。这是我们对 API 的理解，并不是一个单独的 React 属性，请以你安装版本的文档为准。</p>
<h2>我们的看法：手势是快捷方式，不是功能本身</h2>
<p>双指缩放、双击和长按都是看不见的。屏幕上没有任何东西写着「按住我」或「这里用两根手指」，而很多人用的是鼠标、键盘、开关设备或一根手指。WCAG 2.2 早已划好线：成功准则 2.5.1（指针手势，A 级）要求凡是靠多点或路径手势操作的功能，都必须也能用单个指针完成，除非该手势本身不可替代；2.5.7（拖动动作，AA 级）对拖动提出同样要求。所以能上线的形态永远是一对：手势是给熟手的快速通道，旁边还要有一个做完全相同事情的可见控件。</p>
<p>第二个坑更隐蔽。<code>pinch</code> 会在元素上设置 <code>touch-action: none</code>，让浏览器不再滚动或缩放下面的页面。放在图片查看器里这是对的；放在可滚动信息流里的一张通栏大图上，就意味着从图上开始的单指滑动再也滚不动页面。解决办法是设计决策，而不是改一行代码：只在专注的界面里允许缩放——灯箱、地图、画布——信息流里的媒体保持静态。</p>
<p>按压的各种变体也需要同样的克制。除非你能接受单击动作变得迟缓或含糊，否则不要在同一个元素上同时叠单击和双击；一个元素只做一件事。长按最适合用来做破坏性操作的「按住确认」：<code>onHold</code> 的进度可以画成一个随按住逐渐填满的圆环，按住这个动作本身就是保险。把唯一的菜单入口藏在长按里则很糟。按住连发应当放在步进按钮上，普通点一下仍然只加一，旁边还要有可以直接输入的字段。</p>
<h2>上线手势前的清单</h2>
<ol><li><strong>先写可见控件。</strong>缩放按钮和复位、旋转按钮、⋯ 菜单、带确认的删除按钮。然后再把手势作为同一操作的快捷方式加上去。</li>
<li><strong>只在专注界面里允许双指缩放。</strong>灯箱、地图、编辑画布。永远不要放在可滚动页面里的通栏图上，因为 <code>touch-action: none</code> 会接管滑动。</li>
<li><strong>按内容设置限制。</strong>照片用 <code>scale: { min: 1, max: 4 }</code> 和较低的 <code>elastic</code>；除非旋转有意义，否则关掉 <code>rotate</code>。</li>
<li><strong>吸附到用户说得出名字的状态。</strong>方向用 <code>rotate.snap: 90</code>，「适应窗口」复位用 <code>snapToOrigin</code>，并用文字显示当前缩放比例。</li>
<li><strong>每个元素只有一种按压含义。</strong>不要在同一目标上同时用单击和双击。</li>
<li><strong>长按当作带进度的按住确认。</strong>画出 <code>onHold</code> 进度，提前松手要干净地取消，并提供普通的确认对话框作为替代。</li>
<li><strong>按住连发要慢启动。</strong>在 <code>repeat</code> 之前留一小段 <code>hold</code>，让快速点一下仍然只改变一，大幅调整则提供输入框。</li>
<li><strong>只用键盘测一遍。</strong>Tab 到每个可按压元素再按 Enter。按住按键时的表现要实际核对，不要想当然。</li>
<li><strong>在真手机和触控板上测。</strong>桌面鼠标的 Ctrl+滚轮、iOS Safari、安卓 Chrome；确认手势区域周围的页面仍能正常滚动。</li>
<li><strong>只提示一次。</strong>界面第一次打开时给一句提示（「双指缩放，或用 + / − 缩放」），之后就别再打扰。</li></ol>
<pre><code># 把这段贴给你的编程智能体
只给我们的图片查看器（灯箱，不是信息流）加 Motion 手势。
用 pinch()，scale { min: 1, max: 4 }、elastic 0.2、关闭 rotate，
另加一个「适应」按钮，把 scale、rotate、x、y 动画回初始值。
在 effect 里对 ref 挂载，清理时调用返回的停止函数。
每个手势都要有做同样事情的可见控件：
  + / − 缩放按钮、「适应」按钮，并用文字显示当前缩放比例。
「删除照片」用 press()，hold: 1，把 onHold 进度画成圆环；
保留普通的确认对话框作为替代路径。
灯箱外的页面滚动必须正常。只用键盘、iOS Safari 和触控板各测一遍，
列出你没能测试的项目。</code></pre>
<h2>什么时候别用</h2>
<p>内容是文字时不要用 pinch：让浏览器自带的缩放去做，永远不要拦截它。在大多数人用鼠标的网页应用里，不要把主要操作交给长按和双击。只在符合物理直觉的地方用这些手势——照片、地图、画布、步进按钮、按住确认——并把它们当作叠在人人都看得见的控件之上的快捷方式。</p>
<p>UI Hub 相关阅读：<a href="../motion-that-feels-right/">让动效感觉对</a>、<a href="../best-animated-react-component-libraries-2026/">动效 React 组件库</a>，以及<a href="../accessibility-in-ai-generated-ui/">AI 生成界面的无障碍</a>。</p>""",
 refs=[('Motion changelog (14.10.0 on 5 Nov, 14.11.0 and 14.11.1 on 9 Nov 2026)','Motion','https://motion.dev/changelog'),('CHANGELOG.md','motiondivision/motion on GitHub','https://raw.githubusercontent.com/motiondivision/motion/refs/heads/main/CHANGELOG.md'),('pinch','Motion docs','https://motion.dev/docs/pinch'),('press','Motion docs','https://motion.dev/docs/press'),('Pinch zoom live example','Motion examples','https://examples.motion.dev/js/pinch-zoom'),('Gesture animation (React)','Motion docs','https://motion.dev/docs/react-gestures'),('touch-action','MDN Web Docs','https://developer.mozilla.org/en-US/docs/Web/CSS/touch-action'),('Understanding SC 2.5.1: Pointer Gestures','W3C WAI','https://www.w3.org/WAI/WCAG22/Understanding/pointer-gestures.html'),('Understanding SC 2.5.7: Dragging Movements','W3C WAI','https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html')]),
dict(slug='adobe-max-2026-agents-keep-layers-editable', date='2026-11-10', cat='agents', series=None, featured=True, tags=['Adobe MAX','Firefly Builder','Plan Mode','MCP','design systems'],
 t=T('Adobe MAX 2026: when agents edit your layered files, file hygiene becomes the interface',
     'Adobe MAX 2026：当智能体直接改你的分层文件，文件整洁度就成了接口',
     'Adobe MAX 2026：當智能體直接改你的分層檔案，檔案整潔度就成了介面',
     'Adobe MAX 2026：エージェントがレイヤー付きファイルを直接編集するなら、ファイルの整理がインターフェースになる',
     'Adobe MAX 2026: 에이전트가 레이어 파일을 직접 고친다면, 파일 정리가 곧 인터페이스다',
     'Adobe MAX 2026: apabila ejen mengedit fail berlapis anda, kekemasan fail menjadi antara mukanya',
     'Adobe MAX 2026: khi agent sửa thẳng tệp nhiều lớp của bạn, sự gọn gàng của tệp trở thành giao diện',
     'Adobe MAX 2026 : quand des agents modifient vos fichiers à calques, l’hygiène des fichiers devient l’interface',
     'Adobe MAX 2026: cuando los agentes editan tus archivos con capas, el orden del archivo se vuelve la interfaz',
     'Adobe MAX 2026: Wenn Agents deine Ebenen-Dateien bearbeiten, wird Dateihygiene zur Schnittstelle'),
 s=T('At MAX on 10 November 2026 Adobe previewed local MCP integrations that let outside agents change Photoshop, Illustrator, Premiere and After Effects files with layers left editable, added Plan Mode to the Firefly AI Assistant, and put Firefly Builder, a prompt-to-prototype tool, in private beta. What was announced, what is not shipping yet, and a checklist for getting files and brand rules ready for agents.',
     '2026 年 11 月 10 日的 MAX 大会上，Adobe 预告了本地 MCP 集成：让外部智能体直接修改 Photoshop、Illustrator、Premiere 和 After Effects 文件，图层仍保持可编辑；Firefly AI 助手新增 Plan Mode（计划模式）；提示生成原型的 Firefly Builder 进入私测。这篇梳理发布了什么、哪些还没上线，并给出一份让文件和品牌规则为智能体做好准备的清单。',
     '2026 年 11 月 10 日的 MAX 大會上，Adobe 預告了本機 MCP 整合：讓外部智能體直接修改 Photoshop、Illustrator、Premiere 和 After Effects 檔案，圖層仍保持可編輯；Firefly AI 助理新增 Plan Mode（計畫模式）；提示產生原型的 Firefly Builder 進入私測。這篇梳理發布了什麼、哪些還沒上線，並給出一份讓檔案和品牌規則為智能體做好準備的清單。',
     '2026年11月10日のMAXで、Adobeは外部エージェントがPhotoshop・Illustrator・Premiere・After Effectsのファイルをレイヤーを編集可能なまま変更できるローカルMCP連携をプレビューし、Firefly AI AssistantにPlan Modeを追加、プロンプトからプロトタイプを作るFirefly Builderを非公開ベータにした。発表内容、まだ出ていないもの、ファイルとブランドルールをエージェント向けに整えるチェックリスト。',
     '2026년 11월 10일 MAX에서 Adobe는 외부 에이전트가 레이어를 편집 가능한 상태로 둔 채 Photoshop·Illustrator·Premiere·After Effects 파일을 바꿀 수 있는 로컬 MCP 연동을 미리 공개했고, Firefly AI Assistant에 Plan Mode를 더했으며, 프롬프트로 프로토타입을 만드는 Firefly Builder를 비공개 베타로 내놓았다. 발표 내용, 아직 나오지 않은 것, 파일과 브랜드 규칙을 에이전트용으로 준비하는 체크리스트.',
     'Di MAX pada 10 November 2026, Adobe mempratonton integrasi MCP tempatan yang membolehkan ejen luar mengubah fail Photoshop, Illustrator, Premiere dan After Effects dengan lapisan kekal boleh diedit, menambah Plan Mode pada Firefly AI Assistant, dan meletakkan Firefly Builder, alat prompt-ke-prototaip, dalam beta tertutup. Apa yang diumumkan, apa yang belum dihantar, dan senarai semak untuk menyediakan fail serta peraturan jenama bagi ejen.',
     'Tại MAX ngày 10/11/2026, Adobe giới thiệu trước tích hợp MCP cục bộ cho phép agent bên ngoài sửa tệp Photoshop, Illustrator, Premiere và After Effects mà các lớp vẫn chỉnh được, thêm Plan Mode cho Firefly AI Assistant, và đưa Firefly Builder, công cụ biến prompt thành prototype, vào beta kín. Những gì đã công bố, những gì chưa phát hành, và checklist để chuẩn bị tệp cùng quy tắc thương hiệu cho agent.',
     'À MAX, le 10 novembre 2026, Adobe a présenté en avant-première des intégrations MCP locales qui laissent des agents externes modifier des fichiers Photoshop, Illustrator, Premiere et After Effects en gardant les calques modifiables, a ajouté un Plan Mode à Firefly AI Assistant et ouvert Firefly Builder, un outil prompt-vers-prototype, en bêta privée. Ce qui a été annoncé, ce qui n’est pas encore disponible, et une checklist pour préparer fichiers et règles de marque aux agents.',
     'En MAX, el 10 de noviembre de 2026, Adobe adelantó integraciones MCP locales que permiten a agentes externos modificar archivos de Photoshop, Illustrator, Premiere y After Effects manteniendo las capas editables, añadió Plan Mode a Firefly AI Assistant y lanzó en beta privada Firefly Builder, una herramienta de prompt a prototipo. Qué se anunció, qué aún no está disponible y una lista para preparar archivos y reglas de marca para agentes.',
     'Auf der MAX am 10. November 2026 zeigte Adobe lokale MCP-Integrationen, mit denen externe Agents Photoshop-, Illustrator-, Premiere- und After-Effects-Dateien ändern, während die Ebenen bearbeitbar bleiben, ergänzte den Firefly AI Assistant um einen Plan Mode und startete Firefly Builder, ein Prompt-zu-Prototyp-Tool, in der privaten Beta. Was angekündigt wurde, was noch nicht erscheint, und eine Checkliste, um Dateien und Markenregeln für Agents vorzubereiten.'),
 en="""<p>Adobe opened MAX in Miami Beach on 10 November 2026 with a long list of agent features. Most of them are about Adobe’s own assistant. The one that matters most for designers is about other people’s agents: Adobe previewed <strong>local MCP integrations</strong> that let an outside agent, such as one from OpenAI, Google or Anthropic, make changes directly in Photoshop, Illustrator, Premiere and After Effects project files on your own computer, with layers, vectors, bins and sequences still editable afterwards. That is not shipping yet. Adobe says a private beta starts in early 2027. But it tells you where the work is going, and the preparation is mostly about your files, not about the tools.</p>
<h2>What was announced</h2>
<ul><li><strong>Local MCP integrations (preview).</strong> MCP, the Model Context Protocol, is the open standard many assistants use to call outside tools. Adobe’s version runs locally against native project files. Coverage across the announcements is consistent: Photoshop, Illustrator, Premiere and After Effects, edits stay editable, and the agent can chain other MCP tools, for example pulling a brief from Google Docs and posting results to Slack. An Adobe vice president told TechCrunch the company is still deciding which capabilities to expose and will follow how people use it.</li>
<li><strong>Plan Mode in the Firefly AI Assistant (beta).</strong> You review, edit and approve the agent’s plan before it runs a multi-step task. A Model Selector lets you pick the model or leave it on auto. The assistant can now store preferred formats, colours, brand guidelines, characters and products and apply them to every project.</li>
<li><strong>Firefly Builder (private beta).</strong> A natural-language tool that turns an idea into an interactive, on-brand prototype of a website, presentation or app, with no code. TechCrunch framed it as Adobe moving into Figma’s territory; Creative Bloq noted Adobe’s claim that it stays on your design system, and said that is the claim to test first.</li>
<li><strong>Always-on agents (preview).</strong> Agents that keep doing recurring work in the background, such as organising incoming assets, checking quality and preparing channel versions, and come back for your review. Adobe says these arrive in the Firefly AI Assistant first, with no date.</li>
<li><strong>Brand Intelligence goes into the editors.</strong> Adobe’s brand-checking agent gains Intelligent Reflow, which adapts a design to new sizes and layouts, and is coming to Photoshop, Illustrator and InDesign. Firefly also gets a beta design canvas (Firefly Design) and Firefly Graph for saved, repeatable workflows.</li></ul>
<h2>Our take: a named layer is now an API</h2>
<p>When a person opens your file, they can cope with “Layer 47 copy 3”. An agent working through MCP cannot see what you meant; it sees names, groups, artboards, swatches and text frames. If those are tidy, “swap the hero photo on every social size and keep the headline” is one clear instruction. If they are not, the agent will guess, and a wrong guess inside a native file is harder to spot than a bad generated image, because it looks finished. So the first job is boring: name things the way you name components in code, group by function, keep text as live text and brand colours as library swatches.</p>
<p>The second point is the output contract. “Layers stay editable” is the important promise in this release, and it is also what you should check every time. A tool that flattens a layer, outlines text or rasterises a vector has handed you a picture, not a file. Make “still editable” part of review, next to “looks right”.</p>
<p>Third, approvals. Plan Mode is the right default for anything multi-step, and it is the same pattern we argued for in <a href="../agent-approval-ui-budgets-interruptions/">approval UI for agents</a>: read the plan, cut the steps you did not ask for, then run. Always-on agents raise the stakes, because nobody is watching when they work. Give them a review queue, never a publish button.</p>
<p>Finally, Builder. Every prompt-to-prototype tool says it is on-brand; most drift on the first unusual request. Before you trust it, or any rival, run the same small set of awkward prompts and count what leaves your system: new colours, new radii, components you do not have.</p>
<h2>Checklist: get your files ready for agents</h2>
<ol><li><strong>Name layers and artboards like components.</strong> “hero/photo”, “hero/headline”, “cta/primary”. No “copy 3”. Group by function, not by when you made it.</li>
<li><strong>Keep brand rules in one place.</strong> Colours, type and logo rules as library swatches and styles, plus one short written guideline. Load that into the assistant’s preferences instead of retyping it in every prompt.</li>
<li><strong>Lock what must not change.</strong> Logos, legal text and approved photography on locked layers, and say in the prompt that locked layers are off limits.</li>
<li><strong>Turn on plan approval.</strong> For multi-step jobs, read the plan first. Reject any step that touches files, layers or channels you did not name.</li>
<li><strong>Work on a copy, then compare.</strong> Duplicate or version the file before an outside agent edits it, and compare the layer list afterwards: what was added, renamed, flattened or deleted.</li>
<li><strong>Check that output is still editable.</strong> Live text, vector paths, smart objects and adjustment layers, not a flattened bitmap. Treat a flattened result as a failed run.</li>
<li><strong>Stress-test “on-brand” claims.</strong> Five awkward prompts (a dense table, an error state, a long German headline, a dark theme, a new component) and count anything off-system.</li>
<li><strong>Give background agents a queue.</strong> Always-on work lands in a review folder with a daily check, a spending limit and an easy off switch.</li>
<li><strong>Scope every connection.</strong> Which apps and folders an agent may touch, which MCP tools it may chain, and a log of what it changed.</li></ol>
<pre><code># Paste this to your design agent (before any MCP edit)
Work only on the duplicate file I name; never the original.
Before running, write a numbered plan and wait for my approval.
Target layers by name. Do not touch locked layers or anything
named logo/*, legal/*, or approved/*.
Keep text as live text, vectors as paths, smart objects intact.
Use only colours and type styles from the linked brand library.
When done, list every layer you added, renamed, moved, flattened
or deleted, and anything you could not do.</code></pre>
<h2>What to do this week</h2>
<p>Nothing here needs the beta. Pick one real campaign file, clean its names and groups, move its colours into a library, and write the one-page guideline. That file will work better with Adobe’s assistant, with Figma’s agent and with whatever MCP client you use next year. If you already keep tokens for your product UI, point the guideline at them so print, social and product share one source.</p>
<p>Related on UI Hub: <a href="../lint-agents-onto-your-design-system/">lint agents onto your design system</a>, <a href="../ai-design-tool-shutdowns-keep-work-portable/">keep AI design work portable</a>, and <a href="../design-tokens-for-agents/">design tokens for agents</a>.</p>""",
 zh="""<p>2026 年 11 月 10 日，Adobe 在迈阿密海滩开幕 MAX 大会，发布了一长串智能体功能。大部分是关于 Adobe 自家助手的；对设计师最重要的一条，却是关于别人家的智能体：Adobe 预告了<strong>本地 MCP 集成</strong>，让外部智能体（比如来自 OpenAI、Google 或 Anthropic 的）直接在你自己电脑上的 Photoshop、Illustrator、Premiere 和 After Effects 项目文件里动手改，改完之后图层、矢量、素材箱和序列依然可编辑。这项功能还没上线，Adobe 说私测要到 2027 年初。但它指明了方向，而要做的准备主要在你的文件上，而不是在工具上。</p>
<h2>这次发布了什么</h2>
<ul><li><strong>本地 MCP 集成（预览）。</strong>MCP 即模型上下文协议，是许多 AI 助手调用外部工具的开放标准。Adobe 的版本在本机针对原生项目文件运行。各方报道口径一致：覆盖 Photoshop、Illustrator、Premiere 和 After Effects，改动保持可编辑，智能体还能串联其他 MCP 工具，比如从 Google Docs 拉简报、把结果发到 Slack。一位 Adobe 副总裁对 TechCrunch 表示，公司还在决定开放哪些能力，会根据大家怎么用再调整。</li>
<li><strong>Firefly AI 助手（测试版）新增 Plan Mode。</strong>智能体执行多步骤任务之前，你可以审阅、修改并批准它的计划。模型选择器让你指定模型或交给自动选择。助手现在还能保存偏好的格式、颜色、品牌规范、角色和产品，并应用到每个项目。</li>
<li><strong>Firefly Builder（私测）。</strong>用自然语言把想法变成可交互、符合品牌的网站、演示或应用原型，不用写代码。TechCrunch 认为这是 Adobe 进入 Figma 的地盘；Creative Bloq 提到 Adobe 声称它不会偏离你的设计系统，并说这正是最该先测试的说法。</li>
<li><strong>常驻智能体（预览）。</strong>在后台持续处理重复性工作的智能体，比如整理新进素材、检查质量、准备各渠道版本，再交回给你审核。Adobe 说会先进入 Firefly AI 助手，没有给出日期。</li>
<li><strong>Brand Intelligence 进入编辑器。</strong>Adobe 的品牌检查智能体新增 Intelligent Reflow，可把设计自动适配到新尺寸和版式，并将进入 Photoshop、Illustrator 和 InDesign。Firefly 还推出测试版设计画布 Firefly Design，以及可保存、可重复运行工作流的 Firefly Graph。</li></ul>
<h2>我们的看法：一个命名好的图层，现在就是一个 API</h2>
<p>人打开你的文件，还能忍受「图层 47 拷贝 3」。通过 MCP 工作的智能体看不出你的本意，它看到的是名称、分组、画板、色板和文本框。这些整齐，「把每个社媒尺寸里的主图换掉，标题保持不变」就是一条清楚的指令；不整齐，智能体就只能猜。而在原生文件里猜错，比生成一张坏图更难发现，因为它看起来已经完工了。所以第一件事很枯燥：像给代码组件起名那样给图层起名，按功能分组，文字保持为可编辑文字，品牌色放进库里的色板。</p>
<p>第二点是输出约定。「图层保持可编辑」是这次发布里最重要的承诺，也是你每次都该检查的东西。工具一旦把图层拼合、把文字转曲、把矢量栅格化，交给你的就是一张图，而不是一个文件。把「仍可编辑」写进审核项，和「看起来对」并列。</p>
<p>第三是审批。对任何多步骤任务，Plan Mode 都应该是默认设置，这和我们在<a href="../agent-approval-ui-budgets-interruptions/">智能体审批界面</a>一文里主张的模式一样：先读计划，删掉你没要求的步骤，再执行。常驻智能体让风险更高，因为它干活时没人盯着。给它一个审核队列，永远不要给它发布按钮。</p>
<p>最后是 Builder。每个提示生成原型的工具都说自己符合品牌；大多数在第一个不寻常的请求上就跑偏。在信任它或任何竞品之前，用同一组刁钻的小提示跑一遍，数一数有多少东西跑出了你的设计系统：新颜色、新圆角、你没有的组件。</p>
<h2>清单：让文件为智能体做好准备</h2>
<ol><li><strong>像命名组件一样命名图层和画板。</strong>「hero/photo」「hero/headline」「cta/primary」，不要「拷贝 3」。按功能分组，而不是按创建时间。</li>
<li><strong>品牌规则只放一处。</strong>颜色、字体和 Logo 规则做成库里的色板和样式，再加一份简短的书面规范。把它载入助手的偏好设置，而不是每次在提示里重打。</li>
<li><strong>锁住不能改的东西。</strong>Logo、法律文字和已批准的摄影图放在锁定图层上，并在提示里写明锁定图层禁止改动。</li>
<li><strong>打开计划审批。</strong>多步骤任务先读计划。凡是碰到你没点名的文件、图层或渠道的步骤，一律驳回。</li>
<li><strong>在副本上改，再做对比。</strong>外部智能体动手前先复制或存版本，事后对比图层列表：新增、改名、拼合、删除了什么。</li>
<li><strong>检查输出是否仍可编辑。</strong>可编辑文字、矢量路径、智能对象和调整图层，而不是一张拼合的位图。拼合结果一律算作失败。</li>
<li><strong>压力测试「符合品牌」的说法。</strong>五条刁钻提示（密集表格、错误状态、很长的德语标题、深色主题、一个新组件），数出所有超出设计系统的东西。</li>
<li><strong>给后台智能体一个队列。</strong>常驻任务的产出进审核文件夹，每天检查一次，设消费上限，并且能一键关掉。</li>
<li><strong>每个连接都要限定范围。</strong>智能体能碰哪些应用和文件夹、能串联哪些 MCP 工具，并记录它改了什么。</li></ol>
<pre><code># 把这段贴给你的设计智能体（任何 MCP 改动之前）
只在我指定的副本文件上工作，绝不动原文件。
执行前先写编号计划，等我批准。
按名称定位图层。不要碰锁定图层，也不要碰
logo/*、legal/*、approved/* 开头的任何图层。
文字保持可编辑，矢量保持路径，智能对象保持完整。
只使用已链接品牌库里的颜色和文字样式。
完成后列出你新增、改名、移动、拼合或删除的每个图层，
以及你没能完成的事项。</code></pre>
<h2>这周可以做什么</h2>
<p>以上没有一项需要等测试版。挑一个真实的活动文件，把命名和分组理干净，把颜色挪进库里，写一页规范。这个文件无论配 Adobe 的助手、Figma 的智能体，还是你明年用的任何 MCP 客户端，都会更好用。如果你已经为产品界面维护了 Token，就让这份规范指向它们，让印刷、社媒和产品共用一个来源。</p>
<p>UI Hub 相关阅读：<a href="../lint-agents-onto-your-design-system/">用 Lint 把智能体约束在设计系统上</a>、<a href="../ai-design-tool-shutdowns-keep-work-portable/">让 AI 设计成果可迁移</a>，以及<a href="../design-tokens-for-agents/">给智能体的设计 Token</a>。</p>""",
 refs=[('Adobe brings AI agents and new creative tools to Photoshop, Premiere, and Firefly','Ivan Mehta, TechCrunch','https://techcrunch.com/2026/11/10/adobe-adds-more-ai-to-its-products-and-launches-an-mcp/'),('Adobe is going all in on agentic AI','Jess Weatherbed, The Verge','https://www.theverge.com/tech/1030593/adobe-max-ai-agents-mcp-firefly-assistant-updates'),('Adobe Firefly is now a creative studio, and it means AI is everything everywhere all at once','Ian Dean, Creative Bloq','https://www.creativebloq.com/news/adobes-firefly-is-now-a-creative-studio-and-it-means-ai-is-everything-everywhere-all-at-once'),('Adobe Powers a New Era of Creativity, Bringing Agents and Tools to Creatives Wherever and However They Create','Adobe via Business Wire','https://www.businesswire.com/news/home/20261110226769/en/Adobe-Powers-a-New-Era-of-Creativity-Bringing-Agents-and-Tools-to-Creatives-Wherever-and-However-They-Create'),('Architecture overview','Model Context Protocol','https://modelcontextprotocol.io/docs/learn/architecture')]),
dict(slug='figma-motion-physics-springs-handoff', date='2026-11-11', cat='craft', series=None, featured=True, tags=['Figma Motion','springs','Lottie','motion tokens','handoff'],
 t=T('Figma Motion now has physics springs: hand off three numbers, not a duration',
     'Figma Motion 支持物理弹簧了：交付三个数字，而不是一个时长',
     'Figma Motion 支援物理彈簧了：交付三個數字，而不是一個時長',
     'Figma Motionに物理スプリングが来た：渡すのは長さではなく3つの数値',
     'Figma Motion에 물리 스프링이 생겼다: 시간 대신 숫자 세 개를 넘겨라',
     'Figma Motion kini ada spring fizik: serahkan tiga nombor, bukan satu tempoh',
     'Figma Motion đã có spring vật lý: bàn giao ba con số, không phải một thời lượng',
     'Figma Motion a désormais des ressorts physiques : transmettez trois nombres, pas une durée',
     'Figma Motion ya tiene muelles físicos: entrega tres números, no una duración',
     'Figma Motion hat jetzt physikalische Federn: Übergib drei Zahlen statt einer Dauer'),
 s=T('On 10 November 2026 Figma Motion added physics-based springs (mass, stiffness, damping) that can be saved in a design system, plus style previews and Lottie export previews. Why a spring belongs in your tokens, how to convert one spring for SwiftUI, Jetpack Compose, Motion and CSS without it feeling different on each, and a handoff checklist.',
     '2026 年 11 月 10 日，Figma Motion 新增基于物理的弹簧（质量、刚度、阻尼），可以存进设计系统，同时加入动画样式预览和 Lottie 导出预览。为什么弹簧应该成为 Token，如何把同一个弹簧换算到 SwiftUI、Jetpack Compose、Motion 和 CSS 而手感不走样，以及一份交付清单。',
     '2026 年 11 月 10 日，Figma Motion 新增基於物理的彈簧（質量、剛度、阻尼），可以存進設計系統，同時加入動畫樣式預覽和 Lottie 匯出預覽。為什麼彈簧應該成為 Token，如何把同一個彈簧換算到 SwiftUI、Jetpack Compose、Motion 和 CSS 而手感不走樣，以及一份交付清單。',
     '2026年11月10日、Figma Motionに物理ベースのスプリング（質量・剛性・減衰）が加わり、デザインシステムに保存できるようになった。スタイルプレビューとLottie書き出しプレビューも追加。スプリングをトークンにすべき理由、同じスプリングをSwiftUI・Jetpack Compose・Motion・CSSへ手触りを変えずに変換する方法、そして受け渡しチェックリスト。',
     '2026년 11월 10일 Figma Motion에 디자인 시스템에 저장할 수 있는 물리 기반 스프링(질량·강성·감쇠)이 추가됐고, 스타일 미리보기와 Lottie 내보내기 미리보기도 생겼다. 스프링을 토큰으로 둬야 하는 이유, 같은 스프링을 SwiftUI·Jetpack Compose·Motion·CSS로 느낌 그대로 옮기는 방법, 그리고 핸드오프 체크리스트.',
     'Pada 10 November 2026 Figma Motion menambah spring berasaskan fizik (jisim, kekakuan, redaman) yang boleh disimpan dalam sistem reka bentuk, serta pratonton gaya dan pratonton eksport Lottie. Mengapa spring patut menjadi token, cara menukar satu spring untuk SwiftUI, Jetpack Compose, Motion dan CSS tanpa rasa berbeza, dan senarai semak serahan.',
     'Ngày 10/11/2026 Figma Motion thêm spring dựa trên vật lý (khối lượng, độ cứng, giảm chấn) có thể lưu vào design system, cùng xem trước style và xem trước khi xuất Lottie. Vì sao spring nên là token, cách quy đổi một spring cho SwiftUI, Jetpack Compose, Motion và CSS mà cảm giác không đổi, và checklist bàn giao.',
     'Le 10 novembre 2026, Figma Motion a ajouté des ressorts physiques (masse, raideur, amortissement) enregistrables dans un design system, ainsi que des aperçus de styles et d’export Lottie. Pourquoi un ressort doit devenir un token, comment convertir un même ressort pour SwiftUI, Jetpack Compose, Motion et CSS sans changer la sensation, et une checklist de passation.',
     'El 10 de noviembre de 2026 Figma Motion añadió muelles basados en física (masa, rigidez, amortiguación) que se pueden guardar en un sistema de diseño, además de vistas previas de estilos y de exportación Lottie. Por qué un muelle debe ser un token, cómo convertir un mismo muelle para SwiftUI, Jetpack Compose, Motion y CSS sin que cambie la sensación, y una lista de entrega.',
     'Am 10. November 2026 bekam Figma Motion physikbasierte Federn (Masse, Steifigkeit, Dämpfung), die sich im Designsystem speichern lassen, dazu Stil-Vorschauen und Lottie-Exportvorschauen. Warum eine Feder ein Token sein sollte, wie man dieselbe Feder für SwiftUI, Jetpack Compose, Motion und CSS umrechnet, ohne dass sie sich anders anfühlt, und eine Übergabe-Checkliste.'),
 en="""<p>Figma shipped a small Motion bundle on 10 November 2026, and one part of it changes how motion gets handed to engineers. Custom springs in Figma Motion can now be <strong>physics-based</strong>: you set mass, stiffness and damping, and the duration is worked out from them instead of typed in. Figma says you can save that spring in a design system and reuse it. The same release adds <strong>style previews</strong>, so each preset animation plays in the list and on your canvas before you apply it, and <strong>Lottie export previews</strong>, so you can see how an animation will play as a Lottie file before you export it.</p>
<h2>What shipped</h2>
<ul><li><strong>Two kinds of custom spring.</strong> Figma’s help article now offers <em>Time</em> and <em>Physics</em>. A time-based spring takes bounciness and a duration, which is what you want when motion must line up with a sound or a fixed beat. A physics-based spring takes stiffness, damping and mass, and its length follows from those values.</li>
<li><strong>Android has no mass field.</strong> Figma notes that Android springs use stiffness and a damping ratio, with no separate mass, while mass applies to iOS and web.</li>
<li><strong>Physics springs can overrun the timeline.</strong> Because the duration is computed, the motion can finish before or after the next keyframe; a line on the timeline shows where it really ends.</li>
<li><strong>Previews before you commit.</strong> Style previews play presets in place; the Lottie preview shows the exported result before you hand it off.</li>
<li><strong>The API keeps less than you typed.</strong> In Figma’s plugin API a custom spring is stored as a single normalized <code>bounce</code> from 0 to 1, and <code>figma.motion.physicalSpringToNormalized()</code> converts mass, stiffness and damping into it. Figma’s own agent skill notes that reading keyframes back returns only <code>bounce</code>.</li></ul>
<h2>Our take: a spring is a token, and the three numbers are the source of truth</h2>
<p>For years, motion handoff meant “300 ms, ease-out” in a spec and a developer guessing the rest. Springs fix the two things that never survived that handoff: an interruption keeps its velocity instead of jumping, and the feel comes from physics that every platform can reproduce. But a spring is only portable if the numbers travel with it. That last API detail matters. If an agent or plugin reads your file, it gets a normalized bounce, not the mass, stiffness and damping you tuned. So do not let the Figma file be the only place the spring lives. Name it, write the three numbers into your token file next to colour and radius, and treat Figma as one consumer of that token.</p>
<p>The second point is that the platforms do not take the same inputs. SwiftUI and Motion accept mass, stiffness and damping directly. Jetpack Compose takes a damping ratio and a stiffness, and behaves as if the mass were 1. If someone copies “stiffness 300” across without converting, the Android version will feel different. The conversion is simple physics, and it belongs in your tokens so nobody does it by hand:</p>
<ul><li><strong>Damping ratio</strong> ζ = damping ÷ (2 × √(stiffness × mass)). Below 1 it overshoots; 1 settles without overshoot; above 1 creeps in slowly.</li>
<li><strong>Compose</strong>: <code>dampingRatio = ζ</code> and <code>stiffness = stiffness ÷ mass</code>.</li>
<li><strong>Rough settle time</strong> for a spring under 1: about 4 ÷ (ζ × √(stiffness ÷ mass)) seconds. Useful for checking that a “quick” spring is actually quick.</li></ul>
<p>Worked example: a sheet spring of mass 1.2, stiffness 300, damping 26 gives ζ ≈ 0.68, a Compose stiffness of 250, and settles in roughly 0.37 seconds. A button spring of mass 1, stiffness 400, damping 30 gives ζ = 0.75 and settles in about 0.27 seconds. Those are our calculations from the formula, so check the feel on a device, but they show why the numbers, not a duration, are the thing to hand over.</p>
<p>Third, Lottie is not a spring. A Lottie file plays keyframes with easing curves, so the physics is baked in at export and will not respond to an interruption. That is fine for an illustration or a success animation. It is wrong for UI that people drag, dismiss or tap twice. The new Lottie preview is the moment to decide which one you are making.</p>
<h2>Checklist: hand off a spring that feels the same everywhere</h2>
<ol><li><strong>Keep a small set.</strong> Three to five named springs, such as <code>spring.snappy</code>, <code>spring.sheet</code> and <code>spring.bouncy</code>, saved in the Figma design system and mirrored in your token file.</li>
<li><strong>Store mass, stiffness, damping and the derived values.</strong> Add the damping ratio and the Compose stiffness so Android never converts by hand.</li>
<li><strong>Use time-based springs only for synced motion.</strong> Sound, video, a fixed onboarding beat. Everything a person touches gets a physics spring.</li>
<li><strong>Watch the timeline line.</strong> If a physics spring runs past the next keyframe, either let it overlap on purpose or pick a stiffer spring; do not stretch the keyframes to hide it.</li>
<li><strong>Mark what ships as Lottie.</strong> Decorative and celebratory motion can be baked; interactive UI should be built in code with the live spring.</li>
<li><strong>Preview before you apply.</strong> Use style previews on the real frame, in light and dark, not on a placeholder rectangle.</li>
<li><strong>Write the reduced-motion version.</strong> When <code>prefers-reduced-motion</code> is on, swap movement for a short fade or a spring with ζ of 1 and no travel.</li>
<li><strong>Test interruption on a device.</strong> Open and dismiss a sheet halfway through, twice. That is the case springs exist for.</li>
<li><strong>Never use damping 0.</strong> Motion warns that such a spring runs forever; keep a floor in your tokens.</li></ol>
<pre><code># Paste this to your coding agent
Add our motion tokens from tokens/motion.json to the app.
Each spring has mass, stiffness and damping. For every platform:
  SwiftUI: Spring(mass:stiffness:damping:)
  Web (Motion): transition { type: "spring", mass, stiffness, damping }
  Compose: spring(dampingRatio = damping / (2*sqrt(stiffness*mass)),
                  stiffness = stiffness / mass)
Do not replace springs with fixed durations. Use spring.sheet for sheets
and drawers, spring.snappy for buttons and toggles.
Under prefers-reduced-motion, use a 150 ms opacity fade instead.
Test interrupting each animation halfway and list any that jump.</code></pre>
<h2>When a duration is still right</h2>
<p>Keep plain easing and a fixed time for loading indicators, progress, anything synced to media, and CSS-only pages where you cannot ship a spring engine. CSS <code>linear()</code> can approximate a spring curve by sampling it, and Motion can generate that string, but the result has a fixed length and will not carry velocity through an interruption. Use it as a fallback, not as the source.</p>
<p>Related on UI Hub: <a href="../motion-that-feels-right/">motion that feels right</a>, <a href="../motion-pinch-press-gestures-with-fallbacks/">Motion’s pinch and press gestures</a>, and <a href="../design-tokens-for-agents/">design tokens for agents</a>.</p>""",
 zh="""<p>2026 年 11 月 10 日，Figma 发布了一组小小的 Motion 更新，其中一项改变了动效交给工程师的方式。Figma Motion 的自定义弹簧现在可以是<strong>基于物理的</strong>：你设置质量、刚度和阻尼，时长由它们算出来，而不是手动填写。Figma 说这个弹簧可以存进设计系统重复使用。同一次更新还加入了<strong>样式预览</strong>，每个预设动画在应用之前就会在列表里和画布上播放；以及 <strong>Lottie 导出预览</strong>，导出前就能看到动画作为 Lottie 文件播放的效果。</p>
<h2>这次发了什么</h2>
<ul><li><strong>两种自定义弹簧。</strong>Figma 帮助文档现在提供「时间」和「物理」两种。基于时间的弹簧设置弹性和时长，适合需要和音效或固定节拍对齐的动效。基于物理的弹簧设置刚度、阻尼和质量，时长由这些数值决定。</li>
<li><strong>Android 没有质量参数。</strong>Figma 说明 Android 的弹簧使用刚度和阻尼比，没有单独的质量；质量只用于 iOS 和网页。</li>
<li><strong>物理弹簧可能超出时间轴。</strong>因为时长是算出来的，动效可能在下一个关键帧之前或之后结束；时间轴上会有一条线标出它真正结束的位置。</li>
<li><strong>应用前先预览。</strong>样式预览就地播放预设；Lottie 预览在交付前显示导出后的效果。</li>
<li><strong>API 存下的比你填的少。</strong>在 Figma 插件 API 里，自定义弹簧存成一个 0 到 1 的归一化 <code>bounce</code> 值，<code>figma.motion.physicalSpringToNormalized()</code> 负责把质量、刚度、阻尼换算成它。Figma 官方的智能体技能文档写明，读回关键帧时只返回 <code>bounce</code>。</li></ul>
<h2>我们的看法：弹簧是 Token，三个数字才是真相来源</h2>
<p>多年来，动效交付就是规范里写一句「300 毫秒，ease-out」，剩下的让开发去猜。弹簧解决了两件从来交接不过去的事：动画被打断时会保留速度而不是跳变，手感来自每个平台都能复现的物理规律。但只有数字跟着走，弹簧才可移植。上面那条 API 细节很关键：如果智能体或插件读取你的文件，拿到的是归一化的 bounce，而不是你调好的质量、刚度和阻尼。所以别让 Figma 文件成为弹簧唯一存在的地方。给它起名，把三个数字写进 Token 文件，和颜色、圆角放在一起，把 Figma 当作这个 Token 的使用方之一。</p>
<p>第二点是各平台接受的参数不一样。SwiftUI 和 Motion 直接接受质量、刚度和阻尼；Jetpack Compose 接受阻尼比和刚度，表现相当于质量为 1。如果有人不换算就把「刚度 300」照抄过去，Android 版的手感就会不同。换算只是简单的物理，应该写在 Token 里，免得有人手算：</p>
<ul><li><strong>阻尼比</strong> ζ = 阻尼 ÷（2 × √（刚度 × 质量））。小于 1 会过冲；等于 1 不过冲地停下；大于 1 慢慢靠近。</li>
<li><strong>Compose</strong>：<code>dampingRatio = ζ</code>，<code>stiffness = 刚度 ÷ 质量</code>。</li>
<li><strong>大致稳定时间</strong>（ζ 小于 1 时）：约 4 ÷（ζ × √（刚度 ÷ 质量））秒。可以用来核对一个「快」弹簧是不是真的快。</li></ul>
<p>算个例子：抽屉弹簧质量 1.2、刚度 300、阻尼 26，得到 ζ ≈ 0.68，Compose 刚度 250，大约 0.37 秒稳定。按钮弹簧质量 1、刚度 400、阻尼 30，ζ = 0.75，大约 0.27 秒稳定。这些是我们按公式算的，手感仍要在真机上确认，但它说明了为什么要交付的是这些数字，而不是一个时长。</p>
<p>第三，Lottie 不是弹簧。Lottie 文件播放的是带缓动曲线的关键帧，物理效果在导出时就被「烤」死了，不会响应打断。插画或成功动画这样没问题；但对用户会拖动、关闭或连点两下的界面就是错的。新的 Lottie 预览，正是决定你在做哪一种的时刻。</p>
<h2>清单：交付一个在哪里都手感一致的弹簧</h2>
<ol><li><strong>只保留一小组。</strong>三到五个命名弹簧，比如 <code>spring.snappy</code>、<code>spring.sheet</code>、<code>spring.bouncy</code>，存进 Figma 设计系统，并在 Token 文件里同步一份。</li>
<li><strong>存质量、刚度、阻尼和推导值。</strong>加上阻尼比和 Compose 刚度，让 Android 永远不用手算。</li>
<li><strong>只有需要同步的动效才用时间弹簧。</strong>音效、视频、固定节拍的引导页。凡是用户会触碰的，都用物理弹簧。</li>
<li><strong>留意时间轴上那条线。</strong>物理弹簧如果越过下一个关键帧，要么有意让它重叠，要么换一个更硬的弹簧；不要拉长关键帧来掩盖。</li>
<li><strong>标明哪些以 Lottie 交付。</strong>装饰和庆祝类动效可以烤成关键帧；可交互的界面应在代码里用实时弹簧实现。</li>
<li><strong>应用前先预览。</strong>在真实画框上用样式预览，浅色和深色都看，不要在占位矩形上看。</li>
<li><strong>写好减少动效的版本。</strong>开启 <code>prefers-reduced-motion</code> 时，把位移换成短暂淡入淡出，或 ζ 为 1、没有位移的弹簧。</li>
<li><strong>在真机上测打断。</strong>抽屉打开到一半就关掉，来两次。弹簧就是为这种情况存在的。</li>
<li><strong>永远别用阻尼 0。</strong>Motion 文档提醒这种弹簧会无限振荡；在 Token 里设一个下限。</li></ol>
<pre><code># 把这段贴给你的编程智能体
把 tokens/motion.json 里的动效 Token 接入应用。
每个弹簧都有 mass、stiffness、damping。各平台这样用：
  SwiftUI：Spring(mass:stiffness:damping:)
  网页（Motion）：transition { type: "spring", mass, stiffness, damping }
  Compose：spring(dampingRatio = damping / (2*sqrt(stiffness*mass)),
                  stiffness = stiffness / mass)
不要用固定时长替换弹簧。抽屉和底部面板用 spring.sheet，
按钮和开关用 spring.snappy。
开启 prefers-reduced-motion 时改用 150 毫秒的透明度淡入淡出。
每个动画都在进行到一半时打断测试，列出所有出现跳变的地方。</code></pre>
<h2>什么时候仍该用时长</h2>
<p>加载指示、进度条、任何和媒体同步的动效，以及无法引入弹簧引擎的纯 CSS 页面，继续用普通缓动加固定时长。CSS <code>linear()</code> 可以通过采样近似一条弹簧曲线，Motion 也能生成这段字符串，但结果长度固定，打断时不会带上速度。把它当作退路，而不是源头。</p>
<p>UI Hub 相关阅读：<a href="../motion-that-feels-right/">让动效感觉对</a>、<a href="../motion-pinch-press-gestures-with-fallbacks/">Motion 的 pinch 和 press 手势</a>，以及<a href="../design-tokens-for-agents/">给智能体的设计 Token</a>。</p>""",
 refs=[('New Figma Motion updates: physics based springs, style and Lottie export previews (10 Nov 2026)','Figma release notes','https://www.figma.com/release-notes/'),('Adjust an animation’s easing','Figma Learn','https://help.figma.com/hc/en-us/articles/41414048690839-Adjust-an-animation-s-easing'),('Motion (plugin API: MotionEasing, NormalizedSpring, PhysicalSpring)','Figma Developer Docs','https://developers.figma.com/docs/plugins/api/Motion/'),('figma-use-motion: motion-easing.md','figma/mcp-server-guide on GitHub','https://github.com/figma/mcp-server-guide/blob/main/skills/figma-use-motion/references/motion-easing.md'),('How Figma put the bounce in spring animations','Figma Blog','https://www.figma.com/blog/how-we-built-spring-animations/'),('Spring','Apple Developer Documentation','https://developer.apple.com/documentation/swiftui/spring'),('Customize animations (spring)','Android Developers','https://developer.android.com/develop/ui/compose/animation/customize'),('spring','Motion docs','https://motion.dev/docs/spring'),('linear() easing function','MDN Web Docs','https://developer.mozilla.org/en-US/docs/Web/CSS/easing-function/linear'),('prefers-reduced-motion','MDN Web Docs','https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion')]),
]
