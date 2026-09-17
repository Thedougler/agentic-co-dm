# Tasks: Creative Linting

**Input**: Design documents from `/specs/024-creative-linting/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/, quickstart.md

**Organization**: Tasks grouped by user story. US3 (Registry) and US4 (Severity) are foundational — Phase 2 delivers both before any other story can begin.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2)
- Exact file paths included in every task description

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Package structure, directories, tooling prerequisites

- [ ] T001 Create `tools/creative_lint/` package: `__init__.py`, `evaluators/__init__.py`
- [ ] T002 [P] Create `rules/` directory with empty `registry.yml` and `bundles.yml`
- [ ] T003 [P] Create `styles/CoDM/` directory
- [ ] T004 [P] Create `.vale.ini` at repo root per vale-style-contract: `StylesPath = styles`, `MinAlertLevel = suggestion`, `[wiki/*.md] BasedOnStyles = CoDM`, with exclusions for `_raw/`, `_staging/`, `_archive/`, `templates/`
- [ ] T005 [P] Create `tests/fixtures/creative_lint/` directory
- [ ] T006 Verify PyYAML available in `.venv` (`pip install pyyaml` if missing)

---

## Phase 2: Foundational — Registry + Severity (US3 + US4)

**Purpose**: Rule registry and severity model — blocks ALL user stories

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

**Delivers**: US3 (Rule Registry and Stable IDs, P1) + US4 (Five-Level Severity Model, P2)

**Independent Test (US3)**: Load `rules/registry.yml`, verify all rules discoverable by ID, verify `wiki-lint rule <ID>` returns full definition, verify duplicate ID rejected with clear error.

**Independent Test (US4)**: Run wiki-lint against content triggering all five severity levels. Verify BLOCK/REPAIR → `repair_required`, REVIEW alone → `review_needed`, WARN/INFO alone → `clean`. Verify scene/diversity categories cannot exceed WARN.

- [ ] T007 Implement severity model in `tools/creative_lint/severity.py` — define `SEVERITY_ORDER` mapping (`BLOCK > REPAIR > REVIEW > WARN > INFO`), `status_from_findings()` returning `repair_required|review_needed|clean`, `min_severity(a, b)` for bundle gate logic, `TASTE_CEILING` dict mapping categories `scene` and `diversity` to max severity `WARN`
- [ ] T008 [P] Implement `Finding` dataclass in `tools/creative_lint/finding.py` per finding-schema contract — required fields: `rule_id` (str, pattern `^[A-Z]+\d{3}$`), `result` (enum `pass|fail|abstain`), `severity` (enum `BLOCK|REPAIR|REVIEW|WARN|INFO`), `location` (dict with required `file` str, optional `line` int ≥1, `col` int ≥1, `end_line`, `end_col`, `text`), `evidence` (str), `reason` (str), `evaluator` (str, enum `vale|symbolic|retrieval|semantic|human|lint_wiki`); optional: `repair_target` (str|None), `waiver` (dict|None). Include `to_dict()` for JSON serialization.
- [ ] T009 Implement `RuleDefinition` dataclass and `Registry` class in `tools/creative_lint/registry.py` per registry-contract — `RuleDefinition` fields: `id` (str, unique, pattern `^[A-Z]+\d{3}$`), `title` (str), `category` (enum `wiki|canon|temporal|agency|retrieval|scene|diversity`), `scope` (enum `content|frontmatter|corpus|file`), `severity` (enum `BLOCK|REPAIR|REVIEW|WARN|INFO`), `evaluator` (enum `vale|symbolic|retrieval|semantic|human`), `lifecycle` (enum `DRAFT|SHADOW|ACTIVE`), `message` (str), `vale_style` (str|None, required when evaluator=vale), `repair` (str|None), `tags` (list[str]), `conflicts` (list[str]), `depends` (list[str]). `Registry` methods: `load(path)` via PyYAML, `get(rule_id)` raises KeyError, `by_category(cat)`, `by_evaluator(eval)`, `active()` (lifecycle=ACTIVE), `shadow()` (lifecycle=SHADOW), `all_ids()`. `validate()` returns list of errors: duplicate IDs, invalid ID format, invalid enums, severity ceiling violation (scene/diversity > WARN), missing vale_style when evaluator=vale, invalid conflicts/depends references.
- [ ] T010 Populate `rules/registry.yml` with initial ~15 rule definitions per research.md R7: static Vale rules — `AGENCY001` (agency, content, BLOCK, vale, `you (decide|choose|feel|think|believe|realize|know)`), `AGENCY002` (agency, content, BLOCK, vale, `you (must|have to|need to)`), `AGENCY003` (agency, content, REVIEW, vale, `you (suddenly|involuntarily|can't help but)`), `KNOW001` (retrieval, content, REVIEW, vale, `obviously|everyone knows|clearly` without citation), `KNOW002` (retrieval, content, REPAIR, vale, `as you may recall|the player`), `TEMP001` (temporal, content, REVIEW, vale, past-tense future reference), `SCENE001` (scene, content, WARN, vale, min situation marker per section), `SCENE002` (scene, content, WARN, vale, `something happens|stuff occurs|things go`); symbolic — `CANON001` (canon, frontmatter, REPAIR, symbolic, dead/rejected NPC as present), `CANON002` (canon, frontmatter, REVIEW, symbolic, entity updated >30d stale), `WIKI001` (wiki, frontmatter, BLOCK, symbolic, missing required frontmatter), `WIKI002` (wiki, frontmatter, BLOCK, symbolic, invalid type/lifecycle); corpus-level — `DIVERSITY001` (diversity, corpus, INFO, symbolic, vocab frequency), `RETRIEVAL001` (retrieval, content, BLOCK, symbolic, broken wikilink). All rules lifecycle: ACTIVE.
- [ ] T011 Write `tests/test_creative_lint.py` — test registry loading from a minimal YAML fixture, duplicate ID rejection, severity ceiling enforcement (scene rule at BLOCK → validation error), `status_from_findings()` for each status, Finding `to_dict()` round-trip

**Checkpoint**: Registry loads, validates, severity model computes status. US3 and US4 acceptance criteria verifiable.

---

## Phase 3: US6 — Multiple Evaluator Types (Priority: P2)

**Goal**: Vale static evaluator + Python symbolic evaluators share a unified finding contract.

**Independent Test**: Define WIKI001 (symbolic — missing frontmatter) and AGENCY001 (Vale — authored PC decision). Run both. Verify findings share the same JSON schema. Verify the static evaluator makes no LLM call. Verify symbolic evaluator returns `abstain` when uncertain.

- [ ] T012 [P] [US6] Create Vale rule files in `styles/CoDM/` — `AGENCY001.yml` (extends: existence, tokens matching `You decide|You choose|You feel|You think|You believe|You realize|You know`, level: error, scope: text.paragraph), `AGENCY002.yml` (extends: existence, `You must|You have to|You need to`, level: error, scope: text.paragraph), `AGENCY003.yml` (extends: existence, `You suddenly|You involuntarily|You can't help but`, level: warning, scope: text.paragraph), `KNOW001.yml` (extends: existence, `obviously|everyone knows|clearly`, level: warning, scope: text.paragraph), `KNOW002.yml` (extends: existence, `as you may recall|the player`, level: error, scope: text.paragraph), `TEMP001.yml` (extends: conditional, past-tense + future-session marker, level: warning), `SCENE001.yml` (extends: occurrence, vague scene markers, level: suggestion), `SCENE002.yml` (extends: existence, `something happens|stuff occurs|things go`, level: suggestion)
- [ ] T013 [P] [US6] Implement Vale adapter in `tools/creative_lint/vale_adapter.py` — `run_vale(files: list[Path], config: Path) -> list[dict]` invoking `vale --output=JSON --config=<config> <files>`, parse JSON output, map per finding-schema contract Vale Output Mapping: `Check` → strip `CoDM.` prefix → `rule_id`, `Line` → `location.line`, `Span[0]` → `location.col`, `Span[1]` → `location.end_col`, `Match` → `location.text`, `Message` → `evidence`, file key → `location.file` (relative to vault). Set `result` to `fail`, `evaluator` to `vale`. Look up `reason` and `repair_target` from registry. Handle Vale not installed (return empty list, log warning).
- [ ] T014 [P] [US6] Implement symbolic evaluator in `tools/creative_lint/evaluators/symbolic.py` — `run_symbolic(files: list[Path], registry: Registry, vault_path: Path) -> list[Finding]`. Evaluators: `CANON001` (parse frontmatter of target files, cross-reference NPC lifecycle field against referenced NPCs — lifecycle `rejected` or tag `dead` referenced as present → fail), `CANON002` (entity `updated` field >30 days from now → fail), `WIKI001`/`WIKI002`/`RETRIEVAL001` (wrap `tools/lint_wiki.py` findings by running it with `--json` and mapping HARD keys to Finding schema: `missing_frontmatter` → WIKI001, `bad_type`/`bad_lifecycle` → WIKI002, `broken_links` → RETRIEVAL001). Support `abstain` when evaluator cannot determine pass/fail.
- [ ] T015 [US6] Implement engine orchestrator in `tools/creative_lint/engine.py` — `Engine` class with `lint(files, registry, bundle=None, vault_path=None, severity_filter=None) -> LintResult`. Invokes Vale adapter for `evaluator=vale` rules, symbolic evaluator for `evaluator=symbolic` rules. Merges findings. When bundle provided, applies severity gate via `min_severity(rule.severity, gate_ceiling)`. Excludes rules not in bundle's categories. Filters DRAFT and SHADOW rules from agent-facing output (SHADOW rules collected in `LintResult.shadow`). Applies `severity_filter` if set. Computes `LintResult.status` via `status_from_findings()`. `LintResult` fields: `status`, `bundle` (str|None), `files_checked` (int), `rules_evaluated` (int), `findings` (list[Finding]), `summary` (dict mapping severity → count), `shadow` (list[Finding]).

**Checkpoint**: `Engine.lint()` runs Vale + symbolic evaluators, merges findings into unified schema.

---

## Phase 4: US5 — Task-Specific Rule Bundles (Priority: P2)

**Goal**: Named bundles scope rules per task type with severity gates.

**Independent Test**: Define `session-prep` bundle with agency at block, retrieval at review, scene as diagnostics. Run `wiki-lint task session-prep`. Verify only bundled categories execute. Run `wiki-lint task wiki-ingest` — verify different bundle applies.

- [ ] T016 [US5] Implement `BundleDefinition` and `BundleRegistry` in `tools/creative_lint/bundles.py` per registry-contract — `BundleDefinition` fields: `name` (str), `description` (str), `block` (list[str] — categories at BLOCK ceiling), `review` (list[str] — categories at REVIEW ceiling), `diagnostics` (list[str] — categories at WARN ceiling). `resolve(registry)` returns `list[tuple[RuleDefinition, str]]` where str is effective severity = `min(rule.severity, gate_ceiling)`. Only ACTIVE rules included. `BundleRegistry.load(path)` parses `rules/bundles.yml`, `get(name)` raises KeyError for unknown bundle.
- [ ] T017 [US5] Populate `rules/bundles.yml` with initial bundles per research.md R8 — `session-prep` (block: [agency, canon, wiki], review: [retrieval, temporal], diagnostics: [scene, diversity]), `wiki-ingest` (block: [wiki], review: [canon], diagnostics: [retrieval]), `worldbuilding` (block: [canon, wiki], review: [retrieval], diagnostics: [scene]), `live-codm` (block: [agency], review: [], diagnostics: [scene]), `corpus` (block: [wiki, canon], review: [retrieval, temporal, agency], diagnostics: [scene, diversity]). Each bundle includes a `description` field.
- [ ] T018 [US5] Add bundle resolution tests to `tests/test_creative_lint.py` — verify gate logic: agency rule at BLOCK in session-prep stays BLOCK; same rule in corpus bundle under review gate caps at REVIEW; scene rule at inherent WARN in diagnostics gate stays WARN; rule category not in bundle → excluded from results

**Checkpoint**: Bundles resolve to (rule, effective_severity) pairs with correct gate capping.

---

## Phase 5: US2 — wiki-lint CLI for Files and Corpus (Priority: P1)

**Goal**: Extend `scripts/wiki-lint` with subcommands for creative linting. Existing no-subcommand behavior unchanged.

**Independent Test**: Run `wiki-lint file <path>` against a page with missing frontmatter → WIKI001 BLOCK finding in JSON. Run `wiki-lint --json` (no subcommand) → existing output unchanged. Run without `--json` → human-readable.

- [ ] T019 [US2] Refactor `scripts/wiki-lint` to detect subcommands — if first positional arg is `task|file|corpus|changed|rule`, route to new handler function; otherwise preserve existing `main()` behavior exactly. Import `tools.creative_lint` only when subcommand used (no startup cost for existing mode).
- [ ] T020 [US2] Implement `task` subcommand handler in `scripts/wiki-lint` — parse args: `bundle` (required), `path...` (optional, default vault), `--json`, `--severity`. Load Registry from `rules/registry.yml`, BundleRegistry from `rules/bundles.yml`. Resolve bundle. Call `Engine.lint()`. Exit codes per cli-contract: 0 = clean/WARN/INFO only, 1 = BLOCK/REPAIR, 2 = REVIEW (no BLOCK/REPAIR). Unknown bundle → exit 2 listing available bundles.
- [ ] T021 [US2] Implement `file` subcommand handler — run all active rules (no bundle context) against a single file at inherent severity. Same output format and exit codes.
- [ ] T022 [P] [US2] Implement `corpus` subcommand handler — run corpus bundle against all `.md` files under vault path (respecting SKIP_DIRS from lint_wiki.py)
- [ ] T023 [P] [US2] Implement `changed` subcommand handler — get changed files via `git diff --name-only HEAD`, filter to `.md` in vault, run all active rules
- [ ] T024 [US2] Implement `rule` subcommand handler — load Registry, lookup by ID, print definition per cli-contract format: ID, title, category, severity, evaluator, lifecycle, scope, message, repair, tags, bundle memberships (scan bundles.yml for categories matching rule's category). Unknown ID → exit 2.
- [ ] T025 [US2] Implement human-readable output formatter — per cli-contract example: header line (`wiki-lint task <bundle>: N files, M rules → status`), one line per finding (`SEVERITY  RULE_ID  file:line  message`), indented evidence, indented repair hint for BLOCK/REPAIR, summary line. Used when `--json` not passed.
- [ ] T026 [US2] Implement `--severity` filter flag — parse comma-separated severity levels, pass to `Engine.lint()` as `severity_filter`. Applied after bundle gate, before output.

**Checkpoint**: All subcommands work. Existing no-subcommand `wiki-lint` unchanged (quickstart V6).

---

## Phase 6: US1 — Agent Lints Generated Output (Priority: P1) 🎯 MVP

**Goal**: Agents call `wiki-lint task <bundle>` against generated output, receive structured findings, repair BLOCK/REPAIR, surface REVIEW, re-lint clean.

**Independent Test**: Generate session-prep with known AGENCY001 violation + CANON002 violation. Run `wiki-lint task session-prep`. Verify structured findings with correct rule IDs, severity, evidence, repair hints. Verify repair resolves both without introducing new violations.

- [ ] T027 [US1] Add repair-loop helper to `tools/creative_lint/engine.py` — `repair_loop(lint_fn, repair_fn, max_iterations=3) -> LintResult` that calls `lint_fn()`, passes BLOCK/REPAIR findings to `repair_fn()`, re-lints changed surface, repeats up to `max_iterations`. Returns final LintResult with `status` reflecting unconverged findings. If not converged after max iterations, remaining findings surfaced at REVIEW for DM.
- [ ] T028 [US1] Validate end-to-end integration — create a test fixture file at `tests/fixtures/creative_lint/integration/session_prep_violations.md` containing authored PC decision ("You decide the risk is worth it") and verify `wiki-lint task session-prep tests/fixtures/creative_lint/integration/session_prep_violations.md --json` returns AGENCY001 at BLOCK with correct evidence and repair_target

**Checkpoint**: Agent integration works end-to-end. US1 acceptance scenarios 1-4 verifiable. MVP complete.

---

## Phase 7: US9 — Rule Fixtures and Testing (Priority: P3)

**Goal**: Every nontrivial rule has fixture files defining its acceptable region: should-fail, should-pass, ambiguous.

**Independent Test**: Create fixtures for AGENCY001. Run fixture harness. Verify should-fail triggers, should-pass doesn't, ambiguous recorded without failing suite.

- [ ] T029 [P] [US9] Create fixture files for static (Vale) rules in `tests/fixtures/creative_lint/` — for each rule: `<RULE_ID>/fail_<desc>.md` (must trigger), `<RULE_ID>/pass_<desc>.md` (must not trigger), `<RULE_ID>/ambiguous_<desc>.md` (recorded, no suite failure). Minimum fixtures: AGENCY001 (fail: "You decide the risk is worth it"; pass: "The shrine entrance stands before you"; ambiguous: "You cautiously enter the shrine"), AGENCY002, AGENCY003, KNOW001, KNOW002, SCENE002
- [ ] T030 [P] [US9] Create fixture files for symbolic rules — CANON001 (fail: NPC with lifecycle: rejected referenced in body; pass: NPC with lifecycle: accepted referenced), WIKI001 (fail: page missing title frontmatter; pass: page with all required frontmatter), WIKI002 (fail: page with type: invalid_type; pass: page with type: npc)
- [ ] T031 [US9] Implement fixture test harness in `tests/test_creative_lint.py` — discover `tests/fixtures/creative_lint/<RULE_ID>/` directories, for each rule: run Vale (for vale rules) or symbolic evaluator (for symbolic rules) against each fixture file, assert `fail_*.md` triggers the rule, `pass_*.md` does not, `ambiguous_*.md` result is recorded but does not fail the test. Use `pytest.mark.parametrize` over discovered fixtures.

**Checkpoint**: `pytest tests/test_creative_lint.py` passes. All active BLOCK rules have both fail and pass fixtures (SC-008).

---

## Phase 8: US7 — Rule Lifecycle and Shadow Mode (Priority: P3)

**Goal**: New rules progress DRAFT → SHADOW → ACTIVE. Shadow mode records findings without affecting agent output.

**Independent Test**: Create a SHADOW rule. Run wiki-lint. Verify finding recorded in shadow telemetry but absent from agent-facing output. Promote to ACTIVE. Verify it appears.

- [ ] T032 [US7] Implement shadow mode in `tools/creative_lint/shadow.py` — `record_shadow(findings: list[Finding], output_dir: Path)` writes per-rule JSON telemetry to `rules/shadow/<RULE_ID>.jsonl` (append). Each entry: finding dict + timestamp. `load_shadow(rule_id, shadow_dir) -> list[dict]` reads telemetry for analysis.
- [ ] T033 [US7] Wire shadow recording into `Engine.lint()` in `tools/creative_lint/engine.py` — after evaluation, separate SHADOW-lifecycle findings from ACTIVE findings. Record SHADOW findings via `record_shadow()`. Return SHADOW findings in `LintResult.shadow` but exclude from `LintResult.findings` and status computation.
- [ ] T034 [US7] Add lifecycle ceiling enforcement — creative-diagnostic rules (`category: scene|diversity`) have lifecycle ceiling of ACTIVE but severity ceiling of WARN. Registry validation already enforces severity ceiling (T009). Add test: promote a scene rule to ACTIVE with severity BLOCK → validation error.

**Checkpoint**: Shadow rules evaluate and record without affecting agent output. DRAFT rules skip entirely.

---

## Phase 9: US8 — Explicit Waivers (Priority: P3)

**Goal**: DM grants explicit, time-boxed waivers for contextually correct violations.

**Independent Test**: Grant waiver for NPC003 on `npc:archivist-vel` expiring session-15. Run wiki-lint. Verify finding suppressed with waiver metadata. Expire waiver. Verify finding reappears. Submit waiver without expiry → rejected.

- [ ] T035 [US8] Implement waiver system in `tools/creative_lint/waivers.py` — `Waiver` dataclass with required fields: `rule_id` (str), `target` (str, format `file:<path>|npc:<name>|session:<N>|*`), `reason` (str), `owner` (str), `granted` (str, ISO date or session ref), `expires` (str, required — no permanent waivers). `WaiverRegistry.load(path)` parses `rules/waivers.json`. `match(finding, current_session=None) -> Waiver|None` checks rule_id exact match + target pattern match against finding location + expiry not passed. `validate() -> list[str]` rejects missing expires.
- [ ] T036 [US8] Wire waiver matching into `Engine.lint()` — after finding generation, check each finding against WaiverRegistry. If matched: set `finding.waiver` to waiver metadata dict, count as `waived` in summary, exclude from status computation. Load waivers from `rules/waivers.json` if file exists (graceful if absent).
- [ ] T037 [US8] Create empty `rules/waivers.json` (empty array `[]`) as initial state

**Checkpoint**: Waived findings suppressed with metadata. No-expiry waivers rejected. Missing waivers file handled gracefully.

---

## Phase 10: US10 — DM Correction Becomes Rule (Priority: P3)

**Goal**: DM corrections classify against existing rules or draft candidates entering SHADOW mode.

**Independent Test**: Record correction "Stop having NPCs know things they couldn't know." Classify as matching KNOW002 or draft new rule. Verify candidate enters SHADOW. Verify shadow telemetry accumulates.

- [ ] T038 [US10] Document candidate-rule workflow in `docs/creative-linting.md` — how DM corrections are recorded (error-ledger entry), how to classify against existing rules (`wiki-lint rule <ID>` to check coverage), how to draft a candidate rule (add to `rules/registry.yml` with `lifecycle: SHADOW`, create Vale YAML or symbolic evaluator, create fixtures), promotion criteria (shadow telemetry: <10% false positive, >90% human agreement per spec).
- [ ] T039 [US10] Add `wiki-lint candidate <correction-text>` subcommand stub in `scripts/wiki-lint` — search registry for rules whose `message` or `tags` overlap with the correction text (simple keyword matching). Print matching rules. If no match, print template for a new SHADOW rule entry in `rules/registry.yml`. Phase 2+ will add LLM-based classification.

**Checkpoint**: Candidate workflow documented. Stub subcommand available for manual use.

---

## Phase 11: Polish & Cross-Cutting Concerns

**Purpose**: Integration with wiki-maintain, documentation, validation

- [ ] T040 [P] Document creative linting in `docs/creative-linting.md` — architecture (three-layer), rule families, severity model, bundle configuration, CLI usage, agent integration pattern, fixture authoring, waiver granting, shadow mode promotion
- [ ] T041 [P] Add `.gitignore` entry for `rules/shadow/` directory (telemetry is local, not version-controlled)
- [ ] T042 Run quickstart.md validation scenarios V1–V8 end-to-end
- [ ] T043 Verify existing `wiki-lint` (no subcommand) behavior unchanged — run `./scripts/wiki-lint --json wiki` and confirm output schema matches pre-change baseline

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — start immediately
- **Foundational (Phase 2)**: Depends on Setup — BLOCKS all user stories
- **US6 (Phase 3)**: Depends on Phase 2 (registry + severity + finding schema)
- **US5 (Phase 4)**: Depends on Phase 2 (registry). Can parallel with US6.
- **US2 (Phase 5)**: Depends on Phase 3 (engine) and Phase 4 (bundles)
- **US1 (Phase 6)**: Depends on Phase 5 (CLI). MVP checkpoint.
- **US9 (Phase 7)**: Depends on Phase 3 (evaluators). Can parallel with Phases 5-6.
- **US7 (Phase 8)**: Depends on Phase 3 (engine). Can parallel with Phases 5-7.
- **US8 (Phase 9)**: Depends on Phase 3 (engine). Can parallel with Phases 5-8.
- **US10 (Phase 10)**: Depends on Phase 5 (CLI rule subcommand)
- **Polish (Phase 11)**: Depends on all desired stories complete

### User Story Dependencies

- **US3+US4 (Foundational)**: No story dependencies — blocks everything
- **US6**: Needs registry (US3). Independent of US5.
- **US5**: Needs registry (US3). Independent of US6.
- **US2**: Needs engine (US6) + bundles (US5). The core CLI.
- **US1**: Needs CLI (US2). Validates the whole pipeline.
- **US9**: Needs evaluators (US6). Independent of US2/US1.
- **US7**: Needs engine (US6). Independent of US2/US1.
- **US8**: Needs engine (US6). Independent of US2/US1.
- **US10**: Needs CLI (US2). Lightweight.

### Within Each Phase

- Models/dataclasses before services
- Services before CLI
- Infrastructure before integration

### Parallel Opportunities

- T002, T003, T004, T005 in Phase 1 (all different files)
- T007, T008 in Phase 2 (severity.py and finding.py are independent)
- T012, T013, T014 in Phase 3 (Vale rules, Vale adapter, symbolic evaluator — all different files)
- US5 and US6 can run in parallel after Phase 2
- T022, T023 in Phase 5 (corpus and changed subcommands)
- US7, US8, US9 can all run in parallel after Phase 3
- T029, T030 in Phase 7 (Vale fixtures, symbolic fixtures)
- T040, T041 in Phase 11

---

## Parallel Example: Phase 3 (US6)

```
# Launch all evaluator implementations together:
Task T012: "Create Vale rule YAML files in styles/CoDM/"
Task T013: "Implement Vale adapter in tools/creative_lint/vale_adapter.py"
Task T014: "Implement symbolic evaluator in tools/creative_lint/evaluators/symbolic.py"

# Then sequentially:
Task T015: "Implement engine orchestrator in tools/creative_lint/engine.py" (depends on T012-T014)
```

---

## Implementation Strategy

### MVP First (Phase 1 → Phase 6)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (US3 + US4)
3. Complete Phase 3: US6 (Evaluator Types)
4. Complete Phase 4: US5 (Bundles) — can parallel with Phase 3
5. Complete Phase 5: US2 (CLI)
6. Complete Phase 6: US1 (Agent Integration)
7. **STOP and VALIDATE**: Run quickstart.md scenarios V1–V8
8. MVP delivers: rule registry, Vale + symbolic evaluators, bundles, CLI with all subcommands, agent integration

### Incremental Delivery

1. Setup + Foundational → Registry works, rules defined
2. Add US6 + US5 → Engine runs, bundles resolve
3. Add US2 → CLI works end-to-end → **Demo**
4. Add US1 → Agents can lint and repair → **MVP!**
5. Add US9 → Fixtures provide regression safety
6. Add US7 → Shadow mode for new rules
7. Add US8 → Waivers for contextual exceptions
8. Add US10 → Learning loop from DM corrections
9. Polish → docs, wiki-maintain integration, validation

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Existing `scripts/wiki-lint` (no subcommand) behavior MUST remain unchanged throughout
- Vale invoked as subprocess — no Python Vale binding needed
- `tools/lint_wiki.py` is NOT modified — symbolic evaluator wraps its output
- `rules/shadow/` is gitignored (local telemetry)
- All rules start at lifecycle ACTIVE except when testing shadow mode
