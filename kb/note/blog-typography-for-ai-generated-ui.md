# Typography for AI-generated UI: the fastest way to look less generic

> Generators default to one sans at three sizes. A type scale, a second typeface, tighter tracking on display sizes and real line lengths fix most of it.

Blog post: <https://ui.incidental.site/blog/typography-for-ai-generated-ui/>

Ask any generator for a landing page and you will usually get one sans-serif at body, heading and caption sizes. Typography is the cheapest lever to move a page away from that default, and it is easy to specify precisely in a prompt.

## Five rules to put in the brief

- **Use a modular scale.** Pick a ratio (1.2 for dense apps, 1.25–1.333 for marketing) and name the steps as tokens.

- **Pair two typefaces with a job each.** A display face for headlines (a serif such as Instrument Serif, or a tight grotesk) and a workhorse sans for UI.

- **Tighten large text.** Negative letter-spacing (around −0.02em) on display sizes; leave body text at default.

- **Constrain line length.** Roughly 45–75 characters for Latin body text; use `max-width: 65ch`.

- **Fluid sizes.** `clamp()` for headlines so mobile does not inherit desktop sizes.

## CJK needs its own settings

For Chinese and Japanese, use a slightly larger line-height (about 1.7), avoid negative tracking, and use `word-break: keep-all` or `text-wrap: balance` on headings so short phrases are not orphaned, the fix we applied to our own Japanese headings.

## Our take

If you only change one thing in AI output, change the type scale and the display face. It is a two-line token edit with a visible payoff.

## References
- [Practical Typography: line length](https://practicaltypography.com/line-length.html) — Matthew Butterick
- [text-wrap](https://developer.mozilla.org/en-US/docs/Web/CSS/text-wrap) — MDN
- [clamp()](https://developer.mozilla.org/en-US/docs/Web/CSS/clamp) — MDN
- [Utopia fluid type scale](https://utopia.fyi/type/calculator/) — Utopia
- [Requirements for Chinese Text Layout](https://www.w3.org/TR/clreq/) — W3C