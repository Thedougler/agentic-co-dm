# Feature Specification: Wiki Bulk Operations

**Feature Branch**: `023-wiki-bulk-ops`

**Created**: 2026-09-17

**Status**: Draft

**Input**: User description: "Agents working within the llm-wiki need token efficient and idempotent methods of performing safe bulk operations in the llm-wiki that preserves the obsidian markdown syntax and wiki links such as changing the name of a thing on every file it appears etc, or basically any other deterministic action that costs significant tokens agents might undertake while editing markdown files within the llm-wiki"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Rename an Entity Across the Wiki (Priority: P1)

An agent needs to rename a wiki entity (e.g., an NPC whose name changed from "Korvash" to "Korveth"). This requires updating the page filename, frontmatter title, every `[[Korvash]]` wikilink, every `[[Korvash|display text]]` piped wikilink, and body-text references — across all wiki pages — without corrupting markdown structure or inventing content.

**Why this priority**: Renaming is the most common expensive bulk operation agents perform today. Each rename currently costs hundreds of tool calls (one Read + one Edit per file per occurrence) and is the highest-value target for token savings.

**Independent Test**: Rename a test entity in a small wiki subset. Verify all wikilinks resolve, frontmatter is valid YAML, no markdown structure is broken, and no content outside the rename target is altered.

**Acceptance Scenarios**:

1. **Given** an entity "old-name" with pages linking to it, **When** the agent invokes the rename operation with old name and new name, **Then** all `[[old-name]]` links become `[[new-name]]`, piped links `[[old-name|X]]` become `[[new-name|X]]`, the source page filename and title update, and no other content changes.
2. **Given** a rename that would collide with an existing page, **When** the agent invokes the rename, **Then** the operation refuses with a clear error naming the collision and makes zero changes.
3. **Given** a rename where "old-name" appears as a substring of another entity (e.g., "old-name-kin"), **When** the rename runs, **Then** only exact wikilink targets and standalone references change — partial matches within other entity names are preserved.

---

### User Story 2 - Bulk Find-and-Replace with Markdown Safety (Priority: P1)

An agent needs to perform a deterministic text substitution across many wiki files — for example, standardizing a heading name, fixing a repeated typo in a tag, or updating a term per AGENTS.md vocabulary changes. The operation must not break YAML frontmatter, wikilinks, or Obsidian callout syntax.

**Why this priority**: Agents currently spend significant tokens opening, reading, editing, and closing files one at a time for simple deterministic replacements. This is the general-purpose primitive that many bulk operations reduce to.

**Independent Test**: Run a substitution on a test set of wiki pages. Verify only the targeted text changed, frontmatter remains valid YAML, all wikilinks still resolve, and Obsidian callout syntax is intact.

**Acceptance Scenarios**:

1. **Given** a search term and replacement term, **When** the agent invokes the bulk replace, **Then** all occurrences in body text across matching files are replaced and a summary reports files changed and occurrence count.
2. **Given** a replacement that would alter text inside a wikilink target (e.g., replacing "foo" when `[[foobar]]` exists), **When** the operation runs with default settings, **Then** wikilink targets are not altered unless explicitly scoped to include them.
3. **Given** a replacement that would produce invalid YAML in frontmatter, **When** the operation runs, **Then** frontmatter zones are excluded by default and the agent is warned.

---

### User Story 3 - Bulk Frontmatter Update (Priority: P2)

An agent needs to add, rename, or update a frontmatter field across many wiki pages matching a filter (e.g., all pages with `type: npc`, or all pages in `entities/`). Examples: adding a new required field, changing a tag value, normalizing date formats.

**Why this priority**: Frontmatter changes are schema-level operations that touch many files with identical logic. Doing them one file at a time is pure waste.

**Independent Test**: Add a field to all `type: npc` pages. Verify the field is present on every matching page, existing fields are unchanged, and YAML remains valid.

**Acceptance Scenarios**:

1. **Given** a filter (`type: npc`) and a frontmatter mutation (set `connections_reviewed: false`), **When** the agent invokes the bulk frontmatter update, **Then** every matching page has the field added/updated and non-matching pages are untouched.
2. **Given** a frontmatter rename (field `relationships` to `connections`), **When** the operation runs, **Then** the old key is removed, the new key holds the same value, and no body content changes.

---

### User Story 4 - Broken Link Repair (Priority: P1)

An agent needs to resolve existing broken wikilinks across the vault — links pointing to pages that were renamed, moved, or deleted without updating references. The operation auto-resolves targets using known rename history (git log, frontmatter aliases) and fuzzy matching, and accepts an explicit old→new mapping for ambiguous cases. Unresolvable links are reported, not silently dropped.

**Why this priority**: Agents report 1,000+ broken links as existing baseline issues. This is the primary motivating problem for bulk ops — the vault's structural integrity depends on link resolution, and fixing these one-at-a-time is prohibitively expensive.

**Independent Test**: Introduce known broken links in a test wiki subset. Run the repair operation. Verify resolved links point to existing pages, unresolvable links are reported, no valid links are altered, and frontmatter/markdown structure is preserved.

**Acceptance Scenarios**:

1. **Given** broken wikilinks where the target page was renamed (detectable via git history or frontmatter aliases), **When** the agent invokes broken-link repair, **Then** links are updated to the current page name and a summary reports each resolution.
2. **Given** broken wikilinks with multiple candidate targets (fuzzy match ambiguity), **When** the operation runs without an explicit mapping, **Then** ambiguous links are reported with candidate suggestions but not auto-resolved.
3. **Given** an explicit old→new mapping file, **When** the agent invokes broken-link repair with the mapping, **Then** mapped links are resolved per the mapping and unmapped broken links are reported separately.
4. **Given** broken links where the target page no longer exists and no candidate is found, **When** the repair runs, **Then** those links are reported as unresolvable and left unchanged.

---

### User Story 5 - Bulk Tag Normalization (Priority: P2)

An agent needs to normalize tags across the vault — renaming tags to match the controlled vocabulary in `_meta/taxonomy.md`, removing invalid/deprecated tags, and merging variant spellings (e.g., `dnd-5e` vs `dnd5e` vs `D&D-5e`). The operation works through frontmatter `tags:` fields and must not alter body content.

**Why this priority**: Tag inconsistency is a top wiki-lint finding category. Tags are frontmatter fields, so this is a specialized case of bulk frontmatter update with taxonomy awareness.

**Independent Test**: Introduce variant tag spellings in a test subset. Run tag normalization against a taxonomy file. Verify all tags match the canonical vocabulary, no body content changes, and frontmatter remains valid YAML.

**Acceptance Scenarios**:

1. **Given** a taxonomy file defining canonical tags and their aliases, **When** the agent invokes tag normalization, **Then** all alias tags in frontmatter are replaced with their canonical form and a summary reports changes per file.
2. **Given** tags not present in the taxonomy (unknown tags), **When** the operation runs, **Then** unknown tags are reported but not removed unless explicitly flagged for removal.
3. **Given** duplicate tags on a page after normalization (two aliases mapped to the same canonical tag), **When** the operation runs, **Then** duplicates are collapsed to a single instance.

---

### User Story 6 - Dry Run and Diff Preview (Priority: P2)

Before any bulk operation commits changes, the agent can preview exactly what would change. The preview is a machine-readable diff or summary that the agent (or DM) can inspect before applying.

**Why this priority**: Bulk operations on a canonical wiki demand safety. A dry-run mode is the primary safeguard against unintended changes and is constitutionally required (safe automation, additive wiki).

**Independent Test**: Run a rename in dry-run mode. Verify the output lists every file and change that would occur, and that no files are actually modified on disk.

**Acceptance Scenarios**:

1. **Given** any bulk operation with a `--dry-run` flag, **When** invoked, **Then** the tool outputs a summary of files and changes without modifying any file, and exits successfully.
2. **Given** a dry-run output, **When** the agent inspects it, **Then** it contains enough detail (file path, line, old text, new text) to decide whether to proceed.

---

### User Story 7 - Subfolder MOC Generation (Priority: P2)

An agent needs to generate or regenerate `_index.md` Map of Content (MOC) files for content subfolders in the wiki vault. Each MOC has a player-friendly `title:` in frontmatter and serves as both a subindex for llm-wiki agent retrieval and a visual table of contents for users browsing in Obsidian or on GitHub. MOCs are scoped to content category folders only — infrastructure folders (`_archive/`, `_raw/`, `_meta/`, `.obsidian/`, `attachments/`, `templates/`) are excluded.

**Why this priority**: Folder-level MOCs make the vault navigable for human readers in Obsidian and on GitHub, while giving agents a lightweight subindex that avoids loading the full root `index.md`. Currently no subfolder has a `_index.md`; every folder is opaque without opening individual pages.

**Independent Test**: Run MOC generation on a test wiki subset with known pages. Verify each content folder has a `_index.md` with valid frontmatter, a player-friendly title, wikilinks to all contained pages, and no links to pages in other folders. Verify infrastructure folders have no `_index.md`. Verify idempotent re-run produces zero changes.

**Acceptance Scenarios**:

1. **Given** a content folder containing wiki pages, **When** the agent invokes MOC generation, **Then** a `_index.md` is created (or updated) in that folder with valid frontmatter including a player-friendly `title:`, wikilinks to every page in the folder, and standard llm-wiki required frontmatter fields.
2. **Given** a content folder with nested subfolders (e.g., `entities/` containing `entities/npc/`, `entities/place/`), **When** MOC generation runs, **Then** the parent folder's MOC links to child folder MOCs and the child folder MOCs list their own pages.
3. **Given** infrastructure folders (`_archive/`, `_raw/`, `_meta/`, `.obsidian/`, `attachments/`, `templates/`), **When** MOC generation runs, **Then** no `_index.md` is created in those folders.
4. **Given** an existing `_index.md` that is already up to date, **When** MOC generation runs again, **Then** zero changes are reported (idempotent).

---

### Edge Cases

- What happens when the wiki vault path is not set or the vault directory does not exist? → The tool exits with a clear error and makes no changes.
- What happens when a file has encoding issues or is not valid UTF-8? → The tool skips the file, reports it, and continues processing other files.
- What happens when a replacement produces an empty wikilink `[[]]`? → The tool refuses the operation and reports the specific file/line.
- What happens when two concurrent bulk operations run? → File-level operations are atomic (write temp then rename); the tool does not hold cross-file locks but each file write is safe.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The system MUST provide a rename operation that updates a page filename, its frontmatter title, and all wikilink references across the vault in a single invocation.
- **FR-002**: The system MUST provide a bulk find-and-replace operation that substitutes text across matching files while preserving YAML frontmatter integrity and wikilink syntax.
- **FR-003**: The system MUST provide a bulk frontmatter mutation operation that can add, update, rename, or remove frontmatter fields on pages matching a filter.
- **FR-004**: Every bulk operation MUST support a dry-run mode that reports planned changes without modifying files.
- **FR-005**: Every bulk operation MUST be idempotent — running the same operation twice with the same inputs produces the same result and does not corrupt data.
- **FR-006**: The system MUST preserve Obsidian markdown syntax: wikilinks (`[[target]]`, `[[target|display]]`), embeds (`![[file]]`), callouts (`> [!type]`), and YAML frontmatter delimiters (`---`).
- **FR-007**: The system MUST report a summary of changes: files scanned, files modified, occurrences changed, files skipped (with reason).
- **FR-008**: The system MUST exit with distinct exit codes for success (0), no changes needed (0), validation error (1), and partial failure (2).
- **FR-009**: The system MUST refuse operations that would produce broken wikilinks (empty targets, unresolved collisions) and report the specific conflict.
- **FR-010**: Operations MUST be agent-shaped: arguments in, text or JSON out, errors on stderr, per constitution principle VI.
- **FR-011**: The system MUST support file-path filtering (glob patterns or directory scope) so operations can target subsets of the vault.
- **FR-012**: The system MUST handle piped wikilinks (`[[target|display]]`) correctly during renames — updating the target while preserving the display text.
- **FR-013**: The system MUST provide a broken-link repair operation that detects broken wikilinks, auto-resolves targets using known rename history (git log, frontmatter aliases) and fuzzy matching, accepts an explicit old→new mapping for overrides, and reports unresolvable links without altering them.
- **FR-014**: The broken-link repair operation MUST NOT auto-resolve ambiguous matches (multiple candidates) unless an explicit mapping is provided; ambiguous cases MUST be reported with candidate suggestions.
- **FR-015**: The system MUST provide a tag normalization operation that canonicalizes frontmatter tags against a taxonomy file, merges aliases, collapses duplicates, and reports unknown tags without removing them.
- **FR-016**: The system MUST provide an orphan detection report that lists pages with no incoming wikilinks; this is report-only and MUST NOT auto-delete or auto-link pages.
- **FR-017**: The system MUST provide a MOC generation operation that creates or regenerates `_index.md` files in content subfolders with a player-friendly `title:` in frontmatter, wikilinks to all contained pages, and links to child folder MOCs where nested subfolders exist. The operation is fully idempotent — each run regenerates the MOC from current folder contents; manual edits to `_index.md` are not preserved.
- **FR-018**: MOC generation MUST target only content category folders (e.g., `entities/`, `journal/`, `synthesis/`, and type subfolders like `entities/npc/`) and MUST NOT create `_index.md` in infrastructure folders (`_archive/`, `_raw/`, `_meta/`, `.obsidian/`, `attachments/`, `templates/`).
- **FR-019**: Generated `_index.md` files MUST include all required llm-wiki frontmatter fields (`title`, `category`, `tags`, `sources`, `created`, `updated`) and MUST be searchable within Obsidian.
- **FR-020**: The `title:` field in generated MOCs MUST be derived from a static map of known folder names to player-friendly human-readable titles (e.g., `npc` → "Non-Player Characters", `place` → "Places", `entities` → "Entities"). Unmapped folder names MUST fall back to title-cased folder name.
- **FR-021**: MOC body content MUST list pages as a flat alphabetical list of piped wikilinks using each page's frontmatter `title:` as display text (e.g., `[[kebab-name|Page Title]]`). Pages without a `title:` field MUST fall back to the filename.
- **FR-022**: MOC generation MUST update the root `index.md` to include wikilinks to all top-level `_index.md` MOC files, integrating subfolder navigation into the master index.

### Key Entities

- **Operation**: A single bulk action (rename, replace, frontmatter-update, broken-link-repair) with its parameters, scope filter, and dry-run flag.
- **Scope**: The set of files an operation targets, defined by directory path, glob pattern, or frontmatter filter.
- **Change Record**: A per-file report of what was or would be modified (file path, line numbers, old text, new text).
- **MOC (_index.md)**: A Map of Content file in a content subfolder that serves as both an agent subindex and a human-browsable table of contents, with player-friendly title and wikilinks to folder contents.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A full-vault entity rename (touching 50+ files) completes in a single agent tool call instead of 100+ Read/Edit calls.
- **SC-002**: All bulk operations are idempotent — a second run on already-transformed files produces zero changes and reports "no changes needed."
- **SC-003**: No bulk operation increases wiki-lint finding counts in any category — verified by comparing `wiki-lint` results before and after every operation (delta-based, no regressions).
- **SC-004**: Dry-run output matches actual changes — when a dry run is followed by a live run, the set of modified files and change counts are identical.
- **SC-005**: Agent token cost for a vault-wide rename drops by 90% or more compared to the current per-file Read/Edit approach.

## Clarifications

### Session 2026-09-17

- Q: Should the spec include a dedicated broken-link repair operation that resolves existing broken wikilinks, or are rename and replace sufficient primitives? → A: Add a dedicated broken-link repair operation (auto-resolve stale targets from known renames/fuzzy match + manual mapping fallback).
- Q: Should SC-003 mean "no new issues introduced" (delta-based) or "zero total findings" (absolute-clean)? → A: Delta-based — operation must not increase wiki-lint finding count in any category (no regressions).
- Q: Which wiki-lint finding categories beyond broken links should bulk ops address? → A: Broken links + tag normalization as operations; orphan detection as report-only (no auto-fix); index rebuild out of scope (existing tooling).
- Q: Which wiki subfolders should receive `_index.md` MOC files — content folders only, or also infrastructure folders? → A: Content folders only (entities/, journal/, synthesis/, and their type subfolders). Infrastructure folders (_archive/, _raw/, _meta/, .obsidian/, attachments/, templates/) are excluded.
- Q: Should MOC generation be a re-runnable idempotent operation or a one-time scaffold? → A: Auto-regenerate from folder contents each run (idempotent). No manual edits survive — the MOC is fully derived from current folder state.
- Q: How should the player-friendly `title:` be derived for each folder's MOC? → A: Static map of known folder names to human-readable titles (e.g., npc → "Non-Player Characters", place → "Places"). No taxonomy lookup dependency.
- Q: Should the MOC body list pages as a flat alphabetical list or grouped by frontmatter field? → A: Flat alphabetical list using piped wikilinks with the page's `title:` as display text (e.g., `[[kebab-name|Page Title]]`).
- Q: Should the root `index.md` be updated by MOC generation to link to the new `_index.md` files? → A: Yes. MOC generation also updates root `index.md` to link to top-level `_index.md` MOC files.

## Assumptions

- The wiki vault uses UTF-8 encoded markdown files exclusively.
- Wikilink format follows Obsidian conventions (`[[target]]`, `[[target|display]]`, `![[embed]]`) — not standard markdown link format — unless `OBSIDIAN_LINK_FORMAT=markdown` is set in config, in which case standard markdown links are handled instead.
- The existing `remorph-*` scripts demonstrate the project's pattern for bulk transformations (Python scripts, packet-scoped, no lore rewrite). The new system generalizes this pattern.
- Operations target the resolved `OBSIDIAN_VAULT_PATH` directory.
- The `wiki-lint` script is available for post-operation validation.
- Bulk operations are maintenance/structural — they do not invent lore, change accepted facts, or require DM acceptance (per constitution principle XX: "safe deterministic maintenance").
