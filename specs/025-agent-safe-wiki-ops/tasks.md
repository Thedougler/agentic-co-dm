---

description: "Implementation tasks for agent-safe wiki lint, repair, and consolidation"
---

# Tasks: Agent-Safe Wiki Operations

**Input**: Design documents from `/specs/025-agent-safe-wiki-ops/`

**Prerequisites**: `plan.md`, `spec.md`, `research.md`, `data-model.md`, `contracts/`, and `quickstart.md`

**Testing**: Behavioral and causal regression tests are required by the feature specification and project constitution. Write each story's tests before its implementation and make them fail against the pre-change behavior.

**Organization**: User-story phases are ordered by priority, then by dependency within the P1 group so the identity and mutation seams exist before the end-to-end consolidation workflow.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Establish the project dependency, quality-tool configuration, and isolated fixtures used by every story.

- [X] T001 [P] Add the required Vale project dependency and supported Python metadata in `pyproject.toml`, preserving the existing `PyYAML` and Python `>=3.12` constraints.
- [X] T002 [P] Configure Vale scopes and active community packages in `.vale.ini`, including the repository's `styles/Deprecated/`, `styles/ai-tells/`, `styles/proselint/`, and `styles/write-good/` paths.
- [X] T003 [P] Add isolated wiki-operation fixture pages, malformed-index cases, redirect stubs, duplicate identities, and backlink/index/manifest fixtures under `tests/fixtures/wiki_ops/`.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Establish shared agent-shaped command behavior and reusable fixture/test seams before story implementation.

**CRITICAL**: User-story implementation depends on this phase's stable JSON, exit-code, and path-discovery conventions.

- [X] T004 Define shared environment/config discovery, compact JSON serialization, and exit-code conventions for `scripts/wiki-identity`, `scripts/wiki-lint`, and `scripts/wiki-bulk-ops`, using repository and vault defaults instead of requiring infrastructure paths from agents.
- [X] T005 [P] Export the shared wiki-operation library surface from `tools/wiki_ops/__init__.py` and preserve the existing `tools/wiki_ops/` module boundaries for identity, scope, mutations, transactions, index, manifest, and template contracts.
- [X] T006 Extend the isolated-vault subprocess helpers and observable-file assertions in `tests/test_wiki_ops.py` so every CLI story can assert JSON output, exit status, atomic file state, and silent maintenance behavior without touching the live vault.

**Checkpoint**: Shared command conventions and fixture seams are ready; user stories can proceed according to the dependency graph below.

---

## Phase 3: User Story 7 - Identity Resolution Before Work Ordering (Priority: P1)

**Goal**: Resolve page identity before repair ordering, classify candidates as `resolved`, `ambiguous`, or `distinct`, and block unsafe work when candidates are ambiguous.

**Independent Test**: Present two same-type pages with different filenames and overlapping identity signals; `scripts/wiki-identity scan` and `resolve` return `ambiguous` with both candidates and a repair queue refuses automatic mutation. A no-frontmatter raw page is `distinct`, not an error.

### Tests for User Story 7

- [X] T007 [US7] Add failing identity-resolution and regression tests in `tests/test_wiki_ops.py` for title/alias/type matching, shared manifest provenance, QMD similarity, deterministic ordering, no-frontmatter `distinct`, `resolved` canonical pages, ambiguous candidate reporting, and causal coverage for identity-ordering errors e-10 and e-12.

### Implementation for User Story 7

- [X] T008 [P] [US7] Populate duplicate, distinct, and raw-drop identity fixtures under `tests/fixtures/wiki_ops/` with same-type candidates, different-type near matches, aliases, merge history, and manifest provenance.
- [X] T009 [US7] Implement `PageIdentity`, signal extraction, QMD similarity integration, and `resolved`/`ambiguous`/`distinct` classification in `tools/wiki_ops/identity.py`; enforce that `status: ambiguous` requires non-empty `candidates`, every `candidates[].path` references an existing vault file, and `signals.qmd_content_similarity` stays in `0.0–1.0`.
- [X] T010 [US7] Implement `resolve` and `scan` JSON CLI commands, scope handling, and exit codes in `scripts/wiki-identity` using the identity contract's `0 = resolved/no ambiguities`, `1 = error`, and `2 = ambiguous` meanings.
- [X] T011 [US7] Gate automatic repair and consolidation queueing on identity status in `tools/wiki_ops/identity.py`, `tools/wiki_ops/mutations.py`, and `tools/wiki_ops/transactions.py`; exclude legacy `redirects_to` pages from valid identity routing and return an actionable `identity_ambiguous` rejection.

**Checkpoint**: Identity is resolved before ordering or mutation, and ambiguity is an explicit safe stop.

---

## Phase 4: User Story 4 - Typed Mutation Operations (Priority: P1)

**Goal**: Replace line-number patches and regex edits with semantic, preconditioned, atomic mutation operations.

**Independent Test**: Replace a section by heading path with a matching SHA-256 content hash, then repeat with a stale hash; the first operation applies atomically and the second returns `hash_mismatch` with the original file unchanged. Overlapping transaction mutations are rejected before any write.

### Tests for User Story 4

- [X] T012 [US4] Add failing mutation tests in `tests/test_wiki_ops.py` for every required operation kind (`replace_section`, `delete_section`, `insert_section`, `set_frontmatter`, `remove_frontmatter`, `rename_or_merge_page`, `replace_index_entry`, `update_manifest_identity`, and `rewrite_links`), semantic selector errors, stale hashes, invalid invariants, overlap rejection, atomic rollback, and causal coverage for e-21 and e-23.

### Implementation for User Story 4

- [X] T013 [US4] Implement `MutationOp`, heading-path section parsing, SHA-256 `section_hash`, selector resolution, precondition validation, invariant checks, and atomic application in `tools/wiki_ops/mutations.py`; leave the original file untouched for every rejection.
- [X] T014 [US4] Add `mutate` subcommands, `--dry-run`, compact JSON output, actionable error fields, and exit codes to `scripts/wiki-bulk-ops` according to `contracts/mutation-contract.md`.
- [X] T015 [P] [US4] Implement structured index and manifest mutation primitives in `tools/wiki_ops/index_ops.py` and `tools/wiki_ops/manifest_ops.py`, including malformed-index detection, sorted entry operations, and page-level `merged_into`, `renamed_to`, and `archived` transitions without overwriting source provenance.
- [X] T016 [US4] Implement `rename_or_merge_page` in `tools/wiki_ops/mutations.py` to update the canonical page, deterministic backlinks, index, and manifest in one operation, remove the obsolete page, and never create a `redirects_to` redirect stub.

**Checkpoint**: Typed mutations provide semantic selectors, safe preconditions, atomic writes, dry runs, and no redirect-stub creation.

---

## Phase 5: User Story 2 - Template Conformance Without False Mandates (Priority: P1)

**Goal**: Enforce explicit template contracts while respecting optional and lifecycle-conditional sections, allowed callouts, and deprecated guidance ownership.

**Independent Test**: Lint a dormant faction that omits active-only and optional sections; no false-mandatory findings appear, while missing genuinely required sections and disallowed callouts produce exactly the contract findings.

### Tests for User Story 2

- [X] T017 [US2] Add failing template-conformance tests in `tests/test_wiki_ops.py` for optional omission, lifecycle `active`/`dormant`/`dissolved` behavior, required frontmatter, allowed callouts, root-cause versus downstream deprecated-pattern severity, redirect-stub detection, and causal coverage for e-13, e-14, e-20, and e-24 through e-38 template instances.

### Implementation for User Story 2

- [X] T018 [P] [US2] Add machine-readable YAML contracts under `wiki/templates/contracts/`, one per existing `wiki/templates/*.md` type, with explicit `required`, `optional`, `repeatable`, `when`, `parent`, allowed-callout, and required/optional-frontmatter semantics; include the faction contract's lifecycle rules from `data-model.md`.
- [X] T019 [US2] Implement contract loading, lifecycle requirement resolution, section/callout/frontmatter conformance, and contract-version handling in `tools/wiki_ops/template_contracts.py`; fall back to the existing template profile when no explicit contract exists.
- [X] T020 [US2] Extend `tools/lint_wiki.py` and `scripts/wiki-lint` to run template conformance by default, emit `TMPL_*` findings, classify `redirects_to` pages as deterministic deletion repairs, and distinguish critical source guidance from downstream inherited output.

**Checkpoint**: Template lint reports only real violations, not optional or lifecycle-exempt omissions, and redirect stubs are errors rather than routing mechanisms.

---

## Phase 6: User Story 1 - Scoped Faction Lint and Consolidation (Priority: P1) 🎯 MVP

**Goal**: Deliver the end-to-end faction workflow: identity check, scoped lint, compact repair plan, atomic typed repairs, structured consolidation, and one final maintenance pass.

**Independent Test**: Run the identity → scoped lint → repair plan → transaction workflow against the faction fixtures; ambiguity blocks work, scope excludes unrelated files and cross-scope link validation, deterministic findings become typed actions, embeds are reported, and a two-page merge updates backlinks/index/manifest without a redirect stub.

### Tests for User Story 1

- [X] T021 [US1] Add failing end-to-end workflow tests in `tests/test_wiki_ops.py` for ambiguous identity blocking, directory/type/file scopes, compact grouped output, silent cross-scope link skipping, broken embed/image findings, deterministic plan generation and hashing, two-page consolidation, and causal coverage for e-12 through e-19 and e-22.

### Implementation for User Story 1

- [X] T022 [US1] Implement the typed `Scope` object and resolution for `files`, `directory`, `entity_type`, `identity_set`, `changed`, and `bundle` in `tools/wiki_ops/scope.py`, including `resolved_files` materialization and SKIP_DIRS behavior.
- [X] T023 [US1] Extend `tools/lint_wiki.py` and `scripts/wiki-lint` with `--scope`, `--no-template`, `--no-vale`, `--plan`, and `--from`, filtering before checks and returning compact scope/files/counts/findings-by-file JSON while treating out-of-scope links as valid during scoped runs.
- [X] T024 [US1] Add broken embed/image detection, repair-class assignment, deterministic typed action factories, and `RepairPlan` serialization/hash validation in `tools/lint_wiki.py` and `tools/wiki_ops/mutations.py`; include only deterministic repairs in plans and preserve diagnostic/human-only findings.
- [X] T025 [US1] Wire `scripts/wiki-identity`, `scripts/wiki-lint`, and `scripts/wiki-bulk-ops` into the documented end-to-end pipeline from `contracts/transaction-contract.md`, including canonical environment discovery, explicit exit meanings, and actionable ambiguity/precondition errors.

**Checkpoint**: The P1 acceptance workflow is runnable with repository commands only and does not require line patches, regex index edits, or manual manifest rewrites.

---

## Phase 7: User Story 3 - Creative Lint With Applicability Awareness (Priority: P2)

**Goal**: Apply creative heuristics only to applicable narrative surfaces, exempt structural/transient content, and prevent unproven rules from producing ERROR findings.

**Independent Test**: SCENE001 produces no finding for a redirect stub or a faction with explicit pressure, and a rule with no positive fixture remains SHADOW or WARN.

### Tests for User Story 3

- [X] T026 [US3] Add failing applicability and precision tests in `tests/test_creative_lint.py` and `tests/test_wiki_ops.py` for redirects, explicit pressure, narrative-only surfaces, metadata/scaffold/table exemptions, transient transaction state, positive/negative fixtures, and causal coverage for e-15 and its e-24 through e-38 creative-lint instances.

### Implementation for User Story 3

- [X] T027 [P] [US3] Extend rule applicability, structural scopes, exemptions, fixture metadata, and severity promotion rules in `tools/creative_lint/registry.py`, `tools/creative_lint/engine.py`, `tools/creative_lint/findings.py`, and `tools/creative_lint/template_profile.py`.
- [X] T028 [US3] Update `rules/registry.yml`, `rules/bundles.yml`, and applicable `rules/{candidates,shadow}/` entries so SCENE001 and other creative rules declare applicability and cannot emit ERROR/WARN without positive fixtures.
- [X] T029 [US3] Implement `tools/wiki_ops/vale_adapter.py` to parse Vale JSON, prefix rule IDs with `VALE_`, map severity and guidance into the unified finding schema, and create `delete_section` or `replace_section` typed repair actions for every Vale finding.
- [X] T030 [US3] Make `tools/lint_wiki.py` and `scripts/wiki-lint` pass page state and structural applicability into the creative engine without classifying transient pages as orphan/index omissions.

**Checkpoint**: Creative lint is applicability-aware, fixture-gated, and quiet on known false-positive surfaces.

---

## Phase 8: User Story 5 - Index and Manifest as Structured State (Priority: P2)

**Goal**: Make index and manifest updates deterministic typed operations rather than raw-file regex or manual provenance edits.

**Independent Test**: Apply a page merge and verify the old index entry is replaced, the canonical entry remains valid, and `.manifest.json` records a page-level identity transition independently of source-ingest provenance; malformed index input fails without mutation.

### Tests for User Story 5

- [X] T031 [US5] Add failing structured-state tests in `tests/test_wiki_ops.py` for replace/remove/insert-by-slug index operations, malformed-index rejection, atomic writes, manifest transition records, preserved `pages_produced`, and causal coverage for e-16 and e-17.

### Implementation for User Story 5

- [X] T032 [US5] Complete `tools/wiki_ops/index_ops.py` as the sole structured parser/writer for `wiki/index.md`, operating on `- [[slug]] — description` entries and refusing malformed input instead of appending or regex-editing the 107KB document.
- [X] T033 [US5] Extend `scripts/manifest.py` and `tools/wiki_ops/manifest_ops.py` with page-level identity transition CRUD, JSON validation, and `merged_into`/`renamed_to`/`archived` serialization that leaves source-ingest provenance intact.

**Checkpoint**: Index and manifest state can only be changed through typed operations with atomic failure behavior.

---

## Phase 9: User Story 6 - Batched Finalization at Transaction Boundaries (Priority: P2)

**Goal**: Validate and commit a complete mutation set before running derived maintenance exactly once.

**Independent Test**: Apply a three-file transaction with a wrapped QMD command; index and manifest maintenance run once when applicable, QMD runs once after commit, output is compact, and any validation failure leaves every file unchanged.

### Tests for User Story 6

- [X] T034 [US6] Add failing transaction tests in `tests/test_wiki_ops.py` for validate/commit/finalize lifecycle states, overlap and stale-plan rejection, rollback after write failure, one QMD invocation for three mutations, compact finalization output, silent success/no-op behavior, and causal coverage for e-19.

### Implementation for User Story 6

- [X] T035 [US6] Implement validation, in-memory resolution, overlap detection, backup/restore, commit status, and single-pass finalization in `tools/wiki_ops/transactions.py`, preserving `pending` → `committed` → `finalized` and failure states from `data-model.md`.
- [X] T036 [US6] Add `transact --plan-file [--approve]` to `scripts/wiki-bulk-ops`, including preview diffs, plan-hash and mutation-precondition checks, compact `files_changed`/`mutations`/`finalization` JSON, and exit codes `0`, `1`, and `2` from `contracts/transaction-contract.md`.
- [X] T037 [US6] Complete standalone serialized QMD maintenance in `scripts/qmd-hook.sh`: run `qmd update` plus one count-bounded embedding pass, emit zero output on success, return one actionable stderr line on failure, return silent success when QMD is absent, and return deterministic `busy` behavior for concurrent callers.

**Checkpoint**: A transaction is the only finalization boundary; derived maintenance is deferred and never repeated per intermediate file.

---

## Phase 10: User Story 8 - Policy Single-Ownership (Priority: P2)

**Goal**: Give each policy one authoritative owner and detect contradictory lower-level restatements before agents act on them.

**Independent Test**: Add a lower-level policy sentence that semantically contradicts its owner; the policy-conflict check reports both locations and the consumer can instead reference the authoritative owner.

### Tests for User Story 8

- [X] T038 [US8] Add failing ownership and contradiction tests in `tests/test_policy_conflicts.py` for acceptance semantics, callout vocabulary, template optionality, owner/consumer reporting, and causal coverage for e-20.

### Implementation for User Story 8

- [X] T039 [US8] Create `docs/agents/policy-owners.yml` with one owner, governed decision, and consumer list for each cross-cutting policy, including acceptance semantics owned by `docs/agents/work.md`.
- [X] T040 [US8] Extend `scripts/check-policy-conflicts` and update `.agents/skills/faction-design/SKILL.md`, `.agents/skills/wiki-ingest/SKILL.md`, and related consumer guidance to reference `docs/agents/policy-owners.yml` instead of restating policy semantics.

**Checkpoint**: Conflicting policy text is surfaced with both paths, and lower-level skills point to one authority.

---

## Phase 11: Polish & Cross-Cutting Concerns

**Purpose**: Complete Vale rules, harness integration, documentation, and full feature verification without changing story semantics.

- [X] T041 [P] Add the deprecated `DM Thesis` Vale rule and agent-facing guidance in `styles/Deprecated/DMThesis.yml`, plus the configured AI-tells, write-good, and proselint package declarations needed by `.vale.ini`.
- [X] T042 [P] Wire `scripts/qmd-hook.sh` into every successful OMP wiki-write boundary in `.omp/config.yml`, `.omp/RULES.md`, and `OMP.md`, keeping the hook standalone rather than turning it into a git hook.
- [X] T043 [P] Update `docs/cli.md`, `docs/architecture.md`, and relevant feature contracts with the final command surfaces, scope syntax, mutation/transaction exit codes, QMD silent-success behavior, and canonical policy ownership links.
- [X] T044 Run every validation scenario in `specs/025-agent-safe-wiki-ops/quickstart.md`, including `tests/test_wiki_ops.py`, `tests/test_creative_lint.py`, `tests/test_policy_conflicts.py`, Vale JSON output, malformed-index rejection, and the full causal regression set for e-10 and e-12 through e-38.
- [X] T045 Run the repository's targeted baseline checks after the feature scenarios, including `scripts/check-omp-baseline.sh` and `python3 tools/check_readme_sync.py`, and record any actionable runtime failure in `errors.md` before completion.

- [X] T046 Add 1-based source line numbers to default structural, template, and Vale lint findings, preserve them in `findings_by_file`, emit only actual findings or `status: "clean"`, add `--verbose` for the full zero-count matrix, and add CLI regression coverage.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: T001–T003 have no feature dependencies and can run in parallel.
- **Foundational (Phase 2)**: T004–T006 depend on Setup and block story work.
- **P1 identity and mutation**: US7 and the primitive portions of US4 can proceed in parallel after Foundation; US4's identity gate consumes US7's result.
- **P1 template conformance**: US2 can proceed after Foundation and is independent of the mutation implementation.
- **P1 end-to-end workflow**: US1 completes after US7, US4, and US2; its transaction path also consumes the finalization seam from US6.
- **P2 creative lint**: US3 can proceed after Foundation and integrates with the existing creative-lint engine.
- **P2 structured state**: US5 depends on the typed mutation seam from US4 but can be developed independently of US3.
- **P2 finalization**: US6 depends on US4 and US5 so it can finalize their mutation types.
- **P2 policy ownership**: US8 is independent after Foundation.
- **Polish**: T041–T045 depend on the desired story implementations and targeted story checks.

### User Story Completion Order

```text
Foundation
├── US7 Identity Resolution ──┐
├── US4 Typed Mutations ──────┼──> US1 Scoped Faction Workflow (MVP)
├── US2 Template Contracts ────┘          │
├── US3 Creative Lint                    │
├── US5 Structured State ───────> US6 Batched Finalization ──┘
└── US8 Policy Ownership
```

### Parallel Opportunities

- **Setup**: T001, T002, and T003 touch separate files and can run together.
- **Foundation**: T005 and T006 can run in parallel after the shared CLI convention in T004 is agreed.
- **P1 stories**: US7, US2, and the non-gated mutation implementation in US4 can be staffed in parallel after Foundation.
- **US4**: T015's index and manifest modules can run in parallel because they own separate files.
- **Polish**: T041, T042, and T043 touch separate surfaces and can run in parallel; T044/T045 run last.

---

## Parallel Example: P1 Enablement and MVP

```text
After Phase 2:
- Identity owner: T007–T011 in tools/wiki_ops/identity.py and scripts/wiki-identity
- Mutation owner: T012–T016 in tools/wiki_ops/mutations.py, index_ops.py, manifest_ops.py, and scripts/wiki-bulk-ops
- Template owner: T017–T020 in wiki/templates/contracts/, tools/wiki_ops/template_contracts.py, and tools/lint_wiki.py

After US7 + US4 + US2:
- MVP integration owner: T021–T025 in tools/wiki_ops/scope.py, tools/lint_wiki.py, scripts/wiki-lint, and scripts/wiki-bulk-ops
```

## Implementation Strategy

### MVP First

1. Complete Phase 1 and Phase 2.
2. Complete the P1 enablement slices US7, US4, and US2 in dependency order or parallel by file ownership.
3. Complete the US5 structured-state and US6 transaction-finalization seams required by the end-to-end workflow.
4. Complete US1's identity → scoped lint → typed plan → atomic consolidation path.
5. Run US1's independent fixture workflow and stop at the MVP checkpoint.

### Incremental Delivery

1. Add US3 creative-lint applicability without changing structural lint behavior.
2. Add US5 structured index/manifest state and verify merge provenance.
3. Add US6 transaction finalization and the standalone QMD hook.
4. Add US8 policy ownership and contradiction detection.
5. Finish Vale, OMP, documentation, and full causal regression checks.

### Notes

- `[P]` means the task owns a different file set and has no dependency on an incomplete task.
- `[US#]` maps each task to the user story it serves; Setup, Foundational, and Polish tasks intentionally have no story label.
- Tests are behavioral and public-seam focused; they must not assert implementation details or source text.
- No task creates a redirect stub or treats `redirects_to` as valid identity routing.
