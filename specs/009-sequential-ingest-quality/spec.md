# Feature Specification: Sequential Ingest Quality

**Feature Branch**: `009-sequential-ingest-quality`

**Created**: 2026-09-12

**Status**: Draft

**Input**: User description: "when ingesting multiple files, each input file should be processed sequentially so quality is not compromised. After that file is completely ingested should the next be. In addition the temporary period where formats ingested were to be considered exemplary is over and now our own internal formats are the development target and quality bar"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - One file finishes before the next starts (Priority: P1)

A DM asks the Co-DM to ingest several files at once. The Co-DM works one input file all the way through — facts compiled, pages filed, tracking updated, that file judged complete — and only then opens the next. Speed of the batch does not justify overlapping files. Quality of each page matches what that file would get if it were ingested alone.

**Why this priority**: Overlapping ingest is the named quality failure. A file that is only half compiled when the next begins produces thin pages, missed jobs, and mixed outlines.

**Independent Test**: Hand the Co-DM three approved source files. Watch the ingest. File 2 produces no wiki pages and no tracking updates until file 1 is complete. Each resulting page answers the same run jobs it would after a single-file ingest of that source.

**Acceptance Scenarios**:

1. **Given** two or more approved files to ingest, **When** ingest runs, **Then** the next file does not start until the current file is complete (pages filed or explicitly failed, tracking updated for that file).
2. **Given** a mixed batch, **When** file 1 is still being compiled, **Then** no page belonging only to file 2 is created or changed.
3. **Given** the same file ingested alone versus as the third file in a sequential batch, **When** a DM compares the two wiki pages, **Then** both answer the same run jobs for that kind; the batched page is not thinner, missing spoken look, or a different document type.
4. **Given** a large folder of approved sources, **When** ingest runs, **Then** files still complete one at a time; folder size does not authorize overlapping work.

---

### User Story 2 - Campaign formats are the quality bar (Priority: P1)

A DM ingests a source that is not already a campaign wiki page — a foreign dump, an old note, a campaign-of-record file, a transcript. The Co-DM treats that file as evidence of facts, not as the page shape to copy. The filed wiki page matches the campaign’s own kind for that subject (place, item, creature, person, session beat, and the other closed types). Incoming layout, heading order, and density are not the target.

The temporary period of treating ingested source formats as exemplary is over. Internal campaign formats are the development target and the quality bar.

**Why this priority**: Cloning a source outline produces pages the DM cannot run. The product is the campaign wiki, not a photocopy of whatever was dropped in.

**Independent Test**: Ingest one foreign-format source that names a complete place (or other kind). Open the wiki page. A second DM can speak the look and run first contact from the campaign jobs for that kind, even if the source used a different outline.

**Acceptance Scenarios**:

1. **Given** a source whose outline is not the campaign kind, **When** it is ingested, **Then** the wiki page is filed as that campaign kind and answers that kind’s run jobs; it does not keep the foreign outline as the page shape.
2. **Given** a source that already matches a campaign kind, **When** it is ingested, **Then** the wiki page still meets that kind’s jobs and required treatments (including spoken look where the kind requires it); matching the source is not a reason to skip the bar.
3. **Given** several files of different incoming shapes in one sequential ingest, **When** ingest finishes, **Then** every filed page is judged against the campaign kind, not against its source file’s layout.
4. **Given** guidance, samples, or skills that still call an ingested source “exemplary format,” **When** this feature is in force, **Then** those instructions no longer treat incoming files as the format to copy; they point at the campaign kinds instead.

---

### User Story 3 - The DM can see each file complete (Priority: P2)

After a multi-file ingest, the DM can tell which file finished, in what order, which pages each file produced, and which file failed if one did. They do not have to reconstruct the batch from a single mixed dump of pages.

**Why this priority**: Sequential work is unverifiable without a per-file record. The DM is the only person who can accept wiki facts.

**Independent Test**: Run a three-file ingest where the middle file is unreadable. The report lists file 1 complete with its pages, file 2 failed with a reason, file 3 complete after file 2 was closed as failed. No file 3 pages appear before file 2 is closed.

**Acceptance Scenarios**:

1. **Given** a finished multi-file ingest, **When** the DM reads the ingest record, **Then** each input file is listed in processing order with complete or failed, and the pages that file produced.
2. **Given** a file that cannot be compiled, **When** ingest hits it, **Then** that file is closed as failed with a reason before the next file starts; later files still run sequentially.
3. **Given** a later file that updates a page created by an earlier file, **When** the record is read, **Then** both files are complete in order; the later update is attributed to the later file.

---

### Edge Cases

- One file: sequential is trivial; the internal format bar still applies.
- Unreadable, empty, or binary-nonsource file: close it as failed with a reason, then start the next. Do not stall the batch with no record.
- Two files name the same subject: file 1 files (or stubs) the page; file 2 may update that page only after file 1 is complete.
- A file contains several subjects: they all belong to that file’s ingest. The next input file still waits until this file is complete.
- Session-prep and other already-specified campaign kinds remain those kinds. Sequential still applies. Their jobs are internal format, not a license to clone a foreign dump.
- Required treatments that are part of a campaign kind (spoken look as `[!narration]`, run jobs, owner-page numbers) still bind. They bind because they are the internal bar, not because the source was exemplary.
- Unaccepted Work still does not publish, except named ingest of approved sources.
- Legacy pages not in the ingest are not restyled solely to match this feature.
- The DM asking for a faster batch does not authorize overlapping files.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: When ingest is given more than one input file, the Co-DM MUST complete the current file before starting the next. Completing a file means every page that file requires is filed or explicitly stubbed, that file’s tracking is updated, and the file is marked complete or failed.
- **FR-002**: The Co-DM MUST NOT create or change wiki pages for a later file, and MUST NOT update tracking for a later file, while an earlier file is still open.
- **FR-003**: Folder size, batch size, and a request for speed MUST NOT authorize overlapping ingest of two input files.
- **FR-004**: Quality of a page produced in a sequential batch MUST match single-file ingest of that same source: same campaign kind, same run jobs answered, no missing required treatments.
- **FR-005**: Incoming source files MUST be treated as evidence of facts. They MUST NOT be treated as exemplary page format. The development target and quality bar MUST be the campaign’s own page kinds and jobs.
- **FR-006**: A filed wiki page MUST match the campaign kind for its subject and MUST answer that kind’s run jobs. The Co-DM MUST NOT copy a foreign outline, heading list, or density band as the wiki page shape.
- **FR-007**: When a source already matches a campaign kind, ingest MUST still judge the filed page against that kind’s jobs and required treatments. Source match is not a skip of the bar.
- **FR-008**: Agent instructions, samples, and ingest guidance MUST stop presenting ingested source formats as the format to copy. Where they need a quality target, they MUST point at campaign kinds and jobs.
- **FR-009**: After a multi-file ingest, the Co-DM MUST report each file in processing order as complete or failed, with the pages that file produced and a reason for each failure.
- **FR-010**: A failed file MUST be closed (failed + reason) before the next file starts. Remaining files MUST still be processed sequentially.
- **FR-011**: A later file MAY update a page filed by an earlier file only after the earlier file is complete. The later update MUST be attributed to the later file in the ingest record.
- **FR-012**: Existing Co-DM rules still bind: complete-sentence prose; wiki writes after DM accept except named ingest of approved sources; invented names are Work; numbers live on one owner page; spoken look is theatre of the mind.

### Key Entities

- **Input file**: One source the DM named for ingest. The sequential unit.
- **Complete ingest of a file**: That file’s pages are filed or stubbed, tracking for that file is updated, and the file is marked complete or failed.
- **Campaign kind**: A closed wiki type (place, item, creature, person, session-prep, session, and the other already-listed kinds) plus the run jobs and required treatments for that kind.
- **Internal format / quality bar**: Those campaign kinds and jobs. The product target. Not the layout of an incoming file.
- **Incoming source format**: The outline, headings, and density of a file being ingested. Evidence, not exemplar.
- **Ingest record**: The per-file complete/failed report the DM can read after a batch.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: In a watched ingest of at least five approved files, 100% of files reach complete or failed before any wiki page or tracking update for the next file appears. Zero overlapping files.
- **SC-002**: For at least three subjects, a page from a sequential batch is judged the same kind and the same jobs as the page from ingesting that file alone. Zero batched pages are thinner, missing spoken look, or a different document type for that reason.
- **SC-003**: In a side-by-side of at least three foreign-format sources and their wiki pages, 100% of wiki pages answer the campaign kind’s jobs. Zero wiki pages use the foreign outline as the page shape.
- **SC-004**: After this feature is in force, 100% of new ingest guidance that names a format target names campaign kinds and jobs. Zero remaining instructions tell the Co-DM to copy an incoming file’s layout as exemplary format.
- **SC-005**: In 100% of multi-file ingests of three or more files (including one forced failure), the DM can name processing order, each file’s complete/failed state, and which pages came from which file, from the ingest record alone, in under one minute.

## Assumptions

- “File” means one named source document (or one `_raw/` draft). A directory is a list of files, not one ingest unit.
- Processing order is the order the DM named. If they named a folder, it is that folder’s listing order.
- Campaign kinds and run jobs already specified (sample-content guidance, place spoken look, session-prep as its own kind) remain the internal bar. This feature does not invent new kinds.
- This feature ends the bootstrap period in which ingested campaign-of-record or `_raw/` source layouts were treated as exemplary format. `_raw/` may still illustrate quality of jobs; it is not a clone target, and newly ingested files are not either.
- Place spoken look and other required treatments still bind because they are campaign-kind jobs, not because a source file’s layout is sacred. Foreign place sources are mapped into the place kind rather than photocopied.
- Session-prep preserve remains the session-prep kind’s internal shape. It is not a general rule that every incoming format is exemplary.
- History and other multi-file ingest paths follow the same sequential rule and the same quality bar.
- Out of scope: restyling pages that are not in the ingest; inventing new campaign types; trading quality for batch speed; Foundry staging; player-facing sheets.
