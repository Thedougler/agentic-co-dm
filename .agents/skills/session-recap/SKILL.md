---
name: session-recap
description: >-
  Write the player-safe narrative session recap only: propose and file
  wiki/journal/sessions/<campaign-slug>/<NN>/Session-<NN>-Recap.md (type: recap).
  Use after play for wrapup / post-session / “what happened” / recap for players.
  Not for durable DM session logs, canon surgery, clocks, entity filing, or world-tick.
---

# Session recap (narrative only)

Nick standing (2026-09-14): post-session narrative write-up is **just a recap — purely narrative**. `session-wrapup` is retired; this skill is the sole owner.

## Work gate

Show a chat proposal first. Write the wiki recap only after DM accept (FR-019). Reject leaves no page. Follow `docs/agents/work.md`. Players see nothing until the DM accepts and presents.

## HARD: entity-before-spoken + dm-facing-explicit

Follow AGENTS.md **HARD: entity-before-spoken** and **HARD: dm-facing-explicit** (Nick 2026-09-14). Recap narration stays player-safe but grounded in named entities; **Wiki facts** (DM-facing) name concrete owners/stakes — no coy “something happened” bullets without who/what.


Done when: the DM has an accept/rejectable narrative recap; after accept, `Session-<NN>-Recap.md` is filed and inspectable.

## Output (only)

File (after accept):

`wiki/journal/sessions/<campaign-slug>/<NN>/Session-<NN>-Recap.md`

- `type: recap` (not `type: session`)
- Copy scaffold: `wiki/templates/recap.md`
- Player-safe `> [!narration] Recap` past tense, “you” address
- Optional cold open; then `## Wiki facts` as short canon-delta bullets with `[[wikilinks]]` — **pointers only**, not owner-page surgery
- No `[!secret]` / `[!mechanic]` on this surface
- No spaces in basename; no `Aruhe` / `00` prefixes

Align with `wiki/AGENTS.md` session-folder + page-filename rules. Load `obsidian-markdown` for formatting and Markdown standards. Use `writing-for-humans` and/or `copy-writer` for prose standards. After any write, run `./scripts/wiki-lint file <recap-path> --json` on the recap; use the legacy lint scripts only when diagnosing a migration mismatch.

## Procedure

1. **Orient.** Confirm campaign slug and session number (ask rather than guess). Prefer `hot.md` + that session folder over full index/log. If the source is a raw transcript, hand cleanup to `session-transcript-ingest` first and consume its bounded packet (or a bounded packet from `reconciling-session-evidence`).
2. **Propose the recap in chat.** Player-safe story of what play supported. No unearned secrets, DCs, or agent-process notes. Optional short Wiki facts list for the vault (names as wikilinks, clocks moved, next handles) — still proposal-only.
3. **File after accept.** If rejected, write nothing. If accepted: when `WIKI_STAGED_WRITES=true` (vault default), land the same content under `wiki/_staging/journal/sessions/<campaign-slug>/<NN>/Session-<NN>-Recap.md` and tell Nick to promote with `wiki-stage-commit`; otherwise write the live path above. Never skip staging while the flag is true.
4. **Stop.** Return the (staged or live) recap path. Do not cascade other skills from this skill.

## MUST NOT (conflicts resolved)

- Durable DM “session log” via `wiki/templates/session.md` / `type: session`
- Surgical canon updates on owner pages (Campaign Editor / `reconciling-session-evidence` / ingest)
- Invent stubs or lore
- Clocks, entity filing, fronts, `hot.md` writes
- Own or trigger `world-tick`
- Reflection / improvement Work cascade (offer that separately only if Nick asks outside this skill)
- Compete with Campaign Editor, Wiki Ingest, lore-design, or world-tick

## Related skills

| Need | Skill |
|---|---|
| Raw transcript → evidence packet | `session-transcript-ingest` |
| Evidence vs wiki reconcile / canon surgery | `reconciling-session-evidence` / Campaign Editor |
| Off-screen faction advance | `world-tick` (after Nick asks — not auto from recap) |

> **Attribution and license.** Narrative procedure adapted from AntTheLimey/gm-apprentice's former `session-wrapup` skill under **CC BY-SA 4.0**. Remapped 2026-09-14 to `session-recap` as sole narrative skill for ai-co-dm; see vendor `LICENSE` / `ATTRIBUTION.md`.
