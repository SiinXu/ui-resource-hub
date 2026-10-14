# AI-assisted UI design: a workflow that keeps taste in the loop

> Generators are fast but average. Split the job: humans set direction and constraints, AI explores variants, humans curate and polish.

Blog post: https://siinxu.github.io/ui-resource-hub/blog/ai-assisted-ui-design-workflow/

Every AI UI generator converges on the statistical middle of its training data: centred hero, three feature cards, a purple gradient. That is not a bug, it is what "most likely next token" means. The practical consequence is that speed is free and **taste is the scarce input**.

## Split the job into four passes

- **Direction (human).** Write a one-paragraph brief: audience, one adjective you want and one you refuse, a reference product, density level. NN/g's testing of AI design tools found outputs were generic unless the prompt carried real context.

- **Exploration (AI).** Ask v0 or Claude for 4–6 deliberately different directions, not one "best" page. Diversity is where generators shine.

- **Curation (human).** Pick one, then name what is wrong in concrete terms: "line length over 80ch", "two accent colours competing".

- **Polish (AI + human).** Feed those notes back, or run a critique skill such as 
impeccable
 or 
baseline-ui
, then do the last 10% by hand.

## Our take

The biggest win is not generation but **constraint files**: a short DESIGN.md with tokens, spacing scale and banned patterns that every agent reads first. It turns one good decision into a hundred consistent screens. On UI Hub, filter by 
Skill
 to find ready-made ones.

## Checklist

- Brief has a "never" list
- Ask for variants, not a page
- Critique with named problems
- Lock decisions into tokens

## References
- [Status Update: AI UX-Design Tools Are Not Ready for Primetime](https://www.nngroup.com/articles/ai-design-tools-not-ready/) — Nielsen Norman Group
- [v0 Documentation](https://v0.app/docs) — Vercel
- [Agent Skills repository](https://github.com/anthropics/skills) — Anthropic
- [impeccable](https://github.com/pbakaus/impeccable) — Paul Bakaus