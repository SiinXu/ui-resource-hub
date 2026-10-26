# UI Hub context bundle (2026-10-26 04:43 UTC)

Source: https://ui.incidental.site/kb/ · Full skills: https://ui.incidental.site/api/kb.json

# UI Hub — guide for AI agents

Data updated 2026-10-26 04:43 UTC. Endpoints: `https://ui.incidental.site/api/resources.json` (items), `https://ui.incidental.site/api/skills.json` (skills + workflow), `https://ui.incidental.site/llms.txt`.

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
- **What is UI Hub?** A free, curated directory of 4937 public UI resources: 213 component libraries, 1989 component style demos with light/dark screenshots, 70 design skills for AI agents, plus effects, templates, specs and tutorials. It links to original sites and never hosts paid source code.
- **How do I find a component in a given style?** Load https://ui.incidental.site/api/resources.json and filter by ct (component kind, e.g. "dialog") and vs (visual style, e.g. "minimal" or "motion"). type="style" entries are concrete component demos with a libName and page URL; type="library" entries are whole libraries with install info on the site.
- **Which skills should an agent use for good UI?** One direction skill (frontend-design or taste-skill), emil-design-eng for motion and interaction polish, then impeccable, baseline-ui, web-design-guidelines and accessibility as an audit pass. See https://ui.incidental.site/api/skills.json.
- **Can I copy the code?** Open-source libraries can be used under their own licenses (MIT, Apache-2.0 etc.); the card shows the original link. Paid tiers (marked paid/freemium) must be bought from the original vendor.
- **How often is it updated?** Daily via a GitHub Actions job that adds new UI repositories and tools from GitHub, awesome-shadcn-ui and Hacker News. Nothing is deleted. Last update: 2026-10-26 04:43 UTC.


---

# Design specs

# Spacing & layout

> Use one 4/8-based scale, a max content width, and consistent gutters; spacing communicates grouping.

## Rules
- **One scale:** 4, 8, 12, 16, 24, 32, 48, 64, 96 px. No one-off values like 13 or 22.
- **Proximity = grouping:** space inside a group < space between groups (e.g. 8 inside, 24 between).
- **Content width:** body text 60–75 characters; page container 1120–1320 px; side gutters 20 px mobile, 40 px desktop.
- **Grid:** 12 columns desktop, 4 columns mobile; align cards to the same edges as headings and filters.
- **Density:** tools and dashboards can be dense (row height 36–40 px); marketing pages breathe (section padding 64–120 px).
- **No dead space:** a card should not have a large empty middle; size containers to content or fill with real content.

## Tokens
```css
:root{--s1:4px;--s2:8px;--s3:12px;--s4:16px;--s5:24px;--s6:32px;--s7:48px;--s8:64px;--max:1320px;--gut:20px}
@media(min-width:900px){:root{--gut:40px}}
```

## Sources
- [Refactoring UI](https://www.refactoringui.com)
- [Apple HIG — Layout](https://developer.apple.com/design/human-interface-guidelines/layout)
- [Laws of UX — Law of Proximity](https://lawsofux.com/law-of-proximity/)

# Typography

> Two families max, a modular type scale, tight display tracking, comfortable body leading, tabular numbers for data.

## Rules
- **Families:** one sans for UI (e.g. Geist, Inter), optionally one display serif (e.g. Instrument Serif) for headlines. Mono for code/data labels.
- **Scale:** 12 / 13 / 14 / 16 / 20 / 24 / 32 / 48 / 64. UI body 14–16 px, line-height 1.5–1.65.
- **Display:** large headings line-height 1.0–1.15 and letter-spacing −0.01 to −0.02em.
- **Hierarchy with weight and colour, not only size:** secondary text uses a muted ink token, not a smaller font.
- **Numbers:** `font-variant-numeric: tabular-nums` for prices, tables, counters.
- **CJK:** add PingFang SC / Noto Sans CJK fallbacks; avoid letter-spacing on CJK body text.
- **Line length:** 60–75ch for reading text.

## Sources
- [Refactoring UI](https://www.refactoringui.com)
- [Web Interface Guidelines (Vercel)](https://vercel.com/design/guidelines)
- [Material 3 typography](https://m3.material.io/styles/typography/overview)

# Colour

> Neutral base + one accent; semantic tokens; check contrast in both themes; gradients only as accents.

## Rules
- **Palette:** a neutral ramp (bg, surface, mat, line, ink, ink2, ink3) + ONE accent + status colours (success/warn/danger).
- **Semantic tokens**, never raw hex in components: `--bg --surface --ink --ink2 --accent --line`.
- **Contrast:** text ≥ 4.5:1, large text and UI glyphs ≥ 3:1 (WCAG 1.4.3 / 1.4.11) in light AND dark.
- **Gradients:** restrained: a sheen on one headline word or a 1px border, not full rainbow backgrounds.
- **Avoid:** muddy mid-tones, two competing accents, saturated blue on pure black.

## Sources
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [Material 3 colour](https://m3.material.io/styles/color/system/overview)
- [Tailwind CSS colours](https://tailwindcss.com/docs/colors)

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

# Accessibility

> Semantic HTML, visible focus, names for icon buttons, 24px targets, keyboard dialogs, WCAG 2.2 AA.

## Checklist
- Real `<button>`, `<a href>`, `<label>`; headings in order (one h1).
- `:focus-visible` ring on every interactive element; never bare `outline:none`.
- Icon-only buttons have `aria-label`; images have meaningful `alt` (or empty alt if decorative).
- Targets ≥ 24×24 CSS px (WCAG 2.5.8); 44 px recommended on touch.
- Dialogs: focus trap, Esc to close, return focus. Prefer Radix / React Aria / APG patterns.
- Don't convey state by colour alone; announce async results via `aria-live`.
- Test: keyboard only, screen reader smoke test, 200% zoom, reduced motion.

## Sources
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/)
- [Radix Primitives](https://www.radix-ui.com/primitives/docs/overview/introduction)

# Dark mode

> A second palette, not inversion: off-black base, elevation by lightness, desaturated accent, color-scheme set.

## Rules
- Swap semantic tokens with `[data-theme]` or `prefers-color-scheme`; remember the user's choice.
- Base off-black (#06070b–#121212), text off-white (#f3f5fb); avoid pure #000 / #fff pairs.
- Elevation by lighter surfaces; shadows barely read on dark.
- Desaturate / lighten the accent (e.g. #2563eb light → #67e8f9 dark) and re-check contrast.
- Set `color-scheme: light dark` so form controls and scrollbars follow.
- Previews and screenshots need both themes; never ship a "dark-only" demo without saying so.

## Sources
- [Apple HIG — Dark Mode](https://developer.apple.com/design/human-interface-guidelines/dark-mode)
- [web.dev — prefers-color-scheme](https://web.dev/articles/prefers-color-scheme)
- [NN/g — Dark vs Light mode](https://www.nngroup.com/articles/dark-mode/)

# Mobile & responsive

> Mobile-first layout, 44px touch targets, bottom navigation for primary tabs, safe areas, no horizontal scroll.

## Rules
- Design at 375 px first; breakpoints ~640 / 900 / 1280.
- Touch targets 44×44 px; spacing between targets ≥ 8 px.
- Primary navigation: bottom bar (3–5 items) on mobile; top tabs on desktop.
- Respect `env(safe-area-inset-*)` and use `viewport-fit=cover` only with padding.
- No horizontal scroll except intentional carousels with visible affordance.
- Inputs: 16 px font to avoid iOS zoom; correct `inputmode` / `enterkeyhint`.
- Test on a real device size in both themes.

## Sources
- [Apple HIG — Layout](https://developer.apple.com/design/human-interface-guidelines/layout)
- [Material 3 — Navigation bar](https://m3.material.io/components/navigation-bar/overview)
- [WCAG 2.2 — Target Size](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)

---

# House style & lessons

# House style: restrained fancy

> The UI Hub house style for sites we build: fancy but restrained, Aceternity / Magic UI / Cult UI quality, dense real content.

## The rule
"Fancy but restrained": polished like Aceternity UI, Magic UI and Cult UI, never loud.

## Do
- Information-dense cards: lead card + bento grid / collage, aligned edges, consistent gutters.
- One or two restrained accent colours; a gradient sheen on at most one word or edge.
- Real content in every cover and preview (real screenshots or meaningful diagrams).
- Refined motion: spotlight on hover, subtle entrance, ≤ 300 ms.
- Light + dark both designed; mobile checked at 375 px.
- 10 languages with automatic default by browser region.

## Don't (rejected in reviews)
- Documentation-site look for showcase pages.
- Big empty cards, blank covers, placeholder blocks, empty middles.
- Rainbow gradients and glow everywhere; glassmorphism as the main style.
- Muddy / dull palettes; misaligned columns; wrapped mid-word headings.

## Process
1. Read the UI Hub resources and skills first; pick a direction.
2. Produce ≥ 6 design options when the direction is open.
3. Build, then self-audit with impeccable / baseline-ui; deliver public link + light/dark screenshots.
4. If it is ugly, throw it away and redo rather than patching.

## References
- [Aceternity UI](https://ui.aceternity.com/components)
- [Magic UI](https://magicui.design/docs/components)
- [Cult UI](https://www.cult-ui.com)

# Lessons: previews and screenshots

> What we learned shipping 2,000+ component previews.

- Capture the actual component, not the marketing hero; crop to the component.
- Store light and dark shots; label "dark-only demo" honestly when the source has one theme.
- Never hotlink: save compressed WebP locally with credit to the original site.
- Re-check crops at card size: blurry or cut-off previews are worse than none.
- Thumbnails of whole sites are fine for "site" cards; component cards need component shots.


# Lessons: getting good UI from AI agents

> Practical rules that made agent-built UIs look designed instead of generated.

- Give the agent a short DESIGN brief with a "never" list before any code.
- Ask for several directions, choose one, then lock tokens.
- Load one direction skill, one craft skill, one audit skill; more causes conflicts.
- Require real copy; lorem ipsum hides hierarchy problems.
- Make the agent screenshot light/dark/mobile and look at them before saying "done".


---

# Skills index (fetch raw .md for full text)

- **accessibility** (design, full-text): Audit and improve web accessibility following WCAG 2.2 guidelines. Use when asked to "improve accessibility", "a11y audit", "WCAG compliance", "screen reader support", "keyboard na — https://ui.incidental.site/kb/skill/accessibility.md
- **api-design-principles** (engineering, digest): Master REST and GraphQL API design principles to build intuitive, scalable, and maintainable APIs that delight developers. Use when designing new APIs, reviewing API specifications — https://ui.incidental.site/kb/skill/api-design-principles.md
- **architecture-patterns** (engineering, digest): Implement proven backend architecture patterns including Clean Architecture, Hexagonal Architecture, and Domain-Driven Design. Use this skill when designing clean architecture for  — https://ui.incidental.site/kb/skill/architecture-patterns.md
- **baseline-ui** (design, full-text): Quickly deslop UI code by fixing spacing, hierarchy, typography, and small layout issues. Use when the interface needs a fast cleanup or polish pass. — https://ui.incidental.site/kb/skill/baseline-ui.md
- **composition-patterns** (engineering, full-text): React composition patterns that scale. Use when refactoring components with — https://ui.incidental.site/kb/skill/composition-patterns.md
- **emil-design-eng** (design, full-text): This skill encodes Emil Kowalski's philosophy on UI polish, component design, animation decisions, and the invisible details that make software feel great. — https://ui.incidental.site/kb/skill/emil-design-eng.md
- **fastapi-templates** (engineering, digest): Create production-ready FastAPI projects with async patterns, dependency injection, and comprehensive error handling. Use when building new FastAPI applications or setting up backe — https://ui.incidental.site/kb/skill/fastapi-templates.md
- **frontend-design** (design, full-text): Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. Helps with aesthetic direction, typography, and making choices that don't rea — https://ui.incidental.site/kb/skill/frontend-design.md
- **github-actions-templates** (engineering, digest): Create production-ready GitHub Actions workflows for automated testing, building, and deploying applications. Use when setting up CI/CD with GitHub Actions, automating development  — https://ui.incidental.site/kb/skill/github-actions-templates.md
- **impeccable** (design, full-text): Use when the user wants to design, redesign, shape, critique, audit, polish, clarify, distill, harden, optimize, adapt, animate, colorize, extract, or otherwise improve a frontend  — https://ui.incidental.site/kb/skill/impeccable.md
- **javascript-testing-patterns** (engineering, digest): Implement comprehensive testing strategies using Jest, Vitest, and Testing Library for unit tests, integration tests, and end-to-end testing with mocking, fixtures, and test-driven — https://ui.incidental.site/kb/skill/javascript-testing-patterns.md
- **mcp-builder** (engineering, full-text): Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers  — https://ui.incidental.site/kb/skill/mcp-builder.md
- **nodejs-backend-patterns** (engineering, digest): Build production-ready Node.js backend services with Express/Fastify, implementing middleware patterns, error handling, authentication, database integration, and API design best pr — https://ui.incidental.site/kb/skill/nodejs-backend-patterns.md
- **performance** (engineering, full-text): Optimize web performance for faster loading and better user experience. Use when asked to "speed up my site", "optimize performance", "reduce load time", "fix slow loading", "impro — https://ui.incidental.site/kb/skill/performance.md
- **playwright-cli** (engineering, digest): Automate browser interactions, test web pages and work with Playwright tests. — https://ui.incidental.site/kb/skill/playwright-cli.md
- **postgresql-table-design** (engineering, digest): Use this skill when designing or reviewing a PostgreSQL-specific schema. Covers best-practices, data types, indexing, constraints, performance patterns, and advanced features — https://ui.incidental.site/kb/skill/postgresql-table-design.md
- **rag-implementation** (engineering, digest): Build Retrieval-Augmented Generation (RAG) systems for LLM applications with vector databases and semantic search. Use when implementing knowledge-grounded AI, building document Q& — https://ui.incidental.site/kb/skill/rag-implementation.md
- **react-best-practices** (engineering, full-text): React and Next.js performance optimization guidelines from Vercel Engineering. This skill should be used when writing, reviewing, or refactoring React/Next.js code to ensure optima — https://ui.incidental.site/kb/skill/react-best-practices.md
- **redesign-skill** (design, digest): Upgrades existing websites and apps to premium quality. Audits current design, identifies generic AI patterns, and applies high-end design standards without breaking functionality. — https://ui.incidental.site/kb/skill/redesign-skill.md
- **stripe-integration** (engineering, digest): Implement Stripe payment processing for robust, PCI-compliant payment flows including checkout, subscriptions, and webhooks. Use when integrating Stripe payments, building subscrip — https://ui.incidental.site/kb/skill/stripe-integration.md
- **taste-skill** (design, full-text): Anti-slop frontend skill for landing pages, portfolios, and redesigns. The agent reads the brief, infers the right design direction, and ships interfaces that do not look templated — https://ui.incidental.site/kb/skill/taste-skill.md
- **typescript-advanced-types** (engineering, digest): Master TypeScript's advanced type system including generics, conditional types, mapped types, template literals, and utility types for building type-safe applications. Use when imp — https://ui.incidental.site/kb/skill/typescript-advanced-types.md
- **web-design-guidelines** (design, digest): Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check accessibility", "audit design", "review UX", or "check my site against best practic — https://ui.incidental.site/kb/skill/web-design-guidelines.md
- **web-quality-audit** (engineering, full-text): Run an evidence-led web quality audit covering performance, accessibility, SEO, best practices, and agentic browsing. Use when asked to "audit my site", "review web quality", "run  — https://ui.incidental.site/kb/skill/web-quality-audit.md
- **webapp-testing** (engineering, full-text): Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing browser screenshots, a — https://ui.incidental.site/kb/skill/webapp-testing.md

# Blog notes

- AI-assisted UI design: a workflow that keeps taste in the loop — https://ui.incidental.site/kb/note/blog-ai-assisted-ui-design-workflow.md
- Prompting for UI: write specs, not wishes — https://ui.incidental.site/kb/note/blog-prompts-for-ui.md
- Design-to-code with AI: map to your components, not to pixels — https://ui.incidental.site/kb/note/blog-design-to-code-with-ai.md
- Teaching agents taste: how design skills de-slop AI interfaces — https://ui.incidental.site/kb/note/blog-taste-and-skills-for-agents.md
- Component composition: why headless + copy-paste won — https://ui.incidental.site/kb/note/blog-component-composition.md
- Motion that feels right: purpose, duration, easing, restraint — https://ui.incidental.site/kb/note/blog-motion-that-feels-right.md
- Dark mode done right: tokens, elevation and contrast — https://ui.incidental.site/kb/note/blog-dark-mode-done-right.md
- Accessibility in AI-generated UI: the checks models skip — https://ui.incidental.site/kb/note/blog-accessibility-in-ai-generated-ui.md
- v0 in practice: from a prompt to shadcn code you can keep — https://ui.incidental.site/kb/note/blog-v0-prompt-to-shadcn.md
- Lovable and Bolt: when prompt-to-UI becomes prompt-to-app — https://ui.incidental.site/kb/note/blog-lovable-bolt-prompt-to-app.md
- Figma Make and the Figma agent: AI moves onto the canvas — https://ui.incidental.site/kb/note/blog-figma-make-and-figma-agent.md
- MagicOS: Magic Patterns bets on an infinite canvas of AI threads — https://ui.incidental.site/kb/note/blog-magic-patterns-magicos.md
- Prompt-to-UI tools compared: v0, Lovable, Bolt, Figma Make, Magic Patterns — https://ui.incidental.site/kb/note/blog-prompt-to-ui-tools-compared.md
- Aceternity UI deep dive: spectacle, used sparingly — https://ui.incidental.site/kb/note/blog-aceternity-ui-deep-dive.md
- Magic UI deep dive: animated components that install like shadcn — https://ui.incidental.site/kb/note/blog-magic-ui-deep-dive.md
- Cult UI deep dive: tactile components with personality — https://ui.incidental.site/kb/note/blog-cult-ui-deep-dive.md
- shadcn blocks and registries: page sections as source code — https://ui.incidental.site/kb/note/blog-shadcn-blocks-deep-dive.md
- Typography for AI-generated UI: the fastest way to look less generic — https://ui.incidental.site/kb/note/blog-typography-for-ai-generated-ui.md
- OKLCH colour systems: palettes that survive dark mode — https://ui.incidental.site/kb/note/blog-oklch-color-and-dark-mode.md
- Landing page teardown: what Linear and Vercel get right — https://ui.incidental.site/kb/note/blog-landing-page-teardown-linear-vercel.md
- Dashboard patterns that hold up: from KPI strip to drill-down table — https://ui.incidental.site/kb/note/blog-dashboard-design-patterns.md
- Design tokens for agents: the file that makes AI output on-brand — https://ui.incidental.site/kb/note/blog-design-tokens-for-agents.md
- Design skills for Claude and Cursor: SKILL.md, rules and AGENTS.md — https://ui.incidental.site/kb/note/blog-claude-cursor-design-skills.md
- Weekly roundup, 14 Oct 2026: guideline files go mainstream — https://ui.incidental.site/kb/note/blog-weekly-roundup-2026-w42.md
- Tutorial: have an agent build a landing page using UI Hub as context — https://ui.incidental.site/kb/note/blog-tutorial-agent-builds-landing-with-ui-hub.md
- Claude Design everywhere: out of beta, into every chat — https://ui.incidental.site/kb/note/blog-claude-design-everywhere.md
- Figma code layers and Specs: the canvas becomes the shared context again — https://ui.incidental.site/kb/note/blog-figma-code-layers-and-specs.md
- shadcn Trace and AI Elements: one shape for every step an agent takes — https://ui.incidental.site/kb/note/blog-shadcn-trace-and-ai-elements.md
- Lovart 2.0 and Arti: design agents learn to remember, run and review — https://ui.incidental.site/kb/note/blog-lovart-arti-design-agent-memory.md
- Layers, brand kits and JSON: three ways AI visuals stop looking generic — https://ui.incidental.site/kb/note/blog-layers-brand-kits-json-ai-visuals.md
- Lint the agent: keeping AI-written UI on your design system — https://ui.incidental.site/kb/note/blog-lint-agents-onto-your-design-system.md
- AI vectors for UI: what Ideogram Vector 1.0 changes, and the checks before an SVG ships — https://ui.incidental.site/kb/note/blog-ai-svg-for-ui-ideogram-vector.md
