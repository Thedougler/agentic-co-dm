---
status: SUPERSEDED
lever: claude-md
target: CLAUDE.md, utils/scripts/campaign_os_orient.sh
---
**Superseded (2026-07-29):** live haiku-subagent testing showed the mandatory
session-start chain-load this ticket enforced was crowding out compliance
with CLAUDE.md's own routing table — every uncoached test defaulted to or
mis-cited the wrong guardrail doc. User asked for the hook removed outright.
`campaign_os_orient.sh` deleted, its SessionStart registration dropped from
`.claude/settings.json`; llm-wiki/campaign-os now load on their own real
triggers instead (docs/guardrails/WIKI.md WK6, CLAUDE.md's process-engineering
bullet). See docs/history/guardrails-MIGRATION-LOG.md for the full record. Kept below
for history, per git log being the source of truth for anything superseded.

# Mandate llm-wiki + campaign-os + ask-nick as session-start reads (not just campaign-os)

**Gap:** a fresh agent given «you just started a session in this repo, or you're
about to dispatch an ad-hoc general-purpose Agent for project work» previously
only chain-loaded `campaign-os` (per CLAUDE.md line 34 and the
`campaign_os_orient.sh` hook), should also chain-load `llm-wiki` (the design
pattern this whole system is built on) and `ask-nick` (the self-improve loop)
every session and in every ad-hoc subagent dispatch prompt — not just for the
main thread.

**Saves:** an agent operating without `llm-wiki`'s design-pattern context or
`ask-nick`'s self-correct loop working with a partial, less-effective picture
of the project every session; a re-explained "read these skills too" round
trip on every future ad-hoc subagent dispatch.

**RED:** user explicitly requested (via `/flag-the-gap`) that all three skills
be mandatory session-start reads for every agent working in this project.
Scope narrowed after a clarifying question: applies to the main thread
(hook-enforced) and ad-hoc Agent-tool dispatches only — the 10 existing
pre-scoped subagents in `.claude/agents/*.md` (several deliberately
cost/speed-optimized, e.g. haiku-model, single-purpose) keep their current
task-specific skill reads unchanged, by explicit user decision.

**GREEN:** single blind Haiku tester (Read/Grep/Glob only, no Skill/Edit),
given the literal hook TRIGGER line plus CLAUDE.md's Project zone, returned a
plan for both scenarios:
- Scenario A (session start): "Chain-load llm-wiki skill / Chain-load
  campaign-os skill / Chain-load ask-nick skill" — all three present, in
  order, alongside hot.md/index.md.
- Scenario B (ad-hoc subagent dispatch): "A directive to chain-load the three
  skills in order: llm-wiki, then campaign-os, then ask-nick" — confirms the
  dispatch-prompt instruction also carries.
A second independent Haiku tester, given the `hot.md`-missing fallback
TRIGGER line instead, returned the same ordered plan (`Skill(hot-md)` →
`llm-wiki` → `campaign-os` → `ask-nick` → user task), confirming both hook
branches carry all three skills correctly. No unrelated skills were invented
in either run; scope stayed to the three named. Fix spans 2 files (CLAUDE.md
+ campaign_os_orient.sh) with a reworded trigger, which is why 2 independent
testers were run instead of 1 — both came back clean, closing this ticket.
