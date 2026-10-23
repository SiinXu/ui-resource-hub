# Magic UI deep dive: animated components that install like shadcn

> An open-source (MIT) set of motion components distributed through the shadcn registry. Best picks for SaaS pages and how to keep them accessible.

Blog post: <https://ui.incidental.site/blog/magic-ui-deep-dive/>

Magic UI is an open-source library of animated components (MIT licence) designed as a companion to shadcn/ui. Components are added with the shadcn CLI from Magic UI's registry, so the source lands in your repo where you can edit it, rather than living in a dependency.

## Picks that earn their place

- **Marquee** for logo walls and testimonials: motion that carries information.

- **Number ticker** for a single headline metric.

- **Animated beam / orbiting circles** to show integrations, one per page.

- **Shimmer or border-beam buttons** for exactly one primary CTA.

## Accessibility and performance

Continuous motion (marquees, orbits) should pause on hover and stop under `prefers-reduced-motion`; WCAG 2.2.2 asks for a way to pause anything that moves for more than five seconds. Prefer transform and opacity animations, which browsers can composite cheaply.

## Our take

Magic UI is the easiest way to add motion to a shadcn project because it shares the install model and the token variables. The risk is the same as any effects library: use one or two components per page, and let the rest of the UI stay calm.

## References
- [Magic UI](https://magicui.design/) — Magic UI
- [magicuidesign/magicui (MIT)](https://github.com/magicuidesign/magicui) — GitHub
- [Understanding SC 2.2.2: Pause, Stop, Hide](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html) — W3C
- [shadcn registry docs](https://ui.shadcn.com/docs/registry) — shadcn