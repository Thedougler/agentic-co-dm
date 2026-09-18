---
name: wiki-lint
description: >
  Find and repair structural issues in the Obsidian wiki. Default is lint-and-repair: fix every page-scoped
  finding (broken links, missing frontmatter, bad wikilinks). Triggers on "lint", "lint <page>", "clean up
  the wiki", "fix broken links", "what needs fixing", "audit my notes", "wiki health check". Page-scoped:
  pass a vault-relative .md path to lint and repair one page. Pass --check for report-only (no writes).
  Pass --consolidate for the vault-wide dream cycle with dry-run preview and user confirmation before
  bulk writes.
---

# Wiki Lint — Health Audit

You are performing a health check on an Obsidian wiki. Your goal is to find and fix structural issues that degrade the wiki's value over time.

**Retrieval order:** QMD search-then-get first; grep only for targeted evidence QMD cannot answer (exact line numbers, regex patterns). Follow the Retrieval Primitives table in `llm-wiki/SKILL.md` — cheapest primitive that answers the question, escalate only when it cannot. On a large vault, blindly reading every page to lint it is exactly what this framework is built to avoid.

## Before You Start

**Deterministic pass:** from repo root run `./scripts/wiki-lint --json wiki/` (full vault) or `./scripts/wiki-lint --json --scope <path> wiki/` (page-scoped — accepts bare `.md` paths or `files:<path>`). When a page path is given, use the page-scoped form and follow the Page-Scoped Repair flow below. HARD fail keys: `broken_links`, `missing_frontmatter`, `bad_type`, `bad_lifecycle`, `typed_relationships`, `pc_identity_mismatch`, `spaced_basename`, `aruhe_prefix_basename`, `illegal_basename`, `duplicate_stems`, `template_conformance` (redirect stubs with `redirects_to` are omitted from `missing_frontmatter`, `spaced_basename`, and `aruhe_prefix_basename`; reserved files and mechanic allowlist links are omitted from `broken_links`; `_archive`/`_raw`/templates/`_meta` skipped as usual — live pages only for filename HARD keys). Template conformance runs by default: typed pages are checked against `wiki/templates/contracts/{type}.yml` for required sections, required frontmatter, and disallowed callouts. Use that report. Soft keys: `snake_case_labels` (DM-visible snake_case table/list labels `{page,line,token,kind}`); `pc_tag_on_npc` (npc tagged pc without role/player signal); `snake_case_owner_basename` (snake_case owner basenames under `entities/{type}/`, `{page,stem,kind}` — kebab preferred, not HARD). Not HARD. Do not grep the vault for orphans or broken links unless a HARD finding is unclear.

1. **Resolve config** — follow the Config Resolution Protocol in `llm-wiki/SKILL.md` (inline `@name` override → walk up CWD for `.env` → `~/.obsidian-wiki/config` → prompt setup). This gives `OBSIDIAN_VAULT_PATH` plus any `OBSIDIAN_ALLOWED_LIFECYCLES`, `OBSIDIAN_ALLOWED_RELATIONSHIP_TYPES`, `OBSIDIAN_REQUIRED_TRUST_FIELDS`, and `OBSIDIAN_SCHEMA_SOURCE` values.
2. **Read owner rules** — if `$OBSIDIAN_VAULT_PATH/AGENTS.md` exists, read it before interpreting any schema. Owner rules override framework defaults.
3. **Form the effective schema** — record the schema source locator plus effective required/optional frontmatter, lifecycle values, relationship types, and provenance markers. Framework values are defaults; preserve owner extensions and relaxed requiredness exactly. Never coerce an owner type to a framework type.
4. Prefer `$OBSIDIAN_VAULT_PATH/hot.md` + capped `qmd`/`rg` for inventory; full `index.md` only if that fails — whole-file preload is token waste. Read `hot.md` from the resolved vault path, not the repo root.
5. Prefer `$OBSIDIAN_VAULT_PATH/hot.md` for recent activity; open a bounded slice of `log.md` only if needed — do not preload all of `log.md`
6. **Duplicate identity check:** before selecting or editing a page, verify no other page covers the same entity (matching title, aliases, or `redirects_to` target). When two pages cover one identity, surface the conflict before editing either — size-first selection without identity check causes wrong-page edits.
7. **Redirect stubs:** pages with `redirects_to` in frontmatter are pointers, not content pages. Skip them in orphan checks, scene detection, frontmatter validation (they omit campaign required fields), and creative lint. Do not create redirect stubs unless the user explicitly requests one — vault clutter.

Pass the effective schema to deterministic checks explicitly. For example, add each owner extension with `--allow-lifecycle` / `--allow-relationship-type`, replace trust requiredness with repeatable `--required-trust-field`, and identify the authority with `--schema-source "$OBSIDIAN_VAULT_PATH/AGENTS.md"`. The JSON report's `schema` block must match the schema you formed before findings are accepted.

Schema precedence is CLI flags > resolved environment/config values > framework defaults; lifecycle and relationship extensions remain additive. Strip every override before use. An explicitly configured empty or whitespace-only value—and any empty comma-separated list entry—fails closed; never treat it as a valid lifecycle, relationship type, required field, or authority locator. Remove the variable instead when defaults are intended.

## Page-Scoped Repair

When a page path is given ("lint entities/faction/the-passage.md"), repair that page. This is the default — a full vault scan is not required.

1. **Scope the deterministic pass.** Run `./scripts/wiki-lint --json --scope <path> wiki/` where `<path>` is the vault-relative `.md` path (bare paths accepted: `entities/faction/the-passage.md`). The script also accepts `files:<path>` syntax.
2. **Read the page** via QMD search-then-get when available. Fall back to direct file read.
3. **Repair every fixable finding** on that page: broken wikilinks (correct or remove), missing required frontmatter (add with defaults), invalid lifecycle/type values (correct to nearest valid), snake_case or spaced basenames (rename to kebab when remorph is greenlit). **Template ceiling:** when a template contract exists for the page's `type`, repairs add, correct, or remove only sections, frontmatter fields, and callout types defined in that contract. Do not invent sections, callouts, or structural elements absent from the contract. **Source before filling:** when a repair adds a missing required section, use `wiki-query` to retrieve the page's linked entities, related pages, and source material before writing the section body — ground it in wiki content, not generation.
4. **Report** what was fixed inline. List unfixable findings (human judgment) separately. Keep output bounded to the scoped page — no vault-wide report.
5. **Skip rule 12e** (trust-check) when `_meta/trust-ledger.json` does not exist. Trust review is not a lint gate for vaults that do not use it.
6. **QMD refresh** — if QMD is available and the page was modified, run `${QMD_CLI:-qmd} update`.

Done when: every fixable finding on the named page is repaired. Unfixable findings are listed with reasons. No vault-wide scan was performed.

Pass `--check` to report findings without repairing them. The full vault flow below runs when no page path is given.

## Bulk Repair

When vault-wide lint finds fixable issues across multiple files and `--check` is not set, repair them **one file at a time** from the findings backlog. Other files may be read for corroborating context (link targets, cross-references), but only **one file is written at a time**.

1. Run all lint checks (deterministic pass + checks 1–13). Collect the full findings list — this is the **backlog**.
2. Group findings by file. Order: files with the most HARD findings first.
3. For each file in the backlog:
   a. Read the file. Read related files for context as needed (link targets, cross-references) — but write only this file.
   b. Fix every fixable finding on this file (same repairs as Page-Scoped Repair step 3).
   c. Re-run page-scoped lint (`./scripts/wiki-lint --json --scope <path> wiki/`) and fix until clean.
   d. Commit this file's changes before opening the next.
4. **Degradation stop.** After each file completes, assess output quality and remaining context. If quality has degraded (wrong fixes, missed findings, shallow repairs) or context is filling, stop. Report files completed so far, list the remaining backlog, and recommend delegating the rest to a fresh agent.

Done when: every file in the backlog is repaired and verified clean, or the degradation stop fired with a delegation recommendation.

## Lint Checks

Run these checks in order. Report findings as you go.

**Scope:** skip `_archives/`, `_raw/`, `_staging/`, `_readouts/`, and `.obsidian/` in every check. These hold frozen snapshots, unprocessed review drafts, and derived readouts (saved by `wiki-narrate`) — they are not live knowledge-graph pages, so orphan, frontmatter, and link checks don't apply to them. Reserved `README.md`, `AGENTS.md`, `index.md`, `log.md`, and `hot.md` files are operational documents, not content pages.

### 1. Orphaned Pages

Find pages with zero incoming wikilinks. These are knowledge islands that nothing connects to.

**How to check:**
- Glob all `.md` files in the vault
- **Skip redirect stubs** (pages with `redirects_to` in frontmatter) — they are pointers, not knowledge pages
- For each page, Grep the rest of the vault for `[[page-name]]` references
- Pages with zero incoming links (except `index.md` and `log.md`) are orphans

**How to fix:**
- Identify which existing pages should link to the orphan
- Add wikilinks in appropriate sections

### 2. Broken Wikilinks

Find `[[wikilinks]]` that point to pages that don't exist.

**How to check:**
- Grep for `\[\[.*?\]\]` across all pages
- Extract the link targets
- Check if a corresponding `.md` file exists **in the vault** (not just in scope). When running page-scoped lint, a link to a page outside the scope is not broken — resolve link targets against the full vault.

**How to fix:**
- If the target was renamed, update the link
- If the target should exist, create it
- If the link is wrong, remove or correct it

### 3. Missing Frontmatter

Every page should have: title, category, tags, sources, created, updated.

**How to check:**
- Grep frontmatter blocks (scope to `^---` at file heads) instead of reading every page in full
- Flag pages missing required fields

**How to fix:**
- Add missing fields with reasonable defaults

### 3a. Missing Summary (soft warning)

Every page *should* have a `summary:` frontmatter field — 1–2 sentences, ≤200 chars. This is what cheap retrieval (e.g. `wiki-query`'s index-only mode) reads to avoid opening page bodies.

**How to check:**
- Grep frontmatter for `^summary:` across the vault
- Flag pages without it, **but as a soft warning, not an error** — older pages predating this field are fine; the check exists to nudge ingest skills into filling it on new writes.
- Also flag pages whose summary exceeds 200 chars.

**How to fix:**
- Re-ingest the page, or manually write a short summary (1–2 sentences of the page's content).

### 4. Stale Content

Pages whose `updated` timestamp is old relative to their sources.

**How to check:**
- Compare page `updated` timestamps to source file modification times
- Flag pages where sources have been modified after the page was last updated

### 5. Contradictions

Claims that conflict across pages.

**How to check:**
- This requires reading related pages and comparing claims
- Focus on pages that share tags or are heavily cross-referenced
- Look for phrases like "however", "in contrast", "despite" that may signal existing acknowledged contradictions vs. unacknowledged ones

**How to fix:**
- Add an "Open Questions" section noting the contradiction
- Reference both sources and their claims

### 6. Index Consistency

Verify `index.md` matches the actual page inventory.

**How to check:**
- Compare pages listed in `index.md` to actual files on disk
- Check that summaries in `index.md` still match page content

### 7. Provenance Drift

Check whether pages are being honest about how much of their content is inferred vs extracted. See the Provenance Markers section in `llm-wiki` for the convention.

**How to check:**
- For each page with a `provenance:` block or any `^[inferred]`/`^[ambiguous]` markers, count sentences/bullets and how many end with each marker
- Compute rough fractions (`extracted`, `inferred`, `ambiguous`)
- Apply these thresholds:
  - **AMBIGUOUS > 15%**: flag as "speculation-heavy" — even 1-in-7 claims being genuinely uncertain is a signal the page needs tighter sourcing or should be moved to `synthesis/`
  - **INFERRED > 40% with no `sources:` in frontmatter**: flag as "unsourced synthesis" — the page is making connections but has nothing to cite
  - **Hub pages** (top 10 by incoming wikilink count) with INFERRED > 20%: flag as "high-traffic page with questionable provenance" — errors on hub pages propagate to every page that links to them
  - **Drift**: if the page has a `provenance:` frontmatter block, flag it when any field is more than 0.20 off from the recomputed value
- **Skip** pages with no `provenance:` frontmatter and no markers — treated as fully extracted by convention

**How to fix:**
- For ambiguous-heavy: re-ingest from sources, resolve the uncertain claims, or split speculative content into a `synthesis/` page
- For unsourced synthesis: add `sources:` to frontmatter or clearly label the page as synthesis
- For hub pages with INFERRED > 20%: prioritize for re-ingestion — errors here have the widest blast radius
- For drift: update the `provenance:` frontmatter to match the recomputed values

### 8. Fragmented Tag Clusters

Checks whether pages that share a tag are actually linked to each other. Tags imply a topic cluster; if those pages don't reference each other, the cluster is fragmented — knowledge islands that should be woven together.

**How to check:**
- For each tag that appears on ≥ 5 pages:
  - `n` = count of pages with this tag
  - `actual_links` = count of wikilinks between any two pages in this tag group (check both directions)
  - `cohesion = actual_links / (n × (n−1) / 2)`
- Flag any tag group where cohesion < 0.15 and n ≥ 5

**How to fix:**
- Run the `cross-linker` skill targeted at the fragmented tag — it will surface and insert the missing links
- If a tag group is large (n > 15) and still fragmented, consider splitting it into more specific sub-tags

### 9. Visibility Tag Consistency

Checks that `visibility/` tags are applied correctly and aren't silently missing where they matter.

**How to check:**

- **Untagged PII patterns:** Grep page bodies for patterns that commonly indicate sensitive data — lines containing `password`, `api_key`, `secret`, `token`, `ssn`, `email:`, `phone:` followed by an actual value (not a field description). If a page matches and lacks `visibility/pii` or `visibility/internal`, flag it as a likely mis-classification.
- **`visibility/pii` without `sources:`:** A page tagged `visibility/pii` should always have a `sources:` frontmatter field — if there's no provenance, there's no way to verify the classification. Flag any `visibility/pii` page missing `sources:`.
- **Visibility tags in taxonomy:** `visibility/` tags are system tags and must **not** appear in `_meta/taxonomy.md`. If found there, flag as misconfigured — they'd be counted toward the 5-tag limit on pages that include them.

**How to fix:**
- For untagged PII patterns: add `visibility/pii` (or `visibility/internal` if it's team-context rather than personal data) to the page's frontmatter tags
- For missing `sources:`: add provenance or escalate to the user — don't auto-fill
- For taxonomy contamination: remove the `visibility/` entries from `_meta/taxonomy.md`

### 10. Misc Promotion Candidates

Find pages in `misc/` that have accumulated enough project affinity to be promoted.

**How to check:**
- Glob `$OBSIDIAN_VAULT_PATH/misc/*.md`
- For each page, read the `affinity` frontmatter field
- Flag pages where any single project's score ≥ 3

**How to fix:**
- Run the `cross-linker` skill first if affinity scores look stale (e.g., `affinity: {}` on a page with many wikilinks)
- To promote: move the page to `projects/<project-name>/references/` (or another appropriate category), update its `category` frontmatter, remove `promotion_status`, and grep the vault for backlinks to update them

### 12. Confidence and Lifecycle Schema

Enforces the confidence + lifecycle frontmatter schema (see `llm-wiki/SKILL.md`, Confidence and Lifecycle section).

Two modes:
- **`--check`** (default, read-only) — reports errors and warnings
- **`--consolidate`** — may apply separately approved structural maintenance, but **never rewrites `base_confidence`**

Confidence is a semantic judgment. A deterministic tool cannot infer independent evidence lineages or whole-page claim coverage from source strings alone. Confidence automation therefore validates an explicitly approved manual trust ledger; it never substitutes URL counting for review.

#### Rule 12a — `lifecycle` enum validation

**How to check:** Grep frontmatter for `^lifecycle:` across all pages. Flag any value outside the effective lifecycle set (framework default: `{draft, reviewed, verified, disputed, archived}`).

**How to fix:** n/a (only a human should set lifecycle state)

#### Rule 12b — `base_confidence` range

**How to check:** Grep frontmatter for `^base_confidence:` across all pages. Flag any present value outside `[0.0, 1.0]`; flag absence only when the effective owner schema requires the field.

**How to fix:** n/a (wrong value means the skill computed it wrong — surface for manual correction)

#### Rule 12c — Stale page report (computed overlay)

Staleness is never stored — it is computed at read time: `is_stale = (today − updated) > 90 days`.

**How to check:** For each page, read `updated:` from frontmatter and compute `is_stale`. If stale, also check `lifecycle:`. Report:
- Stale pages with `lifecycle: verified` with a louder annotation (these are the most dangerous — high-trust pages that may be wrong)
- All other stale pages as a standard warning

**How to fix:** `--fix` does **not** rewrite `lifecycle`. Staleness clears automatically when a re-ingest bumps `updated`.

#### Rule 12d — Supersession integrity

**How to check:** For each page with `superseded_by: "[[target]]"`:
- Verify the target page exists
- Verify the target page is not itself `archived` (no circular or chained supersession)
- Verify there are no cycles (A supersedes B which supersedes A)
- Warn if `lifecycle != archived` while `superseded_by` is set (inconsistent state)

**How to fix:** n/a — flag for human resolution

#### Rule 12e — Confidence review integrity

**How to check:** First verify `_meta/trust-ledger.json` exists. If absent, skip this entire rule — trust review is not a lint gate for vaults that do not use it. Canon authority for campaign vaults is: DM-provided canon first, session transcripts second, latest version of a fact third.

When the ledger exists, run the deterministic validator:

```bash
obsidian-wiki trust-check "$OBSIDIAN_VAULT_PATH" --strict --json --pretty
```

Use `--strict` for CI and scheduled gates: stale, unreviewed, or missing-page
warnings then return nonzero. Without `--strict`, `trust-check` remains a
read-only reporting command and returns nonzero only for hard ledger errors or
score mismatches.

The approved ledger lives at `_meta/trust-ledger.json`. Each entry records the human-reviewed score plus a SHA-256 fingerprint of material page content and evidence metadata. The fingerprint excludes volatile bookkeeping (`updated`, `base_confidence`, and lifecycle transition fields), so timestamp-only edits do not reopen review.

Interpret results as follows:

- `reviewed` — current material fingerprint and stored score both match the approved review; do **not** recompute from source strings.
- `stale` — body, summary, sources, provenance, tags, or relationships changed; perform a new manual lineage + claim-coverage review.
- `unreviewed` — page has no approved ledger entry; manual review is required.
- `score_mismatches` — material content still matches, but stored `base_confidence` differs from the approved value; fail the lint.
- `errors` — malformed/missing ledger data; fail the lint.

For a separately approved full-vault review, record the accepted state explicitly:

```bash
obsidian-wiki trust-record "$OBSIDIAN_VAULT_PATH" \
  --all --reviewed-at "<ISO-8601 timestamp>" --approved --json --pretty
```

After a separately approved review of only specific stale/unreviewed pages, update only those entries:

```bash
obsidian-wiki trust-record "$OBSIDIAN_VAULT_PATH" \
  --page "concepts/example.md" --page "skills/example.md" \
  --reviewed-at "<ISO-8601 timestamp>" --approved --json --pretty
```

`--approved` means a human approved every score being recorded. It is a workflow
assertion, not a cryptographic signature: keep `_meta/trust-ledger.json` under
version control and require human diff review before merging ledger changes.
`--all` is valid only after a full-vault review; use repeatable `--page` for
partial reviews so unrelated stale pages remain open. Never run `trust-record`
merely to silence warnings.

**Manual recomputation protocol for stale/unreviewed pages:**

1. Decompose the page into material claims and map each claim to evidence.
2. Collapse dependent evidence into independent lineages: files/commits from one repository, retries in one task chain, snapshots plus their captured source, duplicate memories, and parent/child tasks each count once.
3. Assign reviewed quality per independent lineage using `llm-wiki` buckets.
4. Compute the raw base score, then assess whole-page claim coverage. The formula is a starting point, not an automatic target.
5. Classify the result as `raise`, `keep`, `lower`, or `repair first`; require approval before changing `base_confidence` or refreshing the ledger.

**How to fix:** There is no automatic confidence fix. Apply only an explicitly approved exact patch, verify its scope, then refresh only the reviewed ledger state. `--consolidate` must never rewrite `base_confidence`.

#### Current enforcement

Under framework defaults, every non-reserved content page must contain a
finite `base_confidence` in `[0.0, 1.0]` and a documented lifecycle value.
An owner schema may relax either field; present values remain validated.
Missing or malformed trust fields, malformed ledger data, and a missing required
ledger are hard errors. New pages with valid trust fields but no approved ledger
entry are `unreviewed`; material changes to approved pages are `stale`.

#### Output additions

Add to the Wiki Health Report:

```markdown
### Confidence/Lifecycle Issues (N found)
- `concepts/foo.md` — missing `lifecycle` field (warning: Phase 1)
- `entities/bar.md` — `lifecycle: stalestate` is not a valid enum value
- `concepts/scaling.md` — `base_confidence: 1.4` is out of range [0.0, 1.0]
- `synthesis/old-analysis.md` — STALE (last updated 2025-10-01, 182 days ago) lifecycle=verified ⚠️ HIGH PRIORITY
- `concepts/outdated.md` — STALE (last updated 2025-11-15, 137 days ago) lifecycle=draft
- `entities/tool-v1.md` — `superseded_by: [[entities/tool-v2]]` but lifecycle=draft (expected archived)
- `concepts/drift-example.md` — confidence review stale: material fingerprint changed; manual lineage + coverage review required
- `entities/mismatch.md` — confidence mismatch: stored=0.80, approved=0.59
```

Append to the `LINT` log entry:
```
- [TIMESTAMP] LINT ... lifecycle_issues=N
```

### 13. Typed Relationships Validity

Validate `relationships:` frontmatter blocks. Skip pages that have no `relationships:` block — the field is optional.

**Framework-default types:** `extends`, `implements`, `contradicts`, `derived_from`, `uses`, `replaces`, `related_to`. Validate against the effective set after applying owner extensions.

**How to check:**
- Grep frontmatter for `^relationships:` across all vault pages
- For each page that has a `relationships:` block, read its frontmatter (not the full page body)
- For each entry in the block:
  1. **Type validation** — flag any `type:` value not in the allowed set above
  2. **Broken target** — strip `[[` and `]]` from the `target:` string, normalize (lowercase, spaces→hyphens, strip `.md`), and check whether a `.md` file at that path exists in the vault. Flag unresolved targets.
  3. **Self-reference** — flag any entry where the resolved target equals the page's own node id

**How to fix:**
- Invalid type: report the value and effective schema source. Correct it only if it is absent from both framework defaults and owner extensions; never replace a valid owner type with `related_to`.
- Broken target: update or remove the entry; if the target page should exist, create it first
- Self-reference: remove the entry

**Output additions:**

```markdown
### Typed Relationship Issues (N found)
- `concepts/foo.md` — relationships[1]: type "contradication" is not an allowed type (did you mean "contradicts"?)
- `concepts/bar.md` — relationships[0]: target "[[skills/nonexistent-skill]]" resolves to no page in vault
- `entities/baz.md` — relationships[2]: self-reference (target resolves to this page's own id)
```

Append to the `LINT` log entry:
```
... relationship_issues=N
```

### 11. Synthesis Gaps

Identify high-value synthesis opportunities the wiki is missing — concept pairs that co-occur across many pages but have no `synthesis/` page connecting them.

**How to check:**
- List all pages in `synthesis/` — collect the concept pairs each one already covers (from its `[[wikilinks]]` or title)
- Pick 10-15 frequently linked concepts from `concepts/` and `entities/`
- For each pair, run a quick grep to count pages that link to both:
  ```bash
  rg -l --glob '*.md' "\[\[ConceptA\]\]" "$OBSIDIAN_VAULT_PATH" > /tmp/a.txt
  rg -l --glob '*.md' "\[\[ConceptB\]\]" "$OBSIDIAN_VAULT_PATH" > /tmp/b.txt
  comm -12 <(sort /tmp/a.txt) <(sort /tmp/b.txt) | wc -l
  ```
- Flag pairs with co-occurrence ≥ 3 that have no existing synthesis page

**How to fix:**
- Run `/wiki-synthesize` to automatically discover and fill the top gaps

## Output Format

Report findings as a structured list:

```markdown
## Wiki Health Report

### Orphaned Pages (N found)
- `concepts/foo.md` — no incoming links

### Broken Wikilinks (N found)
- `entities/bar.md:15` — links to [[nonexistent-page]]

### Missing Frontmatter (N found)
- `skills/baz.md` — missing: tags, sources

### Stale Content (N found)
- `references/paper-x.md` — source modified 2024-03-10, page last updated 2024-01-05

### Contradictions (N found)
- `concepts/scaling.md` claims "X" but `synthesis/efficiency.md` claims "not X"

### Index Issues (N found)
- `concepts/new-page.md` exists on disk but not in index.md

### Missing Summary (N found — soft)
- `concepts/foo.md` — no `summary:` field
- `entities/bar.md` — summary exceeds 200 chars

### Provenance Issues (N found)
- `concepts/scaling.md` — AMBIGUOUS > 15%: 22% of claims are ambiguous (re-source or move to synthesis/)
- `entities/some-tool.md` — drift: frontmatter says inferred=0.10, recomputed=0.45
- `concepts/transformers.md` — hub page (31 incoming links) with INFERRED=28%: errors here propagate widely
- `synthesis/speculation.md` — unsourced synthesis: no `sources:` field, 55% inferred

### Fragmented Tag Clusters (N found)
- **#systems** — 7 pages, cohesion=0.06 ⚠️ — run cross-linker on this tag
- **#databases** — 5 pages, cohesion=0.10 ⚠️

### Visibility Issues (N found)
- `entities/user-records.md` — contains `email:` value pattern but no `visibility/pii` tag
- `concepts/auth-flow.md` — tagged `visibility/pii` but missing `sources:` frontmatter
- `_meta/taxonomy.md` — contains `visibility/internal` entry (system tag must not be in taxonomy)

### Misc Promotion Candidates (N found)
Pages in misc/ that have ≥ 3 connections to a single project and are ready to be promoted:

| Page | Top Project | Affinity Score |
|---|---|---|
| `misc/web-martinfowler-articles-microservices.md` | `obsidian-wiki` | 4 |

### Typed Relationship Issues (N found)
- `concepts/foo.md` — relationships[1]: type "contradication" is not an allowed type
- `concepts/bar.md` — relationships[0]: target "[[skills/nonexistent]]" resolves to no page

### Synthesis Gaps (N found)
Concept pairs that co-occur frequently but have no synthesis page:

| Pair | Co-occurrence | Suggested Action |
|---|---|---|
| [[Caching]] × [[Consistency]] | 5 pages | Run `/wiki-synthesize` |
| [[Testing]] × [[Observability]] | 3 pages | Run `/wiki-synthesize` |
```

## After Linting

Append to `log.md`:
```
- [TIMESTAMP] LINT issues_found=N orphans=X broken_links=Y stale=Z contradictions=W prov_issues=P missing_summary=S fragmented_clusters=F visibility_issues=V promotion_candidates=C synthesis_gaps=G relationship_issues=R
```

Offer to fix issues automatically or let the user decide which to address.

---

## Consolidate Mode (`--consolidate`)

Triggered by `wiki-lint --consolidate`. Switches from report-only to **act-and-report** — the "dream cycle" that runs periodically so the wiki self-heals.

### Safety protocol

**Always run in dry-run first.** Before writing anything:

1. Run all 12 lint checks (Step 1–12 above).
2. Print the planned consolidation actions as a structured list (see Dry-Run Output below).
3. Ask the user: `"Apply these N changes? [yes / no / select]"`.
4. Only proceed with writes after explicit confirmation. If the user selects individual actions, apply only those.
5. Never merge pages — use `wiki-dedup` for that. Only link, promote, demote, and flag.

### Consolidation actions (in order, after confirmation)

**Pre-write snapshot** — before the first file write, check whether the vault itself is the root of a Git repository. Merely being a subdirectory of a larger repository does not qualify: running `git add -A` there could capture unrelated files. If the vault is not a standalone Git repository, skip this step silently — no nagging, no suggesting `git init`.

```bash
VAULT_REAL_PATH=$(cd "$OBSIDIAN_VAULT_PATH" && pwd -P)
VAULT_GIT_ROOT=$(git -C "$OBSIDIAN_VAULT_PATH" rev-parse --show-toplevel 2>/dev/null || true)
SNAPSHOT_SHA=""

if [ -n "$VAULT_GIT_ROOT" ] && [ "$VAULT_GIT_ROOT" = "$VAULT_REAL_PATH" ]; then
  if git -C "$OBSIDIAN_VAULT_PATH" diff --quiet \
    && git -C "$OBSIDIAN_VAULT_PATH" diff --cached --quiet \
    && [ -z "$(git -C "$OBSIDIAN_VAULT_PATH" ls-files --others --exclude-standard)" ]; then
    SNAPSHOT_SHA=$(git -C "$OBSIDIAN_VAULT_PATH" rev-parse HEAD)
  else
    if ! git -C "$OBSIDIAN_VAULT_PATH" add -A; then
      echo "Pre-write snapshot failed; abort the skill without writing any vault files." >&2
      exit 1
    fi
    if ! git -C "$OBSIDIAN_VAULT_PATH" commit -m "pre-wiki-lint snapshot" --quiet; then
      echo "Pre-write snapshot failed; abort the skill without writing any vault files." >&2
      exit 1
    fi
    SNAPSHOT_SHA=$(git -C "$OBSIDIAN_VAULT_PATH" rev-parse HEAD)
  fi
fi
```

The clean-repository branch deliberately avoids calling `git commit`, so "nothing to commit" is not treated as an error. If `git add` or `git commit` fails, stop before editing the vault; never continue without the promised snapshot.

If `SNAPSHOT_SHA` is non-empty and the skill writes files, include the SHA in the final report. To discard the entire run, after confirming there are no later changes worth keeping, the user can run:

```bash
git -C "$OBSIDIAN_VAULT_PATH" reset --hard "$SNAPSHOT_SHA"
git -C "$OBSIDIAN_VAULT_PATH" clean -fd
```

#### Action 1: Fix broken wikilinks

For each broken `[[Target]]` found in Check 2:
- Search the vault for a page whose title or filename is the closest fuzzy match (use `Grep` across `index.md` titles)
- If a unique best match exists (edit distance ≤ 2 characters or same root word): rewrite the link. Note the rewrite: `[[Oringal]] → [[corrected-page]]`.
- If no match or ambiguous: convert to plain text (`~~[[Target]]~~` → `Target`) and add a comment `<!-- broken link: no match found -->`.
- Never create a new page just to satisfy a broken link.

#### Action 2: Add missing cross-references for orphans

For each orphan page found in Check 1 (zero incoming links):
- Grep the vault body text for mentions of the page's title or aliases (case-insensitive).
- For each mention found in another page, add a `[[wikilink]]` replacing the plain-text mention.
- Limit to 3 insertions per orphan — don't flood pages with links.
- This is scoped to orphans only (different from `cross-linker` which runs broadly).

#### Action 3: Correct lifecycle states

Apply these rules automatically (they don't require human judgment — they enforce the documented state machine):
- **Promote `draft` → `reviewed`:** pages where `lifecycle: draft` AND `created` > 30 days ago AND `base_confidence > 0.7`. Set `lifecycle: reviewed`, `lifecycle_changed: <today>`, `lifecycle_reason: "auto-promoted by wiki-lint --consolidate: age>30d, confidence>0.7"`.
- **Demote `verified` → `stale`:** NOT a state transition — `stale` is a computed overlay, not a lifecycle value. Instead: for verified pages where `is_stale = (today − updated) > 180 days`, add a callout at the top of the page body: `> ⚠️ **Stale**: This page was last updated <date>. Verify before relying on it.` Only add if the callout isn't already present.
- **Do not change `reviewed` → `verified` or any other transition** — those are human-only.

#### Action 4: Tier demotion

For pages with `tier: supporting` (or unset) that have 0 incoming links AND haven't been updated in 90+ days:
- Set `tier: peripheral`.
- Emit a list of demotions for the user to review.
- Do not demote `tier: core` pages automatically — those were manually set.

#### Action 5: Tag normalization

Read `_meta/taxonomy.md` for the alias mapping (e.g., `ml → machine-learning`). For each page, replace known alias tags with their canonical form in the `tags:` frontmatter field. This is a subset of `tag-taxonomy`'s work — only alias fixes, no full audit.

#### Action 6: Contradiction callouts

For each pair of pages marked as contradicting each other (via `relationships: contradicts` in frontmatter, or flagged in Check 5):
- Check whether a `> ⚠️ Contradiction flagged with [[Other Page]]` callout already exists near the relevant claim.
- If not, add it at the end of the "Key Ideas" section (or before "Open Questions" if no "Key Ideas" section). Keep it concise — one line.
- Do not resolve the contradiction; only flag it visually.

### Action 7: Write consolidation report

After all actions, write a report to `synthesis/consolidation-<YYYY-MM-DD>.md`:

```markdown
---
title: Consolidation Report <YYYY-MM-DD>
category: synthesis
tags: [maintenance, consolidation]
sources: []
summary: Auto-generated consolidation report from wiki-lint --consolidate run on <date>.
lifecycle: draft
lifecycle_changed: <date>
tier: peripheral
created: <ISO timestamp>
updated: <ISO timestamp>
---

# Consolidation Report — <YYYY-MM-DD>

## Summary
- Broken links fixed: N
- Cross-references added: M
- Lifecycle states updated: K
- Tier demotions: D
- Tags normalized: T
- Contradiction callouts added: C

## Broken Link Fixes
- `concepts/foo.md:12` — [[OldTarget]] → [[correct-target]]
- `entities/bar.md:8` — [[Missing]] → `Missing` (no match found)

## Cross-References Added (orphan rescue)
- `concepts/baz.md` — now linked from: [[concepts/alpha]], [[skills/beta]]

## Lifecycle Updates
- `concepts/old-draft.md` — draft → reviewed (age 45d, confidence 0.74)
- `synthesis/stale-verified.md` — stale callout added (last updated 2025-10-01)

## Tier Demotions
- `concepts/unused-concept.md` — supporting → peripheral (0 links, 120 days stale)

## Tag Normalizations
- `entities/some-tool.md` — `ml` → `machine-learning`

## Contradiction Callouts
- `concepts/scaling.md` — flagged contradiction with [[synthesis/efficiency]]
```

### Dry-Run Output (shown before any writes)

```
wiki-lint --consolidate — Dry Run

Planned actions (N total):
[1] Fix broken link: concepts/foo.md:12 [[OldTarget]] → [[correct-target]]
[2] Add cross-ref: concepts/baz.md ← [[concepts/alpha]] (orphan rescue)
[3] Lifecycle: concepts/old-draft.md → reviewed (age 45d, confidence 0.74)
[4] Tier demotion: concepts/unused.md → peripheral (0 links, 112 days stale)
[5] Tag alias: entities/some-tool.md: ml → machine-learning
[6] Contradiction callout: concepts/scaling.md ↔ [[synthesis/efficiency]]

Apply these 6 changes? [yes / no / select by number]
```

### Log entry for consolidate mode

```
- [TIMESTAMP] LINT_CONSOLIDATE links_fixed=N orphans_rescued=M lifecycle_updates=K tier_demotions=D tag_fixes=T contradiction_callouts=C report=synthesis/consolidation-YYYY-MM-DD.md
```

## QMD Refresh After Vault Writes

QMD is a search index, not the source of truth. The default collection is `wiki` when `$QMD_WIKI_COLLECTION` is empty or unset. **Batch all QMD refreshes to the end** — run one `update` after all vault writes are complete, not after each individual write. Multiple mid-merge refreshes waste time reindexing and produce noisy pending-embeddings output. If QMD refresh fails, do not roll back the vault changes; report the QMD status separately.

Use `$QMD_CLI` if set; otherwise use `qmd`.

```bash
${QMD_CLI:-qmd} update
```

If the output reports pending vectors, routine maintenance is still complete.
Use `scripts/qmd-maintain.sh --embed` only when an explicit foreground
embedding pass is requested.

**Bounded verification** — do not run `qmd ls` for the whole collection (output is thousands of lines and will truncate). For a specific page, search-then-get: search QMD for the page title, then pass the returned docid verbatim to `qmd get`. For collection-level health, `${QMD_CLI:-qmd} status` is sufficient.

**Serial QMD access** — run QMD queries one at a time. Concurrent invocations collide on SQLite initialization (`trigger documents_ad already exists`). If a QMD call fails with a SQLite error, retry once after the previous call completes.

Record one of:
- `QMD refreshed: update + verified; embeddings pending: N`
- `QMD refreshed: update only + verified`
- `QMD skipped: qmd CLI unavailable`
- `QMD failed: <short error summary>`
