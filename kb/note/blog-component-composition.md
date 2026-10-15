# Component composition: why headless + copy-paste won

> Radix behaviour, your styles, code you own. Compound components keep APIs small and make AI edits safer.

Blog post: <https://siinxu.github.io/ui-resource-hub/blog/component-composition/>

The old model was a styled npm package you fought with overrides. shadcn/ui flipped it: behaviour and accessibility from Radix primitives, styling in Tailwind, and the source copied into your repo.

## Why it suits AI

- Code in your repo is **visible context**, so the agent can read and edit it.
- **Compound components** (`<Dialog.Trigger>`, `<Dialog.Content>`) have small, predictable surfaces, which makes edits less error-prone than a 40-prop monolith.
- Registries let tools install the same component into any project.

## Our take

Compose from three layers: primitives (Radix, Ark, React Aria), your styled kit, and page blocks. Let AI work mainly at the block layer and keep primitives untouched. Atomic design's old atoms→organisms idea maps neatly onto this.

## References
- [shadcn/ui docs](https://ui.shadcn.com/docs) — shadcn
- [Radix Primitives introduction](https://www.radix-ui.com/primitives/docs/overview/introduction) — WorkOS / Radix
- [Compound Pattern](https://www.patterns.dev/react/compound-pattern/) — patterns.dev (Lydia Hallie & Addy Osmani)
- [Atomic Design, chapter 2](https://atomicdesign.bradfrost.com/chapter-2/) — Brad Frost