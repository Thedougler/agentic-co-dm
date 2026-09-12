---
paths:
  - "utils/scripts/**"
---
Which hooks/lint rules are live is read from `.claude/settings.json` +
`.obsidian-linter.jsonc`, never from any doc.

Adding or editing a lint rule -> add a Python module under
`utils/wiki-cli/src/wiki_cli/rules/` (auto-discovered via `pkgutil`).

Writing a per-file hook -> read the edited path from the **stdin JSON
payload** (`tool_input.file_path`), never `"$CLAUDE_FILE_PATHS"` — that env
var is unset in current Claude Code, so a hook passing it lints nothing
(empty string -> no paths -> exit 0). Env vars never work as hook escape
hatches either: a spawned hook process doesn't inherit mid-session exports,
so `export FOO=1` silently never takes effect — use a file flag or explicit
argv. Hooks hot-reload on a `.claude/settings.json` edit; no restart needed.

Canon discipline (CLAUDE.md rules 3/9) holds by convention, not a hook —
see `transcript-ingest` and `canon-review`'s own SKILL.md contracts.
