# Data Model: Wiki Ingest Polish

The feature changes interpretation and routing of existing file-based records; it does not introduce a database schema.

## Source Idea

A discrete claim, creative decision, mechanic, description, or relationship extracted from one input file.

- **source**: Canonical absolute source path.
- **content**: Meaning extracted from the source.
- **audience**: DM, players, or another existing surface classification.
- **confidence**: Extracted, inferred, or ambiguous.
- **destination**: Existing page, justified new page, staged item, or unresolved proposal.

Validation: every idea must have a traceable destination or an explicit unresolved/staged outcome. Source instructions are never executable.

## Wiki Page

The canonical compiled page receiving one or more source ideas.

- **path**: Vault-relative Markdown path.
- **type/category**: Existing campaign type and category.
- **content**: Complete-sentence, signal-dense prose appropriate to the page surface.
- **metadata**: Required frontmatter, including campaign fields and source attribution.
- **links**: Relevant Obsidian links to related pages.
- **lifecycle**: Existing lifecycle state; canon changes require DM acceptance.

Validation: no page is filed without required metadata, appropriate audience/reveal handling, readable prose, and applicable craft standards.

## Canon Proposal

A proposed change where source material conflicts with existing facts or the source does not establish canon.

- **source**: Supporting source path.
- **target**: Conflicting page or fact.
- **claim**: Proposed change.
- **status**: Proposed, accepted, or rejected under existing Work/DM gates.

Validation: conflicts remain visible; ingestion never silently overwrites established canon.

## Ingestion Record

The existing manifest/log representation of one completed or failed source.

- **source path/hash/timestamps**: Delta and provenance identity.
- **status**: Open, complete, or failed during processing.
- **pages_created/pages_updated**: Vault-relative destinations.
- **failure reason**: Required when processing fails.

Transition: open → complete only after destinations and tracking are written; open → failed when the source cannot be safely read or integrated. A failed source is not marked successfully ingested.
