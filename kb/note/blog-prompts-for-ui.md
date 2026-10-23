# Prompting for UI: write specs, not wishes

> "Modern and clean" means nothing to a model. Name layout, tokens, states, content and what to avoid.

Blog post: <https://ui.incidental.site/blog/prompts-for-ui/>

A UI prompt is a tiny design spec. The model fills every gap you leave with its defaults, and defaults are clichés: a centred hero, three feature cards, a purple-to-blue gradient, emoji as icons. A prompt that says "modern and clean" leaves every gap open. This post shows how to close them with a fixed structure, how to iterate without starting over, and which mistakes waste the most rounds.

## Why "make it modern" fails

Language models predict the most likely continuation. For UI, the most likely continuation is the average of thousands of landing pages. Adjectives like 
modern
, 
clean
 or 
premium
 do not narrow that average, because every template on the web claims all three. What narrows it is information the model cannot guess: your audience, your content, your tokens, your states, and the things you refuse.

Anthropic's prompt-engineering guide makes the same point in general terms: be clear and direct, give context, and say what the output is for. Vercel's v0 docs add the UI-specific version: describe the layout, name the components and give real content.

## The six-slot template

Goal: pricing page for a dev tool, 3 tiers, annual/monthly toggle
Layout: 12-col grid, max 1200px; tiers in one row at >= 900px, stacked below
Tokens: Geist; body 14/20; radius 10; one accent #2563eb; neutral greys only
States: hover, focus-visible ring, selected tier, loading on the CTA, disabled
Content: use the copy below verbatim (no lorem); prices 0 / 19 / 49 USD
Avoid: gradient text, glassmorphism, emoji icons, everything centred, drop shadows > 8px

Each slot answers one question the model would otherwise answer with a default:

- **Goal** — what the screen is for and the one thing it must do. Keep it to one line.

- **Layout** — grid, max width, breakpoints and what happens below them. "Responsive" is not a layout.

- **Tokens** — font, type scale, radius, colour. One accent colour is a constraint the model respects surprisingly well.

- **States** — hover, focus, selected, loading, empty, error, disabled. Screenshots never show states, so models skip them unless asked.

- **Content** — paste real copy. Placeholder text hides overflow, wrapping and hierarchy problems that real headlines expose immediately.

- **Avoid** — a short refuse-list. This is the slot that most changes the look.

## A worked example, step by step

**Step 1: write the brief.** Before the six slots, write two sentences about the audience: "Solo developers comparing three plans on a phone during a commute. They care about the limits table more than the hero." This decides density and what goes above the fold.

**Step 2: ask for variants, not a page.** The first message should ask for three deliberately different directions, for example "A: editorial, serif headings; B: dense table-first; C: card-based with a toggle". Diversity is cheap for the model and expensive for you to imagine.

**Step 3: pick one and critique in named problems.** "Make it better" produces random change. Named problems produce targeted change:

Keep variant B. Fix only these:
1. Line length in the FAQ is ~95ch; cap at 68ch.
2. Two accent colours compete (blue CTA, green badge). Use the accent for the CTA only.
3. The selected tier has no visible focus ring when tabbing.
4. Prices are not tabular; use font-variant-numeric: tabular-nums.
Do not change anything else.

**Step 4: lock decisions.** When a decision is good, move it out of the chat into a file the agent reads every time (a `DESIGN.md` or token file). Otherwise the next session starts from the average again.

## Pitfalls that waste the most rounds

- **Stacking adjectives.** "Sleek, minimal, bold, playful" is four conflicting instructions. Pick one adjective you want and one you refuse.

- **Changing many things per round.** If you ask for six changes, you cannot tell which one broke the layout. Two to four named fixes per round is a good rhythm.

- **No negative examples.** Models follow "avoid X" better after they have produced X once. Put the Avoid line first when iterating.

- **Lorem ipsum.** It always fits. Your German translation or 40-character product name will not.

- **Forgetting the dark theme.** Ask for both themes in the first round; retrofitting dark mode is where contrast bugs come from.

- **Asking for "pixel perfect" from a screenshot.** You get absolute positioning. Ask for your components and tokens instead.

## Slot values for three common screens

The template stays the same; what changes is which slots carry the weight. Three examples we reuse:

DATA TABLE
Layout: full width inside a 1280px shell; sticky header; first column sticky on < 768px
Tokens: 13/18 table text; tabular-nums; row height 40; zebra off; 1px dividers
States: sorted column, row hover, row selected (checkbox), loading skeleton rows, empty, error with retry
Content: 8 real rows incl. one 60-char name and one negative number
Avoid: cards on mobile (keep the table, scroll horizontally), icons in every cell

EMPTY STATE
Goal: first-run screen for a project list with zero projects
Layout: centred block max 420px; illustration optional, max 160px tall
Content: one-line headline, one sentence of help, one primary action, one docs link
Avoid: three CTAs, jokes, stock 3D illustrations

SETTINGS FORM
Layout: label column 200px + field column at >= 768px; single column below
States: dirty (unsaved) bar, inline validation on blur, saving, saved toast, server error per field
Avoid: modal dialogs for each setting, auto-save without feedback

Notice that the data table spends its words on **states and content**, the empty state on **content and restraint**, and the form on **states**. When a prompt fails, check which slot that screen depends on and whether you left it to the default.

## How to tell if a prompt is done

A useful test: hand the prompt to a colleague and ask them to sketch the screen in two minutes. If they ask "what colour?", "what happens on mobile?" or "what does the button say?", the model would have guessed too. Every question they ask is a slot you have not filled. A second test: could you reject the output using only the prompt? If "it looks off" is your only objection, the prompt has no checkable rules, and the next round will be a lottery.

## Keeping reusable prompts

Keep one prompt per component type (pricing, settings form, data table, empty state) in your repo. Each one is the six slots with your tokens already filled in, so a new screen only needs Goal and Content. UI Hub's component cards include a copyable prompt you can start from, and the AI prompt block at the end of this post is a ready-made reviewer prompt.

## Checklist

- Two-sentence audience brief written

- All six slots filled; tokens are real values, not adjectives

- First round asks for 3 variants

- Critique lists 2–4 named problems and says "change nothing else"

- Good decisions moved into a file the agent reads every session

- Both themes and all interactive states requested

## References
- [Web Interface Guidelines](https://vercel.com/design/guidelines) — Vercel
- [Web Interface Guidelines (interfaces.rauno.me)](https://interfaces.rauno.me) — Rauno Freiberg
- [v0 Documentation](https://v0.app/docs) — Vercel
- [Refactoring UI](https://www.refactoringui.com) — Adam Wathan & Steve Schoger
- [Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) — Anthropic