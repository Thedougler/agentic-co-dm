# Research: PC Page Redesign

## Decisions

### Canonical owner and source boundary

- **Decision:** Live PC owners remain `wiki/entities/pc/<kebab-slug>.md`. The sole copy-start scaffold is `wiki/templates/pc.md`. Archived facet files under `wiki/_archive/{abilities,character-sheets,combat-profile,galleries,inventory,session-logs,spells,stats,va-scripts}` stay evidence, not competing owners.
- **Rationale:** `wiki/AGENTS.md` already requires one owner page and `type: pc`. The five conformance targets are `jean-claude-tabarnack.md`, `perrin-black-jaw.md`, `catarina-davirelli.md`, `crissdalynn-khinriss.md`, and `delmar-fisk.md`.
- **Alternatives considered:** Split satellite model — rejected; extra `type` or folder — rejected.

### PC-owning skill

- **Decision:** Add one skill at `.agents/skills/player-characters/SKILL.md`. It is the sole skill owner for `type: pc` pages. Name it `player-characters`, not `pc-design`. It records and represents a player-created character from supplied source. It MAY file a new wiki page when the player already made the character. It MUST NOT invent a PC, generate stats, or write the player's actions. `npc-design` and other NPC workflows MUST NOT create, rewrite, or prescribe PC pages; `npc-design` already says it is not for player-character builds, and that exclusion MUST become a hard route to this skill.
- **Rationale:** Agents defaulted to treating PCs as NPCs. A template-only change does not stop that routing. `*-design` naming would invite generation.
- **Alternatives considered:** Template plus existing-skill pointers only — rejected by spec clarification. Allow npc-design to fill combat/portrayal — rejected. Name the skill `pc-design` — rejected.

This skill and the rewritten `wiki/templates/pc.md` are design-impact work. Implementation MUST dispatch them to the designated writer per `docs/agents/skill-design-dispatch.md` and MUST load `writing-for-agents`. Smaller pointer edits in established skills and `wiki/AGENTS.md` are not design-impact.

### Record-only ingest sources

- **Decision:** The skill accepts PDF character sheets, prose descriptions, Foundry VTT actors via the existing MCP server (`get-character`, `list-characters`, `get-character-entity`, and related character tools), and other files the DM supplies. No new PDF parser, database, or Foundry client. The agent reads the source and transcribes it onto the template. Unreadable or unreachable source leaves fields unknown or `[verify]`; it does not invent stats or abort a usable partial page when some source remains.
- **Rationale:** Spec FR-019 names those sources. Existing MCP and file-read tools already do the I/O.
- **Alternatives considered:** New import service — rejected (XIV, YAGNI). Prose-only this feature — rejected by clarification.

### Newest supplied source wins

- **Decision:** When a newer PDF, prose, Foundry actor, or other supplied source disagrees with the live wiki page on the same number, overwrite the wiki number with the newer source. A structure-only conformance pass is not a newer source and MUST NOT overwrite facts. One source that internally disagrees with itself still keeps both values or `[verify]`; the agent does not invent a resolution.
- **Rationale:** Spec FR-020. Conformance remains structure-only (FR-017).
- **Alternatives considered:** Wiki-always-wins — rejected by clarification. Foundry as permanent mechanical SoT — rejected. Side-by-side forever — rejected.

### D&D Beyond page shape

- **Decision:** Filed pages follow D&D Beyond information groups and order, implemented in Obsidian markdown and columns, not a visual clone of D&D Beyond chrome. Spine after the title and player-safe `[!narration]`: featured portrait paired with `Identity` when art exists, then `Combat Stats`, `Ability Scores`, `Skills`, `Actions`, conditional `Spells`, `Inventory`, `Features`, then campaign extras `Connections`, conditional `Stated Goals`, `Session Log`, and conditional `Art`. No `Voice`, `At a Glance`, `Sheet`, `Combat Profile`, or required DM thesis.
- **Rationale:** Spec FR-002–FR-005, FR-021–FR-022. D&D Beyond is a player sheet; Combat Profile / DM thesis is NPC dossier behavior.
- **Alternatives considered:** Keep At a Glance / Combat Profile around a DDB mechanical block — rejected. Pixel-clone cards and site colors — rejected. Identity paired with Combat Stats instead of the portrait — superseded by clarification C.

### Column pairs

- **Decision:** Two scan pairs using nested `col` / `col-md` codeblocks, parent fence longer than children, headings inside child fences when a heading exists, narration outside fences:
  1. Featured portrait + `Identity` when at least one picture of the character exists. Left `col-md` is the portrait embed only (no extra H2). Right `col-md` contains `## Identity`. When no pictures exist, `Identity` is full-width and there is no empty portrait column.
  2. `Ability Scores` + `Skills` (DDB left column).
- `Combat Stats` is full-width immediately after Identity. Campaign extras stay full-width. Additional pictures MAY sit next to the section they illustrate. Leftover pictures go only in `## Art` at the bottom. Linear headings and tables remain the semantic fallback. Add a narrow PC exception in `obsidian-markdown` columns guidance; do not weaken the session/run rule that narration stays outside fences.
- **Rationale:** Spec FR-010, FR-021. Portrait beside Identity is the locked header. Pairing Identity with Combat Stats would steal that pair.
- **Alternatives considered:** `[!col]` callouts — rejected. Keep Identity + Combat Stats as the header pair — rejected by clarification C. Three-column portrait|Identity|Combat Stats — rejected (VII, current `col-md` is a pair). Pair Connections + Session Log — rejected; `Stated Goals` now sits between them.

### Actions vs Features

- **Decision:** `Actions` holds attacks, actions, bonus actions, and reactions (omit empty subsections). `Features` holds traits, class features, and feats. There is no `Abilities` heading. Each populated row states effect and uses or recovery when applicable. These lists record options; they MUST NOT script what the player will do.
- **Rationale:** Spec FR-004, FR-005, and the record-only agency rule.
- **Alternatives considered:** Keep a combined Abilities dump — rejected; it is not DDB order.

### Markdown authorities

- **Decision:** `wiki/AGENTS.md` owns campaign type, path, approval, and the PC layout row plus wiki-kind routing to `player-characters`. `obsidian-markdown` owns syntax. The page contract in `contracts/pc-page.md` is the observable spine. Skills point at those sources; they do not clone the contract. `pc-interview` maps answers into the DDB sections; an interview transcript is evidence, not a live facet. `wiki-ingest` and reconciliation point at `player-characters` for `type: pc`. `reconciling-session-evidence` routes post-session Stated Goals refresh through `player-characters`. `session-beats` and `run-guide` read Stated Goals when planning a session that includes that player and do not write the PC page. Include `pc` in any obsidian-markdown type list that currently omits it. CSS work uses `obsidian-layout-adjustment` on the snippets named above.
- **Rationale:** One owner per fact (IX). Interview/ingest already exist; they must stop implying NPC-like creation. Goals are PC-owner facts, not recap facts.
- **Alternatives considered:** Duplicate the full contract into every skill — rejected. Write goals from session-recap — rejected.

### Verification

- **Decision:** Public seam is the markdown owner-page contract plus skill routing. Keep the feature-local fixture `specs/020-pc-page-redesign/fixtures/check.py` and update its spine/column assertions: portrait+Identity pair when art exists, `Stated Goals` optional and omitted when empty, `cssclasses` contains `pc-sheet`, no Identity+Combat Stats pair. Run scoped wiki/Markdown lint. Do not use `tools/check_wiki_pages.py` as PC proof (`pc` is omitted there). No AST or column parser. CSS presence is a snippet-file plus `cssclasses` check, not a rendered-pixel test.
- **Rationale:** XIV. Existing fixture already fails un-conformed pages.
- **Alternatives considered:** Generic page checker expansion this feature — out of scope.

### Featured portrait and Art gallery

- **Decision:** Use existing generated art of the character. One featured portrait after narration, paired with Identity. Extra pictures MAY appear next to the section they illustrate. Remaining unused pictures appear only in conditional `## Art` at the bottom. One picture only → featured portrait, omit `## Art`. No pictures → no portrait pair, omit `## Art`. Do not mint or rename art in this feature except space-to-kebab under constitution XIII. Filenames already encode kind; the featured portrait is a portrait-kind attachment of that PC, not a battlemap or token.
- **Rationale:** Spec FR-021 and clarification C. Constitution XIII already distinguishes media kind.
- **Alternatives considered:** All art in a bottom gallery only — rejected. Hero image above the title — rejected. Distinct H2 for the portrait — rejected; the embed lives in the column pair.

### Stated Goals

- **Decision:** Optional `## Stated Goals` after `Connections` and before `Session Log`. List only goals the player clearly stated in a game-session transcript, in character or out of character. A session summary MAY help locate or paraphrase a transcript-supported goal and MUST NOT be the sole source. Omit the section when none exist. Do not infer from play, connections, or DM thesis. After every session that included that player, `player-characters` refreshes the section from that session's transcript: add newly stated goals; drop a goal only if the player said it is done or abandoned; silence is not abandonment. Sessions that did not include the player do not refresh that PC. Session planning that includes the player MUST read this section when present. `reconciling-session-evidence` routes the refresh through `player-characters`. `session-beats` / `run-guide` read it; they do not write it. Player-facing recap does not list DM-only goal tracking.
- **Rationale:** Spec FR-022, SC-010, SC-012.
- **Alternatives considered:** Require transcript and summary both — rejected (clarification B). In-character only — rejected (clarification A). Refresh only on explicit skill run — rejected (clarification A, post-session). Store goals on the recap page — rejected; the PC owner is the planning surface.

### Vault CSS and PC-page tweaks

- **Decision:** Keep existing vault-wide snippets `wiki/.obsidian/snippets/ttrpg-styles.css` and `wide-note-surface.css` as the default vault CSS. Add PC-page-only scan tweaks in `wiki/.obsidian/snippets/pc-sheet.css`, scoped to notes with `cssclasses` containing `pc-sheet` (portrait size, Identity/Ability column widths, heading density). No decorative PC theme, cards, site colors, or D&D Beyond chrome. CSS is not semantic; headings and tables remain the fallback. Use `obsidian-layout-adjustment` for the snippet work. Live PC owners get `cssclasses: [pc-sheet]`.
- **Rationale:** Spec FR-023, SC-011. Native Obsidian `cssclasses` is the targeting seam; `type` is not visible to CSS.
- **Alternatives considered:** Distinct PC visual theme — rejected. Vault CSS only with no PC tweaks — rejected. Restyle from a new vault theme — rejected; existing snippets already are the vault default. Path-based CSS plugins — rejected (XIV).

## Alternatives considered (feature-wide)

- Treat PCs through `npc-design` with a prettier template — rejected; that is the named failure.
- Generate player characters the way NPCs are designed — rejected; players create PCs.
- New character-sheet database or Foundry wrapper library — rejected; existing MCP and file reads are enough.
