# Feature Specification: Sample Content Guidance

**Feature Branch**: `006-aruhe-page-standards`

**Created**: 2026-09-11

**Status**: Draft

**Input**: User description: "the design of the place files within _raw/ is the ideal layout, form, and shape for outdoor locations, this is a high quality sample from the island of aruhe that should shape repo design. As well as the related items are representive of items format and layout and quality. In addition the monsters file are also representenive high quality samples from the island of aruhe" plus later direction: distilled guidance, not hard-coded gold standards; this is the default for all sample content, not legacy content.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Any sample page is runnable in one pass (Priority: P1)

A DM opens a sample page — a place, item, hazard, creature, or person. One pass is enough to speak what players can hear, run what the table needs, and stop. Empty headings, cloned outlines, and second copies of numbers are failures.

**Why this priority**: `_raw/` samples are quality evidence, not templates to photocopy. The default for all sample content is the same: runnable, player-safe, no scaffolding. Legacy pages are not in this feature.

**Independent Test**: Hand a complete sample page of any kind to a second DM. They can speak the look and resolve first contact without asking the author or opening a second page for the same numbers.

**Acceptance Scenarios**:

1. **Given** a complete sample page, **When** the DM opens it, **Then** spoken look and the run questions for that kind are on the page.
2. **Given** that page, **When** they speak the look, **Then** players hear senses, not secrets, difficulty classes, or unearned names.
3. **Given** numbers that belong to an object, hazard, or creature, **When** another sample page mentions them, **Then** it links the owner instead of copying the effect, save, or sheet.
4. **Given** a thin sample page and a dense sample page of the same kind, **When** a DM compares them, **Then** both answer the same run questions; the thin page is not missing a required empty section.

---

### User Story 2 - Sample places are a run loop (Priority: P2)

A DM opens a sample place. They can speak the ground, know what the site is now, resolve a move that changes the scene, see who is present or the sign of absence, put objects on the table, know how it connects, and know why it matters.

**Why this priority**: Aruhe outdoor places show this loop clearly. The same jobs are the default for every new sample place, not only those two files.

**Independent Test**: A second DM speaks the look, names a way onward, resolves one consequential move, and says why the site exists, from the sample page alone.

**Acceptance Scenarios**:

1. **Given** a complete sample place, **When** the DM opens it, **Then** look, situation, consequential moves, presence, table objects, connections, and purpose are on the page.
2. **Given** a move that changes nothing, **When** the page is written, **Then** that move is omitted.
3. **Given** nobody is here, **When** the DM reads presence, **Then** absence plus remaining sign is enough; occupants are not invented.
4. **Given** an object or creature with an owner page, **When** the place stocks it, **Then** the place links the owner.

---

### User Story 3 - Sample objects resolve in one use (Priority: P3)

A DM opens a sample takeable object or flora hazard. A consumable is a portrait, a classification, and one effect. A hazard is a look plus start, notice, cost, careful passage, and honest refusal. The page then stops.

**Why this priority**: Related Aruhe items show that quality is a short runnable object, whether it is eaten or walked into.

**Independent Test**: A second DM resolves a consumable use, or notices and refuses a hazard, from that sample page alone.

**Acceptance Scenarios**:

1. **Given** a complete sample consumable, **When** a player uses it, **Then** the owner page is enough.
2. **Given** a complete sample flora hazard, **When** the party contacts or avoids it, **Then** start, notice, cost, careful passage, and refusal are on the page.
3. **Given** a sample place or creature that mentions that object, **When** the DM follows the link, **Then** they do not find a second full copy of the numbers.

---

### User Story 4 - Sample creatures are a hunt (Priority: P4)

A DM opens a sample creature. They can speak the body, run the sheet, know where it lives, how it hunts, and how the party shuts it down. Visual density may vary. The hunt questions do not.

**Why this priority**: Aruhe monster pages are hunts, not statblock stubs. That is the default for sample creatures.

**Independent Test**: A second DM speaks the look, names habitat, runs the opening move, and names one shut-down, from the sample page alone.

**Acceptance Scenarios**:

1. **Given** a complete sample creature, **When** the DM opens it, **Then** look, sheet, life, and hunt are on the page.
2. **Given** life, **When** they read it, **Then** they know habitat, habits, diet, and whether it hunts alone or with others, with links to ground it actually uses.
3. **Given** the hunt, **When** they read it, **Then** they know signs, what starts and ends it, the opening move, a shut-down the party can attempt, and what the scene looks like after.
4. **Given** two sample creatures with different visual density, **When** a DM compares them, **Then** both still answer those questions; neither is a different campaign type.

---

### User Story 5 - Sample people are playable, not cloned bands (Priority: P5)

A DM opens a sample person. They can speak the look, know who this is and what they want, play the first minutes, and know whether a fight is on the page. Extra depth exists only when that person actually has it.

**Why this priority**: The NPC samples are people at different densities, not four frozen classes to photocopy. They fall under the same default as every other sample.

**Independent Test**: A second DM names role, want, first move, and fight handling from the sample page alone, without treating unused extra depth as missing.

**Acceptance Scenarios**:

1. **Given** a complete sample person, **When** the DM opens it, **Then** identity, spoken look, how to play the first minutes, and named ties are on the page.
2. **Given** a sample person who can fight, **When** the DM needs the fight, **Then** the page has the encounter rule and either a sheet or one pointer to the owner sheet.
3. **Given** a sample person who cannot fight, **When** the DM scans the page, **Then** there is no empty combat section.
4. **Given** extra facts (a secret, another form, a live pressure), **When** they exist, **Then** they appear; when they do not, they are omitted.

---

### Edge Cases

- A field or section has no content: omit it.
- A direction or tie is unknown: name the gap; do not invent a neighbor or occupant.
- An island or campaign rule already covers the move: link the rule; do not hide the cost in spoken look.
- Work is not wiki until the DM accepts; the sample page still follows this guidance.
- Named ingest stubs are sentences and identity only.
- New indoor sample places use the same place jobs. They do not get a second standard.
- Sample files may be revised. Guidance stays; a named file is not a freeze.
- Legacy content is out of scope: do not rewrite it to this guidance, do not fail it against these jobs, and do not treat wrapup of a legacy page as a conversion.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: This guidance is the default for all sample content. Samples illustrate jobs and quality. They MUST NOT be treated as a frozen heading list, density class, or clone target. Legacy content is out of scope and MUST NOT be rewritten or scored against this guidance.
- **FR-002**: Every complete sample page MUST be runnable in one pass: spoken look plus the run questions for its kind.
- **FR-003**: Spoken look on a sample page MUST be theatre of the mind. It MUST NOT contain secrets, difficulty classes, unearned names, or author thesis.
- **FR-004**: On sample pages, numbers live on one owner page. Other sample pages MUST link that owner. They MUST NOT copy the effect, save, or sheet.
- **FR-005**: Empty sections MUST NOT appear on sample pages. Unused identity keys MUST be omitted. Density follows what is true of the subject.
- **FR-006**: Outside fight sheets, hazard rows, and short cue lists, sample pages MUST be complete-sentence human prose. Telegraphic agent-speak is invalid. Stubs MAY be short and MUST still be sentences.
- **FR-007**: A sample place MUST answer: look; what the site is now; moves that change the scene; who is present or the sign of absence; what can be put on the table; how it connects; why it matters. No-op moves MUST be omitted. Occupants MUST NOT be invented to look complete.
- **FR-008**: A sample consumable MUST be a spoken portrait, a classification, and one runnable effect, then stop.
- **FR-009**: A sample flora hazard MUST be a spoken look plus start, notice, contact cost, careful passage, and honest counterplay.
- **FR-010**: A sample creature MUST answer: look; runnable sheet; life (habitat, habits, diet, social); hunt (signs, instincts, opening, shut-down, aftermath). Shut-downs MUST be things the party can do. Habitat MUST name ground it uses and ground it refuses when that refusal is true.
- **FR-011**: A sample person MUST answer: who they are and what they want; spoken look; how to play the first minutes and what changes posture; named ties. Combat is present only when they can fight, as an encounter rule plus a sheet or one pointer.
- **FR-012**: Filed campaign types MUST stay in the existing closed set (`place`, `item`, `creature`, `npc`, and the other already-listed wiki types). Authors MUST NOT invent type values. Early sample labels (`location`, `monster`, `lore`) map to `place`, `creature`, and `item` when filed.
- **FR-013**: Sample identity MUST include the wiki's required fields plus campaign, visibility, and a one-sentence summary. Unspecified lifecycle is Work (`proposed`) until the DM accepts. Default visibility is DM-only.
- **FR-014**: The Co-DM MUST apply this guidance when proposing or filing sample pages. No campaign wiki write until the DM accepts, except named ingest stubs. Wrapup of a legacy page MUST NOT convert that page into a sample.

### Key Entities

- **Sample content**: `_raw/` exemplars and new pages authored as samples of those kinds (places, items, hazards, creatures, people).
- **Legacy content**: Existing campaign pages, archives, and historical notes that were not authored as these samples. Out of scope.
- **Run questions**: The jobs a kind must answer so a DM can play it. Headings may vary; the jobs may not.
- **Spoken look**: Theatre of the mind. Player-safe.
- **Owner page**: The only page that holds an object's, hazard's, or combatant's numbers.
- **Place / consumable / flora hazard / creature / person**: Kinds with the jobs in FR-007 through FR-011.
- **Work**: Mutable prep. Not wiki until the DM accepts.
- **Stub**: Thin page for a name in an approved source. Sentences and identity only.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A DM who knows the campaign can open a complete sample page and start play from it in under 45 seconds without asking the author.
- **SC-002**: In a read-aloud test of spoken looks on at least one complete sample page per kind, 100% can be spoken to players without a secret, difficulty class, or unearned name.
- **SC-003**: On a mixed set of at least eight complete sample pages across kinds, 0% show empty headings or a second copy of another page's numbers.
- **SC-004**: A second DM can run first contact from one new sample place, one new sample object, one new sample creature, and one new sample person written from this guidance (not cloned from a named file).
- **SC-005**: A thin sample page and a dense sample page of the same kind are judged the same kind of page; the thin page is not marked incomplete for lacking unused sections.
- **SC-006**: After this guidance is in force, 0% of legacy pages are rewritten solely to match it.

## Assumptions

- Primary reader is the human DM. Players hear theatre of the mind and see play-surface artifacts.
- `_raw/` is evidence of quality across kinds. Distill the jobs those pages do. Do not freeze filenames, heading order, or named density bands as the product.
- This feature does not migrate, lint, or restyle legacy content. Wrapup that updates a legacy page leaves its shape alone unless the DM asks to replace it with a new sample page.
- Earlier NPC page work remains useful as examples of people at different densities. Where it treats named files as required clone targets, this guidance is the default for samples instead.
- Campaign types stay the wiki's closed set.
- `visibility` and `reveal` are different fields.
- Existing Co-DM rules still bind: complete-sentence prose; wiki writes after accept; named ingest may stub; invention is Work.
- Out of scope: legacy content; Foundry actor sync; player-facing sheets; a second parallel format beside this sample default.
