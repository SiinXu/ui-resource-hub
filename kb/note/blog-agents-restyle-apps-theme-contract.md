# Agents can now restyle the apps you use. Give them a theme contract, not your class names

> In mid-November 2026 two coding tools let an agent repaint their own interface: Claude Code themes are mods that call $.theme.set from a few anchor colours, and T3 Code merged agent tools that publish a theme with colours and CSS. Under the fun backdrops sits a design-system lesson: anchors that generate a checked palette, stable data-slot hooks, a guard against remote loads, and a one-key way back. What each tool does, our take, a checklist and an agent prompt.

Blog post: <https://ui.incidental.site/blog/agents-restyle-apps-theme-contract/>

Two of the most-shared developer-tool changes on X this weekend were about looks, not code. Claude Code’s desktop app can now be repainted by a mod: your colours, plus an animated scene behind the conversation with frosted panels over it, and Anthropic ships an example plugin whose `/custom-theme` command offers twenty scenes. In the same days T3 Code, the open-source front end for several coding agents, merged a pull request titled “agents can restyle T3 Code with theme colors and CSS” (merged 14 November UTC, nightly builds only for now). Ask the agent to “give T3 Code a solarized theme” and every connected web and desktop client repaints.

It is easy to file this under desktop wallpaper. We think it is the first public, working example of something design-system teams will have to plan for: an interface whose look is changed through an API that an agent calls, by people who never open your design files. The two tools made different choices, and between them they show what a safe theme surface needs.

## What each tool actually lets an agent change

- **Claude Code: a theme is a mod.** There is no theme file. A mod, a small JavaScript or TypeScript module, calls `$.theme.set` when a session starts, with `colors`, an optional `backdrop`, and a colour-scheme override (v2.1.319 or later). Colours come from `makeColors`, a helper that builds the whole palette from three anchors per mode: `surface-0`, `text-primary` and `text-muted`. It returns a `problems` list, and an entry starting “Desktop won’t paint this theme” means the app refuses it. One theme per session: whichever mod calls last wins, and a call replaces the whole theme.

- **Claude Code: deeper than colour.** Each place Claude Code draws, from the spinner to message rows and the question dialog, is a “render site” a mod may restyle or replace. The permission prompt is deliberately not one.

- **T3 Code: a theme is data.** A theme is a JSON file. The shortest form needs only `appearance`, a `canvas` colour and an `accent`; the app generates the rest, and an optional `css` string adds rules. Two agent tools, `t3_theme_read` (themes plus a styling guide) and `t3_theme_set` (publish and switch), do the work, and only for an agent on the server’s own machine running in Full access.

- **T3 Code: a published selector contract.** The styling guide lists 29 selectors theme CSS may rely on, such as `[data-chat-header]` and `[data-slot="button"]`, and a test fails if one disappears from the source. Elements that had no hook got one (`data-user-message-bubble`, `data-slot="project-monogram"`). The docs say it plainly: class names change between releases, so target `data-` attributes.

- **T3 Code: a guard and a way back.** Clients drop `@import`, `image-set()` and any `url()` that is not a `data:` address or an `#id`, so an imported theme or a prompt-injected agent cannot send the screen to another host. If a rule hides something you need, `t3 theme set t3-chat` or Cmd/Ctrl+Option/Alt+A restores a built-in theme. CSS was capped at 20,000 characters, raised to 50,000 a day later after a community restyle hit the limit.

## Our take: theming is becoming an API, so design it like one

For years a theme was a settings page a person clicked through. Now it is a call an agent makes on someone’s behalf, often from a one-line wish. That changes what a design system owes the outside world. Your tokens and hooks stop being internal implementation and become a public contract, with the same duties as any API: few inputs, validation, versioning and an undo.

The two tools split the problem well. Claude Code keeps the input small (three anchors per mode) and lets code generate and check the rest, which is how you stop an agent from shipping grey-on-grey text. T3 Code keeps the escape hatch, raw CSS, but fences it: only named hooks are promised, nothing remote loads, there is a size cap and a keyboard way back. Neither lets a theme touch the trust surface, the permission prompt in Claude Code, remote requests in T3 Code. A product that wants to be restyled safely needs all three layers.

The caveat is in T3 Code’s own limits: the agent cannot see the result, so the guide tells it to make small changes and ask. Claude Code mods, meanwhile, run with your permissions and are not sandboxed, and the docs say so. A theme you install from a stranger is code first and colour second. Read what it hooks before you let it repaint anything.

## What to do with this, even if your app has no theme editor

The same contract helps your own coding agents. An agent asked to “make the header calmer” edits whatever it can find; give it anchors, role tokens and named slots, and it edits those instead of hunting through generated class names. Three cheap moves: add `data-slot` names to the twenty or so parts people actually want to change; generate light and dark palettes from a few anchors with a contrast check in the build; and keep one built-in theme that every override can fall back to.

## Checklist: a theme surface an agent can use safely

- **Few anchors in, full palette out.** Accept background, text, muted text and accent per mode; derive the rest in code.

- **Check before you paint.** Refuse or flag any generated pair below 4.5:1 for body text and 3:1 for large text and UI parts, in both modes.

- **Publish named hooks.** List the `data-slot` selectors you promise to keep, and add a test that fails when one disappears.

- **Never promise class names.** Utility and hashed classes change every release; say so in the guide.

- **Block remote loads in theme CSS.** Drop `@import`, `image-set()` and external `url()`; allow `data:` only, with a size cap.

- **Keep trust surfaces out of reach.** Permission prompts, payment and security UI are not themeable.

- **Ship a way back.** A built-in theme, a command and a keyboard shortcut that work even if the theme hides the settings.

- **Make the agent look.** Require a light and dark screenshot of the result before the theme is kept.

```
# Paste this to your coding agent
Restyle 
 to 
.
- Change only our theme contract: anchors in 

  (surface, text, muted, accent for light and dark) and the data-slot
  selectors listed in 
. Never target class names.
- After generating the palette, report every text/background pair below
  4.5:1 (3:1 for large text and controls) and fix it before continuing.
- Theme CSS: no @import, no image-set(), no url() except data: under 10 KB.
- Do not restyle permission, payment or security UI.
- Take light and dark screenshots of 
; show them and wait.
Report: anchors chosen, contrast results, selectors touched, and how to
revert to the built-in theme.
```

Related on UI Hub: 
design tokens for agents
, 
OKLCH colour and dark mode
, and 
linting agents onto your design system
.

## References
- [Draw in the interface with a mod (themes and backdrops)](https://code.claude.com/docs/en/plugins/mods/interface) — Claude Code Docs (Anthropic)
- [Mods overview](https://code.claude.com/docs/en/plugins/mods/overview) — Claude Code Docs (Anthropic)
- [Mods reference](https://code.claude.com/docs/en/plugins/mods/reference) — Claude Code Docs (Anthropic)
- [Claude Code Desktop Themes: Build One With Mods](https://vanja.io/claude-code-desktop-themes/) — vanja.io
- [feat: agents can restyle T3 Code with theme colors and CSS (#35247)](https://github.com/pingdotgg/t3code/pull/35247) — GitHub · pingdotgg/t3code
- [feat(themes): theme CSS can hold 50,000 characters (#36656)](https://github.com/pingdotgg/t3code/pull/36656) — GitHub · pingdotgg/t3code
- [Appearance (custom themes, custom CSS, ask an agent)](https://github.com/pingdotgg/t3code/blob/main/docs/user/appearance.md) — GitHub · pingdotgg/t3code docs
- [T3 Code lets your agent restyle the app with theme colors and CSS](https://creatorstoolbox.com/@scout/post/n_0lglos4it08wt) — Creators Toolbox
- [T3 Themes community gallery](https://t3themes.com/) — t3themes.com
- [Theme Color reference](https://code.visualstudio.com/api/references/theme-color) — Visual Studio Code docs
- [Design Tokens Format Module (draft)](https://www.designtokens.org/tr/drafts/format/) — W3C Design Tokens Community Group
- [Understanding SC 1.4.3: Contrast (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) — W3C WAI
- [Attribute selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Attribute_selectors) — MDN Web Docs