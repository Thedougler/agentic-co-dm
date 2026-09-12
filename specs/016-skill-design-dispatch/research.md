# Research: Skill Design Dispatch

## Decision: `AGENTS.md` holds the design-impact gate

**Rationale**: FR-008 — routing must fire in sessions that never load a skill-authoring playbook. `skill-creator` and `omp-harness` are on-demand. `AGENTS.md` is always-loaded across omp (`.omp/AGENTS.md` imports it) and Claude Code (`.claude/CLAUDE.md` imports it). The four bullets plus who-writes is load-bearing (Constitution IX, same pattern as the writing-authority table).

**Alternatives considered**: Gate only in `skill-creator` (leaks when the agent “just edits”). New router skill (Constitution VII; extra trigger surface). Duplicate the gate in `.omp/AGENTS.md` / `.claude/CLAUDE.md` (they already import). Put the full procedure in `AGENTS.md` (token spike; procedure is not needed on every turn).

## Decision: Procedure lives in `docs/agents/skill-design-dispatch.md`

**Rationale**: `docs/` already owns harness dispatch. Progressive disclosure: standing gate classifies; the procedure is reached only when the class is design-impact (or when resuming parked work). Steps: write scoped prompt; invoke designated writer; on non-usage-limit failure restore targets and park; on usage limit restore and wait; on success verify and do not rewrite.

**Alternatives considered**: New skill (always-loaded description cost; competes with `skill-creator`). Fold into `writing-for-agents` (that document owns craft, not who writes). Fold into `harness-dispatch.md` (that document owns Spec Kit harness handoff, not instruction-file authorship).

## Decision: Designated writer is Claude Code CLI, opus, high effort

**Rationale**: Owner named this specialist and its scarcity. `claude --help`: `-p/--print` for non-interactive; `--model opus` (alias, not a pinned version string); `--effort high`. Environment is truth — do not cache a model version in standing docs. Session agent must not substitute itself when the CLI is missing, unauthenticated, usage-limited, or exits non-zero (FR-010).

**Alternatives considered**: omp `task` subagent with a stronger model (quota and expertise the owner reserved live on Claude Code). Interactive `claude` (blocks; Constitution X). New wrapper script around `claude` (restates the CLI; Constitution VI). Pin `opus-4.6` in docs (stale cache).

## Decision: Parked dispatch is a GitHub issue, existing triage label, title prefix

**Rationale**: Constitution II — tracked work is GitHub issues via `gh`. Label `ready-for-agent` so a later session may implement. Title prefix `Parked skill design:` so resume is findable without a sixth triage label. Body is the scoped prompt (outcome, files, bounds). Duplicate park of the same job is FR-016 — search before create.

**Alternatives considered**: Chat-only (dies with the session; fails SC-007). Queue markdown in the repo (second tracker). New triage label (Constitution II names five strings). `ready-for-human` (this is agent work once the writer is available).

## Decision: Usage limits wait; they are not parked dispatch

**Rationale**: FR-017 / SC-008. Owner: do not file a GitHub issue on usage limits. The specific job stays incomplete with a retry time; other in-session work is not marked incomplete for that reason. Retry time is the reset time in the usage-limit report when present; if none, 5 hours from the stop; if a retry still reports a usage limit with no reset time, 24 hours from that attempt. Report the retry time; do not create parked dispatch. A later session after that time retries. Do not put the backoff in `AGENTS.md` (procedure only).

**Alternatives considered**: Park as a GitHub issue (pollutes the tracker on every quota miss; owner rejected). Single 24-hour default always (ignores a reported reset). Owner-picked retry time (human gate; Constitution X). No retry time (immediately re-attempted, burning quota again).

## Decision: On writer failure, restore targets to the revision at dispatch start

**Rationale**: FR-009 — incomplete means files match pre-attempt content, including a writer that died mid-edit. Session agent commits non-design work first (Constitution X), records `HEAD`, invokes the writer, and on non-success restores the prompt’s target paths from that revision. Session agent does not finish the design (FR-010).

**Alternatives considered**: Leave partial writes (half-written skills). Session-agent fallback (guts the policy on the expected quota miss). `git reset --hard` of the whole branch without recording `HEAD` (destroys unrelated work).

## Decision: `skill-creator` and `omp-harness` lose the “you draft it” path for design-impact

**Rationale**: Those skills currently instruct the session agent to write skills and omp context files. That instruction fights the gate. Replace it with a pointer to the procedure when the class is design-impact. Do not copy the four bullets into those skills (Constitution IX).

**Alternatives considered**: Leave them unchanged (session agent follows the skill and writes anyway). Copy the full gate into each (duplication).

## Decision: Quickstart is the behavioral test; no live writer required for classification

**Rationale**: Constitution IV — observe classification and outcome (session-agent / dispatched / parked / usage-limited / out-of-scope), not whether `AGENTS.md` contains a string. Live `claude` is optional for a dispatch smoke; classification must pass without it (SC-001).

**Alternatives considered**: pytest over AGENTS.md text (implementation-coupled). Require a billed Claude Code run in every quickstart (scarcity the feature exists to protect).
