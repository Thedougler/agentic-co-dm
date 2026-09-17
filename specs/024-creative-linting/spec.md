# Feature Specification: Creative Linting

**Feature Branch**: `024-creative-linting`

**Created**: 2026-09-17

**Status**: Draft

**Input**: User description: "Creative Linting Implementation Guide — executable lint rules for canon, agency, temporal truth, knowledge boundaries, retrieval discipline, and creative heuristics as a cross-cutting validation layer over the existing agentic-co-dm architecture"

## User Scenarios & Testing *(mandatory)*

### User Story 1 — Agent Lints Generated Output (Priority: P1)

An agent generates session prep, narration, encounter design, or other campaign Work. Before returning the result, the agent runs `wiki-lint` against the output using the task-appropriate rule bundle. The linter returns structured findings with stable rule IDs, severity levels, evidence, and repair hints. The agent repairs all BLOCK and REPAIR findings, surfaces REVIEW findings for DM judgment, and does not mechanically optimize away WARN or INFO findings. The repaired output re-lints clean of blocking issues.

**Why this priority**: This is the core loop — executable rules replacing prose guidance. Without it, the linter has no consumer.

**Independent Test**: Generate a session-prep artifact containing a known AGENCY violation (authored PC decision) and a known CANON violation (stale entity state). Run `wiki-lint task session-prep`. Verify structured findings identify both with correct rule IDs, severity, evidence, and repair hints. Verify a repair pass resolves both without introducing new violations.

**Acceptance Scenarios**:

1. **Given** a session-prep output containing "You decide the risk is worth it and enter the shrine," **When** the agent runs `wiki-lint` with the `session-prep` bundle, **Then** the linter returns a BLOCK finding for AGENCY001 with the offending text as evidence and a repair hint that preserves the situation while removing the authored decision.
2. **Given** a session-prep output referencing an NPC as alive when canon records them as dead, **When** the agent runs `wiki-lint`, **Then** the linter returns a REPAIR finding for CANON002 with the contradicting canonical source as evidence.
3. **Given** an output with no blocking or repairable findings but a WARN for SCENE001 (no actionable situation), **When** the agent runs `wiki-lint`, **Then** the linter returns status `clean` with the WARN surfaced as a diagnostic, and the agent is not required to alter the output.
4. **Given** a repair pass that fixes AGENCY001, **When** the agent re-lints only the changed surface, **Then** the previously-blocked finding no longer appears and no new BLOCK findings are introduced.

---

### User Story 2 — wiki-lint CLI for Files and Corpus (Priority: P1)

A human or agent runs `wiki-lint` from the command line against individual files, changed files, task profiles, specific rules, or the full corpus. The CLI produces structured JSON output for agents and human-readable output for terminals. Findings use one consistent schema across all execution surfaces.

**Why this priority**: The CLI is the single entry point for all lint consumers — agents, wiki-maintain, CI, and humans.

**Independent Test**: Run `wiki-lint file <path>` against a wiki page with missing required frontmatter. Verify JSON output contains a WIKI001 finding with correct schema. Run `wiki-lint --json` and verify parseable structured output. Run without `--json` and verify human-readable rendering.

**Acceptance Scenarios**:

1. **Given** a wiki page missing the `title` frontmatter field, **When** running `wiki-lint file <path>`, **Then** the output contains a WIKI001 finding with severity BLOCK, the file path, and a message identifying the missing field.
2. **Given** `wiki-lint corpus` is run, **Then** all wiki pages are checked against the corpus-level rule bundle and findings are aggregated with a summary count per severity level.
3. **Given** `wiki-lint changed` is run, **Then** only files changed since the last lint run or commit are checked.
4. **Given** `wiki-lint rule AGENCY001` is run, **Then** the output describes the rule: its ID, title, category, severity, scope, evaluator type, message, and repair guidance.
5. **Given** `wiki-lint --severity block,repair` is run, **Then** only findings at BLOCK or REPAIR severity appear in output.

6. **Given** the repository root, **When** an agent inspects `package.json` or runs `npm run`, **Then** the documented common operations are discoverable as thin aliases to the existing repository CLIs; the aliases add no duplicate implementation, preserve delegated exit status and output streams, and do not require Node runtime dependencies beyond npm's script runner.
7. **Given** the existing `wiki-lint` CLI is run with `--consolidate`, **When** the command evaluates the corpus, **Then** it emits a structured dry-run action list and requires explicit approval before applying safe structural repairs; without that flag, existing report-only behavior remains unchanged.

---

### User Story 3 — Rule Registry and Stable IDs (Priority: P1)

Each lint rule has a stable ID (format: `CATEGORY` + zero-padded number, e.g., `WIKI001`, `AGENCY001`, `CANON002`), a single canonical definition, and metadata including category, scope, severity, evaluator type, message, and repair guidance. Skills and `AGENTS.md` reference rules by ID rather than duplicating rule prose.

**Why this priority**: Stable IDs are the foundation — findings, waivers, bundles, fixtures, and the learning loop all reference them. Without this, no other capability works.

**Independent Test**: Add a rule definition to the registry. Verify it is discoverable by ID. Verify `wiki-lint rule <ID>` returns its full definition. Verify a skill can reference the rule by ID without embedding its logic.

**Acceptance Scenarios**:

1. **Given** a rule defined with ID `CANON001`, **When** any consumer queries the registry for `CANON001`, **Then** the full rule definition (title, category, scope, severity, evaluator, message, repair) is returned.
2. **Given** two rules with the same ID are added, **When** the registry loads, **Then** it rejects the duplicate with a clear error.
3. **Given** a skill references rule bundle `session-prep`, **When** the bundle is resolved, **Then** it expands to the set of rule IDs configured for that bundle, not inline prose.

---

### User Story 4 — Five-Level Severity Model (Priority: P2)

Findings use a five-level severity model designed for creative work: BLOCK (objective invariant violated — must repair), REPAIR (high-confidence defect — auto-repair then re-test), REVIEW (probably problematic but contextual — repair or justify), WARN (creative diagnostic — consider during revision), INFO (observation — no required action). BLOCK correlates only with truth, safety, agency, schema, or deterministic process. Taste never BLOCKs.

**Why this priority**: The severity model determines which findings require agent action versus inform creative judgment. Getting this wrong either blocks creative diversity or misses real defects.

**Independent Test**: Define one rule at each severity level. Run wiki-lint against content that triggers all five. Verify the output correctly categorizes agent-required actions (BLOCK/REPAIR must-fix, REVIEW justify-or-fix) separately from diagnostics (WARN/INFO no mandate).

**Acceptance Scenarios**:

1. **Given** a finding at BLOCK severity, **When** the lint result is evaluated, **Then** the status is `repair_required` and the agent must repair before completion.
2. **Given** only WARN and INFO findings, **When** the lint result is evaluated, **Then** the status is `clean` and the agent is not required to alter the output.
3. **Given** a creative rule proposing BLOCK severity for a subjective judgment (e.g., "narration should be concise"), **When** reviewed against the severity model, **Then** it is rejected or downgraded because taste must not BLOCK.

---

### User Story 5 — Task-Specific Rule Bundles (Priority: P2)

Rules are grouped into named bundles scoped to task types (e.g., `session-prep`, `wiki-ingest`, `worldbuilding`, `live-codm`). Each bundle specifies which rule categories apply at which severity gate (block, review, diagnostics). Running `wiki-lint task <task-type>` activates only the bundle's rules, preventing the entire rule universe from running on every task.

**Why this priority**: Bundles control lint scope and token cost per task. Without them, agents either run too many rules or too few.

**Independent Test**: Define a `session-prep` bundle with canon, temporal, and agency rules at block level, encounter and hook at review, and scene and diversity as diagnostics. Run `wiki-lint task session-prep` and verify only bundled rules execute. Run `wiki-lint task wiki-ingest` and verify a different bundle applies.

**Acceptance Scenarios**:

1. **Given** a `session-prep` bundle configured with AGENCY rules at block, **When** `wiki-lint task session-prep` runs against content with an AGENCY001 violation, **Then** the finding appears at BLOCK severity.
2. **Given** the same content run against `wiki-ingest` bundle which does not include AGENCY rules, **When** `wiki-lint task wiki-ingest` runs, **Then** no AGENCY finding appears.
3. **Given** a rule category included as `diagnostics` in a bundle, **When** that rule fires, **Then** its findings appear at WARN or INFO severity regardless of the rule's standalone severity.

---

### User Story 6 — Multiple Evaluator Types (Priority: P2)

The lint engine dispatches each rule to the cheapest and most deterministic evaluator capable of answering the question. Evaluator types include: static (regex, schema, path validation), symbolic (graph, state, chronology), retrieval/evidence (canon support, citations), and — in later phases — LLM judge (agency, narrative diagnostics) and human (taste, ambiguous canon). All evaluator types share the same finding output contract.

**Why this priority**: Deterministic evaluators handle the majority of rules cheaply. LLM evaluators are reserved for rules that require semantic understanding. The shared contract means consumers don't care which evaluator produced a finding.

**Independent Test**: Define WIKI001 (static evaluator — missing frontmatter) and AGENCY001 (semantic evaluator — authored PC decision). Run both. Verify findings from both evaluator types share the same schema. Verify the static evaluator runs without any LLM call.

**Acceptance Scenarios**:

1. **Given** a rule with evaluator type `static`, **When** it runs, **Then** no LLM call is made and the finding follows the standard schema.
2. **Given** a rule with evaluator type `semantic`, **When** the evaluator cannot determine pass/fail with confidence, **Then** it returns `abstain` rather than manufacturing certainty.
3. **Given** findings from static and semantic evaluators, **When** compared, **Then** both conform to the same JSON schema (rule_id, result, severity, location, evidence, reason, repair_target).

---

### User Story 7 — Rule Lifecycle and Shadow Mode (Priority: P3)

New rules progress through a deployment lifecycle: DRAFT → SHADOW → ACTIVE. Severity is a separate rule attribute with values BLOCK, REPAIR, REVIEW, WARN, or INFO; promotion to ACTIVE does not imply a severity. Shadow mode records what would have triggered without affecting agent behavior. Promotion from shadow to active depends on measured precision (false-positive rate, human agreement, repair helpfulness), not confidence in the rule's wording.

**Why this priority**: Shadow deployment prevents untested rules from disrupting production sessions. Measured promotion prevents rules from accumulating that don't actually help.

**Independent Test**: Create a rule in SHADOW state with severity WARN. Run wiki-lint against content that would trigger it. Verify the finding is recorded in shadow telemetry but does not appear in the active findings returned to the agent. Promote the rule to ACTIVE without changing its severity. Verify it now appears in active findings with WARN severity.

**Acceptance Scenarios**:

1. **Given** a rule in SHADOW state, **When** wiki-lint runs, **Then** the rule evaluates and records results but the finding does not appear in the agent-facing output.
2. **Given** shadow telemetry showing 90%+ human agreement and <10% false positive rate, **When** the rule is promoted to ACTIVE, **Then** it appears in active findings on subsequent runs with its independently configured severity.
3. **Given** a creative diagnostic rule, **When** its severity is assessed, **Then** it can reach WARN but never BLOCK (creative diagnostics have a severity ceiling).


---

### User Story 8 — Explicit Waivers (Priority: P3)

When a violation is correct in context, the DM can grant an explicit waiver for a specific rule + target combination. Waivers require: rule ID, scope/target, reason, owner (who approved), and expiry. No permanent anonymous suppressions. Waivers are stored in a repository-owned configuration file.

**Why this priority**: Without waivers, agents must either violate rules that are contextually correct or produce worse creative output to satisfy them.

**Independent Test**: Grant a waiver for NPC003 on a specific NPC. Run wiki-lint against that NPC page. Verify the finding is suppressed with waiver metadata. Let the waiver expire. Verify the finding reappears.

**Acceptance Scenarios**:

1. **Given** a waiver for rule NPC003 targeting `npc:archivist-vel` expiring at session-15, **When** wiki-lint runs before session-15, **Then** the NPC003 finding for that NPC is suppressed and the waiver reason is recorded.
2. **Given** the same waiver after session-15, **When** wiki-lint runs, **Then** the finding reappears because the waiver has expired.
3. **Given** a waiver without an expiry, **When** it is submitted, **Then** the system rejects it — all waivers must have an expiry.

---

### User Story 9 — Rule Fixtures and Testing (Priority: P3)

Every nontrivial rule has fixture files that define its acceptable region: should-fail cases, should-pass cases, and ambiguous cases. For creative rules, counterexamples (things that should pass despite seeming like violations) are as important as positive examples.

**Why this priority**: Fixtures are the regression safety net. Without them, rule changes can silently expand or contract the acceptable region.

**Independent Test**: Create fixtures for AGENCY001: a should-fail ("You decide the risk is worth it"), a should-pass ("You enter the shrine"), and an ambiguous case ("You cautiously enter the shrine"). Run the fixture harness. Verify should-fail triggers the rule, should-pass does not, and ambiguous is recorded for human review.

**Acceptance Scenarios**:

1. **Given** a should-fail fixture for AGENCY001, **When** the fixture harness runs, **Then** the rule fires and the test passes.
2. **Given** a should-pass fixture for AGENCY001, **When** the fixture harness runs, **Then** the rule does not fire and the test passes.
3. **Given** a fixture marked ambiguous, **When** the fixture harness runs, **Then** the result is recorded but does not cause the test suite to fail.

---

### User Story 10 — DM Correction Becomes Rule (Priority: P3)

When the DM makes a correction that addresses a recurring agent failure, the system can classify it against existing rules or draft a candidate rule. Candidate rules enter SHADOW mode for measured evaluation before promotion. One correction becomes a permanent improvement to the system.

**Why this priority**: This is the long-term learning loop. Without it, the DM repeats the same corrections across sessions.

**Independent Test**: Record a DM correction ("Stop having NPCs know things they couldn't know"). Classify it as matching KNOW002 or as a candidate new rule. Verify it enters shadow mode. Verify shadow telemetry accumulates. Verify promotion path is available when precision thresholds are met.

**Acceptance Scenarios**:

1. **Given** a recurring DM correction that maps to an existing rule KNOW002, **When** classified, **Then** the existing rule's evaluator is reviewed for improvement rather than creating a duplicate.
2. **Given** a recurring DM correction with no existing rule, **When** a candidate rule is drafted, **Then** it enters SHADOW state with fixtures and begins accumulating telemetry.
3. **Given** a candidate rule with insufficient precision in shadow mode, **When** promotion is considered, **Then** it remains in SHADOW until thresholds are met — it is not promoted on confidence alone.


### User Story 11 — Bulk Wiki Cleanup Queue (Priority: P1)

An agent faces a bulk wiki-lint sitting. It does not re-derive an order. It asks `wiki-lint` for the dirty-file queue, which lists pages that still have **safe automatic** findings, smallest-first. Default bulk work is unattended: apply only those safe automatic repairs, re-lint the file, then take the next. Completing the whole corpus is not required. Judgment-only or creative repairs are out of the default loop.

**Why this priority**: Corpus reports alone leave agents inventing order and stopping rules. Bulk cleanup is a primary consumer of the linter and must be an objective, repeatable, autonomous procedure for safe fixes.

**Independent Test**: Seed two pages of different byte sizes that each have one safe automatic finding. Run the bulk queue command. Verify the smaller file is first. Apply the safe repair, re-run the queue, and verify that file is absent and the larger dirty file is now first. Verify a page whose only findings need judgment is not treated as default-queue dirty. Verify the command does not fail solely because other dirty files remain.

**Acceptance Scenarios**:

1. **Given** two pages with safe automatic findings and different sizes, **When** the agent requests the bulk dirty-file queue, **Then** `wiki-lint` returns those paths ordered smallest-first as structured output.
2. **Given** the agent has applied safe automatic repairs so the current head-of-queue file has none left, **When** it requests the queue again, **Then** that file is absent and the next smallest default-dirty file is first.
3. **Given** default-dirty files remain after a sitting, **When** the agent stops, **Then** remaining files stay in the queue for a later sitting and the sitting is not a failure solely for incompleteness.
4. **Given** a page whose remaining findings all require judgment, **When** the default bulk queue is requested, **Then** that page is omitted from the default queue.

---

### User Story 12 — Template-Derived Conformance (Priority: P1)

The linter detects wiki pages that drift from their current template without maintaining a second hardcoded checklist for each template. It selects the applicable template from the page’s current `type` and `kind` mapping, derives a generic template profile from the template file, and compares the page against that profile. The profile covers the template’s current frontmatter shape, heading/layout tree, section order, callout forms, table structure, and formatting markers. Template changes automatically change the comparison baseline.

**Why this priority**: Template drift is a major source of wiki quality degradation. The linter must follow the live templates rather than fossilizing their requirements in implementation code.

**Independent Test**: Create a page mapped to a template with a deliberately missing section and a mismatched formatting construct. Run template conformance lint and verify structured findings identify the template, page location, and mismatch. Change the template by adding a section, re-run without changing the detector, and verify the new mismatch is reported. Verify no per-template hardcoded rule is required.

**Acceptance Scenarios**:

1. **Given** a wiki page with a resolvable `type`/`kind` template mapping, **When** template conformance lint runs, **Then** it compares the page with the current template-derived profile and reports structural or formatting mismatches with locations.
2. **Given** the selected template’s headings or formatting markers change, **When** lint runs again, **Then** the expected profile changes with the template and the page is evaluated against the new layout without code changes.
3. **Given** a page has intentionally omitted an optional or empty template section, **When** conformance lint runs, **Then** it does not report that omission as a mismatch when the template’s current omission convention permits it.
4. **Given** a page has a template-conformance mismatch, **When** default bulk lint runs, **Then** the linter applies the generic template-derived structural or formatting repair automatically and re-lints the page.

---




## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Rules MUST have stable IDs in the format `CATEGORY` + zero-padded number (e.g., `WIKI001`, `AGENCY001`)
- **FR-002**: All findings MUST use one JSON schema: `rule_id`, `result` (pass/fail/abstain), `severity`, `location`, `evidence`, `reason`, `repair_target`
- **FR-003**: Deterministic and semantic evaluators MUST share the same finding output contract
- **FR-004**: Task-specific bundles MUST exist and MUST be configurable in a repository-owned YAML file
- **FR-005**: Blocking findings (BLOCK, REPAIR) MUST prevent agent completion until repaired
- **FR-006**: Warnings (WARN, INFO) MUST NOT silently become requirements — agents MUST NOT be forced to optimize away diagnostic findings
- **FR-007**: Semantic evaluators MUST support ABSTAIN as a valid result alongside PASS and FAIL
- **FR-008**: Every repair MUST be traceable to a specific finding by rule ID and location
- **FR-009**: Waivers MUST be explicit (rule ID, scope, reason, owner) and MUST expire
- **FR-010**: Rules MUST support shadow deployment (evaluate and record without affecting agent output)
- **FR-011**: The `wiki-lint` CLI MUST produce structured JSON output for agents and human-readable output for terminals
- **FR-012**: Rule definitions MUST be the single source of truth — skills and `AGENTS.md` MUST reference rules by ID, not duplicate rule prose
- **FR-014**: The initial rule set MUST cover six families: wiki/structural, canon/world-state, temporal/knowledge, player agency, retrieval/context, and creative diagnostics
- **FR-015**: The linter MUST integrate with `wiki-maintain` as a corpus-level consumer using the same rule implementations as live agent operation
- **FR-016**: BLOCK severity MUST correlate only with truth, safety, agency, schema, or deterministic process — not subjective taste
- **FR-017**: Static and structural lint rules MUST use off-the-shelf linting tools (Vale for prose patterns, using the packages declared in the repository's `.vale.ini`, and markdownlint-cli2 for markdown structure) rather than custom regex engines. Custom Python evaluators are permitted only for cross-page symbolic checks that no off-the-shelf tool supports.
- **FR-018**: All lint tool configurations MUST be agent-readable and agent-writable (YAML/JSON/INI files, not programmatic). Agents MUST be able to inspect and modify rule definitions, bundle configurations, and waivers through standard file operations.
- **FR-019**: The repository MUST provide a `package.json` with discoverable `scripts` aliases for common linting, maintenance, verification, and test operations; each alias MUST delegate directly to the existing agent-shaped command, preserve its arguments, stdout, stderr, and exit status, and MUST NOT duplicate operation logic in Node code.
- **FR-020**: Rule deployment lifecycle (`DRAFT`, `SHADOW`, `ACTIVE`) MUST remain independent from finding severity (`BLOCK`, `REPAIR`, `REVIEW`, `WARN`, `INFO`); promotion to `ACTIVE` MUST NOT implicitly change severity.
- **FR-021**: The `wiki-lint --consolidate` mode MUST preserve report-only behavior by default, emit a structured dry-run plan before writes, and require explicit approval before applying safe structural repairs.
- **FR-022**: The `wiki-lint` CLI MUST emit a bulk dirty-file queue of wiki pages that still have safe automatic findings, ordered smallest-first, as structured output. Default bulk work MUST apply only those safe automatic repairs, unattended. Agents MUST take one file at a time from the head of that queue, leave that file free of remaining safe automatic findings before taking the next, and MUST NOT be required to empty the queue in one sitting. Judgment-only repairs MUST NOT be part of the default bulk loop. Template-conformance repairs derived from the current template profile are safe automatic repairs.
- **FR-023**: Template-conformance lint MUST derive a generic comparison profile from the currently selected `wiki/templates/*.md` file using the page's `type` and `kind` mapping. It MUST compare current template frontmatter shape, heading/layout tree, section order, callout forms, table structure, and formatting markers against the wiki page, report mismatches with locations and the selected template, and MUST NOT encode per-template requirements or duplicate template rules in code. A changed template MUST change the comparison baseline without a detector code change. Every repair produced from that comparison MUST be safe to apply automatically.


### Key Entities

- **Rule**: A lint rule with stable ID, category, scope, independently configured severity, evaluator type, message, repair guidance, deployment lifecycle state, and optional conflict/dependency declarations
- **Finding**: A structured result from evaluating a rule against content — includes rule ID, result, severity, location, evidence, reason, and repair target
- **Bundle**: A named collection of rule categories scoped to a task type, with per-category severity gates (block, review, diagnostics)
- **Waiver**: A time-boxed, explicit suppression of a specific rule for a specific target, with owner and reason
- **Evaluator**: A typed execution strategy for a rule (static, symbolic, retrieval, semantic/LLM, human)
- **Fixture**: A test case for a rule — should-fail, should-pass, or ambiguous — used for regression and precision measurement
- **Dirty-file queue**: Ranked list of wiki pages that still have safe automatic findings, ordered smallest-first, produced by `wiki-lint` rather than by the agent
- **Template profile**: Generic, runtime-derived structural and formatting model extracted from the currently selected template file; it is not a second per-template ruleset

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Agents can lint generated output and receive structured, actionable findings in under 10 seconds for deterministic rules
- **SC-002**: Canon violations (stale state, contradictions) detected by the linter before DM review decrease DM correction rate for those violation types by 50%+ within 3 sessions of activation
- **SC-003**: Player-agency violations (authored PC decisions, prescribed solutions) detected by the linter reach zero in BLOCK-level findings within 2 repair iterations
- **SC-004**: Skill instruction payload decreases measurably when skills reference rule bundles by ID instead of embedding rule prose
- **SC-005**: Creative output does not converge toward fixture phrasing — portfolio-level diversity diagnostics confirm variety is maintained or improving across sessions
- **SC-006**: False-positive rate for promoted rules stays below 15% as measured by DM agreement in shadow telemetry
- **SC-007**: Total linter token overhead (lint + repair calls) is attributable and does not exceed 20% of the generation cost it validates
- **SC-008**: 100% of active BLOCK rules have passing fixture suites with both should-fail and should-pass cases
- **SC-009**: A bulk sitting can obtain a smallest-first default dirty-file queue, apply only safe automatic repairs to one or more files from the head of that queue, and stop with remaining default-dirty files still listed — without treating incompleteness as failure
- **SC-010**: When a template changes its layout or formatting markers, template-conformance lint reports the resulting mismatch on a page mapped to that template without any detector-code or per-template-rule change.

## Assumptions

- The existing `wiki-maintain`, QMD, `error-ledger.py`, quality invariants, Spec Kit workflow, and deterministic wiki tooling are preserved — the linter is a cross-cutting validation layer, not a replacement
- Phase 1 (infrastructure + static evaluators) ships before any LLM-based evaluators are introduced
- The initial rule set targets ~15 high-value rules across six families, not comprehensive coverage
- Semantic/LLM evaluators require API access and are skipped gracefully in environments without it (CI, offline)
- Rule definitions live in repository-owned YAML files, not in agent prompts or skill instructions
- The DM remains the authority over canon and taste — the linter surfaces findings but does not autonomously redefine either
- Portfolio-level diversity diagnostics (DIVERSITY*) operate at INFO severity and inform future design without requiring retroactive changes
- Off-the-shelf linting tools are preferred over custom implementations wherever feasible. Vale handles prose-pattern rules through the package set declared in the repository's `.vale.ini` (`ai-tells`, `proselint`, and `Readability`); markdownlint-cli2 handles structural markdown rules. Together they subsume the custom Python lint scripts (`lint-obsidian-markdown`, `lint-literal-newlines`). Custom Python evaluators are reserved for cross-page symbolic checks that no off-the-shelf tool supports.
- Existing custom lint scripts (`scripts/lint-obsidian-markdown`, `scripts/lint-literal-newlines`, `scripts/lint-wiki-write`) are ported to Vale/markdownlint rules with passing fixtures, then deprecated and removed. They remain functional until the port is complete.

## Clarifications

### Session 2026-09-17

- Q: Which additional off-the-shelf linters beyond Vale should we integrate? → A: Install markdownlint-cli2 for structural markdown rules (heading levels, lists, code fences). Vale handles prose patterns. Together they subsume `lint-obsidian-markdown` and `lint-literal-newlines`.
- **Q: Which repairs count as safe automatic for the default bulk queue?** → **A:** Structural and format-only repairs that cannot invent facts or rewrite narrative prose, including template-conformance repairs derived from the current template profile, literal-newline normalization, unique broken-link retargets, and markdownlint auto-fixes. Missing metadata, canon state, agency, and prose rewrites remain judgment work.
- Q: How should template conformance remain flexible as templates evolve? → A: Derive a generic comparison profile at runtime from the current template selected by `type` and `kind`; do not maintain separate hardcoded requirements for individual templates.
- Q: Should existing custom Python lint scripts be deprecated once ported to Vale/markdownlint? → A: Port then deprecate. Existing scripts stay until all checks ported with passing fixtures, then removed.
- Q: Should the repair loop have a maximum iteration limit, and if so, what default? → A: 3 iterations max (configurable). Unconverged findings surface for DM review.
- Q: Should the package entry point use thin npm aliases rather than new Node wrappers? → A: Add `package.json` scripts that delegate directly to existing repository CLIs; do not move logic into Node or add a second wrapper implementation.
- Q: Should rule lifecycle and finding severity be separate dimensions? → A: Use lifecycle `DRAFT → SHADOW → ACTIVE`; keep severity independently configured as `BLOCK`, `REPAIR`, `REVIEW`, `WARN`, or `INFO`. Promotion to `ACTIVE` does not imply a severity.
- Q: Should Vale-backed prose rules use the packages already declared in `.vale.ini` as the authoritative package set, without duplicating or replacing that package list? → A: Treat `.vale.ini` as authoritative; invoke Vale through its configured `ai-tells`, `proselint`, and `Readability` packages without duplicating package configuration.
- Q: Should the creative-linting feature add a backward-compatible `--consolidate` mode to `scripts/wiki-lint`? → A: Add it to `wiki-lint`; preserve report-only behavior by default, show a dry-run plan, and require explicit approval before safe structural repairs.
- Q: Should bulk wiki cleanup get a CLI that lists dirty files smallest-first, or only a written agent procedure over the existing corpus report? → A: `wiki-lint` emits dirty files smallest-first as a queue; the agent cleans one file, then takes the next until a quality stop. Completing the corpus in one sitting is not required.
- Q: Which findings put a wiki page on the smallest-first dirty queue, and when may the agent leave that page and take the next? → A: Default bulk work is safe automatic fixes only and may run unattended. A page is default-dirty if it has remaining safe automatic findings; it leaves the default queue when a re-lint of that file has none. Judgment-only findings are not a default bulk mandate.
- Q: Should template-conformance findings be excluded from autonomous bulk cleanup because they require review? → A: No. All template-conformance mismatches are safe automatic repairs and belong in the default smallest-first autonomous queue.
