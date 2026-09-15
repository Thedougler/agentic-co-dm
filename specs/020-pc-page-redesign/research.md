# Research: PC Page Redesign

## Decisions

### Canonical owner and source boundary

- **Decision:** Live PC owners remain `wiki/entities/pc/<kebab-slug>.md`. The sole copy-start scaffold is `wiki/templates/pc.md`. Archived facet files under `wiki/_archive/{abilities,character-sheets,combat-profile,galleries,inventory,session-logs,spells,stats,va-scripts}` stay evidence, not competing owners.
- **Rationale:** `wiki/AGENTS.md` already requires one owner page and `type: pc`. Conformance targets: `jean-claude-tabarnack.md`, `perrin-black-jaw.md`, `catarina-davirelli.md`, `crissdalynn-khinriss.md`, `delmar-fisk.md`.
- **Alternatives considered:** Split satellite model — rejected. Extra `type` or folder — rejected.

### PC-owning skill

- **Decision:** Skill id `player-characters` at `.agents/skills/player-characters/SKILL.md` is the sole skill owner for `type: pc`. It records a player-created character from supplied source. It MAY file a new wiki page when the player already made the character. It MUST NOT invent a PC, generate stats, or write the player's actions. `npc-design` MUST hard-route PC work here. Do not name it `pc-design`.
- **Rationale:** Spec FR-016. Agents defaulted to treating PCs as NPCs. `*-design` naming invites generation.
- **Alternatives considered:** Template plus pointers only — rejected by clarification. Allow npc-design to fill combat/portrayal — rejected. Name `pc-design` — rejected.

This skill and rewritten `wiki/templates/pc.md` are design-impact. Implementation MUST dispatch them to the designated writer per `docs/agents/skill-design-dispatch.md` and MUST load `writing-for-agents`. Pointer edits, fixture, CSS snippet, and page conformance are session-agent work.

### Record-only ingest sources

- **Decision:** Accept PDF character sheets, prose, Foundry VTT actors via existing MCP (`get-character`, `list-characters`, `get-character-entity`, related character tools), and other DM-supplied files. No new PDF parser, database, or Foundry client. Unreadable source: transcribe what can be read; omit unread numbers from the live page; do not invent stats; do not abort a usable partial page when some source remains.
- **Rationale:** FR-019. Existing MCP and file-read tools already do I/O. Constitution XVIII forbids `[verify]` interrogatives on wiki pages.
- **Alternatives considered:** New import service — rejected (XIV). Prose-only — rejected by clarification.

### Newest supplied source wins

- **Decision:** A newer PDF, prose, Foundry actor, or other supplied source that disagrees with the live wiki on the same number overwrites that wiki number in place (body home and matching frontmatter mirror). Structure-only conformance is not a newer source. One source that internally disagrees with itself: do not invent a winner; omit the contested number from the live page and file a GitHub issue. Do not print `[verify]` or a user question on the page.
- **Rationale:** FR-020 plus constitution XVIII (replace in place; uncertain facts stay off the page or become an issue).
- **Alternatives considered:** Wiki-always-wins — rejected by clarification. Keep both numbers on the live page — rejected (XVIII, two truths). `[verify]` marker on the live page — rejected (XVIII). Foundry as permanent mechanical SoT — rejected.

### D&D Beyond page shape

- **Decision:** Filed pages follow D&D Beyond information groups and order in Obsidian markdown and columns, not a visual clone of D&D Beyond chrome. After title and player-safe `[!narration]`: featured portrait paired with `Identity` when art exists; `Combat Stats` full-width; then the eight required sheet headings in order — `Identity`, `Combat Stats`, `Ability Scores`, `Skills`, `Actions`, `Spells`, `Inventory`, `Features`. Campaign extras after the sheet: `Connections`, conditional `Stated Goals`, `Session Log`, conditional `Art`. No `Voice`, `At a Glance`, `Sheet`, `Combat Profile`, `Abilities`, or required DM thesis.
- **Rationale:** FR-002–FR-006, FR-010, SC-006.
- **Alternatives considered:** Keep At a Glance / Combat Profile — rejected. Pixel-clone cards and site colors — rejected. Omit `Spells` for non-casters — rejected by clarification A.

### Spells is required

- **Decision:** Every filed PC page includes `## Spells` in sheet order. A character with no spell access still has the heading and states that they have no spells. Spell subsections (Spellcasting, Cantrips, Prepared or Known, Slots or Casting Resources) omit when empty. Multiclass pools stay distinct. Do not omit the `Spells` H2.
- **Rationale:** FR-006, SC-006, clarification A. Delmar Fisk is the non-caster proof.
- **Alternatives considered:** Omit `Spells` for non-casters — rejected. Empty placeholder spell tables — rejected.

### Three-column sheet

- **Decision:** After Combat Stats, one parent `col` fence with three `col-md` children:

  1. `## Ability Scores` (scores, modifiers, and saves on the same rows)
  2. `## Skills` (skill bonuses and proficiencies; this is the spec's "Skills and saves" middle column — saves stay on Ability Scores rows so each ability's save is not a second table)
  3. `## Actions`, `## Spells`, `## Inventory`, `## Features` stacked in that order

  Header pair (when art exists) remains two columns: featured portrait embed | `## Identity`. `Combat Stats` is full-width between those rows. Campaign extras stay full-width after the sheet. Parent fence longer than children. Headings inside child fences. Narration outside fences. Do not use `[!col]` for these PC rows. CSS (`pc-sheet.css`) owns column widths; markdown does not set `flexGrow` unless CSS cannot. Linear headings and tables remain the semantic fallback.
- **Rationale:** FR-010, clarification C, SC-007. obsidian-columns already supports N `col-md` children; the earlier "col-md is a pair" reading was wrong.
- **Alternatives considered:** Two pairs only (Ability Scores+Skills; Actions full-width) — rejected by clarification C. Three-column portrait|Identity|Combat Stats — rejected (portrait+Identity is the locked header; Combat Stats is the full-width combat bar). `[!col]` callouts — rejected (narration must stay a real callout). Pair Connections+Session Log — rejected.

### Actions vs Features

- **Decision:** `Actions` holds attacks, actions, bonus actions, and reactions (omit empty subsections). `Features` holds traits, class features, and feats. No `Abilities` heading. Each populated row states effect and uses or recovery when applicable. Lists record options; they MUST NOT script what the player will do. Required sheet H2s with no rows state none in a sentence rather than a placeholder table.
- **Rationale:** FR-004, FR-005, record-only agency.
- **Alternatives considered:** Combined Abilities dump — rejected.

### Unknowns and constitution XVIII

- **Decision:** Live PC pages hold present facts only. Missing source values are omitted, not invented. Do not write `[verify]`, questions, or prior-version numbers onto live PC pages or the PC template body. Archived satellites may keep historical `[verify]` text; they are not rewritten as live owners. Existing DM-only `[!secret]` callouts on live pages are present facts; preserve them; do not put them in narration; do not add a Secrets spine heading.
- **Rationale:** Constitution XVIII overlays spec edge-case language that said `[verify]`. Spec still requires "unknown rather than invented" and "do not invent a resolution."
- **Alternatives considered:** Keep `[verify]` on live pages as the spec's literal marker — rejected (constitution supersedes). Dual-number conflict rows — rejected (XVIII).

### Featured portrait and Art gallery

- **Decision:** One featured portrait after narration, paired with Identity when pictures exist. Extra pictures MAY sit next to the section they illustrate. Leftovers only in conditional `## Art`. One picture only → featured portrait, omit `Art`. No pictures → Identity full-width, omit `Art`. Blank embeds omitted. Linked images MUST resolve. Do not mint or rename art in this feature except space-to-kebab under XIII.
- **Rationale:** FR-021, clarification C.
- **Alternatives considered:** All art in a bottom gallery only — rejected. Hero image above the title — rejected. Distinct H2 for the portrait — rejected.

### Stated Goals

- **Decision:** Optional `## Stated Goals` after `Connections` and before `Session Log`. List only goals the player clearly stated in a game-session transcript, IC or OOC. Session summary is backup only, never sole source. Omit when none. Do not infer. After every session that included that player, `player-characters` refreshes from that session's transcript: add newly stated goals; drop a goal only if the player said it is done or abandoned; silence is not abandonment. Sessions that did not include the player do not refresh that PC. Session planning that includes the player MUST read this section when present. `session-beats` and `run-guide` read it; they do not write the PC page. `reconciling-session-evidence` routes refresh through `player-characters`.
- **Rationale:** FR-022, SC-010, SC-012.
- **Alternatives considered:** Require transcript and summary both — rejected. In-character only — rejected. Store goals on the recap — rejected.

### Vault CSS and PC-page tweaks

- **Decision:** Keep `wiki/.obsidian/snippets/ttrpg-styles.css` and `wide-note-surface.css` as vault default. Add `wiki/.obsidian/snippets/pc-sheet.css` scoped to `cssclasses` containing `pc-sheet` (portrait size, three-column widths, heading density). No decorative theme, cards, site colors, or D&D Beyond chrome. Use `obsidian-layout-adjustment` for the snippet. Live PC owners get `cssclasses: [pc-sheet]`.
- **Rationale:** FR-023, SC-011. Native `cssclasses` is the targeting seam.
- **Alternatives considered:** Distinct PC visual theme — rejected. Vault CSS only — rejected. Path-based CSS plugins — rejected (XIV).

### Markdown authorities

- **Decision:** `wiki/AGENTS.md` owns campaign type, path, approval, visibility (existing campaign field; this feature preserves it), the PC layout row, and wiki-kind routing to `player-characters`. `obsidian-markdown` / `COLUMNS.md` own syntax and the PC column rows. `contracts/pc-page.md` is the observable spine. Skills point at those sources; they do not clone the contract. `pc-interview` maps answers into DDB sections; the interview transcript is evidence. `wiki-ingest` and reconciliation point at `player-characters` for `type: pc`.
- **Rationale:** XVII, IX. One owner per fact.
- **Alternatives considered:** Duplicate the full contract into every skill — rejected.

### Verification

- **Decision:** Public seam is the markdown owner-page contract plus skill routing. Update `specs/020-pc-page-redesign/fixtures/check.py`: required H2s include `Spells`; non-casters MUST have `Spells` stating none; header `col` has two `col-md` children when art exists; sheet `col` has three `col-md` children; no Identity+Combat Stats pair; live owners and the template MUST NOT contain `[verify]`; `cssclasses` contains `pc-sheet`. Run scoped wiki/Markdown lint. Do not use `tools/check_wiki_pages.py` as PC proof. No AST or column parser. CSS presence is snippet-file plus `cssclasses`, not a rendered-pixel test.
- **Rationale:** XIV. Current fixture still encodes the superseded two-column / optional-Spells shape and MUST change with this plan.
- **Alternatives considered:** Generic page checker expansion — out of scope.

### Existing implementation drift

- **Decision:** Skill, template, live pages, `COLUMNS.md` PC rows, `wiki/AGENTS.md` PC layout row, and `fixtures/check.py` currently implement two column pairs and optional `Spells`. This plan is the source of truth. Implement/converge MUST remorph those files. `tasks.md` MUST be regenerated after this plan.
- **Rationale:** Spec clarifications A/C and constitution XVIII landed after that implementation.
- **Alternatives considered:** Treat current pages as already conforming — rejected; they fail FR-006, FR-010, SC-006, SC-007.

## Alternatives considered (feature-wide)

- Treat PCs through `npc-design` with a prettier template — rejected; that is the named failure.
- Generate player characters the way NPCs are designed — rejected; players create PCs.
- New character-sheet database or Foundry wrapper library — rejected; existing MCP and file reads are enough.
