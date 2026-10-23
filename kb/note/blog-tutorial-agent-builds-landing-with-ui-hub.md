# Tutorial: have an agent build a landing page using UI Hub as context

> Six steps from an empty folder to a verified page: load AGENTS.md, search the encyclopedia, pick components, load skills, build, verify in a browser.

Blog post: <https://ui.incidental.site/blog/tutorial-agent-builds-landing-with-ui-hub/>

UI Hub is built to be read by agents: a JSON API, a design encyclopedia with raw Markdown per entry, and an AGENTS.md. This walkthrough shows the loop we use ourselves. Paste the prompts into Claude Code, Cursor, Codex or any agent that can fetch URLs.

## Six steps

- **Load the guide.** "Read https://siinxu.github.io/ui-resource-hub/AGENTS.md and follow it."

- **Search the encyclopedia** for the house style and the specs you need: `/kb/?q=house style`, `/kb/?q=typography`.

- **Pick components** from `/api/resources.json`, filtered by type and licence; prefer open-source libraries you can copy.

- **Load skills** in order: a taste or frontend-design skill first, then accessibility and quality checks.

- **Build** with tokens in CSS variables, one signature effect, real copy.

- **Verify in a browser** at 390px and 1440px, light and dark, and fix what you see before reporting done.

## A prompt you can copy

```
Use UI Hub as design context: read /AGENTS.md, search /kb/ for
"house style", "typography", "colour". Build a landing page for
[product] with shadcn + one Aceternity background. Tokens in CSS
variables, 10-language-ready copy, then screenshot 390/1440 light/dark.
```

## Why this works

Each step replaces a vague instruction with a document the agent can read. The 
Agents guide
 has a one-click copy of this prompt in 10 languages, plus a downloadable skill bundle.

## References
- [UI Hub AGENTS.md](https://siinxu.github.io/ui-resource-hub/AGENTS.md) — UI Hub
- [UI Hub design encyclopedia](https://siinxu.github.io/ui-resource-hub/kb/) — UI Hub
- [AGENTS.md convention](https://agents.md/) — agents.md
- [anthropics/skills](https://github.com/anthropics/skills) — GitHub