# Dark mode done right: tokens, elevation and contrast

> Dark mode is a second palette, not an inverted one. Use semantic tokens, lighter surfaces for elevation, and desaturated accents.

Blog post: <https://ui.incidental.site/blog/dark-mode-done-right/>

Inverting colours is the fastest way to ship a bad dark mode: pure black backgrounds, glowing saturated blues, borders that vanish and shadows nobody can see. Apple's Human Interface Guidelines and web.dev both treat dark mode as its own design pass, not a filter. This post covers the token structure that makes two themes cheap, the rules for surfaces, colour and contrast, a step-by-step implementation without the white flash, and what to check before you ship.

## Start from semantic tokens

The single decision that makes dark mode manageable is naming colours by **role**, not by value. Components use `--bg`, `--surface`, `--ink`, `--muted`, `--line` and `--accent`. Each theme assigns values to those roles. A component never knows which theme it is in.

:root, [data-theme=&quot;light&quot;] {
  color-scheme: light;
  --bg: #f5f6fa;  --surface: #ffffff;  --raised: #ffffff;
  --ink: #0a0c14; --muted: #4a5164;    --line: rgb(10 12 20 / .10);
  --accent: #2563eb;
}
[data-theme=&quot;dark&quot;] {
  color-scheme: dark;
  --bg: #06070b;  --surface: #0d0f15;  --raised: #151924;
  --ink: #f3f5fb; --muted: #a6adbf;    --line: rgb(255 255 255 / .10);
  --accent: #67e8f9;
}
.card { background: var(--surface); color: var(--ink); border: 1px solid var(--line); }

If your codebase has `#fff` and `text-gray-900` scattered through components, the first step of a dark mode project is replacing them with roles. Agents are good at this mechanical refactor when you give them the role table.

## Rules for surfaces and colour

- **Off-black, not black.** Pure `#000` behind white text maximises halation (the glow around bright text) on many screens. A very dark blue-grey such as `#06070b` reads as black and is easier on the eyes.

- **Off-white text.** `#f3f5fb` instead of `#ffffff` for body text; reserve pure white for small emphasis if at all.

- **Elevation by lightness.** In light mode, shadows separate layers. In dark mode, shadows barely show, so raised surfaces get slightly 
lighter
: background, then surface, then raised. Material's dark theme guidance uses the same idea.

- **Desaturate and lighten accents.** A saturated `#2563eb` that works on white vibrates on near-black. Pick a lighter, less saturated accent for dark, and check it as text and as a button fill separately.

- **Borders carry more weight.** With weak shadows, a 1px translucent line is often what separates cards from the background.

- **Images and illustrations.** Logos and diagrams with white backgrounds become glaring rectangles. Provide dark variants or put them on a neutral surface.

## Contrast in both themes

WCAG asks for at least 4.5:1 contrast for normal text and 3:1 for large text and UI components. Check muted text, placeholder text, disabled states and links in **both** themes. The usual failure is muted grey that passes on white and fails on near-black, or the reverse.

## Step by step: implementing the switch

**Step 1: respect the system, remember the choice.** Default to `prefers-color-scheme`, let the user override it, and store the override.

**Step 2: set the theme before first paint.** A tiny inline script in `<head>` avoids the white flash on load:

<script>
  try {
    const saved = localStorage.getItem(&quot;theme&quot;);
    const sys = matchMedia(&quot;(prefers-color-scheme: dark)&quot;).matches ? &quot;dark&quot; : &quot;light&quot;;
    document.documentElement.dataset.theme = saved || sys;
  } catch (e) {
    document.documentElement.dataset.theme = &quot;light&quot;;
  }
</script>

**Step 3: set `color-scheme`.** It tells the browser to render form controls, scrollbars and the default canvas in the right theme. Without it you get light scrollbars on a dark page.

**Step 4: consider `light-dark()`.** Modern browsers support the CSS `light-dark()` function, which picks a value based on the active `color-scheme`. It is handy for one-off values: `border-color: light-dark(#e5e7eb, #262a35);`.

**Step 5: wire the toggle.** Update `data-theme`, save the choice, and update `aria-pressed` or the label so screen-reader users know the current state.

## A five-minute dark-mode review

Open the page in dark mode on a real phone at low brightness and on a laptop at full brightness. Look for four things: text that glows or blurs at the edges (too much contrast, often pure white on pure black), cards that disappear into the background (missing border or lightness step), accent colours that vibrate, and any white rectangle (an image, embed or code block that was never themed). Then switch themes with the toggle and reload: the page should come back in the theme you chose, without a flash.

## Pitfalls

- **Inverting with a filter.** `filter: invert(1)` flips photos and brand colours too.

- **Forgetting third-party embeds.** Code blocks, maps, charts and iframes often stay light. Theme them or frame them.

- **Shadows as the only separator.** They disappear in dark mode; add borders or lightness steps.

- **Testing only one theme.** Every screenshot review, visual test and design critique should include both.

- **Theme flash.** Setting the theme in a framework effect after hydration flashes the wrong theme on every load.

## Questions we get

**Should dark mode be the default?** Follow the system setting by default. Users who prefer dark have usually already said so at the operating-system level, and the same goes for light. A manual toggle covers everyone else.

**Do we need a separate dark design in Figma?** You need dark values for every role token and a review of key screens in dark. You do not need to redraw every screen if components use role tokens; the theme swap does the work.

**What about charts and data visualisation?** Chart palettes need their own dark variants. Colours that are distinguishable on white can merge on near-black, so check categorical colours side by side in both themes, and never rely on colour alone to distinguish series.

**How do we keep the two themes from drifting?** Run visual regression screenshots in both themes and fail the build on unexpected changes. Treat a component that looks wrong in one theme as a bug, not a polish item.

**Is "dim" or high-contrast a third theme?** If users need it, yes, and the role-token structure makes it a third column of values. Respect `prefers-contrast` before inventing a custom option.

## Our take

NN/g's research shows preference between dark and light is split and situational, so ship both and remember the choice. The cost of the second theme is almost entirely in the token structure: get roles right and dark mode is a second column of values. UI Hub stores light and dark preview screenshots for each component for exactly this reason; a component that only looks good in one theme is half finished.

## Checklist

- Components use role tokens only; no raw colours

- Off-black background, off-white text, lighter raised surfaces

- Dark-specific accent checked as text and as fill

- 4.5:1 text contrast verified in both themes

- Theme set before first paint; `color-scheme` set

- System preference respected and user override remembered

## References
- [Dark Mode — Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/dark-mode) — Apple
- [prefers-color-scheme: Hello darkness, my old friend](https://web.dev/articles/prefers-color-scheme) — web.dev (Thomas Steiner)
- [Dark Mode vs. Light Mode: Which Is Better?](https://www.nngroup.com/articles/dark-mode/) — Nielsen Norman Group
- [Dark mode](https://tailwindcss.com/docs/dark-mode) — Tailwind CSS
- [color-scheme](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-scheme) — MDN
- [light-dark()](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/light-dark) — MDN
- [Understanding SC 1.4.3 Contrast (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) — W3C WAI
- [Color system overview — Material 3](https://m3.material.io/styles/color/system/overview) — Google
- [prefers-contrast](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-contrast) — MDN