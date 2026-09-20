---
name: wiki-lint
description: >-
  Lint and repair wiki pages — structural conformance, broken links, frontmatter,
  type/lifecycle validity, template contracts, filename shape, and duplicate
  resolution. Use for any vault health task: a bare page path for page-scoped
  repair, no path for full vault scan, --check for report-only, --consolidate
  for the periodic self-heal cycle. Also use when asked to audit, fix broken
  links, check wiki health, find duplicates, or clean up pages.
---

# Wiki Lint

File what constitution X makes canon. Follow `docs/agents/work.md`.

## Central principle

A lint pass is **structural repair, not content authorship**. Fix links,
frontmatter, type, lifecycle, template conformance, and filename shape.
Relocate existing content to match its template contract. Never invent
missing field body — a section the page does not have stays empty until a
content skill or the DM fills it. FR-002 structural repairs file without a
wait. Template conformance relocates existing content only; content with no
template field is preserved.

## Setup

1. **Resolve config** — Config Resolution Protocol in AGENTS.md.
   Yields `OBSIDIAN_VAULT_PATH` plus optional `OBSIDIAN_ALLOWED_LIFECYCLES`,
   `OBSIDIAN_ALLOWED_RELATIONSHIP_TYPES`, `OBSIDIAN_REQUIRED_TRUST_FIELDS`,
   `OBSIDIAN_SCHEMA_SOURCE`.
2. **Form effective schema** — record schema source, effective
   required/optional frontmatter, lifecycle values, relationship types,
   provenance markers. Never coerce owner types to framework types.
3. **Read `hot.md`** from the resolved vault path.


## Health

`wiki health` then do `context.act` (first-turn and skill load). Done: heaviest first-turn file is disclosed or kept as a step. Then do `next` (then remaining `focus`).

## Deterministic pass

Run the structural command from repo root before any agent repair:

- **Vault or path:** `wiki lint [path ...]`
- `--full` adds the detailed per-file findings for the selected scope

Default stdout is a compact overview: `counts`, `finding_total`,
`affected_pages`, cache/scope metadata, and `next`. `next.path` is the
smallest dirty file by bytes, then vault-relative path; `next.action` tells
the agent to run `wiki lint <next.path> --full`, repair it, and rerun lint.
Default output does not contain `files`, `unique`, or `backlog` dumps.

`wiki lint` is the sole agent-facing lint command. It runs every configured
checker, including structural, template-conformance, creative, and Vale
checks. Aggregate counts include every finding at every severity. Agents do
not add checker-suppression flags.

Clean = `status: "clean"`, `finding_total: 0`, and no open ledger failures.


### Vale and other checker findings

Every `VALE_*` or mapped Vale finding is included in the aggregate counts.
Use `wiki lint <path> --full` when line-level Vale or other checker findings
are needed for repair.
Repair deterministic findings when safe; route judgment findings to their
owner skill. False positives: correct the rule/config with a narrowly scoped
exemption and regression fixture, then rerun. Rerun after repairs because
follow-on findings can surface. Persisting findings remain explicit manual
review items.

The agent-facing command does not expose hard-only or checker-suppression
carve-outs. The checker backend remains an implementation detail.


### Vale gate

Page-scoped runs the default Vale pass. Use `--full` to expose every finding
with a 1-based line. Repair deterministic findings when safe; route judgment
findings to the owner skill; then rerun until the result is clean or a
concrete manual-review blocker remains.

## Branch: page-scoped repair

The hot path — a single page given by path.

1. **Detect.** Run page-scoped deterministic pass.
2. **Read.** Retrieve the page via QMD search-then-get; fall back to direct
   file read.
3. **Resolve identity.** When `identity.status` is `ambiguous`, read every
   candidate body. Complete Check 14 (`merge`, `digest`, or `differentiate`)
   until identity is `resolved`. Then edit.
4. **Repair every fixable finding:**
   - **Kind home:** `misplaced_entity` → move the page to
     `entities/{type}/{basename}` from frontmatter `type`, then re-run.
     Template and Vale wait until that path is current.
   - Broken wikilinks → resolve to an existing owner; if the target is a
     named missing owner, mint the thinnest valid page from its template
     using only established mentions.
   - Missing required frontmatter → add with defaults.
   - Invalid lifecycle/type → correct to nearest valid.
   - Filename shape (snake_case, spaced, Aruhe, `00`) → rename to kebab.
   - **Template ceiling:** when a contract exists for the page's `type`,
     add/correct/remove only sections, frontmatter, and callouts defined in
     that contract — relocate existing content only. Content with no template
     field is preserved and flagged.
   - **Source before filling:** when adding a missing required section,
     `wiki-query` the page's linked entities and source material before
     writing — ground in wiki content, not generation.
   - Canon contradiction: append `errors.md`, never pick a winner.
5. **Report.** List fixes inline. List unfixable findings separately with
   reasons.
6. **QMD refresh.** If page modified and QMD available,
   `${QMD_CLI:-qmd} update`.

**Done when:** identity resolved; `wiki lint <page> --full` returns
`hard_fail: false` with no findings; unfixable findings listed; one
done-summary names what changed and where.

`--check`: report findings without repairing.

## Branch: bulk repair

When vault-wide lint finds fixable issues and `--check` is not set:

1. Run `wiki lint` and take `next.path` (the smallest dirty file).
2. Run `wiki lint <next.path> --full`, read and repair that page, then run
   the page-scoped lint again.
3. Rerun `wiki lint` and take the new `next.path`.
4. Stop when `next` is null, the user stops the run, or a concrete
   unrecoverable blocker occurs.

**Done when:** backlog empty or a concrete blocker named; one done-summary.

## Branch: full vault checks

For checks beyond the deterministic script, read [checks.md](checks.md).

## Branch: consolidate

`--consolidate` is act-and-report: FR-002 applied without confirm; non-FR-002
actions confirm. Read [consolidate.md](consolidate.md).

## Handoffs

Hand off content authorship to the page's type skill (faction-design,
npc-design, place-design, etc.), deep dedup scans to `wiki-dedup`, tag
audits to `tag-taxonomy`, cross-referencing to `cross-linker`, and vault
lookup to `.agents/skills/qmd` plus
`specs/004-qmd-search-default/contracts/retrieval-precedence.md`.

One done-summary: what changed, where.

## QMD refresh

Batch refreshes to end — one `${QMD_CLI:-qmd} update` after all writes.
QMD failure does not roll back vault changes. Pending vectors in output =
routine. `scripts/qmd-maintain.sh --embed` only on explicit request. Serial
QMD access — no concurrent invocations (SQLite collision). Retry once on
SQLite error.
