# Vercel’s UI SDK lets agents operate your interface. Design for the agent that reads it

> Vercel Labs’ UI SDK (beta, new package releases on 13 November 2026) gives coding agents 50+ tested behaviors to assemble components from, and gives runtime agents a bridge that reads component state and calls actions without screenshots. In Vercel’s own benchmark that cut a settings task from 41 s to 16 s. What changes for designers: labels become the agent’s map, confirmation copy becomes a safety rail, and some regions should be hidden on purpose. With a checklist and an agent prompt.

Blog post: <https://ui.incidental.site/blog/vercel-ui-sdk-agent-operable-interfaces/>

Most agents that use a web app today do it the hard way: take a screenshot or dump the page, guess which element is the “Region” dropdown, click, wait, screenshot again. Vercel Labs’ **UI SDK**, an Apache-2.0 library in beta whose framework packages got a new release on 13 November 2026 and which was all over design feeds on 14 November, proposes a different contract. Components are built from tested 
behaviors
, and an 
agent bridge
 lets an agent read those components and call their actions directly.

That is a developer library, but the consequences land on design. When an agent reads the interface instead of looking at it, the words on the screen, the structure of a form and the copy on a risky button become the agent’s instructions. This post covers what shipped, what the benchmark does and doesn’t show, and what we would change in our own screens.

## What shipped

- **Behaviors, not components, as the unit.** `@ui-sdk/core` ships 50+ framework-free behaviors such as `createPopup`, `createSelection`, `createTypeahead`, `createRovingFocus` and `createReorder`. The pitch on the home page: give an agent the pieces of a Select and it can build a Select, a combobox or a component nobody has named yet. Adapters render the same primitive in React, Vue, Svelte, Solid and Web Components.

- **A skill and versioned docs for the builder.** `npx skills add vercel-labs/ui --skill ui-sdk` gives a coding agent a workflow: choose behaviors, define a primitive, render it, test keyboard, focus and ARIA with the bundled testing kit. Each package also carries Markdown docs for the installed version.

- **A bridge for the operator.** `createAgent()` exposes three tools: `snapshot` lists components with their label, value and available actions; `query` searches components and list choices; `act` runs steps such as `setValue` on “Project name”. The same tools can be registered with a browser’s built-in agent through WebMCP, which Chrome currently offers as an early preview.

- **Permission hooks.** An `allow` callback approves or refuses each step, change callbacks receive `source: "agent"`, and three HTML marks decide what the agent may see or do: `data-agent-confirm`, `data-agent-hidden` and `data-agent-secret`.

## Reading the benchmark carefully

Vercel’s docs report a project-settings task (rename a project, update members and notifications, save) done two ways. Browser tools on a page built with another library: 16 tool calls, 39.8k characters read, 41 s, $0.073. The agent bridge on the same screen built with UI SDK: 5 calls, 6.8k characters, 16 s, $0.032. These are medians of three runs per approach, one model, one task, measured by the vendor. Treat it as a direction rather than a law: structured state beats pixels, and the gap grows with the number of fields. It does not tell you how the approach behaves on a messy real app with ambiguous labels, and that is exactly the part designers control.

## Our take: the accessible name is now the agent’s API

The bridge finds a control by its label, matching whole words regardless of case and accents. If two controls share a label, the call fails with a list of matches. In other words, the same accessible name a screen reader announces is what the agent targets. Three design consequences follow.

- **Labels must be unique and specific on a screen.** Two fields called “Name”, a row of icon buttons with no name, a placeholder pretending to be a label: each one is an accessibility bug and now also an agent failure. WCAG’s “Label in Name” rule, that the visible text appears in the accessible name, is a good default for both audiences.

- **Confirmation copy is a safety rail, so write it like one.** `data-agent-confirm="Charges $20 to your card for 1,000 credits"` appears in the snapshot before the agent tries, and without an `allow` callback the press fails with “Needs a person”. That sentence is shown to a human at the moment of decision. It should name the action, the amount and the target in plain words, not “Are you sure?”.

- **Some regions should be invisible on purpose.** Recovery codes, API keys, a danger zone: mark them `data-agent-hidden` so they are left out of `snapshot` and `query`. Mark fields like a tax ID `data-agent-secret` so the agent can type but reads back “[redacted]”. Password, card and one-time-code fields are treated as secret without a mark.

There is also a trap in the docs worth repeating: an `allow` that returns `true` without reading `step.confirm` answers yes on the person’s behalf. If you write the copy, check that someone wired it to a real prompt.

## Where it fits, and where we would wait

The builder half is useful today in the same way a headless library is: an agent composing `createPopup` plus `createListbox` is far less likely to ship a menu with no focus return than one hand-rolling handlers. The bridge half is worth prototyping on internal tools and settings screens, where actions are bounded and labels are under your control. For checkout, account deletion or anything with money, keep the agent behind confirmation marks and log every `source: "agent"` change. UI SDK is beta under Vercel’s beta terms and WebMCP is an early-preview browser API, so avoid building a public product promise on either yet.

The same week, Google’s 
Modern Web Guidance
 skills (stewarded with Edge, Firefox and MDN) were trending for a related reason: agents default to legacy patterns unless they get current, curated platform guidance in context. Both projects bet that agents write better UI from tested building blocks than from memory.

## Checklist: make a screen agent-operable

- **One name per control.** Every input, select and icon button has a visible or programmatic label, unique on the screen. Search the design for duplicate “Name”, “Edit”, “More”.

- **Visible text inside the name.** The accessible name starts with the words people see, so voice users and agents use the same words.

- **State lives in the component, not in colour.** Selected, expanded, invalid and disabled are real states, not just a tint the agent cannot read.

- **List choices have readable labels.** Option values like `north-america` need human labels like “North America”; avoid options that are only flags or icons.

- **Risky controls carry a confirm sentence.** Action, amount, target, in under 15 words. Put it on the form or dialog to cover everything inside.

- **Hide on purpose.** Mark secrets and danger zones hidden or secret; review the marks in design review, not after launch.

- **Show agent changes to the person.** Plan a visible trace, toast or history entry for changes with `source: "agent"`, plus undo.

- **Test it twice.** Keyboard and screen-reader pass first; then run `agent.snapshot()` in the console and read it as if it were the only view of the screen.

```
# Paste this to your coding agent (React + UI SDK)
Use the ui-sdk skill. Make the settings screen in 
 agent-operable.
- Build any missing control from ui-sdk behaviors; keep our styles and tokens.
- Give every control a unique accessible name that starts with its visible text.
- Create the bridge with createAgent({ allow }) and make allow read step.confirm
  and show our existing confirm dialog; never return true for a confirm step.
- Add data-agent-confirm with a plain sentence (action, amount, target) to
  delete, billing and invite buttons; data-agent-hidden on API keys and
  recovery codes; data-agent-secret on the tax ID field.
- Show a toast for changes whose details.source is "agent", with undo.
Report: the agent.snapshot() output, any duplicate or missing labels you fixed,
and every control you marked, with the sentence you used.
```

Related on UI Hub: 
approval UI for agents
, 
native popovers and dialogs for AI-generated UI
, and 
accessibility in AI-generated UI
.

## References
- [UI SDK — A library of behaviors for agents](https://ui-sdk.dev/) — Vercel Labs
- [Built for Agents (agent bridge and benchmark)](https://ui-sdk.dev/docs/agents) — UI SDK docs
- [Permissions](https://ui-sdk.dev/docs/agents/connect-an-agent/permissions) — UI SDK docs
- [WebMCP](https://ui-sdk.dev/docs/agents/connect-an-agent/webmcp) — UI SDK docs
- [All Behaviors](https://ui-sdk.dev/docs/core/behaviors) — UI SDK docs
- [vercel-labs/ui](https://github.com/vercel-labs/ui) — GitHub
- [WebMCP is available for early preview](https://developer.chrome.com/blog/webmcp-epp) — Chrome for Developers
- [WebMCP specification draft](https://webmachinelearning.github.io/webmcp/) — W3C Web Machine Learning Community Group
- [Modern Web Guidance](https://github.com/GoogleChrome/modern-web-guidance) — GoogleChrome on GitHub
- [AI Design Daily, 14 Nov 2026 (morning edition)](https://studios.greatcreations.art/daily-design/editions/2026-11-14/morning.html) — Daily Design
- [Accessible name](https://developer.mozilla.org/en-US/docs/Glossary/Accessible_name) — MDN Web Docs
- [Understanding SC 2.5.3: Label in Name](https://www.w3.org/WAI/WCAG22/Understanding/label-in-name.html) — W3C WAI