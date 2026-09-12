# Contract: Retrieval precedence

How a Co-DM agent uses default collections.

## Order

1. Search `-c wiki` (this project's compiled pages).
2. If silence, search `-c shattered-sea`.
3. If silence, search `-c legacy-ss`.
4. If still silence, say the wiki is silent. Do not invent a wiki fact.

## Hits

| Collection | Present as | May file to this wiki? |
|---|---|---|
| `wiki` | current canon | already here |
| `shattered-sea` | campaign-of-record context | only after DM accept |
| `legacy-ss` | older Campaign OS context | only after DM accept |

If `wiki` and a legacy collection disagree, cite `wiki`. Mention the legacy wording only as extra context.

## Failures

- `qmd` or index broken: run `scripts/qmd-maintain.sh`. If it still fails, read known wiki paths; report the failure; do not skip as unset.
- Legacy collection missing: search `wiki`; report the miss; continue prep.
- Unrevealed facts stay off the play surface.

## Invalid

Answering from snippets alone when a fact is needed (`qmd get` / `qmd multi-get` after search). Treating a legacy hit as a page in this wiki. Player-visible search output.
