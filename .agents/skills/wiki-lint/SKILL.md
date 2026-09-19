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

1. **Resolve config** — Config Resolution Protocol in `llm-wiki/SKILL.md`.
   Yields `OBSIDIAN_VAULT_PATH` plus optional `OBSIDIAN_ALLOWED_LIFECYCLES`,
   `OBSIDIAN_ALLOWED_RELATIONSHIP_TYPES`, `OBSIDIAN_REQUIRED_TRUST_FIELDS`,
   `OBSIDIAN_SCHEMA_SOURCE`.
2. **Form effective schema** — record schema source, effective
   required/optional frontmatter, lifecycle values, relationship types,
   provenance markers. Never coerce owner types to framework types.
3. **Read `hot.md`** from the resolved vault path. Open bounded `log.md`
   slice only if needed. Do not preload `index.md` or full `log.md`.

## Deterministic pass

Run the structural command from repo root before any agent repair:

- **Full vault (default compact worklist):** `scripts/wiki lint`
- **Single-file scope (findings included):** `scripts/wiki lint <path>`
- **Full findings:** `scripts/wiki lint --full` (also add `--full` to a directory scope)

The default bulk output is compact worklist JSON: counts, `backlog`, and
`next_page`, without per-finding details. A single-file scope includes
findings; `--full` includes findings for bulk scopes.

Pass owner extensions: `--allow-lifecycle` / `--allow-relationship-type`.
The JSON `schema` block must match your effective schema before accepting
findings.

**HARD fail keys:** `broken_links`, `missing_frontmatter`, `bad_type`,
`bad_lifecycle`, `typed_relationships`, `pc_identity_mismatch`,
`spaced_basename`, `aruhe_prefix_basename`, `illegal_basename`,
`duplicate_stems`, `template_conformance`.

**Soft keys:** `snake_case_labels`, `pc_tag_on_npc`,
`snake_case_owner_basename`.

Redirect stubs (`redirects_to` in frontmatter) skip `missing_frontmatter`,
`spaced_basename`, `aruhe_prefix_basename`. Reserved files (`AGENTS.md`,
`README.md`, `index.md`, `log.md`, `hot.md`) and mechanic-allowlist links
skip `broken_links`. `_archive`/`_raw`/templates/`_meta` skipped — live
pages only for filename HARD keys. Template conformance checks typed pages
against `wiki/templates/contracts/{type}.yml`.

Clean = `status: "clean"`, empty findings, `identity.status` `"resolved"`.

Schema precedence: CLI flags > resolved config > framework defaults.
Lifecycle/relationship extensions additive. Empty/whitespace values fail
closed.

### Vale gate

Page-scoped runs the default Vale pass. Every `VALE_*` finding is a lint
finding — repair when deterministic. False positives: correct the Vale
rule/config with narrowly scoped exemption and regression fixture, then
rerun. Overall-clean = no fixable findings, `hard_fail: false`, exit `0`.
Rerun after Vale repairs — fixes surface follow-on findings. Budget three
passes per page; persist → manual review item.

## Branch: page-scoped repair

The hot path — a single page given by path.

1. **Detect.** Run page-scoped deterministic pass.
2. **Read.** Retrieve the page via QMD search-then-get; fall back to direct
   file read.
3. **Resolve identity.** When `identity.status` is `ambiguous`, read every
   candidate body. Complete Check 14 (`merge`, `digest`, or `differentiate`)
   until identity is `resolved`. Then edit.
4. **Repair every fixable finding:**
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

**Done when:** identity resolved; every fixable finding repaired;
page-scoped command returns `hard_fail: false` with empty findings;
unfixable findings listed; one done-summary names what changed and where.

`--check`: report findings without repairing.

## Branch: bulk repair

When vault-wide lint finds fixable issues and `--check` is not set:

1. Run `scripts/wiki lint` for the default compact worklist.
2. Take `next_page` — the first page in `backlog`, sorted by file byte size
   then path.
3. Process one backlog page: read, repair, page-scoped verify, commit.
   Re-run `scripts/wiki lint` and take the new `next_page`.
4. Stop only when `backlog` is empty, the user stops the run, or a concrete
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

## After linting

Append to `log.md`:
```
- [TIMESTAMP] LINT issues_found=N orphans=X broken_links=Y stale=Z contradictions=W prov_issues=P missing_summary=S fragmented_clusters=F visibility_issues=V promotion_candidates=C duplicate_pages=D synthesis_gaps=G relationship_issues=R
```

One done-summary: what changed, where.

## QMD refresh

Batch refreshes to end — one `${QMD_CLI:-qmd} update` after all writes.
QMD failure does not roll back vault changes. Pending vectors in output =
routine. `scripts/qmd-maintain.sh --embed` only on explicit request. Serial
QMD access — no concurrent invocations (SQLite collision). Retry once on
SQLite error.
