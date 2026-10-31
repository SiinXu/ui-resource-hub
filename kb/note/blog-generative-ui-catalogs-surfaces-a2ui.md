# Generative UI gets a design system: CopilotKit catalogs, surfaces and A2UI 1.0

> On 29 October CopilotKit shipped a 70-component catalog, page “surfaces” and a markdown mode for generative UI, all on Google’s A2UI 1.0 protocol; two days earlier Google added A2UI Express, a compact format that cuts tokens up to 3×. The shift for designers: when an agent builds screens, the component catalog becomes the design system’s contract. What changed, what it means for UI teams, and a checklist for a catalog agents can’t break.

Blog post: <https://ui.incidental.site/blog/generative-ui-catalogs-surfaces-a2ui/>

For two years “generative UI” mostly meant a chatbot that sometimes drew a chart inside its bubble. This week it grew up. On 29 October CopilotKit released a large upgrade to its generative UI layer: a standard catalog of 70 components, **surfaces** that let an agent render into named areas of your actual page, and a markdown mode where text and components stream in the same answer. Underneath sits **A2UI**, the open protocol Google started (with CopilotKit and others contributing), whose 1.0 spec is now a release candidate. Two days earlier Google’s A2UI team shipped a faster way for models to write it. Read together, these releases move an important decision from engineers to design-system owners: 
which components an agent may use, where, and with what props
.

## What shipped this week

- **A standard catalog of 70 components.** Layout, text, form inputs, tables, images, video, charts (built on Recharts) and maps (built on MapLibre), plus ready-made blocks such as link previews, citations, product cards and follow-up suggestions. CopilotKit says 18 of them are A2UI’s basic components and 52 are its own.

- **Your components, typed.** You register your own with `createGenerativeUI`: each entry has a description the agent reads to decide when to use it, and a props schema (Zod, Valibot or ArkType). Three switches decide how your catalog sits next to the standard one: `extends` keeps both, `omit` removes components so the agent never sees them, and `overrides` replaces a standard component with yours.

- **Surfaces outside the chat.** Wrap any area in `GenerativeUISurface` with an id, a plain-language description of what belongs there, a list of allowed components and a fallback (your normal hand-built UI). The agent only sees a target while it is on screen; anything outside the allowed list is rejected and the agent is told why.

- **Two streaming modes.** Tool mode (the default) sends UI through a tool call and renders it piece by piece; markdown mode lets the agent write UI straight into its reply. Sliders, live values and form checks run in the browser, so interacting with generated UI costs no extra tokens.

- **Guardrails and debugging.** Every piece is checked against the catalog before it renders, generated UI never executes code on your page, each component gets its own error boundary, and a new Inspector pane shows what rendered, what was rejected and the exact prompt the model saw. CopilotKit labels all of this experimental until A2UI 1.0 is final.

## Why A2UI matters to designers

A2UI’s core idea is simple: an agent does not send HTML or code, it sends a 
declarative description
 of components from a catalog the client has approved, and the client renders them with its own native widgets (renderers exist for Angular, Flutter, Lit, React and markdown). That makes the catalog the only vocabulary the agent has. On 27 October Google added swappable “inference formats”: the model can write **A2UI Express**, a compact line-by-line syntax that the SDK compiles into standard A2UI messages. Google reports up to 3× fewer tokens and up to 3× lower latency than writing the JSON directly, and much bigger speed-ups when a small decision model only picks between layouts you designed in advance. The detail that matters for design quality: both the prompt and the compiler are generated from your catalog schema, so a format cannot describe a component or property your catalog does not have. On 30 October the project also published its first CLI, which generates typed builders from catalog schemas.

## Our take

This is the right shape for agent-built interfaces, and it changes who owns the result. When an agent can only compose from a typed catalog, “on-brand” stops being a hope you put in a prompt and becomes a property of the system: the agent literally cannot emit a neon gradient button if no such variant exists. The flip side is that every weakness in the catalog becomes visible. A vague description (“a card”) makes the agent pick it for everything; a free-text `variant` prop invites invented styles; a surface without a good fallback leaves a hole when the model is slow or wrong. So the craft moves upstream: designers should write component descriptions like usage guidelines, keep prop types narrow, and design the empty, streaming and error states of every surface, because those are now part of the product. Two caveats: the CopilotKit API is explicitly experimental, and the speed numbers are vendor-reported best cases, so pin versions and measure on your own screens.

## Checklist: a catalog an agent can’t break

- **Start narrow.** Give each surface only the components it needs (`components` or `omit`); a product row should accept product cards, not sliders. Smaller lists also mean smaller prompts.

- **Override the basics.** Replace the standard Button, Card and Input with your own so tokens, radii and focus styles come from your system, not the library default.

- **Write descriptions as rules.** Say when to use a component, when not to, and what to use instead. The agent reads these on every run.

- **Type props tightly.** Enums for variants and tones, numbers for numbers, length limits for labels. Free strings are where invented styles come from.

- **Design the fallback first.** Every surface should render your real hand-designed UI until the agent takes over, and again after it lets go.

- **Design the in-between states.** Streaming skeletons, a per-component error fallback, and what the area looks like when the agent removes its surface.

- **Keep user input sacred.** Values the user typed should never be overwritten by the agent; check that your setup enforces it.

- **Theme with tokens and test dark mode.** Generated screens should pass the same contrast checks (4.5:1 for body text) as hand-built ones.

- **Read the rejections.** Review what the Inspector rejected each week: a repeated rejection means a missing component or a misleading description, not a bad model.

- **Match the mode to the screen.** Fixed layouts are faster as predefined templates chosen by the agent; reserve free composition for screens that really vary.

```
StatCard
  use when:  the user asks about one metric over a period
  not for:   more than 4 numbers (use Table) · trends (use LineChart)
  props:     label: string ≤ 24 · value: number · delta: number
             tone: "up" | "down" | "flat"
  tokens:    surface/raised · text/muted · accent only when tone = "up"
```

## How UI Hub helps

A good catalog starts from named values: 
design tokens for agents
 covers writing them down, and 
linting agents onto your design system
 covers catching one-off values afterwards. For the chat side of agent interfaces (steps, tool calls, code output), see 
shadcn Trace and AI Elements
; for approval and interruption patterns when an agent acts on a page, see 
agent approval UI
. The component pages on UI Hub are a useful shopping list when you decide what belongs in your catalog.

## References
- [New in Generative UI: Catalogs, Surfaces and Markdown Mode](https://www.copilotkit.ai/blog/new-generative-ui) — Anmol Baranwal and Eli Berman, CopilotKit Blog
- [Surfaces](https://docs.copilotkit.ai/generative-ui/components/surfaces) — CopilotKit Docs
- [Catalogs](https://docs.copilotkit.ai/generative-ui/components/catalogs) — CopilotKit Docs
- [Standard catalog](https://docs.copilotkit.ai/generative-ui/components/standard-catalog) — CopilotKit Docs
- [Generative UI shop example](https://github.com/CopilotKit/CopilotKit/tree/main/examples/v2/generative-ui-shop) — CopilotKit, GitHub
- [A2UI: a generative UI protocol for cross-platform agentic experiences](https://a2ui.org/) — A2UI project
- [Fast, reliable A2UI, with swappable inference formats](https://developers.googleblog.com/en/fast-reliable-a2ui/) — Vishal Motwani, Google Developers Blog
- [A2UI Express technical specification](https://a2ui.org/specification/proposals/express/a2ui_express/) — A2UI project
- [A2UI CLI v0.1.0 release](https://github.com/a2ui-project/a2ui/releases/tag/cli-v0.1.0) — a2ui-project, GitHub
- [Generative UI timeline](https://ag-ui.ai/en/timeline) — AG-UI.AI