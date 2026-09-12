# Feature Specification: Expert-Grounded D&D Content Guidance

**Feature Branch**: `011-narrative-mechanics`

**Created**: 2026-09-12

**Status**: Draft

**Input**: User description: when creating D&D content, use as default the philosophy that game mechanics should directly serve and drive the narrative forward. Monster stat blocks and tactical rules are not math detached from the story. Combat features should tell lore, origin, or emotional stakes. A creature's mechanics should intertwine with its lair and terrain so the place of the fight creates dramatic pressure. Homebrew mechanical changes should physically manifest a plot point or character beat, not only make the encounter harder. Later: this is one example of standing on experts' shoulders; when solving a problem in agentic instructions, skills, or procedures that create D&D wiki content, first research how experts have solved it, then integrate that into the guidance.

## Clarifications

### Session 2026-09-12

- Q: Should this feature be the combat-mechanics default only, or the general “research experts, then integrate” default for D&D content skills? → A: Expand 011: when authoring or changing skills/procedures that create D&D wiki content, research expert solutions first, then integrate them. Mercer combat is the first instance.
- Q: When research finds an expert technique, should the skill require that technique as the only way to work, or require the outcome the technique achieves? → A: Require the outcome. Expert techniques are sources and examples, not the only valid method.
- Q: Which sources count as experts when that research runs? → A: Prefer named published designers and documented craft; other sources, including high-quality homebrew, only if official sources are silent. Never paste proprietary book text.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Research experts before changing D&D content guidance (Priority: P1)

The Co-DM (or an agent following standing instructions) is about to create or change a skill, standing instruction, or procedure that tells later runs how to make D&D content for the wiki. Before that guidance is treated as done, the author researches how experts have already solved that problem, then folds the **outcomes** those experts achieved into the guidance so it is one harmonious source. Expert techniques are sources and examples, not the only valid method. Vacuum-invented guidance that ignores prior expert solutions is incomplete. Ordinary wiki content jobs follow the resulting guidance; they do not re-run that research unless the guidance itself is being created or changed.

**Why this priority**: The combat default below is one instance. Without this loop, every later D&D content skill is invented in a vacuum.

**Independent Test**: Give an author a job to create or change a D&D content skill. A second reviewer can point to expert-solved outcomes in the guidance, or correctly reject it as vacuum-invented.

**Acceptance Scenarios**:

1. **Given** a job to create or change a skill, standing instruction, or procedure that creates D&D wiki content, **When** the author finishes, **Then** the guidance reflects researched expert solutions to that problem, integrated as one source.
2. **Given** guidance invented without research when experts have already solved the problem, **When** it is reviewed, **Then** it is incomplete.
3. **Given** an ordinary wiki content job that follows existing guidance, **When** it is reviewed, **Then** a fresh expert-research pass is not required.
4. **Given** guidance that requires a named person's process as the only valid method, **When** it is reviewed, **Then** it is incomplete. Another method that hits the same expert-solved outcome is valid.

---

### User Story 2 - New combat Work serves the story by default (Priority: P2)

The Co-DM is about to author or customize combat Work — a combatant, an encounter, a lair, or a mechanical homebrew change. This is the first instance of User Story 1 applied to combat craft: expert outcome is that mechanics drive narrative. Before that Work is treated as done, the mechanics are checked as a vehicle for the story. A second person can name the narrative beat those mechanics serve (lore, origin, stakes, plot, or character). Math that does not serve a named beat is incomplete.

**Why this priority**: Detached math is the named failure of the first instance. Later combat stories prove each branch.

**Independent Test**: Give an author a new combat Work job. A second reviewer, without seeing the first list, names the narrative beat the mechanics serve, or correctly rejects the Work as math detached from the story.

**Acceptance Scenarios**:

1. **Given** a job that authors or customizes combat mechanics, **When** the Co-DM finishes the Work, **Then** a second person can name the narrative beat those mechanics serve.
2. **Given** combat mechanics that only change numbers and do not serve lore, origin, stakes, plot, or character, **When** the Work is reviewed, **Then** it is incomplete.
3. **Given** a job that does not author or customize combat mechanics and does not create or change D&D content guidance, **When** it is reviewed, **Then** the combat instance of this default is not treated as required.

---

### User Story 3 - Combat features tell who the creature is (Priority: P3)

When the Co-DM adds or rewrites a custom ability, phase shift, or legendary action, that feature tells the DM something about the creature's lore, origin, or emotional stakes. Combat is not an interruption that could be swapped for any other fight without changing the story.

**Why this priority**: Features are the most common place math detaches from story. If they speak, the first instance is visible at the table.

**Independent Test**: Give an author a custom combat feature. A second person can state what it says about lore, origin, or stakes without being told. A feature that only adds damage or hit points fails.

**Acceptance Scenarios**:

1. **Given** a custom combat feature, **When** it is reviewed, **Then** a second person can state the lore, origin, or stakes it communicates.
2. **Given** that feature, **When** it is removed on paper, **Then** the fight would lose a story tell, not only a number.
3. **Given** stock published opposition used unchanged, **When** the job is to drop that opposition in as-is, **Then** custom features are not required.

---

### User Story 4 - The place of the fight acts (Priority: P4)

When an encounter has a named place — a lair, site, or battlefield — that place has at least one mechanical pressure tied to it (hazard, terrain, structural change, or similar). Flavor-only scenery that never changes a choice fails. The pressure creates dramatic tension by forcing a strategic adjustment.

**Why this priority**: A fight in a blank room wastes the place. Mechanical place is how the story of the site shows up in play.

**Independent Test**: Give an author an encounter with a named place. A second person can name one mechanical pressure that belongs to that place and would change what the party does.

**Acceptance Scenarios**:

1. **Given** an encounter with a named place, **When** the Work is finished, **Then** that place includes at least one mechanical pressure that changes strategy.
2. **Given** scenery that is only described and never acts, **When** the Work is reviewed, **Then** the place of the fight is incomplete.
3. **Given** a fight the DM asked to keep as a featureless skirmish, or a job with no named place, **When** it is reviewed, **Then** invented lair mechanics are not required.

---

### User Story 5 - Homebrew changes manifest a plot beat (Priority: P5)

When the Co-DM heavily modifies a creature or its rules, each substantial mechanical change names the plot point or character beat it physically manifests — a corruption, a curse, a backstory tell, a faction's method. A change whose only reason is "harder" is incomplete.

**Why this priority**: Homebrew is where detached difficulty hides. The default is that the change *is* the story, not a wrapper around it.

**Independent Test**: Give an author a substantial homebrew modification. A second person can name the plot or character beat it manifests. A difficulty-only rewrite with no named beat fails.

**Acceptance Scenarios**:

1. **Given** a substantial homebrew mechanical change, **When** it is reviewed, **Then** it names the plot or character beat it manifests.
2. **Given** a modification whose only stated reason is increased difficulty, **When** it is reviewed, **Then** it is incomplete.
3. **Given** a light reskin that does not change how the creature acts, **When** it is reviewed, **Then** a tectonic plot-shift is not required.

---

### Edge Cases

- Research-and-integrate applies when creating or changing skills, standing instructions, or procedures that create D&D wiki content. It does not apply to every ordinary wiki page write.
- Contributor docs, issue-tracker chrome, and agent-consumed docs that do not create D&D wiki content are outside the research default.
- Stock published opposition used unchanged does not need custom features, phases, or legendary actions.
- The DM may override the combat instance by asking for a stock or featureless fight. That override is explicit Work, not silence.
- Social, exploration, or recap Work with no combat mechanics is outside the combat instance. It is not outside the research default if the job is to create or change guidance for those kinds.
- A minion group may share one mechanical tell. Every minion does not need a unique legendary action.
- A road or hallway with no named lair does not require invented lair mechanics unless the job names that place as the fight's site.
- Spoken look stays theatre of the mind. Secrets, difficulty classes, and unearned names stay out of player-facing passages. Narrative-serving mechanics live in DM-facing Work.
- Missing wiki lore: flag invention and still name the beat the mechanic serves. Do not invent silent canon.
- Runnable math still binds. Narrative-service does not excuse illegal notation, hidden arithmetic, or unplayable features.
- Craft owners of facts, math, and procedure remain owners. This default does not restock canon or invent a new craft owner.
- Official sources silent: high-quality homebrew may fill the gap. Random or unvetted web pages do not. Proprietary published book text is never pasted.
- No expert source found at all: invent and flag per existing Work rules. Do not pretend a giant spoke.
- Legacy wiki pages are not rewritten solely to prove this default.
- Theatre of the mind, copy-writer, and vault format still apply to their jobs. This feature does not reassign writing or visual authority.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: When creating or changing a skill, standing instruction, or procedure that creates D&D wiki content, the author MUST research how experts have already solved that problem before the guidance is treated as done. Prefer named published designers and documented craft. Other sources, including high-quality homebrew, MAY be used only if official sources are silent. Proprietary book text MUST NOT be pasted.
- **FR-002**: Expert findings MUST be integrated as testable outcomes in one harmonious source. A bolted-on quote dump, a second competing procedure, or a named person's process required as the only valid method MUST be treated as incomplete.
- **FR-003**: Ordinary wiki content jobs MUST follow the resulting guidance. They MUST NOT be required to re-run expert research unless the guidance itself is being created or changed.
- **FR-004**: Vacuum-invented D&D content guidance that ignores prior expert solutions to the same problem MUST be treated as incomplete.
- **FR-005**: Every new Co-DM job that authors or customizes combat mechanics MUST be checkable against a named narrative beat (lore, origin, stakes, plot, or character) before the Work is treated as done. This is the first instance of FR-001 applied to combat craft.
- **FR-006**: Custom combat features (abilities, phase shifts, legendary actions, and equivalent tells) MUST communicate lore, origin, or emotional stakes a second person can state.
- **FR-007**: Combat mechanics that only change numbers and do not serve a named narrative beat MUST be treated as incomplete.
- **FR-008**: When an encounter has a named place, that place MUST include at least one mechanical pressure that changes player strategy.
- **FR-009**: Flavor-only scenery that never acts MUST NOT count as a complete place of the fight.
- **FR-010**: A substantial homebrew mechanical change MUST name the plot or character beat it manifests.
- **FR-011**: A homebrew change whose only reason is increased difficulty MUST be treated as incomplete.
- **FR-012**: Stock published opposition used unchanged MUST NOT be required to receive custom features.
- **FR-013**: An explicit DM request for a stock or featureless fight MUST override the combat instance for that job.
- **FR-014**: Jobs that do not author or customize combat mechanics MUST NOT be required to satisfy the combat instance. They remain subject to FR-001 when the job is to create or change D&D content guidance.
- **FR-015**: Craft owners of facts, math, and procedure remain owners of those jobs. This default MUST NOT reassign fact ownership or replace runnable D&D math.
- **FR-016**: The Co-DM MUST apply the combat instance to new combat Work. Legacy wiki pages MUST NOT be rewritten solely to satisfy this feature.
- **FR-017**: Player-facing spoken text MUST remain theatre of the mind. Narrative-serving mechanics MUST NOT leak secrets, difficulty classes, or unearned names into spoken look.
- **FR-018**: Existing Work rules still bind: chat proposal first; wiki write after DM accept, except named ingest stubs.
- **FR-019**: D&D content guidance MUST NOT prescribe a single creative method, voice, camera, or structure when more than one approach hits the expert-solved outcome. Expert techniques MAY be cited as sources or examples.

### Key Entities

- **D&D content guidance**: A skill, standing instruction, or procedure that tells later runs how to make D&D content for the wiki.
- **Expert research**: Looking up how practitioners have already solved the same content problem, done when guidance is created or changed. Named published designers and documented craft first; high-quality homebrew only if those are silent.
- **Integrated guidance**: One harmonious source that absorbs expert-solved outcomes. Techniques may be cited as sources. Not a quote dump, not a second competing procedure, and not a single person's process as the only valid method.
- **Combat Work**: New Co-DM prep that authors or customizes a combatant, encounter, lair, or mechanical homebrew change. First instance of this feature.
- **Narrative beat**: The story the mechanic serves — lore, origin, emotional stakes, plot point, or character beat. A second person can name it.
- **Custom combat feature**: An ability, phase shift, legendary action, or equivalent tell the Co-DM added or rewrote.
- **Named place**: The lair, site, or battlefield the encounter is in, when the job names one.
- **Mechanical pressure**: A hazard, terrain effect, structural change, or similar rule belonging to that place that changes a choice.
- **Substantial homebrew change**: A mechanical rewrite that changes how the creature acts, not a light reskin.
- **Stock opposition**: Published creature or encounter used unchanged.
- **Override**: Explicit DM request that this combat job stay stock or featureless.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: In a review of new or changed D&D content guidance after this default is in force, 100% show expert-solved outcomes integrated as one source; 0% are vacuum-invented when experts have already solved the same problem; 0% require a named person's process as the only valid method.
- **SC-002**: In a review of ordinary wiki content jobs that were not creating or changing guidance, 0% are failed for skipping a fresh expert-research pass.
- **SC-003**: Two independent reviewers classify a set of at least 12 combat Work jobs (custom features, named-place encounters, homebrew changes, stock opposition, and an explicit override) and agree on pass/fail against the combat instance for 100% of those jobs.
- **SC-004**: In a review of new custom combat features after this default is in force, 100% communicate lore, origin, or stakes a second person can state; 0% are number-only changes with no named beat.
- **SC-005**: In a review of new encounters that have a named place, 100% include at least one mechanical pressure that belongs to that place and would change strategy.
- **SC-006**: In a review of new substantial homebrew mechanical changes, 100% name the plot or character beat they manifest; 0% are difficulty-only.
- **SC-007**: In a review of stock published opposition used unchanged, 0% are failed for lacking custom features.
- **SC-008**: After this default is in force, 0% of legacy wiki pages are rewritten solely to match it.
- **SC-009**: In a read-aloud test of new player-facing passages on pages that include these mechanics, 100% can be presented without a secret, difficulty class, or unearned name leaking from the mechanics.

## Assumptions

- "Creating D&D content" means wiki Work the DM will use at the table. "D&D content guidance" means the skills, standing instructions, and procedures that tell agents how to make that Work.
- Expert research fires when that guidance is created or changed. It does not fire on every ordinary wiki write.
- The combat stories are the first instance: mechanics drive narrative. Later content kinds reuse User Story 1; they do not all need their own instance in this feature.
- The primary human reader of wiki Work is the DM. Players hear and see only what the DM presents.
- A second person naming the narrative beat (combat instance) or pointing to expert-solved outcomes (guidance) is the test. How an author hits that outcome is judgment. This spec does not prescribe a voice, camera, structure, or a single creative method.
- Light reskins that do not change how a creature acts are not substantial homebrew changes.
- A minion group's shared tell counts as the group's combat feature.
- Runnable D&D math and existing monster/encounter craft remain in force. This default stacks with them; it does not replace them.
- Existing writing and visual authorities still apply (agent, DM, players, vault, visual-references, visual-aids).
- Out of scope: rewriting legacy wiki pages to prove the default; Foundry play-surface staging; requiring legendary actions on every creature; inventing a new craft owner; researching experts on every ordinary wiki write; requiring a named person's techniques as the only valid method; pasting proprietary book text.
