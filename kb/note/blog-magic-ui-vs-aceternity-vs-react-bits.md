# Magic UI vs Aceternity vs React Bits: compare the licence before the effects

> Three copy-paste libraries of animated React components, all installed through the shadcn CLI, all free to start. As of 16 November 2026 they differ most in what you may do with the code: MIT, a free tier plus a paid licence, and MIT with the Commons Clause. Component counts, stack, install commands, paid tiers and how we would choose, with every figure linked to its source.

Blog post: <https://ui.incidental.site/blog/magic-ui-vs-aceternity-vs-react-bits/>

Magic UI, Aceternity UI and React Bits are the three names that come up whenever someone asks for “animated components for a landing page”. All three hand you source code rather than a package you import, all three now install through the shadcn CLI, and all three have a free tier. That makes them easy to confuse and easy to mix in one project. We checked each official site, GitHub repository and licence on 16 November 2026. The effects overlap a lot. The terms do not, and the terms are what you cannot change later.

## At a glance (16 November 2026)

- **Magic UI.** “150+ free and open-source animated components and effects built with React, Typescript, Tailwind CSS, and Motion”, described as a “perfect companion for shadcn/ui”. Licence: MIT. The GitHub repository has about 23,300 stars. Install: `pnpm dlx shadcn@latest add @magicui/globe`, with “the exact same installation process as shadcn/ui”. Paid: Magic UI Pro, listed at $199 once for 8 templates and 50+ premium components.

- **Aceternity UI.** “200+ production-ready components, blocks, templates, landing pages and micro-interactions built with React, Tailwind CSS and Motion”. The free section lists 118+ components; the pricing page and FAQ round this to 100+ and say the free tier can be used in personal and commercial projects. Install: `npx shadcn@latest add @aceternity/3d-card`, or through its MCP registry. Paid: All-Access, listed on 16 November at $169 for one year or $199 for lifetime (regular prices $249 and $299), and $1,590 for a team of up to 10. The component library itself has no public open-source repository that we could find; the paid items come under the Aceternity Licence published on the site.

- **React Bits.** “215+ free animated components and backgrounds for React”, in five categories: 33 text animations, 38 animations, 48 components, 34 micro-interactions and 63 backgrounds. Every component comes in four flavours: JavaScript or TypeScript, styled with plain CSS or Tailwind. Licence: MIT plus the Commons Clause. The GitHub repository has about 52,000 stars. Install: `npx shadcn@latest add @react-bits/SplitText-TS-TW`, where the suffix picks the flavour, or the same file through jsrepo. Paid: React Bits Pro, which its README describes as 230 animated components, 300 page sections, 300 app UI blocks, 15 templates and 20 agent skills.

## The licence is the real difference

Copy-paste code becomes your code, so the licence decides what you may do with it afterwards. Here the three libraries take three different positions.

- **Magic UI is plain MIT.** You can use, change, ship and even redistribute the components, as long as the copyright and licence notice travel with them. This is the most permissive of the three.

- **React Bits is MIT with the Commons Clause.** Its LICENSE.md allows any use, commercial included, but you may not sell, sublicense or redistribute the components themselves, alone, in a bundle or as a port. Because of the added clause, GitHub reports the licence as “Other” rather than MIT, and it is not an open-source licence in the OSI sense. Using a React Bits background on a client site is fine; selling a template or a component kit built mainly from React Bits is not.

- **Aceternity UI separates free and paid.** Its FAQ says the free components can be used in personal and commercial projects. The paid blocks and templates are covered by the Aceternity Licence: unlimited end products for yourself or clients, but no redistribution of source files and no reselling of templates or derivative products on any marketplace.

The practical rule: if you build sites and apps, all three are usable. If you build things that other developers will install, such as a starter kit, a theme, a template for sale or your own component library, only Magic UI lets you include the components without asking.

## Stack and install: closer than they look

All three target React, and Magic UI and Aceternity both name Tailwind CSS and Motion as their stack. React Bits is the one to pick if your project does not use Tailwind or TypeScript, because each component also ships as plain JavaScript with plain CSS. Since all three publish shadcn registries, one `components.json` can pull from all of them, and the shadcn MCP server lets a coding agent search and add components for you. Aceternity and React Bits both promote that agent route on their own pages.

The flip side of copy-paste is that updates do not arrive by themselves. Whatever you add is a file in your repository; when the library fixes a bug, you re-run the add command and review the diff. Keep a list of which components came from where.

## How we would choose

- **You already use shadcn/ui and want polished marketing sections:** start with Magic UI. Same CLI, same conventions, and the MIT licence never gets in the way.

- **You want a whole landing page fast and are willing to pay:** look at Aceternity. Its strength is the paid blocks, templates and full pages, not only single effects.

- **You want striking text effects and full-section backgrounds, or your project is plain JavaScript and CSS:** React Bits has the largest free catalogue and the most variants. Just do not resell it.

- **You mix them:** fine for a product, but check the motion budget. Three libraries’ worth of effects on one page is the fastest way to a slow, noisy page.

UI Hub indexes official demo cards from all three: 45 from Magic UI, 34 from Aceternity UI and 30 from React Bits as of 15 November 2026. For each library on its own, read our 
Magic UI deep dive
 and 
Aceternity UI deep dive
.

## Checklist before you copy a component

- **Read the licence file, not the badge.** Note whether you may redistribute the code.

- **Write down the source.** Library, component name and date added, in a comment or a NOTICE file.

- **Check dependencies.** Some effects pull in Motion or WebGL libraries; confirm the bundle cost.

- **Respect reduced motion.** Wrap each effect so `prefers-reduced-motion` turns it off or down.

- **Give loops a pause.** Animations that run longer than five seconds need a way to stop them (WCAG 2.2.2).

- **Re-check prices and counts.** The figures above are from 16 November 2026 and change often.

Related on UI Hub: 
the best animated React component libraries of 2026
 and 
motion that feels right
.

## References
- [Magic UI home page](https://magicui.design/) — magicui.design
- [Magic UI installation](https://magicui.design/docs/installation) — Magic UI docs
- [magicuidesign/magicui (MIT licence)](https://github.com/magicuidesign/magicui) — GitHub
- [Aceternity UI home page and FAQ](https://ui.aceternity.com/) — ui.aceternity.com
- [Aceternity UI pricing](https://ui.aceternity.com/pricing) — ui.aceternity.com
- [Aceternity UI licence](https://ui.aceternity.com/licence) — ui.aceternity.com
- [3D Card Effect: installation](https://ui.aceternity.com/components/3d-card-effect) — Aceternity UI docs
- [React Bits home page](https://reactbits.dev/) — reactbits.dev
- [React Bits installation](https://reactbits.dev/get-started/installation) — React Bits docs
- [DavidHDev/react-bits README](https://github.com/DavidHDev/react-bits) — GitHub
- [React Bits LICENSE.md (MIT + Commons Clause)](https://github.com/DavidHDev/react-bits/blob/main/LICENSE.md) — GitHub · DavidHDev
- [Commons Clause](https://commonsclause.com/) — commonsclause.com
- [The MIT License](https://opensource.org/license/mit) — Open Source Initiative
- [shadcn MCP server](https://ui.shadcn.com/docs/mcp) — shadcn/ui docs
- [Understanding SC 2.2.2: Pause, Stop, Hide](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html) — W3C WAI