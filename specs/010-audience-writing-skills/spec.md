# Feature Specification: Audience Writing and Visual Skills

**Feature Branch**: `010-audience-writing-skills`

**Created**: 2026-09-12

**Status**: Draft

**Input**: User description: "writing-for-agents is utilized for everything agents will read, copy-writer is used for anything humans will read, theatre-of-the-mind is used for anything the players will read, and obsidian-markdown is used for anything in the obsidian vault" plus later direction: visual-references is used for working with visual references; visual-aids is used for producing them.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - The job decides the writing or visual authority (Priority: P1)

The Co-DM is about to write or to work with pictures. The job is classified before any draft or picture is made.

Writing classifiers — who will read the text, and whether it is a wiki vault note:

- An agent will follow it → **writing-for-agents**
- The DM will read it → **copy-writer**
- Players will hear or see it → **theatre of the mind**
- It is a wiki vault note → **obsidian-markdown**

Visual classifiers — what the picture work is:

- Working with visual references (gathering, inspecting, and using existing look so a depiction stays that owner) → **visual-references**
- Producing a visual aid (attaching, grounding, generating, promoting, or placing a picture for an owner or a named moment) → **visual-aids**

More than one classifier can be true. Every matching authority applies. They do not cancel each other.

**Why this priority**: Wrong voice or a picture with no grounded look is the failure this feature exists to stop. One routing rule is the whole product; later stories only prove each branch.

**Independent Test**: Present six jobs (agent instruction, DM Work, player-facing spoken text, wiki vault note, gathering look for a depiction, producing a visual aid). A second author names the same authorities without seeing the first list.

**Acceptance Scenarios**:

1. **Given** a writing or visual job, **When** the author classifies it, **Then** the matching authorities are named before prose is drafted or a picture is made.
2. **Given** a job that matches more than one classifier, **When** the work is done, **Then** every matching authority is applied.
3. **Given** a job that matches only one classifier, **When** the work is done, **Then** the other authorities are not treated as required.

---

### User Story 2 - Agent-consumed text follows writing-for-agents (Priority: P2)

When the Co-DM authors something another agent will follow — a skill, standing instruction, pointed-at procedure, spec, or other agent-consumed document — **writing-for-agents** is the prose authority. Wiki copy and theatre of the mind are not the model.

**Why this priority**: Agent-consumed documents are how later Co-DM runs behave. Human wiki voice in those documents wastes attention and drifts the process.

**Independent Test**: Give an author a job whose only reader is an agent. The result follows writing-for-agents and is not scored as wiki copy or as theatre of the mind.

**Acceptance Scenarios**:

1. **Given** a job whose reader is an agent, **When** the author writes it, **Then** writing-for-agents is the prose authority.
2. **Given** that document, **When** it is reviewed, **Then** it is not scored as DM wiki copy or as player-facing spoken text.
3. **Given** a vault file whose reader is an agent, **When** it is written, **Then** writing-for-agents remains the prose authority and vault format still applies.

---

### User Story 3 - DM-consumed text follows copy-writer (Priority: P3)

When the Co-DM authors Work, wiki, or a chat proposal the DM will read, **copy-writer** is the prose authority. Agent-instruction voice is not the model for that DM-facing text. Player-facing passages inside it are not copy-writer's job.

**Why this priority**: The wiki and Work exist so a human DM can run a session. Agent-speak on those surfaces is unusable at the table.

**Independent Test**: Give an author DM-facing Work with no player-facing passage. The result is complete-sentence human prose a DM can use, not agent instruction.

**Acceptance Scenarios**:

1. **Given** a job whose reader is the DM, **When** the author writes it, **Then** copy-writer is the prose authority.
2. **Given** that text, **When** a DM reads it, **Then** it is ordinary human prose, not telegraphic agent-speak.
3. **Given** DM-facing Work that is not yet a wiki vault note, **When** it is written, **Then** copy-writer applies and vault format is not required until the text is filed as a wiki note.

---

### User Story 4 - Player-facing text follows theatre of the mind (Priority: P4)

When the Co-DM authors text that crosses the DM/player boundary — spoken look, boxed read-aloud, diegetic handout, player-safe rendered text — **theatre of the mind** is the prose authority. Players hear and see only what the DM presents. Secrets, difficulty classes, unearned names, and agent-process language stay out.

**Why this priority**: Players must never hear the recipe. Theatre of the mind is the mouth surface.

**Independent Test**: Give an author a spoken-look job. A second person can read it aloud to players without leaking a secret, difficulty class, unearned name, or process note.

**Acceptance Scenarios**:

1. **Given** text that players will hear or see, **When** the author writes it, **Then** theatre of the mind is the prose authority.
2. **Given** that text, **When** it is spoken or shown, **Then** it contains no secret, difficulty class, unearned name, or agent-process language.
3. **Given** DM procedure on the same page, **When** the player-facing passage is written, **Then** that procedure is not inside the player-facing passage.

---

### User Story 5 - Wiki vault notes follow obsidian-markdown (Priority: P5)

When the Co-DM writes a wiki vault note, **obsidian-markdown** is the format authority. Reader still decides prose: DM-facing bands use copy-writer; player-facing bands use theatre of the mind; agent-consumed vault files use writing-for-agents. Pictures on that note still use the visual authorities.

**Why this priority**: The vault is the product the DM opens. Format and prose are different jobs; format is required on every wiki note regardless of reader.

**Independent Test**: File a new wiki vault note that includes DM-facing text and spoken look. Format matches the vault; DM bands and spoken bands still use their own prose authorities.

**Acceptance Scenarios**:

1. **Given** a wiki vault note, **When** it is written, **Then** obsidian-markdown is the format authority.
2. **Given** that note also has a DM reader, **When** it is written, **Then** copy-writer still applies to DM-facing bands.
3. **Given** that note also has player-facing text, **When** it is written, **Then** theatre of the mind still applies to those passages.
4. **Given** writing that is not a wiki vault note, **When** it is written, **Then** obsidian-markdown is not required.

---

### User Story 6 - Working with visual references uses visual-references (Priority: P6)

When the Co-DM is about to depict a known wiki owner — a person, creature, place, vehicle, item, or named moment — **visual-references** is the authority for gathering and using that owner's existing look. Appearance already on the owner, and pictures already of that owner, are the look. They do not decide camera, mood, or staging. This authority does not place a finished picture on a page.

**Why this priority**: A depiction that ignores the owner's look invents a second face. Gathering look is a different job from producing the aid.

**Independent Test**: Give an author a depiction job for a named owner who already has a look. The author uses that owner's existing look before any new picture is made, and does not treat placing the finished picture as this job.

**Acceptance Scenarios**:

1. **Given** a depiction that includes a known wiki owner, **When** the author works with visual references, **Then** visual-references is the authority.
2. **Given** that owner has an existing look, **When** a new picture is made, **Then** the picture keeps that identity; composition and staging may still be chosen.
3. **Given** a known owner with no usable look, **When** a depiction is requested, **Then** the author stops and asks or routes to the owning craft instead of inventing a face.
4. **Given** finished art that needs to live on a page, **When** that placement is the job, **Then** visual-references is not the authority for placing it.

---

### User Story 7 - Producing visual aids uses visual-aids (Priority: P7)

When the Co-DM attaches, grounds, generates, promotes, or places a player-safe visual aid for a named owner or a named session moment, **visual-aids** is the authority. A reference image is durable identity. An illustration is one moment and is not identity. Spoken look stays theatre of the mind. Distinct things get distinct pictures. Players see nothing until the DM accepts and presents.

**Why this priority**: The screen surface the DM can show must be grounded, player-safe, and not a second identity for the same owner.

**Independent Test**: Give an author a job to place or mint a picture for a named owner with an existing look. The result is a visual aid for that owner or moment, not a reused picture of someone else, and spoken look is still theatre of the mind.

**Acceptance Scenarios**:

1. **Given** a job to attach, ground, generate, promote, or place a visual aid, **When** the author does it, **Then** visual-aids is the authority.
2. **Given** a named owner with an existing look, **When** identity art is produced, **Then** it depicts that owner and is not reused from a different owner, site, or moment.
3. **Given** a named session moment, **When** an illustration is produced, **Then** it stays a moment picture and is not treated as identity.
4. **Given** spoken look on the same page, **When** a visual aid is placed, **Then** theatre of the mind still owns the words the DM says.
5. **Given** a depiction of a known wiki owner, **When** a new picture is generated, **Then** visual-references has already been applied; visual-aids then produces or places the aid.

---

### Edge Cases

- A mixed wiki page (DM-facing bands plus spoken look): copy-writer on DM-facing bands, theatre of the mind on player-facing passages, obsidian-markdown on the note. One voice for the whole file is a failure.
- A vault file whose reader is an agent (standing wiki instruction): writing-for-agents plus obsidian-markdown. copy-writer does not own that prose.
- Chat Work the DM reads that is not yet filed: copy-writer only. Vault format waits until it is a wiki note.
- A player-facing sample inside a DM proposal: theatre of the mind for that passage; copy-writer for the surrounding DM text.
- A handout the players will see: theatre of the mind. If it is also filed as a wiki note, vault format applies.
- Unknown reader: treat as DM-consumed Co-DM output (copy-writer). Do not default to agent-instruction voice.
- A wiki note that also needs an identity picture: visual-aids for the picture, copy-writer and theatre of the mind for their bands, obsidian-markdown for the note.
- Depicting a known owner: visual-references first, then visual-aids to produce or place. Swapping those jobs is a failure.
- Existing art of a different owner, site, or moment: vibe only. It is not identity for a new thing.
- A missing look: stop. Do not invent a PC face or a new identity.
- Maps and battlemaps are not this visual-aid job. Spoken narration is not this visual-aid job.
- Craft jobs (facts, math, procedure) keep their owners. This feature only chooses writing or visual authority; it does not restock canon or invent mechanics.
- Legacy wiki pages are not rewritten solely to prove this routing.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Every writing job MUST be classifiable by reader (agent, DM, players) and by whether it is a wiki vault note, before prose is drafted.
- **FR-002**: Agent-consumed writing MUST follow writing-for-agents as its prose authority.
- **FR-003**: DM-consumed writing MUST follow copy-writer as its prose authority.
- **FR-004**: Player-facing writing MUST follow theatre of the mind as its prose authority.
- **FR-005**: Wiki vault notes MUST follow obsidian-markdown as their format authority.
- **FR-006**: When more than one classifier is true, every matching authority MUST apply. Matching authorities MUST NOT cancel each other.
- **FR-007**: On a mixed document, each passage MUST follow the authority for that passage's reader. DM-facing bands MUST NOT be written as theatre of the mind. Player-facing passages MUST NOT be written as wiki copy or as agent instruction.
- **FR-008**: copy-writer MUST NOT be the prose authority for agent-consumed documents.
- **FR-009**: writing-for-agents MUST NOT be the prose authority for DM-consumed Work or wiki prose.
- **FR-010**: theatre of the mind MUST NOT be the prose authority for DM procedure, hidden truth, or agent instruction.
- **FR-011**: obsidian-markdown MUST NOT be required for writing that is not a wiki vault note.
- **FR-012**: Craft owners of facts, math, and procedure remain owners of those jobs. This routing MUST NOT reassign fact ownership.
- **FR-013**: A writing or visual job is incomplete until every matching authority has been applied.
- **FR-014**: The Co-DM MUST apply this routing to new writing and new picture work. Legacy wiki pages MUST NOT be rewritten solely to satisfy this feature.
- **FR-015**: Every visual job MUST be classifiable as working with visual references or producing a visual aid, before a picture is made or placed.
- **FR-016**: Working with visual references MUST follow visual-references. That authority MUST NOT be the one that places finished art on a page.
- **FR-017**: Attaching, grounding, generating, promoting, or placing a visual aid MUST follow visual-aids. That authority MUST NOT gather visual references in place of visual-references when a known owner is depicted.
- **FR-018**: A depiction of a known wiki owner MUST use that owner's existing look. Composition and staging MAY still be chosen. A missing look MUST stop the depiction rather than invent a face.
- **FR-019**: Identity pictures MUST depict the named owner. An illustration of a named moment MUST NOT become identity. Pictures of a different owner, site, or moment MUST NOT be reused as identity.
- **FR-020**: A visual aid MUST NOT replace theatre of the mind as the words the DM says. Players MUST see nothing until the DM accepts and presents.
- **FR-021**: visual-aids MUST NOT own map rendering or spoken narration.

### Key Entities

- **Writing job**: One act of authoring text with a known reader and destination.
- **Visual job**: One act of working with pictures — gathering look, or producing a visual aid.
- **Reader**: Who the text is for — an agent, the DM, or the players.
- **Wiki vault note**: A campaign page in the wiki the DM opens.
- **writing-for-agents**: Prose authority for text an agent will follow.
- **copy-writer**: Prose authority for text the DM will read.
- **theatre of the mind**: Prose authority for text that crosses the DM/player boundary. The mouth surface.
- **obsidian-markdown**: Format authority for wiki vault notes.
- **visual-references**: Authority for gathering and using an owner's existing look before depicting them.
- **visual-aids**: Authority for attaching, grounding, generating, promoting, or placing a visual aid.
- **Visual aid**: A picture for a named owner or a named session moment. Prep art is Work until the DM accepts.
- **Reference image**: Durable identity for an owner. Not a moment illustration.
- **Illustration**: A session-scoped moment picture. Not identity.
- **Work**: Mutable prep the DM may accept, edit, or reject.
- **Mixed document**: One artifact with more than one reader (typically a wiki note with DM-facing bands and spoken look).

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Two independent reviewers classify a set of at least 16 jobs covering agent, DM, player, vault, mixed writing, gathering visual references, and producing visual aids, and agree on the matching authorities for 100% of those jobs.
- **SC-002**: In a review of new agent-consumed documents after this rule is in force, 0% are written in wiki-copy voice or theatre of the mind voice.
- **SC-003**: In a review of new DM-facing Work and wiki prose after this rule is in force, 0% are telegraphic agent-speak.
- **SC-004**: In a read-aloud test of new player-facing passages, 100% can be presented to players without a secret, difficulty class, unearned name, or agent-process language.
- **SC-005**: 100% of new wiki vault notes use vault format, including spoken text kept as theatre of the mind and separate from DM procedure when spoken text is present.
- **SC-006**: On a mixed wiki page, a reviewer judges DM-facing bands as copy-writer, player-facing passages as theatre of the mind, and the note as vault format — not a single voice for the whole file.
- **SC-007**: After this rule is in force, 0% of legacy wiki pages are rewritten solely to match it.
- **SC-008**: In a review of new depictions of known wiki owners, 100% used visual-references for the existing look and visual-aids to produce or place the picture; 0% invented a face or reused a different owner's picture as identity.
- **SC-009**: In a review of new wiki notes that include a visual aid, 100% still treat spoken look as theatre of the mind; the picture does not replace the words the DM says.

## Assumptions

- The primary human reader of Co-DM output is the DM.
- "Humans will read" means DM-consumed Co-DM output: Work, wiki, and chat proposals. It does not mean README files, contributor docs, or issue-tracker chrome unless that text is Work or wiki.
- "Agents will read" means documents an agent is expected to follow: skills, standing instructions, pointed-at procedures, commands an agent is expected to follow, specs, and the constitution. It does not mean every file an agent might open while researching.
- "Players will read" means text that crosses the DM/player boundary (theatre of the mind, diegetic handouts, player-safe rendered text). Players do not read the wiki.
- "Obsidian vault" means campaign wiki notes the DM opens, including templates and `_raw/` samples. Skill files and repository docs are not wiki vault notes even when they are markdown.
- Working with visual references means gathering and using existing look so a depiction stays that owner. Producing visual aids means attaching, grounding, generating, promoting, or placing the picture. The two jobs stack when a known owner is depicted.
- The six authorities compose. They do not compete.
- Existing Work rules still bind: no campaign wiki write until the DM accepts, except named ingest stubs. Prep art is Work, not auto-canon. Players see nothing until the DM accepts and presents.
- Out of scope: rewriting legacy wiki pages to prove routing; changing who owns facts, math, or procedure; Foundry play-surface staging; map rendering; inventing a seventh writing or visual authority.
