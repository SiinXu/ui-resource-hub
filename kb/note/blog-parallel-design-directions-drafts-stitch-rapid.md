# AI made design variants cheap. Now make them comparable: Lovable Drafts, Stitch Rapid and parallel design

> On 16 November 2026 Lovable launched Drafts, full copies of an app with their own chat, preview and, usually, a backend filled with example data. Five days earlier Google began rolling out Stitch Rapid, which turns a rough prompt into a clickable multi-screen flow in about five seconds. One is high fidelity, one is a throwaway scratchpad, and both make parallel design nearly free. What each does, where the risks hide, our take on judging variants fairly, plus a checklist and an agent prompt.

Blog post: <https://ui.incidental.site/blog/parallel-design-directions-drafts-stitch-rapid/>

Two launches a few days apart point the same way. On 16 November Lovable shipped **Drafts**: from the project name at the top of the editor you hit “New draft” and get a complete copy of your app, from design to database, with its own chat and preview. On 11 November Google started rolling out **Stitch Rapid**, an experiment in its Stitch design tool that turns a rough prompt or a screenshot into a clickable, medium-fidelity flow of several screens in about five seconds, with new variations about two seconds after a tap.

They sit at opposite ends of fidelity, but they remove the same cost. Exploring three directions used to mean three times the work, so most teams quietly shipped their first idea and polished it. That cost is close to zero now. The new bottleneck is judging the variants, and that is a design-process problem, not a tooling one.

## What each tool actually gives you

- **Lovable Drafts: a branch of the whole product.** Each draft has its own chat, preview and edits, and you can compare drafts side by side or ask Lovable to spin up several versions. On a project that uses the built-in backend, a draft usually gets a backend of its own filled with example data, so a new dashboard shows months of bookings instead of an empty table. A project can hold up to 500 open drafts; an untouched new draft disappears after 24 hours.

- **Lovable Drafts: the data can be made consistent.** Unless you say otherwise, Lovable writes a few example rows per table when it creates a draft. Ask it to create an example data file and it saves the rows in `db/seed.sql`, so every later draft starts from the same customers and bookings. For comparing designs, that file matters more than it sounds.

- **Lovable Drafts: accept is not fully reversible.** Accepting adds the draft’s pages to your unpublished changes, but changes to database structure, storage settings and backend functions take effect in the live app immediately. Restoring an earlier version does not undo schema changes. Some drafts share the live backend (no “example data” banner above the preview), and in every draft secrets and connected services use their live values.

- **Stitch Rapid: a scratchpad for flows.** Google calls it an early MVP. You pick one of seven design systems (Wireframe, Breeze and Material Design 3 among them, Auto by default), then edit on the canvas: right-click an element to ask for a change, double-click text to rewrite it, hold Space to speak an edit, or open a Tuner with sliders for size and spacing. Screens come pre-linked, and clicking an unlinked button while playing can generate the next screen.

- **Stitch Rapid: nothing is kept.** The scratchpad is not saved between sessions. “Send to Stitch” moves a flow into regular Stitch for high-fidelity polish, and hands-on reports say the Rapid page reloads when you do, so download keepers as HTML first.

## Our take: the variant is cheap, the comparison is the work

Parallel design is old advice. Nielsen Norman Group’s guidance is three to five quick alternatives, then a merge, then iteration. In their 1996 study, picking the best of four parallel versions gave usability 56% above the average original, merging the best ideas gave 70%, and one further iteration on the merge reached 152%. Note what wins: the merge, not the winner. Tools that make ten variants in a minute tempt you to do the opposite, scroll through them, pick the prettiest and move on.

Three things decide whether cheap variants actually improve the result. First, **fidelity should match the question**. “Which screens does onboarding need, in what order?” is a Stitch Rapid question; answering it in full app copies wastes review time on colours. “Does this dashboard still read when a clinic has 400 bookings a week?” needs real components and realistic data, which is what Drafts provide. Second, **variants must differ on purpose**. Name the one axis each direction changes (density, navigation model, tone) and keep everything else fixed, or you cannot tell what caused the difference. Third, **the data must be the same**. A draft with three tidy rows will always beat one shown with a messy, realistic week. A shared seed file with long names, empty states and outliers is a design asset; treat it like your type scale.

The risks are about what is shared, not what is copied. In Lovable the screens are isolated but schema changes go live on accept, and secrets and integrations are live everywhere, so a “test” email from a draft is a real email. In Stitch Rapid the risk is the opposite: nothing persists, so a good direction can vanish with a tab.

## A workflow that keeps the benefit

- **Write the brief once.** Goal, audience, the three to five key screens, and what success looks like. Every variant gets the same brief.

- **Explore flows at low fidelity.** Use Stitch Rapid or a wireframe system to settle screen count and order. Download every keeper as HTML before sending it on.

- **Fix the seed data.** Create one example data file with realistic volume, long strings, empty and error cases, and one extreme user. All drafts start from it.

- **Branch three directions, one axis each.** Name drafts by the axis (“dense table”, “card timeline”, “calm summary”), not “v2”.

- **Review side by side against the brief.** Same tasks, same data, same viewport, light and dark. Ideally show each person two or three versions and vary the order.

- **Merge, then iterate.** Take the best parts into one direction, record why the others lost, delete the rest, and only then accept and publish.

## Checklist before you accept a draft

- Does the draft have its own backend (example data banner) or share the live one?

- Will accepting change tables, access rules, storage or backend functions? Those go live at once and a restore will not undo them.

- Did anything in the draft call a live integration, such as email, payments or webhooks?

- Were all variants judged on the same seed data and the same tasks?

- Is the losing directions’ best idea carried into the merge, and is the reason written down?

- Were light, dark and a narrow mobile width checked after the merge?

```
# Paste this into your design or coding agent
Create 3 design directions for 
 from the brief below.
- Each direction changes ONE axis only: 
.
  Name each draft after its axis. Keep copy, data and components identical otherwise.
- Use the shared seed data in 
: include a long name, an empty state,
  an error state and one heavy user. Do not invent extra rows per direction.
- Do not change the database schema, access rules or any live integration.
- For each direction: screenshots at 1280px and 390px, light and dark,
  plus 3 sentences on what it optimises for and what it sacrifices.
- Then propose ONE merged direction that keeps the best idea from each,
  and list what you dropped and why. Wait for my approval before accepting anything.
```

UI Hub related reading: 
Lovable and Bolt, prompt to app
, 
prompt-to-UI tools compared
 and 
annotate, don’t describe
.

## References
- [Now you can explore any idea in parallel without touching what’s live](https://lovable.dev/blog/introducing-drafts) — Lovable blog
- [Explore changes with drafts](https://docs.lovable.dev/features/drafts) — Lovable Docs
- [Revert and restore your project with version history](https://docs.lovable.dev/features/projects/history) — Lovable Docs
- [Collaboration](https://docs.lovable.dev/features/collaboration) — Lovable Docs
- [Google releases experimental “Stitch Rapid”: multi-screen prototypes in about five seconds (in Japanese)](https://gihyo.jp/article/2026/11/stitch-rapid) — gihyo.jp
- [What is Google “Stitch Rapid”? Where the five-second multi-screen prototype experiment fits, and its caveats (in Japanese)](https://chot-inc.com/columns/google-stitch-rapid-multi-screen-prototype) — chot Inc.
- [Stitch by Google (official account, Stitch Rapid thread, 11 Nov 2026)](https://x.com/stitchbygoogle) — X · @stitchbygoogle
- [Introducing “vibe design” with Stitch](https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-ai-ui-design/) — Google blog
- [3 Design Processes for High Usability: Iterative Design, Parallel Design, and Competitive Testing](https://www.nngroup.com/articles/parallel-and-iterative-design/) — Therese Fessenden · Nielsen Norman Group