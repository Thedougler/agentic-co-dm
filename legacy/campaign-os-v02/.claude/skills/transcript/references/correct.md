---
name: transcript-correct
description: Run the post-transcription corrector pass over a session transcript CSV — Phase 3 (CAPTURE), in a Campaign OS repo (vault/ present). Use when a CSV exists with no sibling .corrections.jsonl, or for "correct the transcript", "fix transcription errors", "run the corrector pass". Not diarization (transcript-label) or a frozen transcript.md.
---

# Transcript Correct

Phase 3 — CAPTURE, corrector pass. Runs on the transcript CSV **before**
transcript-label freezes anything. Three steps, nothing more: split, fix,
merge. Four fixer agents total, no reviewer, no judge wave — the merge
script's diff is the audit. The main thread handles only paths and counts;
it never reads transcript rows.

## Gate check

Paste before doing anything else:

```
find vault/episodes/NNN/audio -maxdepth 1 -name "*.csv" 2>/dev/null
find vault/episodes/NNN/audio -maxdepth 1 -name "*.corrections.jsonl" 2>/dev/null
```

No CSV → stop; transcription hasn't run. A `.corrections.jsonl` sidecar
already beside the target CSV → the pass has run; re-running needs the
user's explicit say-so.

## Workflow

1. **Split** (script):
   `utils/tools/audio/.venv/bin/shattered-audio correct split --csv <csv>`
   → 4 part CSVs in `<csv-dir>/correction-work/`. Paste the output.
2. **Fix** — dispatch 4 `transcript-corrector` subagents in a single
   message, **explicit `model: sonnet`** (never default), one part path
   each, nothing else in the prompt. Each fixes its part in place and
   returns one line; paste the 4 lines as-is. Agent type unavailable →
   fix in-loop one part at a time with a `NOTED:` line. No review agents,
   no second pass — dispatch, collect, merge.
3. **Merge** (script):
   `utils/tools/audio/.venv/bin/shattered-audio correct merge --csv <csv>`
   Diffs parts against the original, refuses structural damage, rewrites
   the CSV + existing siblings, writes the `.corrections.jsonl` sidecar.
   Paste its output — that is the audit.
4. Paste the final marker:
   `CORRECT: session NN, N field changes applied (sidecar <path>)`.

Optional, on the user's ask only: `correct promote --logs-glob
'vault/episodes/*/audio/*.corrections.jsonl'` proposes recurring single-token
fixes as `utils/tools/audio/autocorrect.csv` rows (dry-run default; append needs
an explicit yes).

## Owned paths

Writes `<csv-dir>/correction-work/` (ephemeral, inside gitignored
`vault/episodes/*/audio/`), the `.corrections.jsonl` sidecar, and the corrected
CSV/JSON/MD in place. Appends to `utils/tools/audio/autocorrect.csv` only on an
explicit human yes. Never touches `vault/`, `vault/campaigns/shattered-sea/pcs/`, `vault/episodes/NNN/transcript.raw.md`,
`vault/episodes/NNN/transcript.md`, `speakers.yaml`; never sets `status: canon` or
`publish: true` — it never opens a wiki page at all.

## Degrade by asking

- Sidecar already exists → ask before re-running; never silently re-correct.
- Merge refuses (row IDs mismatch) → report which part, ask; never hand-fix
  the part or force the merge.
- Promote step → always show the rows and wait; never `--no-dry-run`
  unprompted.
