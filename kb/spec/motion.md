# Motion

> Purposeful, fast (150–300 ms), ease-out on enter, transform/opacity only, honour reduced motion.

## Rules
- **Purpose:** orientation, feedback, continuity. Not decoration on frequent actions.
- **Durations:** micro 120–200 ms, panels 250–350 ms, page transitions ≤ 400 ms.
- **Easing:** ease-out (or spring with no overshoot) for enter; ease-in only for exits.
- **Performance:** animate `transform` and `opacity`; avoid animating layout properties.
- **Reduced motion:** `@media (prefers-reduced-motion: reduce)` swaps movement for fades or nothing.
- **One hero effect per page** (beam, spotlight, marquee). Stacking effects looks like a template.

## Sources
- [Emil Kowalski — Great Animations](https://emilkowal.ski/ui/great-animations)
- [Material 3 motion](https://m3.material.io/styles/motion/overview)
- [MDN prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion)
## Craft motion sources（质感动效）

Curated 2026-11-09. Prefer short, purposeful motion; always honour `prefers-reduced-motion`.

### Transitions.dev (Jakub Antalik)
- Site: https://transitions.dev — 43+ crafted transitions on the marketing library (site is largely grayscale; do not invent brand/accent hex).
- Free Skill (~27+ core): `npx skills add Jakubantalik/transitions.dev` (tooling MIT).
- Free Motion Agent (local score, no account): `npx transitions-agent` (package MIT). Do **not** run `fix` / open PRs in our pipeline without Siin’s OK.
- Pro (~$12/mo): full React/TS recipes + Pro Skill — **link only**, do not copy Pro code. Terms: https://transitions.dev/terms.html ; Pro: https://transitions.dev/pro.html
- Builder MCP (`https://api.transitions.dev/ui/mcp`) needs Pro/Business + browser sign-in — evaluate before installing; do not add as a global MCP without approval.
- **Use for:** dialog open/close, panel reveal, page switch, success check, toast.
- **Avoid:** full-screen spectacle, stacking effects on frequent controls, anything that hurts reading.
- **Required:** `@media (prefers-reduced-motion: reduce)` → fade or none.

### Kubai physical shockwave (reference only)
- Source: https://x.com/Kubai087/status/2119359092334743735 (author 枯白啃设计（@Kubai087）, 2026-11-08).
- Six layers: page snapshot, lens warp, RGB channel split ±8%, four color rings, edge refraction, edge-line specular.
- Palette names: Aurora / Halo / Frost / Spark (hex only if verified from the post; this entry stores none).
- **License:** reference only — **no code license**; do not copy source or prompts into production without separate rights.
- **Use for:** rare completion feedback or a single landing hero beat.
- **Avoid:** reading pages, frequent form actions, a11y-first surfaces, looping full-screen.
- **Reduced motion:** under `prefers-reduced-motion`, in-place half-strength fade in/out, 600ms (per original post).

