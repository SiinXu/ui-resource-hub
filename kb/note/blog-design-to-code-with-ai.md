# Design-to-code with AI: map to your components, not to pixels

> Pixel-perfect export creates throwaway code. Give the agent your component registry and tokens via MCP so output reuses what you already ship.

Blog post: <https://siinxu.github.io/ui-resource-hub/blog/design-to-code-with-ai/>

Early design-to-code tools translated frames into absolutely positioned divs. They looked right and were unmaintainable. The current generation, Figma's Dev Mode MCP server and Builder.io's Visual Copilot among them, works differently: it reads 
structure and variables
 and maps them to code you already own.

## What to feed the agent

- **Tokens** exported as CSS variables, so colours map to `var(--accent)` instead of hex.
- **A component registry**, for example a shadcn registry, so "button" means your Button.
- **Auto-layout in the file**. Frames without it force the model to guess flex rules.

## Our take

Treat generated code as a pull request from a junior: correct-looking, missing edge states. Always check empty, loading, error and long-text states, and run an a11y pass. Teams that publish a registry once get compounding returns from every later generation.

## References
- [Introducing the Figma MCP server](https://www.figma.com/blog/introducing-figma-mcp-server/) — Figma
- [Figma to code with Visual Copilot](https://www.builder.io/blog/figma-to-code-visual-copilot) — Builder.io
- [shadcn/ui Registry](https://ui.shadcn.com/docs/registry) — shadcn
- [Tailwind CSS dark mode docs](https://tailwindcss.com/docs/dark-mode) — Tailwind Labs