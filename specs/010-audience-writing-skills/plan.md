# Implementation Plan: Audience Writing and Visual Skills

**Branch**: `010-audience-writing-skills` | **Date**: 2026-09-12 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/010-audience-writing-skills/spec.md`

## Summary

Make reader and picture-job the switch for six existing authorities. One always-loaded table in `AGENTS.md` names them and says they stack. Each skill's description is the trigger for its branch. `docs/agents/work.md` and `wiki/AGENTS.md` point at that table instead of hardcoding copy-writer plus obsidian-markdown. No seventh skill. No linter. No legacy rewrite.

## Technical Context

**Language/Version**: Markdown skills and standing agent docs. Host agent executes them. No new compiled language.

**Primary Dependencies**: `AGENTS.md`; `docs/agents/work.md`; `wiki/AGENTS.md`; `writing-for-agents`; `copy-writer`; `theatre-of-the-mind`; `obsidian-markdown`; `visual-references`; `visual-aids`.

**Storage**: Files. Not a database.

**Testing**: [quickstart.md](./quickstart.md). Classify the contract jobs. Observe stacked authorities on mixed writing and depictions. No bulk suite. No scanner over `legacy/`.

**Target Platform**: Local DM workstation. Co-DM agent on omp (and other hosts that load `AGENTS.md` plus skills).

**Project Type**: Agent skill pack + standing instructions.

**Performance Goals**: SC-001 — two reviewers agree on 100% of at least 16 classification jobs.

**Constraints**: FR-012 craft owners stay owners. FR-014/SC-007 no legacy rewrite. Constitution I domain language. Constitution VII no creative-method prescription. Constitution IX one source of truth; standing context stays short. Existing accept-gate unchanged.

**Scale/Scope**: Six authorities. One table. Description rewrites only where a trigger misses a branch or claims another authority's job. Craft skills drop the restated vault-write load line. No `src/`.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Gate | Status |
|---|---|
| I. Domain language is binding | Pass — DM, Co-DM, wiki, Work, theatre of the mind, play surface. No GM. No knowledge bank. |
| II. Issues are the work surface | Pass — plan does not treat PRs as a request surface. |
| III. Spec before code | Pass — spec has independently testable stories P1–P7. |
| IV. Tests specify behavior | Pass — quickstart observes classification and stacked authorities, not skill internals. |
| V. Single context | Pass — no second bounded context. No new glossary file. |
| VI. Software is agent-shaped | Pass — AGENTS.md + skills, no GUI, no human-only wrapper. |
| VII. Do not suffocate agents | Pass — table names authorities and stacking; it does not prescribe voice, camera, or method. No seventh skill. No extra checklist. |
| VIII. Safe automation runs unattended | Pass — no new agent chore. No formatter/index step added to skills. |
| IX. Design trends toward token efficiency | Pass — one table; pointers; delete the duplicated vault-write load line. Descriptions carry one trigger per branch. |

**Post-design re-check**: still pass. Contract is the classification of a writing or visual job. Complexity table empty.

## Project Structure

### Documentation (this feature)

```text
specs/010-audience-writing-skills/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── writing-authorities.md
└── tasks.md             # /speckit.tasks — not this command
```

### Source Code (repository root)

```text
AGENTS.md
docs/agents/work.md
wiki/AGENTS.md
.agents/skills/writing-for-agents/SKILL.md
.agents/skills/copy-writer/SKILL.md
.agents/skills/theatre-of-the-mind/SKILL.md
.agents/skills/obsidian-markdown/SKILL.md
.agents/skills/visual-references/SKILL.md
.agents/skills/visual-aids/SKILL.md
.agents/skills/*/SKILL.md   # work-gate load line only, where it restates the table
```

**Structure Decision**: Keep skills + standing docs. `AGENTS.md` holds the six-row stack table. `.omp/AGENTS.md` already imports `AGENTS.md` — do not duplicate the table there. Do not add a skill, a `docs/agents/writing.md`, or a linter. Do not edit `legacy/` or rewrite wiki pages in this feature.

## Complexity Tracking

> None. No constitution violations.
