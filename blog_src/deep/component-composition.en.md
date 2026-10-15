The old model of a component library was a styled npm package: you installed it, then fought its styles with overrides and `!important`. shadcn/ui flipped that. Behaviour and accessibility come from headless primitives such as Radix, styling comes from Tailwind classes, and the component source is copied into your repository, where you own it. This post explains why that composition model suits AI agents unusually well, how to structure the layers, and the patterns that keep generated code maintainable.

## Three layers, three owners

Think of your UI in three layers, each with a different rate of change and a different owner:

1. **Primitives** — headless, accessible behaviour: focus management, keyboard handling, ARIA wiring, portals. Radix Primitives, React Aria and Ark UI live here. You rarely edit them.
2. **Your kit** — styled components built on primitives: `Button`, `Dialog`, `Select`, `Card`. This is what shadcn/ui gives you as source. You edit it occasionally, when the design system changes.
3. **Blocks and pages** — compositions of kit components: a pricing section, a settings form, a dashboard header. This changes every week.

Brad Frost's atomic design described a similar split years ago (atoms, molecules, organisms, templates, pages). The practical rule for AI work is simple: **let agents work mostly at the block layer, carefully at the kit layer, and almost never at the primitive layer.**

## Why this suits agents

- **Visible context.** Code in your repo can be read. An agent asked to "add a destructive variant to Button" can open `button.tsx`, see the existing variants and follow the pattern. With a closed npm package it can only guess at props.
- **Small surfaces.** Compound components split one complex widget into parts with narrow responsibilities, so edits are local and predictable.
- **Registries.** A registry lets any project install the same component with one command, so an agent building a new app reuses your kit instead of writing a fresh one.

## Pattern 1: compound components

A compound component exposes parts that share state through context, instead of one component with forty props. Compare:

```tsx
// monolith: every new need becomes another prop
<Dialog title="Delete project" description="This cannot be undone."
  confirmLabel="Delete" cancelLabel="Cancel" danger showClose
  onConfirm={remove} footerAlign="end" />

// compound: parts you can rearrange, omit or extend
<Dialog>
  <DialogTrigger asChild><Button variant="outline">Delete</Button></DialogTrigger>
  <DialogContent>
    <DialogHeader>
      <DialogTitle>Delete project</DialogTitle>
      <DialogDescription>This cannot be undone.</DialogDescription>
    </DialogHeader>
    <DialogFooter>
      <DialogClose asChild><Button variant="ghost">Cancel</Button></DialogClose>
      <Button variant="destructive" onClick={remove}>Delete</Button>
    </DialogFooter>
  </DialogContent>
</Dialog>
```

The compound version is longer, but every part is obvious, and adding a checkbox ("also delete backups") means inserting one element, not designing a new prop.

## Pattern 2: `asChild` instead of wrapper soup

Radix's `asChild` prop merges a primitive's behaviour into its child element instead of rendering an extra DOM node. `<DialogTrigger asChild><Button/></DialogTrigger>` gives you one `<button>` with the trigger's ARIA attributes and event handlers, not a button nested inside another button. Nested interactive elements are one of the most common accessibility bugs in generated code, so tell your agent to use `asChild` whenever it wraps a kit component in a primitive part.

## Pattern 3: variants as data

shadcn/ui components describe styling options with class-variance-authority. Variants become a small, readable table instead of conditional class strings scattered through JSX:

```tsx
const buttonVariants = cva(
  "inline-flex items-center justify-center rounded-md text-sm font-medium focus-visible:outline-none focus-visible:ring-2 disabled:opacity-50",
  {
    variants: {
      variant: {
        default: "bg-primary text-primary-foreground hover:bg-primary/90",
        outline: "border border-input bg-background hover:bg-accent",
        destructive: "bg-destructive text-destructive-foreground hover:bg-destructive/90",
      },
      size: { sm: "h-8 px-3", md: "h-9 px-4", lg: "h-10 px-6" },
    },
    defaultVariants: { variant: "default", size: "md" },
  }
);
```

Agents edit tables like this reliably. Ask for a new variant and you get one new line, using your existing token classes.

## A step-by-step workflow for adding a block

1. **Inventory first.** Ask the agent to list which kit components the new block needs and which are missing.
2. **Add missing kit pieces deliberately.** Install them from the shadcn registry or your own, then review them once. Do not let a block quietly invent its own button.
3. **Compose the block** only from kit components and layout utilities. No raw `<div onClick>`.
4. **Check states and keyboard.** Tab through the block. Open and close every popover with the keyboard. Check focus returns to the trigger.
5. **Promote repeats.** If the same composition appears in three blocks, promote it into the kit with a name.

## Pitfalls

- **Editing primitives to fix styling.** Styling belongs in the kit layer. Forking a primitive loses upstream accessibility fixes.
- **Prop explosion in the kit.** If `Card` has 15 boolean props, it wants to be a compound component.
- **Duplicated kits.** Agents happily generate a second `Button` in a feature folder. Search for duplicates in review.
- **Mixing primitive libraries.** Radix for dialogs and another library for popovers means two focus-management models. Pick one per project where possible.
- **Losing the source of truth.** Once copied, components drift from upstream. Keep a note of which upstream version you started from.

## Questions we get

**Should we use shadcn/ui or a packaged library like MUI?** If you want agents to edit components and you care about owning the look, source-in-repo kits are easier. If you want upstream updates with no maintenance and accept the library's look, a packaged library is fine. Mixing both in one product is the expensive option.

**How do we stop agents from editing primitives?** Say it in AGENTS.md, keep primitives in a clearly named folder, and add a CODEOWNERS rule or a CI check that flags changes there. Agents follow folder conventions well when they are written down.

**When should a block become a kit component?** When it appears in three places, has a clear name, and its variations can be described as a short variants table. Before that, duplication is cheaper than the wrong abstraction.

**What about non-React stacks?** The same three layers apply. Vue and Svelte have headless primitive libraries too, and the rule "agents compose blocks, carefully edit the kit, leave primitives alone" does not depend on the framework.

## Our take

The composition model is the reason shadcn-style kits became the default target for AI UI tools: the source is local, the parts are small and the variants are data. Keep the three layers explicit in your folder structure, tell your agent which layer it is allowed to touch, and most "AI made a mess of my components" problems disappear.

## Checklist

- Folders reflect primitives / kit / blocks
- Agents compose blocks only from kit components
- Compound components instead of many-prop monoliths
- `asChild` used when a primitive part wraps a kit component
- Variants defined as data (cva or similar)
- Keyboard and focus checked on every new block
