# preview/hero-x3 — SEQUENCE (scroll-driven full-bleed cover sequence)

The library previews were read before any CSS. This file was written up during the build. Hex values are sampled from the preview images.

| # | Library entry (id) | Preview path | Hex | Radius | Shadow | Font | Motion | Used for |
|---|---|---|---|---|---|---|---|---|
| 1 | Akaru (`w16-akaru-fr`) | previews/site/w16-akaru-fr.webp | #f2f1ed / #1c1b22 / #c6d0d9 + #8f8aa0 (blue-grey/violet panes: **tones NOT used**, recomputed warm) | 0 | none | ultra-condensed stretched display wordmark, small centred deck, dotted nav | next-project vertical strips expand | Split panel (chalk left, cover panes right), stretched wordmark, next-cover strips numbered 01–05 |
| 2 | Aceternity Sticky Scroll Reveal (`x16-aceternity-sticky-scroll-reveal`) | previews/site/x16-aceternity-sticky-scroll-reveal.webp | #0f172b / #207475 (navy/teal: not used) | ~6px | none | Inter 600 | content changes as you scroll through a sticky block | Sticky stage + scroll-scrubbed active index |
| 3 | Aceternity Container Scroll Animation (`x16-aceternity-container-scroll-animation`) | previews/site/x16-aceternity-container-scroll-animation.webp | #151722 / #0b0b0c / #3e3f45 | ~24px device | big soft drop | Inter 700 "Scroll Animations" | scroll-linked transform (rotateX→0, scale) | Scroll-linked image transform: scale 1.14→1, parallax -18% of travel |
| 4 | Magic UI Scroll Progress (`cs2-magicui-design--progress--scroll-progress--v0`) | /workspace/ui-hub/previews/cs/cs2-magicui-design--progress--scroll-progress--v0.webp | #ffffff / #f6f6f6 | 12px table | none | mono `className: string` | scaleX bar bound to scroll | 1px progress bar + "01 / 05" counter |
| 5 | AIM Obys (`w16-aim-obys-agency`) | previews/site/w16-aim-obys-agency.webp | #e7e4de / #323231 | 0 | none | grotesk meta row | n/a | Thin top rule, thick bottom rule, meta row |
| 6 | Murmure (`w16-murmure-me`) | previews/site/w16-murmure-me.webp | #111111 / #f8f9f9 | 0 | none | condensed display | n/a | Dark theme: bone wordmark on ink |

## Tokens used
- Light: chalk #f1eee8, ink #121110. Dark: #121110 / #f1eee8. Accent (dot, em, progress): burnt orange #e86a37 (dark) / #c9521f (light).
- Pane tones are each cover's mean colour in HLS: light L .80, S ≤.24; dark L .20, S .12–.26. Any hue in 170–300° is forced to 30°.
- Radius 0. Shadow on the cover image: `0 40px 80px -40px rgba(0,0,0,.55)`.
- Fonts:
  - Wordmark: Anton outlines as an SVG path with `preserveAspectRatio="none"`, stretched to fill the panel the way Akaru does (natural ratio on mobile).
  - Names: Instrument Serif 38–72px.
  - Labels: Geist Mono 10.5px.
- Motion:
  - Over a section of 100svh + 4×55vh, the inner stage is sticky. Each next pane's left clip edge goes from its strip position (W − (n−k)·s) to 0, eased with in-out cubic.
  - The image does translateX(−.18·x) and scale 1.14→1. The outgoing name fades (×2.2).
  - Progress bar scaleX = p.
  - Reduced motion: no scrub (the section collapses to one screen).
- Covers: Grand Matter, THE LINE Studio, Vero, Eladio Dieste, Sophie Dallamore. 800w webp. The first loads eagerly at low priority; the rest load after the first Featured card renders, or on first scroll.
