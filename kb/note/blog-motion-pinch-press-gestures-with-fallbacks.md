# Motion’s new pinch and press gestures: ship them with a visible fallback

> Motion 14.11 (9 November 2026) adds pinch for two-finger and trackpad zoom and rotate; 14.10 (5 November) gave press double press, long press and hold-to-repeat. What the new APIs do, where they quietly break scrolling and accessibility, and a checklist for shipping gestures with buttons that do the same job.

Blog post: <https://ui.incidental.site/blog/motion-pinch-press-gestures-with-fallbacks/>

Motion, the animation library that grew out of Framer Motion, shipped two gesture releases in five days. Version **14.10.0** on 5 November 2026 taught `press` to count, hold and repeat, so one function now covers double press, long press and press-and-hold steppers. Version **14.11.0** on 9 November added `pinch`: two-finger zoom and rotate, and a patch the same day (14.11.1) made rotation snapping use the release velocity and let you choose the pivot. For product teams this closes a gap that usually meant a second gesture library or a pile of pointer-event code. It also makes it very easy to ship interactions nobody can find, and some people cannot perform.

## What shipped

- **`pinch()` handles four kinds of input:** two pointers, trackpads, `wheel` events with `ctrlKey`, and Safari’s own `gesturestart`/`gesturechange`/`gestureend` events. The element scales and rotates around the point between the fingers, or under the cursor on a trackpad.

- **Limits, elasticity and snapping are options, not your maths.** `scale` and `rotate` take `min`/`max`; `elastic` (default 0.35) controls how far you can overshoot; `rotate.snap: 90` lands on the nearest quarter turn; `snapToOrigin` springs back to 1× and upright. `origin` can be the pointer or a fixed point such as the centre.

- **It plays well with the other gestures.** With `drag` on the same element, lifting one finger continues as a drag without a jump, and a zoom does not end in a fling. A pinch is never a press: it cancels a running press with `success: false`.

- **`press()` gained `count`, `hold` and `repeat`.** `count: 2` is a double press (with a 0.3-second default gap); `hold: 1` is a one-second long press with an `onHold` progress value from 0 to 1; `hold` plus `repeat` fires `onRepeat` while a stepper button is held. A long press cancels if the pointer moves more than a few pixels, so scrolling does not trigger it, and Motion suppresses the touch context menu.

- **Keyboard support is built into `press`.** Any element with a press gesture becomes focusable and responds to Enter. The 14.10 release also added Home and End keys to `Reorder` and a new `tap` prop on `motion` components.

The pinch documentation shows a plain JavaScript function that takes an element, an array or a selector and returns a stop function. In a React component the natural shape is to call it on a ref inside an effect and return that stop function as the cleanup. That is our reading of the API, not a separate React prop, so check the docs for your installed version.

## Our take: a gesture is a shortcut, not a feature

Pinch, double press and long press are invisible. Nothing on screen says “hold me” or “two fingers here”, and many people use a mouse, a keyboard, a switch or a single finger. WCAG 2.2 already draws the line. Success criterion 2.5.1 (Pointer Gestures, level A) says anything operated by a multipoint or path-based gesture must also work with a single pointer, unless the gesture is essential. 2.5.7 (Dragging Movements, AA) says the same for dragging. So the shippable pattern is always a pair: the gesture as a fast path for people who know it, and a visible control that does exactly the same thing.

The second trap is quieter. `pinch` sets `touch-action: none` on the element so the browser does not scroll or zoom the page underneath. That is correct inside a photo viewer. On a full-width image in a scrolling feed, it means a one-finger swipe that starts on the image no longer scrolls the page. The fix is a design decision, not a code tweak: make things pinchable inside a focused surface such as a lightbox, a map or a canvas, and keep inline media static.

Press variants need the same discipline. Do not stack a single press and a double press on one element unless you are happy for the single action to feel delayed or ambiguous; give each element one job. Long press is best for 
hold to confirm
 on destructive actions, where the `onHold` progress can draw a ring that fills as you hold, and the hold itself is the safety. It is a poor place to hide the only way to reach a menu. Hold-to-repeat belongs on stepper buttons that still change by one on a normal press, next to a field you can type into.

## Checklist before you ship a gesture

- **Write the visible control first.** Zoom buttons and a reset, a rotate button, a ⋯ menu, a delete button with confirmation. Then add the gesture as a shortcut for the same action.

- **Pinch only inside a focused surface.** Lightbox, map, editor canvas. Never a full-bleed image in a scrolling page, because `touch-action: none` takes over the swipe.

- **Set limits that match the content.** For photos, `scale: { min: 1, max: 4 }` with a low `elastic`; turn `rotate` off unless rotation means something.

- **Snap to states the user can name.** `rotate.snap: 90` for orientation, `snapToOrigin` for a “fit” reset, and show the current zoom as text.

- **One press meaning per element.** Do not combine single and double press on the same target.

- **Use long press as hold-to-confirm, with progress.** Draw `onHold` progress, cancel cleanly on early release, and offer a normal confirm dialog as the alternative.

- **Hold-to-repeat starts slow.** A short `hold` before `repeat`, so a quick tap still changes the value by one, and a text field for big jumps.

- **Test with keyboard only.** Tab to every pressable element and press Enter. Check that held-key behaviour matches what you expect rather than assuming.

- **Test on a real phone and a trackpad.** Ctrl-wheel on a desktop mouse, Safari on iOS, Android Chrome; confirm the page still scrolls around the gesture surface.

- **Tell people once.** A one-line hint (“Pinch or use + / − to zoom”) the first time the surface opens, then get out of the way.

```
# Paste this to your coding agent
Add Motion gestures to our image viewer only (the lightbox, not the feed).
Use pinch() with scale { min: 1, max: 4 }, elastic 0.2, rotate off, and
a "Fit" button that animates scale, rotate, x and y back to their start.
Attach it in an effect on a ref and call the returned stop function on cleanup.
Every gesture needs a visible control that does the same thing:
  + / − zoom buttons, a Fit button, and the current zoom shown as text.
For "Delete photo", use press() with hold: 1 and draw onHold progress as a
ring; keep the normal confirm dialog as the alternative path.
Keep page scrolling working outside the lightbox. Test keyboard-only,
iOS Safari and a trackpad, and list anything you could not test.
```

## When not to use it

Skip pinch when the content is text: let the browser’s own zoom do its job, and never block it. Skip long press and double press for primary actions in a web app that most people will use with a mouse. Use these gestures where they match a physical expectation—photos, maps, canvases, steppers, hold-to-confirm—and treat them as shortcuts layered over controls everyone can see.

Related on UI Hub: 
motion that feels right
, 
animated React component libraries
, and 
accessibility in AI-generated UI
.

## References
- [Motion changelog (14.10.0 on 5 Nov, 14.11.0 and 14.11.1 on 9 Nov 2026)](https://motion.dev/changelog) — Motion
- [CHANGELOG.md](https://raw.githubusercontent.com/motiondivision/motion/refs/heads/main/CHANGELOG.md) — motiondivision/motion on GitHub
- [pinch](https://motion.dev/docs/pinch) — Motion docs
- [press](https://motion.dev/docs/press) — Motion docs
- [Pinch zoom live example](https://examples.motion.dev/js/pinch-zoom) — Motion examples
- [Gesture animation (React)](https://motion.dev/docs/react-gestures) — Motion docs
- [touch-action](https://developer.mozilla.org/en-US/docs/Web/CSS/touch-action) — MDN Web Docs
- [Understanding SC 2.5.1: Pointer Gestures](https://www.w3.org/WAI/WCAG22/Understanding/pointer-gestures.html) — W3C WAI
- [Understanding SC 2.5.7: Dragging Movements](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html) — W3C WAI