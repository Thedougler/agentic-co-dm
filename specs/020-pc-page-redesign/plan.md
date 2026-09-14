# Implementation Plan: PC Page Redesign

**Branch**: `020-pc-page-redesign` | **Date**: 2026-09-14 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/020-pc-page-redesign/spec.md`

## Summary

Redesign the existing `type: pc` Obsidian owner-page template around one predictable, single-H1 page: player-safe narration, orientation, connections, canonical Sheet numbers, Combat Profile interpretation, abilities, conditional spells, inventory, session changes, and optional art. Pair identity and mechanical surfaces with supported fenced `col` / `col-md` blocks while keeping headings and tables readable linearly. Conform the five live PC owners and reconcile PC creation, ingest, reconciliation, and Markdown guidance to one contract without changing campaign facts.

There is no `Voice` section. PCs are player-controlled; existing voice-script facts are either moved into an existing decision-relevant section or remain attributable source evidence. No DM voice-performance instructions are introduced.

## Technical Context

**Language/Version**: Obsidian Flavored Markdown and agent-facing Markdown instructions; Python 3 for a feature-local fixture checker

**Primary Dependencies**: Existing `wiki/AGENTS.md` and `wiki/templates/pc.md`; Obsidian Columns plugin syntax; `obsidian-markdown`, `pc-interview`, `wiki-ingest`, and `reconciling-session-evidence` skills; existing wiki lint scripts

**Storage**: Markdown files in `wiki/`, archived PC satellites under `wiki/_archive/`, and feature artifacts under `specs/020-pc-page-redesign/`

**Testing**: `specs/020-pc-page-redesign/fixtures/check.py`, scoped `./scripts/lint-wiki-write`, strict scoped Markdown lint, `./scripts/wiki-lint --json`, and manual Reading-view/timed-reference review

**Target Platform**: Local Obsidian DM workstation and any agent host that loads repository instructions

**Project Type**: Agent skill pack and Markdown knowledge-base schema

**Performance Goals**: A DM can find required PC reference facts for each conformed page in under 60 seconds; an agent can place facts from a representative caster, non-caster, or multiclass source without opening unrelated satellite pages

**Constraints**: Preserve existing facts, sources, aliases, art, lifecycle, reveal, visibility, campaign, and player handles. Keep `type: pc` and `wiki/entities/pc/`. Flatten satellite representations without dropping facts. Use codeblock `col` / `col-md` for PC pairs, narration outside fences, and linear fallback. Omit empty conditional sections. No `Voice` section, DM voice-performance guidance, new skill, new campaign type, new database, or invented conflict resolution. Unrelated skills and legacy checker behavior stay out of scope.

**Scale/Scope**: One template, five named live PC owner pages, four applicable workflow/guidance files plus `wiki/AGENTS.md`, one feature-local fixture checker, and one page-shape contract

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Gate | Status |
|---|---|
| I. Domain language is binding | Pass — `PC`, `player character`, `owner page`, `Sheet`, `Combat Profile`, `Work`, and `Wiki` follow `CONTEXT.md` and current wiki vocabulary. `Voice` is explicitly removed from the feature contract after the owner correction. |
| II. Issues are the work surface | Pass — this is a Spec Kit feature workflow; no alternate request surface is introduced. |
| III. Spec before code | Pass — `spec.md` contains independently testable P1–P4 scenarios and was corrected before this plan to remove the invalid `Voice` requirement. |
| IV. Tests specify behavior | Pass — the fixture and manual checks assert page shape, routing, omission, preservation, links, narration safety, and rendered scan behavior rather than instruction wording or implementation. |
| V. Single context | Pass — the existing root context and wiki remain the sole domain context; no glossary or second vault is added. |
| VI. Software is agent-shaped | Pass — the fixture is an argument-free repository command with text/JSON-compatible exit behavior; Markdown guidance names paths and observable completion criteria. |
| VII. Do not suffocate agents | Pass — the contract fixes observable safety, ownership, section homes, and failure modes while leaving prose craft and player choices open. |
| VIII. Safe automation runs unattended | Pass — existing lint commands remain explicit validation; no hidden human-only automation is added. |
| IX. Design trends toward token efficiency | Pass — one owner page replaces satellite retrieval, one numeric home avoids duplicate dumps, and paired surfaces improve scan without deleting narrative or mechanics. |
| X. Agents act autonomously by default | Pass — template, guidance, conformance, and validation artifacts have deterministic repository locations and commands. Approval rules remain unchanged for facts. |
| XI. Designated writer bounded concurrency | Pass — this plan contains no source skill edit. Any major skill redesign during implementation is dispatched to the designated writer; session-agent work remains limited to non-design edits. |
| XII. Prompt other agents with objectives | Pass — implementation can use the scoped page-contract and file list without restating standing process. |
| XIII. Wiki media filenames distinguish kind | Pass — existing art embeds and attachment naming remain unchanged; no media is minted or renamed. |
| XIV. Use the simplest tool | Pass — Markdown edits use repository editing tools, existing lint scripts, and one fixture; no AST or column parser is added. |

## Project Structure

### Documentation (this feature)

```text
specs/020-pc-page-redesign/
├── spec.md
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── pc-page.md
└── fixtures/
    └── check.py
```

### Source Changes

```text
wiki/templates/pc.md
wiki/entities/pc/
├── jean-claude-tabarnack.md
├── perrin-black-jaw.md
├── catarina-davirelli.md
├── crissdalynn-khinriss.md
└── delmar-fisk.md
wiki/AGENTS.md
.agents/skills/pc-interview/SKILL.md
.agents/skills/wiki-ingest/SKILL.md
.agents/skills/reconciling-session-evidence/SKILL.md
.agents/skills/obsidian-markdown/SKILL.md
.agents/skills/obsidian-markdown/references/COLUMNS.md
specs/020-pc-page-redesign/fixtures/check.py
```

**Structure Decision**: Keep the current wiki owner-page and skill layout. The template remains the single PC scaffold; five existing owner files are remorphed in place. Archived satellites remain immutable evidence. Guidance points to the page contract rather than cloning it. The fixture is feature-local because no generic PC conformance checker exists and existing root page checking does not recognize `type: pc`.

## Phase 0: Research

Research is complete in [`research.md`](research.md). It resolves the current owner/template paths, supported column syntax, frontmatter and lint rules, stale interview paths, source-satellite policy, conflicting-source handling, no-`Voice` player-control boundary, and the absence of a reusable PC fixture or column parser.

## Phase 1: Design

Design is complete in [`data-model.md`](data-model.md), [`contracts/pc-page.md`](contracts/pc-page.md), and [`quickstart.md`](quickstart.md).

- The data model defines frontmatter, section ownership, relationships, satellite disposition, and invariants.
- The contract defines the exact heading spine, fenced column pairs, one-owner number rule, omission behavior, narration safety, and conflict handling.
- The quickstart defines fixture, lint, wiki-schema, Reading-view, timed-review, and source-preservation checks.
- Implementation must conform all five owners without silently changing campaign facts and must update only the listed applicable guidance.

**Post-design gate**: Pass. The corrected specification, research, model, contract, and quickstart contain no unresolved technical clarifications. No constitution violation requires complexity tracking.

## Complexity Tracking

None.
