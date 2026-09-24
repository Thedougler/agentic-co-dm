# Wiki Lint — Vault Checks

Reference for checks 1–14, run during full-vault lint and bulk repair. The deterministic script handles detection for HARD/soft keys; checks below add what it cannot detect. Run in order, report findings as you go.

**Scope:** skip `_archives/`, `_raw/`, `_readouts/`, `.obsidian/`. Redirect stubs (`redirects_to`) are skipped in orphan, frontmatter, and content checks. Reserved `README.md`, `AGENTS.md`, `index.md`, `log.md`, `hot.md` are operational, not content pages.

### 1. Orphaned Pages

Find pages with zero incoming wikilinks (except reserved operational files). Glob `.md` files, skip redirect stubs. Grep vault for `[[page-name]]` references. Fix: add wikilinks from existing pages that should reference the orphan.

### 2–3. Broken Wikilinks / Missing Frontmatter

Script detects via `broken_links` and `missing_frontmatter` keys. Repair in Page-Scoped step 4.

### 3a. Missing Summary (soft)

Every page should have `summary:` (1–2 sentences, ≤200 chars) for cheap retrieval. Soft warning — older pages predating this field are fine.

**Detect:** grep frontmatter for `^summary:`. Flag missing or >200 chars.

**Fix:** re-ingest or manually write a short summary.

### 4. Stale Content

**Detect:** compare `updated` timestamps to source modification times. Flag when sources modified after page last updated.

### 5. Contradictions

**Detect:** read related pages (shared tags, heavy cross-references). Look for conflicting claims — "however", "in contrast", "despite" may signal them.

**Fix:** add an "Open Questions" section noting the contradiction with both source references.

### 6. Index Consistency

**Detect:** compare `index.md` entries to actual files on disk. Check summary accuracy.

### 7. Provenance Drift

**Detect:** for pages with `provenance:` block or `^[inferred]`/`^[ambiguous]` markers, compute fractions. Thresholds:
- AMBIGUOUS > 15% → "speculation-heavy"
- INFERRED > 40% with no `sources:` → "unsourced synthesis"
- Hub pages (top 10 by incoming links) with INFERRED > 20% → "high-traffic questionable provenance"
- `provenance:` frontmatter > 0.20 off recomputed → "drift"
- Skip pages with no provenance block and no markers (fully extracted by convention).

**Fix:** ambiguous → re-ingest, resolve, or split to `synthesis/`. Unsourced → add `sources:` or label as synthesis. Hub drift → prioritize re-ingestion (widest blast radius). Frontmatter drift → update to match recomputed.

### 8. Fragmented Tag Clusters

**Detect:** for each tag on ≥5 pages, compute `cohesion = actual_links / (n × (n−1) / 2)`. Flag cohesion < 0.15.

**Fix:** run `cross-linker` on the fragmented tag. Large groups (n>15) → consider sub-tags.

### 9. Visibility Tag Consistency

**Detect:**
- Grep bodies for PII patterns (`password`, `api_key`, `secret`, `token`, `ssn`, `email:`, `phone:` + actual value). Flag if page lacks `visibility/pii` or `visibility/internal`.
- Flag `visibility/pii` pages missing `sources:`.
- Flag `visibility/` entries in `_meta/taxonomy.md` (system tags must not be in taxonomy).

**Fix:** add appropriate visibility tag; add provenance or escalate; remove from taxonomy.

### 10. Misc Promotion Candidates

**Detect:** glob `$OBSIDIAN_VAULT_PATH/misc/*.md`. Read `affinity` frontmatter. Flag pages with any project score ≥ 3.

**Fix:** move to `projects/<project>/references/` (or appropriate category), update `category`, remove `promotion_status`, update vault backlinks.

### 11. Synthesis Gaps

**Detect:** pick 10–15 frequently linked concepts. For each pair, count pages linking both. Flag co-occurrence ≥ 3 with no synthesis page.

**Fix:** run `/wiki-synthesize`.

### 13. Typed Relationships

Script detects via `typed_relationships` key. Fix: invalid type → correct only if absent from both framework and owner sets; never replace a valid owner type with `related_to`. Broken target → update/remove. Self-reference → remove.

### 14. Duplicate Pages

Every fact has one owner page. Find pages that duplicate or fragment a concept's authority.

**Completion criterion:** every flagged pair ends as one canonical page, or as distinct situations with `identity.status` `"resolved"`.

**Detect:** from live pages (excluding `_archives/`, `_raw/`, `_readouts/`, redirects), extract `title`, `aliases`, `tags`, `summary`. Compute similarity (title overlap, edit distance, substring containment, alias cross-match — same signals as `wiki-dedup` Step 2a–2b, frontmatter only, no full reads). Flag ≥ 0.75 (HIGH ≥ 0.90, MEDIUM 0.75–0.89). Skip pairs linked by `redirects_to`. Script's `duplicate_stems` catches filename collisions; this check catches semantic duplicates.

**Verdicts:** `merge` (same concept, different name) | `digest` (facts belong on existing canonicals) | `differentiate` (scanner collision, different table jobs).

**Manual merges only.** Read both files, decide, edit through Edit/Write tools.

#### Differentiate (scanner collision, different table jobs)

Read both bodies and their linked owners. Rewrite each page from those facts until each answers a different objective. `identity.status` `"resolved"` is the check.

#### Merge (same concept → one canonical)

1. **Pick canonical:** more incoming links → richer content → more sources.
2. **Merge into canonical:** absorb secondary's title as alias, dedup tags (cap 5 domain + system), merge sources/relationships/body (mark synthesis `^[inferred]`), `updated` → now.
3. **Delete secondary.** No redirect stubs — aliases absorb the old name.
4. **Rewrite wikilinks vault-wide:** `[[secondary]]` → `[[canonical]]` (preserve display text, skip code blocks).
5. **Update tracking:** `index.md`, `.manifest.json` (`merged_into` on secondary), `hot.md`.

#### Digest (facts belong elsewhere)

1. Identify canonical homes for each fact.
2. Merge new facts into canonicals (same mechanics as Merge step 2, scoped to added facts).
3. Delete digested page. No redirect stubs.
4. Rewrite wikilinks to canonical targets.

#### Scope in repair flows

- **Page-scoped:** check if named page duplicates or is duplicated by another. Resolve if found.
- **Bulk:** full scan, resolve one at a time, commit between. Use JSON `backlog` smallest-file-first.
- **`--check`:** report with verdicts, do not resolve.

## Report Format

Structure findings under headings by check: `### Check Name (N found)`. Each finding: `` `path:line` — description ``. Group by severity (HARD before soft). Append summary counts to `log.md` per the format in SKILL.md.
