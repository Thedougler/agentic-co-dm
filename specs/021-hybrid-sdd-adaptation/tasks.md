---

description: "Task list for Hybrid Spec-Driven Development"
---

# Tasks: Hybrid Spec-Driven Development

**Input**: Design documents from `/specs/021-hybrid-sdd-adaptation/`

**Prerequisites**: `plan.md`, `spec.md`, `research.md`, `data-model.md`, `contracts/`, and `quickstart.md`

**Tests**: No separate TDD tasks are included. The specification requires public fixture/CLI checks; those checks are implementation and verification surfaces below.

**Organization**: Tasks are grouped by user story. Each task names its canonical write surface and preserves the single-writer boundary.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Establish maintainer policy, local trace storage, and sanitized feature fixtures without changing generated Spec Kit files.

- [ ] T001 [P] Create maintainer-owned efficiency policy with 90-day retention, `prep`/`wrapup` comparison classes, pair/reduction thresholds, risk paths, canaries, and rollback gates in `config/efficiency.yaml`
- [ ] T002 [P] Ignore normal local efficiency traces, quarantine output, and retention artifacts in `.gitignore`
- [ ] T003 [P] Create the sanitized route, evidence, and telemetry fixture directories with README-free placeholder-free structure in `specs/021-hybrid-sdd-adaptation/fixtures/`
- [ ] T004 [P] Record the feature's generated-file preservation boundary and public command surfaces in `specs/021-hybrid-sdd-adaptation/quickstart.md`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Install the progressive-disclosure route and shared artifact vocabulary before story-specific behavior is implemented.

**CRITICAL**: User-story implementation depends on this phase. Generated `.agents/skills/speckit-*`, `.omp/commands/speckit.*`, and `.specify/templates/*` remain unchanged.

- [ ] T005 Replace the compact Spec Kit routing section with a pointer that classifies substantial work and preserves existing routine campaign routes in `AGENTS.md`
- [ ] T006 Write the detailed hybrid routing, artifact, ownership, agency, completion-evidence, and verification procedure in `docs/agents/hybrid-sdd.md`
- [ ] T007 Define the fixture record shapes and stable scenario identifiers used by the checker in `specs/021-hybrid-sdd-adaptation/fixtures/README.md`

**Checkpoint**: Route policy, detailed contract, policy thresholds, local-trace boundary, and fixture conventions are defined; no story checker can silently invent a second authority.

---

## Phase 3: User Story 1 - Classify work before governing it (Priority: P1) 🎯 MVP

**Goal**: Classify each substantial request as exactly one SDD work class, route routine campaign content through its existing skill, and split mixed requests without fictional canon creation.

**Independent Test**: Run `python3 scripts/hybrid-sdd-check.py classify --fixtures specs/021-hybrid-sdd-adaptation/fixtures/routes/`; all seven representative scenarios, including the mixed request, receive the expected route and rationale.

### Implementation for User Story 1

- [ ] T008 [P] [US1] Add agent-system, campaign-architecture, and creative-system classification cases with expected class, `full-sdd` route, rationale, and scope boundary in `specs/021-hybrid-sdd-adaptation/fixtures/routes/classification-system.json`
- [ ] T009 [P] [US1] Add engineering and routine-content cases proving ordinary engineering SDD and established NPC skill routing in `specs/021-hybrid-sdd-adaptation/fixtures/routes/classification-routine.json`
- [ ] T010 [P] [US1] Add entity-collision, proposed-canon, and mixed-request route cases in `specs/021-hybrid-sdd-adaptation/fixtures/routes/classification-boundaries.json`
- [ ] T011 [US1] Implement CLI parsing, exact work-class/route validation, rationale checks, routine-content handling, and mixed-request splitting in `scripts/hybrid-sdd-check.py`

**Checkpoint**: US1 is independently runnable through the classification CLI and covers Scenarios A–G without creating a feature directory for routine content.

---

## Phase 4: User Story 2 - Specify playable outcomes without closing play (Priority: P1)

**Goal**: Validate campaign-facing and reusable-system specifications for independent actors, pressures, open player decisions, conditional outcomes, continuity, and if-nobody-intervenes motion without screenplay requirements.

**Independent Test**: Run `python3 scripts/hybrid-sdd-check.py agency --fixtures specs/021-hybrid-sdd-adaptation/fixtures/evidence/agency.json`; valid regional-conflict and reputation records pass, while authored player choices, fixed scene order, and fixed endings fail objectively.

### Implementation for User Story 2

- [ ] T012 [P] [US2] Add regional-conflict specification evidence for actors, factions, locations, clocks, relationships, information states, pressures, conditional opportunities, and open endings in `specs/021-hybrid-sdd-adaptation/fixtures/evidence/agency.json`
- [ ] T013 [P] [US2] Add reputation-system evidence for persistent state, faction behavior, information access, player-caused changes, and refusal/avoidance/negotiation responses in `specs/021-hybrid-sdd-adaptation/fixtures/evidence/reusable-system.json`
- [ ] T014 [P] [US2] Add negative agency fixtures for mandatory allegiance, authored player decisions, fixed scene sequence, fixed ending, and missing independent-world motion in `specs/021-hybrid-sdd-adaptation/fixtures/evidence/agency-failures.json`
- [ ] T015 [US2] Extend the agency verifier to require observable value, actors, pressures, open outcomes, conditional possibilities, independent motion, and if-nobody-intervenes consequences while rejecting screenplay constraints in `scripts/hybrid-sdd-check.py`

**Checkpoint**: US2 is independently verifiable from sanitized evidence and does not turn playability judgment into a prose snapshot or authored route.

---

## Phase 5: User Story 3 - Preserve truth ownership and the canon boundary (Priority: P1)

**Goal**: Reuse existing owners, preserve provenance/reveal/visibility, keep proposals distinct from accepted truth, and permit safe deterministic maintenance without needless DM approval.

**Independent Test**: Run `python3 scripts/hybrid-sdd-check.py canon --fixtures specs/021-hybrid-sdd-adaptation/fixtures/evidence/`; aliases resolve or surface ambiguity, proposed events remain proposals, and deterministic maintenance is not blocked.

### Implementation for User Story 3

- [ ] T016 [P] [US3] Add existing-title, alias, stem, wikilink, manifest, QMD, and uncertain-collision evidence with owner-resolution outcomes in `specs/021-hybrid-sdd-adaptation/fixtures/evidence/ownership.json`
- [ ] T017 [P] [US3] Add accepted-truth, affected-truth, proposal, reveal, visibility, DM-acceptance, and filing-state evidence in `specs/021-hybrid-sdd-adaptation/fixtures/evidence/canon-boundary.json`
- [ ] T018 [P] [US3] Add safe deterministic maintenance and invalid accept-before-write cases in `specs/021-hybrid-sdd-adaptation/fixtures/evidence/maintenance-boundary.json`
- [ ] T019 [US3] Extend the checker with owner reuse/collision reporting, canon-state transitions, reveal/visibility checks, accept-before-write hard gates, and non-fact maintenance handling in `scripts/hybrid-sdd-check.py`

**Checkpoint**: US3 is independently verifiable without writing wiki facts, introducing opaque IDs, or adding a second lifecycle/owner model.

---

## Phase 6: User Story 4 - Plan and task real artifact dependencies (Priority: P2)

**Goal**: Represent minimum sufficient context, canonical owners, real dependency edges, serial/parallel waves, agency/continuity constraints, and single-writer ownership in plans and tasks.

**Independent Test**: Run `python3 scripts/hybrid-sdd-check.py topology --fixtures specs/021-hybrid-sdd-adaptation/fixtures/evidence/topology.json`; real prerequisite edges pass, and a parallel wave sharing a canonical artifact fails.

### Implementation for User Story 4

- [ ] T020 [P] [US4] Add a valid creative/agentic dependency graph from grounding and retrieval through owner resolution, systems, situations, presentation, verification, Work, acceptance, filing, and maintenance in `specs/021-hybrid-sdd-adaptation/fixtures/evidence/topology.json`
- [ ] T021 [P] [US4] Add valid disjoint parallel waves and invalid shared-writer/dependent-parallel cases in `specs/021-hybrid-sdd-adaptation/fixtures/evidence/parallel-ownership.json`
- [ ] T022 [P] [US4] Add engineering-plan evidence showing technical architecture, storage, testing, platform, performance, and constraints without campaign-only requirements in `specs/021-hybrid-sdd-adaptation/fixtures/evidence/engineering-plan.json`
- [ ] T023 [US4] Extend the checker with dependency resolution, wave ordering, disjoint-write validation, context-used/omitted checks, and engineering-versus-creative plan vocabulary checks in `scripts/hybrid-sdd-check.py`

**Checkpoint**: US4 is independently verifiable from topology fixtures and reports only real dependency or ownership constraints rather than decorative DAG ceremony.

---

## Phase 7: User Story 5 - Verify the right things and keep both SDD paths compatible (Priority: P2)

**Goal**: Provide deterministic hard gates, redacted efficiency telemetry, promotion evidence, and lifecycle compatibility without treating creative judgment as lint.

**Independent Test**: Run `.venv/bin/python specs/021-hybrid-sdd-adaptation/fixtures/check.py`; it must emit one `PASS` summary after exercising route, evidence, telemetry, schema, retention, promotion, and compatibility fixtures.

### Implementation for User Story 5

- [ ] T024 [US5] Extend the checker with closed-vocabulary/schema/link/owner checks, deterministic-versus-semantic verification boundaries, completion-evidence validation, and Spec Kit compatibility checks in `scripts/hybrid-sdd-check.py`
- [ ] T025 [US5] Implement redacted JSONL record validation, exclusive token attribution, retrieval/fallback recording, measurement-gap handling, additive schema support, quarantine, and explicit errors in `scripts/efficiency-trace.py`
- [ ] T026 [US5] Implement labeled metric-vector reporting, accepted-Work denominators, same-kind comparison filtering, 90-day retention, and low/moderate/high-risk promotion gates in `scripts/efficiency-trace.py`
- [ ] T027 [P] [US5] Add complete, failed, incomplete, disabled, pre-governance, fallback, attribution, additive-schema, incompatible-schema, and retention telemetry fixtures in `specs/021-hybrid-sdd-adaptation/fixtures/telemetry/`
- [ ] T028 [P] [US5] Add deterministic hard-gate, semantic-review-boundary, compatibility, and completion-evidence fixtures in `specs/021-hybrid-sdd-adaptation/fixtures/evidence/verification.json`
- [ ] T029 [US5] Implement the feature-local public fixture runner with isolated temporary trace paths and a single `PASS`/failure exit surface in `specs/021-hybrid-sdd-adaptation/fixtures/check.py`
- [ ] T030 [US5] Complete quickstart commands and expected outputs for both CLIs, Spec Kit integration status, OMP baseline, fixture validation, and native-tokenizer governance blocking in `specs/021-hybrid-sdd-adaptation/quickstart.md`

**Checkpoint**: US5 is independently runnable and preserves specify, clarify, plan, checklist, tasks, analyze, implement, converge, git, and agent-context integration behavior.

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Validate the complete feature without modifying campaign content or managed Spec Kit artifacts.

- [ ] T031 [P] Run the complete fixture suite and record the observed `PASS` result against `specs/021-hybrid-sdd-adaptation/quickstart.md`
- [ ] T032 [P] Run `specify integration status --json` and confirm managed Spec Kit files remain clean in `specs/021-hybrid-sdd-adaptation/quickstart.md`
- [ ] T033 [P] Run `./scripts/check-omp-baseline.sh` and record the result in `specs/021-hybrid-sdd-adaptation/quickstart.md`
- [ ] T034 Audit all feature artifacts for generated-file edits, raw-content telemetry, duplicate authorities, missing file paths, and unlabelled measurement values in `specs/021-hybrid-sdd-adaptation/`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No feature-task dependencies; T001–T004 can run in parallel because they own disjoint files.
- **Foundational (Phase 2)**: T005–T007 depend on the setup policy/fixture boundary and block all user stories.
- **User Story 1 (Phase 3)**: T008–T010 can run in parallel; T011 follows those fixtures and owns the checker baseline.
- **User Story 2 (Phase 4)**: T012–T014 can run in parallel; T015 follows US1's checker baseline and is the sole checker writer in this phase.
- **User Story 3 (Phase 5)**: T016–T018 can run in parallel; T019 follows T015 and extends the same checker serially.
- **User Story 4 (Phase 6)**: T020–T022 can run in parallel; T023 follows T019 and extends the same checker serially.
- **User Story 5 (Phase 7)**: T024 follows T023; T025–T026 are serial because they share `scripts/efficiency-trace.py`; T027–T028 can run in parallel with each other after their schemas are defined; T029 follows T024–T028; T030 follows the public surfaces.
- **Polish (Phase 8)**: T031–T033 can run in parallel after US5; T034 follows all validation and audits the complete feature.

### User Story Dependencies

- **US1 (P1)**: Depends only on Foundational; MVP route classification is independently usable.
- **US2 (P1)**: Depends on US1's checker CLI and route identity, then adds agency validation.
- **US3 (P1)**: Depends on US2's evidence model and checker, then adds owner/canon hard gates.
- **US4 (P2)**: Depends on US3's owner/canon state vocabulary, then adds dependency and single-writer topology.
- **US5 (P2)**: Depends on US4's completion/topology evidence; adds telemetry and compatibility as separate public seams.

### Parallel Opportunities

- Setup policy, ignore rules, fixture directories, and quickstart preservation notes are disjoint and parallelizable.
- Within US1, classification fixture groups are disjoint and parallelizable.
- Within US2–US4, evidence fixture files are disjoint and parallelizable; checker extensions are serial due to one canonical writer.
- Within US5, telemetry fixture generation and verification fixture generation are disjoint; post-US5 repository checks are parallelizable.

---

## Parallel Example: User Story 1

```text
Task T008: Add system-class classification fixtures in specs/021-hybrid-sdd-adaptation/fixtures/routes/classification-system.json
Task T009: Add engineering/routine classification fixtures in specs/021-hybrid-sdd-adaptation/fixtures/routes/classification-routine.json
Task T010: Add boundary and mixed-request fixtures in specs/021-hybrid-sdd-adaptation/fixtures/routes/classification-boundaries.json
```

## Parallel Example: User Story 2

```text
Task T012: Add regional-conflict evidence in specs/021-hybrid-sdd-adaptation/fixtures/evidence/agency.json
Task T013: Add reusable-system evidence in specs/021-hybrid-sdd-adaptation/fixtures/evidence/reusable-system.json
Task T014: Add negative agency fixtures in specs/021-hybrid-sdd-adaptation/fixtures/evidence/agency-failures.json
```

## Parallel Example: User Story 3

```text
Task T016: Add owner-resolution evidence in specs/021-hybrid-sdd-adaptation/fixtures/evidence/ownership.json
Task T017: Add canon-boundary evidence in specs/021-hybrid-sdd-adaptation/fixtures/evidence/canon-boundary.json
Task T018: Add maintenance-boundary evidence in specs/021-hybrid-sdd-adaptation/fixtures/evidence/maintenance-boundary.json
```

## Parallel Example: User Story 4

```text
Task T020: Add valid topology evidence in specs/021-hybrid-sdd-adaptation/fixtures/evidence/topology.json
Task T021: Add parallel ownership evidence in specs/021-hybrid-sdd-adaptation/fixtures/evidence/parallel-ownership.json
Task T022: Add engineering-plan evidence in specs/021-hybrid-sdd-adaptation/fixtures/evidence/engineering-plan.json
```

## Parallel Example: User Story 5

```text
Task T027: Add telemetry fixtures in specs/021-hybrid-sdd-adaptation/fixtures/telemetry/
Task T028: Add verification-boundary fixtures in specs/021-hybrid-sdd-adaptation/fixtures/evidence/verification.json
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Setup and Foundational phases.
2. Complete US1 route fixtures and `scripts/hybrid-sdd-check.py` classification behavior.
3. Run the US1 classification command independently.
4. Stop at the US1 checkpoint for an independently usable route decision.

### Incremental Delivery

1. Add US2 agency/open-outcome checks without changing routine content routing.
2. Add US3 owner/canon hard gates without writing campaign facts.
3. Add US4 real dependency topology and single-writer validation.
4. Add US5 telemetry, promotion, deterministic/semantic boundaries, and compatibility checks.
5. Run the full fixture and repository checks only after the final story is complete.

### Safety Boundaries

- Do not edit `.agents/skills/speckit-*`, `.omp/commands/speckit.*`, or `.specify/templates/*`.
- Do not create a second canon, lifecycle, owner model, retrieval system, or database.
- Do not write accepted campaign truth from specifications, plans, tasks, or telemetry.
- Do not store raw prompt, wiki, campaign, model, or provider content in normal traces.
- Do not activate native-tokenizer comparisons or promotion before the separate governance change; record the explicit measurement gap instead.
