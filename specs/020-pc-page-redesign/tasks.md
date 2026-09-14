---

description: "Task list for the PC Page Redesign feature"
---

# Tasks: PC Page Redesign

**Input**: Design documents from `/specs/020-pc-page-redesign/`

**Prerequisites**: `plan.md`, `spec.md`, `research.md`, `data-model.md`, `contracts/pc-page.md`, and `quickstart.md`

**Tests**: No separate test-first tasks are included. The specification defines independent acceptance scenarios; the feature-local fixture and the scoped lint/manual checks below validate them.

**Organization**: Tasks are grouped by user story so each increment has a clear owner, dependency, and independent acceptance check.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Establish the feature-local validation entrypoint without adding a new dependency or database.

- [ ] T001 Create the argument-free feature checker entrypoint in `specs/020-pc-page-redesign/fixtures/check.py`, using Python 3 and text/JSON-compatible exit behavior.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Make the page contract executable before template, owner-page, or workflow edits begin.

**⚠️ CRITICAL**: The checker is the blocking contract for all user-story work; it must recognize the canonical owner path, required metadata, ordered spine, column fences, omission rules, narration boundary, preservation metadata, and absence of live satellite duplicates.

- [ ] T002 Implement the observable PC contract assertions in `specs/020-pc-page-redesign/fixtures/check.py` for the template and five owner pages under `wiki/entities/pc/`, including `type: pc`, required frontmatter, one H1, no `Voice`, supported nested `col`/`col-md` pairs, conditional-section omission, source/link metadata preservation, and archive-only satellite handling.

**Checkpoint**: The feature has a runnable contract checker that fails clearly for an un-conformed page and can validate the completed five-page set.

---

## Phase 3: User Story 1 - Reference any PC from one page (Priority: P1) 🎯 MVP

**Goal**: Give the DM one predictable, player-safe, scan-friendly PC owner-page shape with orientation, mechanics, abilities, resources, inventory, and current context.

**Independent Test**: Open each of the five files under `wiki/entities/pc/` and, without opening another page, locate player, class/level, AC, current/max HP, initiative, signature options, a named connection, and a decision-relevant pressure in under 60 seconds per page after conformance.

### Implementation for User Story 1

- [ ] T003 [P] [US1] Redesign the canonical PC scaffold in `wiki/templates/pc.md` with the required frontmatter, one-H1 spine, player-safe `Narration`, `At a Glance`, `Connections`, `Sheet`, `Combat Profile`, `Abilities`, conditional `Spells`, `Inventory`, conditional `Session Log`, and conditional `Art` sections.
- [ ] T004 [US1] Encode the paired identity and mechanical scan surfaces in `wiki/templates/pc.md` with nested `col`/`col-md` fences, narration outside fences, headings inside child fences, readable linear fallback tables, and one canonical home for exact numbers.
- [ ] T005 [US1] Make the template’s ability, spell, inventory, session, and art scaffolds omit empty subsections and preserve multiclass pools, resource recovery, owner links, unknowns, and conflict markers in `wiki/templates/pc.md`.

**Checkpoint**: A new PC copied from `wiki/templates/pc.md` has a single predictable reference surface and can be checked by `specs/020-pc-page-redesign/fixtures/check.py` without relying on visual placement.

---

## Phase 4: User Story 2 - Author predictable PC pages (Priority: P2)

**Goal**: Make the canonical template and governing wiki rules sufficient for an agent to place facts, links, unknowns, and player-safe narration without inferring a one-off format.

**Independent Test**: Using only `wiki/templates/pc.md`, `wiki/AGENTS.md`, `specs/020-pc-page-redesign/contracts/pc-page.md`, and representative source evidence, produce caster, non-caster, and multiclass scratch pages with valid metadata, stable headings, correct links, safe narration, and no empty conditional sections.

### Implementation for User Story 2

- [ ] T006 [US2] Update the PC row and owner-page rules in `wiki/AGENTS.md` to name the redesigned Title Case spine, canonical `wiki/entities/pc/` path, `type: pc` contract, player-control boundary, omission behavior, owner-link/source-satellite policy, and structure-only preservation rules; remove the obsolete `Voice` requirement.

**Checkpoint**: The template and governing wiki instructions tell an agent where every required PC fact belongs and distinguish owner facts, source evidence, unknowns, DM content, and player-safe narration.

---

## Phase 5: User Story 3 - Conform the current party without losing canon (Priority: P3)

**Goal**: Bring the five live PC owners onto one page shape while preserving campaign facts, source lineage, links, aliases, art, lifecycle, reveal, visibility, campaign, and player handles.

**Independent Test**: Compare each conformed owner with its pre-change page and applicable archive satellites; confirm the shared contract, preserved facts or explicit owner links/`[verify]` markers, no competing live satellite dump, and no changed campaign state.

### Implementation for User Story 3

- [ ] T007 [P] [US3] Conform `wiki/entities/pc/jean-claude-tabarnack.md` to the canonical PC spine, flatten applicable archive facts into their single owner sections, preserve existing metadata/links/art, and mark the known HP/initiative disagreement with `[verify]` and its source.
- [ ] T008 [P] [US3] Conform `wiki/entities/pc/perrin-black-jaw.md` to the canonical PC spine, flatten applicable archive facts into their single owner sections, preserve existing metadata/links/art, and mark the known AC/player-handle disagreement with `[verify]` and its source.
- [ ] T009 [P] [US3] Conform `wiki/entities/pc/catarina-davirelli.md` to the canonical PC spine, consolidate historical source density without dropping attributable facts, and preserve existing metadata/links/art and campaign state.
- [ ] T010 [P] [US3] Conform `wiki/entities/pc/crissdalynn-khinriss.md` to the canonical PC spine, flatten applicable archive facts into their single owner sections, preserve existing metadata/links/art, and mark the known AC/HP/speed disagreement with `[verify]` and its source.
- [ ] T011 [P] [US3] Conform `wiki/entities/pc/delmar-fisk.md` to the canonical PC spine, flatten applicable archive facts into their single owner sections, and preserve existing metadata/links/art, lifecycle, reveal, visibility, campaign, and player-handle values.

**Checkpoint**: All five live owner pages share the contract, retain their canon, and contain no second live PC facet representation.

---

## Phase 6: User Story 4 - Maintain the standard across PC workflows (Priority: P4)

**Goal**: Make PC creation, ingestion, reconciliation, and Markdown formatting point to one canonical contract without competing headings or satellite instructions.

**Independent Test**: Trace the four applicable workflow files and their governing wiki guidance, then confirm every path names the same template, owner location, frontmatter/section contract, column syntax, omission rules, source boundary, and conflict/unknown behavior.

### Implementation for User Story 4

- [ ] T012 [P] [US4] Update PC interview creation and answer-mapping guidance in `.agents/skills/pc-interview/SKILL.md` to use `wiki/templates/pc.md`, `wiki/entities/pc/`, and existing PC section homes, treating interview transcripts as evidence rather than live facets.
- [ ] T013 [P] [US4] Update PC ingest guidance in `.agents/skills/wiki-ingest/SKILL.md` to point to the canonical template/path, flatten applicable archived satellites, preserve source lineage, and keep conflicts or unknowns explicit without duplicating the full contract.
- [ ] T014 [P] [US4] Update PC reconciliation guidance in `.agents/skills/reconciling-session-evidence/SKILL.md` to route durable changes to the canonical PC owner sections, preserve lifecycle/reveal/visibility rules, and avoid recreating satellite dumps or inventing conflict resolutions.
- [ ] T015 [P] [US4] Update PC formatting and frontmatter guidance in `.agents/skills/obsidian-markdown/SKILL.md` to include `pc`, wikilink and escaped-pipe rules, complete-sentence DM prose, safe narration, inline-code DC/dice, real newlines, omission rules, and the PC column exception.
- [ ] T016 [P] [US4] Update supported column guidance in `.agents/skills/obsidian-markdown/references/COLUMNS.md` to document the PC-only nested `col`/`col-md` scan pairs, longer parent fence, headings/tables as linear fallback, narration outside fences, and prohibition on `[!col]` for PC pairs.

**Checkpoint**: PC interview, ingest, reconciliation, and Markdown workflows converge on the same canonical template and do not reintroduce obsolete paths, `Voice`, or competing facet headings.

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Validate behavior that static page edits alone cannot prove and leave no lint or rendering regressions.

- [ ] T017 Run the feature contract checker against `specs/020-pc-page-redesign/fixtures/check.py`, `wiki/templates/pc.md`, `wiki/entities/pc/`, and applicable `wiki/_archive/` satellites; require exit `0`.
- [ ] T018 Run scoped write validation with `./scripts/lint-wiki-write --path wiki/entities/pc` against all five conformed owner pages.
- [ ] T019 Run strict Obsidian Markdown validation with `./scripts/lint-obsidian-markdown --strict --path wiki/entities/pc` against all five conformed owner pages.
- [ ] T020 Run owner-schema validation with `./scripts/wiki-lint --json` and confirm no HARD findings for PC paths, frontmatter, links, filenames, or duplicate H1/facet structure.
- [ ] T021 Perform an Obsidian Reading-view review of `wiki/entities/pc/jean-claude-tabarnack.md`, `wiki/entities/pc/perrin-black-jaw.md`, `wiki/entities/pc/catarina-davirelli.md`, `wiki/entities/pc/crissdalynn-khinriss.md`, and `wiki/entities/pc/delmar-fisk.md`, confirming full-width safe narration, paired scan surfaces, and readable linear fallback.
- [ ] T022 Perform the timed DM-reference review and source-preservation comparison for `wiki/entities/pc/` against `wiki/_archive/{abilities,character-sheets,combat-profile,galleries,inventory,session-logs,spells,stats,va-scripts}/`, confirming every prior fact is inline, owner-linked, or explicitly marked `[verify]`.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: T001 establishes the argument-free checker entrypoint.
- **Foundational (Phase 2)**: T002 depends on T001 and blocks all story work with executable page-shape and preservation assertions.
- **User Story 1 (Phase 3)**: Depends on T002; defines the canonical template used by later stories.
- **User Story 2 (Phase 4)**: Depends on User Story 1 because its guidance points to the redesigned template.
- **User Story 3 (Phase 5)**: Depends on User Stories 1 and 2; owner conformance must use the final template and governing rules.
- **User Story 4 (Phase 6)**: Depends on User Story 1 and may proceed in parallel with User Story 3 once the template contract is stable.
- **Polish (Phase 7)**: Depends on all desired story work; run the fixture before reporting completion.

### User Story Dependencies

- **User Story 1 (P1)**: Depends only on the foundational checker; MVP template increment.
- **User Story 2 (P2)**: Depends on User Story 1; governing wiki rules must describe the canonical template.
- **User Story 3 (P3)**: Depends on User Stories 1 and 2; each owner task is independent after the contract is fixed.
- **User Story 4 (P4)**: Depends on User Story 1; workflow files are independent of one another and can run alongside User Story 3.

### Within Each User Story

- User Story 1: update the scaffold and its semantic/presentation/omission rules in `wiki/templates/pc.md`.
- User Story 2: update the governing instruction after the scaffold contract is fixed.
- User Story 3: preserve each owner’s metadata and facts before removing or flattening any satellite representation; then validate each owner against the checker.
- User Story 4: update each workflow file to point to the canonical contract rather than copying competing format rules.

### Parallel Opportunities

- User Story 1: T003–T005 touch one canonical file and therefore run sequentially; no unsafe parallel edit is proposed.
- User Story 3: T007–T011 are independent owner files and can run in parallel after User Stories 1–2.
- User Story 4: T012–T016 are independent guidance files and can run in parallel after User Story 1.
- User Story 3 and User Story 4 can run in parallel after the template and governing contract are stable, with one writer per file.
- Validation tasks T018–T020 are read-only checks and may run in parallel after all source edits; T017 must be run before treating the page contract as complete.

---

## Parallel Example: User Story 3

```text
Task: "Conform wiki/entities/pc/jean-claude-tabarnack.md, preserving facts and marking HP/initiative conflicts"
Task: "Conform wiki/entities/pc/perrin-black-jaw.md, preserving facts and marking AC/player-handle conflicts"
Task: "Conform wiki/entities/pc/catarina-davirelli.md, preserving historical source density"
Task: "Conform wiki/entities/pc/crissdalynn-khinriss.md, preserving facts and marking AC/HP/speed conflicts"
Task: "Conform wiki/entities/pc/delmar-fisk.md, preserving metadata and campaign state"
```

## Parallel Example: User Story 4

```text
Task: "Update .agents/skills/pc-interview/SKILL.md for canonical PC creation"
Task: "Update .agents/skills/wiki-ingest/SKILL.md for PC satellite flattening"
Task: "Update .agents/skills/reconciling-session-evidence/SKILL.md for canonical PC state changes"
Task: "Update .agents/skills/obsidian-markdown/SKILL.md for PC syntax and type guidance"
Task: "Update .agents/skills/obsidian-markdown/references/COLUMNS.md for nested PC column pairs"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup.
2. Complete Phase 2: Foundational checker.
3. Complete Phase 3: User Story 1 template redesign.
4. Run `specs/020-pc-page-redesign/fixtures/check.py` against the template and representative page shape.
5. Stop for the first independently reviewable PC reference surface; do not claim live-party conformance until User Story 3 is complete.

### Incremental Delivery

1. Complete Setup + Foundational → executable contract ready.
2. Add User Story 1 → canonical template MVP.
3. Add User Story 2 → predictable agent authoring rules.
4. Add User Story 3 → five live owners conformed without canon loss.
5. Add User Story 4 → workflow regression paths converge.
6. Run Phase 7 → fixture, lint, schema, Reading-view, timed-reference, and preservation evidence.

### Recommended Team Strategy

1. One writer completes T001–T006 because the checker, template, and governing rule establish the shared contract.
2. After that boundary, assign T007–T011 one owner per writer and T012–T016 one guidance file per writer.
3. Run validation only after all page and guidance edits land; do not overlap writers on a canonical file.

---

## Notes

- `[P]` marks tasks that touch different files and have no incomplete dependency.
- `[US#]` labels map implementation work to the prioritized stories in `spec.md`.
- Structure-only conformance preserves facts and campaign state; unresolved conflicts remain explicit rather than being silently resolved.
- The existing repository already supplies the Markdown, lint, Obsidian Columns, and Python 3 infrastructure; no new dependency, database, campaign type, or skill is introduced.
