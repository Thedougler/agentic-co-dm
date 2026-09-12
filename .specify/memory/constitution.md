<!--
Sync Impact Report
- Version change: 1.0.0 → 1.1.0
- Modified principles: none renamed
- Added sections:
  - VI. Tools Are Agent-Shaped
- Removed sections: none
- Follow-up TODOs: none. Prior TODO (product-domain principles after
  CONTEXT.md) is closed: CONTEXT.md exists; I. already binds it. Do not
  duplicate glossary into this file.
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

Rationale: underspecified work produces agent drift and unreviewable diffs.

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

### VI. Tools Are Agent-Shaped

This is an agentic project in early development. Ship. Every script, tool,
and util MUST be agent-shaped:

- An agent MUST be able to invoke it without a GUI: arguments in, text or
  JSON out, errors on stderr, an exit code that distinguishes done from
  failed.
- Agent-facing documents (skills, `AGENTS.md`, context pointers, CLIs
  agents follow) MUST follow `.agents/skills/writing-for-agents`:
  completion criteria on every step, leading words, progressive
  disclosure, one source of truth, the environment as truth (not a stale
  doc cache), positive instruction, prune no-ops and sediment.
- MUST NOT add a human-only wrapper when an agent can run the same command.
- MUST ship the agent-shaped tool first. Human chrome waits until a human
  must operate it.

Rationale: a tool the agent cannot run does not exist. Early speed is
small, invocable tools, not delayed product surface.

## Agent Operating Constraints

- Runtime guidance for agents is `AGENTS.md`. Skills MUST follow
  `docs/agents/issue-tracker.md`, `docs/agents/triage-labels.md`, and
  `docs/agents/domain.md`.
- Skills, `AGENTS.md`, and other agent-consumed docs MUST follow
  `.agents/skills/writing-for-agents`.
- If `CONTEXT.md` or `docs/adr/` is absent, agents MUST proceed without
  flagging the absence or proposing those files as a prerequisite.
- Wayfinder maps (issue labelled `wayfinder:map`) and child tickets are
  the exploration surface when that workflow is in use. Blocking MUST use
  GitHub issue dependencies when available.
- PRs-as-request-surface is **no**.

## Development Workflow

1. Triage: an issue is not implementable until it carries `ready-for-agent`
   or `ready-for-human`.
2. Specify: write the spec (`/speckit.specify`) with prioritized,
   independently testable user stories.
3. Plan and tasks: `/speckit.plan` then `/speckit.tasks` after spec approval.
4. Implement: TDD at agreed seams; one red → green slice at a time.
   Refactoring belongs to review, not the implementation loop. Prefer a
   small agent-shaped tool over waiting for a human-facing one.
5. Review: code review MUST check constitution compliance, ADR conflicts,
   that tests observe behavior rather than internals, and that new
   scripts/tools/utils are agent-shaped.

## Governance

This constitution supersedes informal practice, skill defaults, and
unwritten habit. Where a skill conflicts with this document, this
document wins.

Amendments:

- Propose the change in a GitHub issue.
- Update `.specify/memory/constitution.md` in the same change that
  adopts the amendment.
- Bump **Version** using:
  - MAJOR: remove or redefine a principle incompatibly.
  - MINOR: add or materially expand a principle or section.
  - PATCH: clarification, wording, or typo with no semantic change.
- Set **Last Amended** to the amendment date (ISO `YYYY-MM-DD`).
- **Ratified** does not change after first adoption.

Compliance:

- Reviews and `/speckit.analyze` MUST check proposed work against these
  principles before merge or implementation.
- Unjustified complexity (new context, new abstraction, new tracker
  surface) MUST be rejected or recorded as an ADR.
- A new script, tool, or util that is not agent-shaped MUST be rejected.

Runtime development guidance: `AGENTS.md`.

**Version**: 1.1.0 | **Ratified**: 2026-09-11 | **Last Amended**: 2026-09-11
