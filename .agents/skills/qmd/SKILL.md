---
name: qmd
description: >-
  Search and fetch indexed markdown with qmd. Use when retrieving wiki notes,
  fetching documents after search, or answering from local markdown. Search
  first; qmd multi-get every related hit before citing.
license: MIT
compatibility: Requires qmd CLI.
allowed-tools: Bash(qmd:*), mcp__qmd__*
---

# QMD

Search first. Fetch every related hit in one `qmd multi-get`. Answer from
retrieved text, not snippets. `qmd --help`. Collection `wiki` when
`QMD_WIKI_COLLECTION` is empty. Prefix `env -u CI` for `qmd query` /
`qmd vsearch` / `qmd embed`.

## Fetch

Identifiers come from the search result: the `#docid` or the source string.
Do not construct, URL-encode, or infer a path from an Obsidian filename.

```bash
# CORRECT — comma-separated #docid values from search results
qmd multi-get "#abc123,#def456" --format md

# CORRECT — brace-expanded paths
qmd multi-get 'entities/faction/{the-passage.md,antheri.md}' --format md

# WRONG — qmd:// URIs (rejected with "File not found")
qmd multi-get "qmd://entities/faction/the-passage.md,qmd://entities/faction/antheri.md"
```

One hit: `qmd get` with that same identifier. Line range goes on the path:

```bash
# CORRECT
qmd get "qmd://entities/faction/the-passage.md:1:20" --format md

# WRONG — CLI rejects md:1:20
qmd get "qmd://entities/faction/the-passage.md" --format md:1:20
```

If `multi-get` rejects an identifier, serial `qmd get` immediately. Do not
retry with a different format.

Done when every related hit you will cite or write from is in the fetch
output, or the wiki is silent.
