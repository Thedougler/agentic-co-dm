# Queue: ss35-npc-ruma-delacroix

Source: entities/characters/npcs/ruma-delacroix.md | Gate: MIGRATION-LEDGER.md:137 — "npc :: entities/characters/npcs/ruma-delacroix.md → world/npcs/ruma-delacroix.md; check world/locations/calveno-sewers-grung-magazines.md for existing Ruma canon facts (R13 candidate-canon line) before writing, avoid contradiction/duplication"
Verdict: DUPLICATE, no new content write — world/npcs/ruma-delacroix.md already landed (commit 4e7c996, "ss12-npc-ruma"-era) from THIS SAME source file, cited on the page's own Appearances line as `wiki/entities/characters/npcs/ruma-delacroix.md` (INGESTED.tsv:82 recorded it under a bogus path "entities/creatures/active/ruma-delacroix.md" that never existed in shattered-sea history). Content verified line-for-line: intro, ally-turn status, At-the-Table voice/wants/check-ins, What She Knows/Doesn't Know, Social Triggers, Relationships all already present. Cross-checked world/locations/calveno-sewers-grung-magazines.md (R13 candidate-canon line) — its existing CONTRADICTION block already covers the hostile-quartermaster-vs-ally tension against session-06-export; no new duplication introduced.

## Claims

- [x] npc :: Ruma Delacroix :: world/npcs/ruma-delacroix.md (existing, canon rung 2 — Session 05 capture, no session recap file yet to cite file:line) — no new facts vs already-landed page; cleaned 2 stale relink flags (simone-tabarnack, solange-barret — both pages now live, links already resolved as wikilinks, only the leftover flag text was stale)

## Flags

- ledger-dedup-gap: R35 line 137 duplicates the earlier landing's ledger line (same source, different literal path string in INGESTED.tsv) — same pattern as this round's enzo.md/ruk.md gaps; flagging for orchestrator, not editing ledger
