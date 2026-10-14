# Dark mode

> A second palette, not inversion: off-black base, elevation by lightness, desaturated accent, color-scheme set.

## Rules
- Swap semantic tokens with `[data-theme]` or `prefers-color-scheme`; remember the user's choice.
- Base off-black (#06070b–#121212), text off-white (#f3f5fb); avoid pure #000 / #fff pairs.
- Elevation by lighter surfaces; shadows barely read on dark.
- Desaturate / lighten the accent (e.g. #2563eb light → #67e8f9 dark) and re-check contrast.
- Set `color-scheme: light dark` so form controls and scrollbars follow.
- Previews and screenshots need both themes; never ship a "dark-only" demo without saying so.

## Sources
- [Apple HIG — Dark Mode](https://developer.apple.com/design/human-interface-guidelines/dark-mode)
- [web.dev — prefers-color-scheme](https://web.dev/articles/prefers-color-scheme)
- [NN/g — Dark vs Light mode](https://www.nngroup.com/articles/dark-mode/)