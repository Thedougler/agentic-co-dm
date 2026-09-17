---

description: "Task list for Creative Linting"
---

# Tasks: Creative Linting

**Input**: Design documents from `/specs/024-creative-linting/`

**Prerequisites**: `plan.md`, `spec.md`, `research.md`, `data-model.md`, `contracts/`, `quickstart.md`

**Organization**: Tasks are grouped by user story. Dependency order is used where a lower-priority story provides infrastructure required by an earlier-priority story.

**Tests**: Included because the specification defines independent behavioral tests, fixture suites, and a pytest convention.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Create the repository-owned configuration and package surface required by the linter.

- [X] T001 Create the `tools/creative_lint/` package and `tools/creative_lint/evaluators/` subpackage with `__init__.py` files.
- [X] T002 [P] Create `rules/registry.yml`, `rules/bundles.yml`, and `rules/waivers.json` with valid empty bootstrap content.
- [X] T003 [P] Create the `styles/CoDM/` Vale style directory and `rules/shadow/` telemetry directory.
- [X] T004 [P] Create `.vale.ini` with `StylesPath = styles`, `MinAlertLevel = suggestion`, the `[wiki/*.md]` CoDM scope, and exclusions for `wiki/_raw/`, `wiki/_staging/`, `wiki/_archive/`, and `wiki/templates/`.
- [X] T005 [P] Create `.markdownlint-cli2.jsonc` with the structural Markdown rules required to port `scripts/lint-obsidian-markdown` and `scripts/lint-literal-newlines`.
- [X] T006 [P] Create fixture directories under `tests/fixtures/creative_lint/` for Vale, symbolic, integration, and ambiguous cases.
- [X] T007 Verify and document PyYAML, Vale 3.13.0, and markdownlint-cli2 prerequisites in `specs/024-creative-linting/quickstart.md` without changing existing repository dependency policy.

---

## Phase 2: Foundational (Shared Contracts)

**Purpose**: Implement the shared data and validation primitives that every user story consumes.

**Checkpoint**: Finding construction and shared validation APIs exist before evaluator, bundle, or CLI work begins.

- [X] T008 [P] Implement the `Finding` dataclass and `to_dict()` serialization in `tools/creative_lint/finding.py` according to `specs/024-creative-linting/contracts/finding-schema.md`, including required `rule_id`, `result`, `severity`, `location.file`, `evidence`, `reason`, and `evaluator` fields.
- [X] T009 [P] Add shared enum and path-validation constants in `tools/creative_lint/constants.py` for rule IDs, categories, scopes, severities, evaluators, lifecycles, and `pass|fail|abstain` results.

---

## Phase 3: User Story 3 - Rule Registry and Stable IDs (Priority: P1)

**Goal**: Make every rule discoverable from one validated repository-owned registry and keep consumers on stable IDs.

**Independent Test**: Load `rules/registry.yml`, query a rule by ID, verify full metadata, reject duplicate IDs and invalid IDs, and verify a bundle expands IDs rather than embedded rule prose.

### Tests for User Story 3

- [X] T010 [P] [US3] Add registry behavior tests in `tests/test_creative_lint.py` for YAML loading, `get()`, category/evaluator queries, active/shadow filtering, duplicate IDs, malformed IDs, invalid enums, missing required fields, invalid Vale paths, and unresolved references.

### Implementation for User Story 3

- [X] T011 [US3] Implement `RuleDefinition` and `Registry` in `tools/creative_lint/registry.py` with the fields and APIs specified in `specs/024-creative-linting/contracts/registry-contract.md`.
- [X] T012 [US3] Add registry validation in `tools/creative_lint/registry.py` for `^[A-Z]+\d{3}$` IDs, unique IDs, required fields, allowed enums, Vale file existence, valid references, and the `scene`/`diversity` severity ceiling of `WARN`.
- [X] T013 [US3] Populate `rules/registry.yml` with the initial rule metadata from `specs/024-creative-linting/research.md` R7, including stable IDs, categories, scopes, severities, evaluator types, lifecycle states, messages, repairs, tags, conflicts, dependencies, and Vale style references.
- [X] T014 [US3] Add registry metadata fixtures in `tests/fixtures/creative_lint/registry/` covering a valid rule, duplicate ID, invalid ID, missing Vale file, and scene rule above the `WARN` ceiling.

**Checkpoint**: Rule definitions are the single source of metadata truth and are independently queryable and validated.

---

## Phase 4: User Story 4 - Five-Level Severity Model (Priority: P2)

**Goal**: Compute action status and bundle severity ceilings without turning taste diagnostics into blocking requirements.

**Independent Test**: Evaluate findings containing each severity level and verify `repair_required`, `review_needed`, and `clean` status semantics; reject subjective BLOCK rules in `scene` and `diversity` categories.

### Tests for User Story 4

- [X] T015 [P] [US4] Add severity behavior tests in `tests/test_creative_lint.py` for ordering, `min_severity()`, status computation, WARN/INFO non-blocking behavior, BLOCK/REPAIR repair requirements, REVIEW-only status, and category taste ceilings.

### Implementation for User Story 4

- [X] T016 [US4] Implement `SEVERITY_ORDER`, `min_severity()`, `status_from_findings()`, and category taste ceilings in `tools/creative_lint/severity.py` with the five-level semantics from `specs/024-creative-linting/spec.md` FR-005, FR-006, and FR-016.
- [X] T017 [US4] Implement severity validation errors in `tools/creative_lint/registry.py` or `tools/creative_lint/severity.py` so subjective `scene` and `diversity` rules cannot validate above `WARN`.

**Checkpoint**: Severity decisions are deterministic, observable, and independent of evaluator implementation.

---

## Phase 5: User Story 6 - Multiple Evaluator Types (Priority: P2)

**Goal**: Dispatch static Vale and symbolic checks through one engine and one finding schema, with abstention and unavailable-evaluator states preserved.

**Independent Test**: Run AGENCY001 through Vale and WIKI001/CANON rules through symbolic evaluation; verify identical finding shape, no LLM call for static rules, and `abstain` when semantic certainty is unavailable.

### Tests for User Story 6

- [X] T018 [P] [US6] Add finding-schema and evaluator-dispatch tests in `tests/test_creative_lint.py` covering Vale mapping, symbolic mapping, `pass|fail|abstain`, unavailable evaluator recording, and JSON-schema-required fields.

### Implementation for User Story 6

- [X] T019 [P] [US6] Create Vale rule files `styles/CoDM/AGENCY001.yml`, `AGENCY002.yml`, `AGENCY003.yml`, `KNOW001.yml`, `KNOW002.yml`, `TEMP001.yml`, `SCENE001.yml`, and `SCENE002.yml` using the extension points, scopes, levels, and traceable messages required by `specs/024-creative-linting/contracts/vale-style-contract.md`.
- [X] T020 [P] [US6] Implement Vale subprocess invocation and JSON mapping in `tools/creative_lint/vale_adapter.py`, including `Check` prefix stripping, location spans, registry metadata lookup, relative file paths, graceful Vale absence, and stderr warnings.
- [X] T021 [P] [US6] Implement symbolic evaluation in `tools/creative_lint/evaluators/symbolic.py` for CANON001, CANON002, WIKI001, WIKI002, and RETRIEVAL001, wrapping existing `tools/lint_wiki.py` findings without modifying that engine.
- [X] T022 [US6] Implement `LintResult` and evaluator orchestration in `tools/creative_lint/engine.py`, merging Vale and symbolic findings, applying registry metadata, preserving evaluator-unavailable results, and computing summary counts and status.
- [X] T023 [US6] Implement conflict detection in `tools/creative_lint/engine.py` for conflicting rules active in one run, emitting `LINT-CONFLICT` with precedence guidance without silently choosing a creative outcome.
- [X] T024 [US6] Add symbolic evaluator fixtures in `tests/fixtures/creative_lint/symbolic/` for stale/dead canon references, valid references, missing frontmatter, invalid lifecycle/type, broken wikilinks, and indeterminate evaluation.

**Checkpoint**: The engine runs static and symbolic evaluators through the universal finding contract.

---

## Phase 6: User Story 5 - Task-Specific Rule Bundles (Priority: P2)

**Goal**: Scope evaluation to named task bundles and apply category-specific severity gates.

**Independent Test**: Resolve `session-prep` and `wiki-ingest` against the same registry and verify included categories, excluded categories, and effective severities differ as configured.

### Tests for User Story 5

- [X] T025 [P] [US5] Add bundle-resolution tests in `tests/test_creative_lint.py` for all initial bundles, category exclusion, BLOCK/REVIEW/WARN gate capping, duplicate category placement, and unknown bundle errors.

### Implementation for User Story 5

- [X] T026 [US5] Implement `BundleDefinition` and `BundleRegistry` in `tools/creative_lint/bundles.py` with YAML loading, `get()`, available-name reporting, and `resolve(registry)` returning `(RuleDefinition, effective_severity)` pairs.
- [X] T027 [US5] Populate `rules/bundles.yml` with `session-prep`, `wiki-ingest`, `worldbuilding`, `live-codm`, and `corpus` definitions from `specs/024-creative-linting/research.md` R8, including descriptions and severity gates.
- [X] T028 [US5] Integrate bundle resolution into `tools/creative_lint/engine.py` so only configured categories execute, diagnostics cap at WARN, and SHADOW rules are returned separately from active findings.

**Checkpoint**: Task bundles control rule scope and action severity without duplicating rule logic.

---

## Phase 7: User Story 2 - wiki-lint CLI for Files and Corpus (Priority: P1)

**Goal**: Expose file, task, corpus, changed, and rule operations while preserving existing no-subcommand behavior.

**Independent Test**: Run `wiki-lint file` against missing frontmatter, `wiki-lint task` against a fixture, `wiki-lint corpus`, `wiki-lint changed`, and `wiki-lint rule`; verify JSON, human output, filters, and exit codes.

### Tests for User Story 2

- [X] T029 [P] [US2] Add CLI subprocess tests in `tests/test_creative_lint_cli.py` for `task`, `file`, `corpus`, `changed`, and `rule`, including JSON schema, human-readable output, severity filtering, unknown bundle/rule errors, and exit codes 0/1/2.
- [X] T030 [P] [US2] Add a no-subcommand regression fixture and test in `tests/test_creative_lint_cli.py` proving `scripts/wiki-lint --json wiki` retains the existing structural report shape and behavior.

### Implementation for User Story 2

- [X] T031 [US2] Refactor `scripts/wiki-lint` to dispatch only when the first positional argument is `task`, `file`, `corpus`, `changed`, or `rule`, importing `tools.creative_lint` lazily so existing startup behavior remains unchanged.
- [X] T032 [US2] Implement `task` and `file` handlers in `scripts/wiki-lint` with bundle/inherent severity execution, path resolution, `--json`, `--severity`, and contract exit codes.
- [X] T033 [P] [US2] Implement `corpus` and `changed` handlers in `scripts/wiki-lint`, respecting `tools/lint_wiki.py` skip directories and using `git diff --name-only HEAD` for changed Markdown files.
- [X] T034 [US2] Implement `rule` output in `scripts/wiki-lint` with registry metadata and bundle memberships, plus clear exit-2 messages for unknown IDs and invalid registry YAML.
- [X] T035 [US2] Implement human-readable rendering and severity filtering in `tools/creative_lint/cli_output.py`, matching `specs/024-creative-linting/contracts/cli-contract.md` while keeping JSON machine-readable.

**Checkpoint**: CLI consumers can invoke every specified lint surface without regressing existing structural mode.

---

## Phase 8: User Story 1 - Agent Lints Generated Output (Priority: P1) — MVP

**Goal**: Let agents lint generated Work, repair BLOCK/REPAIR findings, surface REVIEW findings, preserve WARN/INFO diagnostics, and re-lint changed output.

**Independent Test**: Run `wiki-lint task session-prep` against output containing AGENCY001 and CANON002 violations, repair them, and verify the changed surface has no blocking findings.

### Tests for User Story 1

- [X] T036 [P] [US1] Add end-to-end agent-loop tests in `tests/test_creative_lint.py` for AGENCY001 and CANON002 findings, repair traceability by rule ID/location, WARN/INFO non-mandate behavior, REVIEW surfacing, and clean re-lint after repair.

### Implementation for User Story 1

- [X] T037 [US1] Implement `repair_loop()` in `tools/creative_lint/engine.py` with configurable maximum three iterations, repair callbacks receiving exact findings, changed-surface re-linting, and final escalation of unconverged findings to DM review.
- [X] T038 [US1] Add the session-prep violation fixture `tests/fixtures/creative_lint/integration/session_prep_violations.md` containing an authored PC decision and a stale/dead canonical entity reference.
- [X] T039 [US1] Document the agent invocation and repair contract in `docs/creative-linting.md`, stating that BLOCK/REPAIR must be repaired, REVIEW must be surfaced, and WARN/INFO must not be mechanically optimized away.

**Checkpoint**: The MVP agent loop produces actionable structured findings and converges or escalates after three repair passes.

---

## Phase 9: User Story 9 - Rule Fixtures and Testing (Priority: P3)

**Goal**: Define should-fail, should-pass, and ambiguous acceptable-region fixtures for every nontrivial rule.

**Independent Test**: Run the fixture harness and verify fail fixtures trigger, pass fixtures do not, and ambiguous fixtures are recorded without failing the suite.

### Tests and Implementation for User Story 9

- [X] T040 [P] [US9] Create Vale fixtures under `tests/fixtures/creative_lint/<RULE_ID>/` for AGENCY001, AGENCY002, AGENCY003, KNOW001, KNOW002, TEMP001, SCENE001, and SCENE002, with `fail_*.md`, `pass_*.md`, and `ambiguous_*.md` cases.
- [X] T041 [P] [US9] Create symbolic fixtures under `tests/fixtures/creative_lint/<RULE_ID>/` for CANON001, CANON002, WIKI001, WIKI002, and RETRIEVAL001, including valid counterexamples.
- [X] T042 [US9] Implement fixture discovery and assertions in `tests/test_creative_lint.py`, requiring both fail/pass coverage for every active BLOCK rule and recording ambiguous results without failing the suite.

**Checkpoint**: Fixture coverage protects the acceptable region and satisfies the active BLOCK-rule regression requirement.

---

## Phase 10: User Story 7 - Rule Lifecycle and Shadow Mode (Priority: P3)

**Goal**: Evaluate SHADOW rules and record telemetry without changing active agent-facing behavior.

**Independent Test**: Run a SHADOW rule, verify telemetry exists while active findings and status remain unchanged, then promote it to ACTIVE and verify it appears.

### Tests for User Story 7

- [X] T043 [P] [US7] Add lifecycle and shadow tests in `tests/test_creative_lint.py` for DRAFT skipping, SHADOW telemetry, ACTIVE output, promotion thresholds, and creative diagnostic severity ceilings.

### Implementation for User Story 7

- [X] T044 [US7] Implement append-only shadow telemetry in `tools/creative_lint/shadow.py`, writing per-rule JSONL under `rules/shadow/` and loading records for agreement, false-positive, and repair-helpfulness measurement.
- [X] T045 [US7] Wire lifecycle filtering and shadow recording into `tools/creative_lint/engine.py`, excluding SHADOW findings from agent output/status while exposing them in `LintResult.shadow`.
- [X] T046 [US7] Add `rules/shadow/` to `.gitignore` and document DRAFT → SHADOW → ACTIVE promotion evidence in `docs/creative-linting.md`.

**Checkpoint**: New rules can be measured safely before activation.

---

## Phase 11: User Story 8 - Explicit Waivers (Priority: P3)

**Goal**: Suppress a specific rule/target only with an owned, reasoned, expiring waiver.

**Independent Test**: Apply a valid waiver before expiry, verify suppression metadata, then verify the finding returns after expiry; reject a waiver without expiry.

### Tests for User Story 8

- [X] T047 [P] [US8] Add waiver behavior tests in `tests/test_creative_lint.py` for required fields, target matching, active/expired waivers, suppression metadata, summary counts, and rejection of missing expiry.

### Implementation for User Story 8

- [X] T048 [US8] Implement `Waiver` and `WaiverRegistry` in `tools/creative_lint/waivers.py` with exact rule matching, `file:`, `npc:`, `session:`, and `*` targets, required owner/reason/granted/expires fields, and expiry checks.
- [X] T049 [US8] Integrate waiver matching into `tools/creative_lint/engine.py`, attaching waiver metadata, excluding matched findings from status, and counting waived findings without deleting audit records.
- [X] T050 [US8] Validate the initial empty `rules/waivers.json` and document the DM approval and expiry workflow in `docs/creative-linting.md`.

**Checkpoint**: Contextual exceptions are explicit, auditable, and temporary.

---

## Phase 12: User Story 10 - DM Correction Becomes Rule (Priority: P3)

**Goal**: Route recurring DM corrections to an existing rule or a measured SHADOW candidate without creating duplicates.

**Independent Test**: Classify the knowledge-boundary correction against KNOW002 or produce a SHADOW candidate template with telemetry and promotion criteria.

### Tests for User Story 10

- [X] T051 [P] [US10] Add correction-classification tests in `tests/test_creative_lint_cli.py` for existing-rule matches, no-match candidate output, SHADOW lifecycle defaults, and insufficient-precision non-promotion.

### Implementation for User Story 10

- [X] T052 [US10] Implement the `candidate` command in `scripts/wiki-lint` to search registry messages/tags for correction matches and emit a repository-owned SHADOW candidate template when no match exists.
- [X] T053 [US10] Document correction routing, fixture requirements, telemetry thresholds of greater than 90% human agreement and less than 10% false positives, and promotion review in `docs/creative-linting.md`.

**Checkpoint**: A DM correction becomes an inspectable rule improvement path rather than duplicated prompt prose.

---

## Phase 13: Cross-Cutting Validation and Integration

**Purpose**: Complete the shared maintenance integration, off-the-shelf Markdown migration, documentation, and end-to-end verification. This is English-project documentation and tooling work; no Polish-language translation is required.

- [X] T054 [P] Integrate the corpus bundle into `scripts/wiki-maintain` as an optional Layer A report step using the same `tools/creative_lint/engine.py` implementation and compact JSON output.
- [X] T055 [P] Port the checks from `scripts/lint-obsidian-markdown` and `scripts/lint-literal-newlines` into `.markdownlint-cli2.jsonc` and corresponding fixtures under `tests/fixtures/creative_lint/`, retaining the old scripts until passing coverage is demonstrated.
- [X] T056 Remove or deprecate `scripts/lint-obsidian-markdown` and `scripts/lint-literal-newlines` only after their checks have passing markdownlint-cli2 fixtures and update all callers to the replacement surface.
- [X] T057 [P] Complete `docs/creative-linting.md` with architecture, rule authoring, bundle configuration, CLI examples, finding schema, lifecycle, waivers, fixtures, and maintenance integration.
- [X] T058 Run all quickstart scenarios V1–V8 from `specs/024-creative-linting/quickstart.md` and record any required command corrections in that file.
- [X] T059 Run the focused suite `tests/test_creative_lint.py` and `tests/test_creative_lint_cli.py`, then run the existing wiki lint regression command from `specs/024-creative-linting/quickstart.md`.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies.
- **Foundational (Phase 2)**: Depends on Setup and blocks all story phases.
- **US3 (Phase 3)**: Depends on the shared Finding/constants primitives.
- **US4 (Phase 4)**: Depends on shared constants and is consumed by the engine.
- **US6 (Phase 5)**: Depends on US3 and US4; provides evaluators and the engine.
- **US5 (Phase 6)**: Depends on US3, US4, and US6's engine contract.
- **US2 (Phase 7)**: Depends on US5 and US6; provides the command surface.
- **US1 (Phase 8)**: Depends on US2 and validates the complete core loop.
- **US9 (Phase 9)**: Depends on US6; can run in parallel with US2, US1, US7, and US8 after the engine exists.
- **US7 (Phase 10)**: Depends on US6; can run in parallel with US2 and US9.
- **US8 (Phase 11)**: Depends on US6; can run in parallel with US2 and US9.
- **US10 (Phase 12)**: Depends on US2's registry CLI surface.
- **Cross-Cutting Validation (Phase 13)**: Depends on the stories selected for delivery and all replacement checks being covered.

### User Story Dependencies

- **US3**: No story dependency after the shared primitives.
- **US4**: No story dependency after the shared primitives.
- **US6**: Requires US3 registry metadata and US4 severity semantics.
- **US5**: Requires US6 engine integration.
- **US2**: Requires US5 bundle resolution and US6 engine integration.
- **US1**: Requires the complete US2 CLI path.
- **US9, US7, US8**: Require US6 and are otherwise independent.
- **US10**: Requires the US2 rule command and registry.

### Parallel Opportunities

- Setup tasks T002–T006 can run in parallel.
- T008 and T009 can run in parallel.
- After Phase 2, registry tests/implementation and severity tests/implementation can run in parallel.
- In US6, T019, T020, T021, and T024 can run in parallel; T022–T023 follow their contracts.
- After US6, US5's bundle work can proceed while US9, US7, and US8 work on separate files.
- In US2, T033 can run in parallel with T032 once the dispatch contract is fixed.
- In cross-cutting validation, T054, T055, and T057 can run in parallel; T056 follows T055.

### Parallel Example: Evaluator Wave

```text
Task T019: Create Vale rule YAML files in styles/CoDM/
Task T020: Implement Vale adapter in tools/creative_lint/vale_adapter.py
Task T021: Implement symbolic evaluators in tools/creative_lint/evaluators/symbolic.py
Task T024: Add symbolic evaluator fixtures in tests/fixtures/creative_lint/symbolic/
Then Task T022: Integrate both evaluator types in tools/creative_lint/engine.py
```

### Parallel Example: Post-Engine Wave

```text
Task T026: Implement bundle resolution in tools/creative_lint/bundles.py
Task T040: Create Vale fixtures under tests/fixtures/creative_lint/<RULE_ID>/
Task T044: Implement shadow telemetry in tools/creative_lint/shadow.py
Task T048: Implement waivers in tools/creative_lint/waivers.py
```

---

## Implementation Strategy

### MVP First (US1)

1. Complete Setup and Foundational phases.
2. Complete US3 and US4 so metadata and status semantics are stable.
3. Complete US6 and US5 so the engine can evaluate scoped rules.
4. Complete US2 so agents have the CLI entry point.
5. Complete US1 and stop at its checkpoint.
6. Validate the AGENCY001/CANON002 repair loop independently before adding lifecycle, waiver, and learning-loop features.

### Incremental Delivery

1. Add US9 fixtures alongside each active rule to preserve the acceptable region.
2. Add US7 shadow mode before promoting new rules.
3. Add US8 explicit waivers for contextual exceptions.
4. Add US10 correction classification for measured learning.
5. Complete maintenance integration and markdownlint migration only after replacement fixtures pass.

### Format Validation

Every task line uses `- [ ]`, a sequential `T###` ID, `[P]` only for independent parallel work, `[USn]` on user-story tasks, and an explicit repository file path.
