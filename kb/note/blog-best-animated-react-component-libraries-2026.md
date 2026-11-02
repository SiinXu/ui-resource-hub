# Best animated React component libraries 2026: Motion, Magic UI, React Bits and more

> Ten animated React libraries compared with numbers read from GitHub, npm and their own sites on 1 November 2026: engines you write motion with, copy-paste collections, and the licence catch to check before shipping.

Blog post: <https://ui.incidental.site/blog/best-animated-react-component-libraries-2026/>

This is a shortlist of animated React component libraries worth knowing in 2026, with the numbers read straight from GitHub, npm and each project’s own site on 1 November 2026. “Animated React component library” covers two different things: **animation engines** you write motion with, and **copy-paste collections** of ready-made animated components. They solve different problems, so they are listed separately. Stars and downloads move every day; treat them as a snapshot, not a ranking.

## The short answer

- **Need to animate your own components:** Motion (formerly Framer Motion). It is the most downloaded animation engine here and is MIT licensed.

- **Need physics-based springs:** React Spring.

- **Need list add/remove animation with almost no code:** AutoAnimate.

- **Need a landing page with animated sections today:** Magic UI or Aceternity UI. Both are built on React, Tailwind CSS and Motion.

- **Need the largest pool of animated pieces:** React Bits, but read its licence first (below).

- **Need animated components that sit on top of shadcn/ui:** Cult UI, Kokonut UI, Motion Primitives or Animate UI.

## Animation engines: you write the motion

- **Motion** — “An open source animation library for JavaScript, React and Vue.” MIT. 34,779 GitHub stars, last push 1 November 2026. Install with `npm install motion` and import from `motion/react`; its README states that Framer Motion is now Motion. The `motion` package was at version 14.9.0 and had about 33.9 million npm downloads in the week of 23–29 October 2026 (the older `framer-motion` package: about 66.9 million). Its README lists gestures, springs, layout transitions, scroll-linked effects and timelines. A separate paid tier, Motion+, exists; UI Hub lists it as paid, one-time purchase.

- **React Spring** — “A spring physics based React animation library.” MIT. 29,261 stars. `@react-spring/web` was at 10.1.2 with about 7.2 million weekly downloads, and supports React 16.8 through 19.

- **AutoAnimate** (FormKit) — “A zero-config, drop-in animation utility” for React, Vue or plain JavaScript. MIT. 13,954 stars; last push 10 July 2026. `@formkit/auto-animate` was at 0.10.0 with about 2.4 million weekly downloads. It animates elements entering, leaving and moving inside a parent, which is why it needs so little code.

## Copy-paste collections: you own the source

- **Magic UI** — its homepage says “150+ free and open-source animated components and effects built with React, TypeScript, Tailwind CSS, and Motion”, as a companion to shadcn/ui. MIT. 23,026 stars.

- **Aceternity UI** — its homepage lists 118+ free components, and separately 183+ blocks, 17 templates and 4 landing pages; blocks are described as included with its paid All-Access Pass. Built with React, Tailwind CSS and Motion. We did not find a public repository for it to read star counts from.

- **React Bits** — described by its repository as “the largest open-source library of animated, interactive, and customizable React & Next.js components”. 50,984 stars, the highest in this list. You choose JavaScript or TypeScript and plain CSS or Tailwind, then copy the source or install through its CLI. Licence: MIT + Commons Clause (see below).

- **Cult UI** — “150+ free shadcn/ui components, built with Tailwind CSS and Motion. MIT licensed.” 6,899 stars; last push 29 October 2026.

- **Kokonut UI** — an open-source collection of components built with Tailwind CSS, shadcn/ui and Motion. MIT. 2,259 stars.

- **Motion Primitives** — a UI kit of animated interface pieces. MIT. 6,879 stars; last push 28 September 2026.

- **Animate UI** — “fully animated, open-source component distribution built with React, TypeScript, Tailwind CSS, Motion, and Shadcn CLI”. 4,819 stars. Licence: MIT + Commons Clause. Its homepage also advertises an agent skill, installed with `npx skills add imskyleen/animate-ui`.

## Small libraries that animate one thing well

- **Sonner** (toasts) and **Vaul** (mobile-style drawer), both by Emil Kowalski, had about 54.5 million and 31.2 million weekly npm downloads respectively in the same week.

- **Lenis** (smooth scroll) had about 2.4 million weekly downloads, and **GSAP** about 8.3 million. GSAP is not React-only, and UI Hub notes it is free to use under its own licence rather than MIT.

## Read the licence before you ship

Two libraries above use “MIT + Commons Clause”. The React Bits licence says you may use the software, including commercially, as long as you do not sell, sublicense or redistribute the components themselves, whether alone, in a bundle or as a ported version. That is fine for a product or website you build; it rules out publishing the components as your own template pack. The Animate UI licence has the same Commons Clause name, so read its LICENSE file for the exact terms before reusing it. Motion, React Spring, AutoAnimate, Magic UI, Cult UI, Kokonut UI and Motion Primitives show plain MIT on GitHub. Aceternity UI’s free components and paid blocks follow the terms on its own site, and we did not check the licences of the small libraries.

## How to choose

- **Start from the job, not the star count.** Animating state changes in your own components calls for an engine (Motion, React Spring, AutoAnimate). A marketing page calls for a copy-paste collection.

- **Pick one engine.** Most collections here are built on Motion, so using Motion for your own code means one dependency instead of two.

- **Copy only what you use.** Collections install as source files you own, so remove unused components and check each one’s dependencies.

- **One hero effect per page.** Stacked animated backgrounds hurt readability and performance more than they help.

- **Respect reduced motion.** Test with the operating system’s reduce-motion setting on, in light and dark themes, at 375 px width and by keyboard.

```
# Free React libraries with the "motion" visual style in UI Hub
curl -s https://ui.incidental.site/api/resources.json \
 | jq '.items[] | select(.type=="library" and .pricing=="free"
   and (.tags|index("React")) and ((.vs//[])|index("motion"))) | {name,url}'
```

## What UI Hub adds

UI Hub lists 235 component libraries; on 1 November 2026, 11 of them were tagged React with the motion visual style, and 9 of those were marked free. The filter above reproduces that list from the public API. For deeper reading, see our notes on 
motion that feels right
 (durations, easing and reduced motion), and the deep dives on 
Magic UI
, 
Aceternity UI
 and 
Cult UI
.

## References
- [motiondivision/motion (README, licence, stars)](https://github.com/motiondivision/motion) — GitHub
- [Motion for React](https://motion.dev/docs/react) — Motion
- [pmndrs/react-spring](https://github.com/pmndrs/react-spring) — GitHub
- [formkit/auto-animate](https://github.com/formkit/auto-animate) — GitHub
- [Magic UI](https://magicui.design/) — Magic UI
- [magicuidesign/magicui](https://github.com/magicuidesign/magicui) — GitHub
- [Aceternity UI](https://ui.aceternity.com/) — Aceternity
- [React Bits](https://reactbits.dev/) — React Bits
- [DavidHDev/react-bits (LICENSE: MIT + Commons Clause)](https://github.com/DavidHDev/react-bits/blob/main/LICENSE.md) — GitHub
- [nolly-studio/cult-ui](https://github.com/nolly-studio/cult-ui) — GitHub
- [kokonut-labs/kokonutui](https://github.com/kokonut-labs/kokonutui) — GitHub
- [ibelick/motion-primitives](https://github.com/ibelick/motion-primitives) — GitHub
- [Animate UI](https://animate-ui.com/) — Animate UI
- [imskyleen/animate-ui](https://github.com/imskyleen/animate-ui) — GitHub
- [npm weekly downloads API (23–29 October 2026)](https://api.npmjs.org/downloads/point/last-week/motion) — npm
- [UI Hub resources API](https://ui.incidental.site/api/resources.json) — UI Hub