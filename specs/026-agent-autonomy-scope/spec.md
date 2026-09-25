# Feature Specification: Agent Autonomy Scope

> Replaced by feature 030 (FR-018): this feature's agent-standards checker and its three rules are retired. Agent behavior is checked by `scripts/luna-eval` evals (the Work-gate wording case is in `tests/test_luna_eval.py`) and wiki structure by `wiki lint`; the placement and spec-citation rules have no current checker.

**Feature Branch**: `026-agent-autonomy-scope`

**Created**: 2026-09-18

**Status**: Draft

**Input**: User description: "Greater agent autonomy for routine wiki tasks; DM approval only for collaborative creative work; project identity as agent infrastructure not shipped software"

## Clarifications

### Session 2026-09-18

- Q: After an agent finishes routine wiki maintenance with no approval needed, what should the DM see in the conversation? → A: One short done-summary (what changed, where). No question, no wait.
- Q: When a reviewer looks at a change to an agent skill or instruction file, where must the “did the agent behave better?” check live? → A: Existing skill-eval method (held-out prompts, with-skill vs without-skill, graded assertions). No new checklist, PR template, or review skill.
- Q: When one request mixes routine cleanup with new creative content, in what order should the agent do the two parts? → A: Do both. User-requested new content is canon — file it. One done-summary after green. No approval wait.
- Q: If session prep needs a new named character who has no wiki page yet, may the agent file that page before you accept? → A: Yes. User asked for it, so it is canon. File the page. Do not wait.
- Q: Should new agent-facing standards in this feature be machine-checkable rules that agents must make green, with prose only explaining why? → A: Lint is the contract for this feature and every later feature: each new agent-facing standard MUST ship as a checkable rule; agents iterate until green; AGENTS.md is why/examples only. Existing prose-only standards are not retrofitted by this feature.
- Q: Must an agent keep fixing until checkable rules are green before it may say the work is done? → A: Yes. Every task the agent executes is in scope. Self-heal to green, then one short done-summary. No special-case pauses. MUST NOT interrupt the user with findings, contradiction alerts, or extra questions.
- Q: What is the entire canon rule and workflow? → A: If the user said it, it is canon. If the user said it more recently, that is more canon. If a transcript says it, after ASR issues are fixed, it is canon. DM-placed ingest files are canon as long as they do not contradict. No canon gates. No approval wait.
- Q: Must new agent-facing files live in predictable paths with consistent, searchable names so an agent can find and edit them without hunting? → A: Required going forward: new agent-facing files use predictable paths and consistent searchable names; encode that as a checkable rule. No bulk rename of the existing tree.
- Q: Is removing Work gates, DM-approval pauses, and extra canon workflow in scope? → A: Yes. All of it. Canon is only the four-line rule. Do not add gates or extra steps.
- Q: Earlier answers grandfathered old files (no bulk rename, no retrofit). Should this feature bulk-rename existing agent-facing files and bring old files to the new checkable standards? → A: Yes. Everything. No grandfathering. Carve-outs only after a problem already experienced, never proactively. Rename to the placement rule. Update every old instruction file until the new rules are green.





## User Scenarios & Testing

### User Story 1 - Autonomous Routine Wiki Maintenance (Priority: P1)

An agent performing wiki maintenance — linting, template conformance, ingest processing, structural repairs — completes the work, brings checkable rules to green, and reports one short done-summary of what changed and where.


**Why this priority**: Routine maintenance is the highest-volume agent task. These operations are deterministic, safe, and idempotent — Constitution XV ("Autonomous Operation").

**Independent Test**: Agent runs `wiki-lint` with `--fix` on a page with broken links and non-conformant frontmatter. The page is repaired, checkable rules are green, and the last message is a short done-summary (what changed, where), not a question.


**Acceptance Scenarios**:

1. **Given** a wiki page with broken wikilinks and missing frontmatter fields, **When** an agent lints and repairs it, **Then** the page is fixed, checkable rules are green, and the agent reports a short done-summary
2. **Given** a batch of raw ingest sources in `_raw/`, **When** an agent ingests them, **Then** pages are created on live wiki paths, index/log/hot updated, and manifest recorded — then a short done-summary
3. **Given** a wiki page using an outdated template structure, **When** an agent conforms it to the current template, **Then** the page is updated, checkable rules are green, and the agent reports a short done-summary


---

### User Story 2 - Canon (Priority: P1)

If the user said it, it is canon. If the user said it more recently, that is more canon. If a transcript says it, after ASR issues are fixed, it is canon. DM-placed ingest files are canon as long as they do not contradict. That is the whole rule. The agent files the work.

**Why this priority**: Extra workflow around canon was the defect. Removal of Work gates, DM-approval pauses, and extra canon steps is in scope.

**Independent Test**: User says “create an NPC named Varn who runs the docks.” Agent files the page, rules go green, short done-summary.

**Acceptance Scenarios**:

1. **Given** a user request to "create an NPC named Varn who runs the docks," **When** the agent acts, **Then** it files the page, rules are green, and it reports a short done-summary
2. **Given** a user request to "lint all faction pages," **When** the agent lints and fixes structural/template issues, **Then** it completes the work, rules are green, and it reports a short done-summary
3. **Given** a user request to "add a new quest hook to the Bloodhawk page," **When** the agent acts, **Then** it files the hook
4. **Given** a user request to "clean up the broken links on Bloodhawk and add a new quest hook," **When** the agent acts, **Then** it does both, rules are green, and it reports one done-summary
5. **Given** session prep that needs a new named NPC the user asked to introduce, **When** the agent has no owner page, **Then** it files the owner page; spoken text may follow



---

### User Story 3 - Project Identity as Agent Infrastructure (Priority: P2)

Development practices, review criteria, and success metrics treat agent skills, instructions, and guidance documents as the primary deliverables — not shipped software artifacts. Code exists to serve agent operations, not the other way around. Instruction changes are judged with the existing skill-eval method already in `skill-creator`: held-out task prompts, with-skill vs without-skill runs, graded assertions. Do not add a review checklist, GitHub PR template, or new review skill for this.

**Why this priority**: Misidentifying the project as "software" leads to wrong review criteria (code coverage over skill evals), wrong priorities (refactoring scripts over improving skill instructions), and wrong success metrics (test pass rates over session quality). Aligning project identity fixes downstream decision-making.

**Independent Test**: A skill or instruction change is reviewed using skill-eval results (pass/fail on held-out prompts) rather than software engineering criteria (code coverage, type safety).


**Acceptance Scenarios**:

1. **Given** a PR that modifies a skill SKILL.md file, **When** it is reviewed, **Then** the review uses skill-eval results (held-out prompts, with-skill vs without-skill, graded assertions) rather than software metrics as the primary bar

2. **Given** a new feature proposal, **When** it is specified, **Then** the spec describes agent behavior outcomes, not software architecture
3. **Given** a choice between improving a helper script's code quality and improving a skill's instruction clarity, **When** resources are limited, **Then** the skill instruction improvement is prioritized


### User Story 5 - Agent-Facing Standards Are Checkable (Priority: P1)

Each new agent-facing standard — in this feature and every later feature — ships as a machine-checkable rule. Agents treat a failing rule as a defect and iterate until it is green. `AGENTS.md` states why and examples only; it is not a sufficient substitute for the rule.

**Why this priority**: Prose-only standards leave agents believing they complied when they did not. A checkable rule is the executable contract (agent experience); the same rule is the human guarantee (developer experience). The default is project-wide going forward, not a one-feature experiment.

**Independent Test**: A later feature that adds an agent-facing standard without a checkable rule is incomplete. An agent that violates the rule receives a finding, repairs the cause, and reruns until green.

**Acceptance Scenarios**:

1. **Given** this feature or a later feature adds a new agent-facing standard, **When** the change is offered as done, **Then** a corresponding checkable rule exists and is green
2. **Given** `AGENTS.md` explains a new agent-facing standard, **When** an agent applies that standard, **Then** compliance is determined by the checkable rule, not by reading the prose alone
3. **Given** an agent produces output that fails a checkable rule, **When** it notices the finding, **Then** it repairs the cause and reruns until green rather than rewriting the rule away
4. **Given** a later feature spec that introduces an agent-facing standard in prose only, **When** readiness is checked, **Then** that feature is incomplete
5. **Given** checkable rules still fail for work the agent just did, **When** it would report done, **Then** it MUST NOT report done; it repairs and reruns until green, without asking the user

---

### User Story 6 - Predictable Agent-Facing Files (Priority: P1)

Agent-facing files use predictable paths and consistent searchable names. That placement/name rule is checkable. This feature bulk-renames the existing tree to match.

**Why this priority**: Agents cannot find or edit what they cannot grep or glob. Grandfathered names leave the hunt in place.

**Independent Test**: An agent-facing file that is not at the predicted path or that uses an ad-hoc unsearchable name fails the checkable rule, including files that predate this feature.

**Acceptance Scenarios**:

1. **Given** this feature or a later feature adds a new agent-facing file, **When** it is offered as done, **Then** its path and name match the checkable placement rule
2. **Given** an existing agent-facing file whose path or name does not match the placement rule, **When** this feature ships, **Then** it has been renamed and references updated; the placement rule (no current checker) is green

### Edge Cases

- Two user statements conflict — the more recent user statement wins
- Agent conforming a page to a template discovers content that has no template field — preserves the content rather than discarding
- User asks to "clean up and expand" a page — do both; one done-summary after green
- Ingest file placed by the DM contradicts the user or a corrected transcript — that ingest is not canon
- Session prep needs a new named owner the user asked to introduce — file the page
- A later feature adds an agent-facing standard with no checkable rule — the feature is incomplete; do not treat AGENTS.md prose as a substitute
- Existing instruction files that predate this feature are updated and renamed until `luna-eval` evals are green
- An agent-facing file in an ad-hoc path — the checkable placement rule fails; the work is not done


## Requirements

### Functional Requirements


- **FR-001**: This feature MUST remove Work gates, DM-approval pauses, and extra canon workflow from agent-facing instructions. Requested work is done, then a short done-summary. Checkable rule: `luna-eval` Work-gate evals.
- **FR-002**: Agents MUST complete: linting, template conformance, frontmatter normalization, link repair, ingest processing, structural migration, index/log/hot maintenance, manifest recording, staging-area management, and user-requested new content
- **FR-003**: Canon is only this: if the user said it, it is canon; a more recent user statement is more canon; a transcript is canon after ASR issues are fixed; a DM-placed ingest file is canon when it does not contradict those.
- **FR-004**: FR-001–FR-003 MUST be encoded as checkable rules (`luna-eval` Work-gate evals plus constitution X as the four-line owner). `AGENTS.md` MUST state why and examples only and MUST point at those rules.
- **FR-005**: Skills and instructions that still describe Work gates, DM-approval pauses, or extra canon steps MUST have those procedures removed
- **FR-006**: The project's development practices MUST treat agent skills, instructions, and guidance documents as primary deliverables, with helper scripts and tooling as supporting infrastructure
- **FR-007**: Review of skill/instruction changes MUST use the existing skill-eval method (held-out prompts, with-skill vs without-skill, graded assertions). It MUST NOT add a new checklist, PR template, or review skill, and MUST NOT treat coverage or type-safety as the primary bar
- **FR-008**: The only required user-facing report after completed work is one short done-summary. Agents MUST NOT add extra questions.
- **FR-009**: After checkable rules are green, the agent MUST report one short done-summary naming what changed and where. Work is not done while rules for that work still fail.
- **FR-010**: When a single request mixes maintenance and user-requested new content, the agent MUST complete all of it, reach green, and issue one done-summary
- **FR-011**: Each agent-facing standard — this feature's, later features', and existing instruction files this feature updates — MUST ship as a machine-checkable rule. Agents MUST iterate until that rule is green. `AGENTS.md` MAY explain why and give examples and MUST NOT be treated as a sufficient substitute for the rule. Existing instruction files MUST be updated until green. Checkable rule: the spec-citation rule (no current checker).
- **FR-012**: Every task the agent executes is in scope for the green-before-done loop
- **FR-013**: Agent-facing files MUST use predictable paths and consistent searchable names, encoded as a checkable rule (the placement rule (no current checker)). This feature MUST bulk-rename the existing tree to satisfy that rule. References MUST be updated with the rename.
- **FR-014**: The same checkable rules MUST apply on the agent path and the human path. Do not keep an agent-only honor system.



### Key Entities

- **Canon Rule**: User said it → canon; more recent user statement wins; corrected transcript → canon; DM-placed ingest → canon if it does not contradict.
- **Done-summary**: A short conversational report of completed work (what changed, where).
- **Lint Contract**: The machine-checkable rules that encode new agent-facing standards from this feature onward. Prose is why/examples; the rule is the guarantee.


## Success Criteria

### Measurable Outcomes

- **SC-001**: Agents complete wiki maintenance (lint, conform, ingest) end-to-end; checkable rules are green before the done-summary
- **SC-002**: 100% of user-requested new content is filed
- **SC-003**: 100% of Work-gate, DM-approval-pause, and extra canon-step procedures are removed from agent-facing instructions this feature touches
- **SC-004**: Spec and PR reviews for skill/instruction changes cite skill-eval outcomes, not software-only metrics, as the primary bar
- **SC-005**: Two agents given the same task description both complete it
- **SC-006**: 100% of agent-facing standards in this feature, later features, and existing instruction files this feature updates have a corresponding checkable rule; a change that adds such a standard in prose only is incomplete
- **SC-007**: 0% of done-summaries are issued while checkable rules for that work still fail
- **SC-008**: 100% of agent-facing files this feature ships (new and renamed existing) satisfy the checkable path/name rule

## Assumptions

- Constitution XV ("Autonomous Operation"): do the work. User speech is canon.
- Wiki writes go to live vault paths
- `AGENTS.md` explains why and examples; the checkable rule is the contract
- Helper scripts and tooling continue to follow Constitution VI ("Software and Instructions Are Agent-Shaped")
- Skill evaluation for instruction changes reuses the existing `skill-creator` eval loop
- Existing instruction files are updated and renamed in this feature until `luna-eval` evals are green.
- The four-line canon rule is the entire canon workflow
- Checkable rules are shared by agents and humans (FR-014)
