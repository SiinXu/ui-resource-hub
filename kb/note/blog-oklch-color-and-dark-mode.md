# OKLCH colour systems: palettes that survive dark mode

> OKLCH keeps perceived lightness consistent across hues, so you can generate scales and dark themes by math instead of eyeballing. Tailwind v4 uses it by default.

Blog post: <https://siinxu.github.io/ui-resource-hub/blog/oklch-color-and-dark-mode/>

OKLCH is a CSS colour space (CSS Color Level 4) defined by lightness, chroma and hue. Its lightness channel tracks perceived brightness far better than HSL's, so a yellow and a blue at the same L actually look similarly light. Tailwind CSS v4 switched its default palette to OKLCH, and all modern browsers support `oklch()`.

## Building a scale

```
--brand-50:  oklch(97% 0.02 250);
--brand-500: oklch(62% 0.17 250);
--brand-900: oklch(30% 0.09 250);
```

Keep hue fixed, step lightness evenly, and reduce chroma at the extremes, where sRGB screens cannot display high chroma anyway.

## Dark mode by lightness, not inversion

- Surfaces: very low L (around 14–20%) with a hint of the brand hue instead of pure black.

- Text: high L but not 100%, to reduce glare.

- Accent: raise L and lower chroma slightly so it does not vibrate on dark backgrounds.

- Re-check contrast: equal OKLCH lightness differences do not guarantee WCAG ratios, so test with a contrast checker.

## Our take

Give agents colour tokens in OKLCH with light and dark values side by side. It makes "make it darker" or "add a success colour" a predictable edit instead of a guess.

## References
- [oklch()](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/oklch) — MDN
- [OKLCH in CSS: why we moved from RGB and HSL](https://evilmartians.com/chronicles/oklch-in-css-why-quit-rgb-hsl) — Evil Martians
- [OKLCH Color Picker](https://oklch.com/) — oklch.com
- [Tailwind CSS v4.0](https://tailwindcss.com/blog/tailwindcss-v4) — Tailwind Labs
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/) — WebAIM