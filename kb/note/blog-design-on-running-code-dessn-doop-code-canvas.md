# Design on running code: Dessn, Doop and Figma turn the canvas into a place agents and designers share

> On 4 November Dessn launched a canvas that runs your real app from your repo, the open-source Doop canvas trended on GitHub, and a day earlier Figma’s code layers started reading prototype connections. Two kinds of agent canvas are emerging: frames that are your app, and frames that are loose HTML. How they differ, what to check before connecting a repo, and a checklist for designing on code.

Blog post: <https://ui.incidental.site/blog/design-on-running-code-dessn-doop-code-canvas/>

Three releases in two days point the same way. On 4 November **Dessn** launched on Product Hunt with a simple pitch: connect GitHub, GitLab or Bitbucket, and it renders your frontend one to one on a design canvas, with the backend mocked, so the team and their agents look at what is actually live. The same day the open-source **Doop**, a multiplayer canvas where people and AI agents edit HTML frames together, showed up on GitHub’s trending list. And on 3 November **Figma** said that when you turn design frames into a code layer, its agent now reads the prototype connections and interactions between them; it also made repository cloning the default for new GitHub connections.

None of these is “AI generates a mockup”. They are about where the design and the agent meet: a shared canvas that an agent can write to over MCP (the Model Context Protocol that lets coding agents call tools) and that a person can click through.

## Two kinds of agent canvas

- **Frames that are your app.** In Dessn, a frame holds the app’s codebase. Its agent guidance says a new page, state or variation is a copy of the app’s frame whose code the agent writes, that components should be reused or modified rather than recreated, and that the change goes home as a patch, commits or a bundle. Dessn also exposes the components and tokens the app really uses, with file and line. Figma’s code layers sit nearby: you can import a GitHub repo or convert frames, and now the prototype wiring travels with them.

- **Frames that are loose HTML.** Doop frames render HTML in sandboxed iframes. Agents connect over MCP with OAuth and work as you; its README lists 42 tools, including streaming a design into a frame section by section and taking a screenshot so the agent can review its own work. A built-in agent runs on GPT, Claude, Gemini, DeepSeek, Kimi or Qwen models. It is AGPL-3.0, self-hostable with an embedded Postgres, and calls itself an open-source alternative to Paper.

Dessn’s own docs draw the same line: real-app frames are what it is for, and HTML frames are for notes, annotations and visuals that are not a page of the app, such as an OG image or a moodboard.

## Our take

The difference matters more than the brand names. An HTML frame is a fast sketch: great for exploring five directions, but every one of them still has to be translated into your components, and that translation is where design systems drift. A frame that runs your code skips the translation, because the variation is already a diff against your app. The cost moves elsewhere: you are now connecting a repository, deciding what data the mocked backend shows, and reviewing a code change rather than a picture.

That shift also changes what a designer reviews. On a code canvas the useful questions are no longer “is this pixel right” but “did the agent reuse our Button, did it handle the empty and error states, and does the diff touch anything it should not”. Figma reading prototype connections is a small version of the same idea: the flow you wired becomes input for the code, so wiring the flow carefully is now part of the spec.

We would not pick one canvas for everything. Use an HTML canvas to explore directions quickly and cheaply, then move the winner onto a frame that runs your code before anyone calls it done.

## Checklist: designing on running code

- **Decide what the frame is.** Your app (code-backed) for anything that will ship; loose HTML for exploration, moodboards and one-off visuals. Label exploration boards so nobody treats them as spec.

- **Check repository access first.** Know which repos are connected, whether the tool only reads or also clones, and who can see them. In Figma, new GitHub connections now clone by default; admins can turn it off per repository.

- **Seed realistic mock data.** If the backend is mocked, make sure the canvas shows real-looking names, long strings, empty lists and error responses, not just the happy path.

- **Tell agents to reuse, not recreate.** Put “reuse or modify existing components; never rebuild one” in your agent rules, and run your design-system lint on every diff.

- **Wire the flow before you generate.** In Figma, connect the prototype frames and interactions first, since the code layer agent now reads them.

- **Review by clicking, then by diff.** Click through every state on the canvas, then read the patch: changed files, new dependencies, hard-coded colours.

- **Keep one source of truth.** After the change merges, refresh the canvas from the repo so the next round starts from production, not from yesterday’s frame.

- **Read the licence if you self-host.** Doop is AGPL-3.0: if you modify it and let others use it over a network, you must offer them your modified source.

```
# Brief for an agent working on a code-backed canvas
Goal:       add an empty state + error state to the Invoices page
Frame:      copy the live Invoices frame; do not start from blank HTML
Reuse:      EmptyState, Alert, Button from src/components (no new components)
Tokens:     colours and spacing from tokens.css only, no hex values
Data:       mock 0 invoices, 1 invoice, 240 invoices, and a 500 error
States:     loading · empty · error · long names · 375px width
Deliver:    playable frame + patch; list every changed file
Never:      touch API code, add dependencies, or change other pages
```

## How UI Hub helps

For the Figma side, read 
Figma code layers and Specs
. Pointing at a running app instead of describing it is covered in 
annotate, don’t describe
. To make agents reuse your components, use 
lint agents onto your design system
 and keep tokens readable with 
design tokens for agents
. 
GitHub Replica
 shows a related approach where reviewed design-system guidance drives prototypes.

## References
- [Dessn: the design canvas that runs your real code (Product Hunt launch, 4 Nov 2026)](https://hunted.space/product/dessn-2) — Hunted.space
- [Dessn](https://www.dessn.ai/) — Dessn
- [We built what you wished Figma could be (launch video)](https://posts.design/gabriella-we-built-what-you-wished-figma-could-2026-11-04) — Dessn, via posts.design
- [kgoedecke/doop](https://github.com/kgoedecke/doop) — kgoedecke, GitHub
- [Get started](https://doop.design/docs/get-started) — Doop
- [The design MCP for Claude Code](https://doop.design/design-mcp-for-claude-code) — Doop
- [doop open-source canvas lets AI agents design live with humans](https://www.notatechguy.com/doop-open-source-canvas-lets-ai-agents-design-live-with-humans/) — Marcello Babbili, Not a Tech Guy
- [Release notes: prototype connections as context for code layers; cloning by default (3 Nov 2026)](https://www.figma.com/release-notes/) — Figma
- [What’s new from Config India 2026 (code layers open beta)](https://help.figma.com/hc/en-us/articles/43663368947863-What-s-new-from-Config-India-2026) — Figma Learn
- [Paper](https://paper.design/) — Paper
- [Authorization](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization) — Model Context Protocol specification
- [GNU Affero General Public License v3.0](https://choosealicense.com/licenses/agpl-3.0/) — choosealicense.com