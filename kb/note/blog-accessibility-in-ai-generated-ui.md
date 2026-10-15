# Accessibility in AI-generated UI: the checks models skip

> Generated UIs look fine and fail keyboards and screen readers. Start from accessible primitives, then audit against WCAG 2.2.

Blog post: <https://siinxu.github.io/ui-resource-hub/blog/accessibility-in-ai-generated-ui/>

Models optimise for what a screenshot shows. Focus order, accessible names, keyboard behaviour and live regions do not show up in screenshots, so they are the first things to go missing from generated UI. The good news is that the failures are predictable. This post lists the checks models skip most often, gives the fix for each, and shows how to make accessibility part of the agent's definition of done instead of a final pass nobody has time for.

## Why generated UI fails in the same places

A generator learns from millions of pages, and a large share of the web has accessibility problems. Automated audits of popular home pages keep finding the same short list: low-contrast text, missing alternative text, empty links and buttons, missing form labels. Those are exactly the patterns a model reproduces when nobody asks for anything else. The fix is not a smarter model; it is explicit constraints plus a check the agent runs itself.

## The checks models skip most

**1. Clickable divs.** `<div onClick>` looks like a button and is not one: no focus, no Enter or Space, no role. Use `<button>` for actions and `<a href>` for navigation.

<!-- generated -->
<div class=&quot;btn&quot; onclick=&quot;save()&quot;>Save</div>

<!-- fixed -->
<button type=&quot;button&quot; class=&quot;btn&quot; onclick=&quot;save()&quot;>Save</button>

**2. Missing focus styles.** Generators often add `outline: none` to remove the browser ring because it "looks messy" in screenshots. Replace it, don't remove it:

:focus { outline: none; }
:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }

`:focus-visible` shows the ring for keyboard users and hides it for most mouse clicks, which is what designers usually wanted in the first place.

**3. Icon-only buttons with no name.** A trash icon is obvious to sighted users and silent to a screen reader. Add `aria-label="Delete project"` or visually hidden text.

**4. Contrast of secondary text.** Grey-on-grey captions, placeholders and disabled labels are the most common WCAG failure (success criterion 1.4.3 asks for 4.5:1 for normal text). Check both themes.

**5. Target size.** WCAG 2.2 adds 2.5.8 Target Size (Minimum): interactive targets should be at least 24×24 CSS pixels, or have enough spacing. Tiny close buttons and dense icon toolbars fail it on phones.

**6. Dialogs without focus management.** A modal must move focus inside when it opens, keep Tab inside while open, close on Escape and return focus to the trigger. The ARIA Authoring Practices Guide documents the pattern; Radix, React Aria and the native `<dialog>` element implement it.

**7. Forms without labels.** Placeholder text is not a label; it disappears when you type. Every input needs a `<label for>` or `aria-labelledby`, and errors should be linked with `aria-describedby`.

**8. Dynamic updates nobody announces.** "Saved", "3 results" and validation errors that appear without a page change need a live region (`role="status"` or `aria-live="polite"`) to be heard.

## Step by step: build accessibility into the workflow

**Step 1: generate on accessible primitives.** Ask the agent to use your kit built on Radix, React Aria or native elements. It is much easier to keep accessibility than to retrofit it.

**Step 2: put the rules in the prompt and in AGENTS.md.** A short list beats a long one: semantic elements, visible focus, labels, 4.5:1 contrast, 24px targets, dialog focus management.

**Step 3: run an automated check.** axe-core catches a meaningful share of issues automatically. With Playwright you can make it part of the test suite:

import { test, expect } from &quot;@playwright/test&quot;;
import AxeBuilder from &quot;@axe-core/playwright&quot;;

test(&quot;pricing page has no detectable a11y violations&quot;, async ({ page }) => {
  await page.goto(&quot;/pricing&quot;);
  const results = await new AxeBuilder({ page })
    .withTags([&quot;wcag2a&quot;, &quot;wcag2aa&quot;, &quot;wcag22aa&quot;])
    .analyze();
  expect(results.violations).toEqual([]);
});

**Step 4: do a two-minute keyboard pass.** Unplug the mouse. Tab through the page: can you see where you are, reach everything, open and close every menu, and never get trapped? Automated tools cannot judge focus order or whether a label makes sense.

**Step 5: listen once.** Turn on VoiceOver or NVDA and read the main flow. Five minutes is enough to find unlabeled buttons and confusing headings.

## What to put in the pull-request template

A short, repeated checklist does more than a long policy document nobody opens. Ours has five lines: keyboard pass done (yes/no), new interactive elements are native or use an accessible primitive, contrast checked in both themes, new images have alt text or are marked decorative, and axe test passes. When an agent opens the pull request, ask it to fill in the template honestly and to write NEEDS HUMAN where it could not check something itself, such as how the flow sounds in a screen reader.

## Pitfalls

- **Treating automated scores as done.** Automated tools find only part of the problems; keyboard and screen-reader checks find the rest.

- **ARIA as decoration.** `role="button"` on a div still needs keyboard handling. The first rule of ARIA is to prefer native elements.

- **Hiding focus for aesthetics.** Use `:focus-visible` instead.

- **Motion without an off switch.** Respect `prefers-reduced-motion`.

- **Colour as the only signal.** Red borders for errors need text too.

## Questions we get

**Which WCAG level should we aim for?** WCAG 2.2 AA is the common target and what most accessibility laws and procurement rules refer to. Start there; individual AAA criteria are worth adopting where they are cheap, such as larger targets.

**Can the agent test with a screen reader itself?** Not reliably. It can run axe, check the accessibility tree and reason about labels, but a short human pass with VoiceOver or NVDA still finds problems no tool reports, such as confusing reading order or redundant announcements.

**Does using Radix or React Aria make us compliant?** It makes compliance much easier for the widgets they cover. You still own contrast, labels, headings, alt text, focus styles and the content itself.

**How do we stop regressions?** Keep the axe test in CI, add a keyboard-only end-to-end test for the main flow, and include accessibility items in the pull-request template so reviewers check them every time.

## Our take

Make accessibility structural, not a final pass. Generate on top of accessible primitives, keep the eight checks above in your prompts, run axe in CI and add an audit skill (accessibility, web-design-guidelines) to the agent's definition of done. Accessible UI is also better UI for everyone: keyboard power users, people on bright-sunlit phones, and the agent itself, which navigates pages through the same accessibility tree screen readers use.

## Checklist

- Actions are `<button>`, navigation is `<a href>`

- Visible `:focus-visible` style on every interactive element

- Icon-only controls have accessible names

- Text contrast ≥ 4.5:1 in both themes

- Targets ≥ 24×24 CSS px on mobile

- Dialogs trap focus, close on Escape, return focus

- Inputs have labels; errors linked with aria-describedby

- axe check in CI plus a manual keyboard pass

## References
- [Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/) — W3C
- [ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/) — W3C WAI
- [Radix Primitives introduction](https://www.radix-ui.com/primitives/docs/overview/introduction) — Radix
- [Web Interface Guidelines](https://vercel.com/design/guidelines) — Vercel
- [Understanding SC 2.5.8 Target Size (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) — W3C WAI
- [Dialog (Modal) pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/) — W3C WAI APG
- [:focus-visible](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus-visible) — MDN
- [axe-core](https://github.com/dequelabs/axe-core) — Deque
- [Accessibility testing](https://playwright.dev/docs/accessibility-testing) — Playwright
- [The WebAIM Million](https://webaim.org/projects/million/) — WebAIM