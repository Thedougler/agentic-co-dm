# Quickstart: QMD Search Default

Proves search is on, this wiki wins, and maintenance is a command an agent can run.

## Prerequisites

- Branch `004-qmd-search-default`
- `qmd` on PATH
- Host agent in this repo root

## Story 1 — Default on

1. `scripts/qmd-maintain.sh` — expect exit 0 (or exit 1 with a rebuild error, not a silent skip).
2. Search `-c wiki` for `Hinewai` (or another filed entity). Expect a hit under this repo's `wiki/`.
3. A prep lookup of that name cites the wiki page without anyone exporting collection env vars in the session.

## Story 2 — Legacy then canon

1. Search a name that is thin here and fuller under `Documents/ai-co-dm/campaigns/shattered-sea`. Expect a `shattered-sea` hit marked campaign-of-record context, not as a page compiled here.
2. If both stores mention it, the canon answer cites `-c wiki`.

## Story 3 — Maintain after write

1. Change one sentence on a wiki entity (or ingest a page).
2. Run `scripts/qmd-maintain.sh` (ingest should call this; running it once is enough for the check).
3. Search `-c wiki` for a unique phrase from that sentence. Expect a hit.

## Pass

SC-001/005: no skip-if-unset. SC-002/003: legacy marked; wiki wins. SC-004/006: maintain script, no GUI. If sqlite ABI fails, that is a visible fail, not a pass.
