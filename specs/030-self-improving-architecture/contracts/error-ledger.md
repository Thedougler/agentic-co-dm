# Contract: errors.md and `scripts/error-ledger.py` (FR-006–FR-010, FR-036)

Entry shape: data-model.md §1.

| Invocation | Effect | Output (JSON) |
|---|---|---|
| `error append --source S --cause C --sitting X [--detail D] [--attach e-N] [--dry-run]` | Attach `{sitting:X, detail:D or C}` to the open entry with the same `source` and `cause_key`, or to `--attach e-N` (which overrides only the cause match; the named entry's `source` must equal `S`). With no match, create a new entry. An identical occurrence already present changes nothing. | `{"status":"attached"\|"created"\|"already_done","id":"e-N","occurrences":k}` |
| `error drain --id e-N [--dry-run]` | Remove the entry. An absent id changes nothing. | `{"status":"drained"\|"already_done","id":"e-N"}` |
| `error list [--ids-only]` | Print all entries (every entry is open). | `[entry…]` or ids |
| `error recurrence` | FR-009 metric. | `{"total":n,"by_sitting":{"<sitting>":n}}` |
| `error migrate [--dry-run]` | One-time conversion (research R3). Idempotent. | `{"status":"migrated"\|"already_done","removed":[ids],"merged":{"e-205":[…]},"entries":n}` |

- `--cause-fixed` no longer exists (FR-006 drops `cause_fixed`). Passing it exits 2 with `{"status":"error","error":"--cause-fixed was removed","hint":"drain removes the entry; no flag needed","example":"python3 scripts/error-ledger.py error drain --id e-212"}`.
- `--attach e-N` where e-N's `source` differs from `--source` is refused with exit 2 and nothing written: `{"status":"error","error":"source mismatch: e-N has source <X>, got <S>","hint":"attach only within one source; omit --attach to create an entry","example":"python3 scripts/error-ledger.py error append --source <X> --cause \"…\" --sitting \"…\" --attach e-N"}`. An unknown e-N gets the same error shape. A regression test for the refusal is required (FR-007, FR-011) in `tests/test_error_ledger_repairs.py`.
- A missing `--source` exits 2 with an example. `--source` must be an existing repo path or `external:<name>`.
- Runs from any working directory. `errors.md` is found at the repo root.
- Agent guidance, in `AGENTS.md` "Error ledger" (line ~196) and `wiki-lint/SKILL.md` (line ~47): fix and verify the source, then continue. Call `append` only when the fix cannot land in the current task. `drain` goes in the same commit as the verified fix.
