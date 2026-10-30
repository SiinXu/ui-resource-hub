# Canva Brush: AI design moves from generating to editing

> On 29 October Canva Research launched Brush, a vision-language model trained to edit existing designs: it reads the layout, writes code to change elements, checks the page and keeps everything editable. Canva claims up to 69% faster and 46% cheaper edits than its previous agent. What it does, what the numbers do and don’t prove, how it compares with Krea’s brand-kit-first Ad Studio, and a checklist for edit prompts that change only what you meant.

Blog post: <https://ui.incidental.site/blog/canva-brush-edit-dont-regenerate/>

The expensive moment in AI design is rarely the first prompt. It is the second one: “change only the headline”, and the tool rewrites the subtitle, moves the logo and picks a new blue. On 29 October Canva Research launched **Brush**, a vision-language model built for exactly that second prompt. Canva’s own framing is the useful part: generating a design is hard, but editing one is harder, because the model has to know what to change 
and what must stay exactly as it is
.

## What Brush is

- **An editing model, not an image model.** Brush looks at an existing Canva design, works out how it is put together and applies the change you ask for, from one line of copy to every slide in a deck. It arrived a week after Canva Craft, the company’s image-generation model; Canva’s split is that Craft makes the image and Brush refines the design around it.

- **It edits by writing code.** Behind the chat, Brush runs an agentic loop: it writes and runs code that adjusts design elements, then inspects the rendered page to decide the next step. The result is ordinary Canva layers, so text, images, colours and layout stay editable by hand.

- **How it was trained.** Canva started from an open-weights model and post-trained it on real design and editing tasks, using design expertise and anonymised data from people who opted in, then large-scale reinforcement learning. The reward scores visual quality, whether the layout follows design principles and whether the task was actually done, with “good” defined by Canva’s professional designers.

- **Availability.** Canva Pro, for supported edits in Canva AI: open or attach a design and pick 
Brush
 in the Canva AI model dropdown. Wider access is promised but not dated. Still missing, by Canva’s own list: Brand Kit support, referencing attachments, and better handling of image-heavy layouts.

## What the numbers do and don’t say

Canva reports Brush as up to 69% faster on general editing tasks and 46% cheaper per edit task than its previous design agent, and says in internal testing it matched or beat that setup on most editing tasks, strongest at restyling and adapting designs to new formats. These are vendor numbers against Canva’s own earlier agent, not a public benchmark, and “up to” describes the best case. The more telling detail is why Canva cares: at hundreds of millions of users, a few cents per edit decides whether a feature can ship to everyone. A small specialised model that is cheap enough to run on every edit is a product decision as much as a research one.

## Two answers to the same problem

The same evening, Krea launched **Ad Studio**, powered by its first Krea 3 “expert” model for advertising. You paste a brand’s website, it extracts a brand kit (logo, colours, typography) in a minute or two, then generates dozens of ads. Krea claims “full consistency” with the brand; no independent evaluation exists yet. Put side by side, the two launches show where AI design is heading: Krea gets consistency by 
extracting rules first
, Canva by 
starting from a design that already exists
. Both are moving away from the blank-canvas prompt, the same direction we saw with 
visual prompts in Cursor, v0 and Lovable
 and 
JSON brand kits for AI visuals
.

## Our take

An edit model that works through code on real layers is the right architecture: edits become operations on named elements, which can be scoped, repeated across pages and undone, instead of a fresh image that only resembles your design. The catch for teams is the missing Brand Kit support. Today Brush can see your design but not your brand rules, so “keep it on-brand” is still your job, and the best way to do it is to put the values in the prompt. Treat “restyle” and “resize for Instagram” as the sweet spot Canva itself names, and be more careful with image-heavy layouts until the promised fix lands.

## Checklist: edit prompts that change only what you meant

- **Name the scope.** Which pages and which elements: “slide titles on pages 2–5”, not “the deck”.

- **Name what must not move.** Body copy, images, logo position, page order. An edit model is only as precise as its “keep” list.

- **Give values, not adjectives.** Hex colours, font names and sizes beat “more premium”, especially while the model can’t read your Brand Kit.

- **One intent per prompt.** Batch only uniform changes (every header); split mixed requests into separate turns so you can check each.

- **For format remixes, say what to drop.** A slide becoming a 1080×1350 post needs to lose text, not shrink it.

- **Duplicate before sweeping edits.** Multi-page changes are where unrequested drift hides; keep the original to compare.

- **Check the pages you didn’t mention.** Look for text overflow, contrast below 4.5:1, broken alignment and changes outside your scope.

- **Finish by hand.** The output is normal layers; the last 10% is faster in the editor than in another prompt.

```
scope:   pages 2–5 · slide titles only
change:  font → Playfair Display 40 · colour #1F2A44
keep:    body copy · images · logo position · page order
check:   titles ≤ 2 lines · contrast ≥ 4.5:1 · nothing else moved
```

## How UI Hub helps

The “keep” list works best when your values already have names. 
Design tokens for agents
 covers writing them down, and 
linting agents onto your design system
 covers catching one-off values after an AI edit. For pointing at elements instead of describing them, see 
Point, don’t describe
; for how design tools are opening to outside agents, see 
agents that drive design tools
.

## References
- [Introducing Canva Brush, a vision-language model for design](https://www.canva.com/newsroom/news/canva-brush/) — Canva Research Team, Canva Newsroom
- [Introducing Canva Craft](https://www.canva.com/newsroom/news/canva-craft/) — Canva Newsroom
- [Canva launches AI design editing model ‘Brush’](https://www.capitalbrief.com/briefing/canva-launches-ai-design-editing-model-brush-48352e11-c62c-4319-973a-490efa945f92/) — Capital Brief
- [Canva launches Brush, an in-house vision-language model that edits existing designs](https://aipolix.com/en-us/news/canva-brush-vision-language-model-design-editing) — Aipolix
- [Canva Research unveils Brush vision-language model for design editing](https://ashutoshai.com/ai-compass/2026/10/29/canva-brush/) — AI Compass
- [Krea launches Ad Studio, powered by the first Krea 3 “expert” dedicated to advertising](https://neuralbrew.ai/en/articles/2026/10/krea-launches-ad-studio-first-expert/) — Iris & Tomo, Neural Brew
- [Ad Studio](https://www.krea.ai/ad-studio) — Krea
- [Canva AI](https://www.canva.com/ai/) — Canva