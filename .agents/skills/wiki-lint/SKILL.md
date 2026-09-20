---
name: wiki-lint
description: >-
  Lint and repair wiki pages — template conformance, content completeness,
  broken links, frontmatter, type/lifecycle validity, filename shape, and
  duplicate resolution. Use for vault health, page repair, audits, broken
  links, duplicate resolution, and cleanup. A bare page path repairs that page;
  no path repairs the vault; --check reports without writes; --consolidate runs
  the same repair loop with its confirmation rules.
---

# Wiki Lint

File what constitution X makes canon. Follow `docs/agents/work.md`.

## Method

Linting is one loop:

1. Resolve config, form the effective schema, and read `hot.md`.
2. Run `wiki lint [path ...]`.
3. Select `next.path`; run `wiki lint <path> --full`.
4. Read the page through QMD, then read its linked canon.
5. Resolve identity before editing.
6. Repair every finding:
   - resolve links against existing owner filenames;
   - add required frontmatter;
   - correct type, lifecycle, and filename;
   - apply the page template and complete every required section;
   - load the page's owner skill when a section needs domain content;
   - create plot only when the user explicitly asks or instructs it; otherwise
     defer plot creation and continue every non-plot repair;
   - when repair needs novel non-plot content or invention, first ground the
     work in established wiki fact with `wiki-query` and `wiki-context-pack`,
   - ground all content in canon and record gaps or proposals as the owner skill
     requires.
An empty required section is a finding. A sparse page is not repaired until it
contains substantive, actionable content for every non-plot template job. Plot
work is inactive unless the user asks for it; skip it and keep processing all
other findings.
For place pages, use Michael E. Shea's playable-location baseline: named areas,
connections, inhabitants or pressures, and discoverable information
([Designing Fantastic Locations](https://slyflourish.com/designing_fantastic_locations.html);
[Prepping a Dungeon](https://slyflourish.com/prepping_a_dungeon.html)).

`wiki lint` runs every configured check and returns every finding. Handle all
findings through this single repair loop.

**Done:** `next` is null and the final scoped lint has no actionable non-plot
findings.

`--check` runs the same loop without writes. `--consolidate` runs the same loop
with its confirmation rules. Read [consolidate.md](consolidate.md) when using
that mode.

## Handoffs

Use the page's owner skill for content decisions (`faction-design`,
`npc-design`, `place-design`, etc.). Use `wiki-dedup` for deep duplicate scans,
`tag-taxonomy` for tag audits, `cross-linker` for cross-references, and QMD for
vault lookup.

One done-summary: what changed, where.

## QMD refresh

Batch refreshes to the end — one `${QMD_CLI:-qmd} update` after all writes.
QMD failure does not roll back vault changes. Pending vectors are routine.
Retry once on SQLite error.

