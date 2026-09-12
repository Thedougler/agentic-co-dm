# Quickstart: Wiki Ingest Polish

## Prerequisites

From the repository root:

```bash
python --version
```

Use the configured campaign vault and existing wiki maintenance setup. The feature uses the contract in [contracts/ingest-quality.md](contracts/ingest-quality.md) and entities in [data-model.md](data-model.md).

## Validation scenarios

### 1. Existing-page integration

Provide a small source file containing a new idea plus a repeated fragment about an existing page. Run the normal `wiki-ingest` flow. Verify the target page contains the useful idea in complete prose, the repeated fragment is not duplicated, and the source is recorded in provenance.

### 2. New-page threshold

Provide a coherent idea with no existing target. Verify a standards-compliant page is created, linked to related pages, and tracked. Provide an incomplete fragment separately; verify it remains staged or unresolved rather than becoming padded content.

### 3. Intent and conflict preservation

Provide a source with an explicit creative decision and a conflicting claim about an existing page. Verify the decision is retained and the conflict is represented as a proposal or ambiguity, not a silent overwrite.

### 4. Surface quality

Provide source text mixing DM facts, player-safe narration, and a D&D 5e test. Verify the output keeps each item on its correct surface; spoken text has no secrets or DCs; mechanical tests include the required check/save, DC, and consequences; and the page uses valid frontmatter and Obsidian links.

### 5. Tracking and failure

Run ingestion on a readable source and an unreadable/empty source. Verify the readable record is complete with created/updated destinations, while the failed record has a reason and is not marked successfully ingested.

## Repository checks

After implementation, run the smallest applicable existing validators for the changed skill and fixture output. A successful check must demonstrate observable routing, quality, provenance, and failure behavior; do not rely on string snapshots of the skill instructions.
