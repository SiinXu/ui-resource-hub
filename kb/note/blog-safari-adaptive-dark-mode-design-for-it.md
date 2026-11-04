# Safari will darken light-only sites for you: design your own dark mode before Adaptive Dark Mode does

> On 3 November WebKit announced Adaptive Dark Mode in the Safari 27.3 beta: when a reader turns it on, Safari recolours light websites as dark, and your site cannot tell. What it changes, what it skips, the opt-out trap in beta 1, and a checklist for choosing between a real dark theme, letting Safari adapt, or keeping parts light.

Blog post: <https://ui.incidental.site/blog/safari-adaptive-dark-mode-design-for-it/>

On 3 November the WebKit team announced **Adaptive Dark Mode** in the Safari 27.3 beta. If a reader has their system set to dark and lands on a bright page, Safari offers a preview and a “Try” button; MacRumors reports that after the first try it can be switched on for every site or site by site. Once it is on, Safari recolours light pages as dark. WebKit’s reason is a gap it measures itself: almost 40% of page loads come from people in dark mode, but only about 10% of page loads support it. Apple’s point releases that carry the feature are expected in December, according to MacRumors.

For designers the important line is not the feature but the condition. If your site does not declare dark mode support, a browser engine will now make a dark version of it for some of your readers, using its own rules, and you will not be able to see that it happened.

## What Safari changes, and what it leaves alone

- **It skips sites that already declare dark support** with the `color-scheme` meta tag or `color-scheme: light dark` in CSS, and pages that are already mostly dark with light text.

- **On light pages it inverts lightness but keeps hue.** Backgrounds go dark, dark text goes light, and transformed text aims for the WCAG 4.5:1 contrast ratio. Light CSS gradients become dark too.

- **It tries to keep things usable:** buttons keep contrast against their backgrounds, text stays readable over images, hover menus stay clear. MacRumors adds that it lifts raised surfaces and rebalances layered shadows.

- **Images are mostly untouched.** SVGs are inspected and recoloured when needed; for bitmaps Safari reads the pixel histogram and inverts simple black-and-white logos.

- **Some effects get switched off.** Masks and `mix-blend-mode` may be disabled on transformed elements, and `<canvas>` content is left as it is.

- **Your site cannot detect it.** To avoid adding a fingerprinting signal, JavaScript that reads CSS colours gets the authored colours, not the ones on screen.

## The opt-out trap in beta 1

WebKit’s documented way to keep a page or one element light is `color-scheme: light only` (or the meta tag with `light only`). In Safari 27.3 beta 1, the `only` keyword is not supported yet. That leaves a tempting shortcut: declare `light dark` so Safari leaves you alone. Don’t do it without real dark styles. That declaration tells every browser you handle dark mode, so built-in parts such as form controls, scrollbars and the default page background follow the reader’s dark preference, while your hard-coded light colours stay light. You trade Safari’s attempt at a dark page for a mixed one that you made yourself.

## Our take

An automatic dark theme is a floor, not a design. It is probably better than a glaring white page at midnight, and WebKit clearly worked hard on contrast. But it makes decisions a designer would want to make: how light your brand colour becomes when its lightness flips, which surfaces sit above others, whether a photo with a baked-in white box looks pasted on. And because the change is invisible to scripts, you will not see it in analytics or in screenshots your monitoring takes; you will only see it if you open the page in Safari yourself.

The good news is that a real dark theme is cheaper than it used to be. `light-dark()` lets one token hold both values, `color-mix()` derives hover and border shades, and a coding agent can do most of the mechanical work of moving scattered hex values into tokens. The design work that remains is the part worth doing by hand: choosing the dark palette, checking contrast and deciding what must stay light.

## Checklist: decide before Safari decides for you

- **Look at it first.** In the Safari 27.3 beta, set the system to dark, open your key pages and tap Try. Screenshot the home page, a form, a table and anything with your logo.

- **Pick a path per site.** A real dark theme for products people use for long sessions; letting Safari adapt for simple content sites; light only for areas where colour is the content.

- **If you go dark, use tokens.** Put every colour in a token, write both values with `light-dark()`, and declare `color-scheme: light dark` in the HTML head, not later from JavaScript.

- **Check contrast in both themes.** Body text 4.5:1, large text and icons 3:1, including focus rings, disabled states and placeholder text.

- **Fix the inputs Safari struggles with.** Logos and icons as SVG, images with transparent backgrounds rather than a baked page colour, CSS colours instead of tiled background images or sprites.

- **Mark what must stay light.** Product photos, charts with semantic colours, brand artwork: plan `color-scheme: light only` on those elements and re-test when a later beta supports `only`.

- **Remember canvas and blend modes.** Shaders, charts drawn to canvas and `mix-blend-mode` effects will not be adapted, or may be switched off, so they need their own dark versions.

- **Don’t fake support.** Never ship `light dark` as an opt-out without dark styles behind it.

```
/* in <head>: <meta name="color-scheme" content="light dark"> */
:root {
  color-scheme: light dark;
  --bg:      light-dark(#f7f7f5, #0e0f13);
  --surface: light-dark(#ffffff, #171922);
  --ink:     light-dark(#111318, #eceef4);
  --muted:   light-dark(#4b5162, #a4abbd);
  --accent:  light-dark(#2453d6, #8aa8ff);
  --line:    color-mix(in oklch, var(--ink) 14%, transparent);
}
body { background: var(--bg); color: var(--ink); }
/* areas that must stay light (once Safari supports "only") */
.product-photos, .brand-art { color-scheme: light only; }
```

## How UI Hub helps

For the basics of a hand-made dark theme, start with 
dark mode done right
; for building the palette itself, read 
OKLCH colour and dark mode
, and keep the tokens where agents can read them with 
design tokens for agents
. Run the contrast and focus checks in 
accessibility in AI-generated UI
 on both themes. If your hero uses a canvas or shader, 
shipping shader backgrounds
 covers the fallbacks you will need, since Safari leaves canvas content alone.

## References
- [Introducing Adaptive Dark Mode](https://webkit.org/blog/18541/introducing-adaptive-dark-mode/) — Simon Fraser, Luming Yin, Lily Spiniolas, Joanne Pan, Veda Periwal and Jen Simmons, WebKit
- [iOS 27.3 Adds Vertical Tabs and Adaptive Dark Mode to Safari](https://www.macrumors.com/2026/11/03/ios-27-3-safari/) — Juli Clover, MacRumors
- [Safari’s new dark mode repaints light websites without the sites knowing](https://ppc.land/safaris-new-dark-mode-repaints-light-websites-without-the-sites-knowing/) — PPC Land
- [Safari 27.3 Beta Adds Adaptive Dark Mode for Light Websites](https://www.technobezz.com/news/safari-beta-adds-adaptive-dark-mode) — Technobezz
- [Safari introduces Adaptive Dark Mode in 27.3 (discussion)](https://news.ycombinator.com/item?id=50358562) — Hacker News
- [color-scheme](https://developer.mozilla.org/en-US/docs/Web/CSS/color-scheme) — MDN Web Docs
- [light-dark()](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/light-dark) — MDN Web Docs
- [prefers-color-scheme](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) — MDN Web Docs
- [color-mix()](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/color-mix) — MDN Web Docs
- [contrast-color()](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/contrast-color) — MDN Web Docs
- [Improved dark mode default styling with the color-scheme CSS property and the corresponding meta tag](https://web.dev/articles/color-scheme) — web.dev
- [CSS Color Adjustment Module Level 1](https://drafts.csswg.org/css-color-adjust-1/) — W3C CSS Working Group (editor’s draft)
- [Understanding SC 1.4.3: Contrast (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) — W3C Web Accessibility Initiative