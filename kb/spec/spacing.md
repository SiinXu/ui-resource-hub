# Spacing & layout

> Use one 4/8-based scale, a max content width, and consistent gutters; spacing communicates grouping.

## Rules
- **One scale:** 4, 8, 12, 16, 24, 32, 48, 64, 96 px. No one-off values like 13 or 22.
- **Proximity = grouping:** space inside a group < space between groups (e.g. 8 inside, 24 between).
- **Content width:** body text 60–75 characters; page container 1120–1320 px; side gutters 20 px mobile, 40 px desktop.
- **Grid:** 12 columns desktop, 4 columns mobile; align cards to the same edges as headings and filters.
- **Density:** tools and dashboards can be dense (row height 36–40 px); marketing pages breathe (section padding 64–120 px).
- **No dead space:** a card should not have a large empty middle; size containers to content or fill with real content.

## Tokens
```css
:root{--s1:4px;--s2:8px;--s3:12px;--s4:16px;--s5:24px;--s6:32px;--s7:48px;--s8:64px;--max:1320px;--gut:20px}
@media(min-width:900px){:root{--gut:40px}}
```

## Sources
- [Refactoring UI](https://www.refactoringui.com)
- [Apple HIG — Layout](https://developer.apple.com/design/human-interface-guidelines/layout)
- [Laws of UX — Law of Proximity](https://lawsofux.com/law-of-proximity/)