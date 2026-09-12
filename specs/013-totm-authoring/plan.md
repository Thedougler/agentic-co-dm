# Implementation Plan: Theatre of the Mind Authoring

**Branch**: `013-totm-authoring` | **Date**: 2026-09-12 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/013-totm-authoring/spec.md`

## Summary

Make `theatre-of-the-mind` enforce the 013 outcomes on new player-facing Work: complete before the session, world not players, Beat-serving, state-independent, layered reveals, combat without a hidden grid or turn scripts, reusable wiki portraits, traps solvable from the fiction.

Do it by pruning method sediment on that skill and aligning `run-guide` pass 3 with Layer 1 openings. No seventh skill. No second cockpit. No `AGENTS.md` table. No legacy rewrite.

## Technical Context

**Language/Version**: Markdown skills and standing agent docs. Host agent executes them. No new compiled language.

**Primary Dependencies**: `theatre-of-the-mind`; `run-guide` (pass 3 spoken fill only); 010 writing/visual stack; 007 Session 11 cockpit; 011 outcomes-not-method.

**Storage**: Files. Not a database.

**Testing**: [quickstart.md](./quickstart.md). Score prepared-scene jobs against the contract. No bulk suite. No scanner over `legacy/`.

**Target Platform**: Local DM workstation. Co-DM agent on omp (and other hosts that load `AGENTS.md` plus skills).

**Project Type**: Agent skill pack + standing instructions.

**Performance Goals**: SC-003 — two reviewers agree on pass/fail for at least 12 prepared scenes.

**Constraints**: FR-028/FR-033 do not replace Session 11 layout or audience routing. FR-030/SC-009 no legacy rewrite. FR-031 / Constitution VII outcomes not method. Constitution IX `SKILL.md` must not grow; prune sediment. Existing accept-gate unchanged.

**Scale/Scope**: One skill body plus the surfaces reference it already points at. One pass-3 completion line on `run-guide`. Evals that pin sentence architecture are in-scope to drop or retarget. No `src/`.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Gate | Status |
|---|---|
| I. Domain language is binding | Pass — DM, Co-DM, wiki, Work, Session, theatre of the mind. No GM. No knowledge bank. Beat reused from existing session Beat craft. |
| II. Issues are the work surface | Pass — plan does not treat PRs as a request surface. |
| III. Spec before code | Pass — spec has independently testable stories P1–P4. |
| IV. Tests specify behavior | Pass — quickstart observes spoken look, agency, Beat job, layering, combat facts. Not skill-file strings. |
| V. Single context | Pass — no second bounded context. No new glossary file. Wiki portrait = existing standalone portrait. |
| VI. Software is agent-shaped | Pass — existing skills, no GUI, no human-only wrapper. |
| VII. Do not suffocate agents | Pass — outcomes and named failures only. Expert techniques are sources. No 18-section required method. No second scene template. No extra checklist. |
| VIII. Safe automation runs unattended | Pass — no new agent chore. No formatter/index step added to skills. |
| IX. Design trends toward token efficiency | Pass — one owner (`theatre-of-the-mind`); prune hard-gate sediment; no `AGENTS.md` duplicate; `run-guide` keeps cockpit and only corrects pass-3 completeness. |

**Post-design re-check**: still pass. Contract is classification of a TotM job. Complexity table empty.

## Project Structure

### Documentation (this feature)

```text
specs/013-totm-authoring/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── totm-authoring.md
└── tasks.md             # /speckit.tasks — not this command
```

### Source Code (repository root)

```text
.agents/skills/theatre-of-the-mind/SKILL.md
.agents/skills/theatre-of-the-mind/references/surfaces.md
.agents/skills/theatre-of-the-mind/evals/evals.json
.agents/skills/run-guide/SKILL.md
```

**Structure Decision**: Keep skills. `theatre-of-the-mind` owns the 013 outcomes. `surfaces.md` is the routing contract it already loads — align Initial Narration, combat, and spatial bands there; do not add a new reference. `run-guide` still owns cockpit and pass order; change only the pass-3 rule that currently dumps Layer 2/3 into Initial Narration. Do not add a skill, a `docs/agents/totm.md`, or a row to the 010 stack table. Do not edit `session-beats` (chart owner), `legacy/`, or wiki pages. Do not duplicate Beat jobs into `.omp/AGENTS.md`.

## Complexity Tracking

> None. No constitution violations.
