# utils/scripts/

One-line entry per script. Keep alphabetical within each section.

## Hooks (wired in .claude/settings.json)

- `inbox_to_md_sweep.sh` — SessionStart; converts new Inbox/ drops to markdown; silent when nothing new.
- `qmd_session_update.sh` — SessionStart; refreshes the qmd search index/embeddings.
- `session_health.sh` — SessionStart; prints the cached ≤2-line lint summary (background refresh: `npm run lint:sweep` → `wiki debt accept` → summary), fix-on-discovery pending count, and stale-dirty-tree warning; silent when clean.

## Lint / debt

Lint is `utils/wiki-cli/` (Python, [ADR-0045](../../docs/adr/0045-wiki-cli-cutover-complete.md)).
All `npm run lint*` scripts delegate to `uv run --directory utils/wiki-cli wiki <command>`:
`lint` for a scoped path, `sweep` for the corpus, `drain` for the debt queue
([ADR-0064](../../docs/adr/0064-lint-output-is-an-instruction-list.md)).
`wiki drain --over` lists every (file, rule) pair above its floor
([ADR-0062](../../docs/adr/0062-lint-baseline-is-a-suppression-list.md)).

- `lib/prose-scope.mjs` — shared scope/exclude + frontmatter/fence/comment stripping + `runToFile` (still used by non-lint scripts).

### Lint caches

| Cache | Owner | Key | Holds |
|---|---|---|---|
| `.wiki-cli/cache.sqlite3` | wiki-cli | per-file content hash | Rule findings + corpus index |
| `.claude/.lint-sweep.summary` | `session_health.sh` | — | Cached SessionStart lint summary text |

## Pipeline / tools

- `build_site.sh` — Phase 6 publish step; strips `## DM Only` + `%%...%%` from a staging copy of `publish: true` pages, builds the player site with Quartz (`utils/site/`).
- `count-lines.mjs` — line counts for wiki pages (npm: `count:lines`).
- `inbox/` — Inbox toolchain: `check`, `archive`, `similar`, `to-markdown`, `sweep-to-markdown` (npm: `inbox:*`).
- `migrate-statblocks.mjs` — one-shot statblock-format migration helper.
- `obsidian-buttons/` — the Obsidian button system's scripts (`vault/.claude/skills/obsidian-metabind/references/button-actions.md` documents the buttons).
