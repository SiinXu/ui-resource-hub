# LangChain open-sourced its design agent: put taste in context and the rules in code

> Content Studio, the Slack design agent LangChain says has shipped more than 3,000 assets for its own team, is open source (Apache 2.0) and got a fresh push this week. The interesting part is not the model but how the work is split: every asset is code, design knowledge is divided into skills, a wiki, deterministic gates and memory, cheap storyboards come before expensive renders, and people point at a shared canvas instead of describing positions in chat. What to copy even if you never fork it, a checklist and a prompt for turning your brand guide into a brand pack with checks.

Blog post: <https://ui.incidental.site/blog/design-agent-taste-in-context-rules-in-code/>

LangChain’s design agent, Content Studio, is open source as `langchain-ai/design-agent` under the Apache 2.0 licence. The repository first appeared in October alongside a long build post, and this week LangChain pushed it again: on 23 November the README gained a launch video and the company re-posted the project on X (“ICYMI: It’s open source”), and Geeky Gadgets wrote it up on 25 November. It is a Slack agent: someone mentions it in a thread with a brief and attachments, and finished files come back to the same thread. LangChain says it has produced more than 3,000 assets since August, including more than 80 slide decks, that three in four requests now come from outside marketing, and that the median request costs about 50 cents in model spend, down from about $8 in mid-September.

The numbers are LangChain’s own, so treat them as a claim. The part worth studying is the structure, because it answers a question most teams hit after their first “brand skill”: why does an agent that knows our colours and fonts still produce work that looks like everybody else’s? LangChain shows the same prompt given to a local coding agent with a brand skill and to Content Studio. The first got the logo lockup, the font and the primary colour wrong. The model was not the difference. The difference was how much of the brief the agent had to fill in by itself, and with what.

## What is in the repo

- **Every asset is code.** A slide is an HTML page, a chart is a data spec, a video is an animation timeline. Each Slack thread gets its own sandbox (a Linux machine with Chrome, FFmpeg, HyperFrames, D2 and the brand fonts), and the brief, plan, scene code, audio and renders live in one project folder. Moving one element earlier is a changed value and a re-render, not a new generation.

- **Four kinds of knowledge, kept apart.** Skills say how to do a specific job; a router skill, mostly one table, maps each kind of ask to a workflow and keeps small edits out of the big process. The wiki holds the craft and the brand facts, and skills link to it instead of copying it. Anything measurable is a gate, a deterministic check in code: colours, fonts, contrast, sizes and chart maths are checked on every render. Memory holds what people teach it.

- **Memory in two layers.** “Never use orange on LinkedIn” is saved in the same turn, either to team memory or to one person’s memory, and team standards win. Each layer has an index that loads on every run; LangChain capped it at 200 lines after an early version grew to 500K tokens. After each job a `learn_from_job` step writes up to five evidence-backed notes against the skill it used, and later jobs rate them.

- **Cheap before expensive.** A storyboard frame renders in about 50 ms; a second of finished film takes 8 to 40 seconds. So films go storyboard, animatic, production. When the agent sometimes skipped a review to save time, LangChain moved the order into code: assembly waits until every part passes.

- **Point, don’t describe.** A Slack thread is linear and a storyboard is spatial, so the agent drafts on a shared Paper canvas through Paper’s MCP server, where people compare directions, comment on a frame or edit it themselves. Lovable added Paper as a chat connector on 23 November, so this shared-canvas pattern is spreading beyond one team.

- **Long jobs that stay steerable.** The main agent splits big jobs between background subagents and keeps the thread updated with a plan, live status, spend and an approval step before anything goes public. One overnight job reskinned a 52-slide deck by doing three sample slides first, then numbered batches for approval.

## Our take: the rules that last are the ones you can check

The most useful sentence in LangChain’s write-up is about where things live: the order that must always hold lives in code, and the judgment stays in the prompt. Their first harness did the opposite. It shipped 115 reusable components and a lot of instructions to make up for what the model could not yet do, and the output stayed on brand but repeated the same layouts. After a model upgrade they removed most of the hard-coded rules, kept the design principles, and got more variety. Rules that patch a model’s weaknesses expire. Brand facts, principles and countable checks do not.

That gives a clean test for anything in your own agent setup. If a rule can be counted (this hex value, this font, contrast at least 4.5:1, no title case, the chart axis starts at zero), make it a gate that fails the render. If it is a fact (logo lockups, primary versus secondary colours, voice), put it in one brand pack that every skill links to. If it is judgment (is the idea strong, does the message land), write the reasoning down as a principle with an example and let the model apply it. LangChain’s evals follow the same split: they grade delivered files, exact copy and tool-call order without a model judging taste.

Some caution before forking. Managed Deep Agents is in public beta on LangSmith, the first sandbox build takes 10 to 15 minutes, the full eval set costs about $120 per model, and the setup leans on HyperFrames for video and Paper Desktop for the canvas. The bigger limit is your brand. If your guide is a logo and two hex codes, the agent will still fill the gaps with defaults. Most of the work is writing down decisions your designers make without thinking.

## Set up a design agent the same way

- **Pick a code format per asset type.** HTML and CSS for stills and slides, a chart spec for data, a timeline for motion. Never accept a flat image as the master file.

- **Write the brand pack once.** Tokens, fonts, logo lockups with clear space, which colour is primary, voice and a short list of things the brand never does. Skills link to it; nothing copies it.

- **Turn every countable rule into a gate.** Run it after every render and fail loudly. Start with off-palette colours, wrong fonts, contrast, minimum text size, canvas size and capitalisation.

- **Make the agent look before it posts.** Render, inspect the image, fix, then deliver. A file that was never looked at is not done.

- **Route small asks away from the big pipeline.** A resize should not trigger a storyboard; a launch film should not skip one.

- **Keep memory small and layered.** Team rules over personal preferences, one index per layer, and a regular pass that drops notes which did not hold up.

- **Put feedback where it can point.** A shared canvas or at least numbered frames, so “the second card, left edge” is not the main way to give notes.

## Design-agent checklist

- Can every delivered asset be reopened as code and changed with one edit and a re-render?

- Is there exactly one brand pack, and do skills link to it instead of repeating it?

- Do colours, fonts, contrast, sizes and chart maths fail the render automatically when they are wrong?

- Does the agent look at each render before posting it?

- Do expensive jobs start with a cheap draft that a person approves, enforced in code rather than in the prompt?

- Is memory split into team and personal layers with a capped index?

- Is there an approval step before anything is published, and can people steer a long job mid-run?

- Have you deleted the workaround rules you wrote for an older model?

```
# Paste into a coding agent, with our brand guide and website attached
Turn our brand guide into a brand pack and a set of render gates.
1. brand/tokens.json: colours with roles (primary, secondary, surface, ink),
   font families and weights, spacing scale, radii.
2. brand/brand.md: logo lockups and clear space, which colour leads,
   voice in five rules, and a "never" list. Facts only, no workarounds.
3. gates/: one script per countable rule. Fail on off-palette colours,
   fonts outside the pack, text contrast under 4.5:1, text under <min>px,
   wrong canvas size, Title Case in headings.
4. A render step: build the asset from code, screenshot it, run every gate,
   and print each failure with the element that caused it.
List anything in the guide you could not turn into a fact or a check,
so a designer can write it down as a principle.
```

UI Hub related reading: 
measuring AI slop
, 
linting agents onto your design system
, 
asking for editable designs, not pictures
, and 
design agents with memory
.

## References
- [langchain-ai/design-agent (Content Studio)](https://github.com/langchain-ai/design-agent) — LangChain · GitHub
- [How We Built Our Design Agent](https://www.langchain.com/blog/design-agent) — Amal Irgashev, Shreya Talegaonkar · LangChain
- [Content Studio is the design agent we use every day at LangChain](https://x.com/LangChain/status/2124926152703655977) — LangChain · X
- [Meet the Open-Source Slack Agent Behind 3,000 Branded Assets](https://www.geeky-gadgets.com/langchain-content-studio-design-agent/) — Julian Horsey · Geeky Gadgets
- [Deploy the open-source design agent](https://docs.langchain.com/langsmith/python/managed-deep-agents-design-agent) — LangChain Docs
- [Design agent spec (docs/spec.md)](https://github.com/langchain-ai/design-agent/blob/main/docs/spec.md) — LangChain · GitHub
- [Evals (docs/evals.md)](https://github.com/langchain-ai/design-agent/blob/main/docs/evals.md) — LangChain · GitHub
- [How HyperFrames fits into an application](https://hyperframes.heygen.com/developers/overview) — HeyGen · HyperFrames docs
- [Paper](https://paper.design) — Paper
- [Lovable changelog (Chat connectors: Paper, 23 Nov 2026)](https://docs.lovable.dev/changelog) — Lovable
- [Improving frontend design through Skills](https://www.claude.com/blog/improving-frontend-design-through-skills) — Anthropic · Claude blog