# Research: NPC Page Standard

## 1. One template, not four

**Decision:** Ship a single `wiki/templates/npc.md` that is the core spine only. Band extras (extra form, History, activity log, difficulty knobs, Combat) are added from [contracts/npc-page.md](./contracts/npc-page.md) only when they have content.

**Rationale:** FR-008 forbids empty optional headings. Four templates would reintroduce residue. Spec bands are density profiles, not document types (FR-001, FR-016).

**Alternatives considered:** Four templates (Hinewai/Skarn/Nona/Thunk) — agents pick the wrong one and leave unused headings. One mega-template with every optional heading present — fails FR-008. Keep the current three-heading stub (`At a Glance` / `At the table` / `Wiki facts`) — spec FR-016 rejects it.

## 2. Frontmatter `role` vs craft function

**Decision:** Wiki identity `role` is the closed set `rival` | `patron` | `contact`. Craft labels in `npc-templates.md` (informant, gatekeeper, foil, …) stay design notes. They do not become new `role` values.

**Rationale:** Spec FR-003. Rival maps to potentially hostile bands; patron to Nona-class; contact to Thunk-class. Expanding the closed set is a later spec change.

**Alternatives considered:** Put every craft label in frontmatter (unbounded; breaks list filters). Drop craft labels (skill still needs them for play function).

## 3. Combat on the NPC page or a pointer

**Decision:** Fightable NPCs carry `# Combat` with a one-sentence encounter rule and either an on-page fight sheet or exactly one pointer to a creature-page sheet. Do not duplicate numbers. Friendly NPCs who are not expected to fight omit Combat.

**Rationale:** FR-009, FR-012. Thunk is the pointer exemplar; Hinewai/Skarn are on-page sheets; Nona omits Combat. This overrides the current `npc-design` line that forbids a separate monster note.

**Alternatives considered:** Always embed the sheet (duplicates Thunk). Always split to `type: creature` (hostile baselines keep the sheet on the NPC page because that is how the DM runs them). Empty `# Combat` "reserved" heading (FR-008).

## 4. Two-pane glance and spoken look

**Decision:** Keep the baseline codeblock column pair for At a Glance (wide) + spoken look (narrow), and for Running the NPC (two equal columns). Narration stays a real `[!narration]` callout inside the glance row so it matches the four baselines. Creature pages stay linear.

**Rationale:** Spec assumptions and `wiki/AGENTS.md` ("early-dev samples are the layout source"). `obsidian-markdown` already documents codeblock `col` when a spoken callout sits in a column.

**Alternatives considered:** Linear NPC pages like creatures (user named the columned baselines as the new standard). Callout `[!col]` (breaks `[!narration]` styling). Full-width narration under the glance table (not what the four pages do).

## 5. Where the four baselines live

**Decision:** Leave Hinewai, Talon Skarn, Nona Black-Jaw, and Thunk in `wiki/_raw/`. Point `wiki/AGENTS.md` and `npc-design` at those files. Do not promote them to `entities/` in this feature.

**Rationale:** Spec assumption: bulk rewrite and filing are out of scope. Identity-field defaults apply when those pages are next accepted. Layout source does not require a second copy.

**Alternatives considered:** File them now as canon (approval gate; not this feature). Rewrite their frontmatter in `_raw/` to match identity defaults (optional later; body already matches).

## 6. Skill points at the template; does not restate it

**Decision:** `npc-design` keeps craft (want, leverage, limit, signals). Wiki layout becomes: copy `wiki/templates/npc.md`; add optional sections from the contract when facts exist; exemplars are the four `_raw/` pages. Delete the stale paths `wiki/templates/NPC.md` and `wiki/shattered-sea/npcs/Aruhe - Hinewai`.

**Rationale:** Constitution VI and writing-for-agents: one source of truth. The current skill restates a Hinewai-only outline and a missing path.

**Alternatives considered:** Move the full heading list into the skill (duplicates the template). New `npc-layout` skill (YAGNI).
