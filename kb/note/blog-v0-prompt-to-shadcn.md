# v0 in practice: from a prompt to shadcn code you can keep

> v0 is strongest when you treat it as a shadcn/Tailwind code generator, not a design oracle. Brief it like an engineer, then pull the code into your repo.

Blog post: https://siinxu.github.io/ui-resource-hub/blog/v0-prompt-to-shadcn/

v0 by Vercel generates React components built on shadcn/ui and Tailwind CSS. That stack choice is the whole point: the output is ordinary, readable code using primitives many teams already ship, so the result can leave the tool. Treat v0 as a fast pair-programmer for UI, and judge it by whether you would merge its code.

## A brief that works

- **Name the components.** "Use Card, Tabs and a Table with a sticky header" beats "make a nice dashboard". v0 knows the shadcn vocabulary, so use it.

- **Give tokens, not adjectives.** Radius, one accent colour, font, density. "Modern" means nothing to a model; `--radius: 0.5rem` does.

- **List the states.** Empty, loading, error, long text. Generators default to the happy path.

- **Paste real content.** Lorem ipsum hides layout bugs; real names and prices expose them.

## Iterate in small, named steps

Ask for one change per turn ("tighten the table to 40px rows; keep everything else"). Big rewrites tend to regress parts you already liked. When something is right, say so explicitly so it stays.

## Getting the code out

v0 lets you add generated code to a project through the shadcn CLI or download it, and it deploys to Vercel. Whichever path you take, review it like a PR: check that colours come from CSS variables rather than hard-coded hex, that interactive elements are real buttons and links, and that focus styles exist.

## Our take

v0's ceiling is your brief and your design system. Teams that already use shadcn get the most out of it because the output drops straight into their codebase. Pair it with a taste skill or the guidelines in our encyclopedia to avoid the generic "centred hero + three cards" result.

## References
- [v0 by Vercel](https://v0.app/) — Vercel
- [v0 documentation](https://v0.app/docs) — Vercel
- [shadcn/ui](https://ui.shadcn.com/) — shadcn
- [shadcn CLI docs](https://ui.shadcn.com/docs/cli) — shadcn