# Source ingest queue: ss-pc-jean-claude

Source root: /Users/nick/ai-os/shattered-sea/wiki/entities/characters/pcs/jean-claude-tabarnack.md
Mode: migration (ledger line: docs/campaign/MIGRATION-LEDGER.md — `pc :: entities/characters/pcs/jean-claude-tabarnack.md`)
Gate: REVIEWED-BY-HUMAN confirmed — MIGRATION-LEDGER.md:11 "REVIEWED-BY-HUMAN: 2026-07-13 — per the user's handoff mission..."
Started: 2026-07-13

## Sources (batch order, smallest file first)

- [x] entities/characters/pcs/jean-claude-tabarnack.md — triage: character-sheet, skipped — hand off to `dnd5e-character-interview` (registered in skills-registry.md as `character-interview`)

## Claims

- none — hand-off sources get no claims list (SKILL.md § 3: "A file that triages as
  `session` or `character-sheet` gets a `skipped — hand off to <skill>` line, not a
  claims list").

## Flags

1. **Refusal fired on triage, not on a later write.** The source is a full PC sheet
   for Jean-Claude Tabarnack (frontmatter `subtype: pc`; body has `## Mechanics` —
   class/level, species, ability-adjacent traits — matching
   `references/claim-buckets.md` § Source types row exactly: *"`character-sheet` |
   Ability scores, class/level, equipment for a PC | **Hand off** — PC creation is a
   canon-review-signed event"*. SKILL.md's Owned Paths § Never also names it directly:
   *"a PC page (`pcs/` — PC creation is a canon-review-signed event per
   skills-registry.md's `character-interview` row, not this skill's to originate)."*
   Two independent lines in the skill's own text agree — no page was instantiated, no
   `pcs/` or `world/` write was made, migration mode's owned-path exception was never
   reached because condition (c) (disposition must be `canon`, i.e. already-revealed
   legacy material being reformatted) doesn't even apply to a hand-off triage — the
   ledger line's own disposition is `ask`, not `canon`.

2. **Hand-off destination.** `docs/campaign/.claude/skills/campaign-os/references/skills-registry.md:45`:
   `character-interview` → `dnd5e-character-interview` — "output lands as/feeds
   `pcs/<name>.md` (Overview + Backstory), status canon-by-nature since it's
   player-authored — but pc creation is a canon-review-signed event, not a silent
   write." This is the correct owning skill for originating Jean-Claude's `pcs/` page;
   this agent did not invoke it (out of source-ingest's scope, and the interview
   framework needs the *player*, not a legacy document, as its primary input).

3. **Not fully mechanical — the source is legacy prose, not a raw stat block.** The
   file reads as a narrative PC profile (backstory, personality, session log) with a
   compact `## Mechanics` heading, not a traditional character sheet PDF. The
   claim-buckets table's `character-sheet` row description ("ability scores,
   class/level, equipment") is a loose fit — class/species/background are present,
   but no ability scores or equipment list. Triaged as `character-sheet` anyway
   because the frontmatter (`subtype: pc`) and SKILL.md's Owned-Paths bullet both key
   off "PC page", not off stat-block completeness — the identity of the target
   (`pcs/`) governs the refusal, not the shape of the source content. Flagging this
   as the one place the triage table's wording didn't map cleanly onto the actual
   file, in case a future PC-adjacent source (e.g. a partial background note with no
   `## Mechanics` at all) needs the DM to disambiguate rather than auto-triaging.

---
SUPERSEDED (orchestrator note, 2026-07-13): this R1 refusal was correct under
R1's gate. The user later explicitly directed PC ingestion; R4's ledger line
(REVIEWED-BY-HUMAN, MIGRATION-LEDGER § Round 4) is the canon-review signature,
and pcs/jean-claude-tabarnack.md landed via ss4-pc-jean-claude.md (4f649b6).
A future agent finding this file: do not re-litigate the refusal.
