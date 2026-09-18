# Contract: Autonomy Boundary Classification

Owner after implement: `AGENTS.md` heading **Autonomy classification**. This file is the implement-time contract; skills MUST NOT ship a competing table.

## Decision rule

Wait only if the user explicitly asked to make something new, or this operation would invent canon facts or reconcile contradictory canon.

- Yes → `dm-gated` (Work gate: propose → decide → file; spoken that depends on a missing new owner waits)
- No → `autonomous` (execute; honor staged-writes; commit; one done-summary: what changed, where; no question; no wait)

Operations on existing wiki content that neither invent nor reconcile MUST NOT wait.

Unlisted operations use this rule. No `maybe`. Mixed requests split in the same turn: autonomous + done-summary first, then Work proposal; no wait between.

Do not say "autonomous GM" (`CONTEXT.md` avoided term).

## Table (copy into AGENTS.md)

| Operation | Class | Notes |
|-----------|-------|-------|
| Lint repair (links, required frontmatter, nearest-valid type/lifecycle) | autonomous | Default wiki-lint page-scoped/bulk; then done-summary |
| Template conformance of existing content | autonomous | Do not invent missing field body |
| Index / log.md / hot.md / manifest | autonomous | Bookkeeping |
| Named ingest into `_staging/` | autonomous | Sources the DM already named |
| Staging / `_raw/` file management | autonomous | Not canon |
| Layout move (`facts_changed: false`) | autonomous | AGENTS.md Layout |
| Error ledger, QMD refresh | autonomous | DM does not drain the ledger |
| Filename kebab / Aruhe / `00` remorph | autonomous | Greenlit 2026-09-14 |
| New lore / NPC / faction / quest / encounter / narrative the user asked to create | dm-gated | Work gate; includes new creative content on an existing page |
| Invented canon facts (no source) | dm-gated | Work gate |
| Contradictory-canon resolution | dm-gated | Flag during autonomous work; do not pick |
| Invented template-field body | dm-gated | Preserve + flag if no source |
| New named owner with no page (user asked to introduce) | dm-gated | Work-propose the whole owner; file nothing until accept; spoken waits |
| Dedup merge | dm-gated | Nick confirm; not FR-002 |
| wiki-stage-commit promotion | n/a | Staging review; not Work; not this table |

## Invariants

1. Exactly one class per operation after split.
2. `AGENTS.md` is the only table. Skills link or stay silent.
3. `WIKI_STAGED_WRITES` does not change class.
4. Creative pages still require Work accept before `_staging/` or live write (FR-003). FR-002 writes may land in `_staging/` without chat propose.
5. Canon issues found during autonomous work → `errors.md`; no silent resolve (FR-008).
6. After autonomous work: one done-summary (what changed, where). No question. No wait (FR-009).
7. Mixed request: autonomous + done-summary, then Work in the same turn (FR-010).
8. HARD gates `entity-before-spoken` and `dm-facing-explicit` stay quality gates on DM-gated output. They are not approval gates for lint. Missing new owner → Work-propose the whole owner; do not stub.

## Work.md delta

Add one scoped sentence: load Work before prep/wrapup **and** before any FR-003 wait. Do not load Work as a pause for FR-002 operations. Keep the existing Decide bullet: direct imperative to repair/merge a named existing page is acceptance unless the change invents canon.

## Skill deltas

- `wiki-lint/SKILL.md`: structural repair is autonomous; kebab remorph needs no extra greenlight; end with a done-summary.
- `wiki-lint/CONSOLIDATE.md`: apply FR-002 actions without `"Apply these N changes?"`; keep confirm for merge, tier demotion, and other non-FR-002 actions.
- `wiki-ingest/SKILL.md`: named ingest does not wait for a second chat accept; invented names still Work.
- `wiki-maintenance-loop.md`: Layer A may apply FR-002 repairs; Layer C unchanged.

## Project identity (AGENTS.md)

Primary deliverables: skills, agent instructions, guidance documents. Scripts support those. Skill/instruction review uses existing `skill-creator` evals (held-out prompts, with-skill vs without-skill, graded assertions). MUST NOT add a checklist, PR template, or review skill.

## Validation

Given each spec acceptance scenario and each edge case, the table plus decision rule yields one class. Two cold-context agents given the same task description and this table MUST agree (SC-005).
