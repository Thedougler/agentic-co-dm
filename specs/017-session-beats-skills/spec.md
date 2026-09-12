# Feature Specification: Session Beat Skills

**Feature Branch**: `017-session-beats-skills`

**Created**: 2026-09-12

**Status**: Draft

**Input**: User description: "composing session beats should be split into multiple skills that load eachother as necessary, so composing session beats can be done optimally by agents following the methods of /Users/nick/Downloads/RTG-ScriptingtheGamev1.2.pdf with a main skill that loads when agents are planning a session, directing them how to compose the beats together, then beat specific skills for each type of beat, to be used when writing a new session beat of that type, editing a session beat of that type, or creating content for that session beat."

## Clarifications

### Session 2026-09-12

- Q: When a named vehicle page is written, should it include the 5e vehicle sheet from the new template (size, speed, hull HP, weapons, combat) even though vehicle-design currently forbids inventing those numbers? → A: Fill the sheet. Update skills to match the templates. Write positive instructions (jobs and done-when). Treat missing crafts as not-yet-done, now in scope — not as crafts that will never exist. Vehicle design is in scope now and going forward.
- Q: When an author creates or edits a campaign spell page, which skill is primary? → A: New `spell-design` skill is primary for write/edit/create of a spell page.
- Q: For Claude Code skill updates, what is the default prompt shape and model? → A: Minimal, focused, direct prompt with clear deliverables and completion criteria, optimized for token efficiency. Default model: Opus 4.6 medium.
- Q: When should Claude Code write skill work versus the session agent? → A: Claude Code only for novel skill design, skill redesign, or major skill-file change. Session agents do smaller edits to established files, Spec Kit pattern tweaks, and AGENTS.md. Conserve Claude Code; use it only when necessary.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Planning a session uses the composition skill (Priority: P1)

A Co-DM is planning a session, one-shot, adventure arc, or expedition evening. They load the **composition skill**. That skill directs how to compose beats together as a Beat Chart: one Hook to start, alternating Developments and Cliffhangers in the middle, one Climax then one Resolution to end. It sets polarity (action opening then a Development; cerebral opening then a Cliffhanger; the middle beat before an action Climax is a Development; the middle beat before a cerebral Climax is a Cliffhanger), the time budget (about thirty minutes per beat; Hook, Climax, and Resolution together about ninety minutes), thread planting and harvest, escalation, and transitions (how one beat's resolution becomes the next beat's trigger).

They produce a session spine: length, prize, opposition, Hook/Climax/Resolution labels, numbered skeleton, and why each beat exists. They do not need the five type-card catalogs to draw that chart.

**Why this priority**: The named failure is one blob of guidance. Session planning is a chart job. Mixing it with every Hook, Development, Cliffhanger, Climax, and Resolution card wastes attention and produces filler or railroads.

**Independent Test**: Give an author a session-planning job and no type-card catalogs. They can name tonight's Beat Chart (Hook → alternating middle pairs → Climax → Resolution), polarity, time budget, and which live threads each slot advances. A second reviewer judges the chart valid without seeing the type cards.

**Acceptance Scenarios**:

1. **Given** a job to plan a session, **When** the author starts, **Then** the composition skill is the primary skill.
2. **Given** that planning job, **When** the author produces the spine, **Then** the chart starts with one Hook, ends with one Climax then one Resolution, and places Developments and Cliffhangers only in alternating order.
3. **Given** that spine, **When** a reviewer inspects it, **Then** each prepared beat advances at least one live thread, early pairs cost less than later pairs, and How the Scene Resolves of each slot names a trigger for the next.
4. **Given** that planning job, **When** the author draws the chart, **Then** they are not required to open the Hook, Development, Cliffhanger, Climax, or Resolution type-card catalogs.

---

### User Story 2 - Writing, editing, or filling a typed beat uses that type's skill (Priority: P1)

A Co-DM is writing a new session beat of one type, editing an existing beat of that type, or creating content for that beat (situation, pressure, spoken opening, procedure, landing). They load that **type skill** as primary: Hook, Development, Cliffhanger, Climax, or Resolution.

The type skill owns that type's job, when it is complete, its cards (the proven shapes under that type), and how to fill this beat. A Hook author can finish a Hook without reading Development, Cliffhanger, Climax, or Resolution cards. The same isolation holds for the other four types, except the named seams in User Story 3.

**Why this priority**: The second half of the split. A Hook is not a Cliffhanger. Loading every type to write one beat is the same blob as before.

**Independent Test**: Give an author a job to write, edit, or fill a Development and withhold the other four type-card catalogs. The result is a Development: the decision space changed, players can name what they now know or can decide, and a second reviewer does not classify it as a Cliffhanger, Hook, Climax, or Resolution.

**Acceptance Scenarios**:

1. **Given** a job to write, edit, or create content for a Hook, **When** the author works, **Then** the Hook skill is primary and the other four type-card catalogs are not required.
2. **Given** the same kind of job for a Development, Cliffhanger, Climax, or Resolution, **When** the author works, **Then** that type's skill is primary and the other four type-card catalogs are not required.
3. **Given** a newly written or edited beat of one type, **When** a second reviewer classifies it, **Then** they name the same type the author claimed, using that type's completion test.
4. **Given** content created for a typed beat (spoken opening, pressure, procedure, landing), **When** it is placed, **Then** it serves that beat's type job and does not turn the beat into a different type.

---

### User Story 3 - Skills load each other only when the current job needs them (Priority: P2)

Composition and type skills load each other as necessary, then drop. They are not one standing bundle.

Named seams that require a second skill:

- Filling a chart slot → composition loads that type skill.
- Chart position, polarity, thread harvest, or transition is in question while writing a typed beat → the type skill loads composition.
- **Play a Cliffhanger as Hook** or **Play a Development as Hook** → Hook loads the borrowed type.
- How the Scene Resolves names the next type → the current type skill may load that next type only for the handoff, not for rewriting this beat.

Any other reason to open a second type-card catalog is a defect.

**Why this priority**: Split without load-on-need is two copies of the blob. The product is the seam list.

**Independent Test**: Walk a planning job that then fills one Hook and one Development. Record which skills were primary and which were loaded at seams. Composition was primary for the chart; Hook was primary for the Hook; Development was primary for the Development; extra type catalogs opened only if a named seam fired.

**Acceptance Scenarios**:

1. **Given** a session-planning job that then fills a named slot, **When** the author starts filling that slot, **Then** composition loads that type skill and that type skill becomes primary for the fill.
2. **Given** a typed-beat job whose chart position or polarity is unclear, **When** the author needs the chart, **Then** the type skill loads composition for that question and does not keep it as the primary skill for writing the beat.
3. **Given** a Hook that is Play a Cliffhanger as Hook or Play a Development as Hook, **When** the author writes it, **Then** Hook remains the session's one Hook and loads the borrowed type only for that opening shape.
4. **Given** a typed-beat job with no named seam, **When** the author finishes, **Then** no other type-card catalog was opened.

---

### User Story 4 - The chart still follows Scripting the Game, with player agency (Priority: P2)

The composition skill follows the Beat Chart methods in *Scripting the Game* (Pondsmith / R. Talsorian): start with a Hook; end on a Climax followed by a Resolution; Developments move the story without physical conflict; Cliffhangers are contests whose outcome stays in doubt to the end; Developments and Cliffhangers always alternate; keep Cliffhangers short and save the strongest pressure for the Climax; about one beat per half-hour of play.

It also keeps this campaign's agency gates: prepare situations not required outcomes; recompute after every beat; do not force the next scene because a slot is empty; let the chart shrink, branch, pause, or end early when the new state warrants it.

Type skills carry that type's cards from the same method (Kidnapped, Discovery, Chase, Clue, Final Battle, Happy Ending, and the rest already in campaign use), each with a trigger, stakes, player options, and an agency note. A card is chosen because the fiction calls for it, not to fill an empty slot.

**Why this priority**: The split exists so agents can follow those methods well, not so they can invent a second pacing system.

**Independent Test**: Give two reviewers a new session spine and its live beats. They confirm the three Beat Chart rules, polarity, time budget, and that no beat forces a required player outcome. They do not need to see the method source.

**Acceptance Scenarios**:

1. **Given** a newly composed session, **When** a reviewer audits order, **Then** it begins with one Hook, never places two Developments or two Cliffhangers consecutively, and ends with one Climax followed by one Resolution.
2. **Given** an action-heavy Hook, **When** the next beat is placed, **Then** it is a Development. **Given** a cerebral Hook, **When** the next beat is placed, **Then** it is a Cliffhanger.
3. **Given** an action Climax, **When** the last middle beat is placed, **Then** it is a Development. **Given** a cerebral Climax, **When** the last middle beat is placed, **Then** it is a Cliffhanger.
4. **Given** a typed beat written from a card, **When** players act, **Then** at least two viable responses exist and ignoring, failing, or redirecting the beat updates the world rather than replaying the slot.

---

### User Story 5 - Cockpit, Work, and live-beat assembly keep their owners (Priority: P3)

This split does not take jobs that already have owners. New live beats still match the Session 11 cockpit. The session spine still stays the chart, not a second cockpit. No campaign wiki write until the DM accepts. The existing live-beat assembly job still builds the page the DM runs. Theatre of the mind still owns spoken player text. Encounter, trap, place, and monster crafts still own their math and sites. Composition and type skills may hand off to those owners; they do not replace them.

**Why this priority**: A split that rewrites format or steals assembly is a different feature and would break Session 11.

**Independent Test**: After the split, compose one new live beat of any type. A second DM judges it the same kind of card as a Session 11 beat of that type. Work was proposed in chat before any wiki write. Live-beat assembly still produced the cockpit.

**Acceptance Scenarios**:

1. **Given** a new live beat written under a type skill, **When** the DM opens it in Reading view, **Then** it is the same kind of cockpit card as a Session 11 beat of that type.
2. **Given** a new session spine written under composition, **When** the DM opens it, **Then** it still does not duplicate Scene ends when, Zones, or Be ready for.
3. **Given** proposed beats, **When** the DM has not accepted, **Then** no campaign wiki page is written.
4. **Given** spoken player text on a beat, **When** it is written, **Then** theatre of the mind still owns it. **Given** a fight, trap, or site on a beat, **When** those are designed, **Then** their existing craft owners still own them.

---

### User Story 6 - Spell and vehicle wiki pages use the new templates (Priority: P2)

A Co-DM creates or edits a named **vehicle** or **spell** campaign page. They start from `wiki/templates/vehicle.md` or `wiki/templates/spell.md` (the scaffolds provided for this feature). `wiki/AGENTS.md` lists `type: vehicle` and `type: spell` and Layout jobs for those kinds. Pass is those jobs, not heading-order match. Omit unused sections.

A vehicle page is runnable at the table: spoken look, sheet (size, type, speed, crew, passengers, cargo), components (hull, helm, movement, weapons when armed), crew stations, handling, and combat. `vehicle-design` fills that page, including those numbers. Theatre of the mind still owns `[!narration]`.

A spell page is runnable at the table: spoken look of the casting, classification line, 2024 effect block (time, range, components, duration, saves, damage, conditions, scaling when it scales), then Discovery and Lore when the spell needs placement or history. `spell-design` is primary for that page. Theatre of the mind still owns `[!narration]`.

Skills that teach these pages state what to write and when the page is done. They describe work that has not been done yet as the work to do now.

**Why this priority**: The wiki has no spell or vehicle kind yet. The templates are the layout. Skills that still teach "leave the sheet blank" will not produce playable pages.

**Independent Test**: Give an author a job to create a named ship. The page starts from `wiki/templates/vehicle.md` and includes narration, a filled sheet, and hull/component figures so the craft can enter play. Give an author a job to create a spell. `spell-design` is primary. The page starts from `wiki/templates/spell.md` and includes narration, classification, and a runnable 2024 effect. A reviewer can run both without another format guide.

**Acceptance Scenarios**:

1. **Given** a job to create or edit a named vehicle, **When** the author writes the wiki page, **Then** they copy `wiki/templates/vehicle.md` and fill sheet, components, crew, handling, and combat so the vehicle can be run.
2. **Given** a job to create or edit a spell, **When** the author writes the wiki page, **Then** `spell-design` is primary, they copy `wiki/templates/spell.md`, and they fill narration, classification, and the runnable effect block.
3. **Given** `wiki/AGENTS.md`, **When** an author classifies the page, **Then** `type` may be `vehicle` or `spell`, and Layout lists jobs for those kinds.
4. **Given** `vehicle-design` after this feature, **When** an author follows it, **Then** it tells them to fill the vehicle sheet and components as part of the page.

---

### Edge Cases

- Play a Cliffhanger as Hook or Play a Development as Hook: still one Hook for the session; the borrowed type is loaded only for that opening shape; the next beat still follows polarity.
- Editing one beat on an existing spine: type skill is primary; composition loads only if order, polarity, threads, or transitions change.
- Creating content for a beat is filling that beat's jobs, not becoming encounter, trap, place, or spoken-prose crafts. Hand off; do not absorb.
- Two consecutive same-type middle beats: composition rejects the order and recomputes; it does not pad a third beat of the other type just to satisfy the chart.
- The party breaks the chart: recompute; do not force the next prepared slot.
- The central question resolves early: that resolution is the Climax; deliver Resolution rather than padding to a planned slot.
- Session length changes: Hook, Climax, and Resolution still account for about ninety minutes; remaining time is Development/Cliffhanger pairs.
- A cold open before the Hook is not a second Hook.
- A type skill restating the full Beat Chart, or composition restating another type's card catalog, is a defect.
- After this feature, no remaining single skill contains the full chart plus all five type-card catalogs.
- Existing Session 11 beats and spines are not rewritten solely to prove the split.
- Companion notes (hazards tables) are not typed beats and do not load type skills.
- Unused template sections on a new spell or vehicle page are omitted; filled jobs stay.
- A beat that needs a named craft or a spell hands off to that wiki kind; the beat skill still owns the beat.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: A job to plan a session, one-shot, adventure arc, or expedition evening MUST use the composition skill as its primary skill.
- **FR-002**: The composition skill MUST direct Beat Chart assembly: one Hook to start; Developments and Cliffhangers only in alternating order; one Climax followed by one Resolution to end; polarity as in User Story 4; about thirty minutes per beat; Hook, Climax, and Resolution together about ninety minutes; plant threads early, harvest them at the Climax, show their final state in the Resolution; escalate cost across the middle; treat How the Scene Resolves as the next beat's trigger.
- **FR-003**: A job to write a new beat of one type, edit a beat of that type, or create content for that beat MUST use that type's skill as its primary skill.
- **FR-004**: There MUST be exactly five type skills, one each for Hook, Development, Cliffhanger, Climax, and Resolution. Subtype cards MUST live with their type. There MUST NOT be a separate skill per subtype card.
- **FR-005**: A type skill MUST own that type's purpose, completion test, cards, and how to fill this beat. It MUST NOT own Beat Chart assembly.
- **FR-006**: The composition skill MUST NOT include the five type-card catalogs. A type skill MUST NOT include the full Beat Chart or another type's card catalog.
- **FR-007**: Skills MUST load each other only when the current job needs the other skill. They MUST NOT be required together as one standing bundle.
- **FR-008**: Named seams that MAY load a second skill are: composition filling a typed slot; a typed-beat job that needs chart position, polarity, threads, or transition; Play a Cliffhanger as Hook; Play a Development as Hook; a handoff whose next type must be named. Opening another type-card catalog for any other reason MUST be treated as a defect.
- **FR-009**: Play a Cliffhanger as Hook and Play a Development as Hook MUST remain Hook jobs. The session MUST still have one Hook. The borrowed type MUST load only for that opening shape.
- **FR-010**: Newly composed sessions MUST satisfy the three Beat Chart rules and polarity in User Story 4.
- **FR-011**: Prepared beats MUST be situations with at least two viable player responses. The chart MUST recompute after play rather than forcing the next prepared slot. The chart MAY shrink, branch, pause, or end early when the new state warrants it.
- **FR-012**: A card MUST be selected because current fiction calls for it, not to fill an empty slot.
- **FR-013**: New live beats MUST still match the Session 11 cockpit owned by the session-beat format standard. New spines MUST still stay the chart and MUST NOT duplicate the cockpit.
- **FR-014**: No campaign wiki write until the DM accepts, except named ingest stubs already allowed by Work rules.
- **FR-015**: Live-beat assembly, theatre of the mind, and encounter, trap, place, and monster crafts MUST keep their existing jobs. Composition and type skills MAY hand off to them and MUST NOT replace them.
- **FR-016**: Existing Session 11 beats and spines MUST NOT be rewritten solely to satisfy this feature.
- **FR-017**: After this feature, no single skill MAY contain the full Beat Chart plus all five type-card catalogs.
- **FR-018**: Companion notes that are not typed beats MUST NOT be required to load a type skill.
- **FR-019**: `wiki/templates/vehicle.md` and `wiki/templates/spell.md` MUST be the scaffolds for those campaign kinds, matching the templates provided for this feature.
- **FR-020**: Campaign `type` MUST include `vehicle` and `spell`. Layout MUST list jobs for Vehicle and Spell. Pass is those jobs.
- **FR-021**: A new or edited vehicle page MUST include a spoken look and a filled 5e vehicle sheet: size, type, speed, crew, and hull plus component AC/HP. Armed craft include weapons. Handling and combat are filled so the vehicle can enter play.
- **FR-022**: `vehicle-design` MUST teach filling that vehicle template, including the sheet and component numbers.
- **FR-023**: A job to write, edit, or create a spell page MUST use `spell-design` as its primary skill. The page MUST include a spoken look, a classification line, and a runnable 2024 effect block (casting time, range, components, duration, and the effect). Discovery and Lore are filled when the spell needs placement or history.
- **FR-024**: Skills updated for these kinds MUST state what to write and when the page is done. They MUST treat work that has not been done yet as the work to do now.
- **FR-025**: Claude Code MUST be used only for novel skill design, skill redesign, or a major skill-file change. Those dispatches MUST send a minimal, focused, direct prompt that names deliverables and completion criteria, at Opus 4.6 medium (`claude-opus-4-6`, `--effort medium`). Session agents MUST complete smaller edits to established files, Spec Kit pattern tweaks, and `AGENTS.md` without Claude Code.

### Key Entities

- **Composition skill**: The skill that loads when planning a session. It directs how to compose beats together as a Beat Chart. It does not write a typed beat's cards.
- **Type skill**: The skill for one beat type — Hook, Development, Cliffhanger, Climax, or Resolution. Primary when writing, editing, or creating content for a beat of that type.
- **Beat Chart**: The pacing palette: Hook, alternating Development/Cliffhanger pairs, Climax, Resolution.
- **Hook**: The session's one strong start. Completes when the party has committed to a response to the opening pressure.
- **Development**: A non-action beat that changes the decision space and sets direction until the next Development. Completes when players can name what they now know or can decide that they could not before.
- **Cliffhanger**: A contest whose outcome stays in doubt to the end. Changes the physical situation — position, resources, safety, time.
- **Climax**: The highest-stakes confrontation the middle made inevitable. Harvests threads the middle planted. Only Resolution may follow it.
- **Resolution**: The tag after the Climax. Shows what changed, what it cost, and what players can pursue next.
- **Card**: A proven shape under a type (Discovery, Chase, Clue, Final Battle, Happy Ending, and the rest in campaign use). Trigger, stakes, player options, agency note.
- **Named seam**: A job that may load a second skill. Listed in FR-008.
- **Session spine**: The session-level chart the DM opens for order and purpose. Not a cockpit.
- **Live beat**: One ~thirty-minute slice the DM runs. Format owned by the Session 11 cockpit standard.
- **Work**: Mutable prep. Not wiki until the DM accepts.
- **Vehicle page**: A named craft note. `type: vehicle`. Sheet, components, crew, handling, combat. Owner: `vehicle-design`.
- **Spell page**: A named spell note. `type: spell`. Narration, classification, runnable effect. Discovery and Lore when needed. Owner: `spell-design`.
- **spell-design**: The skill that is primary when writing, editing, or creating a spell page.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Two independent reviewers classify a set of at least 15 jobs covering plan-a-session plus write, edit, and create-content for each of the five types, and agree on the primary skill for 100% of those jobs.
- **SC-002**: In a session-planning job, an author produces a valid Beat Chart spine without opening any of the five type-card catalogs.
- **SC-003**: In a typed-beat write, edit, or create-content job with no named seam, 0% of the other four type-card catalogs are opened.
- **SC-004**: In a review of newly composed sessions after this feature is in force, 100% start with one Hook, end with one Climax then one Resolution, and contain no consecutive same-type middle beats.
- **SC-005**: In that same review, 100% of action Hooks are followed by a Development, 100% of cerebral Hooks are followed by a Cliffhanger, 100% of action Climaxes are preceded by a Development, and 100% of cerebral Climaxes are preceded by a Cliffhanger.
- **SC-006**: In a side-by-side Reading-view comparison, a second DM judges 100% of newly composed live beats as the same kind of card as a Session 11 beat of that type.
- **SC-007**: After this feature is in force, 0% of skills contain both the full Beat Chart and all five type-card catalogs.
- **SC-008**: After this feature is in force, 0% of existing Session 11 beats or spines are rewritten solely to prove the split.
- **SC-009**: In a walkthrough that plans a session then fills one Hook and one later typed beat, extra skills load only when a named seam fires; 0% extra type-card catalogs open otherwise.
- **SC-010**: In a review of newly composed beats, 100% offer at least two viable player responses, and 0% require a single prepared outcome to continue the session.
- **SC-011**: 100% of new vehicle pages started from `wiki/templates/vehicle.md` include narration plus a filled sheet (size, type, speed, crew) and hull/component figures a DM can run.
- **SC-012**: 100% of new spell pages started from `wiki/templates/spell.md` include narration, classification, and a runnable 2024 effect block.
- **SC-013**: After this feature, `vehicle-design` directs the author to fill the vehicle sheet and components as part of the page.
- **SC-014**: Two reviewers classify write, edit, and create-content jobs for a spell page and agree `spell-design` is primary for 100% of those jobs.
- **SC-015**: 100% of Claude Code skill dispatches that occur use Opus 4.6 at medium effort with a prompt that names deliverables plus a completion test. 0% of `AGENTS.md`-only edits or Spec Kit pattern tweaks are dispatched to Claude Code.

## Assumptions

- "Type of beat" means the five Beat Chart types (Hook, Development, Cliffhanger, Climax, Resolution), not one skill per subtype card. Cards stay inside their type skill.
- The current session-beats blob is split into the composition skill plus the five type skills. The blob is not kept beside the split.
- Method source is *Scripting the Game* (Pondsmith, with concepts from Flint Dille, R. Talsorian Games, 2020), as already adapted for this campaign: Beat Chart rules plus player-agency gates. Skills teach the methods; they do not paste the source text.
- Session 11 cockpit format, session-folder filing, Work accept-before-wiki, live-beat assembly, theatre of the mind, and encounter/trap/place/monster crafts stay as they are for beats. This feature also adds spell and vehicle wiki kinds: templates, Layout jobs, `vehicle-design` updated to fill the vehicle sheet, and a new `spell-design` skill so those pages are runnable. New skills and major skill redesigns dispatch to Claude Code (minimal prompt, Opus 4.6 medium). `AGENTS.md` tables, templates, and small tweaks to established files stay with the session agent.
- Creating content for a beat means filling that beat's jobs (situation, pressure, spoken opening, procedure, landing), then handing off to existing crafts when those crafts own the work, including vehicle and spell pages when a beat needs a named craft or spell.
- A cold open is not a Hook and is out of scope for the beat skills.
- Out of scope: rewriting Session 11 to prove the split; Foundry staging; a second pacing system beside the Beat Chart; one skill per beat-subtype card; changing who owns cockpit layout or spoken player text.
