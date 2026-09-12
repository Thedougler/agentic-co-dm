# Harness Dispatch Procedure

Coordinate coding harnesses for this repository. This procedure does not own repository truth — it points at canonical files.

## Procedure

1. **Locate repo** — confirm working directory is the repository root.
2. **Read `AGENTS.md`** — the operating map. Follow its Sources of Truth and Workflow sections.
3. **Read git state** — branch, uncommitted changes, recent commits.
4. **Read Spec Kit artifacts** — `specify integration status --json`; inspect `specs/<feature>/{spec,plan,tasks}.md` for the target feature.
5. **Determine phase** — which Spec Kit phase is next (specify, plan, tasks, implement, converge, review).
6. **Pick a coding harness** — by capability and availability. Phases are not permanently bound to one product. Author and independent reviewer should differ when review is warranted.
7. **Hand off** — pass the harness: objective, paths to canonical artifacts, expected phase, and only constraints absent from the repository. Do not paste copies of canonical documents.

## Canonical Pointers

| Document | Role |
|---|---|
| `AGENTS.md` | Operating map |
| `.specify/memory/constitution.md` | Non-negotiable principles |
| `specs/<feature>/spec.md` | Feature requirements |
| `specs/<feature>/plan.md` | Technical design |
| `specs/<feature>/tasks.md` | Implementation work graph |
| Source + tests | Executable truth |

## Prohibitions

- No Bot-local copies of policy or specifications.
- No re-specifying when artifacts already exist — consume them.
- No two writers on one canonical artifact or shared workspace simultaneously.
- No editing generated Spec Kit adapters to add policy.
- No pasting Spec Kit command/prompt bodies into this procedure.
- No constitution principle text or feature requirement text in this file.

## Return Report

After each dispatch, report:

- Harness used
- Artifact or workspace changed
- Tests run and results
- Unresolved findings
- Convergence state
- Commit or PR if applicable

## Grok Claude-Compatibility Isolation

Grok Build may discover Claude project files via compatibility mode. For strict runtime isolation, configure at user level (cannot be repo-enforced):

```toml
# ~/.grok/config.toml
[compat.claude]
agents = false
skills = false
rules = false
```

Verify with `grok inspect --json` when the CLI is present. Missing CLI: skip that check, do not invent a pass.
