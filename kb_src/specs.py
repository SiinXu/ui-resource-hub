# Design spec digests: original summaries written for UI Hub, with sources. Markdown bodies.
SPECS = [
('spacing','Spacing & layout','Use one 4/8-based scale, a max content width, and consistent gutters; spacing communicates grouping.',['layout','tokens'],"""
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
""",[('Refactoring UI','https://www.refactoringui.com'),('Apple HIG — Layout','https://developer.apple.com/design/human-interface-guidelines/layout'),('Laws of UX — Law of Proximity','https://lawsofux.com/law-of-proximity/')]),
('typography','Typography','Two families max, a modular type scale, tight display tracking, comfortable body leading, tabular numbers for data.',['type','tokens'],"""
## Rules
- **Families:** one sans for UI (e.g. Geist, Inter), optionally one display serif (e.g. Instrument Serif) for headlines. Mono for code/data labels.
- **Scale:** 12 / 13 / 14 / 16 / 20 / 24 / 32 / 48 / 64. UI body 14–16 px, line-height 1.5–1.65.
- **Display:** large headings line-height 1.0–1.15 and letter-spacing −0.01 to −0.02em.
- **Hierarchy with weight and colour, not only size:** secondary text uses a muted ink token, not a smaller font.
- **Numbers:** `font-variant-numeric: tabular-nums` for prices, tables, counters.
- **CJK:** add PingFang SC / Noto Sans CJK fallbacks; avoid letter-spacing on CJK body text.
- **Line length:** 60–75ch for reading text.
""",[('Refactoring UI','https://www.refactoringui.com'),('Web Interface Guidelines (Vercel)','https://vercel.com/design/guidelines'),('Material 3 typography','https://m3.material.io/styles/typography/overview')]),
('color','Colour','Neutral base + one accent; semantic tokens; check contrast in both themes; gradients only as accents.',['color','tokens'],"""
## Rules
- **Palette:** a neutral ramp (bg, surface, mat, line, ink, ink2, ink3) + ONE accent + status colours (success/warn/danger).
- **Semantic tokens**, never raw hex in components: `--bg --surface --ink --ink2 --accent --line`.
- **Contrast:** text ≥ 4.5:1, large text and UI glyphs ≥ 3:1 (WCAG 1.4.3 / 1.4.11) in light AND dark.
- **Gradients:** restrained: a sheen on one headline word or a 1px border, not full rainbow backgrounds.
- **Avoid:** muddy mid-tones, two competing accents, saturated blue on pure black.
""",[('WCAG 2.2','https://www.w3.org/TR/WCAG22/'),('Material 3 colour','https://m3.material.io/styles/color/system/overview'),('Tailwind CSS colours','https://tailwindcss.com/docs/colors')]),
('motion','Motion','Purposeful, fast (150–300 ms), ease-out on enter, transform/opacity only, honour reduced motion.',['motion'],"""
## Rules
- **Purpose:** orientation, feedback, continuity. Not decoration on frequent actions.
- **Durations:** micro 120–200 ms, panels 250–350 ms, page transitions ≤ 400 ms.
- **Easing:** ease-out (or spring with no overshoot) for enter; ease-in only for exits.
- **Performance:** animate `transform` and `opacity`; avoid animating layout properties.
- **Reduced motion:** `@media (prefers-reduced-motion: reduce)` swaps movement for fades or nothing.
- **One hero effect per page** (beam, spotlight, marquee). Stacking effects looks like a template.
""",[('Emil Kowalski — Great Animations','https://emilkowal.ski/ui/great-animations'),('Material 3 motion','https://m3.material.io/styles/motion/overview'),('MDN prefers-reduced-motion','https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion')]),
('accessibility','Accessibility','Semantic HTML, visible focus, names for icon buttons, 24px targets, keyboard dialogs, WCAG 2.2 AA.',['a11y'],"""
## Checklist
- Real `<button>`, `<a href>`, `<label>`; headings in order (one h1).
- `:focus-visible` ring on every interactive element; never bare `outline:none`.
- Icon-only buttons have `aria-label`; images have meaningful `alt` (or empty alt if decorative).
- Targets ≥ 24×24 CSS px (WCAG 2.5.8); 44 px recommended on touch.
- Dialogs: focus trap, Esc to close, return focus. Prefer Radix / React Aria / APG patterns.
- Don't convey state by colour alone; announce async results via `aria-live`.
- Test: keyboard only, screen reader smoke test, 200% zoom, reduced motion.
""",[('WCAG 2.2','https://www.w3.org/TR/WCAG22/'),('ARIA Authoring Practices Guide','https://www.w3.org/WAI/ARIA/apg/'),('Radix Primitives','https://www.radix-ui.com/primitives/docs/overview/introduction')]),
('dark-mode','Dark mode','A second palette, not inversion: off-black base, elevation by lightness, desaturated accent, color-scheme set.',['dark mode','color'],"""
## Rules
- Swap semantic tokens with `[data-theme]` or `prefers-color-scheme`; remember the user's choice.
- Base off-black (#06070b–#121212), text off-white (#f3f5fb); avoid pure #000 / #fff pairs.
- Elevation by lighter surfaces; shadows barely read on dark.
- Desaturate / lighten the accent (e.g. #2563eb light → #67e8f9 dark) and re-check contrast.
- Set `color-scheme: light dark` so form controls and scrollbars follow.
- Previews and screenshots need both themes; never ship a "dark-only" demo without saying so.
""",[('Apple HIG — Dark Mode','https://developer.apple.com/design/human-interface-guidelines/dark-mode'),('web.dev — prefers-color-scheme','https://web.dev/articles/prefers-color-scheme'),('NN/g — Dark vs Light mode','https://www.nngroup.com/articles/dark-mode/')]),
('mobile','Mobile & responsive','Mobile-first layout, 44px touch targets, bottom navigation for primary tabs, safe areas, no horizontal scroll.',['mobile','layout'],"""
## Rules
- Design at 375 px first; breakpoints ~640 / 900 / 1280.
- Touch targets 44×44 px; spacing between targets ≥ 8 px.
- Primary navigation: bottom bar (3–5 items) on mobile; top tabs on desktop.
- Respect `env(safe-area-inset-*)` and use `viewport-fit=cover` only with padding.
- No horizontal scroll except intentional carousels with visible affordance.
- Inputs: 16 px font to avoid iOS zoom; correct `inputmode` / `enterkeyhint`.
- Test on a real device size in both themes.
""",[('Apple HIG — Layout','https://developer.apple.com/design/human-interface-guidelines/layout'),('Material 3 — Navigation bar','https://m3.material.io/components/navigation-bar/overview'),('WCAG 2.2 — Target Size','https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html')]),
]
NOTES = [
('restrained-fancy','House style: restrained fancy','The UI Hub house style for sites we build: fancy but restrained, Aceternity / Magic UI / Cult UI quality, dense real content.',['style','lessons'],"""
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
""",[('Aceternity UI','https://ui.aceternity.com/components'),('Magic UI','https://magicui.design/docs/components'),('Cult UI','https://www.cult-ui.com')]),
('lessons-previews','Lessons: previews and screenshots','What we learned shipping 2,000+ component previews.',['lessons','previews'],"""
- Capture the actual component, not the marketing hero; crop to the component.
- Store light and dark shots; label "dark-only demo" honestly when the source has one theme.
- Never hotlink: save compressed WebP locally with credit to the original site.
- Re-check crops at card size: blurry or cut-off previews are worse than none.
- Thumbnails of whole sites are fine for "site" cards; component cards need component shots.
""",[]),
('lessons-ai-ui','Lessons: getting good UI from AI agents','Practical rules that made agent-built UIs look designed instead of generated.',['lessons','AI'],"""
- Give the agent a short DESIGN brief with a "never" list before any code.
- Ask for several directions, choose one, then lock tokens.
- Load one direction skill, one craft skill, one audit skill; more causes conflicts.
- Require real copy; lorem ipsum hides hierarchy problems.
- Make the agent screenshot light/dark/mobile and look at them before saying "done".
""",[]),
]
