# Data Model: Agent Autonomy Scope

No persisted classification store. Canon and done-state are evaluated per request.

## Entities

### Canon Rule

Owner after implement: constitution principle X (amended). AGENTS.md points; does not own.

| Field | Type | Rule |
|-------|------|------|
| user_said | bool | The current user statement asserts the fact |
| more_recent_user_said | bool | A later user statement supersedes an earlier one |
| corrected_transcript | bool | Transcript fact after ASR issues are fixed |
| dm_placed_ingest | bool | Ingest file the DM placed, and it does not contradict the three lines above |

A fact is canon iff one of those four holds, with more-recent user speech winning. That is the entire canon workflow.

Not canon: unsaid invention; ingest that contradicts user/transcript; discarded ASR errors.

### Done-summary

Short conversational report after work is green: what changed, where. Not a question. Not a wait. Mixed requests share one summary.

### Lint Contract

Machine-checkable rules that encode new agent-facing standards from this feature onward.

| id | Encodes | Input | Fail when |
|----|---------|-------|-----------|
| AGENT001 | FR-001, FR-005 | Agent-facing instruction files | Work-gate / approval-wait / extra canon-step procedures remain |
| AGENT002 | FR-013 | Live agent-facing tree | Path or name is ad-hoc |
| AGENT003 | FR-004, FR-011 | `specs/*/spec.md` FRs containing `agent-facing` | No cited `rules/registry.yml` id |

Wiki HARD lint (links, frontmatter, templates, Vale on wiki) already exists. This feature does not duplicate it. Green-before-done (FR-012) means: every checkable rule that applies to the work just done is exit 0 before the done-summary.

### Staging write

Orthogonal. `WIKI_STAGED_WRITES=true` → category pages under `wiki/_staging/`. Not a conversation step. Promotion is `wiki-stage-commit`.

## Operations (FR-002)

Complete without a pause:

- Lint repair, template conformance of existing content, frontmatter normalization, link repair
- Ingest processing, structural migration
- Index / log.md / hot.md / manifest
- Staging-area and `_raw/` management
- User-requested new content (file under Canon Rule)

Unattended loops MUST NOT invent facts the user did not say.

## State transitions

```text
request → file what is canon → run applicable checkable rules
  → fail: repair cause, rerun (no user interrupt)
  → green: one done-summary → stop
```

No Propose / Decide / accept states.

## Relationships

- Canon Rule → wiki page write (immediate; staging flag may redirect path)
- Lint Contract → done-summary (blocks until green)
- AGENT001 → instruction files in R-007; existing files updated until green
- AGENT002 → whole scanned tree; bulk-rename + reference updates
- AGENT003 → this spec and later specs that use `agent-facing`
- `docs/agents/work.md` → no longer a gate; may keep table-aim / reflection that is not an approval wait

## Edge-case resolution

| Scenario | Action |
|----------|--------|
| Two user statements conflict | More recent wins; file it |
| Template field has no home | Preserve content; do not discard |
| "Clean up and expand" | Do both; one done-summary after green |
| Ingest contradicts user/transcript | Ingest is not canon; do not file that contradiction as truth; no ask |
| Session prep needs a named owner the user asked to introduce | File the owner page; spoken may follow |
| Later feature adds agent-facing standard in prose only | AGENT003 fail; feature incomplete |
| Existing instruction file predates this feature | Update and/or rename until AGENT001–AGENT002 green |
| Agent-facing file in an ad-hoc path | AGENT002 fail until renamed |
| Dedup merge without user ask | Not FR-002 unattended; destructive confirm remains |
| User asked to merge duplicates | File the merge; green; done-summary |
