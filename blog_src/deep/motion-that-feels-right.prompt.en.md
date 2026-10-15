Review and fix the motion in <component or page>.
For every animation or transition you find:
1. Name its job: orientation, feedback or delight. If it has none, or the action happens many times a day (tabs, sidebar toggle, command palette), remove it or make it near-instant (<100ms).
2. Durations: 150–250ms for small UI, 300–400ms for large surfaces; exits ~30% faster than entries.
3. Easing: ease-out (e.g. cubic-bezier(0.16,1,0.3,1)) for entering/responding; never ease-in for responses.
4. Animate only transform and opacity. Replace width/height/top/box-shadow animations.
5. Add a prefers-reduced-motion block that keeps opacity and removes movement.
6. Keep at most one decorative "hero" effect on the page; make the rest static.
Output: a table (element · job · before · after) and then the code diff. Do not add new animations.
