<!--
Sync Impact Report
- Version change: 3.1.0 -> 4.0.0
- Modified principles: XV (done-summary follows a clean lint), XXI (redefined: one linter; every finding is an issue; clean means zero issues)
- Added sections: none
- Removed sections: none
- Follow-up TODOs: remove finding tiers from lint tooling, specs, docs, and skills that still grade findings into kinds (see XXI)
-->

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
Filing a new named campaign page is Campaign Work: load and complete the
owner skill for that kind before the page is filed.

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

If the user said it, it is canon. If the user said it more recently, that is more canon. If a transcript says it, after ASR issues are fixed, it is canon. DM-placed ingest files are canon as long as they do not contradict 1–3.

The Co-DM files what those lines make canon (`user_said`, `more_recent_user_said`, `corrected_transcript`, `dm_placed_ingest`). It MUST NOT invent what the user did not say (XII). It MUST NOT pick a winner among contradictions unless the user picked.

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

Agents complete requested work and unattended maintenance with no approval wait. When `wiki lint` is clean (principle XXI) and every other checkable rule passes, emit one short done-summary.

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
files (`.omp/AGENTS.md`, `CODEX.md`, `CLAUDE.md`, `GROK.md`) contain only harness-specific guidance and
MUST NOT restate shared behavior.

### XVII. The Wiki Is Additive and Self-Sealing

The Wiki is the single compiled, citable knowledge layer. Raw evidence is immutable. Changes land as traceable additive operations with provenance. Agents MUST NOT overwrite history or silently merge competing facts. User speech, corrected transcripts, and non-contradicting DM-placed ingest file immediately. Unsaid invention is not canon. Incompatible records MUST be quarantined with an observable error.

Safe deterministic maintenance repairs structural drift without inventing lore or changing
accepted facts.

Wiki operational procedures (staging, linting, branching, maintenance): `AGENTS.md`.

### XVIII. Multi-Step Work Uses a Checked Todo List

Tasks requiring two or more actions MUST have an agent todo list before the first step. Name
every known step, identify the active step, add discovered steps. Mark each step complete
immediately. MUST NOT finish while an actionable step remains unchecked.

### XIX. User Corrections Become Durable Source Fixes

Corrections MUST be applied at the authoritative source, not merely acknowledged in chat. Wiki corrections update the page durably under principle X. Every error-identifying correction MUST be recorded in the error ledger and, when recurring, fixed at the producing skill/template/instruction.

`==text==` in production prose is a user-marked quality error. Fix the language; removing only
the marker is non-compliant. Correct at the applicable skill/instruction level.

### XX. Lean Agent-Facing Documents

Agent-consumed text MUST contain only words necessary for correct execution. Every sentence earns
its context cost. No hedging required steps with "maybe", "perhaps", "consider", or "optional."
`writing-for-agents` is the authority on structure and pruning. This principle MUST NOT be used to
delete necessary safeguards or quality-critical domain detail.

### XXI. One Linter; Every Issue Is Fixed

`wiki lint` is the project's one lint system, and every finding it reports is an **issue**.
Every issue is in scope and MUST be fixed at its cause, then the lint rerun. Work is **clean**
only when the linter reports zero issues; while any issue remains, the work is not done. Clean
has one meaning, and no qualifier or grouping of findings makes any issue optional or out of
scope. MUST NOT evade by rewording without fixing, weakening rules, or adding exclusions.
Recurring causes require fixing the authoritative template/skill/instruction.

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

### XXV. Carve-Outs Are Retrospective

Apply a rule to the whole named set. When the user names *everything*, that set is the work.
A smallest-slice reading of a whole-set instruction is a defect.

Implement one *uniform* *composed* path. A filter, except list, unmanaged set, grandfather
clause, or hardcoded special case exists only to fix a problem already experienced in this
repository. Name that failure when adding it. MUST NOT add one because a change might break
later.

### XXVI. Skill Evaluation Uses the Weakest Sufficient Model

Skill evaluation, behavioral testing, benchmarking, and related validation MUST use the weakest
available model that can complete the task. Evaluation prompts and context MUST be clear,
concise, and focused so success demonstrates instruction quality rather than excess model
capability. The `skill-creator` workflow MUST be used only when modifying agent skills; other
agent-facing or project changes MUST use their applicable workflow. This isolates instruction
quality from model strength and keeps workflow selection bounded.


Sync Impact Report (2026-09-18): MAJOR 3.0.0. Redefined X, XV, XVII and Operating Boundaries: four-line canon; file what those lines make canon; no approval wait; done-summary after green. `AGENTS.md` points. Skills lose Work-gate headers. `AGENT001`–`AGENT003` encode the contract. Wiki, Vale, and templates unchanged except wait language.

Sync Impact Report (2026-09-19): PATCH 3.0.1. Clarified III: filing a new named campaign page is Campaign Work and MUST complete that kind's owner skill before the page is filed. Routing tables stay in `AGENTS.md`. No principle added or renamed. Wiki, Vale, and templates unchanged.

Sync Impact Report (2026-09-23): MAJOR 4.0.0. Redefined XXI: `wiki lint` is the one lint system; every finding is an issue; every issue is in scope and fixed; clean means zero issues, with one meaning. XV's done-summary now follows a clean lint. Lower layers that sort findings into kinds must converge on XXI.

Sync Impact Report (2026-09-19): PATCH 3.0.2. Clarified XXV: the user's named set is the work set; shrinking it with filters, hardcoded special cases, or a smallest-slice reading is a carve-out. Default is one uniform composed path. `AGENTS.md` operationalizes. No principle added or renamed.

## Operating Boundaries

- The Co-DM works in prep and wrapup; the DM is sole runtime at the table.
- Filed wiki facts follow principle X. Drafts and unrevealed information remain protected.
- Runtime procedures, model details, exact commands, and thresholds belong in lower-level docs.
- Codex is the default harness for Spec Kit commands.

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
`AGENTS.md`. Harness behavior: `.omp/AGENTS.md`, `CODEX.md`, `CLAUDE.md`, `GROK.md`.

**Version**: 4.0.0 | **Ratified**: 2026-09-11 | **Last Amended**: 2026-09-23
