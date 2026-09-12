# Contract: worker report

Machine-readable result from `implementer` and `verifier`. `outputSchema` + `schemaMode: strict`.

## Shape

```json
{
  "status": "complete",
  "task_ids": ["T012"],
  "changed_files": [],
  "tests_run": [],
  "tests_passed": true,
  "acceptance_criteria_verified": [],
  "unresolved": []
}
```

| Field | Rule |
|---|---|
| `status` | `complete` \| `blocked` \| `failed` |
| `task_ids` | Spec Kit task ids this worker owned |
| `changed_files` | repo-relative paths; verifier always `[]` |
| `tests_run` | commands or check names actually executed |
| `tests_passed` | false if any listed run failed or none required but status is `complete` without evidence |
| `acceptance_criteria_verified` | ids or short names from spec/tasks |
| `unresolved` | leftover risks; empty on clean `complete` |

## Done

Parent can parse the object. `status` is one of the three values. Missing required field → treat as `failed`.

## Failed

Prose-only reply. Extra keys allowed; missing required keys not allowed. `complete` with non-empty `unresolved` that includes a failed check → parent must not mark the wave done.

## Invalid

Parent inferring success from surrounding sentences. Verifier writing implementation files.
