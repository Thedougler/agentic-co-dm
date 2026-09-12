# Implementation Plan: NPC Page Standard

**Branch**: `003-npc-page-standard` | **Date**: 2026-09-11 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/003-npc-page-standard/spec.md`

## Summary

Replace the thin NPC wiki outline with one core template plus optional sections, using the four `_raw/` baselines as layout source. `npc-design` files that page after DM accept. No `src/`. No second template per band.

## Technical Context

**Language/Version**: Markdown skills and wiki templates. Host agent executes skills. No new compiled language.

**Primary Dependencies**: `wiki/templates/npc.md`; `wiki/AGENTS.md`; `npc-design`; `copy-writer`; `obsidian-markdown`; four `_raw/` baselines (Hinewai, Talon Skarn, Nona Black-Jaw, Thunk).

**Storage**: Wiki pages. Not a database.

**Testing**: [quickstart.md](./quickstart.md). Observe heading order, omitted empty sections, narration safety, defaults on a minimal contact. No bulk suite.

**Target Platform**: Local DM workstation. Prose wiki the DM opens.

**Project Type**: Wiki template + agent skill pack.

**Performance Goals**: SC-001: role, want, first move, fight handling in under 30 seconds.

**Constraints**: FR-008 omit empty optional headings. FR-018 complete sentences. FR-019 accept-gate unchanged. Constitution I domain language. Constitution VI agent-shaped — template and skill are the tools; no GUI wrapper.

**Scale/Scope**: One `type: npc` template. Four bands. New and touched pages only; no bulk rewrite.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Gate | Status |
|---|---|
| I. Domain language is binding | Pass — wiki, Work, Co-DM, theatre of the mind, `type: npc`. No "knowledge bank". |
| II. Issues are the work surface | Pass — plan does not treat PRs as a request surface. |
| III. Spec before code | Pass — spec exists with independently testable stories. |
| IV. Tests specify behavior | Pass — quickstart observes heading order, empty-heading absence, spoken-look leaks, runnable first meeting. |
| V. Single context | Pass — no second bounded context. |
| VI. Tools are agent-shaped | Pass — one template the agent copies; skill steps with done-when; no human-only wrapper. |

**Post-design re-check**: still pass. Contract is the NPC page the DM opens. Complexity table empty.

## Project Structure

### Documentation (this feature)

```text
specs/003-npc-page-standard/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── npc-page.md
└── tasks.md             # /speckit.tasks — not this command
```

### Source Code (repository root)

```text
wiki/templates/npc.md
wiki/AGENTS.md
wiki/_raw/Hinewai.md
wiki/_raw/Talon Skarn.md
wiki/_raw/Nona Black-Jaw.md
wiki/_raw/Thunk.md
.agents/skills/npc-design/SKILL.md
.agents/skills/npc-design/references/npc-templates.md
```

**Structure Decision**: Keep skills + wiki. One NPC template (core spine only). Band extras live in the contract, not four templates. Baselines stay in `_raw/` as layout source; do not file them to `entities/` in this feature.

## Complexity Tracking

> None. No constitution violations.
