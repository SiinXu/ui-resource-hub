# UI Hub — v5 Fancy Restore (2026-10-10)

v4 layout is kept 1:1 (shared 1320 max-width + 20/40 gutters, equal-height cards, 2-line notes, pinned actions, `.more` spacing untouched). v5 only changes colour, light, depth and motion — appended as the "v5 FANCY LAYER" and "v5 THEME-AWARE PREVIEWS" blocks at the end of styles.css.

## Palette: Midnight Ink + Electric Cyan, aurora sheen
Studied: Aceternity UI, Magic UI, React Bits, Beautiful UI, Originkit, Cult UI, Motion, 21st.dev (previews/).
- Dark (default): ink `#06070b` / surface `#0d0f15` / mat `#10131a`; text `#f3f5fb · #a6adbf · #687086`.
- Accent: electric cyan `#67e8f9`; sheen gradient cyan → periwinkle `#a5b4fc` → rose `#f9a8d4`, used only on edges, numbers, the italic headline word, active tab bar and focus — never as a fill. Gold `#fcd34d` for saved stars.
- Light: cool white `#f5f6fa`, ink `#0a0c14`, accent `#2563eb`, sheen `#06b6d4 → #6366f1 → #ec4899`.
- Why: the fancy libs in the catalog are near-black stages where the component itself is the light source; one luminous accent + a thin multi-hue edge reads premium. Black+orange read as a warning palette and fought every thumbnail; purple fills read as generic AI.

## Richness
Ambient aurora + masked dot field; Aceternity-style spotlight beam in the hero; Geist 650 display with gradient serif italic; glass eyebrow pill; gradient-bordered search; gradient stat numbers; cards with pointer-tracked spotlight + gradient border on hover and thumb lift/zoom; pill chips with glow on active; glass media tags; luminous mesh covers for text-only resources; drawer with aurora header + gradient top edge; glass tab bar with glowing active indicator; gradient-bordered toast.

## Theme-aware previews
- Sketches (`.demo`): restyled for light and dark.
- 64 key sites (featured + library homepages): real light AND dark captures (`prefers-color-scheme` emulation, `build_theme.py`), swapped with the site theme; drawer has a Light/Dark switch.
- Every other screenshot is tagged `tone` (l/d by luminance). Never tinted. A small sun/moon chip appears on the card only when the shot's theme differs from the site theme; the drawer states "only a light/dark screenshot exists".
- Live iframes: get `color-scheme` + `postMessage({type:'theme'})` on load and on toggle for demos that listen. Cross-origin iframes can't be forced (Chrome ignores the embedder's color-scheme), so libraries.dev / metal are badged "Dark-only demo" and Paper Shaders "Follows system theme".

---

# UI Hub — Visual Rebuild Brief (v4, 2026-10-10)

## What we studied (screenshots in /workspace/rebuild/ref-*.png)
| Reference | Takeaway we adopt |
|---|---|
| **Mobbin** (sites gallery) | The *mat*: each thumbnail sits inset on a soft neutral plate, image radius < plate radius. Meta below the plate, not inside a bordered box. Two short lines of text, nothing else. |
| **Refero** | Editorial serif display headline over a quiet sans UI. Paper-white canvas, ink-black primary button, one functional accent. Search is the hero object. |
| **Linear** | Density + restraint: 13–14px UI text, hairline 1px dividers, no glow, no gradient backgrounds. Status shown with a 6px dot, not a pill. |
| **Beautiful UI** | Numbered mono labels (`01 Loading State`), dashed/hairline section rules, components shown on a calm neutral stage. |
| **shadcnblocks / taste-skill (anti-slop)** | No purple-blue gradients, no glass blobs, no glowing borders, no emoji headers. Consistent radius scale; buttons are part of the system, not bolted on. |

## Problems in v3 (before)
- Dark purple/blue radial glow + grid background = "generic AI site". Competes with the thumbnails it is supposed to frame.
- Cards: bordered dark boxes, a mono "COMPONENT STYLES" footer, 3 pill tags, 2 big copy pills + star + more → 5 rows of chrome around a small image. Badges ("Official demo") stamped on every thumbnail.
- Filters: three sticky rows of bordered chips overlapping the grid on scroll, cut off mid-word with no edge fade.
- Hero takes 900px before any resource is visible.

## System
- **Canvas** light by default (`#f6f6f4` paper, `#fff` surface, `#ececea` mat). Dark theme is neutral graphite (`#0d0d0d / #161616 / #1c1c1c`), never tinted.
- **Ink**: `#111` / `#5d5d58` / `#8f8f88`. **Accent**: signal orange `#ff5a1f` used only for focus ring, active-filter dot, live dot. Live = green dot.
- **Type**: Display = Instrument Serif (roman + italic), CJK fallback Songti/Noto Serif SC. UI = Geist 13/14/15. Mono = Geist Mono 11–12 for URLs, counts, labels.
  Scale: 11 · 12 · 13 · 14 · 16 · 20 · 28 · 40 · 64 (mobile hero 40).
- **Spacing**: 4px base — 4, 8, 12, 16, 20, 24, 32, 48, 72. Page gutter 20 (mobile) / 40 (desktop), max width 1320.
- **Radius**: 6 (thumb, button, chip) · 10 (mat, inputs) · 14 (sheet, menu). Nothing larger.
- **Lines**: 1px hairlines at 8% ink; shadows only on floating layers (menu, sheet, toast).

## Card anatomy (all 2357 cards, equal row height)
```
┌ mat (10px radius, 10px padding, neutral) ───────┐
│  ┌ thumb 16:10, 6px radius, hairline ring ─────┐ │  website → homepage shot
│  │                                              │ │  component → official demo shot
│  └──────────────────────────────────────────────┘ │  no image → typographic cover (serif name + mono label)
└──────────────────────────────────────────────────┘
 Title (14/600, 1 line)                 Live •  (only when meaningful)
 host.com/path · Free · MIT  (mono 11.5, 1 line)
 Note, 2 lines clamped, height reserved (13/1.45)
 [⧉ Prompt] [</> Code]                    ☆  ⋯     (28px, 6px radius, hairline)
```
- Grid: `repeat(auto-fill,minmax(264px,1fr))`, gap 32/20 desktop; 2 columns at 390px, gap 20/12, icon-only actions.
- Hover: thumb lifts 2px + ring darkens; no scaling of the whole card, no glow.

## Chrome
- Header 56px, paper with blur, hairline appears on scroll. Wordmark, text tabs, search, language, theme.
- Hero: mono eyebrow → serif headline (64/40) → 15px lede → 48px search. ~420px tall on desktop.
- Featured: 4-col bento (big 2×2, wide 2×1) on desktop; horizontal snap rail on mobile.
- Filters: one panel of hairline-separated rows; mono row label left (desktop) / above (mobile); chips 30px, 6px radius, active = ink fill; rows scroll horizontally with edge fade. Not sticky.
- Detail: right drawer 640px desktop / bottom sheet mobile; serif title, ink primary button, prompt/code in mono on the mat colour.
- Mobile nav: flat 56px tab bar with hairline, safe-area aware.

## Non-goals
Data, i18n (8 langs), copy prompt/code logic, licensing/legal text, routing, filters and resource count are unchanged.
