# AGENTS.md — using UI Hub as a design source

You are an AI coding/design agent. UI Hub (https://siinxu.github.io/ui-resource-hub/) is a curated index of UI libraries, component demos and design skills.

## Steps
1. Fetch `https://siinxu.github.io/ui-resource-hub/api/resources.json` (≈2376 items, updated 2026-10-14 08:54 UTC).
2. Filter: `type` (library | style | effect | template | skill …), `ct` (button, input, dialog, table, chart, chat, motion, background, layout …), `vs` (minimal, enterprise, soft, playful, motion, dark-tech, gradient, 3d, apple, editorial, brutalist …), `pricing` (prefer free).
3. Prefer `type=library` with an open license for production code; use `type=style` entries (component demos with `libName`, `page`) to choose a concrete look.
4. Open the original `url` for the install command and source. Respect each license; never copy paid/pro source.
5. Load skills from `https://siinxu.github.io/ui-resource-hub/api/skills.json`: one direction skill (frontend-design | taste-skill) → build → emil-design-eng for motion → audit with impeccable, baseline-ui, web-design-guidelines, accessibility.
6. Verify in a real browser: light + dark, 375px mobile, keyboard focus, reduced motion.

## Rules
- Pick ONE visual style per product and lock it into tokens (CSS variables) before building pages.
- At most one "hero" effect (beams/spotlight/marquee) per page.
- Cite the resources you used (name + URL) in your PR/description.
