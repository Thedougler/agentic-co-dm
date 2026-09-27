---
name: wiki-lint
description: >-
  Lint and repair wiki pages. Unscoped vault health starts at wiki health
  (counts + next dirty page); a named page starts at wiki lint. Sweep once
  with wiki lint fix, refresh QMD, then repair next.path until that file is
  clean and repeat. Read linked canon with wiki query then qmd get. Use for
  vault health, page repair, audits, broken links, duplicate resolution, and
  cleanup.
---

# Wiki Lint

The operator is the agent. **Health orients, lint lists, QMD reads.** After each page, re-observe.

`wiki health --help`, `wiki lint --help`, `wiki lint fix --help`, `wiki query --help`.

## Boundary

### Input

Accept a whole-vault or page/prefix scope plus the user's repair or report
intent. Resolve the existing CLI scope and owner contract before editing.
Preserve that scope through every observation, repair, and rerun.

### Work

One loop. Copy the invocations; flags stay in `--help`.

**Observe.** Unscoped vault health or "repair the wiki" starts here:

```bash
wiki health
wiki health --json
```

Text is counts plus `next:` and a copy-paste action. `--json` when you need
`next.path`, `lint.counts`, ordered `focus`, or `context.act`. Follow
`context.act`, then `next.path`, then `focus`. A named page skips vault health
and starts at `wiki lint <path>`. A request for every finding uses `wiki lint`
for that scope (`--json` for the worklist). `wiki health` already ran lint;
open the worklist only for `next.path`.

**Sweep once** for a repair job (not report-only):

```bash
wiki lint fix
wiki lint fix entities/place/Belumara.md
```

One `wiki lint fix` for the resolved scope. It only transforms bytes already
on the page. Then refresh the search index:

```bash
scripts/qmd-maintain.sh
```

Retry once on SQLite error. `--embed` only when someone asks for a foreground
embedding pass (`scripts/qmd-maintain.sh --help`). If `qmd status` failed at
the start of an unscoped job, this is that repair too.

**Repair `next.path`.** One file until its lint is clean.

```bash
wiki lint entities/place/Belumara.md
wiki lint entities/place/Belumara.md --json
```

Remaining findings are agent repairs (`fix:` is an imperative sentence). Read
the page at the lint `file:line`, then resolve identity and linked canon
through QMD — search, then fetch the returned identifier verbatim (AGENTS.md
Vault retrieval):

```bash
wiki query "Belumara" -n 5
qmd get "<verbatim #docid or qmd:// source>" --format md
```

Append `:start:end` to the verbatim source (`qmd get "<id>:1:20" --format md`).
Several hits: `qmd multi-get "#abc123,#def456" --format md`. `wiki query`
already clears `CI`; prefix `env -u CI` only when you call `qmd query` /
`qmd vsearch` / `qmd embed` directly.

On this file, close every finding: resolve links to existing owner filenames;
set required frontmatter from `wiki/templates/` and page facts; correct type
and filename; keep sections the template marks `Required.` and those with
facts; load the owner skill when a section needs domain content; ground novel
non-plot content with `wiki-query` and `wiki-context-pack`. Plot only when the
user asks. Place pages: named areas, connections, inhabitants or pressures,
and discoverable information
([Designing Fantastic Locations](https://slyflourish.com/designing_fantastic_locations.html);
[Prepping a Dungeon](https://slyflourish.com/prepping_a_dungeon.html)).

Rerun that same `wiki lint <path>` until clean.

Clean → commit that path. Unscoped: `wiki health` again and take the new
`next.path`. Named page: stop when that path is clean.

Keep one active writer per page. After an owner returns, rerun lint on the
affected scope.

Treat the lint profile, `wiki/templates/`, the template contract, and the
owner skill as one output contract. If those sources disagree, reconcile them
before mass repair. A clean structural result is not done when a D&D job on
the page is empty.

### Done

Close only when the affected scope is clean on a fresh observe (`wiki health`
unscoped, `wiki lint <path>` when named). If a finding cannot close, report
path, rule, evidence, and owner. Preserve the full-finding and fixer CLI
contracts.

### Capability Handoff

Semantic page findings → owner skill (`faction-design`, `place-design`,
`npc-design`, …) with page, linked canon, template, and lint evidence.
`wiki-dedup`, `cross-linker`, `tag-taxonomy` only for their named findings.
Duplicate identity procedure: [checks.md](checks.md) Check 14.

One done-summary: what changed, where.
