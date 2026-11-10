# Adobe MAX 2026: when agents edit your layered files, file hygiene becomes the interface

> At MAX on 10 November 2026 Adobe previewed local MCP integrations that let outside agents change Photoshop, Illustrator, Premiere and After Effects files with layers left editable, added Plan Mode to the Firefly AI Assistant, and put Firefly Builder, a prompt-to-prototype tool, in private beta. What was announced, what is not shipping yet, and a checklist for getting files and brand rules ready for agents.

Blog post: <https://ui.incidental.site/blog/adobe-max-2026-agents-keep-layers-editable/>

Adobe opened MAX in Miami Beach on 10 November 2026 with a long list of agent features. Most of them are about Adobe’s own assistant. The one that matters most for designers is about other people’s agents: Adobe previewed **local MCP integrations** that let an outside agent, such as one from OpenAI, Google or Anthropic, make changes directly in Photoshop, Illustrator, Premiere and After Effects project files on your own computer, with layers, vectors, bins and sequences still editable afterwards. That is not shipping yet. Adobe says a private beta starts in early 2027. But it tells you where the work is going, and the preparation is mostly about your files, not about the tools.

## What was announced

- **Local MCP integrations (preview).** MCP, the Model Context Protocol, is the open standard many assistants use to call outside tools. Adobe’s version runs locally against native project files. Coverage across the announcements is consistent: Photoshop, Illustrator, Premiere and After Effects, edits stay editable, and the agent can chain other MCP tools, for example pulling a brief from Google Docs and posting results to Slack. An Adobe vice president told TechCrunch the company is still deciding which capabilities to expose and will follow how people use it.

- **Plan Mode in the Firefly AI Assistant (beta).** You review, edit and approve the agent’s plan before it runs a multi-step task. A Model Selector lets you pick the model or leave it on auto. The assistant can now store preferred formats, colours, brand guidelines, characters and products and apply them to every project.

- **Firefly Builder (private beta).** A natural-language tool that turns an idea into an interactive, on-brand prototype of a website, presentation or app, with no code. TechCrunch framed it as Adobe moving into Figma’s territory; Creative Bloq noted Adobe’s claim that it stays on your design system, and said that is the claim to test first.

- **Always-on agents (preview).** Agents that keep doing recurring work in the background, such as organising incoming assets, checking quality and preparing channel versions, and come back for your review. Adobe says these arrive in the Firefly AI Assistant first, with no date.

- **Brand Intelligence goes into the editors.** Adobe’s brand-checking agent gains Intelligent Reflow, which adapts a design to new sizes and layouts, and is coming to Photoshop, Illustrator and InDesign. Firefly also gets a beta design canvas (Firefly Design) and Firefly Graph for saved, repeatable workflows.

## Our take: a named layer is now an API

When a person opens your file, they can cope with “Layer 47 copy 3”. An agent working through MCP cannot see what you meant; it sees names, groups, artboards, swatches and text frames. If those are tidy, “swap the hero photo on every social size and keep the headline” is one clear instruction. If they are not, the agent will guess, and a wrong guess inside a native file is harder to spot than a bad generated image, because it looks finished. So the first job is boring: name things the way you name components in code, group by function, keep text as live text and brand colours as library swatches.

The second point is the output contract. “Layers stay editable” is the important promise in this release, and it is also what you should check every time. A tool that flattens a layer, outlines text or rasterises a vector has handed you a picture, not a file. Make “still editable” part of review, next to “looks right”.

Third, approvals. Plan Mode is the right default for anything multi-step, and it is the same pattern we argued for in 
approval UI for agents
: read the plan, cut the steps you did not ask for, then run. Always-on agents raise the stakes, because nobody is watching when they work. Give them a review queue, never a publish button.

Finally, Builder. Every prompt-to-prototype tool says it is on-brand; most drift on the first unusual request. Before you trust it, or any rival, run the same small set of awkward prompts and count what leaves your system: new colours, new radii, components you do not have.

## Checklist: get your files ready for agents

- **Name layers and artboards like components.** “hero/photo”, “hero/headline”, “cta/primary”. No “copy 3”. Group by function, not by when you made it.

- **Keep brand rules in one place.** Colours, type and logo rules as library swatches and styles, plus one short written guideline. Load that into the assistant’s preferences instead of retyping it in every prompt.

- **Lock what must not change.** Logos, legal text and approved photography on locked layers, and say in the prompt that locked layers are off limits.

- **Turn on plan approval.** For multi-step jobs, read the plan first. Reject any step that touches files, layers or channels you did not name.

- **Work on a copy, then compare.** Duplicate or version the file before an outside agent edits it, and compare the layer list afterwards: what was added, renamed, flattened or deleted.

- **Check that output is still editable.** Live text, vector paths, smart objects and adjustment layers, not a flattened bitmap. Treat a flattened result as a failed run.

- **Stress-test “on-brand” claims.** Five awkward prompts (a dense table, an error state, a long German headline, a dark theme, a new component) and count anything off-system.

- **Give background agents a queue.** Always-on work lands in a review folder with a daily check, a spending limit and an easy off switch.

- **Scope every connection.** Which apps and folders an agent may touch, which MCP tools it may chain, and a log of what it changed.

```
# Paste this to your design agent (before any MCP edit)
Work only on the duplicate file I name; never the original.
Before running, write a numbered plan and wait for my approval.
Target layers by name. Do not touch locked layers or anything
named logo/*, legal/*, or approved/*.
Keep text as live text, vectors as paths, smart objects intact.
Use only colours and type styles from the linked brand library.
When done, list every layer you added, renamed, moved, flattened
or deleted, and anything you could not do.
```

## What to do this week

Nothing here needs the beta. Pick one real campaign file, clean its names and groups, move its colours into a library, and write the one-page guideline. That file will work better with Adobe’s assistant, with Figma’s agent and with whatever MCP client you use next year. If you already keep tokens for your product UI, point the guideline at them so print, social and product share one source.

Related on UI Hub: 
lint agents onto your design system
, 
keep AI design work portable
, and 
design tokens for agents
.

## References
- [Adobe brings AI agents and new creative tools to Photoshop, Premiere, and Firefly](https://techcrunch.com/2026/11/10/adobe-adds-more-ai-to-its-products-and-launches-an-mcp/) — Ivan Mehta, TechCrunch
- [Adobe is going all in on agentic AI](https://www.theverge.com/tech/1030593/adobe-max-ai-agents-mcp-firefly-assistant-updates) — Jess Weatherbed, The Verge
- [Adobe Firefly is now a creative studio, and it means AI is everything everywhere all at once](https://www.creativebloq.com/news/adobes-firefly-is-now-a-creative-studio-and-it-means-ai-is-everything-everywhere-all-at-once) — Ian Dean, Creative Bloq
- [Adobe Powers a New Era of Creativity, Bringing Agents and Tools to Creatives Wherever and However They Create](https://www.businesswire.com/news/home/20261110226769/en/Adobe-Powers-a-New-Era-of-Creativity-Bringing-Agents-and-Tools-to-Creatives-Wherever-and-However-They-Create) — Adobe via Business Wire
- [Architecture overview](https://modelcontextprotocol.io/docs/learn/architecture) — Model Context Protocol