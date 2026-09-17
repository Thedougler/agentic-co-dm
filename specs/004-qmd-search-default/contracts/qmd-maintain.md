# Contract: qmd-maintain

Agent-shaped maintenance for the project search index.

## Invoke

```text
scripts/qmd-maintain.sh
```

Cwd: repository root. No flags required for the default path.
Use `scripts/qmd-maintain.sh --embed` only when a foreground embedding pass is
explicitly requested. Optional `--max-embed-docs N` and `--max-embed-mb N`
select the supported QMD batch caps and imply `--embed`.

## Done

Exit 0 when:

1. Project `.qmd/` exists.
2. Collections `wiki`, `shattered-sea`, and `legacy-ss` are present.
3. `qmd update` has run.
4. `qmd status` succeeds. Pending vectors are reported as embedding backlog; they do not fail routine maintenance.
5. A search `-c wiki` for a page that exists under `wiki/` returns that page.
6. With `--embed`, the explicit batch pass succeeds and the refreshed status reports the remaining backlog.

Stdout: short status (index path, collection names, last update, and either
`embeddings: current` or a numeric pending backlog). The script unsets `CI`
before every `qmd` call because qmd disables local LLM (embed/query) when
`CI=true`.

## Failed

Exit 1 when `qmd` is missing, sqlite ABI load fails, a required collection cannot be added, update/status fails, the explicit `--embed` pass fails, or the probe search misses.

Stderr: one line the agent can show the DM. Do not skip search as "unset."

## Invalid

GUI; writing wiki pages; modifying campaign-of-record files; indexing `inbox`/`docs`/`skills`.
