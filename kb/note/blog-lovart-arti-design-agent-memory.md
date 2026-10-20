# Lovart 2.0 and Arti: design agents learn to remember, run and review

> Lovart 2.0 adds an editable taste memory, scheduled design delegation and a background consistency check. Read alongside two other launches from 19 Oct, it shows where design agents are heading, and what you should write down before you hand one the work.

Blog post: <https://siinxu.github.io/ui-resource-hub/blog/lovart-arti-design-agent-memory/>

On 19 October Lovart shipped version 2.0 of its design agent, built around a new personal agent called Arti. The pitch is not a better image model. Lovart already routes to several third-party image and video models. The change is everything around generation: Arti keeps a memory of how you work, takes whole jobs on a schedule, researches before you start and checks the canvas while you work. It is a useful snapshot of where design agents are going, and of what you have to write down before you can trust one with real work.

## What actually shipped

- **Memory you can read and edit.** Lovart splits memory into four groups: basic information, collaboration style, aesthetic preferences and frequently used assets. Each entry can be viewed, edited or deleted, you choose whether it applies across projects, and you can seed it by chatting, from past projects, or by uploading a portfolio or a Markdown or memory file from another AI tool.

- **Design delegation.** Instead of a chain of prompts you write a brief (what to make, what to watch for, what done looks like), pick the target project, then run it once or daily, weekly or monthly. Each run has a credit limit, there is a Test run before you commit, and results land on a new canvas page. Lovart's own example: 168 product images for 42 SKUs in four sizes, run overnight after a four-SKU test.

- **Design Research and Design Review.** Research gathers references from sources such as Google, Pinterest and Behance into a report with a mood board. Review checks the canvas against the project's constraints in the background and only changes anything after you confirm. Lovart's example is a hand-drawn storyboard with one oil-paint frame that slipped through.

- **Self-evolving skills.** When you repeat the same workflow across projects more than three times, Lovart offers to save it as a reusable skill. You can switch this off.

## The same week, the same idea elsewhere

Two smaller launches on the same day point the same way. Gemini Notebook added a Review toggle so you can read and edit the outline or producer notes for slides and video overviews 
before
 anything renders. Automo's design engine now has a creative-director judge that looks at several rendered candidates and keeps the strongest, and its thumbs-up and thumbs-down now attach to the exact design you rated. Put together, the pattern is clear. The value is moving from "generate" to three other steps: remember what the person likes, show the plan before spending compute, and judge the output against something other than the average of the training data.

## Our take

Memory is only as good as what is in it. A vague "I like clean, modern design" in memory produces the same generic result as a vague prompt, now on every project. The strongest line in Lovart's announcement is its own example memory: show three clearly different directions first, then build out the one I pick. That is a process rule, and process rules are what agents follow well. Treat the memory panel the way we treat a guideline file: short, specific and testable. The Review step is promising for the same reason. A consistency check needs explicit constraints to check against, so write them down at the start of the project rather than hoping the agent infers them.

Delegation is where the real risk is. A weekly job that quietly drifts off-brand is worse than no job. Lovart's guardrails (test run, credit limit, results on a separate canvas page, run history, pause) are the right shape, and you should use all of them.

## Checklist: before you hand a design agent the work

- **Write the taste memory by hand.** Three to six lines: palette in named values, type pairing, density, two or three references, and a never-list. Upload it as Markdown instead of letting the agent guess from old projects.

- **Add one process rule.** For example "three distinct directions first, then build out the chosen one", or "always show the outline before rendering".

- **State constraints the reviewer can check.** Style, aspect ratios, logo clear space, text-on-image contrast. If it is not written, no background check can catch it.

- **Test before you schedule.** Run a small batch (Lovart's own example used 4 of 42 SKUs), read every output, then set the schedule and a credit cap.

- **Read the memory panel monthly.** Delete anything stale or wrong. Learned preferences are guesses until you confirm them.

- **Keep the final call.** Accept fixes one by one, the way Lovart's Review asks you to, and never let a scheduled run publish straight to a live channel.

```
# taste.md (upload as memory)
palette: cream #f6f1e7 · ink #1d1a16 · one accent, warm brown #8a5a3b
type: serif headlines + neutral sans body; no more than two weights
density: generous white space; one focal image per layout
process: show 3 clearly different directions first, then build the chosen one
never: neon gradients · stock 3D blobs · emoji as icons · text over busy photos
check: same illustration style on every frame · logo clear space ≥ 1× cap height
```

## How UI Hub helps

If you are writing that taste file from scratch, start from the house-style notes and specs in the 
UI Hub encyclopedia
, and our earlier piece on 
teaching agents taste
. The format is the same whether the agent is Lovart, Claude, Cursor or Figma's: short rules first, pixels second.

## References
- [Lovart 2.0: Meet Arti, your personal design agent](https://www.lovart.ai/news/lovart-2-0-arti) — Lovart
- [Lovart](https://www.lovart.ai/) — Lovart
- [How to shape your slides and videos with Gemini Notebook](https://blog.google/innovation-and-ai/products/gemini-notebook/co-create-slides-videos/) — Google (Viraj Doshi, Shan Wang)
- [Designs chosen by taste, not just by rule](https://automo.ai/releases/designs-chosen-by-taste-not-just-by-rule) — Automo.ai
- [Teaching agents taste: how design skills de-slop AI interfaces](https://siinxu.github.io/ui-resource-hub/blog/taste-and-skills-for-agents/) — UI Hub