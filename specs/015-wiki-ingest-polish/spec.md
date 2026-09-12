# Feature Specification: Wiki Ingest Polish

**Feature Branch**: `015-wiki-ingest-polish`
**Created**: 2026-09-12
**Status**: Draft
**Input**: User description: "When ingesting content into the wiki, files represent ideas rather than finished notes; digest them into relevant pages and apply the same quality and formatting standards as new content, while preserving settled creative work."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Digest source ideas into wiki knowledge (Priority: P1)

As a Co-DM, I want ingested files treated as source material so the wiki contains polished, canonical knowledge rather than raw copies.

**Why this priority**: Prevents the wiki from becoming a collection of unfinished or duplicated notes.

**Independent Test**: Give ingestion a file containing ideas that map to existing pages and verify the resulting pages incorporate the ideas without leaving the source file as a competing wiki note.

**Acceptance Scenarios**:

1. **Given** a source file contains ideas related to one or more existing wiki pages, **When** ingestion completes, **Then** each relevant page is updated with the applicable ideas and the source is not promoted as an unedited standalone note.
2. **Given** a source contains ideas with no suitable existing page, **When** ingestion completes, **Then** a new page is created only when the idea meets wiki page standards and is connected to related pages.

### User Story 2 - Preserve settled creative intent (Priority: P2)

As a DM, I want ingestion to polish settled creative material without changing its established meaning.

**Why this priority**: Quality editing must not silently rewrite campaign intent or mechanics.

**Independent Test**: Ingest a source with explicit creative decisions and compare the resulting page for retained facts, intent, and mechanics.

**Acceptance Scenarios**:

1. **Given** a source states settled creative content, **When** it is digested, **Then** the resulting wiki content preserves that content while improving clarity, completeness, and conformity.
2. **Given** ingestion encounters an apparent factual conflict, **When** the page is updated, **Then** the conflict is surfaced as a canon proposal or unresolved issue rather than silently overwritten.

### User Story 3 - Apply all creation quality standards (Priority: P3)

As a wiki reader, I want ingested pages to meet the same content, prose, domain, and formatting standards as newly authored pages.

**Why this priority**: Consistent quality makes pages usable and citable regardless of origin.

**Independent Test**: Review ingested output against the applicable copy-writing, theatre-of-the-mind, D&D 5e mechanics, and Obsidian Markdown standards.

**Acceptance Scenarios**:

1. **Given** ingested content targets a domain with applicable standards, **When** the content is finalized, **Then** it passes those standards for prose, mechanics, audience, and Markdown structure.
2. **Given** a source includes incomplete, telegraphic, duplicated, or malformed material, **When** ingestion completes, **Then** the wiki output contains complete readable prose, resolved duplication where possible, and valid required metadata and links.

### Edge Cases

- A source contains ideas spanning multiple categories or pages; each idea is routed independently.
- A source repeats content already present; ingestion updates only where it improves or corrects the canonical page.
- A source has insufficient information to create a sound page; the material remains staged or is reported for later review rather than padded with invention.
- A source contains player-facing text mixed with DM-only facts, secrets, or mechanics; each is kept on the appropriate surface.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The ingestion process MUST treat each input file as source material containing ideas, not as a finished wiki page.
- **FR-002**: The process MUST identify the relevant existing wiki pages for each source idea and update those pages when a suitable target exists.
- **FR-003**: The process MUST create a new wiki page only when the source idea has sufficient coherent scope and meets required page standards.
- **FR-004**: The process MUST preserve settled creative intent, established facts, and stated D&D 5e mechanics during polishing.
- **FR-005**: The process MUST surface conflicts or uncertain canon as a proposal or explicit unresolved item and MUST NOT silently change canon.
- **FR-006**: The resulting content MUST satisfy the same applicable creation requirements as newly authored wiki content, including copy-writing, theatre of the mind, D&D 5e mechanics, and Obsidian Markdown standards.
- **FR-007**: The process MUST remove or resolve source-level duplication, fragments, malformed formatting, and agent shorthand in the resulting wiki content where the source supports doing so.
- **FR-008**: The process MUST keep DM-only information, player-facing text, mechanics, and other audience-specific material on their appropriate surfaces.
- **FR-009**: The process MUST maintain required frontmatter, complete-sentence prose, relevant links, and source attribution for every resulting wiki page.
- **FR-010**: The process MUST record ingestion status and source tracking according to existing wiki maintenance requirements.

### Key Entities

- **Source idea**: A discrete piece of meaning extracted from an input file for digestion.
- **Wiki page**: Canonical compiled knowledge updated or created from source ideas.
- **Canon proposal**: A suggested change requiring DM acceptance rather than silent canon mutation.
- **Audience surface**: The intended reader or presentation context for content, such as DM or players.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: In a review sample of 20 ingested files, 100% are handled as source material rather than copied into the wiki as unedited finished notes.
- **SC-002**: At least 95% of source ideas in a review sample have a traceable destination in an updated page, a justified new page, or an explicit staged/unresolved outcome.
- **SC-003**: 100% of sampled ingested pages pass required metadata, prose, link, and Markdown checks before being considered complete.
- **SC-004**: In a review sample of 20 files containing settled creative decisions, 100% retain their stated intent and mechanics without silent canon changes.
- **SC-005**: Two independent reviewers agree on pass/fail for at least 90% of sampled ingested outputs across applicable domain standards.
- **SC-006**: A DM can locate the polished result for a source file within 2 minutes using normal wiki retrieval.

## Assumptions

- Existing wiki standards and domain authorities remain the source of truth for quality decisions.
- The DM remains the authority for accepting canon proposals; ingestion does not grant silent canon-editing authority.
- Existing wiki tracking, indexing, and staging conventions are reused rather than replaced.
- Source files may contain multiple ideas and may update multiple pages.
- Creative polish may improve expression and structure but does not invent unsupported facts to fill gaps.
