---

description: "Task list for feature implementation"
---

# Tasks: Creative Linting

**Input**: Design documents from `/specs/024-creative-linting/`

**Prerequisites**: `plan.md`, `spec.md`, `research.md`, `data-model.md`, `contracts/`, `quickstart.md`

**Tests**: Included because the specification defines independently testable acceptance scenarios, fixture suites, and the repository constitution requires behavioral tests for new system behavior.

**Organization**: Tasks are grouped by user story. Story phases follow dependency order within the P1/P2/P3 priority bands so every task is executable; the dependency graph explains why the MVP story is delivered after its enabling P1 stories.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Establish repository-owned configuration, package metadata, directories, and fixture surfaces.

- [ ] T001 Create `tools/creative_lint/__init__.py` and `tools/creative_lint/evaluators/__init__.py` package entry points.
- [ ] T002 [P] Add `PyYAML>=6,<7` to the `dependencies` list in `pyproject.toml` without removing existing dependencies.
- [ ] T003 [P] Create root `package.json` with `private: true`, `engines.node: ">=22"`, and thin `npm run` aliases that delegate directly to existing lint, maintenance, verification, and test commands.
- [ ] T004 Generate and commit the pinned `package-lock.json` for `markdownlint-cli2` version `0.23.2` from `package.json` using npm, with no Node implementation wrapper.
- [ ] T005 [P] Create `.vale.ini` with `StylesPath = styles`, `MinAlertLevel = suggestion`, authoritative packages `ai-tells`, `proselint`, `Readability`, and `Harper`, and the documented wiki, staging, raw, archive, fixture, and template scopes.
- [ ] T006 [P] Create `.markdownlint-cli2.jsonc` with repository structural rules and exclusions for `wiki/_raw`, `wiki/_staging`, `wiki/_archive`, and `wiki/templates`.
- [ ] T007 [P] Create `styles/CoDM/`, `rules/shadow/`, and `rules/candidates/` directory surfaces with tracked placeholders where empty directories cannot be versioned.
- [ ] T008 [P] Create `tests/fixtures/creative_lint/` subdirectories for rule fixtures, integration fixtures, registry fixtures, and symbolic evaluator fixtures.
- [ ] T009 [P] Align prerequisites and commands in `specs/024-creative-linting/quickstart.md` with Python 3.14, PyYAML 6.x, Node.js >=22, Vale 3.13.0, npm, and the committed lockfile.

---

## Phase 2: Foundational (Blocking Contracts)

**Purpose**: Implement shared finding and vocabulary primitives required by every evaluator and CLI surface.

**Checkpoint**: Finding construction, serialization, and validation constants are stable before story-specific implementation begins.

- [ ] T010 [P] Implement the universal `Finding` dataclass and `to_dict()` serialization in `tools/creative_lint/finding.py` from `contracts/finding-schema.md`, including required `rule_id`, `result`, `severity`, `location.file`, `evidence`, `reason`, and `evaluator` fields plus optional `repair_target` and `waiver`.
- [ ] T011 [P] Define shared allowed values, rule-ID validation, severity ordering, category names, evaluator names, lifecycle names, and result names in `tools/creative_lint/constants.py`.

---

**Checkpoint**: Foundation ready; user-story implementation can begin according to the dependency graph.

---

## Phase 3: User Story 3 - Rule Registry and Stable IDs (Priority: P1)

**Goal**: Make rule metadata discoverable from one validated YAML registry and keep consumers on stable IDs rather than duplicated prose.

**Independent Test**: Load `rules/registry.yml`, query a rule by ID, verify complete metadata, reject duplicate or malformed definitions, and confirm bundle resolution later consumes IDs rather than inline rule logic.

### Tests for User Story 3

- [ ] T012 [US3] Add registry behavior tests in `tests/test_creative_lint.py` for YAML loading, `get()`, category/evaluator queries, active/shadow filtering, duplicate IDs, malformed IDs, invalid enums, missing required fields, invalid Vale paths, and unresolved references.

### Implementation for User Story 3

- [ ] T013 [US3] Implement `RuleDefinition` and `Registry` in `tools/creative_lint/registry.py` with the APIs in `contracts/registry-contract.md`: `load`, `get`, `by_category`, `by_evaluator`, `active`, `shadow`, `all_ids`, and `validate`.
- [ ] T014 [US3] Add registry validation in `tools/creative_lint/registry.py` for required fields, unique IDs, `^[A-Z]+\\d{3}$` format, category/scope/severity/evaluator/lifecycle enums, existing Vale styles, reference warnings, and the `scene`/`diversity` severity ceiling of `WARN`.
- [ ] T015 [US3] Populate `rules/registry.yml` with the initial rule set from `research.md` R7: AGENCY001-003, CANON001-002, KNOW001-002, TEMP001, SCENE001-002, WIKI001-002, DIVERSITY001, and RETRIEVAL001, including metadata, lifecycle, repairs, tags, conflicts, dependencies, and Vale style references.
- [ ] T016 [US3] Add registry metadata fixtures under `tests/fixtures/creative_lint/registry/` covering a valid rule, duplicate ID, invalid ID, missing Vale style, invalid enum, unresolved reference, and a scene rule above the `WARN` ceiling.

**Checkpoint**: Rule definitions are the single metadata source and are independently queryable and validated.

---

## Phase 4: User Story 4 - Five-Level Severity Model (Priority: P2)

**Goal**: Compute action status and severity gates so objective defects require repair while creative diagnostics never become hidden mandates.

**Independent Test**: Evaluate findings at all five levels and verify `repair_required`, `review_needed`, and `clean` statuses; reject subjective `BLOCK` definitions in `scene` and `diversity` categories.

### Tests for User Story 4

- [ ] T017 [US4] Add severity behavior tests in `tests/test_creative_lint.py` for ordering, severity capping, `repair_required` for BLOCK/REPAIR, `review_needed` for REVIEW-only results, `clean` for WARN/INFO-only results, and the creative category ceiling.

### Implementation for User Story 4

- [ ] T018 [US4] Implement `SEVERITY_ORDER`, `min_severity()`, status computation, and category ceilings in `tools/creative_lint/severity.py`, preserving the independent lifecycle/severity dimensions and the FR-005, FR-006, and FR-016 action semantics.

**Checkpoint**: Severity decisions are deterministic, observable, and independent of evaluator implementation.

---

## Phase 5: User Story 6 - Multiple Evaluator Types (Priority: P2)

**Goal**: Dispatch static Vale and symbolic checks through one engine and one finding schema, preserving abstention and evaluator-unavailable states.

**Independent Test**: Run AGENCY001 through Vale and WIKI/CANON rules through symbolic evaluation; verify identical finding shape, no LLM call for static rules, and `abstain` or `evaluator_unavailable` when semantic capability is unavailable.

### Tests for User Story 6

- [ ] T019 [US6] Add evaluator and schema tests in `tests/test_creative_lint.py` for Vale mapping, symbolic mapping, `pass|fail|abstain`, unavailable evaluator records, location fields, registry-derived severity, and all required finding-schema fields.

### Implementation for User Story 6

- [ ] T020 [P] [US6] Create Vale rule files `styles/CoDM/AGENCY001.yml`, `AGENCY002.yml`, `AGENCY003.yml`, `KNOW001.yml`, `KNOW002.yml`, `TEMP001.yml`, `SCENE001.yml`, and `SCENE002.yml` using the required extension points, scopes, severity mappings, and ID-bearing messages from `contracts/vale-style-contract.md`.
- [ ] T021 [P] [US6] Implement Vale invocation and JSON mapping in `tools/creative_lint/vale_adapter.py`, passing the repository `.vale.ini`, stripping the `CoDM.` check prefix, mapping line/span/match fields, resolving registry metadata, and warning gracefully when Vale is absent.
- [ ] T022 [P] [US6] Implement symbolic evaluators in `tools/creative_lint/evaluators/symbolic.py` for CANON001, CANON002, WIKI001, WIKI002, and RETRIEVAL001 by wrapping existing `tools/lint_wiki.py` findings without modifying that engine.
- [ ] T023 [P] [US6] Add evaluator fixtures under `tests/fixtures/creative_lint/symbolic/` for dead and stale canon references, valid references, missing frontmatter, invalid lifecycle/type, broken wikilinks, and indeterminate evaluation.
- [ ] T024 [US6] Implement `LintResult` and evaluator orchestration in `tools/creative_lint/engine.py`, merging Vale and symbolic findings, supporting semantic/human unavailable states, applying metadata, computing summary counts, and deriving status.
- [ ] T025 [US6] Add conflict detection to `tools/creative_lint/engine.py` for opposing active rules in one run, emitting `LINT-CONFLICT` with precedence guidance without silently choosing a creative outcome.

**Checkpoint**: Static and symbolic evaluators run through the universal finding contract.

---

## Phase 6: User Story 5 - Task-Specific Rule Bundles (Priority: P2)

**Goal**: Scope evaluation to named task bundles and apply category-specific severity gates without duplicating rule logic.

**Independent Test**: Resolve `session-prep` and `wiki-ingest` against the same registry and verify included categories, excluded categories, and effective severities differ as configured.

### Tests for User Story 5

- [ ] T026 [US5] Add bundle-resolution tests in `tests/test_creative_lint.py` for all initial bundles, category exclusion, BLOCK/REVIEW/WARN gate capping, duplicate category placement, active-only resolution, and unknown bundle errors.

### Implementation for User Story 5

- [ ] T027 [P] [US5] Implement `BundleDefinition` and `BundleRegistry` in `tools/creative_lint/bundles.py` with YAML loading, `get()`, available-name reporting, and `resolve(registry)` returning `(RuleDefinition, effective_severity)` pairs.
- [ ] T028 [P] [US5] Populate `rules/bundles.yml` with `session-prep`, `wiki-ingest`, `worldbuilding`, `live-codm`, and `corpus` definitions from `research.md` R8, including descriptions and block/review/diagnostics category gates.
- [ ] T029 [US5] Integrate bundle resolution into `tools/creative_lint/engine.py` so only configured categories execute, diagnostics cap at WARN, rule severity remains authoritative within the gate, and SHADOW rules are returned separately.

**Checkpoint**: Task bundles control rule scope and action severity.

---

## Phase 7: User Story 2 - wiki-lint CLI for Files and Corpus (Priority: P1)

**Goal**: Expose task, file, corpus, changed, and rule operations while preserving existing no-subcommand structural behavior.

**Independent Test**: Run every CLI surface against fixtures and a missing-frontmatter page; verify JSON and human output, severity filters, unknown-input errors, and exit codes 0/1/2.

### Tests for User Story 2

- [ ] T030 [US2] Add subprocess tests in `tests/test_creative_lint_cli.py` for `task`, `file`, `corpus`, `changed`, `rule`, and `--consolidate`, including JSON schema, human rendering, severity filtering, dry-run/approval behavior, unknown bundle/rule errors, and exit codes.
- [ ] T031 [US2] Add a no-subcommand regression test in `tests/test_creative_lint_cli.py` proving `scripts/wiki-lint --json wiki` retains the existing structural report shape and exit behavior.

### Implementation for User Story 2

- [ ] T032 [US2] Refactor `scripts/wiki-lint` to dispatch only when the first positional argument is `task`, `file`, `corpus`, `changed`, or `rule`, importing `tools.creative_lint` lazily so legacy startup and delegation remain unchanged.
- [ ] T033 [US2] Implement `task` and `file` handlers in `scripts/wiki-lint` with bundle/inherent severity execution, path resolution, `--json`, `--severity`, and the contract exit codes.
- [ ] T034 [US2] Implement `corpus` and `changed` handlers in `scripts/wiki-lint`, respecting the existing wiki skip directories and selecting changed Markdown files from `git diff --name-only HEAD`.
- [ ] T035 [US2] Implement `rule` output in `scripts/wiki-lint` with registry metadata and bundle memberships, plus exit-2 messages for unknown IDs and invalid registry YAML.
- [ ] T036 [US2] Implement human-readable rendering, severity filtering, and `--consolidate` dry-run/explicit-approval orchestration in `tools/creative_lint/cli_output.py` and `scripts/wiki-lint`, preserving report-only behavior and stale-plan rejection from `contracts/cli-contract.md`.

**Checkpoint**: Agents and humans can invoke every specified lint surface without regressing structural mode.

---

## Phase 8: User Story 1 - Agent Lints Generated Output (Priority: P1) — MVP

**Goal**: Let agents lint generated Work, repair BLOCK/REPAIR findings, surface REVIEW findings, preserve WARN/INFO diagnostics, and re-lint changed output.

**Independent Test**: Run `wiki-lint task session-prep` against output containing AGENCY001 and CANON002 violations, apply a repair, and verify the changed surface has no blocking findings while diagnostics remain visible.

### Tests for User Story 1

- [ ] T037 [US1] Add end-to-end agent-loop tests in `tests/test_creative_lint.py` for AGENCY001 and CANON002 findings, repair traceability by rule ID/location, WARN/INFO non-mandate behavior, REVIEW surfacing, changed-surface re-linting, and clean convergence.

### Implementation for User Story 1

- [ ] T038 [US1] Implement `repair_loop()` in `tools/creative_lint/engine.py` with configurable maximum `3` iterations, repair callbacks receiving exact findings, changed-surface re-linting, and escalation of unconverged findings for DM review.
- [ ] T039 [P] [US1] Add `tests/fixtures/creative_lint/integration/session_prep_violations.md` containing an authored PC decision and a stale/dead canonical entity reference for the independent acceptance scenario.
- [ ] T040 [US1] Document the agent invocation and repair contract in `docs/creative-linting.md`, stating that BLOCK/REPAIR must be repaired, REVIEW must be surfaced, and WARN/INFO must not be mechanically optimized away.

**Checkpoint**: The MVP agent loop produces actionable findings and converges or escalates after three repair passes.

---

## Phase 9: User Story 7 - Rule Lifecycle and Shadow Mode (Priority: P3)

**Goal**: Evaluate SHADOW rules and record telemetry without changing active agent-facing behavior.

**Independent Test**: Run a SHADOW rule, verify telemetry exists while active findings and status remain unchanged, then promote it to ACTIVE and verify it appears with the same severity.

### Tests for User Story 7

- [ ] T041 [US7] Add lifecycle and shadow tests in `tests/test_creative_lint.py` for DRAFT skipping, SHADOW telemetry, ACTIVE output, promotion evidence, severity independence, and creative diagnostic ceilings.

### Implementation for User Story 7

- [ ] T042 [US7] Implement append-only shadow telemetry in `tools/creative_lint/shadow.py`, writing per-rule JSONL under `rules/shadow/` and exposing agreement, false-positive, and repair-helpfulness measurements.
- [ ] T043 [US7] Wire lifecycle filtering and shadow recording into `tools/creative_lint/engine.py`, excluding SHADOW findings from agent output/status while exposing them in `LintResult.shadow`.
- [ ] T044 [US7] Add `rules/shadow/` telemetry files to `.gitignore` and document DRAFT → SHADOW → ACTIVE promotion evidence in `docs/creative-linting.md`.

**Checkpoint**: New rules can be measured safely before activation.

---

## Phase 10: User Story 8 - Explicit Waivers (Priority: P3)

**Goal**: Suppress a specific rule/target only with an owned, reasoned, expiring waiver.

**Independent Test**: Apply a valid waiver before expiry, verify suppression metadata and summary counts, then verify the finding returns after expiry; reject a waiver without expiry.

### Tests for User Story 8

- [ ] T045 [US8] Add waiver behavior tests in `tests/test_creative_lint.py` for required fields, exact rule matching, `file:`, `npc:`, `session:`, and `*` targets, active/expired waivers, suppression metadata, and missing expiry rejection.

### Implementation for User Story 8

- [ ] T046 [US8] Implement `Waiver` and `WaiverRegistry` in `tools/creative_lint/waivers.py` with required rule ID, target, reason, owner, granted, and expires fields plus expiry checks.
- [ ] T047 [US8] Integrate waiver matching into `tools/creative_lint/engine.py`, attaching waiver metadata, excluding matched findings from repair status, and counting waived findings without deleting audit records.
- [ ] T048 [US8] Validate the repository-owned `rules/waivers.json` shape and document DM approval, target matching, and expiry workflow in `docs/creative-linting.md`.

**Checkpoint**: Contextual exceptions are explicit, auditable, and temporary.

---

## Phase 11: User Story 9 - Rule Fixtures and Testing (Priority: P3)

**Goal**: Define should-fail, should-pass, and ambiguous acceptable-region fixtures for every nontrivial rule.

**Independent Test**: Run the fixture harness and verify fail fixtures trigger, pass fixtures do not, and ambiguous fixtures are recorded without failing the suite.

### Tests and Implementation for User Story 9

- [ ] T049 [P] [US9] Create Vale fixtures under `tests/fixtures/creative_lint/AGENCY001/`, `AGENCY002/`, `AGENCY003/`, `KNOW001/`, `KNOW002/`, `TEMP001/`, `SCENE001/`, and `SCENE002/` using `fail_*.md`, `pass_*.md`, and `ambiguous_*.md` names.
- [ ] T050 [P] [US9] Create symbolic fixtures under `tests/fixtures/creative_lint/CANON001/`, `CANON002/`, `WIKI001/`, `WIKI002/`, and `RETRIEVAL001/`, including valid counterexamples and the required frontmatter/state context.
- [ ] T051 [US9] Implement fixture discovery and assertions in `tests/test_creative_lint.py`, requiring should-fail and should-pass coverage for every active BLOCK rule and recording ambiguous outcomes without failing the suite.

**Checkpoint**: Fixture coverage protects the acceptable region and satisfies the active BLOCK-rule regression requirement.

---

## Phase 12: User Story 10 - DM Correction Becomes Rule (Priority: P3)

**Goal**: Route recurring DM corrections to an existing rule or a measured SHADOW candidate without creating duplicates.

**Independent Test**: Classify the knowledge-boundary correction against KNOW002 or emit a SHADOW candidate template with fixture and promotion requirements; insufficient precision must not promote it.

### Tests for User Story 10

- [ ] T052 [US10] Add correction-classification tests in `tests/test_creative_lint_cli.py` for existing-rule matches, no-match candidate output, SHADOW lifecycle defaults, duplicate avoidance, and insufficient-precision non-promotion.

### Implementation for User Story 10

- [ ] T053 [US10] Implement the `candidate` command in `scripts/wiki-lint` to match correction text against registry titles/messages/tags and emit a repository-owned SHADOW candidate template under `rules/candidates/` when no existing rule matches.
- [ ] T054 [US10] Document correction routing, fixture requirements, telemetry thresholds of greater than 90% human agreement and less than 10% false positives, and promotion review in `docs/creative-linting.md`.

**Checkpoint**: A DM correction becomes an inspectable rule-improvement path rather than duplicated prompt prose.

---

## Phase 13: Polish & Cross-Cutting Integration

**Purpose**: Integrate corpus maintenance, complete off-the-shelf Markdown migration, finish documentation, and prove the full contract.

- [ ] T055 [P] Integrate the `corpus` bundle into `scripts/wiki-maintain` as an optional Layer A report step using the same `tools/creative_lint/engine.py` implementation and compact JSON output.
- [ ] T056 [P] Port checks from `scripts/lint-obsidian-markdown` and `scripts/lint-literal-newlines` into `.markdownlint-cli2.jsonc` and corresponding fixture cases under `tests/fixtures/creative_lint/`, retaining the legacy scripts until equivalent coverage passes.
- [ ] T057 Remove or deprecate `scripts/lint-obsidian-markdown` and `scripts/lint-literal-newlines` only after their checks have passing markdownlint-cli2 fixtures, and update every caller to the replacement surface.
- [ ] T058 [P] Complete `docs/creative-linting.md` with architecture, rule authoring, bundle configuration, CLI examples, finding schema, lifecycle, waivers, fixtures, and maintenance integration.
- [ ] T059 Run validation scenarios V1–V8 from `specs/024-creative-linting/quickstart.md` and record only required command corrections in that file.
- [ ] T060 Run `.venv/bin/python -m pytest tests/test_creative_lint.py tests/test_creative_lint_cli.py -v` and the existing structural regression command from `specs/024-creative-linting/quickstart.md`; resolve failures without changing accepted behavior.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies; tasks T002–T003, T005–T008 can proceed in parallel, while T004 follows T003.
- **Foundational (Phase 2)**: Depends on Setup and blocks all user stories.
- **US3 (P1)**: Depends on the shared finding/constants primitives; establishes registry metadata.
- **US4 (P2)**: Depends on shared constants and registry validation; establishes status and severity semantics.
- **US6 (P2)**: Depends on US3 and US4; provides evaluator adapters and the engine.
- **US5 (P2)**: Depends on US6's engine contract; adds bundle scoping and gates.
- **US2 (P1)**: Depends on US5 and US6; provides the CLI entry point used by the MVP.
- **US1 (P1 MVP)**: Depends on US2 and the complete engine path; validates the agent repair loop.
- **US7, US8, and US9 (P3)**: Depend on US6 and can proceed independently of one another and of US1 after the engine contract exists.
- **US10 (P3)**: Depends on US2's registry/CLI surface.
- **Polish (final)**: Depends on the selected stories and passing replacement fixtures.

### User Story Dependencies

- **US3**: No user-story dependency after Phase 2.
- **US4**: Depends on Phase 2; registry ceiling validation is consumed by the engine.
- **US6**: Requires US3 registry metadata and US4 severity semantics.
- **US5**: Requires US6 evaluator orchestration.
- **US2**: Requires US5 bundle resolution and US6 engine integration.
- **US1**: Requires the US2 CLI path and is the first independently demonstrable MVP outcome.
- **US7, US8, US9**: Require US6 and are otherwise independent.
- **US10**: Requires the US2 rule/registry surface.

### Parallel Opportunities

- Setup: T002, T003, T005, T006, T007, and T008 are separate files/directories; T004 follows package metadata.
- Foundation: T010 and T011 are independent modules.
- US3 and US4 can be developed in parallel after Phase 2 if the shared constants contract is fixed.
- US6: T020, T021, T022, and T023 are independent evaluator/style surfaces; T024–T025 integrate them afterward.
- US5: T027 and T028 are independent bundle implementation/configuration surfaces after T026.
- After US6: US7, US8, and US9 can proceed in parallel; US5 and US2 remain on the MVP dependency path.
- Polish: T055, T056, and T058 can proceed in parallel; T057 follows T056, and T059–T060 follow all selected changes.

## Parallel Execution Examples Per User Story

### User Story 1

```text
After the engine contract is fixed, T038 (repair loop) and T039 (integration fixture) can be prepared in parallel; T040 documents the completed contract afterward.
```

### User Story 2

```text
T030 and T031 can be written as separate CLI regression tests in parallel; T032–T036 then implement the shared dispatch and rendering contract.
```

### User Story 3

```text
T012 can be authored against the registry contract while T013 begins the registry module; T016 fixture files are independent of the populated production registry after the schema is fixed.
```

### User Story 4

```text
T017 can be written independently of T018 because it targets the public severity contract; run the tests red before completing the implementation.
```

### User Story 5

```text
After T026, T027 (`tools/creative_lint/bundles.py`) and T028 (`rules/bundles.yml`) can proceed in parallel, then T029 integrates both into the engine.
```

### User Story 6

```text
T020 (Vale styles), T021 (Vale adapter), T022 (symbolic evaluators), and T023 (symbolic fixtures) are independent surfaces; T024 and T025 integrate them in order.
```

### User Story 7

```text
T041 can be authored while T042 implements the telemetry module; T043 wires the lifecycle behavior after both contracts are known.
```

### User Story 8

```text
T045 can be authored while T046 implements waiver parsing; T047 integrates waiver matching only after the waiver data contract is stable.
```

### User Story 9

```text
T049 and T050 can create Vale and symbolic fixture families in parallel; T051 implements one harness over both families afterward.
```

### User Story 10

```text
T052 can be written against the candidate command contract while T053 implements matching and SHADOW candidate creation; T054 documents the measured promotion path afterward.
```

---

## Implementation Strategy

### MVP First (User Story 1)

1. Complete Setup and Foundational phases.
2. Complete US3 and US4 so registry metadata and severity semantics are stable.
3. Complete US6 and US5 so deterministic evaluators run with task-specific gates.
4. Complete US2 so agents have the `wiki-lint` entry point.
5. Complete US1 and stop at its checkpoint.
6. Validate the AGENCY001/CANON002 repair loop independently before adding lifecycle, waiver, learning-loop, and migration work.

### Incremental Delivery

1. Add US9 fixtures with every active rule and enforce BLOCK-rule should-fail/should-pass coverage.
2. Add US7 shadow mode before promoting new rules.
3. Add US8 explicit waivers for contextual exceptions.
4. Add US10 correction classification for measured learning.
5. Integrate `wiki-maintain` and complete Markdownlint migration only after equivalent fixtures pass.
6. Run all quickstart and focused regression checks before adoption.

### Format Validation

Every task line uses `- [ ]`, a sequential `T###` ID, `[P]` only for independently parallel work, `[USn]` on user-story tasks, and an explicit repository file path. Setup, foundational, and polish tasks intentionally omit story labels; every task in a user-story phase carries its phase label.
