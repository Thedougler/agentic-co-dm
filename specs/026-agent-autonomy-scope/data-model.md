# Data Model: Agent Autonomy Scope

No persisted store. Classification is evaluated per operation at task time.

## Entities

### Operation

| Field | Type | Rule |
|-------|------|------|
| name | string | Wiki or Co-DM task category |
| creates_or_changes_campaign_fact | bool | Decision-rule answer |
| classification | `autonomous` \| `dm-gated` | Derived; no third value |

**Decision rule**: `creates_or_changes_campaign_fact` true → `dm-gated`; false → `autonomous`.

Campaign fact: a statement about the campaign world the DM owns (people, places, factions, events, lore, motivations, mechanical encounters as fiction).

Not a campaign fact: structural metadata, formatting, link integrity, template shape, index/manifest/hot bookkeeping, search index, file layout with `facts_changed: false`, error-ledger rows.

### Work Gate

Existing entity in `docs/agents/work.md`. States: propose → decide (accept/reject/edit) → file.

Only `dm-gated` operations enter this lifecycle. `autonomous` operations skip Propose.

### Staging write

Orthogonal to classification. When `WIKI_STAGED_WRITES=true`, category page writes land under `wiki/_staging/`. Promotion is `wiki-stage-commit` (Nick file review), not Work.

## Autonomous operations (closed list for the table)

Matches spec FR-002 plus research R-002 bookkeeping that does not change facts:

- Lint repair: broken wikilinks, missing required frontmatter, invalid type/lifecycle to nearest valid
- Template conformance that only relocates existing content
- Index / `log.md` / `hot.md` maintenance
- Manifest recording
- Staging-area and `_raw/` inbox management
- Named ingest into `_staging/` (sources the DM already named)
- Structural layout moves (`facts_changed: false`, `type_changed: false`, `links_resolve: true`)
- Error-ledger append/drain
- QMD refresh / `qmd-hook.sh`

## DM-gated operations (closed list for the table)

Matches spec FR-003:

- New entity invention (NPC, faction, quest, place, item, spell, vehicle, region, lore)
- Narrative content (session beats, cold opens, TotM, recap)
- Canon fact changes on existing pages
- Reconciliation of contradictory canon
- Inventing body to fill a required template field

## Explicitly not autonomous

| Operation | Why |
|-----------|-----|
| `wiki-dedup --merge` / consolidate Check 14 merge | Destructive identity merge; Layer C Nick-gated |
| Trust-ledger `base_confidence` rewrite | Requires approval in wiki-lint CHECKS.md |
| `wiki-stage-commit` promotion | File-review safety net, not classification |
| Creative skill Work headers | Already correct; leave them |

## Edge-case resolution

| Scenario | Classification | Validation |
|----------|----------------|------------|
| Template field empty; existing wiki/source can fill it | `autonomous` grounded fill | Source-before-filling already in wiki-lint |
| Template field empty; no source | `dm-gated` if inventing; else preserve + flag | FR-008 |
| Ingest vs live canon conflict | Stage + marker `autonomous`; resolve `dm-gated` | Spec edge |
| Mixed "clean up and expand" | Split | Spec edge |
| Contradiction during lint | Flag `errors.md` `autonomous`; do not pick winner | FR-008 |
| Unlisted operation | Apply decision rule | FR-001 |

## State transitions

Classification is stateless. Work-gate transitions remain those in `docs/agents/work.md`.

## Relationships

- Classification → Work gate: only `dm-gated`
- Classification → staged writes: independent
- Classification → error ledger: autonomous discovery of canon issues writes an error; resolution is `dm-gated`
- `AGENTS.md` table is the single owner; skills defer
