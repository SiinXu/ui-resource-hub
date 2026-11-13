# Figma’s 3D transforms map straight to CSS. The traps are in what flattens

> On 12 November 2026 Figma opened its 3D transform and Perspective effects in beta, with Dev Mode copying them as CSS and the Figma MCP passing them to coding agents. How each control maps to a CSS property, why opacity, clipping and effects quietly flatten a 3D scene in both Figma and the browser, where depth helps an interface and where it hurts, plus a handoff checklist and a prompt for your coding agent.

Blog post: <https://ui.incidental.site/blog/figma-3d-transforms-css-handoff/>

On 12 November 2026 Figma moved two new effects into open beta for Full seats: **3D transform**, which rotates a layer on the X, Y and Z axes and pushes it along Z with a Depth value, and **Perspective**, which sets the camera distance for everything inside a frame. The Figma agent can compose 3D scenes, Figma Motion can keyframe them, and the release notes pitch the feature as “ship directly to code”: Dev Mode copies the CSS, and coding agents can read and create 3D designs through the Figma MCP server. The same day, Framer’s agent learned to generate images and shaders. Depth and texture are becoming ordinary materials in design tools, which means they will start showing up in the code your agents write.

The good news is that this is the most literal design-to-code mapping Figma has shipped. The less obvious news is that the hard part is not the angles. It is the rules for when a 3D scene silently collapses into a flat picture, and those rules are almost the same on the canvas and in the browser.

## What shipped

- **Two effects, applied like any other.** 3D transform works on vectors, images, frames, components and text, and stays non-destructive: the content remains editable, and text and fills, including shader fills, render with the transformed layer.

- **Camera vs object.** Figma’s help article puts it neatly: Perspective is moving the camera, Depth is moving the object. Perspective goes on the parent frame so its children share one viewpoint.

- **A shared space is opt-in.** “Keep nested layers 3D” lets children intersect and sort by depth; “Turn into flat plane” ends the 3D space at that frame. There are also controls for the origin point and for showing or hiding the backface.

- **Motion and agents.** Rotate X, Rotate Y, Depth and perspective can be keyframed, and the agent accepts prompts like “arrange these layers as the faces of a cube and animate it rotating”.

- **A plugin API in beta.** Plugin update 142 adds `transform3d`, `transformOrigin` and `scene3d`, plus Motion keyframe fields for them. Figma’s Brand Studio wrote that the agent even built them a generative plugin to scatter cards into grids, rings and helices.

## The mapping, control by control

Figma’s docs spell out the correspondence, and the plugin API is stricter still: an editable 3D transform is `translateZ() rotateX() rotateY() rotateZ()`, 
in that order
. Order matters in CSS because each function rotates the coordinate system for the next one, so keep the order when you hand-edit.

- **Rotation X / Y / Z** → `rotateX()`, `rotateY()`, `rotateZ()` in `transform`.

- **Depth** → `translateZ()`, in pixels.

- **Perspective on a frame** → the `perspective` property on the parent. Not the `perspective()` function on each child, which gives every card its own vanishing point.

- **Keep nested layers 3D / Turn into flat plane** → `transform-style: preserve-3d` / `flat`. This property is not inherited, so every intermediate wrapper needs it too.

- **Backface** → `backface-visibility`. Origin point → `transform-origin`.

## Our take: design the flattening, don’t discover it

In Figma, turning on “Keep nested layers 3D” disables the frame’s opacity and hides its blend modes, shaders, other effects, clip content, fills and strokes. That looks like a tool limitation. It is actually the browser’s rule showing through. MDN lists the “grouping” values that force `transform-style` to behave as `flat` even when you wrote `preserve-3d`: `overflow` other than `visible` or `clip`, `opacity` below 1, any `filter`, `clip-path`, `isolation: isolate`, masks, `mix-blend-mode` and paint containment.

That is exactly where AI-generated 3D code breaks. An agent wraps the scene in a card with `overflow: hidden` and rounded corners, or fades it in with `opacity`, or adds a glassy `backdrop` blur, and the cube becomes a flat sticker. Nothing errors. It just looks wrong, and the screenshot review often misses it because the first frame of the animation looks fine.

Figma’s plugin docs describe the fix, and it works in CSS unchanged: **split the scene into two wrappers**. The outer one is flat and carries the perspective, the clipping, the radius, the opacity and any effects. The inner one carries `preserve-3d` and nothing that groups. If designers build that structure in the file, the CSS that Dev Mode or the MCP produces will already be correct.

## Where depth earns its place

Good uses are the ones Figma lists: a tilted device mockup, a fan of cards, a flip between two faces, a hero composition. Our rule of thumb is to keep readable text within small angles and to never put form fields, menus or body copy on a rotated plane. Rotated text is harder to read, and keyboard focus rings on a tilted element are easy to lose.

Motion is the bigger risk. Large rotations, zooms through Z and continuous spins are the kind of movement that can make people with vestibular disorders unwell. WCAG’s “Animation from Interactions” criterion asks for a way to turn motion triggered by interaction off; in CSS that means a `prefers-reduced-motion` branch that keeps the static 3D pose, or swaps the flip for a cross-fade. Animate only `transform` and `opacity` on the outer wrapper, and keep the number of live 3D layers small on mobile.

## Checklist: hand off a 3D layer

- **Perspective on the parent.** One `perspective` per scene, on the flat outer wrapper. Note the value in the spec; small numbers exaggerate distortion.

- **Keep the function order.** `translateZ rotateX rotateY rotateZ`, as Dev Mode copies it.

- **Two wrappers.** Outer: perspective, radius, `overflow`, opacity, filters. Inner: `transform-style: preserve-3d` only.

- **Search the diff for groupers.** `overflow: hidden`, `opacity`, `filter`, `backdrop-filter`, `clip-path`, `isolation`, `mix-blend-mode`, `contain` on any element between the scene root and its faces.

- **Backfaces on purpose.** For a flip card, two layers with `backface-visibility: hidden`, the back pre-rotated 180°.

- **Text stays readable.** Body text, inputs and menus stay flat; only decorative or headline layers rotate.

- **Reduced motion.** A `prefers-reduced-motion: reduce` branch: static pose or a fade, no spinning.

- **Fallback pose.** The flat, unrotated layout must still make sense if the 3D is removed.

- **Check both themes.** Shading and shadows that sell depth on white often vanish on near-black; check light and dark.

```
/* Flip card: flat outer wrapper, 3D inner scene */
.stage { perspective: 900px; border-radius: 16px; overflow: hidden; }
.scene { transform-style: preserve-3d; transition: transform .6s; }
.stage:hover .scene { transform: rotateY(180deg); }
.face  { position: absolute; inset: 0; backface-visibility: hidden; }
.back  { transform: rotateY(180deg); }
@media (prefers-reduced-motion: reduce) {
  .scene { transition: none; }
  .stage:hover .scene { transform: none; }  /* show the back with a fade instead */
}
```

```
# Paste this to your coding agent (with the Figma MCP connected)
Implement the selected Figma frame, including its 3D transform and Perspective effects.
- Copy transforms as translateZ() rotateX() rotateY() rotateZ() in that order.
- Put perspective on ONE flat outer wrapper per scene; it also owns radius,
  overflow, opacity, filters and shadows.
- Put transform-style: preserve-3d on the inner scene and on every wrapper
  between it and the faces. No overflow/opacity/filter/clip-path/isolation/
  mix-blend-mode/contain on those elements.
- Text inputs, menus and body copy stay unrotated.
- Add a prefers-reduced-motion branch (static pose or cross-fade).
Report: each 3D element, its CSS, and any property you removed because it flattened the scene.
```

## What we would not do yet

The feature and its plugin API are in beta, and Figma notes that the API may change; an imported `FREEFORM` transform can be read but not written. Don’t build a design-system token pipeline on the exact Dev Mode output format yet. Treat the CSS as a reference for angles and depth, and keep the structural rule, flat outside and 3D inside, as the part you standardise.

Related on UI Hub: 
handing off Figma Motion springs
, 
shipping Figma shaders
, and 
motion that feels right
.

## References
- [Design in 3D, natively in Figma, and ship directly to code (12 Nov 2026)](https://www.figma.com/release-notes/) — Figma release notes
- [How 3D transforms and Figma’s agent brought a launch video to life — Chad Colby](https://www.figma.com/blog/how-3d-transforms-and-figmas-agent-brought-a-launch-video-to-life/) — Figma Blog
- [Create 3D effects in Figma Design](https://help.figma.com/hc/en-us/articles/44568893374999-Create-3D-effects-in-Figma-Design) — Figma Learn
- [Version 1, Update 142](https://developers.figma.com/docs/plugins/updates/2026/11/12/version-1-update-142/) — Figma Developer Docs
- [Transform3d](https://developers.figma.com/docs/plugins/api/Transform3d/) — Figma Developer Docs
- [Scene3d](https://developers.figma.com/docs/plugins/api/Scene3d/) — Figma Developer Docs
- [Image and Shader Generation (12 Nov 2026)](https://www.framer.com/updates/image-shader-generation) — Framer Updates
- [transform-style](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-style) — MDN Web Docs
- [perspective](https://developer.mozilla.org/en-US/docs/Web/CSS/perspective) — MDN Web Docs
- [backface-visibility](https://developer.mozilla.org/en-US/docs/Web/CSS/backface-visibility) — MDN Web Docs
- [prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion) — MDN Web Docs
- [Understanding SC 2.3.3: Animation from Interactions](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html) — W3C WAI