# AI slop is now measurable: what a blind design benchmark found, and how to check your own pages

> On 18 November 2026 Contra Labs and BenchFlow published the Frontier Design Benchmark: 33 real client briefs, sites built by 15 models, and 4,311 blind votes from 35 professional designers. A stealth model called Gestalt topped it, but the more useful output is a list of patterns that make a page look AI-made, counted across hundreds of pages. What the benchmark measured, why designers still preferred flawed human work, our take on using it, plus a slop-lint checklist, a small eval you can run and an agent prompt.

Blog post: <https://ui.incidental.site/blog/ai-slop-patterns-frontier-design-benchmark/>

On 18 November Contra Labs, the research arm of the freelance marketplace Contra, published the **Frontier Design Benchmark** together with BenchFlow, a company that runs AI agents in sandboxes and records what they produce. The headline went around X and Hacker News within a day: a stealth model called **Gestalt**, with no named maker, ranked first at about 1,930 Elo, ahead of both the best named model and the human designers. A commenter from Contra clarified on Hacker News that it is a single model and not Contra’s own.

The leaderboard is the least durable part of the release. Gestalt cannot be used, and model names will change by spring. What lasts is the method and one of its by-products: a list of the visual habits that make a page look machine-made, each with a measured frequency. If you generate interfaces with AI, that list is a lint rule set you can run on your own work this week.

## What the benchmark actually measured

- **Real briefs, not “a landing page for a coffee shop”.** 27 of the 33 tasks are rewritten jobs from Contra’s marketplace and 6 come from startups with their own brand files and old sites. Contra says the median website brief on its platform runs 138 words on a budget of about $1,050, and three in four stack two or more constraints such as a logo, an audience and a business goal. Outputs include multi-page marketing sites, web apps with working flows and two mobile apps.

- **A human bar in the same race.** Contra designers made a moodboard of three directions, got feedback, built the site with tools of their choice and iterated. These “golden” designs were voted on blind alongside the models.

- **Three different instruments.** Blind pairwise votes from 35 professional designers (4,311 votes over five rounds, turned into ratings with a Bradley–Terry model; two random halves of the panel agree at Spearman 0.95). A Design Critique Rubric of about 35 checks grouped into structure, visual craft, and content and use, such as type hierarchy, spacing, contrast and whether everything renders whole. And a Slop Detector, a classifier trained on human-made and AI-made pages that scores 0 to 100 for how AI-looking a page is and lists the traits behind the score.

## Three findings worth more than the ranking

**The rubric agrees with designers about models, and disagrees about people.** Across the 15 models, rubric score tracks the vote ranking closely (r = 0.94). But the human golden designs scored 73.6 on the rubric, sixth of 16 and behind the top Claude and GPT models, because they had concrete faults: a button label too dark to read, a wordmark clipped by the section above. Designers still picked them in 74% of matchups (425 of 574). A checklist catches mistakes; it does not measure the thing people were voting on.

**Slop is mostly about frequency, and it is countable.** Contra published a small subset of its pattern list with numbers. A tiny letter-spaced label above a heading that repeats the heading appears on at least half the sections of 93% of AI pages in the detector’s training set, against 11% of human pages. One italic word in the headline: up to 51% of one model’s pages, no human golden design. Numbered sections (01, 02, 03): 17% of AI pages, no human page at all. Content boxed in cards almost everywhere: 86% to 97% of pages for three models.

**Each lab leaves fingerprints.** Claude models put a horizontal arrow on links and buttons on 81% to 96% of their pages; GPT models use a diagonal arrow on 87% to 94%. One GPT model writes two- or three-phrase slogan headings on 55% of pages, against 4% for other labs. Another model centres every section heading on 44% of pages, against 1% elsewhere. On the Slop Detector, human goldens read 0.9 and Gestalt read close to them; the three Claude models read 31 to 38, the two GPT models 41 to 53 and the two Gemini models 54 to 57. Among the models Contra ran itself, the lowest reading belonged to DeepSeek V4 Pro, which also ranked last, because its pages were often unfinished. Looking less like AI is not the same as being good.

## Our take

Treat the three instruments as three questions, and never collapse them into one score. 
Votes
 answer “which direction do people want?”. The 
rubric
 answers “what is broken and fixable?”. The 
slop reading
 answers “will this look like everyone else’s generated page?”. The golden-design result shows why the order matters: pick the direction by taste first, then use the rubric as a fix list, then lint for slop. Running the rubric first would have ranked the designs people liked best below five models.

Lint for ratios, not bans. An eyebrow label on one section is a choice; on every section it is a default showing through. The same goes for cards, arrows and centred headings. The fix is rarely to delete the pattern. It is to decide it once in your design system, which arrow glyph, which heading alignment, when a group earns a box, so the model’s house style stops deciding for you.

Read the headline with care. The operator of the ranking also sells evaluation data to labs, Gestalt’s sites do not appear in the public gallery, and its edge over the human designers rests on 28 head-to-head votes. NN/g’s aesthetic-usability effect is a reminder that a blind “which is better” vote rewards appeal, and appeal can hide usability problems. Use the leaderboard to shortlist tools, then test them on your own briefs.

We ran the published list against this blog. Our diagrams numbered their steps, so the diagrams in this post do not. The small uppercase keys inside our diagram boxes stay: each names a different value rather than repeating a heading, which is the case the list warns about.

## How to run a small design eval of your own

- **Write three real briefs.** Take them from past projects, each with at least two constraints: a logo or palette, an audience, a mobile requirement, a business goal. Same assets for every contestant.

- **Generate with each candidate, plus one human reference.** Same time box and the same number of revision turns. If you can, run each model in the tool you would actually use.

- **Vote blind in pairs.** Three to five people who ship design. Strip tool names, shuffle sides for each pair, ask one question (“which would you hand to this client?”) and one optional sentence of why.

- **Diagnose after voting.** Score each output on a short rubric (hierarchy, spacing, contrast, broken or clipped elements, prompt adherence) and run the slop lint below. The deliverable is a fix list per tool, not just a winner.

- **Feed fixes back as rules.** Every recurring fault becomes a line in your design guidelines or agent skill, so the next generation starts above it.

## Slop-lint checklist

- Small uppercase, letter-spaced labels above more than half of the section headings?

- An italic or highlighted word inside the main headline?

- Sections numbered 01, 02, 03 when the order carries no meaning?

- Most content groups inside bordered or filled cards?

- The same arrow glyph (→ or ↗) on nearly every link and button?

- Headings written as parallel slogans, with body copy that never says how the product works?

- Every section heading centred, or cards and phones tilted at an angle by default?

- Rubric basics: one clear type hierarchy, consistent spacing, readable contrast on every button, nothing clipped at 390 px and 1280 px, light and dark?

```
# Paste this into your design or coding agent
Audit the pages in <folder or URL list> for AI-default patterns.
- For each page, count sections and report the share that have:
  a small uppercase letter-spaced label right above the heading,
  a bordered or filled card around most content, a centred heading,
  a rotated element, and an arrow glyph (→ ↗) in links or buttons.
- Flag an italic or highlighted word inside the h1, numbered section
  labels (01, 02 …), and slogan-style headings.
- Flag any ratio above 50% and propose one design-system rule per flag
  (e.g. "arrows only on external links"). Do not change code yet.
- Then check rubric basics at 390 px and 1280 px, light and dark:
  contrast on buttons, clipped text or logos, type hierarchy, spacing.
Return a table and a short fix list. Wait for my approval.
```

Related on UI Hub: 
teaching agents taste with design skills
, 
linting agents onto your design system
, and 
making AI design variants comparable
.

## References
- [Frontier Design: Evaluating AI on Real World Design Tasks](https://contralabs.com/research/frontier-design-benchmark) — Contra Labs
- [Frontier Design Benchmark leaderboard](https://contralabs.com/frontierdesign/leaderboard) — Contra Labs × BenchFlow
- [Methodology](https://contralabs.com/frontierdesign/methodology) — Contra Labs × BenchFlow
- [Design Critique Rubric and Slop Detector](https://contralabs.com/frontierdesign/rubric) — Contra Labs × BenchFlow
- [Gallery of model and human outputs](https://contralabs.com/frontierdesign/gallery) — Contra Labs × BenchFlow
- [Stealth model Gestalt beats Claude Fable 5.2 on the Frontier Design Benchmark](https://pasqualepillitteri.it/en/news/35144/stealth-model-gestalt-beats-fable-5-2-frontier-design-benchmark) — Pasquale Pillitteri
- [Two stealth models just appeared on the leaderboard, both ahead of Fable 5.2 (discussion)](https://news.ycombinator.com/item?id=50558559) — Hacker News
- [BenchFlow](https://benchflow.ai) — BenchFlow
- [Bradley–Terry model](https://en.wikipedia.org/wiki/Bradley%E2%80%93Terry_model) — Wikipedia
- [The Aesthetic-Usability Effect](https://www.nngroup.com/articles/aesthetic-usability-effect/) — Kate Moran · Nielsen Norman Group
- [How to Conduct a Heuristic Evaluation](https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/) — Nielsen Norman Group