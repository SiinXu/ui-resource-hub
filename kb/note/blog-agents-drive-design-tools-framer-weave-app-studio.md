# Your design tools now take orders from agents: Framer MCP, Figma Weave and Runway App Studio

> In five days Framer opened its canvas and CMS to outside agents over MCP, Figma made every Weave image and video model callable from the Figma MCP, and Runway turned plain-language descriptions into shareable creative apps. Three different ways to put a creative tool behind an agent, what each one gates, our take, and a checklist for setting it up safely.

Blog post: <https://ui.incidental.site/blog/agents-drive-design-tools-framer-weave-app-studio/>

Until recently, an AI agent that wanted to change a website or produce a campaign image had two options: write code from scratch, or ask you to open the design tool yourself. Between 22 and 26 October three creative tools removed that gap in three different ways. Framer let outside agents edit its canvas and CMS, Figma let agents call Weave's image and video models through the Figma MCP, and Runway let anyone describe a creative app and get a working one. Each answers the same question, 
what may an agent do inside my creative tool?
, with a different gate.

## What shipped

- **Framer MCP (22 October).** Any client that supports remote MCP servers and OAuth, such as Codex, Claude or Cursor, can connect to `https://mcp.framer.com/mcp`. After you approve the connection, the agent can create pages and edit layouts across desktop, tablet and phone breakpoints using the project's existing styles and components, manage CMS collections and items, and review metadata, headings and alt text. It acts with your account's permissions. Changes stay in the project, or on a branch, until someone publishes; the agent can publish, but only if you explicitly ask. Framer's branches show a diff under Review Changes, and applying a branch to main is a separate step from publishing main.

- **Figma Weave through the Figma MCP (26 October).** With a paid standalone Weave account linked to Figma, an external agent can run a Weave model such as Seedance, Kling or Nano Banana directly, or run a published Weave tool, which is Weave's word for a published workflow such as a product-mockup generator. Runs spend Weave credits, not Figma AI credits. Before a paid run the tool returns a cost-confirmation status and the agent must show you the credit cost and get a yes; workflows whose cost depends on a dynamic iterator say up front that the cost can't be quoted. Private tools are invisible to agents, and creating or editing workflows over MCP is not supported yet.

- **Runway App Studio (26 October).** You describe a tool in plain language and Runway's builder agent plans, designs and deploys an app with its own interface that generates images, video and audio from your Brand Kits, Workflows and assets. Early in the build it asks you to pick one of three colour schemes and can take your logo. An app is a private preview until you publish it to yourself, your workspace or specific people; you can roll back to earlier versions, the code stays inspectable, and each app shows its own credit usage. Launch examples include Precise Edit, which retouches only the region you mark, and AutoComp, which swaps a product into existing footage.

## Our take

These are three rungs of the same ladder. At the bottom, the **agent drives the canvas** (Framer): it can touch anything you can, so the safety comes from where its work lands, a branch with a reviewable diff, and from publishing being a separate, explicit act. In the middle, the **agent calls a published workflow** (Weave): it cannot change how the asset is made, only fill in the inputs someone else designed, and every paid run passes a price check. At the top, the **workflow becomes an app for people** (App Studio): the agent's work is the tool itself, and the guardrails are the Brand Kit it reads, the audience it is published to and the version you can roll back to.

The practical lesson for design teams is that the valuable artefact is moving from the prompt to the published workflow. A prompt that produced a good hero image once is a note; a published Weave tool or App Studio app with fixed references, brand colours and a known cost is something an agent can be trusted to run a hundred times. Framer's version of the same idea is the project's own styles and components, which its agent is told to reuse. If your system is not packaged in one of those forms, outside agents will improvise, and that is where off-brand output comes from.

Two cautions. Framer's agent works with your account's permissions, so an agent connected to a personal account can reach every project that account can. And cost confirmation only protects you if someone reads it: batch runs (Weave allows one to ten per call) multiply quickly.

## Checklist: letting an agent into your creative tools

- **Pick the rung on purpose.** Use canvas access for layout and content edits, published workflows for repeatable assets, and an app when non-designers need to run the workflow themselves.

- **Branch by default.** Tell the agent to create a branch before every Framer task, turn on automatic branching to protect main, and review the diff and a branch preview URL before you apply.

- **Keep publish human.** Never include "and publish" in a standing instruction; publish main yourself after review.

- **Connect the narrowest account.** Use a workspace or account that only holds the projects the agent should touch, since it inherits that account's permissions.

- **Publish workflows, not prompts.** Wrap your best image or video recipe as a Weave tool or App Studio app with fixed references, Brand Kit and named inputs, so agents fill in blanks instead of inventing styles.

- **Set a credit ceiling.** Decide a per-run and per-week credit budget, keep `numberOfRuns` low until the output is proven, and treat "cost can't be quoted" as a reason to run once first.

- **Review assets like code.** Check every generated image or page in light and dark themes, at 375 px, for alt text and contrast, before it enters a library or CMS.

- **Log what the agent made.** Keep a list of agent-generated pages, CMS items and assets with the prompt, workflow version and credit cost, so you can find and replace them later.

```
# creative-agent-policy.yml: a starting spec
framer:
  connect: https://mcp.framer.com/mcp   # OAuth, workspace account only
  always_branch: true
  publish: human_only
  review: [diff, branch_preview_url, 375px, dark_mode]
weave:
  allow: published_tools_only           # no raw model runs in production
  confirm_cost: always
  max_runs_per_call: 2
  weekly_credit_budget: 500
app_studio:
  audience_default: only_me             # widen after review
  brand_kit: required
log: [page, cms_item, asset, prompt, workflow_version, credits]
```

## How UI Hub helps

An agent can only reuse styles that are written down. Our posts on 
design tokens for agents
 and 
linting agents onto your design system
 cover how to package them, and 
layers, brand kits and JSON for AI visuals
 covers the brand-kit side of generated images. For the approval step itself, see 
designing approvals for agents
; for Figma's other agent features, see 
Figma code layers and Specs
.

## References
- [Framer MCP](https://www.framer.com/updates/framer-mcp) — Framer Updates
- [Connect Claude, Codex and Cursor to Framer with MCP](https://www.framer.com/mcp/) — Framer
- [Getting started with Framer MCP](https://www.framer.com/help/articles/getting-started-with-framer-mcp/) — Framer Help
- [What you can do with Framer MCP](https://www.framer.com/help/articles/what-you-can-do-with-framer-mcp/) — Framer Help
- [How to use branches in Framer](https://www.framer.com/help/articles/how-to-use-branches-in-framer/) — Framer Help
- [Review Agent changes safely with Branching](https://www.framer.com/academy/lessons/branching-explore-variations-safely) — Framer Academy
- [Access video and image models from Figma Weave via the Figma MCP](https://www.figma.com/release-notes/) — Figma release notes
- [Figma MCP server FAQs](https://help.figma.com/hc/en-us/articles/39252411778583-Figma-MCP-server-FAQs) — Figma Learn
- [Tools and example prompts](https://help.figma.com/hc/en-us/articles/42495147242903-Tools-and-example-prompts) — Figma Learn
- [Running Weave tools and models from external agents (MCP)](https://help.weavy.ai/en/articles/16202764-running-weave-tools-and-models-from-external-agents-mcp) — Figma Weave Knowledge Center
- [Introducing Runway App Studio](https://runway.com/news/company-news/introducing-runway-app-studio) — Runway
- [App Studio: build your own creative apps](https://runway.com/product/app-studio) — Runway
- [Runway App Studio brings no-code app building to AI filmmaking](https://www.bottlerocketcontent.com/runway-app-studio-no-code-creative-apps/) — Bottle Rocket Content
- [Tools](https://modelcontextprotocol.io/specification/2025-06-18/server/tools) — Model Context Protocol specification