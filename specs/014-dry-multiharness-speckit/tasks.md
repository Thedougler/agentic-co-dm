---
description: "Task list for DRY multi-harness Spec Kit repair"
---

# Tasks: DRY Multi-Harness Spec Kit

**Input**: Design documents from `/specs/014-dry-multiharness-speckit/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/

**Tests**: None requested. Verification is `scripts/check-speckit-dry.sh` and `specify integration status --json` (US7).

**Organization**: User stories from spec.md. Do not switch git branches. Do not edit `specs/015-wiki-ingest-polish/`. Do not run `specify init --force`. Do not add project-authored Spec Kit scripts; use shipped `--script py`.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Parallel (different files, no incomplete deps)
- **[Story]**: US1–US7 from spec.md
- Exact file paths in every task

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Confirm brownfield Spec Kit is healthy before mutation

- [ ] T001 Verify `specify integration status --json` reports `status: ok` with current `omp` install in `.specify/integration.json`; do not run `specify init --force`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Classify owners so later deletes/installs cannot drop unique intent

**⚠️ CRITICAL**: No user story work until this phase is complete

- [ ] T002 Classify instruction files against `specs/014-dry-multiharness-speckit/contracts/ownership-layout.md`: root `AGENTS.md` (owner), root `CLAUDE.md` (duplicate if `cmp` matches `AGENTS.md`), `.omp/AGENTS.md` (import + SPECKIT block), `.omp/RULES.md` (keep), `.github/copilot-instructions.md` (out of scope)
- [ ] T003 Record standing preserve list: `.specify/memory/constitution.md`, existing `specs/*/spec.md` except this feature, `.omp/RULES.md`, `.omp/agents/spec-auditor.md`, `.omp/agents/implementer.md`, `.omp/agents/verifier.md`, `.omp/commands/feature-fast.md`, existing `.omp/config.yml` keys

**Checkpoint**: Classification done; force-init still forbidden

---

## Phase 3: User Story 1 - One owner for every project fact (Priority: P1) 🎯 MVP

**Goal**: Root `AGENTS.md` is the operating map. Constitution and specs stay the owners. No second policy manual.

**Independent Test**: Sample operating rules, principles, and feature requirements. Each has one owner; `AGENTS.md` points at them instead of restating them.

### Implementation for User Story 1

- [ ] T004 [US1] Add a short Sources of Truth section to `AGENTS.md` pointing at `.specify/memory/constitution.md`, `specs/`, and `docs/` without pasting constitution principle text (KnowledgeOwner: `AGENTS.md` must not own constitution text or feature requirements)
- [ ] T005 [US1] Add a short Workflow section to `AGENTS.md` stating Spec Kit artifacts are the handoff protocol and harness files must not copy feature requirements
- [ ] T006 [US1] Keep existing wiki/skill routing in `AGENTS.md`; do not turn the file into an encyclopedia and do not delete load-bearing routing

**Checkpoint**: `AGENTS.md` maps to owners; constitution and specs are unchanged

---

## Phase 4: User Story 2 - Repair preserves unique human intent (Priority: P1)

**Goal**: Unique intent is migrated before any delete or regenerate. Existing specs and constitution survive.

**Independent Test**: Unique notes that existed before repair are in their owner documents; generated adapters do not hold those notes; existing feature specs remain.

### Implementation for User Story 2

- [ ] T007 [US2] Re-run `cmp AGENTS.md CLAUDE.md` immediately before any Claude delete; if they differ, migrate unique `CLAUDE.md` lines into `AGENTS.md` first
- [ ] T008 [US2] Leave preserve-list files from T003 unmodified except `.omp/config.yml` isolation keys added later in US4
- [ ] T009 [US2] If `specify integration status --json` later reports `modified_managed_files` ≠ 0, migrate unique text out of those files before any regenerate (GeneratedAdapter state `modified` → investigate, not overwrite)

**Checkpoint**: Preserve list intact; no unique Claude intent discarded

---

## Phase 5: User Story 3 - Native disposable adapters (Priority: P2)

**Goal**: Codex, Grok, OMP, and Claude each have Spec Kit-generated adapters using shipped Python scripts. Default integration is Codex.

**Independent Test**: Four native adapter locations exist. No extra hand-copied Spec Kit command dirs. `specify integration status --json` matches `contracts/specify-status.md`.

### Implementation for User Story 3

Serialize these: they all mutate `.specify/integration.json`.

- [ ] T010 [US3] Run `specify integration install codex --script py` so `.agents/skills/speckit-*/` exists; do not hand-edit generated skills
- [ ] T011 [US3] Run `specify integration install grok --script py` so `.grok/skills/speckit-*/` exists; do not skip because Codex skills are visible
- [ ] T012 [US3] Run `specify integration install claude --script py` so `.claude/skills/speckit-*/` exists
- [ ] T013 [US3] Run `specify integration upgrade omp --script py` so OMP uses Spec Kit shipped Python, not `script: sh` in `.specify/init-options.json` and `.specify/integration.json`
- [ ] T014 [US3] Register extensions by `specify integration use grok`, then `omp`, then `claude`, then `specify integration use codex` last (default_integration = `codex`; not a mandate that every task uses Codex)
- [ ] T015 [US3] Confirm `specify integration status --json`: `status` is `ok`, `default_integration` is `codex`, installed set includes `codex`, `grok`, `omp`, `claude`, `missing_managed_files` 0, `modified_managed_files` 0, `invalid_manifest_paths` 0, `findings` empty
- [ ] T016 [US3] Confirm generated adapters exist at `.agents/skills/speckit-*/SKILL.md`, `.grok/skills/speckit-*/SKILL.md`, `.omp/commands/speckit.specify.md`, `.claude/skills/speckit-*/SKILL.md` and contain no unique project policy

**Checkpoint**: Four native adapters; default Codex; script py

---

## Phase 6: User Story 4 - Compatibility discovery does not create a second policy (Priority: P2)

**Goal**: Claude imports `AGENTS.md`. OMP and Grok do not treat Claude copies as project policy. One live-context injection site.

**Independent Test**: `.claude/CLAUDE.md` is an import shim. Root `CLAUDE.md` gone. `.omp/AGENTS.md` is import-only. SPECKIT markers only in `AGENTS.md` among those three files.

### Implementation for User Story 4

Touches `AGENTS.md` after US1; do not parallel with US1/US5.

- [ ] T017 [US4] Create `.claude/CLAUDE.md` containing `@../AGENTS.md` plus a Claude-only stub; no wiki routing, constitution, or specs (InstructionShim)
- [ ] T018 [US4] Delete root `CLAUDE.md` only after T007 and T017
- [ ] T019 [US4] Set `.specify/extensions/agent-context/agent-context-config.yml` `context_file: AGENTS.md` (LiveContextBlock file = `AGENTS.md` only)
- [ ] T020 [US4] Ensure `AGENTS.md` has `<!-- SPECKIT START -->` / `<!-- SPECKIT END -->` as the only project live-context injection among `{AGENTS.md,.omp/AGENTS.md,.claude/CLAUDE.md}`
- [ ] T021 [US4] Reduce `.omp/AGENTS.md` to `@../AGENTS.md` only; remove its `<!-- SPECKIT START -->` block
- [ ] T022 [US4] Add `disabledExtensions: [context-file:project:CLAUDE.md]` to `.omp/config.yml` without dropping existing keys (OMP array settings replace, they do not merge). Do not set `disabledProviders: [claude]`. Do not disable `anthropic`
- [ ] T023 [US4] Document user-level Grok `[compat.claude] agents/skills/rules = false` in `docs/agents/harness-dispatch.md` (or a pointer from `AGENTS.md`); do not pretend a project `.grok/config.toml` governs it

**Checkpoint**: Canonical contract wins at runtime for Claude/OMP; Grok isolation documented

---

## Phase 7: User Story 5 - Handoff is repository state (Priority: P2)

**Goal**: Switching harnesses does not re-specify. One writer per canonical artifact. Parallel work uses separate workspaces.

**Independent Test**: `AGENTS.md` Workflow section forbids re-specify, shared-workspace multi-writers, and silent requirement changes in `tasks.md`.

### Implementation for User Story 5

Same file as US1/US4 — after those edits.

- [ ] T024 [US5] Extend the Workflow section in `AGENTS.md` with: read existing `specs/<feature>/{spec,plan,tasks}.md` instead of re-prompting; change spec first then plan then tasks; one writer per canonical artifact; parallel implementation uses separate workspaces
- [ ] T025 [US5] State in `AGENTS.md` that harness changes pass paths, commits, artifacts, expected phase, and only constraints absent from the repo — not pasted copies of canonical documents

**Checkpoint**: Handoff rules live in the operating map only

---

## Phase 8: User Story 6 - Outer-loop orchestration without a fifth source of truth (Priority: P3)

**Goal**: In-repo dispatcher procedure for Grok Bot. No Bot-local Spec Kit. No copied policy/specs.

**Independent Test**: `docs/agents/harness-dispatch.md` matches `contracts/harness-dispatch.md`. No `.grok-bot/speckit/`.

### Implementation for User Story 6

- [ ] T026 [P] [US6] Create `docs/agents/harness-dispatch.md` with purpose, procedure, canonical pointers, prohibitions, and return report per `specs/014-dry-multiharness-speckit/contracts/harness-dispatch.md`
- [ ] T027 [US6] Ensure `docs/agents/harness-dispatch.md` contains no `# Agentic Co-DM Constitution` text, no feature requirements, and no Spec Kit prompt bodies
- [ ] T028 [US6] Confirm no `.grok-bot/speckit/` (or equivalent Bot-local Spec Kit pack) exists; do not create one
- [ ] T029 [US6] Point `AGENTS.md` Sources of Truth at `docs/agents/harness-dispatch.md` (after T004)

**Checkpoint**: Orchestrator procedure is one file; Bot is not a Spec Kit integration

---

## Phase 9: User Story 7 - Manifest-aware maintenance and drift detection (Priority: P3)

**Goal**: Machine-readable healthy status. Check script + CI fail on integration errors and ownership invariants. 005 check still passes OMP baseline.

**Independent Test**: Healthy tree: both check scripts exit 0. Fixture with status error or root `CLAUDE.md` policy twin fails `check-speckit-dry.sh`. Adapters not byte-compared.

### Implementation for User Story 7

Depends on US3 adapters and US4 shims.

- [ ] T030 [US7] Create `scripts/check-speckit-dry.sh` per `specs/014-dry-multiharness-speckit/contracts/check-speckit-dry.md`: cwd repo root, no flags, stdout pass line, exit 0/1, observes status JSON, `script` py not sh, no root `CLAUDE.md`, shims, single SPECKIT block, four adapter locations, dispatcher file, no project-authored Spec Kit scripts
- [ ] T031 [US7] Relax `scripts/check-omp-baseline.sh` so it does not require `integration == omp` or fail a thin `.claude/CLAUDE.md` import; keep OMP command, RULES, specialist, feature-fast, cap checks
- [ ] T032 [P] [US7] Add `.github/workflows/speckit-dry.yml` that runs `specify integration status --json` and `scripts/check-speckit-dry.sh` and fails on `status != ok` or exit 1; do not byte-compare generated adapters (FR-027)
- [ ] T033 [US7] Run `scripts/check-speckit-dry.sh` and `scripts/check-omp-baseline.sh`; both must exit 0

**Checkpoint**: Drift fails closed; 005 OMP baseline still green

---

## Phase 10: Polish & Cross-Cutting Concerns

**Purpose**: Quickstart validation across stories

- [ ] T034 Run the validation steps in `specs/014-dry-multiharness-speckit/quickstart.md` (status JSON, shims, both check scripts)
- [ ] T035 Confirm no unmanaged leftover Spec Kit command copies (`**/.claude/commands/speckit.*`, `**/.grok/commands/speckit.*`) remain active
- [ ] T036 Confirm `.specify/scripts/` contains only Spec Kit-shipped files; no repo-authored replacements for `--script py`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: Immediate
- **Foundational (Phase 2)**: After Setup — BLOCKS all stories
- **US1 (Phase 3)**: After Foundational — MVP
- **US2 (Phase 4)**: After Foundational; complete before US4 deletes
- **US3 (Phase 5)**: After Foundational; serialize T010–T015 (shared `.specify/integration.json`)
- **US4 (Phase 6)**: After US1 + US2; T018 after T007 and T017
- **US5 (Phase 7)**: After US1 (same file `AGENTS.md`); after US4 live-context markers
- **US6 (Phase 8)**: After Foundational; T026 parallel; T029 after T004
- **US7 (Phase 9)**: After US3 + US4
- **Polish**: After desired stories

### User Story Dependencies

- **US1**: After Foundational
- **US2**: After Foundational; gates US4 delete
- **US3**: After Foundational; gates US7
- **US4**: After US1 + US2
- **US5**: After US1 + US4 (`AGENTS.md`)
- **US6**: After Foundational; T026 [P]; T029 needs US1
- **US7**: After US3 + US4

### Parallel Opportunities

- T026 (dispatcher file) can run beside US3 installs
- T032 (workflow file) can run beside T030 once contracts are known; must not land red CI before T017–T018
- Do not parallel tasks that edit `AGENTS.md` (T004–T006, T020, T024–T025, T029)
- Do not parallel Spec Kit install/upgrade/use commands

### Parallel Example: US6 + US3

```bash
# After Foundational:
Task: "Create docs/agents/harness-dispatch.md per contracts/harness-dispatch.md"
# Meanwhile, sequentially:
specify integration install codex --script py
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. T001–T003
2. T004–T006 (`AGENTS.md` map)
3. Stop and sample 20 facts for single ownership among map/constitution/specs

### Incremental Delivery

1. Setup + Foundational
2. US1 map → demo
3. US2 preserve checks
4. US3 adapters (`--script py`, default Codex)
5. US4 shims + OMP isolation
6. US5 handoff text
7. US6 dispatcher
8. US7 check + CI
9. Polish / quickstart

### Parallel Team Strategy

One writer for `AGENTS.md`. One writer for `.specify/integration.json` (US3). Dispatcher doc and check script can use other writers after US3/US4.

---

## Notes

- [P] = different files, no incomplete deps
- Generated adapters are disposable; never add policy there
- User-level Grok config is documented, not repo-enforced
- Copilot twin is out of scope
