---
name: wiki-lint
description: >-
  Lint and repair one wiki page, then the next. wiki health names next:.
  That path is FILE. wiki lint FILE, Read the named skill and template if
  they are not already in context, wiki lint fix, wiki query related
  content named on the page then qmd multi-get, write every Required.
  section with the owner skill (create it if the wiki has none), wiki lint
  until FILE is clean, wiki health, next. A named page skips the first
  health and is FILE. Use for vault health, page repair, audits, broken
  links, duplicate resolution, and cleanup.
---

# Wiki Lint

The operator is the agent. Health prints `clean` or `next: <path>`. That
path is FILE. Close FILE. Health again.

A created page is FILE until `wiki lint` is clean, then health names
**next**. Named page skips the first health and is FILE. Run the commands
below in order. Flags: `wiki health --help`, `wiki lint --help`,
`wiki lint fix --help`, `wiki query --help`.

## Boundary

### Input

`FILE` is `next.path` from `wiki health`, or the path the user named. Explicit
"report only" / "don't fix" stops after step 1; every other lint job runs this
loop to Done.

### Work

```bash
wiki health
```

`clean` → Done. Otherwise `FILE` is the `next:` path. Named page: `FILE` is
that path; skip this command.

```bash
./scripts/qmd-maintain.sh
```

Once per sitting, after the first observe. Retry once on SQLite error.

```bash
wiki lint entities/place/Belumara.md
```

Worklist for `FILE`. When dirty, the first two lines name a skill and a
template. Read each that is not already in this context, then the findings.
`--json` when you need the structured worklist
(`wiki lint entities/place/Belumara.md --json`).

```bash
wiki lint fix entities/place/Belumara.md
```

Deterministic repairs on `FILE` only. Bytes already on the page.

```bash
wiki query "The Passage"
```

Once, before a content write. FILE is already in hand. Query every name it
mentions that the write needs — supporting, collaborating, related. Fetch
all those hits in one `qmd multi-get`. Identifiers come from the query
(AGENTS.md Exact QMD retrieval). `--format md`.

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

If `multi-get` rejects an identifier, serial `qmd get` immediately. Hits
still thin: `wiki-query` / `wiki-context-pack`. Formatting and labels are
already on the skill and template. Named checks: `wiki-dedup`,
`cross-linker`, `tag-taxonomy`. Duplicate identity: [checks.md](checks.md)
Check 14.

Write on `FILE` with the loaded owner skill: resolve links to existing owner
filenames; set required frontmatter from `wiki/templates/` and retrieved
facts; correct type and filename; write every template `Required.` section
as finished table-ready content before the next lint. Search first; if the
wiki has no such content, the owner skill creates it on the live path now
(Shea: "When you need a monster and don't have one handy, use the stat block
for a bear and you'll probably be ok."
[Just Use Bears](https://slyflourish.com/just_use_bears.html) — here that
finished block is the owner skill's output). Place pages: named areas,
connections, inhabitants or pressures, and discoverable information
([Designing Fantastic Locations](https://slyflourish.com/designing_fantastic_locations.html);
[Prepping a Dungeon](https://slyflourish.com/prepping_a_dungeon.html)).

```bash
wiki lint entities/place/Belumara.md
```

Repeat until this command prints no findings. Commit `FILE`. If this pass
created another page, that page is `FILE` now: Read its skill and template
if they are not already in this context, run its owner skill to the skill's
Done, `wiki lint` until clean, commit. Then:

```bash
wiki health
```

`clean` → Done. Else `FILE` is the new `next:` path; go to `wiki lint` on
that file. Named page: skip; that file already clean is Done.

### Done

Unscoped: `wiki health` prints `clean`. Named page: `wiki lint <FILE>` prints
no findings. Every finding on every file this loop touched was closed. Every
`Required.` section on those files is finished table-ready content from the
owner skill. A created page that is lint-clean is not Done while health
still names a `next:` path.

### Capability Handoff

Follow the owner skill on this file yourself. An empty `Required.` section
is that skill's work, done before this loop leaves the file. A stub is not
a response.
