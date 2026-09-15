---

description: "Task list for the PC Page Redesign feature"
---

# Tasks: PC Page Redesign

**Input**: Design documents from `/specs/020-pc-page-redesign/`

**Prerequisites**: `plan.md`, `spec.md`, `research.md`, `data-model.md`, `contracts/pc-page.md`, and `quickstart.md`

**Tests**: No per-story TDD suite. The public seam is `specs/020-pc-page-redesign/fixtures/check.py` plus the scoped lint/manual checks in Polish. Independent acceptance scenarios live in `spec.md`.

**Organization**: Tasks are grouped by user story so each increment has a clear owner, dependency, and independent acceptance check.

**Writer**: Remaining design-impact work is the template and skill follow-through for FR-021–023: `wiki/templates/pc.md` and `.agents/skills/player-characters/SKILL.md`. `/speckit.implement` dispatches the designated writer per `docs/agents/skill-design-dispatch.md` with a scoped prompt (outcome, files, bounds, job) and `writing-for-agents`. Session agent writes the fixture update, CSS snippet, `wiki/AGENTS.md`, pointer edits, and the five owner reconforms. Session agent MUST NOT write the skill or template while a designated writer is usable. T001–T024 already landed the first-pass D&D Beyond sheet.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no incomplete dependencies)
- **[Story]**: Which user story this task belongs to (US1–US4)
- Include exact file paths in descriptions

## Path Conventions

- New skill: `.agents/skills/player-characters/SKILL.md`
- Template: `wiki/templates/pc.md`
- Live owners: `wiki/entities/pc/{jean-claude-tabarnack,perrin-black-jaw,catarina-davirelli,crissdalynn-khinriss,delmar-fisk}.md`
- Governing wiki: `wiki/AGENTS.md`
- Pointers: `.agents/skills/npc-design/SKILL.md`, `.agents/skills/pc-interview/SKILL.md`, `.agents/skills/wiki-ingest/SKILL.md`, `.agents/skills/reconciling-session-evidence/SKILL.md`, `.agents/skills/obsidian-markdown/SKILL.md`, `.agents/skills/obsidian-markdown/references/COLUMNS.md`, `.agents/skills/session-beats/SKILL.md`, `.agents/skills/run-guide/SKILL.md`
- Contract: `specs/020-pc-page-redesign/contracts/pc-page.md`
- Fixture: `specs/020-pc-page-redesign/fixtures/check.py`
- CSS: `wiki/.obsidian/snippets/ttrpg-styles.css`, `wiki/.obsidian/snippets/wide-note-surface.css`, `wiki/.obsidian/snippets/pc-sheet.css`
- Archive evidence: `wiki/_archive/` (immutable; not a second live PC page)
- Do not add a PDF parser, database, Foundry client, `pc-design` skill, extra `type`, decorative PC theme, or visual clone of D&D Beyond chrome

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

- [X] T003 [US1] Dispatch the designated writer per `docs/agents/skill-design-dispatch.md` to rewrite `wiki/templates/pc.md` against `specs/020-pc-page-redesign/contracts/pc-page.md`; instruct the writer to follow `.agents/skills/writing-for-agents`; session agent does not write that file. Outcome: copy-start scaffold with required frontmatter `title` ("Display name; may contain spaces/apostrophes."), `category` (`entities`), `tags` ("Existing campaign/type tags; preserve them."), `sources` ("All evidence supporting the page, including archived satellites and ingest sources; preserve lineage."), `created` / `updated`, `type` ("Exactly `pc`."), `lifecycle`, `reveal`, `campaign` / `visibility`, `summary` ("One concise DM-readable sentence. Not a prescribed pla…

**Checkpoint**: A new PC copied from `wiki/templates/pc.md` is one D&D Beyond-ordered reference surface. The fixture still fails live owners until User Story 3.

---

## Phase 4: User Story 2 - Record predictable PC pages (Priority: P2)

**Goal**: Agents record player-created characters from supplied source through one PC-owning skill. They do not invent a PC, generate stats, prescribe actions, or route through npc-design.

**Independent Test**: Give an agent `.agents/skills/player-characters/SKILL.md`, `wiki/templates/pc.md`, `wiki/AGENTS.md`, `specs/020-pc-page-redesign/contracts/pc-page.md`, and a representative supplied source (PDF, prose, or Foundry actor). Confirm it transcribes a complete `type: pc` page with stable headings, valid frontmatter, correct wikilinks, no satellite dump, no invented stats, and no prescribed actions; with no source, or a request to invent/generate/prescribe, it refuses and does not mint a page.

### Implementation for User Story 2

- [X] T004 [US2] Dispatch the designated writer per `docs/agents/skill-design-dispatch.md` to create `.agents/skills/player-characters/SKILL.md`; instruct the writer to follow `.agents/skills/writing-for-agents`; session agent does not write that file. Outcome: `player-characters` is the sole skill owner for `type: pc`; name is `player-characters` not `pc-design`; state idle → record ("source supplied for a player-created character") → refuse ("no source, or a request to invent/generate/prescribe"); MAY file `wiki/entities/pc/<kebab-slug>.md` by transcribing supplied source only; MUST accept PDF character sheets, prose descriptions, Foundry VTT via existing MCP (`get-character`, `list-characters`, `get-character-entity`, related character tools), and other D…

- [X] T005 [P] [US2] Update `.agents/skills/npc-design/SKILL.md` so player-character builds are a hard stop that routes to `player-characters`; npc-design MUST NOT create, rewrite, or prescribe `type: pc` pages

- [X] T006 [P] [US2] Update the PC layout row and add wiki-kind routing in `wiki/AGENTS.md`: live owner `wiki/entities/pc/` with `type: pc`; copy `wiki/templates/pc.md`; jobs are the D&D Beyond spine (Identity, Combat Stats, Ability Scores, Skills, Actions, conditional Spells, Inventory, Features, Connections, Session Log, Art); no Voice / At a Glance / Sheet / Combat Profile / Abilities / required DM thesis; player controls the PC; omit empty optional sections; flatten satellites; structure-only conformance does not change `lifecycle` / `reveal` / `visibility` / campaign facts; wiki-kind route "Write, edit, or create a named PC page" → `player-characters`

**Checkpoint**: The skill, template, npc-design exclusion, and governing wiki instructions tell an agent how to record a PC from source and when to refuse.

---

## Phase 5: User Story 3 - Conform the current party without losing canon (Priority: P3)

**Goal**: Bring the five live PC owners onto the redesigned contract while preserving campaign facts, source lineage, links, aliases, art, lifecycle, reveal, visibility, campaign, and player handles.

**Independent Test**: Compare each conformed owner with its pre-change page and applicable `wiki/_archive/` satellites. Confirm the shared spine, every previously supported fact is inline or an owner link or `[verify]`, no competing live satellite dump, and no changed campaign state.

### Implementation for User Story 3

- [X] T007 [P] [US3] Conform `wiki/entities/pc/jean-claude-tabarnack.md` to `wiki/templates/pc.md` and `specs/020-pc-page-redesign/contracts/pc-page.md`: flatten applicable archive facts into canonical homes; preserve `tags`, `sources` lineage, `lifecycle` ("Existing value; structure-only conformance does not change it."), `reveal` ("Existing value; structure-only conformance does not change it."), `campaign` / `visibility`, aliases, art, player handle ("Player handle only; never real-player PII."), and `status` ("Existing character status; do not infer a change."); do not overwrite numbers (structure-only is not a newer source); mark one-source disagreements `[verify]` with the source; omit empty optional sections; keep multiclass/resource pools distinct

- [X] T008 [P] [US3] Conform `wiki/entities/pc/perrin-black-jaw.md` to `wiki/templates/pc.md` and `specs/020-pc-page-redesign/contracts/pc-page.md` with the same preservation, flattening, `[verify]`, and omission rules as T007

- [X] T009 [P] [US3] Conform `wiki/entities/pc/catarina-davirelli.md` to `wiki/templates/pc.md` and `specs/020-pc-page-redesign/contracts/pc-page.md` with the same preservation, flattening, `[verify]`, and omission rules as T007; keep caster pools in `Spells` without duplicating Combat Stats numbers

- [X] T010 [P] [US3] Conform `wiki/entities/pc/crissdalynn-khinriss.md` to `wiki/templates/pc.md` and `specs/020-pc-page-redesign/contracts/pc-page.md` with the same preservation, flattening, `[verify]`, and omission rules as T007

- [X] T011 [P] [US3] Conform `wiki/entities/pc/delmar-fisk.md` to `wiki/templates/pc.md` and `specs/020-pc-page-redesign/contracts/pc-page.md` with the same preservation, flattening, `[verify]`, and omission rules as T007; omit the entire `Spells` section (non-caster)

**Checkpoint**: All five live owners share the contract, retain canon, and contain no second live PC facet representation.

---

## Phase 6: User Story 4 - Maintain the standard across PC workflows (Priority: P4)

**Goal**: Interview, ingest, reconciliation, and Markdown guidance point at one PC contract and `player-characters`. They do not reintroduce satellite dumps, invalid columns, competing headings, or NPC treatment of PCs.

**Independent Test**: Trace `.agents/skills/player-characters/SKILL.md`, `.agents/skills/pc-interview/SKILL.md`, `.agents/skills/wiki-ingest/SKILL.md`, `.agents/skills/reconciling-session-evidence/SKILL.md`, `.agents/skills/obsidian-markdown/SKILL.md`, `.agents/skills/obsidian-markdown/references/COLUMNS.md`, `.agents/skills/npc-design/SKILL.md`, and `wiki/AGENTS.md`. Confirm one template, one skill owner, no npc-design PC path, and the same frontmatter/section/column/omission rules.

### Implementation for User Story 4

- [X] T012 [P] [US4] Update `.agents/skills/pc-interview/SKILL.md` to map stated answers into D&D Beyond sections on `wiki/templates/pc.md` at `wiki/entities/pc/`; route page writes through `player-characters`; treat the interview transcript as evidence, not a live facet; leave unknown mechanics unknown; never invent combat math or player choices

- [X] T013 [P] [US4] Update `.agents/skills/wiki-ingest/SKILL.md` so `type: pc` ingest points at `player-characters` and `wiki/templates/pc.md`, files `wiki/entities/pc/<kebab-slug>.md`, flattens archived satellites, preserves `sources` lineage, and keeps conflicts/unknowns explicit without duplicating `specs/020-pc-page-redesign/contracts/pc-page.md`

- [X] T014 [P] [US4] Update `.agents/skills/reconciling-session-evidence/SKILL.md` to route durable PC changes through `player-characters` into canonical owner sections, preserve `lifecycle` / `reveal` / `visibility`, and avoid satellite dumps or invented conflict resolutions

- [X] T015 [P] [US4] Update `.agents/skills/obsidian-markdown/SKILL.md` so the campaign `type` enum includes `pc`; keep wikilink and escaped-pipe (`\|`) table-cell rules, complete-sentence DM prose, player-safe narration, inline-code DC/dice, real newlines, and omission rules; add the PC column exception without weakening the session/run rule that narration stays outside fences

- [X] T016 [P] [US4] Update `.agents/skills/obsidian-markdown/references/COLUMNS.md` with the PC-only nested `col`/`col-md` pairs (Identity+Combat Stats, Ability Scores+Skills), longer parent fence, headings/tables as linear fallback, narration outside fences, and prohibition on `[!col]` for those PC pairs; Connections+Session Log MAY use the same pattern when both exist; Actions/Spells/Inventory/Features/Art stay full-width

**Checkpoint**: PC interview, ingest, reconciliation, and Markdown workflows converge on the same template and skill and do not reintroduce obsolete paths.

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Prove the quickstart: fixture, lint, routing, Reading view, preservation, representative recording, and refuse-to-generate.

- [X] T017 Run `.venv/bin/python specs/020-pc-page-redesign/fixtures/check.py` against `wiki/templates/pc.md`, `wiki/entities/pc/`, and applicable `wiki/_archive/` satellites; require exit `0`
- [X] T018 [P] Run `./scripts/lint-wiki-write --path wiki/entities/pc` against all five conformed owners; require exit `0`
- [X] T019 [P] Run `./scripts/lint-obsidian-markdown --strict --path wiki/entities/pc` against all five conformed owners; require exit `0`
- [X] T020 Run `./scripts/wiki-lint --json` and confirm no HARD findings for PC paths, frontmatter, links, filenames, or duplicate H1/facet structure; do not use `tools/check_wiki_pages.py` as PC proof
- [X] T021 Perform an Obsidian Reading-view review of `wiki/entities/pc/jean-claude-tabarnack.md`, `wiki/entities/pc/perrin-black-jaw.md`, `wiki/entities/pc/catarina-davirelli.md`, `wiki/entities/pc/crissdalynn-khinriss.md`, and `wiki/entities/pc/delmar-fisk.md`: full-width player-safe narration, paired Identity/Combat Stats and Ability Scores/Skills, linear fallback, no Voice / At a Glance / Sheet / Combat Profile / Abilities / empty optional heading / second H1 / required DM thesis / live satellite dump
- [X] T022 Perform the timed DM-reference review (under 60 seconds per page for player, class/level, AC, current/max HP, initiative, signature options, a named connection, and a decision-relevant pressure) and the structure-only preservation comparison of `wiki/entities/pc/` against pre-change copies and `wiki/_archive/{abilities,character-sheets,combat-profile,galleries,inventory,session-logs,spells,stats,va-scripts}/`
- [X] T023 Using only `player-characters`, `wiki/templates/pc.md`, `specs/020-pc-page-redesign/contracts/pc-page.md`, and representative supplied source, produce temporary scratch outputs for a caster with multiple casting pools, a non-caster with no `Spells` section, and a multiclass PC with distinct class/resource pools; each must omit empty sections, leave unknowns uninvented, keep narration safe, and pass scoped lint before scratch files are removed
- [X] T024 Confirm the negative: with no supplied source, or a request to invent a PC / generate stats / write the character's actions, `.agents/skills/player-characters/SKILL.md` refuses and does not mint a page

---

## Phase 8: Foundational update (FR-021–023)

**Purpose**: Make the clarified contract executable. T001–T024 landed Identity+Combat Stats pairing. Remaining story work MUST NOT start until this fixture fails the old pair and requires portrait+Identity, optional Stated Goals, leftover `Art`, and `cssclasses` containing `pc-sheet`.

**⚠️ CRITICAL**: T025 BLOCKS T026–T038.

- [X] T025 Update observable PC contract assertions in `specs/020-pc-page-redesign/fixtures/check.py` for `wiki/templates/pc.md` and the five owners under `wiki/entities/pc/`: required frontmatter `cssclasses` ("Must include `pc-sheet` so PC-only CSS tweaks apply. Not a campaign fact."); D&D Beyond spine `Identity`, `Combat Stats`, `Ability Scores`, `Skills`, `Actions`, conditional `Spells`, `Inventory`, `Features`, `Connections`, conditional `Stated Goals`, `Session Log`, `Art`; featured portrait + `Identity` nested `col`/`col-md` pair when art exists (left child embed only, no extra H2; right child `## Identity`); `Identity` full-width when no pictures exist; no empty portrait column; `Combat Stats` full-width after Identity; forbid pairing `Identity` with…

**Checkpoint**: `specs/020-pc-page-redesign/fixtures/check.py` fails on the current Identity+Combat Stats pair and on missing `pc-sheet` cssclass.

---

## Phase 9: User Story 1 follow-through - scan surface (Priority: P1)

**Goal**: Template and vault CSS match the locked header: featured portrait beside Identity, Combat Stats full-width, PC-page scan tweaks without a decorative theme.

**Independent Test**: Copy-start from `wiki/templates/pc.md`. With a sample portrait embed, the portrait sits beside Identity and Combat Stats is below. With no art, Identity is full-width. Vault CSS still applies; `.pc-sheet` tweaks exist without cards or D&D Beyond chrome.

### Implementation for User Story 1 follow-through

- [X] T026 [US1] Dispatch the designated writer per `docs/agents/skill-design-dispatch.md` to rewrite `wiki/templates/pc.md` against `specs/020-pc-page-redesign/contracts/pc-page.md`; instruct the writer to follow `.agents/skills/writing-for-agents`; session agent does not write that file. Outcome: frontmatter includes `cssclasses` ("Must include `pc-sheet` so PC-only CSS tweaks apply. Not a campaign fact."); after `[!narration]`, featured portrait + `## Identity` pair when art exists; `## Combat Stats` full-width; `Ability Scores`+`Skills` pair unchanged; campaign extras `Connections`, conditional `Stated Goals`, `Session Log`, leftover `Art`; omit empty optional sections; no Identity+Combat Stats pair; no decorative chrome
- [X] T027 [P] [US1] Using `.agents/skills/obsidian-layout-adjustment/SKILL.md`, add PC-page scan tweaks in `wiki/.obsidian/snippets/pc-sheet.css` scoped to `.pc-sheet` (featured-portrait size, Identity/Ability column widths, heading density); keep vault-wide defaults in `wiki/.obsidian/snippets/ttrpg-styles.css` and `wiki/.obsidian/snippets/wide-note-surface.css`; MUST NOT add a distinct decorative theme, cards, site colors, or D&D Beyond chrome

**Checkpoint**: The template is the clarified scan surface. Live owners still fail the fixture until Phase 11.

---

## Phase 10: User Story 2 follow-through - record art and goals (Priority: P2)

**Goal**: `player-characters` records featured portrait / leftover art and transcript-only Stated Goals, and refreshes goals after sessions that included that player.

**Independent Test**: With a transcript where the player stated a goal in or out of character, the skill adds `## Stated Goals` citing that session and does not add summary-only or inferred goals. After a session that did not include the player, Stated Goals is unchanged. Art: one picture is the featured portrait; leftovers only in `## Art`.

### Implementation for User Story 2 follow-through

- [X] T028 [US2] Dispatch the designated writer per `docs/agents/skill-design-dispatch.md` to update `.agents/skills/player-characters/SKILL.md`; instruct the writer to follow `.agents/skills/writing-for-agents`; session agent does not write that file. Outcome: point at `specs/020-pc-page-redesign/contracts/pc-page.md` instead of cloning it; state idle → record ("source supplied for a player-created character") → refresh-goals ("post-session transcript for a player who was in that session") → refuse ("no source, or a request to invent/generate/prescribe, or inventing goals"); featured portrait + Identity when pictures exist; additional pictures MAY sit next to the section they illustrate; leftover pictures only in `## Art`; Stated Goals lists only goals the …
- [X] T029 [P] [US2] Update the PC layout row in `wiki/AGENTS.md`: spine is featured portrait + Identity when art exists, Combat Stats full-width, Ability Scores, Skills, Actions, conditional Spells, Inventory, Features, Connections, conditional Stated Goals, Session Log, leftover Art; `cssclasses` must include `pc-sheet`; wiki-kind route remains `player-characters`

**Checkpoint**: The skill and wiki-kind row describe art placement and transcript-only Stated Goals refresh.

---

## Phase 11: User Story 3 follow-through - conform live owners (Priority: P3)

**Goal**: Five live PC owners use the clarified spine, `cssclasses` containing `pc-sheet`, featured portrait when art exists, leftover `Art` only, and transcript-only Stated Goals (omit when none), without changing campaign facts.

**Independent Test**: Each owner has `cssclasses` including `pc-sheet`. If the page has pictures, one featured portrait is paired with Identity and leftovers are only in `## Art` (omit `Art` when none remain). `## Stated Goals` is present only for transcript-supported player statements. Structure-only pass does not overwrite numbers or lifecycle.

### Implementation for User Story 3 follow-through

- [X] T030 [P] [US3] Reconform `wiki/entities/pc/jean-claude-tabarnack.md` to `wiki/templates/pc.md` and `specs/020-pc-page-redesign/contracts/pc-page.md`: set `cssclasses` ("Must include `pc-sheet` so PC-only CSS tweaks apply. Not a campaign fact."); pair one featured portrait with Identity when pictures exist; leftover pictures only in `## Art`; add `## Stated Goals` only for transcript-supported player statements (in or out of character) citing session; omit Stated Goals and Art when empty; preserve `lifecycle` ("Existing value; structure-only conformance does not change it."), `reveal` ("Existing value; structure-only conformance does not change it."), `campaign` / `visibility`, aliases, sources, player handle ("Player handle only; never real-player PII.…
- [X] T031 [P] [US3] Reconform `wiki/entities/pc/perrin-black-jaw.md` to `wiki/templates/pc.md` and `specs/020-pc-page-redesign/contracts/pc-page.md` with the same `cssclasses`, portrait/Art, Stated Goals, preservation, and omission rules as T030
- [X] T032 [P] [US3] Reconform `wiki/entities/pc/catarina-davirelli.md` to `wiki/templates/pc.md` and `specs/020-pc-page-redesign/contracts/pc-page.md` with the same `cssclasses`, portrait/Art, Stated Goals, preservation, and omission rules as T030
- [X] T033 [P] [US3] Reconform `wiki/entities/pc/crissdalynn-khinriss.md` to `wiki/templates/pc.md` and `specs/020-pc-page-redesign/contracts/pc-page.md` with the same `cssclasses`, portrait/Art, Stated Goals, preservation, and omission rules as T030
- [X] T034 [P] [US3] Reconform `wiki/entities/pc/delmar-fisk.md` to `wiki/templates/pc.md` and `specs/020-pc-page-redesign/contracts/pc-page.md` with the same `cssclasses`, portrait/Art, Stated Goals, preservation, and omission rules as T030; keep `Spells` omitted (non-caster)

**Checkpoint**: All five live owners pass the clarified fixture assertions without canon loss.

---

## Phase 12: User Story 4 follow-through - workflows (Priority: P4)

**Goal**: Columns guidance, session evidence, and session planning agree on portrait+Identity, leftover Art, and transcript-only Stated Goals. Planning reads goals; it does not write the PC page.

**Independent Test**: Trace `.agents/skills/obsidian-markdown/references/COLUMNS.md`, `.agents/skills/reconciling-session-evidence/SKILL.md`, `.agents/skills/session-beats/SKILL.md`, and `.agents/skills/run-guide/SKILL.md`. Confirm portrait+Identity pair, no Identity+Combat Stats pair, Stated Goals refresh routed through `player-characters`, and planning reads Stated Goals when the player is in the session.

### Implementation for User Story 4 follow-through

- [X] T035 [P] [US4] Update `.agents/skills/obsidian-markdown/references/COLUMNS.md` with the PC-only nested `col`/`col-md` pairs (featured portrait+Identity when art exists, Ability Scores+Skills), Combat Stats full-width, longer parent fence, headings/tables as linear fallback, narration outside fences, prohibition on `[!col]` for those PC pairs, and full-width Connections / Stated Goals / Session Log / Art
- [X] T036 [P] [US4] Update `.agents/skills/reconciling-session-evidence/SKILL.md` so post-session Stated Goals refresh for PCs who were in that session routes through `player-characters`; do not invent goals; do not refresh a PC who was not in the session; preserve `lifecycle` / `reveal` / `visibility`
- [X] T037 [P] [US4] Update `.agents/skills/session-beats/SKILL.md` so session planning that includes a player MUST read that PC's `## Stated Goals` when present and MUST NOT write the PC owner page
- [X] T038 [P] [US4] Update `.agents/skills/run-guide/SKILL.md` so a run guide that includes a player MUST read that PC's `## Stated Goals` when present and MUST NOT write the PC owner page

**Checkpoint**: Columns, reconciliation, and planning converge on the clarified contract.

---

## Phase 13: Polish follow-through

**Purpose**: Re-run quickstart checks for the clarified contract.

- [X] T039 Run `.venv/bin/python specs/020-pc-page-redesign/fixtures/check.py` against `wiki/templates/pc.md` and `wiki/entities/pc/`; require exit `0`
- [X] T040 [P] Run `./scripts/lint-wiki-write --path wiki/entities/pc` against all five owners; require exit `0`
- [X] T041 [P] Run `./scripts/lint-obsidian-markdown --strict --path wiki/entities/pc` against all five owners; require exit `0`
- [X] T042 Confirm `wiki/.obsidian/snippets/pc-sheet.css` exists and is scoped to `.pc-sheet`, vault snippets `wiki/.obsidian/snippets/ttrpg-styles.css` and `wiki/.obsidian/snippets/wide-note-surface.css` remain, and each live PC has `cssclasses` containing `pc-sheet`
- [X] T043 Perform an Obsidian Reading-view review of the five owners: featured portrait beside Identity when art exists, Combat Stats full-width, Ability Scores/Skills paired, vault CSS plus PC scan tweaks without a decorative theme, Stated Goals only when transcript-supported, leftover Art only at the bottom
- [X] T044 Confirm the negatives in `.agents/skills/player-characters/SKILL.md`: no source / invent PC / generate stats / write actions / invent goals → refuse; summary-only goal is not filed; a session that did not include the player does not refresh that PC's Stated Goals


---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: T001 already landed the checker entrypoint
- **Foundational (Phase 2)**: T002 already landed; BLOCKED first-pass stories
- **User Stories 1–4 and Polish (Phases 3–7)**: T003–T024 already landed the first-pass D&D Beyond sheet
- **Foundational update (Phase 8)**: T025 depends on T001 and BLOCKS T026–T038
- **US1 follow-through (Phase 9)**: Depends on T025; T026 and T027 are different files
- **US2 follow-through (Phase 10)**: Depends on T026 so the skill can point at the clarified template
- **US3 follow-through (Phase 11)**: Depends on T026–T029; five owner files are independent
- **US4 follow-through (Phase 12)**: Depends on T028; T035–T038 are independent of one another and of US3
- **Polish follow-through (Phase 13)**: Depends on T026–T038; T039 before treating the clarified contract as complete

### User Story Dependencies

- **User Story 1 (P1)**: First-pass done. Follow-through after T025
- **User Story 2 (P2)**: Follow-through after US1 follow-through template
- **User Story 3 (P3)**: Follow-through after US1–US2 follow-through. Each owner file is independent
- **User Story 4 (P4)**: Follow-through after US2 follow-through. Workflow files are independent of US3

### Within Each User Story

- User Story 1 follow-through: designated-writer template, then CSS snippet on a different file
- User Story 2 follow-through: designated-writer skill, then `wiki/AGENTS.md`
- User Story 3 follow-through: preserve metadata; then portrait/Art/Stated Goals/`cssclasses`
- User Story 4 follow-through: point each workflow at the contract; do not copy the contract into every skill

### Parallel Opportunities

- T026 and T027 after T025 (template vs CSS snippet)
- T029 after T028 (`wiki/AGENTS.md`)
- T030–T034 after T026–T029 (five owner files)
- T035–T038 after T028 (four guidance files)
- T040 and T041 after source edits; T039 before claiming the clarified contract complete

---

## Parallel Example: User Story 3 follow-through

```text
Task: "Reconform wiki/entities/pc/jean-claude-tabarnack.md"
Task: "Reconform wiki/entities/pc/perrin-black-jaw.md"
Task: "Reconform wiki/entities/pc/catarina-davirelli.md"
Task: "Reconform wiki/entities/pc/crissdalynn-khinriss.md"
Task: "Reconform wiki/entities/pc/delmar-fisk.md"
```

## Parallel Example: User Story 4 follow-through

```text
Task: "Update .agents/skills/obsidian-markdown/references/COLUMNS.md"
Task: "Update .agents/skills/reconciling-session-evidence/SKILL.md"
Task: "Update .agents/skills/session-beats/SKILL.md"
Task: "Update .agents/skills/run-guide/SKILL.md"
```

---

## Implementation Strategy

### MVP remaining (User Story 1 follow-through)

1. Complete Phase 8: T025 fixture must fail the old Identity+Combat Stats pair
2. Complete Phase 9: T026 template (designated writer) and T027 `pc-sheet.css`
3. Stop and inspect `wiki/templates/pc.md` against the Independent Test
4. Do not claim live-party conformance until Phase 11

### Incremental Delivery

1. T001–T024 already delivered the first-pass sheet
2. T025 → executable clarified contract
3. T026–T027 → template + PC CSS
4. T028–T029 → skill + wiki-kind row
5. T030–T034 → five live owners
6. T035–T038 → columns, reconcile, planning reads
7. T039–T044 → fixture, lint, CSS files, Reading-view, refuse-to-invent-goals

### Dispatch

- T026: designated writer only. Target `wiki/templates/pc.md`. Session agent writes the scoped prompt, leaves the template unmodified, then invokes `claude -p --model claude-opus-4-6 --effort medium`
- T028: designated writer only. Target `.agents/skills/player-characters/SKILL.md`. Same dispatch. Do not overlap T026 and T028 on the same writer instance if they would share a workspace
- T025, T027, T029–T044: session agent
- On usage-limit wait: leave T026/T028 incomplete on this file with a retry time; complete independent session-agent tasks that do not depend on them; do not write the skill or template in-session unless both designated writers are usage-limited

---

## Notes

- `[P]` marks tasks that touch different files and have no incomplete dependency
- `[US#]` labels map implementation work to the prioritized stories in `spec.md`
- Data-model constraints are quoted in T025–T026 and T030–T034
- Structure-only conformance preserves facts and campaign state; a newer supplied source overwrites conflicting wiki numbers; unresolved internal conflicts stay `[verify]`
- Stated Goals are transcript-only; session summaries are backup; silence is not abandonment
- Existing Markdown, lint, Obsidian Columns, Python 3, Foundry MCP, and vault snippets stay in place; no new parser, database, `pc-design` skill, or decorative PC theme
- Stop at any checkpoint to validate the story independently

## Phase 14: Convergence

- [ ] T045 Update `.agents/skills/obsidian-markdown/SKILL.md` so PC column guidance names `player-characters` and `wiki/templates/pc.md`, and replace the Identity+Combat Stats anti-pattern with featured-portrait+Identity (Combat Stats full-width) per FR-010, FR-016, US4/AC2, SC-008 (contradicts)
- [ ] T046 Restore archive art onto `wiki/entities/pc/perrin-black-jaw.md`, `wiki/entities/pc/crissdalynn-khinriss.md`, and `wiki/entities/pc/delmar-fisk.md`: one featured portrait paired with Identity, leftovers only in `## Art`, omitted when none remain per FR-014, FR-021, SC-003, US3/AC3 (missing)
- [ ] T047 Move `type: pc` ingest routing in `.agents/skills/wiki-ingest/SKILL.md` out of the Preserve GUARD onto the general ingest path, include `pc` in the campaign type list, and except PC number conflicts so a newer supplied source overwrites via `player-characters` per FR-016, FR-020, T013 (partial)
- [ ] T048 Remove Ranger spell slot counts from Combat Stats on `wiki/entities/pc/jean-claude-tabarnack.md` so caster pools live only in Spells per US1/AC4, FR-006 (partial)
- [ ] T049 Rewrite the Work-gate invention sentence in `.agents/skills/pc-interview/SKILL.md` so it cannot require inventing combat math or player choices when the wiki lacks a fact per T012, FR-016, US2/AC5 (contradicts)

## Phase 15: Convergence

- [ ] T050 Restore dropped frontmatter aliases on `wiki/entities/pc/jean-claude-tabarnack.md` (`JC`, `Jumpy Don't Touch`, `Sticky Tongue Death Skin`, `Hopstradamus`), `wiki/entities/pc/perrin-black-jaw.md` (`Perrin`), `wiki/entities/pc/catarina-davirelli.md` (`Da'Virelli`, `Catarina`, `Caterina Da Virelle`, `Catarina Da Vrelle`), and `wiki/entities/pc/delmar-fisk.md` (`Delmar Atticus Fisk`) without renaming kebab titles or H1s per FR-014, SC-003, US3/AC3 (missing)
- [ ] T051 Relink in-vault owners: `wiki/entities/pc/jean-claude-tabarnack.md` `[[boots-of-flying]]` → `[[flying-boots]]`; `wiki/entities/pc/delmar-fisk.md` bare Cloak of the Manta Ray → `[[delmars-cloak-of-the-manta-ray]]` per FR-011, FR-018, US2/AC3 (missing)
- [ ] T052 Restore omitted archive satellite paths on `wiki/entities/pc/perrin-black-jaw.md` and `wiki/entities/pc/crissdalynn-khinriss.md` `sources` (abilities, stats, character-sheets, inventory, spells, galleries; Perrin also va-script) per FR-014, SC-003 (missing)
- [ ] T053 Flatten dropped Delmar archive facts into canonical homes on `wiki/entities/pc/delmar-fisk.md`: Session Log 01–04, 07, 08; five captains and fleet; Pearl theft; childhood wreck; mother's watch; Maggie; Serafina; keep DM answers in secrets, not Stated Goals unless a transcript supports them per FR-014, FR-022, SC-003, US3/AC2 (missing)
