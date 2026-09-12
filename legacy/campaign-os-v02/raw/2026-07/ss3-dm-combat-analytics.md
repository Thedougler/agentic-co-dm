# Source ingest queue: ss3-dm-combat-analytics

Source root: /Users/nick/ai-os/shattered-sea/wiki/dm/combat-analytics.md
Mode: migration (ledger line: docs/campaign/MIGRATION-LEDGER.md:76 —
`dm :: dm/combat-analytics.md → triage honestly (process/meta expected —
skip/mapping is the likely correct outcome)`)
Gate: REVIEWED-BY-HUMAN confirmed — MIGRATION-LEDGER.md:63 "REVIEWED-BY-HUMAN:
2026-07-13 — same user instruction; blessing covers exactly the 14 lines
below." (line 76 is one of the 14.)
Started: 2026-07-13

## Sources (batch order, smallest file first)

- [x] dm/combat-analytics.md — triage: `internal-equivalent-check`, skipped —
  map to `encounter-design`'s `combat-calibration.md`. No page written.

## Claims

- none — mapped outcome gets no claims list, same convention
  `ss2-dm-perrin-primer.md` used for its refusal (SKILL.md §3: a hand-off/
  skip/map source gets a queue line, not a claims list).

## Triage verdict: MAPPED, not written — `internal-equivalent-check`

**Deciding row: `references/claim-buckets.md` § Source types, row
`internal-equivalent-check`** (one of the two rows added since R2, "System/
meta doc whose function campaign-os already provides... → Map, don't
duplicate — hunt the equivalent... queue-file records source → equivalent +
coverage gaps; no wiki page"). This is the row that decides it, and it
decides cleanly — no analogy or improvisation needed, unlike R2's
`dm/perrin-primer.md` triage (which had no matching row and had to reason
from Owned-paths by analogy). **The gap the ledger's "two rows since R2"
note points at is closed for this file**: `internal-equivalent-check` covers
it on the letter.

1. **Content shape.** Frontmatter: `type: dm-intelligence, subtype:
   dm-intelligence, audience: dm, publish: false, system_role:
   dm-intelligence, token_profile: quick-ref, mandatory_for:
   [encounter-design], update_trigger: "After each combat; when encounter
   difficulty patterns become clear"`. Body: an Encounter Log table
   (session/CR/rounds/downs), "Patterns Observed" per-PC combat behavior
   notes (Perrin, Crissdalynn, Delmar, Jean-Claude), and "Calibration Notes"
   (e.g. "CR 14 four-on-one held for exactly 3 rounds… CR 12–14 with
   legendary actions is the sweet spot"). This is not campaign fact wearing
   a process wrapper — it *is* the process artifact: a standing,
   session-updated empirical-difficulty-calibration document, explicitly
   `mandatory_for: encounter-design`.

2. **The equivalent exists, and explicitly discarded this exact pattern on
   purpose.** `.claude/skills/encounter-design/references/combat-
   calibration.md:12-24` ("What was dropped, and why"):
   > "The legacy skill maintained a whole second tier of standing
   > documents — `wiki/dm/{pc}-combat-profile.md` and
   > `wiki/dm/party-combat-profile.md`, compiled and recalculated across
   > sessions, holding computed DPR/effective-HP/synergy data as its own
   > source of truth. That doesn't fit this repo's ownership model...
   > So this reference keeps the derivation method and drops the
   > persistence layer — calibration is recomputed fresh, from what's
   > already on the page, every time an encounter needs it."

   `dm/combat-analytics.md` is functionally that exact dropped
   `party-combat-profile.md` shape: a hand-maintained, cross-session,
   recalculated combat-intelligence file feeding encounter design. Writing
   a campaign-os equivalent of it would resurrect the precise persistence
   layer `combat-calibration.md` was authored to replace. Mapping, not
   migrating, is correct — recreating this file as a wiki page (even
   `prep/`-scoped) would duplicate a skill's already-built and
   deliberately-shaped alternative.

3. **Not `pc-tactical-note`.** That row is for guidance keyed to a *single*
   existing PC (the R2 `perrin-primer.md` shape). This source spans the
   whole party (4 PCs) and an encounter log, not one PC's spotlight levers —
   `internal-equivalent-check` is the better-fitting row on content shape
   alone, independent of the fact it also happens to be the row that
   resolves cleanly.

4. **Not `session-record`.** No session chronology/narrative — it's
   aggregated tactical data *about* sessions 03-04, not a recap of what
   happened. Hard Rule 5's session-record hand-off doesn't apply.

## Coverage note (queue-file record per the row's own instruction)

- **Equivalent found:** `combat-calibration.md`'s 7-step procedure (baseline
  XP budget → read party stats from `pcs/*.md` → read `## Session Log` →
  adjust → multi-enemy scaling table → confidence label → paste into the
  encounter page). Functionally supersedes what `combat-analytics.md` was
  doing by hand.
- **Genuine coverage gap, not this skill's to close:** the procedure reads
  its evidence from `pcs/*.md` frontmatter and each PC's `## Session Log`
  section. `grep -ril "Perrin\|Crissdalynn\|Delmar\|Jean-Claude"
  /Users/nick/ai-os/campaign-os/pcs/*.md` → no hits; `ls
  /Users/nick/ai-os/campaign-os/pcs/` → only `CLAUDE.md`, no PC pages exist
  in this repo yet. So the *method* has an equivalent, but the *evidence*
  this source captured (the whip-shark/Kyzil-spar/Grung-ambush encounter
  log, the per-PC behavioral patterns) has nowhere to land until PC pages
  exist — PC creation is `dnd5e-character-interview`'s canon-review-signed
  territory (skills-registry.md), not this skill's or `encounter-design`'s
  to originate. This is a real gap (no page carries the empirical data
  forward today), but it is not a gap `internal-equivalent-check` or this
  skill closes — flagging for the DM/orchestrator, not acting on it.
- **No world/ or pcs/ write.** No page created, no claim written.

## Flags

1. **Downstream seed, once PCs exist.** Once `pcs/perrin-black-jaw.md`,
   `pcs/crissdalynn-*.md`, `pcs/delmar-*.md`, `pcs/jean-claude-*.md` land
   (via the character-interview pipeline), this source's per-encounter data
   (session 03 whip shark, session 04 Kyzil spar CR 14 4v1, session 04 Grung
   sewer ambush) is the natural seed for each PC's `## Session Log` entries
   — but originating those entries is outside `source-ingest`'s and
   `encounter-design`'s owned paths either way (CANONIZE/canon-review's
   territory per project rule 3, transcripts→ledgers→wiki). Not invoking
   any skill now; naming the destination for the orchestrator.
2. **Wikilinks in source, not followed.** No wikilinks in this source body
   (plain PC first names only, no `[[...]]` syntax) — nothing to relink.
3. **No CONTRADICTION, no blocked claim.** Clean triage-time map, not a
   conflict between sources — nothing routed to canon-review.
4. **`hot.md`-adjacent, not identical.** This file is a sibling instance of
   the same "legacy standing DM-intelligence doc with no campaign-os owning
   path" shape as the ledger's other R3 `root :: hot.md` line, but resolved
   independently here since its actual equivalent (`combat-calibration.md`)
   is a different, more specific target than `hot.md`'s mapping
   (`docs/STATE.md`'s Campaign block + `pipeline_status`).
