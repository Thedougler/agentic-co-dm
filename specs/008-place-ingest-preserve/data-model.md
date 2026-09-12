# Data Model: Place Ingest Preserve

Entities are wiki pages. No database.

## Place page

Campaign `type: place` the DM runs.

| Field | Rule |
|---|---|
| `type` | `place` (map early `location` → `place` on file) |
| `category` | `entities` |
| `campaign` | Required |
| `visibility` | Default `dm` |
| `lifecycle` | Default `proposed` until DM accepts |
| `reveal` | Distinct from `visibility` |
| `summary` | One sentence |
| `kind` | Often `site`; omit unused |
| `region` | When placed |
| Filed path | `wiki/entities/<filename>` after ingest |
| Staging | `_raw/` evidence stays; ingest files a copy |

### Required spoken look

Open `[!narration]` titled **Narration** (typically under Overview). Theatre of the mind. Complete place: filled. Thin/stub place: empty titled stub still present. Ingest never deletes this block.

### Place format (jobs)

Look; what the site is now; moves that change the scene; presence or sign of absence; table objects; connections; purpose. Campaign shape: Overview + narration, At a glance, If the party, Who, What, Where, Why, Art when art exists. Omit unused. No-op moves omitted. Occupants not invented.

### Wiki-markdown treatments to preserve

`[!narration]`, image embeds, wikilinks, real line breaks, complete-sentence DM lines. Ingest copies these; it does not compile them away.

## Owner page

Exactly one page holds an object’s, hazard’s, or combatant’s numbers. The place links it. Ingest does not copy those numbers onto the place.

## Ingest / promote

Approved source → wiki. For `type: place`: preserve-and-file. For ordinary knowledge: distill as today. Session-prep stays on the 007 preserve path.

### States

`draft` → `proposed` → `accepted` / `rejected`. Rejected leaves no page. Re-ingest with no body change does not rewrite.

## Relationships

- Place *—* owner pages (wikilink)
- Place 1—1 spoken look block
- Ingest of place → `wiki/entities/`, preserve body
- Ingest of knowledge → compile
- Ingest of session-prep → session folder (007), not this model

## Out of model

Legacy places. Items, creatures, people. Session-prep. Foundry. Player sheets.
