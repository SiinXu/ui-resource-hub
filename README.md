# UI Hub v3 · 公开 UI 资源聚合

纯静态网站，不需要构建，不依赖 CDN。本站只做公开 UI 资源的聚合与导航，不托管、不转载付费或专有源码。

## 本地打开
`python3 -m http.server 8080`，然后打开 `http://localhost:8080`。

## 每张卡片
- 预览：真实预览（原站 iframe）/ 可嵌入试看（原站允许 frame 时整页加载）/ 原站封面或截图（og:image 或首页截图，版权归原站）/ 自制示意（纯 CSS 画的抽象示意，明确标注，不含原站素材）。卡片右下角按钮：能嵌入就全屏打开原站，不能嵌入就全屏看图（灯箱里也有原站链接和复制按钮）。
- 「在原站预览」：始终打开原站。
- 复制 Prompt：中英双语，要求参考公开设计语言，明确写了不要复制源码、图片、文案和付费素材。
- 复制代码：只有许可已核实为 MIT / Apache-2.0、且官方 README/文档公开了安装命令的库才有（共 34 个），内容只是安装命令或几行官方用法。付费 / 专有 / 许可不明的资源按钮禁用，点按会提示「付费源码请前往原站购买，本站仅聚合公开预览与链接」等原因。

## 文件
- `index.html` / `styles.css` / `app.js`：页面、样式、逻辑
- `i18n.js`：界面文字 8 种语言（zh-CN、en、ja、ko、ms、es、de、fr），右上角切换，存在 localStorage `uihub.lang`。资源名称和中文备注保持原文；指南标题和问题描述已翻译，推荐理由保持中文。
- `legal.js`：每条资源的许可类型、官方片段、npm/GitHub 链接，由 `build_legal.py` 生成（规则写在脚本顶部）
- `data.json` / `data.js`（`build.py`）、`media.js`（`build_media.py`）、`previews/`：同 v2
- `screenshots/v3-*.png`：v3 截图

## 功能
精选大图、全屏试玩/看图、类型和标签筛选、搜索（`/` 聚焦，也能搜许可如 MIT）、详情（预览、Prompt、代码片段及许可说明、原站/npm/GitHub 链接、收藏、自定义标签、同类推荐、所在指南）、调教指南、收藏页、深浅色、多语言。页脚和详情页底部都有声明。

## v3d（2026-10-10）
- 组件样式卡（type=style，266 张）：一张卡 = 一个组件类型 × 一个来源库，预览是该库官方文档公开演示的截图（`previews/cs/`），深链到原站组件文档页；来源库是小标签。抓取脚本在 `/workspace/cap/`（cap.py + spec.py），人工复核后剔除的截图列在 `styles_reject.json`。只存截图，不存源码；复制代码沿用来源库已核实许可的安装命令。构建：`build.py → build_media.py → build_styles.py → build_notes.py`。
- 组件库卡片：原来共用「自制示意」的 106 条换成各自官网首页截图（`previews/_home_shots.txt`）。
- 真实预览 iframe 改为 contain 缩放：整块演示区完整缩进卡片，手机上不再左右裁切。
- 卡面复制按钮收成 26px 小胶囊；窄屏「复制代码」只留图标。

## v3f（2026-10-10）完整官方代码
- `_orig/fetch_full.py`：从官方 GitHub 仓库的文档演示源文件抓原文（PrimeVue / PrimeNG / PrimeReact、Ant Design、NG-ZORRO、TDesign Vue Next、Naive UI、Quasar、Vuetify、shadcn/ui、Arco、HeroUI v3），写 `_orig/fullcode.json`（树缓存 `_orig/full/*.json`，原文缓存 `_orig/full/raw/`）。
- `build_orig.py`：复制代码的「原站原文」按 ① 安装 → ② 配置 → ③ 引入 → ④ 示例 排列，每段注释写官方来源文件；注释行是本站分段标题，代码逐字不改。「聚合站补充」只放原站链接、许可、付费部分说明。
- `build_legal.py`：Prime 系社区版核实为 MIT（LTS / PrimeBlocks 付费，不提供）；HeroUI v3 仓库为 Apache-2.0。
- 卡片和详情显示框架标签（Vue / Angular / React）；Prime 系详情里有「同一演示的其他框架版本」互链。
- 构建顺序：`build_legal.py → _orig/fetch_full.py → build_orig.py`。

## v3h（2026-10-10）资源类型 + 页面样式风格 + 第二批资源
- 新增 187 张卡（`build_ued.py`，数据在 `_ued/items_[a-d].py`，8 语说明人工撰写）：Agent 设计 Skills、大厂 UED / 设计系统（Apple HIG、Material 3、Fluent 2、Polaris、Atlassian、Spectrum、GOV.UK…）、设计教程、组件风格与 Token 规范（DTCG、WCAG、APG、Open UI…）、UI 灵感站与素材、AI Coding × 设计。已和现有卡按 URL 去重（Ant / Arco / Semi / TDesign / Element / Vant / Carbon / Primer 等沿用原卡，只补标签）。
- 每张卡新增两个多选字段：`rt` 资源类型（19 类）、`vs` 页面样式风格（20 种）；首页筛选栏变为「资源类型 / 页面风格 / 按组件找」三行，计数为分面计数，可与搜索、标签、收藏叠加；详情页里的类型 / 风格标签可点击直接筛选。
- 原站原文：`_ued/fetch.py` 抓 GitHub 仓库描述与许可、宽松许可（MIT / Apache-2.0 等）Skill 仓库的 SKILL.md 原文和 README 中的安装命令、其他站点的 meta description，写入 `orig.js`。无许可或非宽松许可的仓库只给描述和链接。
- 封面：网站 / 灵感站 / 设计系统 / 文档类卡片统一用原站首页真实截图（`/workspace/cap/home2.py`，1440×900 首屏缩到 800×500，`previews/site/`，选用清单 `_ued/covers.json`）；拿不到截图（如 X 帖子、Cloudflare 拦截）的新卡用文字卡，不用自制示意。
- 构建顺序：原有流程之后运行 `python3 build_ued.py`（可重复运行）；i18n 增量在 `_ued/i18n_v3h.py`。
