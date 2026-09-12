# Data Model: Session Beat Format

Entities are wiki pages and one folder per planned night. No database.

## Session folder

Home for one planned session after ingest or accept.

| Field | Rule |
|---|---|
| Path | `wiki/journal/sessions/<campaign-slug>/<session-number>/` |
| Session 11 | `wiki/journal/sessions/shattered-sea/11/` |
| Contains | Spine, numbered live beat cards, that night’s companion notes only |
| Must not contain | Owner pages (place, creature, person, item) |
| Media | Embeds point at `wiki/attachments/…`; no second media dump |
| Staging | `_raw/` until ingest or accept; not the long-term home |

Two campaigns never share a session-number folder. A later session gets its own number folder beside Session 11.

## Session spine

Session-level chart the DM opens first. Evidence: `_raw/Session-11-00-Birds-of-a-Feather.md`.

| Field | Rule |
|---|---|
| `type` | `session-prep` |
| `campaign` | Required |
| `session` | Integer session number; matches folder name |
| `visibility` | Default `dm` |
| `status` | As used (`ready` when runnable) |
| `summary` | Optional one sentence |
| Filename | `Session-<N>-00-<Spine-Title>.md` |
| Jobs | Length, tone, prize, opposition, Hook/Climax/Resolution labels, dramatic spine, numbered skeleton with links to each live beat, per-beat purpose / table sees / truth / pressure / if they break / landing |
| Must not | Duplicate Scene ends when, Zones, or Be ready for |

Planning candidates may still live in `session-skeleton.md` during prep. The filed spine is the page in the session folder.

## Session beat card

One live slice (~30 minutes). Evidence: `_raw/Session-11-01-Angry-Birds.md` through `10`.

| Field | Rule |
|---|---|
| `type` | `session-prep` |
| `campaign` | Required |
| `session` | Matches spine and folder |
| `visibility` | Default `dm` |
| `tags` | Include `session-prep`; beat cards also use `run-guide` when that is the vault’s tag |
| `summary` | One sentence |
| Filename | `Session-<N>-<BB>-<Label>.md` with two-digit `<BB>` (`01` …) matching skeleton position |
| Cockpit jobs (order) | Identity; optional first-beat recap; overview art if it exists; Scene ends when + At a Glance; Now; Action cards; Initial Narration; Procedure + Secondary objective if a second question exists; Zones; Be ready for; Threat clock + dials if a fuse exists; How the Scene Resolves; Roster if combat-mode sheets will be rolled; Backup; Battlemap at bottom if art exists |
| Omit | Any job with no content this slice — no empty heading |

Beat identity: `<BB>` matches the spine skeleton; How the Scene Resolves hands to a beat on that skeleton.

### Glance

Stakes, goal or exit, danger, silence, situation magnets.

### Scene ends when

Stop condition, ~30-minute budget, behind/ahead cuts when pacing is not obvious.

### Spoken surfaces

Unconditional speech: open `[!narration]` (Initial Narration; How the Scene Resolves). Conditional speech: highlighted italic table cells. No secrets, DCs, or unearned names there. Only callout on the card is `[!narration]`.

## Companion note

Session-adjacent table or encounter list (e.g. hazards). Same session folder. Must not use a live beat number in the filename. Not scored against the cockpit. May keep `type: encounter`.

## Owner page

Canon page for a creature, place, item, or person. Lives outside the session folder. Beats wikilink or heading-embed. Default-mode action-card numbers the DM rolls this slice may sit on the beat. The beat is not a second owner page.

## Wiki-markdown shape

Columns, tables, open spoken callouts, highlighted conditional speech, wikilinks, image embeds, real line breaks, complete-sentence DM lines, at-table check/save grammar. Ingest copies these treatments; it does not compile them away.

## Work / lifecycle

Mutable prep until the DM accepts. Default `proposed` when the vault requires `lifecycle`. Rejected leaves no wiki page. Named ingest of approved sources may file stubs and the preserved session pages.

## Relationships

- Session folder 1—* spine (exactly one)
- Session folder 1—* beat cards (numbered)
- Session folder 0—* companion notes
- Spine 1—* beat cards (skeleton links)
- Beat card *—* owner pages (wikilink / embed)
- Beat card 1—1 next beat via How the Scene Resolves
- Ingest of session-prep → file in session folder, preserve body
- Ingest of ordinary knowledge → compile as today

## Out of model

Older session-prep not in the Session 11 production set. Recaps already in `wiki/journal/`. Foundry staging. Player-facing sheets.
