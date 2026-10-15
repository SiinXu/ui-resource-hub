# Accessibility in AI-generated UI: the checks models skip

> Generated UIs look fine and fail keyboards and screen readers. Start from accessible primitives, then audit against WCAG 2.2.

Blog post: <https://siinxu.github.io/ui-resource-hub/blog/accessibility-in-ai-generated-ui/>

Models optimise for what a screenshot shows. Focus order, accessible names and live regions do not show up in screenshots, so they are the first things to go missing.

## The checks models skip most

- **Clickable divs** instead of `<button>`. Prompt for semantic elements explicitly.
- **Missing focus-visible styles**, often removed with `outline:none`.
- **Icon-only buttons** without `aria-label`.
- **Contrast** of grey-on-grey secondary text (WCAG 1.4.3).
- **Target size**: at least 24×24 CSS px (WCAG 2.2, 2.5.8).
- **Dialogs** without focus trap and Escape. Use the ARIA APG patterns or Radix and React Aria.

## Our take

Make accessibility structural, not a final pass. Generate on top of accessible primitives and add an audit skill (accessibility, web-design-guidelines) to the agent's definition of done.

## References
- [Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/) — W3C
- [ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/) — W3C WAI
- [Radix Primitives introduction](https://www.radix-ui.com/primitives/docs/overview/introduction) — Radix
- [Web Interface Guidelines](https://vercel.com/design/guidelines) — Vercel