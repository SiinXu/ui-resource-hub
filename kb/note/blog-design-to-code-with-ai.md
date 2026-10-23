# Design-to-code with AI: map to your components, not to pixels

> Pixel-perfect export creates throwaway code. Give the agent your component registry and tokens via MCP so output reuses what you already ship.

Blog post: <https://ui.incidental.site/blog/design-to-code-with-ai/>

Early design-to-code tools translated frames into absolutely positioned divs. The result looked right in one viewport and was unmaintainable everywhere else. The current generation works differently. Figma's MCP server, Builder.io's Visual Copilot and agents running inside Cursor or Claude Code read 
structure and variables
 and can map them to code you already own. Whether you get reusable code or throwaway markup now depends less on the tool and more on what you feed it.

## The core idea: map, don't trace

A design file contains three kinds of information: **structure** (frames, auto-layout, nesting), **decisions** (variables for colour, spacing, radius, type) and **components** (instances of a button, an input, a card). Tracing copies the pixels. Mapping turns structure into flex and grid, decisions into your CSS variables, and component instances into your own `<Button>` and `<Input>`. Mapped output is a pull request you can merge. Traced output is a screenshot written in HTML.

## Step 1: make the design file readable

Models can only map what is explicit. Before you connect any tool:

- **Use auto-layout everywhere.** A frame without it forces the model to guess flex direction, gap and alignment from coordinates. Guessed layouts break at the first resize.

- **Bind styles to variables.** A fill of `#2563EB` gives the model a hex code. A fill bound to `color/accent` gives it a name it can map to `var(--accent)`.

- **Use real component instances.** A detached button is just a rectangle with text. An instance of your Button component tells the agent which code component to use.

- **Name layers like code.** "Frame 482" carries no meaning. `PricingCard / Featured` carries a lot.

## Step 2: export tokens as code

Keep one source of truth for design decisions and generate CSS variables from it. The Design Tokens Community Group format is a JSON shape that tools like Style Dictionary can transform:

{
  &quot;color&quot;: {
    &quot;accent&quot;:  { &quot;$type&quot;: &quot;color&quot;, &quot;$value&quot;: &quot;#2563eb&quot; },
    &quot;surface&quot;: { &quot;$type&quot;: &quot;color&quot;, &quot;$value&quot;: &quot;#ffffff&quot; }
  },
  &quot;radius&quot;: { &quot;md&quot;: { &quot;$type&quot;: &quot;dimension&quot;, &quot;$value&quot;: &quot;10px&quot; } }
}

:root {
  --color-accent: #2563eb;
  --color-surface: #ffffff;
  --radius-md: 10px;
}
[data-theme=&quot;dark&quot;] {
  --color-surface: #0d0f15;
}

When the agent sees that `color/accent` in Figma and `--color-accent` in CSS share a name, it uses the variable instead of pasting hex values.

## Step 3: publish a component registry

A registry tells tools which components exist in your codebase and how to install them. With shadcn/ui, a `registry.json` lists your items and the CLI builds them into installable JSON files:

# build registry items from registry.json into public/r/
npx shadcn@latest build

# install one of your own components into another project
npx shadcn@latest add https://your-domain.com/r/pricing-card.json

Figma's Code Connect solves the same problem from the design side: it links a Figma component to the code component, so design context sent to an agent can say "this is `<Button variant="primary">`" instead of describing a blue rectangle.

## Step 4: connect the bridge

The Figma MCP server exposes the selected frame's structure, variables and component mappings to an MCP client such as Cursor, VS Code or Claude Code. The workflow is short:

- Select one frame, not the whole page. Smaller context gives better code.

- Ask the agent to fetch the design context for the selection and list which of your components it will use before writing code.

- Correct that list first. It is much cheaper to fix "use `Card`, not a div" before 200 lines exist.

- Let it generate, then review the diff like any other PR.

Builder.io's Visual Copilot follows a similar path from a Figma plugin and can also map to your components. Whichever bridge you use, the quality ceiling is set by Steps 1–3.

## Step 5: review generated code like a junior's PR

Generated UI is usually right in the default state and wrong at the edges. Review these every time:

- **Empty, loading and error states.** The design file usually shows only the happy path.

- **Long content.** Paste a 60-character name and a German translation; check wrapping and truncation.

- **Responsive behaviour** below the smallest frame in the file.

- **Hard-coded values.** Search the diff for hex colours and pixel sizes that should be tokens.

- **Accessibility.** Buttons are `<button>`, inputs have labels, focus is visible, dialogs trap focus.

# quick checks on a generated diff
git diff | grep -nE '#[0-9a-fA-F]{3,6}\b'      # raw hex colours
git diff | grep -nE '\b[0-9]{2,}px\b'           # magic pixel values
git diff | grep -n 'onClick' | grep -n '<div'   # clickable divs

## Pitfalls

- **Converting a whole page at once.** The context gets huge and the model starts inventing structure. Go frame by frame.

- **Detached instances.** One detached component in a frame produces one-off markup that never updates with your library.

- **Two sources of truth for tokens.** If Figma variables and CSS variables drift, the agent will faithfully reproduce the drift.

- **Skipping the plan step.** Asking for code immediately means you review 300 lines instead of a 10-line component list.

- **Pixel-perfect expectations.** Mapped code will differ by a few pixels because it uses your spacing scale. That is the point.

## Questions we get

**Is it worth it for a small project?** If you will build fewer than five screens, skip the registry and just give the agent your tokens file and a list of components. The full pipeline pays off when several people or several agents build screens over months.

**What if the design file is messy and we cannot fix it?** Then do not convert from it directly. Ask the agent to describe the frame in words first (sections, components, content), correct that description, and generate from the description plus your kit. A clean description beats a messy file.

**Which bridge should we pick?** Pick the one your designers already use and that can see your component mappings. The bridge matters less than whether variables, auto-layout and component instances exist in the file.

**How do we measure success?** Count how much generated code survives review unchanged, and how many raw values reviewers had to replace with tokens. Both numbers should improve week over week as the registry grows.

## Our take

Treat the registry and token pipeline as infrastructure, not a one-off. The first screen takes longer because you are setting up mappings; every later screen gets cheaper because the agent reuses them. Teams that skip this step get fast first drafts and slow maintenance forever.

## Checklist

- Frames use auto-layout; layers have meaningful names

- Fills, spacing and radii are bound to variables

- Tokens exported to CSS variables with the same names

- Components published in a registry or linked with Code Connect

- Agent lists components before generating code

- Diff reviewed for states, long content, hex values and a11y

## References
- [Introducing the Figma MCP server](https://www.figma.com/blog/introducing-figma-mcp-server/) — Figma
- [Figma to code with Visual Copilot](https://www.builder.io/blog/figma-to-code-visual-copilot) — Builder.io
- [shadcn/ui Registry](https://ui.shadcn.com/docs/registry) — shadcn
- [Tailwind CSS dark mode docs](https://tailwindcss.com/docs/dark-mode) — Tailwind Labs
- [Guide to the Figma MCP server](https://help.figma.com/hc/en-us/articles/32132100833559-Guide-to-the-Figma-MCP-server) — Figma Help Center
- [Code Connect](https://help.figma.com/hc/en-us/articles/23920389749655-Code-Connect) — Figma Help Center
- [Design Tokens Community Group](https://www.designtokens.org/) — W3C Community Group
- [Style Dictionary](https://styledictionary.com/) — Style Dictionary
- [shadcn CLI](https://ui.shadcn.com/docs/cli) — shadcn