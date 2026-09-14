# Wiki staging (`_staging/`)

LLM-proposed wiki pages land here when `WIKI_STAGED_WRITES=true` so Nick can review before they hit the live vault.

## Procedure (agents)

1. **Write** new/updated category pages to `wiki/_staging/<category>/…` (or `.patch.md` beside existing targets) — **not** straight into live `entities/` / `journal/` / etc.
2. Tell Nick pages are waiting in `_staging/`.
3. Nick reviews with **`wiki-stage-commit`** (`/wiki-stage-commit`, “promote staged pages”, “what’s waiting in staging”).
4. Accepted → final vault path. Rejected → back toward `_raw/` for edit (per skill).
5. `_staging/` is **not** the same as `_raw/` (ingest inbox) or `_archive/` (promoted sources).

Empty `_staging/` (aside from this README) means nothing is waiting.
