---

description: "Task list for the PC Page Redesign feature"
---

# Tasks: PC Page Redesign

**Input**: Design documents from `/specs/020-pc-page-redesign/`

**Prerequisites**: `plan.md`, `spec.md`, `research.md`, `data-model.md`, `contracts/pc-page.md`, and `quickstart.md`

**Tests**: No per-story TDD suite. The public seam is `specs/020-pc-page-redesign/fixtures/check.py` plus the scoped lint/manual checks in Polish. Independent acceptance scenarios live in `spec.md`.

**Organization**: Tasks are grouped by user story so each increment has a clear owner, dependency, and independent acceptance check.

**Writer**: `.agents/skills/player-characters/SKILL.md` (new) and `wiki/templates/pc.md` (rewrite) are design-impact. `/speckit.implement` dispatches the designated writer per `docs/agents/skill-design-dispatch.md` with a scoped prompt (outcome, files, bounds, job) and `writing-for-agents`. Session agent writes the fixture spine update, `wiki/AGENTS.md`, pointer edits, and the five owner pages. Session agent MUST NOT write the skill or template while a designated writer is usable.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no incomplete dependencies)
- **[Story]**: Which user story this task belongs to (US1–US4)
- Include exact file paths in descriptions

## Path Conventions

- New skill: `.agents/skills/player-characters/SKILL.md`
- Template: `wiki/templates/pc.md`
- Live owners: `wiki/entities/pc/{jean-claude-tabarnack,perrin-black-jaw,catarina-davirelli,crissdalynn-khinriss,delmar-fisk}.md`
- Governing wiki: `wiki/AGENTS.md`
- Pointers: `.agents/skills/npc-design/SKILL.md`, `.agents/skills/pc-interview/SKILL.md`, `.agents/skills/wiki-ingest/SKILL.md`, `.agents/skills/reconciling-session-evidence/SKILL.md`, `.agents/skills/obsidian-markdown/SKILL.md`, `.agents/skills/obsidian-markdown/references/COLUMNS.md`
- Contract: `specs/020-pc-page-redesign/contracts/pc-page.md`
- Fixture: `specs/020-pc-page-redesign/fixtures/check.py`
- Archive evidence: `wiki/_archive/` (immutable; not a second live PC page)
- Do not add a PDF parser, database, Foundry client, `pc-design` skill, extra `type`, or visual clone of D&D Beyond chrome

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Keep the existing argument-free feature checker; no new dependency or database.

- [X] T001 Create the argument-free feature checker entrypoint in `specs/020-pc-page-redesign/fixtures/check.py`, using Python 3 with text/JSON-compatible output and a done-vs-failed exit code

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Make the current page contract executable before template, skill, owner-page, or workflow edits.

**⚠️ CRITICAL**: No user story work begins until this phase is complete. The checker MUST fail on the current At a Glance / Sheet / Combat Profile / Abilities spine.

- [X] T002 Update observable PC contract assertions in `specs/020-pc-page-redesign/fixtures/check.py` for `wiki/templates/pc.md` and the five owners under `wiki/entities/pc/`: required frontmatter including `type` Exactly `pc`; one H1; player-safe `> [!narration] Narration`; D&D Beyond spine `Identity`, `Combat Stats`, `Ability Scores`, `Skills`, `Actions`, conditional `Spells`, `Inventory`, `Features`, `Connections`, `Session Log`, `Art`; forbid `Voice`, `At a Glance`, `Sheet`, `Combat Profile`, `Abilities`, and required DM thesis; two nested `col`/`col-md` pairs with headings inside child fences (`Identity`+`Combat Stats`, `Ability Scores`+`Skills`); parent fence longer than children; no `[!col]`; omit empty optional sections/subsections; Delmar Fisk omits…

**Checkpoint**: `specs/020-pc-page-redesign/fixtures/check.py` fails clearly on un-conformed template and pages, and can pass the completed five-page set.

---

## Phase 3: User Story 1 - Reference any PC from one page (Priority: P1) 🎯 MVP

**Goal**: One predictable, player-safe, D&D Beyond-ordered PC scaffold the DM can scan for identity, combat numbers, options, inventory, and connections without a satellite dump or prescribed play pattern.

**Independent Test**: Copy-start a scratch page from `wiki/templates/pc.md` and, without another page, locate player, class/level, AC, current/max HP, initiative, Actions, and Connections in D&D Beyond order in under 60 seconds. Confirm no `Voice` / `At a Glance` / `Sheet` / `Combat Profile` / `Abilities` / DM thesis.

### Implementation for User Story 1

- [ ] T003 [US1] Dispatch the designated writer per `docs/agents/skill-design-dispatch.md` to rewrite `wiki/templates/pc.md` against `specs/020-pc-page-redesign/contracts/pc-page.md`; instruct the writer to follow `.agents/skills/writing-for-agents`; session agent does not write that file. Outcome: copy-start scaffold with required frontmatter `title` ("Display name; may contain spaces/apostrophes."), `category` (`entities`), `tags` ("Existing campaign/type tags; preserve them."), `sources` ("All evidence supporting the page, including archived satellites and ingest sources; preserve lineage."), `created` / `updated`, `type` ("Exactly `pc`."), `lifecycle`, `reveal`, `campaign` / `visibility`, `summary` ("One concise DM-readable sentence. Not a prescribed play pattern."), `player` ("yes for a live PC"; "Player handle only; never real-player PII."), `class_levels` ("yes when known"; "Human-readable single- or multiclass levels."), `level`, `ac`, `hp_max`, `init_mod`, `pp` ("yes when known"; "Scalar identity/reference values. Unknown values remain explicit unknowns."), `speed` ("yes when known"; "Walk and conditional movement as a string."), `status` ("yes when known"; "Existing character status; do not infer a change."), optional `aliases`, `foundry_id`, `provenance`, `base_confidence`, `tier`, `lifecycle_changed` ("Preserve when present; omit when absent."); one H1; player-safe `[!narration]` outside fences; spine Identity, Combat Stats, Ability Scores, Skills, Actions (Attacks/Actions/Bonus Actions/Reactions; omit empty), conditional Spells (Spellcasting/Cantrips/Prepared or Known/Slots or Casting Resources; omit for a non-caster; keep multiclass pools distinct), Inventory (Attuned/Carried/Stowed/Currency; omit empty), Features (Traits/Class Features/Feats; omit empty), Connections, Session Log, Art; nested `col`/`col-md` pairs Identity+Combat Stats and Ability Scores+Skills; headings inside child fences; linear table fallback; Combat Stats is the human-readable authority for AC/current/max HP/initiative/passive perception/speed; lists record options and numbers and MUST NOT script the player's action; no Voice / At a Glance / Sheet / Combat Profile / Abilities / required DM thesis / D&D Beyond chrome

**Checkpoint**: A new PC copied from `wiki/templates/pc.md` is one D&D Beyond-ordered reference surface. The fixture still fails live owners until User Story 3.

---

## Phase 4: User Story 2 - Record predictable PC pages (Priority: P2)

**Goal**: Agents record player-created characters from supplied source through one PC-owning skill. They do not invent a PC, generate stats, prescribe actions, or route through npc-design.

**Independent Test**: Give an agent `.agents/skills/player-characters/SKILL.md`, `wiki/templates/pc.md`, `wiki/AGENTS.md`, `specs/020-pc-page-redesign/contracts/pc-page.md`, and a representative supplied source (PDF, prose, or Foundry actor). Confirm it transcribes a complete `type: pc` page with stable headings, valid frontmatter, correct wikilinks, no satellite dump, no invented stats, and no prescribed actions; with no source, or a request to invent/generate/prescribe, it refuses and does not mint a page.

### Implementation for User Story 2

- [ ] T004 [US2] Dispatch the designated writer per `docs/agents/skill-design-dispatch.md` to create `.agents/skills/player-characters/SKILL.md`; instruct the writer to follow `.agents/skills/writing-for-agents`; session agent does not write that file. Outcome: `player-characters` is the sole skill owner for `type: pc`; name is `player-characters` not `pc-design`; state idle → record ("source supplied for a player-created character") → refuse ("no source, or a request to invent/generate/prescribe"); MAY file `wiki/entities/pc/<kebab-slug>.md` by transcribing supplied source only; MUST accept PDF character sheets, prose descriptions, Foundry VTT via existing MCP (`get-character`, `list-characters`, `get-character-entity`, related character tools), and other DM-supplied files; no new PDF parser/database/Foundry client; unreadable source leaves fields unknown or `[verify]` and MUST NOT invent stats or abort a usable partial page when some source remains; "When a newer supplied source disagrees with the live wiki page on the same number, the PC-owning skill MUST keep the newer source's value and overwrite the wiki number" including matching frontmatter mirrors; structure-only conformance is not a newer source; one source that internally disagrees keeps both values or `[verify]`; point at `wiki/templates/pc.md`, `wiki/AGENTS.md`, `obsidian-markdown`, and `specs/020-pc-page-redesign/contracts/pc-page.md` rather than cloning the contract; MUST NOT invent a PC, generate stats, or write the player's actions

- [ ] T005 [P] [US2] Update `.agents/skills/npc-design/SKILL.md` so player-character builds are a hard stop that routes to `player-characters`; npc-design MUST NOT create, rewrite, or prescribe `type: pc` pages

- [ ] T006 [P] [US2] Update the PC layout row and add wiki-kind routing in `wiki/AGENTS.md`: live owner `wiki/entities/pc/` with `type: pc`; copy `wiki/templates/pc.md`; jobs are the D&D Beyond spine (Identity, Combat Stats, Ability Scores, Skills, Actions, conditional Spells, Inventory, Features, Connections, Session Log, Art); no Voice / At a Glance / Sheet / Combat Profile / Abilities / required DM thesis; player controls the PC; omit empty optional sections; flatten satellites; structure-only conformance does not change `lifecycle` / `reveal` / `visibility` / campaign facts; wiki-kind route "Write, edit, or create a named PC page" → `player-characters`

**Checkpoint**: The skill, template, npc-design exclusion, and governing wiki instructions tell an agent how to record a PC from source and when to refuse.

---

## Phase 5: User Story 3 - Conform the current party without losing canon (Priority: P3)

**Goal**: Bring the five live PC owners onto the redesigned contract while preserving campaign facts, source lineage, links, aliases, art, lifecycle, reveal, visibility, campaign, and player handles.

**Independent Test**: Compare each conformed owner with its pre-change page and applicable `wiki/_archive/` satellites. Confirm the shared spine, every previously supported fact is inline or an owner link or `[verify]`, no competing live satellite dump, and no changed campaign state.

### Implementation for User Story 3

- [ ] T007 [P] [US3] Conform `wiki/entities/pc/jean-claude-tabarnack.md` to `wiki/templates/pc.md` and `specs/020-pc-page-redesign/contracts/pc-page.md`: flatten applicable archive facts into canonical homes; preserve `tags`, `sources` lineage, `lifecycle` ("Existing value; structure-only conformance does not change it."), `reveal` ("Existing value; structure-only conformance does not change it."), `campaign` / `visibility`, aliases, art, player handle ("Player handle only; never real-player PII."), and `status` ("Existing character status; do not infer a change."); do not overwrite numbers (structure-only is not a newer source); mark one-source disagreements `[verify]` with the source; omit empty optional sections; keep multiclass/resource pools distinct

- [ ] T008 [P] [US3] Conform `wiki/entities/pc/perrin-black-jaw.md` to `wiki/templates/pc.md` and `specs/020-pc-page-redesign/contracts/pc-page.md` with the same preservation, flattening, `[verify]`, and omission rules as T007

- [ ] T009 [P] [US3] Conform `wiki/entities/pc/catarina-davirelli.md` to `wiki/templates/pc.md` and `specs/020-pc-page-redesign/contracts/pc-page.md` with the same preservation, flattening, `[verify]`, and omission rules as T007; keep caster pools in `Spells` without duplicating Combat Stats numbers

- [ ] T010 [P] [US3] Conform `wiki/entities/pc/crissdalynn-khinriss.md` to `wiki/templates/pc.md` and `specs/020-pc-page-redesign/contracts/pc-page.md` with the same preservation, flattening, `[verify]`, and omission rules as T007

- [ ] T011 [P] [US3] Conform `wiki/entities/pc/delmar-fisk.md` to `wiki/templates/pc.md` and `specs/020-pc-page-redesign/contracts/pc-page.md` with the same preservation, flattening, `[verify]`, and omission rules as T007; omit the entire `Spells` section (non-caster)

**Checkpoint**: All five live owners share the contract, retain canon, and contain no second live PC facet representation.

---

## Phase 6: User Story 4 - Maintain the standard across PC workflows (Priority: P4)

**Goal**: Interview, ingest, reconciliation, and Markdown guidance point at one PC contract and `player-characters`. They do not reintroduce satellite dumps, invalid columns, competing headings, or NPC treatment of PCs.

**Independent Test**: Trace `.agents/skills/player-characters/SKILL.md`, `.agents/skills/pc-interview/SKILL.md`, `.agents/skills/wiki-ingest/SKILL.md`, `.agents/skills/reconciling-session-evidence/SKILL.md`, `.agents/skills/obsidian-markdown/SKILL.md`, `.agents/skills/obsidian-markdown/references/COLUMNS.md`, `.agents/skills/npc-design/SKILL.md`, and `wiki/AGENTS.md`. Confirm one template, one skill owner, no npc-design PC path, and the same frontmatter/section/column/omission rules.

### Implementation for User Story 4

- [ ] T012 [P] [US4] Update `.agents/skills/pc-interview/SKILL.md` to map stated answers into D&D Beyond sections on `wiki/templates/pc.md` at `wiki/entities/pc/`; route page writes through `player-characters`; treat the interview transcript as evidence, not a live facet; leave unknown mechanics unknown; never invent combat math or player choices

- [ ] T013 [P] [US4] Update `.agents/skills/wiki-ingest/SKILL.md` so `type: pc` ingest points at `player-characters` and `wiki/templates/pc.md`, files `wiki/entities/pc/<kebab-slug>.md`, flattens archived satellites, preserves `sources` lineage, and keeps conflicts/unknowns explicit without duplicating `specs/020-pc-page-redesign/contracts/pc-page.md`

- [ ] T014 [P] [US4] Update `.agents/skills/reconciling-session-evidence/SKILL.md` to route durable PC changes through `player-characters` into canonical owner sections, preserve `lifecycle` / `reveal` / `visibility`, and avoid satellite dumps or invented conflict resolutions

- [ ] T015 [P] [US4] Update `.agents/skills/obsidian-markdown/SKILL.md` so the campaign `type` enum includes `pc`; keep wikilink and escaped-pipe (`\|`) table-cell rules, complete-sentence DM prose, player-safe narration, inline-code DC/dice, real newlines, and omission rules; add the PC column exception without weakening the session/run rule that narration stays outside fences

- [ ] T016 [P] [US4] Update `.agents/skills/obsidian-markdown/references/COLUMNS.md` with the PC-only nested `col`/`col-md` pairs (Identity+Combat Stats, Ability Scores+Skills), longer parent fence, headings/tables as linear fallback, narration outside fences, and prohibition on `[!col]` for those PC pairs; Connections+Session Log MAY use the same pattern when both exist; Actions/Spells/Inventory/Features/Art stay full-width

**Checkpoint**: PC interview, ingest, reconciliation, and Markdown workflows converge on the same template and skill and do not reintroduce obsolete paths.

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Prove the quickstart: fixture, lint, routing, Reading view, preservation, representative recording, and refuse-to-generate.

- [ ] T017 Run `.venv/bin/python specs/020-pc-page-redesign/fixtures/check.py` against `wiki/templates/pc.md`, `wiki/entities/pc/`, and applicable `wiki/_archive/` satellites; require exit `0`
- [ ] T018 [P] Run `./scripts/lint-wiki-write --path wiki/entities/pc` against all five conformed owners; require exit `0`
- [ ] T019 [P] Run `./scripts/lint-obsidian-markdown --strict --path wiki/entities/pc` against all five conformed owners; require exit `0`
- [ ] T020 Run `./scripts/wiki-lint --json` and confirm no HARD findings for PC paths, frontmatter, links, filenames, or duplicate H1/facet structure; do not use `tools/check_wiki_pages.py` as PC proof
- [ ] T021 Perform an Obsidian Reading-view review of `wiki/entities/pc/jean-claude-tabarnack.md`, `wiki/entities/pc/perrin-black-jaw.md`, `wiki/entities/pc/catarina-davirelli.md`, `wiki/entities/pc/crissdalynn-khinriss.md`, and `wiki/entities/pc/delmar-fisk.md`: full-width player-safe narration, paired Identity/Combat Stats and Ability Scores/Skills, linear fallback, no Voice / At a Glance / Sheet / Combat Profile / Abilities / empty optional heading / second H1 / required DM thesis / live satellite dump
- [ ] T022 Perform the timed DM-reference review (under 60 seconds per page for player, class/level, AC, current/max HP, initiative, signature options, a named connection, and a decision-relevant pressure) and the structure-only preservation comparison of `wiki/entities/pc/` against pre-change copies and `wiki/_archive/{abilities,character-sheets,combat-profile,galleries,inventory,session-logs,spells,stats,va-scripts}/`
- [ ] T023 Using only `player-characters`, `wiki/templates/pc.md`, `specs/020-pc-page-redesign/contracts/pc-page.md`, and representative supplied source, produce temporary scratch outputs for a caster with multiple casting pools, a non-caster with no `Spells` section, and a multiclass PC with distinct class/resource pools; each must omit empty sections, leave unknowns uninvented, keep narration safe, and pass scoped lint before scratch files are removed
- [ ] T024 Confirm the negative: with no supplied source, or a request to invent a PC / generate stats / write the character's actions, `.agents/skills/player-characters/SKILL.md` refuses and does not mint a page

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: T001 already landed the checker entrypoint
- **Foundational (Phase 2)**: T002 depends on T001 and BLOCKS all user stories
- **User Story 1 (Phase 3)**: Depends on T002; designated-writer template rewrite
- **User Story 2 (Phase 4)**: Depends on User Story 1 so the skill can point at the redesigned template
- **User Story 3 (Phase 5)**: Depends on User Stories 1 and 2; owner conformance uses the final template, skill, and `wiki/AGENTS.md` rules
- **User Story 4 (Phase 6)**: Depends on User Story 2; pointer files are independent of one another and can run alongside User Story 3
- **Polish (Phase 7)**: Depends on all desired story work; T017 before treating the page contract as complete

### User Story Dependencies

- **User Story 1 (P1)**: After Foundational only. MVP template increment
- **User Story 2 (P2)**: After User Story 1. Skill + npc-design exclusion + wiki-kind routing
- **User Story 3 (P3)**: After User Stories 1 and 2. Each owner file is independent after the contract is fixed
- **User Story 4 (P4)**: After User Story 2. Workflow files are independent of one another and of US3

### Within Each User Story

- User Story 1: one designated-writer rewrite of `wiki/templates/pc.md`
- User Story 2: designated-writer skill, then session-agent pointers in `npc-design` and `wiki/AGENTS.md`
- User Story 3: preserve each owner's metadata and facts before flattening satellites; then validate each owner against the checker
- User Story 4: point each workflow at the canonical contract; do not copy the contract into every skill

### Parallel Opportunities

- T005 and T006 after T004 (different files)
- T007–T011 after User Stories 1–2 (five owner files)
- T012–T016 after User Story 2 (five guidance files)
- User Story 3 and User Story 4 in parallel after User Story 2, one writer per file
- T018 and T019 after source edits; T017 before claiming the contract complete

---

## Parallel Example: User Story 2 pointers

```text
Task: "Hard-route player-character builds from .agents/skills/npc-design/SKILL.md to player-characters"
Task: "Update PC layout row and wiki-kind routing in wiki/AGENTS.md"
```

## Parallel Example: User Story 3

```text
Task: "Conform wiki/entities/pc/jean-claude-tabarnack.md"
Task: "Conform wiki/entities/pc/perrin-black-jaw.md"
Task: "Conform wiki/entities/pc/catarina-davirelli.md"
Task: "Conform wiki/entities/pc/crissdalynn-khinriss.md"
Task: "Conform wiki/entities/pc/delmar-fisk.md"
```

## Parallel Example: User Story 4

```text
Task: "Update .agents/skills/pc-interview/SKILL.md"
Task: "Update .agents/skills/wiki-ingest/SKILL.md"
Task: "Update .agents/skills/reconciling-session-evidence/SKILL.md"
Task: "Update .agents/skills/obsidian-markdown/SKILL.md"
Task: "Update .agents/skills/obsidian-markdown/references/COLUMNS.md"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational checker (must fail on the old spine)
3. Complete Phase 3: User Story 1 template rewrite (designated writer)
4. Stop and inspect `wiki/templates/pc.md` against the Independent Test
5. Do not claim live-party conformance until User Story 3

### Incremental Delivery

1. Setup + Foundational → executable D&D Beyond contract
2. Add User Story 1 → canonical template MVP
3. Add User Story 2 → record-only skill, npc-design exclusion, wiki-kind routing
4. Add User Story 3 → five live owners conformed without canon loss
5. Add User Story 4 → interview/ingest/reconcile/Markdown converge
6. Run Phase 7 → fixture, lint, schema, Reading-view, timed-reference, recording, refuse-to-generate

### Dispatch

- T003: designated writer only. Target `wiki/templates/pc.md`. Session agent writes the scoped prompt, leaves the template unmodified, then invokes `claude -p --model claude-opus-4-6 --effort medium`
- T004: designated writer only. Target `.agents/skills/player-characters/SKILL.md`. Same dispatch. Do not overlap T003 and T004 on the same writer instance if they would share a workspace
- T005–T016 and T002: session agent
- On usage-limit wait: leave T003/T004 incomplete on this file with a retry time; complete independent session-agent tasks that do not depend on them; do not write the skill or template in-session unless both designated writers are usage-limited

---

## Notes

- `[P]` marks tasks that touch different files and have no incomplete dependency
- `[US#]` labels map implementation work to the prioritized stories in `spec.md`
- Data-model constraints are quoted in T002–T004 and T007–T011
- Structure-only conformance preserves facts and campaign state; a newer supplied source overwrites conflicting wiki numbers; unresolved internal conflicts stay `[verify]`
- Existing Markdown, lint, Obsidian Columns, Python 3, and Foundry MCP stay in place; no new parser, database, or `pc-design` skill
- Stop at any checkpoint to validate the story independently
