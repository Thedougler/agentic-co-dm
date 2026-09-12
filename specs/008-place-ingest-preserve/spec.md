# Feature Specification: Place Ingest Preserve

**Feature Branch**: `008-place-ingest-preserve`

**Created**: 2026-09-12

**Status**: Draft

**Input**: User description: "agents have been losing the required narration blocks when ingesting places and mutating the format"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Ingested places still have spoken look (Priority: P1)

A DM asks to ingest or promote a place page that already has a required spoken look. After ingest, the wiki place still has that spoken block as an open `[!narration]` the DM can read aloud. The block is not dropped, emptied, folded into ordinary prose, or rewritten as a knowledge summary.

**Why this priority**: A place without theatre of the mind is not runnable. Losing narration on ingest is the named failure.

**Independent Test**: Ingest one complete place that has a filled `[!narration]` Narration under Overview. Open the filed wiki page. Speak the look. It is still there, still a narration callout, still player-safe.

**Acceptance Scenarios**:

1. **Given** a complete place with `> [!narration] Narration` and a filled spoken look, **When** it is ingested or promoted, **Then** the wiki page still has that open `[!narration]` block with the spoken look intact.
2. **Given** that ingested page, **When** the DM reads the spoken look aloud, **Then** players hear senses, routes, and what a body can use — not secrets, difficulty classes, or unearned names.
3. **Given** a place whose source narration was empty (Work stub), **When** it is ingested, **Then** the empty titled `[!narration] Narration` stub remains; ingest does not delete the required block.

---

### User Story 2 - Ingest does not mutate place format (Priority: P1)

The DM ingests a place written in the campaign place shape (Overview with spoken look, At a glance, If the party, Who, What, Where, Why, Art when art exists). After ingest, Reading view still shows that shape. Ingest does not compile the place into a distilled concept page, flatten callouts, or restyle it into a different outline.

**Why this priority**: Format mutation is the second named failure. Jobs from sample-place guidance still hold; ingest must not replace the page with a different document type.

**Independent Test**: Side-by-side the source place and the ingested wiki page. Heading spine, image embeds, wikilinks, and `[!narration]` still match. The page is still `type: place`, not a concept note.

**Acceptance Scenarios**:

1. **Given** a complete place in the campaign place shape, **When** it is ingested, **Then** the wiki page keeps that shape: identity image, Overview with `[!narration]`, At a glance, If the party, Who, What, Where, Why, and Art when art exists. Unused jobs stay omitted, not filled with empty headings.
2. **Given** mixed ingest that also includes ordinary knowledge sources, **When** those sources are compiled, **Then** place pages are still filed as places with their layout preserved.
3. **Given** an already-ingested place with no body change, **When** ingest runs again, **Then** narration and format are not rewritten into a different template.
4. **Given** a place that names an object or creature with an owner page, **When** ingest files it, **Then** it still links the owner instead of copying numbers.

---

### Edge Cases

- A job has no content (no occupants, no art): omit that section; do not invent occupants or leave an empty heading.
- Named ingest stubs for a new name in an approved source may be identity plus complete sentences; they still carry an empty `[!narration] Narration` stub if the page is a place.
- Unaccepted Work does not publish a wiki page except named ingest of approved sources.
- Legacy places not authored as campaign samples are out of scope: do not restyle them solely to match this format.
- Session-prep ingest preserve is a different page kind (already specified). This feature is places.
- Indoor and outdoor places use the same place jobs and the same narration block. They do not get a second format.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: When a `type: place` page is ingested or promoted, the system MUST preserve the source layout and markdown treatments. It MUST NOT distill the place into a knowledge-wiki concept page, flatten callouts or tables, drop image embeds, or replace the place outline with a different template.
- **FR-002**: A complete ingested place MUST keep a required open `[!narration]` Narration block as the spoken look (typically under Overview). Ingest MUST NOT delete, empty, or convert that block into ordinary body prose.
- **FR-003**: Spoken look on an ingested place MUST remain theatre of the mind: no secrets, difficulty classes, unearned names, or author thesis inside `[!narration]`.
- **FR-004**: Place run questions still apply after ingest: look; what the site is now; moves that change the scene; who is present or the sign of absence; what can be put on the table; how it connects; why it matters. No-op moves stay omitted. Occupants MUST NOT be invented to look complete.
- **FR-005**: Empty sections MUST NOT appear. Unused identity keys MUST be omitted. Density follows what is true of the place.
- **FR-006**: Mixed ingest MUST keep compiling ordinary knowledge sources as compiled wiki pages, while places remain `type: place` with FR-001 and FR-002 preservation.
- **FR-007**: Re-ingest of an unchanged place MUST NOT rewrite narration or format.
- **FR-008**: Numbers that belong on an owner page MUST stay linked, not copied, after ingest.
- **FR-009**: The Co-DM MUST apply this when ingesting or promoting places. No campaign wiki write until the DM accepts, except named ingest of approved sources.
- **FR-010**: Legacy places outside the campaign sample set MUST NOT be rewritten solely to match this format.

### Key Entities

- **Place page**: A campaign `type: place` note the DM runs. Spoken look plus run questions.
- **Spoken look / narration block**: Open `[!narration]` Narration. Theatre of the mind. Required on a complete place.
- **Place format**: The campaign place shape (Overview + narration, At a glance, If the party, Who, What, Where, Why, Art when present). Jobs required; empty sections omitted.
- **Ingest / promote**: Filing an approved place source into the wiki. For places, filing preserves shape; it does not compile facts away from the page.
- **Owner page**: The only page that holds an object’s, hazard’s, or combatant’s numbers.
- **Work**: Mutable prep. Not wiki until the DM accepts.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: After ingest of at least three complete places that had filled narration, 100% of the wiki pages still have an open `[!narration]` Narration block whose spoken look can be read aloud in under 45 seconds.
- **SC-002**: In a side-by-side Reading-view comparison of those sources and wiki pages, 0% lose Overview, drop the narration callout, or become a concept-style page.
- **SC-003**: In a read-aloud test of ingested place narration, 100% can be spoken to players without a secret, difficulty class, or unearned name.
- **SC-004**: On a mixed ingest of at least one place and one ordinary knowledge source, 0% of places are rewritten as distilled concept pages, and the knowledge source is still compiled as a wiki page.
- **SC-005**: After this rule is in force, 0% of legacy places are rewritten solely to match it.

## Assumptions

- Primary reader is the human DM. Players hear theatre of the mind.
- Sample-place run questions from existing campaign guidance still bind. This feature does not replace those jobs; it stops ingest from destroying the spoken block and the place shape.
- Evidence places in `_raw/` (for example Old Gardens) illustrate the shape. They are not clone titles.
- Session-prep preserve is out of scope here; it is already specified.
- Items, creatures, and people are out of scope unless the DM later asks to extend the same preserve rule.
- Existing Co-DM rules still bind: complete-sentence prose; wiki writes after accept; named ingest may stub; invention is Work.
- Out of scope: Foundry staging; player-facing sheets; mass restyle of legacy places; inventing a second indoor place format.
