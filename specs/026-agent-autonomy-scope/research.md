# Research: Agent Autonomy Scope

## Hybrid SDD

```text
work_class: agent-system
route: full-sdd
reason: reusable operating rule for when agents may write wiki/system files without DM chat approval
```

`context_used`: constitution XV/X/VIII/XVI/XX, `specs/026-agent-autonomy-scope/spec.md`, `AGENTS.md`, `docs/agents/work.md`, `docs/agents/wiki-maintenance-loop.md`, `.agents/skills/wiki-lint/{SKILL.md,CONSOLIDATE.md}`, `.agents/skills/wiki-ingest/SKILL.md`, `CONTEXT.md` glossary.

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

**Decision**: Autonomous iff the operation does not create, extend, or modify a campaign fact. Exhaustive list for the AGENTS.md table:

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

## R-003: DM-gated set (FR-003)

**Decision**: Any operation that creates, extends, or modifies a campaign fact enters the existing Work gate. No new approval mechanism.

Includes: new entity invention; narrative (beats, cold opens, TotM, recap); canon fact edits on existing pages; choosing a winner among contradictory canon; filling a required template field by invention.

**Rationale**: Constitution X + work.md Propose/Decide/File. work.md already files on a direct imperative to repair a named page unless invention occurs.

**Alternatives considered**: Auto-accept "obvious" corrections (rejected: judgment). Third classification value (rejected: SC-005).

## R-004: Gray zone — mechanical tiebreakers

**Decision**: One question: does this operation create, extend, or modify a campaign fact? Yes → `dm-gated`. No → `autonomous`. Mixed requests split.

| Scenario | Split |
|----------|--------|
| Template conformance needs invented field body | Structure move `autonomous`; invented sentences `dm-gated` |
| Ingest contradicts live canon | Stage + conflict marker `autonomous`; pick-a-winner `dm-gated` |
| "Clean up and expand" | Cleanup `autonomous`; expansion `dm-gated` |
| Lint finds two facts that disagree | Flag to `errors.md` `autonomous`; resolution `dm-gated` |
| Content has no template field | Preserve + flag `autonomous`; discard would lose facts |
| `--consolidate` mix | FR-002 actions apply without confirm; merge/demote/lifecycle-judgment keep confirm |

**Alternatives considered**: `flag-and-proceed` as a third class (rejected: the flag is an error-ledger write during autonomous work).

## R-005: Expression

**Decision**: One heading in `AGENTS.md`: **Autonomy classification**. Binary table + the one-sentence decision rule. Skills and `work.md` point at it; they MUST NOT restate a competing list.

**Rationale**: Constitution V + XVI + XX. `AGENTS.md` is already the operating manual. A separate `docs/agents/autonomy.md` would fragment SoT.

**Alternatives considered**: Flowchart (harder in markdown). Per-skill tables (N copies).

## R-006: Project identity (FR-006, FR-007)

**Decision**: Short **Project identity** block in `AGENTS.md`: primary deliverables are skills, agent instructions, and guidance documents; scripts/tooling support those. Instruction PRs are reviewed on cold-context agent behavior (Constitution IV), not coverage/type-safety as primary criteria.

**Rationale**: Spec Story 3. No existing review-criteria doc mentions behavioral validation for SKILL.md changes.

**Alternatives considered**: Separate identity doc (rejected: SoT). Constitution amendment (rejected: XVI — operating rule, not a new principle).

## R-007: Skills that over-ask (FR-005)

**Decision**: Edit only surfaces that currently pause or contradict FR-002.

| File | Change |
|------|--------|
| `AGENTS.md` | Add table + identity; align kebab sentence with greenlit remorph |
| `docs/agents/work.md` | Work gate applies to campaign-fact operations; FR-002 ops do not enter Propose |
| `docs/agents/wiki-maintenance-loop.md` | Layer A may apply FR-002 structural repairs unattended; Layer C unchanged for lore/dedup/contradiction |
| `.agents/skills/wiki-lint/SKILL.md` | Page-scoped/bulk structural repair is autonomous; kebab remorph already greenlit |
| `.agents/skills/wiki-lint/CONSOLIDATE.md` | Do not confirm FR-002 actions; keep confirm for merge/demote/non-FR-002 |
| `.agents/skills/wiki-ingest/SKILL.md` | Named ingest → `_staging/` without a second chat approval; invented names still Work |

**Leave unchanged**: `wiki-dedup` merge confirm, `wiki-stage-commit` promotion review (orthogonal safety net, not Work), creative skills' existing Work-gate headers.

**Rationale**: Shortest diff that removes over-ask without weakening canon gates.

## R-008: Staged writes vs Work

**Decision**: Orthogonal. Classification answers "ask in chat?" Staging answers "live tree or `_staging/`?" Autonomous ops still honor `WIKI_STAGED_WRITES`. Promotion via `wiki-stage-commit` is Nick review of staged files, not a Work proposal.

**Rationale**: Spec Assumptions. Quickstart must not treat `_staging/` writes as Work-gate violations for FR-002, nor as a license to skip Work for FR-003 (creative pages in `_staging/` still require prior chat accept).

## R-009: Domain language

**Decision**: Use Constitution/spec terms: autonomous operation, Work gate, campaign fact. Do not use CONTEXT.md avoided term "autonomous GM". Do not add glossary entries to `CONTEXT.md` (operating rule, not campaign glossary).

**Unresolved**: none. No `NEEDS CLARIFICATION`.
