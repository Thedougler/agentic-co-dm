# Agentic Co-DM Constitution

## Core Principles

Product Invariant: The product is professional-quality, runnable D&D sessions comparable to
WotC material — coherent, specific, polished, mechanically sound, playable, and useful at the
table. Software, agent instructions, skills, and every other system surface serve that product.
Every change MUST identify an observable improvement to preparation, playability, player agency,
canon fidelity, or wrapup without sacrificing those qualities.

### I. Domain Language Is Binding

All work MUST use terms defined by `CONTEXT.md` and the applicable domain owner. Avoided terms
MUST NOT be used as synonyms. A missing term is a modeling gap, not permission to invent one.
Work conflicting with an ADR or accepted canon MUST name the conflict.

### II. Issues Are the Work Surface

Tracked project work MUST have an issue as its accountable surface. Agents MUST NOT begin
implementation from untracked requests when the issue workflow applies. External review artifacts
MAY land work but MUST NOT replace the issue as source of scope and ownership.

### III. Spec Before System Change

System changes MUST have a specification with independently testable acceptance before
implementation, connecting the change to an observable D&D improvement. Specs describe outcomes
and constraints, not creative method. Campaign Work follows its owner skill.

### IV. Behavioral Tests

Tests MUST assert observable behavior at public seams using domain language. New behavior MUST be
expressed by a failing test before implementation, one slice at a time. Tests MUST NOT pin
internals, recompute expected values, or bulk-speculate.

Agent-facing surface changes require behavioral validation: an independent test subject with cold
context performing the task the change improves. The lead reconciles subagent output as evidence.
When independent validation cannot run, record the blocker and compensating validation.

### V. Single Source of Truth

Each fact MUST have one authoritative owner. Copies MAY link or summarize but MUST NOT create
competing versions. Conflicts remain visible until resolved. Ownership map: `AGENTS.md` "Sources
of Truth."

### VI. Software and Instructions Are Agent-Shaped

Scripts, tools, and software MUST be agent-operable: arguments in, text/JSON out, errors on
stderr, exit status. Agent-facing documents MUST state positive instructions, completion criteria,
and named failure modes. `writing-for-agents` is the authority on agent-facing prose structure.

Agent-shaped software that inhibits wiki quality or slows operations is a defect — log it, fix or
remove the cause.

### VII. Creative Judgment Is Protected

Skills, specs, and reviews constrain only acceptance, safety, domain language, and named failure
modes — not creative method, voice, or structure. Narrative craft, mechanics, specificity, canon
fidelity, playability, player agency, and DM usefulness MUST NOT be traded for process metrics or
system optimization.

### VIII. Safe Automation Runs Unattended

Safe, idempotent maintenance runs without human chores. Repeatable operations MUST be encoded as
deterministic helper scripts, not re-derived by agents each session. Unsafe or judgment-requiring
automation MUST remain explicit. Automation preserves data and surfaces failures.

### IX. Measured, Quality-Bounded Efficiency

Fewer tokens for the same quality is always better. Token improvements MUST use objective
measurement comparing equivalent work. Protected quality constraints: narrative craft, mechanics,
specificity, canon fidelity, playability, player agency, DM usefulness.

Every standing instruction MUST earn its context cost. Unused scripts, friction-adding wrappers,
and duplicate instructions are waste.

### X. DM Owns Canon

The DM is the authority over campaign truth. The Co-DM MAY retrieve, infer, propose, and identify
contradictions. It MUST NOT silently convert invention into canon, fabricate evidence, or silently
reconcile conflicting canon. Canon-changing Work remains inspectable until the DM accepts it.

The system preserves boundaries between DM truth, player-visible information, and unrevealed
information. A presentation surface MUST NOT expose information outside its intended boundary.

### XI. Players Choose; The World Acts

Agents MUST NOT author PC decisions, intentions, beliefs, emotions, or predetermined routes.
Preparation supports materially different responses including engagement, negotiation, avoidance,
failure, and unexpected approaches.

NPCs, factions, and threats MAY move independently per established motives. Agents prepare
pressures and consequences; they MUST NOT treat a predetermined player outcome as the only route.

### XII. Evidence Precedes Invention

Agents MUST retrieve authoritative knowledge before inventing. Current accepted canon outranks
legacy, proposed, and external context. Silence MAY permit invention, but invented material MUST
remain distinguishable from retrieved fact. Evidence and citations MUST never be fabricated.

### XIII. Self-Improvement Is Evidence-Driven

Improvements MUST be demonstrated, not asserted — addressing observed failures or measured waste,
comparing equivalent work. Uncertain changes remain reversible until evidence supports promotion.

Self-reporting SOP: when an agent experiences friction on any agent-facing surface, it MUST record
the issue in `errors.md` before continuing. Every recorded error MUST be diagnosed by a different
agent and remediated at its authoritative source; continued progress is not resolution.

### XIV. The Simplest Adequate Tool

Use the simplest tool that works. Existing tools, stdlib, and platform features before new
abstractions. Project-declared dependencies are mandatory — install immediately if missing,
without asking. Reuse existing software and patterns before inventing.

### XV. Autonomous Operation

Agents proactively complete routine, deterministic, safe, idempotent maintenance without human
approval. Novel campaign content creation is the DM approval boundary.

Current standards are the only baseline. Legacy behavior has no grandfathered status — proactively
correct nonconformance when discovered. When the user directs work on a feature branch, that
branch is owned; agents MUST NOT reset, rebase, or merge it without explicit authorization.

Wiki branch, merge, and commit rules: `AGENTS.md` "Helpers."

### XVI. Constitutional Layering

Constitution: stable invariants, governance, cross-cutting rules. `AGENTS.md`: project context,
routing, sources of truth, operating procedures. Specs/contracts: feature behavior. Skills: task
procedures. ADRs: resolved architecture. Lower layers operationalize but MUST NOT duplicate
principles.

Reader-specific routing (`AGENTS.md` "Writing and visual authorities") is mandatory. Harness
files (`OMP.md`, `CODEX.md`, `CLAUDE.md`, `GROK.md`) contain only harness-specific guidance and
MUST NOT restate shared behavior.

### XVII. The Wiki Is Additive and Self-Sealing

The Wiki is the single compiled, citable knowledge layer. Raw evidence is immutable. Changes land
as traceable additive operations with provenance. Agents MUST NOT overwrite history, silently
merge competing facts, or turn proposals into canon. Accepted facts change only through the DM
acceptance boundary. Incompatible records MUST be quarantined with an observable error.

Safe deterministic maintenance repairs structural drift without inventing lore or changing
accepted facts.

Wiki operational procedures (staging, linting, branching, maintenance): `AGENTS.md`.

### XVIII. Multi-Step Work Uses a Checked Todo List

Tasks requiring two or more actions MUST have an agent todo list before the first step. Name
every known step, identify the active step, add discovered steps. Mark each step complete
immediately. MUST NOT finish while an actionable step remains unchecked.

### XIX. User Corrections Become Durable Source Fixes

Corrections MUST be applied at the authoritative source, not merely acknowledged in chat. Wiki
corrections update the page durably, subject to the DM boundary. Every error-identifying
correction MUST be recorded in the error ledger and, when recurring, fixed at the producing
skill/template/instruction.

`==text==` in production prose is a user-marked quality error. Fix the language; removing only
the marker is non-compliant. Correct at the applicable skill/instruction level.

### XX. Lean Agent-Facing Documents

Agent-consumed text MUST contain only words necessary for correct execution. Every sentence earns
its context cost. No hedging required steps with "maybe", "perhaps", "consider", or "optional."
`writing-for-agents` is the authority on structure and pruning. This principle MUST NOT be used to
delete necessary safeguards or quality-critical domain detail.

### XXI. Linter Findings Require Root-Cause Repair

Every finding is evidence of a defect. Repair the cause and rerun. MUST NOT evade by rewording
without fixing, weakening rules, or adding exclusions. Recurring causes require fixing the
authoritative template/skill/instruction.

### XXII. Appropriate Delegation

Delegate bounded, independent work to subagents when it reduces context load or improves
verification. The delegator retains integration and correctness responsibility. MUST NOT delegate
when overhead or missing context makes direct execution safer. Subagents receive only necessary
context.

### XXIII. Validation Uses Real Surfaces

Wiki-affecting validation MUST exercise the current Wiki and real repository surfaces, not
fixtures alone. When wiki-grounded validation cannot run, record the blocker and compensating
evidence.

### XXIV. Synchronized Content Systems

The three systems — compiled Wiki, authoring guidance (templates/skills), and validation rules
(Vale) — stay synchronized. Changes to one MUST update relevant counterparts in the same change.
Agents proactively maintain all three using observed failures, corrections, and evidence.

## Operating Boundaries

- The Co-DM works in prep and wrapup; the DM is sole runtime at the table.
- Work is mutable until the DM accepts it. Drafts and unrevealed information remain protected.
- Runtime procedures, model details, exact commands, and thresholds belong in lower-level docs.
- Codex is the default harness for Spec Kit commands.
- Campaign facts remain DM-gated even when agents own routine maintenance.

## Development Workflow

1. **Triage**: accountable issue and clear ownership before system work.
2. **Specify**: independently testable outcomes; resolve domain/ADR conflicts.
3. **Plan and task**: implementation plan and dependency-ordered tasks from the spec.
4. **Implement**: one behavioral slice at a time, simplest adequate surface.
5. **Review**: constitution, source ownership, behavioral evidence, safety, quality, canon.

## Governance

This constitution supersedes informal practice and skill defaults. Amendments require tracked
work, stated governance effect, and a Sync Impact Report.

Versioning: MAJOR (remove/redefine principle), MINOR (add principle/section), PATCH (clarify).

`Ratified` MUST NOT change. `Last Amended` records latest amendment date.

Compliance reviews check proposed work against this constitution before merge. Project context:
`AGENTS.md`. Harness behavior: `OMP.md`, `CODEX.md`, `CLAUDE.md`, `GROK.md`.

**Version**: 2.11.0 | **Ratified**: 2026-09-11 | **Last Amended**: 2026-09-17
