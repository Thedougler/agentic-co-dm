---

description: "Task list for Agent-Safe Wiki Operations"
---

# Tasks: Agent-Safe Wiki Operations

**Input**: Design documents from `/specs/025-agent-safe-wiki-ops/`

**Prerequisites**: `plan.md`, `spec.md`, `research.md`, `data-model.md`, `quickstart.md`, and `contracts/`

**Tests**: Behavioral tests are included because the specification requires independent story tests, SC-007 causal regression coverage, and the constitution requires public-seam tests for new behavior.

**Organization**: Story phases are ordered by priority; ties are dependency-ordered so reusable mutation and identity seams land before the end-to-end faction workflow.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Establish the package, fixture, and contract paths used by later story increments.

- [X] T001 [P] Create the `tools/wiki_ops/` package and module paths in `tools/wiki_ops/__init__.py`, `tools/wiki_ops/identity.py`, `tools/wiki_ops/mutations.py`, `tools/wiki_ops/transactions.py`, `tools/wiki_ops/index_ops.py`, and `tools/wiki_ops/manifest_ops.py`
- [X] T002 [P] Create isolated wiki-operation fixture files in `tests/fixtures/wiki_ops/fisks-fleet.md`, `tests/fixtures/wiki_ops/fisks-captains.md`, `tests/fixtures/wiki_ops/index.md`, and `tests/fixtures/wiki_ops/.manifest.json`
- [X] T003 [P] Create creative-lint applicability fixture paths in `tests/fixtures/creative_lint/SCENE001/redirect_stub.md`, `tests/fixtures/creative_lint/SCENE001/pass_explicit_pressure.md`, and `tests/fixtures/creative_lint/SCENE001/fail_missing_pressure.md`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Provide shared scope semantics, repository path discovery, and the behavioral test harness before story implementation.

**Critical**: No user-story implementation begins until this phase is complete.

- [X] T004 Implement the typed `Scope` model and `files`, `directory`, `entity_type`, `identity_set`, `changed`, and `bundle` resolution in `tools/wiki_ops/scope.py`
- [X] T005 Extend repository/vault discovery, JSON emission, actionable errors, and exit codes 0/1/2 without breaking existing commands in `scripts/wiki-bulk-ops`, `scripts/wiki-lint`, and `scripts/manifest.py`
- [X] T006 Add the temporary-vault subprocess harness and shared assertions following `tests/test_wiki_bulk_ops.py` conventions in `tests/test_wiki_ops.py`
- [X] T007 Add command `--help`, JSON-mode, vault-discovery, and exit-status contract checks in `tests/test_wiki_ops.py`

**Checkpoint**: Scope objects, CLI conventions, fixture builders, and public-seam assertions are ready for all stories.

---

## Phase 3: User Story 4 - Typed Mutation Operations (Priority: P1)

**Goal**: Apply semantic edits with preconditions, complete-result validation, and atomic rejection semantics.

**Independent Test**: Replace a section by heading path with a matching SHA-256 content hash, then retry with a stale hash and overlapping transaction targets; the first applies atomically and the latter two leave the original untouched with actionable rejection reasons.

### Tests for User Story 4

- [X] T008 [US4] Add failing public-seam regressions for section parsing, heading-path selection, SHA-256 preconditions, dry-run parity, malformed targets, and overlap rejection in `tests/test_wiki_ops.py`

### Implementation for User Story 4

- [X] T009 [US4] Implement `MutationOp`, section parsing, semantic heading-path selectors, `section_hash`, frontmatter invariants, and atomic single-operation application in `tools/wiki_ops/mutations.py`
- [X] T010 [US4] Implement `replace_section`, `delete_section`, `insert_section`, `set_frontmatter`, `remove_frontmatter`, and `rewrite_links` dispatch, validation, diffs, and JSON results in `scripts/wiki-bulk-ops`
- [X] T011 [US4] Implement stale repair-plan hash validation and typed `RepairPlan` serialization with finding provenance and SHA-256 plan hashes in `tools/wiki_ops/mutations.py`
- [X] T012 [US4] Implement `rename_or_merge_page` result computation with canonical-page updates, deterministic backlink rewrites, obsolete-page removal, and an explicit no-redirect-stub invariant in `tools/wiki_ops/mutations.py`
- [X] T013 [US4] Wire mutation operation dispatch, dry-run/apply status values, and rejection exit code 2 into `scripts/wiki-bulk-ops`

**Checkpoint**: Every typed mutation can be previewed, validated, applied atomically, or rejected without line-number or regex patch composition.

---

## Phase 4: User Story 7 - Identity Resolution Before Work Ordering (Priority: P1)

**Goal**: Resolve entity identity from repository signals before repair ordering and block ambiguous work.

**Independent Test**: Scan fixture pages with overlapping same-type content and different titles; the result is `ambiguous` with both candidates, a clean page is `resolved`, and a raw no-frontmatter page is `distinct`.

### Tests for User Story 7

- [X] T014 [US7] Add failing identity regressions for title/alias matches, same-type QMD/body overlap, shared manifest provenance, merge history, redirects exclusion, distinct raw pages, deterministic classification, and mutation gating in `tests/test_wiki_ops.py`

### Implementation for User Story 7

- [X] T015 [US7] Implement `PageIdentity`, identity signal extraction from frontmatter, filenames, wikilinks, manifest provenance, type/kind, merge history, and QMD-backed similarity in `tools/wiki_ops/identity.py`
- [X] T016 [US7] Implement `resolved`, `ambiguous`, and `distinct` classification rules with required candidate validation and signal output in `tools/wiki_ops/identity.py`
- [X] T017 [US7] Implement `scripts/wiki-identity resolve` and `scripts/wiki-identity scan` with scope support, JSON output, and exit codes 0/1/2 in `scripts/wiki-identity`
- [X] T018 [US7] Gate repair queueing and consolidation on resolved identity, reporting `identity_ambiguous` candidates without filename/size ordering in `scripts/wiki-lint` and `scripts/wiki-bulk-ops`

**Checkpoint**: No automatic repair or consolidation proceeds from an ambiguous identity result.

---

## Phase 5: User Story 2 - Template Conformance Without False Mandates (Priority: P1)

**Goal**: Enforce explicit required, optional, lifecycle-conditional, callout, and frontmatter semantics without scaffold false positives.

**Independent Test**: Lint faction fixtures that omit optional sections and use dormant/dissolved lifecycles; no false-mandatory findings appear, while missing required sections and disallowed callouts produce the specified findings.

### Tests for User Story 2

- [X] T019 [US2] Add failing template regressions for omitted optional sections, dormant/dissolved lifecycle exemptions, genuinely missing required sections, required frontmatter, allowed callouts, and exactly one disallowed-callout finding in `tests/test_wiki_ops.py`
- [X] T020 [US2] Add failing regressions for deprecated faction-clock guidance at source and inherited downstream output, plus `redirects_to` stub detection and deterministic deletion/rewrite action in `tests/test_wiki_ops.py`

### Implementation for User Story 2

- [X] T021 [US2] Define the faction `TemplateContract` with required frontmatter, required/optional headings, parent paths, lifecycle `when` rules, and allowed `[!narration]` callouts in `wiki/templates/contracts/faction.yml`
- [X] T022 [US2] Implement YAML contract loading, lifecycle requirement resolution, heading-path checks, callout validation, frontmatter checks, and exemption counts in `tools/wiki_ops/template_contracts.py`
- [X] T023 [US2] Extend deterministic lint to detect disallowed callouts, deprecated clock guidance in `wiki/templates/faction.md` and `.agents/skills/faction-design/SKILL.md`, inherited clock output, and legacy `redirects_to` stubs in `tools/lint_wiki.py`
- [X] T024 [US2] Integrate contract selection, `--template` output, repair classes, and fallback to `TemplateProfile` in `scripts/wiki-lint`

**Checkpoint**: Faction conformance reports only genuine violations and distinguishes critical source guidance from downstream error symptoms.

---

## Phase 6: User Story 1 - Scoped Faction Lint and Consolidation (Priority: P1) 🎯 MVP

**Goal**: Complete identity preflight through scoped lint, deterministic repair planning, atomic consolidation, and one final maintenance pass.

**Independent Test**: Run the faction fixture through identity scan, scoped lint, plan preview, and approved transaction; only scoped files appear, ambiguity blocks unsafe work, deterministic actions are typed, and finalization is summarized once.

### Tests for User Story 1

- [X] T025 [US1] Add the failing end-to-end faction workflow regression for compact file-grouped findings, silent cross-scope links, deterministic plan actions, dry-run preview, approval gating, atomic merge, index/manifest changes, and ambiguity blocking in `tests/test_wiki_ops.py`

### Implementation for User Story 1

- [X] T026 [US1] Extend scoped structural lint to filter pages before checks, detect broken wikilinks and broken `![[embed]]`/image links, and emit compact scope/count/file-grouped JSON in `tools/lint_wiki.py`
- [X] T027 [US1] Implement `--scope`, `--template`, `--plan`, `--from`, `--vault`, and `--json` orchestration with silent cross-scope link handling in `scripts/wiki-lint`
- [X] T028 [US1] Build deterministic repair plans from lint findings with typed actions, human/diagnostic counts, stable ordering, and stale-plan hashes in `scripts/wiki-lint` and `tools/wiki_ops/mutations.py`
- [X] T029 [US1] Wire identity preflight, scoped lint, plan preview, approval, and consolidation transaction sequencing through `scripts/wiki-lint` and `scripts/wiki-bulk-ops`

**Checkpoint**: A known faction can be safely linted and consolidated using only repository-provided typed CLI surfaces.

---

## Phase 7: User Story 5 - Index and Manifest as Structured State (Priority: P2)

**Goal**: Update index entries and page identity transitions through typed operations while preserving source-ingest provenance.

**Independent Test**: Replace/remove/insert an index entry and record a `merged_into` transition; unrelated entries and source-level `pages_produced` history remain unchanged, and malformed index state is rejected.

### Tests for User Story 5

- [X] T030 [US5] Add failing structured-state regressions for entry replacement/removal/sorted insertion, malformed-index rejection, additive page transitions, and provenance preservation in `tests/test_wiki_ops.py`

### Implementation for User Story 5

- [X] T031 [US5] Implement newline-safe structured index parsing, validation, `replace_index_entry`, `remove_index_entry`, and sorted `insert_index_entry` in `tools/wiki_ops/index_ops.py`
- [X] T032 [US5] Implement `ManifestTransition` validation and additive `merged_into`, `renamed_to`, and `archived` records in `tools/wiki_ops/manifest_ops.py`
- [X] T033 [US5] Extend `scripts/manifest.py` with the page-level identity transition command while preserving source-level `pages_produced` and ingest history
- [X] T034 [US5] Wire index and manifest operations into mutation resolution with malformed-state errors and atomic writes in `tools/wiki_ops/mutations.py` and `scripts/wiki-bulk-ops`

**Checkpoint**: Structured index and manifest state is addressable without raw 107KB index regex editing or manual provenance substitution.

---

## Phase 8: User Story 6 - Batched Finalization at Transaction Boundaries (Priority: P2)

**Goal**: Validate and commit a complete mutation set atomically, then run derived maintenance exactly once with compact output.

**Independent Test**: Apply a three-file transaction with a counting QMD wrapper; all files commit, QMD runs once at the end, and a finalization failure reports `committed` for retry rather than false success.

### Tests for User Story 6

- [X] T035 [US6] Add failing transaction regressions for all-or-nothing validation, overlapping ranges, write rollback, one QMD invocation, compact finalization output, and retryable finalization failure in `tests/test_wiki_ops.py`

### Implementation for User Story 6

- [X] T036 [US6] Implement `Transaction` accumulation, precondition validation, overlap detection, in-memory result resolution, invariant checks, atomic multi-file writes, backups, and rollback in `tools/wiki_ops/transactions.py`
- [X] T037 [US6] Implement pending/committed/failed/finalized lifecycle states and deferred index, manifest, and single QMD finalization in `tools/wiki_ops/transactions.py`
- [X] T038 [US6] Implement `scripts/wiki-bulk-ops transact --plan-file --approve --vault --json` with preview output, validation exit 2, write/finalization exit 1, and compact summary fields in `scripts/wiki-bulk-ops`
- [X] T039 [US6] Connect `scripts/qmd-maintain.sh`, `tools/wiki_ops/index_ops.py`, and `tools/wiki_ops/manifest_ops.py` to transaction finalization without intermediate refreshes

**Checkpoint**: Multi-file repairs commit once and finalize derived maintenance once.

---

## Phase 9: User Story 3 - Creative Lint With Applicability Awareness (Priority: P2)

**Goal**: Run creative heuristics only on applicable narrative surfaces and cap unproven rules at safe severity.

**Independent Test**: SCENE001 produces no finding for a redirect stub, metadata/template/table content, or a pressured faction narrative; a rule without positive fixtures remains SHADOW or WARN.

### Tests for User Story 3

- [X] T040 [P] [US3] Add SCENE001 positive/negative applicability fixtures in `tests/fixtures/creative_lint/SCENE001/redirect_stub.md`, `tests/fixtures/creative_lint/SCENE001/pass_explicit_pressure.md`, and `tests/fixtures/creative_lint/SCENE001/fail_missing_pressure.md`
- [X] T041 [US3] Add failing applicability, structural-exemption, zero-positive-fixture severity, and transient-transaction-state regressions in `tests/test_creative_lint.py` and `tests/test_creative_lint_cli.py`

### Implementation for User Story 3

- [X] T042 [US3] Extend `Finding` and `RuleDefinition` schemas with document applicability, structural scope, exemptions, repair class, and fixture metadata in `tools/creative_lint/finding.py` and `tools/creative_lint/registry.py`
- [X] T043 [US3] Enforce applicability filtering, structural exclusions, redirect exemptions, and SHADOW/WARN capping for rules lacking positive fixtures in `tools/creative_lint/engine.py`
- [X] T044 [US3] Declare SCENE001 narrative applicability, structural exclusions, redirect exemption, repair class, and fixture metadata in `rules/registry.yml`
- [X] T045 [US3] Expose applicability and repair-class metadata in `tools/creative_lint/cli_output.py` and `scripts/wiki-lint`

**Checkpoint**: Creative lint evaluates meaningful narrative surfaces without drowning actionable findings in false positives.

---

## Phase 10: User Story 8 - Policy Single-Ownership (Priority: P2)

**Goal**: Register one authority per policy and surface contradictory lower-level restatements.

**Independent Test**: Point a consumer skill at the acceptance-semantics owner, add a contradictory fixture restatement, and verify the checker reports both locations and the conflict.

### Tests for User Story 8

- [X] T046 [US8] Add failing policy ownership regressions for owner resolution, consumer references, semantic-difference detection, and actionable conflict output in `tests/test_policy_conflicts.py`

### Implementation for User Story 8

- [X] T047 [US8] Complete `docs/agents/policy-owners.yml` entries for acceptance semantics, callout vocabulary, template optionality, repair safety, and mutation approval with exactly one owner each
- [X] T048 [US8] Replace duplicated acceptance and template-policy prose with registry references in `docs/agents/work.md`, `.agents/skills/faction-design/SKILL.md`, and `.agents/skills/wiki-ingest/SKILL.md`
- [X] T049 [US8] Implement owner/consumer parsing, semantic conflict detection, JSON output, and exit statuses in `scripts/check-policy-conflicts`
- [X] T050 [US8] Add policy-conflict checking to the routine maintenance path without hiding conflicts behind automatic mutation in `scripts/wiki-maintain`

**Checkpoint**: Every governed policy has one visible authority and conflicts are actionable rather than silently resolved.

---

## Phase 11: Polish & Cross-Cutting Concerns

**Purpose**: Close causal regression coverage, document the canonical command surface, and validate the quickstart end to end.

- [X] T051 [P] Add causal public-seam regressions for e-10, e-12 through e-23, and e-24 through e-38, mapping each error to the preventing behavior in `tests/test_wiki_ops.py`, `tests/test_creative_lint.py`, `tests/test_creative_lint_cli.py`, and `tests/test_policy_conflicts.py`
- [X] T052 [P] Document identity, scope, template, mutation, repair-plan, transaction, and policy commands plus architecture boundaries in `docs/cli.md` and `docs/architecture.md`
- [X] T053 Run every validation scenario in `specs/025-agent-safe-wiki-ops/quickstart.md` and record command-contract corrections in `tests/test_wiki_ops.py`
- [X] T054 Run the focused suites from `specs/025-agent-safe-wiki-ops/quickstart.md`, then verify `python3 scripts/check-policy-conflicts --json` and `python3 scripts/wiki-lint --scope dir:entities/faction --json --vault wiki`

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies; T001–T003 can run in parallel.
- **Foundational (Phase 2)**: Depends on Setup; T004–T007 block all story work.
- **P1 stories**: US4 and US7 depend only on Foundational; US2 depends only on Foundational; US1 depends on US2, US4, and US7, and consumes US6 for finalization.
- **P2 stories**: US5 depends on US4; US6 depends on US4 and US5; US3 and US8 depend on Foundational and existing 024 interfaces.
- **Polish (Phase 11)**: Depends on all desired stories and their public seams.

### User Story Completion Order

1. US4 — typed mutation primitives
2. US7 — identity resolution and gating
3. US2 — template contracts and false-mandate-free lint
4. US1 — scoped faction lint and consolidation MVP
5. US5 — structured index and manifest state
6. US6 — batched transaction finalization
7. US3 — applicability-aware creative lint
8. US8 — policy ownership and conflict reporting

### Parallel Opportunities

- Setup T001–T003 are independent.
- After Foundational, US4, US7, US2, US3, and US8 can begin on separate files; do not parallelize tasks sharing `scripts/wiki-bulk-ops`, `scripts/wiki-lint`, or `tests/test_wiki_ops.py`.
- In US4, T009 and T011 are library work that can proceed separately after the mutation contract is fixed; CLI wiring follows them.
- In US7, T015 and T017 can proceed separately after the identity JSON contract is fixed.
- In US2, T019/T020 test work can proceed with T021 contract authoring; loader and CLI integration follow the schema.
- In US5, T031 and T032 can proceed in parallel; T033/T034 follow their APIs.
- In US3, T040 and T042/T044 can proceed in parallel; engine integration follows metadata and fixtures.
- In US8, T046 and T047 can proceed in parallel; consumer cleanup and maintenance wiring follow the registry/checker contract.

---

## Implementation Strategy

### MVP First (User Story 1)

1. Complete Setup and Foundational.
2. Complete US4 typed mutation primitives and US7 identity gating.
3. Complete US2 template conformance.
4. Complete US1 scoped lint, deterministic repair planning, and consolidation integration.
5. Add US6 transaction finalization needed by the approved end-to-end run, then validate the independent faction workflow from `quickstart.md`.

### Incremental Delivery

1. Deliver US4 + US7: safe semantic mutation and identity gates.
2. Add US2: false-mandate-free template lint.
3. Add US1 + US6: complete scoped lint-to-consolidation with one finalization pass.
4. Add US5: structured index and manifest operations.
5. Add US3: applicability-aware creative lint.
6. Add US8: policy ownership and contradiction reporting.
7. Run Polish and causal regression coverage for every listed open error.

### Notes

- Every task uses `- [ ] T###` with exact repository paths; `[P]` appears only for independent work.
- Story labels appear only in user-story phases and map directly to `spec.md` stories.
- No task creates redirect stubs, edits `wiki/index.md` with regex/line-number patches, or asks an agent to compose low-level hunk grammar.
