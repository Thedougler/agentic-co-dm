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

### User Story 4 - Dry Run and Diff Preview (Priority: P2)

Before any bulk operation commits changes, the agent can preview exactly what would change. The preview is a machine-readable diff or summary that the agent (or DM) can inspect before applying.

**Why this priority**: Bulk operations on a canonical wiki demand safety. A dry-run mode is the primary safeguard against unintended changes and is constitutionally required (safe automation, additive wiki).

**Independent Test**: Run a rename in dry-run mode. Verify the output lists every file and change that would occur, and that no files are actually modified on disk.

**Acceptance Scenarios**:

1. **Given** any bulk operation with a `--dry-run` flag, **When** invoked, **Then** the tool outputs a summary of files and changes without modifying any file, and exits successfully.
2. **Given** a dry-run output, **When** the agent inspects it, **Then** it contains enough detail (file path, line, old text, new text) to decide whether to proceed.

---

### Edge Cases

- What happens when the wiki vault path is not set or the vault directory does not exist? → The tool exits with a clear error and makes no changes.
- What happens when a file has encoding issues or is not valid UTF-8? → The tool skips the file, reports it, and continues processing other files.
- What happens when a replacement produces an empty wikilink `[[]]`? → The tool refuses the operation and reports the specific file/line.
- What happens when two concurrent bulk operations run? → File-level operations are atomic (write temp then rename); the tool does not hold cross-file locks but each file write is safe.
- What happens when the wiki is in staged-writes mode (`WIKI_STAGED_WRITES=true`)? → Bulk operations respect staging: new pages go to `_staging/`, existing page edits happen in-place (they are deterministic maintenance, not lore invention).

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

### Key Entities

- **Operation**: A single bulk action (rename, replace, frontmatter-update) with its parameters, scope filter, and dry-run flag.
- **Scope**: The set of files an operation targets, defined by directory path, glob pattern, or frontmatter filter.
- **Change Record**: A per-file report of what was or would be modified (file path, line numbers, old text, new text).

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A full-vault entity rename (touching 50+ files) completes in a single agent tool call instead of 100+ Read/Edit calls.
- **SC-002**: All bulk operations are idempotent — a second run on already-transformed files produces zero changes and reports "no changes needed."
- **SC-003**: No bulk operation produces invalid YAML frontmatter, broken wikilinks, or corrupted Obsidian markdown syntax, verified by `wiki-lint` passing after every operation.
- **SC-004**: Dry-run output matches actual changes — when a dry run is followed by a live run, the set of modified files and change counts are identical.
- **SC-005**: Agent token cost for a vault-wide rename drops by 90% or more compared to the current per-file Read/Edit approach.

## Assumptions

- The wiki vault uses UTF-8 encoded markdown files exclusively.
- Wikilink format follows Obsidian conventions (`[[target]]`, `[[target|display]]`, `![[embed]]`) — not standard markdown link format — unless `OBSIDIAN_LINK_FORMAT=markdown` is set in config, in which case standard markdown links are handled instead.
- The existing `remorph-*` scripts demonstrate the project's pattern for bulk transformations (Python scripts, packet-scoped, no lore rewrite). The new system generalizes this pattern.
- Operations target the resolved `OBSIDIAN_VAULT_PATH` directory.
- The `wiki-lint` script is available for post-operation validation.
- Bulk operations are maintenance/structural — they do not invent lore, change accepted facts, or require DM acceptance (per constitution principle XX: "safe deterministic maintenance").
