---

description: "Task list for Agent-Safe Wiki Operations"
---

# Tasks: Agent-Safe Wiki Operations

**Input**: Design documents from `/specs/025-agent-safe-wiki-ops/`

**Prerequisites**: `plan.md`, `spec.md`, `research.md`, `data-model.md`, `quickstart.md`, and `contracts/`

**Tests**: Behavioral tests are included because the specification requires independent story tests, SC-007 causal regression coverage, and the constitution requires public-seam tests for new behavior.

**Organization**: Story phases are ordered by priority; ties are dependency-ordered so reusable mutation and identity seams land before the end-to-end faction workflow.

## Format: `- [ ] [TaskID] [P?] [Story?] Description`

- **[P]**: Can run in parallel only when it touches different files and has no dependency on incomplete work.
- **[Story]**: Maps a task to its user story; setup, foundational, and polish tasks have no story label.
- Every task names the exact repository path it changes or validates.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Establish package, fixture, and contract paths used by later story increments.

- [ ] T001 [P] Create or update the `tools/wiki_ops/` package modules in `tools/wiki_ops/__init__.py`, `tools/wiki_ops/identity.py`, `tools/wiki_ops/mutations.py`, `tools/wiki_ops/transactions.py`, `tools/wiki_ops/index_ops.py`, and `tools/wiki_ops/manifest_ops.py`.
- [ ] T002 [P] Create isolated wiki-operation fixtures in `tests/fixtures/wiki_ops/fisks-fleet.md`, `tests/fixtures/wiki_ops/fisks-captains.md`, `tests/fixtures/wiki_ops/index.md`, and `tests/fixtures/wiki_ops/.manifest.json`.
- [ ] T003 [P] Create the creative-lint fixture directory roots in `tests/fixtures/creative_lint/` and `tests/fixtures/creative_lint/SCENE001/`; add the actual scenario files in T043.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Provide shared scope semantics, repository discovery, CLI conventions, and the behavioral test harness before story implementation.

**Critical**: No user-story implementation begins until this phase is complete.

- [ ] T004 Implement the typed `Scope` model and resolution for `files | directory | entity_type | identity_set | changed | bundle` in `tools/wiki_ops/scope.py`, including required `kind`, `value`, and materialized `resolved_files` fields.
- [ ] T005 Extend repository/vault discovery, JSON output, actionable errors, and exit statuses `0/1/2` without breaking existing behavior in `scripts/wiki-bulk-ops`, `scripts/wiki-lint`, and `scripts/manifest.py`.
- [ ] T006 Add the temporary-vault subprocess harness, fixture builders, and shared public-seam assertions following `tests/test_wiki_bulk_ops.py` conventions in `tests/test_wiki_ops.py`.
- [ ] T007 Add command `--help`, JSON-mode, vault-discovery, and exit-status contract checks for `scripts/wiki-bulk-ops`, `scripts/wiki-lint`, and `scripts/manifest.py` in `tests/test_wiki_ops.py`.

**Checkpoint**: Scope objects, CLI conventions, fixture builders, and public-seam assertions are ready for all stories.

---

## Phase 3: User Story 4 - Typed Mutation Operations (Priority: P1)

**Goal**: Apply semantic edits with preconditions, complete-result validation, and atomic rejection semantics.

**Independent Test**: Replace a section by heading path with a matching SHA-256 content hash, then retry with a stale hash and overlapping transaction targets; the first applies atomically and the latter two leave the original untouched with actionable rejection reasons.

### Tests for User Story 4

- [ ] T008 [US4] Add failing public-seam regressions for section parsing, heading-path selection, SHA-256 preconditions, dry-run parity, malformed targets, and overlap rejection in `tests/test_wiki_ops.py`.

### Implementation for User Story 4

- [ ] T009 [US4] Implement `MutationOp`, section parsing, semantic heading-path selectors, `section_hash`, frontmatter invariants, and atomic single-operation application in `tools/wiki_ops/mutations.py`; enforce `kind`, `target`, `selector`, and `payload` as required fields and reject selectors that resolve to zero or multiple sections.
- [ ] T010 [US4] Implement `replace_section`, `delete_section`, `insert_section`, `set_frontmatter`, `remove_frontmatter`, and `rewrite_links` dispatch, validation, diffs, and JSON results in `scripts/wiki-bulk-ops`.
- [ ] T011 [US4] Implement typed `RepairPlan` serialization with `scope`, `source_findings`, `deterministic_actions`, `human_only`, ordered actions, and a SHA-256 `hash` for stale-plan detection in `tools/wiki_ops/mutations.py`.
- [ ] T012 [US4] Implement `rename_or_merge_page` result computation with canonical-page updates, deterministic backlink rewrites, obsolete-page removal, and an explicit no-redirect-stub invariant in `tools/wiki_ops/mutations.py`.
- [ ] T013 [US4] Wire mutation dispatch, dry-run/apply status values (`applied`, `rejected`, `dry_run`), actionable rejection reasons, and exit code `2` for precondition failures into `scripts/wiki-bulk-ops`.

**Checkpoint**: Every typed mutation can be previewed, validated, applied atomically, or rejected without line-number or regex patch composition.

---

## Phase 4: User Story 7 - Identity Resolution Before Work Ordering (Priority: P1)

**Goal**: Resolve entity identity from repository signals before repair ordering and block ambiguous work.

**Independent Test**: Scan fixture pages with overlapping same-type content and different titles; the result is `ambiguous` with both candidates, a clean page is `resolved`, and a raw no-frontmatter page is `distinct`.

### Tests for User Story 7

- [ ] T014 [US7] Add failing identity regressions for title/alias matches, same-type QMD/body overlap, shared manifest provenance, merge history, redirect exclusion, distinct raw pages, deterministic classification, and mutation gating in `tests/test_wiki_ops.py`.

### Implementation for User Story 7

- [ ] T015 [US7] Implement `PageIdentity` signal extraction from frontmatter, filenames, wikilinks, manifest provenance, type/kind, merge history, and QMD-backed similarity in `tools/wiki_ops/identity.py`; require `path`, `stem`, `title`, `status`, and `signals`, with `type`, `lifecycle`, and `aliases` optional.
- [ ] T016 [US7] Implement `resolved`, `ambiguous`, and `distinct` classification rules in `tools/wiki_ops/identity.py`; enforce `status: ambiguous` requires non-empty `candidates`, every candidate path exists, and `signals.qmd_content_similarity` remains in the range `0.0–1.0`.
- [ ] T017 [US7] Implement `resolve` and `scan` commands with scope support, structured JSON output, and exit codes `0/1/2` in `scripts/wiki-identity`.
- [ ] T018 [US7] Gate repair queueing and consolidation on resolved identity, report `identity_ambiguous` candidates, and remove filename/file-size ordering as an authority in `scripts/wiki-lint` and `scripts/wiki-bulk-ops`.

**Checkpoint**: No automatic repair or consolidation proceeds from an ambiguous identity result.

---

## Phase 5: User Story 2 - Template Conformance Without False Mandates (Priority: P1)

**Goal**: Enforce explicit required, optional, lifecycle-conditional, callout, and frontmatter semantics without scaffold false positives.

**Independent Test**: Lint faction fixtures that omit optional sections and use dormant/dissolved lifecycles; no false-mandatory findings appear, while missing required sections and disallowed callouts produce the specified findings.

### Tests for User Story 2

- [ ] T019 [US2] Add failing template regressions for omitted optional sections, dormant/dissolved lifecycle exemptions, genuinely missing required sections, required frontmatter, allowed callouts, and exactly one disallowed-callout finding in `tests/test_wiki_ops.py`.
- [ ] T020 [US2] Add failing regressions for deprecated faction-clock guidance at source and inherited downstream output, plus `redirects_to` stub detection and deterministic deletion/rewrite action in `tests/test_wiki_ops.py`.

### Implementation for User Story 2

- [ ] T021 [US2] Define the faction `TemplateContract` with explicit required/optional headings, repeatable/parent paths, lifecycle `when` rules, allowed `[!narration]` callouts, and required frontmatter in `wiki/templates/contracts/faction.yml`.
- [ ] T022 [US2] Implement YAML contract loading, lifecycle requirement resolution, heading-path checks, callout validation, frontmatter checks, and exemption counts in `tools/wiki_ops/template_contracts.py`; support `required`, `optional`, and `omit` outcomes with `default` fallback.
- [ ] T023 [US2] Extend deterministic lint to detect disallowed callouts, deprecated clock guidance in `wiki/templates/faction.md` and `.agents/skills/faction-design/SKILL.md`, inherited clock output, and legacy `redirects_to` stubs in `tools/lint_wiki.py`.
- [ ] T024 [US2] Integrate contract selection, template findings and repair classes, `--no-template` behavior, and fallback to `TemplateProfile` in `scripts/wiki-lint`.

**Checkpoint**: Faction conformance reports only genuine violations and distinguishes critical source guidance from downstream error symptoms.

---

## Phase 6: User Story 1 - Scoped Faction Lint and Consolidation (Priority: P1) 🎯 MVP

**Goal**: Complete identity preflight through scoped lint, deterministic repair planning, atomic consolidation, and one final maintenance pass.

**Independent Test**: Run the faction fixture through identity scan, scoped lint, plan preview, and approved transaction; only scoped files appear, ambiguity blocks unsafe work, deterministic actions are typed, and finalization is summarized once.

### Tests for User Story 1

- [ ] T025 [US1] Add the failing end-to-end faction workflow regression for compact file-grouped findings, silent cross-scope links, deterministic plan actions, Vale findings and `--no-vale` suppression, dry-run preview, approval gating, atomic merge, index/manifest changes, and ambiguity blocking in `tests/test_wiki_ops.py`.

### Implementation for User Story 1

- [ ] T026 [US1] Extend scoped structural and Vale lint to filter pages before checks, detect broken wikilinks and broken `![[embed]]`/image links, invoke the Vale adapter, and emit compact scope/count/file-grouped JSON in `tools/lint_wiki.py`, `tools/wiki_ops/vale_adapter.py`, `.vale.ini`, `styles/Deprecated/DMThesis.yml`, `styles/AITells/`, `styles/write-good/`, and `styles/proselint/`.
- [ ] T027 [US1] Implement `--scope`, `--template`, `--plan`, `--from`, `--vault`, and `--json` orchestration with silent cross-scope link handling in `scripts/wiki-lint`.
- [ ] T028 [US1] Build deterministic repair plans from lint findings with typed actions, diagnostic/human/deterministic counts, stable ordering, and stale-plan hashes in `scripts/wiki-lint` and `tools/wiki_ops/mutations.py`.
- [ ] T029 [US1] Wire identity preflight, scoped lint, plan preview, approval, and consolidation transaction sequencing through `scripts/wiki-lint` and `scripts/wiki-bulk-ops`.

**Checkpoint**: A known faction can be safely linted and consolidated using only repository-provided typed CLI surfaces.

---

## Phase 7: User Story 5 - Index and Manifest as Structured State (Priority: P2)

**Goal**: Update index entries and page identity transitions through typed operations while preserving source-ingest provenance.

**Independent Test**: Replace, remove, and insert an index entry and record a `merged_into` transition; unrelated entries and source-level `pages_produced` history remain unchanged, and malformed index state is rejected.

### Tests for User Story 5

- [ ] T030 [US5] Add failing structured-state regressions for entry replacement/removal/sorted insertion, malformed-index rejection, additive page transitions, and provenance preservation in `tests/test_wiki_ops.py`.

### Implementation for User Story 5

- [ ] T031 [P] [US5] Implement newline-safe structured index parsing, validation, `replace_index_entry`, `remove_index_entry`, and sorted `insert_index_entry` in `tools/wiki_ops/index_ops.py`; reject malformed `wiki/index.md` instead of appending.
- [ ] T032 [P] [US5] Implement `ManifestTransition` validation and additive `merged_into`, `renamed_to`, and `archived` records in `tools/wiki_ops/manifest_ops.py`, preserving source-level provenance.
- [ ] T033 [US5] Extend `scripts/manifest.py` with the page-level identity transition command while preserving source-level `pages_produced` and ingest history.
- [ ] T034 [US5] Wire index and manifest operations into mutation resolution with malformed-state errors and atomic writes in `tools/wiki_ops/mutations.py` and `scripts/wiki-bulk-ops`.

**Checkpoint**: Structured index and manifest state is addressable without raw 107KB index regex editing or manual provenance substitution.

---

## Phase 8: User Story 6 - Batched Finalization at Transaction Boundaries (Priority: P2)

**Goal**: Validate and commit a complete mutation set atomically, then run derived maintenance exactly once with compact output.

**Independent Test**: Apply a three-file transaction with a counting QMD wrapper; all files commit, QMD runs once at the end, and a finalization failure reports `committed` for retry rather than false success.

### Tests for User Story 6

- [ ] T035 [US6] Add failing transaction regressions for all-or-nothing validation, overlapping ranges, write rollback, one QMD invocation, compact finalization output, and retryable finalization failure in `tests/test_wiki_ops.py`.

### Implementation for User Story 6

- [ ] T036 [US6] Implement `Transaction` accumulation, precondition validation, overlap detection, in-memory result resolution, invariant checks, atomic multi-file writes, backups, and rollback in `tools/wiki_ops/transactions.py`.
- [ ] T037 [US6] Implement `pending`, `committed`, `failed`, and `finalized` lifecycle states plus deferred index, manifest, and single-QMD finalization in `tools/wiki_ops/transactions.py`; preserve `finalization` status fields for index, manifest, and QMD.
- [ ] T038 [US6] Implement `transact --plan-file --approve --vault --json` with preview output, validation exit `2`, write/finalization exit `1`, and compact summary fields in `scripts/wiki-bulk-ops`.
- [ ] T039 [US6] Connect `tools/wiki_ops/index_ops.py` and `tools/wiki_ops/manifest_ops.py` to transaction finalization without intermediate refreshes in `tools/wiki_ops/transactions.py`.
- [ ] T040 [US6] Implement standalone `scripts/qmd-hook.sh` with count-bounded embedding, serialized concurrent invocations, zero output on success, one actionable stderr line on failure, and silent exit-0 no-op when QMD is absent.
- [ ] T041 [US6] Add behavioral tests for `scripts/qmd-hook.sh` covering zero output on success, silent no-op without QMD, embedding bound, concurrent serialization, and maintenance failure output in `tests/test_wiki_ops.py`.
- [ ] T042 [US6] Replace direct `qmd-maintain.sh` finalization with exactly one `scripts/qmd-hook.sh` invocation per successful live write boundary in `tools/wiki_ops/transactions.py`.

**Checkpoint**: Multi-file repairs commit once and finalize derived maintenance once. The QMD hook is standalone and harness-agnostic.

---

## Phase 9: User Story 3 - Creative Lint With Applicability Awareness (Priority: P2)

**Goal**: Run creative heuristics only on applicable narrative surfaces and cap unproven rules at safe severity.

**Independent Test**: SCENE001 produces no finding for a redirect stub, metadata/template/table content, or a pressured faction narrative; a rule without positive fixtures remains SHADOW or WARN.

### Tests for User Story 3

- [ ] T043 [P] [US3] Add SCENE001 positive/negative applicability fixtures in `tests/fixtures/creative_lint/SCENE001/redirect_stub.md`, `tests/fixtures/creative_lint/SCENE001/pass_explicit_pressure.md`, and `tests/fixtures/creative_lint/SCENE001/fail_missing_pressure.md`.
- [ ] T044 [US3] Add failing applicability, structural-exemption, zero-positive-fixture severity, and transient-transaction-state regressions in `tests/test_creative_lint.py` and `tests/test_creative_lint_cli.py`.

### Implementation for User Story 3

- [ ] T045 [US3] Extend `Finding` and `RuleDefinition` schemas with document applicability, structural scope, exemptions, repair class, and fixture metadata in `tools/creative_lint/finding.py` and `tools/creative_lint/registry.py`.
- [ ] T046 [US3] Enforce applicability filtering, structural exclusions, redirect exemptions, and SHADOW/WARN capping for rules lacking positive fixtures in `tools/creative_lint/engine.py`.
- [ ] T047 [US3] Declare SCENE001 narrative applicability, structural exclusions, redirect exemption, repair class, and fixture metadata in `rules/registry.yml`.
- [ ] T048 [US3] Expose applicability and repair-class metadata in `tools/creative_lint/cli_output.py` and `scripts/wiki-lint`.

**Checkpoint**: Creative lint evaluates meaningful narrative surfaces without drowning actionable findings in false positives.

---

## Phase 10: User Story 8 - Policy Single-Ownership (Priority: P2)

**Goal**: Register one authority per policy and surface contradictory lower-level restatements.

**Independent Test**: Point a consumer skill at the acceptance-semantics owner, add a contradictory fixture restatement, and verify the checker reports both locations and the conflict.

### Tests for User Story 8

- [ ] T049 [US8] Add failing policy ownership regressions for owner resolution, consumer references, semantic-difference detection, and actionable conflict output in `tests/test_policy_conflicts.py`.

### Implementation for User Story 8

- [ ] T050 [US8] Complete `docs/agents/policy-owners.yml` entries for acceptance semantics, callout vocabulary, template optionality, repair safety, and mutation approval with exactly one owner each.
- [ ] T051 [US8] Replace duplicated acceptance and template-policy prose with registry references in `docs/agents/work.md`, `.agents/skills/faction-design/SKILL.md`, and `.agents/skills/wiki-ingest/SKILL.md`.
- [ ] T052 [US8] Implement owner/consumer parsing, semantic conflict detection, JSON output, and exit statuses in `scripts/check-policy-conflicts`.
- [ ] T053 [US8] Add policy-conflict checking to the routine maintenance path without hiding conflicts behind automatic mutation in `scripts/wiki-maintain`.

**Checkpoint**: Every governed policy has one visible authority and conflicts are actionable rather than silently resolved.

---

## Phase 11: Polish & Cross-Cutting Concerns

**Purpose**: Close causal regression coverage, document the canonical command surface, validate quickstart behavior, and wire the harness hook.

- [ ] T054 [P] Add causal public-seam regressions for e-10, e-12 through e-23, and e-24 through e-38, mapping each error to the preventing behavior in `tests/test_wiki_ops.py`, `tests/test_creative_lint.py`, `tests/test_creative_lint_cli.py`, and `tests/test_policy_conflicts.py`.
- [ ] T055 [P] Document identity, scope, template, mutation, repair-plan, transaction, QMD, and policy commands plus architecture boundaries in `docs/cli.md` and `docs/architecture.md`.
- [ ] T056 Run every validation scenario in `specs/025-agent-safe-wiki-ops/quickstart.md` and record any command-contract corrections in `tests/test_wiki_ops.py`.
- [ ] T057 Run the focused suites from `specs/025-agent-safe-wiki-ops/quickstart.md`, then verify `python3 scripts/check-policy-conflicts --json` and `python3 scripts/wiki-lint --scope dir:entities/faction --json --vault wiki`.
- [ ] T058 Wire `scripts/qmd-hook.sh` into OMP wiki-write boundaries through `.omp/config.yml`, `.omp/RULES.md`, or the authoritative OMP instruction surface, so OMP agents invoke the hook after committed wiki writes.

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies; T001–T003 can run in parallel.
- **Foundational (Phase 2)**: Depends on Setup; T004–T007 block all user stories.
- **P1 stories**: US4, US7, and US2 depend only on Foundational. US1 depends on US2, US4, and US7, and consumes US6 for finalization.
- **P2 stories**: US5 depends on US4; US6 depends on US4 and US5; US3 and US8 depend on Foundational and existing 024 interfaces.
- **Polish (Phase 11)**: Depends on the stories and public seams it validates. T058 depends on T040–T042.

### User Story Completion Order

1. US4 — typed mutation primitives
2. US7 — identity resolution and gating
3. US2 — template contracts and false-mandate-free lint
4. US1 — scoped lint and consolidation MVP
5. US5 — structured index and manifest state
6. US6 — batched transaction finalization and QMD hook
7. US3 — applicability-aware creative lint
8. US8 — policy ownership and conflict reporting

### Parallel Opportunities

- T001–T003 are independent setup work.
- After Foundational, US4, US7, US2, US3, and US8 can begin on separate files; serialize edits to `scripts/wiki-bulk-ops`, `scripts/wiki-lint`, and `tests/test_wiki_ops.py`.
- Within US4, T009 and T011 can proceed after the mutation contract; CLI wiring follows both.
- Within US7, T015 and T017 can proceed after the identity JSON contract; gating follows both.
- Within US2, T019/T020 and T021 can proceed independently; loader and CLI integration follow the contract.
- Within US5, T031 and T032 are independent; T033/T034 follow their APIs.
- Within US6, T036–T039 and T040/T041 can proceed on separate files after the transaction contract; T042 follows the hook and transaction APIs.
- Within US3, T043 and T045/T047 can proceed independently; engine and CLI integration follow metadata and fixtures.
- Within US8, T049 and T050 can proceed independently; consumer cleanup and maintenance wiring follow the registry/checker contract.
- After all stories, T054, T055, and T058 can proceed in parallel; T056/T057 validate the integrated result.

---

## Implementation Strategy

### MVP First (User Story 1)

1. Complete Setup and Foundational.
2. Complete US4 typed mutation primitives and US7 identity gating.
3. Complete US2 template conformance.
4. Complete US1 scoped lint, deterministic repair planning, and consolidation integration.
5. Complete the US6 transaction/QMD finalization slice required by the approved end-to-end faction workflow.
6. Stop and validate the independent faction workflow from `specs/025-agent-safe-wiki-ops/quickstart.md`.

### Incremental Delivery

1. Deliver US4 + US7: safe semantic mutation and identity gates.
2. Add US2: false-mandate-free template lint.
3. Add US1 + the required US6 transaction slice: complete scoped lint-to-consolidation with one finalization pass.
4. Add US5: structured index and manifest operations.
5. Complete the remainder of US6: standalone QMD hook and retryable finalization.
6. Add US3: applicability-aware creative lint.
7. Add US8: policy ownership and contradiction reporting.
8. Run Polish, wire QMD into OMP, and execute causal regression coverage for every listed open error.

### Notes

- Every implementation task uses `- [ ] T###`; `[P]` appears only where files and dependencies permit parallel execution.
- Story labels appear only in user-story phases and map directly to `spec.md` stories.
- No task creates redirect stubs, edits `wiki/index.md` with regex/line-number patches, or asks an agent to compose low-level hunk grammar.
