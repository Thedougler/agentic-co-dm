# Feature Specification: Copy Foundry Config

**Feature Branch**: `002-copy-foundry-config`

**Created**: 2026-09-12

**Status**: Draft

**Input**: User description: "foundry is already up and useable for development, its config just needs to be copied from ai-co-dm" plus "also when ingesting content, a search of ai-co-dm should be done for the linked art assets so they can be imported into the new vault"

## Clarifications

### Session 2026-09-12

- Q: How should this project authenticate to the local development table, and how strictly must connection secrets be kept out of the project? → A: User `mcp-api`, password `nickisagod`; laptop-only home game, not exposed; security is not a concern.
- Q: How much manual setup may an agent need before it can log in and use the table connection? → A: None that matters: agents must log in and use the MCP server easily, without setup or many manual steps; agent-shaped software is the goal.



## User Scenarios & Testing *(mandatory)*

### User Story 1 - Reach the live development table (Priority: P1)

The DM already has a development table running and working from the campaign of record. This project cannot present accepted prep there until it has the same connection settings. The DM brings those settings over so this project talks to that table without standing up a second one.

**Why this priority**: User Story 3 of Agentic Co-DM (present accepted content at the table) is blocked until this project can reach the table that already exists.

**Independent Test**: An agent, given this repo, logs in as `mcp-api` and lists or stages against the existing table in one go. No extra setup wizard. No new table.

**Acceptance Scenarios**:

1. **Given** the development table is already running and the campaign of record can reach it, **When** the DM copies that table's connection settings into this project, **Then** this project can confirm the same table is reachable as `mcp-api`.
2. **Given** those settings are in place, **When** the DM attempts to present one piece of accepted prep, **Then** the players' table receives that content on the existing development world — not a new or empty world.
3. **Given** the local account `mcp-api` (password known to the operator), **When** an agent in this project connects, **Then** it authenticates as that user without creating a second table or a second account, and without the DM performing extra setup steps.

---

### User Story 2 - Bring linked art with ingest (Priority: P1)

When the DM ingests a note into this vault, pictures and other art that note already links to often live only in the campaign of record. The ingest searches that vault for those linked assets and imports the matches here so the new page's images resolve instead of showing empty embeds.

**Why this priority**: A distilled page the DM cannot see illustrated is not usable prep. Notes such as the Bloodhawk already name flight and token art.

**Independent Test**: Ingest one named source that embeds art. Confirm each linked asset that exists in the campaign of record is present in this vault and the embed opens. Confirm no asset is invented for a name the campaign of record does not have.

**Acceptance Scenarios**:

1. **Given** a named source embeds or wikilinks art that exists in the campaign of record, **When** that source is ingested, **Then** those assets are imported into this vault and the filed page's links resolve.
2. **Given** a named source links art the campaign of record does not have, **When** ingest finishes, **Then** no fake image is created; the missing names are reported.
3. **Given** this vault already has an asset with the same name, **When** ingest finds a match in the campaign of record, **Then** the existing file is not silently overwritten; the DM is told.

---

### Edge Cases

- The development table is running but this project still cannot reach it (wrong host, module not connected, or wrong account).
- The campaign of record settings are missing or older than the running table.
- This project already has partial or stale table settings.
- Account `mcp-api` is missing from the world or the password does not match.
- A note links art by a name that does not match the file in the campaign of record.
- Several files in the campaign of record share a similar name; the wrong one must not be imported.
- Linked art exists but is not an image (or is outside the campaign of record).

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The DM MUST be able to reuse the campaign of record's working table-connection settings in this project without creating a second development table.
- **FR-002**: After those settings are present, this project MUST be able to confirm the existing development table is reachable.
- **FR-003**: Presenting accepted prep from this project MUST target the same development world the campaign of record already uses.
- **FR-004**: This project MUST authenticate to the development table as local user `mcp-api` (password `nickisagod`). The project runs only on the DM's laptop, is not exposed, and is for home games; extra secret-handling beyond that local account is not required.
- **FR-005**: Existing Co-DM rules still apply: only accepted, presentable prep may appear on the table; unaccepted or unrevealed material stays off the play surface.
- **FR-006**: When a named source is ingested, this project MUST search the campaign of record for every art asset that source links or embeds.
- **FR-007**: Matching assets MUST be imported into this vault so the filed page's art links resolve.
- **FR-008**: Ingest MUST NOT invent or generate art for a linked name the campaign of record does not contain; missing assets MUST be reported to the DM.
- **FR-009**: Ingest MUST NOT silently overwrite an art file that already exists in this vault.
- **FR-010**: An agent MUST be able to log in as `mcp-api` and use the table connection in a single invocation (arguments in, text or JSON out). The DM MUST NOT have to complete a setup wizard, dashboard walkthrough, or multi-step checklist before that invocation works.

### Key Entities

- **Development table**: The already-running play surface used for this campaign's development. One table, not a new instance.
- **Table connection settings**: Host, world, and the local `mcp-api` account the campaign of record already uses. Copied, not reinvented.
- **Accepted prep**: Campaign content the DM has approved for the table.
- **Linked art asset**: An image or other media file a source already names (embed or wikilink), whose original copy lives in the campaign of record.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: An operator who already has the campaign of record talking to the development table can get this project talking to the same table in one sitting, without creating a new table.
- **SC-002**: A reachability check from this project succeeds against that table on the first attempt after the copy.
- **SC-003**: One piece of accepted prep presented from this project is visible on the existing development world (same wording the DM accepted).
- **SC-004**: After settings are copied, an agent connects as `mcp-api` on the first attempt without creating a new table account and without the DM performing extra setup steps.
- **SC-005**: After ingesting one source that links art present in the campaign of record, the DM can open every such embed in this vault in under 2 minutes without hunting the other vault.
- **SC-006**: An ingest whose source names art absent from the campaign of record completes without creating placeholder images, and lists the missing names.

## Assumptions

- Foundry VTT is the player-facing table (designated surface). It is already running and usable for development.
- The campaign of record (`ai-co-dm`) already holds working connection settings for that table, and the original art for notes ingested from early-dev samples and similar sources.
- This project does not stand up, install, or replace the table; it only reuses the existing one.
- One campaign, one development table. No second world for this repo.
- This project runs on the DM's laptop only, is not exposed, and is for home games. Security of the local table password is not a concern.

- Agentic Co-DM accept-gate and reveal rules are unchanged; this feature unblocks reaching the table and resolving linked art on ingest.
- Agent-shaped tools only (constitution VI): invoke without a GUI; no human-only wrapper when the agent can run the same command.

- Ingest still requires a named, approved source. Art import is part of that ingest, not a second silent canon write.
- Only assets the source already links are in scope. No extra gallery scrape of the campaign of record.
