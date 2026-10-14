# Per-post images. type=shot: real screenshot captured by scripts/blog_images.py (credit = site owner). Others: our own diagrams.
def S(url, site, alt_en, alt_zh, **kw): return dict(type='shot', url=url, site=site, alt=dict(en=alt_en, zh=alt_zh), **kw)
def D(kind, title, alt_en, alt_zh, **kw): return dict(type=kind, kind=kind, title=title, alt=dict(en=alt_en, zh=alt_zh), **kw)
IMAGES = {
'ai-assisted-ui-design-workflow': dict(cover=dict(chips=[('Human','Direction'),('AI','Variants'),('Human','Curate'),('Both','Polish')]), inline=[
  S('https://v0.app/','v0 by Vercel','v0 home page: a prompt box for generating UI','v0 首页：用于生成界面的提示输入框'),
  D('flow','Four-pass AI design workflow','Diagram of the four passes: direction, exploration, curation, polish','四遍工作流示意：定方向、铺变体、挑选、打磨',
    steps=[('01 · Human','Direction','Brief, refuse-list, reference, density'),('02 · AI','Exploration','4–6 deliberately different variants'),('03 · Human','Curation','Pick one, name concrete problems'),('04 · AI + Human','Polish','Critique skill, tokens, last 10% by hand')]),
  S('https://www.nngroup.com/articles/ai-design-tools-not-ready/','Nielsen Norman Group','NN/g article on the state of AI UX-design tools','NN/g 关于 AI 设计工具现状的文章')]),
'prompts-for-ui': dict(cover=dict(chips=[('Layout','12-col'),('Tokens','1 accent'),('States','focus · load'),('Avoid','no gradients')]), inline=[
  D('code','Six-slot UI prompt','A six-line UI prompt template: goal, layout, tokens, states, content, avoid','六格 UI 提示词模板：目标、布局、Token、状态、内容、禁止',
    lines=[('Goal','pricing page, 3 tiers, annual toggle'),('Layout','12-col, max 1200px, stack < 900px'),('Tokens','Geist 14/20 · radius 10 · accent #2563eb'),('States','hover · focus-visible · selected · loading'),('Content','real copy, prices 0 / 19 / 49'),('Avoid','text gradients, glass, emoji icons')]),
  S('https://vercel.com/design/guidelines','Vercel','Vercel Web Interface Guidelines page','Vercel 的 Web Interface Guidelines 页面'),
  S('https://interfaces.rauno.me','Rauno Freiberg','Rauno Freiberg’s interface guidelines','Rauno Freiberg 的界面规范页面')]),
'design-to-code-with-ai': dict(cover=dict(chips=[('Input','Tokens'),('Input','Registry'),('Bridge','MCP'),('Output','Your code')]), inline=[
  D('flow','Design-to-code pipeline','Diagram: design file and tokens flow through MCP and a component registry into reusable code','示意：设计稿与 Token 经 MCP 和组件注册表变成可复用代码',
    steps=[('Figma','Auto-layout + variables','Structure the model can read'),('MCP','Context bridge','Exposes frames, tokens, components'),('Registry','Your components','“Button” means your Button'),('Code','PR to review','Check empty/loading/error states')]),
  S('https://www.builder.io/blog/figma-to-code-visual-copilot','Builder.io','Builder.io Visual Copilot announcement','Builder.io Visual Copilot 介绍页'),
  S('https://ui.shadcn.com/docs/registry','shadcn','shadcn/ui registry documentation','shadcn/ui 注册表文档')]),
'taste-and-skills-for-agents': dict(cover=dict(chips=[('Direction','taste-skill'),('Craft','emil-design-eng'),('Audit','impeccable'),('Rules','AGENTS.md')]), inline=[
  S('https://github.com/Leonxlnx/taste-skill','GitHub · Leonxlnx','taste-skill repository on GitHub','GitHub 上的 taste-skill 仓库'),
  D('stack','One skill per role','Diagram of a skill stack: direction, craft, audit, project rules','skill 组合示意：方向、工艺、走查、项目规则',
    steps=[('Direction','frontend-design / taste-skill','Commit to one aesthetic, ban the tells'),('Craft','emil-design-eng','Motion & micro-interaction judgement'),('Audit','impeccable · baseline-ui · web-design-guidelines','Critique after a draft exists'),('Project','AGENTS.md “never” rules','Overrides generic taste')]),
  S('https://github.com/pbakaus/impeccable','GitHub · pbakaus','impeccable repository on GitHub','GitHub 上的 impeccable 仓库')]),
'component-composition': dict(cover=dict(chips=[('Layer 1','Primitives'),('Layer 2','Styled kit'),('Layer 3','Blocks'),('AI edits','Layer 3')]), inline=[
  D('stack','Three composition layers','Diagram of primitives, styled kit and page blocks','三层组合示意：底层原语、样式组件包、页面区块',
    steps=[('Blocks','Pages & sections','Where AI should do most edits'),('Styled kit','Your Button, Dialog, Card','Tailwind + tokens, code you own'),('Primitives','Radix · Ark · React Aria','Behaviour + accessibility, untouched')]),
  S('https://ui.shadcn.com/docs','shadcn','shadcn/ui introduction page','shadcn/ui 介绍页'),
  S('https://www.radix-ui.com/primitives/docs/overview/introduction','Radix / WorkOS','Radix Primitives introduction','Radix Primitives 介绍页')]),
'motion-that-feels-right': dict(cover=dict(chips=[('Small','150–250ms'),('Large','300–400ms'),('Easing','ease-out'),('A11y','reduced motion')]), inline=[
  D('curves','Easing curves','Three easing curves compared: linear, ease-in, ease-out','三种缓动曲线对比：linear、ease-in、ease-out',
    notes=['Mechanical; fine for progress bars','Starts slow, feels laggy on UI entry','Responds instantly, settles softly: default for UI']),
  S('https://emilkowal.ski/ui/great-animations','Emil Kowalski','Emil Kowalski’s “Great Animations” article','Emil Kowalski 的《Great Animations》文章'),
  S('https://www.joshwcomeau.com/animation/css-transitions/','Josh W. Comeau','Josh Comeau’s interactive guide to CSS transitions','Josh Comeau 的 CSS 过渡交互教程')]),
'dark-mode-done-right': dict(cover=dict(chips=[('--bg','#06070b'),('--ink','#f3f5fb'),('Elevation','lighter'),('Contrast','4.5:1')]), inline=[
  D('swatch','Semantic tokens, two palettes','The same card rendered with light and dark semantic tokens','同一张卡片分别用浅色和深色语义 Token 渲染'),
  S('https://developer.apple.com/design/human-interface-guidelines/dark-mode','Apple','Apple Human Interface Guidelines: Dark Mode','Apple 人机界面指南：深色模式'),
  S('https://web.dev/articles/prefers-color-scheme','web.dev (Google)','web.dev article on prefers-color-scheme','web.dev 关于 prefers-color-scheme 的文章')]),
'accessibility-in-ai-generated-ui': dict(cover=dict(chips=[('Semantics','<button>'),('Focus','visible'),('Target','≥ 24px'),('Spec','WCAG 2.2')]), inline=[
  D('checks','Checks models skip','Grid of six accessibility checks AI-generated UIs often miss','AI 生成界面常漏的六项无障碍检查',
    steps=[('Semantics','Real <button>','Not clickable divs'),('Focus','focus-visible ring','Never bare outline:none'),('Names','aria-label','On icon-only buttons'),('Contrast','≥ 4.5:1','WCAG 1.4.3'),('Target','≥ 24×24 px','WCAG 2.5.8'),('Dialogs','Trap + Esc','APG / Radix / React Aria')]),
  S('https://www.w3.org/TR/WCAG22/','W3C','WCAG 2.2 specification','WCAG 2.2 规范'),
  S('https://www.w3.org/WAI/ARIA/apg/','W3C WAI','ARIA Authoring Practices Guide','ARIA 编写实践指南')]),
}
