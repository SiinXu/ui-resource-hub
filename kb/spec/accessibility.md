# Accessibility

> Semantic HTML, visible focus, names for icon buttons, 24px targets, keyboard dialogs, WCAG 2.2 AA.

## Checklist
- Real `<button>`, `<a href>`, `<label>`; headings in order (one h1).
- `:focus-visible` ring on every interactive element; never bare `outline:none`.
- Icon-only buttons have `aria-label`; images have meaningful `alt` (or empty alt if decorative).
- Targets ≥ 24×24 CSS px (WCAG 2.5.8); 44 px recommended on touch.
- Dialogs: focus trap, Esc to close, return focus. Prefer Radix / React Aria / APG patterns.
- Don't convey state by colour alone; announce async results via `aria-live`.
- Test: keyboard only, screen reader smoke test, 200% zoom, reduced motion.

## Sources
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/)
- [Radix Primitives](https://www.radix-ui.com/primitives/docs/overview/introduction)