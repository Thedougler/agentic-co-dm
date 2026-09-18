# Research: Agent Autonomy Scope

## Hybrid SDD

```text
work_class: agent-system
route: full-sdd
reason: reusable operating rule for when agents may write wiki/system files without DM chat approval
```

`context_used`: constitution XV/X/VIII/XVI/XX, `specs/026-agent-autonomy-scope/spec.md` (including Session 2026-09-18 clarifications), `AGENTS.md`, `docs/agents/work.md`, `docs/agents/wiki-maintenance-loop.md`, `.agents/skills/wiki-lint/{SKILL.md,CONSOLIDATE.md}`, `.agents/skills/wiki-ingest/SKILL.md`, `.agents/skills/skill-creator/SKILL.md` eval loop, `CONTEXT.md` glossary.

`context_omitted`: Foundry/beat skill bodies (already Work-gated), `tools/wiki_ops` internals (025 owns mutations), Vale rule text.

## R-001: Where does the boundary live today?

**Decision**: No single classification table. Agents infer from three overlapping sources that disagree on apply-vs-ask.

**Rationale**:

- Constitution XV: routine deterministic safe idempotent maintenance without approval; novel campaign content is the DM boundary.
- `docs/agents/work.md`: Work is chat proposal then accept. Repair/merge of a named existing page is acceptance unless the change invents canon.
- `AGENTS.md` Helpers: "Never auto lore invent, mass kebab rename, dedup merge, or craft cuts." Filename kebab remorph is already greenlit in `docs/agents/wiki-maintenance-loop.md` (2026-09-14); AGENTS.md is stale on kebab.
- Maintenance loop Layer A is scan/dry-run; Layer C forbids auto lore, auto-dedup merge, auto-resolve contradictions.
- Default `wiki-lint` page-scoped repair already applies structural fixes without a Work prompt. `--consolidate` always asks `"Apply these N changes?"` even for broken-link rewrites.

**Alternatives considered**: Leave inference as-is (rejected: SC-005 fails). Per-skill copies of the boundary (rejected: Constitution V).

## R-002: Autonomous set (FR-002 only)

**Decision**: Autonomous iff the operation does not invent canon, reconcile contradiction, or create something the user asked to make new. Exhaustive list for the AGENTS.md table:

| Operation | Evidence it is already or should be unattended |
|-----------|-----------------------------------------------|
| Lint repair (broken links, required frontmatter, invalid type/lifecycle nearest-valid) | `wiki-lint` page-scoped steps 1–5; no Work prompt today |
| Template conformance of existing content into contract sections | wiki-lint "Template ceiling"; do not invent missing section body |
| Index / `log.md` / `hot.md` maintenance | ingest and lint already write these without accept |
| Manifest recording | `scripts/manifest.py record` |
| Staging-area management (`_staging/` writes, `_raw/` inbox) | `WIKI_STAGED_WRITES` policy |
| Named ingest processing into `_staging/` | work.md "Named ingest is DM approval for those sources" |
| Structural layout moves with `facts_changed: false` | AGENTS.md Layout |
| Error-ledger append/drain | DM MUST NOT fill or drain |
| QMD index/hook refresh | post-write hook |

**Not autonomous** (research overreach in earlier draft): `wiki-dedup --merge`, consolidate Check 14 merges, trust-ledger confidence rewrites, inventing content to fill empty template fields.

**Rationale**: Spec FR-002. Dedup merge is destructive and Layer C / AGENTS.md still Nick-gated. Spec does not list it.

**Alternatives considered**: Treat "obvious" canon typos as autonomous (rejected: Constitution X). Auto-merge clear duplicates (rejected: FR-002 omission + Layer C).

## R-003: When to wait (FR-003, Session 2026-09-18)

**Decision**: The agent waits only when the user explicitly asked to make something new, or the operation would invent canon facts or reconcile contradictory canon. Operations on existing wiki content do not wait.

DM-gated (Work propose → accept → file):

- New lore, NPC, faction, quest, encounter, or narrative the user asked to create (including new creative content on an existing page, e.g. "add a quest hook to Bloodhawk")
- Inventing canon facts (no source)
- Reconciling contradictory canon

Reuse the existing Work gate. No new approval mechanism.

**Rationale**: Clarification Q4 + FR-003. Earlier draft gated every campaign-fact edit on an existing page; that over-asks and violates "existing wiki content does not wait."

**Alternatives considered**: Gate every fact-touching edit (rejected: clarification). Auto-accept "obvious" corrections that invent (rejected: Constitution X). Third classification value (rejected: SC-005).

## R-004: Gray zone — mechanical tiebreakers

**Decision**: One question: would this invent canon, reconcile contradiction, or create something the user asked to make new? Yes → `dm-gated`. No → `autonomous`. Mixed requests split in one turn (R-011).

| Scenario | Split |
|----------|--------|
| Template conformance needs invented field body | Structure move `autonomous`; invented sentences `dm-gated` |
| Ingest contradicts live canon | Stage + conflict marker `autonomous`; pick-a-winner `dm-gated` |
| "Clean up and expand" | Cleanup `autonomous` + done-summary; expansion Work in the same turn |
| Lint finds two facts that disagree | Flag to `errors.md` `autonomous`; resolution `dm-gated` |
| Content has no template field | Preserve + flag `autonomous`; discard would lose facts |
| `--consolidate` mix | FR-002 actions apply without confirm; merge/demote/lifecycle-judgment keep confirm |
| Session prep needs a new named owner with no page | Work-propose the whole owner; file nothing; spoken waits (R-012) |

**Alternatives considered**: `flag-and-proceed` as a third class (rejected: the flag is an error-ledger write during autonomous work).

## R-005: Expression

**Decision**: One heading in `AGENTS.md`: **Autonomy classification**. Binary table + the one-sentence wait rule. Skills and `work.md` point at it; they MUST NOT restate a competing list.

**Rationale**: Constitution V + XVI + XX. `AGENTS.md` is already the operating manual. A separate `docs/agents/autonomy.md` would fragment SoT.

**Alternatives considered**: Flowchart (harder in markdown). Per-skill tables (N copies).

## R-006: Project identity (FR-006, FR-007)

**Decision**: Short **Project identity** block in `AGENTS.md`: primary deliverables are skills, agent instructions, and guidance documents; scripts/tooling support those. Review of skill/instruction changes uses the existing `skill-creator` eval loop: held-out prompts, with-skill vs without-skill (or old-skill snapshot), graded assertions. Do not add a review checklist, GitHub PR template, or new review skill. Coverage/type-safety are not the primary bar.

**Rationale**: Spec Story 3 + clarification Q2. Eval method already lives in `.agents/skills/skill-creator/SKILL.md` ("Running and evaluating test cases"). A second harness would violate FR-007 and Constitution XIV.

**Alternatives considered**: New PR template / review skill (rejected: FR-007). Constitution amendment (rejected: XVI — operating rule, not a new principle). Separate identity doc (rejected: SoT).

## R-007: Skills that over-ask (FR-005)

**Decision**: Edit only surfaces that currently pause or contradict FR-002.

| File | Change |
|------|--------|
| `AGENTS.md` | Add table + identity + wait rule + done-summary; align kebab sentence with greenlit remorph |
| `docs/agents/work.md` | Work gate applies when FR-003 wait conditions hold; FR-002 ops do not enter Propose |
| `docs/agents/wiki-maintenance-loop.md` | Layer A may apply FR-002 structural repairs unattended; Layer C unchanged for lore/dedup/contradiction |
| `.agents/skills/wiki-lint/SKILL.md` | Page-scoped/bulk structural repair is autonomous + done-summary; kebab remorph already greenlit |
| `.agents/skills/wiki-lint/CONSOLIDATE.md` | Do not confirm FR-002 actions; keep confirm for merge/demote/non-FR-002 |
| `.agents/skills/wiki-ingest/SKILL.md` | Named ingest → `_staging/` without a second chat approval; invented names still Work |

**Leave unchanged**: `wiki-dedup` merge confirm, `wiki-stage-commit` promotion review (orthogonal safety net, not Work), creative skills' existing Work-gate headers, `skill-creator` eval loop (reused, not extended).

**Rationale**: Shortest diff that removes over-ask without weakening canon gates.

## R-008: Staged writes vs Work

**Decision**: Orthogonal. Classification answers "ask in chat?" Staging answers "live tree or `_staging/`?" Autonomous ops still honor `WIKI_STAGED_WRITES`. Promotion via `wiki-stage-commit` is Nick review of staged files, not a Work proposal.

**Rationale**: Spec Assumptions. Quickstart must not treat `_staging/` writes as Work-gate violations for FR-002, nor as a license to skip Work for FR-003 (creative pages in `_staging/` still require prior chat accept).

## R-009: Domain language

**Decision**: Use Constitution/spec terms: autonomous operation, Work gate, campaign fact, done-summary. Do not use CONTEXT.md avoided term "autonomous GM". Do not add glossary entries to `CONTEXT.md` (operating rule, not campaign glossary).

## R-010: Done-summary (FR-009)

**Decision**: After autonomous work, the agent’s last message for that slice is one short done-summary: what changed, where. Not a question. Not a wait. Not a Work proposal.

**Rationale**: Clarification Q1. Current agents often end maintenance with "want me to commit?" / "look ok?" which is the over-ask this feature removes.

**Alternatives considered**: Silent completion (rejected: DM still needs to know what moved). Full Work-shaped proposal for maintenance (rejected: Q1).

## R-011: Mixed request, same turn (FR-010)

**Decision**: Cleanup now → done-summary → Work-propose the creative part in the same turn. No wait between those steps.

**Rationale**: Clarification Q3. Two treatments, one message (or one turn with both). Waiting for DM accept on the cleanup would reintroduce the P1 pause.

**Alternatives considered**: Wait after cleanup (rejected: Q3). Bundle both into one Work proposal (rejected: autonomous work must not wait).

## R-012: Missing owner for something new (FR-003, entity-before-spoken)

**Decision**: If the user asked to make something new and a required named owner has no page, Work-propose the whole owner. File nothing until accept. Spoken text that depends on that owner waits. Do not file a stub. Do not pause for existing wiki content that is already filed.

**Rationale**: Clarification Q4. HARD entity-before-spoken stays; the wait is the Work gate on the new owner, not a pause to invent a stub.

**Alternatives considered**: File a stub then narrate (rejected: Q4). Skip the owner page (rejected: entity-before-spoken).

**Unresolved**: none. No `NEEDS CLARIFICATION`.
