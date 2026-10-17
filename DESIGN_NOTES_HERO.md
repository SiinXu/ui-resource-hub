# DESIGN_NOTES — UI Hub hero preview B「黑白拼贴 / B&W collage masonry」

Branch `preview/hero-collage` · preview only, not for `main`. Written before any CSS.
Scope: ONLY the first screen (`#hero`). Featured + catalog grid below unchanged. Rejected A/B/C themes not reused.

## References (UI Hub library, real images read)
Primary full-page reference (gold, not flagged): **#183 `cs2-reactbits-dev--layout--components-masonry--v0` — React Bits · Masonry**.
Component ref (max 2): React Bits Spotlight Card (surface + chip tokens only, its effect is NOT used — one hero effect rule).

| # | Image read (path under /workspace/ui-hub/) | Library | hex sampled | radius | shadow | font | motion |
|---|---|---|---|---|---|---|---|
| 1 | previews/cs/cs2-reactbits-dev--layout--components-masonry--v0.webp | React Bits · Masonry | stage #120e16, frame line #19151d, photos full grayscale | tiles ~8px, frame 14px | none | — | masonry columns, varied heights |
| 2 | previews/cs/cs2-reactbits-dev--layout--components-masonry--v1.webp | React Bits · Masonry (props) | control #1a1a1f | 8px | — | sans 13px | **Ease power3.out, Animate From Bottom, Duration 0.6s, Stagger 0.05s, Scale on Hover ON, Blur to Focus ON, Color Shift on Hover** |
| 3 | previews/cs/cs2-reactbits-dev--card--components-spotlight-card--v0.webp | React Bits · Spotlight Card | card #111111, chip #232323/#c6c6c6 text, muted #454545 | card 24px, chips 999px, button 999px | none | sans 600 | (spotlight — not used) |
| 4 | previews/cs/cs2-reactbits-dev--card--components-spotlight-card--v1.webp | Spotlight Card (props) | spotlight #ffffff intensity .15 | — | — | — | not used |
| 5 | previews/cs/cs2-reactbits-dev--card--components-tilted-card--v0.webp | React Bits · Tilted Card | B&W photo, tooltip #6b6b6b | 15px | — | sans 700 caption | not used (A uses it) |
| 6 | previews/reactbits-dev.webp | React Bits site | violet #5b2a86 haze | — | glow | pixel display | **rejected for us: purple glow** |
| 7 | /tmp/ref6.html → https://skills.incidental.site/preview/6/ | our own Masonry preview (house ref) | #0b0b0b / #171717 / #f2f2f2 / #bdbdbd | tiles 10–12px, pills 999px | none | Geist-like 800 display + mono label | columns drift |

## Locked tokens (hero band only, `.hx`)
- Dark: stage `#0b0b0b` (#1 stage #120e16 neutralised — brief bans purple tint), tile bg `#171717`, rule `#222222`, ink `#f2f2f2`, ink-2 `#bdbdbd`, ink-3 `#8a8a8a`, chip `#171717`/on `#f2f2f2`.
- Light: stage `#f2f2f0`, tile bg `#e4e4e2`, rule `#d9d9d6`, ink `#0b0b0b`, ink-2 `#454545`, ink-3 `#6b6b6b`; photos stay grayscale (it is the concept).
- One accent: none — colour only appears from the real covers on hover (the “colour shift” of #2).
- Radius: tiles 10px, wall frame 14px, pills 999px (from #3).
- Shadow: none (flat, like #1). Caption scrim `linear-gradient(transparent, rgba(0,0,0,.85))`.
- Fonts (max 2): **Geist** (800 display, -0.035em; body 400) + **Geist Mono** (eyebrow/labels). Both already in `fonts/` (Geist preloaded). No CJK webfont.

## Layout
- Desktop ≥1024: grid `240px | minmax(0,5fr) | minmax(0,6fr)`, band height min(82vh,720px).
  LEFT = existing `#chipsBar` (moved, same ids/logic), internal scroll; middle = mono eyebrow, H1 800, lede, pill search, stats; right = masonry wall of 12 real covers (gold items with media.js images, downscaled copies only), 3 columns, top/bottom fade mask.
- Mobile: copy → 2-col masonry (6 tiles, fixed 400px) → existing horizontal filter rows.

## Motion (one hero effect)
- Hero effect = **React Bits Masonry hover**: grayscale(1)→grayscale(0) colour reveal + scale .97 (hoverScale), caption slides up; 0.6s `cubic-bezier(.215,.61,.355,1)` (power3.out).
- Entrance = Masonry “blur to focus, from bottom”, 0.6s, stagger 0.05s (same component, its own entrance — not a second effect). Runs once, transform/filter only.
- `prefers-reduced-motion`: no entrance, no scale; colour reveal still instant on hover/focus.

## Perf guardrails
No libraries; inline CSS < 7 KB, JS < 1.5 KB; 12 thumbs 400px webp q60, width/height set, first 6 eager+low priority, rest lazy. Fixed wall/rail boxes → CLS 0.

## Avoid
Purple tint/glow, rainbow, murky green, column auto-scroll marquee (extra motion), 3D, studio-portfolio look, drawers, CJK on non-zh.
