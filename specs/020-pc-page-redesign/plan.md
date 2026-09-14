# Implementation Plan: PC Page Redesign

**Branch**: `020-pc-page-redesign` | **Date**: 2026-09-14 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/020-pc-page-redesign/spec.md`

## Summary

Add a `player-characters` owning skill that records player-created characters onto `type: pc` wiki pages. Do not generate PCs or treat them as NPCs. Redesign `wiki/templates/pc.md` to D&D Beyond information groups and order, in Obsidian markdown and columns (not a visual clone). Conform the five live PC owners. Ingest from PDF, prose, Foundry MCP, or other DM-supplied source. Newest supplied source overwrites conflicting wiki numbers; structure-only conformance does not.

There is no `Voice`, `At a Glance`, `Sheet`, `Combat Profile`, `Abilities`, or required DM thesis. The page lists options and numbers; it does not prescribe player actions.

## Technical Context

**Language/Version**: Obsidian Flavored Markdown and agent-facing Markdown instructions; Python 3 for the existing feature-local fixture checker

**Primary Dependencies**: `wiki/AGENTS.md`, `wiki/templates/pc.md`, Obsidian Columns plugin syntax (`col` / `col-md`); skills `player-characters` (new), `npc-design` (exclusion), `pc-interview`, `wiki-ingest`, `reconciling-session-evidence`, `obsidian-markdown`; existing Foundry VTT MCP character tools; existing wiki lint scripts

**Storage**: Markdown files in `wiki/`, archived PC satellites under `wiki/_archive/`, feature artifacts under `specs/020-pc-page-redesign/`

**Testing**: `specs/020-pc-page-redesign/fixtures/check.py`, scoped `./scripts/lint-wiki-write`, strict scoped Markdown lint, `./scripts/wiki-lint --json`, skill-routing inspection, and manual Reading-view/timed-reference review

**Target Platform**: Local Obsidian DM workstation and any agent host that loads repository instructions and the Foundry MCP server when Foundry ingest is used

**Project Type**: Agent skill pack and Markdown knowledge-base schema

**Performance Goals**: A DM can find required PC reference facts for each conformed page in under 60 seconds; an agent can transcribe a representative caster, non-caster, or multiclass from supplied source without npc-design and without inventing missing stats

**Constraints**: Players create PCs; the skill only records them. Keep `type: pc` and `wiki/entities/pc/`. No `Voice` / NPC-dossier spine. No new database, PDF parser, or Foundry client. No visual clone of D&D Beyond chrome. Structure-only conformance preserves facts; ingest from a newer source overwrites conflicting numbers. Unrelated skills stay out of scope.

**Scale/Scope**: One new skill, one rewritten template, five named live PC owner pages, wiki-kind routing plus pointer edits in applicable skills, one fixture, one page-shape contract

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Gate | Status |
|---|---|
| I. Domain language is binding | Pass — uses existing wiki terms `PC`, `player character`, `type: pc`, `owner page`. Skill id `player-characters` is a filename, not a new glossary synonym for NPC. No `_Avoid_` term used. |
| II. Issues are the work surface | Pass — Spec Kit feature workflow; no alternate request surface. |
| III. Spec before code | Pass — `spec.md` has independently testable P1–P4 scenarios and five recorded clarifications. |
| IV. Tests specify behavior | Pass — fixture and quickstart assert page shape, routing, omission, preservation, overwrite-on-ingest, narration safety, and refusal to generate a PC. |
| V. Single context | Pass — existing root context and wiki remain the sole domain context. |
| VI. Software is agent-shaped | Pass — fixture stays an argument-free command; the skill is agent-invoked Markdown procedure; Foundry ingest uses existing MCP tools. |
| VII. Do not suffocate agents | Pass — contract fixes ownership, section homes, agency (no prescribed actions), and named failure modes. Prose craft and player choices stay open. |
| VIII. Safe automation runs unattended | Pass — existing lint remains explicit validation. |
| IX. Design trends toward token efficiency | Pass — one owner page, one skill owner, one numeric home, DDB scan order without cloning chrome. Skill points at the contract instead of restating it. |
| X. Agents act autonomously by default | Pass — deterministic paths and commands. New campaign facts still wait on accept; structure-only conformance does not. |
| XI. Designated writer bounded concurrency | Pass — novel skill and rewritten `wiki/templates/pc.md` are design-impact and MUST go to the designated writer with `writing-for-agents`. Pointer edits and page conformance are session-agent work. |
| XII. Prompt other agents with objectives | Pass — designated-writer prompt can name the skill, template, contract, and acceptance without restating Spec Kit process. |
| XIII. Wiki media filenames distinguish kind | Pass — existing art embeds unchanged; no media minted or renamed. |
| XIV. Use the simplest tool | Pass — Markdown edits, existing lint, existing Foundry MCP, one fixture. No new parser. |
| XV. Wiki page filenames are kebab slugs | Pass — live PC stems already kebab; no spaced rename in this feature. |
| XVI. Named owners before spoken work | Pass — this feature records PC owner pages so named PCs exist before spoken work. It does not invent PCs to fill session prose. |

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
.agents/skills/player-characters/SKILL.md
wiki/templates/pc.md
wiki/entities/pc/
├── jean-claude-tabarnack.md
├── perrin-black-jaw.md
├── catarina-davirelli.md
├── crissdalynn-khinriss.md
└── delmar-fisk.md
wiki/AGENTS.md
.agents/skills/npc-design/SKILL.md
.agents/skills/pc-interview/SKILL.md
.agents/skills/wiki-ingest/SKILL.md
.agents/skills/reconciling-session-evidence/SKILL.md
.agents/skills/obsidian-markdown/SKILL.md
.agents/skills/obsidian-markdown/references/COLUMNS.md
specs/020-pc-page-redesign/fixtures/check.py
```

**Structure Decision**: Keep the current wiki owner-page layout. Add one skill beside existing design skills. Rewrite the PC template in place. Remorph the five owner files. Archived satellites stay immutable evidence. Guidance points at the page contract. Designated writer owns the new skill and template rewrite; session agent owns pointer edits, fixture spine update, and conformance.

## Phase 0: Research

Research is complete in [`research.md`](research.md). It resolves skill ownership and naming, record-only ingest (PDF, prose, Foundry MCP), newest-source overwrite vs structure-only preservation, D&D Beyond spine and column pairs, Actions vs Features, and verification.

## Phase 1: Design

Design is complete in [`data-model.md`](data-model.md), [`contracts/pc-page.md`](contracts/pc-page.md), and [`quickstart.md`](quickstart.md).

- The data model defines frontmatter, DDB section ownership, ingest overwrite, skill state, and invariants.
- The contract defines heading spine, column pairs, agency rules, source kinds, and conflict handling.
- The quickstart defines fixture, lint, skill-routing, Reading-view, preservation, and refuse-to-generate checks.

**Post-design gate**: Pass. No unresolved technical clarifications. No constitution violation requires complexity tracking.

## Complexity Tracking

None.
