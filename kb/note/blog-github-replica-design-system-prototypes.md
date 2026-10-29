# GitHub Replica: AI prototypes that start from your design system, not a blank page

> On 28 October GitHub open-sourced Replica, an MIT-licensed prototyping tool from GitHub Design and Microsoft CoreAI Design that runs in the Copilot app. Its real idea is not the canvas but the guidance: reviewed context files split by owner, drafts kept out of active use, missing evidence marked manual instead of passed. What it does, where it is heavy, and a checklist you can apply even without Replica.

Blog post: <https://ui.incidental.site/blog/github-replica-design-system-prototypes/>

Most prompt-to-UI tools start from a blank page and a model’s idea of what a “clean SaaS app” looks like. You get something polished and generic, and the first hour of review is spent explaining that your product doesn’t have that sidebar, that button style or that kind of empty state. On 28 October GitHub open-sourced **Replica**, a prototyping tool built by GitHub Design and Microsoft CoreAI Design, which tries to fix the order of operations: 
designers write and approve the rules first, then anyone on the team prototypes inside them.

## What Replica is

- **Where it runs.** Inside the GitHub Copilot app. A plugin adds a Replica canvas that shows your running prototype next to the conversation, so you describe a change, try it, and refine it in one place. It is MIT-licensed and maintained by GitHub staff.

- **Four parts.** Starters (a 
Minimal
 app to adapt to your own system, or a 
CoreAI Sandbox
 with Microsoft’s CoreAI design system already wired in), the canvas plugin, an optional self-hosted **Replica Hub** for publishing and comments, and a GitHub build action that only matters once you publish.

- **Local first.** A local prototype needs the Copilot app, Git, Node.js and npm on macOS or Linux. No Hub, Docker, domain or GitHub repository is required. Hub needs a Linux server, a dedicated domain with wildcard DNS and HTTPS, and GitHub approvals, and your organisation runs it, not GitHub.

- **Models.** GitHub-hosted models with a Copilot plan, or your own model provider (public preview, provider’s terms apply). Viewing or reviewing a finished prototype needs no Copilot subscription.

## The interesting part: guidance as a reviewed artifact

You run `/setup-skills`, point Copilot at approved sources (product docs, design-system docs, component and token packages), and it drafts guidance. The docs are explicit that drafting does not activate anything: designers and design-system maintainers review the drafts, and activation is a separate approval. The result is a set of context files, each owning one concern: `DESIGN-SYSTEM.md` for components, tokens and patterns, `PRODUCT-DESIGN.md` for scenarios and state behaviour, `RESPONSIVE-DESIGN.md` for widths, plus accessibility, browser validation, seed data and repository rules.

The bundled skills are strict about how they use that context. The design-system review skill reads only the active folder, never drafts. A rule labelled `proposed-default` is treated as a proposal, not policy. And when required evidence is missing, the check is marked 
manual, never pass
; the skill is told not to guess components or tokens. The template for `DESIGN-SYSTEM.md` also rejects lazy context: “TextInput exists” is not an answer to how validation errors are shown.

There is a feedback loop too. With Hub connected, `/review-hub-feedback` looks for recurring themes across prototype reviews, and `/prepare-feedback-proposals` turns chosen findings into proposed guidance edits, each shown before you approve it. Comments improve the rules, not just the one prototype that got them.

## Our take

Replica is less a new generator than a workflow wrapped around one: branch per prototype, sample data only, ask before committing, never push or publish without approval. That is the right shape for teams where a PM or engineer prototypes alongside designers. The strongest idea is portable: **split guidance by owner, separate draft from active, and make “I don’t know” visible**. Most agent context files we see are one long, unreviewed `AGENTS.md` that nobody owns and every agent treats as gospel.

The costs are real. It assumes the Copilot app (macOS or Linux) and, for sharing, someone willing to operate a Hub with wildcard DNS. The canvas proxies the preview from a different origin, so apps that depend on their own origin for storage or sign-in may need extra work. And the docs themselves warn about the failure we see most often in AI-built UI: the agent using 
similar-looking replacements
 instead of your real components. Guidance lowers that risk; it does not remove it, so check imports, not screenshots.

## Checklist: design-system-first prototyping (with or without Replica)

- **Split guidance into owned files.** Design system, product behaviour, responsive widths, accessibility, seed data and repository rules each get one file and one owner.

- **Give every rule a condition and evidence.** “Use Banner for page-level errors, InlineMessage inside forms — see docs link” beats “use our components”.

- **Keep drafts out of active context.** Agent-written guidance goes to a drafts folder until a designer approves it; label unreviewed defaults as proposed.

- **Make unknowns visible.** If the agent can’t find evidence for a token or pattern, it should say so and leave the check manual, not invent a value.

- **One prototype, one branch.** Keep the default branch as the reviewed starting point; never let a prototype rewrite it.

- **Sample data only.** No production credentials or customer data in prototypes, ever.

- **Verify the real components.** Grep the prototype’s imports for your package and wrappers; a lookalike `<button>` is a failed check.

- **Route feedback into the rules.** When the same review comment appears twice, change the guidance file, not just the prototype.

```
# .agents/context/  (one concern per file, reviewed before use)
DESIGN-SYSTEM.md      # imports, tokens, layout, forms, feedback — each with a docs link
PRODUCT-DESIGN.md     # scenarios, saving, empty / loading / error behaviour
RESPONSIVE-DESIGN.md  # required widths, what collapses at 375px
ACCESSIBILITY.md      # keyboard, contrast, screen-reader expectations
SEED-DATA.md          # sample data rules (no real customers)
REPOSITORY.md         # required wrappers, branch + commit rules
# drafts/ is never read as active; "proposed-default" ≠ policy
```

## How UI Hub helps

Replica only works as well as the guidance you feed it. Our posts on 
design tokens for agents
 and 
design skills for Claude and Cursor
 cover how to write that context; 
linting agents onto your design system
 covers catching lookalike components after the fact. For how Replica sits next to v0, Lovable, Figma Make and Magic Patterns, see 
prompt-to-UI tools compared
, and for Figma’s own library guidelines, 
Figma Make and the Figma agent
.

## References
- [Introducing Replica, an open-source AI prototyping tool](https://github.blog/changelog/2026-10-28-introducing-replica-an-open-source-ai-prototyping-tool/) — GitHub Changelog
- [github/replica](https://github.com/github/replica) — GitHub Design & Microsoft CoreAI Design, GitHub
- [Create your first local prototype](https://github.com/github/replica/blob/main/docs/local-prototyping.md) — Replica docs
- [Set up and configure your prototype environment](https://github.com/github/replica/blob/main/docs/prototype-environment.md) — Replica docs
- [Replica setup and workflows (REPLICA.md)](https://github.com/github/replica/blob/main/starters/shared/REPLICA.md) — Replica starters
- [Component design-system review skill](https://github.com/github/replica/blob/main/starters/shared/.agents/skills/component-design-system-review/SKILL.md) — Replica starters
- [Design-system research template](https://github.com/github/replica/blob/main/starters/shared/.agents/context-templates/DESIGN-SYSTEM.md) — Replica starters
- [GitHub open-sources Replica for prototypes built with your design system](https://bytefwd.com/github-replica-design-system-prototypes-local-hub/) — Jordan Reid, ByteForward
- [GitHub Open-Sources Replica for On-Brand AI Prototypes](https://nvdium.com/en/articles/140006649) — Nvdium
- [Figma product news and release notes](https://www.figma.com/release-notes/) — Figma