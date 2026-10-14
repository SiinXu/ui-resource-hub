"""One-off coverage fill (2026-10-14). URLs verified HTTP 200. Only public, free/open pages; paid tiers marked freemium."""
from hub_lib import append, lib_item as L
R = ['React','开源']
items = [
 L('lib-coss-origin','Origin UI (coss.com/origin)','https://coss.com/origin','大量可直接复制的 shadcn 风格基础组件：输入框、按钮、选择器、日期、表格、时间线等，Tailwind + React，开源',['input','button','select','table','form','nav'],R),
 L('lib-inspira-ui','Inspira UI','https://inspira-ui.com','Vue / Nuxt 版本的动效组件集合，思路与 Aceternity、Magic UI 相近，免费开源',['motion','background','card','button'],['Vue','开源'],vs=('fancy',)),
 L('lib-shadcnblocks','Shadcnblocks','https://www.shadcnblocks.com','基于 shadcn/ui 的落地页区块：Hero、定价、FAQ、页脚等；部分免费，另有付费完整包',['layout'],['React','shadcn'],pricing='freemium'),
 L('lib-tailark','Tailark','https://tailark.com','shadcn 风格的营销页区块：Hero、特性、日志墙、CTA，免费区块可直接复制',['layout'],['React','shadcn'],pricing='freemium'),
 L('lib-kibo-ui','Kibo UI','https://www.kibo-ui.com','shadcn 注册表形式的高级组件：看板、甘特图、日历、代码块、颜色选择器、AI 输入框',['table','editor','input','chat'],R+['shadcn']),
 L('lib-animate-ui','Animate UI','https://animate-ui.com','带动效的 shadcn 风格组件与图标：Motion 驱动的 Tabs、Accordion、按钮、文字特效',['motion','button','tabs'],R+['shadcn'],vs=('fancy',)),
 L('lib-smoothui','Smooth UI','https://smoothui.dev','精致的微交互组件：动态岛、展开卡片、手势按钮，React + Motion',['motion','card','button'],R,vs=('fancy',)),
 L('lib-shadcn-studio','shadcn/studio','https://shadcnstudio.com','shadcn 组件变体与主题生成器，按组件给出大量样式变体，可一键复制',['button','input','card','form'],R+['shadcn'],pricing='freemium'),
 L('lib-prompt-kit','prompt-kit','https://www.prompt-kit.com','专为 AI 应用设计的组件：提示输入框、消息气泡、Markdown 渲染、推理过程、加载态',['chat','input','loader'],R+['shadcn','AI 聊天']),
 L('lib-ai-elements','AI Elements (Vercel AI SDK)','https://ai-sdk.dev/elements','Vercel 官方 AI 界面组件：对话、消息、工具调用、推理、来源引用，基于 shadcn/ui',['chat','loader'],R+['shadcn','AI 聊天']),
 L('lib-assistant-ui','assistant-ui','https://www.assistant-ui.com','开源 React AI 对话组件库：线程、流式输出、附件、工具 UI，可接任意模型',['chat','input'],R+['AI 聊天']),
 L('lib-zag','Zag.js','https://zagjs.com','用状态机实现的无框架 UI 组件逻辑（Ark UI 的底层），React/Vue/Solid/Svelte 通用',['dialog','menu','select','tabs'],['React','Vue','Svelte','开源'],rt=('component-library','a11y')),
 L('lib-ui-layouts','UI Layouts','https://www.ui-layouts.com','React + Tailwind 的布局与动效组件：图片画廊、抽屉、轮播、滚动动效',['layout','motion','dialog'],R,vs=('fancy',)),
 L('lib-cuicui','Cuicui','https://cuicui.day','可复制粘贴的 React 组件与区块，按场景分类，带实时预览',['button','card','layout','input'],R),
 L('lib-watermelon','Watermelon UI','https://www.watermelon.sh','shadcn 风格的动效组件与区块，偏现代营销页',['motion','layout','card'],R+['shadcn'],vs=('fancy',)),
 L('lib-lukacho','Lukacho UI','https://ui.lukacho.com','少而精的高级交互组件：动态卡片、手风琴、悬浮效果',['motion','card'],R,vs=('fancy',)),
 L('lib-neobrutalism','neobrutalism components','https://www.neobrutalism.dev','新粗野主义风格的 shadcn 组件：粗描边、硬阴影、高饱和色',['button','card','input'],R+['shadcn'],vs=('brutal',)),
 L('lib-retroui','RetroUI','https://www.retroui.dev','复古/新粗野风 React 组件库，适合个性化落地页',['button','card','input'],R,vs=('brutal',)),
 L('lib-8bitcn','8bitcn/ui','https://8bitcn.com','像素风 8-bit 版 shadcn 组件，游戏化与复古站点',['button','card','dialog'],R+['shadcn'],vs=('playful',)),
 L('lib-tweakcn','tweakcn','https://tweakcn.com','shadcn/ui 主题可视化编辑器：调色、圆角、字体、阴影，导出 CSS 变量',['input'],R+['shadcn','配色'],type='generator',rt=('theme',)),
 L('lib-jln-themes','shadcn themes (ui.jln.dev)','https://ui.jln.dev','上万套 shadcn/ui 配色主题，可预览后复制 CSS 变量',[],R+['shadcn','配色'],type='generator',rt=('theme',)),
 L('lib-shadcn-io','shadcn.io','https://www.shadcn.io','社区整理的 shadcn 组件、区块、图标与模板目录',['layout','button'],R+['shadcn'],type='collection'),
 L('lib-heroui-components','HeroUI 组件总览（原 NextUI）','https://www.heroui.com','HeroUI（前身 NextUI）：基于 Tailwind 与 React Aria 的漂亮组件库，暗色模式开箱即用',['button','input','card','dialog','table','tabs'],R,vs=('modern',)),
 L('lib-tailwind-plus-blocks','Tailwind Plus UI Blocks（含免费示例）','https://www.tailwindcss.com/plus/ui-blocks','Tailwind 官方区块库（原 Tailwind UI）。完整版付费，官网有部分免费预览',['layout','form','nav','table'],['React','Vue','HTML'],pricing='paid'),
 L('lib-aceternity-components','Aceternity UI 全部组件','https://ui.aceternity.com/components','Aceternity 免费组件全列表：聚光灯、3D 卡片、背景光束、文字生成、浮动导航',['motion','background','card','nav'],R,vs=('fancy',)),
 L('lib-magicui-components','Magic UI 全部组件','https://magicui.design/docs/components','Magic UI 组件全列表：Marquee、Bento Grid、数字滚动、光束、粒子、Dock',['motion','background','card','layout'],R+['shadcn'],vs=('fancy',)),
 L('lib-hover-components','Hover.dev 组件','https://www.hover.dev/components','Hover.dev 动画组件目录：按钮、导航、卡片、Hero；部分免费',['motion','button','nav','card'],['React'],pricing='freemium',vs=('fancy',)),
 L('lib-flowbite-blocks','Flowbite Blocks','https://flowbite.com/blocks/','Flowbite 的 Tailwind 区块：营销页、应用后台、电商；部分免费',['layout','table','form'],['HTML','React','开源'],pricing='freemium'),
 L('lib-shadcn-blocks-official','shadcn/ui Blocks（官方）','https://ui.shadcn.com/blocks','shadcn 官方区块：仪表盘、侧边栏、登录页、日历，CLI 一键安装',['layout','nav','form'],R+['shadcn']),
]
added = append(items)
print('added', len(added), [a['name'] for a in added])
