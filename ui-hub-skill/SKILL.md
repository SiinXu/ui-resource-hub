---
name: ui-hub
description: Use UI Hub (https://ui.incidental.site/) as a design source. Search 4881+ UI resources (component libraries, component style demos, effects, design systems) by component kind and visual style, copy code/prompts from original sources, and apply design skills (frontend-design, taste-skill, emil-design-eng, impeccable, baseline-ui, web-design-guidelines, accessibility) to build and audit good-looking, accessible UIs. Use when picking a component library or visual style, building a landing/pricing/dashboard page, or auditing UI quality.
---

# UI Hub — guide for AI agents

Data updated 2026-10-23 04:46 UTC. Endpoints: `https://ui.incidental.site/api/resources.json` (items), `https://ui.incidental.site/api/skills.json` (skills + workflow), `https://ui.incidental.site/llms.txt`.

## One-line prompt
EN: Use UI Hub (https://ui.incidental.site/) as your design source. First read https://ui.incidental.site/AGENTS.md, then fetch https://ui.incidental.site/api/resources.json and filter by ct (component kind), vs (visual style) and pricing=free to pick ONE open-source library and a visual style; lock tokens (font, spacing, radius, one accent, light+dark) before building. Load skills in this order from https://ui.incidental.site/api/skills.json: frontend-design or taste-skill → emil-design-eng → impeccable + baseline-ui + web-design-guidelines + accessibility. Verify in a browser (light/dark, 375px, keyboard, reduced motion) and cite every resource you used.

中文：请把 UI Hub（https://ui.incidental.site/）当作设计资料库。先读 https://ui.incidental.site/AGENTS.md，再获取 https://ui.incidental.site/api/resources.json，按 ct（组件类型）、vs（视觉风格）和 pricing=free 筛选，只选一个开源组件库和一种视觉风格；动手前先把字体、间距、圆角、唯一强调色和亮/暗两套 token 定下来。按顺序加载 https://ui.incidental.site/api/skills.json 里的 skill：frontend-design 或 taste-skill → emil-design-eng → impeccable + baseline-ui + web-design-guidelines + accessibility。最后在浏览器里验证（亮/暗、375px 手机、键盘、减少动效），并列出用到的每个资源。

## What this is for
- **Pick a component library** — type=library, filter by framework tag (React/Vue/Svelte), licence, pricing=free.
- **Find a visual style** — vs = minimal · enterprise · soft · playful · motion · dark-tech · gradient · 3d · apple · editorial · brutalist; type=style shows real demos per component.
- **Copy component code & prompts** — Open the original url for install + source; each card on the site has a copyable AI prompt.
- **Load design skills** — api/skills.json lists 29 agent skills and the order to run them.
- **Audit a UI** — Run impeccable / baseline-ui / web-design-guidelines / accessibility against the draft, then verify in a browser.

## Query the encyclopedia
- Search everything: `{BASE}api/search-index.json` (fields t=title, k=kind skill|spec|note|resource|component, u=url, r=raw md, d=description, g=tags). Human UI: {BASE}kb/?q=pricing
- Full knowledge entries: `{BASE}api/kb.json` (type, slug, tags, url, raw, md).
- Raw markdown per entry: `{BASE}kb/<type>/<slug>.md`, e.g. `kb/spec/spacing.md`, `kb/spec/dark-mode.md`, `kb/note/restrained-fancy.md`, `kb/skill/emil-design-eng.md`.
- One-file context: `{BASE}context-bundle.md` (this guide + specs + house style + skills index).
```bash
curl -s {BASE}api/search-index.json | jq '.items[] | select(.k=="spec" or .k=="note") | {{t,r}}'
curl -s {BASE}kb/spec/motion.md
```

## Fields
- `type`: library | style | effect | template | skill | system | spec | tool | tutorial | collection | generator | inspiration
- `ct` (component kind): button, input, select, dialog, menu, tabs, table, chart, card, nav, form, toast, avatar, loader, layout, chat, motion, background, editor, icon, mobile
- `vs` (visual style): minimal, enterprise, material, soft, playful, motion, dark-tech, utilitarian, gradient, 3d, apple, editorial, swiss, brutalist, glass, retro
- `pricing`: free | freemium | paid | unknown

## Workflow
1. Fetch resources.json; start from `gold==true` (curated 精选 tier), skip items with `flag`; then filter by `ct`, `vs`, `pricing=free`. Pick ONE primary page-level reference (gold) + at most TWO supporting component references, and match the primary closely.
2. Pick ONE direction skill (frontend-design or taste-skill); lock tokens: font, spacing scale, radius, one accent, light + dark.
3. Choose `type=library` for code and `type=style` demos for the concrete look; open the original `url` for install and source.
4. Start from the card's prompt; add layout, states, real content and an "avoid" list.
5. Polish motion with emil-design-eng; audit with impeccable, baseline-ui, web-design-guidelines, accessibility.
6. Verify in a browser: light/dark, 375px, keyboard, reduced motion. Cite resources used.

## Filter snippets
### Free React libraries with dialogs
```bash
curl -s https://ui.incidental.site/api/resources.json | jq '.items[] | select(.type=="library" and .pricing=="free" and (.ct//[]|index("dialog")) and (.tags|index("React"))) | {name,url}'
```

### Dark-tech style demos for cards
```bash
curl -s https://ui.incidental.site/api/resources.json | jq '[.items[] | select(.type=="style" and (.vs//[]|index("dark-tech")) and (.ct|index("card")))] | .[:10] | map({name,libName,page})'
```

### Count items per visual style
```bash
curl -s https://ui.incidental.site/api/resources.json | jq '[.items[].vs[]?] | group_by(.) | map({(.[0]):length}) | add'
```

### fetch (JS): motion effects, free
```bash
const r = await fetch('https://ui.incidental.site/api/resources.json').then(r => r.json());
const picks = r.items.filter(i => ['effect','library'].includes(i.type) && i.vs?.includes('motion') && i.pricing === 'free');
```

### New this week
```bash
curl -s https://ui.incidental.site/api/resources.json | jq --arg d "$(date -u -d '7 days ago' +%F)" '.items[] | select(.added and .added >= $d) | {name,url,added}'
```

## Worked examples
### Build a dark SaaS pricing page
- **Filter:** curl -s https://ui.incidental.site/api/resources.json | jq '.items[] | select(.type=="library" and .pricing=="free" and (.tags|index("React")) and ((.ct//[]) | index("card") or index("button") or index("layout"))) | {name,url}'
- **Choose:** shadcn/ui (base components); shadcn/ui Blocks (pricing section); Radix Primitives (underneath); Magic UI Number Ticker (the one accent moment)
- **Tokens:** bg #06070b, surface #10131a, ink #f3f5fb, accent #67e8f9, radius 12px, font Geist 14/20, numbers tabular-nums
- **Skills order:** taste-skill (set the direction), then emil-design-eng (toggle and hover motion, 200ms or less, ease-out), then impeccable + baseline-ui + accessibility (final audit)
- **Verify:** Monthly / annual toggle works with the keyboard; Visible focus ring on every CTA; Muted text reaches 4.5:1 contrast; At 375px the tiers stack vertically; Reduced motion turns the ticker off; Light theme still looks right

### Add a fancy but restrained landing hero
- **Filter:** curl -s https://ui.incidental.site/api/resources.json | jq '.items[] | select((.type=="effect" or .type=="library") and .pricing=="free" and ((.vs//[])|index("motion")) and ((.ct//[])|index("background"))) | {name,url}'
- **Choose:** Aceternity Spotlight (pick one of these two); Magic UI Beams (or this one); Motion (entrance only)
- **Skills order:** frontend-design (set the direction), then emil-design-eng (motion polish), then web-design-guidelines + performance (audit)
- **Verify:** LCP under 2.5s; Effect pauses when reduced motion is on; Text stays readable over the effect in both themes

### Audit an existing admin dashboard
- **Filter:** curl -s https://ui.incidental.site/api/resources.json | jq '[.items[] | select(.type=="style" and ((.vs//[])|index("enterprise")) and ((.ct//[]) | index("table") or index("nav") or index("form")))] | .[:20] | map({name,libName,page})'
- **Skills order:** redesign-skill (find the problems), then baseline-ui (fix the basics), then accessibility (accessibility pass), then web-quality-audit (final score)
- **Verify:** Table header stays sticky; Rows can be focused with the keyboard; Empty, loading and error states exist; Click targets are at least 24px; Dark mode matches light mode

## Style decision table
| Product | vs | Libraries | Key rules |
|---|---|---|---|
| Developer tool / SaaS | minimal · dark-tech | shadcn/ui, Radix, Origin UI | One accent, tabular numbers, dense tables |
| Enterprise admin | enterprise | Ant Design, Mantine, MUI X, AG Grid | Density, keyboard, data states |
| Consumer / playful | playful · soft | HeroUI, daisyUI, Animate UI | Rounded, warm colour, light motion |
| Marketing / launch page | motion · gradient | Magic UI, Aceternity, Tailark | One hero effect, strong type |
| Editorial / content | editorial · swiss | Tailwind Typography, Radix Themes | Serif display, measure 60–75ch |
| Apple-like product | apple · glass (sparingly) | Radix, Motion, Vaul | Springs, blur only on chrome |
| Characterful indie | brutalist · retro | neobrutalism, RetroUI, 8bitcn | Thick borders, hard shadows, still accessible |

## Do
- Pick ONE library and ONE visual style per product
- Lock tokens (CSS variables) before pages
- Prefer pricing=free + permissive licences for shipped code
- Use type=style demos to match a concrete look
- At most one hero effect per page
- Verify light/dark, 375px, keyboard, reduced motion
- Cite resources (name + URL) in your PR

## Don't
- Mix three component libraries in one UI
- Copy paid / Pro source or hotlink preview images
- Stack gradients, glass and glow together
- Use clickable divs or remove focus outlines
- Animate frequent actions or exceed ~300ms in UI
- Trust a screenshot: always open the original url
- Invent licences or affiliate links

## Skills
- `accessibility` (design): Audit and improve web accessibility following WCAG 2.2 guidelines. Use when asked to "improve accessibility", "a11y audit", "WCAG compliance", "screen reader support", "keyboard navigation", or "make 
- `baseline-ui` (design): Quickly deslop UI code by fixing spacing, hierarchy, typography, and small layout issues. Use when the interface needs a fast cleanup or polish pass.
- `composition-patterns` (engineering-ui): React composition patterns that scale. Use when refactoring components with
- `emil-design-eng` (design): This skill encodes Emil Kowalski's philosophy on UI polish, component design, animation decisions, and the invisible details that make software feel great.
- `frontend-design` (design): Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. Helps with aesthetic direction, typography, and making choices that don't read as templated defau — https://github.com/anthropics/skills
- `impeccable` (design): Use when the user wants to design, redesign, shape, critique, audit, polish, clarify, distill, harden, optimize, adapt, animate, colorize, extract, or otherwise improve a frontend interface. Covers we — https://github.com/pbakaus/impeccable
- `iterate-until-verified` (engineering-ui): Apply a prompt-agnostic execution and verification loop to any substantial task while preserving the original request. Use when the user asks to fan out work, use subagents or independent reviewers, l
- `performance` (engineering-ui): Optimize web performance for faster loading and better user experience. Use when asked to "speed up my site", "optimize performance", "reduce load time", "fix slow loading", "improve page speed", or "
- `playwright-cli` (engineering-ui): Automate browser interactions, test web pages and work with Playwright tests.
- `react-best-practices` (engineering-ui): React and Next.js performance optimization guidelines from Vercel Engineering. This skill should be used when writing, reviewing, or refactoring React/Next.js code to ensure optimal performance patter
- `redesign-skill` (design): Upgrades existing websites and apps to premium quality. Audits current design, identifies generic AI patterns, and applies high-end design standards without breaking functionality. Works with any CSS 
- `taste-skill` (design): Anti-slop frontend skill for landing pages, portfolios, and redesigns. The agent reads the brief, infers the right design direction, and ships interfaces that do not look templated. Real design system — https://github.com/Leonxlnx/taste-skill
- `web-design-guidelines` (design): Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check accessibility", "audit design", "review UX", or "check my site against best practices".
- `web-quality-audit` (design): Run an evidence-led web quality audit covering performance, accessibility, SEO, best practices, and agentic browsing. Use when asked to "audit my site", "review web quality", "run lighthouse audit", "
- `webapp-testing` (engineering-ui): Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing browser screenshots, and viewing browser l — https://github.com/anthropics/skills

## FAQ
- **What is UI Hub?** A free, curated directory of 4881 public UI resources: 201 component libraries, 1989 component style demos with light/dark screenshots, 70 design skills for AI agents, plus effects, templates, specs and tutorials. It links to original sites and never hosts paid source code.
- **How do I find a component in a given style?** Load https://ui.incidental.site/api/resources.json and filter by ct (component kind, e.g. "dialog") and vs (visual style, e.g. "minimal" or "motion"). type="style" entries are concrete component demos with a libName and page URL; type="library" entries are whole libraries with install info on the site.
- **Which skills should an agent use for good UI?** One direction skill (frontend-design or taste-skill), emil-design-eng for motion and interaction polish, then impeccable, baseline-ui, web-design-guidelines and accessibility as an audit pass. See https://ui.incidental.site/api/skills.json.
- **Can I copy the code?** Open-source libraries can be used under their own licenses (MIT, Apache-2.0 etc.); the card shows the original link. Paid tiers (marked paid/freemium) must be bought from the original vendor.
- **How often is it updated?** Daily via a GitHub Actions job that adds new UI repositories and tools from GitHub, awesome-shadcn-ui and Hacker News. Nothing is deleted. Last update: 2026-10-23 04:46 UTC.
