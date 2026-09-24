# Feature Specification: Self-Improving Architecture

**Feature Branch**: `030-self-improving-architecture`

**Created**: 2026-09-24

**Status**: Draft

**Input**: User description: "The architecture should collapse, not expand. One loop, one evaluation path, one error surface, one ownership model, and a small set of reliable commands. Make normal agent work continuously improve the repository: when the system makes a task unnecessarily difficult, fix the source of that difficulty, prove the fix, then continue the task." Full request: `/workspace/specify-inbox/self-improving-architecture.md` (20 sections, three-phase implementation order). Addendum: improve the wiki CLI using the `cli-for-agents` guidance.

**Guiding principle** (Nick, 2026-09-24; binding, see FR-046 and SC-014): the overall goal is simplification, reliability, and ease of future development. The work improves, fixes, simplifies, and consolidates the existing systems rather than extending them. New code is allowed where it is used well, but sprawling extra code is not, and the result must be maintainable. There is no line-count limit. This is primarily an agentic skill project. Code is a relatively minor part of the repository and exists to assist agents: it does deterministic work that is not worth an agent's reasoning. In Nick's words: "No code should be making judgement calls; that's purely the agent's domain, and those judgement calls must be backed by skills. Code is diagnostic, not a prosthetic for reasoning."

## Clarifications

### Session 2026-09-24

- Q: Should the repo-local `Deprecated` Vale style and the `CoDM` vocabulary move to Python tooling along with the removed `CoDM` style, or stay in Vale? (FR-022, FR-023) → A (Nick's decision, 2026-09-24): Remove only the `CoDM` Vale style reference. The repo-local `Deprecated` style (`styles/Deprecated/*.yml`, including `DMThesis.yml` and `FactionClock.yml`) stays in Vale unchanged, and `Vocab = CoDM` stays unchanged. Nothing moves to Python. This replaces an earlier agent proposal to move `Deprecated` into Python tooling.
- Q: The constitution's principle XIII requires every friction to be logged and diagnosed by a different agent. Should FR-006–FR-008 be narrowed to fit it, or should the constitution be amended to match the request? (FR-006–FR-008) → A: Keep FR-006–FR-008 as requested. Amending principle XIII is a blocking prerequisite, done as separate Constitution work before implementation (see Assumptions, "Dependency"; met by v6.0.0 590af34e and v6.0.1 bf021f03). Reason: request §3–§4 and the Core Rule have the agent that meets friction fix the source, verify, and continue, and they keep `errors.md` for reusable unresolved defects only. XIII requires logging every friction before continuing and a diagnosis by a different agent, so a careful reading still finds no way to satisfy both. Confirmed by Nick, 2026-09-24.
- Q: What time target should SC-007 set for scoped lint and `wiki health`, given that the 5-second figure was assumed? (SC-007) → A: The target is based on a measurement taken 2026-09-24 at d1c3250 on an 8-core Linux box without the Vale binary. One changed page with a lint-cache miss took 3.1 s (identity 0.94 s). Two changed pages took 3.8 s (identity 1.3 s). An unchanged page came from the lint cache in 0.18 s. e-213's ~38 s was recorded before commit 6c374829 limited pairwise similarity to selected pages, but identity still walks the whole vault. The "warm, unchanged" target is already met, so SC-007 now covers the cache-miss path: under 5 s including Vale, with identity work limited to the selected pages and their cheap-signal candidates. No health timeout is defined in the repository; the timeout in e-208 is the agent harness's. So health must finish without timing out and record its wall time rather than meet an invented number. Confirmed by Nick, 2026-09-24. The health bound and the measurements with Vale were updated in the health-bound decision below.
- Q: What shape does each `errors.md` evidence occurrence take, and how is the recurrence metric counted once drained entries are removed? (FR-006, FR-009, FR-010) → A: `evidence` is a list of occurrences `{sitting, detail}`. On migration, each entry's current `sitting` and `cause` text become its first occurrence. `status` and `cause_fixed` are dropped because only open entries remain. The recurrence metric counts the occurrences after the first on open entries, reported as a total and per sitting. Reason: request §4 names exactly four fields. `sitting` is the only existing field that dates an occurrence. Git history keeps drained entries. Confirmed by Nick, 2026-09-24.
- Q: Is the eval schema's `skill` a new field on each record, or the per-file owner that already exists? (FR-013) → A: `skill` is the file-level `skill_name`. It is required in every `evals/evals.json` and must be added to the 7 files missing it: `session-beats`, `wiki-capture`, `wiki-context-pack`, `wiki-ingest`, `wiki-lint`, `wiki-query`, and `wiki-update`. The per-record `subject_skill` stays as the optional override that `scripts/luna-eval` already honors. Other existing optional keys (`core`; file-level `trajectory_records`, `principles`) are kept. Reason: the owning skill is one fact per file (constitution V), so copying it into 533 records would create competing copies. Confirmed by Nick, 2026-09-24.
- Q: Which skills count as owners for FR-003 and SC-005? (FR-003, SC-005) → A: Decided by Nick, 2026-09-24: the six owners named in the request (§2): `place-design`, `faction-design`, `session-beats`, `run-guide`, `wiki-query`, `wiki-lint`. Every skill still keeps its own ownership statement. Further `skill_selected` evals are added from real misroutes.
- Q: What time bound does `wiki health` meet, and may lint keep rewriting tracked cache files? (SC-007, FR-017, FR-028) → A: Decided by Nick, 2026-09-24: health must finish under 50 s whenever the identity index is current, including after a lint-rules change that empties the lint cache, and under 10 s when only a few pages changed. A from-scratch rebuild is recorded, not bounded. `wiki/_meta/lint-cache.json`, `wiki/_meta/identity-index.json`, and `styles/config/vocabularies/CoDM/accept.txt` stay tracked and count as FR-028 bookkeeping, not read-side mutation. Basis: e-208's harness kill at 52 s; health measured at 82.0 s cold and 2.6 s warm.
- Q: How are semantic quality, non-inferiority, and measurable reduction measured for promotion? (FR-016, FR-044, SC-012) → A: Decided by Nick, 2026-09-24: semantic quality is the pass rate of the eval's `quality`-type assertions. A candidate is non-inferior when, with one run per configuration on the same evals, no eval's task outcome is worse and no assertion that passed for the incumbent fails. A measurable reduction is a lower median of tool calls, retries, or tokens, with none of the three higher.
- Q: Which consistency fixes came out of analysis, plan, and checklist review? → A: Applied without a product choice: (1) identity candidates include cached character-profile prefilter passes (> 0.6), so FR-026 holds (FR-024, US4-1, SC-007); (2) FR-007 "same cause" means the same `source` and a mechanical cause match, and a forced attach cannot cross sources (tightened to an exact match by the rule that code reports and agents decide); (3) `expected_output` is optional (all 533 records have one; the request's examples omit it); (4) the assertion type list is fixed, with `qualitative`/`structural` folded into `quality`/`structure`; (5) the SC-009 window stays an assumption; (6) stale text corrected (XIII dependency met, nine ledger entries, SC-007 measurements with Vale); (7) SC-003 counts all records; (8) "cold agent" and "invocation error" defined for SC-010; (9) the FR-019 baseline model and effort are pinned; (10) FR-017's read-side mutation scope is defined.
- Q: What overriding goal constrains how this feature is built? → A: Decided by Nick, 2026-09-24: simplify, make it reliable, keep it maintainable, and improve and fix existing systems rather than extend them. This is not zero code, but every piece of new code must be used well. No line-count limit. Recorded as FR-046 and SC-014.
- Q: Where is the line between skills and code? → A: Decided by Nick, 2026-09-24: this is primarily an agentic skill project, and code is a relatively minor part that assists agents. Behavior and judgment belong in skills (`SKILL.md` instructions, references, evals). Code exists only for deterministic, mechanical work that is not worth an agent's reasoning, such as lint, indexing, schema checks, eval running, and file bookkeeping. Sharpened by Nick the same day: "No code should be making judgement calls; that's purely the agent's domain, and those judgement calls must be backed by skills. Code is diagnostic, not a prosthetic for reasoning." Code may detect, measure, check, index, and report facts, and may apply only fully deterministic fixes. Every agent judgment names its governing skill. Recorded as FR-046 rule 5 and SC-014 (d) and (e).
- Q: Should `wiki-lint --consolidate`'s threshold promotion (`draft` → `reviewed` when `base_confidence > 0.7` and age > 30 days) stay automatic? → A: Decided by Nick, 2026-09-24: bring it into scope. The score and age are only reported, and the agent decides promotion under the `wiki-lint` skill. The rule lives in `.agents/skills/wiki-lint/consolidate.md` §3; `scripts/wiki-lint` `consolidate_main` currently emits no actions. Recorded in FR-046 rule 5 and SC-014 (f). **Superseded by FR-047** (next bullet): there is no promotion at all.
- Q: What decides wiki canon, and what happens to page lifecycle, promotion, and confidence? → A: Decided by Nick, 2026-09-24: canon is three rules in precedence order: "Something is canon if the DM says so > something is canon if it's present in the wiki in multiple places > something is canon if it doesn't conflict with the wiki." That is the entire system. The lifecycle states, `base_confidence`, `lifecycle_changed`, `lifecycle_reason`, age rules, and consolidate promotion are the kind of overengineering this feature removes. Recorded in FR-047 and SC-015; this supersedes FR-046 rule 5's consolidate-promotion bullet and SC-014 (f).

## Classification and Scope

- **work_class**: `agent-system`
- **route**: `full-sdd`
- **Objective**: Normal owner work repairs the source of any friction it meets, proves the repair with the one existing evaluation path, and resumes the original task, so the repository gets easier for the next agent without a separate self-improvement system.
- **User value**: The DM gets finished Work with fewer stalls, fewer repeated failures, and shorter trajectories; maintainers get one evaluator, one error surface, and commands that do their own bookkeeping.
- **In scope**: The 20 sections of the request, reduced to one runtime loop, one ownership model, one friction rule, one error surface (`errors.md`), one evaluation system (`scripts/luna-eval` shared with `skill-creator`), one promotion rule, the three-rule wiki canon replacing page lifecycle, promotion, and confidence (FR-047), and fixes to the named existing commands, checkers, Vale configuration, and eval corpus.
- **Out of scope**: New orchestrators, workflow engines, optimizer runtimes, loop ledgers, progress commands, parallel eval runners, new skills without repeated usage evidence, hand-maintained ownership maps outside the skills, campaign canon changes, and edits to `.specify/memory/constitution.md`.
- **Canon impact**: The rule that decides canon changes to FR-047's three rules, and page lifecycle and confidence metadata is deleted. No campaign fact is added, removed, or edited. Constitution X states the same rule verbatim; the amendment this depended on is met (constitution v7.0.0, commit f489409d).

### Verified repository surfaces

| Request names | Real path / state on `main` (2026-09-24) |
|---|---|
| Capability loop | `AGENTS.md` "Capability loop" (line 72) and "Capability execution contract"; full rule in `docs/agents/hybrid-sdd.md`; formalized by `specs/029-agent-loop-closure/spec.md` FR-001 |
| Owners | `.agents/skills/place-design/`, `faction-design/`, `session-beats/`, `run-guide/`, `wiki-query/`, `wiki-lint/` (all present, each with `evals/evals.json`) |
| `scripts/luna-eval` | Present; reads `<skill>/evals/evals.json` fields `id`, `prompt`, `files`, `outputs`, `context`, `subject_skill`; writes `<out>/<name>/<config>/run-<n>/{outputs/, events.jsonl, final.txt, timing.json}` |
| `skill-creator` | `.agents/skills/skill-creator/`; its `scripts/run-eval.py` expects `{"query", "should_trigger"}` entries and `references/schemas.md` uses `expectations[]` — incompatible with the repo corpus (open ledger entry e-210) |
| Eval corpus | 60 `.agents/skills/*/evals/evals.json` files, 533 evals; 390 use typed `assertions[]` (types: quality, guardrail, process, content, structure, and rarer variants), 143 use `expectations[]`; no `skill_selected` or `behavior` assertion type exists yet |
| Stale eval behavior | "Work gate" / "chat proposal" / approval wording appears 42 times across 13 eval files (e.g. `place-design` eval 1 asserts a work gate before writes), contradicting feature 026's removal of Work gates |
| `errors.md` | Repo root; JSON-lines entries with `id`, `cause`, `cause_fixed`, `sitting`, `status`; written by `scripts/error-ledger.py` (`error append`/`drain`/`list`). No `source` or `evidence` field exists |
| Feature 026 | `specs/026-agent-autonomy-scope/`; its plan, tasks, quickstart, research, and contract cite `scripts/check-agent-standards.py`, `tests/test_agent_standards.py`, and rules `AGENT001`–`AGENT003`, none of which exist on `main` |
| Feature 029 | `specs/029-agent-loop-closure/`; `tasks.md` has 9 open evidence tasks (T003, T011, T018, T030, T037, T044, T046, T047, T049) |
| Wiki CLI | `scripts/wiki` (`lint`, `lint fix` via a positional `fix` token, `query`, `mutate`, `repair`, `health`); engine in `tools/wiki_ops/`; `scripts/wiki-lint`; `scripts/manifest.py`; `scripts/error-ledger.py` |
| Scoped identity | `tools/wiki_ops/identity.py` walks the whole vault (`vault.rglob("*.md")`) on every run; since 6c374829 (2026-09-24) pairwise similarity is limited to pairs touching selected pages. Open entries e-206 (45.9 s whole-vault, 44.3 s identity), e-208 (52 s, health timeout), e-213 (~38 s to lint 2 pages, before 6c374829). Measured 2026-09-24 at d1c3250 (8-core Linux, no Vale binary): 1 changed page 3.1 s (identity 0.94 s), 2 changed pages 3.8 s (identity 1.3 s), unchanged page 0.18 s (lint-cache hit). Re-measured with Vale 3.21.0 at bf021f03: 1 changed page 3.72 s, cache hit 0.28 s, `wiki health` 82.0 s cold (identity 54.7 s) and 2.6 s warm |
| Vale | `.vale.ini` lists `Packages = ai-tells, proselint, write-good, Readability` but `BasedOnStyles` also names `CoDM` (directory absent from `styles/`) and the repo-local `Deprecated` style (`styles/Deprecated/DMThesis.yml`, `FactionClock.yml`; faction/agenda clock is also checked in Python by `scripts/wiki-lint` `TMPL_deprecated_guidance` / `TMPL_inherited_deprecated_guidance`); `Vocab = CoDM` (`styles/config/vocabularies/CoDM/accept.txt`, generated from wiki titles and aliases by `tools/creative_lint/vale_vocab.py`). Open entries e-212, e-214, e-215, e-216, e-218 |
| OMP baseline | `.omp/config.yml` sets `memory:` / `backend: false`; `scripts/check-omp-baseline.sh` requires `backend: "off"` and fails with "memory not off". Open entries e-205, e-207, e-209, e-211. No test covers the checker |
| Shared agent guidance | `AGENTS.md` (588 lines) and `docs/agents/` |
| `cli-for-agents` guidance | Cursor plugin skill `cli-for-agents` (not a repository file); rules are stated inline in FR-030–FR-039 |

## User Scenarios & Testing *(mandatory)*

Stories follow the requested phase order: Phase 1 "make the current system coherent" (P1), Phase 2 "close the loop" (P2), Phase 3 "optimize" (P3).

### User Story 1 - Green Baseline Checks (Priority: P1)

As a maintainer, I want the OMP baseline checker and scoped wiki lint to pass on a correctly configured repository so that verification failures mean real defects instead of known configuration mismatches.

**Why this priority**: Nine open ledger entries (e-205, e-207, e-209, e-211 for OMP; e-212, e-214–e-216, e-218 for Vale) block every verification run and bury real failures. Nothing else can be measured until these pass.

**Independent Test**: Run the OMP baseline checker against the current `.omp/config.yml` and run scoped wiki lint on one entity page; both complete without the "memory not off" or missing-`CoDM`-style failures, and the full test suite runs.

**Acceptance Scenarios**:

1. **Given** `.omp/config.yml` with `memory:` / `backend: false`, **When** the baseline checker runs, **Then** the memory check passes.
2. **Given** a config where memory is enabled with a real backend, **When** the baseline checker runs, **Then** the memory check fails with the reason naming the configured value.
3. **Given** the simplified Vale configuration, **When** scoped wiki lint runs on any page, **Then** Vale loads without a missing-style error and applies ai-tells, write-good, proselint, Readability, and the repo-local `Deprecated` style.
4. **Given** the fixes land, **When** `scripts/error-ledger.py error list` runs, **Then** no open entry cites the OMP memory mismatch or the missing `CoDM` style.

---

### User Story 2 - One Coherent Evaluator and Corpus (Priority: P1)

As a skill author, I want `skill-creator` and `scripts/luna-eval` to run the same eval records and write the same result format so that any skill change is proven one way.

**Why this priority**: Two incompatible eval systems (e-210) and a corpus that still asserts removed Work-gate behavior make every eval result untrustworthy.

**Independent Test**: Take one existing `place-design` eval and one new skill-selection eval, run both through the `skill-creator` workflow and directly through `scripts/luna-eval`; both paths read the same record and produce results in the same format with per-assertion pass/fail.

**Acceptance Scenarios**:

1. **Given** an eval record with `assertions: [{"type": "skill_selected", "text": "place-design"}]`, **When** it runs, **Then** the result reports whether the subject selected `place-design`.
2. **Given** an eval record with a `behavior` assertion, **When** it runs through `skill-creator`, **Then** `skill-creator` invokes the same runner as a direct `scripts/luna-eval` call and the grading output is identical in shape.
3. **Given** the corpus after reconciliation, **When** it is searched for Work-gate, chat-proposal approval, read-side mutation, retired paths, or superseded completion rules, **Then** no eval asserts them as required behavior.
4. **Given** feature 026's documents, **When** executable references are checked, **Then** every cited script, test, and rule either exists or the reference is removed or updated to its current replacement.

---

### User Story 3 - Feature 029 Baseline Evidence (Priority: P1)

As a project owner, I want feature 029's open evidence tasks completed through the one evaluator so that there is a measured baseline for every later simplification claim.

**Why this priority**: Phase 3 comparisons ("7 calls → 3") are unprovable without a recorded baseline.

**Independent Test**: Run the representative cases through `scripts/luna-eval` and confirm each record carries the required metrics.

**Acceptance Scenarios**:

1. **Given** the nine case categories (owner completion, specific blocking, scope preservation, read isolation, retrieval convergence, child handoff, parent resumption, write finalization, recovery), **When** the baseline runs, **Then** each category has at least one recorded case.
2. **Given** a recorded case, **When** it is inspected, **Then** it lists task outcome, tool calls, retries, duplicate actions, tokens, completion reason, and semantic quality.

---

### User Story 4 - Scoped Lint Costs Scoped Work (Priority: P1)

As an agent linting one page, I want lint and health to take time proportional to the pages I selected so that scoped work does not wait on whole-vault identity comparison.

**Why this priority**: Scoped lint of two pages takes ~38 s and `wiki health` times out (e-208, e-213); every owner's completion guard runs lint.

**Independent Test**: Lint one page on an unchanged, warmed vault and time it; then edit one unrelated page and lint the first page again.

**Acceptance Scenarios**:

1. **Given** a warm index and one selected page, **When** scoped lint runs, **Then** expensive content comparison runs only against candidates that share an exact cheap signal (slug, alias, title, manifest identity) with the selected page or pass the cached character-profile prefilter (> 0.6).
2. **Given** a relevant file changes, **When** the next lint runs, **Then** cached identity data for that file is refreshed and findings match a cold run.
3. **Given** a whole-vault request, **When** lint runs, **Then** findings are identical to the current whole-vault output.

---

### User Story 5 - Friction Is Fixed at the Source, Then Work Resumes (Priority: P2)

As a DM, I want an agent that hits a broken command, wrong instruction, broken checker, stale test, or slow scoped operation to fix that source, verify it, and finish my original request in the same session.

**Why this priority**: This is the self-improvement system itself, and it depends on Phase 1 checks and evaluator being trustworthy.

**Independent Test**: Seed a known friction (for example a skill instruction naming a retired command path) in a disposable branch, give a cold agent an owner task that hits it, and observe the trajectory.

**Acceptance Scenarios**:

1. **Given** an owner task that meets friction, **When** the agent handles it, **Then** it identifies the cause, edits the authoritative source, runs the relevant evidence, and resumes the original task to its owner completion guard.
2. **Given** a real failure, **When** it is fixed, **Then** a regression eval or test reproducing it exists and passes after the fix.
3. **Given** a defect that cannot be fixed in the current task, **When** the agent records it, **Then** `errors.md` gets one entry with `id`, `cause`, `source`, `evidence` (a list of `{sitting, detail}` occurrences), or one occurrence is appended to an existing entry with the same `source` and cause.

---

### User Story 6 - Recurring Causes Trend to Zero (Priority: P2)

As a maintainer, I want duplicate `errors.md` entries collapsed to their root cause and drained when fixed so that the ledger shows only reusable, unresolved defects.

**Why this priority**: The current ledger holds four entries for one OMP mismatch and five for one missing Vale style.

**Independent Test**: Run the ledger's recurrence report before and after deduplication.

**Acceptance Scenarios**:

1. **Given** two failures with the same root cause, **When** the second is recorded, **Then** it attaches as evidence to the existing entry instead of creating a new id.
2. **Given** an entry whose source fix is verified, **When** the fix lands, **Then** the entry is drained.
3. **Given** the ledger, **When** the recurrence metric is requested, **Then** it reports how often an already-known root cause recurred.

---

### User Story 7 - Wiki Commands Agents Can Drive Headlessly (Priority: P2)

As an agent, I want `wiki lint`, `wiki lint fix`, `wiki query`, `wiki health`, typed mutation, `luna-eval`, and `error-ledger` to discover their environment, take obvious inputs, and return structured results with correct-invocation errors, so that I stop spending retries on invocation mistakes.

**Why this priority**: Drained entries e-186 (scope syntax), e-187 (missing `--` separator), and e-188 (option order) are invocation failures an agent-shaped CLI prevents.

**Independent Test**: Give a cold agent only `wiki --help` and a task per subcommand; count invocation errors and retries.

**Acceptance Scenarios**:

1. **Given** any subcommand, **When** `--help` is requested, **Then** it prints that subcommand's options and an Examples block of real invocations, and nothing about other subcommands.
2. **Given** a missing or malformed required input, **When** the command runs, **Then** it exits non-zero immediately with an error naming the problem and one correct example invocation.
3. **Given** `wiki lint fix` or a typed mutation run twice with the same inputs, **When** the second run completes, **Then** it makes no further change and reports "already done" (or zero changes) in its structured result.
4. **Given** any mutating command with `--dry-run`, **When** it runs, **Then** it reports the planned changes and writes nothing.

---

### User Story 8 - Incumbent vs Candidate Instruction Promotion (Priority: P3)

As a project owner, I want instruction edits proposed from execution evidence and kept only when they beat the current version on the same evals so that skills get shorter and better by measurement, not author judgment.

**Why this priority**: Depends on the baseline (US3), one evaluator (US2), and regression evals from real failures (US5).

**Independent Test**: For one owner skill, generate one small candidate edit from recorded failures, run the incumbent and candidate on the same eval set, and apply the promotion rule.

**Acceptance Scenarios**:

1. **Given** an incumbent skill file and a candidate edit, **When** both run on the same evals, **Then** the result records success, quality, tool calls, retries, tokens, latency, and scope for each.
2. **Given** the candidate is worse on success or quality, **When** the agent decides following `skill-creator`, **Then** the incumbent is kept regardless of efficiency gains.
3. **Given** equal success and quality and a simpler trajectory, **When** the comparison runs, **Then** it reports per-eval regressions and medians only, and the agent decides whether to keep the candidate in the existing source file or refuse it, following `skill-creator`.

---

### User Story 9 - Skills Stay Small; Procedure Moves into Tools (Priority: P3)

As an agent loading an owner skill, I want it to answer only when I own the task, what evidence I need, what I do, which child I may call, and how I know I am done, with repeated mechanical reasoning handled by existing commands.

**Why this priority**: Shrinks per-task context after the evaluator can prove non-regression.

**Independent Test**: For one skill, move one repeated manual procedure into an existing command, shorten the skill, and rerun that skill's evals.

**Acceptance Scenarios**:

1. **Given** a repeated manual procedure observed in recorded trajectories (repair bookkeeping, manifest facts, path discovery, health facts), **When** it is compiled, **Then** an existing command performs the deterministic part and reports facts, the skill keeps any judgment, and the skill text for the deterministic part is removed.
2. **Given** the shortened skill, **When** its evals rerun, **Then** success and quality are non-inferior to the incumbent.

### Edge Cases

- Friction's authoritative source is outside the repository (harness binary, external package): the agent records one `errors.md` entry with the external source and continues or blocks per the owner guard.
- The fix for friction is larger than the original task (e.g. identity restructuring discovered during a place edit): the agent records the defect and completes the task by the current sanctioned path; source repair is not forced inside a small task.
- A candidate instruction improves one skill's evals but regresses a cross-skill case: promotion is refused.
- Two ledger entries look similar but have different sources: they stay separate; same-root-cause requires the same `source`.
- An eval asserts behavior that is still current but uses retired wording: the wording is updated; the assertion is kept.
- A skill-selection eval where two owners are plausible: the eval names the owner defined by the skills' own ownership text; ambiguity is fixed in the skill, not in the eval.
- The Vale `Deprecated` style catches retired terms (`DM Thesis`, faction/agenda clock); it stays in Vale unchanged, so removing the `CoDM` style reference must not drop those checks.
- The OMP config is missing the `memory:` block entirely: the checker fails with a message naming the missing key.
- The identity cache is corrupted or from an older format: it is discarded and rebuilt; findings match a cold run.
- Luna usage limit is hit mid-baseline (`scripts/luna-eval` exit 3/5): partial results are kept and only missing cases rerun.

## Requirements *(mandatory)*

### Functional Requirements

**Loop, ownership, friction (request §1–3, §15)**

- **FR-001**: The existing capability loop (route → observe → act → re-observe → complete or block) MUST remain the only runtime loop; friction handling MUST be expressed as a branch of it (act → friction → fix source → re-observe → continue), with no separate self-improvement workflow, command, or skill.
- **FR-002**: Shared agent guidance MUST state the friction rule once: identify cause → find authoritative source → fix it → verify → continue the original task, preferring the smallest source change that removes the problem for future agents.
- **FR-003**: Every skill MUST keep its own ownership statement; any ownership analysis MUST be derived from the skills and MUST NOT be stored as a separate hand-maintained map. The owner set for this feature's evaluation is the six request §2 owners: `place-design`, `faction-design`, `session-beats`, `run-guide`, `wiki-query`, `wiki-lint`.
- **FR-004**: After a child capability returns, the owner MUST resume its original objective (per `specs/029-agent-loop-closure/spec.md` FR-031–FR-033).
- **FR-005**: Durable learning MUST land as a change to a skill, tool, test, eval, or shared instruction and be committed; chat acknowledgement or ledger text alone MUST NOT count as learning.

**Error surface (request §4, §6)**

- **FR-006**: `errors.md` MUST contain only reusable, unresolved defects, each with exactly the fields `id`, `cause`, `source` (authoritative file or component), and `evidence` (a list of one or more occurrences, each `{sitting, detail}`). A friction the agent fixes and verifies in the same task MUST NOT create an entry.
- **FR-007**: `error append` MUST auto-attach an occurrence only on an exact mechanical match: an open entry with the same `source` and identical `cause` text, ignoring leading and trailing whitespace. It MUST report the id of the entry it matched, and the attach MUST be reversible with one documented `scripts/error-ledger.py` invocation. Whether a differently worded cause is the same root cause is the agent's call, made with `--attach e-N` (refused when the `source` differs). The `AGENTS.md` "Error ledger" section governs that call; no skill covers it today, so the plan adds the instruction to that section rather than creating a new skill.
- **FR-008**: A verified fix MUST drain its entry in the same change that lands the fix.
- **FR-009**: `scripts/error-ledger.py` MUST report the recurrence metric: the number of occurrences after the first on open entries (i.e., occurrences whose root cause was already open), as a total and per sitting.
- **FR-010**: On first run of the new format, existing open entries MUST be migrated to the four fields (current `sitting` + `cause` text become the first occurrence; `status` and `cause_fixed` dropped) and duplicates merged (OMP: e-205, e-207, e-209, e-211; Vale `CoDM`: e-212, e-214, e-215, e-216, e-218; identity performance: e-206, e-208, e-213); already-drained entries MUST be removed.
- **FR-011**: Every fixed real failure MUST gain a regression case (an eval in the owning skill's `evals/evals.json`, or a test under `tests/` for tool defects) that fails before the fix and passes after.

**One evaluation system (request §5, §7, §8)**

- **FR-012**: `scripts/luna-eval` MUST be the single runner for skill evaluation; `skill-creator` MUST invoke it for with-skill/baseline runs and MUST NOT require `run-eval.py`'s `query`/`should_trigger` shape.
- **FR-013**: All eval records MUST use one schema: `id`, `prompt`, optional `files`/`context`/`outputs` inputs, optional `expected_output`, and `assertions[]` of `{type, text}`; the 143 `expectations[]` records MUST be converted. The `skill` is the file-level `skill_name`, required in every `evals/evals.json` (added to `session-beats`, `wiki-capture`, `wiki-context-pack`, `wiki-ingest`, `wiki-lint`, `wiki-query`, `wiki-update`); per-record `subject_skill` remains the optional override; existing optional keys (`core`, file-level `trajectory_records`, `principles`) are preserved.
- **FR-014**: The assertion vocabulary MUST be `skill_selected` (text = expected owner skill name), `behavior`, and the existing types `quality`, `guardrail`, `process`, `content`, `structure`, `scope`, `handoff`, `coverage`; the spellings `qualitative` and `structural` MUST be converted to `quality` and `structure`, and each converted `expectations[]` string becomes a `behavior` assertion.
- **FR-015**: Skill-selection and behavior evals MUST live in the same per-skill `evals/evals.json` files and run through the same runner; no separate trigger-eval corpus MAY exist.
- **FR-016**: Every run MUST write one result format containing, per eval: per-assertion pass/fail with evidence, task outcome, tool calls, retries, duplicate actions, tokens, latency, completion reason, and semantic quality. Semantic quality is the pass rate of the eval's `quality`-type assertions.
- **FR-017**: Eval records asserting superseded behavior MUST be updated to current behavior: Work-gate or chat-proposal approval before writes, obsolete approval flows, read-side mutation, retired paths, and outdated completion rules. Read-side mutation means a read capability changing canonical wiki pages, manifests, indexes, or logs (`AGENTS.md` "Capability execution contract"); derived caches are governed by FR-028.
- **FR-018**: Feature 026 documents MUST NOT cite executables absent from the repository (`scripts/check-agent-standards.py`, `tests/test_agent_standards.py`, rules `AGENT001`–`AGENT003`); each reference MUST point at the current enforcing surface or be removed with a note of what replaced it.
- **FR-019**: Feature 029 open evidence tasks (T003, T011, T018, T030, T037, T044, T046, T047, T049) MUST be completed through `scripts/luna-eval`, covering the nine categories in US3, and recorded as the baseline for FR-043–FR-045. Baseline runs use `scripts/luna-eval`'s default model and effort at the time of the run and record both in each run; later comparisons (FR-043, SC-012) use the same model and effort.

**Checker and lint fixes (request §10–12)**

- **FR-020**: `scripts/check-omp-baseline.sh` MUST treat `memory:` / `backend: false` (and the existing `"off"` form) as disabled and MUST fail when memory has an enabled backend or the key is missing.
- **FR-021**: One regression test MUST cover FR-020 with the disabled (`false`) state passing and an enabled state failing.
- **FR-022**: Vale configuration MUST base prose checks on ai-tells, write-good, proselint, and Readability plus the existing repo-local `Deprecated` style, and MUST NOT reference the `CoDM` style. `styles/Deprecated/*.yml` and `Vocab = CoDM` stay unchanged.
- **FR-023**: Repository-specific structural and semantic checks (D&D/wiki structure, ownership, identity, links, templates, canon) MUST live in the Python wiki tooling (`tools/wiki_ops/`, `scripts/wiki-lint`), not in new custom Vale styles. The existing `Deprecated` Vale style (retired terms `DM Thesis`, faction/agenda clock) and `Vocab = CoDM` stay in Vale unchanged; nothing moves from them to Python. Findings from the `Deprecated` style (for example `Deprecated.DMThesis`) MUST be labelled as judgment repairs, not `deterministic_repair`, because removing or relocating that content is the agent's call, governed by `wiki-lint`.
- **FR-024**: Scoped wiki lint and health MUST resolve identity by: cached vault index → selected pages → candidates (pages sharing a cheap exact signal — slug, title, aliases, manifest identity — or passing the cached character-profile prefilter, similarity > 0.6) → expensive content comparison only for those candidates. The similarity thresholds (prefilter > 0.6, shared-source stem ratio > 0.7) only report candidates and gate mutations as `ambiguous`; they never pick a winner. Resolving an ambiguous identity is the agent's call, governed by `wiki-dedup` and `wiki-lint`.
- **FR-025**: Reusable corpus information MUST be cached and invalidated when a relevant file is added, removed, renamed, or changed; cached and cold runs MUST produce identical findings.
- **FR-026**: Whole-vault lint findings MUST be unchanged by FR-024–FR-025.

**Commands (request §9, §13; `cli-for-agents` guidance)**

- **FR-027**: `wiki lint`, `wiki lint fix`, `wiki query`, `wiki health`, typed wiki mutation (`wiki mutate` / `wiki repair`), `scripts/luna-eval`, and `scripts/error-ledger.py` MUST discover the repository root and vault themselves from any working directory.
- **FR-028**: Each command in FR-027 MUST stay within the requested scope, perform its own safe bookkeeping (index, manifest, log, cache, ledger updates), and state its result clearly in a structured object. Lint's bookkeeping writes are `wiki/_meta/lint-cache.json`, `wiki/_meta/identity-index.json`, and the generated Vale vocabulary `styles/config/vocabularies/CoDM/accept.txt`; all three stay tracked, and they are derived caches, not read-side mutation (FR-017).
- **FR-029**: Repeated deterministic work observed in trajectories MUST move into the existing command that owns it: repair bookkeeping → `wiki lint fix`; manifest facts → `scripts/manifest.py`; repo/vault path discovery → every command; health facts → `wiki health`. `wiki health` and `scripts/manifest.py` report facts or rank targets by a fixed, documented rule. Choosing the next step stays with the agent, governed by `wiki-lint` or the owning skill. The skill text replaced by each MUST be removed.
- **FR-030**: Non-interactive first: every input to the FR-027 commands MUST be expressible as a flag or argument; no command MAY prompt, and missing inputs MUST fail rather than fall back to a prompt.
- **FR-031**: Layered discovery: bare `wiki` MUST list subcommands with one-line summaries only; each subcommand MUST own its `--help`, which MUST NOT print other subcommands' documentation.
- **FR-032**: Every subcommand `--help` MUST include an Examples block of real, copy-pasteable invocations (e.g. `wiki lint entities/place/high-eyrie.md`, `wiki lint fix dir:entities/place --dry-run`).
- **FR-033**: Where input is naturally a list or document (paths to lint, a mutation payload), the command MUST accept it on stdin via an explicit flag, and outputs MUST support chaining (e.g. an option emitting only paths or only ids).
- **FR-034**: Argument order MUST NOT matter for options, and command shape MUST be consistent `resource verb` across subcommands; `lint fix` MUST be a real subcommand, not a positional `fix` token inside the path list.
- **FR-035**: On missing or invalid input (unknown path, bad scope syntax such as a missing `kind:value`, misplaced option), the command MUST exit non-zero immediately with an error naming the problem, one correct example invocation, and where to list valid values.
- **FR-036**: `wiki lint fix`, typed mutation, repair, and `error-ledger` drain/append MUST be idempotent: re-running with identical inputs MUST cause no additional change and MUST report zero changes or "already done".
- **FR-037**: Every mutating command MUST support `--dry-run` that reports the planned change set without writing, and MUST support a confirmation bypass flag wherever any confirmation exists.
- **FR-038**: Success output MUST contain machine-useful data: changed paths, entry ids, counts before/after, durations, and the next actionable target where one exists.
- **FR-039**: A regression test per FR-030–FR-038 rule class MUST exercise the public command surface.

**Small skills and promotion (request §14, §16–19)**

- **FR-040**: Each owner skill MUST answer: when do I own this, what evidence do I need, what do I do, which child capability may I call, how do I know I am done; reference material MUST sit behind links or supporting files, deterministic procedure in tools, shared behavior in shared guidance.
- **FR-041**: One promotion rule MUST govern every source change: reproduce the problem → change the source → rerun relevant evidence → keep the change only if actual behavior improves or is non-inferior with a simpler trajectory.
- **FR-042**: Evidence MUST scale with change size: a parser or checker fix needs one focused regression; a skill rewrite needs that skill's behavioral evals; a shared agent-system change needs representative cross-skill cases from the FR-019 baseline.
- **FR-043**: Instruction improvement MUST compare an incumbent source file against one small candidate edit on the same evals through `scripts/luna-eval`, with the candidate generated from: current instruction, failed task, successful comparison tasks, tool results, assertion failures, user corrections, and token/tool-call cost. It MUST edit existing files and MUST NOT add a runtime system.
- **FR-044**: The promotion comparison MUST report, per eval, task-outcome regressions, assertions that passed for the incumbent and fail for the candidate, and the medians of tool calls, retries, tokens, latency, and scope; it MUST NOT promote or refuse. The agent decides keep or refuse following `skill-creator`, ranking success and semantic quality first; among non-inferior candidates, fewer tool calls, retries, tokens, less latency, and narrower scope win. A candidate is non-inferior when, with one run per configuration on the same evals, no eval's task outcome is worse and no assertion that passed for the incumbent fails.
- **FR-045**: New, merged, split, or retired skills MUST require repeated recorded evidence of need; improving an existing owner or tool MUST be attempted first.

**Simplify and consolidate (cross-cutting; Nick, 2026-09-24)**

- **FR-046**: Every requirement in this feature MUST be delivered under these rules. Plan, Tasks, Converge, and Review check them.
  1. **Modify the owner of the concern.** Each capability is delivered by changing or consolidating the existing module that owns it:
     - error surface: `scripts/error-ledger.py` and `errors.md`;
     - skill evaluation: `scripts/luna-eval`, with `skill-creator`'s `agents/grader.md` and `scripts/aggregate-benchmark.py`;
     - wiki command surface and repo/vault discovery: `scripts/wiki` and `tools/wiki_ops/cli.py`;
     - lint engine: `scripts/wiki-lint`, `tools/lint_wiki.py`, and `tools/creative_lint/`;
     - identity: `tools/wiki_ops/identity.py`;
     - lint caching: `tools/wiki_ops/lint_cache.py`;
     - manifest reasoning: `scripts/manifest.py`;
     - OMP baseline: `scripts/check-omp-baseline.sh`;
     - Vale: `.vale.ini`;
     - tests: the existing `tests/` files for that module.

     Before adding any new module, file, command, subcommand, config key, or data store (including derived caches and result files), the plan MUST name the existing one it extends or replaces and state why that one cannot be improved instead.
  2. **One implementation per concern.** No two modules, commands, or data formats may own the same concern. Where this feature touches a duplicate, dead, or superseded path (for example `skill-creator`'s `scripts/run-eval.py`, `run-loop.py`, and `improve-description.py`), the same change removes it and updates its references.
  3. **Reuse before adding.** New code MUST reuse the existing helpers, CLIs (`wiki`, `wiki-lint`, `luna-eval`, `error-ledger.py`, `manifest.py`), and data formats (`evals.json`, the `luna-eval` run directory, the `errors.md` JSON lines, `lint-cache.json`) rather than add parallel ones.
  4. **Root cause at the authoritative source.** A fix changes the source of the defect (for example the OMP checker's parsing, not the config value; the missing `CoDM` style reference in `.vale.ini`, not a suppression). It MUST NOT be a wrapper, special case, or workaround layered on top (constitution XXV).
  5. **Skills first; code is diagnostic, not a prosthetic for reasoning.** "No code should be making judgement calls; that's purely the agent's domain, and those judgement calls must be backed by skills." (Nick, 2026-09-24)
     - Code MAY detect, measure, check, index, and report facts (lint, indexing, schema checks, eval running, metrics, file bookkeeping). It MAY apply a fix only when the fix is fully deterministic: exactly one correct output for the given input, with no choice among alternatives.
     - Code MUST NOT decide on the agent's behalf. For example, it must not choose which duplicate page wins, rule that two errors share a root cause beyond a mechanical match, decide that a candidate instruction is better and promote it, or act on a similarity score rather than report it.
     - Every judgment an agent makes in this feature MUST name the skill that governs it (`SKILL.md` instructions, references, evals). Where this feature touches code that makes a judgment call, that call MUST move into the governing skill, and the code MUST report the facts the skill needs.
     - Where this feature touches deterministic work that agents are doing by hand, that work MUST become code in the owning module (rule 1).
     - The plan MUST justify each new or changed piece of code as diagnostic or fully deterministic work.
     - Superseded by FR-047 (Nick, 2026-09-24): there is no page promotion at all. The earlier bullet that kept `wiki-lint --consolidate` promotion as a reported, agent-decided step is withdrawn; `.agents/skills/wiki-lint/consolidate.md` §3 "Lifecycle corrections" is deleted, not converted.
  6. There is no numeric line-count limit; these rules are judged by module ownership and by the skill/code dividing line, not by size.

**Wiki canon (Nick, 2026-09-24)**

- **FR-047**: The wiki page lifecycle, promotion, and confidence machinery MUST be replaced by Nick's canon rule, in precedence order:

  > Something is canon if the DM says so > something is canon if it's present in the wiki in multiple places > something is canon if it doesn't conflict with the wiki.

  That is the entire system.
  1. **One owner, verbatim.** The rule text appears verbatim only in `.agents/skills/llm-wiki/SKILL.md` among maintained surfaces, matching constitution X (v7.0.0, f489409d) word for word. `llm-wiki/SKILL.md` already owns "confidence/lifecycle" (its description, line 5). It replaces that file's "Confidence and Lifecycle" section (lines 231–313). Other surfaces link to it and never restate it: root `AGENTS.md` line 87 ("Canon owner: constitution principle X …"), `wiki/AGENTS.md` lines 54 and 64, and `docs/agents/work.md` line 7.
  2. **Agents apply it; code only reports.** Deciding whether something is canon is agent judgment under `llm-wiki` (FR-046 rule 5). Code MUST NOT assign, store, or gate on canon. The lint engine (`tools/lint_wiki.py`, `scripts/wiki-lint`) MAY report only facts that feed the rule. These are declared conflicts (`relationships: contradicts`, existing `> ⚠️ Contradiction flagged` callouts) and single-source facts (a live page whose subject no other live page links to or names). Finding a semantic conflict stays agent work under `.agents/skills/wiki-lint/checks.md` §5 "Contradictions".
  3. **Where "the DM says so" is recorded.** The rule adds no field. A DM ruling is recorded where the repo already records it: the session log under `wiki/journal/sessions/<campaign>/<NN>/` (e.g. "Snatch (Session 12 ruling)" in `Session-12-01-River-Slack-Reprise.md`) or the recap's `## Wiki facts` section (`session-recap`). It is also recorded in the DM's chat statement that the agent files on the owner page. The owner page cites that source in its existing `sources:` list, and `retcon` still handles corrections.
  4. **Delete the machinery.**
     - Fields: `lifecycle`, `lifecycle_changed`, `lifecycle_reason`, `base_confidence`, and the ad hoc `canon_status`. These are removed from the 27 templates in `wiki/templates/*.md` and from the `required:` lists in the 15 `wiki/templates/contracts/*.yml` that name `lifecycle`. They are also removed from every page in one mechanical, deterministic migration: 833 live pages plus 15 archived/meta pages. `reveal`, `visibility`, `truth`, `invention`, and entity `status` stay; they are not canon-promotion fields.
     - Skill text: `llm-wiki/SKILL.md` "Confidence and Lifecycle" (lines 231–313) and the `OBSIDIAN_ALLOWED_LIFECYCLES` / `OBSIDIAN_REQUIRED_TRUST_FIELDS` keys; `wiki-lint/checks.md` §12 (lines 75–98); `wiki-lint/consolidate.md` §3 (lines 44–48), the `lifecycle` line in step 3 (line 13), the `lifecycle: draft` report frontmatter (lines 75–76), and `lifecycle_updates` in the log line (line 92); the frontmatter/formula blocks in `wiki-ingest/SKILL.md` (lines 503–517) and `wiki-ingest/references/url-sources.md` (lines 148–196); the same blocks in `wiki-update`, `wiki-capture` (and `references/raw-format.md`), `wiki-research`, `wiki-synthesize`, `wiki-dedup`, `wiki-import`, `wiki-digest`, `obsidian-markdown`, `vault-skill-factory`, the seven `*-history-ingest` skills, `lore-design` lines 93 and 105, and the `lifecycle` mentions in the design skills; `templates/work.md` "`lifecycle` stays `proposed` until that decision".
     - Code: `tools/lint_wiki.py` `OWNER_LIFECYCLES`/`DEFAULT_LIFECYCLES` (lines 24–25), `lifecycle` in `CAMPAIGN_REQUIRED` (line 30), lifecycle parsing from `wiki/AGENTS.md` (lines 198–208), `--required-trust-field` and `missing_trust` (lines 320–322, 649–658), and `bad_lifecycle` (lines 615–618); `tools/wiki_ops/worklist.py` `bad_lifecycle` (line 14); `tools/creative_lint/evaluators/symbolic.py` lifecycle checks (lines 89, 117) and `CANON001` (lines 156–161) with its `rules/registry.yml` entry, plus the lifecycle half of the rule at lines 47–49; `tools/creative_lint/engine.py` lifecycle exemptions (lines 145–150; no rule declares one); `tools/wiki_ops/identity.py` `lifecycle` (lines 108, 139, 202); `tools/check_wiki_pages.py` lifecycle check (lines 25, 61–66); `scripts/wiki-reveal` line 54; and the `lifecycle`/`base_confidence` defaults in `scripts/wiki-bulk-ops` (lines 971–974) and `scripts/ingest-raw.py` (line 74).
     - Tests and evals that exist only for the machinery are deleted: fixtures `tests/fixtures/creative_lint/symbolic/invalid_lifecycle.md` and `tests/fixtures/creative_lint/WIKI002/ambiguous_proposed_state.md`, and the lifecycle/`base_confidence` assertions in `tests/test_wiki_ops.py`, `test_creative_lint.py`, `test_creative_lint_cli.py`, `test_wiki_bulk_ops.py`, `test_wiki_cli.py`, and `test_error_ledger_repairs.py`. Other assertions are kept and made independent of the removed fields.
  5. **Rewrite or drop every reader.**
     - Foundry gates: `foundry-token/SKILL.md` line 16 and `foundry-battlemap/SKILL.md` line 12 require `lifecycle: accepted`, and today only 7 pages pass. They are rewritten to require that the source page is canon under the rule (agent judgment citing `llm-wiki`). Their evals `foundry-token/evals/evals.json` (lines 28–31) and `foundry-battlemap/evals/evals.json` (lines 18–21) are rewritten to match.
     - Faction contract: `wiki/templates/contracts/faction.yml` `when:` blocks (lines 21–22, 64–65, 74–75) drop the `accepted`/`proposed` keys and key on entity `status` alone. `tools/wiki_ops/template_contracts.py` line 160 reads `status`, not `lifecycle`. This also fixes the dead `active`/`dormant`/`dissolved` keys that never fire while `lifecycle` is present. The fixture `tests/fixtures/wiki_ops/templates/dormant-faction.md` follows.
     - `wiki-query/SKILL.md` trust annotations (lines 244–261) are dropped. When a cited fact has a reported conflict, the answer names it (rule 3).
     - `wiki-digest` "Drafts" (lines 47, 81, 143) is dropped.
     - Evals that assert lifecycle fields are updated: `wiki-import` line 10, `wiki-ingest` line 85, `vehicle-design` lines 22 and 88, `city-design` line 76, `spell-design` lines 22 and 84, `narrative-islands` line 136, and `wiki-dashboard`.

### Key Entities

- **Owner skill**: The direct owner of a task kind; holds its own ownership statement, completion guard, allowed children, and evals.
- **Eval record**: One case in a skill's `evals/evals.json`: id, prompt, inputs, expected output, typed assertions; its skill is the file-level `skill_name` unless `subject_skill` overrides it.
- **Assertion**: `{type, text}`; `type` is one of the FR-014 vocabulary.
- **Eval result**: One run's per-assertion grades plus trajectory metrics (outcome, tool calls, retries, duplicate actions, tokens, latency, completion reason, semantic quality).
- **Error entry**: `errors.md` line with `id`, `cause`, `source`, `evidence[]` of `{sitting, detail}` occurrences; open by definition; drained (removed) when its fix is verified.
- **Incumbent / candidate**: The current source file and one proposed edit, compared on the same eval set.
- **Friction**: Any cause that makes a task unnecessarily difficult: bad CLI, bad instruction, broken checker, repeated manual procedure, stale test, slow scoped operation.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: The OMP baseline checker passes on the current configuration, and its regression test passes for the disabled state and fails for an enabled state.
- **SC-002**: Zero scoped lint runs fail on a missing Vale style across all page kinds in `wiki/`; the full test suite runs to completion.
- **SC-003**: 100% of eval records (533 at spec time, plus every record added by this feature) use one schema, and 0 records assert Work-gate, chat-proposal approval, read-side mutation, or retired-path behavior.
- **SC-004**: One eval record produces identical-shape results whether run from `skill-creator` or directly from `scripts/luna-eval`; `skill-creator` has no second runner in use.
- **SC-005**: Each of the six FR-003 owners (6/6) has at least one passing `skill_selected` eval; further `skill_selected` evals are added from real misroutes (FR-011).
- **SC-006**: Feature 029's nine open evidence tasks are complete, with at least ten baseline cases covering all nine categories, each carrying all FR-016 metrics.
- **SC-007**: Scoped lint of one changed page (lint-cache miss, Vale included) finishes in under 5 s on the maintainer workstation, against a measured 3.72 s with Vale on 2026-09-24 (bf021f03, 8-core Linux box). The lint result reports how many pages the identity step compared, and that count equals the selected pages plus their candidates (cheap exact signal or cached-prefilter pass), not the vault page count. A rerun on the unchanged page is served from the lint cache (measured 0.28 s). `wiki health` finishes in under 50 s whenever the identity index is current, including after a lint-rules change that invalidates the whole lint cache, and in under 10 s when only a few pages changed (measured 82.0 s cold and 2.6 s warm on 2026-09-24); a from-scratch rebuild (no index) records its wall time next to the SC-006 baseline.
- **SC-008**: Feature 026 documents contain 0 references to absent scripts, tests, or rules.
- **SC-009**: After migration, `errors.md` holds no two open entries with the same root cause, and the recurrence metric for already-known causes reaches 0 over the 20 sittings following Phase 2.
- **SC-010**: A cold agent given only `wiki --help` completes one task per FR-027 wiki subcommand with 0 invocation errors; re-running each mutating command produces 0 additional changes. A cold agent is a `scripts/luna-eval` subject with default model and effort and no context beyond `wiki --help` and the task prompt (constitution IV). An invocation error is a call to an FR-027 command rejected as a usage error (the FR-035 error object, or an argparse usage error, with non-zero exit), counted even when the agent corrects it; each run's `metrics.json` `invocation_errors` must be 0.
- **SC-011**: In seeded-friction trials, at least 4 of 5 cold agents fix the source, add a regression, and complete the original task in the same session.
- **SC-012**: At least one owner skill is promoted by an agent following `skill-creator`, using an incumbent-vs-candidate comparison report that shows non-inferior success and quality (FR-044) and a lower median of tool calls, retries, or tokens, with none of the three higher, against the incumbent on the same evals.
- **SC-013**: Owner skills touched by this feature are no longer than before, and each answers the five FR-040 questions.
- **SC-014**: At Converge and at Review, the feature diff passes six checks. (a) Every new file, module, command, subcommand, config key, or data store maps to a named existing module that it replaces, extends, or consolidates, with the reason recorded in plan.md. (b) No two modules own the same concern. (c) Every duplicate, dead, or superseded path that plan.md identifies is deleted and no longer referenced. (d) Every new or changed piece of code is diagnostic (it detects, measures, checks, indexes, or reports) or applies only fully deterministic fixes, and plan.md justifies it as such; no code decides on the agent's behalf. (e) Every agent judgment this feature introduces or relies on (duplicate choice, same-root-cause beyond a mechanical match, promotion, repair choice) names the skill that governs it. (f) Superseded by SC-015: there is no promotion to check. No numeric line limit applies.
- **SC-015**: At Converge and at Review, (a) maintained surfaces contain no page lifecycle, promotion, or confidence fields or rules. The maintained surfaces are `wiki/` outside `_raw/`, `wiki/templates/`, `.agents/skills/`, `AGENTS.md`, `wiki/AGENTS.md`, `docs/agents/`, `tools/`, `scripts/`, `rules/`, `tests/`, and skill `evals/`. A search for `lifecycle:`, `lifecycle_changed`, `lifecycle_reason`, `base_confidence`, and `canon_status` in page or template frontmatter, and for their rules in skills and code, returns 0 hits; ACTIVE/SHADOW rule status in `creative_lint` is unrelated and exempt. (b) The FR-047 rule text appears verbatim in exactly one maintained file, `.agents/skills/llm-wiki/SKILL.md`, and the AGENTS.md files point to it. (c) Every canon-related lint finding is either a reported conflict or a single-source fact, and no code path assigns or gates on canon.

## Assumptions

- The phased order is binding: Phase 1 (US1–US4: OMP baseline, Vale, 026 references, stale evals, shared evaluator, 029 evidence, scoped identity), Phase 2 (US5–US7: friction rule, failures as regressions, ledger dedup, repair during normal work, command fixes), Phase 3 (US8–US9: incumbent vs candidate, execution-feedback edits, metric tracking, skill simplification).
- `skill_selected` is graded from the subject's process record (`process.md` / `events.jsonl`): the owner whose `SKILL.md` the subject loads to perform the task.
- The unified result format extends `scripts/luna-eval`'s existing run layout; `skill-creator`'s viewer and benchmark scripts read it rather than a second format.
- The `errors.md` migration keeps existing ids for continuity.
- "Scoped" means the paths or `kind:value` scopes passed to `wiki lint`/`wiki health`; whole-vault behavior is the no-argument case.
- The SC-007 5 s budget sits above the 2026-09-24 measurement of 3.72 s (one page, cache miss, Vale 3.21.0, bf021f03, 8-core Linux box). Plan re-measures on the maintainer workstation against the current vault (about 1,640 non-raw pages).
- The 20-sitting window in SC-009 is an assumed measurement window; the request only says the recurrence metric should trend to zero.
- Behavioral evaluation uses the weakest sufficient model and composes real wiki content (constitution XXIII, XXVI).
- Feature 027's result contract (`specs/027-wiki-agent-cli/spec.md`: agent-shaped default output, `--pretty` for humans, no fuzzy paths) stays in force; FR-030–FR-039 extend it.
- **Dependency (met)**: constitution principle XIII was redefined to match FR-006–FR-008 and US5–US6 in v6.0.0 (590af34e), with VI and XIX aligned in the same amendment; v6.0.1 (bf021f03) keeps it. No constitution work remains for this feature.
