# Feature Specification: Session Beat Format

**Feature Branch**: `007-session-beats-format`

**Created**: 2026-09-12

**Status**: Draft

**Input**: User description: "Ive supplied high quality production ready session 11 beats for the entire planned session. These are the exact layout, format, quality, obsidian markdown shape we want, the best yet. New session beats should be composed in this format and when ingested there formatting should be maintained" plus later direction: define a folder structure for sessions as well.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - New beats match the Session 11 cockpit (Priority: P1)

A Co-DM authors a new live beat for a planned session. The DM opens that beat in Reading view and gets the same scan jobs, section order, and wiki-markdown shape as the Session 11 production beat cards: timebox and glance side by side, current situation, compact action cards, spoken opening, procedure, zones, rulings, fuse, handoff, then backup and battlemap when those exist.

**Why this priority**: Session 11 is the first full planned session whose beat cards are production-ready. Later sessions fail if they invent a second cockpit.

**Independent Test**: Hand a newly composed live beat (not copied from a Session 11 filename) to a second DM. They can timebox the slice, speak the opening, place the party, roll default-mode numbers, and name the next state from that page alone, and they judge the page the same kind of card as a Session 11 beat.

**Acceptance Scenarios**:

1. **Given** a new live beat, **When** the DM opens it in Reading view, **Then** they see the Session 11 cockpit jobs in Session 11 order: scene end plus glance, Now, action cards, Initial Narration, procedure, zones, Be ready for, threat clock when a fuse exists, How the Scene Resolves, backup links, and battlemap at the bottom when art exists.
2. **Given** that beat, **When** they scan without editing, **Then** columns, tables, spoken callouts, highlighted table speech, wikilinks, and image embeds are intact — not flattened into a single knowledge dump.
3. **Given** a thin Development and a dense Cliffhanger, **When** a DM compares them to Session 11 cards of those types, **Then** unused jobs are omitted rather than left as empty headings, and both still read as the same kind of beat card.
4. **Given** the first beat of a session, **When** the DM opens it, **Then** a previous-session recap may appear. **Given** any later beat, **When** the DM opens it, **Then** it starts from the current situation and does not recap earlier beats.

---

### User Story 2 - Ingest keeps the beat shape (Priority: P1)

The DM asks to ingest or promote Session 11 beats, or later beats written in that shape, into the wiki. After ingest, Reading view still shows the same cockpit: columns, tables, spoken callouts, highlighted conditional speech, wikilinks, and embeds. Ingest does not compile a beat into a distilled concept page.

**Why this priority**: Distilling these files as ordinary knowledge sources is the named failure. The product the DM runs is the page shape, not extracted facts.

**Independent Test**: Ingest one complete Session 11 beat card and one newly composed beat in the same shape. Open both wiki pages in Reading view. Layout jobs and markdown treatments still match the source files.

**Acceptance Scenarios**:

1. **Given** a complete Session 11 beat card, **When** it is ingested or promoted into the wiki, **Then** the wiki page keeps the source body shape: heading spine, column pairs, tables, `[!narration]` blocks, highlighted narration cells, wikilinks, and image embeds.
2. **Given** that ingested page, **When** the DM runs the beat, **Then** they do not need the `_raw/` source to recover layout or rulings.
3. **Given** a mixed ingest that also includes ordinary knowledge sources, **When** those sources are compiled, **Then** beat cards and the session spine are still filed as session-prep pages with their layout preserved.
4. **Given** an already-ingested beat, **When** ingest runs again with no body change, **Then** the cockpit is not rewritten into a different template.

---

### User Story 3 - The session spine stays the chart, not a second cockpit (Priority: P2)

A Co-DM authors the session-level chart for a planned session. The DM opens that spine and sees the Session 11 session note jobs: length, tone, prize, opposition, Hook/Climax/Resolution labels, dramatic spine, numbered skeleton linking each live beat, and per-beat purpose / table sees / truth / pressure / if they break / landing. They then run tonight from the linked beat cards, not from a rewritten cockpit on the spine.

**Why this priority**: Session 11 ships a spine plus beat cards. Collapsing both into one format, or turning the spine into a tenth cockpit, breaks the planned session.

**Independent Test**: A second DM names tonight's Hook, the beat order, and where to start from the spine alone, then opens beat 1 and runs from that card.

**Acceptance Scenarios**:

1. **Given** a new planned session, **When** the DM opens the spine, **Then** they can name length, prize, opposition, dramatic spine, and the numbered beat list with links to each card.
2. **Given** that spine, **When** they pick a beat, **Then** they follow a link to a cockpit card; the spine does not duplicate Scene ends when, Zones, or Be ready for.
3. **Given** ingest of that spine, **When** the wiki page opens, **Then** the skeleton, beat summaries, and links remain in the Session 11 session-note shape.

---

### User Story 4 - One folder is the session home (Priority: P1)

The DM opens tonight's session as one folder, not a flat dump of `_raw/` files mixed with unrelated notes. That folder holds the spine, the numbered beat cards, and only that session's companion notes. Owner pages for places, creatures, people, and items stay on their owner paths. After ingest, Session 11 and later planned sessions live in that home with names the DM can scan in order.

**Why this priority**: Format without a home still leaves the DM hunting. Ingest has nowhere stable to file a preserved beat.

**Independent Test**: Point a second DM at the session folder for a planned night. They open the spine, then beat 1 through the last beat, in order, without searching the vault root or `_raw/`.

**Acceptance Scenarios**:

1. **Given** a planned session, **When** the DM opens its session folder, **Then** they see the spine, each live beat card in numbered order, and any companion notes for that night only.
2. **Given** that folder, **When** they follow a creature, place, or item mentioned on a beat, **Then** they land on the owner page outside the session folder — the beat is not a second copy of the owner.
3. **Given** ingest of Session 11, **When** filing completes, **Then** the spine and beat cards sit in the Session 11 folder with Session 11 filenames preserved, not scattered into knowledge categories.
4. **Given** a new session 12, **When** it is composed and accepted, **Then** it gets its own folder beside Session 11 and does not share a dump with it.

### Edge Cases

- A job has no content this slice (no combat roster, no secondary objective, no battlemap, no recap): omit the section; do not leave an empty heading.
- The first beat may embed a previous-session recap; later beats must not.
- Companion notes such as a session hazards table are not beat cards and are not scored against the cockpit layout.
- Older session-prep that was not authored as Session 11 production beats is out of scope: do not rewrite it solely to match this format.
- Work is not wiki until the DM accepts; a proposed beat still uses this shape.
- Ingest of a rejected or unaccepted draft does not publish a wiki page.
- Column pairs appear only when both sides have content; a missing partner does not leave a blank column.
- If play breaks the chart, the spine's rebuild log records the break; beat cards are recomposed in the same cockpit shape rather than patched into a new format.
- Staging in `_raw/` is not the long-term session home; ingest or accept files the session into its folder.
- Two campaigns MUST NOT share one session-number folder.
- A companion note belongs in the same session folder and MUST NOT be renamed into a beat-card filename.
- Session logs from wrapup MAY join that session folder; they MUST NOT replace the spine or beat cards.
- Attachments and battlemaps stay in the campaign attachments tree; the session folder stores pages, not a second media dump.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The Session 11 production beat cards are the format standard for new live session-prep beats. New beats MUST be composed in that layout, quality, and wiki-markdown shape. Those files are evidence of the standard; authors MUST NOT photocopy a named Session 11 title as the only valid beat.
- **FR-002**: A live beat page MUST present the Session 11 cockpit jobs in Session 11 order: identity and summary; optional first-beat recap; overview art when it exists; Scene ends when paired with At a Glance; Now; Action cards; Initial Narration; Procedure paired with Secondary objective when a second question exists; Zones; Be ready for; Threat clock paired with bloodied, cover, or dials when a fuse exists; How the Scene Resolves; Roster embeds when combat-mode sheets will be rolled; Backup links; Battlemap at the bottom when art exists.
- **FR-003**: At a Glance MUST scan as stakes, goal or exit, danger, silence discipline, and situation magnets. Scene ends when MUST state the stop condition, a roughly thirty-minute budget, and behind/ahead cuts when pacing is not obvious.
- **FR-004**: Spoken player text MUST live in `[!narration]` for unconditional speech and in highlighted italic table cells for conditional speech. Those surfaces MUST remain theatre of the mind: no secrets, difficulty classes, or unearned names. The only callout on a beat card is `[!narration]`. Callouts on live session surfaces MUST stay open.
- **FR-005**: Beat cards MUST use the Session 11 wiki-markdown treatments: heading spine, column pairs for dashboard / procedure / clock / roster, ruling tables, wikilinks to owners, and image embeds. DM-facing lines MUST be complete grammatical sentences. Body text MUST use real line breaks. Checks and saves MUST follow the vault's at-table scan grammar.
- **FR-006**: Empty sections MUST NOT appear. A missing job is omitted. Density follows what this slice spends at the table, not a cloned outline.
- **FR-007**: When a session-prep beat or session spine is ingested or promoted into the wiki, the system MUST preserve the source layout and markdown treatments. It MUST NOT distill those pages into knowledge-wiki concept pages, flatten columns or tables, rewrite callouts, or replace the cockpit with a different template.
- **FR-008**: Mixed ingest MUST keep compiling ordinary knowledge sources as compiled wiki pages, while session-prep beats and spines remain session-prep pages with FR-007 preservation.
- **FR-009**: A planned session MUST have a session spine in the Session 11 session-note shape: working title, length, tone, prize, opposition, Hook/Climax/Resolution labels, dramatic spine, numbered skeleton with links to each live beat, and per-beat purpose, table sees, truth, pressure, if they break, and landing. The spine MUST NOT duplicate the beat cockpit.
- **FR-010**: Beat identity MUST stay aligned with the spine: the card's number matches its skeleton position, and How the Scene Resolves hands to a beat on that skeleton.
- **FR-011**: Numbers that belong on an owner page (creature sheet, item effect, place rule) MUST be linked or heading-embedded from the owner. Default-mode action-card numbers the DM will roll this slice MAY sit on the beat. The beat MUST NOT become a second full owner page.
- **FR-012**: The Co-DM MUST apply this format when proposing or filing new session beats. No campaign wiki write until the DM accepts, except named ingest stubs. Companion encounter tables for a session are out of scope for the cockpit standard.
- **FR-013**: Existing session-prep that is not part of the Session 11 production set MUST NOT be rewritten solely to match this format.
- **FR-014**: Each planned session MUST have one session folder as its home. The folder MUST contain the spine, the numbered live beat cards, and only that session's companion notes. It MUST NOT hold owner pages for places, creatures, people, or items.
- **FR-015**: Session folders MUST be grouped by campaign, then by session number, under the wiki's time-bound journal tree: `journal/sessions/<campaign-slug>/<session-number>/`. Session 11 files to `journal/sessions/shattered-sea/11/`. A later session uses the same pattern with its own number. Staging remains `_raw/` until ingest or accept.
- **FR-016**: Beat and spine filenames MUST keep the Session 11 pattern: `Session-<number>-00-<Spine-Title>` for the spine, `Session-<number>-<beat-number>-<Label>` for live beats, two-digit beat numbers (`01`, `02`, …). Companion notes in that folder MUST NOT use a live beat number.
- **FR-017**: Ingest or promote of session-prep MUST file pages into that session folder and MUST preserve those filenames. It MUST NOT scatter beats into `concepts/`, `entities/`, or other knowledge folders.

### Key Entities

- **Session beat card**: One live slice of session-prep the DM runs for about thirty minutes. Session 11 cards `01` through `10` are the format evidence.
- **Session spine**: The session-level chart that lists tonight's beats and why they exist. Session 11 `Birds of a Feather` is the format evidence.
- **Cockpit**: The Reading-view layout of a beat card — the jobs and markdown shape the DM scans while running.
- **Wiki-markdown shape**: Columns, tables, open spoken callouts, highlighted conditional speech, wikilinks, embeds, and real line breaks as they appear on the Session 11 beat cards.
- **Ingest / promote**: Filing an approved session-prep source into the wiki. For beats and spines, filing preserves shape; it does not compile facts away from the page.
- **Companion note**: A session-adjacent table or encounter list (for example a hazards table). Not a beat card.
- **Work**: Mutable prep. Not wiki until the DM accepts.
- **Owner page**: The canon page for a creature, place, item, or person. Beats link or embed; they do not replace owners.
- **Session folder**: The DM's home for one planned night — spine, beat cards, optional companion notes. Not a media folder and not an owner-page folder.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A DM who knows the campaign can open a newly composed live beat and start that slice in under 45 seconds without asking the author or opening a second page for the same default-mode rulings.
- **SC-002**: In a side-by-side Reading-view comparison of a new live beat against a Session 11 beat of the same type, a second DM judges them the same kind of card (same jobs and markdown shape), not a different campaign format.
- **SC-003**: After ingest or promote of the full Session 11 planned session (spine plus live beat cards), 100% of those wiki pages still show their source heading spine, column pairs, tables, spoken callouts, and embeds in Reading view.
- **SC-004**: In a read-aloud test of Initial Narration and How the Scene Resolves on at least three Session 11 beats and one newly composed beat, 100% can be spoken to players without a secret, difficulty class, or unearned name.
- **SC-005**: On a mixed ingest that includes at least one beat card and one ordinary knowledge source, 0% of beat cards are rewritten as distilled concept pages, and the knowledge source is still compiled as a wiki page.
- **SC-006**: After this format is in force, 0% of older non-Session-11 session-prep is rewritten solely to match it.
- **SC-007**: After Session 11 is ingested, a DM can open `journal/sessions/shattered-sea/11/` and reach the spine plus every live beat in filename order in under 15 seconds, without using `_raw/`.
- **SC-008**: After a second planned session is filed, 100% of its spine and beat cards live in that session's own folder; 0% land in Session 11's folder or in knowledge-wiki category folders.

## Assumptions

- Primary reader is the human DM in Reading view. Players hear theatre of the mind and see play-surface artifacts the DM presents.
- The Session 11 files already supplied in `_raw/` are the production-ready evidence set: the session spine, live beat cards `01`–`10`. Companion hazards tables illustrate a different kind and stay out of the cockpit standard, but they file into the same session folder when they belong to that night.
- "Exact layout" means the cockpit jobs, section order, and wiki-markdown treatments on those beat cards — not a freeze of Session 11 plot, filenames, or island facts as the only valid session.
- Ingest in this feature means filing approved session-prep into the wiki. It does not mean transcript wrapup rewriting what happened at the table.
- Existing Co-DM rules still bind: complete-sentence prose; wiki writes after accept; named ingest may stub; invention is Work; owners stay canon.
- Concrete distances and compass directions remain the measurement on beat cards.
- Out of scope: mass restyle of older sessions; Foundry staging; player-facing sheets; treating companion encounter tables as beat cards; a second parallel beat format beside this standard; moving owner pages into the session folder.
