# Feature Specification: QMD Search Default

**Feature Branch**: `004-qmd-search-default`

**Created**: 2026-09-12

**Status**: Draft

**Input**: User description: "qmd searching should be enabled by default for this project with appropriate collections, as well as utilizing the legacy collections for older but potentially more complete info. Mainteanace of qmd should be automated in this repo so its always availiable to agents"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Search is on without a setup ritual (Priority: P1)

A Co-DM agent starts work in this repository. It can search the project's wiki for campaign facts without the DM first enabling a collection, filling a missing setting, or telling the agent to skip search. Prep skills that already hand off to vault retrieval actually retrieve.

**Why this priority**: Today ingest and retrieval skip when collections are unset. Agents then invent or miss facts. Default-on search is the whole request.

**Independent Test**: From a clean agent session in this repo, ask for a fact that exists only on a compiled wiki page. The agent finds and cites that page without being told to enable search.

**Acceptance Scenarios**:

1. **Given** a wiki page that already exists in this project, **When** a Co-DM agent looks up that subject in prep, **Then** it retrieves from the project's search collections without a human turning search on.
2. **Given** no extra environment ritual beyond cloning and ordinary project config, **When** the agent would previously skip search as "unset", **Then** it does not skip; it searches.
3. **Given** a retrieval handoff in a prep skill, **When** that skill runs, **Then** vault lookup happens against the default collections, not unaudited chat memory.

---

### User Story 2 - Legacy collections fill gaps; this wiki wins conflicts (Priority: P2)

The campaign of record still holds older, sometimes fuller notes. An agent searching a name that is thin or missing here also searches those legacy collections. If this project's wiki and a legacy collection disagree, the agent treats this wiki as current canon and uses the legacy hit as extra context, marked as not this vault's page.

**Why this priority**: The user named legacy collections as a required source of older, more complete info. Without precedence, agents will mix two canons.

**Independent Test**: Ask a fact present only in the campaign of record; the agent surfaces it and does not present it as a page in this wiki. Ask a fact both stores have differently; the agent cites this wiki.

**Acceptance Scenarios**:

1. **Given** a subject documented in a legacy collection and absent from this wiki, **When** the agent searches, **Then** it returns the legacy hit and marks it as campaign-of-record context, not as a compiled page here.
2. **Given** the same subject on this wiki and in a legacy collection with different wording, **When** the agent answers a canon question, **Then** it cites this wiki and does not silently prefer the older text.
3. **Given** a subject in neither store, **When** the agent searches, **Then** it reports silence and does not invent a wiki fact.

---

### User Story 3 - The index stays current without an agent remembering (Priority: P3)

After wiki pages are created or changed, search stays usable. An agent that arrives later in the day can find the new page. No one has to run a manual refresh as a separate remembered step. If the index is missing or stale, repair happens as part of ordinary project maintenance, not a human dashboard.

**Why this priority**: "Always available to agents" fails if every ingest forgets to refresh. Automation is what keeps P1 true over time.

**Independent Test**: File or update one wiki page, wait for the project's maintenance cycle, then search for a unique phrase from that page; it is found. Repeat after a later session without anyone typing a refresh command.

**Acceptance Scenarios**:

1. **Given** a newly filed or updated wiki page, **When** maintenance has run, **Then** a later agent can find that page by search.
2. **Given** an agent session that does not mention search maintenance, **When** it looks up a recently ingested page, **Then** the page is findable.
3. **Given** a missing or stale index at session start, **When** project maintenance runs, **Then** search becomes available without a GUI and without the DM operating a control panel.

---

### Edge Cases

- Search index absent on first clone: maintenance creates it; agents do not treat "unset" as permission to skip forever.
- Maintenance fails: the wiki remains the source of truth; the agent still reads pages it already knows; the failure is visible (exit status / log), not silent.
- Legacy collection unreachable: search this wiki; report the legacy miss; do not block prep.
- This wiki is silent and legacy has a hit: use legacy as context, not as a silent wiki write.
- Two legacy hits disagree: present the conflict; do not pick a winner against this wiki.
- Page deleted from the wiki: after maintenance, search no longer returns it as current.
- Secrets and unrevealed facts: search results stay DM-addressed; they are not player-visible.
- Agent has no network: local collections still work; remote-only collections fail closed like "legacy unreachable."

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Search MUST be enabled by default for agents working in this repository. Agents MUST NOT skip vault search solely because a collection setting was left empty.
- **FR-002**: Default collections MUST include this project's wiki (the compiled pages the Co-DM retrieves from) as the primary collection.
- **FR-003**: Default collections MUST also include the campaign-of-record (ai-co-dm) legacy collections so older or fuller notes remain searchable.
- **FR-004**: When this wiki and a legacy collection conflict, the agent MUST treat this wiki as current canon and MUST mark the legacy hit as campaign-of-record context.
- **FR-005**: When this wiki is silent and a legacy collection has a hit, the agent MUST return that hit as extra context and MUST NOT file it as a wiki page without DM accept.
- **FR-006**: After wiki pages are created, updated, or removed, automated maintenance MUST keep the search index aligned with those pages so a later agent can find current content.
- **FR-007**: Maintenance MUST be agent-shaped: invocable without a GUI, with a clear done-or-failed result. A human-only control panel MUST NOT be required for search to stay available.
- **FR-008**: Prep and wrapup skills that already require vault retrieval MUST use these default collections rather than unaudited chat memory.
- **FR-009**: If maintenance or a legacy collection fails, the agent MUST still be able to read known wiki pages, MUST surface the failure, and MUST NOT invent a wiki fact to cover the gap.
- **FR-010**: Search output is for the Co-DM and DM. It MUST NOT appear on the player-facing play surface unless the DM accepts a reveal.

### Key Entities

- **Search index**: The retrieval layer over compiled wiki pages (and configured collections) that agents query instead of rereading the whole vault.
- **Project collection**: The searchable set for this repository's wiki.
- **Legacy collection**: A searchable set from the campaign of record (ai-co-dm), older and possibly more complete, not this vault's canon.
- **Maintenance cycle**: The unattended update that keeps the search index aligned with wiki writes.
- **Retrieval handoff**: The existing Co-DM practice of looking up vault facts before inventing.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: In 10 lookups of facts that exist only on this project's wiki, a Co-DM agent cites the supporting page at least 9 times without anyone enabling search in that session.
- **SC-002**: In 5 lookups of facts that exist only in a legacy collection, the agent returns the legacy context all 5 times and presents none of them as a page compiled in this wiki.
- **SC-003**: Given one conflicting fact, 100% of agent answers cite this wiki, not the older collection, as current canon.
- **SC-004**: After one wiki page is filed or changed, a later agent finds a unique phrase from that page by search in under 5 minutes of unattended maintenance, with no human refresh command in the second session.
- **SC-005**: Zero prep sessions in a three-session sample skip vault search because collections were "unset."
- **SC-006**: A DM can confirm search is available (a known page is findable) without opening a graphical settings app.

## Assumptions

- Primary users are Co-DM agents and the human DM. Players do not query the search index.
- Designated retrieval layer is the search index already assumed by prep skills (commonly called QMD in this repo). The wiki remains the source of truth; the index is derived.
- Campaign of record remains `ai-co-dm` until cutover (`CONTEXT.md`). Legacy collections live there. This repo's wiki is current compiled canon after ingest.
- "Appropriate collections" for this project: this wiki as primary; campaign-of-record collections as legacy; no extra collections invented in v1.
- Automation runs on the DM's workstation as part of this repo (after wiki writes and as a catch-up if the index is missing). Cloud-hosted search is out of scope.
- Existing Co-DM rules still bind: complete-sentence wiki prose; no silent canon writes; retrieval silence is a stub, not invention.
- Out of scope: replacing the prose wiki; player-facing search; live search during a session; non-campaign document corpora beyond the named legacy vault.
