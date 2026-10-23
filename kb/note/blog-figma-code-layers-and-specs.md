# Figma code layers and Specs: the canvas becomes the shared context again

> At Config India (15 Oct 2026) Figma moved code layers into open beta, launched Specs as a Markdown home on the canvas, and let libraries carry guidelines and code sources. The lesson for UI builders: agents are short of constraint files, not generators.

Blog post: <https://ui.incidental.site/blog/figma-code-layers-and-specs/>

On 15 October 2026, at Config India in Bengaluru, Figma shipped a set of updates that are easy to read as “more AI features” and more useful to read as a single idea: put the code, the written intent and the design-system rules on the same canvas, so people and agents work from one context instead of five tabs. Dylan Field’s recap post frames the problem bluntly. AI made code cheap, so teams “build to think”, but that vibe-coding loop is usually single-player; one customer is quoted describing it as “fast, fast, fast… then slow”.

## What launched

- **Code layers, open beta on all plans.** A code layer is a running, interactive prototype that sits on the canvas. You can start one from scratch (Code tool or 
B
), convert selected frames with 
Build selection
, clone a connected GitHub repo, upload a local folder, push a prototype in from your coding tool through the Figma MCP server, or capture a live page with the Chrome extension. Teammates can duplicate a layer to try another direction, comment and annotate it, edit the code, ask the agent to merge the best parts of two versions, pull screens back out with 
Extract designs
, and push to a branch and open a pull request.

- **Specs, open beta on paid plans.** A multiplayer Markdown container that lives as its own file or next to designs in Figma Design and FigJam (press 
D
, or drop any `.md` file on the canvas). A spec can embed frames, FigJam boards and other canvas nodes, the Figma agent can read and reply to comments, and connectors such as GitHub and Hex can pull outside context in. Paste a spec link into a coding agent’s prompt and, according to Figma, the Markdown, frame references, diagrams, code layers and Code Connect snippets travel with it.

- **Design systems that carry rules and code.** Guidelines attached to published libraries (open beta, Professional and above) are handed to the agent automatically whenever someone builds with that library. Code sources (closed beta) attach a GitHub repo or npm package to a library so code layers pull from real components. A centralised design-system space with a system map and a “system check” for gaps such as missing descriptions or interactive states is preview only.

- **Figma MCP.** Figma says the server is now faster and uses fewer tokens; it can create code layers, read and write Specs, generate images and run Weave workflows, and adds tools such as `html_to_figma` and `generate_image`, plus 20 new partner integrations (OpenCode, Dia, Junie, Meta Muse and others).

- **Payload in Figma Make.** Make now scaffolds a Payload backend (CMS, database, auth, APIs, admin panel) as its native backend; Supabase stays available as a third-party connection.

## Why it matters: three shifts

**Prototypes go back to multiplayer.** The real cost of coding-agent prototypes has not been generation; it has been review. A link to a running demo shows the result but hides the alternatives and the reasoning. Putting several running versions side by side on a canvas, with comments pinned to them, restores the critique loop design teams already know. The branch-and-PR exit matters too: the prototype has a route into the repo rather than being rebuilt.

**Markdown finally gets an address.** Most teams working with agents already keep PRDs, `AGENTS.md` files and prompt notes in Markdown, scattered across laptops and repos with no link to the screens they describe. Specs is Figma’s bet that the brief should sit beside the frames, be editable by both humans and agents, and be passable to a coding agent by URL. Whether or not you adopt Specs, the pattern is right: one canonical brief, versioned with the work.

**Design systems become agent-readable.** Guidelines and code sources are the most consequential part of the launch and the least flashy. A library that ships its own do/don’t rules and points at the real npm package turns “please match our design system” from a hope into an input the agent receives every time.

## Our take

The scarce input in AI-assisted UI is still the constraint file. Every tool this month, from Claude Design’s design systems to the Figma agent’s guideline files, has converged on the same lesson: generation is abundant, and quality comes from short, explicit rules about tokens, states and what never to do. Figma is now giving those rules a native place to live and an automatic route to the agent. Teams that already wrote a tight guideline file will see the benefit immediately; teams that skipped it will get faster, on-brand-looking noise.

Two caveats. First, these are betas with staggered rollouts, so features may appear for one teammate before another. Second, cost: code layers use AI credits, free for creating and editing on paid plans only until 4 November 2026, and guidelines can make a prompt more expensive because they add context. Figma’s customer numbers (for example, Merkle reporting 30% faster iteration) are vendor-published snapshots, not independent benchmarks.

## How to try it this week

- **Pick one flow, not a product.** Convert a single real flow (sign-up, checkout, settings) into a code layer from existing frames or a lightweight prototype repo. Duplicate it once to compare two directions.

- **Write a short Spec next to it.** Tokens to use, states that must exist, content rules and a never-list. Keep it to one screen of text so it is actually read.

- **Add guidelines to the library.** Move your do/don’t pairs onto the published library so every agent prompt against it inherits them. If you are in the code-sources beta, attach the npm package your product really ships.

- **Wire MCP from your coding agent.** Connect Claude Code, Cursor, Codex or similar to the Figma MCP server, paste the spec link into the prompt, and let the agent create or update the code layer.

- **Review on canvas like a pull request.** Check empty, loading and error states, long text, keyboard focus and contrast, at 390px and 1440px, before anyone says “ship it”. Then push to a branch.

```
# Spec: Checkout v2
## Tokens
surface / text-muted / accent only; radius 10; Geist 14/20
## States (must exist)
empty cart · loading · card declined · success · long names
## Content
real prices, real error copy; sentence case
## Never
text gradients · emoji icons · placeholder-only labels · raw hex
## Done when
390 + 1440 · light + dark · focus visible · AA contrast
```

## Where UI Hub fits

If you are writing that guideline file or Spec from scratch, start from the design skills and agent guides already collected on UI Hub: filter the resource list by 
skills
 for SKILL.md-style rule files, and see the 
Agents guide
 for the search, pick and verify loop that pairs well with an MCP-connected coding agent. The point is the same whichever canvas you use: give the agent the rules before you ask it for pixels.

## References
- [Build by design: New workflows for new ways of building](https://www.figma.com/blog/build-by-design/) — Figma (Dylan Field)
- [Design together with code layers on the canvas](https://www.figma.com/blog/design-together-with-code-layers/) — Figma
- [Introducing Specs: Markdown as a medium](https://www.figma.com/blog/introducing-figma-specs/) — Figma
- [What's new from Config India 2026](https://help.figma.com/hc/en-us/articles/43663368947863-What-s-new-from-Config-India-2026) — Figma Help Center
- [Code layers in Figma Design](https://help.figma.com/hc/en-us/articles/44193259600535-Code-layers-in-Figma-Design) — Figma Help Center
- [Guide to Specs in Figma](https://help.figma.com/hc/en-us/articles/44049066011671-Guide-to-Specs-in-Figma) — Figma Help Center
- [Guide to the Figma MCP server](https://help.figma.com/hc/en-us/articles/32132100833559-Guide-to-the-Figma-MCP-server) — Figma Help Center
- [Here's everything from Config India 2026](https://forum.figma.com/product-updates-3/here-s-everything-from-config-india-2026-59008) — Figma Forum
- [Figma deepens investment in India with largest international Config yet](https://www.figma.com/blog/figma-deepens-investment-in-india/) — Figma