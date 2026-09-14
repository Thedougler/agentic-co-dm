# Feature Specification: PC Page Redesign

**Feature Branch**: `020-pc-page-redesign`
**Created**: 2026-09-14
**Status**: Draft
**Input**: User description: "Id like player character representation to be improved in the llm-wiki, utilizing proper obsidian markdown and columns (via the codeblock syntax), optimizing for dm usability and utility, while ensuring it remains easy and predictable for an agent in the llm-wiki to understand. The pc template will be redesigned and the pcs themselves should be conformed to it. skills and instructions must be updated as appropriate."

## User Scenarios & Testing

### User Story 1 - Reference any PC from one page (Priority: P1)

A DM opens a player character page during preparation or play. The page gives them an immediate player-safe look, party orientation, combat reference, key abilities, current resources, useful inventory, and the character's table-facing voice without requiring a search through satellite pages or source dumps. The players make all decisions and run their characters; the page helps the DM understand, portray, and adjudicate their choices.

**Why this priority**: The PC page is the DM's primary reference surface for portraying and adjudicating a party member, not a control sheet for the DM to run. Fast retrieval improves rulings and responsive table play.

**Independent Test**: Open each of the five current PC pages and, without opening another page, identify the character's player, class and level, current combat resources, signature actions, key relationships, and voice in under one minute.

**Acceptance Scenarios**:

1. **Given** a complete PC page, **When** the DM opens it, **Then** the page begins with one title, a player-safe narration block, and an At a Glance surface containing the player's identity, class and level, home ship, and a concise reference thesis.
2. **Given** a PC page during combat, **When** the DM needs to adjudicate a player choice, **Then** ability scores, modifiers, saves, skills, AC, HP, initiative, passive perception, speed, and other character-specific combat resources are findable in one predictable Sheet or Combat Profile area.
3. **Given** a PC page during a scene, **When** the DM needs to portray or respond to the character, **Then** Connections, Voice, and relevant session changes identify named ties and concrete table consequences without prescribing the player's action.
4. **Given** a PC with spells or other limited resources, **When** the DM needs to understand a player's available options, **Then** the page separates casting information, abilities, actions, uses, recovery, and current inventory without duplicating the same number in multiple sections.

---

### User Story 2 - Author predictable PC pages (Priority: P2)

A wiki agent creates or updates a PC page from the standard template. The agent can determine required frontmatter, canonical section homes, link behavior, omission rules, and the distinction between player-safe narration and DM-only facts without inferring from one-off pages.

**Why this priority**: A visually attractive page that agents cannot reliably create or update will drift immediately and increase retrieval cost.

**Independent Test**: Give an agent only the PC template, the applicable wiki instructions, and a representative character source. Confirm it can produce a complete page with stable headings, valid frontmatter, correct wikilinks, and no duplicate satellite dump.

**Acceptance Scenarios**:

1. **Given** a new or incomplete PC source, **When** an agent applies the standard, **Then** it knows which fields and sections are required, which sections are conditional, and where unknown values remain explicit rather than invented.
2. **Given** a PC page containing a narration block, **When** an agent updates DM-facing mechanics, **Then** it keeps secrets and mechanical details out of the player-facing narration and preserves complete-sentence wiki prose.
3. **Given** a page with an item, spell, place, faction, or party tie, **When** the referenced owner exists, **Then** the PC page uses a wikilink and states the relationship or table consequence without copying the owner's full content.
4. **Given** a non-caster or a character without a particular optional facet, **When** the page is filed, **Then** the unused heading and placeholder table are omitted rather than left as template residue.

---

### User Story 3 - Conform the current party without losing canon (Priority: P3)

A DM opens the existing pages for Jean-Claude Tabarnack, Perrin Black-Jaw, Catarina Da'Virelli, Crissdalynn Khinriss, and Delmar Fisk and sees the same PC document shape. Their established facts, source lineage, names, links, status, and campaign history remain available after the conformance pass.

**Why this priority**: The standard only provides value if the live party uses it. Conformance also demonstrates that the design handles multiclassing, spellcasting, special resources, different densities, and live session history.

**Independent Test**: Compare all five live pages against the redesigned template and their pre-change versions. Confirm every page has the shared spine, every previously supported fact remains represented or linked, and no archived source is mistaken for the canonical owner page.

**Acceptance Scenarios**:

1. **Given** any of the five current PC pages, **When** it is conformed, **Then** it uses the same required heading spine and frontmatter contract while retaining its character-specific density.
2. **Given** facts currently held in a page body, frontmatter, source list, or linked satellite, **When** the live PC page is conformed, **Then** the facts are preserved, moved to their canonical section, or represented by a clear owner link; they are not silently dropped.
3. **Given** a conformed page with existing art, aliases, sources, and wikilinks, **When** it is saved, **Then** those references remain usable and filenames or unrelated entities are not changed as part of the PC layout work.
4. **Given** a page whose fact status is proposed or canon, **When** only its structure changes, **Then** its lifecycle, reveal, visibility, and campaign meaning remain unchanged.

---

### User Story 4 - Maintain the standard across PC workflows (Priority: P4)

A maintainer updates the PC template or an applicable wiki workflow. The instructions, ingest path, interview path, and Markdown guidance agree on the same PC contract, so future authoring and reconciliation do not reintroduce satellite dumps, invalid columns, or competing headings.

**Why this priority**: The template alone cannot prevent regression when multiple skills create and revise PC pages.

**Independent Test**: Trace PC creation, interview, ingest, and Markdown formatting guidance. Confirm each path points to the same template and describes the same required frontmatter, section homes, column syntax, and omission rules.

**Acceptance Scenarios**:

1. **Given** an agent using a PC-related skill, **When** it creates or updates a PC page, **Then** the skill points to the canonical PC template and the governing wiki/Markdown instructions rather than restating a conflicting format.
2. **Given** a template or guidance update, **When** the maintainer searches PC-related skills and instructions, **Then** obsolete paths, satellite-template directions, and contradictory PC terminology are removed or corrected.
3. **Given** an Obsidian Reading view, **When** the DM opens a conformed page, **Then** supported column codeblocks render as paired scan surfaces while narration remains a real callout and the document still has a meaningful linear reading order if columns are unavailable.

### Edge Cases

- A PC is multiclassed: class and level data remains readable without assuming a single class or collapsing distinct spell/resource pools.
- A PC is a non-caster: the entire Spells section is omitted; the page does not retain an empty casting table.
- A PC has several resource systems, such as Focus, pact slots, charges, or temporary HP: each resource has one named home and an explicit recovery or source when known.
- A PC has current HP or conditions different from maximum or baseline values: the page distinguishes current state from durable maximum without rewriting the character sheet's identity.
- A source contains conflicting names, numbers, or spell lists: the page preserves the conflict or marks the value for verification; the agent does not silently choose an invented resolution.
- A referenced owner page is absent: use an explicit unresolved link or stated unknown according to existing wiki rules; do not invent an entity merely to fill a row.
- A PC has no current session change, art, or named connection: omit that optional section rather than leaving an empty heading.
- A source includes a legacy satellite page: treat it as source material and consolidate its facts into the live PC owner page or a named owner link without reproducing the satellite dump.
- A page contains a player handle: retain the handle needed by the DM, but do not add real-player identifying information.
- Columns cannot render in a particular Markdown viewer: heading order and readable tables remain sufficient to understand the page linearly.

## Requirements

### Functional Requirements

- **FR-001**: The system MUST provide one canonical `type: pc` template for player character owner pages under `wiki/entities/pc/`, with the repository's required frontmatter fields and PC-specific identity fields.
- **FR-002**: The PC template MUST define a stable, single-H1 section spine covering player-safe spoken look, At a Glance, Connections, Sheet, Combat Profile, Abilities, conditional Spells, Inventory, Session Log, Voice, and conditional Art; unused optional sections MUST be omitted from filed pages.
- **FR-003**: At a Glance MUST expose player, class and level, home ship or equivalent current base, and a concise DM thesis describing the PC's play pattern, party role, pressure, or decision-relevant weakness.
- **FR-004**: Sheet and Combat Profile MUST make the character's table-critical numbers and combat behavior scannable, including ability scores and modifiers, saves, skills, AC, HP, initiative, passive perception, speed, signature resources, counters, and party synergy when those facts exist.
- **FR-005**: Abilities MUST organize traits, features, actions, bonus actions, reactions, and feats into predictable subsections or omit unused subsections; each entry MUST state its effect and uses or recovery when applicable.
- **FR-006**: A caster's Spells section MUST distinguish spellcasting ability and calculations, cantrips, prepared or known spells, and slots or other casting resources; a non-caster MUST NOT receive an empty Spells section.
- **FR-007**: Inventory MUST distinguish attuned, carried, stowed, and currency information when present, and MUST link named item owners instead of duplicating their full descriptions.
- **FR-008**: Session Log MUST preserve concise, dated or session-numbered changes that affect current play; long-form historical source material MUST remain attributable without becoming a duplicate satellite dump.
- **FR-009**: Connections and Voice MUST give the DM named relationship links, table consequences, portrayal cues, and decision-relevant pressures in complete sentences; player-safe narration MUST remain free of secrets, DCs, unearned names, and DM thesis.
- **FR-010**: The template and applicable PC guidance MUST use the repository's supported Obsidian column codeblock syntax (`col` and `col-md`) for paired scan surfaces, keep narration callouts outside those fences, and preserve a readable linear order.
- **FR-011**: All PC pages MUST use Obsidian wikilinks for in-vault entities and MUST escape alias or embed-size pipes inside Markdown table cells so links remain valid single cells.
- **FR-012**: All PC pages MUST use complete-sentence prose for DM-facing content, the shared Title Case headings, inline-code formatting for DCs and dice, and the repository's callout meanings without introducing competing treatments for the same information.
- **FR-013**: Agents MUST be able to distinguish canonical owner-page facts, source evidence, unknowns, and player-safe narration from the template and governing instructions; the format MUST NOT require agents to infer meaning from visual placement alone.
- **FR-014**: The conformance pass MUST update Jean-Claude Tabarnack, Perrin Black-Jaw, Catarina Da'Virelli, Crissdalynn Khinriss, and Delmar Fisk to the redesigned contract while preserving their facts, source references, lifecycle, reveal, visibility, links, aliases, art, and player handles where present.
- **FR-015**: The conformance pass MUST consolidate facts from applicable PC satellite dumps into the canonical PC page or a clear owner-page link, and MUST NOT leave competing live PC representations that can be mistaken for the owner page.
- **FR-016**: Applicable creation and maintenance guidance MUST be updated to point to the canonical template and contract, including PC interview, wiki ingest, Obsidian Markdown, and the governing wiki authoring instructions; unrelated skills MUST NOT be restyled solely for this feature.
- **FR-017**: The feature MUST preserve existing campaign `type`, lifecycle, reveal, visibility, source, and approval rules; structural conformance MUST NOT silently promote, reject, invent, or alter campaign facts.
- **FR-018**: The redesigned template and conformed pages MUST be compatible with the existing wiki lint and link conventions, with no broken in-vault links, invalid required frontmatter, duplicate H1 facet dumps, or literal escaped newlines in prose bodies.

### Key Entities

- **PC owner page**: The canonical `type: pc` wiki page for one player character, containing DM-facing identity, portrayal, mechanical scan, relationships, inventory, and current session state.
- **PC template**: The copy-start scaffold that defines required frontmatter, canonical section homes, supported column syntax, player-safe narration, and omission rules for PC owner pages.
- **PC section spine**: The stable sequence of headings shared by complete PC pages so agents and DMs can predict where information lives.
- **DM thesis**: A short At a Glance statement describing the PC's table role, play pattern, pressure, or decision-relevant weakness.
- **Combat Profile**: A compact DM-facing interpretation of how the PC operates, including counters, dependencies, resources, and synergy; it does not replace the canonical Sheet numbers.
- **Source satellite**: An archived or imported PC facet such as a sheet, abilities, spells, inventory, gallery, or combat profile that supplies evidence but is not a second live owner page.
- **Conformance pass**: A structure-preserving rewrite that brings an existing PC page onto the PC template without changing its campaign facts or lifecycle.

## Success Criteria

### Measurable Outcomes

- **SC-001**: In a timed review, a DM can locate player, class and level, AC, current/max HP, initiative, signature combat options, a named connection, and voice for each of the five conformed PCs in under 60 seconds per page.
- **SC-002**: 100% of the five live PC owner pages share the required frontmatter contract, single-H1 rule, and section spine; 0% retain a competing live satellite dump as a second PC representation.
- **SC-003**: 100% of conformed PC pages preserve all previously supported facts or provide a clear owner-page link or explicit verification marker for each fact that cannot remain inline; no source list, alias, art embed, lifecycle, reveal, visibility, or player handle is silently lost.
- **SC-004**: A second agent can create or update a representative caster, non-caster, and multiclass PC from the template without asking where required facts belong, and all three outputs pass applicable wiki lint on the first review.
- **SC-005**: 100% of PC pages with a narration block can be read aloud to players without exposing a secret, DC, unearned name, or DM thesis; 100% of DM-only mechanics remain outside that narration block.
- **SC-006**: 100% of conditional PC sections are absent when their source contains no applicable content; no conformed page contains an empty optional heading or placeholder table.
- **SC-007**: In an Obsidian Reading view, the primary PC reference surfaces render as intended column pairs using the supported codeblock syntax, while the same page remains understandable in linear Markdown when column rendering is unavailable.
- **SC-008**: A maintainer tracing PC interview, ingest, and Markdown-formatting workflows finds one canonical PC template and no obsolete PC path or contradictory instruction in the applicable skills and governing wiki guidance.
- **SC-009**: In a DM usability review of the five conformed pages, at least four of five are rated usable as a reference during a live session without reformatting, and every reported failure maps to a concrete missing or ambiguous contract item.

## Assumptions

- The primary reader is the human DM using the existing Obsidian wiki; players make decisions and run their own characters, while the DM uses the page for reference, portrayal, and adjudication. Players receive only explicitly player-safe narration or other approved player-facing surfaces.
- `wiki/entities/pc/` remains the canonical depth-one location for live PC owner pages, and `type: pc` remains the existing campaign type.
- The existing `wiki/AGENTS.md`, `obsidian-markdown` skill, and current PC pages establish the baseline vocabulary and supported `col` / `col-md` syntax; this feature refines that contract rather than introducing a second PC format.
- The five named current PC pages are the conformance set for this feature. Historical archived material remains evidence and is not itself rewritten into a second live representation.
- Existing campaign approval rules remain binding: structural conformance may proceed without a new fact-approval cycle when facts and lifecycle are unchanged; newly invented or changed campaign facts remain DM-gated.
- Missing mechanics remain unknown or marked for verification. The feature does not require a new character-sheet import integration or a new database.
- Existing item, spell, place, faction, creature, ship, and party owner pages remain the owners of their own detailed facts; PC pages link to them and retain only the information needed for PC play.
- Column rendering depends on the currently supported Obsidian plugin/viewer behavior. The document's headings and tables remain the semantic fallback, so agents do not rely on columns alone to infer meaning.
- Real-player PII is out of scope; player fields contain only the handles already permitted by current wiki instructions.
