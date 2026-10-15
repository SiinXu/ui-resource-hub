# Motion that feels right: purpose, duration, easing, restraint

> Most UI motion should be under 300ms, ease-out, and skipped for frequent actions. Spectacle belongs on marketing pages, not in tools.

Blog post: <https://siinxu.github.io/ui-resource-hub/blog/motion-that-feels-right/>

Emil Kowalski's rule of thumb is blunt: if a user triggers something a hundred times a day, do not animate it. Motion in an interface has three legitimate jobs: **orientation** (where did this come from and where did it go?), **feedback** (your action worked) and, sparingly, **delight**. Everything else is decoration that costs time on every interaction. This post gives starting numbers, a step-by-step way to add motion to a component, code you can paste, and the mistakes that make AI-generated pages feel cheap.

## Decide the job before the animation

Before writing a transition, write one sentence: "This animates so the user understands ___." If you cannot fill the blank, leave it static. Some examples:

- A dropdown scales from its trigger so the user sees which button opened it (orientation).

- A "Copied" check replaces the copy icon for 1.5 seconds (feedback).

- A hero illustration drifts slowly on first load of a marketing page (delight, once).

A command palette that opens 50 times a day should appear almost instantly. Keep frequent surfaces fast and spend motion on rare moments.

## Numbers to start from

- **Duration:** 150–250ms for small UI changes (tooltips, dropdowns, toggles); 300–400ms for larger surfaces (drawers, modals, page sections). Material 3's motion tokens sit in the same ranges.

- **Easing:** enter and respond with **ease-out**, so the element moves immediately and settles. Avoid ease-in for UI responses; it feels like lag. Use ease-in-out for elements moving from one on-screen position to another.

- **Distance:** small. A dropdown needs 4–8px of travel or a scale from 0.96, not a slide from off-screen.

- **Properties:** animate `transform` and `opacity`. Animating `width`, `height`, `top` or `box-shadow` triggers layout or paint on every frame and stutters on mid-range phones.

## Step by step: a dropdown that feels right

**Step 1: set the origin.** Scale from the trigger, not from the centre. Radix and similar libraries expose the transform origin as a CSS variable you can use.

**Step 2: write enter and exit separately.** Exits should be faster than entries; the user has already decided to move on.

.menu {
  transform-origin: var(--radix-dropdown-menu-content-transform-origin, top left);
}
.menu[data-state=&quot;open&quot;] {
  animation: menu-in 180ms cubic-bezier(0.16, 1, 0.3, 1);
}
.menu[data-state=&quot;closed&quot;] {
  animation: menu-out 120ms ease-in;
}
@keyframes menu-in {
  from { opacity: 0; transform: scale(0.96) translateY(-4px); }
  to   { opacity: 1; transform: none; }
}
@keyframes menu-out {
  to { opacity: 0; transform: scale(0.98); }
}

**Step 3: respect reduced motion.** Some users get motion sickness from movement. Keep the opacity change, drop the movement:

@media (prefers-reduced-motion: reduce) {
  .menu[data-state=&quot;open&quot;],
  .menu[data-state=&quot;closed&quot;] {
    animation-name: fade;
  }
  @keyframes fade { from { opacity: 0; } to { opacity: 1; } }
}

**Step 4: test at speed.** Open and close it ten times quickly. If the animation ever blocks the next click, it is too long or not interruptible.

## Springs and layout animation

For elements that move between positions (a reordered list item, an expanding card, a tab indicator), springs feel more natural than fixed curves because they respond to interruption. Motion (formerly Framer Motion) makes layout animation one prop:

import { motion } from &quot;motion/react&quot;;

<motion.div
  layout
  transition={{ type: &quot;spring&quot;, stiffness: 500, damping: 40 }}
  className=&quot;tab-indicator&quot;
/>

Keep springs stiff and well damped for UI. A bouncy spring is fun once and annoying the twentieth time.

## One hero moment per page

Aceternity- and Magic UI-style effects (beams, spotlights, meteor showers, marquees) are designed to impress. They work as **one hero moment per page**. Put a spotlight on the hero and a marquee on the logo strip and an animated gradient border on every card, and the page reads as a template. When an AI generator gives you three effects, keep the one closest to your story and make the rest static.

## A quick motion audit

To review an existing page, list every animation in a table with four columns: element, trigger, duration and job. Anything without a job is deleted. Anything triggered often gets shortened to near-instant. Anything over 400ms needs a reason. Then record the screen at normal speed and watch it back at half speed: you will see easing problems, overlapping animations and elements that move in different directions at once, which are hard to notice live.

## Pitfalls

- **Animating frequent actions.** Toggling a sidebar, switching tabs or opening a command palette should feel instant.

- **Ease-in on responses.** The element seems to hesitate before reacting.

- **Long exits.** Users wait for a closing modal before they can click what is behind it.

- **Layout properties.** Height animations on accordions jank; animate a wrapper's transform or use the grid-rows `0fr` to `1fr` technique.

- **Ignoring reduced motion.** It is a single media query and it matters to real people.

- **Scroll-jacking.** Scroll-linked effects that change scroll speed break trackpads and screen readers.

## Questions we get

**CSS transitions or a JavaScript library?** Use CSS for simple state changes (hover, open/close, fades): it is cheap and runs off the main thread for transform and opacity. Reach for a library like Motion when you need layout animation, shared-element transitions, gestures or interruptible springs.

**How do I find janky animations?** Open the browser's performance panel, record while triggering the animation, and look for long frames and layout or paint work on every frame. On a real mid-range phone, jank you cannot see on a laptop becomes obvious.

**What about loading states?** Skeletons with a subtle shimmer are fine, but the shimmer should be slow and low-contrast. Better still, show content as soon as it arrives instead of fading everything in together.

**Should marketing pages follow the same rules?** Mostly. Marketing pages can afford one bigger moment because they are visited rarely, but the same limits on duration, easing and reduced motion still apply to buttons, menus and navigation on those pages.

**How do I brief an AI generator about motion?** Give it the numbers: durations, the easing curve, "transform and opacity only", "one hero effect", and a reduced-motion requirement. Without numbers, generators default to slow, floaty transitions on everything.

## Our take

Good motion is mostly invisible: users notice that the interface feels responsive, not that it animates. Start every component static, add motion only where you can name its job, keep it short and ease-out, and spend your one big effect where the story needs it. Josh Comeau's interactive guide to CSS transitions is the best explanation of why easing curves matter; read it once and you will see bad easing everywhere.

## Checklist

- Each animation has a named job: orientation, feedback or delight

- Small UI 150–250ms, large surfaces 300–400ms; exits faster than entries

- Ease-out for entering and responding

- Only transform and opacity animated

- prefers-reduced-motion handled

- At most one hero effect per page

## References
- [Great animations](https://emilkowal.ski/ui/great-animations) — Emil Kowalski
- [animations.dev](https://animations.dev) — Emil Kowalski
- [Motion overview — Material 3](https://m3.material.io/styles/motion/overview) — Google
- [An Interactive Guide to CSS Transitions](https://www.joshwcomeau.com/animation/css-transitions/) — Josh W. Comeau
- [prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion) — MDN
- [Motion docs](https://motion.dev/docs) — Motion
- [Animations guide](https://web.dev/articles/animations-guide) — web.dev
- [Layout animations](https://motion.dev/docs/react-layout-animations) — Motion