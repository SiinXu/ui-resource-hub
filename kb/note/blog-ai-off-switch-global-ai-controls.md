# Design the AI off switch: what Flodesk and Firefox teach about global AI controls

> On 17 November 2026 Flodesk moved its AI email designer into the main product and shipped, alongside it, one toggle that turns AI off across the whole account. Firefox has offered a similar “Block AI enhancements” switch since version 148. An off switch looks like a settings detail, but it is really a statement of scope, and getting that scope right is design work. What the two products do, our take on what makes an off switch trustworthy, plus a build checklist and an agent prompt.

Blog post: <https://ui.incidental.site/blog/ai-off-switch-global-ai-controls/>

On 17 November Flodesk, an email marketing platform for small businesses and creators, brought **Flodesk Studio**, its prompt-to-create email designer, inside the main product. The same release added what the company calls an **AI kill switch**: in Account settings → AI, one toggle turns off every AI feature in the account, including prompt-to-create, subject line generation and “refine text”. With it off, the Prompt to Create option no longer appears when you start a new email, and you can turn it back on at any time. The announcement is blunt about why: most companies have refused to build this, or their off switch does not fully turn AI off.

Flodesk is not the first. Firefox 148, which rolled out on 24 February 2026, added an **AI controls** section to desktop settings with a single “Block AI enhancements” switch plus per-feature controls. And on the same day as Flodesk, SNO, a website platform for student newsrooms, launched AI design widgets with a different kind of promise: the AI never sees your stories or photos, because the code is generated outside SNO and pasted in by you. Three products, three ways of telling users where AI stops. For anyone designing an AI-enabled product, the off switch is becoming part of the interface, not an afterthought in a legal page.

## What the two switches actually do

- **Flodesk: one account-wide toggle.** It covers the three generative features by name. The manual drag-and-drop builder stays fully usable, and Flodesk’s help centre even has a newsletter guide written for people who work with AI turned off. The help article also states that member content is not used to train AI models, by Flodesk or by Anthropic, the provider behind the feature.

- **Firefox: a master switch with per-feature overrides.** “Block AI enhancements” hides current 
and future
 AI features and the pop-ups that promote them. Each feature (translations, alt text in PDFs, AI tab grouping, link previews, the sidebar chatbot) also has a dropdown with three states: Available (you can see and use it), Enabled (you opted in) and Blocked (hidden and unusable). You can block everything and still keep, say, translations. Mozilla says the choices persist across updates.

- **Firefox is explicit about what the switch does not cover.** Its guide separates newer AI-enhanced features from the ranking and classification systems browsers have used for years, and its support page notes that extensions calling third-party AI services are not stopped by the switch.

## Our take: an off switch is a scope statement

A toggle labelled “AI” only earns trust if the user can predict exactly what changes when they flip it. That turns a one-line setting into four design decisions.

**First, name the scope, both ways.** List what turns off, and say what does not. Flodesk lists its three features; Firefox draws the line between generative features and older machine learning. “AI” on its own is too vague a label: users will assume spam filters, search ranking or autocomplete are included unless you tell them otherwise. Microsoft’s 2019 Guidelines for Human-AI Interaction already had a rule for this (“provide global controls”); what has changed is that users now go looking for the switch.

**Second, off means gone, not greyed out.** Both products remove the entry points rather than disabling them, and Firefox also stops the promotional pop-ups. A sparkle button that is still visible but dead, or a “Try AI” banner that comes back next week, tells the user the switch is cosmetic. The 
future
 part matters too: a switch that only covers today’s features is broken by your next launch.

**Third, the no-AI path must be a complete product.** A kill switch is only honest if everything still works without it. Flodesk can offer one because its full builder predates Studio. If your onboarding, empty states or templates now assume the AI writes the first draft, turning AI off will leave people staring at blank screens. Test the product with the switch off as a first-class flow, with screenshots, like any other state.

**Fourth, keep the feature switch and the data promise separate.** “Does AI appear in my product?” and “What does the AI see, and is it used for training?” are different questions. SNO answers the second one without offering a toggle at all; Flodesk answers both in separate places. Users will read a toggle as an answer to whichever question worries them, so put a one-line data statement right under it.

Finally, it is a toggle, so the old toggle rules apply. Nielsen Norman Group’s guidance is that switches should take effect immediately, with clear labels. If turning AI off needs a save button, a reload or a confirmation dialog, use a different control or fix the flow.

## How to build one

- **Inventory every AI touchpoint.** Buttons, menu items, inline suggestions, generated defaults, onboarding steps, emails and promos. Put them in one registry with a feature id and a one-line plain-language name.

- **Gate them all with one flag, plus overrides.** A global value (on / off) and, if you have several features, a per-feature state that can re-enable one while the rest stay off. New features must register before they ship, so the switch covers the future by default.

- **Remove, don’t disable.** When off, entry points and promos disappear and layouts close the gap. No disabled sparkle buttons, no upsell banners.

- **Design the no-AI empty states.** Templates, blank-canvas guidance and manual tools should carry the user where the AI used to.

- **Persist and scope it.** Save the choice server-side so it survives updates and follows the user across devices. Decide whether it is per user, per workspace or set by an admin, and show who set it.

- **Write the labels.** Title, a sentence listing what turns off, a sentence on what stays, and a link to the data policy. Apply immediately and confirm with a quiet inline message.

## Checklist before you ship an AI switch

- Does the description list every feature it turns off, and name what stays (search, ranking, spam filtering)?

- With it off, are all AI entry points and promotional messages gone, on web, mobile and in emails?

- Will a feature launched next month respect the switch without extra work?

- Can someone block everything but keep one feature they like?

- Does every core task still work end to end with AI off, including onboarding and empty states?

- Does the choice survive app updates, sign-out and a new device?

- Is there a plain statement next to the switch about what data the AI sees and whether it trains on it?

- Do light, dark and narrow mobile layouts look finished with the AI elements removed?

```
# Paste this into your design or coding agent
Add a global "AI features" setting to this app.
- First list every AI touchpoint you can find (buttons, menus,
  suggestions, generated defaults, onboarding, promos) with file paths.
  Wait for my confirmation of the list.
- Create one registry of AI features (id, plain-language name) and gate
  every touchpoint through it: global on/off plus per-feature override.
  Any new AI feature must register to render.
- When off, remove entry points and promos; do not show disabled buttons.
  Fill the gap with the manual path or a non-AI empty state.
- Settings copy: title, one sentence on what turns off, one on what
  stays, and a link to the data policy. Apply immediately, no save button.
- Persist the choice server-side. Then screenshot the main flows with AI
  on and off, light and dark, at 1280px and 390px.
```

Related reading on UI Hub: 
Approval UI for agents
, 
Accessibility in AI-generated UI
 and 
Native popovers and dialogs for AI UI
.

## References
- [Flodesk Brings Studio Inside Its Platform With a Whole New Way to Create Emails](https://www.prnewswire.com/news-releases/flodesk-brings-studio-inside-its-platform-with-a-whole-new-way-to-create-emails-302941983.html) — Flodesk via PR Newswire
- [Create an email from a prompt in Flodesk (incl. how to turn off AI features)](https://help.flodesk.com/en/articles/14449281) — Flodesk Help Center
- [How to send a newsletter in Flodesk](https://help.flodesk.com/en/articles/4482113) — Flodesk Help Center
- [Official information about Flodesk (AI)](https://flodesk.com/ai-information) — Flodesk
- [AI controls are coming to Firefox](https://blog.mozilla.org/en/firefox/ai-controls/) — Ajit Varma · Mozilla blog
- [How to turn off AI features in Firefox, or choose the ones you want](https://blog.mozilla.org/en/firefox/how-to-use-ai-controls/) — Mozilla blog
- [Firefox AI controls](https://support.mozilla.org/en-US/kb/firefox-ai-controls) — Mozilla Support
- [A new way to design your SNO site, on your terms](https://snosites.com/news-announcements/2026/11/17/a-new-way-to-design-your-sno-site-on-your-terms/) — SNO Sites
- [Provide global controls (Guideline 17)](https://www.microsoft.com/en-us/haxtoolkit/guideline/provide-global-controls/) — Microsoft HAX Toolkit
- [Guidelines for Human-AI Interaction](https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/) — Saleema Amershi et al. · Microsoft Research (CHI 2019)
- [Toggle-Switch Guidelines](https://www.nngroup.com/articles/toggle-switch-guidelines/) — Alita Kendrick · Nielsen Norman Group