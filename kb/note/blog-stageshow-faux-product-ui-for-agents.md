# Stageshow: teaching agents to make product demos that look real

> Benji Taylor’s open-source Stageshow skill, released on 31 October, writes down the judgment behind good faux product UI for coding agents: five ways mockups fail, a seven-step workflow, gold examples, a React kit and a script that films the result so the agent can check its own work. What is in it, what it gets right, the accessibility and honesty gaps you still have to close, and a ten-step checklist for your next hero demo.

Blog post: <https://ui.incidental.site/blog/stageshow-faux-product-ui-for-agents/>

On 31 October designer Benji Taylor open-sourced **Stageshow**, an agent skill for one narrow job: faux product UI. That means the miniature, simplified screens on a landing page, a feature card or a docs hero, either as a still or as a short looping demo with a cursor. His point is that good models can already draw these, but the results tend to look heavy and generated. Stageshow is his attempt to write down the hundred small decisions a designer makes by hand so an agent can make them too. The launch post on X passed 1.3 million views and 24,000 bookmarks within two days, which says how many teams are fighting the same problem.

## What is in the skill

- **One idea and five failures.** The demo should read as a real product, simplified to what the viewer needs, framed with intent, with a cause for every motion. It fails when it is 
too much
 (real text everywhere), a 
wireframe
 (two gray blobs and a button), 
boxed
 (a whole window shrunk into a card), 
flat
 (everything the same weight) or 
bland
 (a gray window whatever the brief asked for).

- **A seven-step workflow.** Medium and placement, look, story, start from an example, build the screen, choreograph, rehearse. Most of the quality is decided before code: where the demo sits, the focal object, the action, the payoff and what can be left out.

- **Gold examples and teaching pairs.** Dozens of reference scenes (hero demo, bento grids, chart scrub, drag to reorder, an AI answer streaming in), product studies, and bad and good versions side by side. The agent copies the closest gold example instead of starting blank.

- **A small React kit.** A `Stage` with a scripted `Act` API, windows and phones drawn from real geometry, and motion parts such as `Roll`, `Count` and `Fly`. It handles the hard parts but deliberately supplies no look; you map your own tokens onto it.

- **Tools that film the result.** `film.mjs` opens the page in headless Chrome and shoots a contact sheet; `layout.mjs` checks that text and controls fit their boxes. The agent looks at its own frames and fixes the largest fault first: framing, then hierarchy, then motion, then polish.

## The numbers worth stealing

The rules are concrete enough to check. Design at the size the demo is seen: about 720 × 340 for a hero beside copy, 900 to 1100 wide for a full-width hero, 400 × 300 for a card, plus a separate compact design for a 358px phone column. Budget words, not elements: usually 3 to 7 real strings, with placeholder bars for the rest. Crop 10 to 40% of the hero window off the stage and let it fill at least two thirds of the width. A story is three to five beats in 10 to 16 seconds; the payoff holds for about two seconds; data never rewinds in view. And the faux app’s title is a `div`, never a real heading, because the demo lives inside someone else’s page outline.

## Our take

The kit is useful, but the real lesson is the shape of the skill. It pairs a short list of named failures with gold examples to copy and a way for the agent to 
see
 its own output. Most design skills only do the first. A rule like “avoid clutter” is easy to agree with and easy to ignore; a filmed frame next to the gold example is not. If you write design skills for your own team, copy that structure: failures with names, examples with numbers, and a check the agent can run.

Two things the skill leaves to you. First, **accessibility**: a 10 to 16 second loop that starts on its own and sits next to other content needs a way to pause it under WCAG 2.2.2, and readers who ask for reduced motion should get the poster frame, not the animation. Stageshow’s emphasis on a poster frame that tells the story on its own makes this easy, but you have to wire it up. Second, **honesty**: a polished faux screen can quietly become the spec, or promise a feature that does not exist yet. Show only what ships, label illustrations as illustrations, and re-film when the real product changes. Also note the licence: the code is MIT, but the bundled app icons and brand marks stay with their owners.

## Checklist: your next hero demo with an agent

- **Install and look first.** `npx skills add benjitaylor/skills --skill stageshow`, then run the playground and film the gold example closest to your idea.

- **Write the plan before any code.** Placement and size, focal object, the one action, the payoff, and what to leave out.

- **Map your tokens.** Font, accent, radius and light or dark ground from your real product, not the kit’s defaults.

- **Set a word budget.** Three to seven real strings on what the story is about; placeholder bars at the edges.

- **Frame it.** One hero, at most one satellite straddling its edge, the window bled off an edge, one consistent gutter.

- **Script three to five beats.** Ten to sixteen seconds, every cursor move explained, a payoff that holds, a loop that ends where it began.

- **Choose the poster frame.** The single frame that tells the story; serve it under `prefers-reduced-motion` and as the thumbnail.

- **Add a pause control.** Auto-playing loops over five seconds need one; give the demo an accessible name and keep its fake headings out of the outline.

- **Film at both widths.** Desktop and 390px; fix the largest visible fault first and re-film until the gate passes, then look again yourself.

- **Run an honesty pass.** Every feature shown exists today; the demo is captioned as an illustration; someone owns re-filming it after UI changes.

```
demo-plan.md
  place:    homepage hero, beside copy · 720×340 · compact 358
  focus:    the issue row being assigned
  beats:    open menu → pick teammate → avatar lands → status rolls
  payoff:   assigned row holds 2s · poster = this frame
  words:    issue title · teammate name · status   (3 real strings)
  a11y:     pause button · reduced motion → poster · role="img" + label
  honesty:  shipped feature only · caption "Illustration"
```

## How UI Hub helps

Stageshow is one of a growing set of design skills; 
teaching agents taste
 and 
design skills for Claude and Cursor
 explain how to stack them. Its motion rules sit well next to 
motion that feels right
, and 
our Linear and Vercel teardown
 shows why the first image on a landing page should be your real product. Before a demo ships, run the checks in 
accessibility in AI-generated UI
. The skill library on UI Hub lists Stageshow’s neighbours by role.

## References
- [Stageshow](https://benji.org/stageshow) — Benji Taylor, benji.org
- [Stageshow launch post](https://x.com/benjitaylor/status/2116593247854453244) — Benji Taylor (@benjitaylor), X
- [stageshow/SKILL.md](https://github.com/benjitaylor/skills/blob/main/stageshow/SKILL.md) — Benji Taylor, GitHub (benjitaylor/skills)
- [Framing reference](https://github.com/benjitaylor/skills/blob/main/stageshow/references/framing.md) — Benji Taylor, GitHub (benjitaylor/skills)
- [Craft reference](https://github.com/benjitaylor/skills/blob/main/stageshow/references/craft.md) — Benji Taylor, GitHub (benjitaylor/skills)
- [Motion reference](https://github.com/benjitaylor/skills/blob/main/stageshow/references/motion.md) — Benji Taylor, GitHub (benjitaylor/skills)
- [Rehearse reference (filming and checks)](https://github.com/benjitaylor/skills/blob/main/stageshow/references/rehearse.md) — Benji Taylor, GitHub (benjitaylor/skills)
- [Notices: licence and third-party assets](https://github.com/benjitaylor/skills/blob/main/stageshow/NOTICE.md) — Benji Taylor, GitHub (benjitaylor/skills)
- [Stageshow skill listing](https://agentools.sh/skills/stageshow/) — agentools.sh
- [Reply on labelling faux UI as a mock](https://x.com/themuscleai/status/2116917325613908205) — Muscle AI (@themuscleai), X
- [Understanding SC 2.2.2: Pause, Stop, Hide](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html) — W3C Web Accessibility Initiative
- [prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion) — MDN Web Docs
- [The open agent skills ecosystem](https://skills.sh/) — skills.sh