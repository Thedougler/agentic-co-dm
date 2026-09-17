---

description: "Task list for feature implementation"
---

# Tasks: Hybrid Spec-Driven Development

**Input**: Design documents from `/specs/021-hybrid-sdd-adaptation/`

**Prerequisites**: `plan.md`, `spec.md`, `research.md`, `data-model.md`, `contracts/`, and `quickstart.md`

**Tests**: No separate TDD tasks are included. The specification requires public fixture and CLI checks; those checks are implementation and verification surfaces below.

**Organization**: Tasks are grouped by user story in priority order. Each task names an exact canonical write surface, real predecessors, and the evidence that closes it.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Establish maintainer policy, local telemetry boundaries, and the feature fixture contract without editing generated Spec Kit integrations.

- [ ] T001 [P] Create the maintainer-owned efficiency policy with `schema_version`, `retention_days: 90`, `prep`/`wrapup` comparison classes, same-kind pairing, reduction thresholds, risk paths, canaries, shadow review, human review, rollback gates, and the pending native-tokenizer governance measurement gap in `config/efficiency.yaml`
- [ ] T002 [P] Add gitignore rules for `.local/efficiency/traces.jsonl`, quarantine output, and retention artifacts while leaving committed sanitized fixtures trackable in `.gitignore`
- [ ] T003 [P] Define sanitized fixture containers, stable scenario identifiers, route/evidence/telemetry record shapes, and the no-raw-content boundary in `specs/021-hybrid-sdd-adaptation/fixtures/README.md`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Install the progressive-disclosure route and shared artifact vocabulary before story-specific behavior is implemented.

**CRITICAL**: User-story implementation depends on this phase. Do not edit generated `.agents/skills/speckit-*`, `.omp/commands/speckit.*`, `.claude/skills/speckit-*`, `.grok/skills/speckit-*`, or managed `.specify/templates/*`.

- [ ] T004 [P] Replace the compact Spec Kit section outside the managed block with a route pointer that classifies substantial work, preserves routine campaign skill routing, and links to the detailed contract in `AGENTS.md`
- [ ] T005 [P] Write the progressive-disclosure hybrid SDD procedure covering classification, minimum context, canonical owners, agency, canon/DM acceptance, topology, verification, telemetry, promotion, and Spec Kit compatibility in `docs/agents/hybrid-sdd.md`
- [ ] T006 Record the generated-file preservation boundary, public command surfaces, and native-tokenizer governance prerequisite in `specs/021-hybrid-sdd-adaptation/quickstart.md`

**Checkpoint**: Route policy, detailed contract, maintainer thresholds, local-trace boundary, and fixture conventions are defined; no story checker can introduce a second authority.

---

## Phase 3: User Story 1 - Classify work before governing it (Priority: P1) 🎯 MVP

**Goal**: Classify substantial requests as exactly one SDD work class, route routine campaign content through its existing skill, and split mixed requests without fictional canon creation.

**Independent Test**: Run `python3 scripts/hybrid-sdd-check.py classify --fixtures specs/021-hybrid-sdd-adaptation/fixtures/routes/`; Scenarios A–G receive the expected route, rationale boundary, and mixed-slice split.

### Implementation for User Story 1

- [ ] T007 [P] [US1] Add agent-system, campaign-architecture, and creative-system route fixtures with `work_class`, `route: full-sdd`, rationale evidence, and scope boundaries in `specs/021-hybrid-sdd-adaptation/fixtures/routes/classification-system.json`
- [ ] T008 [P] [US1] Add engineering and routine-NPC fixtures proving ordinary engineering SDD and the existing `npc-design` skill route in `specs/021-hybrid-sdd-adaptation/fixtures/routes/classification-routine.json`
- [ ] T009 [P] [US1] Add entity-collision, proposed-canon, and mixed-request fixtures proving owner-resolution evidence, proposal status, and separate full-SDD/existing-skill slices in `specs/021-hybrid-sdd-adaptation/fixtures/routes/classification-boundaries.json`
- [ ] T010 [US1] Implement classification CLI parsing and validation for the exact classes `engineering`, `agent-system`, `campaign-architecture`, and `creative-system`, `full-sdd` versus `existing-skill` routes, rationale boundaries, routine content, and mixed-request splitting in `scripts/hybrid-sdd-check.py`

**Checkpoint**: US1 is independently runnable through the classification CLI and does not create a feature directory for routine content.

---

## Phase 4: User Story 2 - Specify playable outcomes without closing play (Priority: P1)

**Goal**: Validate campaign-facing and reusable-system specifications for independent actors, pressures, open player decisions, conditional outcomes, continuity, and if-nobody-intervenes motion without screenplay requirements.

**Independent Test**: Run `python3 scripts/hybrid-sdd-check.py agency --fixtures specs/021-hybrid-sdd-adaptation/fixtures/evidence/agency.json`; valid regional-conflict and reputation records pass while authored choices, fixed sequences/endings, and missing independent motion are rejected by negative fixtures.

### Implementation for User Story 2

- [ ] T011 [P] [US2] Add regional-conflict evidence for actors, factions, locations, clocks, relationships, information states, pressures, conditional opportunities, continuity, and open outcomes in `specs/021-hybrid-sdd-adaptation/fixtures/evidence/agency.json`
- [ ] T012 [P] [US2] Add reputation-system evidence for persistent state, faction behavior changes, information access changes, player-caused changes, and refusal/avoidance/negotiation response surfaces in `specs/021-hybrid-sdd-adaptation/fixtures/evidence/reusable-system.json`
- [ ] T013 [P] [US2] Add negative agency fixtures for mandatory allegiance, authored player decisions, fixed scene sequence, fixed ending, predetermined route, and missing independent-world motion in `specs/021-hybrid-sdd-adaptation/fixtures/evidence/agency-failures.json`
- [ ] T014 [US2] Extend the agency verifier to require observable value, actors, pressures, open outcomes, conditional possibilities, independent motion, if-nobody-intervenes consequences, player-owned decisions, and continuity while rejecting screenplay constraints in `scripts/hybrid-sdd-check.py`

**Checkpoint**: US2 is independently verifiable from sanitized evidence and keeps creative judgment separate from objective agency-boundary checks.

---

## Phase 5: User Story 3 - Preserve truth ownership and the canon boundary (Priority: P1)

**Goal**: Reuse existing owners, preserve provenance/reveal/visibility, keep proposals distinct from accepted truth, and allow safe deterministic maintenance without needless DM approval.

**Independent Test**: Run `python3 scripts/hybrid-sdd-check.py canon --fixtures specs/021-hybrid-sdd-adaptation/fixtures/evidence/`; equivalent aliases reuse owners or surface ambiguity, proposed events remain proposals, and deterministic maintenance is not blocked.

### Implementation for User Story 3

- [ ] T015 [P] [US3] Add title, alias, stem, deterministic-path, wikilink, QMD, manifest, duplicate-candidate, equivalent-owner, and uncertain-collision evidence in `specs/021-hybrid-sdd-adaptation/fixtures/evidence/ownership.json`
- [ ] T016 [P] [US3] Add current-truth, affected-truth, proposal, provenance, reveal, visibility, DM-acceptance, canon-state, and filing-state evidence in `specs/021-hybrid-sdd-adaptation/fixtures/evidence/canon-boundary.json`
- [ ] T017 [P] [US3] Add safe deterministic maintenance and invalid accept-before-write evidence, distinguishing `not-required` maintenance from DM-gated fact changes, in `specs/021-hybrid-sdd-adaptation/fixtures/evidence/maintenance-boundary.json`
- [ ] T018 [US3] Extend canon verification with owner reuse and collision reporting, `unchanged`/`proposal`/`accepted-truth` states, acceptance transitions, reveal/visibility protection, accept-before-write hard gates, and non-fact maintenance handling in `scripts/hybrid-sdd-check.py`

**Checkpoint**: US3 is independently verifiable without writing wiki facts, introducing opaque IDs, or adding a second lifecycle or owner model.

---

## Phase 6: User Story 4 - Plan and task real artifact dependencies (Priority: P2)

**Goal**: Represent minimum sufficient context, canonical owners, real dependency edges, serial/parallel waves, agency/continuity constraints, and single-writer ownership in plans and tasks.

**Independent Test**: Run `python3 scripts/hybrid-sdd-check.py topology --fixtures specs/021-hybrid-sdd-adaptation/fixtures/evidence/topology.json`; valid prerequisites pass while a parallel wave sharing a canonical artifact or containing dependent nodes fails.

### Implementation for User Story 4

- [ ] T019 [P] [US4] Add a valid dependency graph from grounding/retrieval through owner resolution, missing owners, rules/system/world state, relationships/agendas, playable situations, presentation, continuity verification, Work proposal, DM acceptance, filing/promotion, and deterministic maintenance in `specs/021-hybrid-sdd-adaptation/fixtures/evidence/topology.json`
- [ ] T020 [P] [US4] Add valid disjoint parallel waves plus invalid shared-writer and dependent-parallel cases with artifact owners and evidence in `specs/021-hybrid-sdd-adaptation/fixtures/evidence/parallel-ownership.json`
- [ ] T021 [P] [US4] Add engineering-plan evidence for technical context, architecture, storage, testing, platform, performance, constraints, and source structure without campaign-only vocabulary in `specs/021-hybrid-sdd-adaptation/fixtures/evidence/engineering-plan.json`
- [ ] T022 [US4] Extend topology and plan verification with dependency resolution, cycle detection, wave ordering, disjoint canonical write surfaces, `context_used`/`context_omitted`, and engineering-versus-creative vocabulary checks in `scripts/hybrid-sdd-check.py`

**Checkpoint**: US4 is independently verifiable from topology fixtures and reports only real dependency, context, or ownership constraints.

---

## Phase 7: User Story 5 - Verify the right things and keep both SDD paths compatible (Priority: P2)

**Goal**: Provide deterministic hard gates, redacted efficiency telemetry, promotion evidence, preset trust-boundary checks, and lifecycle compatibility without treating creative judgment as lint.

**Independent Test**: Run `.venv/bin/python specs/021-hybrid-sdd-adaptation/fixtures/check.py`; it emits one `PASS` summary after exercising route, evidence, telemetry, schema, retention, promotion, preset, and compatibility fixtures.

### Implementation for User Story 5

- [ ] T023 [US5] Extend verification with closed-vocabulary, schema, filename, link, owner, lifecycle, canon-precedence, entity-before-spoken, DM-explicitness, reveal, visibility, accept-before-write, completion-evidence, semantic-boundary, and Spec Kit compatibility checks in `scripts/hybrid-sdd-check.py`
- [ ] T024 [US5] Implement `record` validation for explicit `schema_version`, `prep`/`wrapup` sitting classes, produced/accepted/failed/incomplete Work, complete/measurement-gap status, model/tokenizer identity, non-negative trajectory and retrieval counts, redacted-only fields, and one exclusive primary source owner per token occurrence in `scripts/efficiency-trace.py`
- [ ] T025 [US5] Implement labeled report metrics for trajectory/input/output/source-component/retrieval tokens, retries, hard failures, DM acceptance/revisions, runtime failures, useful/unused retrieval, status counts, denominators, and same-kind job groups in `scripts/efficiency-trace.py`
- [ ] T026 [US5] Implement additive schema compatibility, incompatible-record quarantine without history rewriting, explicit measurement gaps, 90-day retention, same-family comparison rejection, and low/moderate/high-risk promotion gates with pinned pairs, 5% median reduction, canary/shadow/human review, and rollback in `scripts/efficiency-trace.py`
- [ ] T027 [P] [US5] Add complete, produced/accepted/failed/incomplete, disabled, pre-governance, fallback, attribution, additive-schema, incompatible-schema, paired-promotion, and retention records under `specs/021-hybrid-sdd-adaptation/fixtures/telemetry/`
- [ ] T028 [P] [US5] Add deterministic hard-gate, independent blind paired semantic-review boundary, completion-evidence, and managed-integration compatibility records in `specs/021-hybrid-sdd-adaptation/fixtures/evidence/verification.json`
- [ ] T029 [P] [US5] Create the repository-owned `creative-llm-wiki` meta-preset package with manifest, reviewed selective adaptations, source-candidate provenance, validation metadata, and no third-party runtime dependency under `.specify/presets/creative-llm-wiki/`
- [ ] T030 [US5] Implement the feature-local fixture runner with isolated temporary trace/quarantine paths, route/evidence/telemetry/preset checks, one `PASS` summary, and failure exit status in `specs/021-hybrid-sdd-adaptation/fixtures/check.py`
- [ ] T031 [US5] Document public CLI commands, fixture expectations, report labels and denominators, promotion paths, preset staging, compatibility checks, and native-tokenizer governance blocking in `specs/021-hybrid-sdd-adaptation/quickstart.md`

**Checkpoint**: US5 is independently runnable and preserves specify, clarify, plan, checklist, tasks, analyze, implement, converge, git, and agent-context behavior.

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Validate the complete feature without modifying campaign content or managed Spec Kit artifacts.

- [ ] T032 [P] Run `.venv/bin/python specs/021-hybrid-sdd-adaptation/fixtures/check.py` and record the observed route, evidence, telemetry, preset, promotion, retention, and compatibility `PASS` result in `specs/021-hybrid-sdd-adaptation/quickstart.md`
- [ ] T033 [P] Run `specify integration status --json` and record `status: ok`, default `omp`, four integrations, and zero missing/modified managed files in `specs/021-hybrid-sdd-adaptation/quickstart.md`
- [ ] T034 [P] Run `./scripts/check-omp-baseline.sh` and record its passing result in `specs/021-hybrid-sdd-adaptation/quickstart.md`
- [ ] T035 Audit `specs/021-hybrid-sdd-adaptation/` and all feature-owned source paths for generated-file edits, raw-content telemetry, duplicate authorities, missing owner/evidence fields, invalid vocabulary, unlabelled metrics, and missing preset provenance; record corrections in the owning files

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: T001–T003 have disjoint write surfaces and can run in parallel.
- **Foundational (Phase 2)**: T004–T006 depend on the feature documents and block all user stories.
- **User Story 1 (Phase 3)**: T007–T009 can run in parallel; T010 follows those fixtures and owns the checker classification seam.
- **User Story 2 (Phase 4)**: T011–T013 can run in parallel; T014 follows T010 and extends the checker serially.
- **User Story 3 (Phase 5)**: T015–T017 can run in parallel; T018 follows T014 and extends the checker serially.
- **User Story 4 (Phase 6)**: T019–T021 can run in parallel; T022 follows T018 and extends the checker serially.
- **User Story 5 (Phase 7)**: T023 follows T022; T024–T026 are serial because they share `scripts/efficiency-trace.py`; T027–T029 can run in parallel after their schemas are defined; T030 follows T023–T029; T031 follows the public surfaces.
- **Polish (Phase 8)**: T032–T034 can run in parallel after US5; T035 follows all validation and audits the complete feature.

### User Story Dependencies

- **US1 (P1)**: Depends only on Foundational; the route classification CLI is the MVP.
- **US2 (P1)**: Depends on US1's checker CLI and route identity, then adds agency validation.
- **US3 (P1)**: Depends on US2's evidence vocabulary and checker, then adds owner/canon hard gates.
- **US4 (P2)**: Depends on US3's owner/canon state vocabulary, then adds dependency and single-writer topology.
- **US5 (P2)**: Depends on US4's topology/completion evidence, then adds telemetry, presets, deterministic/semantic boundaries, and compatibility checks.

### Parallel Opportunities

- Setup policy, ignore rules, and fixture-contract documentation are disjoint.
- US1 route fixture groups are disjoint.
- US2–US4 evidence fixture files are disjoint; checker changes remain serial because `scripts/hybrid-sdd-check.py` has one canonical writer.
- US5 telemetry, verification, and preset package artifacts are disjoint after their schemas are fixed; post-US5 repository checks are disjoint.
- No task is marked `[P]` when it depends on another incomplete task or shares a canonical write surface with another task in its wave.

## Parallel Example: User Story 1

```text
Task T007: Add system-class route fixtures in specs/021-hybrid-sdd-adaptation/fixtures/routes/classification-system.json
Task T008: Add engineering/routine route fixtures in specs/021-hybrid-sdd-adaptation/fixtures/routes/classification-routine.json
Task T009: Add boundary/mixed route fixtures in specs/021-hybrid-sdd-adaptation/fixtures/routes/classification-boundaries.json
```

## Parallel Example: User Story 2

```text
Task T011: Add regional-conflict evidence in specs/021-hybrid-sdd-adaptation/fixtures/evidence/agency.json
Task T012: Add reusable-system evidence in specs/021-hybrid-sdd-adaptation/fixtures/evidence/reusable-system.json
Task T013: Add negative agency evidence in specs/021-hybrid-sdd-adaptation/fixtures/evidence/agency-failures.json
```

## Parallel Example: User Story 3

```text
Task T015: Add owner-resolution evidence in specs/021-hybrid-sdd-adaptation/fixtures/evidence/ownership.json
Task T016: Add canon-boundary evidence in specs/021-hybrid-sdd-adaptation/fixtures/evidence/canon-boundary.json
Task T017: Add maintenance-boundary evidence in specs/021-hybrid-sdd-adaptation/fixtures/evidence/maintenance-boundary.json
```

## Parallel Example: User Story 4

```text
Task T019: Add valid topology evidence in specs/021-hybrid-sdd-adaptation/fixtures/evidence/topology.json
Task T020: Add parallel-ownership evidence in specs/021-hybrid-sdd-adaptation/fixtures/evidence/parallel-ownership.json
Task T021: Add engineering-plan evidence in specs/021-hybrid-sdd-adaptation/fixtures/evidence/engineering-plan.json
```

## Parallel Example: User Story 5

```text
Task T027: Add telemetry fixtures under specs/021-hybrid-sdd-adaptation/fixtures/telemetry/
Task T028: Add verification-boundary fixtures in specs/021-hybrid-sdd-adaptation/fixtures/evidence/verification.json
Task T029: Create the reviewed creative-llm-wiki package under .specify/presets/creative-llm-wiki/
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Setup and Foundational phases.
2. Complete US1 route fixtures and `scripts/hybrid-sdd-check.py` classification behavior.
3. Run `python3 scripts/hybrid-sdd-check.py classify --fixtures specs/021-hybrid-sdd-adaptation/fixtures/routes/` independently.
4. Stop at the US1 checkpoint for an independently usable route decision.

### Incremental Delivery

1. Add US2 agency/open-outcome checks without changing routine content routing.
2. Add US3 owner/canon hard gates without writing campaign facts.
3. Add US4 real dependency topology and single-writer validation.
4. Add US5 telemetry, promotion, preset trust-boundary, deterministic/semantic boundaries, and compatibility checks.
5. Run the complete fixture and repository checks only after the final story is complete.

### Safety Boundaries

- Do not edit generated harness adapters or managed Spec Kit templates.
- Do not create a second canon, lifecycle, owner model, retrieval system, database, or opaque entity-ID layer.
- Do not write accepted campaign truth from specifications, plans, tasks, telemetry, or preset packages.
- Do not store raw prompt, wiki, campaign, model, or provider content in normal traces.
- Do not activate native-tokenizer comparisons or promotion before the separate governance change; record `measurement-gap` with reason `native-tokenizer-governance-pending` instead.
- Treat community preset packages as pinned, inspected, untrusted staging inputs; adapt selected patterns with provenance and never install or copy a complete package wholesale.
