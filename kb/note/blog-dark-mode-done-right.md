# Dark mode done right: tokens, elevation and contrast

> Dark mode is a second palette, not an inverted one. Use semantic tokens, lighter surfaces for elevation, and desaturated accents.

Blog post: https://siinxu.github.io/ui-resource-hub/blog/dark-mode-done-right/

Inverting colours gives you pure black backgrounds, glowing saturated blues and shadows nobody can see. Apple's HIG and web.dev both describe dark mode as its own design pass.

## Rules

- **Semantic tokens:** `--bg`, `--surface`, `--ink`, `--accent`, swapped per theme with `[data-theme]` or `prefers-color-scheme`.
- **Elevation by lightness:** raised surfaces get slightly lighter, because shadows barely read on dark.
- **Off-black, off-white:** e.g. #06070b and #f3f5fb reduce halation.
- **Desaturate accents** and re-check 4.5:1 text contrast in both themes.
- Set `color-scheme` so form controls and scrollbars follow.

## Our take

NN/g's research shows preference is split, so ship both and remember the choice. Screenshots of previews need both themes too; UI Hub stores light and dark shots per component for exactly this reason.

## References
- [Dark Mode — Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/dark-mode) — Apple
- [prefers-color-scheme: Hello darkness, my old friend](https://web.dev/articles/prefers-color-scheme) — web.dev (Thomas Steiner)
- [Dark Mode vs. Light Mode: Which Is Better?](https://www.nngroup.com/articles/dark-mode/) — Nielsen Norman Group
- [Dark mode](https://tailwindcss.com/docs/dark-mode) — Tailwind CSS