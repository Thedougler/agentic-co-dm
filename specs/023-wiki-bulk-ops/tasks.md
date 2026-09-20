# Tasks: Wiki Bulk Operations

**Input**: Design documents from `/specs/023-wiki-bulk-ops/`

**Prerequisites**: `plan.md`, `spec.md`, `research.md`, `data-model.md`, `contracts/cli-contract.md`, `quickstart.md`, `.specify/memory/constitution.md`

**Tests**: Behavioral tests are included because the specification defines independently testable acceptance scenarios, the plan requires `tests/test_wiki_bulk_ops.py`, and the constitution requires public-seam tests for new behavior. Tests use stdlib `unittest`; the script also keeps an assert-based `__main__` self-check.

**Organization**: Tasks are grouped by user story in priority order. Every story has an independent test criterion and can be delivered as an incremental CLI capability after the foundational phase.

## Format

Every implementation task uses `- [ ] T###`, an optional `[P]` marker only for independent work, and a `[US#]` label only inside a user-story phase. Each task names the file it changes or the feature artifact it validates.

## Path Conventions

- CLI source: `scripts/wiki-bulk-ops`
- Behavioral tests: `tests/test_wiki_bulk_ops.py`
- Feature artifacts: `specs/023-wiki-bulk-ops/`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Establish the executable script and public-seam test module from the implementation plan.

- [x] T001 Create the executable Python 3.14 CLI entrypoint with a stdlib-only shebang and module docstring in `scripts/wiki-bulk-ops`
- [x] T002 [P] Create the stdlib `unittest` module scaffold and CLI subprocess helper in `tests/test_wiki_bulk_ops.py`
- [x] T003 Add isolated temporary-vault fixture helpers that create UTF-8 markdown pages and clean up after each test in `tests/test_wiki_bulk_ops.py`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Build shared traversal, parsing, reporting, atomicity, and argument infrastructure required by every operation.

**CRITICAL**: No user-story implementation begins until this phase is complete.

- [x] T004 Implement vault resolution in `scripts/wiki-bulk-ops` using `--vault`, then `OBSIDIAN_VAULT_PATH`, then `wiki/`, with a clear stderr error and exit code 1 for a missing or non-directory vault
- [x] T005 Implement scoped markdown traversal in `scripts/wiki-bulk-ops` for `--glob`, `--directory`, and whole-vault defaults, excluding `.obsidian`, `_archive`, `_raw`, `_readouts`, `_meta`, `templates`, and `attachments`
- [x] T006 Implement UTF-8 file reads and per-file skip records in `scripts/wiki-bulk-ops`; decode failures must continue processing, report `skip_reason`, and produce partial-failure exit code 2
- [x] T007 Implement flat frontmatter fence extraction and line-level key/value parsing in `scripts/wiki-bulk-ops`, preserving `---` delimiters and validating keys as `alphanumeric + underscore + hyphen`
- [x] T008 Implement shared Obsidian wikilink/embedded-link parsing in `scripts/wiki-bulk-ops` for bare, piped, path-qualified, anchored, and embedded targets without altering display text or anchors
- [x] T009 Implement `Change`, `ChangeRecord`, and `OperationResult` reporting in `scripts/wiki-bulk-ops`, including text and JSON output fields `files_scanned`, `files_modified`, `files_skipped`, `total_changes`, and per-file records
- [x] T010 Implement same-directory tempfile plus `os.replace` atomic writes in `scripts/wiki-bulk-ops`, honoring `--dry-run` so preview mode performs no writes
- [x] T011 Implement shared argparse global options and exit-status handling in `scripts/wiki-bulk-ops` for `--vault`, `--dry-run`, `--json`, `--glob`, and `--directory`, distinguishing success/no-op (0), validation errors (1), and partial failures (2)
- [x] T012 [P] Add foundational CLI tests for missing vaults, JSON output shape, dry-run no-write behavior, atomic no-partial-write behavior, scope filters, and partial UTF-8 failure handling in `tests/test_wiki_bulk_ops.py`

**Checkpoint**: Shared traversal, parsing, output, dry-run, atomicity, and exit-code behavior is ready for all stories.

---

## Phase 3: User Story 1 — Rename an Entity Across the Wiki (Priority: P1) 🎯 MVP

**Goal**: Rename exactly one entity page and rewrite its structural references across the scoped vault without changing unrelated prose or markdown syntax.

**Independent Test**: In a temporary vault, rename a page referenced by bare, piped, embedded, anchored, and path-qualified links; verify the source filename/title and every exact target change, preserved display text/anchors, valid frontmatter, unchanged unrelated prose, collision refusal with zero writes, and preservation of substring names such as `old-name-kin`.

### Tests for User Story 1

- [x] T013 [US1] Add failing rename behavior tests for source filename/title updates and bare, piped, embedded, anchored, and path-qualified wikilink rewrites in `tests/test_wiki_bulk_ops.py`
- [x] T014 [US1] Add failing rename safety tests for destination collisions, zero-change validation failures, exact-target matching, title options/defaults, body-prose preservation, dry-run output, and idempotent result reporting in `tests/test_wiki_bulk_ops.py`
- [x] T015 [US1] Implement `rename` argument validation in `scripts/wiki-bulk-ops` requiring exactly one existing `OLD_STEM.md`, rejecting an existing `NEW_STEM.md`, and reporting collision/not-found errors on stderr
- [x] T016 [US1] Implement exact wikilink and embed target rewriting in `scripts/wiki-bulk-ops` that preserves path prefixes, anchors, and piped display text while excluding body-text title mentions and substring entity names
- [x] T017 [US1] Implement source-page frontmatter title mutation and filename change records in `scripts/wiki-bulk-ops`, using `--old-title`/`--new-title` when supplied and title-cased `--new` otherwise
- [x] T018 [US1] Integrate rename preflight, scoped reference planning, atomic source-file move, dry-run records, and zero writes on validation failure in `scripts/wiki-bulk-ops`
- [x] T019 [US1] Add rename CLI acceptance coverage for JSON change records, line numbers/zones, exit codes, and dry-run/live modified-file parity in `tests/test_wiki_bulk_ops.py`

**Checkpoint**: `scripts/wiki-bulk-ops rename` is independently usable as the MVP and is idempotent after a successful rename.

---

## Phase 4: User Story 2 — Bulk Find-and-Replace with Markdown Safety (Priority: P1)

**Goal**: Replace literal or regex text in scoped body zones while protecting frontmatter, wikilink targets, embeds, and callout syntax by default.

**Independent Test**: In a temporary vault containing frontmatter, body text, callouts, embeds, and wikilinks, verify default replacement changes body occurrences only; opt-in flags change the requested protected zones; empty wikilinks are refused; line-level JSON records are correct; and a second run reports zero changes.

### Tests for User Story 2

- [x] T020 [US2] Add failing replace tests for literal body-only substitution, occurrence/file summaries, preserved YAML delimiters, preserved callouts/embeds, and unchanged wikilink targets in `tests/test_wiki_bulk_ops.py`
- [x] T021 [US2] Add failing replace safety tests for `--include-frontmatter`, `--include-links`, regex mode, empty-wikilink refusal, glob/directory scope, line-numbered records, partial failures, dry-run parity, and idempotency in `tests/test_wiki_bulk_ops.py`
- [x] T022 [US2] Implement `replace` argument validation and literal/Python-regex search compilation in `scripts/wiki-bulk-ops`, refusing an empty search pattern with exit code 1
- [x] T023 [US2] Implement frontmatter, wikilink-target, and body safety-zone splitting in `scripts/wiki-bulk-ops`, defaulting to body replacement and requiring explicit `--include-frontmatter` or `--include-links` opt-in
- [x] T024 [US2] Implement zone-aware replacement and line-numbered `Change` records in `scripts/wiki-bulk-ops`, preserving callouts, embeds, YAML delimiters, anchors, and pipe display text
- [x] T025 [US2] Refuse any planned result containing an empty wikilink target `[[]]` in `scripts/wiki-bulk-ops`, naming the specific file and line without writing any file
- [x] T026 [US2] Integrate replace with scope traversal, dry-run/atomic apply, text/JSON summaries, and idempotent no-change success in `scripts/wiki-bulk-ops`
- [x] T027 [US2] Add replace CLI acceptance coverage for scoped operations, JSON output, partial UTF-8 failures, and repeated invocation in `tests/test_wiki_bulk_ops.py`

**Checkpoint**: User Stories 1 and 2 independently provide safe structural and body-text bulk operations.

---

## Phase 5: User Story 4 — Broken Link Repair (Priority: P1)

**Goal**: Detect broken wikilinks and resolve them through explicit mapping, git rename history, aliases, or unambiguous fuzzy matching; report ambiguous and unresolved targets without silently changing them.

**Independent Test**: In a temporary vault, introduce mapping-resolvable, git-resolvable, alias-resolvable, fuzzy-resolvable, ambiguous, and dead links. Verify only safe single candidates are repaired, mapped/piped links preserve display text, ambiguous/dead links remain unchanged and are reported, valid links remain unchanged, and output records resolution sources.

### Tests for User Story 4

- [x] T028 [US4] Add failing link-repair behavior tests for explicit TSV mapping, git-detected rename, frontmatter alias, single-candidate fuzzy repair, ambiguous candidate reporting, unresolved reporting, and preserved valid links in `tests/test_wiki_bulk_ops.py`
- [x] T029 [US4] Add failing link-repair safety tests for tier-disabling flags, fuzzy threshold validation (1–5), malformed TSV warnings, piped/embedded/anchored rewrites, dry-run parity, partial failures, and idempotency in `tests/test_wiki_bulk_ops.py`
- [x] T030 [US4] Add the `link-repair` subparser and validate `--mapping`, `--no-git`, `--no-aliases`, `--no-fuzzy`, and `--fuzzy-threshold` (default 2, allowed range 1–5) in `scripts/wiki-bulk-ops`
- [x] T031 [US4] Implement broken-target detection in `scripts/wiki-bulk-ops` by scanning wikilinks, indexing existing markdown stems, and retaining target/line/display metadata
- [x] T032 [US4] Implement explicit TSV mapping resolution in `scripts/wiki-bulk-ops` for `old_stem<TAB>new_stem`, ignoring `#` comments and warning/skipping lines that do not contain exactly two columns
- [x] T033 [US4] Implement git rename-history resolution in `scripts/wiki-bulk-ops` using `git log --all --diff-filter=R` and accepting only mappings whose destination markdown stem currently exists
- [x] T034 [US4] Implement frontmatter `aliases` resolution in `scripts/wiki-bulk-ops` and normalize alias values to canonical existing page stems
- [x] T035 [US4] Implement stdlib-only Levenshtein matching in `scripts/wiki-bulk-ops`; auto-resolve one candidate within threshold and report multiple candidates as ambiguous without changing them
- [x] T036 [US4] Apply resolved mappings through shared link rewriting in `scripts/wiki-bulk-ops`, preserving anchors, pipe display text, embeds, and zone-labeled change records with mapping/git/alias/fuzzy source annotations
- [x] T037 [US4] Integrate link repair with dry-run/atomic apply, JSON/text summaries, scope filters, skipped-file reporting, and idempotent re-run behavior in `scripts/wiki-bulk-ops`
- [x] T038 [US4] Add link-repair CLI acceptance coverage for output shape, resolution-source reporting, scope, dry-run/live parity, and partial-failure exit code 2 in `tests/test_wiki_bulk_ops.py`

**Checkpoint**: The highest-priority link-integrity workflow repairs only unambiguous links and leaves judgment-required cases visible.

---

## Phase 6: User Story 3 — Bulk Frontmatter Update (Priority: P2)

**Goal**: Set, rename, or remove a flat frontmatter field on files matching scope and repeated `KEY=VALUE` filters without changing body content.

**Independent Test**: In a temporary vault with matching and non-matching `type: npc` pages, set a scalar field, rename an existing field while preserving its value, remove a field, and verify only matching frontmatter changes, body bytes remain unchanged, and resulting YAML remains parseable.

### Tests for User Story 3

- [x] T039 [US3] Add failing frontmatter tests for filtered `set`, idempotent existing-value handling, non-matching-page preservation, body-byte preservation, and valid YAML in `tests/test_wiki_bulk_ops.py`
- [x] T040 [US3] Add failing frontmatter tests for `rename`, `remove`, repeated filters, invalid keys, missing action parameters, scope filters, dry-run output, and partial failures in `tests/test_wiki_bulk_ops.py`
- [x] T041 [US3] Validate `frontmatter` actions and required `--value`/`--new-field` parameters in `scripts/wiki-bulk-ops`; enforce valid YAML keys matching `alphanumeric + underscore + hyphen`
- [x] T042 [US3] Implement repeated `--filter KEY=VALUE` parsing and exact flat-frontmatter predicate matching in `scripts/wiki-bulk-ops`
- [x] T043 [US3] Implement line-level frontmatter set/update, rename-with-value-preservation, and remove mutations in `scripts/wiki-bulk-ops` without reformatting unrelated keys or body content
- [x] T044 [US3] Integrate frontmatter mutations with validation, dry-run/atomic apply, idempotent no-op handling, and `frontmatter` zone change records in `scripts/wiki-bulk-ops`
- [x] T045 [US3] Add frontmatter CLI acceptance coverage for directory/glob scope, JSON output, valid YAML, body preservation, and partial UTF-8 failures in `tests/test_wiki_bulk_ops.py`

**Checkpoint**: Filtered schema-level updates work independently and preserve all non-target page content.

---

## Phase 7: User Story 5 — Bulk Tag Normalization (Priority: P2)

**Goal**: Canonicalize frontmatter tags against `_meta/taxonomy.md`, merge aliases, collapse duplicates, and report unknown tags without removing them unless explicitly requested.

**Independent Test**: In a temporary vault with variant spellings and a taxonomy defining canonical tags/aliases, verify aliases canonicalize, duplicates collapse, unknown tags are reported but retained by default, `--remove-unknown` removes them, body content is unchanged, and YAML remains valid.

### Tests for User Story 5

- [x] T046 [US5] Add failing tag-normalize tests for alias replacement, duplicate collapse, unknown-tag reporting without default removal, body preservation, and valid YAML in `tests/test_wiki_bulk_ops.py`
- [x] T047 [US5] Add failing tag-normalize safety tests for `--remove-unknown`, custom `--taxonomy`, missing taxonomy validation, scope filters, dry-run parity, partial failures, and idempotency in `tests/test_wiki_bulk_ops.py`
- [x] T048 [US5] Add the `tag-normalize` subparser and resolve/validate the custom or default `_meta/taxonomy.md` path in `scripts/wiki-bulk-ops`, exiting 1 when it is missing or unreadable
- [x] T049 [US5] Parse canonical tags and aliases from heading/list-item taxonomy syntax in `scripts/wiki-bulk-ops` and build an alias-to-canonical mapping without external dependencies
- [x] T050 [US5] Normalize inline and block-list frontmatter `tags:` values in `scripts/wiki-bulk-ops`, canonicalizing aliases, collapsing duplicates, collecting unknowns, and removing unknowns only with `--remove-unknown`
- [x] T051 [US5] Integrate tag normalization with dry-run/atomic apply, `frontmatter` change records, unknown-tag reporting, JSON/text summaries, and idempotent no-change behavior in `scripts/wiki-bulk-ops`
- [x] T052 [US5] Add tag-normalize CLI acceptance coverage for JSON output, scope filters, dry-run/live parity, and partial UTF-8 failures in `tests/test_wiki_bulk_ops.py`

**Checkpoint**: Taxonomy-aware tag cleanup is deterministic, reviewable, and body-safe.

---

## Phase 8: User Story 6 — Dry-Run and Diff Preview (Priority: P2)

**Goal**: Make every mutating operation preview exact file/line/old/new changes without writing, while providing a report-only orphan diagnostic.

**Independent Test**: Run each mutating command with `--dry-run --json`, verify no bytes or filenames change and every planned change has file, line, old text, and new text, then run live and compare modified-file/change counts. Run `orphan-report` in both modes and verify it always exits 0 with zero modifications.

### Tests for User Story 6

- [x] T053 [US6] Add failing cross-command dry-run tests for rename, replace, frontmatter, link-repair, tag-normalize, and MOC generation that compare preview records/counts with the subsequent live operation in `tests/test_wiki_bulk_ops.py`
- [x] T054 [US6] Add failing orphan-report tests for zero-incoming-link pages, linked-page exclusion, `index.md`/`log.md`/`hot.md` exclusion, skipped directories, exit code 0, zero modifications, and unchanged bytes in `tests/test_wiki_bulk_ops.py`
- [x] T055 [US6] Add the `orphan-report` subparser and implement incoming-wikilink indexing in `scripts/wiki-bulk-ops`, excluding special pages and infrastructure directories from orphan candidacy
- [x] T056 [US6] Emit orphan paths as report records in the shared text/JSON `OperationResult` from `scripts/wiki-bulk-ops`, force `files_modified: 0`, perform no writes in either mode, and always exit 0
- [x] T057 [US6] Audit and correct shared dry-run planning in `scripts/wiki-bulk-ops` so every mutating command exposes file/line/old/new detail and live application consumes the same plan without recomputation drift
- [x] T058 [US6] Add cross-operation acceptance coverage for dry-run no-write guarantees, preview/live count parity, repeated-run zero changes, and report-only orphan behavior in `tests/test_wiki_bulk_ops.py`

**Checkpoint**: Agents can inspect any planned mutation before applying it, and orphan detection is strictly diagnostic.

---

## Phase 9: User Story 7 — Subfolder MOC Generation (Priority: P2)

**Goal**: Generate idempotent `_index.md` Map of Content files for content folders and update root `index.md` with top-level MOC links, excluding infrastructure folders.

**Independent Test**: In a temporary vault with nested content folders and infrastructure folders, verify each content folder gets a valid-frontmatter `_index.md` with player-friendly title, alphabetical piped links to its own pages, and child-MOC links; verify no infrastructure MOC is created, root `index.md` links top-level MOCs, and a second run reports zero changes.

### Tests for User Story 7

- [x] T059 [US7] Add failing MOC tests for content-folder `_index.md` creation, required frontmatter, static/fallback folder titles, alphabetical piped page links using page titles or filenames, and nested child-MOC links in `tests/test_wiki_bulk_ops.py`
- [x] T060 [US7] Add failing MOC safety tests for infrastructure-folder exclusion, root `index.md` integration, manual-content regeneration semantics, dry-run parity, and idempotent re-run in `tests/test_wiki_bulk_ops.py`
- [x] T061 [US7] Add the `moc-generate` subparser and content-folder discovery in `scripts/wiki-bulk-ops`, excluding `_archive`, `_raw`, `_meta`, `.obsidian`, `attachments`, and `templates`
- [x] T062 [US7] Implement static folder-name title mapping with title-cased fallback in `scripts/wiki-bulk-ops` for generated MOC frontmatter `title:` values
- [x] T063 [US7] Implement deterministic MOC rendering in `scripts/wiki-bulk-ops` with required `title`, `category`, `tags`, `sources`, `created`, and `updated` fields; flat alphabetical piped wikilinks; and nested child `_index.md` links
- [x] T064 [US7] Implement root `index.md` regeneration in `scripts/wiki-bulk-ops` to include links to every top-level content-folder `_index.md` while preserving the specified derived-file semantics
- [x] T065 [US7] Integrate MOC generation with dry-run/atomic live writes, change records, JSON/text output, and idempotent regeneration in `scripts/wiki-bulk-ops`
- [x] T066 [US7] Add MOC CLI acceptance coverage for generated frontmatter, link ordering, infrastructure exclusions, root integration, dry-run/live parity, and idempotency in `tests/test_wiki_bulk_ops.py`

**Checkpoint**: Content-folder navigation is generated from current vault state and remains safe to rerun.

---

## Phase 10: Polish & Cross-Cutting Concerns

**Purpose**: Verify the complete public seam, performance, syntax preservation, and repository conventions after all stories are implemented.

- [x] T067 [P] Extend the assert-based `__main__` self-check in `scripts/wiki-bulk-ops` to cover all seven subcommands, dry-run/apply round trips, validation errors, and idempotency
- [x] T068 [P] Add a full-vault performance smoke scenario for a 1,565-file fixture and verify rename completes in under 5 seconds in `tests/test_wiki_bulk_ops.py`
- [x] T069 Run the documented quickstart scenarios for rename, replace, frontmatter, link repair, tag normalization, MOC generation, and orphan reporting from `specs/023-wiki-bulk-ops/quickstart.md`
- [x] T070 Run `python3 tests/test_wiki_bulk_ops.py` and the `scripts/wiki-bulk-ops` self-check; fix failures in `scripts/wiki-bulk-ops` or `tests/test_wiki_bulk_ops.py` only when attributable to this feature
- [x] T071 Compare representative pre/post `wiki-lint` findings for each mutating operation and record any feature-caused regression in `errors.md` using `scripts/error-ledger.py`
- [x] T072 Review executable permission, stdlib-only imports, stderr/error behavior, exit codes, idempotency, atomicity, and markdown preservation against `specs/023-wiki-bulk-ops/spec.md` and `specs/023-wiki-bulk-ops/contracts/cli-contract.md`

---

## Phase 11: MOC noise correction

**Purpose**: Keep structural navigation useful without creating or linting redundant one-page leaf indexes.

- [x] T073 Narrow MOC generation to folders with at least two direct pages or eligible child MOCs, remove stale one-page leaf MOCs, and exempt generated MOCs from identity/template lint in `scripts/wiki-bulk-ops`, `tools/wiki_ops/identity.py`, `tools/lint_wiki.py`, and `scripts/wiki-lint`
- [x] T074 Update MOC acceptance coverage and run focused structural verification in `tests/test_wiki_bulk_ops.py`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies; T001–T003 establish the two owned source surfaces.
- **Foundational (Phase 2)**: Depends on Setup; T004–T012 block all stories.
- **P1 stories (Phases 3–5)**: Each depends on Phase 2. US4 also reuses the shared link parser and rewrite helper delivered in US1, so T028–T038 follow US1's implementation unless isolated workspaces provide an equivalent handoff.
- **P2 stories (Phases 6–9)**: Depend on Phase 2. US3 and US5 reuse frontmatter parsing; US6's parity audit depends on the mutating command plans; US7 is independent of operation semantics except for shared output/atomicity.
- **Polish (Phase 10)**: Depends on all desired stories.

### User Story Completion Order

1. **US1 (P1)** — rename; MVP and shared wikilink rewrite foundation.
2. **US2 (P1)** — safe replacement.
3. **US4 (P1)** — broken-link repair; consumes US1 link rewriting.
4. **US3 (P2)** — frontmatter mutation.
5. **US5 (P2)** — taxonomy-aware tags; consumes shared frontmatter logic.
6. **US6 (P2)** — dry-run parity and orphan report; audits all operation plans.
7. **US7 (P2)** — MOC generation; consumes shared scope, frontmatter, output, and atomicity.

### Within Each User Story

- Write the story's failing public-seam tests before its implementation tasks.
- Implement argument validation before operation logic, then operation logic before pipeline integration.
- Keep one writer for `scripts/wiki-bulk-ops` and one writer for `tests/test_wiki_bulk_ops.py`; parallel labels apply only to isolated workspaces or independent setup/polish surfaces.
- Complete the story checkpoint and run its independent test before advancing to the next priority.

### Parallel Opportunities

- T002 and T003 can run in parallel with T001 in isolated setup workspaces.
- T012 can be authored in parallel with foundational source work in a separate workspace, then merged before story implementation.
- After Phase 2, US2 and US3 can be designed/test-authored in parallel with US1 only when each uses an isolated workspace; shared-script implementation remains serialized.
- US5 test authoring can run in parallel with US4 implementation in an isolated workspace; both consume only foundational contracts.
- T053/T054 and T059/T060 can be test-authored in parallel after the shared command contract is stable.
- T067 and T068 can run in parallel because they touch distinct concerns (`scripts/wiki-bulk-ops` self-check versus test fixture/performance coverage).

## Parallel Execution Examples Per User Story

### US1

```text
Parallel in isolated workspaces: T013 and T014 (test-authoring slices).
Then serialize T015 → T016 → T017 → T018 → T019 because they share scripts/wiki-bulk-ops.
```

### US2

```text
Parallel in isolated workspaces: T020 and T021 (test-authoring slices).
Then serialize T022 → T023 → T024 → T025 → T026 → T027 because safety-zone logic shares the CLI source.
```

### US4

```text
Parallel in isolated workspaces: T028 and T029 (test-authoring slices).
Then serialize T030 → T031 → T032 → T033 → T034 → T035 → T036 → T037 → T038; resolution tiers share one source pipeline.
```

### US3

```text
Parallel in isolated workspaces: T039 and T040 (test-authoring slices).
Then serialize T041 → T042 → T043 → T044 → T045; all frontmatter mutations share the parser and writer.
```

### US5

```text
Parallel in isolated workspaces: T046 and T047 (test-authoring slices).
Then serialize T048 → T049 → T050 → T051 → T052; taxonomy parsing and normalization share one command path.
```

### US6

```text
Parallel in isolated workspaces: T053 and T054 (test-authoring slices).
After command plans exist, serialize T055 → T056 → T057 → T058 because orphan reporting and parity share output contracts.
```

### US7

```text
Parallel in isolated workspaces: T059 and T060 (test-authoring slices).
Then serialize T061 → T062 → T063 → T064 → T065 → T066 because MOC discovery, rendering, and root integration share generated-file state.
```

---

## Implementation Strategy

### MVP First

1. Complete Phase 1 Setup.
2. Complete Phase 2 Foundational; this is the blocking safety boundary.
3. Complete Phase 3 US1 rename and its independent tests.
4. Validate dry-run/live behavior, exact link rewrites, collision safety, and idempotency.
5. Stop at the US1 checkpoint for the first usable delivery.

### Incremental Delivery

1. Add US2 safe replace and validate independently.
2. Add US4 broken-link repair, reusing US1's exact link machinery.
3. Add US3 frontmatter mutation, then US5 tag normalization.
4. Add US6 orphan reporting and cross-command preview parity.
5. Add US7 MOC generation.
6. Run Phase 10 only after all selected stories pass their checkpoints.

### Single-Writer Strategy

The feature has one executable source and one test module. Parallelize planning/test-authoring only across isolated workspaces; serialize source integration to avoid conflicting edits and preserve one canonical implementation.

## Notes

- `[P]` appears only when work can proceed independently without an incomplete prerequisite.
- `[US#]` labels map every story-phase task to the corresponding prioritized story in `spec.md`.
- Data-model constraints are preserved in the task descriptions: exact-one rename source, collision refusal, non-empty search, valid YAML keys, UTF-8 skip behavior, two-column TSV, fuzzy threshold 1–5, and readable taxonomy.
- All mutating operations remain stdlib-only, agent-shaped, markdown-safe, atomic per file, and idempotent.
