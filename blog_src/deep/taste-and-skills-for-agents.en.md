An agent skill is a folder with a `SKILL.md` file that the agent reads when a task matches the skill's description. For design work this matters more than it sounds: opinions about spacing, motion and what never to ship survive between sessions, instead of living in one long prompt you paste every morning. This post explains how skills load, which kinds of design skill are worth having, how to combine them without conflicts, and how to write a small project skill of your own.

## How a skill is loaded

A skill starts with a short YAML header, a `name` and a `description`, followed by instructions in Markdown. Agents that support skills, such as Claude Code, read only the name and description of every installed skill up front. The full body is loaded when the current task matches the description. Extra files in the folder (reference docs, scripts, examples) are read only when the body points to them.

That design has two consequences for you:

1. **The description is the trigger.** "Design helper" never fires at the right time. "Use when building or restyling a web page or component; enforces our type scale, spacing and banned patterns" does.
2. **Bodies can be long, but should be layered.** Put the rules the agent always needs in `SKILL.md`, and move long references (the full token table, component examples) into separate files it can open on demand.

```markdown
---
name: house-ui
description: Use when creating or restyling any web page or UI component in this repo. Enforces tokens, spacing, motion limits and banned patterns.
---
# House UI rules
1. Read tokens.css before writing styles. Never use raw hex colours.
2. Spacing comes from the 4px scale: 4, 8, 12, 16, 24, 32, 48, 64.
3. One accent colour per screen. Body text max 68ch.
4. Motion: 150–250ms, ease-out, transform/opacity only; honour prefers-reduced-motion.
5. Never: gradient text, glassmorphism cards, emoji icons, centred body copy.
For component examples, open examples.md.
```

## Four jobs, four kinds of skill

Design skills fall into four jobs. Mixing two skills that do the same job is where conflicts come from.

1. **Direction** — runs *before* code. It commits to an aesthetic and bans the generic tells. Examples: *frontend-design* from Anthropic's skills repository, *taste-skill*.
2. **Craft** — runs *while* building. It carries judgement about motion, micro-interaction and detail. Example: *emil-design-eng*.
3. **Audit** — runs *after* a draft exists. It checks against named rules and reports problems. Examples: *impeccable*, *baseline-ui*, *web-design-guidelines*.
4. **Redesign** — runs on an *existing* site. It inventories what is there before changing it. Example: *redesign-skill*.

## A working stack, step by step

**Step 1: install one skill per job.** One direction, one craft, one audit skill per project is enough. Two direction skills will argue about whether the page should be editorial or brutalist, and the agent will average them into neither.

**Step 2: write project rules in AGENTS.md.** Generic taste skills do not know your brand. AGENTS.md is a plain Markdown file at the repo root that coding agents read for project instructions. Put the hard rules there, and say explicitly that they win over any skill:

```markdown
## Design rules (override any installed skill)
- Brand accent is #2563eb; do not introduce a second accent.
- Headings use Instrument Serif; body uses Geist.
- Light and dark themes are both required for every screen.
- Max one animated "hero moment" per page.
```

**Step 3: run the direction skill first.** Ask the agent to propose a direction in words before any code: palette, type pairing, layout idea, the one thing that will make the page memorable. Approve or correct it.

**Step 4: build with the craft skill active.** Let it handle hover, focus and transition details, and keep your AGENTS.md limits on motion in force.

**Step 5: audit, then fix in named items.** Run the audit skill on the result and ask for a numbered list of problems with file and line. Fix them in small batches, not all at once.

## Pitfalls

- **Loading everything.** Ten design skills means ten sets of advice competing for the same decisions. More skills is not more taste.
- **Vague descriptions.** If the description does not match how you phrase tasks, the skill never loads and you will think it does not work.
- **Rules only in chat.** A rule you typed once disappears next session. If you repeat it twice, it belongs in AGENTS.md or a skill.
- **Audit before direction.** Auditing a page with no committed direction produces a list of nitpicks on a generic layout.
- **Copying a skill without reading it.** Skills can run scripts. Read the files before you install one, the same way you would read a dependency.

## Questions we get

**Do skills replace a design system?** No. A skill tells the agent how to use your design system and what to avoid. The tokens and components still have to exist; the skill points at them.

**How long should a project skill be?** Short enough that you would read it yourself: 20–40 lines of rules in `SKILL.md`, with longer material in linked files. If the agent ignores a rule, the usual cause is that it was buried in a long list, not that the list was too short.

**How do we know a skill is working?** Give the agent a task that should trigger it and ask it which skills it used. Then check the output against two or three rules from the skill. If the skill never fires, rewrite the description using the exact words you use for tasks.

**Can different agents share the same skills?** Several coding agents now read skill folders or AGENTS.md. Keep the rules in plain Markdown with no tool-specific syntax, and the same files can serve more than one agent. Check each agent's documentation for where it looks.

**What about public skills that change?** Pin the version you reviewed. Treat an update like a dependency upgrade: read the diff before you accept it.

## Our take

Skills turn taste from a prompt into infrastructure. The most valuable one in most repos is not a famous public skill but a 30-line project skill that encodes your tokens and your "never" list. Start there, add one public skill per job, and remove any skill that you notice giving advice you keep overriding.

## Checklist

- Each skill has a description that matches how you phrase tasks
- One direction, one craft, one audit skill per project
- Project rules in AGENTS.md, marked as overriding skills
- Direction agreed in words before code
- Audit output is a numbered list with file and line
- Every installed skill has been read before use
