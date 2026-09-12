# Source ingest queue: ss4-rule-ship-upgrades

Source root: /Users/nick/ai-os/shattered-sea/wiki/rules/subsystems/ship-upgrades.md
Mode: migration (ledger line: docs/campaign/MIGRATION-LEDGER.md — Round 4, `rules-hb :: rules/subsystems/ship-upgrades.md → world/rules/ship-upgrades.md`)
Started: 2026-07-13

Gate proof:

- `REVIEWED-BY-HUMAN: 2026-07-13 — user instructions: "at least 5 rounds of iterative...` (MIGRATION-LEDGER.md:84) covers Round 4's 11 lines, including this one.
- Ledger line unchecked at start: `- [ ] rules-hb :: rules/subsystems/ship-upgrades.md → world/rules/ship-upgrades.md — subtype: subsystem; THE real [HB]-density test (16 hits — carpenters-shop was a framing miss)` (MIGRATION-LEDGER.md:97)

## Sources (batch order, smallest file first)

- [x] wiki/rules/subsystems/ship-upgrades.md — triage: rule (subtype: subsystem), ready

## Claims — wiki/rules/subsystems/ship-upgrades.md

- [x] rule :: Ship Upgrades :: world/rules/ship-upgrades.md (new) — full catalog transcription, 4 rarity tiers, 18 items, [RAW]/[HB]/[RAW reskin]/[RAW adaptation] labels preserved verbatim (%%src: legacy%%)

## Flags

- **Dispatch-claim mismatch (verified, not acted on):** dispatch line said `world/rules/carpenters-shop.md`'s source names ship-upgrades as a Connection. Checked `~/ai-os/shattered-sea/wiki/rules/subsystems/carpenters-shop.md` directly — its `## Connections` section lists only Bastions, Weapons Locker, Rigger's Workshop. No mention of ship-upgrades. No reciprocal link added to either page; this is a dispatch-generation error, not a source fact.
- `relink: catarina-davirelli — once her page lands` (currently a sub-entry mention only, in world/locations/calveno.md and world/locations/calveno-sewers-grung-magazines.md — no dedicated NPC page; W9-near-miss-adjacent, flagging for DM rather than creating a page from a shopping-catalog claim)
- `relink: ship-mechanics — once its rule page lands` (wiki/rules/subsystems/ship-mechanics.md exists in source, not yet migrated)
- `relink: ship-bastion — once its rule page lands` (wiki/rules/subsystems/ship-bastion.md exists in source, not yet migrated — distinct from `world/rules/carpenters-shop.md`'s already-relinked `bastions`, different source file/slug)
- 13 item-level relinks (all homebrew campaign items, not generic SRD/PHB gear — each gets its own flag per skill's "generic ruleset items" exception NOT applying here):
  - `relink: auto-helm`
  - `relink: clockwork-deck-crew`
  - `relink: depth-eye`
  - `relink: fog-cannon`
  - `relink: ghost-keel-coating`
  - `relink: hull-patch-automaton`
  - `relink: sending-stone-anchor`
  - `relink: tide-reader`
  - `relink: wind-callers-boom`
  - `relink: cartographers-table`
  - `relink: wardstone-figurehead`
  - `relink: arcane-artillery`
  - `relink: the-drowned-keel`
- Status rung: `pending`, ladder rung 4 (no signal of any kind). Checked source-repo sessions 01-03 recaps + this repo's sessions 01-02 transcripts/state-changes for any of the 18 catalog items or a ship-upgrades-context Catarina mention — none found. Source frontmatter `audience: players`/`publish: true` confirmed uniform across all 14 files in `wiki/rules/subsystems/` (export default, not a real per-file signal), same conclusion `world/rules/carpenters-shop.md` reached.
- Vessel pages `[[vethka]]`/`[[greyteeth-runner]]` named in the dispatch as existing — confirmed both exist (`world/_meta/index.md`), but the source text names neither ship, so no link added; noted only in case a sibling dispatch needs this cross-check.
