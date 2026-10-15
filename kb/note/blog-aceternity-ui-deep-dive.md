# Aceternity UI deep dive: spectacle, used sparingly

> Copy-paste React + Tailwind + Motion effects that made the "fancy" landing look popular. Which pieces carry a page and which turn it into a demo reel.

Blog post: <https://siinxu.github.io/ui-resource-hub/blog/aceternity-ui-deep-dive/>

Aceternity UI, created by Manu Arora, is a collection of copy-paste components built with React, Tailwind CSS and Motion (formerly Framer Motion). It is known for showpiece effects: spotlight and beam backgrounds, 3D cards, animated grids, parallax hero scrolls. Free components are open to copy; there is also a paid tier of templates and blocks.

## What works on real pages

- **One ambient background** behind the hero (grid, dots, a soft spotlight). It adds depth without competing with copy.

- **Bento grids and feature sections** with restrained hover motion.

- **Text reveal or typewriter** for a single headline, not for paragraphs.

## What to avoid

Stacking three effects in one viewport, animating body text, and 3D tilt on cards that hold data. These read as a demo reel and cost performance on low-end phones. Always respect `prefers-reduced-motion`, which several effects do not handle by default, so wrap them yourself.

## How we use it in UI Hub

Aceternity is one of the references behind the user's "restrained fancy" house style: borrow one signature effect per page, keep typography and spacing doing the heavy lifting. Search "aceternity" in the hub to see every Aceternity component we index with a live preview.

## References
- [Aceternity UI](https://ui.aceternity.com/) — Manu Arora
- [Aceternity UI components](https://ui.aceternity.com/components) — Aceternity
- [Motion for React](https://motion.dev/) — Motion
- [prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion) — MDN