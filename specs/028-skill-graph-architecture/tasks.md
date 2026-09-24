---

description: "Implementation tasks for the skill graph architecture"
---

# Tasks: Skill Graph Architecture

**Input**: Design documents from `/specs/028-skill-graph-architecture/`

**Prerequisites**: `plan.md`, `spec.md`, `research.md`, `data-model.md`, `contracts/capability-boundaries.md`, `quickstart.md`

**Tests**: Required. The specification and constitution require cold, focused behavioral evaluation for agent-facing changes.

**Organization**: Tasks are grouped by user story. Each story has an independently runnable acceptance scenario; shared authority and evaluation prerequisites live in Setup and Foundational.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel because it changes disjoint files and has no incomplete prerequisite.
- **[Story]**: Maps the task to a user story in `spec.md`.
- Every implementation task names its write surface and its verification surface.

## Phase 1: Setup (Accountability and Inventory)

**Purpose**: Establish the tracked work surface and derive the complete named set from live authority before editing guidance.

- [X] T001 Create or link the accountable implementation issue and record its URL beside the implementation gate in `specs/028-skill-graph-architecture/plan.md`
- [X] T002 Reconcile every live wiki-facing route in `AGENTS.md` with existing skill paths and `docs/agents/policy-owners.yml`; correct absent-owner routes to the established owner and record each resolved conflict in `specs/028-skill-graph-architecture/plan.md`
- [X] T003 Capture the pre-change cold-routing baseline for V-001 through V-007 with the weakest sufficient model in `specs/028-skill-graph-architecture/quickstart.md`


---

## Phase 2: Foundational (Authority Chain and Evaluation Contract)

**Purpose**: Establish canonical pointers and shared behavioral assertions before owner-specific changes.

**⚠️ CRITICAL**: Do not remove duplicate skill procedure or begin owner normalization until these authority surfaces are complete.

- [X] T004 Update direct intent-to-owner routing, global invariants, parent-return semantics, and read/write isolation in `AGENTS.md`
- [X] T005 Update cross-capability dependency, context projection, handoff, and completion composition in `docs/agents/hybrid-sdd.md`
- [X] T006 Update wiki semantic/output pointers without duplicating owner procedures in `wiki/AGENTS.md`
- [X] T007 Reconcile governing-counterpart ownership for the changed guidance in `docs/agents/policy-owners.yml`
- [X] T008 Define the cold typed assertion matrix for direct routing, parent return, dependency order, bounded context, read-only behavior, validation feedback, specialized craft, and forbidden machinery in `specs/028-skill-graph-architecture/quickstart.md`

**Checkpoint**: Root, composition, wiki semantics, and evaluation assertions have one explicit authority each.

---

## Phase 3: User Story 1 - Enter the Correct Capability (Priority: P1) 🎯 MVP

**Goal**: Route representative requests directly to the existing owner, preserve subtype seams, and keep read-only work non-mutating.

**Independent Test**: Run V-001 and V-004 from `specs/028-skill-graph-architecture/quickstart.md`; faction, wiki-question, page-repair, typed-beat, and city requests select their named owner with no generic intermediate capability, and read requests leave canonical wiki state unchanged.

### Behavioral Tests for User Story 1

- [X] T009 [P] [US1] Add failing direct-owner and read-only assertions to `.agents/skills/wiki-query/evals/evals.json`
- [X] T010 [P] [US1] Add failing direct-owner and semantic-repair-handoff assertions to `.agents/skills/wiki-lint/evals/evals.json`
- [X] T011 [P] [US1] Add failing kind-owner and subtype-handoff assertions to `.agents/skills/faction-design/evals/evals.json`, `.agents/skills/city-design/evals/evals.json`, and `.agents/skills/session-beats/evals/evals.json`

### Implementation for User Story 1

- [X] T012 [P] [US1] Make read ownership, evidence sufficiency, and no-canonical-mutation completion explicit in `.agents/skills/wiki-query/SKILL.md`, `.agents/skills/wiki-context-pack/SKILL.md`, `.agents/skills/wiki-narrate/SKILL.md`, `.agents/skills/memory-bridge/SKILL.md`, and `.agents/skills/session-search/SKILL.md`
- [X] T013 [P] [US1] Make direct named-owner entry and local subtype handoff explicit in `.agents/skills/faction-design/SKILL.md`, `.agents/skills/city-design/SKILL.md`, `.agents/skills/region-design/SKILL.md`, `.agents/skills/place-design/SKILL.md`, and `.agents/skills/session-beats/SKILL.md`
- [X] T014 [US1] Run V-001 and V-004 and record route, loaded context, canonical-state diff, and pass/fail evidence in `specs/028-skill-graph-architecture/quickstart.md`

**Checkpoint**: Correct owner selection and read-only isolation pass independently.

---

## Phase 4: User Story 2 - Complete Cross-Capability Work (Priority: P1)

**Goal**: Preserve the parent objective through bounded child work, valid dependency order, safe concurrency, rejoin, and return.

**Independent Test**: Run V-002 with missing faction and place owners; disjoint owner writes remain concurrent-eligible, dependent spoken work waits, and the parent session artifact closes after both child contracts pass.

### Behavioral Tests for User Story 2

- [X] T015 [P] [US2] Add a failing parent-return and dependency-order scenario to `.agents/skills/session-beats/evals/evals.json`
- [X] T016 [P] [US2] Add failing child-scope and return-evidence assertions to `.agents/skills/faction-design/evals/evals.json` and `.agents/skills/place-design/evals/evals.json`
- [X] T017 [P] [US2] Add a failing deterministic-to-owner repair loop scenario to `.agents/skills/wiki-lint/evals/evals.json`

### Implementation for User Story 2

- [X] T018 [P] [US2] Define bounded child output, return evidence, rejoin, and parent resume in `.agents/skills/session-beats/SKILL.md`, `.agents/skills/run-guide/SKILL.md`, and `.agents/skills/theatre-of-the-mind/SKILL.md`
- [X] T019 [P] [US2] Define owner-return contracts for missing faction and place dependencies in `.agents/skills/faction-design/SKILL.md`, `.agents/skills/place-design/SKILL.md`, `.agents/skills/city-design/SKILL.md`, and `.agents/skills/region-design/SKILL.md`
- [X] T020 [P] [US2] Define semantic-finding handoff, deterministic repair, owner return, and affected-scope rerun in `.agents/skills/wiki-lint/SKILL.md`
- [X] T021 [US2] Run V-002 and the lint handoff case from V-005 and record dependency order, concurrent-eligible children, rejoin, and completion evidence in `specs/028-skill-graph-architecture/quickstart.md`

**Checkpoint**: Cross-capability work completes the original objective without task drift.

---

## Phase 5: User Story 3 - Load Bounded Context at Each Boundary (Priority: P2)

**Goal**: Give each capability its minimum sufficient owner, target, canon, contract, validation, dependency, and omission context; deepen only when evidence is insufficient.

**Independent Test**: Run V-003 for a targeted place edit after broader session planning; the place owner receives relevant place/campaign evidence, omits unrelated prior-child artifacts, and resumes after focused retrieval only when needed.

### Behavioral Tests for User Story 3

- [X] T022 [P] [US3] Add a failing context-projection and focused-retrieval scenario to `.agents/skills/place-design/evals/evals.json`
- [X] T023 [P] [US3] Add failing sufficient-evidence stop and no-parent-context-inheritance assertions to `.agents/skills/wiki-context-pack/evals/evals.json` and `.agents/skills/wiki-query/evals/evals.json`

### Implementation for User Story 3

- [X] T024 [P] [US3] Define minimum context projection, deliberate omissions, evidence sufficiency, and same-owner retrieval resume in `.agents/skills/place-design/SKILL.md`, `.agents/skills/wiki-query/SKILL.md`, and `.agents/skills/wiki-context-pack/SKILL.md`
- [X] T025 [P] [US3] Apply the same bounded-context contract to ingest parents in `.agents/skills/wiki-ingest/SKILL.md`, `.agents/skills/wiki-update/SKILL.md`, `.agents/skills/wiki-capture/SKILL.md`, `.agents/skills/wiki-agent/SKILL.md`, and `.agents/skills/wiki-history-ingest/SKILL.md`
- [X] T026 [US3] Run V-003 and record per-capability files supplied, omitted artifact groups, retrieval deepening, and stop conditions in `specs/028-skill-graph-architecture/quickstart.md`

**Checkpoint**: Context is complete for the owned slice and excludes unrelated inherited material.

---

## Phase 6: User Story 4 - Close Work on Observable Evidence (Priority: P2)

**Goal**: Close write and maintenance branches only on valid output contracts, green affected scope, or a specific owner-level blocker.

**Independent Test**: Run V-005 and V-006 on a disposable configured vault; deterministic findings use registered repair, semantic findings return to the owner, affected scope reruns, and health action ordering is consumed without reranking.

### Behavioral Tests for User Story 4

- [X] T027 [P] [US4] Add failing write-completion and tracking/finalization assertions to `.agents/skills/wiki-ingest/evals/evals.json`, `.agents/skills/wiki-update/evals/evals.json`, and `.agents/skills/wiki-capture/evals/evals.json`
- [X] T028 [P] [US4] Add failing health-order and no-second-planner assertions to `.agents/skills/wiki-status/evals/evals.json`
- [X] T029 [P] [US4] Add failing clean-or-specific-blocker assertions to `.agents/skills/wiki-lint/evals/evals.json`

### Implementation for User Story 4

- [X] T030 [P] [US4] Make output-contract validation, one-time tracking/finalization, and clean-or-blocker completion explicit in `.agents/skills/wiki-ingest/SKILL.md`, `.agents/skills/wiki-update/SKILL.md`, `.agents/skills/wiki-capture/SKILL.md`, `.agents/skills/wiki-agent/SKILL.md`, and `.agents/skills/wiki-history-ingest/SKILL.md`
- [X] T031 [P] [US4] Make health ordering, complete lint findings, registered repair, semantic owner return, and scoped rerun explicit in `.agents/skills/wiki-status/SKILL.md`, `.agents/skills/wiki-lint/SKILL.md`, `.agents/skills/daily-update/SKILL.md`, and `docs/agents/wiki-maintenance-loop.md`
- [X] T032 [P] [US4] Make observable completion and owner handoff explicit in `.agents/skills/wiki-rebuild/SKILL.md`, `.agents/skills/wiki-export/SKILL.md`, and `.agents/skills/wiki-switch/SKILL.md`
- [X] T033 [US4] Run V-005 and V-006 through `scripts/wiki lint`, `scripts/wiki lint fix`, and `scripts/wiki health`, then record findings, actions, reruns, and final status in `specs/028-skill-graph-architecture/quickstart.md`

**Checkpoint**: No write or maintenance task succeeds because prose merely exists.

---

## Phase 7: User Story 5 - Maintain Legible Capability Contracts (Priority: P3)

**Goal**: Expose Input, Work, Done, and Capability Handoff or clear equivalents across the complete live wiki-facing owner set while preserving owner-specific craft.

**Independent Test**: Run V-007 against every live route in `AGENTS.md`; all four boundary concepts are identifiable, owner-specific completion and craft remain, duplicated lower-authority procedure is removed only after a canonical pointer exists, and no forbidden orchestration machinery appears.

### Behavioral Tests for User Story 5
- [X] T034 [US5] Extend the cold review matrix to every live root-routed wiki-facing capability and every named failure in `spec.md` using `.agents/skills/skill-creator/scripts/run-eval.py` and record the command matrix in `specs/028-skill-graph-architecture/quickstart.md`

### Implementation for User Story 5

- [X] T035 [P] [US5] Normalize Input, Work, Done, and Capability Handoff while preserving craft in `.agents/skills/cross-linker/SKILL.md`, `.agents/skills/tag-taxonomy/SKILL.md`, `.agents/skills/wiki-dedup/SKILL.md`, `.agents/skills/wiki-import/SKILL.md`, `.agents/skills/wiki-research/SKILL.md`, `.agents/skills/wiki-synthesize/SKILL.md`, `.agents/skills/wiki-dashboard/SKILL.md`, and `.agents/skills/graph-colorize/SKILL.md`
- [X] T036 [P] [US5] Normalize the remaining read, maintenance, and history boundaries in `.agents/skills/wiki-narrate/SKILL.md`, `.agents/skills/memory-bridge/SKILL.md`, `.agents/skills/session-search/SKILL.md`, `.agents/skills/daily-update/SKILL.md`, `.agents/skills/wiki-rebuild/SKILL.md`, `.agents/skills/wiki-export/SKILL.md`, and `.agents/skills/wiki-switch/SKILL.md`
- [X] T037 [P] [US5] Normalize typed-beat and presentation boundaries while preserving their completion tests in `.agents/skills/hook-beats/SKILL.md`, `.agents/skills/development-beats/SKILL.md`, `.agents/skills/cliffhanger-beats/SKILL.md`, `.agents/skills/climax-beats/SKILL.md`, `.agents/skills/resolution-beats/SKILL.md`, `.agents/skills/run-guide/SKILL.md`, and `.agents/skills/theatre-of-the-mind/SKILL.md`
- [X] T038 [P] [US5] Normalize artifact-owner boundaries while preserving distinct craft in `.agents/skills/lore-design/SKILL.md`, `.agents/skills/narrative-islands/SKILL.md`, `.agents/skills/vehicle-design/SKILL.md`, `.agents/skills/spell-design/SKILL.md`, `.agents/skills/npc-design/SKILL.md`, `.agents/skills/encounter-prep/SKILL.md`, and `.agents/skills/dungeon-design/SKILL.md`
- [X] T039 [P] [US5] Normalize challenge, travel, creature, item, and Foundry staging boundaries while preserving distinct craft in `.agents/skills/traps-trials/SKILL.md`, `.agents/skills/travel-events/SKILL.md`, `.agents/skills/homebrew-monsters-5e/SKILL.md`, `.agents/skills/dnd-5e-magic-item-design/SKILL.md`, and `.agents/skills/foundry-stage/SKILL.md`
- [X] T040 [US5] Remove superseded duplicate workflow prose only after pointer coverage is verified in `AGENTS.md`, `docs/agents/hybrid-sdd.md`, `wiki/AGENTS.md`, and the owner files changed by T035 through T039
- [X] T041 [US5] Run V-007 with the weakest sufficient model and record per-owner boundary visibility, preserved craft, named-failure coverage, and forbidden-machinery review in `specs/028-skill-graph-architecture/quickstart.md`

**Checkpoint**: The whole live named set has legible boundaries without a universal schema or flattened craft.

---

## Phase 8: Polish & Cross-Cutting Verification

**Purpose**: Synchronize only governing counterparts, run real repository surfaces, and leave complete evidence.
- [X] T042 Assess every changed behavior against the synchronization contract and update only affected `wiki/templates/`, `rules/`, `styles/`, consuming skills, and public-seam tests; record unchanged counterparts with reasons in `specs/028-skill-graph-architecture/quickstart.md`
- [X] T043 [P] Run targeted skill-creator evaluations with the weakest sufficient executor and record typed results in `specs/028-skill-graph-architecture/quickstart.md`
- [X] T044 [P] Run applicable targeted pytest public-seam tests for any runtime contract changed and record the exact paths/results in `specs/028-skill-graph-architecture/quickstart.md`
- [X] T045 Run `scripts/check-omp-baseline.sh` and `specify integration status --json`, recording exit status and the `ok`/`omp`/four-integrations evidence in `specs/028-skill-graph-architecture/quickstart.md`
- [X] T046 Run `scripts/wiki lint` on every affected real wiki scope when wiki/template/validation behavior changed and record clean scope or a specific blocker in `specs/028-skill-graph-architecture/quickstart.md`
- [X] T047 Record final route, context used/omitted, owners affected/resolved, dependencies, deterministic checks, cold quality review, work status, unchanged campaign canon, filing, and measured/estimated/inferred context results in `specs/028-skill-graph-architecture/quickstart.md`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: Starts immediately; T001 is the implementation gate. T002 derives the whole named set. T003 establishes the baseline.
- **Foundational (Phase 2)**: Depends on Setup. T004 → T005 → T006 are serial shared authority surfaces. T007 and T008 follow their governing authority changes.
- **User Story 1 (Phase 3)**: Depends on Foundational and supplies direct routing required by later capability composition.
- **User Story 2 (Phase 4)**: Depends on User Story 1 owner selection; its tests and disjoint child-owner edits can run in parallel within the phase.
- **User Story 3 (Phase 5)**: Depends on Foundational; may run alongside User Story 2 after shared owner files are scheduled to one writer.
- **User Story 4 (Phase 6)**: Depends on Foundational; may run alongside User Story 3 where files are disjoint.
- **User Story 5 (Phase 7)**: Depends on User Stories 1–4 so normalization preserves their established contracts instead of inventing a competing schema.
- **Polish (Phase 8)**: Depends on all selected stories; T042 precedes validation when a governing counterpart changes.

### User Story Dependencies

- **User Story 1 (P1)**: No story dependency after Foundational; MVP entry point.
- **User Story 2 (P1)**: Depends on User Story 1 because valid handoffs require known owners.
- **User Story 3 (P2)**: Depends only on Foundational, but shared files serialize with active US1/US2 writers.
- **User Story 4 (P2)**: Depends only on Foundational, but shared files serialize with active US1/US2 writers.
- **User Story 5 (P3)**: Depends on the behavioral contracts from User Stories 1–4.

### Within Each User Story

- Add the cold failing behavioral assertion before changing its owner guidance.
- Design-impact skill batches use `docs/agents/skill-design-dispatch.md`; one designated writer owns each accepted skill/eval slice.
- Shared files have one active writer. Disjoint skill/eval files may proceed concurrently.
- Run the story's independent test before its checkpoint.

### Parallel Opportunities

- T009–T011, T015–T017, T022–T023, and T027–T029 operate on disjoint evaluation files except where explicitly serialized by file.
- T012 and T013 are disjoint owner groups.
- T018–T020 are disjoint parent, artifact-owner, and maintenance surfaces.
- T024 and T025 are disjoint context-projection owner groups.
- T030–T032 are disjoint write, maintenance, and supporting-maintenance groups.
- T035–T039 are disjoint owner-skill batches.
- T043 and T044 can run concurrently when both apply.

---

## Parallel Example: User Story 2

```text
Task: "Add parent-return scenario in .agents/skills/session-beats/evals/evals.json"
Task: "Add child-scope assertions in .agents/skills/faction-design/evals/evals.json and .agents/skills/place-design/evals/evals.json"
Task: "Add repair-loop scenario in .agents/skills/wiki-lint/evals/evals.json"

After those assertions fail:
Task: "Update parent-return contract in session-beats, run-guide, and theatre-of-the-mind"
Task: "Update faction/place owner-return contracts"
Task: "Update wiki-lint semantic-finding handoff"
```

## Parallel Example: User Story 5

```text
Task: "Normalize cross-linker/tag-taxonomy/dedup/import/research/synthesis/dashboard/graph-colorize boundaries"
Task: "Normalize remaining read/maintenance/history boundaries"
Task: "Normalize typed-beat and presentation boundaries"
Task: "Normalize artifact-owner boundaries"
Task: "Normalize challenge/travel/creature/item/Foundry staging boundaries"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Setup and Foundational.
2. Add the US1 cold failing assertions.
3. Implement direct routing and read-only owner contracts.
4. Run V-001 and V-004 independently.
5. Stop if direct owner selection or canonical-state isolation fails.

### Incremental Delivery

1. **US1**: Direct owner selection and read-only isolation.
2. **US2**: Parent retention, child return, dependency order, and safe concurrency.
3. **US3**: Minimum context projection and focused retrieval feedback.
4. **US4**: Output-contract validation and maintenance feedback.
5. **US5**: Whole-set boundary legibility and duplication cleanup.
6. **Polish**: Counterpart synchronization and repository verification.

### Parallel Team Strategy

1. One session agent completes shared authority surfaces serially.
2. Designated writers take disjoint skill/eval batches only after cross-slice contracts are fixed.
3. One integration owner rejoins results, runs cold evaluations, and records final evidence.

---

## Notes

- `[P]` means different files and no incomplete dependency; overlapping files serialize even across stories.
- Every skill change preserves specialized craft, safeguards, and output contracts.
- No task adds a graph runtime, owner registry, execution database, persistent ledger, universal state schema, bespoke node class, global DAG, or generic orchestrator.
- Generated `.omp/commands/speckit.*` and generated Spec Kit adapters remain unchanged.
- Campaign canon remains unchanged.
