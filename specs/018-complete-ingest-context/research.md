# Research: Complete Ingest Context

## Decision: Keep `wiki-ingest` as the single workflow owner

**Rationale**: The skill already owns sequential file closure, source trust, distillation, and the ingest record. Completeness is a pass *inside* the open primary, not a second workflow.

**Alternatives considered**: A new “complete ingest” skill or a pre-ingest crawler. Rejected because they would split completion rules and duplicate 009/015.

## Decision: Ingest-time corroboration is not query-time precedence

**Rationale**: Feature 004 short-circuits: `wiki` → `shattered-sea` → `legacy-ss` → silence. That order is for answering canon questions. During ingest, a staging hit must not skip legacy, and a legacy hit must not skip staging (FR-005). Compiled `wiki` remains the page to update (015) and current canon on conflict (004). It is not a reason to skip source corroboration.

**Alternatives considered**: Reuse 004 order unchanged during ingest. Rejected because a `wiki` or staging hit would hide older supporting context.

## Decision: Search staging on disk; search legacy collections with the existing search index

**Rationale**: Staging drafts live in `_raw/` and are often not in a collection yet. Older variants live in campaign-of-record collections (`shattered-sea`, `legacy-ss`) and, when named, the `legacy/` archive collection (`-c legacy`). The designated retrieval layer is already QMD. XIV: run that CLI; do not wrap it.

**Alternatives considered**: Index `_raw/` into a new collection; grep the whole vault; change default query order. Rejected as extra machinery and as a 004 regression.

## Decision: Discover from the primary’s content and subject, then stop

**Rationale**: FR-002 forbids treating the rest of the vault as in-scope. Candidates are links, embeds, explicit names, and the primary’s own subject. Each related file is read at most once per primary.

**Alternatives considered**: Walk all of `_raw/` or all legacy hits for the campaign. Rejected as unbounded and token-heavy.

## Decision: Recency ranks corroborating sources; compiled wiki is still canon

**Rationale**: Among the primary and its related *sources*, the newest file is the latest DM decision; older variants supply uncontradicted support. That does not license silent overwrite of an already-compiled wiki page, nor filing a legacy hit as a wiki page without DM accept. Named ingest of an approved primary still compiles that primary’s latest decisions per 015, with older contradiction surfaced as a proposal.

**Alternatives considered**: (a) Always prefer newest over compiled wiki. Rejected — recency of an unapproved or legacy file is not canon. (b) Ignore recency among sources (015 research’s rejected alternative, in a different context). Rejected for 018 — the user named newest files as latest decisions among the evidence set.

## Decision: Related reads are not overlapping named ingests

**Rationale**: 009’s sequential unit is the DM-named input file. Reading a related draft as corroboration keeps the current primary `open`. If that related file is itself a later named input, it is ingested as a primary only on its turn.

**Alternatives considered**: Auto-expand the batch to every related file as a new primary, in parallel or immediately. Rejected: overlaps 009 and unbounded scope.

## Decision: Extend the ingest record; do not add a new tracking store

**Rationale**: Completeness is unverifiable without naming related reads, misses, staging vs legacy, and recency conflicts. `log.md` / the per-file report already exist.

**Alternatives considered**: A new sidecar database or manifest schema. Rejected; the DM-facing report is the seam.

## Decision: Skill edit is design-impact; validate with fixtures

**Rationale**: Adding a required complete-context pass is a major change to `wiki-ingest`. Implement dispatches the designated writer with a scoped prompt. Tests observe compiled pages and the ingest record, not skill phrasing.

**Alternatives considered**: Session-agent rewrite of the skill during plan. Rejected by XI. Grep-based skill snapshots. Rejected by IV.
