---
type: runbook
status: canon
publish: false
aliases: []
created: 2026-07-30
updated: "2026-08-08"
tags: [survival]
summary: "Phase 4: spawn per-chunk extractor agents that write transcript facts to vault/campaigns/shattered-sea/pcs pages at status: canon, then human spot-check."
phase: 4
uid: 2eaa62f7-9ea1-427e-8f3c-c1bd4dd83351
---

# INGEST runbook (Phase 4)

GATE: `ls vault/episodes/NNN/transcript.md`, paste. Missing ->
`vault/refs/runbook-capture.md` (Phase 3) hasn't produced it yet. Full
precondition (speaker-label density, resume state): `transcript-ingest`
SKILL.md § Gate check.

1. Run the `transcript-ingest` skill
   (`.claude/skills/transcript/SKILL.md`) — it owns
   chunking, the `extractor` agent (`.claude/agents/extractor.md`), entity
   resolution, contradiction handling, and human review/finish.

Done = `INGEST: chunk L#-L#, N pages touched` pasted per chunk,
`REVIEWED-BY-HUMAN:` recorded, commit `ingest(sNN): ...` (transcript-ingest's
own Finish step).
