# Queue: ss7-historical-log

Source: wiki/log.md | Gate: MIGRATION-LEDGER.md:167 — "historical-log :: log.md (527-line campaign log) → honest triage per claim-buckets; chronological table-play material hands off (Hard Rule 5), a documented refusal/mapping is a correct outcome"
Verdict: claim-buckets: internal-equivalent-check ("Map, don't duplicate") — no wiki page. File is `type: system, subtype: change-log, audience: agent`: an append-only CREATE/UPDATE/INGEST/FIX/MOVE/DELETE/FLAG op-log for the LEGACY shattered-sea wiki tooling (`ttrpg-llm-wiki-init`/`ttrpg-wiki-ingest`), not campaign narrative.

## Claims

- [x] internal :: log.md → maps to campaign-os `archive/2026-07/INGESTED.tsv` + `MIGRATION-LEDGER.md` + git commit history (equivalent ingest/structural-change tracking) — no separate page needed
- [x] chronological :: session-01/02/03 one-line glosses (L22,43,64) name `Inbox/Session-0N-Recap.md` as source, not narrated content — Hard Rule 5 hand-off target is `transcript-ingest`, already exercised per-session on OTHER ledger lines: session-01 DONE 75ae5e5, session-02 DONE 8c83215, session-03 already queued MIGRATION-LEDGER.md:166 (unchecked) — no new hand-off created here, would duplicate
- [x] residual :: none — every fact log.md references (entity/rules/bestiary pages, L226-527) is itself a separate legacy source file that would need its own ledger line if not already covered; log.md carries zero facts not already anchored elsewhere

## Flags

- none — refusal is the deliverable per gate line
