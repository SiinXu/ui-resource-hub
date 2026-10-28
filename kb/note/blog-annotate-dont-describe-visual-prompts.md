# Point, don’t describe: visual prompts for UI edits in Cursor, v0 and Lovable

> On 27 October Cursor added Annotate to Design Mode: click, box, draw, edit text or CSS on your running app and the agent gets the element’s identity plus a cropped screenshot. v0 and Lovable already let you point at a preview. What each one actually sends to the model, where pointing beats a paragraph, where it quietly breaks your design system, and a checklist for notes that land first time.

Blog post: <https://ui.incidental.site/blog/annotate-dont-describe-visual-prompts/>

“Make the second card match the first, but tighter” is a hard sentence for a coding agent. Which second card? Tighter how? The agent has to search the code for something that looks like your description, and when it guesses wrong you write a correction that is longer than the original request. On 27 October Cursor shipped Annotate, a reworked version of its browser Design Mode that lets you answer those questions by pointing at the running app. v0 and Lovable offer their own version of the same idea. Taken together they show that, for interface work, the useful prompt is becoming 
a pointer plus a small change
 rather than a paragraph.

## What each tool sends to the model

- **Cursor Design Mode with Annotate (27 October, Cursor 3.24.18 or later).** It lives in the browser inside the Agents Window; click Annotate or press `Cmd/Ctrl + Shift + D`. You click an element (arrow keys move the highlight to its parent or child), Shift-click to add more elements to the same note, drag to box an area and draw with pen, ellipse, rectangle or arrow, double-click text to edit it in place, open a CSS inspector on a single element, or dictate. For every picked element the agent receives the tag, id, classes, attributes, a selector path, the first 200 characters of visible text, size and position, six computed styles (colour, background, font size, font family, display, position) and, in React, Vue and Svelte apps, the component name and component stack. It also gets a screenshot cropped to the element or to your marked-up area. Notes go out one at a time by default; a 
Batch edits
 switch collects them as numbered pins and sends them as one message. Cursor recommends a fast UI-capable model for this loop, naming Composer 2.5.

- **v0 Design mode.** You select an element in the live preview and either adjust it in a panel (typography, colour, background, margin and padding, border, opacity and radius, shadow, text) or type an instruction, and v0 attaches a screenshot of the element to it. When the project uses Tailwind, the panel offers Tailwind-compatible values. Edits stay pending, with undo, reset and a before-and-after toggle, until you press Apply; Apply sends everything to the chat and produces a normal new version you can diff or revert. A Design Mode API lets teams embed the same editor in their own product.

- **Lovable preview toolbar.** It replaced the older Visual edits panel with four modes: select elements (Cmd/Ctrl-click for several), edit text inline, draw an annotation that is sent as a marked-up screenshot (rough shapes are cleaned up), and pinned comments for teammates. Comments are free; sending one to Lovable, selecting, and drawing use build credits. Each account gets 100 free inline text edits per rolling 24 hours, with a shared workspace cap of 2,000.

## Our take

The three tools split along one line: **does the tool apply your visual change itself, or translate it for the agent?** v0 sits closest to a design tool: panel edits are concrete values, the result is a reviewable version, and the model mainly turns them into source. Cursor and Lovable treat your mark as context: the agent still decides what code to change, but it starts from the right component instead of a guess. Cursor sends the richest context, structured element data and the component stack as well as pixels, which is why it can work inside large existing codebases rather than only in a generated project.

Pointing has two blind spots. First, a note captures one frozen state at one width. The agent sees the hover you circled at 1440 px, not the empty state, the error state or the 375 px layout, and will happily fix only what it saw. Cursor’s announcement mentions reviewing designs at different screen sizes, but the check is still yours. Second, direct manipulation produces raw values. Drag a padding to 18 px or pick `#3b82f6` in an inspector and you have just written a one-off that your design system doesn’t know about. v0’s Tailwind-aware values help, but none of these tools promise to map an edit to your tokens. Tell the agent to do it, and lint for it afterwards.

Our rule of thumb: **point for 
where
, write for 
why
.** The mark gives location, the sentence gives intent and limits. “Match this card’s spacing to the one on the left, use our space tokens, don’t change the copy” is a better note than either a drawing or a paragraph on its own.

## Checklist: visual notes that land first time

- **Pick the smallest target.** Use the parent and child highlight (arrow keys in Cursor) until the box is the component you mean, not its wrapper or one span inside it.

- **Use multi-select for relationships.** Select both elements when the change is “make A match B”, “remove the duplicate” or “align these”. A single selection makes the agent hunt for the other one.

- **Draw only for areas.** Box or circle when the change is about a region (crowding, a gap, where a new element goes), not to point at a single button.

- **Write intent and limits in one line.** Say what should change, the token or component to use, and what must not change.

- **Translate raw values into tokens.** After a CSS-inspector or panel tweak, add “use the nearest existing token” and let your design-system lint fail on hard-coded colours and spacing.

- **Batch related notes, send unrelated ones alone.** A round of spacing fixes on one screen is one batch; a copy fix and a layout change on different pages are separate notes the agent can run in parallel.

- **Re-check the other states.** After each round, look at 375 px, dark mode, empty, loading, error and keyboard focus. The note only showed one of them.

- **Review the diff, not just the preview.** Hot reload shows that it looks right. The diff shows whether the agent changed a shared component that ten other pages use.

```
# a visual note that works (target + intent + limits)
target:  PricingCard[plan="Pro"]  + PricingCard[plan="Team"]   # multi-select
change:  make Team match Pro: same padding, same badge position
use:     --space-6 for padding, Badge variant="outline"
keep:    copy, prices, button labels
check:   375px stack, dark mode, focus ring on CTA
```

## How UI Hub helps

Pointing only stays on-brand if the agent has tokens to map onto. Our post on 
design tokens for agents
 covers how to write them down, and 
linting agents onto your design system
 covers catching the one-off values that visual edits produce. For the tools themselves, see 
v0 in practice
 and 
Lovable and Bolt
; for the states a single note won’t show, see 
accessibility in AI-generated UI
.

## References
- [Design Mode](https://cursor.com/docs/agent/design-mode) — Cursor Docs
- [Direct agents with visual prompts in Design Mode](https://cursor.com/blog/design-mode) — Erik Nilsson, Ian Huang & Ryo Lu, Cursor
- [Release notes](https://cursor.com/docs/release-notes) — Cursor Docs
- [New in Cursor design mode: Annotate](https://x.com/cursor_ai/status/2115159585548021814) — @cursor_ai on X
- [Cursor’s Design Mode adds Annotate: point and draw instead of describing UI changes to agents](https://automater.ai/news/cursor-design-mode-annotate-point-draw-agents/) — Automater News
- [Cursor adds Annotate to Design mode](https://daily.dev/posts/cursor-adds-annotate-to-design-mode-t6xlmktyu) — daily.dev
- [Design mode](https://v0.app/docs/design-mode) — v0 Docs
- [Edit from the preview](https://docs.lovable.dev/features/visual-edit) — Lovable Documentation