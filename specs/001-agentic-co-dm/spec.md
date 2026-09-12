# Feature Specification: Agentic Co-DM

**Feature Branch**: `001-agentic-co-dm`

**Created**: 2026-09-11

**Status**: Draft

**Input**: User description: "We are building an agentic co-dm system utilizing the llm-wiki design for knowledge bank, obsidian vault for the user interface for the second brain, and foundryvtt for presenting the content to the players during play. This repo is largely an exercise and experimentation in agent to human communication to human communication."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Distill campaign knowledge into a second brain (Priority: P1)

A Dungeon Master (DM) has campaign notes, adventure text, session recaps, and table rulings scattered across sources. They ingest those sources into a compiled knowledge bank of interconnected pages. The DM browses and corrects that bank in their existing second-brain workspace. The Co-DM agent can retrieve from the same bank.

**Why this priority**: Without a shared, citable knowledge bank there is nothing trustworthy for the agent to say or for the DM to hand to the table. This slice is a usable second brain even if the agent never speaks.

**Independent Test**: Ingest a small set of campaign sources, open the compiled pages in the DM workspace, confirm the pages are linked and match the sources, and confirm the agent can answer a question from those pages with a citation.

**Acceptance Scenarios**:

1. **Given** a campaign with at least one source (notes, recap, or published text), **When** the DM ingests it, **Then** the knowledge bank contains distilled pages the DM can open in their second-brain workspace.
2. **Given** distilled pages exist, **When** the DM follows links between related people, places, and events, **Then** they reach the related pages without leaving the workspace.
3. **Given** a distilled page, **When** the DM edits it, **Then** the corrected text is what later retrieval uses.
4. **Given** ingested sources, **When** the DM asks the Co-DM a factual question covered by those sources, **Then** the agent answers from the bank and names the page(s) it used.

---

### User Story 2 - Agent proposes; DM decides (Priority: P2)

During prep or play, the DM asks the Co-DM for a ruling, recap, NPC voice, clue, or scene framing. The agent replies to the DM only, with a short proposal and citations. The DM accepts, edits, or rejects before anything reaches the players.

**Why this priority**: The repo's experiment is agent → human (DM) → human (players). The agent is a co-DM, not the table's voice. This slice works against a frozen knowledge bank.

**Independent Test**: Ask the agent for a table-facing beat covered by the bank; confirm the DM sees a cited proposal; confirm players see nothing until the DM accepts.

**Acceptance Scenarios**:

1. **Given** a question the knowledge bank can answer, **When** the DM asks the Co-DM, **Then** the DM receives a concise proposal plus citations, and players receive nothing.
2. **Given** a proposal, **When** the DM edits and accepts it, **Then** the accepted wording is the only version marked ready for the table.
3. **Given** a proposal, **When** the DM rejects it, **Then** it is not marked ready for the table and is not shown to players.
4. **Given** a question the bank cannot support, **When** the DM asks the Co-DM, **Then** the agent says it does not know and does not invent lore, mechanics, or secret information.

---

### User Story 3 - Present accepted content at the table (Priority: P3)

The DM takes accepted content (handout, recap, map note, NPC line, clue) and presents it on the player-facing play surface so the table sees the same artifact the DM approved.

**Why this priority**: Closes the communication loop. Depends on accepted content from P2; the table still plays if the DM pastes by hand, so this is valuable automation, not the MVP of the knowledge bank.

**Independent Test**: Accept one piece of content as the DM; present it on the play surface; confirm players see that wording and not earlier drafts or rejected proposals.

**Acceptance Scenarios**:

1. **Given** content the DM has accepted, **When** the DM presents it to the table, **Then** players see that content on the play surface.
2. **Given** a draft or rejected proposal, **When** anyone tries to present it, **Then** it is not shown to players.
3. **Given** content already presented, **When** the DM presents an updated accepted version, **Then** players see the updated version rather than mixed draft text.

---

### User Story 4 - Return table outcomes to the bank (Priority: P4)

After a session, the DM captures what actually happened (new facts, deaths, promises, revealed secrets, rulings). Those outcomes are distilled back into the knowledge bank so the next session's agent proposals match play, not the pre-session plan.

**Why this priority**: Prevents the second brain from lying to the next session. Can wait until P1–P3 exist; a DM can still edit pages by hand.

**Independent Test**: Record one session outcome that contradicts prep; confirm the knowledge bank reflects the outcome; confirm a later agent answer uses the outcome, not the obsolete prep.

**Acceptance Scenarios**:

1. **Given** a finished session with at least one new or changed fact, **When** the DM files the outcome, **Then** the knowledge bank pages update to match play.
2. **Given** an updated page, **When** the DM later asks the Co-DM about that fact, **Then** the agent cites the post-session page, not the superseded prep.

---

### Edge Cases

- Source contradicts an existing page: surface the conflict to the DM; do not silently overwrite.
- Two pages describe the same entity under different names: DM can merge or link; the agent must not treat them as unrelated once linked.
- Empty or uningested campaign: agent refuses to invent; DM is told the bank has no coverage.
- DM is mid-session and has no time to review: nothing is auto-presented; the table waits on the DM.
- Player-facing content would reveal a secret the bank marks unrevealed: it stays off the play surface until the DM accepts a reveal.
- Ingest fails partway: already-written pages remain; the DM is told which sources did not land.
- Agent proposal cites a page the DM has since deleted: proposal is invalid until regenerated.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: A DM MUST be able to ingest campaign sources into a compiled knowledge bank of distilled, interconnected pages.
- **FR-002**: The knowledge bank MUST be browseable and editable in the DM's second-brain workspace.
- **FR-003**: Distilled pages MUST retain a traceable link back to the source material they came from.
- **FR-004**: The Co-DM agent MUST retrieve answers from the knowledge bank rather than from unaudited conversation memory.
- **FR-005**: Every agent proposal to the DM MUST include citations to knowledge-bank pages, or an explicit "unknown" when coverage is missing.
- **FR-006**: The agent MUST address the DM, never the players, unless the DM has accepted content and chosen to present it.
- **FR-007**: The DM MUST be able to accept, edit, or reject each proposal before it is eligible for the table.
- **FR-008**: Only accepted content MUST be presentable on the player-facing play surface.
- **FR-009**: The play surface MUST show players the accepted wording, not drafts or rejected alternatives.
- **FR-010**: The DM MUST be able to file session outcomes so the knowledge bank reflects what happened in play.
- **FR-011**: When sources or outcomes conflict, the system MUST show the conflict to the DM instead of picking a winner.
- **FR-012**: Content marked unrevealed MUST NOT appear on the player-facing play surface until the DM accepts a reveal.
- **FR-013**: Agent and DM communication MUST be inspectable after the fact (what was asked, proposed, accepted, and presented).

### Key Entities

- **Campaign**: The bounded body of play this instance serves (one table, one campaign for v1).
- **Source**: Raw material ingested into the bank (notes, recaps, published text, transcripts).
- **Page**: A distilled, named unit of campaign knowledge the DM can open and the agent can cite.
- **Citation**: A pointer from an agent proposal or distilled claim to the page(s) that support it.
- **Proposal**: Agent output addressed to the DM; not player-visible until accepted.
- **Accepted Content**: A proposal the DM has approved (possibly after edit); the only class of content eligible for the table.
- **Play Surface Artifact**: The player-visible form of accepted content (handout, recap, scene text, and similar).
- **Session Outcome**: A fact established at the table that must update the knowledge bank.
- **Reveal State**: Whether a fact is still secret from the players.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A DM who knows the campaign can locate a specific fact in the second brain in under 2 minutes without asking the agent.
- **SC-002**: In a 10-question factual quiz drawn from ingested sources, the Co-DM cites supporting pages on at least 9 answers and answers "unknown" rather than inventing on the rest.
- **SC-003**: 100% of player-visible artifacts in a test session match DM-accepted wording; 0% of rejected or draft proposals reach the play surface.
- **SC-004**: After filing a session with at least three new or changed facts, a later Co-DM recap of those facts matches the outcomes, not the pre-session prep, on all three.
- **SC-005**: A DM can complete one full loop — ingest a source, ask for a proposal, accept it, present it, file the outcome — in a single prep-plus-session sitting without a second operator.
- **SC-006**: In a debrief of at least three sessions, the DM rates the agent→DM handoff as "usable at the table" for 80% or more of proposals (clear, cited, short enough to review under time pressure).

## Assumptions

- Primary user is a human DM. Players receive content; they do not operate the knowledge bank or the agent.
- The agent is a co-DM: it proposes; the DM is the authority. Nothing is auto-presented to players.
- v1 is one campaign and one table. Multi-campaign orchestration is out of scope.
- Rules system is not locked; the bank holds whatever sources the DM ingests.
- Designated surfaces (product choices, not success metrics): knowledge bank follows the compiled-wiki pattern (raw sources → distilled pages → queryable schema); the DM workspace is an Obsidian vault; the player-facing play surface is Foundry VTT.
- This repository is an experiment in agent-to-human and human-to-human communication quality, not a fully autonomous GM.
- Out of scope for this spec: player accounts in the knowledge bank, live voice at the table, billing, and replacing the DM.

