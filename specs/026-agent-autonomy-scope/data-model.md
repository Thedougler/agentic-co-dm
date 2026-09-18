# Data Model: Agent Autonomy Scope

No persisted store. Classification is evaluated per operation at task time.

## Entities

### Operation

| Field | Type | Rule |
|-------|------|------|
| name | string | Wiki or Co-DM task category |
| user_asked_to_make_something_new | bool | Explicit create/invent request (including new creative content on an existing page) |
| invents_canon_or_reconciles_contradiction | bool | No-source invention, or pick-a-winner among conflicting facts |
| classification | `autonomous` \| `dm-gated` | Derived; no third value |

**Wait / decision rule** (FR-003): `user_asked_to_make_something_new` OR `invents_canon_or_reconciles_contradiction` → `dm-gated`; else `autonomous`. Operations on existing wiki content that neither invent nor reconcile do not wait.

Campaign fact: a statement about the campaign world the DM owns (people, places, factions, events, lore, motivations, mechanical encounters as fiction).

Not a campaign fact: structural metadata, formatting, link integrity, template shape, index/manifest/hot bookkeeping, search index, file layout with `facts_changed: false`, error-ledger rows.

### Work Gate

Existing entity in `docs/agents/work.md`. States: propose → decide (accept/reject/edit) → file.

Only `dm-gated` operations enter this lifecycle. `autonomous` operations skip Propose.

### Done-summary

Short conversational report after autonomous work: what changed, where. Not a Work proposal. Not a question. Does not wait.

### Staging write

Orthogonal to classification. When `WIKI_STAGED_WRITES=true`, category page writes land under `wiki/_staging/`. Promotion is `wiki-stage-commit` (Nick file review), not Work.

## Autonomous operations (closed list for the table)

Matches spec FR-002 plus research R-002 bookkeeping that does not invent facts:

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

- New lore, NPC, faction, quest, encounter, or narrative the user asked to create
- New creative content on an existing page the user asked to add (quest hook, new lore paragraph)
- Inventing canon facts (no source)
- Reconciliation of contradictory canon
- Inventing body to fill a required template field
- Whole new owner required by something the user asked to make (file nothing until accept; spoken waits)

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
| Mixed "clean up and expand" | Autonomous cleanup + done-summary, then Work in the same turn | FR-010 |
| Contradiction during lint | Flag `errors.md` `autonomous`; do not pick winner | FR-008 |
| New named owner, no page, user asked to introduce | Work-propose whole owner; file nothing; spoken waits | FR-003 / Q4 |
| Unlisted operation | Apply decision rule | FR-001 |

## State transitions

Classification is stateless. Work-gate transitions remain those in `docs/agents/work.md`.

Autonomous slice: execute → done-summary → stop (no wait). Mixed: autonomous slice then Work proposal in the same turn.

## Relationships

- Classification → Work gate: only `dm-gated`
- Classification → staged writes: independent
- Classification → error ledger: autonomous discovery of canon issues writes an error; resolution is `dm-gated`
- Classification → done-summary: every completed autonomous slice
- `AGENTS.md` table is the single owner; skills defer
