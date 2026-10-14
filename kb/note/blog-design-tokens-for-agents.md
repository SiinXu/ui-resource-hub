# Design tokens for agents: the file that makes AI output on-brand

> A machine-readable token file (the W3C DTCG format) plus a short usage note beats any adjective in a prompt. Structure, naming, and how to hand it to an agent.

Blog post: https://siinxu.github.io/ui-resource-hub/blog/design-tokens-for-agents/

Agents follow concrete values far more reliably than descriptions. A design token file turns "clean, premium, a bit playful" into numbers the agent can apply everywhere. The W3C Design Tokens Community Group (DTCG) publishes a vendor-neutral JSON format for this, supported by tools such as Style Dictionary and Tokens Studio.

## A minimal structure

```
{
  "color": { "accent": { "$type": "color", "$value": "oklch(62% 0.17 250)" } },
  "radius": { "md": { "$type": "dimension", "$value": "10px" } },
  "space": { "4": { "$type": "dimension", "$value": "16px" } }
}
```

## Three tiers of naming

- **Primitive:** raw values (`blue-500`, `space-4`).

- **Semantic:** intent (`surface`, `text-muted`, `accent`, `danger`). Agents should mostly use these.

- **Component:** optional overrides (`button-radius`).

## Handing it to an agent

- Export tokens to CSS variables and commit them; tell the agent "never hard-code colours or spacing, use these variables".

- Add a one-page usage note: which token for which job, plus three do/don't pairs.

- Reference both from your AGENTS.md, Cursor rules or skill so every session loads them.

- Verify: grep generated code for raw hex values as a cheap lint.

Our encyclopedia's colour, spacing and type spec digests are written to be pasted into exactly this kind of usage note.

## References
- [Design Tokens Community Group](https://www.w3.org/community/design-tokens/) — W3C
- [Design Tokens Format Module](https://www.designtokens.org/) — DTCG
- [Style Dictionary](https://styledictionary.com/) — Style Dictionary
- [Tokens Studio](https://tokens.studio/) — Tokens Studio