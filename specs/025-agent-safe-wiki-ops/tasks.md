---

description: "Task list for Agent-Safe Wiki Operations"
---

# Tasks: Agent-Safe Wiki Operations

**Input**: Design documents from `/specs/025-agent-safe-wiki-ops/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, quickstart.md, contracts/

**Tests**: Behavioral and causal regression tests are included because the specification requires SC-007 coverage for open errors and the constitution requires public-seam tests for new behavior.

**Organization**: Tasks are grouped by user story. Story phases remain independently testable after their stated prerequisites; shared package and CLI foundations are completed first.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Establish the package, fixture, and contract locations used by later story increments.

- [ ] T001 [P] Create the `tools/wiki_ops/` package with `__init__.py`, `identity.py`, `mutations.py`, `transactions.py`, `index_ops.py`, and `manifest_ops.py` paths per `specs/025-agent-safe-wiki-ops/plan.md`
- [ ] T002 [P] Create isolated wiki-operation fixtures at `tests/fixtures/wiki_ops/fisks-fleet.md`, `tests/fixtures/wiki_ops/fisks-captains.md`, `tests/fixtures/wiki_ops/index.md`, and `tests/fixtures/wiki_ops/.manifest.json`
- [ ] T003 [P] Add the policy ownership registry skeleton at `docs/agents/policy-owners.yml` with one entry per governed policy and its authoritative owner

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Provide shared scope resolution, CLI conventions, and test harness support before story implementations.

**Critical**: No user-story implementation begins until this phase is complete.

- [ ] T004 [P] Implement the typed scope parser and resolver for `files`, `directory`, `entity_type`, `identity_set`, `changed`, and `bundle` in `tools/wiki_ops/scope.py`
- [ ] T005 Extend shared argument parsing, vault validation, JSON emission, and exit-status handling in `scripts/wiki-bulk-ops`, `scripts/wiki-lint`, and `scripts/manifest.py` to preserve existing commands while exposing actionable errors
- [ ] T006 Add the subprocess CLI harness, temporary-vault builder, and common assertions in `tests/test_wiki_ops.py` using the existing `tests/test_wiki_bulk_ops.py` fixture conventions
- [ ] T007 Add the repository-level wiki-operation command help and error contract checks in `tests/test_wiki_ops.py` for `--help`, JSON mode, and exit codes 0/1/2

**Checkpoint**: Shared package paths, scope semantics, CLI conventions, and fixtures are ready.

---

## Phase 3: User Story 1 - Scoped Faction Lint and Consolidation (Priority: P1)

**Goal**: Complete the agent workflow from identity preflight through scoped lint, typed repair plan, atomic application, and one final maintenance pass.

**Independent Test**: Run the faction fixture through identity scan, scoped lint, deterministic plan preview, and approved transaction; verify only scoped files are reported, ambiguous identity blocks unsafe work, typed mutations apply, and finalization is summarized once.

### Tests for User Story 1

- [ ] T008 [US1] Add the end-to-end scoped faction lint/consolidation regression in `tests/test_wiki_ops.py`, covering compact file-grouped findings, deterministic actions, dry-run preview, approval gating, and ambiguity blocking

### Implementation for User Story 1

- [ ] T009 [US1] Extend `scripts/wiki-lint` with `--scope`, `--template`, `--plan`, `--from`, `--vault`, and `--json`, filtering files before checks and emitting scope, counts, and findings grouped by file
- [ ] T010 [US1] Add deterministic repair-class classification and `RepairPlan` serialization with action provenance and SHA-256 plan hash in `tools/wiki_ops/mutations.py`
- [ ] T011 [US1] Extend `scripts/wiki-bulk-ops` with `mutate` and `transact` dispatch that accepts `RepairPlan` JSON and never asks agents to compose line-number or regex patches
- [ ] T012 [US1] Wire the identity preflight, scoped lint, plan generation, preview, approval, and finalization sequence through `scripts/wiki-lint` and `scripts/wiki-bulk-ops`

**Checkpoint**: A known faction can be linted and safely consolidated using only repository CLI surfaces.

---

## Phase 4: User Story 2 - Template Conformance Without False Mandates (Priority: P1)

**Goal**: Enforce explicit section, lifecycle, callout, and frontmatter semantics without flagging optional or lifecycle-omitted structure.

**Independent Test**: Lint faction fixtures with omitted optional headings, dormant lifecycle, and disallowed callouts; only genuinely missing required sections and invalid callouts are reported.

### Tests for User Story 2

- [ ] T013 [US2] Add template-conformance regressions in `tests/test_wiki_ops.py` for optional sections, dormant/dissolved lifecycle exemptions, required sections, allowed callouts, and exactly one disallowed-callout finding

### Implementation for User Story 2

- [ ] T014 [US2] Define the faction `TemplateContract` at `wiki/templates/contracts/faction.yml`, including required frontmatter, required/optional headings, lifecycle `when` rules, parent paths, and allowed `[!narration]` callouts
- [ ] T015 [US2] Implement YAML contract loading, lifecycle requirement resolution, heading-path presence checks, callout validation, and missing-frontmatter findings in `tools/wiki_ops/template_contracts.py`
- [ ] T016 [US2] Extend `tools/lint_wiki.py` to apply an explicit template contract to the already scoped page set and report lifecycle exemptions without deriving mandates from comments
- [ ] T017 [US2] Integrate contract selection, `--template` behavior, JSON output, and fallback to `TemplateProfile` in `scripts/wiki-lint`

**Checkpoint**: Faction template lint distinguishes required, optional, and lifecycle-omitted structure.

---

## Phase 5: User Story 3 - Creative Lint With Applicability Awareness (Priority: P2)

**Goal**: Keep creative heuristics on applicable narrative surfaces, exempt structural text, and prevent unproven rules from producing high-severity noise.

**Independent Test**: Run SCENE001 against a redirect stub, metadata/template/table content, and a faction narrative page with explicit pressure; the exempt and pressured cases produce no false finding, while a rule without positive fixtures remains SHADOW or WARN.

### Tests for User Story 3

- [ ] T018 [US3] Add SCENE001 positive/negative applicability fixtures at `tests/fixtures/creative_lint/SCENE001/redirect_stub.md`, `tests/fixtures/creative_lint/SCENE001/pass_explicit_pressure.md`, and `tests/fixtures/creative_lint/SCENE001/fail_missing_pressure.md`
- [ ] T019 [US3] Add applicability, structural-exemption, and zero-positive-fixture severity regressions in `tests/test_creative_lint.py` and `tests/test_creative_lint_cli.py`

### Implementation for User Story 3

- [ ] T020 [US3] Extend `Finding` and `RuleDefinition` schemas in `tools/creative_lint/finding.py` and `tools/creative_lint/registry.py` with document applicability, structural scope, exemptions, and repair class fields
- [ ] T021 [US3] Enforce applicability filtering, structural exclusions, and SHADOW/WARN severity capping for rules lacking positive fixtures in `tools/creative_lint/engine.py`
- [ ] T022 [US3] Update SCENE001 applicability, scope, exemptions, repair class, and fixture metadata in `rules/registry.yml` and preserve its WARN ceiling in `tools/creative_lint/severity.py`
- [ ] T023 [US3] Expose the applicability and repair-class metadata in `tools/creative_lint/cli_output.py` and `scripts/wiki-lint`

**Checkpoint**: Creative lint evaluates only meaningful narrative surfaces and reports safe severities.

---

## Phase 6: User Story 4 - Typed Mutation Operations (Priority: P1)

**Goal**: Apply semantic mutations with selectors and preconditions, resolve every result before writing, and leave originals untouched on rejection.

**Independent Test**: Replace a section with a matching content hash, then repeat with a stale hash and overlapping operations; the first emits a diff and applies atomically, while the latter two reject before any write.

### Tests for User Story 4

- [ ] T024 [US4] Add mutation regressions in `tests/test_wiki_ops.py` for section parsing, heading-path selection, SHA-256 hash matches/mismatches, dry-run parity, malformed targets, and overlap rejection

### Implementation for User Story 4

- [ ] T025 [US4] Implement `MutationOp`, section parsing, semantic heading-path selectors, `section_hash`, invariant validation, and atomic single-operation application in `tools/wiki_ops/mutations.py`
- [ ] T026 [US4] Implement `replace_section`, `delete_section`, `insert_section`, `set_frontmatter`, `remove_frontmatter`, `rewrite_links`, and `rename_page` argument validation and JSON results in `scripts/wiki-bulk-ops`
- [ ] T027 [US4] Add canonical-page merge behavior to `tools/wiki_ops/mutations.py`, preserving the source as a redirect and producing deterministic backlink and index/manifest mutation operations
- [ ] T028 [US4] Add stale-plan hash validation and clean rejection reporting to `tools/wiki_ops/mutations.py` and `scripts/wiki-bulk-ops`

**Checkpoint**: Typed semantic operations are safe to preview, reject, and apply without low-level patch syntax.

---

## Phase 7: User Story 5 - Index and Manifest as Structured State (Priority: P2)

**Goal**: Treat index entries and page identity transitions as structured state managed by typed operations rather than raw regex edits.

**Independent Test**: Replace a slug entry and record a `merged_into` transition through the mutation API; unrelated index entries and source-ingest provenance remain unchanged.

### Tests for User Story 5

- [ ] T029 [US5] Add structured index and manifest regressions in `tests/test_wiki_ops.py` for entry replacement/removal/insertion, malformed-index rejection, page-level transitions, and provenance preservation

### Implementation for User Story 5

- [ ] T030 [US5] Implement newline-safe index parsing and `replace_index_entry`, `remove_index_entry`, and sorted `insert_index_entry` in `tools/wiki_ops/index_ops.py`
- [ ] T031 [US5] Implement `ManifestTransition` validation and additive `merged_into`, `renamed_to`, and `archived` records in `tools/wiki_ops/manifest_ops.py`
- [ ] T032 [US5] Extend `scripts/manifest.py` with the page-level identity transition command while preserving source-level `pages_produced` and ingest history
- [ ] T033 [US5] Wire index and manifest operations into `MutationOp` resolution and `scripts/wiki-bulk-ops`, including malformed-state errors and atomic writes

**Checkpoint**: Index and manifest changes are addressable through typed state operations.

---

## Phase 8: User Story 6 - Batched Finalization at Transaction Boundaries (Priority: P2)

**Goal**: Validate and commit a complete mutation set atomically, then refresh derived state once with a compact summary.

**Independent Test**: Apply a three-file transaction with a counting QMD wrapper; all files commit, index/manifest update once where needed, QMD runs exactly once, and a finalization failure reports `committed` rather than pretending success.

### Tests for User Story 6

- [ ] T034 [US6] Add transaction regressions in `tests/test_wiki_ops.py` for all-or-nothing precondition validation, overlapping ranges, rollback on write failure, one QMD invocation, compact finalization output, and retryable finalization failure

### Implementation for User Story 6

- [ ] T035 [US6] Implement `Transaction` validation, overlap detection, in-memory resolution, invariant checks, atomic multi-file writes, backups, and rollback in `tools/wiki_ops/transactions.py`
- [ ] T036 [US6] Implement deferred index, manifest, and single QMD finalization with `pending`, `committed`, `failed`, and `finalized` lifecycle states in `tools/wiki_ops/transactions.py`
- [ ] T037 [US6] Implement `scripts/wiki-bulk-ops transact --plan-file --approve --vault --json` with preview, validation-failure exit 2, write/finalization-failure exit 1, and compact summary output
- [ ] T038 [US6] Connect `scripts/qmd-maintain.sh`, `tools/wiki_ops/index_ops.py`, and `tools/wiki_ops/manifest_ops.py` to transaction finalization without intermediate refreshes

**Checkpoint**: Multi-file repairs commit once and finalize derived maintenance once.

---

## Phase 9: User Story 7 - Identity Resolution Before Work Ordering (Priority: P1)

**Goal**: Resolve page identity from all available signals before queueing repairs, classify candidates deterministically, and block ambiguous work.

**Independent Test**: Resolve the faction fixture and scan its type scope; explicit redirects resolve canonically, overlapping same-type pages become ambiguous with candidates, and ambiguous queue items are rejected.

### Tests for User Story 7

- [ ] T039 [US7] Add identity regressions in `tests/test_wiki_ops.py` for redirects, title/alias matches, same-type content overlap, shared provenance, distinct raw pages without frontmatter, deterministic classification, and mutation gating

### Implementation for User Story 7

- [ ] T040 [US7] Implement `PageIdentity`, signal extraction from frontmatter, filenames, redirects, wikilinks, manifest provenance, type/kind, merge history, and `difflib.SequenceMatcher` body overlap in `tools/wiki_ops/identity.py`
- [ ] T041 [US7] Implement `resolve_identity` and `scan_identities` classification rules for `resolved`, `ambiguous`, and `distinct`, including required candidates and signal output in `tools/wiki_ops/identity.py`
- [ ] T042 [US7] Add `scripts/wiki-identity resolve` and `scripts/wiki-identity scan` with scope support, JSON output, and exit codes 0/1/2 in `scripts/wiki-identity`
- [ ] T043 [US7] Gate repair queueing and consolidation in `scripts/wiki-lint` and `scripts/wiki-bulk-ops` on resolved identity, reporting candidates and `identity_ambiguous` without ordering by filename or size

**Checkpoint**: No automatic repair or consolidation proceeds from an ambiguous identity.

---

## Phase 10: User Story 8 - Policy Single-Ownership (Priority: P2)

**Goal**: Register one authority for each policy and surface contradictory lower-level restatements instead of silently choosing one.

**Independent Test**: Point a consumer skill at the acceptance-semantics owner, introduce a contradictory restatement in a test fixture, and verify the checker reports both locations and the conflict.

### Tests for User Story 8

- [ ] T044 [US8] Add policy ownership and contradiction regressions in `tests/test_policy_conflicts.py` for owner resolution, consumer references, semantic-difference detection, and actionable conflict output

### Implementation for User Story 8

- [ ] T045 [US8] Complete `docs/agents/policy-owners.yml` entries for acceptance semantics, callout vocabulary, template optionality, repair safety, and mutation approval with one authoritative owner each
- [ ] T046 [US8] Replace duplicated acceptance and template-policy prose with registry references in `docs/agents/work.md`, `.agents/skills/faction-design/SKILL.md`, and `.agents/skills/wiki-ingest/SKILL.md`
- [ ] T047 [US8] Implement the deterministic policy conflict checker at `scripts/check-policy-conflicts`, including owner/consumer parsing, contradiction locations, JSON output, and exit status
- [ ] T048 [US8] Add policy-checker invocation to the repository maintenance path in `scripts/wiki-maintain` without hiding conflicts behind automatic mutation

**Checkpoint**: Policy conflicts are visible and every governed rule has one owner.

---

## Phase 11: Polish & Cross-Cutting Concerns

**Purpose**: Close regression coverage, document the canonical command surface, and validate the feature end to end.

- [ ] T049 [P] Add causal regressions for errors e-10, e-12 through e-21, and e-23 in `tests/test_wiki_ops.py`, each asserting the observable failure is prevented at the public CLI or library seam
- [ ] T050 [P] Document identity, scope, mutation, plan, transaction, and policy commands in `docs/cli.md` and their architecture boundaries in `docs/architecture.md`
- [ ] T051 Run every validation scenario in `specs/025-agent-safe-wiki-ops/quickstart.md` and record any command-contract corrections in `tests/test_wiki_ops.py`
- [ ] T052 Run the focused wiki-operation and creative-lint suites from `specs/025-agent-safe-wiki-ops/quickstart.md`, then verify `python3 scripts/check-policy-conflicts --json` and `python3 scripts/wiki-lint --scope dir:entities/faction --json --vault wiki`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies; T001–T003 can run in parallel.
- **Foundational (Phase 2)**: Depends on Setup; T004–T007 establish shared scope, CLI, and fixtures and block all story work.
- **User Stories**: Story phases depend on Foundational. Their additional dependencies are listed below; unrelated stories may run in parallel once their prerequisites are complete.
- **Polish (Phase 11)**: Depends on all desired stories and their public seams being complete.

### User Story Dependencies

- **US1 (P1)**: Depends on US4 and US7 for typed mutations and identity gating; consumes US2 template conformance and US6 finalization for the complete pipeline.
- **US2 (P1)**: Depends only on Foundational and is independently testable.
- **US3 (P2)**: Depends only on Foundational and existing 024 creative-lint interfaces; is independently testable.
- **US4 (P1)**: Depends only on Foundational; US5 supplies structured index/manifest operations used by merge behavior.
- **US5 (P2)**: Depends on US4 mutation dispatch; is independently testable through the typed operations.
- **US6 (P2)**: Depends on US4 and US5; US1 consumes its finalization pipeline.
- **US7 (P1)**: Depends only on Foundational; US1 consumes its identity gate.
- **US8 (P2)**: Depends only on Foundational and is independently testable against the registry/checker.

### Within Each User Story

- Tests are written before implementation and must fail against the pre-feature behavior.
- Parsers and data models precede services/engines; libraries precede CLI wiring.
- Mutation preconditions and complete-result validation precede atomic writes.
- A story checkpoint requires its independent test criteria to pass without full-vault work.

### Parallel Opportunities

- **US1**: T009 and T010 can proceed in parallel after T008's test contract is agreed; T011 follows the mutation API.
- **US2**: T014 can proceed in parallel with the test additions in T013; T015 follows the YAML shape, while T016 and T017 follow the loader.
- **US3**: T018 is independent of T020; T020 and T022 can proceed in parallel before T021 engine integration.
- **US4**: T025 is the shared library seam; CLI option wiring T026 and regression assertions T024 should not edit the same implementation symbols concurrently.
- **US5**: T030 and T031 can proceed in parallel; T032 and T033 follow their respective state APIs.
- **US6**: T035 and T037 can proceed in parallel only after the transaction contract is fixed; T036 and T038 follow transaction lifecycle decisions.
- **US7**: T040 and T042 can proceed in parallel after the identity JSON contract is fixed; T041 and T043 follow the resolver.
- **US8**: T045 and T044 can proceed in parallel; T046 and T048 follow the registry/checker contract.
- **Across stories**: US2, US3, US7, and the initial US4 library work can proceed in parallel after Foundational; US1, US5, and US6 retain their stated dependencies.

---

## Implementation Strategy

### MVP First (User Story 1)

1. Complete Phase 1 and Phase 2.
2. Complete US4 typed mutation primitives and US7 identity resolution because US1 depends on them.
3. Complete US2 template contracts and US6 transaction finalization needed by the full acceptance workflow.
4. Complete US1 scoped lint, repair planning, and consolidation integration.
5. Stop and validate the independent faction workflow from `quickstart.md` before adding P2 policy and creative improvements.

### Incremental Delivery

1. Deliver Foundational + US4 + US7: safe semantic mutation and identity gates.
2. Add US2: false-mandate-free template lint.
3. Add US1 + US6: complete scoped lint-to-consolidation MVP with one finalization pass.
4. Add US5: structured index and manifest state operations.
5. Add US3: applicability-aware creative lint.
6. Add US8: policy ownership and contradiction reporting.
7. Run Polish and causal regression coverage for every listed open error.

### Suggested Parallel Team Strategy

1. One owner completes Setup and Foundational.
2. After the checkpoint, assign US4 and US7 to separate owners; assign US2 and US3 independently.
3. Integrate US5 after US4, then US6; integrate US1 after US2, US4, US6, and US7.
4. Run US8 separately because it owns agent-facing policy files; avoid concurrent edits to the same canonical artifact.

---

## Notes

- Every task uses the required `- [ ] T###` checklist form; `[P]` appears only where files and prerequisites permit parallel work.
- `[US#]` labels appear only in user-story phases and map directly to the eight stories in `spec.md`.
- Every task names an exact repository path or explicit file set; no line-number patching or regex index editing is part of the implementation plan.
