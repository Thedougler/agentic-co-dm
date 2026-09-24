# Contract: errors.md and `scripts/error-ledger.py` (FR-006–FR-010, FR-036)

Entry shape: data-model.md §1.

| Invocation | Effect | Output (JSON) |
|---|---|---|
| `error append --source S --cause C --sitting X [--detail D] [--attach e-N] [--dry-run]` | Attach `{sitting:X, detail:D or C}` to the open entry with the same `source` and `cause_key`, or to `--attach e-N`. With no match, create a new entry. An identical occurrence already present changes nothing. | `{"status":"attached"\|"created"\|"already_done","id":"e-N","occurrences":k}` |
| `error drain --id e-N [--dry-run]` | Remove the entry. An absent id changes nothing. `--cause-fixed true` is accepted and ignored. | `{"status":"drained"\|"already_done","id":"e-N"}` |
| `error list [--ids-only]` | Print all entries (every entry is open). | `[entry…]` or ids |
| `error recurrence` | FR-009 metric. | `{"total":n,"by_sitting":{"<sitting>":n}}` |
| `error migrate [--dry-run]` | One-time conversion (research R3). Idempotent. | `{"status":"migrated"\|"already_done","removed":[ids],"merged":{"e-205":[…]},"entries":n}` |

- A missing `--source` exits 2 with an example. `--source` must be an existing repo path or `external:<name>`.
- Runs from any working directory. `errors.md` is found at the repo root.
- Agent guidance, in `AGENTS.md` "Error ledger" (line ~196) and `wiki-lint/SKILL.md` (line ~47): fix and verify the source, then continue. Call `append` only when the fix cannot land in the current task. `drain` goes in the same commit as the verified fix.
