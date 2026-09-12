# Data Model: OMP Spec Kit Integration

## Spec Kit artifact

Canonical SDLC document. Owner: Spec Kit.

| Field | Rule |
|---|---|
| kinds | constitution, spec, plan, tasks, checklist, converge notes |
| location | `.specify/memory/` or `specs/<feature>/` |
| mutation | only via Spec Kit commands, never by specialists rewriting the phase |

Validation: no harness agent named `specify`, `clarify`, `plan`, `checklist`, `tasks`, `analyze`, `implement`, or `converge`.

## Live context

Standing, feature-current instruction. Owner: agent-context extension.

| Field | Rule |
|---|---|
| path | `.omp/AGENTS.md` |
| import | first lines include `@../AGENTS.md` |
| managed block | between `<!-- SPECKIT START -->` and `<!-- SPECKIT END -->` |
| payload | pointer to current `plan.md` (extension-owned text) |
| unmanaged | wiki routing stays in root `AGENTS.md`; not copied |

State: `missing → file with import → managed block present → block matches active plan path`.

## Sticky rules

Durable safety constraints. Owner: project RULES file.

| Field | Rule |
|---|---|
| path | `.omp/RULES.md` |
| contents | verify; do not edit generated files; no push/deploy unless asked; map to tasks; completion needs evidence |
| conflict | safety beats live context; live context beats “which feature is active” |

## Specialist

Narrow OMP agent. Owner: coding harness.

| Field | Rule |
|---|---|
| names | `spec-auditor`, `implementer`, `verifier` only |
| `spawns` | `[]` |
| auditor | `@plan`, read-only tools, blocking, high thinking, no writes |
| implementer | `@task`, may edit, one `tasks.md` item |
| verifier | `@review`, read-only, blocking, high thinking, no writes |
| isolation | requested on the implementer delegation when files are disjoint; never on auditor/verifier |

## Dependency wave

| Field | Rule |
|---|---|
| members | tasks with no undone dependencies on each other |
| size | 1–4 implementers |
| shared files | those items excluded; sequential |
| context | one shared Spec Kit context for the batch |

State: `gated (analyze clean) → wave running → reports valid → wave complete \| blocked \| failed`.

## Structured worker report

See [contracts/worker-report.md](./contracts/worker-report.md).

Invalid structure = `failed`. Parent does not guess from prose.

## Thin orchestrator

See [contracts/feature-fast.md](./contracts/feature-fast.md).

State: `idle → specify…analyze → stop on material finding → waves → converge → append-only waves → verifier → complete`.

## Project harness config

| Field | Rule |
|---|---|
| path | `.omp/config.yml` |
| concurrency | 4 |
| recursion | 1 |
| advisor | off |
| memory | off |
| autolearn | off |
| isolation | enabled |
| roles | `default`, `plan`, `task`, `review`, `smol` defined in this file |

## Baseline check

See [contracts/check-omp-baseline.md](./contracts/check-omp-baseline.md).

State: `fail (exit 1) → pass (exit 0)`.
