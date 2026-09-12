# Implementation Plan: Expert-Grounded D&D Content Guidance

**Branch**: `011-narrative-mechanics` | **Date**: 2026-09-12 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/011-narrative-mechanics/spec.md`

## Summary

When creating or changing a skill, standing instruction, or procedure that makes D&D wiki content, research how experts already solved that problem, then integrate the **outcomes** into that one document. Expert techniques are sources, not the only valid method. Official designers and documented craft first; high-quality homebrew only if those are silent; never paste proprietary book text. Ordinary wiki writes follow the resulting guidance — they do not re-research.

First instance: combat craft. Custom features, named-place encounters, and substantial homebrew changes must serve a named narrative beat. Stock opposition used unchanged is exempt. Explicit DM override is allowed.

No seventh skill. No linter. No legacy rewrite. No research pass on every wiki write.

## Technical Context

**Language/Version**: Markdown skills and standing agent docs. Host agent executes them. No new compiled language.

**Primary Dependencies**: `writing-for-agents`; `homebrew-monsters-5e`; `encounter-prep`; host web search. Existing Work gate and 010 writing/visual stack table stay.

**Storage**: Files. Not a database.

**Testing**: [quickstart.md](./quickstart.md). Classify guidance jobs vs ordinary wiki jobs. Classify combat-instance jobs. No bulk suite. No scanner over `legacy/`.

**Target Platform**: Local DM workstation. Co-DM agent on omp (and other hosts that load `AGENTS.md` plus skills).

**Project Type**: Agent skill pack + standing instructions.

**Performance Goals**: SC-001 / SC-003 — reviewers agree on guidance jobs and on at least 12 combat Work jobs.

**Constraints**: FR-003 no research on ordinary wiki writes. FR-015 craft owners stay owners. FR-016/SC-008 no legacy rewrite. FR-019 outcomes not method (Constitution VII). Constitution IX one source of truth; do not grow `AGENTS.md` with a second table. Existing accept-gate unchanged. No proprietary book paste.

**Scale/Scope**: One description branch plus a short in-file section on `writing-for-agents`. Outcome lines on two combat craft skills. No `src/`.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Gate | Status |
|---|---|
| I. Domain language is binding | Pass — DM, Co-DM, wiki, Work, theatre of the mind. No GM. No knowledge bank. |
| II. Issues are the work surface | Pass — plan does not treat PRs as a request surface. |
| III. Spec before code | Pass — spec has independently testable stories P1–P5. |
| IV. Tests specify behavior | Pass — quickstart observes classification of jobs and named beats, not skill internals. |
| V. Single context | Pass — no second bounded context. No new glossary file. |
| VI. Software is agent-shaped | Pass — existing skills + host web search. No GUI. |
| VII. Do not suffocate agents | Pass — research yields outcomes; techniques are sources. No seventh skill. No extra checklist. No named-person process as the only method. |
| VIII. Safe automation runs unattended | Pass — no new agent chore. Research is judgment on a guidance change, not a formatter hook. |
| IX. Design trends toward token efficiency | Pass — one branch on writing-for-agents; combat outcomes on existing craft descriptions; no AGENTS.md duplicate table; no research on every wiki write. |

**Post-design re-check**: still pass. Contract is classification of a guidance job or a combat Work job. Complexity table empty.

## Project Structure

### Documentation (this feature)

```text
specs/011-narrative-mechanics/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── dnd-content-guidance.md
└── tasks.md             # /speckit.tasks — not this command
```

### Source Code (repository root)

```text
.agents/skills/writing-for-agents/SKILL.md
.agents/skills/homebrew-monsters-5e/SKILL.md
.agents/skills/encounter-prep/SKILL.md
```

**Structure Decision**: Keep skills. `writing-for-agents` owns the research-then-integrate loop for D&D content guidance (description branch + short in-file steps). Combat first instance lives as outcome lines on `homebrew-monsters-5e` and `encounter-prep`. Do not add a skill, a `docs/agents/narrative.md`, or a row to the 010 stack table. Do not edit `legacy/` or rewrite wiki pages. Do not duplicate the loop in `.omp/AGENTS.md`. Host web search is the research tool — do not add one.

## Complexity Tracking

> None. No constitution violations.
