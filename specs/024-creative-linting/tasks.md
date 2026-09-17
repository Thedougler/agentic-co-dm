---

description: "Task list for feature implementation"
---

# Tasks: Creative Linting

**Input**: Design documents from `/specs/024-creative-linting/`

**Prerequisites**: `plan.md`, `spec.md`, `research.md`, `data-model.md`, `contracts/`, `quickstart.md`

**Tests**: Included because the specification requires independently testable acceptance scenarios, fixture suites, and behavioral coverage for new public CLI and evaluator behavior.

**Organization**: User-story phases are dependency-ordered within the P1/P2/P3 priority bands. Every story has an independent test criterion; the dependency graph makes cross-story prerequisites explicit.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Establish repository-owned dependencies, lint configuration, rule storage, and fixture surfaces.

- [ ] T001 [P] Add `PyYAML>=6,<7` to `pyproject.toml` while preserving the existing project dependencies and Python requirement.
- [ ] T002 [P] Create root `package.json` with `private: true`, `engines.node: ">=22"`, pinned `markdownlint-cli2` `0.23.2`, and thin scripts delegating directly to `scripts/wiki-lint`, `scripts/wiki-maintain`, `scripts/check-omp-baseline.sh`, and pytest.
- [ ] T003 Generate `package-lock.json` from `package.json` with npm so the `markdownlint-cli2` dependency is reproducible and no Node implementation wrapper is introduced.
- [ ] T004 [P] Create `.vale.ini` with `StylesPath = styles`, `MinAlertLevel = suggestion`, packages `ai-tells`, `proselint`, and `Readability`, plus the documented wiki, raw, staging, archive, fixture, and template scopes from `contracts/vale-style-contract.md`.
- [ ] T005 [P] Create `.markdownlint-cli2.jsonc` with the repository Markdown rules and exclusions for `wiki/_raw`, `wiki/_staging`, `wiki/_archive`, and `wiki/templates`.
- [ ] T006 [P] Create tracked `styles/CoDM/`, `rules/shadow/`, `rules/candidates/`, and `tests/fixtures/creative_lint/` directory surfaces, including fixture subdirectories for registry, symbolic, and integration cases.
- [ ] T007 [P] Create repository-owned `rules/registry.yml`, `rules/bundles.yml`, and `rules/waivers.json` configuration files with valid empty or initial-document shapes consumed by later tasks.

---

## Phase 2: Foundational (Blocking Contracts)

**Purpose**: Stabilize the universal finding contract and shared domain vocabulary before evaluator, bundle, or CLI work.

**Checkpoint**: Findings serialize and validate against `contracts/finding-schema.md`; all later modules use the same constants and field names.

- [ ] T008 [P] Implement the universal `Finding` dataclass and `to_dict()`/`from_dict()` contract in `tools/creative_lint/finding.py`, requiring `rule_id`, `result`, `severity`, `location.file`, `evidence`, `reason`, and `evaluator` while allowing nullable `repair_target` and `waiver`.
- [ ] T009 [P] Define allowed rule categories, scopes, severities, evaluator types, lifecycle states, result values, rule-ID regex `^[A-Z]+\\d{3}$`, and severity ordering in `tools/creative_lint/constants.py`.
- [ ] T010 [P] Add public-contract tests in `tests/test_creative_lint.py` for finding serialization, required fields, valid `pass|fail|abstain` results, valid five-level severities, and rejection of malformed schema values.

---

## Phase 3: User Story 3 - Rule Registry and Stable IDs (Priority: P1)

**Goal**: Make every rule discoverable from one validated YAML registry and keep consumers on stable IDs instead of duplicated prose.

**Independent Test**: Load `rules/registry.yml`, query a rule by ID, verify complete metadata, and verify duplicate, malformed, and invalid definitions fail clearly.

### Tests for User Story 3

- [ ] T011 [US3] Add registry tests in `tests/test_creative_lint.py` for `load`, `get`, `by_category`, `by_evaluator`, `active`, `shadow`, `all_ids`, duplicate IDs, required fields, ID format, enum values, invalid Vale paths, severity ceilings, and unresolved-reference warnings.

### Implementation for User Story 3

- [ ] T012 [US3] Implement `RuleDefinition` and `Registry` in `tools/creative_lint/registry.py` with every API in `contracts/registry-contract.md`, including `tags`, `auto_repair`, `conflicts`, and `depends` fields.
- [ ] T013 [US3] Implement registry validation in `tools/creative_lint/registry.py` for required fields, unique IDs, `^[A-Z]+\\d{3}$`, category/scope/severity/evaluator/lifecycle enums, existing `vale_style` files, valid references as warnings, and the `scene`/`diversity` maximum severity `WARN`.
- [ ] T014 [US3] Populate `rules/registry.yml` with AGENCY001-003, CANON001-002, KNOW001-002, TEMP001, SCENE001-002, WIKI001-002, DIVERSITY001, and RETRIEVAL001, including canonical metadata, lifecycle, repair guidance, tags, conflicts, dependencies, `auto_repair`, and Vale style references.
- [ ] T015 [P] [US3] Add registry fixtures under `tests/fixtures/creative_lint/registry/` for valid metadata, duplicate IDs, invalid IDs, missing required fields, invalid enums, missing Vale styles, unresolved references, and a creative rule above the `WARN` ceiling.

**Checkpoint**: Rule definitions are single-source metadata and are independently queryable and validated.

---

## Phase 4: User Story 4 - Five-Level Severity Model (Priority: P2)

**Goal**: Separate objective repair gates from creative diagnostics using BLOCK, REPAIR, REVIEW, WARN, and INFO.

**Independent Test**: Evaluate findings at all five levels and verify `repair_required`, `review_needed`, and `clean` statuses, including rejection or downgrade of subjective BLOCK rules.

### Tests for User Story 4

- [ ] T016 [US4] Add severity tests in `tests/test_creative_lint.py` for ordering, bundle ceilings, BLOCK/REPAIR status, REVIEW-only status, WARN/INFO clean status, and the prohibition on creative `scene`/`diversity` severities above WARN.

### Implementation for User Story 4

- [ ] T017 [US4] Implement severity ordering, `min_severity()`, category ceilings, and status computation in `tools/creative_lint/severity.py`, preserving independent lifecycle and severity dimensions and returning the contract statuses `repair_required`, `review_needed`, or `clean`.

**Checkpoint**: Severity decisions are deterministic and do not turn taste diagnostics into mandatory repairs.

---

## Phase 5: User Story 6 - Multiple Evaluator Types (Priority: P2)

**Goal**: Dispatch Vale static rules and Python symbolic checks through one engine and one finding schema, with graceful unavailable/abstain states.

**Independent Test**: Run Vale and symbolic rules together; verify identical finding fields, registry-derived severity, no LLM call for deterministic rules, and valid abstention/unavailability behavior.

### Tests for User Story 6

- [ ] T018 [US6] Add evaluator tests in `tests/test_creative_lint.py` for Vale JSON mapping, symbolic findings, `pass|fail|abstain`, evaluator-unavailable handling, location spans, registry metadata, and all required finding-schema fields.

### Implementation for User Story 6

- [ ] T019 [P] [US6] Create Vale rule files `styles/CoDM/AGENCY001.yml`, `AGENCY002.yml`, `AGENCY003.yml`, `KNOW001.yml`, `KNOW002.yml`, `TEMP001.yml`, `SCENE001.yml`, and `SCENE002.yml` using the required extension points, scopes, ID-bearing messages, and registry-to-Vale severity mapping.
- [ ] T020 [P] [US6] Implement `run_vale()` and Vale JSON mapping in `tools/creative_lint/vale_adapter.py`, invoking `vale --output=JSON --config=.vale.ini`, stripping `CoDM.`, mapping line/span/match fields, and warning without crashing when Vale is unavailable.
- [ ] T021 [P] [US6] Implement symbolic evaluators in `tools/creative_lint/evaluators/symbolic.py` for CANON001, CANON002, WIKI001, WIKI002, and RETRIEVAL001 by wrapping `tools/lint_wiki.py` findings without changing that existing engine.
- [ ] T022 [US6] Implement `LintResult` and evaluator dispatch in `tools/creative_lint/engine.py`, merging Vale and symbolic findings, preserving semantic/human `abstain` or unavailable records, applying registry metadata, and computing summary/status values.
- [ ] T023 [US6] Detect opposing active rules in `tools/creative_lint/engine.py` and emit a traceable `LINT-CONFLICT` finding with precedence guidance rather than silently selecting a creative outcome.
- [ ] T024 [P] [US6] Add symbolic fixtures under `tests/fixtures/creative_lint/symbolic/` for dead/stale canon references, valid references, missing frontmatter, invalid lifecycle/type, broken wikilinks, and indeterminate evaluation.

**Checkpoint**: Static and symbolic evaluators produce the universal finding contract through one engine.

---

## Phase 6: User Story 5 - Task-Specific Rule Bundles (Priority: P2)

**Goal**: Scope linting to named task bundles and apply category-specific severity gates without duplicating rule logic.

**Independent Test**: Resolve `session-prep` and `wiki-ingest` against the same registry and verify included categories, excluded categories, and effective severities differ as configured.

### Tests for User Story 5

- [ ] T025 [US5] Add bundle tests in `tests/test_creative_lint.py` for all configured bundles, category exclusion, BLOCK/REVIEW/WARN gates, duplicate category placement rejection, active-only resolution, and unknown bundle errors.

### Implementation for User Story 5

- [ ] T026 [P] [US5] Implement `BundleDefinition` and `BundleRegistry` in `tools/creative_lint/bundles.py`, loading YAML and exposing `get`, `available`, and `resolve(registry)` as `(RuleDefinition, effective_severity)` pairs.
- [ ] T027 [P] [US5] Populate `rules/bundles.yml` with `session-prep`, `wiki-ingest`, `worldbuilding`, `live-codm`, and `corpus`, using the block/review/diagnostics category gates from `research.md` R8.
- [ ] T028 [US5] Integrate bundle resolution into `tools/creative_lint/engine.py` so unlisted categories are excluded, diagnostics cap at WARN, active rules execute, and shadow rules are separately recorded.

**Checkpoint**: Task bundles control rule scope, severity gates, and deterministic cost.

---

## Phase 7: User Story 2 - wiki-lint CLI for Files and Corpus (Priority: P1)

**Goal**: Expose task, file, corpus, changed, and rule operations with structured JSON, human output, filters, and preserved legacy mode.

**Independent Test**: Run every CLI surface against fixtures and a missing-frontmatter page; verify output schema, human rendering, filters, unknown-input errors, and exit codes 0/1/2 while `wiki-lint --json wiki` retains its structural report shape.

### Tests for User Story 2

- [ ] T029 [US2] Add subprocess tests in `tests/test_creative_lint_cli.py` for `task`, `file`, `corpus`, `changed`, `rule`, severity filters, JSON schema, human rendering, unknown bundle/rule errors, and exit codes.
- [ ] T030 [US2] Add a structural regression test in `tests/test_creative_lint_cli.py` proving no-subcommand `scripts/wiki-lint --json wiki` still delegates to `tools/lint_wiki.py` with the existing `counts` and `hard_fail` output.

### Implementation for User Story 2

- [ ] T031 [US2] Refactor `scripts/wiki-lint` dispatch to recognize only creative subcommands while lazily importing `tools.creative_lint`, preserving legacy argument forwarding and startup behavior.
- [ ] T032 [US2] Implement `task` and `file` parsing in `scripts/wiki-lint` with bundle/inherent severity execution, relative/absolute path resolution, `--json`, `--severity`, and contract exit codes.
- [ ] T033 [US2] Implement `corpus` and `changed` parsing in `scripts/wiki-lint`, scanning the configured vault and Markdown paths from `git diff --name-only HEAD` while respecting existing skipped trees.
- [ ] T034 [US2] Implement `rule` output in `scripts/wiki-lint` with ID, title, category, severity, evaluator, lifecycle, scope, message, repair, tags, and bundle memberships, including exit-2 errors.
- [ ] T035 [US2] Implement human rendering and severity filtering in `tools/creative_lint/cli_output.py` and `scripts/wiki-lint`, keeping all findings in the universal schema and preserving WARN/INFO diagnostics.
- [ ] T036 [US2] Implement `wiki-lint --consolidate [vault] [--json] [--approve]` in `scripts/wiki-lint` with deterministic dry-run plans, `requires_approval: true`, safe-action validation, snapshot revalidation, no-write default behavior, and documented exit codes.

**Checkpoint**: Agents and humans can invoke every specified file/corpus CLI surface without structural-mode regression.

---

## Phase 8: User Story 1 - Agent Lints Generated Output (Priority: P1) — MVP

**Goal**: Let agents repair BLOCK/REPAIR findings, surface REVIEW findings, preserve WARN/INFO diagnostics, and re-lint only changed output.

**Independent Test**: Run `wiki-lint task session-prep` on output containing AGENCY001 and CANON002 violations, apply a repair, and verify the changed surface has no blocking findings while diagnostics remain visible.

### Tests for User Story 1

- [ ] T037 [US1] Add end-to-end repair-loop tests in `tests/test_creative_lint.py` for AGENCY001 and CANON002, rule/location repair traceability, REVIEW surfacing, WARN/INFO non-mandate behavior, changed-surface re-linting, and clean convergence.

### Implementation for User Story 1

- [ ] T038 [US1] Implement `repair_loop()` in `tools/creative_lint/engine.py` with configurable maximum `3` iterations, repair callbacks receiving exact findings, changed-surface re-linting, and escalation of unconverged findings for DM review.
- [ ] T039 [P] [US1] Add `tests/fixtures/creative_lint/integration/session_prep_violations.md` containing an authored PC decision and an NPC reference contradicting canonical dead/stale state.
- [ ] T040 [US1] Document the agent repair contract in `docs/creative-linting.md`: BLOCK/REPAIR must be repaired, REVIEW must be surfaced, WARN/INFO must not be mechanically optimized away, and every repair cites rule ID plus location.

**Checkpoint**: The MVP agent loop produces actionable findings and converges or escalates after three repair passes.

---

## Phase 9: User Story 11 - Bulk Wiki Cleanup Queue (Priority: P1)

**Goal**: Emit a stateless smallest-first queue containing only pages with safe automatic findings; leave judgment-only pages out of the unattended loop.

**Independent Test**: Seed two differently sized pages with safe findings, verify ascending byte-size order, repair the head, re-request the queue, and verify judgment-only pages are excluded without requiring the queue to empty.

### Tests for User Story 11

- [ ] T041 [US11] Add queue behavior tests in `tests/test_creative_lint_cli.py` for smallest-first byte sorting, safe-finding counts, queue removal after re-lint, judgment-only exclusion, total-dirty accounting, and successful incomplete queues.

### Implementation for User Story 11

- [ ] T042 [US11] Implement stateless dirty-file queue computation in `tools/creative_lint/engine.py` using only findings with non-null `repair_target` and registry `auto_repair: true`, returning `queue`, `excluded_judgment_only`, and `total_dirty`.
- [ ] T043 [US11] Implement `wiki-lint queue [--json]` in `scripts/wiki-lint` with smallest-first human/JSON output, exit 0 for non-empty queues, and exit 2 only for invalid arguments or registry errors.
- [ ] T044 [US11] Mark template-conformance, literal-newline, unique-link-retarget, and markdownlint structural repairs as safe automatic while excluding missing metadata, canon, agency, and prose judgment findings from `tools/creative_lint/engine.py` queue inclusion.

**Checkpoint**: Bulk cleanup has an objective queue and does not treat unfinished judgment work as failure.

---

## Phase 10: User Story 12 - Template-Derived Conformance (Priority: P1)

**Goal**: Derive a generic profile from the current mapped wiki template and report or safely repair page drift without per-template hardcoded rules.

**Independent Test**: Lint a mapped page missing a required section and formatting construct, change the selected template, re-lint without detector code changes, and verify the new baseline is used while optional omissions remain clean.

### Tests for User Story 12

- [ ] T045 [US12] Add template conformance tests in `tests/test_creative_lint.py` for type/kind mapping, frontmatter shape, heading tree/order, optional omissions, callout forms, tables, formatting markers, locations, template changes, and automatic-repair eligibility.

### Implementation for User Story 12

- [ ] T046 [US12] Implement runtime profile derivation in `tools/creative_lint/template_profile.py` for frontmatter key types, ordered `##`/`###` headings, section order, callouts, table headers, formatting markers, and omit-if-empty/omit-unused optional sections.
- [ ] T047 [US12] Implement generic profile comparison in `tools/creative_lint/evaluators/symbolic.py` with TMPL001 missing section, TMPL002 extra section, TMPL003 order, TMPL004 frontmatter shape, and TMPL005 formatting findings, all using `evaluator: symbolic` and safe repair targets where applicable.
- [ ] T048 [US12] Add `wiki-lint template <path> [--json]` to `scripts/wiki-lint`, resolving templates from `type`/`kind` and returning selected template, page, structured findings, and exit codes for clean, repair, or unresolved-template results.
- [ ] T049 [US12] Connect template comparison repairs to the safe queue in `tools/creative_lint/engine.py`, ensuring all TMPL repairs are automatic, generic, re-lintable, and never invent canon or rewrite prose.
- [ ] T050 [P] [US12] Add mapped-page and template-mutation fixtures under `tests/fixtures/creative_lint/template/` covering missing sections, mismatched constructs, optional omissions, and a changed template baseline.

**Checkpoint**: Template edits change the lint baseline without detector-code or per-template rule changes.

---

## Phase 11: User Story 7 - Rule Lifecycle and Shadow Mode (Priority: P3)

**Goal**: Evaluate SHADOW rules and record telemetry without changing active agent-facing findings or severity.

**Independent Test**: Run a SHADOW rule, verify telemetry exists while active output/status is unchanged, promote it to ACTIVE, and verify it appears with the same severity.

### Tests for User Story 7

- [ ] T051 [US7] Add lifecycle tests in `tests/test_creative_lint.py` for DRAFT skipping, SHADOW telemetry, ACTIVE output, promotion evidence, severity independence, and the creative diagnostic ceiling.

### Implementation for User Story 7

- [ ] T052 [US7] Implement append-only per-rule JSONL telemetry in `tools/creative_lint/shadow.py`, exposing run ID, agreement, false-positive, and repair-helpfulness measurements under `rules/shadow/`.
- [ ] T053 [US7] Wire DRAFT/SHADOW/ACTIVE filtering and shadow recording into `tools/creative_lint/engine.py`, excluding SHADOW findings from active findings/status while exposing them in `LintResult.shadow`.
- [ ] T054 [US7] Add `rules/shadow/` telemetry to `.gitignore` and document measured promotion thresholds and independent severity in `docs/creative-linting.md`.

**Checkpoint**: New rules can be measured safely before activation.

---

## Phase 12: User Story 8 - Explicit Waivers (Priority: P3)

**Goal**: Suppress a specific rule/target only through an owned, reasoned, expiring waiver.

**Independent Test**: Apply a valid waiver before expiry, verify suppression metadata and summary counts, verify the finding returns after expiry, and reject a waiver without expiry.

### Tests for User Story 8

- [ ] T055 [US8] Add waiver tests in `tests/test_creative_lint.py` for required fields, exact rule matching, `file:`, `npc:`, `session:`, and `*` targets, active/expired behavior, suppression metadata, and missing expiry rejection.

### Implementation for User Story 8

- [ ] T056 [US8] Implement `Waiver` and `WaiverRegistry` in `tools/creative_lint/waivers.py`, requiring rule ID, target, reason, owner, granted, and expires and rejecting permanent or anonymous waivers.
- [ ] T057 [US8] Integrate waiver matching into `tools/creative_lint/engine.py`, attaching metadata, excluding matched findings from repair status, and counting waived findings without deleting audit records.
- [ ] T058 [US8] Validate `rules/waivers.json` on load and pass session identity into `LintEngine.run()` from `scripts/wiki-lint` so `expires: session-N` works in CLI runs; document approval and expiry behavior in `docs/creative-linting.md`.

**Checkpoint**: Contextual exceptions are explicit, auditable, temporary, and DM-owned.

---

## Phase 13: User Story 9 - Rule Fixtures and Testing (Priority: P3)

**Goal**: Define acceptable regions for every nontrivial rule with should-fail, should-pass, and ambiguous fixtures.

**Independent Test**: Run the fixture harness and verify fail fixtures trigger, pass fixtures do not, and ambiguous fixtures are recorded without failing the suite.

### Tests and Implementation for User Story 9

- [ ] T059 [P] [US9] Create Vale fixtures under `tests/fixtures/creative_lint/AGENCY001/`, `AGENCY002/`, `AGENCY003/`, `KNOW001/`, `KNOW002/`, `TEMP001/`, `SCENE001/`, and `SCENE002/` using `fail_*.md`, `pass_*.md`, and `ambiguous_*.md` names.
- [ ] T060 [P] [US9] Create symbolic and template fixtures under `tests/fixtures/creative_lint/CANON001/`, `CANON002/`, `WIKI001/`, `WIKI002/`, `RETRIEVAL001/`, `DIVERSITY001/`, and `template/` with valid counterexamples and required state/frontmatter context.
- [ ] T061 [US9] Implement fixture discovery/assertions in `tests/test_creative_lint.py`, requiring should-fail and should-pass coverage for each active BLOCK rule and recording ambiguous outcomes without failing the suite.

**Checkpoint**: Fixtures protect each rule's acceptable region and active BLOCK rules have regression coverage.

---

## Phase 14: User Story 10 - DM Correction Becomes Rule (Priority: P3)

**Goal**: Route recurring DM corrections to an existing rule or a measured SHADOW candidate without duplicates.

**Independent Test**: Classify a knowledge-boundary correction against KNOW002 or emit a SHADOW candidate with promotion requirements; insufficient precision must not promote it.

### Tests for User Story 10

- [ ] T062 [US10] Add correction-routing tests in `tests/test_creative_lint_cli.py` for existing-rule matches, no-match candidate creation, SHADOW defaults, duplicate avoidance, fixture requirements, telemetry accumulation, and insufficient-precision non-promotion.

### Implementation for User Story 10

- [ ] T063 [US10] Implement correction matching in `scripts/wiki-lint` using registry titles, messages, and tags, returning matching stable IDs without creating duplicate rule definitions.
- [ ] T064 [US10] Implement unmatched-correction candidate output in `scripts/wiki-lint` under `rules/candidates/` with lifecycle `SHADOW`, required rule metadata, and a machine-readable promotion requirement.
- [ ] T065 [US10] Connect candidate promotion reporting to `tools/creative_lint/shadow.py` and document the thresholds of greater than 90% human agreement and less than 10% false positives in `docs/creative-linting.md`.

**Checkpoint**: A correction becomes an inspectable rule-improvement path rather than duplicated prompt prose.

---

## Phase 15: Polish & Cross-Cutting Concerns

**Purpose**: Integrate maintenance, complete off-the-shelf lint migration, document operations, and validate the complete feature.

- [ ] T066 [P] Add the `corpus` creative report as optional Layer A7 output in `scripts/wiki-maintain`, reusing `tools/creative_lint/engine.py` and preserving compact existing A1-A6 output.
- [ ] T067 [P] Port checks from `scripts/lint-obsidian-markdown` and `scripts/lint-literal-newlines` into `.markdownlint-cli2.jsonc`, Vale, or safe symbolic evaluators with passing fixtures, retaining legacy scripts until parity is proven.
- [ ] T068 Update callers in `scripts/lint-wiki-write` and `.agents/skills/session-recap/SKILL.md` to use the replacement lint surfaces after equivalent fixture coverage passes, then deprecate or remove only the superseded legacy scripts.
- [ ] T069 [P] Complete `docs/creative-linting.md` with architecture boundaries, rule authoring, bundles, CLI examples, finding schema, lifecycle, waivers, fixtures, queue workflow, template conformance, and maintenance integration.
- [ ] T070 Run validation scenarios V1-V11 from `specs/024-creative-linting/quickstart.md`, correcting only commands or expectations that conflict with the accepted contracts.
- [ ] T071 Run `.venv/bin/python -m pytest tests/test_creative_lint.py tests/test_creative_lint_cli.py -v` plus the existing structural regression command from `specs/024-creative-linting/quickstart.md`; resolve failures without changing accepted behavior.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies; T003 follows T002, and T007 follows the directory/config surfaces.
- **Foundational (Phase 2)**: Depends on Setup and blocks user-story work.
- **US3 (P1)**: Depends on the foundational finding/constants contract; establishes registry metadata.
- **US4 (P2)**: Depends on foundational constants and registry validation; establishes severity semantics.
- **US6 (P2)**: Depends on US3 and US4; provides Vale, symbolic, and engine execution.
- **US5 (P2)**: Depends on US6's engine contract; adds bundle scoping and gates.
- **US2 (P1)**: Depends on US5 and US6; exposes the CLI used by agent and queue stories.
- **US1 (P1 MVP)**: Depends on US2's task path and the complete evaluator engine.
- **US11 (P1)**: Depends on US1/US6 finding metadata and safe-repair semantics; can be delivered independently of lifecycle and waiver work.
- **US12 (P1)**: Depends on US6 symbolic dispatch and US11 safe queue; can be delivered independently of lifecycle and waiver work.
- **US7 and US8 (P3)**: Depend on US6 and are independent of each other and of US9.
- **US9 (P3)**: Depends on evaluator contracts and rule files; strengthens all prior stories without changing their public APIs.
- **US10 (P3)**: Depends on US2 registry/CLI surfaces and US7 telemetry.
- **Polish (Phase 15)**: Depends on all selected stories and passing replacement fixtures.

### User Story Dependencies

- **US3**: Phase 2 only.
- **US4**: Phase 2 and registry validation.
- **US6**: US3 and US4.
- **US5**: US6.
- **US2**: US5 and US6.
- **US1**: US2, US5, and US6.
- **US11**: US1/US6 safe-finding contract; does not require P3 stories.
- **US12**: US6 symbolic contract and US11 queue; does not require P3 stories.
- **US7, US8, US9**: US6; these three can proceed in parallel.
- **US10**: US2 and US7 telemetry.

### Parallel Opportunities

- **Setup**: T001, T002, T004, T005, and T006 are independent; T003 follows T002 and T007 follows the configuration surfaces.
- **Foundation**: T008, T009, and T010 touch separate contracts/modules and can proceed in parallel after the shared schema decision.
- **US3**: T011 and T015 can be prepared in parallel once the registry contract is fixed; T012-T014 integrate the registry.
- **US6**: T019, T020, T021, and T024 are independent style/adapter/evaluator/fixture surfaces; T022-T023 integrate them.
- **US5**: T025 can be authored while T026 and T027 implement the module/config; T028 integrates both.
- **US2**: T029 and T030 are independent CLI regression tests; T031-T036 implement the shared dispatch and outputs.
- **US1**: T037 and T039 can proceed in parallel; T038 integrates the repair loop and T040 documents it afterward.
- **US11**: T041 can be written while T042 implements queue computation; T043-T044 expose and constrain it afterward.
- **US12**: T045 and T050 can proceed in parallel; T046-T047 derive/compare profiles before T048-T049 integrate CLI and queue repairs.
- **US7, US8, US9**: These story phases can run in parallel after US6; within them tests and independent storage/config files can proceed separately.
- **Polish**: T066, T067, and T069 are independent; T068 follows T067, and T070-T071 follow selected implementation changes.

## Parallel Execution Examples Per User Story

### User Story 1

```text
Prepare T037 end-to-end tests and T039 integration fixtures in parallel; complete T038 repair-loop integration, then T040 documentation.
```

### User Story 2

```text
Write T029 and T030 subprocess regressions in parallel; implement T031 dispatch before T032-T036 handlers and rendering.
```

### User Story 3

```text
Author T011 registry tests and T015 metadata fixtures in parallel; implement T012-T014 against the fixed contract.
```

### User Story 4

```text
Write T016 against the public severity contract while T017 implements the isolated severity module; run the tests red before integration.
```

### User Story 5

```text
After T025, implement T026 and author T027 in parallel; finish T028 only after both the module and YAML gates exist.
```

### User Story 6

```text
Implement T019 Vale styles, T020 adapter, T021 symbolic evaluator, and T024 fixtures in parallel; integrate them with T022-T023.
```

### User Story 7

```text
Author T051 while T052 implements telemetry; wire T053 after both the lifecycle tests and telemetry format are stable.
```

### User Story 8

```text
Author T055 while T056 implements waiver parsing; integrate T057-T058 after target matching and expiry semantics are fixed.
```

### User Story 9

```text
Create T059 Vale fixtures and T060 symbolic/template fixtures in parallel; implement the shared fixture harness in T061 afterward.
```

### User Story 10

```text
Write T062 against the candidate command contract while T063-T064 implement matching and SHADOW candidate output; add T065 promotion reporting last.
```

### User Story 11

```text
Author T041 queue acceptance tests while T042 computes the stateless queue; expose it through T043 and safe-repair filtering through T044.
```

### User Story 12

```text
Prepare T045 conformance tests and T050 mutation fixtures in parallel; implement T046-T047 profile/compare logic before T048-T049 integration.
```

## Implementation Strategy

### MVP First (User Story 1)

1. Complete Setup and Foundational phases.
2. Complete US3 and US4 so registry metadata and severity semantics are stable.
3. Complete US6 and US5 so deterministic evaluators run with task-specific gates.
4. Complete US2 so agents have the `wiki-lint` task surface.
5. Complete US1 and stop at its checkpoint.
6. Validate the AGENCY001/CANON002 repair loop independently before adding queue, lifecycle, waiver, learning, or migration work.

### Incremental Delivery

1. Add US11 and US12 for safe bulk cleanup and live-template conformance.
2. Add US9 fixture coverage for every active rule.
3. Add US7 shadow mode before promoting new rules.
4. Add US8 explicit waivers for contextual exceptions.
5. Add US10 correction classification for measured learning.
6. Integrate `wiki-maintain` and complete legacy Markdown-lint migration only after equivalent fixtures pass.
7. Run all quickstart and focused regression checks before adoption.

### Format Validation

Every task line uses `- [ ]`, a sequential `T###` ID, `[P]` only for independently parallel work, `[USn]` on every user-story task, and an explicit repository file path. Setup, foundational, and polish tasks intentionally omit story labels. No sample or placeholder task lines remain.
