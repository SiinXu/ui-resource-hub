# Design skills for Claude and Cursor: SKILL.md, rules and AGENTS.md

> Three file formats, one idea: durable instructions an agent loads when relevant. How to write a design skill that changes output, with a template.

Blog post: <https://ui.incidental.site/blog/claude-cursor-design-skills/>

Anthropic's Agent Skills are folders with a `SKILL.md` file: YAML front matter (a name and a description) followed by instructions, optionally with scripts and assets. The agent sees the descriptions and loads a skill's full body only when it is relevant. Cursor offers project rules in `.cursor/rules`, and many coding agents read an `AGENTS.md` at the repo root. Different files, same idea: durable, scoped instructions.

## What makes a design skill work

- **A precise description**, because it decides when the skill loads ("Use when building or restyling web UI").

- **Bans before wishes.** Models respond well to a short list of things never to do (text gradients, emoji icons, centred paragraphs, more than one accent).

- **Concrete values:** tokens, scales, a reference to the token file.

- **A verification step:** "render in a browser at 390px and 1440px, light and dark, before saying done".

## A template

```
---
name: house-ui
description: Use when creating or restyling any web page or component.
---
1. Load tokens from styles/tokens.css. Never hard-code colour/spacing.
2. Type: Instrument Serif display, Geist UI, scale 1.25.
3. Never: text gradients, emoji icons, glassmorphism stacks.
4. One signature effect per page (see /kb/ house style).
5. Verify in a browser: 390/1440px, light/dark, keyboard focus.
```

## Where to find good ones

Anthropic's public skills repository includes a frontend-design skill; community skills such as taste-skill and impeccable focus on aesthetics. Our encyclopedia indexes the ones we use, with full text where the licence allows.

## References
- [Agent Skills overview](https://docs.anthropic.com/en/docs/agents-and-tools/agent-skills/overview) — Anthropic
- [anthropics/skills](https://github.com/anthropics/skills) — GitHub
- [Rules](https://docs.cursor.com/context/rules) — Cursor docs
- [AGENTS.md](https://agents.md/) — agents.md
- [taste-skill](https://github.com/Leonxlnx/taste-skill) — GitHub