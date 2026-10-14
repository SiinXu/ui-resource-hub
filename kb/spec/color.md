# Colour

> Neutral base + one accent; semantic tokens; check contrast in both themes; gradients only as accents.

## Rules
- **Palette:** a neutral ramp (bg, surface, mat, line, ink, ink2, ink3) + ONE accent + status colours (success/warn/danger).
- **Semantic tokens**, never raw hex in components: `--bg --surface --ink --ink2 --accent --line`.
- **Contrast:** text ≥ 4.5:1, large text and UI glyphs ≥ 3:1 (WCAG 1.4.3 / 1.4.11) in light AND dark.
- **Gradients:** restrained: a sheen on one headline word or a 1px border, not full rainbow backgrounds.
- **Avoid:** muddy mid-tones, two competing accents, saturated blue on pure black.

## Sources
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [Material 3 colour](https://m3.material.io/styles/color/system/overview)
- [Tailwind CSS colours](https://tailwindcss.com/docs/colors)