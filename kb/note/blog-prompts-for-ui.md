# Prompting for UI: write specs, not wishes

> "Modern and clean" means nothing to a model. Name layout, tokens, states, content and what to avoid.

Blog post: https://siinxu.github.io/ui-resource-hub/blog/prompts-for-ui/

A UI prompt is a tiny design spec. The model fills every gap with defaults, so each gap you leave becomes a cliché.

## The six-slot template

```
Goal: pricing page for a dev tool, 3 tiers, annual toggle
Layout: 12-col, max 1200px, tiers in a row ≥ 900px, stacked below
Tokens: Geist, 14/20 body, radius 10, one accent #2563eb, neutral greys
States: hover, focus-visible ring, selected tier, loading on CTA
Content: real copy below (no lorem), prices 0 / 19 / 49
Avoid: gradients on text, glassmorphism, emoji icons, centred everything
```

## Why it works

Vercel's design guidelines and Rauno Freiberg's "Interfaces" both stress small, checkable rules: focus states, hit targets, tabular numbers. Turning those into explicit lines makes the output verifiable. Real content matters too; placeholder text hides overflow and hierarchy problems.

## Our take

Put the "Avoid" line first when iterating. Models obey negative constraints better once they have seen the bad version. Keep a reusable prompt per component type; UI Hub's component cards include a copyable prompt you can start from.

## References
- [Web Interface Guidelines](https://vercel.com/design/guidelines) — Vercel
- [Web Interface Guidelines (interfaces.rauno.me)](https://interfaces.rauno.me) — Rauno Freiberg
- [v0 Documentation](https://v0.app/docs) — Vercel
- [Refactoring UI](https://www.refactoringui.com) — Adam Wathan & Steve Schoger