# Research: Wiki Bulk Operations

**Feature**: 023-wiki-bulk-ops | **Date**: 2026-09-17

## Decision 1: Single script vs. subcommand library

**Decision**: Single script with subcommands (`rename`, `replace`, `frontmatter`)

**Rationale**: The existing remorph scripts each handle one transformation type as standalone scripts. This works but forces agents to know N script names. A single entry point with subcommands (`wiki-bulk-ops rename ...`, `wiki-bulk-ops replace ...`, `wiki-bulk-ops frontmatter ...`) gives one tool to learn, one `--dry-run` / `--json` surface, and shared vault-traversal code — without needing a package or import structure. `argparse` subparsers handle this natively.

**Alternatives considered**:
- Separate scripts per operation (matches existing remorph pattern but multiplies agent tool knowledge)
- Python package with `__main__` (unnecessary structure for one file)

## Decision 2: Wikilink rewrite strategy

**Decision**: Regex-based, matching the proven `remorph-page-filename-kebab` patterns

**Rationale**: The existing `PATH_LINK` and `BARE_LINK` regexes in `remorph-page-filename-kebab` already handle path-qualified wikilinks, bare wikilinks, embeds, anchors, and piped display text. They are battle-tested on 1565 files. We reuse the same regex approach and patterns. A full markdown parser (e.g., `markdown-it`) would add a dependency, and regex is sufficient for the structural patterns Obsidian uses.

**Alternatives considered**:
- Full markdown AST parser (dependency, overkill for link target substitution)
- Line-by-line string replace (misses multi-line edge cases, less precise)

## Decision 3: Frontmatter handling

**Decision**: Regex extraction of the `---` fenced block, key-value manipulation with YAML-safe line-level edits

**Rationale**: The existing scripts use `FM_BLOCK = re.compile(r"\A---\n(.*?)\n---\n?", re.DOTALL)` to isolate frontmatter. For the bulk-ops tool, frontmatter mutations (add/update/rename/remove a field) operate on simple top-level scalar keys. The wiki's frontmatter is flat YAML (no nested objects beyond `tags: [...]` and `aliases: [...]` inline arrays). Line-level regex manipulation avoids a PyYAML dependency and avoids PyYAML's tendency to reformat YAML (reordering keys, changing quote style).

**Alternatives considered**:
- PyYAML / ruamel.yaml (external dependency; reformatting risk; overkill for flat key-value ops)
- Full AST roundtrip (would change formatting on every file touched)

## Decision 4: Safety zones for find-and-replace

**Decision**: Exclude YAML frontmatter and wikilink targets by default; opt-in flags to include them

**Rationale**: Per FR-002 and FR-006, body-text replacement must not break frontmatter or wikilinks. The safest default is to split each file into zones: frontmatter (between `---` delimiters), wikilink targets (inside `[[...]]` before `|` or `]]`), and body text. Replacements apply to body text only by default. `--include-frontmatter` and `--include-links` flags opt in to those zones when the agent explicitly intends it.

**Alternatives considered**:
- Replace everywhere with a post-validation check (risky; validation can't undo corruption mid-write)
- Exclude only frontmatter (wikilink corruption is the more common agent mistake)

## Decision 5: Atomicity and concurrency

**Decision**: Per-file atomic writes (write to tempfile in same directory, then `os.replace`); no cross-file locking

**Rationale**: Per spec edge case on concurrent operations: `os.replace` is atomic on POSIX. Writing to a tempfile first means a crash mid-operation leaves the original file intact. Cross-file locking is unnecessary — the wiki is single-writer (agents run sequentially per constitution XIV), and atomic per-file writes prevent partial corruption.

**Alternatives considered**:
- Write-in-place (crash = corrupted file)
- Global lock file (unnecessary given single-writer constraint)

## Decision 6: Output format

**Decision**: Default human-readable text summary; `--json` for machine-readable structured output

**Rationale**: Matches the existing remorph script pattern exactly. Agents parse `--json`; humans read the text summary. JSON output includes: `files_scanned`, `files_modified`, `files_skipped` (with reasons), and per-file `changes` arrays.

**Alternatives considered**:
- JSON only (harder for humans to spot-check)
- Diff format (harder for agents to parse programmatically)

## Decision 7: Exit codes

**Decision**: 0 = success (including "no changes needed"), 1 = validation/argument error, 2 = partial failure (some files skipped due to errors)

**Rationale**: Per FR-008. Matches Unix conventions. "No changes needed" is success (idempotency).

**Alternatives considered**:
- Distinct code for "no changes" (overcomplicates agent logic; idempotent ops should be silent success)

## Decision 8: Vault path resolution

**Decision**: `--vault PATH` argument, defaulting to `OBSIDIAN_VAULT_PATH` env var, falling back to `wiki/` relative to CWD

**Rationale**: Matches the existing remorph `--wiki`/`--vault` pattern and the config resolution protocol in AGENTS.md. Agents always run from repo root with the env var set.

**Alternatives considered**:
- Config file lookup (unnecessary indirection; env var is already resolved by the agent framework)
