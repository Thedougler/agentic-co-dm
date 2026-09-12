# Implementation Plan: Blind Cold Evaluation of D&D Content

**Branch**: `012-blind-content-eval` | **Date**: 2026-09-12 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/012-blind-content-eval/spec.md`

## Summary

When D&D content-producing guidance changes, sample Work from that guidance is judged cold by two independent evaluators who did not author it and do not see the authoring session. File-shape checking alone cannot pass the change. Axes: form, appropriate use, DM-reference copy, theatre of the mind. Omit an axis when that band is absent.

One new eval skill. Rubrics stay `copy-writer`, `theatre-of-the-mind`, `obsidian-markdown`, and `wiki/AGENTS.md` Layout. `writing-for-agents` D&D content guidance gains a completion criterion that dispatches those two evals. No pytest suite. No legacy rewrite. No AGENTS.md table row.

## Technical Context

**Language/Version**: Markdown skills and standing agent docs. Host agent executes them (isolated evals). No new compiled language.

**Primary Dependencies**: `writing-for-agents`; new `blind-content-eval`; `copy-writer`; `theatre-of-the-mind`; `obsidian-markdown`; `wiki/AGENTS.md` Layout. Host isolated-agent dispatch.

**Storage**: Files. Not a database.

**Testing**: [quickstart.md](./quickstart.md). Two cold evals of sample jobs. No bulk suite. No scanner over `legacy/`.

**Target Platform**: Local DM workstation. Co-DM agent on omp (and other hosts that can run a separate evaluator without the authoring transcript).

**Project Type**: Agent skill pack + standing instructions.

**Performance Goals**: SC-001 / SC-003 — two independent evaluators agree on pass/fail for at least 8 samples.

**Constraints**: FR-002 evaluators did not author and do not see the session. FR-003 automatic file-shape checks are not sufficient. FR-011 not required on non-D&D-content guidance. FR-012 accept-gate unchanged. FR-013 010 authorities stay owners of prose/format. FR-014/SC-007 no legacy rewrite. Constitution VII: eval names fail modes, not a writing method. Constitution IX: do not restate copy-writer or TotM in the eval skill.

**Scale/Scope**: One new skill. One completion-criterion step on `writing-for-agents`. No `src/`.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Gate | Status |
|---|---|
| I. Domain language is binding | Pass — DM, Co-DM, wiki, Work, theatre of the mind. No GM. |
| II. Issues are the work surface | Pass — plan does not treat PRs as a request surface. |
| III. Spec before code | Pass — spec has independently testable stories P1–P4. |
| IV. Tests specify behavior | Pass — the test is cold judgment of sample Work at public seams (form, use, DM copy, spoken look), not skill internals. |
| V. Single context | Pass — no second bounded context. |
| VI. Software is agent-shaped | Pass — skill + isolated evaluators, no GUI. |
| VII. Do not suffocate agents | Pass — eval names axes and fail modes. Rubrics already live on copy-writer / TotM / vault format. No extra writing method. |
| VIII. Safe automation runs unattended | Pass — eval is judgment, not a formatter hook. Existing file chores may still run; they are not the gate. |
| IX. Design trends toward token efficiency | Pass — one skill; one completion line; load existing rubrics; no duplicated quality essay; no always-loaded AGENTS.md table. |

**Post-design re-check**: still pass. Contract is classification of an eval job. Complexity table empty. A new skill is justified: evaluation is a different job from writing, and the author cannot be the cold judge.

## Project Structure

### Documentation (this feature)

```text
specs/012-blind-content-eval/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── blind-content-eval.md
└── tasks.md             # /speckit.tasks — not this command
```

### Source Code (repository root)

```text
.agents/skills/blind-content-eval/SKILL.md
.agents/skills/writing-for-agents/SKILL.md
```

**Structure Decision**: Add `blind-content-eval` as the evaluator job. Point at it from the existing D&D content guidance section in `writing-for-agents` as the done-gate. Evaluators load `copy-writer`, `theatre-of-the-mind`, `obsidian-markdown`, and `wiki/AGENTS.md` Layout — do not copy those rubrics. Do not add a row to the 010 stack table. Do not add pytest. Do not edit `legacy/` or rewrite wiki pages. Host isolated dispatch is the environment; do not add a runner script.

## Complexity Tracking

> None. No constitution violations. New skill is a new job (judge ≠ author), not a duplicate writing authority.
