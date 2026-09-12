# Feature Specification: NPC Page Standard

**Feature Branch**: `003-npc-page-standard`

**Created**: 2026-09-11

**Status**: Draft

**Input**: User description: "within _raw/ there are two sample npc files (Hinewai and Talon Skarn) that represent a high level complex potentially hostile npc, and slightly lower level potentially hostile npc. Both of these are the best version yet weve found to represent these ideas in markdown, thus represent the new baseline standard for high level hostile npc creation. The Nona Blackjaw represents a complex friendly npc and Thunk represents a less complex friendly npc. The format should be standardized with intelligent defaults and optional sections to make pages consistent, readable, usable, and perfect for the dm reading them in obsidian."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - One page a DM can run without hunting (Priority: P1)

A DM opens an NPC page during prep or at the table pause between scenes. In one pass they see who this person is, how to play them, what they want, and whether a fight is on the page. They do not reconstruct the NPC from scattered headings, empty stubs, or agent shorthand.

**Why this priority**: The wiki is the product the DM opens. If the page is not runnable, no later skill or ingest helps.

**Independent Test**: Open each of the four baseline pages (Hinewai, Talon Skarn, Nona Black-Jaw, Thunk) and confirm a DM can name role, want, first move, and fight handling without leaving the page.

**Acceptance Scenarios**:

1. **Given** any complete NPC page, **When** the DM opens it, **Then** they find the core block in this order: title, At a Glance, spoken look, Running the NPC, Relationships.
2. **Given** that page, **When** the DM needs the spoken look, **Then** they copy the narration block and it contains no secrets, difficulty classes, or unearned names.
3. **Given** that page, **When** the DM needs the first table move, **Then** Running the NPC states how the meeting starts and what changes the NPC's posture.
4. **Given** a page for an NPC who can fight, **When** the DM looks for combat, **Then** they find either a runnable fight sheet on the page or a single pointer to the fight sheet, with the encounter rule in one sentence.

---

### User Story 2 - Hostile NPCs share one spine, two depths (Priority: P2)

A Co-DM authors a potentially hostile NPC. High-complexity landmark hostiles follow Hinewai: extra form, true weakness, history, and staged fight sheets tied to a condition the party can change. Lower-complexity skirmish hostiles follow Talon Skarn: combat-forward running notes, one fight sheet, counterplay, and difficulty knobs. Both keep the same core spine so the DM is never surprised by heading order.

**Why this priority**: The user named these two pages as the new hostile baseline. Without a shared spine, later hostiles drift back into one-off layouts.

**Independent Test**: Author one landmark hostile and one skirmish hostile from the standard; a second reader finds the same core headings in the same order on both, with extra hostile sections present only on the landmark page.

**Acceptance Scenarios**:

1. **Given** a landmark hostile (Hinewai-class), **When** the DM reads At a Glance, **Then** they see Role, Nature, Home, Wants, plus the extra rows that make the threat runnable (weakness, return, or permanent end) and a one-sentence DM thesis.
2. **Given** that landmark hostile, **When** they have more than one body or face, **Then** each extra form has its own glance-and-spoken-look pair, and combat stages map to a condition the party can change, not to hit points on the walking body alone.
3. **Given** a skirmish hostile (Skarn-class), **When** the DM reads Running the NPC, **Then** they get opening, default turn, pressure response, target priority, and counterplay without a second lore document.
4. **Given** that skirmish hostile, **When** the DM needs to tune the fight, **Then** difficulty knobs change tactics or starting position without rewriting the rest of the page.

---

### User Story 3 - Friendly NPCs share one spine, two depths (Priority: P3)

A Co-DM authors a friendly NPC. Complex patrons follow Nona Black-Jaw: current pressure, public face versus secret, a limit, relationship invitations, and an activity log. Simpler contacts follow Thunk: a short glance, first-meeting cadence, one current pressure, and practical use (ship, shop, skill) without a secret ledger. Both stay on the same core spine as hostile pages.

**Why this priority**: Friendly pages currently diverge more than hostile pages (Nona has no Combat; Thunk points at a fight sheet). The standard must allow that without looking unfinished.

**Independent Test**: Author one patron and one contact from the standard; empty optional headings are absent; a DM can still run first meeting and current pressure on both.

**Acceptance Scenarios**:

1. **Given** a patron (Nona-class), **When** the DM reads Running the NPC, **Then** they know how the first meeting starts, what help buys, and what closes the door.
2. **Given** that patron, **When** they have a live plot, **Then** Current pressure, public-versus-secret, and Relationships with invitations are present, and an activity log records what already happened at the table.
3. **Given** a contact (Thunk-class), **When** the DM opens the page, **Then** glance, running notes, practical use, one current pressure, and Relationships are enough; unused patron sections are omitted.
4. **Given** a friendly NPC who is not expected to fight, **When** the DM scans the page, **Then** there is no empty Combat heading and no leftover fight sheet.

---

### User Story 4 - New pages inherit defaults; unused sections stay gone (Priority: P4)

A Co-DM creates a new NPC page. Required fields and core sections appear with intelligent defaults. Optional sections appear only when they have content. The DM reads a short contact and a landmark hostile as the same kind of page, not two different document types.

**Why this priority**: Consistency is the point of a standard. Defaults prevent missing identity fields; omitting unused sections prevents template residue.

**Independent Test**: Create a minimal contact using only required fields and core sections; confirm defaults fill identity fields; confirm no empty optional headings render.

**Acceptance Scenarios**:

1. **Given** a new NPC with only a name, role, want, spoken look, and first meeting, **When** the page is filed, **Then** identity fields that were not supplied take the defaults in this spec, and the core sections still appear in standard order.
2. **Given** that minimal page, **When** the DM scans headings, **Then** they do not see History, extra forms, activity log, difficulty knobs, or Combat unless those sections have content.
3. **Given** two complete NPC pages of different bands, **When** a DM compares heading order, **Then** every shared heading appears in the same relative order.

---

### Edge Cases

- NPC is potentially hostile but the party meets them as a guest first (Hinewai-class): Running the NPC starts with welcome, then the line that ends it; Combat is still present.
- NPC can fight but the wiki already has a separate fight sheet: Combat is a pointer plus encounter rule, not a second copy of the numbers.
- NPC has two bodies or faces: each form gets glance plus spoken look; Combat still chooses sheets from a named condition.
- Friendly NPC later becomes a combatant: add Combat (sheet or pointer) without reordering the core spine.
- Combatant later becomes a contact only: remove or collapse Combat; do not leave an empty heading.
- Location or faction is unknown: use `unknown` or `none`; do not invent a place or faction to satisfy the field.
- Thin stub from named ingest: complete sentences, core identity fields, no optional-section scaffolding.
- Spoken look would leak a secret, phylactery, or difficulty class: that fact stays in At a Glance, Running the NPC, or Combat, never in narration.
- Extra lore (phylactery, ship guns, missing-persons desk) is unique to one NPC: it is an optional section after Running the NPC and before Relationships; it does not reorder the core spine.
- Page is Work, not canon: identity fields still follow this standard; the page is not filed to the wiki until the DM accepts, per existing Co-DM rules.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Every NPC page MUST use campaign type `npc` and MUST include the core body in this order: title; At a Glance; spoken look; Running the NPC; Relationships. Optional sections, when present, MUST keep the relative order defined in Key Entities.
- **FR-002**: Every NPC page MUST include identity fields: `title`, `category`, `tags`, `sources`, `created`, `updated`, `type`, `lifecycle`, `reveal`, `campaign`, `status`, `role`, `location`, `faction`, `visibility`, and `summary`. Optional identity fields (`aliases`) MUST be omitted when unused.
- **FR-003**: Unspecified identity fields MUST take these defaults: `category` `entities`; `type` `npc`; `lifecycle` `proposed` until the DM accepts; `reveal` `unrevealed`; `status` `alive`; `visibility` `dm`; `faction` `none`; `location` `unknown`. `role` MUST be supplied by the author (`rival`, `patron`, or `contact`). `summary` MUST be one sentence the DM can read in a list.
- **FR-004**: At a Glance MUST be a cue table, not prose, and MUST include rows Role, Nature, Home, and Wants. It MUST end with a one-sentence **DM thesis**. Extra rows are allowed only when they change how the DM runs the NPC (pressure, limit, fear, hate, love, hook, leverage, kit, signature, weakness, return, permanent end, arrival, fight posture).
- **FR-005**: Spoken look MUST be theatre of the mind the DM can read aloud. It MUST NOT contain secrets, difficulty classes, unearned names, or DM thesis. When a portrait or reference image exists, it belongs with the spoken look, not inside Combat.
- **FR-006**: Running the NPC MUST tell the DM the first move and the change that shifts posture. Potentially hostile pages MUST include how welcome ends or how the fight opens. Friendly pages MUST include how help is received and what closes the door or takes priority.
- **FR-007**: Relationships MUST be a table of wiki links and what each link means at the table. Patron pages MAY add an invitation on the same row. Empty relationship tables are forbidden; omit the section only on a stub that has no named ties yet.
- **FR-008**: Optional sections MUST be omitted when they have no content. Forbidden residue: empty History, empty Combat, empty activity log, placeholder extra forms, or unused difficulty knobs.
- **FR-009**: Combat, when present, MUST open with a one-sentence encounter rule. A fightable NPC MUST provide either a runnable fight sheet on the page or exactly one pointer to the fight sheet. Numbers MUST NOT be duplicated across pages.
- **FR-010**: Landmark hostiles (Hinewai-class) MUST include true weakness or permanent end in At a Glance when those facts exist, MUST give each extra form its own glance-and-spoken-look pair, and MUST key combat stages to a named condition the party can change.
- **FR-011**: Skirmish hostiles (Skarn-class) MUST put opening, default turn, pressure response, target priority, and counterplay in Running the NPC, MUST include one fight sheet, and MAY include difficulty knobs that change tactics or starting position only.
- **FR-012**: Patrons (Nona-class) MUST include Current pressure and MUST distinguish public face from secret when a secret exists. They MUST record table-facing activity when the NPC has already appeared. They MUST NOT carry a Combat section unless the NPC can enter a fight.
- **FR-013**: Contacts (Thunk-class) MUST stay on the core spine plus at most one Current pressure and one practical-use block (what they do for the party or the ship). They MUST NOT add patron ledgers, extra forms, or staged fight sheets unless the NPC actually has those facts.
- **FR-014**: An italic epithet under the title is optional. Unique lore that is not a core section (place-bound weakness, ship guns, missing-persons desk) MUST sit after Running the NPC and before Relationships.
- **FR-015**: NPC pages MUST be complete-sentence human prose outside cue tables, fight sheets, and activity logs. They MUST NOT use telegraphic agent-speak. Stubs MAY be short; they MUST still be sentences.
- **FR-016**: The four baseline pages — Hinewai (landmark hostile), Talon Skarn (skirmish hostile), Nona Black-Jaw (patron), Thunk (contact) — are the layout source. New and revised NPC pages MUST match their heading order and density for the matching band, not the thin three-heading stub currently used as a generic NPC outline.
- **FR-017**: The Co-DM MUST apply this standard when proposing or filing an NPC page. Existing Co-DM approval rules still apply: no campaign wiki write until the DM accepts, except named ingest stubs.
- **FR-018**: This standard applies to `type: npc` pages only. Creature, place, item, and hazard pages keep their own layouts. A fight sheet that lives on a creature page is linked from Combat; it is not rewritten as an NPC.

### Key Entities

- **NPC page**: A wiki page with `type: npc`. The DM's runnable brief for one person.
- **Core spine**: Title → At a Glance → spoken look → Running the NPC → Relationships. Present on every complete NPC page.
- **Identity fields**: Frontmatter that names the person, campaign, life status, role, place, faction, visibility, reveal, and lifecycle.
- **At a Glance**: DM cue table. Required rows: Role, Nature, Home, Wants. Ends with DM thesis.
- **Spoken look**: Theatre of the mind. Player-safe sensory copy.
- **Running the NPC**: How to play the first minutes and the posture change.
- **Relationships**: Named ties as wiki links plus table meaning.
- **Stance**: Potentially hostile or friendly. Does not equal alignment. A hostile may receive guests; a friendly may still fight.
- **Band**: Density profile, not a separate document type.
  - **Landmark hostile**: Hinewai. Extra form, true weakness, history, staged fight sheets.
  - **Skirmish hostile**: Talon Skarn. Combat-forward running notes, one fight sheet, counterplay, optional knobs.
  - **Patron**: Nona Black-Jaw. Pressure, public versus secret, invitations, activity log.
  - **Contact**: Thunk. Short glance, practical use, one pressure, Combat only as pointer or omitted.
- **Optional section**: Extra form, unique lore, History, Current pressure, public versus secret, limit, practical use, activity log, appearances, difficulty knobs, Combat, extra art. Omit when empty.
- **Fight sheet**: Runnable combat numbers. Either on the NPC page or on a linked creature page, never both.
- **Encounter rule**: One sentence that says which sheet to use and what the NPC is trying to achieve in a fight.
- **Stub**: Thin NPC page for a name in an approved source. Identity fields and sentences only; no optional scaffolding.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A DM who knows the campaign can open any complete NPC page and state role, want, first move, and fight handling in under 30 seconds.
- **SC-002**: Across the four baseline bands, 100% of complete NPC pages present the core spine in the same order; 0% of complete pages omit At a Glance, spoken look, Running the NPC, or Relationships.
- **SC-003**: On a sample of at least eight NPC pages (the four baselines plus four new or revised pages), 0% show empty optional headings.
- **SC-004**: In a read-aloud test of spoken-look blocks from those eight pages, 100% can be spoken to players without leaking a secret, difficulty class, or unearned name.
- **SC-005**: Given one new NPC in each band, a second DM can classify the band from the page alone and run first meeting without asking the author.
- **SC-006**: A minimal contact authored from defaults is usable at the table (first meeting and want are present) and is visually the same kind of page as a landmark hostile, not a different outline.
- **SC-007**: Fightable NPCs never require the DM to hunt a second unsourced document for the encounter rule; 100% have the rule and either a sheet or a single pointer on the page.
- **SC-008**: After this standard is in force, a DM rates four newly authored NPC pages as "usable at the table without reformatting" on at least three of the four.

## Assumptions

- Primary reader is the human DM in the wiki. Players hear narration and see play-surface artifacts; they do not open NPC pages.
- Designated reading surface is the existing prose wiki in the DM's second-brain workspace. Two-pane glance-and-look and compact fight sheets already used on the four baselines are the layout to keep for NPC pages. Creature pages stay linear.
- The four `_raw/` baselines are the best current expression of the four bands and remain the layout source until replaced by a later accepted revision of those same pages.
- `visibility` (who may read the page) and `reveal` (whether players have met or learned of the NPC) are different fields. Default `visibility` is DM-only.
- Role is a closed set for this feature: `rival` (potentially hostile), `patron` (complex friendly), `contact` (simple friendly). New role words wait for a later change.
- Existing Co-DM rules still bind: complete-sentence wiki prose; no campaign wiki write until the DM accepts; named ingest may create thin stubs; invention is Work until accepted.
- Bulk rewrite of every historical NPC is out of scope. New pages and pages touched in prep or wrapup MUST follow this standard. The four baselines already satisfy it in body layout; identity-field defaults apply when those pages are next accepted into the wiki.
- Out of scope: creature, place, item, and hazard templates; Foundry actor sync; player-facing NPC sheets; non-5e rules; a second NPC format beside this one.
