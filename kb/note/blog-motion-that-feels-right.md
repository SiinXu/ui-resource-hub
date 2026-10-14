# Motion that feels right: purpose, duration, easing, restraint

> Most UI motion should be under 300ms, ease-out, and skipped for frequent actions. Spectacle belongs on marketing pages, not in tools.

Blog post: https://siinxu.github.io/ui-resource-hub/blog/motion-that-feels-right/

Emil Kowalski's rule of thumb is blunt: if a user triggers something a hundred times a day, do not animate it. Motion is for orientation (where did this come from?), feedback (it worked) and, sparingly, delight.

## Numbers to start from

- Small UI changes: 150–250ms; larger surfaces 300–400ms. Material 3's motion tokens sit in the same ranges.
- Enter with **ease-out**, so the element responds immediately; avoid ease-in for UI.
- Animate `transform` and `opacity` only for smooth 60fps.
- Respect `prefers-reduced-motion`: swap movement for fades.

## Our take

Aceternity- and Magic UI-style effects (beams, spotlights, marquees) work as **one hero moment per page**. Stack three and the page looks like a template. Josh Comeau's transition guide is the best explanation of why easing curves matter.

## References
- [Great animations](https://emilkowal.ski/ui/great-animations) — Emil Kowalski
- [animations.dev](https://animations.dev) — Emil Kowalski
- [Motion overview — Material 3](https://m3.material.io/styles/motion/overview) — Google
- [An Interactive Guide to CSS Transitions](https://www.joshwcomeau.com/animation/css-transitions/) — Josh W. Comeau
- [prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion) — MDN
- [Motion docs](https://motion.dev/docs) — Motion