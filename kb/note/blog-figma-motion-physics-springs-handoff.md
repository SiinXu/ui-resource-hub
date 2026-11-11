# Figma Motion now has physics springs: hand off three numbers, not a duration

> On 10 November 2026 Figma Motion added physics-based springs (mass, stiffness, damping) that can be saved in a design system, plus style previews and Lottie export previews. Why a spring belongs in your tokens, how to convert one spring for SwiftUI, Jetpack Compose, Motion and CSS without it feeling different on each, and a handoff checklist.

Blog post: <https://ui.incidental.site/blog/figma-motion-physics-springs-handoff/>

Figma shipped a small Motion bundle on 10 November 2026, and one part of it changes how motion gets handed to engineers. Custom springs in Figma Motion can now be **physics-based**: you set mass, stiffness and damping, and the duration is worked out from them instead of typed in. Figma says you can save that spring in a design system and reuse it. The same release adds **style previews**, so each preset animation plays in the list and on your canvas before you apply it, and **Lottie export previews**, so you can see how an animation will play as a Lottie file before you export it.

## What shipped

- **Two kinds of custom spring.** Figma’s help article now offers 
Time
 and 
Physics
. A time-based spring takes bounciness and a duration, which is what you want when motion must line up with a sound or a fixed beat. A physics-based spring takes stiffness, damping and mass, and its length follows from those values.

- **Android has no mass field.** Figma notes that Android springs use stiffness and a damping ratio, with no separate mass, while mass applies to iOS and web.

- **Physics springs can overrun the timeline.** Because the duration is computed, the motion can finish before or after the next keyframe; a line on the timeline shows where it really ends.

- **Previews before you commit.** Style previews play presets in place; the Lottie preview shows the exported result before you hand it off.

- **The API keeps less than you typed.** In Figma’s plugin API a custom spring is stored as a single normalized `bounce` from 0 to 1, and `figma.motion.physicalSpringToNormalized()` converts mass, stiffness and damping into it. Figma’s own agent skill notes that reading keyframes back returns only `bounce`.

## Our take: a spring is a token, and the three numbers are the source of truth

For years, motion handoff meant “300 ms, ease-out” in a spec and a developer guessing the rest. Springs fix the two things that never survived that handoff: an interruption keeps its velocity instead of jumping, and the feel comes from physics that every platform can reproduce. But a spring is only portable if the numbers travel with it. That last API detail matters. If an agent or plugin reads your file, it gets a normalized bounce, not the mass, stiffness and damping you tuned. So do not let the Figma file be the only place the spring lives. Name it, write the three numbers into your token file next to colour and radius, and treat Figma as one consumer of that token.

The second point is that the platforms do not take the same inputs. SwiftUI and Motion accept mass, stiffness and damping directly. Jetpack Compose takes a damping ratio and a stiffness, and behaves as if the mass were 1. If someone copies “stiffness 300” across without converting, the Android version will feel different. The conversion is simple physics, and it belongs in your tokens so nobody does it by hand:

- **Damping ratio** ζ = damping ÷ (2 × √(stiffness × mass)). Below 1 it overshoots; 1 settles without overshoot; above 1 creeps in slowly.

- **Compose**: `dampingRatio = ζ` and `stiffness = stiffness ÷ mass`.

- **Rough settle time** for a spring under 1: about 4 ÷ (ζ × √(stiffness ÷ mass)) seconds. Useful for checking that a “quick” spring is actually quick.

Worked example: a sheet spring of mass 1.2, stiffness 300, damping 26 gives ζ ≈ 0.68, a Compose stiffness of 250, and settles in roughly 0.37 seconds. A button spring of mass 1, stiffness 400, damping 30 gives ζ = 0.75 and settles in about 0.27 seconds. Those are our calculations from the formula, so check the feel on a device, but they show why the numbers, not a duration, are the thing to hand over.

Third, Lottie is not a spring. A Lottie file plays keyframes with easing curves, so the physics is baked in at export and will not respond to an interruption. That is fine for an illustration or a success animation. It is wrong for UI that people drag, dismiss or tap twice. The new Lottie preview is the moment to decide which one you are making.

## Checklist: hand off a spring that feels the same everywhere

- **Keep a small set.** Three to five named springs, such as `spring.snappy`, `spring.sheet` and `spring.bouncy`, saved in the Figma design system and mirrored in your token file.

- **Store mass, stiffness, damping and the derived values.** Add the damping ratio and the Compose stiffness so Android never converts by hand.

- **Use time-based springs only for synced motion.** Sound, video, a fixed onboarding beat. Everything a person touches gets a physics spring.

- **Watch the timeline line.** If a physics spring runs past the next keyframe, either let it overlap on purpose or pick a stiffer spring; do not stretch the keyframes to hide it.

- **Mark what ships as Lottie.** Decorative and celebratory motion can be baked; interactive UI should be built in code with the live spring.

- **Preview before you apply.** Use style previews on the real frame, in light and dark, not on a placeholder rectangle.

- **Write the reduced-motion version.** When `prefers-reduced-motion` is on, swap movement for a short fade or a spring with ζ of 1 and no travel.

- **Test interruption on a device.** Open and dismiss a sheet halfway through, twice. That is the case springs exist for.

- **Never use damping 0.** Motion warns that such a spring runs forever; keep a floor in your tokens.

```
# Paste this to your coding agent
Add our motion tokens from tokens/motion.json to the app.
Each spring has mass, stiffness and damping. For every platform:
  SwiftUI: Spring(mass:stiffness:damping:)
  Web (Motion): transition { type: "spring", mass, stiffness, damping }
  Compose: spring(dampingRatio = damping / (2*sqrt(stiffness*mass)),
                  stiffness = stiffness / mass)
Do not replace springs with fixed durations. Use spring.sheet for sheets
and drawers, spring.snappy for buttons and toggles.
Under prefers-reduced-motion, use a 150 ms opacity fade instead.
Test interrupting each animation halfway and list any that jump.
```

## When a duration is still right

Keep plain easing and a fixed time for loading indicators, progress, anything synced to media, and CSS-only pages where you cannot ship a spring engine. CSS `linear()` can approximate a spring curve by sampling it, and Motion can generate that string, but the result has a fixed length and will not carry velocity through an interruption. Use it as a fallback, not as the source.

Related on UI Hub: 
motion that feels right
, 
Motion’s pinch and press gestures
, and 
design tokens for agents
.

## References
- [New Figma Motion updates: physics based springs, style and Lottie export previews (10 Nov 2026)](https://www.figma.com/release-notes/) — Figma release notes
- [Adjust an animation’s easing](https://help.figma.com/hc/en-us/articles/41414048690839-Adjust-an-animation-s-easing) — Figma Learn
- [Motion (plugin API: MotionEasing, NormalizedSpring, PhysicalSpring)](https://developers.figma.com/docs/plugins/api/Motion/) — Figma Developer Docs
- [figma-use-motion: motion-easing.md](https://github.com/figma/mcp-server-guide/blob/main/skills/figma-use-motion/references/motion-easing.md) — figma/mcp-server-guide on GitHub
- [How Figma put the bounce in spring animations](https://www.figma.com/blog/how-we-built-spring-animations/) — Figma Blog
- [Spring](https://developer.apple.com/documentation/swiftui/spring) — Apple Developer Documentation
- [Customize animations (spring)](https://developer.android.com/develop/ui/compose/animation/customize) — Android Developers
- [spring](https://motion.dev/docs/spring) — Motion docs
- [linear() easing function](https://developer.mozilla.org/en-US/docs/Web/CSS/easing-function/linear) — MDN Web Docs
- [prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion) — MDN Web Docs