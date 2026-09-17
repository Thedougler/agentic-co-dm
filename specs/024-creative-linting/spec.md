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

New rules progress through a lifecycle: DRAFT → SHADOW → WARN → REPAIR → BLOCK. Not every rule reaches BLOCK. Shadow mode records what would have triggered without affecting agent behavior. Promotion from shadow to active depends on measured precision (false-positive rate, human agreement, repair helpfulness), not confidence in the rule's wording.

**Why this priority**: Shadow deployment prevents untested rules from disrupting production sessions. Measured promotion prevents rules from accumulating that don't actually help.

**Independent Test**: Create a rule in SHADOW state. Run wiki-lint against content that would trigger it. Verify the finding is recorded in shadow telemetry but does not appear in the active findings returned to the agent. Promote the rule to WARN. Verify it now appears in active findings.

**Acceptance Scenarios**:

1. **Given** a rule in SHADOW state, **When** wiki-lint runs, **Then** the rule evaluates and records results but the finding does not appear in the agent-facing output.
2. **Given** shadow telemetry showing 90%+ human agreement and <10% false positive rate, **When** the rule is promoted to WARN, **Then** it appears in active findings on subsequent runs.
3. **Given** a creative diagnostic rule, **When** its lifecycle is assessed, **Then** it can reach WARN but never BLOCK (creative diagnostics have a lifecycle ceiling).

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

---

### Edge Cases

- What happens when two rules conflict (e.g., STYLE012 "be concise" vs. SCENE008 "establish environmental context")? The engine detects the conflict and surfaces it as LINT-CONFLICT with precedence guidance; the agent chooses based on scene purpose.
- What happens when a rule's evaluator is unavailable (e.g., LLM judge during CI without API access)? The rule is skipped with a recorded `evaluator_unavailable` status; it does not silently pass.
- What happens when the initial rule set is incomplete and a violation type has no rule? The violation goes undetected. The error-ledger convergence (Story 10) provides the path to close the gap.
- What happens when a repair introduces a new violation? The re-lint loop detects it. The repair loop has a configurable maximum iteration count to prevent infinite repair cycles.
- What happens when portfolio-level diversity diagnostics flag a pattern across sessions? The INFO finding surfaces the pattern for the next session's design without requiring retroactive changes to existing content.

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
- **FR-013**: Rule conflicts MUST be detectable and surfaced when two rules in the same bundle pull in opposing directions
- **FR-014**: The initial rule set MUST cover six families: wiki/structural, canon/world-state, temporal/knowledge, player agency, retrieval/context, and creative diagnostics
- **FR-015**: The linter MUST integrate with `wiki-maintain` as a corpus-level consumer using the same rule implementations as live agent operation
- **FR-016**: BLOCK severity MUST correlate only with truth, safety, agency, schema, or deterministic process — not subjective taste

### Key Entities

- **Rule**: A lint rule with stable ID, category, scope, severity, evaluator type, message, repair guidance, lifecycle state, and optional conflict/dependency declarations
- **Finding**: A structured result from evaluating a rule against content — includes rule ID, result, severity, location, evidence, reason, and repair target
- **Bundle**: A named collection of rule categories scoped to a task type, with per-category severity gates (block, review, diagnostics)
- **Waiver**: A time-boxed, explicit suppression of a specific rule for a specific target, with owner and reason
- **Evaluator**: A typed execution strategy for a rule (static, symbolic, retrieval, semantic/LLM, human)
- **Fixture**: A test case for a rule — should-fail, should-pass, or ambiguous — used for regression and precision measurement

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

## Assumptions

- The existing `wiki-maintain`, QMD, `error-ledger.py`, quality invariants, Spec Kit workflow, and deterministic wiki tooling are preserved — the linter is a cross-cutting validation layer, not a replacement
- Phase 1 (infrastructure + static evaluators) ships before any LLM-based evaluators are introduced
- The initial rule set targets ~15 high-value rules across six families, not comprehensive coverage
- Semantic/LLM evaluators require API access and are skipped gracefully in environments without it (CI, offline)
- Rule definitions live in repository-owned YAML files, not in agent prompts or skill instructions
- The DM remains the authority over canon and taste — the linter surfaces findings but does not autonomously redefine either
- Portfolio-level diversity diagnostics (DIVERSITY*) operate at INFO severity and inform future design without requiring retroactive changes
