---
description: "Task list for NPC Page Standard"
---
# Tasks: NPC Page Standard

**Input**: Design documents from `/specs/003-npc-page-standard/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/, quickstart.md

**Tests**: Not requested. Validate with each story's Independent Test and `specs/003-npc-page-standard/quickstart.md`.

**Organization**: Setup → Foundational → US1 → US2 → US3 → US4 → Polish.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Parallel (different files, no incomplete deps)
- **[Story]**: US1–US4 only on story phases
- Every task names an exact path

## Path Conventions

Wiki: `wiki/`  
Skills: `.agents/skills/<name>/SKILL.md`  
Contracts: `specs/003-npc-page-standard/contracts/`  
Baselines: `wiki/_raw/Hinewai.md`, `wiki/_raw/Talon Skarn.md`, `wiki/_raw/Nona Black-Jaw.md`, `wiki/_raw/Thunk.md`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Point the vault layout table at the NPC template and the four baselines.

- [x] T001 Add an `npc` row to the Layout table in `wiki/AGENTS.md`: sample pages `wiki/_raw/Hinewai.md`, `wiki/_raw/Talon Skarn.md`, `wiki/_raw/Nona Black-Jaw.md`, `wiki/_raw/Thunk.md`; campaign `type` `npc`; template `wiki/templates/npc.md`; two-pane columns allowed (creature notes stay linear)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: One core NPC template. All stories copy it. No optional headings in the file.

**⚠️ CRITICAL**: No user story work until this phase is complete

- [x] T002 Replace `wiki/templates/npc.md` with identity frontmatter and core spine only. Keys and defaults: `title` required; `category` always `entities`; `tags` include `npc`; `sources` required; `created`/`updated` ISO dates; `type` `npc`; `lifecycle` `proposed` until DM accept; `reveal` `unrevealed`; `campaign` current campaign; `status` `alive`; `role` `rival` \| `patron` \| `contact` (required, no silent default); `location` `unknown` when unknown; `faction` `none` when unknown; `visibility` `dm`; `summary` one sentence; omit `aliases` when unused. Body order: `#` title; `## At a Glance` table rows Role, Nature, Home, Wants ending with `> **DM thesis:**`; `[!narration]` spoken look; `## Running {Name}` first move + posture change; `# Relationships` wikilink + meaning. Two-pane column pair as in `wiki/_raw/Thunk.md`. No History, extra form, activity log, knobs, or Combat headings.

**Checkpoint**: Foundation ready — user stories can start

---

## Phase 3: User Story 1 - One page a DM can run without hunting (Priority: P1) 🎯 MVP

**Goal**: New NPC pages use the core spine. A DM finds role, want, first move, and fight handling without hunting.

**Independent Test**: Open each of `wiki/_raw/Hinewai.md`, `wiki/_raw/Talon Skarn.md`, `wiki/_raw/Nona Black-Jaw.md`, `wiki/_raw/Thunk.md` and name role, want, first move, and fight handling without leaving the page.

### Implementation for User Story 1

- [x] T003 [US1] Rewrite the Wiki note structure section in `.agents/skills/npc-design/SKILL.md`: copy `wiki/templates/npc.md`; core order title → At a Glance → spoken look → Running the NPC → Relationships; spoken look is `[!narration]` with no secrets, DCs, unearned names, or DM thesis; keep the Work gate (chat proposal; wiki write after accept)
- [x] T004 [US1] In `.agents/skills/npc-design/SKILL.md`, replace stale paths `wiki/templates/NPC.md` and `wiki/shattered-sea/npcs/Aruhe - Hinewai` with `wiki/templates/npc.md` and the four `wiki/_raw/` baselines

**Checkpoint**: US1 independently testable (spec Independent Test / quickstart Story 1)

---

## Phase 4: User Story 2 - Hostile NPCs share one spine, two depths (Priority: P2)

**Goal**: Landmark and skirmish hostiles share the core spine. Extra hostile sections only when they have content.

**Independent Test**: Author one landmark hostile and one skirmish hostile from the standard; same core heading order; extra hostile sections only on the landmark page.

### Implementation for User Story 2

- [x] T005 [US2] Update Combat handoff in `.agents/skills/npc-design/SKILL.md`: `# Combat` only if fightable; one-sentence encounter rule; on-page fight sheet **or** exactly one pointer, never both; landmark stages keyed to a named condition the party can change, not walking-body hit points alone
- [x] T006 [US2] Update `.agents/skills/npc-design/SKILL.md` for `role: rival`: landmark (Hinewai) extra Glance rows for weakness/return/permanent end when those facts exist, extra form glance+narration pairs, History; skirmish (Skarn) Running must include opening, default turn, pressure response, target priority, counterplay; optional difficulty knobs change tactics or starting position only. Exemplars: `wiki/_raw/Hinewai.md`, `wiki/_raw/Talon Skarn.md`

**Checkpoint**: US1 + US2 independently testable

---

## Phase 5: User Story 3 - Friendly NPCs share one spine, two depths (Priority: P3)

**Goal**: Patrons and contacts share the core spine. Unused patron/combat sections stay gone.

**Independent Test**: Author one patron and one contact from the standard; no empty optional headings; first meeting and current pressure runnable on both.

### Implementation for User Story 3

- [x] T007 [US3] Update `.agents/skills/npc-design/SKILL.md` for `role: patron` and `role: contact`. Patron (Nona): Current pressure; public vs secret when a secret exists; Relationships MAY add invitation; activity log after appearances; omit Combat unless the NPC can fight. Contact (Thunk): core spine plus at most one Current pressure and one practical-use block; no patron ledger, extra forms, or staged sheets. Unique lore sits after Running and before Relationships. Exemplars: `wiki/_raw/Nona Black-Jaw.md`, `wiki/_raw/Thunk.md`

**Checkpoint**: US1–US3 independently testable

---

## Phase 6: User Story 4 - New pages inherit defaults; unused sections stay gone (Priority: P4)

**Goal**: Defaults fill unspecified identity fields. Optional sections appear only with content. One document type, four densities.

**Independent Test**: Create a minimal contact from `wiki/templates/npc.md`; defaults fill identity fields; no empty optional headings.

### Implementation for User Story 4

- [x] T008 [US4] Update `.agents/skills/npc-design/SKILL.md`: omit unused optional sections (no empty History/Combat/activity log/knobs); named-ingest stubs are identity fields + complete sentences with no optional scaffolding; `role` must be supplied (`rival` \| `patron` \| `contact`); add optional sections only from `specs/003-npc-page-standard/contracts/npc-page.md` when they have content
- [x] T009 [P] [US4] Update `.agents/skills/npc-design/references/npc-templates.md`: wiki identity `role` is `rival` \| `patron` \| `contact`; craft labels (informant, gatekeeper, foil, …) stay design notes, not frontmatter; destination table matches `specs/003-npc-page-standard/contracts/npc-page.md`

**Checkpoint**: All four stories independently testable (quickstart Story 2)

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: End-to-end check against the contract.

- [x] T010 Run `specs/003-npc-page-standard/quickstart.md` Stories 1–3 (four baselines scan; do not rewrite `_raw/` bodies in this feature)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: None
- **Foundational (Phase 2)**: After Setup — BLOCKS all stories
- **US1 (Phase 3)**: After Foundational — MVP
- **US2 (Phase 4)**: After Foundational; skill edits after T003–T004 (same file)
- **US3 (Phase 5)**: After Foundational; skill edits after US2 (same file)
- **US4 (Phase 6)**: After Foundational; T008 after US3 skill edits; T009 parallel with T008
- **Polish (Phase 7)**: After desired stories

### User Story Dependencies

- **US1 (P1)**: After Phase 2 only
- **US2 (P2)**: After US1 only because `.agents/skills/npc-design/SKILL.md` is one file
- **US3 (P3)**: After US2 for the same file
- **US4 (P4)**: T008 after US3; T009 independent file

### Parallel Opportunities

- None in Phase 1–2 (single files)
- T003 then T004 (same `SKILL.md` — sequential)
- T005 then T006 (same `SKILL.md` — sequential)
- T009 with T008 (different files)
- Do not parallelize two edits to `.agents/skills/npc-design/SKILL.md`

---

## Parallel Example: User Story 4

```text
Task: Omit-unused + stub rules in .agents/skills/npc-design/SKILL.md (T008)
Task: Identity role vs craft labels in .agents/skills/npc-design/references/npc-templates.md (T009)
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Phase 1 Setup
2. Phase 2 Foundational (`wiki/templates/npc.md`)
3. Phase 3 US1 (`npc-design` points at the template)
4. STOP — quickstart Story 1
5. Demo: open the four `_raw/` baselines; copy the template for a new contact

### Incremental Delivery

1. Setup + Foundational
2. US1 → core spine
3. US2 → hostile bands + Combat contract
4. US3 → friendly bands
5. US4 → defaults + omit-empty
6. Polish → quickstart

---

## Notes

- [P] = different files, no incomplete deps
- No `src/` tree — template + `npc-design`
- Do not add test files unless a later command asks
- Do not file the four baselines into `entities/` in this feature
- Commit after each task or logical group
- Stop at checkpoints
