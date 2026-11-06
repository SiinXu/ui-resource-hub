# Figma’s agent now draws icons as strokes: keep the line weight editable

> On 5 November 2026 Figma improved agent-generated vector illustrations and icons: line work comes as strokes (not filled outlines), layers are grouped for editing, you can attach style references, and the structure is ready for Figma Motion. Why that matters for icon systems, how to brief the agent, and a checklist from prompt to shipped SVG.

Blog post: <https://ui.incidental.site/blog/figma-agent-vector-strokes-icons/>

On 5 November 2026 Figma’s release notes listed a quiet but useful change: the Figma agent now generates polished vector illustrations and icons that are easier to edit, match to a style, or animate. Four details matter for anyone who has inherited an AI icon set they could not finish: functional layer grouping, attachable style references, line work drawn as **strokes instead of fills**, and a layer tree clean enough for Figma Motion.

That is a different promise from “AI drew a nice picture”. A filled outline bakes the weight into the shape. A stroke keeps weight and end caps as settings, so you can drag them later without redrawing. Figma’s own help centre says the agent can generate illustrations and icon sets from a prompt or from reference images, with editable strokes and fills and an organised layer structure, and you can watch them appear live on the canvas.

## What actually changed

- **Strokes for line work.** Change stroke weight and end caps without redrawing the path. That is the difference between a one-off asset and a system you can still tune.

- **Layers grouped by function.** Independent layers that are grouped intuitively, so you can revise one part of an icon set without exploding the whole file.

- **Style references.** Attach your own illustrations so the agent generates more components or on-brand icons at scale, instead of inventing a new look every time.

- **Motion-ready structure.** The same clean tree is meant to animate in Figma Motion, by you or by the agent.

The same week Figma also put code layers into open beta with a workflow lab (4 November) and earlier raised shader export to 4096 px and into code layers (2 November). Vectors, motion and code on one canvas are converging; this post stays on the vector side.

## Our take

The useful unit is not “an illustration”, it is **an editable line decision**. Most prompt-to-image tools still hand you a raster or a flattened SVG that looks right until you need a 1.5 px hairline next to a 2 px icon. Drawing in strokes moves the decision back into the file. Keep that decision open all the way to production: export SVG with real `stroke` attributes, set `stroke="currentColor"`, hold width in a CSS custom property, and use `vector-effect: non-scaling-stroke` when the icon must keep one optical weight at every size.

Style references are the other half. An agent that has never seen your icon set will invent a second dialect. Attach three of your best icons, name the stroke weight and end cap in the prompt, and ask for three more in the same family before you commission a whole set. Open the layers panel before you admire the preview—generated art is only as useful as its structure.

We would still clean the SVG before shipping (SVGO, viewBox, aria-hidden or a title). Treat the agent like a junior illustrator who drafts in your file, not like a CDN of finished icons.

## Checklist: from prompt to a shipped stroke icon

- **Brief the line, not the vibe.** Name stroke weight, end caps (round / butt / square), corner joins, and whether fills are allowed.

- **Attach style references.** Two or three existing icons beat a paragraph of adjectives. Ask for a small batch first and compare strokes side by side.

- **Open the layers panel.** Confirm independent, sensibly grouped layers before you accept the result.

- **Tune weight on the stroke.** Adjust stroke weight and caps; if you have to redraw, the file is still a filled outline—reject it.

- **Animate only if the tree is clean.** Use Figma Motion on paths that already separate; do not animate a flattened blob.

- **Export as live strokes.** Keep `stroke` / `stroke-width` / `stroke-linecap` in the SVG. Outline only for logos that need a fixed silhouette.

- **Tokenise on the page.** One `--line` (or similar) for icons, rules and markers; `currentColor` for theme; check light and dark.

- **Access and credits.** Agent work uses Figma AI credits; check your plan before generating a large set.

```
# Brief for the Figma agent (icon set)
Goal:       6 outline icons for a docs site (search, copy, link, warn, check, menu)
Style ref:  attach icons/search.svg + icons/copy.svg (our current set)
Stroke:     1.5 px, round caps, round joins, no filled outlines for line work
Grid:       24×24 viewBox, 2 px padding, optical centre
Colour:     single currentColor; no hard-coded greys
Deliver:    one frame per icon, layers grouped by path, ready for Motion if needed
Never:      drop shadows, gradients, emoji style, mismatched weights across the set
First pass: make only search / copy / link so we can compare strokes before the rest
```

## How UI Hub helps

For SVG workflows that start outside Figma, see 
AI SVG for UI with Ideogram Vector
. Shaders that now travel into code layers are covered in 
Figma shaders GA
. Broader agent-on-canvas context sits in 
Figma Make and the Figma agent
 and 
code layers and Specs
. When the destination is code you already ship, 
design on running code
 is the matching workflow post.

## References
- [Improvements to agent-generated vector illustrations and icons (5 Nov 2026)](https://www.figma.com/release-notes/) — Figma release notes
- [Generate and edit vectors with Figma AI](https://help.figma.com/hc/en-us/articles/38031452710807-Generate-and-edit-vectors-with-Figma-AI) — Figma Learn
- [Figma’s agent now draws in strokes, so the line weight stays yours](https://artdirectiondaily.com/issues/2026-11-05-figma-agent-draws-in-strokes.html) — Art Direction Daily
- [AI Vector Illustrations in Figma: the agent finally draws clean](https://www.mazette.co/en/blog/ai-vector-illustrations-in-figma-the-agent-finally-draws-clean) — Mazette.co
- [stroke-linecap](https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/stroke-linecap) — MDN Web Docs
- [vector-effect](https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/vector-effect) — MDN Web Docs
- [Workflow lab: Test ideas with code layers and the Figma agent (4 Nov 2026)](https://www.figma.com/blog/workflow-lab-build-with-code-on-the-canvas-using-the-figma-agent-and-code-layers/) — Figma Blog
- [Design Tools news (RSS checked 6 Nov 2026)](https://designtools.fyi/news) — designtools.fyi