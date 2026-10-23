# Lint the agent: keeping AI-written UI on your design system

> On 22 October the open-source onsystem went public, joining shadcn’s agent-first linter and Figma’s new Guidelines and system check. The shared idea: stop asking agents to follow your design system and start checking every edit. What the benchmark shows, and a setup checklist.

Blog post: <https://ui.incidental.site/blog/lint-agents-onto-your-design-system/>

Ask a coding agent for a settings card in a shadcn/ui project and you often get something that type-checks and still looks wrong: a hex red instead of the destructive token, `p-[13px]` instead of the spacing scale, a native `<button>` with hand-rolled classes next to your real Button, and a `variant="danger"` your Button has never heard of. The agent is not careless. It writes from its training data, and it cannot see your Storybook. This week the tooling around that gap got noticeably more serious.

## Three tools, one shift

- **onsystem (22 October).** Diogo Esteves made public an MIT-licensed checker that reads your design system from source and flags agent-written React that strays from it. Its eight rules cover hard-coded colours, spacing and radius, native elements your system already wraps, invented components, unknown props, unknown variant values, and icon buttons without an accessible name. Each finding comes with the replacement to write. It runs in three places: an MCP server the agent can call (`check_ui`) to see your components and tokens, a hook that checks each file right after the agent edits it in Claude Code, and a CLI, ESLint plugin and GitHub Action for pull requests. It makes no model calls.

- **@shadcn/lint.** shadcn's own "agent-first linter for Tailwind design systems" takes the policy route. You declare what may change, for example that a Button accepts margin and width but owns its padding, and when an agent breaks the rule the error explains why and points to an existing size or variant. It works with Tailwind v4 in React, Svelte and Vue, through ESLint or Oxlint, and does not require shadcn/ui.

- **Figma Guidelines and system check.** Announced at Config India on 15 October, Guidelines (open beta) let you attach written rules to a published library so agents reading it through Figma's MCP server follow the patterns your team set. A previewed system check scans the library itself for gaps such as missing descriptions and interactive states. That is the same idea one layer up: lint the source of truth, not only the code.

## What the benchmark says

onsystem ships with a public benchmark run on 12 October: six models from three providers each wrote the same 20 UI components in five open-source repositories, 240 runs per configuration. Measured by onsystem's own check, design-system errors fell from 0.85 per run with no help to 0.00 with its skill, MCP server and hook together, with type-check pass rates (93% vs 92%) and cost per run essentially unchanged. Scored by @shadcn/lint, a linter it does not control, findings per run went from 4.97 to 2.64.

Two readings matter more than the headline. First, the tool under test scores the headline, which the author states openly, so the independent number is the one to quote: roughly half the problems gone, not all of them. Second, the breakdown by part is the real lesson. The written skill alone, a set of instructions in the prompt, cut errors to 0.42 per run. The MCP server alone reached 0.01 and the hook alone 0.05. Telling the agent the rules helps; giving it something to query and something that pushes back helps far more.

## Our take

For two years the answer to off-brand AI UI has been better context: tokens files, AGENTS.md, taste skills, guideline documents. Those still matter, because they tell the agent what good looks like. But context is a request, and a linter is a contract. The pattern emerging this month is a loop of read, write, check, fix: the agent reads your components and tokens, writes, gets a precise error with the fix, and corrects itself before you ever review it. Designers should care, because the rules in that loop are design decisions. Which props may be overridden, which spacing values are legal, which elements need a label: someone has to write those down, and it should be the people who own the system.

A caution: static checks only see what they can read. onsystem documents that classes built at runtime, such as `bg-${color}-500`, or values passed in from another file are not followed. @shadcn/lint's `require-static-classes` rule exists to flag exactly those cases. Linting also says nothing about hierarchy, rhythm or taste, so it shrinks review work rather than replacing it.

## Checklist: putting a design-system check in the agent loop

- **Run a baseline first.** Check your current app with no setup (`npx -y onsystem check .` for React, or the @shadcn/lint quickstart) and count findings by rule. That tells you where agents and people already drift.

- **Write policies, not just tokens.** For each core component, decide what callers may change (layout, margin, width) and what the component owns (padding, radius, colour). Put that in lint config, where an agent gets an error, not in a wiki.

- **Make every error teach.** Prefer rules whose message names the token, size or variant to use instead. An error that only says "not allowed" sends the agent guessing again.

- **Check at edit time and at merge time.** A hook or MCP tool keeps the agent honest while it works; the same rules in CI catch anything that slips through, including human edits.

- **Forbid what you cannot read.** Turn on a rule that rejects dynamically built class names, so the linter's blind spots do not become the agent's favourite escape hatch.

- **Fix the system when the lint is noisy.** If agents keep reaching for a missing variant, that is a gap in your design system. Add it on purpose, as both tools suggest, rather than loosening the rule.

- **Still review the pixels.** Clean lint means the parts are legal, not that the screen is good. Keep a visual check for hierarchy, density and states.

```
# 1. see what drifts today (React, no install)
npx -y onsystem check .

# 2. or ask your agent to set up shadcn's linter
"Read https://github.com/shadcn-ui/lint/blob/main/SETUP.md
 and set up @shadcn/lint in this project."

# 3. a policy: Button keeps its own size and shape
"shadcn/no-restyle": ["error", { allow: ["layout"] }]

# 4. the same rules on every pull request
- uses: dgesteves/onsystem@v0
```

## How UI Hub helps

A linter can only enforce choices that exist. If you are still defining them, start with our posts on 
design tokens for agents
 and 
component composition
, then use 
design skills for Claude and Cursor
 for the instruction layer. This post is the missing third step: once the agent knows the rules, check that it kept them.

## References
- [I built three open-source tools for coding agents: onsystem, ondocs and signoff-ui](https://dev.to/dgesteves/i-built-three-open-source-tools-for-coding-agents-onsystem-ondocs-and-signoff-ui-2ho7) — Diogo Esteves, DEV Community
- [onsystem: keeps coding agents on your design system](https://onsystem.vercel.app/) — onsystem
- [Benchmark: coding agents with and without onsystem](https://onsystem.vercel.app/benchmark) — onsystem
- [Rules](https://onsystem.vercel.app/rules) — onsystem
- [onsystem repository](https://github.com/dgesteves/onsystem) — GitHub (dgesteves)
- [@shadcn/lint: write design system rules that agents can verify](https://github.com/shadcn-ui/lint) — shadcn (GitHub)
- [Build by design: New workflows for new ways of building](https://www.figma.com/blog/build-by-design/) — Figma (Dylan Field)
- [What's new from Config India 2026](https://help.figma.com/hc/en-us/articles/43663368947863-What-s-new-from-Config-India-2026) — Figma Learn
- [Figma's new system check finds the hover state nobody drew](https://artdirectiondaily.com/issues/2026-10-16-figma-check-finds-missing-hover.html) — Art Direction Daily