# Queue: ss35-npc-enzo

Source: entities/characters/minor/enzo.md | Gate: MIGRATION-LEDGER.md:107 — "npc :: entities/characters/minor/enzo.md → world/npcs/enzo.md, verify canon/pending"
Verdict: DUPLICATE, no write — world/npcs/enzo.md already landed R11 (ss11-npc-enzo, commit 6cbf93f) from THIS SAME source file (ss11's own queue flagged "source path mismatch: ledger says entities/characters/npcs/enzo.md; actual source lives at entities/characters/minor/enzo.md"). Content verified line-for-line identical: table fields, prose, Appearance & Manner, both Session Events, full statblock all already present (Player-Known + Stats & Combat sections), enriched with Relationships/Appearances + transcript citations (sessions/03:132,144; sessions/04:67).

## Claims

- [x] npc :: Enzo :: world/npcs/enzo.md (existing, canon rung 2) — no new facts vs already-landed page; verified, not written

## Flags

- ledger-dedup-gap: R35 line 107 duplicates R11's ledger line 275 (same source, different literal path string) — check script's exact-string match on INGESTED.tsv missed it because R11 recorded the source as "entities/characters/npcs/enzo.md" (mismatched-in-source-repo path) not "entities/characters/minor/enzo.md" (actual path) — flagging for orchestrator, not editing ledger
