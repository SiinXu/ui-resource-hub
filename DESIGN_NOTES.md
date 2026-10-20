# preview/hero-x2 — INDEX (giant wordmark + hover reveal, editorial name index)

The library previews were read before any CSS. This file was written up during the build. Hex values are sampled from the preview images.

| # | Library entry (id) | Preview path | Hex | Radius | Shadow | Font | Motion | Used for |
|---|---|---|---|---|---|---|---|---|
| 1 | Artworld (`w16-artworld-agency`) | previews/site/w16-artworld-agency.webp | #ffffff / #000000 / #a6a6a6 | 0 | none | high-contrast serif names, alternating italics, tiny superscript tags; ultra-black grotesk wordmark | hover on names | Centred inline name index with "(01)" superscripts, alternating italics, giant black wordmark at the bottom |
| 2 | AIM Obys (`w16-aim-obys-agency`) | previews/site/w16-aim-obys-agency.webp | #e7e4de / #323231 | 0 | none | heavy display wordmark + neue-grotesk deck "AIM— AI Modernism" | scroll | Paper #e7e4de, ink-only palette, thick rule + meta row, grotesk deck h1 |
| 3 | Aceternity Text Hover Effect (`cs2-ui-aceternity-com--motion--text-hover-effect--v0`) | /workspace/ui-hub/previews/cs/cs2-ui-aceternity-com--motion--text-hover-effect--v0.webp | #ffffff / #f6f6f6 | 4px chips | none | mono props: `text: string`, `duration: number` | radial-gradient mask follows the cursor inside SVG text | Radial `<mask>` that follows the cursor inside the UI HUB glyphs and reveals a cover (vanilla SVG port) |
| 4 | Aceternity Direction Aware Hover (`…direction-aware-hover--v0`) | /workspace/ui-hub/previews/cs/cs2-ui-aceternity-com--motion--direction-aware-hover--v0.webp | #ffffff / #4d5145 | ~8px | soft | Inter-like | slide-in by direction | Floating cover that lags the cursor with velocity tilt (±8°) |
| 5 | Aceternity Direction Aware Hover props (`…--v1`) | /workspace/ui-hub/previews/cs/cs2-ui-aceternity-com--motion--direction-aware-hover--v1.webp | #ffffff / #f6f6f6 | 4px | none | mono | n/a | imageUrl/children API mirrored by data-src on each name |
| 6 | p5aholic Experiments (`w16-experiments-p5aholic-me`) | previews/site/w16-experiments-p5aholic-me.webp | #0f0f0f / #6b6b6b | 0 | none | condensed index + italic numbers | hover index | Index-as-navigation idea: hovering a row dims the others |

## Tokens used
- Light: paper #e7e4de, ink #111110. Dark: #111110 / #e7e4de. Accent = ink (zero hue in the hero chrome).
- Radius 0. Shadow only on the floating cover: `0 30px 60px -24px rgba(0,0,0,.55)`.
- Fonts:
  - Wordmark: Geist at wght 900, instanced from the repo's variable `fonts/geist.woff2` and baked to an SVG path (tracking -.055em).
  - Index: Instrument Serif through a `font-display:block` alias `hxS`, so the font swap causes no re-wrap or CLS.
  - Deck: Geist 600 with a -.04em tracking plus a serif italic em.
  - Meta: Geist 10.5px.
- Motion:
  - Hovering a name sets the mask radius to full, crossfades the cover in the letters (.6s) and dims the other names to .18 (.45s, `cubic-bezier(.16,1,.3,1)`).
  - Hovering the wordmark gives a radius 0.8×cap-height circle that follows the cursor (lerp .12).
  - Idle and touch: auto-cycle every 2.6s, with a circular wipe from a random point in the wordmark.
  - Reduced motion: static full fill.
- Covers: 7 real resources (Marfala, The New Industrials, DRĄSA, Dead North, Pasqua Wines, Carrière scène, Bureau for Visual Affairs), 800w webp, about 130 KB. They load only after the first Featured card renders.
