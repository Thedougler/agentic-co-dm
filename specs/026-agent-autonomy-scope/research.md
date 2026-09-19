# Research: Agent Autonomy Scope

```text
work_class: agent-system
route: full-sdd
reason: reusable operating rules for canon, lint-as-contract, and no approval wait
```

`context_used`: constitution X/XII/XV/XVI/XVII/XX/XXI/XXIV and Operating Boundaries; `specs/026-agent-autonomy-scope/spec.md` (Session 2026-09-18 clarifications); `AGENTS.md` Autonomy classification (now stale vs spec); `docs/agents/work.md`; `docs/agents/wiki-maintenance-loop.md`; `docs/agents/hybrid-sdd.md`; `docs/agents/policy-owners.yml`; `wiki/AGENTS.md`; `.agents/skills/**/SKILL.md` Work-gate headers; `rules/registry.yml`; `tools/creative_lint/evaluators/symbolic.py`; `.vale.ini`; `.agents/skills/skill-creator/SKILL.md` eval loop; `scripts/check-policy-conflicts`.

`context_omitted`: Foundry MCP, beat-card catalogs, `tools/wiki_ops` mutation internals (025), Vale prose-quality styles.

Subagent redeploy (`scout`, then `task`) failed with OpenCode billing 401. Parent completed this research.

## R-001: Spec vs current instructions

**Decision**: Treat Session 2026-09-18 clarifications as the spec. Existing `plan.md` / `autonomy-boundary.md` / `AGENTS.md` table (`autonomous` vs `dm-gated`, Work wait on new content) are stale and must be replaced.

**Rationale**: Clarifications Q3–Q4, Q7, Q9: user speech is canon; file it; no Work gates; no approval wait; mixed requests do both then one done-summary after green.

**Alternatives considered**: Keep the binary classification table (rejected: contradicts FR-001/FR-003/FR-005).

## R-002: Constitution must amend in this feature

**Decision**: MAJOR constitution amendment in the same change. Principles X, XV, XVII and Operating Boundaries currently require DM acceptance before campaign-fact writes. Implementing FR-001 in `AGENTS.md` without amending them violates XVI (lower layers must not contradict).

| Current | Replacement |
|---------|-------------|
| X DM Owns Canon — invent/reconcile wait; Work inspectable until accept | Four-line canon (FR-003). Co-DM files what those lines make canon. Do not invent what the user did not say. Do not pick a winner among contradictions unless the user picked. |
| XV — novel campaign content is the DM approval boundary | Agents complete requested work and unattended maintenance. No approval wait. Done-summary after green. |
| XVII — accepted facts only through DM acceptance | Wiki stays additive and sourced. User/transcript/non-contradicting ingest file immediately. |
| Operating Boundaries — campaign facts remain DM-gated | Delete that sentence. |

Version: `2.11.0` → `3.0.0` (redefine principles). Governance: this feature branch is the tracked work; Sync Impact Report lives in the constitution amendment notes.

Keep XII (evidence before invention; invented distinguishable). That is not a wait gate.

**Rationale**: Spec Q9 + XVI. Papering over the conflict would ship competing SoTs.

**Alternatives considered**: Complexity-track an unjustified X/XV/XVII violation (rejected: ERROR gate). Leave constitution and only edit AGENTS.md (rejected: XVI).

## R-003: Four-line canon is the whole workflow

**Decision**: Encode exactly:

1. If the user said it, it is canon.
2. If the user said it more recently, that is more canon.
3. If a transcript says it, after ASR issues are fixed, it is canon.
4. DM-placed ingest files are canon as long as they do not contradict 1–3.

No extra steps. File the work. Self-heal checkable rules to green. One short done-summary. No question. No wait. MUST NOT interrupt with findings, contradiction alerts, or extra questions (Q6).

Conflict handling without a pause: more recent user statement wins; contradicting ingest is not canon; do not ask.

**Rationale**: FR-003, Q7, Q9.

**Alternatives considered**: Keep Work propose/accept for “collaborative creative work” (rejected: Q9). Flag contradictions to the user (rejected: Q6).

## R-004: Lint is the contract

**Decision**: Each new agent-facing standard in this feature ships as a machine-checkable rule. Agents iterate until green, then done-summary. `AGENTS.md` is why/examples plus a pointer. Same rules on the agent path and the human path (FR-014).

Do not retrofit existing prose-only standards (FR-011 last sentence).

**Rationale**: FR-004, FR-011, FR-012, FR-014, Q5, Q6, Constitution XXI.

**Alternatives considered**: Prose-only AGENTS.md table (rejected: Q5). New review skill/checklist (rejected: FR-007).

## R-005: Where the checks live

**Decision**: Smallest existing surface, not a new lint framework.

| Rule | Encodes | Evaluator | Why this surface |
|------|---------|-----------|------------------|
| AGENT001 | FR-001, FR-005 | New `scripts/check-agent-standards.py` + `rules/registry.yml` | Vale `[*]` would false-positive wiki mentions of Work; `creative_lint` symbolic.py is wiki-loader scoped |
| AGENT002 | FR-013 | Same script | Filename/path is not a Vale token check |
| AGENT003 | FR-004, FR-011 | Same script | Later `specs/*/spec.md` agent-facing FRs must cite a `rules/registry.yml` id |

Copy pattern: `scripts/check-policy-conflicts` (args in, JSON out, exit 0/1) + `tests/test_policy_conflicts.py`. Register ids in `rules/registry.yml` (`evaluator: symbolic`, `scope: instruction`, `severity: BLOCK`). One pytest runs the script. No new CI job; existing pytest catches it.

Green-before-done for wiki pages remains existing `wiki-lint` / Vale / template HARD keys (already checkable). This feature does not re-encode those.

**Alternatives considered**: Extend `evaluate_symbolic` (rejected: wiki loader). Vale existence on `## Work gate` (rejected: path scoping + wiki false positives). New Vale package (rejected: XIV).

## R-006: AGENT001 / AGENT002 / AGENT003 mechanics

**AGENT001**: Fail if agent-facing instruction files still describe Work-gate / DM-approval-wait / extra canon workflow. Scan: `AGENTS.md`, `wiki/AGENTS.md`, `docs/agents/**/*.md`, `.agents/skills/**/*.md`. Forbidden procedure language after this feature: `## Work gate`, `dm-gated`, `file nothing until accept`, `wiki write after DM accept`, `Work-propose`, `wait for accept`. Existing files in that scan MUST be edited until green.

**AGENT002**: Scan the live agent-facing tree. Paths must match:

- `.agents/skills/<kebab>/SKILL.md`
- `.agents/skills/<kebab>/<kebab>.md`
- `docs/agents/<kebab>.md` or `docs/agents/<kebab>.yml`
- `AGENTS.md`, `wiki/AGENTS.md`, `.omp/AGENTS.md`

Non-conforming files MUST be renamed in this feature; references updated. `checks.md` / `consolidate.md` remorph to kebab.

**AGENT003**: A `specs/*/spec.md` Functional Requirement that uses `agent-facing` must cite at least one `rules/registry.yml` `id`. This feature’s spec.md cites AGENT001–AGENT003. Every existing spec that uses that phrase MUST cite an id.

**Alternatives considered**: Grandfather existing tree (rejected: later user statement). Proactive adapter exclude-list (rejected: carve-outs only after a problem already experienced).

## R-007: Instruction files to strip

**Decision**: Remove Work-gate / accept-before-write procedures from every instruction this feature’s lint will scan. Positive replacement: four-line canon, file it, green, done-summary.

Hottest surfaces:

| File | Current wait sentence |
|------|------------------------|
| `AGENTS.md` | Autonomy table; `Load docs/agents/work.md` Work gate; new owner “file nothing until accept” |
| `docs/agents/work.md` | Propose: do not create wiki page yet; Decide accept/reject |
| `wiki/AGENTS.md` | `lifecycle` defaults to `proposed` until DM accepts; “Wiki facts change only after the DM accepts” |
| `docs/agents/wiki-maintenance-loop.md` | Classify via Autonomy table; Layer C lore invent Nick-gated even when the user asked |
| `docs/agents/hybrid-sdd.md` | `dm_acceptance` / Work acceptance produces accepted truth |
| `docs/agents/policy-owners.yml` | `acceptance_semantics` owner `work.md`; `mutation_approval` requires acceptance |
| Creative `SKILL.md` `## Work gate` | campaign-planning, cold-opens, dnd-5e-magic-item-design, dnd5e-mechanics, dungeon-design, encounter-prep, homebrew-monsters-5e, npc-design, pc-interview, place-design, reconciling-session-evidence, run-guide, sandbox-narrative, session-recap, theatre-of-the-mind, traps-trials, travel-events, visual-aids, visual-references, world-tick, writing-beats (plus any remaining `## Work gate` hit) |
| `wiki-lint` / `wiki-ingest` | Align with file-it + green + done-summary; named ingest already files without a second ask |

Skill-design class: `not` (established-file strips + AGENTS.md). No designated-writer dispatch.

**Rationale**: FR-005. AGENT001 will fail until these are gone.

**Alternatives considered**: Leave Work-gate headers as pointers to work.md (rejected: AGENT001 and FR-005). New skill (rejected: XIV, FR-007).

## R-008: Wiki writes go live

**Decision**: Category pages land on live vault paths. “Create NPC Varn” → write the page, lint green, done-summary.

**Rationale**: Spec Assumptions.

**Alternatives considered**: Bypass staging for user-requested canon (rejected: orthogonal safety net). Chat-wait for stage-commit (rejected: FR-001).

## R-009: Project identity

**Decision**: Keep the short **Project identity** block already in `AGENTS.md`. Review of skill/instruction diffs uses existing `skill-creator` eval loop (held-out prompts, with-skill vs without-skill, graded assertions). MUST NOT add checklist, PR template, or review skill.

**Rationale**: FR-006, FR-007, Q2.

## R-010: Done-summary and mixed requests

**Decision**: After green, one short done-summary: what changed, where. Not a question. Mixed maintenance + new content: do both, one summary (FR-010, Q3).

**Rationale**: FR-008, FR-009, Q1.

**Alternatives considered**: Autonomous-then-Work same-turn split (rejected: Q3/Q9). Silent completion (rejected: Q1).

## R-011: Unattended maintenance vs user-asked invent

**Decision**: FR-002 list still runs unattended (lint, conform, ingest, bookkeeping). User-asked new content files under FR-003. Unattended Layer C still MUST NOT invent lore the user did not say (XII + four-line rule: unsaid is not canon). Dedup merge stays a destructive confirm (not a canon Work gate); if the user said merge, file the merge.

**Rationale**: FR-002 + XII + Q9.

## R-012: Carve-outs

**Decision**: A carve-out exists only to fix a problem already experienced. Do not add exclude lists, unmanaged sets, or grandfather clauses because a rename *might* break generated adapters, skill protocol, or later Spec Kit regeneration.

**Rationale**: User: "when I say everything I mean everything"; "carve outs only exist to solve a problem already experienced, they are not applied proactively."

**Alternatives considered**: Exclude `speckit-*` / `.omp/commands/speckit.*` / templates up front (rejected: no breakage yet).

**Unresolved**: none. No `NEEDS CLARIFICATION`.
