# Typography

> Two families max, a modular type scale, tight display tracking, comfortable body leading, tabular numbers for data.

## Rules
- **Families:** one sans for UI (e.g. Geist, Inter), optionally one display serif (e.g. Instrument Serif) for headlines. Mono for code/data labels.
- **Scale:** 12 / 13 / 14 / 16 / 20 / 24 / 32 / 48 / 64. UI body 14–16 px, line-height 1.5–1.65.
- **Display:** large headings line-height 1.0–1.15 and letter-spacing −0.01 to −0.02em.
- **Hierarchy with weight and colour, not only size:** secondary text uses a muted ink token, not a smaller font.
- **Numbers:** `font-variant-numeric: tabular-nums` for prices, tables, counters.
- **CJK:** add PingFang SC / Noto Sans CJK fallbacks; avoid letter-spacing on CJK body text.
- **Line length:** 60–75ch for reading text.

## Sources
- [Refactoring UI](https://www.refactoringui.com)
- [Web Interface Guidelines (Vercel)](https://vercel.com/design/guidelines)
- [Material 3 typography](https://m3.material.io/styles/typography/overview)