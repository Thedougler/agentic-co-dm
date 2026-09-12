# Campaign wiki

Owner conventions for this vault. Load before every write to `wiki/`. Overrides llm-wiki defaults for campaign pages.

## Prose

Write **complete-sentence human prose**. A DM reads this without decoding agent shorthand. Telegram stubs, slash-stacks, and AI note-speak are invalid (FR-018).

Load `copy-writer` and `obsidian-markdown` on every `.md` write.

Spoken player text is `[!narration]` only.

## Frontmatter

Required on every page: `title`, `category`, `tags`, `sources`, `created`, `updated`.

Campaign pages also require:

| Field | Values |
|---|---|
| `type` | `npc` \| `place` \| `faction` \| `item` \| `creature` \| `session` \| `recap` \| `work` |
| `lifecycle` | `draft` \| `proposed` \| `accepted` \| `rejected` \| `canon` |
| `reveal` | `unrevealed` \| `revealed` |

Do not invent `type` values. Category is the llm-wiki folder (`entities/`, `journal/`, …). `type` is the campaign kind.

Work pages also set `grounded_in` and `invention` — see `docs/agents/work.md`.

Done when: required fields are present, body is complete sentences, related pages are `[[wikilinked]]`.

## Layout

Copy `wiki/templates/` for the campaign `type`. Early-dev samples in `wiki/_raw/` are the layout source for those templates.

| Sample `type` | Campaign `type` | Template |
|---|---|---|
| location | `place` | `wiki/templates/place.md` |
| item (consumable) | `item` | `wiki/templates/item.md` |
| lore (flora hazard) | `item` | `wiki/templates/hazard.md` |
| monster | `creature` | `wiki/templates/creature.md` (linear; no `col` wrappers) |
| Hinewai, Talon Skarn, Nona Black-Jaw, Thunk | `npc` | `wiki/templates/npc.md` (two-pane `col` for Glance+look and Running; creature notes stay linear) |

Done when: the filed note matches the template headings in that order.


## Approval (FR-019)

Do not create or change a campaign wiki page until the DM approves.

Exceptions: named ingest of approved sources, and thin complete-sentence stubs for names those sources contain (including as links). Invented names not in the source are Work — chat proposal first.

Rejected proposals leave no page. Wiki facts change only after accept.
