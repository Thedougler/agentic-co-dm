---
name: memory-bridge
description: >
  Browse and compare wiki knowledge by which AI tool originally produced it. Use this skill when the user
  says "/memory-bridge", "browse codex memory", "what did codex know about X", "show me claude knowledge",
  "cross-tool memory", "what does hermes know that claude doesn't", "show me knowledge from <tool>",
  "compare my AI tool memories", or wants to explore knowledge gaps between tools. Works from any project.
  Diff mode ("what's different", "unique to codex", "gaps between tools") is the killer feature — it surfaces
  blind spots between tools that the user may not know exist.
---

# Memory Bridge — Cross-Tool Knowledge Browser

You are helping the user browse and compare their Obsidian wiki knowledge filtered by which AI tool originally produced it. The wiki tracks source provenance in `.manifest.json` and page `sources:` frontmatter — this skill surfaces that metadata as a navigable view.
## Capability Boundary

**Accepted input.** A recognized source tool, optional topic, `diff` pair, or `map` request, plus the resolved vault profile.

**Owner work.** Enter `memory-bridge` directly, build a capped tool-to-page map through `manifest.py` projections, inspect only the frontmatter or focused matching sections required by the selected mode, and report provenance asymmetries with the existing counts and link format.

**Done.** Complete only with a provenance-grounded browse, search, diff, or map result whose page counts and cited links are sufficient for the requested mode. Do not mutate canonical pages, index, manifest, or other wiki knowledge; the specified `MEMORY-BRIDGE` log append is the only side effect.

**Capability handoff.** Handoff occurs only when ownership changes: route a requested content edit or ingest to `wiki-capture`/`wiki-update`, or a compiled-knowledge question to `wiki-query`; do not add a generic coordinator.


## Before You Start

1. **Resolve config** — follow the Config Resolution Protocol in AGENTS.md (inline `@name` override → walk up CWD for `.env` → `~/.obsidian-wiki/config` → prompt setup). This gives `OBSIDIAN_VAULT_PATH`.
2. Provenance lives in the ingest ledger — query via `python3 scripts/manifest.py` (`stats` / `tool-pages [--tool|--limit]` / `list --limit` / `get` / `lookup`); do **not** load whole `.manifest.json` into context (S1).
3. Read `$OBSIDIAN_VAULT_PATH/index.md` for page titles and one-line descriptions.

## Commands

Parse the user's invocation to determine mode:

| Invocation | Mode |
|---|---|
| `/memory-bridge <tool>` | **Browse** — list all wiki pages sourced from `<tool>` |
| `/memory-bridge <tool> "<topic>"` | **Search** — pages from `<tool>` that mention `<topic>` |
| `/memory-bridge diff` | **Diff** — pages unique to each tool; overlap; blind spots |
| `/memory-bridge diff <tool-a> <tool-b>` | **Diff** — compare two specific tools |
| `/memory-bridge map` | **Map** — full origin matrix: every page × every tool that touched it |

Recognized tool names: `claude`, `codex`, `hermes`, `openclaw`, `copilot`, `pi`, `manual` (hand-written), `ingest` (wiki-ingest documents).

## Step 1: Build the Source Map

**HARD (context-waste S1):** Never Read, open, or paste whole `.manifest.json` into agent context. Full-file ledger ingest is a bug. The CLI may open the file on disk; you only consume capped command output.

1. `python3 scripts/manifest.py stats "$OBSIDIAN_VAULT_PATH"` — counts only.
2. Build the tool→page map with the thin projector (preferred):
   ```bash
   python3 scripts/manifest.py --format tsv tool-pages "$OBSIDIAN_VAULT_PATH" [--tool <name>] [--limit N]
   ```
   Output is `tool\tpage` only (tools already mapped from `source_type`). Cap with `--limit` when browsing; raise the cap only if the mode needs it, still never dump the raw ledger.
3. Fallback for one source key: `get` / `lookup --page` — still one entry, not the whole file. `list --limit N` may include `source_type` but does **not** expand page paths; prefer `tool-pages` for this skill.

Build:

```
tool_pages = {
  "claude": set(pages from tool-pages rows),
  "codex":  set(...),
  ...
}
```

A page can appear in multiple tools' sets if multiple tools contributed to it.

## Step 2: Execute the Mode

### Browse Mode

Filter `tool_pages[<tool>]` and present as a grouped list:

```
## Knowledge from <tool> (<N> pages)

### By category
- concepts/ — N pages
- entities/ — N pages
- skills/   — N pages
...

### Pages
| Page | Category | Tags | Last updated |
|------|----------|------|--------------|
| [[page-name]] | concept | tag1, tag2 | 2026-04-10 |
...
```

Read frontmatter for the listed pages (grep for `^(title|category|tags|updated):`) — do not read full page bodies unless the user asks.

### Search Mode

Within the filtered page set, run:
```
rg -l "<topic>" <pages in tool set>
```
Then grep section headers (`^##`) around matches to give context without full reads. Present results as a ranked list with the matching excerpt.

### Diff Mode

Compute:
- `only_in_a` = `tool_pages[a]` − `tool_pages[b]`
- `only_in_b` = `tool_pages[b]` − `tool_pages[a]`
- `shared` = `tool_pages[a]` ∩ `tool_pages[b]`

If no specific tools are given, compare all tools pairwise (limit to pairs with >0 overlap or unique pages to keep output concise).

Present:

```
## Memory Bridge Diff — <tool-a> vs <tool-b>

### Only in <tool-a> (<N> pages)
These concepts exist in your wiki from <tool-a> sessions but <tool-b> has never touched them.
<list with one-line descriptions from index.md>

### Only in <tool-b> (<N> pages)
<list>

### Shared (<N> pages)
Both tools have contributed to these pages.
<list — only show if ≤15; otherwise just the count>

### Notable gaps
<highlight the most interesting asymmetries — e.g. "codex has 12 pages on build tooling that claude has never seen">
```

### Map Mode

Build a matrix from `tool-pages` rows (not a raw ledger dump). Cap at 50 rows; sort by number of contributing tools descending (most cross-tool pages first — these are the richest nodes).

```
| Page | claude | codex | hermes | copilot | pi |
|------|--------|-------|--------|---------|----|
| [[react-patterns]] | ✓ | ✓ | — | ✓ | — |
| [[rust-ownership]] | — | ✓ | — | — | ✓ |
```

## Step 3: Spawn impl-validator (if available)

After generating output, if the `impl-validator` skill is available in the current environment, spawn it as a subagent:

```
impl-validator check:
  goal: "Browse/diff wiki knowledge by source tool and surface cross-tool blind spots"
  artifacts: [the output you just generated]
  checks:
    - Did tool→page rows come from `manifest.py tool-pages` (or capped `list`/`get`) — never a full `.manifest.json` load into context?
    - Are page counts plausible (not 0 unless vault is empty / stats say empty)?
    - Is the diff symmetric (a−b and b−a are disjoint)?
    - Did you avoid reading full page bodies when not needed?
```

Apply any issues it surfaces before presenting output to the user.

## Step 4: Log

Append to `$OBSIDIAN_VAULT_PATH/log.md`:
```
- [TIMESTAMP] MEMORY-BRIDGE mode=<browse|search|diff|map> tool=<tool> pages_shown=N
```

## Output Conventions

- Always show page counts so the user can calibrate how much knowledge is in each tool's silo.
- Use `[[wikilinks]]` for page references (or standard Markdown links if `OBSIDIAN_LINK_FORMAT=markdown` is set).
- In diff mode, call out the most *surprising* asymmetry explicitly — that's the insight the user came for.
- If `manifest.py stats` shows empty/missing ledger, say so clearly and suggest ingesting with `wiki-agent` first. Do not open `.manifest.json` to check.
