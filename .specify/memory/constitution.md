<!--
Sync Impact Report
- Version change: 1.12.0 → 1.13.0
- Modified principles: none
- Added sections:
  - XIII. Wiki Media Filenames Distinguish Kind
- Removed sections: none
- Other modified sections:
  - Agent Operating Constraints (wiki media filenames follow XIII)
  - Development Workflow / Review (same)
  - Governance / Compliance (reject kind-silent media filenames)
- Follow-up TODOs: none
-->

# Agentic Co-DM Constitution

## Core Principles

### I. Domain Language Is Binding

Issue titles, specs, tests, and code names MUST use terms as defined in
`CONTEXT.md`. Terms listed under `_Avoid_` MUST NOT be used as synonyms.
A missing glossary term is a domain-modeling gap: MUST NOT invent language
in those artifacts. Work that contradicts an existing ADR MUST name the
conflict and MUST NOT silently override the decision.

Rationale: one vocabulary across agents and humans is what keeps specs and
code from drifting.

### II. Issues Are the Work Surface

All tracked work MUST live as GitHub issues, operated through `gh`.
Triage labels MUST use these exact strings: `needs-triage`, `needs-info`,
`ready-for-agent`, `ready-for-human`, `wontfix`. External pull requests
MUST NOT be treated as a feature-request surface. An agent MAY implement
only issues labelled `ready-for-agent`.

Rationale: labels and `gh` are the contract between humans, AFK agents,
and triage skills.

### III. Spec Before Code

A feature MUST have a Spec Kit specification with independently testable
acceptance scenarios before implementation starts. The Full SDD Cycle is
specify → plan → tasks → implement; spec and plan review gates MUST be
honored when that workflow is used. `ready-for-agent` means the spec is
complete enough to implement without further human clarification.
Acceptance scenarios MUST name outcomes. They MUST NOT prescribe a
creative method, voice, or implementation when more than one approach
meets those outcomes (see VII).

Rationale: underspecified work produces agent drift; overspecified work
suffocates the creative product.

### IV. Tests Specify Behavior

Permanent tests MUST assert observable behavior at public seams, never
internals. New behavior MUST be expressed as a failing test before the
code that passes it (red → green, one slice). Tests MUST NOT couple to
implementation, recompute their own expected values, or be written as a
bulk suite of imagined behavior. Test names MUST use `CONTEXT.md` terms
when those terms exist.

Rationale: tests that survive refactors are the only tests worth keeping.

### V. Single Context, Documented Decisions

This repository is single-context. Domain language lives in root
`CONTEXT.md`; decisions live in `docs/adr/`. A second bounded context
MUST NOT be added without a root `CONTEXT-MAP.md`. ADRs MUST record
resolved decisions, not speculative architecture. Missing `CONTEXT.md`
or ADRs is not a defect; they MUST be created when a term or decision
is actually resolved, not up front.

Rationale: one context until the map proves otherwise keeps the glossary
and ADRs findable.

### VI. Software Is Agent-Shaped

This is an agentic project in early development. Ship. Every script, tool,
util, and other software in this repository MUST be agent-shaped and
usable by an agent as the primary operator:

- An agent MUST be able to invoke it without a GUI: arguments in, text or
  JSON out, errors on stderr, an exit code that distinguishes done from
  failed.
- Agent-facing documents (skills, `AGENTS.md`, context pointers, CLIs
  agents follow) MUST follow `.agents/skills/writing-for-agents`:
  completion criteria on every step, leading words, progressive
  disclosure, one source of truth, the environment as truth (not a stale
  doc cache), positive instruction, prune no-ops and sediment.
- Regardless of the agent utilized for a skill change, that agent MUST
  receive an instruction, in addition to all original Spec Kit requirements
  and the task-specific prompt, to use `.agents/skills/writing-for-agents`
  for that work.
- MUST NOT add a human-only wrapper when an agent can run the same command.
- MUST ship the agent-shaped tool first. Human chrome waits until a human
  must operate it.

Rationale: a tool the agent cannot run does not exist. Early speed is
small, invocable tools, not delayed product surface.

### VII. Do Not Suffocate Agents

Overspecificity is a defect in creative work and in the agentic design of
creative software and infrastructure. Specs, skills, templates, checklists,
and reviews MUST constrain only independently testable acceptance, safety,
domain language, and named failure modes. They MUST NOT prescribe a single
creative method, voice, structure, or implementation when more than one
valid approach meets those constraints. A required step, gate, or checklist
item that does not prevent a named failure MUST NOT be added. Agents
working in this repository MUST retain judgment on creative Work.

Rationale: this product exists to produce playable creative Work. Process
that smothers judgment produces worse Work, not safer Work.

### VIII. Safe Automation Runs Unattended

Easy, safe, idempotent automation MUST run without an agent choosing to
invoke it or sequencing it in a skill. Formatters, index refresh,
hook-driven repository init, and equivalent post-write maintenance MUST be
automatic, idempotent, and safe to re-run. Agents MUST assume those steps
already ran and MUST NOT spend tokens considering them. Automation that is
not easy, not safe, or not idempotent MUST stay explicit. It MUST NOT be
hidden in a hook.

Rationale: chores that need no judgment are not agent work.

### IX. Design Trends Toward Token Efficiency

Agent-consumed surfaces (skills, `AGENTS.md`, constitutions, CLIs, errors)
MUST trend toward fewer tokens for the same outcome. Standing context MUST
be load-bearing. Skills MUST use progressive disclosure; the environment
is truth. A change that increases tokens an agent must read or emit to
complete the same task MUST be justified by a named failure it prevents.
Duplicating guidance that already lives in one source of truth is a defect.

Rationale: extra tokens are latency, cost, and noise that drown the signal.

### X. Agents Act Autonomously By Default

Agents MUST complete the git and context loop without waiting to be asked.
Waiting for a human to say "commit", "push", "make a branch", or "update
from main" is a defect unless a named safety failure applies.

Git by default:

- Agents MUST commit completed work on the current task as they go.
- Agents MUST push the working branch to `origin` after those commits.
- Agents MUST use a feature branch for work that does not already have
  one. They MUST NOT commit feature work directly to `main`.
- Agents MUST fetch and update the working branch from `origin/main`
  before starting substantial work and before reporting done.
- When the assigned work is complete and required checks pass, agents MUST
  land it on `main` by the repository's normal path (merge or PR) and MUST
  leave `origin/main` current. They MUST NOT wait for a human to merge a
  ready branch.
- Agents MUST NOT force-push `main` or rewrite published default-branch
  history. They MUST NOT commit secrets, credentials, or unrelated dirty
  files. They MUST NOT skip required checks to land on `main`.

Agent context by default:

- Spec Kit agent-context MUST be used. Live feature context MUST live in
  the configured agent context file, not in chat paste.
- After specify, plan, or equivalent artifact changes, agents MUST refresh
  that context file rather than telling the next session to "remember"
  the plan.

Agentic development defaults otherwise follow this constitution and
established agentic practice: spec before code, small slices, evidence
before done, one writer per canonical artifact, no duplicate sources of
truth. A skill or sticky rule that requires a human prompt for commit,
push, branch, or agent-context refresh is informal practice and loses
(see Governance).

Rationale: an agent that stops for git ceremony is not autonomous. The
repository and its context files are the memory; the default branch must
not lag completed work.

### XI. Designated Writer Work Has Bounded Concurrency

Agents MAY run up to two concurrent Claude Code designated-writer
instances. An agent MAY use a second Claude Code instance only when the
agents involved have no other task to complete. Agents MUST NOT run more
than one concurrent Codex designated-writer instance, and Codex MUST NOT
overlap with Claude Code designated-writer instances. Multiple tasks that
modify the same canonical artifact MUST remain single-writer and MUST NOT
overlap. Independent non-writer work MAY continue concurrently unless
another governance rule forbids it. Deferred designated-writer tasks MUST
remain incomplete on the feature `tasks.md` with a retry time. Completing
other or new work during a usage-limit wait MUST NOT drop, close, or omit
those tasks; they MUST be carried over and retried only after the recorded
time, except where the Codex fallback or session-agent usage-limit
fallback below applies. When both Claude Code and Codex are unavailable
due to usage limits, the session agent MAY write the deferred
design-impact change. The session agent MUST NOT write design-impact work
while either designated writer is usable.

Rationale: bounded Claude Code concurrency uses available capacity without
allowing competing edits to the same artifact. Codex remains serialized
and isolated from Claude Code. Carry-over keeps deferred work findable on
the Spec Kit task list when other work lands. Session-agent write is last
resort when both designated writers are usage-limited.

### XII. Prompt Other Agents With Objectives

When a session agent prompts another coding agent (Claude Code, Codex, or
equivalent), that prompt MUST trust the target to operate itself and its
environment. It MUST state the objective. It MUST completely communicate
independently testable acceptance criteria and deliverables. It MUST use
the most token-efficient, cost-effective wording that still does those
three things.

The prompt MUST NOT include tool tutorials, harness walkthroughs, or
environment operating manuals the target already has. MUST NOT pad with
restated standing procedure, git ceremony, or skill internals the target
already loads. Extra tokens are a defect unless they prevent a named
failure or carry missing acceptance or deliverable facts. Required
instructions from this constitution (including VI's writing-for-agents
instruction) remain in the prompt; they are named-failure prevention,
not padding.

Rationale: the other agent already knows its tools and environment.
Tokens spent teaching that are cost without signal. Incomplete
acceptance criteria is the actual failure.

### XIII. Wiki Media Filenames Distinguish Kind

Wiki media assets MUST encode their kind in the filename so an agent can
classify the file from the name alone, without opening it or guessing from
nearby notes. Distinct kinds include at least battlemap, portrait, token,
and scene. New media kinds MUST also encode kind in the filename. Two
assets of different kinds MUST NOT be distinguishable only by directory,
extension, or surrounding prose. A filename that is silent on kind is a
defect.

MUST NOT treat folder placement as the only kind signal. Agents MUST NOT
guess kind from pixels or adjacent wiki text when the filename does not
name it.

Rationale: opening every image to learn whether it is a token or a
battlemap wastes tokens and produces wrong attachments.

## Agent Operating Constraints

- Runtime guidance for agents is `AGENTS.md`. Skills MUST follow
  `docs/agents/issue-tracker.md`, `docs/agents/triage-labels.md`, and
  `docs/agents/domain.md`.
- Skills, `AGENTS.md`, and other agent-consumed docs MUST follow
  `.agents/skills/writing-for-agents` and MUST stay as short as the
  named failure they prevent.
- If `CONTEXT.md` or `docs/adr/` is absent, agents MUST proceed without
  flagging the absence or proposing those files as a prerequisite.
- Wayfinder maps (issue labelled `wayfinder:map`) and child tickets are
  the exploration surface when that workflow is in use. Blocking MUST use
  GitHub issue dependencies when available.
- PRs-as-request-surface is **no**. PRs remain a landing path for X.
- Agents MUST NOT re-run or document easy, safe, idempotent automation
  that already runs unattended.
- Agents MUST auto-commit, auto-push the working branch, keep it current
  with `main`, and refresh agent-context, per X. They MUST NOT ask
  permission for those steps.
- Prompts to Claude Code, Codex, or equivalent MUST follow XII: objective,
  complete acceptance and deliverables, no operating-manual padding.
- Wiki media assets MUST follow XIII: kind in the filename, no guessing.
- Designated writer, when used: Claude Code at `claude-opus-4-6`
  `--effort medium`. MUST NOT use the `opus` alias or default Opus.
  Default Opus output is worthless for language work (issue #3). Up to
  two Claude Code instances MAY run concurrently only when the agents
  involved have no other task to complete; they MUST NOT modify the same
  canonical artifact concurrently. Use that writer only for novel skill
  design, skill redesign, or a major skill-file change (issue #4). Session
  agents complete smaller edits to established files, Spec Kit pattern
  tweaks, and `AGENTS.md`. A Claude Code usage limit defers only that
  Claude-dependent task on the feature `tasks.md` with a retry time;
  remaining independent work continues. Completing other or new work while
  waiting MUST carry those deferred tasks forward still incomplete; they
  MUST NOT be dropped, closed, or omitted. If every remaining open task is
  blocked by that usage limit, no other work can be done, and the retry time
  on the blocked task is more than one hour away, the session agent MAY
  invoke the Codex CLI at ChatGPT 5.5 medium with the same tightly scoped
  skill-writing prompt. Codex MUST NOT run concurrently with Claude Code.
  If that Codex invocation is itself unavailable due to a usage limit, and
  Claude Code remains unavailable due to a usage limit, the session agent
  MAY write the design-impact change itself. Otherwise the session agent
  MUST NOT write the design-impact change itself. Before each remaining
  blocked skill job, the session agent MUST re-check those gates and MUST
  prefer Claude Code if it is usable again, then Codex if Claude Code is
  still usage-limited. Retry after the recorded time unless that Codex
  fallback or session-agent fallback applied.

## Development Workflow

1. Triage: an issue is not implementable until it carries `ready-for-agent`
   or `ready-for-human`.
2. Specify: write the spec (`/speckit.specify`) with prioritized,
   independently testable user stories. Stop at acceptance. Do not encode
   a creative method. Refresh agent-context. Commit and push.
3. Plan and tasks: `/speckit.plan` then `/speckit.tasks` after spec approval.
   Plans MUST NOT add steps an unattended hook already performs. Refresh
   agent-context. Commit and push. Keep the branch current with `main`.
4. Implement: TDD at agreed seams; one red → green slice at a time.
   Refactoring belongs to review, not the implementation loop. Prefer a
   small agent-shaped tool over waiting for a human-facing one. Commit per
   slice, push, and land on `main` when the slice is done and checks pass.
5. Review: code review MUST check constitution compliance, ADR conflicts,
   that tests observe behavior rather than internals, that new software is
   agent-shaped, that process is not overspecific, that easy safe idempotent
   automation is unattended, that standing agent context did not grow
   without a named failure, that prompts to other agents carry objectives
   and complete acceptance rather than operating manuals, that wiki media
   filenames distinguish kind without guessing, and that git/context
   autonomy was not reintroduced as a human gate.

## Governance

This constitution supersedes informal practice, skill defaults, and
unwritten habit. Where a skill conflicts with this document, this
document wins.

Amendments:

- Propose the change in a GitHub issue.
- Update `.specify/memory/constitution.md` in the same change that adopts
  the amendment.
- Bump **Version** using:
  - MAJOR: remove or redefine a principle incompatibly.
  - MINOR: add or materially expand a principle or section.
  - PATCH: clarification, wording, or typo with no semantic change.
- Set **Last Amended** to the amendment date (ISO `YYYY-MM-DD`).
- **Ratified** does not change after first adoption.

Compliance:

- Reviews and `/speckit.analyze` MUST check proposed work against these
  principles before merge or implementation.
- Reviews MUST verify that every skill-change assignment preserves all
  original Spec Kit requirements and includes the writing-for-agents
  instruction, regardless of the agent utilized.
- Unjustified complexity (new context, new abstraction, new tracker
  surface) MUST be rejected or recorded as an ADR.
- A new script, tool, or util that is not agent-shaped MUST be rejected.
- A required creative procedure, extra standing context, or agent-facing
  chore that does not prevent a named failure MUST be rejected.
- Easy, safe, idempotent work left as a manual agent step MUST be
  rejected in favor of unattended automation.
- A required human prompt to commit, push, branch, update from `main`,
  or refresh agent-context MUST be rejected unless it prevents a named
  safety failure (secrets, force-push of `main`, skipping checks).
- A prompt to another coding agent that includes an operating manual,
  omits acceptance criteria or deliverables, or is longer than needed to
  state those facts MUST be rejected.
- A wiki media filename that does not encode kind, or that requires
  opening the file or guessing from nearby notes to classify it, MUST be
  rejected.
- Reviews MUST verify that no more than two Claude Code designated-writer
  instances run concurrently, that a second is used only when the agents
  involved have no other task to complete, and that no canonical artifact
  is modified by concurrent writers. Reviews MUST verify that Codex remains
  single-instance and does not overlap with Claude Code. Usage-limited tasks
  MUST remain on the feature `tasks.md` with a retry time when other work
  completed during the wait, and Codex fallback may run only when every
  remaining open task was blocked, no other work could be done, and the
  retry time was more than one hour away. Session-agent write of a
  design-impact change is allowed only when both Claude Code and Codex
  were unavailable due to usage limits under those same gates.

Runtime development guidance: `AGENTS.md`.

**Version**: 1.13.0 | **Ratified**: 2026-09-11 | **Last Amended**: 2026-09-12
