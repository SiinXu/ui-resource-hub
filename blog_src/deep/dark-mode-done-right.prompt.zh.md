为 <项目> 做一套规范的深色主题，或者走查现有的深色主题。
1. 找出组件里所有裸颜色（hex、rgb、Tailwind 颜色类名）并列出来。提出一张角色表：--bg、--surface、--raised、--ink、--muted、--line、--accent（用到的话再加 danger/success）。
2. 用角色变量替换裸颜色。分别为 [data-theme="light"] 和 [data-theme="dark"] 定义数值，并在两者中设置 color-scheme。
3. 深色数值：近黑背景（不要 #000）、近白文字（不要 #fff）、浮层比背景更亮、强调色更亮且饱和度更低。
4. 在两套主题里检查 WCAG 对比度（文字 4.5:1，大字/界面组件 3:1）：正文、次要文字、占位文字、链接和按钮；输出带比值的表格，并修复不合格项。
5. 在 <head> 加一段内联脚本，在首次绘制前设置 data-theme（优先用已保存的选择，否则用 prefers-color-scheme）；加一个切换按钮，保存选择并更新 aria-pressed。
6. 列出需要深色版本的第三方嵌入、图片和代码块。
不要使用 filter: invert。
