---
name: wiki-lint
description: >
  Lint and repair wiki pages. Branches: bare path → page-scoped repair;
  no path → full vault scan; --check → report only;
  --consolidate → dream cycle (dry-run; FR-002 apply; confirm non-FR-002).
---

# Wiki Lint

FR-002 structural repair (links, required frontmatter, nearest-valid type/lifecycle) files without a wait. Template conformance relocates existing content only; MUST NOT invent missing field body. Content with no template field is preserved. After Linting: one done-summary after green.

## Setup

1. **Resolve config** — Config Resolution Protocol in `llm-wiki/SKILL.md`. Yields `OBSIDIAN_VAULT_PATH` plus optional `OBSIDIAN_ALLOWED_LIFECYCLES`, `OBSIDIAN_ALLOWED_RELATIONSHIP_TYPES`, `OBSIDIAN_REQUIRED_TRUST_FIELDS`, `OBSIDIAN_SCHEMA_SOURCE`.
2. **Form effective schema** — record schema source, effective required/optional frontmatter, lifecycle values, relationship types, provenance markers. Never coerce owner types to framework types.
3. **Read `hot.md`** from the resolved vault path. Open bounded `log.md` slice only if needed. Do not preload `index.md` or full `log.md`.

## Deterministic Pass

Run from repo root:

- **Full vault:** `./scripts/wiki-lint --json wiki/`
- **Page-scoped:** `./scripts/wiki-lint --json --scope <path> wiki/` (bare `.md` paths or `files:<path>`)

Pass owner extensions: `--allow-lifecycle` / `--allow-relationship-type`. The JSON `schema` block must match your effective schema before accepting findings.

**HARD fail keys:** `broken_links`, `missing_frontmatter`, `bad_type`, `bad_lifecycle`, `typed_relationships`, `pc_identity_mismatch`, `spaced_basename`, `aruhe_prefix_basename`, `illegal_basename`, `duplicate_stems`, `template_conformance`. **Soft keys:** `snake_case_labels`, `pc_tag_on_npc`, `snake_case_owner_basename`.

Redirect stubs (`redirects_to` in frontmatter) are skipped for `missing_frontmatter`, `spaced_basename`, `aruhe_prefix_basename`; reserved files (`AGENTS.md`, `README.md`, `index.md`, `log.md`, `hot.md`) and mechanic-allowlist links skipped for `broken_links`; `_archive`/`_raw`/templates/`_meta` skipped — live pages only for filename HARD keys. Template conformance checks typed pages against `wiki/templates/contracts/{type}.yml`.

Clean = `status: "clean"`, empty findings, `identity.status` `"resolved"`.

Schema precedence: CLI flags > resolved config > framework defaults. Lifecycle/relationship extensions additive. Empty/whitespace values fail closed.

**Vale gate:** page-scoped runs the default Vale pass. Every `VALE_*` finding is a lint finding — repair when deterministic. False positives: correct the Vale rule/config with narrowly scoped exemption and regression fixture, then rerun. Overall-clean = no fixable findings, `hard_fail: false`, exit `0`. Rerun after Vale repairs — fixes surface follow-on findings. Budget three passes per page; persist → manual review item.

## Page-Scoped Repair

When a page path is given (the hot path):

1. Run page-scoped deterministic pass.
2. Read the page via QMD search-then-get; fall back to direct file read.
3. **Identity.** When `identity.status` is `ambiguous`, read every candidate body. Complete Check 14 (`merge`, `digest`, or `differentiate`) until identity is `resolved`. Then edit.
4. **Repair every fixable finding** (autonomous FR-002; no Work prompt; kebab remorph needs no extra greenlight): broken wikilinks (resolve to an existing owner; if the target is a named missing owner, mint the thinnest valid owner from its template using only established mentions — do not delete a named live-wiki reference to go green), missing required frontmatter (add with defaults), invalid lifecycle/type (correct to nearest valid), snake_case/spaced/Aruhe/`00` basenames (rename to kebab). Removal is valid only for malformed links, mechanic-allowlist tokens, or accidental junk. **Template ceiling:** when a contract exists for the page's `type`, add/correct/remove only sections, frontmatter, and callouts defined in that contract — relocate existing content only; MUST NOT invent missing field body. Content with no template field is preserved and flagged. **Source before filling:** when adding a missing required section, `wiki-query` the page's linked entities and source material before writing — ground in wiki content, not generation. Canon contradiction: append `errors.md` and MUST NOT pick a winner.
5. Report fixes inline. List unfixable findings separately with reasons.
6. **QMD refresh** — if page modified and QMD available, `${QMD_CLI:-qmd} update`.

**Done when:** identity is `resolved`; every fixable finding repaired; page-scoped command has `hard_fail: false` and empty findings; remaining unfixable findings listed; one done-summary names what changed and where (no question, no wait).

`--check`: report findings without repairing.

## Bulk Repair

When vault-wide lint finds fixable issues across files and `--check` is not set:

1. Run `./scripts/wiki-lint --json wiki/` (bare = every live page). `--scope X` never escapes X.
2. Use JSON `backlog`: live pages with findings, sorted by file byte size then path. `next_page` is the first item.
3. Process one backlog page: read, repair, page-scoped verify, commit. Re-run lint and take the new `next_page`.
4. Stop only when `backlog` is empty, the user stops the run, or a concrete unrecoverable blocker occurs.

**Done when:** the applicable backlog is empty, or a concrete unrecoverable blocker is named; then one done-summary (what changed, where; no question; no wait).

## Full Vault Checks

For checks beyond the deterministic script, see [checks.md](checks.md).

## Consolidate Mode

`--consolidate` is act-and-report: apply FR-002 without `"Apply these N changes? [yes / no / select]"`; keep that confirm for merge, tier demotion, and other non-FR-002 actions. See [consolidate.md](consolidate.md).

## After Linting

Append to `log.md`:
```
- [TIMESTAMP] LINT issues_found=N orphans=X broken_links=Y stale=Z contradictions=W prov_issues=P missing_summary=S fragmented_clusters=F visibility_issues=V promotion_candidates=C duplicate_pages=D synthesis_gaps=G relationship_issues=R
```


Then one done-summary: what changed, where. MUST NOT ask a question or wait for a reply.

## QMD Refresh

Batch refreshes to end — one `${QMD_CLI:-qmd} update` after all writes. QMD failure does not roll back vault changes.

Pending vectors in output = routine. `scripts/qmd-maintain.sh --embed` only on explicit request. Serial QMD access — no concurrent invocations (SQLite collision). Retry once on SQLite error.
