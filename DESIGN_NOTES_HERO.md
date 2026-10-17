# DESIGN_NOTES — UI Hub hero preview A「画廊线描 / Gallery line-art」

Branch `preview/hero-gallery` · preview only, not for `main`. Written before any CSS.
Scope: ONLY the first screen (`#hero`). Featured + catalog grid below are unchanged
(same markup, same styles.css, same app.js). Rejected A Scène / B Montréal / C Index are not reused.

## References (UI Hub library, real images read)
Primary full-page reference (gold, not flagged): **#327 `lib-component-gallery` — The Component Gallery**
(why in data.json: 「大衬线标题 + 纸感，信息型站点也能有品味」). Component refs (max 2): React Bits Tilted Card (hero effect),
Motion Primitives Tilt (same effect, spring values only).

| # | Image read (path under /workspace/ui-hub/) | Library | hex sampled | radius | shadow | font | motion |
|---|---|---|---|---|---|---|---|
| 1 | previews/lib-component-gallery.webp | The Component Gallery (light) | paper #f7f6f2, rule lines #e0deda, ink #353837, illus fill #c4d2df / #c3cfdb, card #ffffff | header/“View all” pill 6–8px; cards 4px | none — depth comes from an offset solid duplicate (#c4d2df shape shifted ~8px right/down) | large serif display (Instrument-Serif-like, 400, tight -0.01em), humanist sans body | static; grid paper fades radially from centre |
| 2 | previews/theme/lib-component-gallery-d.webp | The Component Gallery (dark) | bg #343132, lines #767474, ink #f5f3ef, illus stays white #fdffff with grey offset | same | same offset-duplicate shadow | same | static |
| 3 | previews/site/lib-component-gallery.webp (catalog cover) | The Component Gallery | same as #1 (cover = site home) | — | — | — | — |
| 4 | previews/cs/cs2-reactbits-dev--card--components-tilted-card--v0.webp | React Bits · Tilted Card | stage #120e16, tooltip pill #6b6b6b on photo | card 15px, tooltip 10px | soft drop only on hover | sans bold caption | 3D tilt following pointer |
| 5 | previews/cs/cs2-reactbits-dev--card--components-tilted-card--v1.webp | React Bits · Tilted Card (props) | — | — | — | — | **Rotate Amplitude 12, Scale on Hover 1.05, Show Tooltip on, Overlay content on** |
| 6 | previews/cs/cs2-motion-primitives-com--card--tilt--v0.webp | Motion Primitives · Tilt (props) | table #ffffff / rule #e5e5e5 | 8px | — | sans | **rotationFactor 15 (default), spring** — we use the React Bits amplitude 12 and a CSS spring-ish ease |
| 7 | previews/cs/cs2-lib-flowbite-com--carousel--components-gallery--v0.webp | Flowbite gallery (looked at, NOT used) | #f3f4f6 | 8px | — | — | rejected: commercial product carousel feel |
| 8 | /tmp/ref5.html → https://skills.incidental.site/preview/5/ | our own Gallery preview (house reference) | #f4f2ec / #d6d2c7 / #2c2c2c / #d8e6f3 | 8px buttons | offset duplicate | Instrument Serif + sans | none |

## Locked tokens (hero band only, scoped under `.hx`)
- Light: paper `#f7f6f2`, grid line `#e6e3dc` (44px squares, radial fade like #1), rule `#e0deda`, ink `#353837`, ink-2 `#5d5a52`, ink-3 `#8a857a`, illus fill `#c4d2df`, mat `#ffffff`.
- Dark (from #2): paper `#343132`, grid `#3f3c3d`, rule `#58544f`, ink `#f5f3ef`, ink-2 `#cfcac0`, ink-3 `#a39d92`, illus fill `#5b6670`, mat `#fbfaf6` (prints keep a white mat, like the white illustrations on dark).
- One accent: none beyond ink (gallery is monochrome + the pale blue illustration fill).
- Radius: print mat 4px, buttons/search 8px (gallery “View all” pill). Chips in the rail 6px.
- Shadow: **offset solid duplicate** `8px 8px 0 var(--fill)` (from #1 illustrations) — no blur shadows, no glow.
- Fonts (max 2): **Instrument Serif** (display, numbers) + **Geist** (body, labels). Both already self-hosted in `fonts/` and preloaded → zero extra font bytes. No CJK webfont; zh titles fall back to system Songti via the existing `--serif` stack.
- Labels: Geist 500 12px, letter-spacing .08em, uppercase (gallery “COMPONENTS / SEARCH” style).

## Layout (first screen)
- Desktop ≥1024: framed band (border-inline rules like #1). Grid `250px | 1fr`.
  - LEFT column = the existing `#chipsBar` (moved, same ids → same renderChips/match logic), internal scroll with fade, plus a “results” jump that mirrors `#meta` text.
  - RIGHT: stats as serif numbers line (gallery “60 components, 95 design systems…”), serif H1 (existing hero_title + em), lede, search; flanked by 3 hand-drawn line illustrations (avatar / bubble / image card — same vocabulary as #1).
  - Bottom of right column: **salon wall** of 7 real covers (data.json gold items with media.js images; thumbs are downscaled copies of `previews/site/*.webp`, nothing invented), white mat + 1px ink frame + offset fill shadow, museum label (No. 0x · name) beneath.
- Mobile <1024: copy first, wall becomes a horizontal snap strip, filter rows (existing horizontal chip rows) after the wall.

## Motion (only one hero effect)
- Hero effect = **React Bits Tilted Card** on wall prints: rotate amplitude 12° (we cap at 10° because prints are small), scale 1.05, tooltip caption follows pointer; ease `cubic-bezier(.23,1,.32,1)` 300ms on leave. Pointer:fine only.
- No entrance animation beyond a 0→1 opacity fade on images when decoded. `prefers-reduced-motion`: tilt + tooltip off, no transitions.

## Perf guardrails
- No new libraries. Hero JS < 2 KB inline, CSS < 7 KB inline. Thumbs 480px webp q62 (~10–20 KB), `width/height` set, `loading=lazy` except first 3, `fetchpriority=low`, `decoding=async`. Rail + wall boxes have fixed sizes → CLS 0 when chips fill after the data bundle.

## Avoid
Purple glow glass, rainbow gradients, murky green, 3D demo scenes, studio-portfolio hero, side drawers, CJK on non-zh pages, new copy without 10-locale strings.

## Revision 2026-10-17 00:22 EDT — user: no blue/purple anywhere
- The #327 illustration fill (#c4d2df, hue ~208°) is **dropped**. Tokens now follow component.gallery's own CSS variables
  (fetched from https://component.gallery/ CSS): bg-primary #f7f5f2 / #343232, bg-secondary #e2dfdb / #4a4846, border #ccc9c5 / #8b8885,
  text #4a4846 / #ccc9c5, highlight #1f1d1d. Offset shadow = #e2dfdb (light) / #4a4846 (dark).
- One warm accent = **#d95151**, the only warm colour in component.gallery's CSS (used for the eyebrow dot, active-chip tick, print hover/focus shadow).
  Text-level accent (links, `--acc`) darkened to #b8423f (light) / lightened to #e27a72 (dark) for 4.5:1.
- Whole page retheme (resource area too, layout untouched): `styles.hx.css` = main `styles.css` passed through `_hero_preview/decolor.py`
  (every colour literal with hue 170–300° → warm neutral of the same lightness, saturated ones → `var(--acc)`) + `tokens-a.css`.
  `.demo` sketches (hsl(var(--h)) rainbow) → grayscale+light sepia; `.vsw` swatches → grayscale. Favicon accent → #d95151.
