# Source ingest queue: ss3-rule-carpenters-shop

Source root: /Users/nick/ai-os/shattered-sea/wiki/rules/subsystems/carpenters-shop.md
Mode: migration (ledger line: docs/campaign/MIGRATION-LEDGER.md — Round 3,
"rules-subsystem :: rules/subsystems/carpenters-shop.md → world/rules/ — subtype:
subsystem; [HB]-heavy minority pile test")
Gate proof: `grep -n "REVIEWED-BY-HUMAN" docs/campaign/MIGRATION-LEDGER.md` line 63
("REVIEWED-BY-HUMAN: 2026-07-13 — same user instruction; blessing covers exactly the
14 lines below.") covers Round 3 line 72, the exact line this queue executes.
Started: 2026-07-13

## Sources (batch order, smallest file first)

- [x] rules/subsystems/carpenters-shop.md — triage: rule (subsystem/facility), ready

## Claims — rules/subsystems/carpenters-shop.md

- [x] rule :: Carpenter's Shop :: world/rules/carpenters-shop.md (new) — 2024 Bastions
  Smithy facility (Tier 1), player-facing crafting rules (%%src: legacy%%)

## Flags

- **MISSION-FRAMING CONTRADICTED BY SOURCE**: the ledger line's own parenthetical
  billed this file as "[HB]-heavy minority pile test ... real DM Only content
  expected, unlike subclasses." Actual file content: `grep -c "\[HB\]"` on the source
  = 0, zero DM-only/table-ruling text of any kind. Surveyed the whole
  `rules/subsystems/` pile (14 files) for context: only 2 of 14 carry any `[HB]`
  marker at all (`ship-upgrades.md` = 16, `ship-bastion.md` = 1, `surgeons-berth.md`
  = 1); `carpenters-shop.md` itself is 100% RAW 2024 DMG Bastions text, same shape as
  the swashbuckler/draconic-sorcery precedent this ledger line explicitly contrasted
  itself against. Per Hard Rule 1 (fidelity only), no DM Only content or [HB]
  mechanic was invented to satisfy the framing — the page states plainly that none
  exists. Flagged for the DM: the "[HB]-heavy" pile hypothesis may not hold, or a
  different file in the pile (`ship-upgrades.md`, 16 hits) would have been the real
  test case.
- **Status determination — rung cited**: no explicit unrevealed marker (rung 1 does
  not fire — no "planned" dir, no "not yet encountered" line). Rung 2 (actual-play
  evidence) checked against source-repo sessions
  (`grep -rli carpenter /Users/nick/ai-os/shattered-sea/wiki/sessions/`): one hit,
  `sessions/session-02-scene-04-ship-exploration.md:225` — "If the party ever
  installs a **Carpenter's Shop** (Smithy facility) on the Surety, he can run it
  without additional staff." This is conditional/hypothetical framing ("if...ever"),
  not confirmed use — rung 2 does not fire. Rung 3 (per-file `audience: players` +
  `publish: true`) checked against the whole sub-pile: verified uniform across all 14
  files in `rules/subsystems/` (`audience: players`, `publish: true`, `status:
  active` on every one) — export default per claim-buckets rules-row shortcut, not a
  genuine per-file signal, so rung 3 does not fire either. Landed on **rung 4 (no
  genuine signal) → `status: pending`** — same shortcut precedent as
  `world/rules/swashbuckler.md` and `world/rules/draconic-sorcery.md`.
- **Tags dropped**: source tags `maritime`, `player-resource` — neither is in
  `world/_meta/tags.md`'s canonical Domain (tone/genre) list, and the page carries no
  genuine tonal signal (dry mechanical rules text). Landed `tags: []` per WIKI.md §
  Tag taxonomy, matching the swashbuckler/draconic-sorcery precedent. Not added to
  the taxonomy — no per-file signal to justify growing it.
- **Connection targets — relink, no wikilinks (migration-mode link deferral)**: source
  page links three entities, none of which have a `world/` page yet (stub check:
  `grep -ril` for each returned no page hits — `bastions` no hits at all;
  `weapons-locker` and `riggers-workshop`/`rigger` hits were false positives, either
  a plain-text table mention on `world/ships/greyteeth-runner.md` or the unrelated
  word "outrigger"):
  - `relink: bastions — once its rule page lands (parent subsystem)`
  - `relink: weapons-locker — once its rule page lands (cost-halving synergy)`
  - `relink: riggers-workshop — once its rule page lands (sibling facility, source
    Connections list)`
- **Reciprocal mention already in the wiki, not touched**: `world/ships/
  greyteeth-runner.md:63` already names "Carpenter's Shop" as a facility in its own
  upgrade-fit table, written before this page existed — plain text, not a wikilink.
  Owned-paths restricts this queue to `world/rules/carpenters-shop.md` only; not
  edited. Candidate for Round 3's own `link-pass R3` ledger line (unchecked,
  authorizes canon-page edits including ships) — flagged there, not here.
- **Skeleton fit**: rule skeleton held cleanly for a subsystem page — Player-Known /
  DM Only / Mechanics / Provenance mapped 1:1 onto the source's prose /
  (nothing) / stat-block-and-options / sources field, same as the subclass
  precedents. The "real DM-side content" split the ledger anticipated never
  materialized on this particular file — see the mission-framing flag above.
