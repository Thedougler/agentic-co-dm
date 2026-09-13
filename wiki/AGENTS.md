# Campaign wiki

Owner conventions for this vault. Load before every write to `wiki/`. Overrides llm-wiki defaults for campaign pages.

## Prose

Write **complete-sentence human prose**. A DM reads this without decoding agent shorthand. Telegram stubs, slash-stacks, and AI note-speak are invalid (FR-018).

Classify each write against the stack table in `AGENTS.md`. Vault is `true` on wiki vault notes. Mixed documents classify per passage, then apply vault format to the whole note.

Spoken player text is `[!narration]` only.

## Frontmatter

Required on every page: `title`, `category`, `tags`, `sources`, `created`, `updated`.

Campaign pages also require:

| Field | Values |
|---|---|
| `type` | `npc` \| `place` \| `faction` \| `item` \| `creature` \| `vehicle` \| `spell` \| `lore` \| `quest` \| `region` \| `session-prep` \| `session` \| `recap` \| `work` |
| `lifecycle` | `draft` \| `proposed` \| `accepted` \| `rejected` \| `canon` |
| `reveal` | `unrevealed` \| `revealed` |

Do not invent `type` values. Category is the llm-wiki folder (`entities/`, `journal/`, …). `type` is the campaign kind.
Map early sample labels on file: `location`→`place`, `monster`→`creature`. World-truth notes use `type: lore`. Actual items stay `item`. Campaign situation pages use `type: quest`.
`lifecycle` defaults to `proposed` until the DM accepts. `visibility` defaults to `dm` and is distinct from `reveal`. `summary` is one sentence a DM can read in a list. Omit unused identity keys.


Work pages also set `grounded_in` and `invention` — see `docs/agents/work.md`.

Done when: required fields are present, body is complete sentences, related pages are `[[wikilinked]]`.

## Layout

Copy `wiki/templates/` as a scaffold for the campaign `type`. Omit empty sections. Pass is run jobs, not heading-order match.

`wiki/_raw/` illustrates quality. It is not a clone target. Incoming ingest files are evidence of facts, not exemplary format. Filed pages are judged against the kinds and jobs in this file.

| Kind | Jobs |
|---|---|
| Place | Look; situation now; moves that change the scene; presence or sign of absence; table objects; connections; purpose |
| Consumable | Portrait; classification; one runnable effect; then stop |
| Flora hazard | Look; start; notice; contact cost; careful passage; honest counterplay |
| Creature | Look; runnable sheet; life (habitat, habits, diet, social); hunt (signs, instincts, opening, shut-down, aftermath) |
| Person | Who and want; look; first minutes and posture change; named ties; combat only if they can fight |
| Session beat | Cockpit jobs: `.agents/skills/run-guide/SKILL.md`. Evidence `wiki/_raw/Session-11-01-Angry-Birds.md`–`10`. Omit empty. |
| Session spine | Filed spine: `.agents/skills/session-beats/SKILL.md`. Evidence `wiki/_raw/Session-11-00-Birds-of-a-Feather.md`. |
| Vehicle | Look; sheet; components; crew stations; handling; combat. Pass is those jobs. |
| Spell | Look of the casting; classification; runnable 2024 effect; Discovery when placement needed; Lore when history needed. Pass is those jobs. |
| Faction | Public face; DM thesis; current state; one active agenda; table-relevant assets, people, places, and relationships; faction-turn log. Pass is those jobs. |
| Lore | One durable question; At a Glance (core truth + why it matters); Current Truth; At the Table (notice / explains / enables / warns). Pass is those jobs. |
| Quest | Summary (objective, why now, deadline); Situation; Stakes including walk-away; World in motion (driver and next move if uninterrupted); at least two independent leads. Resolution omitted while unresolved. Pass is those jobs. |
| City | Arrival; At a glance including current pressure; Orientation (districts and getting around); Gazetteer enough to intentionally seek a place; rules that matter at the table; at least one active situation with if-nobody-intervenes. Page is `type: place` with `kind: city`. Site places keep using `wiki/templates/place.md` and existing Place jobs. Pass is those jobs. |
| Region | Spoken look; At a glance; Current state; geography/travel enough to choose a route; active powers; change log. Pass is those jobs. |

Spoken look is theatre of the mind: no secrets, DCs, unearned names, author thesis.

Ingest of campaign-shaped `type: place` keeps required treatments (including `[!narration]`); it does not distill. Foreign sources map into the kind. Session-prep stays its own kind.

Numbers live on one owner page. Other sample pages wikilink; they do not copy the effect, save, or sheet.

Consumable and flora hazard both use `type: item`; they differ by jobs.

Legacy pages are out of scope. Wrapup MUST NOT convert a legacy page into a sample.

Done when: the kind's jobs are answered, empty sections are omitted, spoken look is player-safe.

Session home after ingest or accept: `wiki/journal/sessions/<campaign-slug>/<session-number>/` (Session 11 → `wiki/journal/sessions/shattered-sea/11/`). Spine, numbered beat cards, and that night’s companion notes only. Owner pages stay outside. `_raw/` is staging. Two campaigns do not share a session-number folder. `session` remains the post-play log, not a map of `session-prep`.


## Approval (FR-019)

Do not create or change a campaign wiki page until the DM approves.

Exceptions: named ingest of approved sources, and thin complete-sentence stubs for names those sources contain (including as links). Invented names not in the source are Work — chat proposal first.

Rejected proposals leave no page. Wiki facts change only after accept.
