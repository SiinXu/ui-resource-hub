Add a proper dark theme to <project>, or audit the existing one.
1. Find every raw colour in components (hex, rgb, Tailwind colour classes) and list them. Propose a role table: --bg, --surface, --raised, --ink, --muted, --line, --accent (+ danger/success if used).
2. Replace raw colours with role variables. Define values for [data-theme="light"] and [data-theme="dark"]; set color-scheme in each.
3. Dark values: off-black background (not #000), off-white text (not #fff), raised surfaces lighter than the background, a lighter/less saturated accent.
4. Check WCAG contrast (4.5:1 text, 3:1 large text/UI) for ink, muted, placeholder, links and buttons in BOTH themes; report a table with the ratios and fix failures.
5. Add an inline <head> script that sets data-theme before first paint (saved choice, else prefers-color-scheme), and a toggle that saves the choice and updates aria-pressed.
6. List third-party embeds, images and code blocks that need dark variants.
Do not use filter: invert.
