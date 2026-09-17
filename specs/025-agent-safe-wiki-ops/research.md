# Research: Agent-Safe Wiki Operations

**Branch**: `025-agent-safe-wiki-ops` | **Date**: 2026-09-17

## Identity Resolution

### Decision: Use existing frontmatter, manifest, filenames, wikilinks, and QMD-backed content similarity as identity signals — no new dependency or redirect routing.

**Rationale**: Every identity signal needed already exists in the repository. Frontmatter has `title`, `type`, `lifecycle`, `aliases`; manifest has source provenance and `pages_produced`; wikilinks provide backlink graph; filenames provide stem-based matching; QMD is already installed and provides content similarity without adding a dependency. Legacy `redirects_to` pages are not valid routing; they are lint errors that must be removed during repair. The duplicate_stems check in `tools/lint_wiki.py` already detects basename collisions but doesn't classify ambiguity. QMD similarity plus discrete signals classifies same-entity candidates before agents order work by filename or file size.

**Alternatives considered**:
- New embedding service: Adds dependency and CI friction; QMD already covers this repository.
- Stdlib-only body similarity: Useful as a test seam/fallback, but insufficient for the spec's QMD-backed overlap requirement.
- Manual identity registry: Extra maintenance burden, drifts from actual files.
- Redirect stubs: Rejected by clarification; the vault policy is zero redirect files.

### Decision: Three-state classification — `resolved`, `ambiguous`, `distinct`.

**Rationale**: Matches spec FR-001. `resolved` = one canonical page, proceed. `ambiguous` = multiple candidates for same entity, blocks mutation (FR-002). `distinct` = different entities sharing a stem or partial name, safe to ignore. A legacy redirect stub is not a resolved identity; lint reports it as an error and deterministic repair removes it after inbound links are rewritten. The Fisk incident (e-12) was caused by skipping this step entirely and ordering by file size.

**Alternatives considered**:
- Binary match/no-match: Too coarse — can't distinguish "same entity, different pages" from "different entities, similar names."

## Mutation Operations

### Decision: Python library in `tools/wiki_ops/` with CLI subcommands exposed via `scripts/wiki-bulk-ops`.

**Rationale**: `wiki-bulk-ops` already has the infrastructure: `parse_frontmatter()`, `parse_fields()`, `atomic_write()`, `rewrite_links()`, `link_repair()`, `rename()`. Adding mutation subcommands (replace_section, set_frontmatter, rename_or_merge_page) composes naturally. Library code in `tools/wiki_ops/` keeps complex logic testable independently of CLI argument parsing.

**Alternatives considered**:
- New separate script: Fragments the CLI surface. Agents already know `wiki-bulk-ops`.
- Extending `tools/lint_wiki.py`: Wrong surface — lint_wiki is read-only; mutations need a write-capable entry point.

### Decision: Content-hash preconditions for section mutations using hashlib.sha256 on section content.

**Rationale**: Prevents stale writes (FR-009). Agent reads section, gets hash, submits mutation with hash. If file changed between read and write, hash mismatch → rejection. stdlib hashlib, zero dependencies. Per-section hash is more precise than whole-file hash — parallel non-overlapping edits don't conflict.

**Alternatives considered**:
- File mtime: Race-prone, filesystem dependent.
- Whole-file hash: Too coarse — rejects non-conflicting edits to different sections.
- Line-number anchoring: Fragile — any insertion above shifts all line numbers (root cause of e-21, e-23).

### Decision: Heading-path selectors for section targeting (e.g., `["Active Agenda", "Milestones"]`).

**Rationale**: Heading paths are semantic, stable across content edits within a section, and composable. The existing markdown structure uses `#`-level headings as section boundaries. A heading path like `["Current State", "Internal fracture"]` uniquely identifies a section regardless of line numbers. This is what the spec means by "semantic anchors" (FR-008).

**Alternatives considered**:
- Line ranges: Fragile (e-21, e-23).
- Regex patterns: Non-deterministic, hard to validate overlap.
- CSS-like selectors: Over-engineered for markdown headings.

## Index Operations

### Decision: Parse index.md entries by regex pattern `- \[\[slug\]\] — description` and operate on entries by slug.

**Rationale**: The index is a long-line file where entries follow the pattern `- [[slug]] — summary ( #tag1 #tag2)`. Entry-level operations (replace, remove, insert-sorted) need only parse this structure. The existing `wiki-bulk-ops` link regex (`LINK_RE`) can extract wikilinks. Writing back uses `atomic_write()`.

The index is 15 lines / 107KB — entries are separated by newlines but rendered as very long lines. Parsing by the `- [[` prefix pattern is reliable.

**Alternatives considered**:
- Whole-file regex substitution: What agents were doing (e-16) — fragile on a 107KB file.
- JSON index: Migration cost, breaks existing consumers.
- Database: Overkill for a flat list.

## Manifest Identity Transitions

### Decision: Add page-level `merged_into` records in manifest alongside existing source-level provenance.

**Rationale**: The manifest currently tracks source → pages_produced (source-level). Page merges need page-level tracking: "fisks-captains.md merged_into fisks-fleet.md on date X." This is orthogonal to source provenance — a page can be both a source-ingest output and a merge target. The existing `scripts/manifest.py` `upsert` command can be extended with a `merge` subcommand that records the transition.

**Alternatives considered**:
- Separate merge-history file: Extra file to maintain, not co-located with provenance.
- Overwriting pages_produced entries: Loses provenance history (violates Constitution XIX).

## Template Contracts

### Decision: YAML contract files co-located with templates at `wiki/templates/contracts/<type>.yml`.

**Rationale**: Each contract derives from its template's structure but adds machine-readable semantics (required/optional/conditional, lifecycle applicability). Co-location with templates means the contract and template evolve together. YAML is already used in the project (rules/registry.yml) and parsed with PyYAML (added by 024).

Section optionality is derived from template comments: `<!-- Omit unused sections -->`, `<!-- Omit when unused -->`, `<!-- Omit this entire section for dormant or dissolved factions -->`. The contract makes these explicit rather than requiring comment parsing at lint time.

**Alternatives considered**:
- JSON Schema: More verbose, less readable for section-level semantics.
- Inline template annotations: Changes the template files themselves (spec assumption violation).
- Convention-based (e.g., all h3+ optional): Too coarse — some h2 sections are optional, some h3 are required.

### Decision: Lifecycle-conditional sections use a `when` field mapping lifecycle values to required/optional/omit.

**Rationale**: The faction template has sections that should be omitted for dormant/dissolved factions (e.g., "Faction Turn", "Current Turn"). Rather than a flat required/optional flag, a `when` field captures lifecycle-dependent behavior: `{active: required, dormant: omit, dissolved: omit, default: optional}`. This directly addresses e-14 (579 false-mandatory findings from ignoring lifecycle).

**Alternatives considered**:
- Separate contract per lifecycle: Duplicates the non-conditional sections.
- Skip-list approach: Less expressive — can't distinguish "required when active" from "optional always."

## Scoped Lint

### Decision: Scope object as a typed specification passed to existing `tools/lint_wiki.py` and `tools/creative_lint/engine.py`.

**Rationale**: The spec defines a scope object accepting files, directory, entity type, resolved identity set, changed files, or task bundle (FR-003). This filters the file iterator before any check runs. `lint_wiki.py` already iterates with `load()` which returns all pages — inserting a scope filter before the check loop is minimal change. 024's engine already accepts file paths.

**Alternatives considered**:
- Post-filter (run all, then filter output): Wastes compute on out-of-scope files (the current e-18 problem).
- Separate scoped lint script: Fragments the CLI surface.

## Transaction and Finalization

### Decision: Transaction context manager that collects mutations, validates the set, applies atomically, then runs finalization once.

**Rationale**: The spec requires multi-file transactions with deferred finalization (FR-013). A Python context manager accumulates mutations, checks for overlapping targets, resolves all preconditions, writes all files (via `atomic_write`), then triggers index update + manifest update + QMD refresh once. If any precondition fails, none are written. This directly addresses e-19 (repeated QMD refreshes).

QMD refresh is the most expensive step. Deferring it to transaction end means one refresh per transaction instead of one per file write.

**Alternatives considered**:
- Per-file write with deferred refresh only: Doesn't catch overlapping mutations across files.
- Database-style WAL: Overkill for filesystem operations on ~200 files.

## Repair Classes

### Decision: Three repair classes on lint findings — `diagnostic`, `human_repair`, `deterministic_repair`.

**Rationale**: Maps to spec FR-011. `diagnostic` = informational only (no action). `human_repair` = needs judgment (e.g., rewrite prose). `deterministic_repair` = can be automated with a typed mutation (e.g., fix broken link, add missing frontmatter field). Only `deterministic_repair` findings produce typed mutation actions. This is the gate between "lint found it" and "agent can fix it."

**Alternatives considered**:
- Binary auto/manual: Loses the diagnostic-only case (findings that are pure information, like INFO-level creative lint).

## Policy Single-Ownership

### Decision: Document policy ownership in a YAML registry at `docs/agents/policy-owners.yml`.

**Rationale**: A single file listing each policy rule, its authoritative owner file, and what it governs. Lower-level skills reference this registry rather than restating rules. A simple `check-policy-conflicts` script can grep for restated rules and flag contradictions. This directly addresses e-20 (contradictory acceptance semantics).

**Alternatives considered**:
- Convention-only (no registry): Can't automate conflict detection.
- Inline ownership markers: Scattered, hard to audit.
