# Figma shaders are generally available: how to ship shader backgrounds that stay fast and readable

> On 2 November Figma made shaders generally available, raised export to 4096 px and let shaders travel into code layers. That moves glowing gradients, grain and glass effects from mockups toward real pages. What changed, what is still unclear, and a checklist for shipping a shader without hurting contrast, motion comfort or battery life.

Blog post: <https://ui.incidental.site/blog/figma-shaders-ga-ship-shader-backgrounds/>

On 2 November Figma shipped a short release note with a big consequence: **shaders are now generally available to all users**, they render and export at up to **4096 px**, and they can be included when you use “build this with code” to turn a design into a **code layer**. Inside a code layer the shader runs when the layer is set to Play. Figma says this part works in the browser on Chrome 157 and is rolling out this week. A week earlier, on 27 October, shaders also gained version history, with an agent-written description for each version.

Put together, a shader is no longer a canvas trick that ends up as a flat PNG or a looping MP4 at handoff. It can stay code. Designers replying to Figma’s announcement on X picked up on exactly that, and one asked the question nobody has answered yet: does the shader stay editable once it lands in code, or is it flattened? That is worth testing before you plan around it.

## What a Figma shader is

- **Shader fills** replace a layer’s fill with a generated visual: patterns, mesh gradients, noise, procedural textures such as marble or water. They can be static or animated, apply to fills and strokes, and stack with ordinary fills.

- **Shader effects** take the layer’s existing pixels as input and change them: grain, blur, distortion, halftone, dithering, colour shifts, even hover-triggered motion.

- **You build them by prompting.** Open the Figma agent and ask it to “build me a shader”, describe what you want to see, and name the controls you want, such as a slider for glow intensity. Figma’s own tips: say “shader” explicitly (“make me a mesh gradient” may give you a plain image fill), use real-world references (“like a risograph print”), and state what must survive, such as legible text, crisp edges or brand hues.

- **They behave like design-system parts.** Combinations of shader fills or effects can be saved as styles and published to a team library, and you can view the code behind each one.

## What changed on 2 November, and what did not

Three things changed: general availability, the 4096 px export ceiling, and the path into code layers. The higher export matters more than it sounds, because a sharp still is exactly what you need as the fallback for a live shader. The code layer path matters because it is the first official route from a Figma shader to running code rather than a video.

Some things did not change. On the canvas only one animated or interactive shader plays per page at a time. Code layers are still in open beta, and code layer generation is free on paid plans only through 4 November; after that it uses AI credits like other agent features. And a code layer is a prototype on the canvas, not your production stack, so treat it as a working reference for engineering, not the final component.

## Our take

Shaders are the most “fancy” thing a design tool can hand to a developer, and that is the risk. The same properties that make them striking are the ones that break pages: they move behind text, they change brightness frame by frame, and they keep a GPU busy whether anyone is looking or not. A shader that looked fine in a Figma frame can fail contrast on its brightest frame, drain a phone battery, or run a full-screen loop for a reader who asked their system for reduced motion.

So treat a shader like a design token with rules attached, not like an image. Decide where it is allowed (hero backgrounds and illustrations, not behind body copy), how bright it may get, whether it may move, and what replaces it when it cannot run. If you code shaders directly instead of going through Figma, small libraries such as Paper Shaders (zero-dependency WebGL shaders for React and vanilla JavaScript, Apache-2.0, about 1.3 million npm downloads in the week to 2 November) make that easy, but their docs ask you to pin an exact version because breaking changes still ship under 0.0.x.

## Checklist: shipping a shader background

- **Prompt for controls, not just a look.** Ask the agent for named sliders (intensity, speed, scale) and for what must stay unchanged, so engineering can tune it without a new prompt.

- **Save it as a style.** Publish the shader to the team library so every screen uses the same one, and lean on version history when someone changes it.

- **Export a 4096 px poster.** Use the sharpest still as the fallback image, the social card and the first paint before WebGL starts.

- **Check contrast on the worst frame.** Body text needs 4.5:1 against the brightest moment of the animation, not the average. Add a scrim behind text if needed.

- **Respect reduced motion.** Under `prefers-reduced-motion: reduce`, show the poster or set speed to zero.

- **Give long motion a pause.** If it moves for more than five seconds next to other content, WCAG 2.2.2 asks for a way to pause, stop or hide it.

- **Stop when nobody is looking.** Pause the render loop when the canvas leaves the viewport (Intersection Observer) or the tab is hidden.

- **Budget live canvases.** One live shader per view; everything else uses its still. Browsers cap how many WebGL contexts a page can hold.

- **Test the code layer handoff.** Build one design with a shader into a code layer and check whether its controls survive, before a team depends on it.

- **Pin and record.** Pin the shader library version in `package.json` and note which Figma style version the code matches.

```
shader-spec.md
  name:      hero-glow (Figma style v3)
  where:     hero background only, never behind body copy
  controls:  intensity 0–1 · speed 0–0.4 · hue locked to brand
  poster:    hero-glow@4096.webp (first paint, og image, reduced motion)
  contrast:  headline + CTA ≥ 4.5:1 on brightest frame · scrim 40%
  motion:    pause button · stops offscreen and on hidden tab
  budget:    1 live canvas per view
```

## How UI Hub helps

For the code layer workflow itself, read 
Figma code layers and Specs
. Motion rules from 
motion that feels right
 apply to shaders too, and 
OKLCH colour and dark mode
 helps you keep a shader inside your palette on both themes. Before shipping, run the checks in 
accessibility in AI-generated UI
, and if you would rather code the effect, compare options in 
the best animated React component libraries of 2026
.

## References
- [Release notes: Export shaders at higher resolutions and bring them into code layers (2 Nov 2026)](https://www.figma.com/release-notes/) — Figma
- [Create shaders with the Figma agent](https://help.figma.com/hc/en-us/articles/41147702210071-Create-shaders-with-the-Figma-agent) — Figma Learn
- [Use shaders in designs](https://help.figma.com/hc/en-us/articles/41175721167767-Use-shaders-in-designs) — Figma Learn
- [Prompting tips for generative plugins and shaders](https://help.figma.com/hc/en-us/articles/41408020198935-Prompting-tips-for-generative-plugins-and-shaders) — Figma Learn
- [Workflow lab: Figma Motion, Figma Weave and shaders](https://help.figma.com/hc/en-us/articles/42847574436119-Workflow-lab-New-tools-more-expression-with-Figma-Motion-Figma-Weave-and-shaders) — Figma Learn
- [What’s new from Config India 2026 (code layers open beta and credits)](https://help.figma.com/hc/en-us/articles/43663368947863-What-s-new-from-Config-India-2026) — Figma Learn
- [Reply asking whether shaders stay editable in code layers](https://x.com/SheryButtUXUI/status/2117367128642687211) — Shaheryar Butt (@SheryButtUXUI), X
- [Reply on shaders reaching sites instead of an MP4](https://x.com/lokidotdev/status/2117311148962058335) — Loki (@lokidotdev), X
- [paper-design/shaders](https://github.com/paper-design/shaders) — Paper, GitHub
- [Paper Shaders gallery](https://shaders.paper.design/) — Paper
- [Understanding SC 1.4.3: Contrast (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) — W3C Web Accessibility Initiative
- [Understanding SC 2.2.2: Pause, Stop, Hide](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html) — W3C Web Accessibility Initiative
- [prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion) — MDN Web Docs
- [Intersection Observer API](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API) — MDN Web Docs
- [WebGL best practices](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/WebGL_best_practices) — MDN Web Docs