# Open image models now draw UI drafts. Use the picture as a reference, never as the layout

> Ant Group’s inclusionAI open-sourced Ming-Image-0.2-Design this week, an MIT-licensed 6B image model aimed at UI drafts, hero images and posters, which the team says now leads open-weight models on a public text-to-image leaderboard. A picture of a screen is a tempting handoff and a bad one: the copy is invented, the text is pixels and nothing has states. The companion Ling UI Design skill shows the discipline that makes it useful: the brief owns copy and behaviour, the image only guides appearance, layers become assets rather than layout, and every build is rendered and compared. What to copy, where image models help in UI work and where they do not, a checklist and a prompt.

Blog post: <https://ui.incidental.site/blog/ui-mockup-image-models-reference-not-layout/>

On 25 November inclusionAI, Ant Group’s open model team, put the weights of **Ming-Image-0.2-Design** on Hugging Face and announced it a day later. It is a 6-billion-parameter diffusion transformer under the MIT licence, built for the pictures designers are asked for most: e-commerce hero images, posters, spatial renderings and UI design drafts. The model card says it handles complex composition, lighting and in-image text better than the 0.1 release from September, and inclusionAI reports that on 25 November it ranked first among open-weight models on Artificial Analysis’s text-to-image leaderboard (AA-Image-T2I v2.1, 1,095 Elo, ahead of FLUX.2 [max] and Qwen-Image-2.0 in the team’s own chart). That ranking is the maker’s claim, and leaderboards move weekly, so read it as “good enough to try”, not “best”.

The interesting part for UI work is not the leaderboard. It is that the release ships with a way of working: a structured prompt format, a model that splits a flat design into layers, and an MIT-licensed agent skill, **Ling UI Design**, that turns a generated or supplied screen image into real front-end code. Read together, they are a clear answer to a question every team using image models for interfaces runs into: what is the picture actually for?

## What shipped, in practical terms

**The model.** Defaults are 2048 × 2048 output, 12 sampling steps and CFG 1.0, with 2K buckets for 16:9, 4:3 and 2:3. inclusionAI validated it on a single CUDA GPU with 80 GB of memory in BF16, served through vLLM-Omni, so most teams will reach it through a hosted API rather than a laptop. **The prompt format.** Plain sentences work, but the team recommends a Figma-style JSON caption: `canvas_settings` (aspect ratio, lighting, style) plus a list of `layers` from back to front, each with a description, coordinates, its relation to other layers and hex colours. Any text to render is quoted verbatim, once. **The layer model.** Ming-Image-0.1-Design-Layer turns a flattened design into separate transparent PNG layers; inclusionAI says a finer version is due next week. **The skill.** Ling UI Design wires the image model and the layer model into a coding agent, with a default 4-layer split into text, image, container and background.

## The workflow worth copying

- **The brief comes first and stays in charge.** The agent reads the repository, the brief, the required views and the target viewports before any image is made, and keeps the existing stack.

- **Get one usable reference.** Either the person supplies screenshots, or the agent generates a page image in a chosen visual direction. It retries only for structural defects such as the wrong page type, a collapsed layout or the wrong mood, names the defect each time, and stops after three attempts. Wrong copy or a missing section is not a reason to regenerate: those get fixed in code from the brief.

- **Turn the image into assets, not layout.** Decompose once, crop candidate assets, inspect every one, and record each material raster region as accepted, refined, generated or omitted. An unresolved region blocks the build. A gradient, a flat fill, an emoji or the whole screenshot is never allowed to stand in for a real asset.

- **Write down the layout before writing code.** Region order, column proportions, spacing, heading wraps, type scale and colours go into a short checklist, then text, controls, layout and simple icons are built in code.

- **Render, compare, fix the biggest mismatch, repeat.** Capture the requested viewports, fix the largest structural, asset, type, overflow or interaction difference, and capture again, with a ceiling of five cycles so polishing does not run forever.

## Why a picture of a screen is a bad handoff

A generated screen looks finished, which is exactly the problem. Its copy was invented by the model, its text is pixels that a screen reader cannot read and a translator cannot change, its spacing is approximate rather than on your scale, and it shows one state of a component that in real life has hover, focus, loading, empty and error states. Traced pixel for pixel, it also locks in the model’s defaults: the centred hero, the three soft cards, the single purple button. The Ling UI Design skill guards against this with an explicit order of evidence: the brief, supplied screenshots and supplied assets first; the selected generated image second, for appearance only and never as the source of copy; a screenshot of the current build third; decomposed layers last, because they can overlap, drop content or invent hidden pixels. When two sources disagree, the higher one wins.

## Our take

Image models are becoming a normal step in front-end work, and an MIT model that a team can self-host makes that step cheaper to automate. The useful shift is in what the agent is allowed to take from the picture. Taking colour, mood, density, hierarchy and real raster assets is a fast way past the blank page. Taking copy, structure for screen readers, component behaviour or the exact layout is how AI-flavoured, inaccessible pages get shipped. Put that boundary in writing, in the skill or in `AGENTS.md`, and give the agent hard stopping rules, because “regenerate until it looks right” is the most expensive loop in the workflow.

## Where image models help in UI work, and where they do not

- **Use them for direction:** two or three mood boards or page studies before anyone commits to a layout. Figma’s image tools added multi-model, multi-image generation on 18 November for the same reason.

- **Use them for raster assets:** hero art, product shots, illustrations and empty-state pictures, cut out from layers and saved at a defined slot size.

- **Use them as a review target:** a reference makes “the hero feels heavier than the mockup” a checkable statement.

- **Do not use them for copy:** every word on the page comes from the brief or a writer, then is localised in code.

- **Do not use them for components:** buttons, inputs, tables and charts come from your design system with real states and real data.

- **Do not ship text inside images:** headings and labels in pictures fail translation, search and accessibility checks.

## Reference-first UI checklist

- Is the brief, not the mockup, the source for every word on the page?

- Is the reference stored in `artifacts/` and kept out of the shipped bundle?

- Does every raster region on the page have an outcome: accepted, refined, generated or omitted?

- Are there zero full-screen screenshots, gradients or emoji standing in for real assets?

- Are buttons, inputs and icons real elements from your component library, with focus and disabled states?

- Was the build rendered at every target viewport and compared with the reference, in light and dark?

- Are retries capped (three for references, five for render-and-fix) and are the reasons logged?

- Are API keys read from the environment and kept out of prompts, logs and the repository?

```
# Paste into a coding agent, with the brief and one reference image attached
Build this page from the brief, using the image only as a visual reference.
1. Write down from the brief: every heading, label and paragraph, the views,
   the target viewports (375, 768, 1440) and the components we already have.
2. From the image, take only: colours, type scale, spacing rhythm, density,
   region order and column proportions. Record them in notes/reference.md.
3. List every raster region (photos, illustrations). For each one, record
   accepted / cropped / generated / omitted and the slot size it will fill.
   Never use the whole screenshot, a gradient or an emoji as a stand-in.
4. Build text, controls and layout in code with our components and tokens.
   No copy from the image. No text inside images.
5. Render each viewport in light and dark, compare with the reference, fix
   the largest mismatch, and repeat at most 5 times. Report what still differs.
```

UI Hub related reading: 
layers, brand kits and JSON prompts for AI visuals
, 
visual prompts for UI edits
, 
comparing parallel design directions
, and 
putting the rules of a design agent in code
.

## References
- [Ming-Image-0.2-Design (model card)](https://huggingface.co/inclusionAI/Ming-Image-0.2-Design) — inclusionAI · Hugging Face
- [inclusionAI/Ming-Image (inference code, prompt format, layer decomposition)](https://github.com/inclusionAI/Ming-Image) — inclusionAI · GitHub
- [Ming-Image-0.1-Design-Layer (model card)](https://huggingface.co/inclusionAI/Ming-Image-0.1-Design-Layer) — inclusionAI · Hugging Face
- [Ling UI Design (README)](https://github.com/inclusionAI/ling-cookbook/blob/main/resources/recommended-skills/ling-ui-design/README.md) — inclusionAI · ling-cookbook on GitHub
- [Ling UI Design (SKILL.md)](https://github.com/inclusionAI/ling-cookbook/blob/main/resources/recommended-skills/ling-ui-design/SKILL.md) — inclusionAI · ling-cookbook on GitHub
- [Ant Group open-sources Ming-Image-0.2-Design: a design image model under MIT, validated on one 80 GB GPU](https://gpujournal.ai/story/ming-image-0-2-design-nov-26) — GPUJournal
- [inclusionAI open-sources 6B Ming-Image-0.2-Design under MIT licence](https://ashutoshai.com/ai-compass/2026/11/26/inclusionai-ming-image-0-2-design-mit/) — Ashutosh Shrivastava · AI Compass
- [New AI design tool releases](https://www.aipixtools.com/releases/) — AI Pix Tools
- [Text to Image leaderboard](https://artificialanalysis.ai/image/leaderboard/text-to-image) — Artificial Analysis
- [Figma release notes (Generate multiple images from a single prompt, 18 Nov 2026)](https://www.figma.com/release-notes/) — Figma