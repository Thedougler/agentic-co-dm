# Implementation Plan: Sample Content Guidance

**Branch**: `006-aruhe-page-standards` | **Date**: 2026-09-11 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/006-aruhe-page-standards/spec.md`

## Summary

Make distilled run-jobs the default for **sample** pages (place, item/hazard, creature, person). `wiki/AGENTS.md` is the one source of truth. Templates stay copy-start scaffolds. `_raw/` illustrates quality; it is not a clone target. Skills that currently say “match these headings / these named files” point at the jobs instead. Legacy content is not migrated, linted, or restyled.

## Technical Context

**Language/Version**: Markdown skills, wiki templates, owner conventions. Host agent executes skills. No new compiled language.

**Primary Dependencies**: `wiki/AGENTS.md`; `wiki/templates/{place,item,hazard,creature,npc}.md`; `copy-writer`; `obsidian-markdown`; `place-design`; `npc-design`; `homebrew-monsters-5e`; `dnd-5e-magic-item-design`; `wiki-ingest`.

**Storage**: Wiki pages. Not a database.

**Testing**: [quickstart.md](./quickstart.md). Observe jobs answered, empty sections absent, spoken-look safety, owner-link uniqueness, legacy untouched. No bulk suite. No scanner over `legacy/` or historical `wiki/entities/`.

**Target Platform**: Local DM workstation. Prose wiki the DM opens.

**Project Type**: Wiki guidance + agent skill pack.

**Performance Goals**: SC-001 — start play from a complete sample page in under 45 seconds.

**Constraints**: FR-001 samples illustrate, do not clone. FR-001/FR-014/SC-006 legacy out of scope. FR-005 omit empty. FR-006 complete sentences. Existing accept-gate unchanged. Constitution I domain language. Constitution VI — AGENTS.md and skills are the tools; no GUI.

**Scale/Scope**: Five sample kinds. One Layout section. Existing templates, not new types. No `src/`. No bulk rewrite of `_raw/`, filed entities, or `legacy/`.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Gate | Status |
|---|---|
| I. Domain language is binding | Pass — wiki, Work, Co-DM, theatre of the mind, sample content, legacy content. Campaign types `place` / `item` / `creature` / `npc`. No “knowledge bank”. No GM. |
| II. Issues are the work surface | Pass — plan does not treat PRs as a request surface. |
| III. Spec before code | Pass — spec has independently testable stories P1–P5. |
| IV. Tests specify behavior | Pass — quickstart observes runnable jobs, omitted empty sections, spoken-look leaks, owner uniqueness, legacy not rewritten. |
| V. Single context | Pass — no second bounded context. |
| VI. Tools are agent-shaped | Pass — AGENTS.md + skills, done-when on steps, no human-only wrapper. |

**Post-design re-check**: still pass. Contract is the sample page the DM opens. Complexity table empty.

## Project Structure

### Documentation (this feature)

```text
specs/006-aruhe-page-standards/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── sample-page.md
└── tasks.md             # /speckit.tasks — not this command
```

### Source Code (repository root)

```text
wiki/AGENTS.md
wiki/templates/place.md
wiki/templates/item.md
wiki/templates/hazard.md
wiki/templates/creature.md
wiki/templates/npc.md
.agents/skills/copy-writer/SKILL.md
.agents/skills/place-design/SKILL.md
.agents/skills/place-design/references/location-skeleton.md
.agents/skills/npc-design/SKILL.md
.agents/skills/npc-design/references/npc-templates.md
.agents/skills/homebrew-monsters-5e/SKILL.md
.agents/skills/dnd-5e-magic-item-design/SKILL.md
.agents/skills/wiki-ingest/SKILL.md
.agents/skills/obsidian-markdown/SKILL.md
```

**Structure Decision**: Keep skills + wiki. One Layout section in `wiki/AGENTS.md` holds run-jobs. Templates remain optional scaffolds with omit-if-empty. Do not add a sixth template, a linter, or a new skill. Do not edit `legacy/` or rewrite `_raw/` samples in this feature.

## Complexity Tracking

> None. No constitution violations.
