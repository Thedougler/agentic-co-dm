# Feature Specification: Agentic Co-DM

**Feature Branch**: `001-agentic-co-dm`

**Created**: 2026-09-11

**Status**: Draft

**Input**: User description: "We are building an agentic co-dm system utilizing the llm-wiki design for knowledge bank, obsidian vault for the user interface for the second brain, and foundryvtt for presenting the content to the players during play. This repo is largely an exercise and experimentation in agent to human communication to human communication."

## Clarifications

### Session 2026-09-11

- Q: When does the Co-DM run? → A: Prep before a session and wrapup after. Never during a session. Only the human DM is present at the table (may be revisited later).
- Q: What must this system be good at? → A: Agent→DM→table communication quality and campaign/session craft. Both.
- Q: What does the table hear and see? → A: Theatre of the mind (spoken language the DM can read aloud) and Foundry play-surface artifacts, both staged in prep.
- Q: Who wins if fun and bank facts conflict? → A: Fun may shape Work. Bank facts change only when the DM accepts a canon proposal. No silent invention.
- Q: What is current vs this repo? → A: The live Co-DM vault (ai-co-dm) is current. This repo is a candidate redesign, not the campaign of record until cutover.
- Q: What is the vault shape? → A: A prose wiki — typed Obsidian pages and templates the DM opens. Not a compiler/OS.
- Q: What drives the redesign? → A: Best practice. Not a patch list of current-vault failures. Domain docs are a glossary; they do not record work packets or operational grain.
- Q: Which copied D&D skills belong in v1? → A: All of them. The full copied D&D campaign-craft toolkit is in v1; none of it is deferred.
- Q: Does v1 lock this Co-DM to D&D 5e? → A: Yes. v1 is D&D 5e; other systems are out of scope.
- Q: When may the Co-DM invent new 5e material the bank does not already contain? → A: Invention is required and encouraged. Ground it in established lore; never contradict a page; it is Work until the DM accepts. Do not refuse to invent. Do not present invention as a bank fact.
- Q: What counts as established lore that invention must be grounded in? → A: Bank pages + D&D 5e rules. A published adventure is lore only after it is ingested.
- Q: What is the compiled campaign knowledge called? → A: The wiki (formerly referred to as "knowledge bank"). Do not call it the bank.
- Q: How must wiki pages be written? → A: Full normal sentences. High-quality copy a human can read. No AI shorthand or telegraphic agent-speak.

### Session 2026-09-12

- Q: What must the Co-DM show you and get approved before it is allowed to create it? → A: Any new or changed campaign wiki page. A named ingest is approval for those sources only; no extra pages.
- Q: When you approve ingest of a recap, may the Co-DM also create separate wiki pages for people and places named in that recap? → A: Yes, thin minimal stubs, lazily, for names that appear in the source (including as links). A recap may create many small partial files to expand later. Invented names not in the source still need a separate proposal.
- Q: When you approve ingest of a campaign note that already uses your finished Obsidian section layout, what should the Co-DM do to that formatting? → A: Keep that layout only for these early-development sample notes; it is not a general ingest rule. General ingest still distills.
- Q: Should templates and skills follow the sample note layouts? → A: Yes. Study the early-dev samples and align templates and skills to them. Creature notes are linear (no column wrappers). This is not a general ingest-preserve rule.


## User Scenarios & Testing *(mandatory)*

### User Story 1 - Distill campaign knowledge into a second brain (Priority: P1)

A Dungeon Master (DM) has campaign notes, adventure text, session recaps, and table rulings scattered across sources. They name those sources and approve ingest. The Co-DM distills those sources into compiled wiki pages written in complete sentences a human can read, and may add thin stub pages for people, places, and things named in those sources. It does not invent extra pages for names the sources do not contain. The DM browses and corrects that wiki in their existing second-brain workspace. The Co-DM agent can retrieve from the same wiki.

**Why this priority**: Without a shared, citable wiki there is nothing trustworthy for the agent to say or for the DM to hand to the table. This slice is a usable second brain even if the agent never speaks.

**Independent Test**: Name a small set of campaign sources and approve ingest; open the compiled pages in the DM workspace; confirm the pages are linked and match those sources; confirm stub pages exist only for names in those sources; confirm a human can read them as ordinary prose without decoding agent shorthand; confirm the agent can answer a question from those pages with a citation.

**Acceptance Scenarios**:

1. **Given** a campaign with at least one source (notes, recap, or published text) the DM has named for ingest, **When** the DM approves ingest, **Then** the wiki contains distilled pages from those sources the DM can open in their second-brain workspace, plus thin stub pages only for names that appear in those sources.
2. **Given** distilled pages exist, **When** the DM follows links between related people, places, and events named in the sources, **Then** they reach the related stub or page without leaving the workspace.
3. **Given** a distilled page, **When** the DM edits it, **Then** the corrected text is what later retrieval uses.
4. **Given** ingested sources, **When** the DM asks the Co-DM a factual question covered by those sources, **Then** the agent answers from the wiki and names the page(s) it used.
5. **Given** a newly distilled page, **When** a human DM opens it, **Then** it is written in complete sentences they can understand without a decoder ring for agent jargon.

---

### User Story 2 - Agent proposes; DM decides (Priority: P2)

During prep, the DM asks the Co-DM for any procedure in the v1 campaign-craft toolkit (ruling, recap, NPC, place, dungeon, encounter, item, faction, travel, beat, mouth copy, play-surface staging, and the rest of the copied D&D pack). The agent replies to the DM only, with a short proposal and citations. It does not create or change a campaign wiki page until the DM approves that proposal. The DM accepts, edits, or rejects before anything is eligible for the table. The Co-DM does not run during the session.

**Why this priority**: The repo's experiment is agent → human (DM) → human (players). The agent is a co-DM in prep and wrapup, not the table's voice. This slice works against a frozen wiki.

**Independent Test**: In prep, ask for a table-facing beat covered by the wiki and for a new NPC the wiki lacks; confirm both are DM-addressed proposals and that no wiki page is created until the DM approves; confirm the new NPC is marked invention, grounded in wiki pages and/or 5e rules, and not written as canon until accepted; confirm players see nothing; confirm the agent is not in the session.

**Acceptance Scenarios**:

1. **Given** a question the wiki can answer, **When** the DM asks the Co-DM in prep, **Then** the DM receives a concise proposal plus citations, no wiki page is created yet, and players receive nothing.
2. **Given** a proposal, **When** the DM edits and accepts it, **Then** the accepted wording is the only version marked ready for the table, and only then may a wiki page be created or changed.
3. **Given** a proposal, **When** the DM rejects it, **Then** it is not written to the wiki, is not marked ready for the table, and is not shown to players.
4. **Given** a gap the wiki does not cover, **When** the DM asks the Co-DM, **Then** the agent invents a proposal grounded in wiki pages and D&D 5e rules, marks it as invention, does not contradict existing pages, does not write a wiki page until the DM approves, and does not write it as canon until accepted.
5. **Given** a session in progress, **When** play is happening, **Then** no Co-DM agent is running.
6. **Given** the v1 campaign-craft toolkit, **When** the DM requests any procedure in that toolkit during prep or wrapup, **Then** that procedure is available and its output is addressed to the DM, not the players.

---

### User Story 3 - Present accepted content at the table (Priority: P3)

The DM takes accepted content (handout, recap, map note, NPC line, clue) and presents it on the player-facing play surface so the table sees the same artifact the DM approved.

**Why this priority**: Closes the communication loop. Depends on accepted content from P2; the table still plays if the DM pastes by hand, so this is valuable automation, not the MVP of the wiki.

**Independent Test**: Accept one piece of content as the DM; present it on the play surface; confirm players see that wording and not earlier drafts or rejected proposals.

**Acceptance Scenarios**:

1. **Given** content the DM has accepted, **When** the DM presents it to the table, **Then** players see that content on the play surface.
2. **Given** a draft or rejected proposal, **When** anyone tries to present it, **Then** it is not shown to players.
3. **Given** content already presented, **When** the DM presents an updated accepted version, **Then** players see the updated version rather than mixed draft text.

---

### User Story 4 - Return table outcomes to the wiki (Priority: P4)

After a session, the DM captures what actually happened (new facts, deaths, promises, revealed secrets, rulings). The Co-DM proposes those outcomes. Wiki pages update only after the DM approves, so the next session's agent proposals match play, not the pre-session plan.

**Why this priority**: Prevents the second brain from lying to the next session. Can wait until P1–P3 exist; a DM can still edit pages by hand.

**Independent Test**: Propose one session outcome that contradicts prep; after the DM approves, confirm the wiki reflects the outcome; confirm a later agent answer uses the outcome, not the obsolete prep.

**Acceptance Scenarios**:

1. **Given** a finished session with at least one new or changed fact, **When** the DM approves the filed outcome, **Then** the wiki pages update to match play.
2. **Given** an updated page, **When** the DM later asks the Co-DM about that fact, **Then** the agent cites the post-session page, not the superseded prep.

---

### Edge Cases

- Source contradicts an existing page: surface the conflict to the DM; do not silently overwrite.
- Two pages describe the same entity under different names: DM can merge or link; the agent must not treat them as unrelated once linked.
- Empty or uningested campaign: the Co-DM still invents a proposal (5e-grounded), marks it as invention, does not write a wiki page until the DM approves, and does not fake campaign-page citations.
- DM is mid-session: the Co-DM is not running; nothing is auto-presented; the table waits on the DM.
- Player-facing content would reveal a secret the wiki marks unrevealed: it stays off the play surface until the DM accepts a reveal.
- Ingest fails partway: already-written pages remain; the DM is told which sources did not land.
- Agent proposal cites a page the DM has since deleted: proposal is invalid until regenerated.
- Fun would play better if a wiki fact changed: the Co-DM may propose the change; it does not silently edit canon.
- Published adventure or setting not in the wiki: it is not lore; do not ground invention in unaudited module memory.
- Distilled page is telegraphic AI shorthand: it is not done; rewrite as ordinary prose before it counts as a wiki page.
- Named ingest would mint a page for a person, place, or thing the source does not name: propose it; do not write it.
- Agent creates a campaign wiki page without a prior approved proposal (and it is not a stub for a name in an approved ingest): invalid; delete or do not file.
- Early-development sample notes already in the DM's finished layout: ingest keeps their section order, markdown, callouts, tables, and embeds. This is not a general ingest rule.


## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: A DM MUST be able to ingest campaign sources into a compiled wiki of distilled, interconnected pages.
- **FR-002**: The wiki MUST be browseable and editable in the DM's second-brain workspace.
- **FR-003**: Distilled pages MUST retain a traceable link back to the source material they came from.
- **FR-004**: The Co-DM agent MUST retrieve answers from the wiki rather than from unaudited conversation memory.
- **FR-005**: Claims about existing canon MUST cite wiki pages. Invented Work MUST be marked as invention, grounded in established lore (wiki pages and D&D 5e rules), and MUST NOT contradict an existing page. The Co-DM MUST NOT present invention as a wiki fact. Uningested published adventures are not lore.
- **FR-006**: The agent MUST address the DM, never the players, unless the DM has accepted content and chosen to present it.
- **FR-007**: The DM MUST be able to accept, edit, or reject each proposal before a campaign wiki page is created or changed and before it is eligible for the table.
- **FR-008**: Only accepted content MUST be presentable on the player-facing play surface.
- **FR-009**: The play surface MUST show players the accepted wording, not drafts or rejected alternatives.
- **FR-010**: The DM MUST be able to file session outcomes so the wiki reflects what happened in play.
- **FR-011**: When sources or outcomes conflict, the system MUST show the conflict to the DM instead of picking a winner.
- **FR-012**: Content marked unrevealed MUST NOT appear on the player-facing play surface until the DM accepts a reveal.
- **FR-013**: Agent and DM communication MUST be inspectable after the fact (what was asked, proposed, accepted, and presented).
- **FR-014**: The Co-DM MUST run only in prep and wrapup, never during a session.
- **FR-015**: The Co-DM MUST NOT silently change wiki facts; canon edits require a DM-accepted proposal. Fun MAY shape Work without changing canon.
- **FR-016**: v1 MUST include the full D&D 5e campaign-craft toolkit copied into this repository (prep, wrapup, mouth, play-surface staging, and design procedures). No procedure in that pack is deferred.
- **FR-017**: The Co-DM MUST invent when craft needs new 5e material. Invention is required, not a last resort. It is a proposal until the DM approves. It MUST NOT be filed as a wiki page before that approval.
- **FR-018**: Wiki pages MUST be written in complete sentences of high-quality human prose. They MUST NOT use AI shorthand, telegraphic agent-speak, or other copy a human DM cannot read as ordinary language. Stub pages MUST still use complete sentences; they MAY be short.
- **FR-019**: The Co-DM MUST NOT create or change a campaign wiki page until the DM has approved a proposal. A named ingest is approval for those sources and for thin stub pages of people, places, and things named in those sources. The Co-DM MUST NOT add pages for names the approved sources do not contain.


### Key Entities

- **Campaign**: The bounded body of play this instance serves (one table, one D&D 5e campaign for v1).
- **Source**: Raw material ingested into the wiki (notes, recaps, published text, transcripts).
- **Wiki**: Compiled, citable campaign pages the DM browses and the Co-DM retrieves from (formerly referred to as "knowledge bank"). Pages are human prose, not agent notes.
- **Page**: A distilled, named unit of campaign knowledge the DM can open and the agent can cite. A stub is a short Page for a name that appeared in an approved source, to be expanded later.
- **Citation**: A pointer from an agent proposal or distilled claim to the page(s) that support it.
- **Co-DM**: Agent work in prep and wrapup. It addresses the DM, never the players, and does not run during a session.
- **Prep**: The before-session window where the Co-DM authors Work for the DM.
- **Wrapup**: The after-session window where the Co-DM files session outcomes into the wiki.
- **Session**: Table time with only humans present.
- **Proposal**: Agent output addressed to the DM, shown before any wiki write; not player-visible until accepted.
- **Work**: Mutable prep the DM may accept, edit, or reject before it is filed to the wiki or eligible for the table.
- **Accepted Content**: A proposal the DM has approved (possibly after edit); the only class of content eligible for the table.
- **Play Surface Artifact**: The player-visible form of accepted content (handout, recap, scene text, map, token, and similar).
- **Theatre of the mind**: Spoken, sensory language the DM can read aloud.
- **Session Outcome**: A fact established at the table that must update the wiki.
- **Reveal State**: Whether a fact is still secret from the players.
- **Canon proposal**: A suggested change to wiki facts; not applied unless the DM accepts.
- **Craft toolkit**: The Co-DM's prep and wrapup procedures. In v1 this is the full D&D 5e pack copied into this repository, not a subset.
- **Established lore**: Wiki pages plus D&D 5e rules. Published adventures count only after ingest.


## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A DM who knows the campaign can locate a specific fact in the second brain in under 2 minutes without asking the agent.
- **SC-002**: In a 10-question factual quiz drawn from ingested sources, the Co-DM cites supporting pages on at least 9 answers and does not present invented material as a wiki fact on the rest.
- **SC-003**: 100% of player-visible artifacts in a test session match DM-accepted wording; 0% of rejected or draft proposals reach the play surface.
- **SC-004**: After the DM approves filing a session with at least three new or changed facts, a later Co-DM recap of those facts matches the outcomes, not the pre-session prep, on all three.
- **SC-005**: A DM can complete one full loop — name and approve ingest of a source, ask for a proposal in prep, accept it (wiki write only then), present it at the table without an agent running, approve filing the outcome in wrapup — in a single prep-plus-session sitting without a second operator.
- **SC-006**: In a debrief of at least three sessions, the DM rates prep handoff as "usable at the table" for 80% or more of accepted Work (clear, cited, runnable without a live agent).
- **SC-007**: For every procedure in the v1 D&D 5e campaign-craft toolkit, a DM can request it in the correct window (prep or wrapup) and receive DM-addressed output; zero procedures from that pack are missing.
- **SC-008**: Given a design request the wiki does not already contain, the Co-DM produces a proposal (not a wiki page) that names the wiki pages and/or 5e rules it is grounded in, contradicts zero existing pages, does not cite uningested published adventures as lore, and is not filed to the wiki until the DM approves.
- **SC-009**: A DM who knows the campaign but not agent jargon can read three newly distilled wiki pages and understand them as ordinary prose, with zero pages that require decoding shorthand.


## Assumptions

- Primary user is a human DM. Players receive content; they do not operate the wiki or the agent.
- The agent is a co-DM in prep and wrapup: it proposes; the DM is the authority and the only runtime during a session. Nothing is auto-presented to players.
- v1 is one campaign and one table. Multi-campaign orchestration is out of scope.
- v1 is D&D 5e. Other rules systems are out of scope.
- Designated surfaces (product choices, not success metrics): the wiki is a prose wiki (typed pages and templates; raw sources → distilled pages); the DM workspace is an Obsidian vault; the mouth surface is theatre of the mind; the player-facing play surface is Foundry VTT. Both mouth and screen are staged in prep.
- The D&D 5e campaign-craft skill pack copied into this repository is the v1 Co-DM toolkit. All of it ships in this feature.
- This repository is a candidate redesign of the current live Co-DM vault. That vault remains the campaign of record until cutover. The redesign follows best practice, not a failure catalog.
- Domain language lives in `CONTEXT.md`. That glossary does not record work packets or operational grain.
- This repository is an experiment in agent-to-human and human-to-human communication quality and in campaign craft, not a fully autonomous GM.
- The Co-DM is a creative partner. Invention is required and encouraged, always as a proposal, always grounded in wiki pages and D&D 5e rules, never as a wiki write before DM approval, never as a silent wiki edit.
- Wiki pages are for humans. Complete sentences, high-quality copy. Agent-facing skills may be terse; the wiki may not.
- Early development only: sample campaign notes already written in the DM's preferred layout keep that formatting on ingest. Templates and skills for place, item, hazard, and creature notes follow those samples. Creature notes are linear. Later or other sources still distill. This is not a standing layout-preservation rule for every ingest.
- Out of scope for this spec: player accounts in the wiki, live voice at the table, a Co-DM agent running during a session, billing, replacing the DM, and non-5e rules systems.
