# preview/hero-x1 — TRAIL (image trail of real covers that follows the cursor)

The library previews were read before any CSS. This file was written up during the build. Hex values are sampled from the preview images (PIL quantize). Radius, shadow, font and motion are read off the preview or the entry's own demo.

| # | Library entry (id) | Preview path | Hex | Radius | Shadow | Font | Motion | Used for |
|---|---|---|---|---|---|---|---|---|
| 1 | Codrops (`tympanus-net-codrops`) | /workspace/ui-hub/previews/tympanus-net-codrops.webp | #2f46e2 / #0c274c (blue: **cited only, colour NOT used**) | 0 | none | wide grotesk caps | Codrops "Image Trail" demos: images spawn on a distance threshold, inner image zooms 1.6→1, older ones scale down and fade | The trail mechanic itself (vanilla port, no GSAP) |
| 2 | Murmure (`w16-murmure-me`) | previews/site/w16-murmure-me.webp | #111111 / #f8f9f9 / #381414 | 0 (cards ~0) | none | full-bleed condensed display wordmark | static hero; grid below | Full-width condensed wordmark on ink, bone type |
| 3 | Mosby's Files (`w16-mosbyfiles-com`) | previews/site/w16-mosbyfiles-com.webp | #181818 / #b31c1f / #726d93 (violet: not used) | tabs ~12px; body 0 | none | condensed grotesk caps + serif names + mono micro labels | tab accordion | One hot-red accent on black; mono micro-labels; serif names |
| 4 | p5aholic Experiments (`w16-experiments-p5aholic-me`) | previews/site/w16-experiments-p5aholic-me.webp | #0f0f0f / #6b6b6b / #420b2c | 0 | none | condensed caps index + tiny italic numbers | scroll index | Numbered captions "Nº07" in the trail cards |
| 5 | Aceternity Direction Aware Hover (`cs2-ui-aceternity-com--motion--direction-aware-hover--v0`) | /workspace/ui-hub/previews/cs/cs2-ui-aceternity-com--motion--direction-aware-hover--v0.webp | #ffffff / #4d5145 / #c3cbcc | ~8px | soft | Inter-like | image slides in from the entry direction | Each card enters from the previous cursor point (translate from last → current) |
| 6 | Aceternity Direction Aware Hover, props (`…--v1`) | /workspace/ui-hub/previews/cs/cs2-ui-aceternity-com--motion--direction-aware-hover--v1.webp | #ffffff / #f6f6f6 | 4px chips | none | mono props | n/a | API shape (imageUrl / children / imageClassName), mirrored as card image + caption children |

Also checked: inspiration entry `rd-dxmiccw-puffer-cursor-fashion-editorial` ("Puffer Cursor Fashion"; no preview image on the box) as the fashion-editorial use of a cursor image trail. User refs: 01-murmure.png and fancy-firstscreen/07-codrops-trail.png.

## Tokens used
- Dark: bg #0e0d0c, ink (bone) #ece8e1, ink2 #b8b2a8, ink3 #8b857b. Light: bg #ece8e1, ink #0e0d0c. Accent: vermilion #e5482e (dark) / #cf3a1f (light), hue 9°.
- Radius: 0 everywhere in the hero. The original pill chips above the grid are untouched (999px).
- Shadow: `0 30px 60px -24px rgba(0,0,0,.65)` on trail cards only.
- Fonts: wordmark = Anton glyph outlines baked into an inline SVG path (OFL; no font request, no swap). Deck = Instrument Serif. Micro labels = Geist Mono 10–10.5px, uppercase, +.08em tracking.
- Motion:
  - Spawn every 100px of pointer travel (78px on mobile). Each card animates from the last point to the cursor with scale .55→1 and opacity 0→1 over 1050ms, `cubic-bezier(.16,1,.3,1)`. The inner image zooms 1.6→1 over 1300ms.
  - The card 5 places back fades: scale →.82, 760ms, `cubic-bezier(.7,0,.84,0)`.
  - After 2.6s idle, and on touch, a virtual cursor runs a Lissajous path.
  - Reduced motion: a static 5-card collage.
- Covers: 16 real UI Hub site resources (`previews/site/<id>.webp` re-encoded to 420w webp, about 117 KB total). None contain blue or purple.
