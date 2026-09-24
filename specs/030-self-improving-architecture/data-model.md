# Data Model: Self-Improving Architecture (030)

## 1 Error entry (`errors.md`)

The file is a `# Error ledger` heading, a blank line, then one JSON object per line, with sorted keys (as `write_errors` does today).

| Field | Type | Rule |
|---|---|---|
| `id` | `"e-<n>"` | Unique. Migration keeps existing ids. New ids use `next_error_id`. |
| `cause` | string | The first-recorded root-cause text. Never rewritten when an occurrence is added. |
| `source` | string | The authoritative file (repo-relative path) or component the fix lands in. An external source is written as `external:<name>`, e.g. `external:codex-cli`. |
| `evidence` | list of `{sitting, detail}`, length ≥ 1 | Append-only while open. `sitting` uses the same labels as `sittings.jsonl` (e.g. `"lint: aggregate repair loop"`). |

- **Invariants**: every entry is open. No two entries share `(source, cause.strip())`. Whether two differently worded causes are the same root is the agent's `--attach` call, governed by `AGENTS.md` "Error ledger". The fields `status` and `cause_fixed` do not exist.
- **Transitions**: absent → open (`append`, no exact match) → open with +1 occurrence (`append` with exact match, or `--attach e-N` on the same `source`) → open with −1 occurrence (`detach --id e-N --index k`, the undo; never removes the last occurrence) → removed (`drain`, in the same commit as the verified fix).
- **Recurrence**: reported by `error list` as `recurrence: {total, by_sitting}`, where `total = Σ(len(evidence) − 1)` and `by_sitting[s]` counts the non-first occurrences with `sitting == s`. `error list` also reports `missing_sources`: ids whose `source` path no longer exists.

## 2 Eval file (`.agents/skills/<skill>/evals/evals.json`)

```json
{
  "skill_name": "place-design",
  "trajectory_records": "...optional, kept",
  "principles": ["...optional, kept"],
  "evals": [
    {
      "id": 1,
      "prompt": "Add the Salt Stair as a place under High Eyrie.",
      "files": [], "context": "", "outputs": "wiki/entities/place/",
      "subject_skill": null,
      "core": true,
      "expected_output": "optional human description",
      "assertions": [
        {"type": "skill_selected", "text": "place-design"},
        {"type": "behavior", "text": "Writes the page without asking for approval first"}
      ]
    }
  ]
}
```

- `skill_name` is required and equals the skill directory name. `subject_skill` is an optional repo-relative skill path that `luna-eval` honors ahead of `--skill`.
- `assertions[]` is required and non-empty. `type` ∈ {`skill_selected`, `behavior`, `quality`, `guardrail`, `process`, `content`, `structure`, `scope`, `handoff`, `coverage`}. `qualitative` is folded into `quality` and `structural` into `structure`.
- `expectations[]` must not appear after conversion. Each string `s` becomes `{"type":"behavior","text":s}`.
- For `skill_selected`, `text` is an existing directory name under `.agents/skills/`.

## 3 Eval run directory (one result format)

```text
<out>/<name>/<config>/run-<n>/
├── outputs/        # subject artifacts (existing)
├── events.jsonl    # codex --json stream (existing)
├── final.txt       # subject final message (existing)
├── stderr.txt      # existing
├── timing.json     # existing: duration_ms, total_duration_seconds, exit
├── metrics.json    # NEW, derived from events.jsonl by luna-eval
└── grading.json    # written by skill-creator grader (existing schema + `type`)
```

`metrics.json`:

```json
{"tool_calls": {"command": 7, "file_change": 2}, "total_tool_calls": 9, "retries": 1,
 "invocation_errors": 1, "invocation_error_commands": ["scripts/wiki lint wiki/entities/place/Belumara.md"],
 "duplicate_actions": 0, "tokens": {"input": 0, "output": 0, "total": 0},
 "completion_reason": "ok|no_output|usage_limit|error", "model": "gpt-6-luna", "effort": "high", "skills_read": [".agents/skills/place-design/SKILL.md"]}
```

- `model`, `effort`: the values `luna-eval` actually passed to codex (its `--model`/`--effort`, defaults at run time), recorded in every run (FR-019). The FR-019 baseline and every later comparison (FR-043, SC-012) must use the same pair. A comparison whose runs differ in `model` or `effort` is invalid.
- `retries`: a failed command re-run with identical argv.
- `invocation_errors`: the number of `command_execution` items in `events.jsonl` that invoke an FR-027 command (`scripts/wiki`, `scripts/wiki-lint`, `scripts/luna-eval`, `scripts/error-ledger.py`, `scripts/manifest.py`) and were rejected as a usage error. A usage error is either the FR-035 error object on stdout (`"status":"error"` with an `example` key; see contracts/wiki-cli.md) or argparse's `usage: … error:` on stderr, with a non-zero exit. Such a call counts whether or not it is later corrected. `invocation_error_commands` lists the offending command lines. Exit codes alone are not used, because exit 2 also means "rejected" (`tools/wiki_ops/cli.py` `EXIT_REJECTED`). This is the SC-010 measure: a cold-agent run passes SC-010 only with `invocation_errors == 0`.

`grading.json`: the existing `skill-creator` schema (`expectations[{text, passed, evidence}]`, `summary`), plus `type` on each item and the new top-level fields `task_outcome` (`pass|fail|blocked`) and `semantic_quality` = pass rate of that eval's `quality`-type assertions (passed / total, `null` when the eval has none), computed from the graded items (FR-016). The grader assigns no separate score. A `skill_selected` item is graded by `luna-eval`: it passes when the first owner `SKILL.md` in `skills_read` matches `text`. Latency is taken from `timing.json`. Together, `timing.json`, `metrics.json`, and `grading.json` carry every FR-016 metric.

## 4 Identity index (`wiki/_meta/identity-index.json`, derived; I/O in `tools/wiki_ops/lint_cache.py`)

```json
{"version": 1, "manifest_sha256": "…",
 "rows": {"entities/place/belumara.md": {
   "size": 5123, "mtime_ns": 0, "content_sha256": "…",
   "stem": "belumara", "title": "Belumara", "type": "place", "lifecycle": "canon",
   "aliases": ["…"], "redirects_to": "", "body_len": 4800,
   "profile": {"e": 512, "a": 390}}},
 "pairs": {"<sha_a>|<sha_b>": 0.7312}}
```

- `profile` is the body character `Counter`, the input to today's prefilter `2·|A∩B| / (lenA+lenB) > 0.6`.
- `pairs` holds `SequenceMatcher.ratio()` for pairs that passed the prefilter, keyed by the sorted content hashes. Entries whose hashes no longer match any row are pruned on save.
- **Validity**: a row is reused when `(size, mtime_ns)` matches, or when the rehashed `content_sha256` matches. A changed `version`, a JSON error, or a changed `manifest_sha256` refreshes the affected state; version and parse errors rebuild everything.
- **Result shape added to `wiki-lint --json`**: `"identity": {"status", "ambiguous", "scanned": <selected>, "compared": <|selected ∪ candidates|>, "index": {"hits", "misses"}}`.
- **Use**: `scan_identities`, `resolve_identity`, and `_path_for` all read this index. The thresholds (prefilter > 0.6; shared-source stem ratio > 0.7) only put a page in `candidates` and set `status: ambiguous`, which gates mutations. No code picks the canonical page; that is the agent's call under `wiki-dedup` and `wiki-lint`.
- **Tracking**: `wiki/_meta/lint-cache.json`, `wiki/_meta/identity-index.json`, and `styles/config/vocabularies/CoDM/accept.txt` stay tracked. They are FR-028 bookkeeping written by lint, not read-side mutation (FR-017), and are committed with the change that caused them.
