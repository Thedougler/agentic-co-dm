# Implementation Plan: QMD Search Default

**Branch**: `004-qmd-search-default` | **Date**: 2026-09-12 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/004-qmd-search-default/spec.md`

## Summary

Turn vault search on by default in this repo. Project-local QMD index: this `wiki/` is primary. Campaign-of-record collections (`shattered-sea`, `legacy-ss`) are legacy. One agent-shaped maintain script keeps the index current. This wiki wins conflicts.

## Technical Context

**Language/Version**: Markdown skills + bash. Host `qmd` CLI (`@tobilu/qmd`). No new compiled language.

**Primary Dependencies**: `qmd` CLI; `wiki-ingest`; `AGENTS.md`; `CONTEXT.md`; campaign of record at `Documents/ai-co-dm`.

**Storage**: Project-local `.qmd/` index (sqlite gitignored). Collection list in `.qmd/index.yml`.

**Testing**: [quickstart.md](./quickstart.md). Observe: search finds a wiki page; legacy hit marked; maintain script exit 0/1. No bulk suite.

**Target Platform**: Local macOS DM workstation.

**Project Type**: Agent skill pack + local search index + one maintain script.

**Performance Goals**: SC-004 unique phrase findable within 5 minutes after a wiki write.

**Constraints**: FR-001 no skip-if-unset. FR-004 this wiki wins. FR-007 agent-shaped. Constitution VI. Wiki remains source of truth.

**Scale/Scope**: One project index. Three collections: `wiki`, `shattered-sea`, `legacy-ss`. No extra corpora.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Gate | Status |
|---|---|
| I. Domain language is binding | Pass — wiki, Co-DM, campaign of record, ai-co-dm. Add **Search index** to `CONTEXT.md` (gap: QMD is used in skills but missing from the glossary). |
| II. Issues are the work surface | Pass — plan does not treat PRs as a request surface. |
| III. Spec before code | Pass — spec exists with independently testable stories. |
| IV. Tests specify behavior | Pass — quickstart observes findable pages, precedence, maintain exit codes. |
| V. Single context | Pass — no second bounded context. |
| VI. Tools are agent-shaped | Pass — `scripts/qmd-maintain.sh` args in, text/JSON out, exit 0/1. No GUI. |

**Post-design re-check**: still pass. Contracts are CLI + retrieval precedence. Complexity table empty.

## Project Structure

### Documentation (this feature)

```text
specs/004-qmd-search-default/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   ├── qmd-maintain.md
│   └── retrieval-precedence.md
└── tasks.md             # /speckit.tasks — not this command
```

### Source Code (repository root)

```text
.qmd/index.yml                 # tracked collection list (not sqlite)
scripts/qmd-maintain.sh        # init/update/embed/status
CONTEXT.md                     # Search index glossary term
AGENTS.md                      # retrieval is on; this wiki wins
.env.example                   # QMD_* defaults (no secrets)
.agents/skills/qmd/            # installed QMD skill
wiki-ingest Step 8             # call maintain; do not skip if unset
```

**Structure Decision**: Repo-local `qmd init`. Do not use `~/.cache/qmd` as the project index. Do not add `src/`.

## Complexity Tracking

> None. No constitution violations.
