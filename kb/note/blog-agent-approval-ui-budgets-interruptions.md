# Designing approvals for agents that act for people: budgets, previews and when to interrupt

> In one week Walmart announced Agent Profiles with spending limits, Anthropic opened Claude Duet, which asks before it sends, pays, signs or deletes, and 1Password shipped approvals for agent sign-ins. Together they sketch a shared pattern for agent permission UI: what each one shipped, our take, and a checklist for your own product.

Blog post: <https://ui.incidental.site/blog/agent-approval-ui-budgets-interruptions/>

Most agent interfaces still have one permission model: the agent can do everything the person can, because it signs in as them. That worked while agents mostly read and drafted. It stops working the moment they buy, send and sign. In the week of 21 October three launches, from a retailer, a model lab and a password manager, each shipped a different piece of the same answer. Read together, they are the clearest picture yet of what a permission screen for an agent should look like.

## What shipped

- **Walmart Agent Profiles (announced 21 October, launching within a month).** Today an agent shopping on Walmart signs in with the customer's account, so its orders are mixed in with theirs. Agent Profiles give each agent its own profile inside the account, with its purchases listed separately. By default every agent purchase needs approval; the customer can instead allow spending up to a limit such as $50, $100 or $200, and Walmart says it may still ask for approval inside that limit. Profiles can be turned off or deleted at any time. Under the new terms, agents never receive card details, cannot add or change payment methods, and may only use the information a task needs. A beta Agent Gateway connects agents over MCP and, in Walmart's example, helps an agent find your usual milk without handing over your whole shopping history.

- **Claude Duet (research preview, 21 October).** Anthropic's proactive agent sends a morning brief, checks connected apps every few hours rather than continuously, and messages you only when something needs your attention; you can tell it what you want to hear about and how often. It reads, drafts and prepares work on its own, but before it sends a message, makes a payment, signs a document or deletes anything, it shows exactly what it is about to do and waits. Some actions, such as trading securities or moving money between accounts, stay off-limits even with approval, and any connected app can be disconnected. Anthropic says the preview may still misjudge what is urgent and cannot yet show you its browser.

- **1Password for Agents (October).** When an agent hits a sign-in form, 1Password shows a prompt naming which agent is asking and suggesting a login; you approve on your own device, and 1Password fills the form without the credential ever reaching the agent. Its Claude integration goes further: there are no standing approvals, so a new agent session means a new prompt, and released credentials expire with the session.

One early hands-on review of Duet, by Claire Vo and summarised in the FocusHeron 
AI and Designers
 newsletter, adds the human side: a proactive agent needs a deliberate rule for when it may interrupt, and slow responses quickly erode the willingness to work with it in real time.

## Our take

The three launches agree on more than they differ, and the agreement is a design pattern rather than a security feature. Autonomy is not one switch; it is a setting per action type, with four rungs. Some actions are **never** allowed. Consequential ones are **asked every time** by default. Routine ones can run **within a budget** the person chose. Everything the agent did is **visible afterwards** in its own ledger, separate from what the person did. The approval itself has to be a preview of the exact action, not a generic "Allow?" dialog: Duet's "shows you exactly what it is about to do" and 1Password's "which agent is asking, for which login" are the two halves of a good approval card.

The quieter lesson is about attention. A permission model that asks for everything trains people to tap Approve without reading, which is worse than no approval at all. Duet's few-hours check-in and per-topic notification settings, and Walmart's budget tier, both exist to reduce how often the person is asked, so that the remaining questions get read. If your product adds agent actions, design the interruption budget at the same time as the spending budget.

## Checklist: an approval UI for agent actions

- **Give each agent its own identity.** Show its name and icon on every request and on every action in history, never the person's avatar.

- **Classify actions before you design screens.** Read, draft, act within budget, act with approval, never. Write the list down; it is your permission spec.

- **Default consequential actions to "ask".** Sending, paying, signing, deleting and changing account settings start in the ask tier; the person can loosen it later, per agent.

- **Make the approval card a preview.** Show the exact recipient and text, item and price, or file and change, plus who is asking and why. Offer Approve, Edit and Deny, and make Deny as easy to hit as Approve.

- **Budgets in the person's units.** Money per purchase or per week, messages per day, or recipients outside the team. Show the remaining budget on the card and in settings.

- **Keep a separate ledger.** Agent actions get their own list with filters, an undo or return path where one exists, and a one-tap way to pause or remove the agent.

- **Set an interruption rule.** Batch low-stakes items into a brief, interrupt only for blocked or time-critical work, and let people choose topics and frequency.

- **No standing secrets.** Never paste credentials into the agent's context; hand sign-in to a credential manager and expire access with the session.

- **Make the approval accessible.** A blocking approval is an `alertdialog` with a clear title, focus on the safest option, and text a screen reader can read in full.

```
# agent-permissions.yml: a starting spec
agent: "Shopping assistant"
never:    [change_payment_method, move_money, trade]
ask:      [send_message, purchase_over_budget, sign, delete]
budget:   { purchase: "$100 / week", messages: "10 / day" }
auto:     [read, search, draft, add_to_cart]
notify:   { brief: "08:00", interrupt: [blocked, deadline_today] }
ledger:   separate_from_owner
session:  { credentials: via_password_manager, expire: on_end }
```

## How UI Hub helps

The building blocks for this UI already exist. Our post on 
shadcn Trace and AI Elements
 covers the Confirmation and Tool patterns that an approval card can be built from, and 
accessibility in AI-generated UI
 covers focus and dialog roles. For making the agent itself follow your rules while it builds screens like these, see 
linting agents onto your design system
.

## References
- [Making it possible for agents to shop on behalf of customers](https://corporate.walmart.com/news/2026/10/Making-It-Possible-for-Agents-to-Shop-on-Behalf-of-Customers) — Walmart
- [Walmart is inviting AI agents to shop for you](https://www.theverge.com/ai-artificial-intelligence/1015715/walmart-ai-shopping-agents) — The Verge
- [Walmart will let AI agents shop for you, with their own spending limits](https://thenextweb.com/news/walmart-ai-agents-shop-agent-profiles) — The Next Web
- [Walmart AI agent shopping: new controls and spending limits](https://www.digitalcommerce360.com/2026/10/23/walmart-unveils-ai-agent-shopping-controls-spending-limits/) — Digital Commerce 360
- [Introducing Claude Duet](https://claude.com/resources/articles/claude-duet) — Anthropic
- [Get started with Claude Duet](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet) — Claude Help Center
- [Anthropic announces preview of Claude Duet](https://www.cnbc.com/2026/10/21/anthropic-preview-of-claude-duet-personal-ai-agent-take-on-muse-dots.html) — Ashley Capoot, CNBC
- [Use 1Password to sign in to sites with supported agents](https://support.1password.com/1password-for-agents/) — 1Password Support
- [1Password for Agents launches as the trust layer for personal AI agents](https://1password.com/press/2026/october/1password-for-agents-trust-layer-personal-ai-agents) — 1Password
- [About the security of 1Password for Claude](https://support.1password.com/1password-claude-security/) — 1Password Support
- [AI and Designers, issue 2 (25 October 2026)](https://focusheron.com/n/agentic-for-designers/i/iss_974440f090eb494aaff677d12748be1e) — FocusHeron
- [AI Elements](https://ui.shadcn.com/docs/ai-elements) — shadcn/ui
- [Alert and message dialogs pattern](https://www.w3.org/WAI/ARIA/apg/patterns/alertdialog/) — W3C WAI-ARIA APG