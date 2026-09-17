# Quickstart: Complete Ingest Context

## Prerequisites

From the repository root, after implement lands the skill change and fixture check:

```bash
python3 --version
.venv/bin/python specs/018-complete-ingest-context/fixtures/check.py
```

Use the contract in [contracts/complete-ingest-context.md](contracts/complete-ingest-context.md) and entities in [data-model.md](data-model.md). Fixture sources belong under `fixtures/sources/`; a tiny staging + legacy + wiki layout belongs under `fixtures/vault/`.

The check asserts observable page and record outcomes. Do not replace it with a string snapshot of `wiki-ingest` instructions.

## Validation scenarios

### 1. Staging relative is read

Primary: `fixtures/sources/01-primary.md` names or links `01-related.md` in staging. Only the related file says the harbor bell is cracked.

**Observed:** Ingest record lists `01-related.md` as a staging read. Compiled page includes the cracked-bell fact. Primary is not marked complete before that read.

### 2. Legacy variant is read even when staging also hits

Primary subject also exists as a staging sibling and as an older legacy note with extra color (the bell’s green verdigris) absent from the primary.

**Observed:** Record lists both a staging read and a legacy read. Compiled page keeps uncontradicted verdigris. Legacy note is not filed as its own wiki page.

### 3. Newest decision wins; older contradiction is not silent

Newest primary: the lighthouse is black. Older variant: the lighthouse is white.

**Observed:** Compiled page uses black. White is a proposal or `^[ambiguous]` item in the record, not an overwrite. Record names the recency conflict.

### 4. Miss does not stall

Primary names `missing-ally.md`. File does not exist in staging or legacy.

**Observed:** Record lists the miss. Primary still `complete` from found evidence (or `failed` only for an unrelated primary-read failure).

### 5. No related hits still records the search

Primary with no links, embeds, or other names, and no legacy subject hit.

**Observed:** Primary `complete`. Record states related search returned nothing.

### 6. Related read does not overlap a later named primary

Batch: `06-a.md` (open primary) then `06-b.md` (later named file). `06-a.md` links `06-b.md` as corroboration.

**Observed:** `06-b.md` may be read as related while `06-a` is open. No wiki page or tracking update is attributed to `06-b` as an ingest unit until `06-a` is `complete` or `failed`. Then `06-b` ingests as its own primary.

## Repository checks

```bash
.venv/bin/python specs/018-complete-ingest-context/fixtures/check.py
```

That check is the public seam. Implement may add it; this plan does not ship the checker or the fixture files.
