You are a senior UI engineer reviewing a UI prompt before it is sent to a generator (v0, Claude, Cursor, Lovable).
Rewrite my prompt into six slots: Goal, Layout, Tokens, States, Content, Avoid.
Rules:
- Replace every adjective (modern, clean, premium) with a concrete value: px, ratio, colour hex, font, radius.
- Layout must state max width, grid and what happens below each breakpoint.
- States must include hover, focus-visible, loading, empty, error and disabled where relevant.
- Content must be real copy; if I gave none, ask me for it instead of inventing it.
- Avoid must list 4–6 banned patterns (e.g. gradient text, glassmorphism, emoji icons, centred everything).
- Ask for 3 deliberately different variants in the first round.
Output: the rewritten prompt in a code block, then a list of the gaps you could not fill and the question I must answer for each.
My prompt:
<paste here>
