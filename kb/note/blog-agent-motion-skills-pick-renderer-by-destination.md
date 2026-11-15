# Coding agents are turning into motion studios. Pick the renderer by where the motion ships

> On 14–15 November 2026 a list of 18 free GitHub tools for making animation with Claude Code or Codex was the most-saved design post on X, and one catalogue now counts 146 motion-skill repositories. The tools differ less in what they can animate than in what they hand back: code in your app, a Lottie file or a rendered MP4. How to choose by destination, why a frame-driven clock matters, the licence and house-style traps, plus a checklist and an agent prompt.

Blog post: <https://ui.incidental.site/blog/agent-motion-skills-pick-renderer-by-destination/>

The design post people saved most on X between 14 and 15 November 2026 was not a model launch. It was a list of 18 free GitHub projects to hand Claude Code or Codex for animation, from Remotion’s agent skills and Motion Canvas to Lottie, Manim, three.js, Blender and Godot. It passed 5,800 bookmarks within a day, and AI Design Daily’s 15 November edition named it the most-saved post of its sweep. None of those tools is new. What is new is the habit of treating them as parts an agent can pick up, and the speed at which skills for them are appearing: motif’s catalogue counted 146 motion-skill repositories holding 901 skill files on 12 November.

A long list invites the wrong question, which is “which one is best?”. For anyone who designs interfaces, the useful question is where the motion will live when it is done: inside the product, inside a video, or inside a file someone else will play. That decides the tool, the review and the licence. This post maps the main options to those destinations and lists the traps we would check before letting an agent animate anything for us.

## What is in the toolbox

- **HTML to video: HyperFrames.** HeyGen’s Apache-2.0 framework turns HTML, CSS, media and seekable animations into deterministic MP4s. It ships nine agent skills, a registry of about 450 editable blocks (titles, captions, charts, transitions) and a CLI that lints, previews and renders. Two of the skills, reverse-any-video and style-sampling, need the paid Pro plan.

- **React to video: Remotion.** Compositions are React components whose every property is computed from the current frame. Remotion maintains 13 official skills, installed with `npx remotion skills add`, for creating, previewing, rendering, captions and maps.

- **Vector files that play anywhere: Lottie.** Diffusion Studio’s MIT-licensed text-to-lottie skill has the agent write Lottie JSON and preview it live in a bundled player. The output plays on the web, iOS, Android, React Native and Flutter, or opens in After Effects for a human pass.

- **Diagrams and explainers: Motion Canvas and Manim.** Code-first tools for animated diagrams and maths; several skills now plan the scenes, render low-quality previews and check frames before the final render.

- **Interface motion: skills, not a renderer.** Emil Kowalski’s MIT-licensed skills (animate, choreograph, review-animations, remove-animations, animation-performance) write and review the CSS or Motion code that ships in your app. This is product motion, not video.

## Our take: choose by destination, then check the clock

Most comparisons sort these tools by what they can draw. In practice they overlap heavily; HyperFrames, Remotion and Motion Canvas can all make a kinetic title. What separates them is what comes back and who edits it next.

- **It ships inside the product** (enter, exit, hover, layout, loading): use your app’s own CSS or Motion code with an interface-motion skill. Never ship a rendered video of UI where real UI would do; it cannot respond to input, theme or text size.

- **It ships as a film** (launch video, changelog clip, explainer): use a deterministic renderer. Pick HyperFrames if your team thinks in HTML and GSAP, Remotion if it thinks in React and wants the composition next to its components.

- **It ships as an asset inside apps** (empty state, success tick, onboarding illustration): ask for Lottie, so a motion designer can open it in After Effects and engineers can play it natively.

- **It explains something** (a data change, an algorithm, a formula): Motion Canvas or Manim, which keep the values on screen tied to the code.

Then check the clock. A film renderer captures one frame at a time, so every movement must be computed from the frame number. Remotion’s docs warn that animations not driven by `useCurrentFrame()`, CSS transitions for example, can flicker during rendering. Agents trained mostly on web UI reach for exactly those transitions. In a video project, a wall-clock animation is a bug even when the preview looks fine.

## Three traps we would check first

- **Licences differ more than the README badges suggest.** HyperFrames is Apache-2.0. Remotion is source-available: free for individuals, non-profits and for-profit companies with up to three employees, while larger companies need a company licence, and every skill built on Remotion inherits that rule. Some catalogue entries have no licence file at all, and several bundle GSAP under its own standard licence, which is not an open-source licence. Check before a client project, not after.

- **A skill is code with permissions.** motif’s catalogue and HyperFrames’ community-skills README both warn that a skill can tell your agent to run commands, read files or spend money on paid APIs. Read the SKILL.md and its scripts, install only the skills the job needs, and keep paid keys out of the environment unless the job calls for them.

- **Every agent film moves the same way.** The motion-kit project points out that HyperFrames’ own animation guide sets a house default of 0.6 seconds on `power3.out`, so agents that follow it fade everything up with the same curve and even staggers. Its fix is the same advice good interface motion follows: duration from distance and weight, one element leading and the rest reacting at uneven offsets, and many texts simply cut on. If your product already has motion tokens, give the agent those numbers instead of letting a framework default become your brand.

## Where we would start

For a design team, the cheapest first win is a 15-second changelog clip built from the product’s real components and tokens, rendered by HyperFrames or Remotion, reviewed on a contact sheet of frames before the full render. The second is replacing one hand-made Lottie with an agent draft that a motion designer finishes in After Effects. Both keep a human on taste and the agent on keyframes. Interface motion is the place to be strictest: one skill to write it, one to review it, and a reduced-motion check every time.

## Checklist: brief an agent for motion

- **Name the destination.** In-app code, MP4, Lottie JSON or an explainer. One per request.

- **Name the renderer and the licence.** Confirm your company qualifies for the free tier of anything source-available, and note bundled libraries with their own terms.

- **Give the clock rule.** For films: everything computed from the frame number, no CSS transitions or timers. For apps: transform and opacity only, no layout thrash.

- **Hand over your motion tokens.** Durations, curves and springs from your design system, or ask for durations derived from distance and size instead of one global default.

- **Specify format.** Frame rate, total frames or seconds, aspect ratios (16:9 and 9:16), safe zones, transparent background if needed.

- **Ask for a review artefact.** A contact sheet of key frames or a low-resolution preview before the final render.

- **Keep in-product motion accessible.** Respect `prefers-reduced-motion`, and give any loop longer than five seconds a pause control (WCAG 2.2.2).

- **Audit the skills you installed.** Read each SKILL.md and script; remove skills you no longer use.

```
# Paste this to your coding agent
Make a 15-second 
 clip for 
.
- Destination: MP4, 1920x1080 and 1080x1920, 30 fps. Renderer: 
.
- Licence: confirm we qualify for the renderer’s licence; list any bundled
  library with its own terms (e.g. GSAP) before you start.
- Build scenes from our real components and tokens in 
; no stock UI.
- Clock: every animated value comes from the frame number. No CSS
  transitions, setTimeout or requestAnimationFrame.
- Motion: use our tokens 
. If missing, derive
  duration from distance and size; one element leads, others react at uneven
  offsets; most text cuts on. Do not apply one global ease to everything.
- Before the final render, give me a contact sheet of 12 key frames and wait.
Report: renderer and version, licence check, skills used, and anything you
could not verify.
```

Related on UI Hub: 
motion that feels right
, 
handing off Figma Motion springs
, and 
the best animated React component libraries of 2026
.

## References
- [18 free GitHub tools for making animation with a coding agent — @okapi_fukugyo (14 Nov 2026)](https://x.com/okapi_fukugyo/status/2121725407867351215) — X
- [AI Design Daily, 15 Nov 2026 (morning edition)](https://studios.greatcreations.art/daily-design/editions/2026-11-15/morning.html) — Daily Design
- [Agent skills for making motion with Claude](https://createmotion.io/resources/agent-skills/) — motif
- [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) — GitHub
- [HyperFrames introduction](https://hyperframes.heygen.com/introduction) — HyperFrames docs (HeyGen)
- [Agent Skills](https://www.remotion.dev/docs/ai/skills) — Remotion docs
- [Animating properties](https://www.remotion.dev/docs/animating-properties) — Remotion docs
- [Remotion License](https://github.com/remotion-dev/remotion/blob/main/LICENSE.md) — GitHub · remotion-dev
- [diffusionstudio/lottie (text-to-lottie)](https://github.com/diffusionstudio/lottie) — GitHub
- [emilkowalski/skills](https://github.com/emilkowalski/skills) — GitHub
- [hughminhphan/motion-kit](https://github.com/hughminhphan/motion-kit) — GitHub
- [Motion Canvas](https://motioncanvas.io/) — motioncanvas.io
- [prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion) — MDN Web Docs
- [Understanding SC 2.2.2: Pause, Stop, Hide](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html) — W3C WAI