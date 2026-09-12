# Data Model: Sequential Ingest Quality

Entities are wiki pages and ingest records. No database.

## Input file

One source the DM named. The sequential unit. A directory is a list of files, not one unit.

| Field | Rule |
|---|---|
| Identity | Path the DM named (or listing order inside a named folder) |
| Order | DM-named order; else folder listing order |
| State | `open` → `complete` \| `failed` |
| Pages | Wiki pages filed or stubbed from this file |
| Tracking | Manifest hash updated only on `complete` |

Unreadable, empty, or non-source binary → `failed` with a reason, then next file.

## Ingest run

One Co-DM pass over one or more input files.

| Field | Rule |
|---|---|
| Files | Ordered list of input files still to ingest (unchanged skipped) |
| Cursor | At most one file `open` |
| Report | After the run: each file complete/failed, pages, failure reasons |

Later file may update a page from an earlier file only after the earlier file is `complete` or `failed`.

### States (file)

`pending` → `open` → `complete` | `failed`. No second file `open` while one is `open`.

## Campaign kind

Closed wiki `type` plus run jobs and required treatments (`wiki/AGENTS.md` Layout). Quality bar. Not the incoming outline.

| Kind | Jobs live in |
|---|---|
| place, item, creature, npc, … | AGENTS.md Layout (006) |
| session-prep | 007 + Layout session beat/spine |
| ordinary knowledge | llm-wiki distill path |

Incoming source format is evidence. It is not an entity to copy.

## Wiki page (filed)

Must match the campaign kind for its subject. Must answer that kind’s jobs. Required treatments (place spoken look, owner-page numbers, complete-sentence prose) still bind.

## Ingest record

What the DM reads after a multi-file run. Lines in `log.md` plus the end-of-run report. Not a new store.

| Field | Rule |
|---|---|
| Order | Processing order |
| Per file | complete or failed |
| Pages | Which pages that file produced or updated |
| Failure | Reason when failed |

## Relationships

- Ingest run 1—* input files (ordered)
- Input file 1—* wiki pages (filed or stubbed)
- Wiki page *—1 campaign kind
- Later input file may update an earlier page only after earlier file closed

## Out of model

Legacy pages not in the ingest. Foundry. Player sheets. New campaign types. A second log format.
