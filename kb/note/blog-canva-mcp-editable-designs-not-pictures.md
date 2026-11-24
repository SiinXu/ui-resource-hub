# Canva MCP is open to every agent: ask for an editable design, not a picture

> Canva made its MCP server generally available this week with no waitlist, rebuilt the toolset for agents, and added REST APIs, a CLI for bulk jobs and service accounts. The useful shift is in what comes back: a design with layers and an edit link instead of a flat PNG. How to choose between MCP, REST and CLI, what Magic Layers can and cannot rescue, how to design the handoff in your own AI features, plus a checklist and an agent prompt.

Blog post: <https://ui.incidental.site/blog/canva-mcp-editable-designs-not-pictures/>

Canva has made its MCP server generally available. Its newsroom post, dated 23 November, says there is no longer a waitlist: any developer can create an app in the Canva Developer Portal, switch on MCP and connect. The same release adds REST APIs for design generation, image generation, background removal and Magic Layers, a wider Canva CLI, service accounts with API billing, and access to Canva’s own image model, Craft. The Next Web picked it up the next morning, and posts on X were already showing chat assistants returning layered Canva files instead of images.

The numbers Canva shared explain why it is pushing: nearly 500,000 people signed up for Canva through MCP since October, MCP usage rose 93% from September to October, and 72% of the commands typed into the Canva CLI in October came from agents. For people who design or build interfaces, the interesting part is not the growth. It is the shape of the result. An agent that used to hand back a picture now hands back an object you can open, edit, comment on and resize.

## What changed in this release

- **Open access, per-user sign-in.** MCP now has no waitlist. Each person still signs in with their own Canva account, and the tools only do what that account is allowed to do. Canva’s docs say MCP does not support organisation-level or service-account sign-in.

- **A smaller, clearer toolset.** Canva says it merged overlapping tools so agents, even on smaller models, choose the right one with less context. The public tool list covers generating design candidates, editing through draft transactions, resizing, autofilling templates, separating a flat image into layers, comments and exports to PDF, PNG, JPG, PPTX and MP4.

- **Three ways in.** MCP lets the agent decide the steps. REST APIs give fixed, predictable calls inside your own product, and with service accounts your users do not need Canva accounts while you pay per job from a credit pool. The CLI gives coding agents one focused command at a time, with one JSON object per call on standard output, which suits bulk and repeated jobs.

- **Editing in the chat.** In ChatGPT and Claude, Canva’s connector now opens an editing side panel for text, images and layout, with one click into the full editor. Video generation follows the same idea: you approve a timed production plan before anything is generated, and the result lands on an editable timeline.

## Our take: the edit link is the deliverable

We have argued before that AI design is moving from generating to editing. This release turns that into an interface contract. Canva’s own developer guidance is unusually direct about it: after any tool touches a design, return the edit URL and tell the user they can open it, show candidates instead of auto-picking one, report success only after the tool confirms it, and treat thumbnail and export links as short-lived. That is good advice for anyone building AI features, not only Canva partners.

The same day, Figma made its agent generally available in FigJam and Slides on paid plans, pitching boards turned into a Spec that “your team, and your agents, can act on”. Two of the biggest design tools are converging on the same idea: the agent’s output should be a live file in the tool where people already review work. A flat image ends the conversation. A layered file with a link starts the next round of edits.

Two cautions. First, Magic Layers is a rescue tool, not a source format. Canva says it is built for flat, non-photographic graphics such as posters, banners and social posts, does not accept SVG or EPS, and its REST version is still a preview API that public integrations cannot ship with. If you already have the layered source, use it; do not export to PNG and ask a model to guess the layers back. Second, decide who owns the account before you build. MCP acts as each signed-in user, REST service accounts act as your app, and those choices decide who sees the files, who pays and what plan features exist: autofill, brand kits and resizing need Canva Pro or above.

## How to choose the path

- **Your users chat with an assistant and already have Canva:** use MCP. Send the full brief, not a summary, and let the user choose between candidates.

- **Your product generates assets for users who may not have Canva:** use REST with a service account. Budget per job from Canva’s credit table, for example 10 credits per autofilled page, 3 per CRAFT-1 2K image and 1.7 per page through Magic Layers. Failed jobs refund their credits.

- **A coding agent runs a batch:** use the CLI. Run `--dry-run` first, pipe the JSON into `jq`, and keep the design IDs it returns.

- **Someone sends you a flattened poster:** separate it into layers, then check every text box before you trust the result.

## Editable handoff checklist

- Does every design-touching step return an edit link with a short, clear call to action?

- Are several candidates shown for the person to pick, rather than the agent choosing silently?

- Is “done” shown only after the tool confirms success, with progress shown during long jobs?

- Do edits stay in a draft until someone commits them, and does a failed commit start a fresh draft instead of retrying a stale one?

- Is anything destructive, such as refilling a template in place, behind an explicit yes? Canva notes that in-place autofill cannot be undone.

- After layer separation: is the headline live text in your brand font, is the background its own layer, and are any logos still sharp?

- Are preview and export URLs kept out of your database and out of shared messages?

- Does the result use the brand kit, not colours the model guessed, and is the plan tier that brand kits require actually in place?

```
# Paste this into an agent that has a design tool connected (Canva MCP or similar)
Make <asset> for <audience> in <format and size>.
Brief: purpose, key copy (exact text), tone, brand kit name, things to avoid.
Rules:
- Return 2–4 candidates with thumbnails and wait for me to pick one.
- Use live text and my brand kit fonts and colours. No text baked into images.
- Keep edits in a draft. Show me the changes, then commit only when I say yes.
- Never overwrite an existing design in place.
- When done, give me the edit link and list the layers: text, images, background.
- If you only have a flat image, separate it into layers first and tell me
  which parts could not be recovered.
```

Related on UI Hub: 
Canva Brush and the shift from generating to editing
, 
keeping layered files tidy for agents
, and 
keeping AI design work portable
.

## References
- [Building the design layer of the internet: opening Canva to every agent and developer](https://www.canva.com/newsroom/news/canva-mcp-update/) — Anwar Haneef · Canva Newsroom
- [Campaign-ready video generation, Magic Layers and several new ways to create with Canva + AI assistants](https://www.canva.com/newsroom/news/canva-mcp-video-generation/) — Canva Newsroom
- [Canva opens its design tools to AI agents and outside developers](https://thenextweb.com/news/canva-mcp-ai-agents-developers) — Ana Maria Constantin · The Next Web
- [How to use Canva MCP in your AI application](https://www.canva.dev/blog/developers/canva-mcp-ga/) — Meredith Hassett · Canva Developers Blog
- [Best practices for Canva MCP](https://www.canva.dev/docs/apps/mcp/best-practices/) — Canva Developers
- [Design edit handoff](https://www.canva.dev/docs/apps/mcp/workflows/design-edit/) — Canva Developers
- [MCP tools and rate limits](https://www.canva.dev/docs/apps/mcp/tools/) — Canva Developers
- [Access and permissions](https://www.canva.dev/docs/apps/mcp/access/) — Canva Developers
- [separate-image-layers](https://www.canva.dev/docs/apps/mcp/tools/separate-image-layers/) — Canva Developers
- [autofill-design](https://www.canva.dev/docs/apps/mcp/tools/autofill-design/) — Canva Developers
- [commit-editing-transaction](https://www.canva.dev/docs/apps/mcp/tools/commit-editing-transaction/) — Canva Developers
- [Create image-to-design import job](https://www.canva.dev/docs/apps/rest-apis/reference/design-imports/create-image-to-design-import-job/) — Canva Developers
- [Canva REST API credit rates](https://www.canva.dev/docs/apps/rest-apis/credit-rates/) — Canva Developers
- [Canva CLI](https://www.canva.dev/docs/apps/canva-cli/) — Canva Developers
- [The Figma agent is now available in FigJam and Slides](https://www.figma.com/blog/introducing-figma-agent-in-figjam-and-slides/) — Jinen Kamdar · Figma Blog
- [Canva launches Craft, its first in-house image model](https://the-decoder.com/canva-launches-craft-its-first-in-house-image-model/) — Maximilian Schreiner · The Decoder