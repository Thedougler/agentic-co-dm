---

description: "Task list for Wiki Bulk Operations"
---

# Tasks: Wiki Bulk Operations

**Input**: Design documents from `/specs/023-wiki-bulk-ops/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/cli-contract.md, quickstart.md, constitution.md

**Tests**: Behavioral tests are included because the specification requires independently testable scenarios and the constitution requires public-seam tests for new behavior. Use stdlib `unittest`; keep the script's assert-based `__main__` self-check aligned with the public CLI behavior.

**Organization**: Tasks are grouped by user story so each story can be implemented and exercised as an independently testable increment.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Establish the executable script and behavioral-test locations required by the implementation plan.

- [X] T001 Create the executable CLI entrypoint with Python 3.14 shebang and stdlib-only imports in `scripts/wiki-bulk-ops`
- [X] T002 [P] Create the unittest module scaffold in `tests/test_wiki_bulk_ops.py`
- [X] T003 Add reusable temporary-vault fixture helpers for CLI behavior tests in `tests/test_wiki_bulk_ops.py`
---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Build shared parsing, scope, output, validation, and safe-write infrastructure before any operation-specific behavior.

**CRITICAL**: No user story implementation begins until this phase is complete.

- [X] T004 Implement vault resolution from `--vault`, then `OBSIDIAN_VAULT_PATH`, then `wiki/`, and reject a missing or non-directory vault with stderr diagnostics and exit code 1 in `scripts/wiki-bulk-ops`
- [X] T005 Implement shared scope traversal for `--glob`, `--directory`, and whole-vault defaults, excluding `.obsidian`, `_archive`, `_raw`, `_readouts`, `_meta`, `templates`, and `attachments`, in `scripts/wiki-bulk-ops`
- [X] T006 Implement UTF-8 reading with per-file skip records for decode failures, relative-path reporting, and partial-failure exit code 2 in `scripts/wiki-bulk-ops`
- [X] T007 Implement frontmatter fence extraction, flat top-level scalar parsing, YAML-key validation (`alphanumeric + underscore + hyphen`), and preservation of the `---` delimiters in `scripts/wiki-bulk-ops`
- [X] T008 Implement `Change`/`ChangeRecord`/`OperationResult` dataclasses and text/JSON summaries containing `files_scanned`, `files_modified`, `files_skipped`, `total_changes`, and per-file records in `scripts/wiki-bulk-ops`
- [X] T009 Implement per-file atomic writes through a same-directory temporary file followed by `os.replace`, honoring `--dry-run` so no file or rename is committed in `scripts/wiki-bulk-ops`
- [X] T010 Implement common argparse global options (`--vault`, `--dry-run`, `--json`, `--glob`, `--directory`) and distinct exit statuses 0, 1, and 2 in `scripts/wiki-bulk-ops`
- [X] T011 [P] Add foundational CLI invocation and output-shape tests for missing vaults, dry-run no-write behavior, JSON summaries, and partial UTF-8 failure handling in `tests/test_wiki_bulk_ops.py`

**Checkpoint**: Shared traversal, validation, atomicity, dry-run, and reporting are ready; user-story work can proceed in priority order.

---

## Phase 3: User Story 1 - Rename an Entity Across the Wiki (Priority: P1) 🎯 MVP

**Goal**: Rename exactly one entity page and update its structural references across the scoped vault without altering unrelated prose or markdown syntax.

**Independent Test**: In a temporary vault, rename a page referenced by bare, piped, embedded, and path-qualified wikilinks; verify the source filename and title change, display text remains unchanged, unrelated text is unchanged, YAML remains valid, collisions make zero changes, and substring entity names remain untouched.

### Tests for User Story 1

> Write these behavioral tests first and confirm they fail before the implementation tasks.

- [X] T012 [US1] Add failing rename behavior tests for source filename/title updates and exact `[[target]]`, `[[target|display]]`, `![[target]]`, and path-qualified rewrites in `tests/test_wiki_bulk_ops.py`
- [X] T013 [US1] Add failing rename safety tests for existing-destination collisions, zero-change-on-validation-error, exact matching that preserves `old-name-kin`, and body prose preservation in `tests/test_wiki_bulk_ops.py`

### Implementation for User Story 1

- [X] T014 [US1] Implement `rename` argument validation requiring exactly one existing `OLD_STEM.md`, rejecting an existing `NEW_STEM.md`, and reporting validation errors on stderr in `scripts/wiki-bulk-ops`
- [X] T015 [US1] Implement exact wikilink and embed target rewriting that preserves anchors, piped display text, and path prefixes while excluding body-text title mentions in `scripts/wiki-bulk-ops`
- [X] T016 [US1] Implement source-page frontmatter title mutation using `--old-title`/`--new-title` or the title-cased `--new` default, plus the source filename change record, in `scripts/wiki-bulk-ops`
- [X] T017 [US1] Integrate rename planning across all scoped markdown files with preflight collision validation, atomic apply, dry-run records, and zero writes on any validation error in `scripts/wiki-bulk-ops`
- [X] T018 [US1] Add rename idempotency and CLI acceptance coverage for repeated invocation, JSON line records, and exit code behavior in `tests/test_wiki_bulk_ops.py`

**Checkpoint**: User Story 1 is independently runnable and delivers the MVP entity-rename workflow.

---

## Phase 4: User Story 2 - Bulk Find-and-Replace with Markdown Safety (Priority: P1)

**Goal**: Replace literal or regex text in scoped body zones while protecting frontmatter and wikilink targets by default, with explicit opt-in zones.

**Independent Test**: In a temporary vault containing frontmatter, body text, callouts, embeds, and wikilinks, verify default replacement changes body occurrences only, opt-in flags change the requested zones, callout syntax remains intact, empty wikilinks are refused, and a second run reports zero changes.

### Tests for User Story 2

> Write these behavioral tests first and confirm they fail before the implementation tasks.

- [X] T019 [US2] Add failing replace tests for literal body-only substitution, occurrence/file summaries, preserved YAML and callout syntax, and unchanged wikilink targets in `tests/test_wiki_bulk_ops.py`
- [X] T020 [US2] Add failing replace safety tests for `--include-frontmatter`, `--include-links`, regex mode, empty-wikilink refusal, idempotency, and line-numbered change records in `tests/test_wiki_bulk_ops.py`

### Implementation for User Story 2

- [X] T021 [US2] Implement `replace` argument validation requiring non-empty search text and safe literal or Python-regex compilation in `scripts/wiki-bulk-ops`
- [X] T022 [US2] Implement frontmatter, wikilink-target, and body safety-zone splitting so replacements default to body text and require explicit `--include-frontmatter` or `--include-links` for protected zones in `scripts/wiki-bulk-ops`
- [X] T023 [US2] Implement replacement application with line-numbered `Change` records, preservation of Obsidian callouts/embeds/YAML delimiters, and refusal when any result would contain `[[]]` in `scripts/wiki-bulk-ops`
- [X] T024 [US2] Integrate replace scope traversal, dry-run/atomic apply, summary output, and idempotent no-change success in `scripts/wiki-bulk-ops`
- [X] T025 [US2] Add replace CLI acceptance coverage for glob/directory filtering and partial-failure reporting in `tests/test_wiki_bulk_ops.py`

**Checkpoint**: User Stories 1 and 2 independently support safe structural and body-text bulk operations.

---

## Phase 5: User Story 3 - Bulk Frontmatter Update (Priority: P2)

**Goal**: Set, rename, or remove a flat frontmatter field on files matching scope and optional repeated `key=value` filters without changing body content.

**Independent Test**: In a temporary vault with matching and non-matching `type: npc` pages, set a scalar field, rename an existing field while preserving its value, remove a field, and verify only matching frontmatter changes and the resulting YAML remains parseable.

### Tests for User Story 3

> Write these behavioral tests first and confirm they fail before the implementation tasks.

- [X] T026 [US3] Add failing frontmatter tests for filtered `set`, idempotent existing-value handling, non-matching-page preservation, and body-byte preservation in `tests/test_wiki_bulk_ops.py`
- [X] T027 [US3] Add failing frontmatter tests for `rename`, `remove`, repeated filters, invalid keys, missing action parameters, and YAML-preserving change records in `tests/test_wiki_bulk_ops.py`

### Implementation for User Story 3

- [X] T028 [US3] Implement `frontmatter` argument validation for `set`, `rename`, and `remove`, including required `--value`/`--new-field` parameters and valid YAML key names, in `scripts/wiki-bulk-ops`
- [X] T029 [US3] Implement frontmatter filter parsing for repeated `--filter KEY=VAL` predicates and matching against flat top-level values in `scripts/wiki-bulk-ops`
- [X] T030 [US3] Implement line-level frontmatter set/update, rename-with-value-preservation, and remove mutations without reformatting unrelated keys or body content in `scripts/wiki-bulk-ops`
- [X] T031 [US3] Integrate frontmatter validation, dry-run/atomic apply, idempotent no-op handling, and per-line `frontmatter` change records in `scripts/wiki-bulk-ops`
- [X] T032 [US3] Add frontmatter CLI acceptance coverage for directory/glob scope, JSON output, and partial UTF-8 failures in `tests/test_wiki_bulk_ops.py`

**Checkpoint**: User Story 3 independently performs filtered schema-level updates while preserving page bodies.

---

## Phase 6: User Story 4 - Dry Run and Diff Preview (Priority: P2)

**Goal**: Make every operation preview exact file/line/old/new/zone changes in machine-readable output without modifying disk.

**Independent Test**: Run each operation with `--dry-run --json` against a temporary vault, snapshot all files before and after, verify output records every planned change with file, line, old, new, and zone, then run live mode and compare changed-file and change counts.

### Tests for User Story 4

> Write these behavioral tests first and confirm they fail before the implementation tasks.
- [X] T033 [US4] Add failing cross-operation dry-run tests proving rename, replace, and frontmatter emit detailed JSON records and leave file bytes and filenames unchanged in `tests/test_wiki_bulk_ops.py`
- [X] T034 [US4] Add failing dry-run parity tests comparing preview and apply modified-file/change counts and verifying repeated live runs return zero changes in `tests/test_wiki_bulk_ops.py`

### Implementation for User Story 4

- [X] T035 [US4] Complete shared dry-run planning so rename filename changes and all content changes are represented with exact relative file paths, 1-indexed lines (filename line 0), old text, new text, and zones in `scripts/wiki-bulk-ops`
- [X] T036 [US4] Ensure all commands perform full validation and conflict detection before any write or rename, including staged-writes-compatible in-place maintenance and no creation outside the resolved vault in `scripts/wiki-bulk-ops`
- [X] T037 [US4] Add the script `__main__` assert-based self-check covering parser, safety-zone, idempotency, and dry-run invariants in `scripts/wiki-bulk-ops`

**Checkpoint**: Every operation has a reviewable, exact dry-run contract and parity with live execution.

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Verify the complete public seam and document the finished operational contract without adding new behavior.

- [X] T038 [P] Add executable permission and confirm the Python 3.14 stdlib-only shebang/import contract for `scripts/wiki-bulk-ops`
- [X] T039 [P] Run `python3 tests/test_wiki_bulk_ops.py` and the script self-check from `scripts/wiki-bulk-ops`; fix only failures attributable to this feature
- [X] T040 Run the quickstart scenarios from `specs/023-wiki-bulk-ops/quickstart.md` against temporary vault fixtures, including the bad-encoding partial-failure case
- [X] T041 Run `wiki-lint` validation after representative rename, replace, and frontmatter operations and record any feature-caused repair in the prescribed error ledger path
- [X] T042 Review `scripts/wiki-bulk-ops` output, stderr, exit codes, idempotency, atomicity, and `WIKI_STAGED_WRITES` behavior against `specs/023-wiki-bulk-ops/contracts/cli-contract.md` and `specs/023-wiki-bulk-ops/spec.md`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No feature dependencies; establish the two implementation surfaces.
- **Foundational (Phase 2)**: Depends on Setup and blocks all stories because every command shares traversal, parsing, reporting, validation, and atomic-write code.
- **User Story 1 (Phase 3)**: Depends on Foundational; MVP and first operation-specific slice.
- **User Story 2 (Phase 4)**: Depends on Foundational; can be implemented after shared infrastructure, but the same CLI script means a single writer should serialize it after US1.
- **User Story 3 (Phase 5)**: Depends on Foundational; can be implemented after shared infrastructure, but the same CLI script means a single writer should serialize it after US1/US2.
- **User Story 4 (Phase 6)**: Depends on the operation implementations because it verifies their shared dry-run parity; its shared improvements must remain compatible with all prior stories.
- **Polish (Phase 7)**: Depends on all desired stories and is the final verification pass.

### User Story Dependencies

- **US1 (P1)**: Foundational only; no dependency on another story.
- **US2 (P1)**: Foundational only at the contract level; consumes the same shared CLI infrastructure as US1 and should be integrated by the same script owner.
- **US3 (P2)**: Foundational only at the contract level; consumes the shared frontmatter parser and reporting model.
- **US4 (P2)**: Depends on US1–US3 for complete cross-operation preview coverage.

### Parallel Opportunities

- Phase 1: T002 can run independently of T001; T003 depends on the test-module scaffold, and quickstart scenarios remain the validation source exercised in Phase 7.
- Phase 2: T011 can be prepared in parallel with implementation of shared code, but must fail before the corresponding implementation is accepted; T004–T010 touch the same script and require one writer.
- Within each story: the two behavior-test tasks can be drafted together, then implementation tasks remain ordered because they modify the same script and shared test module.
- Across stories: after Foundational, independent test design for US1/US2/US3 can be parallelized in separate workspaces; implementation of the single script must remain serialized.
- Polish: T038 is independent of T040; T039–T042 are verification tasks and should run after implementation.

### Parallel Example: User Story 1

```text
# Separate workspace/test-author pass (before implementation):
Task: "Add rename behavior tests in tests/test_wiki_bulk_ops.py"
Task: "Add rename safety and collision tests in tests/test_wiki_bulk_ops.py"

# Then serialize the single-script implementation:
Task: "Implement rename validation, exact wikilink rewriting, title mutation, and atomic apply in scripts/wiki-bulk-ops"
```

### Parallel Example: User Story 2

```text
# Separate workspace/test-author pass (before implementation):
Task: "Add body-only and safety-zone tests in tests/test_wiki_bulk_ops.py"
Task: "Add opt-in link/frontmatter, regex, empty-link, and idempotency tests in tests/test_wiki_bulk_ops.py"

# Then serialize the single-script implementation:
Task: "Implement replace zones, validation, records, and atomic apply in scripts/wiki-bulk-ops"
```

### Parallel Example: User Story 3

```text
# Separate workspace/test-author pass (before implementation):
Task: "Add filtered set/idempotency tests in tests/test_wiki_bulk_ops.py"
Task: "Add rename/remove/filter validation tests in tests/test_wiki_bulk_ops.py"

# Then serialize the single-script implementation:
Task: "Implement frontmatter mutations and filtered atomic apply in scripts/wiki-bulk-ops"
```

### Parallel Example: User Story 4

```text
# Separate workspace/test-author pass:
Task: "Add cross-operation dry-run no-write tests in tests/test_wiki_bulk_ops.py"
Task: "Add dry-run/live parity and repeated-run tests in tests/test_wiki_bulk_ops.py"

# Then serialize the shared implementation:
Task: "Complete dry-run change records and preflight validation in scripts/wiki-bulk-ops"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1 Setup.
2. Complete Phase 2 Foundational prerequisites.
3. Write and fail T012–T013, then implement T014–T018.
4. Run the independent US1 tests plus a temporary-vault dry-run/apply scenario.
5. Stop at the US1 checkpoint for the smallest useful delivery: exact entity rename, collision safety, wikilink preservation, JSON summary, and idempotency.

### Incremental Delivery

1. Complete Setup + Foundational and verify shared CLI behavior.
2. Add US1 rename and validate independently.
3. Add US2 replace and validate independently without regressing US1.
4. Add US3 frontmatter mutation and validate independently.
5. Add US4 cross-operation dry-run parity and exact diff preview.
6. Run Polish checks and representative `wiki-lint` validation.

### Single-Writer Strategy

Because the plan intentionally uses one executable script and one behavioral test module, assign one implementation writer per shared workspace. Parallelize only isolated test design or documentation/verification work; do not merge concurrent edits to `scripts/wiki-bulk-ops` or `tests/test_wiki_bulk_ops.py` without reconciliation.

---

## Notes

- Every task uses the required `- [ ] T###` checklist form; `[P]` appears only on tasks that can be isolated without incomplete dependencies; `[US#]` appears only in user-story phases.
- Exact constraints from the data model are preserved in the relevant task descriptions, including scope exclusions, valid key syntax, idempotent zero-change behavior, and UTF-8 skip semantics.
- The implementation must remain stdlib-only, agent-shaped, atomic per file, markdown-safe, and compatible with `WIKI_STAGED_WRITES=true` as specified by the design artifacts.
