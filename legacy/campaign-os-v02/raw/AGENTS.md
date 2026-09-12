## Project — raw/

`raw/` holds ingested files, read only, organized into subdirectories by
month -> never edit a file here.

Exception (migration mode only — a source handed in from outside `inbox/`,
e.g. `~/ai-os/shattered-sea/`): the `llm-wiki-ingest` skill owns
`raw/<YYYY-MM>/<source-slug>.md` (its per-source batch queue, live until
that source's ingestion is fully checked off) and `raw/INGESTED.tsv` (the
undated, append-only dedupe manifest) -> `llm-wiki-ingest` may create and
append to these; nothing else may edit them.

Anything archived via the `inbox/` flow instead uses `npm run inbox:archive`
(see `inbox/CLAUDE.md`) — no exception needed here for that path, and no
ledger anywhere: which vault/ page(s) a given archived file produced is
derived on demand from that page's own `source: "raw/<YYYY-MM>/<name>"`
frontmatter (`grep -rh '^source:' vault/` against `raw/`'s contents), never
stored separately. Redoing an ingest, or checking one for mistakes, is
running that grep and comparing it against `ls raw/**` — no state file to
go stale.

Every other file under `raw/` stays read only.

Moving a file into `raw/` (e.g. after ingestion) -> place it under
`raw/YYYY-MM/` for the current year and month (create the subdirectory if
it doesn't exist yet), never directly in `raw/`.
