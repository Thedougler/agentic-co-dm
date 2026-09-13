# Feature Specification: Complete Ingest Context

**Feature Branch**: `018-complete-ingest-context`

**Created**: 2026-09-12

**Status**: Draft

**Input**: User description: "during a wiki-ingest process, agents should aim for a complete ingest, ingest the primary file, and search for and read the relevant linked/related/corroborating files from the files content both from within _raw/ and by searching the legacy collections with qmd. Results that from the newest files represent the latest decisions by the user but there is still relevant supporting context from older versions or variants of the same or related content within legacy/"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - A primary ingest is complete only with related evidence (Priority: P1)

A DM names one source for wiki ingest — a draft in staging, a session note, a place file. That file is the primary. It mentions other names, links, embeds, or the same subject in another draft. The Co-DM does not compile from that file alone. It finds and reads the linked, related, and corroborating files that the primary’s content points to, then compiles. Completeness means the primary’s ideas were distilled with that related evidence in hand, not that the Co-DM wandered the whole vault.

**Why this priority**: Isolated ingest of a primary that clearly sits in a cluster produces thin pages, missed supporting detail, and decisions compiled without the rest of the DM’s related notes.

**Independent Test**: Give ingest one approved primary that names or links two related drafts in staging. Watch the run. Both related drafts are read before the primary is marked complete. The filed wiki page includes uncontradicted supporting facts that exist only in those related drafts.

**Acceptance Scenarios**:

1. **Given** an approved primary whose content names or links related files in staging, **When** ingest of that primary completes, **Then** those related files were searched for and read before the primary was marked complete.
2. **Given** a primary with no linked or related files in staging or in legacy collections, **When** ingest runs, **Then** the primary still completes from its own content; absence of related files is not a stall.
3. **Given** a related file named by the primary that cannot be found, **When** ingest of the primary completes, **Then** the miss is recorded and the primary still completes from what was found.
4. **Given** a primary that is one file in a sequential batch, **When** related files are read as corroboration, **Then** those reads do not start a second overlapping ingest of another primary; sequential completion of named input files still holds.

---

### User Story 2 - Staging and legacy are both searched for corroboration (Priority: P1)

Related evidence lives in two places the DM already uses: other drafts in the staging area, and older or variant notes in the campaign-of-record collections. The Co-DM searches both. Staging often holds the current cluster. Legacy often holds an older version or a fuller variant of the same or a related subject. A hit in one place does not excuse skipping the other.

**Why this priority**: The DM named both sources. Stopping at the primary, or at staging only, leaves older supporting context on the table and compiles an incomplete page.

**Independent Test**: Ingest a primary whose subject also exists as a staging sibling and as an older legacy note. Both are found and read. The compiled page is not built from the primary alone.

**Acceptance Scenarios**:

1. **Given** a primary whose content points at related drafts in staging, **When** ingest runs, **Then** those staging files are searched for and read as corroboration.
2. **Given** a primary whose subject (or a clearly related subject) exists in a legacy collection, **When** ingest runs, **Then** that legacy material is searched for and read as corroboration, even if staging already had a related draft.
3. **Given** staging is silent for a related name and a legacy collection has a hit, **When** ingest runs, **Then** the legacy hit is read as supporting context and is not filed as a compiled wiki page without DM accept.
4. **Given** a legacy collection is unreachable, **When** ingest runs, **Then** staging search still happens, the legacy miss is visible, and the primary still completes.

---

### User Story 3 - Newest files win decisions; older files still inform (Priority: P1)

Among the primary and its related evidence, the newest files are the DM’s latest decisions. Older versions and variants — especially in legacy collections — still carry supporting context: extra description, history, names, and detail the newest file does not repeat. The Co-DM compiles the latest decision and keeps uncontradicted older support. It does not let an older variant silently replace a newer decision.

**Why this priority**: Without recency, ingest either freezes old canon over a later decision or throws away the only copy of supporting detail.

**Independent Test**: Ingest a newest primary that changes one decision and omits color that exists only in an older variant. The wiki page uses the new decision and still includes the uncontradicted older color. A second case where the older variant contradicts the newest decision keeps the newest decision and surfaces the conflict instead of overwriting.

**Acceptance Scenarios**:

1. **Given** a newest primary and an older variant of the same subject, **When** they agree or the older file only adds uncontradicted detail, **Then** the compiled page uses the newest decisions and keeps that supporting detail.
2. **Given** a newest primary that changes a decision present in an older variant, **When** ingest compiles the page, **Then** the newest decision is the one filed; the older wording is not silently preferred.
3. **Given** an older variant that contradicts a newest decision, **When** ingest would have to pick a canon fact, **Then** the conflict is surfaced as a proposal or explicit unresolved item rather than a silent overwrite of the newest decision.
4. **Given** several related files of different ages, **When** ingest ranks them for decisions, **Then** recency is taken from which file is newer unless the content itself dates the decision more clearly than the file.

---

### User Story 4 - The DM can see what was read for completeness (Priority: P2)

After ingest, the DM can tell which file was primary, which related files were found and read (staging vs legacy), which named related files were missed, and whether an older variant contributed supporting context or lost a decision conflict. They do not have to reconstruct completeness from the wiki page alone.

**Why this priority**: Completeness is unverifiable without a record. The DM is the only person who can accept wiki facts.

**Independent Test**: Run an ingest with one primary, one staging relative, one legacy variant, and one missing named link. The ingest record lists all four outcomes. A DM names them from the record in under one minute.

**Acceptance Scenarios**:

1. **Given** a finished ingest of a primary with related evidence, **When** the DM reads the ingest record, **Then** the primary, each related file that was read, each miss, and whether a hit was staging or legacy are listed.
2. **Given** an older variant that lost a decision conflict, **When** the record is read, **Then** that conflict is visible as a proposal or unresolved item, attributed to the files involved.
3. **Given** no related files were found, **When** the record is read, **Then** it still names the primary as complete and states that related search returned nothing, rather than omitting the search.

---

### Edge Cases

- Primary with no links, embeds, or other names: still search by the subject the primary is about; do not invent extra subjects to chase.
- Related file is itself a later named input in the same batch: read it now as corroboration; ingest it as a primary only when its sequential turn arrives.
- Two staging drafts link to each other: each related file is read at most once per primary; do not loop.
- Many weakly related hits: only files the primary’s content makes relevant are in scope; a shared campaign or folder is not enough.
- Duplicate or near-duplicate variants: newest decision plus uncontradicted older support; do not file two competing wiki pages for the same subject from those variants.
- Legacy hit disagrees with this wiki’s already-compiled page: this wiki remains current canon; the legacy hit is extra context and a proposal if it would change that page.
- Linked media (images, maps, tokens): existing media-attachment rules still apply; this feature is about corroborating text sources, not a new art pipeline.
- Unreadable related file: record the miss-or-fail reason; do not stall the primary.
- Named ingest of approved sources and unaccepted Work still bind. Related legacy material is not a license to publish unapproved canon.
- The DM asking for a faster ingest does not authorize skipping related-file search.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Wiki ingest of a named primary MUST aim for a complete ingest: the primary is compiled, and relevant linked, related, and corroborating files named or implied by that primary’s content are searched for and read before the primary is marked complete.
- **FR-002**: The Co-DM MUST discover candidate related files from the primary’s content (links, embeds, explicit names, and the primary’s own subject). It MUST NOT treat the rest of the vault as in-scope merely because it exists.
- **FR-003**: The Co-DM MUST search the staging area for those related files and MUST read each relevant hit found there.
- **FR-004**: The Co-DM MUST search the legacy collections for the same subject and for clearly related subjects, and MUST read relevant hits as supporting context.
- **FR-005**: A hit in staging MUST NOT skip the legacy search, and a hit in legacy MUST NOT skip the staging search.
- **FR-006**: Among the primary and its related evidence, the newest files MUST be treated as the DM’s latest decisions.
- **FR-007**: Older versions and variants MUST still be used as supporting context. Uncontradicted detail from older files MUST be available to the compiled page.
- **FR-008**: An older file MUST NOT silently override a newer decision. When an older variant contradicts a newer decision, ingest MUST keep the newer decision and MUST surface the conflict as a proposal or explicit unresolved item.
- **FR-009**: Related files are corroborating evidence for the open primary. Reading them MUST NOT start overlapping ingest of another named input file. Sequential completion of named input files still holds.
- **FR-010**: Legacy hits remain campaign-of-record context. They MUST NOT be filed as compiled wiki pages without DM accept. This wiki remains current canon when it already disagrees with a legacy hit.
- **FR-011**: After ingest, the Co-DM MUST report the primary, each related file read, whether each hit was staging or legacy, each miss, and each recency conflict that was surfaced.
- **FR-012**: A missing, unreadable, or unreachable related source MUST be recorded and MUST NOT stall completion of the primary from evidence that was found.
- **FR-013**: Related-file search is required for completeness. A request for speed MUST NOT authorize skipping it.
- **FR-014**: Existing Co-DM rules still bind: sequential named-file ingest; complete-sentence prose; wiki writes after DM accept except named ingest of approved sources; invented names are Work; this wiki wins compiled-canon conflicts with legacy; retrieval silence is not invention.

### Key Entities

- **Primary source**: The named input file currently being ingested. The completeness unit.
- **Related source**: A linked, related, or corroborating file discovered from the primary’s content or from a search for the same or a clearly related subject.
- **Staging area**: The vault’s draft staging tree (`_raw/`) where current related drafts often live.
- **Legacy collection**: Searchable campaign-of-record notes, often older or variant, not this vault’s compiled canon.
- **Latest decision**: The DM’s current call on a fact or creative choice, taken from the newest relevant file unless the content itself dates the decision more clearly.
- **Supporting context**: Uncontradicted detail from older versions or variants that the newest file does not repeat.
- **Complete ingest**: The primary is compiled with related evidence read, misses recorded, recency applied, and the primary marked complete or failed.
- **Ingest record**: The report the DM can read naming primary, related reads, misses, and recency conflicts.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: In a watched sample of 10 primary ingests whose content names or links related staging files, 100% of those named related staging files that exist are read before the primary is marked complete.
- **SC-002**: In a watched sample of 10 primary ingests whose subject also exists in a legacy collection, 100% read that legacy material as supporting context before the primary is marked complete.
- **SC-003**: In a side-by-side of at least 5 newest-plus-older pairs, 100% of compiled pages use the newest file’s decisions. Zero pages silently prefer the older wording for a changed decision.
- **SC-004**: In that same sample, at least 90% of uncontradicted supporting details that exist only in the older variant appear on the compiled page or are explicitly recorded as unused with a reason.
- **SC-005**: In 100% of sampled ingests (including cases with a miss and cases with no related hits), the DM can name the primary, related reads, misses, and any recency conflict from the ingest record alone in under one minute.
- **SC-006**: In a watched sequential batch of at least 3 named input files, related-file reads do not cause a second named file to start ingest before the current primary is complete. Zero overlapping named-file ingests.
- **SC-007**: In 100% of sampled ingests where a related file is missing or a legacy collection is unreachable, the primary still reaches complete or failed from found evidence, and the miss is in the record.

## Assumptions

- “Primary” is one named source document (or one staging draft). A directory remains a list of named files, not one completeness unit.
- Discovery is driven by the primary’s content and its subject. A full crawl of staging or of legacy collections is out of scope.
- Recency defaults to which file is newer. If the content itself dates a decision more clearly than the file, that dating wins for that decision.
- Reading a related file as corroboration is not the same as making it the next named ingest unit. Named files still complete one at a time.
- Staging search covers the vault `_raw/` tree. Legacy search uses the project’s existing search index over campaign-of-record collections.
- This wiki remains current compiled canon. Legacy remains extra context. Feature 004’s precedence is not replaced.
- Feature 009’s sequential quality bar is not replaced. Completeness adds related reads inside the open primary; it does not overlap two primaries.
- Feature 015 still holds: files are evidence containing ideas, not finished notes to photocopy.
- Existing accept rules still hold. Related legacy material does not grant silent canon writes.
- Out of scope: ingesting the entire legacy vault; changing query-time lookup order for ordinary wiki questions; a new media pipeline; Foundry staging; player-facing sheets; restyling pages that are not in the ingest.
