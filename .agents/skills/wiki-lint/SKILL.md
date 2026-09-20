---
name: wiki-lint
description: >-
  Lint and repair wiki pages — bulk auto-fix, QMD re-index, then sequential
  manual repair file-by-file with commits. Use for vault health, page repair,
  audits, broken links, duplicate resolution, and cleanup. A bare page path
  repairs that page; no path repairs the vault; --check reports without writes;
  --consolidate runs the same repair loop with its confirmation rules.
---

# Wiki Lint

File what constitution X makes canon. Follow `docs/agents/work.md`.

## Method

Three phases: **sweep**, **reindex**, **repair**.

### 1. Sweep — bulk auto-fix

Resolve config, form the effective schema, and read `hot.md`.

Run `wiki lint fix` with no path argument. This auto-fixes every deterministic
finding across the entire vault in one pass — redirect stubs, link repairs,
index entries, manifest identity. One run; do not call it per-file.

Commit the sweep: `wiki lint fix: bulk auto-repair`.

### 2. Reindex — QMD refresh

Run `scripts/qmd-maintain.sh` immediately after the sweep. The manual repair
phase reads pages through QMD; stale embeddings after bulk file changes produce
wrong retrievals. Retry once on SQLite error. QMD failure does not block
repair — note it and continue.

### 3. Repair — sequential file-by-file

Run `wiki lint` to get the post-sweep worklist. All remaining findings need
manual repair.

For each file in the worklist, starting from `next.path`:

1. Run `wiki lint <path> --full` for that file's findings.
2. Read the page through QMD, then read its linked canon.
3. Resolve identity before editing.
4. Repair **every** finding in this file:
   - resolve links against existing owner filenames;
   - add required frontmatter;
   - correct type, lifecycle, and filename;
   - apply the page template and complete every required section;
   - load the page's owner skill when a section needs domain content;
   - create plot only when the user explicitly asks; otherwise defer and
     continue all non-plot repairs;
   - when repair needs novel non-plot content, ground in established wiki fact
     with `wiki-query` and `wiki-context-pack`;
   - ground all content in canon; record gaps or proposals as the owner skill
     requires.
5. Run `wiki lint <path>` to confirm clean (non-plot findings only).
6. Commit: the file path and a short description of what was repaired.
7. Proceed to the next file.

An empty required section is a finding. A sparse page is not repaired until it
contains substantive, actionable content for every non-plot template job. Plot
work is inactive unless the user asks for it.

For place pages, use Michael E. Shea's playable-location baseline: named areas,
connections, inhabitants or pressures, and discoverable information
([Designing Fantastic Locations](https://slyflourish.com/designing_fantastic_locations.html);
[Prepping a Dungeon](https://slyflourish.com/prepping_a_dungeon.html)).

**Done:** the worklist is empty (non-plot) and every repaired file is committed.

`--check` runs the same loop without writes. `--consolidate` runs the same loop
with its confirmation rules. Read [consolidate.md](consolidate.md) when using
that mode.

## Handoffs

Use the page's owner skill for content decisions (`faction-design`,
`npc-design`, `place-design`, etc.). Use `wiki-dedup` for deep duplicate scans,
`tag-taxonomy` for tag audits, `cross-linker` for cross-references, and QMD for
vault lookup.

One done-summary: what changed, where.
