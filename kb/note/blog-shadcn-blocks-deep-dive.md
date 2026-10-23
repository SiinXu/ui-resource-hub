# shadcn blocks and registries: page sections as source code

> Blocks (dashboards, sidebars, login pages) install with one CLI command, and any team can publish its own registry. Why this is the best substrate for AI agents.

Blog post: <https://ui.incidental.site/blog/shadcn-blocks-deep-dive/>

shadcn/ui is not a package you install; it is a set of components whose source you copy into your project. Blocks extend the idea to whole sections: dashboards, sidebars, login and signup pages, charts. Each is added with the CLI, for example `npx shadcn@latest add dashboard-01`, and lands as editable files.

## Registries: everyone can publish

The shadcn registry format lets any team publish components, blocks, hooks and theme files as JSON that the CLI understands. Magic UI, Cult UI and many others distribute this way, and you can run a private registry for your own design system.

```
npx shadcn@latest add https://your-registry.example/r/pricing-01.json
```

## Why agents love this model

- The code is local, so an agent can read and edit it like any file.

- Names are stable and documented, so prompts can reference them ("add sidebar-07").

- Theme lives in CSS variables, so one token change restyles everything the agent generated.

## Our take

If you want AI-generated UI to stay consistent, give the agent a registry, not a style adjective. Start from official blocks, restyle via tokens, and publish your modified versions to a private registry so every future session builds from your system.

## References
- [Blocks](https://ui.shadcn.com/blocks) — shadcn/ui
- [Registry](https://ui.shadcn.com/docs/registry) — shadcn/ui
- [CLI](https://ui.shadcn.com/docs/cli) — shadcn/ui
- [Theming](https://ui.shadcn.com/docs/theming) — shadcn/ui