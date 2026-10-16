# shadcn Trace and AI Elements: one shape for every step an agent takes

> On 14 Oct 2026 shadcn/ui shipped Trace, Code Block and 21 copy-in AI Elements patterns that replace AI SDK Elements. The design lesson: reasoning, tool calls, sources and subagents are all one line with an icon, a title and a status, so agent UIs stop looking like debug logs.

Blog post: <https://siinxu.github.io/ui-resource-hub/blog/shadcn-trace-and-ai-elements/>

On 14 October 2026 shadcn published **Trace**, a component for agent activity, together with **Code Block** and **AI Elements**, a set of patterns for agentic interfaces built entirely from shadcn/ui components. The announcement post passed 4,500 likes on X within two days, and shadcn-svelte followed with its own AI Elements a day later. The interesting part is not that there are new components. It is the design claim underneath them: reasoning, tool calls, sources, plans and subagent runs all have the same shape, so they should look and behave the same.

## What shipped

- **Trace.** A list of lines for the steps an agent takes. The shadcn team says it was distilled from studying hundreds of components in agentic interfaces. Each line has an icon, a title, an optional description and a status (`running`, `error` or `pending`, with a shimmer while a step runs). A line can expand, link to a page, or open a dialog, sheet, drawer or popover, and lines can nest, so a summary opens into steps and a step into its output. It reads the reasoning, tool and source parts that the AI SDK streams.

- **Code Block.** Displays code, terminal output, logs and diffs, with a header for a title and actions, line numbers, wrapping, highlighted and diff lines, and a small size (`size="sm"`) meant for tool output inside a Trace.

- **AI Elements, 21 patterns.** Chat, Prompt Input, Reasoning, Tool, Plan, Subagent, Confirmation, Context, Sources, File Tree, Terminal, Test Results and more. There is no package: each pattern is a composition you copy into your repo, and every docs page also exists as Markdown so a coding agent can read it directly.

- **Every base and style.** Trace and Code Block are available for Base UI, React Aria and Radix across all eight shadcn/ui styles, and they join the chat components released in June: Message Scroller, Message, Bubble, Marker, Attachment and Questionnaire.

- **AI SDK Elements is being deprecated.** Code you already copied from elements.ai-sdk.dev keeps working. Each pattern page has a migration prompt that rebuilds the wrapper in `components/ai-elements` on the new components while keeping every export and its props. A few low-usage elements (artifact, audio player, the React Flow canvas pieces, JSX preview, voice and mic selectors) were not rebuilt; the docs list which existing components to compose them from.

## Why it matters: agent UIs get a grammar

Until now most agent interfaces have been assembled one part type at a time: a reasoning accordion here, a tool-call card there, a sources popover somewhere else, each with its own spacing, icon logic and loading state. The result is the familiar “debug log” look, where every turn is a pile of unrelated widgets. Trace replaces that with one row grammar. What changes between a thought, a shell command and a subagent is only the icon, the title and what happens when you open the line.

That grammar also forces good copy. The accessibility notes are unusually specific: the icon is hidden from assistive tech, so the title is the accessible name and should be a sentence that says what happened (“Edited trace.tsx”, not “trace.tsx”). Because status is shown with colour and motion, it also belongs in the words: “Running pnpm build” while it runs, “Failed to run pnpm build” when it errors. The shimmer stops for readers who prefer reduced motion, and inside a Message Scroller each new line is announced once.

The Confirmation pattern adds one more useful rule. A pending approval is a prompt, not activity, so it sits outside the Trace as an item with Deny and Approve buttons, and only becomes a Tool line once the person answers. Asking and doing are visually different things.

## Our take

This is the same move the whole field made this month, from Figma Specs to Claude Design: the useful unit is not a generator but a shared, explicit shape that people and agents can both follow. For agent UIs, Trace is that shape. Teams building copilots, coding agents or research tools should adopt the grammar even if they never install the component, because users judge trust from whether they can see what the agent did, in order, with honest status.

Three caveats. The patterns are written around AI SDK message parts; if you stream from another SDK you will write the mapping yourself. The release is days old, so expect APIs and examples to move, and remember that copied code does not update on its own. And showing raw reasoning is a product decision as well as a design one: the shadcn Reasoning demo collapses the text into “Thought for 5s” once the step finishes, which is a sensible default.

## How to adopt it this week

- **List every step type your agent emits.** Reasoning, tool calls, sources, plans, subagents, errors, approvals. If one does not fit “icon + title + status + optional detail”, question it before designing a new widget.

- **Write titles as past-tense sentences.** Present tense while running, past tense when done, and say the failure in words. That one rule fixes most screen-reader and scanning problems.

- **Open while running, collapse when done.** The demos open a line while the step streams and fold it afterwards; the person can still expand it.

- **Put output in a small Code Block, never in the sentence.** Commands, logs and diffs go inside the line’s expanded content at `size="sm"`.

- **Keep approvals out of the trace.** Ask with an explicit Deny / Approve item; record the decision as a normal line afterwards.

- **Test the states, not just the happy path.** Running, error, pending, nested, a very long title, keyboard-only, reduced motion, light and dark.

```
# install
pnpm dlx shadcn@latest add trace
pnpm dlx shadcn@latest add code-block

# let your coding agent read the pattern
Add the Reasoning pattern from https://ui.shadcn.com/docs/ai-elements/base/reasoning.md to my chat.

# map message parts to lines
reasoning  → "Thinking" / "Thought for 5s", collapsible
tool call  → "Running <cmd>" / "Ran <cmd>" / "Failed to run <cmd>", output in Code Block sm
source     → link line, "(opens in a new tab)" in sr-only text
approval   → Confirmation item outside Trace, then a Tool line
```

## Where UI Hub fits

Trace and Code Block cover the activity inside a turn; the rest of the page still needs a direction. Browse the 
chat
 component kind in the UI Hub resource list for other agent and chat libraries to compare against, and pair them with the restrained look in our 
shadcn Blocks deep dive
. If your agent also restyles your system, the same week shadcndesign turned its DS Manager into an MCP server, so a coding agent can change a shadcn theme while respecting locked values.

## References
- [October 2026 - Trace, Code Block and AI Elements](https://ui.shadcn.com/docs/changelog/2026-10-ai-elements) — shadcn/ui changelog
- [AI Elements: patterns for agentic interfaces](https://ui.shadcn.com/docs/ai-elements) — shadcn/ui docs
- [Trace](https://ui.shadcn.com/docs/components/base/trace) — shadcn/ui docs
- [Code Block](https://ui.shadcn.com/docs/components/base/code-block) — shadcn/ui docs
- [Confirmation pattern](https://ui.shadcn.com/docs/ai-elements/base/confirmation) — shadcn/ui docs
- [Reasoning pattern (Markdown for coding agents)](https://ui.shadcn.com/docs/ai-elements/base/reasoning.md) — shadcn/ui docs
- [“I just published Trace, a new component for agent activity”](https://x.com/shadcn/status/2110410655165779985) — shadcn on X
- [AI Elements for Svelte](https://shadcn-svelte.com/docs/ai-elements) — shadcn-svelte docs
- [AI SDK Elements (being deprecated)](https://elements.ai-sdk.dev/) — Vercel
- [Chatbot: message parts with useChat](https://ai-sdk.dev/docs/ai-sdk-ui/chatbot) — AI SDK docs
- [shadcn chatbot template](https://github.com/shadcn-ui/chatbot-template) — shadcn-ui on GitHub
- [Connect your coding agent to your design system](https://www.shadcndesign.com/blog/ds-manager-mcp-server) — shadcndesign (Matt Wierzbicki)