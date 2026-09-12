# Domain Docs

How engineering skills consume this repo's domain documentation when exploring the codebase.

**The domain is the process, not the campaign.** This repo's product is the campaign-OS system — the session pipeline, the LLM-safe wiki conventions, the skills/hooks/linters that run it. `CONTEXT.md`'s glossary and `docs/adr/` decisions are about that system. Campaign content (`vault/`, including `vault/campaigns/shattered-sea/pcs/` and `vault/episodes/`) is a dogfooding artifact governed by the wiki pipeline (`vault/CLAUDE.md`, `vault/refs/runbook-wiki.md`), not by these domain docs. Campaign terminology and DM rulings live in `vault/srd/rules/rules-glossary.md` and `docs/rulings/`, maintained by the `campaign-domain-modeling` skill.

## Before exploring, read

- `CONTEXT.md` at the repo root, or `CONTEXT-MAP.md` if it exists, pointing to one `CONTEXT.md` per context.
- `docs/adr/` — the ADRs that touch the area you're about to work in.
- `docs/guardrails/PROJECT.md` — this repo's guardrails-kit project-zone rules.

Any of these missing → proceed silently. `domain-modeling` creates them lazily when a term or decision actually resolves.

## Use the glossary's vocabulary

When your output names a domain concept — an issue title, a refactor proposal, a hypothesis, a test name — use the term as `CONTEXT.md` defines it, not a synonym the glossary avoids. A concept missing from the glossary is a signal: either you're inventing language the project doesn't use, or there's a real gap to note for `domain-modeling`.

## Flag ADR conflicts

Output that contradicts an existing ADR is surfaced, never silently overridden:

> *Contradicts ADR-0007 (event-sourced orders) — but worth reopening because…*
