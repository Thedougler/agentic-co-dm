---

description: "Task list for Hybrid Spec-Driven Development"
---

# Tasks: Hybrid Spec-Driven Development

**Input**: Design documents from `/Users/nick/agentic-co-dm/specs/021-hybrid-sdd-adaptation/`

**Prerequisites**: [plan.md](./plan.md), [spec.md](./spec.md), [research.md](./research.md), [data-model.md](./data-model.md), [contracts/](./contracts/), and [quickstart.md](./quickstart.md)

**Tests**: The feature specification requires independently testable scenarios and measurable outcomes. Tests use the existing standard-library fixture-check pattern; no pytest suite or instruction-prose snapshots are added.

**Organization**: Tasks are grouped by user story. Foundational tasks create the shared route, policy, helper, and checker seams; story tasks add fixtures and behavior checks in dependency order.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Establish the local storage boundary and committed fixture surfaces without touching generated Spec Kit files.

- [ ] T001 [P] Add `.local/efficiency/traces.jsonl` and `.local/efficiency/quarantine/` ignore rules to `.gitignore`, preserving all existing ignore entries.
- [ ] T002 [P] Create the initial route schema and base class cases in `specs/021-hybrid-sdd-adaptation/fixtures/routes/classification.json`; leave the Scenario A–G edge cases for US1.
- [ ] T003 [P] Create sanitized telemetry fixtures at `specs/021-hybrid-sdd-adaptation/fixtures/telemetry/complete-prep.json` and `specs/021-hybrid-sdd-adaptation/fixtures/telemetry/measurement-gap.json` containing counts and provenance identifiers only.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Establish the shared policy, route contract, agent-shaped CLIs, and fixture runner. No user-story task starts before this phase passes.

- [ ] T004 Create maintainer-owned `config/efficiency.yaml` with policy schema version, 90-day retention, `prep`/`wrapup` comparison classes, 10 paired cases, 5% median reduction, risk paths, canary rules, non-inferiority rule, and rollback thresholds from `contracts/efficiency-telemetry.md`.
- [ ] T005 Write the detailed routing, artifact, dependency, canon, agency, and completion-evidence procedure in `docs/agents/hybrid-sdd.md`, pointing to existing `docs/agents/work.md`, campaign skills, QMD precedence, and 012 blind evaluation instead of copying them.
- [ ] T006 Add a compact hybrid-SDD route pointer to `AGENTS.md` that loads `docs/agents/hybrid-sdd.md` for substantial work and explicitly preserves routine campaign-content routing.
- [ ] T007 [P] Implement schema-validated append, redaction checks, retention, and incompatible-record quarantine in `scripts/efficiency-trace.py`; accept structured input, emit JSON/text, write errors to stderr, and return non-zero on invalid or cross-tokenizer data.
- [ ] T008 [P] Implement the objective route, evidence, state-transition, source-attribution, denominator, and hard-gate checks in `scripts/hybrid-sdd-check.py` without duplicating wiki, link, or QMD implementations.
- [ ] T009 Create the standard-library public fixture runner in `specs/021-hybrid-sdd-adaptation/fixtures/check.py`, invoking the two CLIs in temporary directories and reporting one PASS/FAIL result without snapshotting instruction prose.

**Checkpoint**: `config/efficiency.yaml`, `docs/agents/hybrid-sdd.md`, `AGENTS.md`, both CLIs, and the fixture runner exist; generated `.agents/skills/speckit-*`, `.omp/commands/speckit.*`, `.specify/templates/*`, and `.specify/extensions/*` remain untouched.

---

## Phase 3: User Story 1 — Classify work before governing it (Priority: P1) 🎯 MVP

**Goal**: Classify substantial work exactly once, route routine content through its existing process, and split mixed requests without creating fictional canon.

**Independent Test**: Run the route fixture through `scripts/hybrid-sdd-check.py` and `specs/021-hybrid-sdd-adaptation/fixtures/check.py`; every representative request receives the expected class/route/reason and the routine case creates no feature directory.

### Tests for User Story 1

- [ ] T010 [US1] Complete `specs/021-hybrid-sdd-adaptation/fixtures/routes/classification.json` with the Scenario A–G full-SDD, routine-content, existing-entity, proposed-canon, and mixed-request cases, including exact `work_class`, `route`, and rationale fields.
- [ ] T011 [US1] Add route assertions to `specs/021-hybrid-sdd-adaptation/fixtures/check.py` for Scenarios A–G, including one class only, `full-sdd` for substantial work, existing skill routing for routine content, and separated slices for mixed work.

### Implementation for User Story 1

- [ ] T012 [US1] Extend `scripts/hybrid-sdd-check.py` to reject missing/unknown `work_class`, invalid `route`, missing classification rationale, duplicate class assignments, and mixed requests that collapse routine content into full SDD.

**Checkpoint**: User Story 1 passes independently and validates SC-001, SC-013, and the routing parts of SC-008.

---

## Phase 4: User Story 2 — Specify playable outcomes without closing play (Priority: P1)

**Goal**: Require agency, independent world motion, conditional possibilities, and observable system behavior without authoring player decisions or fixed endings.

**Independent Test**: Run the regional-conflict and reputation-system fixtures; required agency fields pass and fixed player routes/endings fail.

### Tests for User Story 2

- [ ] T013 [P] [US2] Add a five-to-ten-session regional-conflict specification fixture at `specs/021-hybrid-sdd-adaptation/fixtures/evidence/regional-conflict.md` with actors, pressures, clocks, relationships, information states, if-nobody-intervenes motion, and open player decisions.
- [ ] T014 [P] [US2] Add a reusable reputation-system fixture at `specs/021-hybrid-sdd-adaptation/fixtures/evidence/reputation-system.md` with persistent state, faction behavior changes, information access changes, and conditional outcomes without selecting player actions.
- [ ] T015 [US2] Add fixture assertions to `specs/021-hybrid-sdd-adaptation/fixtures/check.py` for open outcomes, independent world motion, refusal/avoidance/negotiation/failure response surfaces, and rejection of mandatory allegiance, scene order, or ending.

### Implementation for User Story 2

- [ ] T016 [US2] Extend `scripts/hybrid-sdd-check.py` to validate the required agency fields from `data-model.md` and report predetermined player decisions or fixed campaign endings as objective contract violations.

**Checkpoint**: User Story 2 passes independently and validates SC-003 plus FR-007–FR-009.

---

## Phase 5: User Story 3 — Preserve truth ownership and the canon boundary (Priority: P1)

**Goal**: Resolve existing owners, preserve provenance and visibility, and keep proposed material outside accepted campaign truth until the existing DM acceptance path completes.

**Independent Test**: Run alias, uncertain-collision, conditional-event, and deterministic-maintenance fixtures; owner reuse/ambiguity, proposal state, visibility, and acceptance gates are observable.

### Tests for User Story 3

- [ ] T017 [P] [US3] Add an alias and uncertain-identity fixture at `specs/021-hybrid-sdd-adaptation/fixtures/evidence/entity-collision.md` showing owner reuse, collision evidence, and explicit distinction before a new owner.
- [ ] T018 [P] [US3] Add a canon-boundary fixture at `specs/021-hybrid-sdd-adaptation/fixtures/evidence/canon-boundary.md` showing current truth, affected truth, proposal, reveal/visibility, DM acceptance, and safe deterministic maintenance states.
- [ ] T019 [US3] Add fixture assertions to `specs/021-hybrid-sdd-adaptation/fixtures/check.py` that reject opaque IDs/second owners, silent canonization, lost provenance/visibility, and needless DM gates on deterministic maintenance.

### Implementation for User Story 3

- [ ] T020 [US3] Extend `scripts/hybrid-sdd-check.py` to validate canonical-owner reuse/ambiguity evidence, proposal versus accepted-truth transitions, reveal/visibility boundaries, and accept-before-write evidence using the existing vocabulary.

**Checkpoint**: User Story 3 passes independently and validates SC-004, SC-005, SC-014, and the canon/provenance failure modes NF-003–NF-005.

---

## Phase 6: User Story 4 — Plan and task real artifact dependencies (Priority: P2)

**Goal**: Make plans and task lists express authoritative context, ownership, agency/canon constraints, real dependency edges, and bounded parallelism without process theater.

**Independent Test**: Run the topology fixture; every dependency has a reason, parallel nodes have disjoint write ownership, and no task is parallel solely because it is prose.

### Tests for User Story 4

- [ ] T021 [P] [US4] Add serial/parallel dependency fixtures at `specs/021-hybrid-sdd-adaptation/fixtures/evidence/dependency-topology.json` covering grounding, owner resolution, missing owners, system state, relationships, situations, presentation, verification, Work, acceptance, filing, and maintenance where applicable.
- [ ] T022 [US4] Add topology assertions to `specs/021-hybrid-sdd-adaptation/fixtures/check.py` for dependency reasons, canonical owner identity, one active writer, disjoint parallel surfaces, and omission of ceremony without a real edge.

### Implementation for User Story 4

- [ ] T023 [US4] Extend `scripts/hybrid-sdd-check.py` to validate plan/task context-used and context-omitted fields, dependency ordering, owner/writer uniqueness, serial versus parallel waves, and class-appropriate engineering versus creative planning fields.

**Checkpoint**: User Story 4 passes independently and validates SC-006, SC-011, and NF-007–NF-008.

---

## Phase 7: User Story 5 — Verify the right things and keep both SDD paths compatible (Priority: P2)

**Goal**: Enforce objective hybrid gates, record efficiency evidence, preserve the normal Spec Kit lifecycle, and keep semantic judgment separate from deterministic lint.

**Independent Test**: Run hard-gate, telemetry, schema-evolution, promotion, and compatibility fixtures plus the live Spec Kit/OMP checks; objective failures are reported, semantic failures stay in blind evaluation, and integrations remain healthy.

### Tests for User Story 5

- [ ] T024 [P] [US5] Add the remaining failed, incomplete, additive-schema, incompatible-schema, retrieval-fallback, and tokenizer-mismatch inputs under `specs/021-hybrid-sdd-adaptation/fixtures/telemetry/`, alongside the seeded complete and measurement-gap records, with no raw prompt, wiki, campaign, or model content.
- [ ] T025 [P] [US5] Add hard-gate and semantic-separation fixtures at `specs/021-hybrid-sdd-adaptation/fixtures/evidence/verification-boundary.md`, covering canon precedence, entity-before-spoken, DM explicitness, reveal, visibility, accept-before-write, objective schema checks, and blind semantic review.
- [ ] T026 [US5] Add trace, report, quarantine, denominator, promotion, and compatibility assertions to `specs/021-hybrid-sdd-adaptation/fixtures/check.py`, including 90-day retention, measurement gaps, exclusive source ownership, and audit/replay metadata-only treatment.

### Implementation for User Story 5

- [ ] T027 [US5] Complete report and promotion input handling in `scripts/efficiency-trace.py` for the required metric vector, measured/estimated/inferred labels, same-kind paired replay, semantic non-inferiority, risk paths, canaries, and rollback results from `config/efficiency.yaml`.
- [ ] T028 [US5] Extend `scripts/hybrid-sdd-check.py` to record objective hard-gate results, reject subjective-quality lint claims, validate compatibility evidence, and fail closed on schema/tokenizer mismatches.

**Checkpoint**: User Story 5 passes independently and validates SC-007–SC-010 and SC-015–SC-025 without modifying generated Spec Kit integration files.

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Verify the complete route, preserve ownership boundaries, and leave a runnable handoff.

- [ ] T029 [P] Align `specs/021-hybrid-sdd-adaptation/quickstart.md` with the implemented CLI flags, fixture names, expected outputs, and native-tokenizer governance prerequisite.
- [ ] T030 Run `.venv/bin/python specs/021-hybrid-sdd-adaptation/fixtures/check.py`, `specify integration status --json`, and `./scripts/check-omp-baseline.sh`; record failures in `errors.md` and fix them before completion.
- [ ] T031 Verify `AGENTS.md`, `docs/agents/hybrid-sdd.md`, `config/efficiency.yaml`, `scripts/hybrid-sdd-check.py`, and `scripts/efficiency-trace.py` do not duplicate constitution, Work, QMD, token-measurement, or existing rubric ownership; keep generated `.agents/skills/speckit-*`, `.omp/commands/speckit.*`, and `.specify/templates/*` clean.
- [ ] T032 Run focused `git diff --check` and Markdown/literal-newline checks for `AGENTS.md`, `docs/agents/hybrid-sdd.md`, `config/efficiency.yaml`, `scripts/hybrid-sdd-check.py`, `scripts/efficiency-trace.py`, and `specs/021-hybrid-sdd-adaptation/` before handoff.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: T001–T003 can run in parallel; they establish ignored local storage and sanitized fixture inputs.
- **Foundational (Phase 2)**: T004–T009 depend on Setup. T007 and T008 can run in parallel after T004; T009 depends on both CLIs.
- **User Stories (Phases 3–7)**: All depend on T004–T009. Stories 1–3 are P1 and should complete before the first campaign-facing rollout. Story 4 depends on the route/ownership behavior from Stories 1 and 3. Story 5 depends on all prior contract surfaces and closes the compatibility/efficiency gate.
- **Polish (Phase 8)**: T029–T032 depend on the desired user stories; T030 and T032 are final validation gates.

### User Story Dependencies

- **US1 (P1)**: Starts after Foundational; no story dependency.
- **US2 (P1)**: Starts after Foundational; consumes US1's class/route identity but remains independently testable.
- **US3 (P1)**: Starts after Foundational; consumes US1's route identity and protects all campaign-facing routes.
- **US4 (P2)**: Depends on US1 and US3 for class/owner identity; independently tests topology after those contracts exist.
- **US5 (P2)**: Depends on US1–US4 for route, agency, canon, and topology evidence; compatibility checks also depend on the unchanged Spec Kit baseline.

### External Prerequisite

The separate tracked governance change that updates the repository-wide tokenizer authority must land before native-tokenizer comparisons are activated. No task in this feature may silently edit `AGENTS.md` token policy or `docs/agents/token-measurement.md` to bypass that prerequisite.

### Parallel Opportunities

- Setup fixtures T002–T003 can run in parallel with the `.gitignore` change T001.
- Foundational CLIs T007–T008 can run in parallel after policy T004; they have disjoint files.
- US2 fixture files T013–T014, US3 fixture files T017–T018, and US5 fixture files T024–T025 can each run in parallel within their story before shared checker assertions.
- No tasks that edit `fixtures/check.py`, `scripts/hybrid-sdd-check.py`, or `scripts/efficiency-trace.py` may run in parallel with another task editing the same file.

## Implementation Strategy

### MVP First

1. Complete Setup and Foundational phases.
2. Complete US1 and validate the seven-case route independently.
3. Complete US3 before exposing campaign-facing use, because routing without the canon boundary is unsafe.
4. Stop at the US1 + US3 checkpoint for the first reviewable MVP; do not activate native-tokenizer comparisons until the external governance prerequisite lands.

### Incremental Delivery

1. Deliver the route map and classifier fixture (US1).
2. Add agency/open-outcome protection (US2).
3. Add canon/provenance/acceptance protection (US3).
4. Add dependency topology and bounded parallelism checks (US4).
5. Add verification, telemetry, promotion, and compatibility evidence (US5).
6. Run the full quickstart and cross-cutting checks.

### Completion Evidence

Every completed task group reports the route, context used/omitted, affected owners, dependency state, deterministic checks, semantic/agency/continuity review where applicable, Work/DM acceptance state, filing state, and measurement status using [contracts/hybrid-sdd.md](./contracts/hybrid-sdd.md) and [contracts/efficiency-telemetry.md](./contracts/efficiency-telemetry.md).
