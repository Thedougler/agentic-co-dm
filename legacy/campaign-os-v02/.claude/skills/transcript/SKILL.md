---
name: transcript
description: >-
  Session transcript pipeline — three phases in order: CORRECT (fix CSV errors before
  freeze), LABEL (resolve speaker IDs, produce frozen transcript.md), INGEST (mine
  transcript.md into canon PC-page edits). In a Campaign OS repo (vault/ present).
  Use for "correct/label/ingest the transcript", "resolve speakers", "fix transcription
  errors", "process session NN", "extract state changes", "run INGEST". Phase detected
  from which files exist; see routing table below.
---

# Transcript

Three sequential phases, one skill. Detect your phase from the routing table and load
that reference file — next tool call is Read on it, no acting call beside it.

## Phase routing

| Trigger | Gate condition | Reference |
|---------|----------------|-----------|
| "correct the transcript", "fix transcription errors", "run the corrector pass" | CSV exists, no sibling corrections.jsonl | `references/correct.md` |
| "label the transcript", "resolve speakers", "who is SPEAKER_00" | transcript.raw.md exists, no sibling transcript.md | `references/label.md` |
| "ingest the transcript", "process session NN", "mine the session", "extract state changes", "run INGEST" | transcript.md present, no sibling ingest-review.md, speaker-label count ≥ 50 | `references/ingest.md` |

Ambiguous trigger or multiple conditions true → ask which phase to run; never assume order.

## Reference index

| File | Covers |
|------|--------|
| `references/correct.md` | CORRECT phase: split → fix → merge CSV; corrector subagents |
| `references/label.md` | LABEL phase: speaker resolution, speakers.yaml, frozen transcript.md |
| `references/ingest.md` | INGEST phase: chunk → extractor subagents → PC-page edits at `status: canon` |
| `references/contradictions.md` | How INGEST handles conflicting facts |
| `references/entity-resolution.md` | Alias and entity lookup rules for INGEST |
| `references/extraction-elaborations.md` | Extraction edge cases for INGEST |
| `references/human-review-example.md` | Worked example of ingest-review.md for INGEST |
| `references/ic-ooc-classification.md` | In-character vs out-of-character classification for INGEST |
| `references/legacy-source-gate.md` | Legacy prose-recap alternative gate for INGEST |
