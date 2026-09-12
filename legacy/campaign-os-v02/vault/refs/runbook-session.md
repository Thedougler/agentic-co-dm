---
type: runbook
status: canon
publish: false
aliases: []
created: 2026-07-30
updated: "2026-08-15"
tags: [craft]
summary: "Phase 1: identify loose threads via grep, draft the session story, then hand off to composing-beats."
phase: 1
uid: 1e2330f0-4b09-4cdb-bdb9-5cd4068c3df1
---

# PREP runbook (Phase 1)

GATE: previous session ingested. Run `git log --oneline | grep ingest` and paste.

1. Loose threads by grep, not memory (paste each as a PREP: line):
   - open quests: `grep -l "quest_status: active" vault/campaigns/shattered-sea/quests/`
   - unresolved REVIEW lines: `grep -rn "REVIEW" vault/episodes/ --include="state-changes.md" 2>/dev/null`
   - recent NPC pages: tail of `## Session Log` on pages touched last session
2. Write the session story first (`draft-story` skill) →
   `vault/episodes/NNN/session-NN-<slug>.md`; paste the path as a PREP: line
   once signed off. A side cold open's own story is composed separately, not this step.
3. Hand off to `composing-beats`'s overview route to build
   `vault/episodes/NNN/eNN-overview.md` from the story, then the run-guide
   route to compose each `vault/episodes/NNN/eNN-run-guide-<slug>.md`. It resolves every
   named entity, hands each at-table situation to its frame route, and runs
   lint, `continuity-checker`, and `content-quality-checker` before its own
   commit — this runbook doesn't restate those steps.
   The party ends the session somewhere it didn't start → every crossing
   is a `type: route`, designed by `travel-events` (the overview Journey
   check enforces this; "you arrive" is never a transition line).
Done = PREP: markers pasted, lint clean, commit `prep(sNN): ...`
