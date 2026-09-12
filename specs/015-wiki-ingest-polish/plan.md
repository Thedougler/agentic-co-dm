# Implementation Plan: Wiki Ingest Polish

**Branch**: `015-wiki-ingest-polish` | **Date**: 2026-09-12 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/015-wiki-ingest-polish/spec.md`

## Summary

Treat every ingestion input as evidence containing ideas. Route each idea into the relevant existing wiki page or a justified new page, then apply the same applicable creation standards used for new content. Preserve settled intent, surface canon conflicts, keep audience boundaries intact, and leave source tracking and staging behavior explicit.

Implementation is a focused update to the existing `wiki-ingest` workflow and its supporting quality guidance. No new ingestion engine, storage model, or parallel processing path is needed.

## Technical Context

**Language/Version**: Markdown skill instructions executed by the host agent; shell maintenance scripts already present

**Primary Dependencies**: `wiki-ingest`, `llm-wiki`, `copy-writer`, `obsidian-markdown`, `theatre-of-the-mind`, `dnd5e-mechanics`, `wiki/AGENTS.md`

**Storage**: Obsidian Markdown files, `_raw/` and `_archive/` staging paths, `.manifest.json`, `index.md`, `log.md`, and `hot.md`

**Testing**: Existing repository validators and one runnable fixture-based ingestion smoke check; no bulk suite

**Target Platform**: Local DM workstation and any agent host that loads repository skills and `AGENTS.md`

**Project Type**: Agent skill pack and documentation workflow

**Performance Goals**: A single source file is fully routed and quality-checked without duplicate page creation; normal ingestion remains sequential per existing workflow

**Constraints**: Preserve raw-source safety, DM approval gates for canon, existing page types and layouts, complete-sentence prose, required frontmatter, provenance, links, and audience/reveal boundaries. Do not add a second wiki or rewrite legacy evidence.

**Scale/Scope**: One ingestion skill and its directly referenced quality guidance; existing tracking surfaces remain authoritative. No compiled application code.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Gate | Status |
|---|---|
| I. Domain language is binding | Pass — uses source idea, Wiki, Work, canon proposal, DM, Co-DM, and existing campaign types. |
| II. Issues are the work surface | Pass — this plan changes the specified feature workflow, not the request surface. |
| III. Spec before code | Pass — spec has independently testable P1–P3 scenarios. |
| IV. Tests specify behavior | Pass — validation observes routed pages, preserved intent, quality compliance, and tracking rather than instruction wording. |
| V. Single context | Pass — no new context, glossary, or parallel store. |
| VI. Software is agent-shaped | Pass — existing agent-readable skill workflow and text artifacts remain the interface. |
| VII. Do not suffocate agents | Pass — requirements constrain outcomes and named failure modes, not a single editorial method. |
| VIII. Safe automation runs unattended | Pass — reuses existing tracking and maintenance automation; adds no manual chore. |
| IX. Design trends toward token efficiency | Pass — one owner skill, existing standards as sources of truth, no duplicated standing guidance. |

## Project Structure

### Documentation (this feature)

```text
specs/015-wiki-ingest-polish/
├── spec.md
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
└── contracts/
    └── ingest-quality.md
```

### Source Changes

```text
.agents/skills/wiki-ingest/SKILL.md
.agents/skills/wiki-ingest/references/ingest-prompts.md   # only if prompt guidance needs alignment
.agents/skills/copy-writer/SKILL.md                       # only if cross-skill ingest handoff needs alignment
```

**Structure Decision**: Keep the existing skill-based workflow. `wiki-ingest` owns source classification, routing, provenance, and completion; existing craft skills own quality checks for their surfaces. The design artifacts define the seam without introducing a new runtime module or page type.

## Complexity Tracking

None. The plan reuses existing files, standards, and tracking surfaces.

## Phase 0: Research

- Confirm the existing ingest lifecycle and source-trust boundary.
- Confirm page-quality authorities and campaign metadata requirements.
- Confirm staging, manifest, index, log, and raw-source behavior.
- Resolve whether any external interface needs a contract; the command-facing skill contract is documented because agents consume it directly.

## Phase 1: Design

- Model source ideas, destinations, quality status, provenance, and conflict outcomes.
- Document the agent-facing ingestion quality contract.
- Provide fixture scenarios covering update, new-page, duplicate, insufficient-source, conflict, and audience-boundary cases.

**Post-design gate**: The design preserves the constitution checks above; no unresolved technical unknowns remain.
