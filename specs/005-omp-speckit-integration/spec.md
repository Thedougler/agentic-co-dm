# Feature Specification: OMP Spec Kit Integration

**Feature Branch**: `005-omp-speckit-integration`

**Created**: 2026-09-11

**Status**: Draft

**Input**: User description: "Adopt Spec Kit’s native coding-harness integration (not a generic adapter). Keep Spec Kit as owner of requirements, constitution, spec, plan, tasks, checklists, and convergence. Keep the coding harness as owner of model routing, tools, subagents, concurrency, isolation, context, implementation, and verification. Separate live feature context from sticky rules. Cap parallel workers, keep recursion shallow, use narrow specialists, isolate independent writes, require structured worker reports, run quality gates before fan-out, disable always-on review and learned memory as authority, avoid duplicate instruction files and dual workflow engines, wrap Spec Kit in one thin orchestrator, prefer a direct session over RPC, and optimize for append-only convergence rather than one-shot completion."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Native Spec Kit in the coding harness (Priority: P1)

A maintainer (or an agent acting for them) sets up this repository so Spec Kit runs as a first-class coding-harness integration. Spec Kit commands live in the harness’s native command location. There is no generic adapter and no translation layer between Spec Kit phases and the harness.

Ownership is explicit: Spec Kit is the source of truth for requirements, constitution, specification, plan, tasks, acceptance checklists, and convergence. The coding harness is the source of truth for model routing, tool access, specialists, concurrency, isolation, context management, implementation execution, and verification. Spec Kit lifecycle phases are not recreated as harness agents.

**Why this priority**: Without native integration and a clean ownership split, every later feature pays a tax in duplicated phases, shadowed instructions, and upgrade breakage.

**Independent Test**: Inspect the project: Spec Kit is initialized with the native harness integration; Spec Kit commands are present in the harness native command location; no generic-adapter integration is in use; an ownership check shows Spec Kit artifacts vs harness execution concerns are not duplicated as agents.

**Acceptance Scenarios**:

1. **Given** this repository, **When** a maintainer inspects Spec Kit integration, **Then** it is the native coding-harness integration and not a generic adapter.
2. **Given** native integration, **When** an operator invokes a Spec Kit command (specify, plan, tasks, analyze, implement, converge, and the rest of the lifecycle), **Then** the command runs from the harness’s native command location without a translation layer.
3. **Given** a feature in flight, **When** anyone asks who owns a document, **Then** requirements, constitution, specification, plan, tasks, checklists, and convergence are Spec Kit artifacts, not harness-agent rewrites of those phases.
4. **Given** a feature in flight, **When** anyone asks who owns execution, **Then** model choice, tools, specialists, concurrency, isolation, live context, implementation, and verification are harness concerns that consume Spec Kit artifacts.
5. **Given** the Spec Kit lifecycle, **When** a specialist roster is reviewed, **Then** there is no harness agent whose job is to re-enact a Spec Kit phase (specify, clarify, plan, checklist, tasks, analyze, implement, or converge).

---

### User Story 2 - Live context stays current; sticky rules survive (Priority: P2)

Operators need two kinds of standing instruction. Live feature context (current feature, architecture, active plan references, repository conventions) updates as Spec Kit artifacts change. Sticky engineering rules (do not skip verification, do not edit generated files by hand, do not push or deploy unless asked, implementation maps to tasks, completion requires evidence) survive long sessions and compaction.

Learned harness memory and auto-generated skills are not an authority that can compete with the specification. Instruction for this project lives in the harness-native locations; equivalent files for other clients are not maintained unless portability is an explicit goal (it is not).

**Why this priority**: Wrong or stale standing instruction is how agents bypass the spec. This slice is valuable even if parallel implementation is never used.

**Independent Test**: After a feature’s spec and plan exist, confirm live context names that feature and its plan; confirm sticky rules still forbid skipping verification and hand-editing generated files; confirm harness memory is not treated as project authority; confirm there is not a second same-scope instruction file for another client.

**Acceptance Scenarios**:

1. **Given** an active feature with a spec and plan, **When** a new coding session starts, **Then** live context includes the current feature, architecture notes, and active plan references without the operator pasting them by hand.
2. **Given** a long session that has compacted, **When** the agent continues implementation, **Then** sticky rules still apply: verification is required, generated files are not edited directly, push/deploy does not happen without an explicit instruction, work maps to tasks, and completion requires evidence.
3. **Given** a conflict between a learned heuristic and a Spec Kit artifact, **When** the agent chooses a source of truth, **Then** the Spec Kit artifact (or sticky rules / live context / repository documentation) wins; harness memory is not authoritative.
4. **Given** this project, **When** instruction locations are inventoried, **Then** the preferred set is the harness-native context, rules, commands, specialists, skills, and external-tool config — not a parallel copy for another coding client.
5. **Given** an external system (issue tracker, database, observability, design tool, or documentation service), **When** no in-flight work needs it, **Then** it is not injected into every session; it is exposed only when an agent actually needs it.

---

### User Story 3 - Independent work proceeds in bounded parallel (Priority: P3)

After Spec Kit tasks exist, an operator implements only tasks that do not depend on each other in the same wave. Each bounded task goes to a narrow implementer, not a generic catch-all worker. Writable work on disjoint files is isolated. Work that touches shared architectural files is sequential or explicitly coordinated. Workers report a structured result (status, task ids, changed files, tests run, whether tests passed, which acceptance criteria were checked, what remains unresolved). Workers do not spawn further workers. At most four implementation workers run at once.

Planning and independent verification use the strongest available reasoning. Bounded implementation and cheap classification use faster, cheaper capacity. Always-on extra review after every turn is off; review happens at meaningful gates via an explicit verifier.

**Why this priority**: This is the speed win, but only after P1–P2 exist. Unbounded fan-out without isolation produces merge conflicts and duplicate investigation.

**Independent Test**: Take a tasks list with two independent items and one shared-file item. Run a wave: the two independent items proceed isolated and in parallel; the shared-file item waits or is coordinated; each worker returns the structured report; no worker spawns another worker; concurrent workers never exceed four; a verifier then checks the wave without editing implementation.

**Acceptance Scenarios**:

1. **Given** a tasks list, **When** a wave is formed, **Then** only dependency-independent items are in that wave; dependent items wait for a later wave.
2. **Given** two independent items that touch disjoint files, **When** they run in the same wave, **Then** they run isolated from each other and do not overwrite one another’s files.
3. **Given** items that touch the same architectural files, **When** a wave is formed, **Then** those items are sequential or have an explicit coordination rule; they are not blindly parallelized.
4. **Given** a finished worker, **When** the orchestrator reads the result, **Then** it can machine-read status, task ids, changed files, tests, acceptance checks, and unresolved items without parsing free prose.
5. **Given** any implementation wave, **When** concurrency and recursion are inspected, **Then** at most four workers run at once and no worker spawns another worker.
6. **Given** planning, implementation, and verification roles, **When** work is assigned, **Then** planning and verification use high-reasoning capacity, implementation uses fast coding capacity, and trivial classification uses cheap capacity — changed in one project mapping, not per-prompt.
7. **Given** ordinary turns, **When** a turn completes, **Then** there is no automatic extra reviewer on every turn; verification is an explicit gate after a wave or after convergence.

---

### User Story 4 - Quality gates, then converge — not one-shot completion (Priority: P4)

An operator does not fan out implementation until Spec Kit quality gates have run: specify, clarify if ambiguity remains, plan, checklist, tasks, then a read-only analyze that must stop the line on material contradictions. After a wave, targeted verification runs, then Spec Kit converge compares completed work to spec, plan, and tasks and appends missing work. Only appended items are implemented next. The loop repeats until converge is clean. A thin orchestrator sequences this; generated Spec Kit commands are not edited. Spec Kit owns the macro lifecycle; the harness owns only implementation-wave parallelism. The primary path is a direct coding session, not an RPC/ACP session that would silently drop project task settings.

**Why this priority**: Parallel implementation without gates ships the wrong work quickly. One-shot “done” without converge leaves gaps that become large late rewrites.

**Independent Test**: Run the orchestrated path on a small feature: analyze findings with material contradictions block implementation; a wave that omits an acceptance criterion is caught by converge as new tasks; a second wave implements only those tasks; generated Spec Kit commands remain unmodified; the session is a direct harness session.

**Acceptance Scenarios**:

1. **Given** a new feature request, **When** the thin orchestrator runs, **Then** it sequences specify → clarify if needed → plan → checklist → tasks → analyze before any parallel implementation.
2. **Given** material contradictions among spec, plan, and tasks, **When** analyze completes, **Then** implementation does not start until those findings are resolved.
3. **Given** a completed implementation wave, **When** converge runs, **Then** missing work is appended to tasks rather than silently ignored, and the next implementation pass covers only the appended items.
4. **Given** a clean converge, **When** an independent verifier runs, **Then** it checks behavior against spec, plan, tasks, and checklists using tests, diagnostics, and code evidence, and it does not modify implementation.
5. **Given** generated Spec Kit commands, **When** orchestration is added or changed, **Then** those generated commands stay upgradeable and unmodified; custom sequencing lives in a separate harness command (or extension).
6. **Given** macro lifecycle vs implementation waves, **When** orchestration is inspected, **Then** Spec Kit owns the lifecycle DAG and the harness owns only in-wave parallelism — the two engines do not both own the same graph.
7. **Given** a choice of session path, **When** this workflow runs, **Then** it uses a direct coding-harness session. RPC or ACP is not the primary path unless a named version has been verified to preserve project task, isolation, and related settings.

---

### Edge Cases

- Native integration is already present: do not destroy existing Spec Kit state; verify native commands and fill missing baseline pieces only.
- Generic adapter remnants exist alongside native commands: native wins; the generic path is removed or documented as unused, not left as a second entry point.
- Analyze finds only non-material nits: implementation may proceed; only material contradictions stop the line.
- A wave has one independent item: run it alone; do not invent sibling workers for parallelism theater.
- Isolation is requested for read-only audit: do not isolate; isolation is for writable disjoint work.
- Worker returns `blocked` or `failed`: the wave does not count as complete; unresolved items stay visible; converge still runs against actual code.
- Worker prose is valid but structured fields are missing: treat as failed output; do not have the parent guess.
- Shared architectural file and disjoint files in one wave: split the wave; shared work waits.
- Sticky rules and live context disagree: sticky rules win for safety constraints; live context wins for “what feature is active.”
- Learned memory suggests a shortcut that skips tests: forbidden; specification and sticky rules win.
- Operator starts via RPC/ACP: warn that project task settings may reset; do not treat that path as the supported workflow until verified.
- External-tool config exists user-wide and project-local: project-local applies to this repo; do not duplicate the same server in both without a reason.
- Thin orchestrator is invoked with an empty request: fail with a missing-description error; do not invent a feature.
- Constitution requires GitHub issues as the tracked work surface: Spec Kit tasks remain feature SDLC state; they do not replace issue tracking.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The project MUST use Spec Kit’s native coding-harness integration. A generic adapter MUST NOT be the integration path.
- **FR-002**: Spec Kit MUST own requirements, constitution, specification, plan, tasks, acceptance checklists, and convergence as canonical artifacts.
- **FR-003**: The coding harness MUST own model routing, tool access, specialists, concurrency, isolation, context management, implementation execution, and verification.
- **FR-004**: Spec Kit lifecycle phases MUST NOT be duplicated as harness agents. Specialists consume Spec Kit artifacts; they do not replace Spec Kit commands.
- **FR-005**: Live feature context MUST stay synchronized with the active spec and plan in the harness’s highest-priority project context file.
- **FR-006**: Sticky engineering rules MUST live separately from live context and MUST survive session compaction. Those rules MUST include: never skip verification; never modify generated files directly; never push or deploy without an explicit instruction; implementation MUST map to tasks; completion REQUIRES verification evidence.
- **FR-007**: Harness memory and auto-learned skills MUST NOT be an authoritative source of project decisions.
- **FR-008**: Same-scope instruction MUST NOT be duplicated across other coding-client files unless portability is an explicit, recorded goal.
- **FR-009**: Parallel implementation MUST include only dependency-independent tasks in a wave, using one shared Spec Kit context for that wave.
- **FR-010**: Writable parallel work on disjoint files MUST be isolated. Read-only audit MUST NOT require isolation. Shared architectural files MUST be sequential or explicitly coordinated.
- **FR-011**: Implementation and verification workers MUST return a structured result with status (`complete`, `blocked`, or `failed`), task ids, changed files, tests run, tests-passed flag, acceptance criteria verified, and unresolved items. Invalid structure MUST be treated as failure.
- **FR-012**: Concurrent implementation workers MUST be capped at four. Workers MUST NOT spawn workers (one orchestrator-to-worker hop).
- **FR-013**: The project MUST provide three narrow specialists: a read-only spec auditor, a bounded-task implementer, and a read-only verifier. Generic catch-all workers MUST NOT be the default for those jobs.
- **FR-014**: Planning and verification MUST use high-reasoning capacity. Bounded implementation MUST use fast coding capacity. Trivial classification MUST use cheap capacity. Role mappings MUST be changed in one project place, not per prompt.
- **FR-015**: Always-on extra review after every turn MUST be off. Review MUST occur at explicit gates (after a wave and after converge) via the verifier.
- **FR-016**: Implementation fan-out MUST NOT start until specify, optional clarify, plan, checklist, tasks, and read-only analyze have run. Material analyze findings MUST block implementation.
- **FR-017**: After implementation, converge MUST compare code to spec, plan, and tasks, append missing work to tasks, and restrict the next implementation pass to appended items until converge is clean.
- **FR-018**: Custom sequencing MUST live in one thin orchestrator command (or extension) that invokes unmodified generated Spec Kit commands.
- **FR-019**: Spec Kit MUST own the macro lifecycle graph. The harness MUST own only implementation-wave parallelism. Both MUST NOT own the same graph.
- **FR-020**: The primary operating path MUST be a direct coding-harness session. RPC or ACP MUST NOT be the primary path unless a named installed version is verified to preserve project task, isolation, async, memory, and advisor settings.
- **FR-021**: External systems MUST be exposed to agents only when in-flight work needs them.
- **FR-022**: If native integration already exists, setup MUST be additive and non-destructive: verify native commands, then add missing baseline pieces. It MUST NOT wipe existing Spec Kit artifacts.

### Key Entities

- **Spec Kit artifact**: Canonical SDLC document (constitution, spec, plan, tasks, checklist, convergence notes).
- **Coding harness**: The agent runtime that routes models, tools, specialists, concurrency, isolation, and verification.
- **Live context**: Standing, feature-current instructions (active feature, architecture, plan references, conventions).
- **Sticky rules**: Short, durable constraints that outlive compaction.
- **Specialist**: A narrow harness agent (auditor, implementer, verifier) that consumes Spec Kit artifacts.
- **Dependency wave**: A set of tasks with no remaining undone dependencies on each other.
- **Structured worker report**: Machine-readable completion record for one task or verification pass.
- **Thin orchestrator**: A single custom command that sequences Spec Kit phases and harness waves without editing generated Spec Kit commands.
- **Convergence loop**: Implement wave → verify → converge → implement only appended tasks → repeat until clean.
- **Material finding**: An analyze contradiction that would cause wrong implementation if ignored.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: On a cold start of this repo, an operator can invoke the full Spec Kit lifecycle from the harness without using a generic adapter; 100% of those invocations resolve to native harness commands.
- **SC-002**: In an audit of one completed feature cycle, 0 Spec Kit phases are reimplemented as harness agents, and 100% of implementation items trace to a tasks entry.
- **SC-003**: Given two independent disjoint-file tasks and one shared-file task, the independent pair finishes in one wave without overwriting each other, and the shared-file task is not in that pair; 100% of worker results are structured and parseable.
- **SC-004**: Across a feature with more than four ready tasks, observed concurrent implementation workers never exceed four, and worker-spawned workers equal zero.
- **SC-005**: When spec, plan, and tasks are deliberately contradictory, implementation does not start; the operator sees the contradiction from the read-only analyze gate before any implementation wave.
- **SC-006**: When a first wave omits at least one in-scope acceptance criterion, converge appends that work, the next pass implements only the appended items, and a second converge is clean — without a full rewrite of already-correct work.
- **SC-007**: After a session compaction, sticky rules still prevent skipped verification and direct edits to generated files in 100% of sampled continuations (at least three).
- **SC-008**: A maintainer who is not an internals expert can complete one loop (specify through analyze, one wave, converge, independent verify) in a single sitting without a second operator and without editing generated Spec Kit commands.
- **SC-009**: In a debrief of at least three features run on this baseline, the maintainer rates “the spec remained the authority” as true for 100% of features (no learned-memory override, no competing instruction file, no RPC-reset surprise on the primary path).

## Assumptions

- Designated surfaces (product choices, not success metrics): Spec Kit is the SDLC toolkit; the coding harness is Oh My Pi (OMP) with native Spec Kit integration; live context is the harness-native project context file; sticky rules are the harness-native rules file; specialists live in the harness-native agents directory; the thin orchestrator is a separate harness command such as `/feature-fast`.
- This repository already has Spec Kit with native OMP integration in `init-options`. This feature completes the operating baseline; it does not re-initialize from scratch unless native commands are missing.
- Concrete model identifiers are out of spec. Roles are: default (balanced interactive), plan (strong reasoning), task (fast coding), review (strong or independently trained reasoning), smol (cheap/fast), advisor (unused globally).
- Concurrency cap is four. Recursion is one hop (orchestrator → worker). Depth two is out of scope except a future, separately specified research case.
- Spec Kit `agent-context` is in scope as the mechanism that keeps live context synchronized with the active spec/plan, targeting the harness-native context file.
- GitHub issues remain the tracked work surface per the constitution. Spec Kit `tasks.md` is feature SDLC state consumed by the harness, not a second issue tracker and not a replacement for `gh`.
- Cross-client portability (parallel CLAUDE.md, root AGENTS.md copies, Cursor/Codex/Copilot instruction twins) is out of scope.
- Global advisor, harness memory backends, and autolearn are out of scope as authority; they stay off.
- Editing generated `speckit.*` commands is out of scope.
- Dual ownership of one DAG by Spec Kit workflows and harness Swarm is out of scope.
- RPC/ACP as primary orchestration is out of scope until a named OMP version is verified to preserve project task settings.
- Human chrome around this baseline waits; the orchestrator and specialists MUST be agent-invocable (arguments in, text or structured result out, distinct success vs failure).
