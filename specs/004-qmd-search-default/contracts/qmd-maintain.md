# Contract: qmd-maintain

Agent-shaped maintenance for the project search index.

## Invoke

```text
scripts/qmd-maintain.sh
```

Cwd: repository root. No flags required for the default path.

## Done

Exit 0 when:

1. Project `.qmd/` exists.
2. Collections `wiki`, `shattered-sea`, and `legacy-ss` are present.
3. `qmd update` has run.
4. Embeddings exist or `qmd embed` has been attempted and succeeded. The script unsets `CI` before every `qmd` call because qmd disables local LLM (embed/query) when `CI=true`.
5. `qmd status` succeeds.
6. A search `-c wiki` for a page that exists under `wiki/` returns that page.

Stdout: short status (index path, collection names, last update).

## Failed

Exit 1 when `qmd` is missing, sqlite ABI load fails, a required collection cannot be added, update/embed/status fails, or the probe search misses.

Stderr: one line the agent can show the DM. Do not skip search as "unset."

## Invalid

GUI; writing wiki pages; modifying campaign-of-record files; indexing `inbox`/`docs`/`skills`.
