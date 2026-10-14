# Mobile & responsive

> Mobile-first layout, 44px touch targets, bottom navigation for primary tabs, safe areas, no horizontal scroll.

## Rules
- Design at 375 px first; breakpoints ~640 / 900 / 1280.
- Touch targets 44×44 px; spacing between targets ≥ 8 px.
- Primary navigation: bottom bar (3–5 items) on mobile; top tabs on desktop.
- Respect `env(safe-area-inset-*)` and use `viewport-fit=cover` only with padding.
- No horizontal scroll except intentional carousels with visible affordance.
- Inputs: 16 px font to avoid iOS zoom; correct `inputmode` / `enterkeyhint`.
- Test on a real device size in both themes.

## Sources
- [Apple HIG — Layout](https://developer.apple.com/design/human-interface-guidelines/layout)
- [Material 3 — Navigation bar](https://m3.material.io/components/navigation-bar/overview)
- [WCAG 2.2 — Target Size](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)