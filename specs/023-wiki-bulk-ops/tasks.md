# Tasks: Wiki Bulk Operations

**Input**: Design documents from `/specs/023-wiki-bulk-ops/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/cli-contract.md, quickstart.md, constitution.md

**Tests**: Behavioral tests are included because the specification requires independently testable scenarios and the constitution requires public-seam tests for new behavior. Use stdlib `unittest`; keep the script's assert-based `__main__` self-check aligned with the public CLI behavior.

**Organization**: Tasks are grouped by user story so each story can be implemented and exercised as an independently testable increment.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Establish the executable script and behavioral-test locations required by the implementation plan.

- [x] T001 Create the executable CLI entrypoint with Python 3.14 shebang and stdlib-only imports in `scripts/wiki-bulk-ops`
- [x] T002 [P] Create the unittest module scaffold in `tests/test_wiki_bulk_ops.py`
- [x] T003 Add reusable temporary-vault fixture helpers for CLI behavior tests in `tests/test_wiki_bulk_ops.py`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Build shared parsing, scope, output, validation, and safe-write infrastructure before any operation-specific behavior.

**⚠️ CRITICAL**: No user story implementation begins until this phase is complete.

- [x] T004 Implement vault resolution from `--vault`, then `OBSIDIAN_VAULT_PATH`, then `wiki/`, and reject a missing or non-directory vault with stderr diagnostics and exit code 1 in `scripts/wiki-bulk-ops`
- [x] T005 Implement shared scope traversal for `--glob`, `--directory`, and whole-vault defaults, excluding `.obsidian`, `_archive`, `_raw`, `_readouts`, `_meta`, `templates`, and `attachments`, in `scripts/wiki-bulk-ops`
- [x] T006 Implement UTF-8 reading with per-file skip records for decode failures, relative-path reporting, and partial-failure exit code 2 in `scripts/wiki-bulk-ops`
- [x] T007 Implement frontmatter fence extraction, flat top-level scalar parsing, YAML-key validation (`alphanumeric + underscore + hyphen`), and preservation of the `---` delimiters in `scripts/wiki-bulk-ops`
- [x] T008 Implement `Change`/`ChangeRecord`/`OperationResult` dataclasses and text/JSON summaries containing `files_scanned`, `files_modified`, `files_skipped`, `total_changes`, and per-file records in `scripts/wiki-bulk-ops`
- [x] T009 Implement per-file atomic writes through a same-directory temporary file followed by `os.replace`, honoring `--dry-run` so no file or rename is committed in `scripts/wiki-bulk-ops`
- [x] T010 Implement common argparse global options (`--vault`, `--dry-run`, `--json`, `--glob`, `--directory`) and distinct exit statuses 0, 1, and 2 in `scripts/wiki-bulk-ops`
- [x] T011 [P] Add foundational CLI invocation and output-shape tests for missing vaults, dry-run no-write behavior, JSON summaries, and partial UTF-8 failure handling in `tests/test_wiki_bulk_ops.py`

**Checkpoint**: Shared traversal, validation, atomicity, dry-run, and reporting are ready; user-story work can proceed in priority order.

---

## Phase 3: User Story 1 — Rename an Entity Across the Wiki (Priority: P1) 🎯 MVP

**Goal**: Rename exactly one entity page and update its structural references across the scoped vault without altering unrelated prose or markdown syntax.

**Independent Test**: In a temporary vault, rename a page referenced by bare, piped, embedded, and path-qualified wikilinks; verify the source filename and title change, display text remains unchanged, unrelated text is unchanged, YAML remains valid, collisions make zero changes, and substring entity names remain untouched.

### Tests for User Story 1

- [x] T012 [US1] Add failing rename behavior tests for source filename/title updates and exact `[[target]]`, `[[target|display]]`, `![[target]]`, and path-qualified rewrites in `tests/test_wiki_bulk_ops.py`
- [x] T013 [US1] Add failing rename safety tests for existing-destination collisions, zero-change-on-validation-error, exact matching that preserves `old-name-kin`, and body prose preservation in `tests/test_wiki_bulk_ops.py`

### Implementation for User Story 1

- [x] T014 [US1] Implement `rename` argument validation requiring exactly one existing `OLD_STEM.md`, rejecting an existing `NEW_STEM.md`, and reporting validation errors on stderr in `scripts/wiki-bulk-ops`
- [x] T015 [US1] Implement exact wikilink and embed target rewriting that preserves anchors, piped display text, and path prefixes while excluding body-text title mentions in `scripts/wiki-bulk-ops`
- [x] T016 [US1] Implement source-page frontmatter title mutation using `--old-title`/`--new-title` or the title-cased `--new` default, plus the source filename change record, in `scripts/wiki-bulk-ops`
- [x] T017 [US1] Integrate rename planning across all scoped markdown files with preflight collision validation, atomic apply, dry-run records, and zero writes on any validation error in `scripts/wiki-bulk-ops`
- [x] T018 [US1] Add rename idempotency and CLI acceptance coverage for repeated invocation, JSON line records, and exit code behavior in `tests/test_wiki_bulk_ops.py`

**Checkpoint**: User Story 1 is independently runnable and delivers the MVP entity-rename workflow.

---

## Phase 4: User Story 2 — Bulk Find-and-Replace with Markdown Safety (Priority: P1)

**Goal**: Replace literal or regex text in scoped body zones while protecting frontmatter and wikilink targets by default, with explicit opt-in zones.

**Independent Test**: In a temporary vault containing frontmatter, body text, callouts, embeds, and wikilinks, verify default replacement changes body occurrences only, opt-in flags change the requested zones, callout syntax remains intact, empty wikilinks are refused, and a second run reports zero changes.

### Tests for User Story 2

- [x] T019 [US2] Add failing replace tests for literal body-only substitution, occurrence/file summaries, preserved YAML and callout syntax, and unchanged wikilink targets in `tests/test_wiki_bulk_ops.py`
- [x] T020 [US2] Add failing replace safety tests for `--include-frontmatter`, `--include-links`, regex mode, empty-wikilink refusal, idempotency, and line-numbered change records in `tests/test_wiki_bulk_ops.py`

### Implementation for User Story 2

- [x] T021 [US2] Implement `replace` argument validation requiring non-empty search text and safe literal or Python-regex compilation in `scripts/wiki-bulk-ops`
- [x] T022 [US2] Implement frontmatter, wikilink-target, and body safety-zone splitting so replacements default to body text and require explicit `--include-frontmatter` or `--include-links` for protected zones in `scripts/wiki-bulk-ops`
- [x] T023 [US2] Implement replacement application with line-numbered `Change` records, preservation of Obsidian callouts/embeds/YAML delimiters, and refusal when any result would contain `[[]]` in `scripts/wiki-bulk-ops`
- [x] T024 [US2] Integrate replace scope traversal, dry-run/atomic apply, summary output, and idempotent no-change success in `scripts/wiki-bulk-ops`
- [x] T025 [US2] Add replace CLI acceptance coverage for glob/directory filtering and partial-failure reporting in `tests/test_wiki_bulk_ops.py`

**Checkpoint**: User Stories 1 and 2 independently support safe structural and body-text bulk operations.

---

## Phase 5: User Story 4 — Broken Link Repair (Priority: P1)

**Goal**: Detect broken wikilinks and auto-resolve via three-tier strategy: explicit old→new TSV mapping, git rename history, frontmatter aliases, and fuzzy stem matching. Ambiguous multi-candidate matches are reported with candidates, not auto-resolved. Unresolvable links are reported and left unchanged.

**Independent Test**: In a temporary vault, introduce known broken links (renamed pages, alias matches, fuzzy-distance-1 stems, ambiguous stems, truly dead links). Run repair. Verify: resolved links point to existing pages, ambiguous links reported with candidates but unchanged, unresolvable links reported and unchanged, no valid links altered, frontmatter/markdown structure preserved.

### Tests for User Story 4

> Write these behavioral tests first and confirm they fail before the implementation tasks.

- [x] T026 [US4] Add failing link-repair tests for: explicit TSV mapping resolves broken links; git-detected renames resolve links; frontmatter `aliases` field resolves links; single-candidate fuzzy match (Levenshtein ≤ threshold) resolves; multi-candidate fuzzy match reports candidates without resolving; unresolvable links reported unchanged — all in `tests/test_wiki_bulk_ops.py`
- [x] T027 [US4] Add failing link-repair safety tests for: `--no-git`/`--no-aliases`/`--no-fuzzy` flags disable respective tiers; `--fuzzy-threshold` value 1-5 controls match distance (reject outside range with exit 1); malformed TSV lines skipped with warning; piped wikilink targets `[[broken|display]]` updated while display preserved; idempotent re-run produces `files_modified: 0` — in `tests/test_wiki_bulk_ops.py`

### Implementation for User Story 4

- [x] T028 [US4] Add `link-repair` subparser to argparse with `--mapping FILE`, `--no-git`, `--no-aliases`, `--no-fuzzy`, `--fuzzy-threshold N` (default 2, validate 1-5) and wire to handler in `scripts/wiki-bulk-ops`
- [x] T029 [US4] Implement broken link detection: scan all scoped `.md` files for wikilink targets via existing `LINK_RE`; build set of existing page stems from vault; identify links where target stem has no matching `.md` file in `scripts/wiki-bulk-ops`
- [x] T030 [US4] Implement resolution tier 1 — explicit mapping: parse TSV file (`old_stem<tab>new_stem`, `#` comment lines, skip lines with wrong column count with stderr warning) per research.md Decision 10 in `scripts/wiki-bulk-ops`
- [x] T031 [US4] Implement resolution tier 2 — git rename history: run `git log --all --diff-filter=R --summary --name-status` in vault directory; parse renamed `.md` file paths; build old_stem→new_stem mapping (only for stems that currently exist) in `scripts/wiki-bulk-ops`
- [x] T032 [US4] Implement resolution tier 3 — frontmatter aliases: scan all vault pages for `aliases:` frontmatter field (inline YAML list); build alias_stem→canonical_stem mapping in `scripts/wiki-bulk-ops`
- [x] T033 [US4] Implement resolution tier 4 — fuzzy stem matching: Levenshtein edit distance function (stdlib-only, ~20 lines); for each unresolved broken link, find existing stems within `--fuzzy-threshold` edits; single-candidate → auto-resolve; multi-candidate → report with candidates list, do not resolve per FR-014 in `scripts/wiki-bulk-ops`
- [x] T034 [US4] Implement resolution application: for each resolved broken link, rewrite wikilink target using existing `LINK_RE` patterns (reuse rename rewrite logic from T015); preserve anchors, display text, embeds; produce zone-labeled `Change` records in `scripts/wiki-bulk-ops`
- [x] T035 [US4] Wire link-repair into dry-run/atomic-apply pipeline, JSON/text output with resolution source annotation (mapping/git/alias/fuzzy/ambiguous/unresolved), and idempotent re-run behavior in `scripts/wiki-bulk-ops`
- [x] T036 [US4] Add link-repair CLI acceptance tests for dry-run parity, `--json` output shape, glob/directory scoping, and partial-failure on bad-encoding files in `tests/test_wiki_bulk_ops.py`

**Checkpoint**: `scripts/wiki-bulk-ops link-repair --vault wiki` detects and repairs broken links through all four resolution tiers with dry-run, JSON output, and idempotency.

---

## Phase 6: User Story 3 — Bulk Frontmatter Update (Priority: P2)

**Goal**: Set, rename, or remove a flat frontmatter field on files matching scope and optional repeated `key=value` filters without changing body content.

**Independent Test**: In a temporary vault with matching and non-matching `type: npc` pages, set a scalar field, rename an existing field while preserving its value, remove a field, and verify only matching frontmatter changes and the resulting YAML remains parseable.

### Tests for User Story 3

- [x] T037 [US3] Add failing frontmatter tests for filtered `set`, idempotent existing-value handling, non-matching-page preservation, and body-byte preservation in `tests/test_wiki_bulk_ops.py`
- [x] T038 [US3] Add failing frontmatter tests for `rename`, `remove`, repeated filters, invalid keys, missing action parameters, and YAML-preserving change records in `tests/test_wiki_bulk_ops.py`

### Implementation for User Story 3

- [x] T039 [US3] Implement `frontmatter` argument validation for `set`, `rename`, and `remove`, including required `--value`/`--new-field` parameters and valid YAML key names, in `scripts/wiki-bulk-ops`
- [x] T040 [US3] Implement frontmatter filter parsing for repeated `--filter KEY=VAL` predicates and matching against flat top-level values in `scripts/wiki-bulk-ops`
- [x] T041 [US3] Implement line-level frontmatter set/update, rename-with-value-preservation, and remove mutations without reformatting unrelated keys or body content in `scripts/wiki-bulk-ops`
- [x] T042 [US3] Integrate frontmatter validation, dry-run/atomic apply, idempotent no-op handling, and per-line `frontmatter` change records in `scripts/wiki-bulk-ops`
- [x] T043 [US3] Add frontmatter CLI acceptance coverage for directory/glob scope, JSON output, and partial UTF-8 failures in `tests/test_wiki_bulk_ops.py`

**Checkpoint**: User Story 3 independently performs filtered schema-level updates while preserving page bodies.

---

## Phase 7: User Story 5 — Bulk Tag Normalization (Priority: P2)

**Goal**: Canonicalize frontmatter tags against `_meta/taxonomy.md`, merge aliases, collapse post-normalization duplicates, and report unknown tags without removing them (unless `--remove-unknown`).

**Independent Test**: In a temporary vault with variant tag spellings and a taxonomy file defining canonical tags and aliases, run normalization. Verify all alias tags replaced with canonical form, duplicates collapsed, unknown tags reported but not removed, body content unchanged, YAML valid.

### Tests for User Story 5

> Write these behavioral tests first and confirm they fail before the implementation tasks.

- [x] T044 [US5] Add failing tag-normalize tests for: alias tags replaced with canonical form; duplicate tags collapsed after normalization; unknown tags reported but NOT removed; body content unchanged; YAML remains valid — in `tests/test_wiki_bulk_ops.py`
- [x] T045 [US5] Add failing tag-normalize safety tests for: `--remove-unknown` flag removes unknown tags; `--taxonomy FILE` overrides default `_meta/taxonomy.md` path; taxonomy file must exist (exit 1 if missing); idempotent re-run produces `files_modified: 0`; glob/directory scoping — in `tests/test_wiki_bulk_ops.py`

### Implementation for User Story 5

- [x] T046 [US5] Add `tag-normalize` subparser to argparse with `--taxonomy FILE` (default `_meta/taxonomy.md` in vault) and `--remove-unknown` flag; validate taxonomy file exists (exit 1 if not) in `scripts/wiki-bulk-ops`
- [x] T047 [US5] Implement taxonomy parser: read taxonomy file; extract canonical tags and aliases from heading/list-item format per research.md Decision 11; build bidirectional alias→canonical mapping in `scripts/wiki-bulk-ops`
- [x] T048 [US5] Implement tag normalization logic: for each scoped file, parse frontmatter `tags:` field (inline YAML list `[a, b]` or block list `- a\n- b`); replace alias tags with canonical form; collapse duplicates; collect unknown tags; remove unknowns only if `--remove-unknown` per FR-015 in `scripts/wiki-bulk-ops`
- [x] T049 [US5] Wire tag-normalize into dry-run/atomic-apply pipeline with `Change` records (zone `frontmatter`), summary reporting unknown tags separately, and idempotent re-run behavior in `scripts/wiki-bulk-ops`
- [x] T050 [US5] Add tag-normalize CLI acceptance tests for dry-run parity, `--json` output shape, and partial-failure on bad-encoding files in `tests/test_wiki_bulk_ops.py`

**Checkpoint**: `scripts/wiki-bulk-ops tag-normalize --vault wiki` canonicalizes tags with dry-run, JSON output, and idempotency.

---

## Phase 8: Orphan Report and Dry-Run Parity (Priority: P2)

**Goal**: Orphan detection (report-only, no modifications) and cross-operation dry-run contract validation.

**Independent Test**: In a temporary vault, create pages with and without incoming links. Run orphan-report. Verify orphan pages listed, well-connected pages excluded, special pages (`index.md`, `log.md`, `hot.md`) excluded, exit code 0, no files modified. For dry-run parity: run each command `--dry-run --json`, then live, compare counts match.

### Tests for User Story 6

> Write these behavioral tests first and confirm they fail before the implementation tasks.

- [x] T051 [US6] Add failing orphan-report tests for: pages with zero incoming wikilinks are listed; pages with incoming links excluded; `index.md`, `log.md`, `hot.md` excluded; skip dirs excluded; exit code 0 always; `files_modified: 0`; no files changed on disk — in `tests/test_wiki_bulk_ops.py`
- [x] T052 [US6] Add failing cross-operation dry-run parity tests comparing preview and apply modified-file/change counts for link-repair, tag-normalize, and orphan-report, and verifying repeated live runs return zero changes in `tests/test_wiki_bulk_ops.py`

### Implementation for User Story 6

- [x] T053 [US6] Add `orphan-report` subparser to argparse (no operation-specific flags beyond global opts) and wire to handler in `scripts/wiki-bulk-ops`
- [x] T054 [US6] Implement orphan detection: build incoming-link index by scanning all vault `.md` files for wikilink targets; identify pages with zero incoming wikilinks; exclude special pages (`index.md`, `log.md`, `hot.md`) and skip dirs; report as `OperationResult` with `files_modified: 0` and records listing orphan paths per FR-016 in `scripts/wiki-bulk-ops`
- [x] T055 [US6] Wire orphan-report into JSON/text output pipeline; always exit 0 (report-only); verify dry-run and non-dry-run produce identical output (no writes in either mode) in `scripts/wiki-bulk-ops`

**Checkpoint**: All six subcommands support `--dry-run` and `--json` with consistent output format.

---

## Phase 9: Polish & Cross-Cutting Concerns

**Purpose**: Final verification of the complete public seam.

- [x] T056 [P] Confirm executable permission and Python 3.14 stdlib-only shebang/import contract for `scripts/wiki-bulk-ops`
- [x] T057 Update `__main__` assert-based self-check at bottom of `scripts/wiki-bulk-ops` to cover link-repair, tag-normalize, and orphan-report round-trips in addition to existing rename/replace/frontmatter checks
- [x] T058 Run `python3 tests/test_wiki_bulk_ops.py` and the script self-check; fix only failures attributable to this feature
- [x] T059 Run quickstart scenarios 9-12 from `specs/023-wiki-bulk-ops/quickstart.md` (link-repair, tag-normalize, orphan-report) against temporary vault fixtures
- [x] T060 Run `wiki-lint` validation after representative link-repair and tag-normalize operations and record any feature-caused finding in the error ledger
- [x] T061 Review all six subcommand outputs, stderr, exit codes, idempotency, atomicity, and `WIKI_STAGED_WRITES` behavior against `specs/023-wiki-bulk-ops/contracts/cli-contract.md` and `specs/023-wiki-bulk-ops/spec.md`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: Complete. ✅
- **Foundational (Phase 2)**: Complete. ✅
- **US1 Rename (Phase 3)**: Complete. ✅
- **US2 Replace (Phase 4)**: Complete. ✅
- **US4 Broken Link Repair (Phase 5)**: Depends on Foundational; reuses wikilink regex from US1 (T015). Ready to start.
- **US3 Frontmatter (Phase 6)**: Complete. ✅
- **US5 Tag Normalization (Phase 7)**: Depends on Foundational; reuses frontmatter parsing from Phase 2. Ready to start.
- **US6 Orphan + Dry-Run Parity (Phase 8)**: Depends on all command implementations.
- **Polish (Phase 9)**: Depends on all phases; final verification pass.

### Parallel Opportunities

- **Phases 5 and 7** (link-repair and tag-normalize) can proceed in parallel — they touch different subcommand code paths in the same script, but with a single writer they should serialize.
- **Test tasks** (T026-T027, T044-T045, T051-T052) can be drafted in parallel with implementation if using separate workspaces.
- **Polish tasks** T057 and T058 can run in parallel (different concerns).

### Within Each New User Story

- Test tasks → implementation tasks (TDD: tests fail first, then implement)
- Argument parsing → core logic → pipeline wiring → acceptance tests

---

## Parallel Example: New P1 Story (Link Repair)

```text
# Test-author pass (before implementation):
Task: T026 "Add link-repair behavior tests"
Task: T027 "Add link-repair safety tests"

# Then serialize single-script implementation:
Task: T028 → T029 → T030 → T031 → T032 → T033 → T034 → T035 → T036
```

---

## Implementation Strategy

### Current State

Phases 1-4 and Phase 6 (US1 rename, US2 replace, US3 frontmatter) are complete. The script handles three of six specified subcommands.

### Remaining Work — Priority Order

1. **US4 Broken Link Repair (P1)**: Highest remaining priority. Fixes 1000+ broken links — the primary motivating problem for this feature.
2. **US5 Tag Normalization (P2)**: Specialized frontmatter operation with taxonomy awareness.
3. **US6 Orphan Report + Dry-Run Parity (P2)**: Read-only diagnostic; lightweight.
4. **Polish (Phase 9)**: Update self-check, run full quickstart validation, wiki-lint.

### Single-Writer Strategy

One executable script and one test module — assign one writer per workspace. Parallelize only isolated test design; serialize implementation edits to `scripts/wiki-bulk-ops`.

---

## Notes

- Every task uses the required `- [ ] T###` checklist form; `[x]` marks tasks completed in prior implementation passes.
- `[P]` appears only on tasks that can be isolated without incomplete dependencies; `[US#]` appears only in user-story phases.
- Tasks T001-T025 and T037-T043 (renumbered from prior T026-T042) map to the already-implemented rename, replace, and frontmatter subcommands.
- Tasks T026-T036 (link-repair), T044-T050 (tag-normalize), and T051-T055 (orphan-report) are new work.
- The implementation must remain stdlib-only, agent-shaped, atomic per file, markdown-safe, and compatible with `WIKI_STAGED_WRITES=true`.
- Levenshtein distance for fuzzy matching: ~20-line stdlib-only implementation (no dependency needed).
