---
type: runbook
status: canon
publish: false
aliases: [recap]
created: 2026-07-30
updated: "2026-08-08"
tags: [craft]
summary: "Phase 5: write the player-facing recap from this session's just-ingested canon pages, plus a highlights reel."
phase: 5
uid: a37fa66f-a7c0-4546-af87-b59c75ed4983
---

# RECAP runbook (Phase 5)

GATE: `git log --oneline | grep "ingest(sNN)"`. Paste the commit.
No commit -> STOP. Tell the user `vault/refs/runbook-ingest.md` (INGEST) is
the missing step and offer to run it.

1. `sNN-recap.md`: player-facing prose, length judged not counted (ADR 0028;
   `vault/refs/qc-recap.md` BREVITY row), built ONLY from this session's
   just-ingested `status: canon` pages (find them via `git show --stat` on
   the `ingest(sNN)` commit, or the transcript-ingest report) + transcript
   for color.
2. `sNN-highlights.md`: 3-8 verbatim quotes (speaker + L-number) + 1-3 one-line moments.
3. Propose publish: true in the Phase-6 proposal. Never set it here.
Done = RECAP: marker, word count pasted, commit `recap(sNN): ...`
