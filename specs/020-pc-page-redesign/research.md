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

- **Decision:** Filed pages follow D&D Beyond information groups and order, implemented in Obsidian markdown and columns, not a visual clone of D&D Beyond chrome. Spine after the title and player-safe `[!narration]`: `Identity`, `Combat Stats`, `Ability Scores`, `Skills`, `Actions`, conditional `Spells`, `Inventory`, `Features`, then campaign extras `Connections`, `Session Log`, and conditional `Art`. No `Voice`, `At a Glance`, `Sheet`, `Combat Profile`, or required DM thesis.
- **Rationale:** Spec FR-002–FR-005. D&D Beyond is a player sheet; Combat Profile / DM thesis is NPC dossier behavior.
- **Alternatives considered:** Keep At a Glance / Combat Profile around a DDB mechanical block — rejected. Pixel-clone cards and site colors — rejected.

### Column pairs

- **Decision:** Two required pairs using nested `col` / `col-md` codeblocks, parent fence longer than children, headings inside child fences, narration outside fences:
  1. `Identity` + `Combat Stats` (DDB header / combat bar)
  2. `Ability Scores` + `Skills` (DDB left column)
- Campaign extras MAY pair `Connections` + `Session Log` the same way when both exist. `Actions`, `Spells`, `Inventory`, `Features`, and `Art` stay full-width. Linear headings and tables remain the semantic fallback. Add a narrow PC exception in `obsidian-markdown` columns guidance; do not weaken the session/run rule that narration stays outside fences.
- **Rationale:** Spec FR-010. Two pairs match DDB scan order without inventing chrome.
- **Alternatives considered:** `[!col]` callouts — rejected. Pair every remaining section — rejected (VII).

### Actions vs Features

- **Decision:** `Actions` holds attacks, actions, bonus actions, and reactions (omit empty subsections). `Features` holds traits, class features, and feats. There is no `Abilities` heading. Each populated row states effect and uses or recovery when applicable. These lists record options; they MUST NOT script what the player will do.
- **Rationale:** Spec FR-004, FR-005, and the record-only agency rule.
- **Alternatives considered:** Keep a combined Abilities dump — rejected; it is not DDB order.

### Markdown authorities

- **Decision:** `wiki/AGENTS.md` owns campaign type, path, approval, and the PC layout row plus wiki-kind routing to `player-characters`. `obsidian-markdown` owns syntax. The page contract in `contracts/pc-page.md` is the observable spine. Skills point at those sources; they do not clone the contract. `pc-interview` maps answers into the DDB sections; an interview transcript is evidence, not a live facet. `wiki-ingest` and reconciliation point at `player-characters` for `type: pc`. Include `pc` in any obsidian-markdown type list that currently omits it.
- **Rationale:** One owner per fact (IX). Interview/ingest already exist; they must stop implying NPC-like creation.
- **Alternatives considered:** Duplicate the full contract into every skill — rejected.

### Verification

- **Decision:** Public seam is the markdown owner-page contract plus skill routing. Keep the feature-local fixture `specs/020-pc-page-redesign/fixtures/check.py` and update its spine/column assertions. Run scoped wiki/Markdown lint. Do not use `tools/check_wiki_pages.py` as PC proof (`pc` is omitted there). No AST or column parser.
- **Rationale:** XIV. Existing fixture already fails un-conformed pages.
- **Alternatives considered:** Generic page checker expansion this feature — out of scope.

## Alternatives considered (feature-wide)

- Treat PCs through `npc-design` with a prettier template — rejected; that is the named failure.
- Generate player characters the way NPCs are designed — rejected; players create PCs.
- New character-sheet database or Foundry wrapper library — rejected; existing MCP and file reads are enough.
