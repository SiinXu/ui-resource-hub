# Two AI design tools closed on 31 October: how to keep your design work portable

> Motiff’s export window and Visily’s service both ended on 31 October 2026; Visily deletes all data on 30 November. Neither had an open file format, so what survived was whatever teams exported in time. What happened, why AI design tools are consolidating, the export ladder from code down to PNG, and a ten-point exit plan to set up before you adopt the next tool.

Blog post: <https://ui.incidental.site/blog/ai-design-tool-shutdowns-keep-work-portable/>

Yesterday, 31 October 2026, was a quiet deadline for two AI design tools. **Motiff**, the Figma-class editor that later pivoted to AI UI generation, closed its last export window: the service itself went offline on 23 June, and Motiff says all remaining data is deleted after 31 October. **Visily**, the AI wireframing tool, shut down the same day and says its data will be permanently deleted on 30 November. Neither event is dramatic on its own. Together they are a useful reminder that the files in a cloud design tool are often the only copy of your work, and that the market for these tools is changing fast.

## What happened

- **Motiff.** The shutdown was announced on 24 April 2026, when new sign-ups and renewals stopped. The editor went offline on 23 June, and export stayed open until 31 October, with every export option made free: PNG, JPEG, WebP, PDF, Copy to Figma, HTML code, React code and a project ZIP. The motiff.com home page now shows a “discontinued” banner, and the old editor survives only as an export page.

- **Visily.** Announced on 3 October, the team wrote that “the market for tools like Visily has changed substantially in the last couple of years.” Designs could be exported as images, PDF, code (React, Vue or HTML on paid plans, up to 10 screens per ZIP) or to Figma through a plugin, and assets could also be pulled through Visily’s MCP server. Free-plan image exports were limited to 1× scale.

- **No open format.** As the migration guide from Brilliant points out, Motiff never published a documented file format, so there was no file to hand to a converter later. The only way out was through the exports, before the deadline.

## Why this keeps happening

Generating a screen has become cheap, and the large platforms now bundle it. Figma, Canva, Framer and GitHub have all shipped agents or prototyping tools in the last month that work inside your existing design system. That squeezes standalone tools whose main feature was “a prompt that makes a screen.” Figma’s own pitch this week is telling: in a survey it cited in South Korea, 62% of respondents said AI output needed six to ten rounds of revision before it could ship, and its answer is an agent that reads a team’s design context. In other words, the value has moved from the generated pixels to the decisions behind them: tokens, components, specs and the reasons for each screen. Those decisions are exactly what gets lost when they only live inside one vendor’s canvas.

## Our take

Treat every AI design tool, including the big ones, as a place where work 
happens
, not where it 
lives
. The source of truth should sit in formats you control: code in your repository, tokens in the open DTCG JSON format (its first stable version, 2025.10, is supported by Figma, Penpot, Sketch, Framer, Tokens Studio and others), and specs and briefs in plain markdown. Then a shutdown, a price change or a pivot costs you a migration weekend instead of your archive. The test is simple: if the tool vanished tomorrow, could you rebuild your three most important screens from what is on your own disk? If the honest answer is no, fix that before you design anything else in it.

## The export ladder

When you export, take the highest rung the tool offers, and take the lower rungs too. **Code** you can run beats a **design file** another tool can open; both beat **structured files** such as SVG and token JSON; and those beat **flat images and PDF**, which are a faithful record but cannot be edited. Images are still worth keeping, named by screen and date, as proof of what was agreed.

## Checklist: an exit plan for any AI design tool

- **Find the export page on day one.** Before your team commits, export one real screen in every format offered and open it somewhere else.

- **Check which exports are paywalled.** At Visily, code and Figma exports needed a paid plan and free images were 1×. Know what you lose if you downgrade.

- **Keep tokens outside the tool.** Colours, type, spacing and radii belong in a DTCG JSON file in git that the tool imports, not the other way round.

- **Put generated code in git straight away.** A ZIP in a downloads folder is not a source of truth.

- **Write down the brief.** Save the prompt, the constraints and the reason you chose a direction for each key screen in a markdown file next to the code.

- **Export on a schedule.** Monthly, the richest format available, to storage your team owns. Batch limits (10 screens per ZIP at Visily) mean large boards take longer than you expect.

- **Bring your fonts and assets.** Code exports often lose custom fonts and licensed images; keep originals and licences separately.

- **Prefer tools with an MCP server or API.** Visily’s MCP server gave agents a second way to pull assets out. Programmatic access is an exit door.

- **Watch the warning signs.** Renewals paused, a home page that suddenly promotes a different product, or a support article titled “what you need to know.”

- **If you just missed a deadline, ask today.** Visily says data is deleted on 30 November and lists support@visily.ai for questions; it does not say whether export still works after 31 October, so ask now rather than assume.

```
design-exit.md
  tool:       <name> · plan: <tier> · owner: <person>
  source:     tokens/*.json (DTCG) · src/ (code) · specs/*.md
  exports:    monthly · code ZIP + Figma copy + PNG @2x
  last test:  2026-11-01 · opened in <other tool>: OK
  if closed:  export all · move tokens · rebuild top 3 screens
```

## How UI Hub helps

Getting values out of a tool starts with naming them: 
design tokens for agents
 covers writing tokens down in a form agents and tools can share. 
Figma code layers and Specs
 and 
GitHub Replica
 show the platforms moving toward code and written context as the shared source. If you are choosing a replacement, 
prompt-to-UI tools compared
 is a starting point, and the tool pages on UI Hub list what each one exports.

## References
- [Motiff is shutting down — what you need to know](https://motiff.com/help/others/462390803479041) — Motiff Help Center
- [Motiff home page (discontinued banner)](https://motiff.com/home) — Motiff
- [Moving from Motiff](https://brilliant.design/docs/solutions/moving-from-motiff) — Brilliant Docs
- [Visily is shutting down](https://www.visily.ai/blog/visily-is-shutting-down) — The Visily Team, Visily Blog
- [How to export designs to code](https://support.visily.ai/portal/en/kb/articles/how-to-export-designs-to-code) — Visily Support
- [How to export designs as images](https://support.visily.ai/portal/en/kb/articles/how-to-export-designs-as-images) — Visily Support
- [Visily shutdown: dates, export steps, alternatives](https://shutdownwatch.com/shutdowns/visily/) — Shutdown Watch
- [Week of Oct 26 to Nov 1, 2026: what changed](https://designengindex.com/weekly/2026-44) — Design Eng Index
- [Figma bets on design-specific AI agent as quality lags speed](https://gmasia.ai/news/figma-bets-on-design-specific-ai-agent-as-quality-lags-speed) — GMAsia News
- [Design Tokens Community Group (DTCG), first stable version 2025.10](https://www.designtokens.org/) — W3C Design Tokens Community Group