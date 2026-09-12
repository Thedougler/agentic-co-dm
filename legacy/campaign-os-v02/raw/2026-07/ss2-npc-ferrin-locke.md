# Source ingest queue: ss2-npc-ferrin-locke

Source root: /Users/nick/ai-os/shattered-sea/wiki/entities/characters/minor/ferrin-locke.md
Mode: migration (ledger line: docs/campaign/MIGRATION-LEDGER.md — Round 2, npc :: entities/characters/minor/ferrin-locke.md → restructure → world/npcs/)
Started: 2026-07-13

Gate proof:

- docs/campaign/MIGRATION-LEDGER.md:41 `REVIEWED-BY-HUMAN: 2026-07-13 — user instruction
  "implement all your recommended fixes, then proceed to round two". Blessing covers
  exactly the 13 lines below.`
- docs/campaign/MIGRATION-LEDGER.md:47 `- [ ] npc :: entities/characters/minor/ferrin-locke.md
  → restructure → world/npcs/ — status per source reveal signal`

## Sources (batch order, smallest file first)

- [x] entities/characters/minor/ferrin-locke.md — triage: npc, ready

## Claims — entities/characters/minor/ferrin-locke.md

- [x] npc :: Ferrin Locke :: world/npcs/ferrin-locke.md (new) — chandlery factor in Calveno, Dravosi intelligence leak run by Petra Venn via family leverage (%%src: legacy%%)

## Flags

- relink: warren-ferrin-locke — narrative-island page (source/narrative-islands/warren-ferrin-locke.md), not one of the 10 known pages; source's own wikilink withheld, plain text only ("the Warren" thread)
- relink: le-paludi — location where Ferrin's wife and daughter live; not one of the 10 known pages; plain text only
- relink: petra-venn — handler running Ferrin as an intelligence asset; not one of the 10 known pages; plain text only
- tag mapping: source tags `needs-detail` (work-status/origin-style tag, not Domain-tone) — DROPPED per WIKI.md § Tag taxonomy final bullet; `dravosi` (entity-identity/nation tag, same bucket as the "tessarine" example) — DROPPED, relationship captured in prose instead
- tag mapping: source content (state-sponsored espionage, blackmail leverage, secret leak) maps to canonical Domain tag `intrigue` (matches world/locations/calveno.md's own tag set) — logged, applied
- reveal signal: source page carries no `## Session Events` / Appearances section at all (unlike estratto.md's explicit "Not yet encountered" line) — no signal found means treated as unrevealed; landed `status: pending`, not `canon`
- location field: `[[calveno]]` — world/locations/calveno.md confirmed to exist (Round 1, canon)
