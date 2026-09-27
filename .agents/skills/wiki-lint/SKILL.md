---
name: wiki-lint
description: >-
  Lint and repair wiki pages in a loop, one file at a time. Run wiki health,
  then on next.path: wiki lint fix, wiki lint, qmd query/search, qmd get, load
  the owner skill, close every finding, wiki lint until clean, wiki health
  again. A named page skips the first health and is that file. Use for vault
  health, page repair, audits, broken links, duplicate resolution, and
  cleanup.
---

# Wiki Lint

The operator is the agent. **This file only — then the next.** Run the
commands below in order. Substitute `FILE` with `next.path` (or the named
page). Flags: `wiki health --help`, `wiki lint --help`, `wiki lint fix --help`,
`wiki query --help`. QMD: `qmd query`, `qmd search`, `qmd get`.

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

Worklist for `FILE`. When dirty, the first lines are `skill:` and
`template:` — load that skill and that template before any edit. Then the
findings. Each `fix:` is an imperative; it does not repeat the template.
`--json` when you need the structured worklist
(`wiki lint entities/place/Belumara.md --json`).

```bash
wiki lint fix entities/place/Belumara.md
```

Deterministic repairs on `FILE` only. Bytes already on the page.

```bash
wiki query "Belumara" -n 5
env -u CI qmd query "Belumara" -n 5 -c wiki
qmd search "Belumara" -n 5 -c wiki
qmd get "<verbatim #docid or qmd:// source>" --format md
qmd multi-get "#abc123,#def456" --format md
```

Before any content write, search then fetch (AGENTS.md Vault retrieval).
`qmd query` is hybrid search; `qmd search` is keyword search when query cannot
run. Collection `wiki` (`-c wiki`). Copy a hit's `#docid` or `qmd://` source
verbatim into `qmd get`. Line range on the path:
`qmd get "<id>:1:20" --format md`. `wiki query` wraps `qmd query` and clears
`CI`; prefix `env -u CI` on direct `qmd query`. Named checks: `wiki-dedup`,
`cross-linker`, `tag-taxonomy`. Duplicate identity: [checks.md](checks.md)
Check 14.

Write on `FILE` from that context: resolve links to existing owner filenames;
set required frontmatter from `wiki/templates/` and retrieved facts; correct
type and filename; keep sections the template marks `Required.` and those with
facts. Place pages: named areas, connections, inhabitants or pressures, and
discoverable information
([Designing Fantastic Locations](https://slyflourish.com/designing_fantastic_locations.html);
[Prepping a Dungeon](https://slyflourish.com/prepping_a_dungeon.html)).

```bash
wiki lint entities/place/Belumara.md
```

Repeat until this command prints no findings. Commit `FILE`.

```bash
wiki health
```

`clean` → Done. Else `FILE` is the new `next:` path; go to `wiki lint` on
that file. Named page: skip; that file already clean is Done.

### Done

Unscoped: `wiki health` prints `clean`. Named page: `wiki lint <FILE>` prints
no findings. Every finding on every file this loop touched was closed.

### Capability Handoff

Follow the owner skill on this file yourself.
