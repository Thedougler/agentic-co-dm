# Research: Agentic Co-DM

## 1. Where the product lives

**Decision:** Candidate wiki is `wiki/` in this repo. Craft lives in `.agents/skills/`. Campaign of record stays at `Documents/ai-co-dm` until cutover (ADR 0002).

**Rationale:** Spec already named those surfaces. A third copy of the campaign is forbidden by `CONTEXT.md`.

**Alternatives considered:** Point this repo at the live vault (risks the campaign of record). Compiler/OS vault (rejected in spec). Empty wiki as source of truth (forbidden).

## 2. Runtime

**Decision:** No application process. The host agent runs skills. Obsidian is the DM UI. Foundry is the player surface, driven in prep through MCP tools already described by `foundry-stage`.

**Rationale:** Constitution VI — ship the agent-shaped tool. Spec forbids a Co-DM during the session.

**Alternatives considered:** A Foundry module that auto-presents (violates ADR 0001). A custom server for proposals (second store beside the vault).

## 3. Work and canon are wiki pages

**Decision:** Proposal, Work, accepted content, and canon are typed markdown pages (or a `lifecycle` field on a page). Accept/edit/reject is a frontmatter transition the DM makes, not a database row. See [contracts/work.md](./contracts/work.md).

**Rationale:** Spec: wiki is the product. FR-015 / ADR 0003: no silent canon.

**Alternatives considered:** Chat-only proposals (not inspectable — FR-013). A sidecar SQLite of proposals (second store).

## 4. Copied skills vs this spec

**Decision:** All copied D&D 5e skills are v1. Integration means rewrite in place to (a) writing-for-agents, (b) this spec, (c) `CONTEXT.md` (wiki not bank). Sequence by user stories, not a big-bang dump.

Gaps already visible:

- `foundry-stage` stages vault notes without an accepted-Work gate.
- `session-wrapup` writes surgical canon updates; must propose, then write after accept.
- `copy-writer` still names a `## Bank` band; rename to wiki/owner facts. Its prose bar already matches FR-018 (complete sentences, no telegram stubs).
- Wrapup/foundry skills assume ai-co-dm paths (`campaigns/<slug>/`, `./scripts/qmd`). Remap to `wiki/` + llm-wiki ingest/query.

**Rationale:** Spec FR-016. Constitution VI. User: wiki is human prose; skills may stay terse.

**Alternatives considered:** Leave skills as-is (they contradict accept-gate and glossary). Defer the pack (user said all v1).

## 5. Page shape

**Decision:** Keep llm-wiki frontmatter (`title`, `category`, `tags`, `sources`, `created`, `updated`) and add campaign `type` plus Work `lifecycle` and `reveal`. Body is complete-sentence human prose (`copy-writer` + `obsidian-markdown` on every write). Spoken player text is `[!narration]` only.

Campaign `type` values are listed in `wiki/AGENTS.md`: `npc`, `place`, `faction`, `item`, `creature`, `session`, `recap`, `work`. Sample notes may still say `location` / `monster` / `lore`; map those to `place` / `creature` / `item`. Do not invent types.

Place, item, hazard, and creature bodies copy `wiki/templates/` (studied from `wiki/_raw/`). Creature notes are linear: no `col` / `col-md` wrappers.

**Rationale:** Spec prose wiki + FR-018. Session 2026-09-12: templates and skills follow the sample layouts; linear creatures.

**Alternatives considered:** llm-wiki categories only (too generic for NPCs/places). Compiler vault (rejected). Column-wrapped monster sheets as the default (DM said linear).

## 6. Grounding and 5e

**Decision:** Established lore = wiki pages + D&D 5e rules. Foundry staging already sets `sourceRules: "2024"` in `foundry-stage`. Treat v1 as 5e including that 2024 mapping. Uningested published adventures are not lore.

**Rationale:** Spec clarifications. Do not open a 2014 vs 2024 fork in this plan.

**Alternatives considered:** System-agnostic pack (rejected). Model memory of modules as lore (rejected).

## 7. Testing

**Decision:** Observe pages and Foundry artifacts. Reuse skill `evals/` where they exist. Quickstart is the loop in [quickstart.md](./quickstart.md). One red→green slice per story when implementing.

**Rationale:** Constitution IV.

**Alternatives considered:** Unit-test skill markdown (pins wording). Mock Foundry (does not prove SC-003).

## 8. Glossary debt

**Decision:** When a skill or ADR is touched, replace "bank" with "wiki". Do not mass-edit untouched files in this plan.

**Rationale:** Domain language is binding; ponytail says only touch what the slice needs.

## 9. Propose before any wiki write (FR-019)

**Decision:** The Co-DM shows a proposal in the conversation and waits for DM approval before creating or changing a campaign wiki page. A named ingest is that approval for those sources, plus thin complete-sentence stubs for people/places/things named in them (including as links). Invented names not in the source are a separate proposal. Rejected proposals are never filed. Chat-only proposals that were never approved leave no wiki page.

**Rationale:** Session 2026-09-12 clarifications. Stops minting extra NPCs during ingest or prep (Sable-class failure). US1 still gets followable links via stubs.

**Alternatives considered:** Write `lifecycle: proposed` pages before the DM sees them (still a wiki write; rejected). Entity pages only after a ticked list (user chose lazy stubs for named-in-source instead). Approve every repo file including skills (rejected; campaign wiki pages only).

## 10. Early-dev sample layout

**Decision:** `wiki/_raw/` sample notes are the layout source for templates and skills. Ingest of those samples keeps section order, markdown, callouts, tables, and embeds. That exception is early-development only. General ingest still distills. Creature notes filed from craft skills are linear.

**Rationale:** Session 2026-09-12. The samples are already the DM's Obsidian reading format. Aligning templates is cheaper than rewriting them on every ingest. A standing "never reformat" ingest rule would freeze every future source.

**Alternatives considered:** Always preserve any source layout (rejected — not a general rule). Rewrite samples into Glance / At the table / Wiki facts (rejected — undoes DM layout work).
