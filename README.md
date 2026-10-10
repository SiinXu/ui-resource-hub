# UI Hub v2 · 精华组件展

纯静态网站，不需要构建，不依赖 CDN。字体（Geist / Geist Mono / Instrument Serif，均为 OFL 协议）打包在 `fonts/` 里，中文使用系统字体。

## 本地打开
- 运行 `python3 -m http.server 8080`，然后打开 `http://localhost:8080`。也可以直接双击 `index.html`，但「真实预览」需要联网才能加载原站。
- 没有部署。

## 预览分三种（页面上都有标注）
- **真实预览**（绿色标签）：用 iframe 嵌入原站页面，裁出演示区域，能直接上手操作。首页一共 5 个：Liquid Metal、Libraries.dev Voice（详情页可以切换 7 个效果）、Thinking Orbs、Border Beam、Paper Shaders 液态金属。Orbs 和 Border Beam 的旧域名已经跳到 libraries.dev，所以嵌入的是新地址。卡片进入屏幕时才加载，离开屏幕后卸载。手机上点卡片会全屏试玩。
- **可嵌入试看**（紫色标签）：原站允许被嵌入（curl 检查过 X-Frame-Options 和 CSP frame-ancestors），在详情页点「在这里加载原站页面」，就会缩小显示原站。
- **原站封面 / 原站截图**：原站的 og:image 社交分享图，或者用无头 Chrome 截的首页图，保存在 `previews/`，版权归原站所有。不允许嵌入的站只显示图片，并提供「在原站预览」按钮。
- 没有使用 CSS 仿制的「示意」效果。所有动态画面都来自原站本身。

## 文件
- `index.html` / `styles.css` / `app.js`：页面、样式和逻辑。精选列表 `FEAT` 和裁剪参数写在 app.js 顶部
- `data.json` / `data.js`：142 条资源和 6 篇指南（内容没有改动），由 `build.py` 生成
- `media.js`：每条资源的预览图路径，以及能不能嵌入，由 `build_media.py` 根据 `_probe/probe.json` 和 `previews/` 生成
- `previews/*.webp`：预览图。`live-*.webp` 是真实预览加载出来之前显示的截图
- `_probe/`：探测脚本、探测结果和原始截图
- `screenshots/v2-*.png`：v2 截图

## 功能
精选大图（手机上横滑，桌面上是 bento 布局）、全屏试玩、按类型和标签筛选、搜索（按 `/` 聚焦）、详情（大图预览、复制 AI 提示词、复制链接、收藏、自定义标签、同类推荐、所在指南）、调教指南、收藏页、深色模式（默认）和浅色模式。收藏、标签和主题保存在 localStorage，只存在当前设备上。
