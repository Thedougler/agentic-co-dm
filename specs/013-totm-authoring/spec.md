# Feature Specification: Theatre of the Mind Authoring

**Feature Branch**: `013-totm-authoring`

**Created**: 2026-09-12

**Status**: Draft

**Input**: User description: write complete, pre-session, player-facing Theatre of the Mind narration the DM can read or paraphrase at the table without an agent during play. Treat narration as session architecture, not decorative prose. Every block serves its Beat. Narrate the world, never the player. Keep blocks state-independent. Layer information. Combat uses relational space and clustered threats, not a hidden grid or turn-by-turn scripts. Wiki portraits are reusable first impressions, not scene scripts. Experts cited as sources: *Scripting the Game*, Sly Flourish, AbyssalBrews, The Nerdd.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - The DM speaks prepared look without an agent (Priority: P1)

The Co-DM authors player-facing theatre of the mind during prep. When the session starts, the DM is the only runtime. They open the prepared Work and can read or paraphrase the spoken look for that Beat without inventing the opening picture, without generating new prose at the table, and without an agent present.

**Why this priority**: The product exists because the Co-DM is absent during play. Incomplete spoken look is the failure this feature exists to stop.

**Independent Test**: Hand a prepared Beat to a second DM who was not the author. They can speak the opening picture from that Work alone and return the table to a decision. They do not need the author or an agent to finish the spoken look.

**Acceptance Scenarios**:

1. **Given** a prepared Beat that needs spoken look, **When** the DM opens that Work at the table, **Then** a complete player-facing narration block is already there for the opening picture.
2. **Given** that block, **When** it is read or paraphrased, **Then** the table has a stable shared picture and something live to respond to, without the DM inventing the opening.
3. **Given** a piece of spoken look that can only be written after players act, **When** the Work is reviewed, **Then** that piece is omitted rather than guessed. Turn-by-turn combat summaries and other runtime-dependent lines are not prewritten.

---

### User Story 2 - Narration never scripts the players (Priority: P1)

Player-facing theatre of the mind describes the world: what is present, what is happening independently of the party, what can be perceived, spatial relationships, obvious dangers, environmental opportunities, NPC behavior, sensory information, and consequences that have already occurred. It does not prescribe what a PC does, where they move, what they think or feel, what they notice beyond perception, what they intend, what the party chooses, whether they succeed, or the outcome of an unresolved action.

**Why this priority**: Scripted players are a railroad in the mouth. If this fails, later stories still decide play.

**Independent Test**: Give a second person only the player-facing block. They cannot point to a line that assigns a PC action, thought, emotion, intent, success, or unresolved outcome. They can still picture the situation.

**Acceptance Scenarios**:

1. **Given** a player-facing narration block, **When** it is reviewed, **Then** it describes the world and does not assign PC action, thought, emotion, intent, choice, success, or an unresolved outcome.
2. **Given** an involuntary reaction, **When** it is written, **Then** it is expressed through the environment (the room reeks) rather than assigned to a character (your stomach turns).
3. **Given** DM procedure or hidden truth on the same page, **When** the player-facing passage is written, **Then** that procedure and hidden truth stay out of the spoken look.

---

### User Story 3 - Every block serves its Beat (Priority: P2)

Before spoken look is treated as done, it has a Beat type and a job. The block makes that job easier: Hook involves quickly; Development changes what the table knows or can decide; Cliffhanger makes danger or instability immediate; Climax makes central opposition, stakes, and meaningful features unmistakable; Resolution shows visible consequences without deciding player-controlled outcomes. Decorative atmosphere that could be deleted without making the Beat harder is incomplete.

**Why this priority**: Session architecture is the reason the mouth surface exists in prep. Pretty prose that does no Beat work wastes the DM's read-aloud.

**Independent Test**: Cover the Beat label. A second person names the job the block performs, or correctly rejects it as decorative. Deleting the block would make that Beat harder to run.

**Acceptance Scenarios**:

1. **Given** a prepared scene's spoken look, **When** it is reviewed, **Then** it has a Beat type (Hook, Development, Cliffhanger, Climax, or Resolution) and a one-sentence job, and the block performs that job.
2. **Given** a block that can be deleted without making the Beat harder, **When** it is reviewed, **Then** it is incomplete.
3. **Given** a Development, **When** it is spoken, **Then** the changed information is unmistakable, not buried under atmosphere.
4. **Given** a Cliffhanger or Climax, **When** it is spoken, **Then** danger, opposition, or pressure is front-loaded; exposition is secondary.
5. **Given** a Resolution whose Climax can end in substantially different established outcomes, **When** it is prepared, **Then** it includes conditional variants rather than one canonical result. It states only outcomes that play can actually establish.

---

### User Story 4 - The situation is scripted; the response is not (Priority: P2)

A narration block remains usable regardless of party formation, individual position, hit points or resources, weapons drawn, who speaks first, who investigates, which approach the players intend, party mood, or character-specific reactions — unless the Beat itself guarantees a resulting world state. Information is layered: the opening block is the immediate frame; salient features and discoverable information wait as complete reveal blocks that describe the discovery, not the method. The scene exposes things players can interact with before they would need to know those things exist. It does not write around an expected solution.

**Why this priority**: Prep that assumes a rush across the bridge, a kneeling rogue, or one planned approach breaks the first time the table does something else.

**Independent Test**: Rewrite the party's approach (sneak, talk, wait, split, refuse). The same opening block and reveal blocks still work. A second person can name at least one actionable feature and one relationship among important elements.

**Acceptance Scenarios**:

1. **Given** a narration block, **When** the party approaches differently than the author expected, **Then** the block remains usable without rewrite.
2. **Given** an opening block, **When** it is spoken, **Then** it is the immediate frame only — obvious without deliberate investigation — and deeper information is not dumped into it.
3. **Given** a salient or hidden feature, **When** players ask, scan, or investigate, **Then** a complete reveal block describes what is found, not who found it or how.
4. **Given** a feature that matters tactically or interactively, **When** the opening is spoken, **Then** that feature is already in the fiction before a player would need it.
5. **Given** the last sentence of an opening block, **When** it is spoken, **Then** it leaves a live situation (danger, contradiction, unanswered question, opportunity, NPC demand, objective, or changing circumstance) and does not choose the party's response.

---

### User Story 5 - Combat look preserves decisions without a grid (Priority: P3)

When violence is imminent, clarity outranks literary flourish. The combat opening makes immediate threats, threat relationships, important objectives, relative distance, major terrain, cover, hazards, interactable opportunities, routes, and any obvious exceptional condition understandable. Distance is relational (Melee, Near, Far) unless a rule or encounter truly needs a measurement. Enemy grouping is legible enough that the DM can answer how many a reasonable area effect would catch. Combat prep includes that opening, concise DM-only tactical facts, optional world-triggered escalation blocks, and reveal blocks for transformations and newly visible facts. It does not prewrite turn-by-turn narration or top-of-round summaries.

**Why this priority**: A hidden grid in prose, or a scripted fight, either freezes the table or railroads it. Combat is where runtime state most tempts incomplete prep.

**Independent Test**: Give a second DM only the combat opening and tactical facts. They can name threats, who is near what, cover, hazards, the objective, and a reasonable cluster for an area effect, then start the fight. They are not handed a turn script.

**Acceptance Scenarios**:

1. **Given** a combat opening, **When** it is spoken, **Then** threats, relationships, objectives, relative distance, terrain, cover, hazards, opportunities, and routes are understandable without a floor plan.
2. **Given** that opening, **When** distance matters to a decision, **Then** it uses relational bands (Melee, Near, Far), not coordinates disguised as prose. Exact distance appears only when a rule or encounter requires it.
3. **Given** clustered or dispersed opposition, **When** a player asks how many an area effect can reasonably catch, **Then** grouping in the fiction is enough for a generous, consistent answer.
4. **Given** combat Work, **When** it is reviewed, **Then** it has a complete opening and DM-only tactical facts, and it does not include turn-by-turn or top-of-round scripts.
5. **Given** a world-triggered change (ritual phase, collapsing structure, visible reinforcements), **When** that trigger fires, **Then** a complete escalation or reveal block is already prepared and does not assume PC behavior.

---

### User Story 6 - Wiki portraits stay first impressions, not scenes (Priority: P3)

A wiki portrait of a location, person, creature, ship, artifact, faction, landmark, or region is a reusable first-impression model. It remains valid across sessions. It does not reference current party state, assume an encounter, or include unlabeled transient facts. After one reading, a DM can recognize the subject at the table and reuse the language later in situated narration.

**Why this priority**: Owner pages outlive tonight. A portrait that stages a fight or plants the party is unusable next session.

**Independent Test**: Read a wiki portrait with no session context. A second person can picture and distinguish the subject, and the block still works if no encounter occurs.

**Acceptance Scenarios**:

1. **Given** a wiki portrait, **When** it is reviewed with no party or encounter supplied, **Then** it remains valid and does not invent a scene.
2. **Given** that portrait, **When** it is reused in a later session, **Then** it still identifies the subject without rewrite for last session's positions or mood.
3. **Given** transient facts, **When** they appear, **Then** they are clearly labeled as transient or they are omitted.

---

### User Story 7 - Interactive problems are solvable from the fiction (Priority: P4)

Hazards, traps, trials, and similar interactive problems expose enough in the spoken fiction for meaningful interaction. A challenge whose only solution depends on information omitted from the current or earlier fiction is incomplete. Betrayal and sabotage remain opportunities to detect, prevent, or respond; they are not predetermined outcomes.

**Why this priority**: A silent trap is not a Beat; it is a gotcha. Prep must make solving possible without solving it for the players.

**Independent Test**: Give a second DM the visible symptom and any earlier clue. They can name at least one approach that could work. The spoken look does not announce the solution.

**Acceptance Scenarios**:

1. **Given** a trap, hazard, or trial, **When** the opening fiction is spoken, **Then** a visible symptom or usable clue is present in this scene or an earlier one.
2. **Given** that challenge, **When** it is reviewed, **Then** it is not solvable only by information the players were never given.
3. **Given** betrayal or sabotage, **When** it is prepared, **Then** players have a chance to detect, prevent, or respond before it is irreversible.

---

### Edge Cases

- A mixed wiki page (DM-facing bands plus spoken look): theatre of the mind owns only the player-facing passages. Hidden information stays out of those passages.
- A wiki portrait and a Beat opening for the same place: the portrait stays reusable; the Beat opening is the situated frame. One does not replace the other.
- Combat that never starts: the combat opening is unused; it must not have already assigned PC actions as if the fight began.
- Runtime combat: the DM restates threats, engagement, conditions, and objectives from current fiction. Those restatements are not prewritten.
- A Beat that guarantees a world state (the bridge has already fallen): narration may depend on that guaranteed state. It still must not depend on how the party caused it unless play already established that.
- Resolution when the Climax ends in one established way: a single consequence block is enough. Variants are required only when substantially different endings are in play.
- Noncombat exploration, social space, travel, and discovery: unknown space is useful; hidden causes stay hidden; evidence may appear without the answer.
- Exact distances and compass on a beat card's DM-facing zones or rulings: allowed when those facts help the DM scan. They do not belong in player-facing theatre of the mind unless the fiction itself makes them perceptible and decision-constraining.
- Session 11 beat-card layout remains the cockpit. This feature does not invent a second page template for the same Beat.
- Stock published boxed text used unchanged is out of scope unless the Co-DM rewrites it as Work.
- Legacy wiki pages are not rewritten solely to prove this standard.
- Missing wiki facts: invention is Work, flagged, not silent canon. Spoken look still must not leak secrets, difficulty classes, or unearned names.
- Players creating plausible environmental details that fit the established fiction: the DM may accept them. Prep is not a closed inventory.
- A recap, hit line, or one-turn spoken update: still theatre of the mind and still must not script the players. Completeness means complete for that surface, not a full scene opening.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Player-facing theatre of the mind for a prepared Beat MUST be complete before the session so the DM can read or paraphrase it without an agent and without inventing the opening picture.
- **FR-002**: Spoken look that depends on runtime player decisions (including turn-by-turn combat and top-of-round battlefield summaries) MUST NOT be prewritten.
- **FR-003**: Player-facing narration MUST describe the world. It MUST NOT prescribe PC action, movement, thought, emotion, notice beyond what perception justifies, intent, party choice, success, or the outcome of an unresolved action.
- **FR-004**: Involuntary or emotional reactions MUST be expressed through the environment when they appear, not assigned to a PC.
- **FR-005**: Secrets, difficulty classes, unearned names, hidden causes, and agent-process language MUST stay out of player-facing narration.
- **FR-006**: Every prepared scene's spoken look MUST name a Beat type (Hook, Development, Cliffhanger, Climax, or Resolution) and a job, and MUST perform that job. Decorative prose that can be removed without making the Beat harder MUST be treated as incomplete.
- **FR-007**: A Hook MUST establish immediate interest, disturbance, mystery, threat, or opportunity with minimal orientation before the point of interest.
- **FR-008**: A Development MUST make the changed information unmistakable.
- **FR-009**: A Cliffhanger MUST front-load immediate unstable danger, confrontation, chase, obstacle, or pressure.
- **FR-010**: A Climax MUST make central opposition, immediate stakes, changing environment, objective, major tactical features, and consequences already in motion unmistakable. It MUST NOT narrate victory, defeat, sacrifice, surrender, escape, or any other player-controlled outcome.
- **FR-011**: A Resolution MUST show what remains, what has changed, what has become possible, and what consequences are now visible. It MUST state only outcomes established through play. When the preceding Climax can end in substantially different ways, the prepared Resolution MUST include conditional variants.
- **FR-012**: Narration blocks MUST remain usable regardless of party formation, position, resources, drawn weapons, speaking order, investigation order, intended approach, mood, or character-specific reactions, unless the Beat guarantees the resulting world state.
- **FR-013**: Opening narration MUST be the immediate frame only. Salient features and discoverable information MUST be prepared as separate complete reveal blocks that describe the discovery, not the discoverer or method.
- **FR-014**: Features that matter tactically or interactively MUST be present in the fiction before a player would need to know they exist.
- **FR-015**: An opening block MUST end on a live situation and MUST NOT choose the party's response.
- **FR-016**: Important elements MUST be related to one another clearly enough that a second person can form a mental model (beneath, beyond, between, blocking, and equivalent relationships). Isolated inventories without relationships MUST be treated as incomplete.
- **FR-017**: The most important perceptible thing MUST be presented first. Architectural inventory MUST NOT lead.
- **FR-018**: Sensory information MUST be selective. One or two details that define the scene suffice. Cycling every sense MUST NOT be required.
- **FR-019**: When violence is imminent, combat opening narration MUST make threats, threat relationships, objectives, relative distance, major terrain, cover, hazards, interactable opportunities, routes, and obvious exceptional conditions understandable. Clarity MUST outrank literary flourish.
- **FR-020**: Player-facing distance MUST default to relational bands (Melee, Near, Far). Exact measurements MUST appear only when a rule or encounter requires them. Coordinates disguised as prose MUST be treated as incomplete.
- **FR-021**: Enemy grouping MUST be legible enough for the DM to answer how many a reasonable area effect can catch, using generous consistent adjudication.
- **FR-022**: Combat Work MUST include a complete combat opening and concise DM-only tactical facts (groups, starting relationships, features, cover, hazards, exits, elevations, clusters, objectives). It MUST NOT include a turn-by-turn script.
- **FR-023**: World-triggered combat or scene changes MUST have complete escalation or reveal blocks that do not assume PC behavior.
- **FR-024**: A wiki portrait MUST remain valid across sessions, MUST NOT reference current party state, MUST NOT assume an encounter, and MUST NOT include unlabeled transient facts. It MUST prioritize a few identity anchors over exhaustive detail.
- **FR-025**: Hazards, traps, and trials MUST expose a visible symptom or usable clue in the current or earlier fiction so a solution is available in play. A challenge solvable only by omitted information MUST be treated as incomplete.
- **FR-026**: Betrayal and sabotage MUST remain detectable, preventable, or respondable opportunities. They MUST NOT be written as predetermined outcomes with no chance to notice.
- **FR-027**: Reasonable player-created details that fit the established fiction MUST be permitted. Prep MUST NOT be treated as a closed inventory of the only legal facts.
- **FR-028**: Theatre of the mind remains the prose authority for text that crosses the DM/player boundary. This feature MUST NOT reassign writing or visual authority, replace Session 11 beat-card layout, or restock canon.
- **FR-029**: Existing Work rules still bind: chat proposal first; wiki write after DM accept, except named ingest stubs. Players see nothing until the DM accepts and presents.
- **FR-030**: The Co-DM MUST apply this standard to new player-facing theatre of the mind Work. Legacy wiki pages MUST NOT be rewritten solely to satisfy this feature.
- **FR-031**: Guidance that implements this feature MUST constrain testable outcomes. It MUST NOT prescribe a single sentence architecture, voice, or page template when more than one approach hits those outcomes. Expert techniques MAY be cited as sources or examples.
- **FR-032**: A prepared scene MUST give the DM, in some form: the Beat and job; complete player-facing narration; fixed scene truths that do not depend on player behavior; actionable features; spatial relationships that matter; reveal blocks when layering applies; and DM-only notes for hidden information and adjudication. Sections that add no value MAY be omitted. Hidden information MUST NOT sit inside player-facing narration.
- **FR-033**: How those facts appear on a Session 11 beat card remains that card's layout. This feature MUST NOT require a second competing cockpit for the same Beat.

### Key Entities

- **Theatre of the mind**: Spoken, sensory language the DM can read aloud. The mouth surface. Players hear and see only what the DM presents.
- **Narration block**: One complete player-facing spoken picture for a surface (scene opening, reveal, combat opening, wiki portrait, escalation).
- **Beat**: One live slice of session architecture: Hook, Development, Cliffhanger, Climax, or Resolution. Session chart ownership stays with existing Beat craft. This feature owns the spoken look that serves that Beat.
- **Beat job**: The one thing that spoken look must accomplish for that Beat type.
- **Immediate frame**: What is obvious without deliberate investigation. Layer 1. The primary opening block.
- **Reveal block**: Complete optional player-facing narration for a salient feature or a discovery. Describes the finding, not the method.
- **Wiki portrait**: Reusable first-impression model of an owner (place, person, creature, ship, artifact, faction, landmark, region). Not a scene script.
- **Combat opening**: Initial battlefield frame spoken when violence is imminent.
- **Tactical reference**: DM-only concise facts for starting combat (groups, bands, cover, hazards, exits, clusters, objectives).
- **Escalation block**: Complete narration for a world-triggered change. Does not assume PC behavior.
- **Fixed scene truth**: A fact the DM can rely on regardless of player behavior.
- **Relational distance**: Melee (immediately interactable), Near (reachable with normal movement this turn), Far (not meaningfully interactable in melee this turn without extra movement). Very Far only when genuinely useful.
- **Work**: Mutable prep the DM may accept, edit, or reject.
- **Session**: Table time with only humans present. The DM is the sole runtime.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A DM who knows the campaign can open a newly prepared Beat and speak its opening picture from the Work alone, then return the table to a decision, in one read-through without asking the author or an agent to finish the prose.
- **SC-002**: In a read-aloud test of new player-facing blocks, 100% can be presented to players without a secret, difficulty class, unearned name, agent-process note, or a line that assigns PC action, thought, emotion, intent, choice, success, or an unresolved outcome.
- **SC-003**: Two independent reviewers score a set of at least 12 prepared scenes covering Hook, Development, Cliffhanger, Climax, Resolution, combat opening, wiki portrait, and a trap or hazard, and agree on pass/fail against this standard for 100% of those scenes.
- **SC-004**: In that set, 100% of opening blocks still work if the party's approach is rewritten (sneak, talk, wait, refuse, or split) unless the Beat guarantees the world state.
- **SC-005**: Covering the Beat label, a second person can name the job of 100% of non-portrait scene openings, or correctly reject a block as decorative.
- **SC-006**: In a review of new combat Work, 100% have a complete opening plus DM-only tactical facts; 0% include turn-by-turn or top-of-round scripts; 100% make grouping legible enough to answer a reasonable area-effect question.
- **SC-007**: In a review of new wiki portraits, 100% remain valid with no party and no encounter; 0% assume an encounter or unlabeled transient party state.
- **SC-008**: In a review of new traps, hazards, or trials, 100% expose a visible symptom or usable clue in the current or earlier fiction; 0% are solvable only by omitted information.
- **SC-009**: After this standard is in force, 0% of legacy wiki pages are rewritten solely to match it.
- **SC-010**: In a side-by-side of a new live Beat against a Session 11 beat card, a second DM still judges them the same kind of cockpit; this standard has not replaced that layout with a second template.

## Assumptions

- Primary human reader of Co-DM output is the DM. Players hear theatre of the mind and see play-surface artifacts the DM presents.
- The DM is the only runtime during a session. Completeness means the spoken look the table needs at the start of a Beat (and prepared reveals/escalations) exists before play. It does not mean predicting every player line.
- Theatre of the mind is already the prose authority for text that crosses the DM/player boundary (audience writing). This feature specifies what that authority must accomplish as session architecture.
- Beat types and session chart remain owned by existing Beat craft. This feature does not re-pace the night or replace the Session 11 cockpit.
- Expert sources (*Scripting the Game*; Sly Flourish's situation → intent → adjudication and prominent features; AbyssalBrews's exploration-versus-combat communication and relational descriptors; The Nerdd's environment, relative distance, hiding, and focus) are sources for outcomes, not the only valid method.
- Relational Melee / Near / Far is the player-facing default. DM-facing zones and rulings on a beat card MAY keep exact distances or compass when those help the DM scan.
- "Very Far" is optional. Prefer three bands.
- In a normal-sized combat area, combatants are generally reachable and ranged targets generally in range unless the encounter establishes otherwise.
- Area-effect baselines (tiny ~1–2, small ~2, large ~4, huge potentially everyone, short line ~2, long line ~3, adjusted for cluster or terrain) are adjudication aids, not geometry the players must reverse-engineer.
- Length follows the job: the shortest block that creates a stable shared picture and performs the Beat. Authoring targets (wiki portrait roughly a short paragraph; scene opening and combat opening a bit longer; reveals shorter; a major Climax frame longest) are guidance, not pass/fail word counts.
- How an author hits hierarchy, relationships, sensory anchors, actionable features, and a live ending is judgment. Another structure that presents the important thing first, relates what matters, exposes usable features, and ends on a live situation is valid.
- Recaps, hit lines, and short updates remain theatre of the mind but are not scored as full scene openings.
- Existing Work rules, vault format, copy-writer on DM-facing bands, and visual authorities still apply.
- Out of scope: live agent at the table; replacing Session 11 beat-card layout; replacing audience-writing routing; Foundry play-surface staging; rewriting legacy pages to prove the standard; requiring a single sentence architecture or a second cockpit template; prewriting runtime combat summaries; pasting proprietary published boxed text.
