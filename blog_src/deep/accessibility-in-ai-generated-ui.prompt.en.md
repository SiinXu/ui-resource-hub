Audit <page or component> for accessibility and fix what you find. Work through this list in order and report each item as PASS / FIXED / NEEDS HUMAN:
1. Actions use <button>, navigation uses <a href>; no clickable div/span.
2. Every interactive element has a visible :focus-visible style; no bare outline:none.
3. Icon-only controls have an accessible name (aria-label or visually hidden text).
4. Text contrast ≥ 4.5:1 (3:1 for large text and UI parts) in light AND dark themes; list the ratios.
5. Touch targets ≥ 24×24 CSS px or adequately spaced.
6. Dialogs/menus: focus moves in on open, Tab stays inside, Escape closes, focus returns to the trigger.
7. Every input has a programmatic label; errors linked with aria-describedby; no placeholder-as-label.
8. Status messages (saved, results count, errors) use role="status" or aria-live.
9. Headings form a logical outline; images have meaningful alt or alt="".
Then add an @axe-core/playwright test for this page (tags wcag2a, wcag2aa, wcag22aa).
Prefer native elements over ARIA. Do not change the visual design beyond what a fix requires.
