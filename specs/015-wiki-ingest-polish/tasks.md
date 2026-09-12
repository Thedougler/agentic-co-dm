---

description: "Task list for Wiki Ingest Polish"
---

# Tasks: Wiki Ingest Polish

**Input**: Design documents from `/specs/015-wiki-ingest-polish/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/, quickstart.md

**Tests**: No permanent test tasks are included; the feature specification requests observable validation scenarios, not TDD. Run the quickstart validation in the final phase.

**Organization**: Tasks are grouped by user story so each story can be implemented and validated independently.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Establish the existing skill surfaces and feature scope.

- [ ] T001 Review the existing ingestion workflow and referenced craft-skill boundaries in `.agents/skills/wiki-ingest/SKILL.md`
- [ ] T002 [P] Review existing ingestion prompt guidance in `.agents/skills/wiki-ingest/references/ingest-prompts.md`
- [ ] T003 [P] Review campaign page and metadata constraints in `wiki/AGENTS.md`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Define the shared routing and completion seam before story-specific edits.

- [ ] T004 Update the source-trust, idea-extraction, and destination-routing guidance in `.agents/skills/wiki-ingest/SKILL.md`
- [ ] T005 [P] Align the agent-facing quality handoff with `copy-writer`, `obsidian-markdown`, `theatre-of-the-mind`, and `dnd5e-mechanics` in `.agents/skills/wiki-ingest/SKILL.md`
- [ ] T006 [P] Align ingestion prompt framing with source-as-evidence and polish-not-copy behavior in `.agents/skills/wiki-ingest/references/ingest-prompts.md`
- [ ] T007 Document the shared completion invariant—every idea has a page, justified new page, staged result, or explicit unresolved outcome—in `.agents/skills/wiki-ingest/SKILL.md`

**Checkpoint**: Shared source handling, quality handoffs, and completion semantics are explicit.

---

## Phase 3: User Story 1 - Digest Source Ideas into Wiki Knowledge (Priority: P1) MVP

**Goal**: Route source ideas into relevant existing or justified new pages instead of copying files as finished notes.

**Independent Test**: Ingest a source containing ideas for an existing page, a new coherent topic, and an incomplete fragment; verify integration, justified creation, and staged/unresolved handling.

### Implementation for User Story 1

- [ ] T008 [US1] Specify topic-based routing and existing-page preference in `.agents/skills/wiki-ingest/SKILL.md`
- [ ] T009 [US1] Specify the sufficient-scope threshold for creating a new page in `.agents/skills/wiki-ingest/SKILL.md`
- [ ] T010 [US1] Specify duplicate, fragment, and insufficient-source handling in `.agents/skills/wiki-ingest/SKILL.md`
- [ ] T011 [US1] Specify per-file destination attribution and completion reporting in `.agents/skills/wiki-ingest/SKILL.md`

**Checkpoint**: A single source is digested into canonical destinations without raw-copy duplication.

---

## Phase 4: User Story 2 - Preserve Settled Creative Intent (Priority: P2)

**Goal**: Polish source material without silently changing established facts, creative decisions, or mechanics.

**Independent Test**: Ingest a source with explicit decisions and a conflicting claim; verify the decision survives and the conflict becomes a proposal or ambiguity rather than an overwrite.

### Implementation for User Story 2

- [ ] T012 [US2] Define preservation of settled facts, intent, and stated mechanics during source digestion in `.agents/skills/wiki-ingest/SKILL.md`
- [ ] T013 [US2] Define inferred and ambiguous provenance handling for synthesized or unclear claims in `.agents/skills/wiki-ingest/SKILL.md`
- [ ] T014 [US2] Define canon-proposal handling for conflicts and uncertain campaign facts in `.agents/skills/wiki-ingest/SKILL.md`
- [ ] T015 [US2] Align conflict and approval language with existing Work and DM gates in `.agents/skills/wiki-ingest/references/ingest-prompts.md`

**Checkpoint**: Ingestion cannot silently convert uncertainty or conflict into canon.

---

## Phase 5: User Story 3 - Apply Creation Quality Standards (Priority: P3)

**Goal**: Ensure ingested output meets the same applicable prose, audience, mechanics, and Markdown standards as new content.

**Independent Test**: Ingest mixed DM-facing, player-facing, and mechanical source material; verify each result uses the correct surface and passes applicable quality checks.

### Implementation for User Story 3

- [ ] T016 [US3] Require destination-specific quality passes and craft-skill handoffs in `.agents/skills/wiki-ingest/SKILL.md`
- [ ] T017 [US3] Require complete-sentence, signal-dense copy and removal of agent shorthand in `.agents/skills/wiki-ingest/SKILL.md`
- [ ] T018 [US3] Require audience, reveal, narration, and DM-only separation during ingestion in `.agents/skills/wiki-ingest/SKILL.md`
- [ ] T019 [US3] Require applicable D&D 5e test grammar and consequence completeness without inventing unsupported mechanics in `.agents/skills/wiki-ingest/SKILL.md`
- [ ] T020 [US3] Require frontmatter, source attribution, Obsidian links, and existing page layout preservation in `.agents/skills/wiki-ingest/SKILL.md`

**Checkpoint**: Ingested output is indistinguishable in quality from newly authored content for its target surface.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Validate the integrated workflow and keep documentation aligned.

- [ ] T021 [P] Update the ingestion quality contract to match final workflow behavior in `specs/015-wiki-ingest-polish/contracts/ingest-quality.md`
- [ ] T022 [P] Update the validation scenarios and expected outcomes in `specs/015-wiki-ingest-polish/quickstart.md`
- [ ] T023 Run the repository's applicable skill/document validators against `.agents/skills/wiki-ingest/SKILL.md` and `.agents/skills/wiki-ingest/references/ingest-prompts.md`
- [ ] T024 Run every scenario in `specs/015-wiki-ingest-polish/quickstart.md` and record observed routing, preservation, quality, and tracking results

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies.
- **Foundational (Phase 2)**: Depends on Setup; blocks all user stories.
- **User Story 1 (Phase 3)**: Depends on Foundational; MVP and routing baseline.
- **User Story 2 (Phase 4)**: Depends on Foundational; can be implemented independently of US1 after shared seam exists.
- **User Story 3 (Phase 5)**: Depends on Foundational; can be implemented independently of US1 and US2 after shared seam exists.
- **Polish (Phase 6)**: Depends on the desired user stories being complete.

### User Story Dependencies

- **US1**: No dependency on another story after Foundational.
- **US2**: No dependency on another story after Foundational; shares the source-routing seam.
- **US3**: No dependency on another story after Foundational; shares the quality handoff seam.

### Parallel Opportunities

- T002 and T003 can run in parallel.
- T005 and T006 can run in parallel after T004 establishes the seam.
- T008–T011 are sequential because they refine the same workflow file.
- T012–T015 are sequential because preservation and conflict handling share the same workflow contract.
- T021 and T022 can run in parallel after implementation.
- US1, US2, and US3 can proceed in parallel after Phase 2 only if edits are coordinated; otherwise implement sequentially to avoid same-file conflicts.

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Setup and Foundational phases.
2. Complete US1 routing and completion tasks.
3. Run the US1 independent test from the quickstart.
4. Proceed to US2 and US3 only after routing behavior is sound.

### Incremental Delivery

1. Route and digest ideas (US1).
2. Preserve intent and expose conflicts (US2).
3. Apply destination-specific creation standards (US3).
4. Run cross-cutting validation and update contract/quickstart artifacts.

## Notes

- Every task follows the required checklist format with a sequential ID and exact file path.
- `[P]` appears only where tasks can usefully run in parallel without incomplete dependencies.
- No new runtime module, page type, storage system, or duplicate quality authority is proposed.
