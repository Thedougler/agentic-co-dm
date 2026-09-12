# Implementation Plan: Place Ingest Preserve

**Branch**: `008-place-ingest-preserve` | **Date**: 2026-09-12 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/008-place-ingest-preserve/spec.md`

## Summary

Ingest of `type: place` files the page; it does not distill it. Required open `[!narration]` Narration stays. Place shape stays (Overview + spoken look, At a glance, If the party, Who, What, Where, Why, Art when present). Extend the existing `wiki-ingest` preserve branch (already used for session-prep) to places. File into `wiki/entities/`. No new skill. No `_raw/` rewrite. No legacy restyle. Place run jobs stay in `wiki/AGENTS.md` Layout (006); this feature does not duplicate them.

## Technical Context

**Language/Version**: Markdown skills, wiki templates, owner conventions. Host agent executes skills. No new compiled language.

**Primary Dependencies**: `wiki-ingest`; `wiki/AGENTS.md`; `wiki/templates/place.md`; `obsidian-markdown`; `copy-writer`; `place-design` (pointer only if it still treats ingest as rewrite).

**Storage**: Wiki place pages under `wiki/entities/`. Staging `_raw/`. Not a database.

**Testing**: [quickstart.md](./quickstart.md). Side-by-side source vs ingested place; narration callout present; mixed batch. No bulk lint over legacy.

**Target Platform**: Local DM workstation. Prose wiki the DM opens in Reading view.

**Project Type**: Wiki guidance + agent skill pack.

**Performance Goals**: SC-001 — speak ingested place narration in under 45 seconds.

**Constraints**: FR-001 preserve layout. FR-002 keep `[!narration]`. FR-010 / SC-005 legacy out of scope. Constitution VII — do not freeze Old Gardens as the only outline. Constitution IX — do not copy place jobs into `wiki-ingest`; point at AGENTS.md.

**Scale/Scope**: One ingest-preserve extension for `type: place`. Session-prep preserve unchanged. Items, creatures, people out of scope. No `src/`.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Gate | Status |
|---|---|
| I. Domain language is binding | Pass — wiki, Work, Co-DM, place, theatre of the mind. No knowledge bank. No GM. |
| II. Issues are the work surface | Pass — plan does not treat PRs as a request surface. |
| III. Spec before code | Pass — spec stories P1 ingest narration + P1 format. Independently testable. |
| IV. Tests specify behavior | Pass — quickstart observes narration callout, shape, mixed ingest, legacy untouched. |
| V. Single context | Pass — no second bounded context. |
| VI. Software is agent-shaped | Pass — skill + AGENTS.md; agent files pages; no GUI. |
| VII. Do not suffocate agents | Pass — constrain preserve + required narration block. Do not freeze a named file’s heading list as the only valid place. |
| VIII. Safe automation unattended | Pass — no new agent chore. |
| IX. Token efficiency | Pass — extend existing preserve GUARD; place jobs stay in AGENTS.md Layout. |

**Post-design re-check**: still pass. Contract is the place page the DM opens. Complexity table empty.

## Project Structure

### Documentation (this feature)

```text
specs/008-place-ingest-preserve/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── place-ingest.md
└── tasks.md             # /speckit.tasks — not this command
```

### Source Code (repository root)

```text
.agents/skills/wiki-ingest/SKILL.md
wiki/AGENTS.md                          # pointer only if Layout omits narration-on-ingest
wiki/templates/place.md                 # already has [!narration] Narration; no clone freeze
wiki/_raw/Aruhe - Old Gardens.md        # evidence; do not rewrite
.agents/skills/obsidian-markdown/SKILL.md  # pointer only if live-surface rules skip places
.agents/skills/place-design/SKILL.md       # pointer only if it instructs ingest rewrite
```

**Structure Decision**: One edit surface: `wiki-ingest` preserve GUARD includes `type: place`. File preserved copies to `wiki/entities/` with source filename and body. Session-prep preserve path stays `journal/sessions/…`. Do not add a place-ingest skill.

## Complexity Tracking

> None. No constitution violations.
