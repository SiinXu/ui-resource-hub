# Dashboard patterns that hold up: from KPI strip to drill-down table

> AI tools love to generate twelve charts. Good dashboards answer three questions in order: is it OK, what changed, why. A layout and a component list for each.

Blog post: https://siinxu.github.io/ui-resource-hub/blog/dashboard-design-patterns/

Ask a generator for an "analytics dashboard" and you will likely get a sidebar, four stat cards and a grid of charts of equal weight. It looks complete and answers nothing. A better structure follows the questions a user actually asks, in order.

## Three layers

- **Is everything OK?** A KPI strip of 3–5 numbers, each with the comparison period and a direction, not a sparkline zoo.

- **What changed?** One primary time-series chart with a range selector, annotated where something happened.

- **Why?** A sortable, filterable table that drills into detail. Tables are where people actually work.

## Details generators skip

- Tabular figures (`font-variant-numeric: tabular-nums`) so numbers align.

- Right-aligned numeric columns, left-aligned text.

- Empty, loading (skeleton) and error states for every widget.

- Units and time zone in labels; a "last updated" timestamp.

- Colour used for status only, with a non-colour cue (icon or text) for colour-blind users.

## Components to start from

shadcn's dashboard blocks and its charts (built on Recharts) give you the scaffolding; Tremor offers dashboard-focused React components. Specify the three layers in your prompt and you get a page people can use, not just screenshot.

## References
- [Dashboard blocks](https://ui.shadcn.com/blocks) — shadcn/ui
- [Charts](https://ui.shadcn.com/charts) — shadcn/ui
- [Tremor](https://tremor.so/) — Tremor
- [Dashboards: making charts and graphs easier to understand](https://www.nngroup.com/articles/dashboards-preattentive/) — Nielsen Norman Group
- [font-variant-numeric](https://developer.mozilla.org/en-US/docs/Web/CSS/font-variant-numeric) — MDN