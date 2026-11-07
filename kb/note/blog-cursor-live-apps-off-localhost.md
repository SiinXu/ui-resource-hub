# Cursor Live Apps: get the UI off localhost before the demo dies

> On 5 November 2026 Cursor let cloud agents scaffold, host, and publish a live app with Postgres, SSO, and security checks. Why that changes the design loop, how it compares to Lovable and v0, and a checklist before you hit publish.

Blog post: <https://ui.incidental.site/blog/cursor-live-apps-off-localhost/>

On 5 November 2026 Cursor’s changelog shipped **Build Live Apps**: tell a cloud agent you want an app, and it scaffolds the web app, spins up Postgres when needed, puts authentication behind Cursor SSO, provisions hosting, and hands you a shareable URL after you pick a domain. The company’s own framing is blunt—agents made writing code cheap, but most apps still die on localhost. The day after, on 6 November, Cursor also shipped Voice Chat with Agents (Grok Voice) so you can talk through a change while work is running; useful as a design-loop companion, not the main story here.

Coverage from The New Stack (Paul Sawers, 6 November) places the release next to Lovable and Replit’s prompt-to-app turf, and notes Vercel’s public reply that the hosting path sits on **Vercel for Platforms**—deploy without each teammate opening their own Vercel account or wiring deploy config by hand. Availability is on paid plans with cloud agents enabled. That is the product. The design problem underneath is older: demos that only run on one laptop are not products.

## What shipped, and how it works

- **Cloud agent, not a localhost wizard.** You kick off a cloud agent and say you want an app; Cursor scaffolds, optionally provisions Postgres, configures auth behind Cursor SSO, and hosts it.

- **Secrets on demand.** If the app must talk to your systems (for example a warehouse), Cursor asks for the secrets it needs instead of inventing them.

- **Security checks before go-live.** On publish, deterministic and agentic checks look for common failures such as secrets in app files. Failures block the ship until the agent can fix them and you explicitly publish.

- **Share scope is a product decision.** After checks pass you get the live URL; share with people, groups, or the whole team behind Cursor sign-in. On individual plans you can also share publicly. Team admins can see apps and secrets, add review rules, approve blocked publishes, and unpublish.

- **Repos and git.** Apps can come from new or existing repos on Cursor Origin and GitHub; other providers such as GitLab are listed as coming soon. Cursor also notes you can provision an API key so a script or Grok Bot can call the app.

Cursor’s own examples lean internal: ops tools, customer multimedia decks, onboarding, sales dashboards, engineering-service portals. That is a clue. Live Apps are strongest when “share with the team behind SSO” is the point, not when you need a public brand site with a long design history.

## Our take: treat Live Apps like an internal product surface

The design problem moved from **“generate a screen”** to **“what ships past localhost”**. A pretty preview that only you can open is still a localhost demo with better lighting. Live Apps collapse scaffold → host → auth → share into one publish path; that is useful, and it is also where taste and security both get decided by default if you do not decide first.

Lock tokens and components 
before
 the agent scaffolds. A cloud agent that has never seen your Button, radius, or type scale will invent a second UI dialect the moment Postgres comes up. Put a short design file (tokens, one accent, density, never-list) in the repo the agent reads, the same way you would for any coding agent. Decide auth and share scope 
before
 you hit publish: team-only behind SSO is a different product from a public link on an individual plan. Treat the security checks as a gate, not a vibe—The New Stack reminds readers that Semafor previously reported Replit employees finding sensitive exposure in a sample of Lovable-built apps, after which Lovable said it added further pre-publish checks. Cursor’s checks are addressing that class of failure; they are not a substitute for reviewing what the app can actually reach.

Know when adjacent tools still fit better. **v0** stays the component-oriented path: prompt into shadcn/Tailwind you pull into an existing repo, with Design mode and design-system hooks when the deliverable is UI inside code you already ship (see v0’s docs). **Lovable** remains a dedicated prompt-to-app surface with its own changelog cadence—recent entries such as GPT Image models for in-app AI features (6 November) and “Dreaming” memory tidy-ups (4 November) show it is still iterating as a full product builder, not a side feature of an IDE. Replit-style environments still win when the whole collaborative runtime is the product. Live Apps win when your team already lives in Cursor and the app’s natural home is “behind our SSO, shareable tomorrow”.

## Checklist before you hit publish

- **Write the surface brief first.** Audience (team / group / public), one job the app does, and a never-list for UI chrome.

- **Lock tokens and components in the repo.** Radius, type, accent, your Button/Card—before the scaffold, not after the first share link.

- **Name the data boundary.** Which secrets, which warehouse tables, which environments. Do not paste production keys into a chat because the agent asked politely.

- **Choose share scope on purpose.** SSO teammates vs public. Individual-plan public links are a different threat model from internal ops tools.

- **Read every failed security check.** Fix or accept with admin override only after a human understands the finding. Do not treat “agent said it fixed it” as a merge.

- **Click the live URL like a stranger.** Empty, loading, error, mobile width, and sign-out. Localhost habits hide all four.

- **Decide ownership.** Who can unpublish, who rotates secrets, which admin sees the app list—before the third teammate bookmarks it.

- **Pick the right tool if Live Apps are wrong.** Components for an existing React app → v0. Open-ended public product with Lovable’s own stack → Lovable. Cursor-native internal tool with SSO → Live Apps.

```
# Live Apps publish brief (paste into the cloud agent first)
Surface:   internal ops tool for desk seating + event registration
Audience:  whole team behind Cursor SSO (not public)
Stack:     reuse our Button/Card; tokens in styles/tokens.css
Data:      read-only seat map from warehouse; ask before any write secret
Auth:      Cursor SSO only; no anonymous link
Never:     hard-coded API keys, second accent colour, emoji icons
Gate:      stop on any security-check failure; I review before Publish
Companion: Voice Chat OK for iteration talk-track; publish stays a click I make
```

## When not to use Live Apps

Skip them when the deliverable must merge into a mature design system with PR review as the only ship path—v0 or a hand PR still fit better. Skip them when you need Lovable’s (or Replit’s) full product surface and you are not standardising on Cursor. Skip them for customer-facing marketing sites that need brand art direction the agent has never seen. Use them when the pain is real: a useful internal UI that would otherwise die on someone’s laptop between the standup and the demo.

Related on UI Hub: 
Lovable and Bolt
, 
v0 to shadcn
, 
prompt-to-UI tools compared
, and 
annotate, don’t describe
 for iterating on a running preview.

## References
- [Build Live Apps in Cursor (5 Nov 2026)](https://cursor.com/changelog/build-live-apps) — Cursor Changelog
- [Voice Chat with Agents (6 Nov 2026)](https://cursor.com/changelog) — Cursor Changelog
- ["Most apps never make it off localhost": Cursor takes on Lovable and Replit with fully managed app deployment](https://thenewstack.io/cursor-ai-app-deployment/) — Paul Sawers / The New Stack
- [Lovable changelog](https://docs.lovable.dev/changelog) — Lovable
- [What is v0?](https://v0.app/docs) — v0 by Vercel
- [v0 by Vercel](https://v0.app/) — Vercel