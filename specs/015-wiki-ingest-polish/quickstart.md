# Quickstart: Wiki Ingest Polish

## Prerequisites

From the repository root:

```bash
python --version
.venv/bin/python specs/015-wiki-ingest-polish/fixtures/check.py
```

Use the contract in [contracts/ingest-quality.md](contracts/ingest-quality.md) and entities in [data-model.md](data-model.md). Fixture sources live in [fixtures/sources/](fixtures/sources/); compiled destinations are in [fixtures/vault/](fixtures/vault/).

## Validation scenarios

### 1. Existing-page integration

Source: `fixtures/sources/01-existing-page.md` (Ila Voss + repeated "lighthouse is white") against existing `entities/red-harbor.md`.

**Observed:** `entities/red-harbor.md` includes Ila Voss in complete prose. "The lighthouse is white." appears once. Source is listed in `sources:`. Source filename is not a wiki page.

### 2. New-page threshold

Sources: `02-new-coherent.md` (Tide-glass) and `02b-fragment.md` (`bell?`).

**Observed:** `entities/tide-glass.md` created with required frontmatter and `[[Red Harbor]]`. Fragment staged at `_raw/02b-fragment.md` with `Insufficient scope`; no padded `bell` page.

### 3. Intent and conflict preservation

Source: `03-conflict.md` ("lighthouse is black").

**Observed:** "The lighthouse is white." remains. Black is a **Canon proposal** with `^[ambiguous]`, not an overwrite.

### 4. Surface quality

Source: `04-surfaces.md` (narration, DM secret, Perception test).

**Observed:** `[!narration]` has no DC or ledger. Ledger is in `[!secret]`. Test is **Wisdom (Perception) — `DC 12`** with Success/Failure consequences. Frontmatter and wikilinks present.

### 5. Tracking and failure

Sources: `05-readable.md` (outer pier) and `05b-empty.md`.

**Observed:** Outer pier compiled into Red Harbor; `05-readable.md` is in `.manifest.json`. Empty source is `failed` in `log.md` / `report.md` and absent from the success manifest.

## Repository checks

```bash
.venv/bin/python specs/015-wiki-ingest-polish/fixtures/check.py
```

That check asserts routing, preservation, quality, provenance, and failure behavior on the fixture vault. Do not replace it with a string snapshot of the skill instructions.
