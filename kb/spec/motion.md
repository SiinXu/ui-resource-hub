# Motion

> Purposeful, fast (150–300 ms), ease-out on enter, transform/opacity only, honour reduced motion.

## Rules
- **Purpose:** orientation, feedback, continuity. Not decoration on frequent actions.
- **Durations:** micro 120–200 ms, panels 250–350 ms, page transitions ≤ 400 ms.
- **Easing:** ease-out (or spring with no overshoot) for enter; ease-in only for exits.
- **Performance:** animate `transform` and `opacity`; avoid animating layout properties.
- **Reduced motion:** `@media (prefers-reduced-motion: reduce)` swaps movement for fades or nothing.
- **One hero effect per page** (beam, spotlight, marquee). Stacking effects looks like a template.

## Sources
- [Emil Kowalski — Great Animations](https://emilkowal.ski/ui/great-animations)
- [Material 3 motion](https://m3.material.io/styles/motion/overview)
- [MDN prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion)