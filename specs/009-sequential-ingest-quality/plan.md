# Implementation Plan: Sequential Ingest Quality

**Branch**: `009-sequential-ingest-quality` | **Date**: 2026-09-12 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/009-sequential-ingest-quality/spec.md`

## Summary

Multi-file ingest is one input file at a time: complete or fail that file (pages filed or stubbed, tracking updated) before the next starts. Parallel batch dispatch is gone. Incoming files are evidence of facts, not exemplary format. Filed pages match campaign kinds and jobs in `wiki/AGENTS.md`. Edit `wiki-ingest`; point at existing Layout. No new skill. No new store.

## Technical Context

**Language/Version**: Markdown skills and owner conventions. Host agent executes skills. No new compiled language.

**Primary Dependencies**: `wiki-ingest`; `wiki/AGENTS.md` Layout (006 jobs); preserve path for campaign-shaped session-prep (007) and place (008); `copy-writer`; `obsidian-markdown`.

**Storage**: Wiki pages. Per-file tracking via existing manifest + `log.md`. Not a database.

**Testing**: [quickstart.md](./quickstart.md). Watched sequential batch; foreign source maps to campaign kind; failed file closes before next. No bulk lint over legacy.

**Target Platform**: Local DM workstation. Co-DM ingest. Prose wiki the DM opens.

**Project Type**: Wiki guidance + agent skill pack.

**Performance Goals**: Quality over throughput. SC-005 — DM reads the per-file ingest record in under one minute. Sequential time for large folders is accepted.

**Constraints**: FR-001–003 sequential complete-before-next. FR-005–008 campaign kinds are the quality bar. Constitution VII — do not freeze a named `_raw/` outline. Constitution IX — do not copy kind jobs into `wiki-ingest`; point at AGENTS.md.

**Scale/Scope**: `wiki-ingest` sequential loop + quality-bar retarget. History ingest follows the same rule if it takes multiple files; this repo’s history skills do not currently fan out. No `src/`.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Gate | Status |
|---|---|
| I. Domain language is binding | Pass — wiki, Work, Co-DM, campaign kind. No knowledge bank. No GM. |
| II. Issues are the work surface | Pass — plan does not treat PRs as a request surface. |
| III. Spec before code | Pass — spec P1 sequential + P1 internal format bar. Independently testable. |
| IV. Tests specify behavior | Pass — quickstart observes file order, kind jobs, ingest record. |
| V. Single context | Pass — no second bounded context. |
| VI. Software is agent-shaped | Pass — skill + AGENTS.md; agent files pages; no GUI. |
| VII. Do not suffocate agents | Pass — constrain sequential unit + quality bar. Do not freeze heading lists or a named sample file. |
| VIII. Safe automation unattended | Pass — no new agent chore. Manifest/log already exist. |
| IX. Token efficiency | Pass — replace parallel Step 0; do not duplicate Layout jobs; `_raw/` stays evidence not clone target. |

**Post-design re-check**: still pass. Contract is the ingest the DM watches and the page they open. Complexity table empty.

## Project Structure

### Documentation (this feature)

```text
specs/009-sequential-ingest-quality/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── sequential-ingest.md
└── tasks.md             # /speckit.tasks — not this command
```

### Source Code (repository root)

```text
.agents/skills/wiki-ingest/SKILL.md     # sequential loop; kill parallel dispatch; quality bar
wiki/AGENTS.md                          # ingest judges against Layout kinds, not source outline
wiki/log.md                             # per-file complete/failed lines (existing log)
wiki/.manifest.json                     # per-file tracking after each complete file (existing)
```

**Structure Decision**: One edit surface: `wiki-ingest`. Sequential file loop replaces Step 0 parallel subagents. Quality target is `wiki/AGENTS.md` Layout. Preserve for *campaign-shaped* session-prep and place stays (required treatments). Foreign sources map into the kind; they are not photocopied. Do not add an ingest-orchestrator skill or a new log format.

## Complexity Tracking

> None. No constitution violations.
