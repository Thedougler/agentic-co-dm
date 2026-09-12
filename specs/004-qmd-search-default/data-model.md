# Data Model: QMD Search Default

## Search index

Derived retrieval layer over markdown collections. Not canon.

| Field | Rule |
|---|---|
| location | Project `.qmd/` after `qmd init` in this repo |
| sqlite | Gitignored |
| collection list | Tracked `.qmd/index.yml` |
| source of truth | Wiki pages, not the index |

Validation: `qmd status` from repo root names the three collections. A search `-c wiki` can return a compiled page.

## Collection

| Name | Path | Default query | Canon? |
|---|---|---|---|
| `wiki` | this repo `wiki/` | yes | yes — compiled pages here |
| `shattered-sea` | `Documents/ai-co-dm/campaigns/shattered-sea` | after `wiki` silence | no — campaign of record |
| `legacy-ss` | `/Users/nick/shattered-sea/wiki/shattered-sea` | after `shattered-sea` silence | no — older Campaign OS |

Validation: names are exact. `inbox` / `docs` / `skills` from ai-co-dm are not on this index.

## Retrieval result

| Field | Rule |
|---|---|
| collection | `wiki` \| `shattered-sea` \| `legacy-ss` |
| path | File in that collection |
| role | `canon` if `wiki`; else `legacy-context` |
| player-visible | never, unless DM accepts a reveal |

## Maintenance run

| Field | Rule |
|---|---|
| trigger | After wiki write; or session start when status fails |
| steps | ensure index + collections → update → embed if needed → status |
| ok | exit 0; known wiki page findable |
| fail | exit 1; stderr; agents still read known wiki files |

## State

```text
index: absent → inited → collections-present → updated → searchable
search: wiki-hit (canon) | legacy-hit (context) | silence
legacy unreachable → wiki-only + reported miss
```
