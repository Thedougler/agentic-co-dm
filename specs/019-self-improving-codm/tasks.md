---

description: "Task list for Self-Improving Co-DM"
---

# Tasks: Self-Improving Co-DM

**Input**: Design documents from `/specs/019-self-improving-codm/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/, quickstart.md

**Tests**: No per-story TDD suite. Plan names one fixture check as the public seam (`specs/019-self-improving-codm/fixtures/check.py`); that lands in Polish. Assert files and Work outcomes. Do not snapshot `AGENTS.md` or `session-wrapup` wording.

**Organization**: Tasks are grouped by user story so each story can be implemented and validated independently.

**Writer**: Edits to `.agents/skills/session-wrapup/SKILL.md` are design-impact. `/speckit.implement` dispatches the designated writer with a scoped prompt (outcome, files, bounds, job) and `writing-for-agents`. Session agent writes `AGENTS.md`, `docs/agents/work.md`, `errors.md`, `scripts/error-ledger.py`, `wiki/templates/{encounter,rules,campaign-state,dm-intelligence}.md`, and `wiki/AGENTS.md` layout rows. No new skill. No new campaign `type`. No layout-kind frontmatter.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1–US6)
- Include exact file paths in descriptions

## Path Conventions

- Standing loop: `AGENTS.md`, `docs/agents/work.md`
- Wrapup reflection: `.agents/skills/session-wrapup/SKILL.md`
- Ledger helper: `scripts/error-ledger.py`
- Ledger file: `errors.md` (repo root, not wiki)
- Sitting log: append-only file next to `errors.md`, owned by the helper
- Source Material: `wiki/_raw/`
- System: `AGENTS.md`, `.agents/skills/`, `docs/agents/`
- Wiki templates: `wiki/templates/encounter.md`, `rules.md`, `campaign-state.md`, `dm-intelligence.md`
- Contract: `specs/019-self-improving-codm/contracts/self-improving-codm.md`
- Do not add a `self-improve` skill. Do not wrap `qmd` or git. Do not add a tokenizer. Do not add `type: encounter` or `type: rules`.

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Confirm existing owners so 019 points at them instead of restating.

- [X] T001 Review the Work gate and wiki-fact accept path in `docs/agents/work.md` and the Campaign Co-DM pointer in `AGENTS.md` against `specs/001-agentic-co-dm/` so 019 does not duplicate 001
- [X] T002 [P] Review `specs/019-self-improving-codm/contracts/self-improving-codm.md` and `specs/019-self-improving-codm/data-model.md` (table aim, sitting, error entry, helper, layout kind, layout move, reflection)
- [X] T003 [P] Review `docs/agents/skill-design-dispatch.md` for the wrapup design-impact edit; 012 does not gate reflection chat

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Shared ledger helper and no-new-skill pointer. Blocks all user stories.

**CRITICAL**: No user story work begins until this phase is complete.

- [X] T004 Create empty repo-root `errors.md` as the agent-owned error ledger (not a wiki page, not under `wiki/`)
- [X] T005 Create `scripts/error-ledger.py` with `error` (`append`, `drain`, `list`) and `sitting` (`record`, `list`) subcommands: arguments in, JSON or Markdown out, exit distinguishes done vs failed; `drain` without `cause_fixed` true exits non-zero; do not wrap `qmd` or git
- [X] T006 Persist sitting records as an append-only log next to `errors.md` owned by `scripts/error-ledger.py` (not `wiki/log.md`)
- [X] T007 Add a Campaign Co-DM pointer in `AGENTS.md` that the 019 loop lives in `AGENTS.md` plus `docs/agents/work.md`, wrapup owns the required reflection, and there is no new skill; do not restate the 001 Work gate; do not add a campaign `type`

**Checkpoint**: Ledger file, helper CLI, sitting log, and no-new-skill pointer exist.

---

## Phase 3: User Story 1 - Aim at these players (Priority: P1) 🎯 MVP

**Goal**: Shared table aim on the campaign hub (Campaign State). Missing aim is asked. Work that could swap tables is not aimed. DM Intelligence is not the aim.

**Independent Test**: Name a table of at least three players and a current campaign intent. Ask the DM and the Co-DM separately what the campaign is for. They match on who and on intent. A later prep proposal that could have been written for any table fails this test. The aim is on the hub, not a DM Intelligence page.

### Implementation for User Story 1

- [X] T008 [US1] In `AGENTS.md`: if table aim status is `missing`, ask the DM to name the players ("at least one; tests use three") and the current campaign intent before treating Work as aimed (FR-003)
- [X] T009 [P] [US1] In `docs/agents/work.md`: after DM accept, file table aim (`players` + `intent`) on the existing campaign hub; **home**: "Campaign hub wiki page, grouped under layout kind Campaign State"; status `missing` → `recorded` (after DM accept on the campaign hub) → `updated`; do not invent a new wiki kind or `type`
- [X] T010 [US1] In `docs/agents/work.md`: "Co-DM MUST NOT treat Work as aimed while `missing`"; "Work that could swap onto another table without edits is not aimed"; "DM Intelligence MUST NOT hold a second copy of the aim"; when the DM updates players or intent, later Work uses the updated aim (FR-001, FR-002, FR-004)

**Checkpoint**: Missing aim is asked; recorded aim is on the hub under Campaign State; generic-table Work does not count as aimed.

---

## Phase 4: User Story 2 - Gaps do not stall playable Work (Priority: P2)

**Goal**: Missing wiki fact or missing Co-DM practice still yields playable Work in that sitting; the gap is named; campaign-facing practice stays gated.

**Independent Test**: Ask for prep the wiki does not cover, and separately for a job the Co-DM has no standing practice for. In both cases the DM receives a proposal in that sitting, the gap is named, and how the Co-DM works is unchanged.

### Implementation for User Story 2

- [X] T011 [US2] In `AGENTS.md` and `docs/agents/work.md`: a missing wiki fact or missing Co-DM practice MUST NOT prevent playable Work in that sitting; when Work is offered despite a gap, name the gap (FR-005, FR-006)
- [X] T012 [US2] In `docs/agents/work.md`: a campaign-facing practice fix is a proposal the DM accepts, edits, or rejects; how the Co-DM works is unchanged until accept; a rejected fix is not applied (FR-007)
- [X] T013 [US2] In `AGENTS.md`: a gap that is only wasted context is closed by agents without a DM proposal; point at the token/helper/layout rules rather than restating them

**Checkpoint**: Gaps produce named, playable Work; campaign-facing practice does not change before accept.

---

## Phase 5: User Story 3 - Reflect, then improve only with the DM (Priority: P3)

**Goal**: Wrapup offers a reflection as chat Work. Reject leaves wiki and campaign-facing practice untouched. Accepted campaign or practice change is a proposal, still gated.

**Independent Test**: Finish wrapup for a session with at least one thing that served the table and one that did not. Confirm a reflection exists, the DM can accept or reject it, an accepted campaign change is proposed rather than filed, and an accepted campaign-facing practice change is proposed rather than applied. Confirm a rejected reflection leaves wiki and campaign-facing practice untouched.

### Implementation for User Story 3

- [X] T014 [US3] In `docs/agents/work.md`: after wrapup, offer a reflection; after prep, offer a reflection only if the DM asks; do not run reflection or improvement during a session (FR-008, FR-009, FR-014)
- [X] T015 [P] [US3] Dispatch the designated writer per `docs/agents/skill-design-dispatch.md` to add a required chat reflection step in `.agents/skills/session-wrapup/SKILL.md`: `observation` is "At least one concrete note about these players"; `next_change` optional; status `offered` → `accepted` | `edited` | `rejected`; "reject leaves wiki facts and campaign-facing practice unchanged"; instruct the writer to follow `.agents/skills/writing-for-agents`; do not run 012 blind-eval on reflection chat; session agent does not write that file
- [X] T016 [US3] In `docs/agents/work.md`: accepted reflection that needs a campaign fact change becomes a canon proposal and still waits for accept; accepted campaign-facing practice change becomes an improvement proposal and still waits for accept; later sittings of that kind of job follow the accepted change (FR-010–FR-013)

**Checkpoint**: Wrapup always offers inspectable reflection Work; wiki facts and campaign-facing practice change only after accept.

---

## Phase 6: User Story 4 - Agents cut waste, quality holds (Priority: P4)

**Goal**: Agents record sitting token cost (what was loaded and finished, not a tokenizer), cut wasted context, and create agent-shaped helpers for repeating jobs. The DM does not gate this.

**Independent Test**: Record token cost and accepted Work for a sitting. Agents apply an efficiency change without a DM accept step, including a helper when the job will repeat. Repeat the same kind of sitting. Token cost is lower, at least as much Work is accepted, quality still passes, and the later sitting uses the helper rather than re-teaching the procedure. The DM was not asked to manage any of this.

### Implementation for User Story 4

- [X] T017 [P] [US4] In `scripts/error-ledger.py` sitting `record`: `kind` is `prep` | `wrapup`; fields `jobs`, `paths_read`, `skills_loaded`, `helpers_used`, `waste_named`, `errors_filled`; `token_cost` is "Derived from paths/skills/output for same-kind compare — not a tokenizer"; status `open` → `recorded`; "every finished prep/wrapup sitting is `recorded`"; "DM is not a field"
- [X] T018 [US4] In `AGENTS.md`: agents record token cost of every prep or wrapup sitting; "The DM MUST NOT be asked to record or accept it"; compare only same-kind sittings (FR-019, FR-020)
- [X] T019 [US4] In `AGENTS.md`: agents cut wasted context without waiting; "A change MUST NOT count as an improvement if it lowers token cost by lowering Work quality"; "A change MUST NOT count as an improvement if it raises token cost for the same jobs without preventing a named failure" (FR-021–FR-025)
- [X] T020 [US4] In `AGENTS.md`: if a job will repeat and no existing command does it, create an agent-shaped helper without being asked ("Arguments in, text or JSON out, exit done vs failed"); use it on the next same-kind sitting; keep it current or remove it; "no helper for a one-off"; "No wrap of an existing command" (FR-026–FR-031)

**Checkpoint**: Finished sittings are recorded without the DM; helpers exist only for repeating jobs with no existing command.

---

## Phase 7: User Story 5 - Fill the error ledger, drain it when the wiki improves (Priority: P5)

**Goal**: Runtime failures append to `errors.md`. Drain only when the cause is actually fixed. The DM does not edit the ledger.

**Independent Test**: Cause a runtime failure. Confirm an entry exists. Land a wiki improvement that removes the cause. Confirm that entry is gone and that no other entry disappeared without its cause being fixed. The DM was not asked to edit the ledger.

### Implementation for User Story 5

- [X] T021 [P] [US5] In `scripts/error-ledger.py` error `append`/`drain`: Error Entry has `id` (stable id), `cause`, `sitting`, status `open` → `drained`, `cause_fixed` boolean; "drain requires true"; "Drain-without-fix is invalid"; "Bulk-clear is invalid"
- [X] T022 [US5] In `AGENTS.md`: on runtime failure, append to `errors.md` before the sitting is complete; drain matching entries when a wiki improvement or other landed fix actually removes the cause; leftover entries for already-fixed causes are wasted context; the DM MUST NOT fill, review, or drain the ledger; a wiki fact write that is the fix still waits on accept; drain after that write lands (FR-032–FR-038)

**Checkpoint**: Fill happens without the DM; drain happens only with `cause_fixed` after the fix lands.

---

## Phase 8: User Story 6 - Layout grows into agent-shaped structure (Priority: P6)

**Goal**: Mixed growth is regrouped by layout kind. Wiki kinds: Encounters, Rules, Campaign State, DM Intelligence. Agent-facing: System, Source Material. Existing `type` stays. Facts stay gated. Four wiki copy-start templates exist; existing pages in those groups are rewritten when facts stay the same.

**Independent Test**: Start from mixed System + Source Material (`wiki/_raw/`) and mixed Encounters + Rules wiki pages. After growth-triggered organization, retrieving one layout kind opens only that kind. The DM was not asked. Wiki facts and campaign `type` were not rewritten. Source Material was not filed as canon. Links still resolve. Aim remains on the hub. The four templates exist with pinned `type` values. Existing pages in those groups match template jobs without a fact change.

### Implementation for User Story 6

- [X] T023 [US6] In `AGENTS.md`: as agent-facing files and the wiki (llm-wiki) grow mixed, regroup so one job or layout kind does not load unrelated trees; trigger is `growth` ("mixed dump / unrelated load"). "Not `tidiness`"; "One-off files MUST NOT be reorganized solely for tidiness"; do not mandate a folder taxonomy (FR-039, FR-044)
- [X] T024 [US6] In `AGENTS.md`: wiki layout kinds are Encounters, Rules, Campaign State, and DM Intelligence; agent-facing layout kinds are System and Source Material; "MUST NOT duplicate an existing `type`"; do not add `type: encounter` or `type: rules`; no layout-kind frontmatter (FR-040)
- [X] T025 [US6] In `AGENTS.md`: wiki layout moves have `facts_changed` "Must be false for wiki moves", `type_changed` "Must be false", and `links_resolve` "Must be true after the move"; Source Material is `wiki/_raw/` staging; System is skills/`AGENTS.md`/`docs/agents`; "System and Source Material MUST NOT be treated as wiki canon"; "Copying table aim onto DM Intelligence is not a layout move"; wiki fact changes still wait on accept (FR-041–FR-046)
- [X] T030 [P] [US6] Create copy-start `wiki/templates/encounter.md` with existing campaign `type` `session-prep`; "MUST NOT add a campaign `type`"; follow `.agents/skills/writing-for-agents` for D&D content guidance; omit empty sections; pass is jobs not heading-order match (FR-047)
- [X] T031 [P] [US6] Create copy-start `wiki/templates/rules.md` with existing campaign `type` `lore`; "MUST NOT add a campaign `type`"; follow writing-for-agents; omit empty sections (FR-047)
- [X] T032 [P] [US6] Create copy-start `wiki/templates/campaign-state.md` with existing campaign `type` `lore`; table aim home is the campaign hub; "MUST NOT add a campaign `type`"; follow writing-for-agents (FR-047)
- [X] T033 [P] [US6] Create copy-start `wiki/templates/dm-intelligence.md` with existing campaign `type` `work`; "DM Intelligence is not the aim"; "MUST NOT add a campaign `type`"; follow writing-for-agents; "System and Source Material MUST NOT get wiki templates" (FR-047)
- [X] T034 [US6] In `wiki/AGENTS.md` layout table, add Encounter, Rules, Campaign State, and DM Intelligence rows that name jobs and the copy-start path (`wiki/templates/encounter.md`, `rules.md`, `campaign-state.md`, `dm-intelligence.md`); "Pass is those jobs, not heading-order match"; do not add `type: encounter` or `type: rules` (FR-047)
- [X] T035 [US6] Rewrite existing Encounters, Rules, Campaign State, and DM Intelligence wiki pages onto the matching templates; "Existing pages of that layout kind are rewritten onto the template when facts stay the same"; "A rewrite that would change facts waits on accept"; "Table aim MUST remain on the campaign hub" (FR-048)
**Checkpoint**: Growth splits mixed dumps by layout kind; wiki moves keep facts and `type`; four templates exist with pinned types; existing pages rewritten without fact change; System/Source Material stay non-canon; one-offs stay put.

---

## Phase 9: Polish & Cross-Cutting Concerns

**Purpose**: Public-seam fixture and artifact alignment after standing rules, helper, and wiki templates land.

- [X] T026 [P] Align final contract language in `specs/019-self-improving-codm/contracts/self-improving-codm.md` with landed standing rules (no new skill, no tokenizer, wrapup owns required reflection, layout kinds 34–37)
- [X] T027 [P] Align expected outcomes in `specs/019-self-improving-codm/quickstart.md`
- [X] T028 Add the runnable fixture check at `specs/019-self-improving-codm/fixtures/check.py` with `fixtures/wiki/` and `fixtures/ops/` covering quickstart scenarios 1–8 (missing aim on hub not DM Intelligence; gap does not stall; wrapup reflection is Work; sitting is recorded without the DM; ledger fill and drain; helper on a repeating job; mixed Encounters vs Rules plus System vs Source Material; layout is not a canon back door). Assert observable files and Work outcomes; drain without `cause_fixed` fails the helper; do not snapshot `AGENTS.md` or `session-wrapup` wording
- [X] T029 Run every scenario in `specs/019-self-improving-codm/quickstart.md` via `.venv/bin/python specs/019-self-improving-codm/fixtures/check.py`
- [X] T036 Extend `specs/019-self-improving-codm/fixtures/check.py` for quickstart scenarios 9–10: four templates exist with `type` `session-prep`/`lore`/`lore`/`work`; no `type: encounter` or `type: rules`; existing-page rewrite keeps facts and aim on the hub; structure-only rewrite has no DM accept; fact-changing rewrite fails without accept
- [X] T037 Run every scenario in `specs/019-self-improving-codm/quickstart.md` via `.venv/bin/python specs/019-self-improving-codm/fixtures/check.py`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion — BLOCKS all user stories
- **User Story 1 (Phase 3)**: Depends on Foundational — MVP
- **User Story 2 (Phase 4)**: Depends on Foundational
- **User Story 3 (Phase 5)**: Depends on Foundational
- **User Story 4 (Phase 6)**: Depends on Foundational helper skeleton
- **User Story 5 (Phase 7)**: Depends on Foundational helper skeleton
- **User Story 6 (Phase 8)**: Depends on Foundational — layout standing rule; aim-on-hub constraint shares US1
- **Polish (Phase 9)**: Depends on the desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: After Foundational only.
- **User Story 2 (P2)**: After Foundational. Shares `docs/agents/work.md` with US1/US3 — serialize those edits.
- **User Story 3 (P3)**: After Foundational. Wrapup skill is independent; `work.md` reflection gate shares that file with US1/US2.
- **User Story 4 (P4)**: After Foundational. Helper sitting fields share `scripts/error-ledger.py` with US5.
- **User Story 5 (P5)**: After Foundational. Error fields share `scripts/error-ledger.py` with US4.
- **User Story 6 (P6)**: After Foundational. Shares `AGENTS.md` with US1/US2/US4/US5 — serialize those edits. Aim-on-hub vs DM Intelligence depends on US1 landing first if one writer.

### Parallel Opportunities

- T002 and T003 can run in parallel
- T009 can run in parallel with T008 (different files)
- T015 can run in parallel with T014 (wrapup skill vs `work.md`)
- T017 can run in parallel with T018–T020 (helper vs `AGENTS.md`)
- T021 can run in parallel with T022 (helper vs `AGENTS.md`)
- T026 and T027 can run in parallel after implementation
- T030–T033 can run in parallel (different template files)
- `AGENTS.md` tasks (T007, T008, T011, T013, T018–T020, T022–T025) are sequential — one writer
- `docs/agents/work.md` tasks (T009, T010, T011, T012, T014, T016) are sequential — one writer
- `scripts/error-ledger.py` tasks (T005, T006, T017, T021) are sequential — one writer
- `wiki/AGENTS.md` T034 and rewrite T035 are sequential after T030–T033

---

## Parallel Example: User Story 1

```text
T008 In AGENTS.md: ask for table aim while status is missing
T009 In docs/agents/work.md: file players + intent on the campaign hub under Campaign State
```

## Parallel Example: User Story 3

```text
T014 In docs/agents/work.md: wrapup reflection required; prep only if asked
T015 Dispatch designated writer for .agents/skills/session-wrapup/SKILL.md reflection step
```

## Parallel Example: User Story 4

```text
T017 Sitting record fields in scripts/error-ledger.py
T018 Token-cost ownership standing rule in AGENTS.md
```

## Parallel Example: User Story 6 templates

```text
T030 wiki/templates/encounter.md type session-prep
T031 wiki/templates/rules.md type lore
T032 wiki/templates/campaign-state.md type lore
T033 wiki/templates/dm-intelligence.md type work
```


---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL — blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Independent Test — named table of three players; DM and Co-DM match on who and intent; aim on hub not DM Intelligence; generic-table prep fails
5. Then continue to US2 (gaps) before claiming the loop is closed

### Incremental Delivery

1. Setup + Foundational → helper and no-new-skill pointer ready
2. Add US1 → shared aim on hub (MVP)
3. Add US2 → gaps do not stall
4. Add US3 → wrapup reflection as Work (designated writer)
5. Add US4 → sitting records and helpers
6. Add US5 → ledger fill/drain
7. Add US6 → layout kinds (wiki vs agent-facing) and four wiki templates
8. Polish → fixture check covering quickstart 1–10

### Dispatch

- T015: designated writer only. Session agent writes the scoped prompt, leaves `.agents/skills/session-wrapup/SKILL.md` unmodified, then invokes `claude -p --model claude-opus-4-6 --effort medium` per `docs/agents/skill-design-dispatch.md`.
- T030–T035: session agent. Follow writing-for-agents (D&D content guidance) for the four templates. 012 still binds.
- All other tasks: session agent.
- On usage-limit wait: leave T015 incomplete on this file with a retry time; complete independent tasks; do not write the wrapup skill in-session unless both designated writers are usage-limited.

---

## Notes

- [P] tasks = different files, no incomplete dependencies
- [Story] label maps task to US1–US6
- Data-model constraints are quoted in T008–T010, T015, T017, T020, T021, T023–T025, T030–T035
- No new skill, no tokenizer, no second ledger helper, no wiki `type` for table aim / Encounters / Rules, no layout-kind frontmatter, no mandated folder taxonomy, no wiki templates for System or Source Material
- Stop at any checkpoint to validate the story independently

---

## Phase 10: Convergence

- [X] T038 In `wiki/AGENTS.md` Approval, except layout moves and structure-only template rewrites that keep facts and `type` unchanged so agents do not wait on DM accept per FR-007, FR-041, FR-048 (contradicts)
