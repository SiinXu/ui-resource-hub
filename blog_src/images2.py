from images import S, D
IMAGES2 = {
'v0-prompt-to-shadcn': dict(cover=dict(chips=[('Input','Brief'),('Stack','shadcn'),('Loop','1 change/turn'),('Out','Your repo')]), inline=[
  S('https://v0.app/','v0 by Vercel','v0 home page with the prompt box','v0 首页与提示输入框'),
  D('code','A v0 brief that works','Prompt template: components, tokens, states, content','有效的 v0 提示模板：组件、Token、状态、内容',lines=[('Components','Card · Tabs · Table (sticky header)'),('Tokens','--radius .5rem · accent #2563eb · Geist'),('States','empty · loading · error · long text'),('Content','real names, real prices'),('Iterate','one change per turn, keep the rest'),('Review','CSS vars, real buttons, focus rings')]),
  S('https://ui.shadcn.com/','shadcn/ui','shadcn/ui home page, the component layer v0 builds on','shadcn/ui 首页，v0 生成代码所用的组件层')]),
'lovable-bolt-prompt-to-app': dict(cover=dict(chips=[('Prompt','Style first'),('Pass 1','Static UI'),('Pass 2','Backend'),('Guard','design.md')]), inline=[
  S('https://bolt.new/','Bolt by StackBlitz','Bolt.new home page','Bolt.new 首页'),
  D('flow','Front-load the look','Workflow: style paragraph, static UI, backend, drift check','流程：风格段落、静态界面、接后端、跑偏检查',steps=[('01','Style brief','palette · type · radius · reference'),('02','Static UI','fake data, approve the look'),('03','Wire backend','auth · DB · integrations'),('04','Drift check','compare each new screen to design.md')]),
  S('https://webcontainers.io/','StackBlitz WebContainers','WebContainers page: Node.js running in the browser','WebContainers 页面：在浏览器里运行 Node.js')]),
'figma-make-and-figma-agent': dict(cover=dict(chips=[('Make','Prompt → proto'),('Agent','GA 6 Oct'),('Context','guidelines.md'),('Team','live canvas')]), inline=[
  S('https://www.figma.com/make/','Figma','Figma Make product page','Figma Make 产品页',dismiss=['[aria-label*="lose"]','button:has-text("Accept all")','button:has-text("Accept")','button:has-text("Allow all")']),
  D('code','What goes in a guideline file','Guideline file outline: tokens, scales, do/don’t, voice, never-list','规范文件提纲：Token、阶梯、该做/不该做、语气、禁止清单',lines=[('Tokens','names + when to use each'),('Scales','space 4/8/12/16/24 · type 1.25'),('Components','do / don’t pairs with links'),('Voice','UI copy tone, sentence case'),('Never','text gradients · emoji icons · centred body'),('Length','short enough to be read')]),
  S('https://www.theverge.com/tech/1004953/figmas-ai-agent-for-product-design-is-now-generally-available','The Verge','The Verge report on the Figma agent reaching general availability','The Verge 关于 Figma 智能体正式可用的报道')]),
'magic-patterns-magicos': dict(cover=dict(chips=[('Canvas','Files'),('Coordinator','Chat'),('Threads','Parallel'),('MCP','Coding agents')]), inline=[
  S('https://www.magicpatterns.com/','Magic Patterns','Magic Patterns home page introducing MagicOS','Magic Patterns 首页介绍 MagicOS'),
  D('stack','How MagicOS is organised','Diagram: canvas, coordinator, threads, sidebar','示意图：画布、协调者、线程、侧栏',steps=[('Canvas','Everything is a file','designs, docs, images, repos, notes'),('Coordinator','The chat you talk to','answers quick questions, spawns threads'),('Threads','One agent per task','run in parallel, report back'),('Sidebar','Status at a glance','working · done · waiting on you')]),
  S('https://www.magicpatterns.com/blog/introducing-magicos','Magic Patterns','Introducing MagicOS announcement post','MagicOS 发布公告')]),
'prompt-to-ui-tools-compared': dict(cover=dict(chips=[('v0','Components'),('Lovable · Bolt','Full-stack'),('Figma Make','Canvas'),('Magic Patterns','Exploration')]), inline=[
  D('checks','Pick by deliverable','Decision grid: which tool for which deliverable','决策网格：哪种交付物用哪个工具',steps=[('v0','Components for a React repo','shadcn/Tailwind output, CLI install'),('Lovable · Bolt','Working full-stack prototype','backend integrations, in-browser dev'),('Figma Make · agent','Next to design files','team guideline files on the canvas'),('Magic Patterns','Many directions at once','MagicOS canvas, MCP to coding agents')]),
  D('flow','Four questions that decide it','Decision flow: keep code, match system, who iterates, where context lives','决策流程：留不留代码、匹不匹配系统、谁迭代、上下文在哪',steps=[('Q1','Keep the code?','throwaway vs merged'),('Q2','Match a system?','import components / guidelines'),('Q3','Who iterates?','designer canvas vs dev repo'),('Q4','Where is context?','file every session can read')]),
  S('https://www.figma.com/make/','Figma','Figma Make page, one of the five tools compared','Figma Make 页面，五个对比工具之一',dismiss=['[aria-label*="lose"]','button:has-text("Accept all")','button:has-text("Accept")','button:has-text("Allow all")'])]),
'aceternity-ui-deep-dive': dict(cover=dict(chips=[('Stack','React · Motion'),('Use','1 effect/page'),('Avoid','animated body'),('A11y','reduced motion')]), inline=[
  S('https://ui.aceternity.com/','Aceternity UI','Aceternity UI home page','Aceternity UI 首页'),
  S('https://ui.aceternity.com/components','Aceternity UI','Aceternity component index','Aceternity 组件目录'),
  D('checks','Spectacle budget','Do and avoid grid for effect components','特效组件的该做与避免',steps=[('Do','One ambient background','grid, dots or a soft spotlight'),('Do','Headline-only text reveal','never on paragraphs'),('Avoid','Three effects per viewport','reads as a demo reel'),('Always','prefers-reduced-motion','wrap effects yourself')])]),
'magic-ui-deep-dive': dict(cover=dict(chips=[('Licence','MIT'),('Install','shadcn CLI'),('Pick','Marquee'),('A11y','Pause > 5s')]), inline=[
  S('https://magicui.design/','Magic UI','Magic UI home page','Magic UI 首页'),
  D('code','Install like shadcn','Commands to add Magic UI components via the shadcn CLI','用 shadcn CLI 添加 Magic UI 组件的命令',lines=[('add','npx shadcn@latest add "https://magicui.design/r/marquee"'),('lands in','components/magicui/marquee.tsx'),('theme','uses your CSS variables'),('motion','transform + opacity only'),('a11y','pause on hover, stop on reduced motion'),('budget','1–2 animated components per page')]),
  S('https://github.com/magicuidesign/magicui','GitHub','Magic UI repository on GitHub (MIT licence)','Magic UI 的 GitHub 仓库（MIT 许可）')]),
'cult-ui-deep-dive': dict(cover=dict(chips=[('Feel','Tactile'),('Motion','Springs'),('Base','shadcn'),('Rule','1 signature')]), inline=[
  S('https://www.cult-ui.com/','Cult UI','Cult UI home page','Cult UI 首页'),
  D('checks','Adopting a personality component','Checklist before adopting a tactile component','采用个性组件前的检查清单',steps=[('Tokens','Map colours and radii','onto your semantic tokens'),('Motion','Share spring settings','one family of motion'),('Keyboard','Visible focus, real roles','custom toggles need ARIA'),('Scope','One signature interaction','let it recur, don’t mix all')]),
  S('https://github.com/nolly-studio/cult-ui','GitHub','Cult UI repository on GitHub','Cult UI 的 GitHub 仓库')]),
'shadcn-blocks-deep-dive': dict(cover=dict(chips=[('Blocks','Sections'),('CLI','npx shadcn add'),('Registry','Publish yours'),('Theme','CSS vars')]), inline=[
  S('https://ui.shadcn.com/blocks','shadcn/ui','shadcn/ui Blocks page','shadcn/ui Blocks 页面'),
  D('flow','Registry pipeline','Diagram: registry JSON to CLI to local source to tokens','示意图：registry JSON → CLI → 本地源码 → Token',steps=[('Registry','JSON items','components · blocks · themes'),('CLI','npx shadcn add','by name or URL'),('Repo','Local source','agent can read and edit'),('Tokens','CSS variables','one edit restyles all')]),
  S('https://ui.shadcn.com/docs/registry','shadcn/ui','shadcn registry documentation','shadcn registry 文档')]),
'typography-for-ai-generated-ui': dict(cover=dict(chips=[('Scale','1.25'),('Pair','Serif + Sans'),('Track','−0.02em'),('Measure','65ch')]), inline=[
  D('stack','Modular type scale (1.25)','Type scale steps from caption to display','从说明文字到展示标题的字号阶梯',steps=[('display · 61px','Instrument Serif, −0.02em','one per page'),('h1 · 49px','tight tracking','clamp() on mobile'),('h2 · 31px','section headings','text-wrap: balance'),('body · 16px','Geist / system sans','max-width 65ch'),('caption · 13px','muted colour','never below 12px')]),
  S('https://utopia.fyi/type/calculator/','Utopia','Utopia fluid type scale calculator','Utopia 流式字号计算器'),
  S('https://practicaltypography.com/line-length.html','Practical Typography','Practical Typography on line length','Practical Typography 关于行长的章节')]),
'oklch-color-and-dark-mode': dict(cover=dict(chips=[('L','Lightness'),('C','Chroma'),('H','Hue'),('Dark','by L')]), inline=[
  S('https://oklch.com/','oklch.com','OKLCH colour picker','OKLCH 颜色选择器'),
  D('swatch','Light and dark tokens','Light and dark theme token swatches','亮色与暗色主题 Token 色块'),
  S('https://evilmartians.com/chronicles/oklch-in-css-why-quit-rgb-hsl','Evil Martians','Evil Martians article on OKLCH in CSS','Evil Martians 关于 CSS 中 OKLCH 的文章')]),
'landing-page-teardown-linear-vercel': dict(cover=dict(chips=[('Hero','1 sentence'),('Image','Real product'),('Colour','Restraint'),('Proof','Right after')]), inline=[
  S('https://linear.app/','Linear','Linear homepage hero','Linear 首页首屏'),
  S('https://vercel.com/','Vercel','Vercel homepage hero','Vercel 首页首屏'),
  D('checks','Landing page checklist','Four checks for a landing page','落地页四项检查',steps=[('5 seconds','Can a stranger say what you sell?','one sentence of positioning'),('Image','Is the first image your product?','real UI over illustration'),('CTA','Exactly one primary action?','accent reserved for it'),('Sections','One claim each, proven?','heading + demonstrating visual')])]),
'dashboard-design-patterns': dict(cover=dict(chips=[('L1','Is it OK?'),('L2','What changed?'),('L3','Why?'),('Nums','tabular')]), inline=[
  D('stack','Three dashboard layers','Dashboard layers: KPI strip, primary chart, drill-down table','仪表盘三层：指标条、主图、下钻表格',steps=[('Is it OK?','KPI strip','3–5 numbers, period + direction'),('What changed?','Primary time series','range selector, annotations'),('Why?','Drill-down table','sort, filter, tabular-nums')]),
  S('https://ui.shadcn.com/charts','shadcn/ui','shadcn/ui charts page (built on Recharts)','shadcn/ui 图表页（基于 Recharts）'),
  S('https://tremor.so/','Tremor','Tremor dashboard components site','Tremor 仪表盘组件网站')]),
'design-tokens-for-agents': dict(cover=dict(chips=[('Format','DTCG JSON'),('Tier','Semantic'),('Ship','CSS vars'),('Lint','no raw hex')]), inline=[
  D('stack','Three tiers of tokens','Token tiers: primitive, semantic, component','Token 三层：基础、语义、组件',steps=[('Primitive','blue-500 · space-4','raw values'),('Semantic','surface · text-muted · accent','what agents should use'),('Component','button-radius','optional overrides')]),
  S('https://www.designtokens.org/','Design Tokens Community Group','Design Tokens Community Group site','设计 Token 社区组网站'),
  S('https://styledictionary.com/','Style Dictionary','Style Dictionary site','Style Dictionary 网站')]),
'claude-cursor-design-skills': dict(cover=dict(chips=[('Claude','SKILL.md'),('Cursor','rules'),('Any agent','AGENTS.md'),('Must','verify')]), inline=[
  S('https://github.com/anthropics/skills','GitHub','anthropics/skills repository','anthropics/skills 仓库'),
  D('code','Anatomy of a design skill','SKILL.md template: front matter, tokens, bans, verification','SKILL.md 模板：元数据、Token、禁令、验证',lines=[('name','house-ui'),('description','Use when creating or restyling web UI'),('tokens','styles/tokens.css, never hard-code'),('type','Instrument Serif + Geist, 1.25'),('never','text gradients · emoji icons · glass'),('verify','390/1440 · light/dark · focus')]),
  S('https://agents.md/','agents.md','AGENTS.md convention site','AGENTS.md 约定网站')]),
'weekly-roundup-2026-w42': dict(cover=dict(chips=[('6 Oct','Figma agent'),('8 Oct','Lovable'),('13 Oct','MagicOS'),('Chrome','HTML-in-Canvas')]), inline=[
  S('https://www.magicpatterns.com/blog/introducing-magicos','Magic Patterns','MagicOS launch post','MagicOS 发布文章'),
  D('flow','This week in design tools','Timeline: Figma agent GA, Lovable change, MagicOS launch','时间线：Figma 智能体正式可用、Lovable 改动、MagicOS 发布',steps=[('6 Oct','Figma agent GA','guideline files, live canvas'),('8 Oct','Lovable','look from prompt, 9 connectors'),('13 Oct','MagicOS','canvas + parallel threads'),('Takeaway','Write the file','context outlives the chat')]),
  S('https://artdirectiondaily.com/issues/2026-10-12-lovable-cut-pick-look-step.html','Art Direction Daily','Art Direction Daily issue on the Lovable change','Art Direction Daily 关于 Lovable 改动的一期')]),
'tutorial-agent-builds-landing-with-ui-hub': dict(cover=dict(chips=[('1','AGENTS.md'),('2','/kb/ search'),('3','components'),('6','verify')]), inline=[
  S('https://siinxu.github.io/ui-resource-hub/agents/','UI Hub','UI Hub Agents guide page','UI Hub 的 Agent 指南页'),
  D('flow','The six-step loop','Six-step loop: guide, search, pick, skills, build, verify','六步循环：指南、搜索、挑选、技能、构建、验证',steps=[('1–2','Guide + search','AGENTS.md, /kb/?q='),('3','Pick','resources.json by licence'),('4–5','Skills + build','tokens, one effect'),('6','Verify','390/1440, light/dark')]),
  S('https://siinxu.github.io/ui-resource-hub/kb/','UI Hub','UI Hub design encyclopedia','UI Hub 设计百科')]),
'claude-design-everywhere': dict(cover=dict(chips=[('8 Oct','Out of beta'),('Design','Every chat'),('Dashboards','Paid beta'),('14 Dec','Standalone ends')]), inline=[
  S('https://claude.com/product/design','Anthropic','Claude Design product page: design inside every Claude conversation','Claude Design 产品页：在每场 Claude 对话里做设计',dismiss=['button:has-text("Accept")','button:has-text("Accept all")','button:has-text("Got it")','[aria-label*="lose"]','button:has-text("Dismiss")']),
  D('flow','From chat to shippable UI','Flow: migrate system, brief in chat, refine on canvas, hand off','流程：迁移系统、对话写需求、画布打磨、交接',steps=[('01','Migrate','design systems → Artifacts'),('02','Brief','chat + /design-sync'),('03','Refine','comments · canvas'),('04','Ship','Code / connectors')]),
  S('https://claude.com/resources/articles/dashboards-and-motion','Anthropic','Anthropic announcement: Dashboards and Motion beta, Design out of beta','Anthropic 公告：Dashboards 与 Motion 测试版，Design 退出测试',dismiss=['button:has-text("Accept")','button:has-text("Accept all")','button:has-text("Got it")','[aria-label*="lose"]'])]),
'figma-code-layers-and-specs': dict(cover=dict(chips=[('Code layers','Open beta'),('Specs','Markdown'),('Guidelines','On libraries'),('MCP','+20 partners')]), inline=[
  S('https://www.figma.com/blog/build-by-design/','Figma','Figma blog: Build by design, the Config India 2026 launch recap','Figma 博客：Build by design，Config India 2026 发布汇总',dismiss=['[aria-label*="lose"]','button:has-text("Accept all")','button:has-text("Accept")','button:has-text("Allow all")']),
  S('https://www.figma.com/blog/introducing-figma-specs/','Figma','Figma’s Specs announcement: why Markdown needs a shared, multiplayer home','Figma 的 Specs 公告：为什么 Markdown 需要一个共享的多人协作位置',dismiss=['button:has-text("Do not allow")','[aria-label*="lose"]','button:has-text("Accept all")'],scroll=1500),
  D('flow','From spec to reviewed code layer','Flow: write a spec, attach library guidelines, build a code layer via MCP, review on canvas','流程：写 Spec、给组件库挂规范、经 MCP 生成代码图层、在画布上验收',steps=[('01','Spec','tokens · states · never-list'),('02','Guidelines','on the published library'),('03','Code layer','frames · repo · MCP'),('04','Review','empty · loading · error · a11y')])]),
'shadcn-trace-and-ai-elements': dict(cover=dict(chips=[('Trace','1 line / step'),('Code Block','size sm'),('AI Elements','21 patterns'),('Status','in the title')]), inline=[
  S('https://ui.shadcn.com/docs/changelog/2026-10-ai-elements','shadcn/ui','shadcn/ui changelog: Trace, Code Block and AI Elements, with a live Trace demo','shadcn/ui 更新日志：Trace、Code Block 与 AI Elements，附 Trace 实时演示',captured='2026-10-16',scroll=420),
  D('stack','Anatomy of an agentic interface','Diagram: Message Scroller holds turns, Message holds Bubble and Trace, Trace lines hold Code Block output, Confirmation sits outside','示意图：Message Scroller 承载各轮，Message 包含 Bubble 与 Trace，Trace 行内放 Code Block 输出，Confirmation 位于 Trace 之外',steps=[('Scroller + Message','The thread, one turn each','anchors turns · Bubble for the person'),('Trace','Steps inside the turn','icon · title · status · opens'),('Code Block sm','Output of a step','commands · logs · diffs'),('Confirmation','A prompt, not activity','Deny / Approve, then a Tool line')]),
  S('https://ui.shadcn.com/docs/ai-elements','shadcn/ui','AI Elements index: 21 copy-in patterns from Chain of Thought to Tool','AI Elements 目录：从 Chain of Thought 到 Tool 的 21 个可复制模式',captured='2026-10-16',scroll=380)]),
}
