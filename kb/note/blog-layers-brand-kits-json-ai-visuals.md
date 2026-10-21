# Layers, brand kits and JSON: three ways AI visuals stop looking generic

> On 20 October Coco Labs launched Vyb, a design model that builds in layers; Gemini started remembering an uploaded brand style; and Bria shipped Fibo 2, which turns every edit into editable JSON. Three different answers to the same problem, and a checklist for using them.

Blog post: <https://siinxu.github.io/ui-resource-hub/blog/layers-brand-kits-json-ai-visuals/>

The most common complaint about AI-made graphics is not that they look bad. It is that they all look the same: the right mood, the wrong font, a brand colour that is almost but not quite yours, and a headline that melts when you try to change one word. Three launches on 20 October attack that problem from three different directions, and together they make a useful map of what to ask from any visual AI tool you adopt.

## Three launches, three answers

- **Vyb (Coco Labs): build in layers.** Vyb is pitched as a design model, not an image generator. It assembles your own images, fonts and colours layer by layer, so text stays text, graphics stay vectors and photos stay pixels, and it calls image generators only to fill gaps. Under the hood is a new design language, Cocolang, which Coco Labs says is compact enough for a model's context window and exports losslessly to tools such as Figma. It is in early access behind a waitlist.

- **Gemini: remember the brand.** Google's new business hub in Gemini lets you define a brand style by uploading your website, brand kit, fonts or colour palettes. Paired with its Nano Banana 2.1 image model, Gemini keeps that style for later requests, so you do not have to re-upload guidelines for every campaign. Google says it rolls out globally over the coming days.

- **Fibo 2 (Bria): make the edit inspectable.** Bria's new open-weights model, trained on licensed data, turns a plain-language edit into a structured JSON instruction (objects, lighting, background, text and the edit itself), then applies that JSON. You can generate the JSON separately, review or change it, and pass your own. With the same images, JSON and seed you can recreate a result. Edits can combine up to four reference images, or use a mask on a single image to protect everything outside it.

## What the numbers do and do not say

Coco Labs published its own benchmarks. On 145 Google fonts, Vyb matched the reference letter shapes 90.3% of the time against 76.0% for the next model it tested; on exact hex colours its average error was zero; and over 200 edits it changed 11.9% of pixels on average, while the image models it compared changed more than 90%. Those are vendor tests on public fonts, not independent results, but the last figure is the one that matters for daily work. A model that repaints the whole image to change one word slowly erodes everything you liked about the first version. Vyb's approval rate was also slightly lower than its best rival's, which Coco Labs puts down to the model declining edits that would hurt legibility.

## Our take

All three are moving taste out of the prompt and into something you can check. Layers make your fonts and colours facts rather than suggestions. A stored brand style turns guidelines into a reusable asset. Structured JSON turns an edit into a diff you can review before it renders. The common failure they target is the same one we see in generated interfaces: the model drifts toward the average of its training data unless your choices are pinned down in a form it cannot reinterpret.

Two cautions. First, a remembered brand style is only as good as the kit you upload. A logo and a vague palette will give you consistent mediocrity. Second, do not mistake a layered export for a design system. If the tool outputs editable text in your font but ignores your spacing and hierarchy rules, you still have cleanup work. Ask for the layers, and still check the layout.

## Checklist: making AI visuals look like yours

- **Prepare a real brand kit before you start.** Fonts as files, colours as hex values, logo in vector, two or three approved reference layouts, and a short list of things you never do.

- **Test fidelity with one boring asset.** Ask for a plain banner with your headline font and primary colour, then check the font and pick the colour with an eyedropper. If either is off, the tool is guessing.

- **Test edit drift.** Change one word or one colour and compare before and after. Anything else that moved is a warning sign for multi-round work.

- **Prefer outputs you can open.** Layered files or Figma export for anything that will be edited again; flat images only for one-off use.

- **Keep the instruction, not just the image.** When a tool exposes structured instructions and seeds, as Fibo 2 does, save them next to the asset so a variant next month starts from the same spec.

- **Protect what must not change.** Use masks, locked layers or explicit "keep everything else" rules for product photos, faces and logos.

```
{
  "brand": "Northwind Tea",
  "fonts": { "display": "Fraunces 600", "body": "Inter 400" },
  "colors": { "ink": "#1d1a16", "paper": "#f6f1e7", "accent": "#8a5a3b" },
  "logo": "logo.svg  (clear space ≥ 1× cap height)",
  "layout": "one focal photo · headline top-left · max 2 text blocks",
  "never": ["gradients on text", "stock 3D", "more than one accent"],
  "keep": "product photo pixels untouched; edit text and colour only"
}
```

## How UI Hub helps

The brand kit above is the visual sibling of a token file. If you are setting one up for a product, our posts on 
design tokens for agents
 and 
OKLCH colour
 cover naming and colour choices, and yesterday's piece on 
Lovart's taste memory
 shows the same idea from the agent side: write your taste down in a form a machine can check.

## References
- [Introducing Vyb - Our First Design Model That Understands Taste](https://cocolabs.ai/blog/introducing-vyb) — Coco Labs (David Zats, Anusha Ramesh)
- [Coco Labs](https://cocolabs.ai/) — Coco Labs
- [New Gemini tools for small business owners](https://blog.google/innovation-and-ai/products/gemini-app/new-tools-small-business-owners/) — Google (Vishnu Sivaji)
- [Fibo 2 is live](https://docs.bria.ai/whats-new/fibo-2) — Bria AI docs
- [Generate Structured Instruction](https://docs.bria.ai/image-editing/editing/generate-structured-instruction) — Bria AI docs
- [Image Edit by Text](https://docs.bria.ai/image-editing/editing/edit-image) — Bria AI docs
- [Bria AI models](https://huggingface.co/briaai) — Hugging Face
- [Qwen-Image-Layered](https://github.com/QwenLM/Qwen-Image-Layered) — QwenLM on GitHub
- [Design tokens for agents](https://siinxu.github.io/ui-resource-hub/blog/design-tokens-for-agents/) — UI Hub