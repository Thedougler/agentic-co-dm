# Implementation Plan: Complete Ingest Context

**Branch**: `018-complete-ingest-context` | **Date**: 2026-09-12 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/018-complete-ingest-context/spec.md`

## Summary

Wiki ingest of a named primary is complete only after the Co-DM searches for and reads linked, related, and corroborating sources implied by that primary’s content. Search both the staging area and the campaign-of-record legacy collections. Newest files are the DM’s latest decisions; older versions and variants remain supporting context and must not silently override. Related reads happen inside the open primary; they do not overlap another named ingest.

Implementation is a focused change to the existing `wiki-ingest` workflow. No new skill, ingest engine, collection, or query-time precedence rewrite.

## Technical Context

**Language/Version**: Markdown skill instructions executed by the host agent; existing `qmd` CLI and `scripts/qmd-maintain.sh`

**Primary Dependencies**: `wiki-ingest`, search index (QMD), `llm-wiki` Config Resolution, existing retrieval collections (`wiki`, `shattered-sea`, `legacy-ss`, `legacy`)

**Storage**: Vault Markdown; `_raw/` staging; campaign-of-record collections; `.manifest.json`, `index.md`, `log.md`, `hot.md`

**Testing**: One runnable fixture-based ingest-context check at the public seam (related reads, recency, misses, sequential non-overlap, ingest record). No bulk suite. Do not snapshot skill wording.

**Target Platform**: Local DM workstation and any agent host that loads repository skills

**Project Type**: Agent skill pack and documentation workflow

**Performance Goals**: Related discovery stays bounded to the primary’s content and subject. A primary with no related hits still completes. Related reads do not start a second named ingest.

**Constraints**: Sequential named-file ingest (009) still holds. Compiled wiki remains current canon vs legacy (004). Files remain evidence, not photocopies (015). Unaccepted Work does not publish except named ingest of approved sources. Do not crawl the whole vault. Do not add a second wiki or a wrapper around `qmd`.

**Scale/Scope**: One ingest skill and its ingest-record fields. Query-time lookup order is unchanged. No compiled application code.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Gate | Status |
|---|---|
| I. Domain language is binding | Pass — primary source, related source, Wiki, Work, canon proposal, DM, Co-DM, staging area, legacy collection, latest decision, supporting context. |
| II. Issues are the work surface | Pass — this plan specifies the feature workflow, not a new request surface. |
| III. Spec before code | Pass — spec has independently testable P1–P2 scenarios. |
| IV. Tests specify behavior | Pass — fixtures observe related reads, recency, misses, sequential non-overlap, and the ingest record. Not instruction wording. |
| V. Single context | Pass — no new glossary or parallel store. |
| VI. Software is agent-shaped | Pass — agent-readable skill plus existing `qmd` CLI. No GUI wrapper. |
| VII. Do not suffocate agents | Pass — outcomes and named failures only; discovery method inside the bound is not a single prescribed outline. |
| VIII. Safe automation runs unattended | Pass — reuses existing QMD maintenance; adds no manual chore. |
| IX. Design trends toward token efficiency | Pass — one owner skill; point at 004/009/015 instead of restating them. |
| X. Agents act autonomously by default | Pass — no new human git/context ritual. |
| XI. Designated writer bounded concurrency | Pass — skill edit is design-impact; implement dispatches one writer; this plan does not write the skill. |
| XII. Prompt other agents with objectives | Pass — implement uses a scoped prompt (outcome, files, bounds, job). |
| XIII. Wiki media filenames distinguish kind | Pass — media stays on the existing linked-art path; this feature is corroborating text sources. |
| XIV. Use the simplest tool | Pass — `qmd` CLI for collection search; filesystem read for `_raw/`; no new launcher. |

## Project Structure

### Documentation (this feature)

```text
specs/018-complete-ingest-context/
├── spec.md
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
└── contracts/
    └── complete-ingest-context.md
```

### Source Changes

```text
.agents/skills/wiki-ingest/SKILL.md
```

**Structure Decision**: Keep `wiki-ingest` as the workflow owner. Add a complete-context pass inside the open primary (after the primary is read, before extract/compile). Do not create a second skill. Do not copy ingest-time search into query-time `AGENTS.md` retrieval. Progressive disclosure to `references/` only if the step would duplicate standing guidance; prefer one file.

Implementation of that skill edit is **design-impact**. The session agent writes these Spec Kit artifacts only. The skill file is unmodified until `/speckit.implement` dispatches the designated writer.

## Complexity Tracking

None. Reuses existing skill, collections, sequential unit, and tracking surfaces.

## Phase 0: Research

- Confirm ingest-time search is not query-time precedence (004 short-circuit would skip legacy).
- Confirm related reads are not a second sequential ingest unit (009).
- Reconcile recency (018) with “newest source ≠ silent canon” (015).
- Confirm discovery bound: primary content and subject, not a vault crawl.
- Confirm designated-writer dispatch for the skill edit.

## Phase 1: Design

- Model primary, related source, recency rank, supporting context, miss, and ingest-record fields.
- Document the agent-facing complete-context contract.
- Provide fixture scenarios for staging relative, legacy variant, recency conflict, miss, no-related, and sequential non-overlap.

**Post-design gate**: Constitution checks above still pass. No unresolved technical unknowns remain.
