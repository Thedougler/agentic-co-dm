<!--
Sync Impact Report
- Version change: 7.0.0 -> 7.1.0 (MINOR: VI gains a named authority for command design)
- Modified principles:
  - VI. Software and Instructions Are Agent-Shaped: adds `cli-for-agents` as the authority on
    command design, loaded before creating or changing any repository command, beside
    `writing-for-agents` for agent-facing prose (Nick, 2026-09-24).
- Added sections: none
- Removed sections: none (the 7.0.0 Sync Impact Report is replaced; git holds amendment history)
- Templates requiring updates: none (plan, spec, tasks, and checklist templates read the
  constitution at runtime; no template names command-design rules)
- Follow-up: AGENTS.md Skill Routing and Helpers point at `cli-for-agents`.
-->

# Agentic Co-DM Constitution

## Core Principles

Product Invariant: The product is professional-quality, runnable D&D sessions comparable to
WotC material — coherent, specific, polished, mechanically sound, playable, and useful at the
table, so a DM can run each beat cold from its page. Software, agent instructions, skills, and
every other system surface serve that product. **Table quality** names what the product protects:
narrative craft, mechanics, specificity, canon fidelity, playability, player agency, and DM
usefulness. Every change MUST identify an observable improvement to preparation, playability,
player agency, canon fidelity, or wrapup without lowering table quality.

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
and named failure modes. `writing-for-agents` is the authority on agent-facing prose structure;
`cli-for-agents` is the authority on command design, and agents load it before creating or
changing any repository command (flags, `--help`, errors, stdin/output, dry-run, idempotency).

Agent-shaped software that inhibits wiki quality or slows operations is a defect — fix or remove
the cause (XIII). Record it in `errors.md` only when it stays unresolved.

### VII. Creative Judgment Is Protected

Skills, specs, and reviews constrain acceptance, safety, domain language, and named failure
modes. Creative method and voice stay with the author; page structure stays with the templates
(XVI). Table quality MUST NOT be traded for process metrics or system optimization.

### VIII. Safe Automation Runs Unattended

Safe, idempotent maintenance runs without human chores. Repeatable operations MUST be encoded as
deterministic helper scripts, not re-derived by agents each session. Unsafe or judgment-requiring
automation MUST remain explicit. Automation preserves data and surfaces failures.

### IX. Measured, Quality-Bounded Efficiency

Fewer tokens for the same table quality is always better. Token improvements MUST use objective
measurement comparing equivalent work.

Every standing instruction MUST earn its context cost. Unused scripts, friction-adding wrappers,
and duplicate instructions are waste.

### X. DM Owns Canon

Canon is decided by Nick's rule, in precedence order:

> Something is canon if the DM says so > something is canon if it's present in the wiki in
> multiple places > something is canon if it doesn't conflict with the wiki.

That is the entire system: there is no page lifecycle, promotion, or confidence gate. The rule's
single owner is `.agents/skills/llm-wiki/SKILL.md`; other lower layers link to it and MUST NOT
restate it. Agents apply the rule; code MUST NOT assign, store, or gate on canon, and MAY only
report the facts that feed it (declared conflicts and single-source facts). A DM ruling is
recorded where the repo already records it (session log, recap `## Wiki facts`, or the DM's chat
statement filed on the owner page) and cited in that page's `sources:`. Where wiki sources
conflict, the agent names the conflicting sources; `retcon` handles corrections.

The system preserves boundaries between DM truth, player-visible information, and unrevealed
information. A presentation surface MUST NOT expose information outside its intended boundary.

### XI. Players Choose; The World Acts

Decide the world; leave the party's choices open. Preparation states what NPCs, factions,
threats, and clocks want and do, on their own schedule and per their motives, so the world acts
whether or not the party engages. Only the party's choices and the dice stay open.

Agents MUST NOT author PC decisions, intentions, beliefs, emotions, or predetermined routes.
Preparation supports materially different responses including engagement, negotiation, avoidance,
failure, and unexpected approaches, and no predetermined player outcome is the only route.

### XII. Evidence Precedes Invention

Agents MUST retrieve authoritative knowledge before inventing. Current canon (X) outranks
legacy and external context. Existing content is cast before new content is minted: a
page already in play, or an unrevealed page that fits the role, fills it first. Where canon is
silent on something the Work needs, agents decide it under X; where it contradicts itself, agents
name the conflicting sources under X. A gap left open where the DM needs an answer is a
defect. Evidence and citations MUST never be fabricated.

### XIII. Self-Improvement Is Evidence-Driven

Improvements MUST be demonstrated, not asserted — addressing observed failures or measured waste,
comparing equivalent work. Uncertain changes remain reversible until evidence supports promotion.

Friction rule: an agent that meets friction on any agent-facing surface MUST identify the cause,
fix the authoritative source, verify the fix, and continue the original task. Chat
acknowledgement or ledger text alone is not resolution.

`errors.md` MUST contain only reusable, unresolved defects. A friction the agent fixes and
verifies in the same task MUST NOT create an entry. A defect that cannot be fixed in the current
task, including one whose source is outside the repository, is recorded once; a failure whose
source and cause match an open entry adds an occurrence to that entry rather than a new one. A
verified fix MUST drain its entry in the same change that lands the fix.

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
procedures and craft. Templates: page structure. ADRs: resolved architecture. Lower layers operationalize but MUST NOT duplicate
principles.

Reader-specific routing (`AGENTS.md` "Writing and visual authorities") is mandatory. Harness
files (`.omp/AGENTS.md`, `CODEX.md`, `CLAUDE.md`, `GROK.md`) contain only harness-specific guidance and
MUST NOT restate shared behavior.

### XVII. The Wiki Is Additive and Self-Sealing

The Wiki is the single compiled, citable knowledge layer. Raw evidence is immutable. Changes land as traceable additive operations with provenance. Agents MUST NOT overwrite history or silently merge competing facts. Canon is decided under principle X.
Incompatible records MUST be quarantined with an observable error.

Safe deterministic maintenance repairs structural drift without inventing lore or changing
accepted facts.

Wiki operational procedures (staging, linting, branching, maintenance): `AGENTS.md`.

### XVIII. Multi-Step Work Uses a Checked Todo List

Tasks requiring two or more actions MUST have an agent todo list before the first step. Name
every known step, identify the active step, add discovered steps. Mark each step complete
immediately. MUST NOT finish while an actionable step remains unchecked.

### XIX. User Corrections Become Durable Source Fixes

Corrections MUST be applied at the authoritative source, not merely acknowledged in chat. Wiki corrections update the page durably under principle X. Every error-identifying correction MUST be fixed and verified at the producing
skill/template/instruction; it is recorded in `errors.md` only when that fix cannot land in the
current task (XIII).

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
(`wiki lint` Python checks, and Vale with the repo-local `Deprecated` style and the `CoDM`
vocabulary) — stay synchronized. Changes to one MUST update relevant counterparts in the same
change.
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
available model and reasoning effort that can complete the task. Evaluation prompts give cold,
focused context and the inputs the task needs, and compose real Wiki content (XXIII) rather than
minting new settings, so success demonstrates instruction quality rather than excess model
capability or context. The `skill-creator` workflow MUST be used only when modifying agent skills; other
agent-facing or project changes MUST use their applicable workflow. This isolates instruction
quality from model strength and keeps workflow selection bounded.

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

**Version**: 7.1.0 | **Ratified**: 2026-09-11 | **Last Amended**: 2026-09-24
