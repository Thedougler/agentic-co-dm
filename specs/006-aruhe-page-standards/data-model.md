# Data Model: Sample Content

Entities are wiki pages. No database.

## Sample page

A page authored as sample content: `_raw/` exemplar or a new page of those kinds.

| Field | Rule |
|---|---|
| `title` | Required |
| `category` | Default `entities` |
| `tags` | Required |
| `sources` | Required |
| `created` / `updated` | Required |
| `type` | Closed set. Sample kinds: `place`, `item`, `creature`, `npc`. Map early labels `location`→`place`, `monster`→`creature`, `lore`→`item` on file. |
| `lifecycle` | Default `proposed` (Work) until DM accepts |
| `reveal` | Default `unrevealed` |
| `campaign` | Required on campaign pages |
| `visibility` | Default `dm`. Distinct from `reveal`. |
| `summary` | One sentence a DM can read in a list |
| `region` | When the subject is placed |
| Kind extras | Place: `kind` (often `site`). Item: `kind`, `rarity`, `attunement`; omit `owner` when unused. Creature: `role`, `cr`. Person: `role`, `location`, `faction`; omit unused. |

Unused optional keys are omitted, not blank theatre.

### States (lifecycle)

`draft` → `proposed` → `accepted` / `rejected`. `canon` after accept when that is the vault’s term. Rejected leaves no page. This feature does not invent new lifecycle values.

## Kind (run questions)

Not a separate file type. Jobs the page must answer. Headings may vary.

| Kind | Campaign `type` | Jobs |
|---|---|---|
| Place | `place` | Look; situation now; moves that change the scene; presence or sign of absence; table objects; connections; purpose |
| Consumable | `item` | Look; classification; one effect; stop |
| Flora hazard | `item` | Look; start; notice; contact cost; careful passage; honest counterplay |
| Creature | `creature` | Look; runnable sheet; life (habitat, habits, diet, social); hunt (signs, instincts, opening, shut-down, aftermath) |
| Person | `npc` | Who and want; look; first minutes and posture change; named ties; combat only if they can fight |

## Spoken look

Theatre of the mind. Player-safe. No secrets, difficulty classes, unearned names, author thesis.

## Owner page

Exactly one page holds an object’s, hazard’s, or combatant’s numbers. Other sample pages link it. They do not copy the effect, save, or sheet.

## Stub

Named ingest only. Identity + complete sentences. No empty run-loop scaffolding.

## Legacy page

Not this model. Do not migrate, score, or convert on wrapup.

## Relationships

- Place stocks objects/creatures → links owner pages
- Creature habitat → links places; refusals → link hazards
- Person combat → sheet on page or one pointer to owner
- Sample page MUST NOT point at legacy as a clone target
