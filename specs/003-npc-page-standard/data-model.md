# Data Model: NPC Page Standard

## NPC page

A wiki page with `type: npc`. One person the DM can run.

| Field | Rule |
|---|---|
| title | Display name. Required. |
| category | Always `entities`. |
| tags | Include `npc`. Domain tags as needed. |
| sources | Traceable origins. Empty list only on unsourced Work. |
| created, updated | ISO dates. |
| type | `npc`. Do not invent type values. |
| lifecycle | `draft` \| `proposed` \| `accepted` \| `rejected` \| `canon`. Default `proposed` until DM accept. |
| reveal | `unrevealed` \| `revealed`. Default `unrevealed`. |
| campaign | Current campaign id. |
| status | `alive` \| `dead` \| `unknown`. Default `alive`. |
| role | `rival` \| `patron` \| `contact`. Required; no silent default. |
| location | Wikilink when known; else `unknown`. |
| faction | Wikilink or name when known; else `none`. |
| visibility | Who may read the page. Default `dm`. Distinct from `reveal`. |
| aliases | Optional list. Omit when unused. |
| summary | One sentence for lists. Required. |

Validation: every complete page has the identity fields above and the core spine. Stubs may omit Relationships if they have no named ties yet; they still use complete sentences.

## Core spine (ordered)

1. Title (`# Name`)
2. At a Glance (cue table: Role, Nature, Home, Wants; ends with DM thesis)
3. Spoken look (`[!narration]`; theatre of the mind)
4. Running the NPC (first move + posture change)
5. Relationships (wikilink + table meaning)

Optional italic epithet sits under the title and does not count as a heading.

## Stance and band

| Stance | Identity `role` | Bands |
|---|---|---|
| Potentially hostile | `rival` | Landmark (Hinewai), skirmish (Talon Skarn) |
| Friendly | `patron`, `contact` | Patron (Nona), contact (Thunk) |

Band is density, not a stored field. Infer it from which optional sections have content.

## Optional sections (ordered when present)

After Running the NPC, before Relationships:

- Extra form (own glance + spoken look)
- Unique lore (weakness place, practical use, public vs secret, limit)
- History
- Current pressure

After Relationships:

- Activity log
- Appearances
- Difficulty knobs
- Combat
- Extra art

Omit any section with no content. No empty heading.

## Combat

Present only if the NPC can enter a fight.

| Field | Rule |
|---|---|
| Encounter rule | One sentence. Required when Combat exists. |
| Sheet | On-page fight sheet **or** exactly one pointer to a `type: creature` sheet. Never both. |
| Stages | Landmark only. Keyed to a named condition the party can change, not walking-body hit points alone. |

## Spoken look

Player-safe sensory copy. Forbidden: secrets, difficulty classes, unearned names, DM thesis.

## Lifecycle

```text
proposed (chat Work) → accepted (wiki write allowed) → canon
                      → rejected (no page)
stub (named in approved ingest) → expanded on later accept
```

`type: npc` does not become `canon` until DM accept (existing Work gate).

## Relationships

| Field | Rule |
|---|---|
| target | Wikilink |
| meaning | What the tie does at the table |
| invitation | Optional. Patron rows MAY add one. |

Empty table forbidden. Omit the section only on a stub with no named ties.
