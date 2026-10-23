# AI vectors for UI: what Ideogram Vector 1.0 changes, and the checks before an SVG ships

> On 22 October Ideogram shipped Vector 1.0, a model that writes editable SVG from a prompt or traces an image, joining Recraft V4.1 and QuiverAI Arrow 2. Editable is not the same as ready for an interface: what the three tools actually return, and a checklist for icons and illustrations.

Blog post: <https://ui.incidental.site/blog/ai-svg-for-ui-ideogram-vector/>

Most AI images reach an interface as a flat PNG: fine for a hero photo, useless for an icon that has to follow your theme colour, an empty-state illustration that must stay sharp on a 3x screen, or a logo you will resize forty times. On 22 October Ideogram launched Vector 1.0, its first model that returns SVG instead of pixels. It joins Recraft V4.1 and QuiverAI's Arrow 2, which already generate vectors. With three serious options, the question for UI work is no longer whether AI can draw a vector, but what it takes to make one ship.

## What shipped, and what the three tools return

- **Ideogram Vector 1.0 (22 October).** Two jobs under one model: text-to-vector, with optional reference images, three quality levels and a seed, and image-to-vector, which traces a JPEG, PNG or WebP up to 50 MB. It runs in the Ideogram app, through the API, and on partner platforms such as fal from day one. Ideogram pitches it for logos, wordmarks, print, labels, stickers and illustrations, and says each shape arrives as its own element you can recolour, move or resize. API prices on the product page run from $0.13 to $0.20 per SVG by quality ($0.32 at high quality with references) and $0.10 per image-to-vector conversion. One caveat from an early reading of the API reference: the vectorizer's layer-grouping option is listed as not yet available, so a traced image comes back as paths rather than neatly named groups. Its two modes trade fidelity against shape count: default keeps fine detail, simple draws fewer, cleaner shapes.

- **Recraft V4.1.** Generates SVG from a prompt for logos, icons and illustrations, converts raster images, and has a vector editor in Recraft Studio where you can move points, add tangents and recolour without leaving the canvas. Its docs note that the vector generation type does not take reference images.

- **QuiverAI Arrow 2.** A generally available model that does SVG generation, vectorization, editing and animation in one place, priced per token ($4 input and $20 output per million), with a larger Arrow 2 Telos at 50% higher rates. A third-party guide to it recommends prompts that name hex colours and one outline weight, say the drawing must read at 32 px, and rule out gradients, text and shadows, and notes that it is not meant for photographs.

The same day, Canva released Craft, its first image model, which writes a plan of the composition before rendering and uses that plan to turn images into editable layers. It still outputs pixels, but it points the same way: generated visuals are starting to arrive as structure you can edit, not a picture you have to redraw.

## Our take

For interfaces, editable is necessary but not enough. An icon that works in a product is a contract: a fixed grid (usually 24 by 24), one stroke weight across the set, colour taken from the surrounding text so it follows light and dark themes, a small file, and a clear role for screen readers. Generators optimise for a picture that looks good at full size. Nothing in the launches suggests they target those rules, so treat their output like a strong first draft from an illustrator who has never seen your icon set. The biggest win is in the middle of the range: empty states, onboarding spots, marketing illustrations and logo exploration, where a vector you can recolour to your tokens beats a PNG you cannot. For the core icon set, a maintained open library is still the safer default, with AI filling the gaps it does not cover.

Two practical warnings. Traced artwork can carry thousands of anchor points, which bloats pages and makes hand edits painful, so prefer the simple mode or a fresh generation for UI assets. And check the licence and output privacy for your plan before you put a generated mark into a product; Ideogram's docs say outputs are private by default, but terms differ between tools and tiers.

## Checklist: getting an AI SVG ready for an interface

- **Prompt for the system, not the picture.** Give the grid size, stroke weight, cap style, fill or no fill, the exact hex values from your tokens, and the smallest size it must read at. Ban gradients, text and shadows for icons.

- **Generate the set together.** Ask for several icons in one prompt, or reuse the seed and a reference, so weights and corner radii match. Mixed weights are the first thing users notice.

- **Prefer generation over tracing for UI.** Trace only when you must keep an existing drawing, and use the simplest mode that still looks right.

- **Clean the file.** Run it through an optimizer such as SVGO, keep the `viewBox`, drop editor metadata, and look at the path count before and after.

- **Hand colour to CSS.** For single-colour icons, replace fixed fills and strokes with `currentColor` so the icon follows text colour in both themes. For multicolour illustrations, map each colour to a CSS variable from your tokens.

- **Give it the right role.** Decorative icons next to a text label get `aria-hidden="true"`; a standalone meaningful graphic gets `role="img"` and a `<title>` or an accessible name on its button.

- **Check it small and in both themes.** View it at 16 and 24 px on light and dark backgrounds before you merge. If it only works large, it is an illustration, not an icon.

```
# 1. prompt for a UI icon, not a poster
"Six 24 px line icons for a finance app: wallet, card,
 receipt, chart, bell, lock. 2 px stroke, round caps,
 no fill, one colour #111827, no text, no gradients.
 Each must read at 16 px."

# 2. clean the file
npx svgo wallet.svg -o wallet.min.svg

# 3. let CSS own the colour and the role
<svg viewBox="0 0 24 24" fill="none"
     stroke="currentColor" aria-hidden="true">…</svg>
```

## How UI Hub helps

A generated vector only fits if your tokens exist first. Our posts on 
design tokens for agents
 and 
OKLCH colour and dark mode
 cover the colour side, and 
layers, brand kits and JSON
 covers the same "editable, not flat" shift for raster images. For accessible names and roles, see 
accessibility in AI-generated UI
.

## References
- [Ideogram Vector: ready-to-use SVG artwork](https://ideogram.ai/models/vector/) — Ideogram
- [Ideogram launches its first vector model for editable SVG design](https://runtimewire.com/article/ideogram-vector-1-svg-model-launch) — Ryan Merket, Runtime Wire
- [Ideogram Vector 1.0: Editable SVGs with an API layer caveat](https://www.orcarouter.ai/blog/ideogram-vector-1-0-release-editable-svg) — OrcaRouter blog
- [Ideogram Vector 1.0: Editable SVGs from a prompt](https://artrealmai.com/article/ideogram-vector-1-0-editable-svg-text-image-to-vector) — ArtRealmAI
- [Ideogram Vector text-to-vector API](https://fal.ai/models/ideogram/vector/text-to-vector/api) — fal
- [AI vector generator: text to SVG](https://www.recraft.ai/ai-vector-generator) — Recraft
- [Vector Editor](https://www.recraft.ai/docs/recraft-studio/image-editing/vector-editor) — Recraft docs
- [Arrow 2](https://quiver.ai/models/arrow-2/) — QuiverAI
- [Models](https://docs.quiver.ai/developers/models) — QuiverAI docs
- [Arrow](https://batchbanana.com/docs/models/arrow) — Batch Banana docs
- [Introducing Canva Craft](https://www.canva.com/newsroom/news/canva-craft/) — Canva Newsroom
- [Canva releases its first image generation model](https://techcrunch.com/2026/10/22/canva-releases-its-first-image-generation-model/) — Ivan Mehta, TechCrunch
- [SVGO](https://svgo.dev/) — SVGO
- [Decorative images](https://www.w3.org/WAI/tutorials/images/decorative/) — W3C WAI