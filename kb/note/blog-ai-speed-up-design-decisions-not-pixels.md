# AI made the code fast but not the design decisions: speed up the decision, not the pixels

> On 26 November Tailwind CSS creator Adam Wathan wrote that he still spends as long on every design decision as he did in 2021, and the post drew about 2,000 likes and 360 replies in two days. His examples were not pixel problems: what to show, dialog or page, save instantly or confirm, how to mark unsaved batch edits. AI cannot make those calls for you, but it can shorten the three slow parts of every decision: gathering evidence, making the options concrete and remembering what was decided. How to sort decisions by how hard they are to undo, his four questions worked through, a checklist and a prompt.

Blog post: <https://ui.incidental.site/blog/ai-speed-up-design-decisions-not-pixels/>

On 26 November Adam Wathan, who created Tailwind CSS, posted that he still had not found a way to use AI to meaningfully speed up design work, and that he spends as long on every decision as he did in 2021. By 28 November the post had about 2,000 likes, 360 replies and more than 229,000 views, which says the feeling is widely shared. A day later he listed the kind of decisions he meant: what information would be useful to show here; should this be a dialog or its own page; should a button save instantly or ask for confirmation; and, for batch edits, how to mark what has changed but is not yet saved.

The replies split along a useful line. Emil Kowalski, who builds and teaches interface craft, answered that AI works best as support on details such as shadows, motion values and typography, and that handing the bigger decisions to an agent seems both hard and less healthy than leaving them to people. Wathan agreed, and added the part that stings: because everything else now moves so fast, time spent thinking about design starts to feel like time you are not allowed to spend. Alex Barashkov, from the other side, argued that the frustration usually comes from how designers use AI: one thread at a time, all-or-nothing expectations, no design system the agent can read, problems scoped too small, and no plan for letting agents work overnight while you review in the morning.

## What the thread is really about

Look at the four examples again. None of them is about how a screen looks. Each one is a judgement about people, data and risk: what this user is trying to do at this moment, how much context they need on screen, what happens if they make a mistake. Models are fast at producing an answer to “make a settings dialog”. They are not in a position to know whether your users edit one record a week or two hundred a day. So the generation step got much faster, and the decision step did not, which is exactly what Wathan describes.

Our take is that both sides of the thread are right, and that the fix is to stop timing the wrong thing. A design decision has three slow parts that are not the decision itself, and AI is good at all three:

- **Evidence.** Reading support tickets, analytics events, the data model, the design system docs and how comparable products handle the same flow. An agent can gather and summarise this in minutes; you read the summary, not the raw pile.

- **Concrete options.** Arguing about “dialog or page” in the abstract is slow. Two working versions, built in your real app with real data and real text lengths, usually settle it in minutes. This is where cheap code changes the economics of design most.

- **Memory.** Most teams re-decide the same questions every few months because the answer lived in a meeting. A short decision record in the repository, which the agent reads before building, turns one decision into a rule that applies everywhere.

## Sort decisions by how hard they are to undo

The other way to get faster is to spend less time on decisions that do not deserve it. Jeff Bezos’s shareholder letters describe this well: most decisions are “two-way doors” that can be reversed and should be made quickly with about 70% of the information you wish you had, while a few are “one-way doors” that deserve slow, careful deliberation. The mistake is running every decision through the heavy process. Lovable shipped the same idea into its agent on 19 November: when it asks you a question it now keeps building whatever does not depend on the answer, picks an option for the rest and reworks it if you choose differently, but it waits for you before a step that is hard to undo, such as deleting data.

In interface work, most choices are two-way doors once the UI is code: dialog versus page, the order of fields, which columns a table shows, the wording of an empty state. Pick a sensible default, ship it, watch what happens and change it. The one-way doors are the ones where users or their data get hurt: destructive actions, anything involving money or permissions, emails and notifications that go out to people, migrations, and public URLs. Spend your slow, human thinking there.

## Wathan’s four questions, worked through

- **What information is useful to show here?** Ask the agent for every field the data model has, what users ask about in support tickets and which fields are used in search or filters. Then you decide one thing: what is the user trying to do on this screen? Show what serves that task, put the rest one click away.

- **Dialog or its own page?** Nielsen Norman Group’s guidance is a good default: modal dialogs interrupt, so keep them for short, focused input that is needed to continue, and avoid them for complex decisions that need information the dialog hides. Have the agent build both with your longest real content, and the answer is usually obvious once you see a form scroll inside a modal.

- **Save instantly, or confirm first?** Decide by reversibility. If a change can be undone, save it instantly and offer undo. If it cannot, confirm, and say exactly what will happen; NN/g warns that confirmations on routine actions train people to click through them. For long multi-step submissions, a review step like the GOV.UK Design System’s check answers pattern gives people a second chance to catch errors.

- **How do we mark unsaved batch edits?** This one is a craft question, which is where AI helps most. Ask for three markers side by side (a dot on the changed row, a tinted cell with the old value on hover, a sticky bar counting unsaved changes with Save and Discard), check that none of them relies on colour alone, then pick.

## Plan for the slow part

Barashkov’s scheduling tip is the most practical idea in the thread. Spend the last half hour of the day turning open design questions into agent tasks: gather the evidence, build the two variants, list the edge cases. In the morning, review the results in one sitting and make the calls. The thinking time does not disappear, but it stops being spent on setup and on arguing about options that nobody has seen. And keep Kowalski’s point in mind: the goal is not to delegate taste, it is to give your taste better material to work with.

## Checklist: speeding up a design decision

- Did you write the decision as a question with the user’s task in it, not as a screen to produce?

- Is it a one-way door (data loss, money, permissions, messages to users, public URLs) or a two-way door?

- For two-way doors: did you pick a default with the evidence you have and move on?

- Did an agent gather the evidence (tickets, analytics, data model, design system, comparable flows) before you started thinking?

- Did you compare at least two working variants in the real app with real data, not mockups?

- Did you write the criteria before looking at the variants, so the prettiest one does not win by default?

- Do destructive or irreversible actions say exactly what will happen, and do reversible ones offer undo instead of a dialog?

- Is the decision recorded in the repository (one line on what, one on why) where the agent reads it next time?

```
# Paste into a coding agent, with the design question filled in
Design question: [e.g. edit a customer’s address in a dialog or on its own page?]
Do not decide for me. Prepare the decision:
1. Evidence: summarise what the data model, support tickets, analytics events
   and our design system docs say about this flow. Quote sources, max 10 bullets.
2. Classify: is this reversible (two-way door) or not? List what could
   go wrong for users or their data in each option.
3. Options: build two working variants behind a flag in the real app, using
   our components, real data and the longest real text. No mockups.
4. Criteria: propose 3–5 criteria from the evidence before showing the variants.
5. Record: draft a decision entry for docs/decisions.md with a blank for
   the choice and one line of rationale. I will fill in the choice.
```

UI Hub related reading: 
making parallel design directions comparable
, 
taste and skills for agents
, 
approval UI for agents
, and 
putting the rules of a design agent in code
.

## References
- [“I still haven’t figured out how to use AI to meaningfully accelerate design work”](https://x.com/adamwathan/status/2125974928327369009) — Adam Wathan · X
- [Examples of the design decisions he means](https://x.com/adamwathan/status/2126323078254694755) — Adam Wathan · X
- [AI works best as a support when it comes to design](https://x.com/emilkowalski/status/2126324277154652350) — Emil Kowalski · X
- [Reply: “it appears so slow compared to how quickly we can move on other things”](https://x.com/adamwathan/status/2126325200249876820) — Adam Wathan · X
- [Where designers’ frustration with AI usually comes from](https://x.com/alex_barashkov/status/2126000568820724122) — Alex Barashkov · X
- [Lovable changelog (Lovable keeps working while you answer its questions, 19 Nov 2026)](https://docs.lovable.dev/changelog) — Lovable
- [2016 Letter to Shareholders (two-way doors, decisions with about 70% of the information)](https://www.aboutamazon.com/news/company-news/2016-letter-to-shareholders) — Jeff Bezos · Amazon
- [Confirmation Dialogs Can Prevent User Errors — If Not Overused](https://www.nngroup.com/articles/confirmation-dialog/) — Jakob Nielsen · Nielsen Norman Group
- [Modal & Nonmodal Dialogs: When (& When Not) to Use Them](https://www.nngroup.com/articles/modal-nonmodal-dialog/) — Nielsen Norman Group
- [Check answers pattern](https://design-system.service.gov.uk/patterns/check-answers/) — GOV.UK Design System
- [Understanding SC 1.4.1: Use of Color](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html) — W3C WAI