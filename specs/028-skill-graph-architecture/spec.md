# Feature Specification: Skill Graph Architecture

**Feature Branch**: `028-skill-graph-architecture`

**Created**: 2026-09-20

**Status**: Draft

**Input**: User description: "Make the existing skill architecture behave as a well-engineered execution graph through clear ownership, shallow routing, bounded context, explicit dependencies, clean handoffs, feedback cycles, and observable completion. Do not add a graph framework, separate execution database, persistent workflow ledger, generic orchestrator skill, universal state schema, or giant workflow."

## Classification and Scope

- **work_class**: `agent-system`
- **route**: `full-sdd`
- **Objective**: Make future agents reliably select the correct existing skill, load only relevant context, satisfy real dependencies, return control after capability handoffs, and close work only on observable completion evidence.
- **User value**: The DM receives more reliable, complete, canon-faithful Work with less wasted context and less agent drift between capabilities.
- **In scope**: Root routing and invariants; wiki-facing skill boundaries; cross-skill capability handoffs; capability dependency semantics; context projection at capability boundaries; read, write, ingest, and maintenance workflow shapes; lint and retrieval feedback cycles; agent-facing observation surfaces; route-level behavioral evaluation; removal of duplicated workflow prose after authority is established.
- **Out of scope**: New graph runtimes, graph databases for execution, persistent workflow ledgers, generic orchestrator capabilities, universal workflow state schemas, bespoke node classes, hand-maintained all-skill DAGs, replacement of wiki canon stores, and consolidation of the knowledge graph with the execution graph.
- **Canon impact**: Campaign canon remains unchanged. This feature changes agent operating behavior and supporting guidance only.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Enter the Correct Capability (Priority: P1)

As a DM asking for wiki or campaign work, I want the agent to route directly from my intent to the capability that owns the requested artifact or operation so that specialized rules apply without unrelated instruction loading.

**Why this priority**: Correct ownership must be established before any capability dependency, output contract, or completion guard can be applied reliably.

**Independent Test**: Give a cold agent representative requests for a faction page, a wiki question, a page repair, and session content; verify each reaches the correct existing owner without a generic intermediate router.

**Acceptance Scenarios**:

1. **Given** a request whose artifact kind has a named owner capability, **When** the agent classifies the request, **Then** it selects that owner directly and loads that capability's instructions.
2. **Given** a request that belongs to a capability with genuine subtypes, **When** a subtype changes ownership, **Then** the selected capability delegates directly to the subtype owner and does not introduce another generic routing layer.
3. **Given** a read-only knowledge question, **When** retrieval reveals a useful possible edit, **Then** the read operation answers without mutating the wiki unless the user requested mutation.

---

### User Story 2 - Complete Cross-Capability Work (Priority: P1)

As a DM requesting work that depends on several artifact owners, I want the parent operation to preserve my original objective while specialized capabilities produce their artifacts and return control so that the entire request completes without task drift.

**Why this priority**: The highest-risk failures occur at capability routes and capability handoffs rather than inside a single capability.

**Independent Test**: Give a cold agent a session-content request requiring a missing faction and place; verify dependency owners run in valid order, independent dependencies may proceed concurrently, control returns to the parent, and the original session artifact closes only after all contracts pass.

**Acceptance Scenarios**:

1. **Given** a parent operation requiring a missing owner artifact, **When** ownership changes, **Then** the parent retains the original objective, the child owns only its specialized artifact, and control returns to the parent after child completion.
2. **Given** several dependencies with disjoint write surfaces and no prerequisite relation, **When** the agent schedules work, **Then** it may execute them independently and rejoins them before dependent work begins.
3. **Given** one dependency whose content determines another, **When** the agent schedules work, **Then** it preserves the dependency order rather than forcing parallel execution.
4. **Given** a lint finding requiring domain judgment, **When** deterministic repair cannot close it, **Then** lint hands the finding to the artifact owner, receives control back, and reruns until the scope is green.

---

### User Story 3 - Load Bounded Context at Each Boundary (Priority: P2)

As a repository maintainer, I want every capability to retrieve only the canon and operational context needed for its current work so that agents remain accurate without carrying unrelated prior-capability context.

**Why this priority**: Bounded context reduces wasted tokens and cross-domain contamination while preserving the evidence needed for quality.

**Independent Test**: Give a cold agent a targeted place edit after a broader session-planning request; verify the place capability retrieves the place and directly relevant campaign state, does not inherit unrelated entities, and deepens retrieval only when its evidence is insufficient.

**Acceptance Scenarios**:

1. **Given** a capability boundary, **When** the receiving capability starts, **Then** it identifies and retrieves its minimum necessary context instead of inheriting all material read by its parent.
2. **Given** insufficient evidence during execution, **When** the capability detects the gap, **Then** it retrieves deeper evidence and resumes the same work rather than guessing.
3. **Given** sufficient cheap metadata and focused evidence, **When** the capability can complete its job, **Then** it does not load broader full-page or whole-vault context.

---

### User Story 4 - Close Work on Observable Evidence (Priority: P2)

As a DM, I want mutations and maintenance work to finish only when their applicable output contracts are valid, so that prose existence is never mistaken for completion.

**Why this priority**: Observable completion guards make completion reliable and keep invalid work from shipping.

**Independent Test**: Give a cold agent one write and one maintenance request with an induced semantic finding; verify each uses the correct feedback edge, returns to the owner when needed, and reports completion only after the target scope is valid.

**Acceptance Scenarios**:

1. **Given** a wiki mutation, **When** authoring finishes, **Then** the applicable template, owner conventions, and validation contract determine whether the branch is complete.
2. **Given** a deterministic validation finding, **When** an eligible deterministic repair exists, **Then** the repair runs and validation repeats.
3. **Given** a semantic validation finding, **When** owner judgment is required, **Then** the finding routes to the owner capability and validation repeats after repair.
4. **Given** an observation surface that identifies a next target, **When** the agent acts, **Then** it follows that explicit target instead of independently rebuilding the same prioritization.

---

### User Story 5 - Maintain Legible Capability Contracts (Priority: P3)

As a skill author, I want wiki-facing capabilities to expose consistent boundary information while preserving their distinct craft, so that agents can understand inputs, ownership, completion, and capability handoffs quickly.

**Why this priority**: Consistent boundaries improve graph traversal without flattening specialized procedures into one generic workflow.

**Independent Test**: Review the named wiki-facing capabilities and verify each makes Input, Work, Done, and Capability Handoff legible, with no requirement that their internal procedures become identical.

**Acceptance Scenarios**:

1. **Given** a wiki-facing capability, **When** an agent opens its guidance, **Then** the expected input, owned work, observable completion condition, and capability handoff are immediately identifiable.
2. **Given** two capabilities with different craft requirements, **When** their boundary contracts are normalized, **Then** their internal procedures remain capability-specific.
3. **Given** duplicated workflow guidance across authority layers, **When** one canonical owner is established, **Then** lower-value duplication is removed without deleting global invariants or quality-critical detail.

### Edge Cases

- A request combines read-only inquiry and mutation: classify each slice and preserve read/write isolation until mutation is explicitly in scope.
- A page type or artifact kind has no established owner: stop at the ownership gap rather than silently assigning a generic authoring capability.
- A child capability discovers another dependency: preserve the original parent objective and return through each parent after the dependency closes.
- A validation loop repeats without progress: report the unresolved owner-level defect rather than weakening validation or looping indefinitely.
- An observation surface is silent or unavailable: use the existing documented fallback without inventing a second durable state store.
- Two dependencies target the same canonical write surface: serialize them under one active writer.
- A route-level evaluation finds correct final prose but an invalid route, broad context load, missed capability handoff, or premature completion: treat the composition as failed.
- Guidance, templates, or validation rules are changed: assess and update relevant counterparts in the same change when the behavior they jointly govern is affected.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The system MUST preserve four authority layers: global routing and invariants; capability-owned execution; wiki semantic conventions; and output-shape validation.
- **FR-002**: Global guidance MUST answer which capability branch owns a job and MUST NOT restate branch-specific execution procedures already owned elsewhere.
- **FR-003**: Each in-scope wiki-facing capability MUST make its Input, Work, Done, and Capability Handoff contract immediately identifiable.
- **FR-004**: Boundary normalization MUST preserve each capability's specialized procedures and craft requirements.
- **FR-005**: Routing MUST normally proceed directly from user intent to one owner capability.
- **FR-006**: Additional classification steps MUST exist only where subtype choice changes the actual owner or execution branch.
- **FR-007**: The parent operation MUST retain responsibility for the user's original objective across every child capability handoff.
- **FR-008**: A delegated capability MUST own only the specialized artifact or operation named by the capability handoff and MUST return control when its completion condition is met.
- **FR-009**: Cross-capability guidance MUST identify real prerequisite relationships rather than prescribe one rigid procedure for every request.
- **FR-010**: Independent dependencies with disjoint canonical write surfaces MUST be eligible for concurrent execution; dependencies sharing a write surface or prerequisite relationship MUST remain serial.
- **FR-011**: Session-facing work MUST preserve entity-before-spoken dependency order and DM-facing explicitness while using owner capabilities for missing dependencies.
- **FR-012**: Each capability MUST project and retrieve the minimum sufficient context at its boundary instead of inheriting all incidental context from prior work.
- **FR-013**: Retrieval guidance MUST support progressive deepening when current evidence is insufficient and MUST stop once the capability's evidence condition is met.
- **FR-014**: Durable campaign and operational truth MUST remain in the existing wiki and existing operational surfaces; execution coordination MUST remain ephemeral and limited to the current objective, branch, targets, and completed dependencies.
- **FR-015**: The system MUST keep the campaign knowledge graph distinct from the capability execution graph.
- **FR-016**: The system MUST define canonical read, write, ingest, and maintenance workflow shapes as recurring compositions of existing capabilities and operations.
- **FR-017**: The read workflow MUST remain read-only unless mutation is explicitly requested.
- **FR-018**: Every vault-write workflow MUST reach the applicable validation contract before completion.
- **FR-019**: Validation MUST act as a feedback cycle: clean results close the branch; deterministic findings route to deterministic repair; semantic findings route to the artifact owner; repaired scope returns to validation.
- **FR-020**: Retrieval MUST act as a feedback cycle: sufficient evidence proceeds; insufficient evidence triggers focused retrieval and resumes the same capability.
- **FR-021**: Agent-facing query, lint, and health observation surfaces MUST provide compact, stable, actionable evidence sufficient to select the next existing operation without requiring agents to reconstruct hidden prioritization.
- **FR-022**: Maintenance guidance MUST treat health as an observation surface and MUST NOT layer a second planner over its explicit action ordering.
- **FR-023**: Existing owner-skill routing MUST remain the deterministic domain boundary between artifact kind, owner capability, template or jobs, and validation.
- **FR-024**: A new machine-readable owner registry MAY be proposed only after observed duplication creates a maintenance failure; this feature MUST NOT add one speculatively.
- **FR-025**: The feature MUST NOT add a graph runtime, execution graph database, persistent workflow ledger, generic orchestrator capability, universal state schema, bespoke node classes, hand-maintained global DAG, or giant all-purpose workflow.
- **FR-026**: Duplicate routing or workflow prose MUST be removed only after its canonical owner is established, while global invariants and quality-critical safeguards remain available at their required authority layer.
- **FR-027**: Route-level behavioral evaluations MUST cover direct routing, child return to parent, dependency order, context scope, read/write isolation, validation feedback, and observable completion.
- **FR-028**: Agent-facing behavioral evaluation MUST use cold focused context and the weakest sufficient available model.
- **FR-029**: Each named failure in this specification MUST map to an acceptance scenario or route-level evaluation.
- **FR-030**: When an in-scope change affects compiled wiki guidance, authoring guidance, templates, or validation rules that govern the same behavior, all relevant counterparts MUST be updated in the same change.
- **FR-031**: The implementation plan MUST identify one canonical owner and one active writer for every changed artifact and MUST order shared write surfaces serially.
- **FR-032**: Tracked implementation work MUST have an accountable issue before implementation begins.

### Key Entities

- **Capability**: An existing skill or deterministic wiki operation with a defined input, owned work, observable completion condition, and possible capability handoff.
- **Capability route**: A direct selection or capability handoff from one owner capability to another based on user intent, artifact kind, prerequisite, or finding class.
- **Completion guard**: An observable prerequisite or completion condition that permits traversal or closes a branch.
- **Parent operation**: The capability retaining responsibility for the user's original objective while dependencies or specialized artifacts are delegated.
- **Capability dependency**: A real prerequisite artifact or state required before dependent work can be valid.
- **Context projection**: The minimum sufficient canon and operational evidence retrieved for one capability's current work.
- **Observation surface**: Compact query, lint, or health evidence that reports relevant knowledge, invalid output, or the next attention target.
- **Output contract**: The combined template, owner conventions, and validation rules defining a valid artifact.
- **Knowledge graph**: Campaign pages and their semantic relationships; distinct from the execution relationships among capabilities.
- **Execution graph**: Ephemeral traversal among capabilities, capability dependencies, completion guards, observation surfaces, and capability handoffs for the current request.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: In route-level evaluation, 100% of representative requests reach the correct existing owner capability without an unnecessary generic routing step.
- **SC-002**: In capability-handoff evaluation, 100% of child capabilities return control to the parent operation and the original objective closes only after all required child contracts pass.
- **SC-003**: In dependency evaluation, 100% of prerequisite relationships execute in valid order, while every evaluated independent pair with disjoint write surfaces remains eligible for concurrent execution.
- **SC-004**: In context evaluation, 100% of evaluated capabilities load required owner and canon evidence, and no evaluated capability loads unrelated artifact groups solely because a prior capability read them.
- **SC-005**: In read/write isolation evaluation, 100% of read-only requests complete without wiki mutation.
- **SC-006**: In validation-loop evaluation, 100% of vault mutations either finish with a green applicable scope or report a specific unresolved owner-level blocker; none report success merely because prose was written.
- **SC-007**: Every in-scope wiki-facing capability exposes all four boundary elements—Input, Work, Done, and Capability Handoff—without losing its specialized completion requirements.
- **SC-008**: Review finds zero new graph runtimes, execution databases, persistent workflow ledgers, generic orchestrator capabilities, universal state schemas, bespoke node classes, or hand-maintained global DAGs.
- **SC-009**: A maintainer can identify the owner, required context, dependencies, completion guard, and next capability handoff for each canonical workflow in under two minutes using the authoritative guidance.
- **SC-010**: Representative cold-context evaluations pass 100% of critical routing, dependency, read-only, and completion assertions and introduce no regression in applicable existing behavior checks.

## Assumptions

- Existing skills, owner mappings, templates, wiki conventions, query/lint/health observation surfaces, and durable wiki state remain the foundation; the feature clarifies composition rather than replacing them.
- The four recurring workflows are descriptive canonical shapes, not a universal engine or mandatory serialized recipe.
- Input, Work, Done, and Capability Handoff are legibility headings or clearly equivalent concepts, not a new configuration schema.
- A capability handoff occurs only when ownership changes; trivial decisions remain inside the receiving capability.
- Existing health action ordering, lint repair behavior, and query retrieval behavior remain owned by their current specifications and implementations.
- Campaign canon is unaffected unless implementation uncovers a separately governed campaign-content defect.
- An accountable issue will be created or linked before implementation, as required by project governance.

## Dependencies and Authoritative Context

- **context_used**: User-provided graph-engineering direction; project constitution v3.1.0; root agent context and routing rules; `CONTEXT.md`; hybrid SDD contract; active wiki CLI specification for query, lint, and health observation-surface semantics.
- **context_omitted**: Individual campaign entity pages, session content, and full bodies of unrelated capability guidance because this specification defines system behavior rather than modifying campaign canon or prescribing each capability's internal craft.
- **Canonical owners**: Root agent context for global routing and invariants; each capability's guidance for execution; wiki agent context for semantic artifact meaning; templates and validation rules for output validity; current CLI specification for query, lint, and health behavior.
- **External dependency**: An accountable issue before implementation.

## Named Failure Modes and Evidence

- **Wrong owner selected** → User Story 1 scenarios; FR-005–FR-006; SC-001.
- **Parent objective lost after delegation** → User Story 2 scenarios; FR-007–FR-008; SC-002.
- **Dependency executed out of order or unsafe parallel write** → User Story 2 scenarios; FR-009–FR-011; SC-003.
- **Broad inherited context contaminates a capability** → User Story 3 scenarios; FR-012–FR-013; SC-004.
- **Read operation mutates the wiki** → User Story 1 scenario 3; FR-017; SC-005.
- **Prose treated as complete before contracts pass** → User Story 4 scenarios; FR-018–FR-020; SC-006.
- **Boundary normalization erases specialized craft** → User Story 5 scenarios; FR-003–FR-004; SC-007.
- **New orchestration machinery duplicates existing truth** → FR-014–FR-015 and FR-024–FR-025; SC-008.
- **Authority refactor deletes safeguards** → User Story 5 scenario 3; FR-026 and FR-030; route-level regression review.
