I want to add one Cult UI component (<component name>) to this shadcn-based project as our single signature interaction.
1. Read the component's source (I will paste it or give you the file). Summarise its props, its dependencies (e.g. motion) and every hard-coded colour, radius, shadow and spring value.
2. Place it in the kit folder next to the other components; make sure there is only one copy in the repo.
3. Replace hard-coded styling with our tokens (<tokens file>) and replace its spring values with our presets in motion.ts (create snappy/soft presets if none exist).
4. Add accessibility the demo lacks: real <button> or correct role, visible focus, keyboard support, aria-expanded/aria-controls, and a live region if content changes without focus moving.
5. Add a reduced-motion fallback with useReducedMotion.
6. Give a tap/always-visible alternative for anything that only appears on hover.
Output: the summary, then the diff, then a list of anything that still differs from our design system. Remind me to check the repository licence.
