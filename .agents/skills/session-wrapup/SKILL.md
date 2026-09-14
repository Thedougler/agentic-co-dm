---
name: session-wrapup
description: >-
  Write the player-safe narrative session recap only: propose and file
  wiki/journal/sessions/<campaign-slug>/<NN>/Session-<NN>-Recap.md (type: recap).
  Use after play when Nick wants a recap / wrapup / “what happened.” Not for
  durable DM session logs, canon surgery, clocks, entity filing, or world-tick.
---

# Session wrap-up (narrative recap only)

Nick standing (2026-09-14): wrapup is **just for recapping a session — purely narrative write-up**. Nothing more.

## Work gate

Show a chat proposal first. Write the wiki recap only after DM accept (FR-019). Reject leaves no page. Players see nothing until the DM accepts and presents.

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

Align with `wiki/AGENTS.md` session-folder + page-filename rules.

## Procedure

1. **Orient.** Confirm campaign slug and session number (ask rather than guess). Prefer `hot.md` + that session folder over full index/log. If the source is a raw transcript, hand cleanup to `session-transcript-ingest` first and consume its bounded packet.
2. **Propose the recap in chat.** Player-safe story of what play supported. No unearned secrets, DCs, or agent-process notes. Optional short Wiki facts list for the vault (names as wikilinks, clocks moved, next handles) — still proposal-only.
3. **File after accept.** Write only the recap path above. If rejected, write nothing.
4. **Stop.** Return the recap path. Do not cascade other skills from this skill.

## MUST NOT (conflicts resolved)

- Durable DM “session log” via `wiki/templates/session.md` / `type: session`
- Surgical canon updates on owner pages (CE / `reconciling-session-evidence` / ingest)
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
| Off-screen faction advance | `world-tick` (after Nick asks — not auto from wrapup) |
| Alias phrase “session recap” | `session-recap` → points here |

> **Attribution and license.** Adapted from AntTheLimey/gm-apprentice's `session-wrapup` skill under **CC BY-SA 4.0**. Remapped 2026-09-14 to narrative-recap-only for ai-co-dm. See vendor `LICENSE` / `ATTRIBUTION.md`.
