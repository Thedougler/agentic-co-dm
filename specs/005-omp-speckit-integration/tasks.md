---
description: "Task list for OMP Spec Kit Integration"
---
# Tasks: OMP Spec Kit Integration

**Input**: Design documents from `/specs/005-omp-speckit-integration/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/, quickstart.md

**Tests**: Not requested. Validate with each story's Independent Test, `specs/005-omp-speckit-integration/quickstart.md`, and `scripts/check-omp-baseline.sh`.

**Organization**: Setup → Foundational → US1 → US2 → US3 → US4 → Polish.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Parallel (different files, no incomplete deps)
- **[Story]**: US1–US4 only on story phases
- Every task names an exact path

## Path Conventions

Harness: `.omp/`  
Spec Kit: `.specify/`  
Contracts: `specs/005-omp-speckit-integration/contracts/`  
Do not edit generated `.omp/commands/speckit.*`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Additive path. Native OMP integration stays. No re-init.

- [x] T001 Leave `.specify/init-options.json` `integration: omp` and `.specify/integration.json` `installed_integrations` containing `omp`. Do not run `specify init`. Do not switch to `generic`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Keep extra instruction surfaces out of the repo so later stories do not grow twins.

**⚠️ CRITICAL**: No user story work until this phase is complete

- [x] T002 Do not add `.omp/mcp.json` or a project-root `CLAUDE.md` (FR-008/021). If a foreign-client file already exists, do not maintain a Spec Kit twin of it

**Checkpoint**: Foundation ready — user stories can start

---

## Phase 3: User Story 1 - Native Spec Kit in the coding harness (Priority: P1) 🎯 MVP

**Goal**: Spec Kit runs as native OMP commands. Spec Kit owns SDLC artifacts. Harness does not re-enact phases as agents.

**Independent Test**: Inspect the project: `integration` is `omp`; `/speckit.specify` and `/speckit.converge` resolve from `.omp/commands/`; no harness agent is named after a Spec Kit phase.

### Implementation for User Story 1

- [x] T003 [US1] Leave generated `.omp/commands/speckit.specify.md`, `.omp/commands/speckit.clarify.md`, `.omp/commands/speckit.plan.md`, `.omp/commands/speckit.checklist.md`, `.omp/commands/speckit.tasks.md`, `.omp/commands/speckit.analyze.md`, `.omp/commands/speckit.implement.md`, and `.omp/commands/speckit.converge.md` unmodified. Do not add `.omp/agents/` files named `specify`, `clarify`, `plan`, `checklist`, `tasks`, `analyze`, `implement`, or `converge` (kinds: constitution, spec, plan, tasks, checklist, converge notes — mutation only via Spec Kit commands)

**Checkpoint**: US1 independently testable (quickstart Story 1)

---

## Phase 4: User Story 2 - Live context stays current; sticky rules survive (Priority: P2)

**Goal**: Feature-current context in `.omp/AGENTS.md` (Spec Kit-managed block; imports root `AGENTS.md`). Sticky rules in `.omp/RULES.md`. Memory is not authority.

**Independent Test**: After this plan exists, live context names the plan path; compacted session still applies the five sticky rules; no second same-scope client instruction file.

### Implementation for User Story 2

- [x] T004 [US2] Set `context_file: .omp/AGENTS.md` in `.specify/extensions/agent-context/agent-context-config.yml`. Leave `context_files` empty. Keep `context_markers` start `<!-- SPECKIT START -->` end `<!-- SPECKIT END -->`
- [x] T005 [US2] Create `.omp/AGENTS.md`: unmanaged preamble includes `@../AGENTS.md`; then empty managed block between `<!-- SPECKIT START -->` and `<!-- SPECKIT END -->`. Do not copy wiki routing out of root `AGENTS.md`
- [x] T006 [P] [US2] Create `.omp/RULES.md` with only: never skip verification; never modify generated files directly; never push or deploy without an explicit instruction; implementation MUST map to tasks; completion REQUIRES verification evidence. Conflict rule: safety beats live context; live context beats which feature is active
- [x] T007 [US2] Run `/speckit.agent-context.update` so the managed block in `.omp/AGENTS.md` points at `specs/005-omp-speckit-integration/plan.md`

**Checkpoint**: US1 + US2 independently testable (quickstart Story 2)

---

## Phase 5: User Story 3 - Independent work proceeds in bounded parallel (Priority: P3)

**Goal**: Project OMP config caps waves at four, recursion one hop. Three specialists only. Structured worker reports.

**Independent Test**: Config shows concurrency 4 and recursion 1; agents are only `spec-auditor`, `implementer`, `verifier` with `spawns: []`; dry-read a two-disjoint + one-shared wave.

### Implementation for User Story 3

- [x] T008 [US3] Create `.omp/config.yml` with `modelRoleStorage: project`; `task.batch: true`; `task.maxConcurrency: 4`; `task.maxRecursionDepth: 1`; `task.isolation.enabled: true`; `advisor.enabled: false`; `memory.backend: off`; `autolearn.enabled: false`; compaction enabled; `tools.approvalMode: write`; LSP on. Roles in this file: `default` balanced medium, `plan` strong high, `task` fast coding medium, `review` strong high, `smol` cheap low. Seed concrete model IDs from `~/.omp/agent/config.yml`. Do not set per-prompt models on agents except `@plan` / `@task` / `@review`
- [x] T009 [P] [US3] Create `.omp/agents/spec-auditor.md`: `name: spec-auditor`; `model: "@plan"`; tools `[read, grep, glob, lsp]`; `spawns: []`; `thinking-level: high`; `blocking: true`. Body: read spec/plan/tasks/code; report contradictions; do not modify files. Isolation off (read-only)
- [x] T010 [P] [US3] Create `.omp/agents/implementer.md`: `name: implementer`; `model: "@task"`; tools `[read, grep, glob, edit, write, bash, lsp]`; `spawns: []`. Body: implement only the assigned `tasks.md` item; preserve architecture; run targeted validation; return [contracts/worker-report.md](./contracts/worker-report.md) (`status` complete\|blocked\|failed; `task_ids`; `changed_files`; `tests_run`; `tests_passed`; `acceptance_criteria_verified`; `unresolved`). Isolation on when files are disjoint
- [x] T011 [P] [US3] Create `.omp/agents/verifier.md`: `name: verifier`; `model: "@review"`; tools `[read, grep, glob, bash, lsp]`; `spawns: []`; `thinking-level: high`; `blocking: true`. Body: verify against spec/plan/tasks/checklists; evidence from tests/diagnostics/code; do not modify implementation; `changed_files` always `[]`; same worker-report schema. Isolation off

**Checkpoint**: US3 independently testable (quickstart Story 3). T009–T011 after T008

---

## Phase 6: User Story 4 - Quality gates, then converge (Priority: P4)

**Goal**: One thin `/feature-fast` sequences unmodified Spec Kit commands, then implementer waves, then converge, then verifier. Direct OMP session only.

**Independent Test**: Read `.omp/commands/feature-fast.md` against [contracts/feature-fast.md](./contracts/feature-fast.md): analyze before waves; stop on material findings; append-only converge; empty input fails; no RPC path.

### Implementation for User Story 4

- [x] T012 [US4] Create `.omp/commands/feature-fast.md` per `specs/005-omp-speckit-integration/contracts/feature-fast.md`: require a feature description; invoke unmodified `/speckit.specify` → optional clarify → plan → checklist → tasks → analyze; stop on material findings; waves of `implementer` (≤4, isolated if disjoint, sequential if shared architectural files, `outputSchema` strict worker-report); `/speckit.converge`; implement only appended ids; `verifier` not isolated; short completion report. Do not edit `.omp/commands/speckit.*`. Do not add a Spec Kit workflow that re-owns implementation waves

**Checkpoint**: US4 independently testable (quickstart Story 3 dry-read)

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Agent-shaped observation of the whole baseline.

- [x] T013 Create `scripts/check-omp-baseline.sh` per `specs/005-omp-speckit-integration/contracts/check-omp-baseline.md`: no flags; cwd repo root; exit 0 iff integration omp, speckit specify+converge commands exist, `.omp/AGENTS.md` has `@../AGENTS.md` and both SPECKIT markers, `.omp/RULES.md` has the five constraints, `.omp/config.yml` has concurrency 4 / recursion 1 / advisor false / memory and autolearn off, three specialists with `spawns: []`, no phase-named agents, `feature-fast.md` exists, no CLAUDE.md added by this baseline; else exit 1 and one-line stderr; do not repair files
- [x] T014 Run `scripts/check-omp-baseline.sh` (exit 0) and `specs/005-omp-speckit-integration/quickstart.md` Stories 1–3. RPC/ACP as the session path is a fail

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: None
- **Foundational (Phase 2)**: After Setup — BLOCKS all stories
- **US1 (Phase 3)**: After Foundational — MVP
- **US2 (Phase 4)**: After Foundational; T005 before T007 (same `.omp/AGENTS.md`); T004 before T007; T006 parallel with T004/T005
- **US3 (Phase 5)**: After Foundational; T009–T011 after T008 (role aliases)
- **US4 (Phase 6)**: After Foundational; `/feature-fast` may land before specialists exist as markdown, but dry-read of waves needs US3 agents
- **Polish (Phase 7)**: After US1–US4 files exist (T013 observes them)

### User Story Dependencies

- **US1 (P1)**: After Phase 2 only
- **US2 (P2)**: After Phase 2; no US1 file overlap
- **US3 (P3)**: After Phase 2; no US2 file overlap
- **US4 (P4)**: After Phase 2; T012 new file; prefer after US3 so specialist names exist

### Parallel Opportunities

- T004 and T006 (config yml vs RULES)
- T005 and T006 (AGENTS vs RULES)
- T009, T010, T011 after T008
- Do not parallelize two edits to `.omp/AGENTS.md` or `.omp/config.yml`
- Do not edit generated `speckit.*` in any task

---

## Parallel Example: User Story 3

```text
# After T008 .omp/config.yml:
Task: spec-auditor.md (T009)
Task: implementer.md (T010)
Task: verifier.md (T011)
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Phase 1 Setup (no re-init)
2. Phase 2 Foundational (no MCP/CLAUDE twins)
3. Phase 3 US1 (native commands stay; no phase-named agents)
4. **STOP** — quickstart Story 1
5. Demo: `/speckit.specify` resolves from `.omp/commands/`

### Incremental Delivery

1. Setup + Foundational
2. US1 → native ownership
3. US2 → AGENTS import + RULES + agent-context target
4. US3 → config + three specialists
5. US4 → `/feature-fast`
6. Polish → check script + quickstart

---

## Notes

- [P] = different files, no incomplete deps
- No `src/` tree — harness files + one script
- Do not add test files unless a later command asks
- Do not edit generated `.omp/commands/speckit.*`
- Direct OMP session only; not RPC/ACP
- Commit after each task or logical group
- Stop at checkpoints
