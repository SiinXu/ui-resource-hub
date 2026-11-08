# Twombly: pin comments on the agent’s frames so it iterates on the team’s feedback

> On 7 November 2026 Jaytel showed Twombly on Hacker News: a localhost canvas where coding agents place each design version as a live frame, and a Share link adds live cursors, comments and voice huddles the agent can read. How that differs from Dessn, Doop and Cursor Live Apps, plus a checklist before you share.

Blog post: <https://ui.incidental.site/blog/twombly-shared-canvas-team-comments/>

On 7 November 2026, software designer Jaytel posted a Show HN for **Twombly**: give your coding agent a skill, and it places each design version on one infinite canvas as a live frame. Click Share and the team gets a single link with live cursors, following, comments pinned to frames, and voice huddles. The loop he stressed is what happens next: the agent can read those comments and see which frame someone is looking at, so the next pass is steered by the team’s feedback, not only by the person who typed the prompt.

The npm package `twombly`, published by Materic, Inc. on 5 November and updated through version 0.4.12 on 7 November, matches that description. It works with Claude Code, Codex, Cursor, and any agent that can run a command, in any framework and any repo. You can install the skill with `npx skills add materic-inc/twombly-skill -g -y`, or run `npx -y twombly@latest guide` and hand the guide to the agent. The homepage, the project’s `llms.txt`, and the skill repository on GitHub all tell the same story. The interesting design claim is smaller than “another AI canvas”: explorations become addressable frames a group can stand around.

## What a frame is, and what stays local

- **A frame is a folder of static files** that should run with no server and no network: a Vite, Next.js, SvelteKit or Astro build, one component bundled with mock data, a frozen capture of a running page, or a picture.

- **Nothing goes online until a person clicks Share.** The canvas opens on localhost. Twombly’s own docs say the agent never shares unless asked.

- **Gates check every frame** for secrets, outside requests and server code, locally and again in the cloud, before it is placed.

- **The agent has two machine-readable signals:** `twombly context` returns what the person is looking at; `twombly comments` returns the feedback left on the frames. Output is JSON.

- **Several agents can share one canvas**, and a folder can hold any number of named canvases. Typical commands include `twombly init --name "Notification Explorations"` and `twombly add ./dist --title "V1" --width 1280 --height 800`.

Sharing has a clearer privacy story than most prototype tools bother to write down. Twombly’s privacy page (updated 7 November) says an unshared canvas stays on your computer; once you share, anyone with the link can see the canvas, its comments and who is present, and can join the huddle. Links are hard to guess and search engines are asked not to index them, but they are not private. Huddle audio passes through the host and is not recorded or stored. Materic says it does not use canvases to train AI models. Account data for shared work comes from Google sign-in (name, email, picture and account ID).

## Our take: this is annotate-don’t-describe, made multiplayer

A week of canvas news has been circling the same problem. 
Dessn, Doop and Figma code layers
 let people and agents design on something that actually runs. 
Cursor Live Apps
 take a different cut: get a useful internal UI off localhost and behind SSO. Twombly is neither a production runtime nor a hosted app. It is a review surface for versions. That is the gap many agent workflows still leave as a chat scroll—“try it again, but tighter”—with no one else able to point at the frame they mean.

The move that matters is making each exploration 
addressable
. A comment pinned to “V2 — denser table” is a different artifact from a paragraph in a prompt. Combined with `twombly context`, the agent can see which frame a teammate is looking at. That is the same instinct as 
annotate, don’t describe
, except the note lives where the whole team can add it, and the agent is expected to read it back.

Treat the frames as what they are. They are static folders—builds, captures, pictures—not your connected app. They are good for comparing layout, type, density and empty states; they are a weak place to judge auth, live data or anything that needs a server. Dessn (or a Figma code layer wired to the repo) is still the better canvas once you have picked a direction and need the real components. Cursor Live Apps are still the better path when the pain is “this demo dies on my laptop.” Twombly is for the messy middle: several directions on the table, several people talking, one agent that should hear all of them.

Two caveats follow from the docs themselves. First, a shared link is public to anyone who receives it; do not put customer data, unreleased work you would not email, or anything the gates might miss, on a frame you then Share. Second, the product is days old—the package appeared on 5 November—so command names and defaults may move. Read `twombly help` on the version you installed rather than memorising a blog post.

## Checklist before you share a canvas

- **Name the canvas after the question.** “Notification density” beats “Explorations”.

- **Init on localhost first.** Install the skill, run the guide, and do not click Share until you have looked at every frame yourself.

- **Add frames from real builds with mock data.** Include empty, loading, error and a long string—not only the happy-path screenshot.

- **Title frames as directions, not as winners.** “V1 dense table / V2 editorial cards,” never “Final”.

- **Keep tokens and components in the repo the agent builds from.** A pretty frame that invents a second accent is not an option; it is drift.

- **Read the gate results.** Secrets, outside requests and server code should fail closed. If something slips through, do not share.

- **Treat the Share link as public.** Anyone with it can see comments, presence and the huddle. Send it the way you would send a prototype link you are willing to forward.

- **Comment on the frame you mean, with something checkable.** “Tighten the header 8px and drop the second accent” beats “make it cleaner.”

- **Have the agent read before it rebuilds.** Run `twombly context` then `twombly comments`, then one change set—not a fresh prompt that ignores the board.

- **When you pick a direction, leave the exploration canvas.** Take the winner into the real repo, a code-backed canvas, or a pull request. Twombly is not the source of truth.

```
# Paste this to your coding agent (after the skill is installed)
Put this project's main screens on a Twombly canvas named "Notification density".
Add three frames from a static build with mock data:
  V1 dense table — our current tokens, 8px density
  V2 editorial cards — same tokens, more whitespace
  V3 split inbox — list + preview, empty + error states included
Do not click Share. Do not invent a second accent or a new typeface.
After I (or the team) comment, run `twombly context` and `twombly comments`
and change only what those notes ask for. Rebuild the same frame titles.
When we pick a winner, stop exploring and open a PR in this repo.
```

## When Twombly is the wrong surface

Skip it when you already know the direction and need to edit the running product—use a code-backed canvas or a pull request. Skip it when the deliverable is a hosted internal tool behind SSO: that is Live Apps territory. Skip it when the only reviewer is you and a screenshot thread would do. Use it when several people need to stand around several live versions, and the agent should iterate on what they marked, not on a recap you typed from memory.

Related on UI Hub: 
design on running code
, 
Cursor Live Apps
, 
annotate, don’t describe
, and 
design skills for Claude and Cursor
.

## References
- [Twombly: a canvas for your agent’s explorations](https://twombly.app/) — Twombly
- [Twombly llms.txt](https://twombly.app/llms.txt) — Twombly
- [Privacy (updated 7 November 2026)](https://twombly.app/privacy) — Twombly / Materic, Inc.
- [twombly on npm](https://www.npmjs.com/package/twombly) — Materic, Inc.
- [materic-inc/twombly-skill](https://github.com/materic-inc/twombly-skill) — GitHub
- [Show HN: Twombly – A collaborative canvas for your agent’s design explorations](https://news.ycombinator.com/item?id=50405205) — Hacker News (jaytel)
- [twombly skill listing](https://www.skills.sh/materic-inc/twombly-skill/twombly) — skills.sh