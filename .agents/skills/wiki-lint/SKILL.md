---
name: wiki-lint
description: >-
  Lint and repair wiki pages — run the deterministic auto-fix once, then
  manually repair every remaining finding one file at a time. Use for vault
  health, page repair, audits, broken links, duplicate resolution, and cleanup.
  A bare page path repairs that page; no path repairs the vault.
---

# Wiki Lint

File what constitution X makes canon. Follow `docs/agents/work.md`.

## Method

Three phases: **sweep**, **reindex**, **repair**.

### 1. Sweep — one deterministic auto-fix

Resolve config, form the effective schema, and read `hot.md`.

Run `wiki lint fix` with no path argument once. This applies every registered
deterministic repair across the entire vault. Do not run the fixer per file.

Commit the sweep: `wiki lint fix: bulk auto-repair`.

### 2. Reindex — QMD refresh

Run `scripts/qmd-maintain.sh` immediately after the sweep. The manual repair
phase reads pages through QMD; stale embeddings after bulk file changes produce
wrong retrievals. Retry once on SQLite error. QMD failure does not block
repair — note it and continue.

### 3. Repair — sequential file-by-file

Run `wiki lint` to get the post-sweep full worklist. Every remaining finding is
manual work.

Start at `next.path`. Work on exactly one file until its full lint is clean,
regardless of backlog size. Do not batch files, invoke another fixer, generate
repair scripts, or replace this manual phase with automation.

For the current file:

1. Read the page through QMD, then read its linked canon.
2. Resolve identity before editing.
3. Repair **every** finding in this file:
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
4. Run `wiki lint <path>` to confirm the file is clean.
5. Commit: the file path and a short description of what was repaired.
6. Return to `next.path` and repeat for the next file.

An empty required section is a finding. A sparse page is not repaired until it
contains substantive, actionable content for every non-plot template job. Plot
work is inactive unless the user asks for it.

For place pages, use Michael E. Shea's playable-location baseline: named areas,
connections, inhabitants or pressures, and discoverable information
([Designing Fantastic Locations](https://slyflourish.com/designing_fantastic_locations.html);
[Prepping a Dungeon](https://slyflourish.com/prepping_a_dungeon.html)).

**Done:** the full worklist is empty and every repaired file is committed.

## Handoffs

Use the page's owner skill for content decisions (`faction-design`,
`npc-design`, `place-design`, etc.). Use `wiki-dedup` for deep duplicate scans,
`tag-taxonomy` for tag audits, `cross-linker` for cross-references, and QMD for
vault lookup.

One done-summary: what changed, where.
