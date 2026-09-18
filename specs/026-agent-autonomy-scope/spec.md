# Feature Specification: Agent Autonomy Scope

**Feature Branch**: `026-agent-autonomy-scope`

**Created**: 2026-09-18

**Status**: Draft

**Input**: User description: "Greater agent autonomy for routine wiki tasks; DM approval only for collaborative creative work; project identity as agent infrastructure not shipped software"

## User Scenarios & Testing

### User Story 1 - Autonomous Routine Wiki Maintenance (Priority: P1)

An agent performing wiki maintenance — linting, template conformance, ingest processing, structural repairs — completes the full operation without pausing for DM approval. The agent fixes broken links, normalizes frontmatter, conforms pages to current templates, and commits the results directly.

**Why this priority**: Routine maintenance is the highest-volume agent task. Every unnecessary approval pause wastes DM attention and agent tokens. These operations are deterministic, safe, and idempotent — exactly what Constitution XV ("Autonomous Operation") already endorses.

**Independent Test**: Agent runs `wiki-lint` with `--fix` on a page with broken links and non-conformant frontmatter. The page is repaired, committed, and pushed without any DM prompt.

**Acceptance Scenarios**:

1. **Given** a wiki page with broken wikilinks and missing frontmatter fields, **When** an agent lints and repairs it, **Then** the page is fixed and committed without requesting DM approval
2. **Given** a batch of raw ingest sources in `_raw/`, **When** an agent ingests them, **Then** pages are created under `_staging/` (per staged-writes policy), index/log/hot updated, and manifest recorded — no DM approval requested for any step
3. **Given** a wiki page using an outdated template structure, **When** an agent conforms it to the current template, **Then** the page is updated and committed without DM approval

---

### User Story 2 - DM Approval Only for Creative Canon Work (Priority: P1)

When a user explicitly requests collaborative creative work — inventing new lore, writing narrative content, designing encounters, creating NPCs — the agent proposes the content through the existing Work gate and waits for DM acceptance before it becomes canon.

**Why this priority**: This is the counterpart to Story 1. The boundary between "autonomous" and "DM-gated" must be clear, or agents either over-ask (current problem) or silently invent canon (Constitution X violation).

**Independent Test**: Agent is asked to create a new NPC for an upcoming session. Agent drafts the NPC page but routes it through the Work gate for DM acceptance before committing to the wiki.

**Acceptance Scenarios**:

1. **Given** a user request to "create an NPC named Varn who runs the docks," **When** the agent drafts the page, **Then** it proposes the content via the Work gate and does not commit until the DM accepts
2. **Given** a user request to "lint all faction pages," **When** the agent lints and fixes structural/template issues, **Then** it commits directly because linting is routine maintenance, not creative canon invention
3. **Given** a user request to "add a new quest hook to the Bloodhawk page," **When** the agent drafts new narrative content, **Then** it routes through the Work gate because the request is explicitly creative

---

### User Story 3 - Project Identity as Agent Infrastructure (Priority: P2)

Development practices, review criteria, and success metrics treat agent skills, instructions, and guidance documents as the primary deliverables — not shipped software artifacts. Code exists to serve agent operations, not the other way around.

**Why this priority**: Misidentifying the project as "software" leads to wrong review criteria (code coverage over behavioral validation), wrong priorities (refactoring scripts over improving skill instructions), and wrong success metrics (test pass rates over session quality). Aligning project identity fixes downstream decision-making.

**Independent Test**: A spec or PR review evaluates a skill instruction change using behavioral validation criteria (does the agent produce better output?) rather than software engineering criteria (code coverage, type safety).

**Acceptance Scenarios**:

1. **Given** a PR that modifies a skill SKILL.md file, **When** it is reviewed, **Then** the review criteria emphasize behavioral validation (agent output quality) over software metrics
2. **Given** a new feature proposal, **When** it is specified, **Then** the spec describes agent behavior outcomes, not software architecture
3. **Given** a choice between improving a helper script's code quality and improving a skill's instruction clarity, **When** resources are limited, **Then** the skill instruction improvement is prioritized

---

### User Story 4 - Clear Autonomy Boundary Definition (Priority: P2)

The system provides an unambiguous classification of which operations are autonomous (no DM approval) and which require the Work gate. Agents can determine the classification without judgment calls on borderline cases.

**Why this priority**: Without a clear boundary, agents will either over-ask (defeating Story 1) or under-ask (violating Story 2). The boundary must be mechanical, not vibes-based.

**Independent Test**: An agent encountering any wiki task can classify it as autonomous or DM-gated using the defined rules without ambiguity.

**Acceptance Scenarios**:

1. **Given** the autonomy classification rules, **When** an agent encounters a linting task, **Then** the rules unambiguously classify it as autonomous
2. **Given** the autonomy classification rules, **When** an agent encounters a request to write new lore, **Then** the rules unambiguously classify it as DM-gated
3. **Given** the autonomy classification rules, **When** an agent encounters a request to conform an existing page to a current template without changing its factual content, **Then** the rules classify it as autonomous

### Edge Cases

- Agent discovers factual contradictions during routine lint — flags the contradiction as an error but does not resolve it (resolution is a canon judgment, not maintenance)
- Agent conforming a page to a template discovers the page contains content that has no template field — preserves the content and flags it rather than discarding
- User asks to "clean up and expand" a page — the cleanup portion is autonomous; the expansion is creative and DM-gated; agent splits the work accordingly
- Ingest produces a page that contradicts existing wiki canon — agent stages the page with a visible conflict marker rather than silently overwriting

## Requirements

### Functional Requirements

- **FR-001**: System MUST define a classification boundary between autonomous operations and DM-gated operations, expressed as a deterministic rule agents can evaluate
- **FR-002**: Autonomous operations MUST include: linting, template conformance, frontmatter normalization, link repair, ingest processing, structural migration, index/log/hot maintenance, manifest recording, and staging-area management
- **FR-003**: DM-gated operations MUST include: new lore invention, narrative content creation, NPC/faction/quest/encounter design when user explicitly requests creative work, canon fact changes, and reconciliation of contradictory canon
- **FR-004**: The classification boundary MUST be documented in `AGENTS.md` as the authoritative source, replacing any conflicting guidance in individual skills
- **FR-005**: Skills that currently pause for DM approval on routine operations MUST be updated to follow the new classification boundary
- **FR-006**: The project's development practices MUST treat agent skills, instructions, and guidance documents as primary deliverables, with helper scripts and tooling as supporting infrastructure
- **FR-007**: Review criteria for skill/instruction changes MUST prioritize behavioral validation (does the agent produce correct output?) over software engineering metrics
- **FR-008**: When an autonomous operation discovers a canon-level issue (contradiction, missing entity, ambiguous fact), the agent MUST flag it as an error without resolving it autonomously

### Key Entities

- **Autonomy Classification**: The rule set that determines whether a given operation requires DM approval or can proceed autonomously
- **Routine Operation**: A deterministic, safe, idempotent wiki maintenance task that does not create or modify campaign canon
- **Creative Work**: Content that invents, extends, or modifies campaign lore, narrative, or world state — triggered by explicit user request for collaborative creation
- **Work Gate**: The existing DM-acceptance boundary for canon-changing content

## Success Criteria

### Measurable Outcomes

- **SC-001**: Agents complete routine wiki maintenance (lint, conform, ingest) end-to-end without requesting DM approval in 100% of maintenance-only sessions
- **SC-002**: Agents correctly route creative canon work through the Work gate in 100% of cases where the user explicitly requests creative content
- **SC-003**: No routine maintenance operation is blocked waiting for DM input that does not arrive within the session
- **SC-004**: Spec and PR reviews for skill/instruction changes evaluate behavioral outcomes, not software-only metrics, in their review criteria
- **SC-005**: Agent classification of any wiki task as autonomous or DM-gated is deterministic — two agents given the same task description reach the same classification

## Assumptions

- Constitution XV ("Autonomous Operation") and Constitution X ("DM Owns Canon") already establish the philosophical boundary; this spec operationalizes it with explicit classification rules
- The existing Work gate mechanism is sufficient for DM-gated operations; no new approval mechanism is needed
- Staged writes (`WIKI_STAGED_WRITES=true`) remain the safety net for autonomous operations — agents commit freely but content lands in `_staging/` for review when that flag is set
- The project's `AGENTS.md` is the single authoritative location for the classification boundary; individual skills defer to it
- Helper scripts and tooling continue to follow Constitution VI ("Software and Instructions Are Agent-Shaped") regardless of the infrastructure-first identity shift
