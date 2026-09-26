# Campaign wiki

Owner conventions for this vault. Load before every write to `wiki/`. Overrides llm-wiki defaults for campaign pages.

## Prose

Write **complete-sentence human prose**. A DM reads this without decoding agent shorthand. Telegram stubs, slash-stacks, and AI note-speak are invalid (FR-018).

**HARD (Nick 2026-09-14):** Production session-prep / TotM / spoken text that names or requires an entity MUST have that owner page filed first (kebab + template, live path). Vague stand-ins for missing entities do not ship — see root `AGENTS.md` entity-before-spoken. **DM-facing layers** (actor entries, Checks, secrets, Wiki facts, owner pages): no coy/vague placeholders — see root `AGENTS.md` dm-facing-explicit.

Classify each write against the stack table in `AGENTS.md`. Vault is `true` on wiki vault notes. Mixed documents classify per passage, then apply vault format to the whole note.

Spoken player text is `[!narration]`, the only callout.
## Capability boundary

Wiki-facing skills receive a bounded intent, target, evidence, and constraints.
Their procedure remains in the owning skill; this file owns wiki semantics and
output constraints rather than duplicating craft.

For wiki work, project only the owner instructions, target source or page,
relevant current canon, applicable template or contract, validation evidence,
real dependencies, and deliberate omissions. Do not inherit unrelated artifact
groups from another capability.

Completion requires the owner's output contract plus applicable scoped
validation. A possible edit does not authorize a read route to mutate canonical
pages, manifests, indexes, or logs. Query, lint, and health observation shapes
remain owned by their current CLI contracts.

When ownership changes, hand off only the bounded artifact or operation to the
named receiving skill and return its evidence to the parent. The parent retains
the original objective; dependent spoken or presentation work waits for owner
pages and contracts. Use `AGENTS.md` for global routing and
`docs/agents/hybrid-sdd.md` for cross-capability composition.

### Capability convergence pointer

Use the full owner-relative `observe → act → re-observe` rule in
[`docs/agents/hybrid-sdd.md`](../docs/agents/hybrid-sdd.md) whenever wiki
work has an incomplete boundary. Continue only on changed owner evidence or a
passed owner guard; an unchanged observation requires a different sanctioned
path or a blocker. This file keeps wiki mutation, scope, canon, and handoff
semantics; it does not duplicate the common procedure.

## Frontmatter

Required on every page: `title`, `category`, `tags`, `sources`, `created`, `updated`.

Campaign pages also require:

| Field | Values |
|---|---|
| `type` | `npc` \| `pc` \| `place` \| `faction` \| `item` \| `creature` \| `vehicle` \| `spell` \| `lore` \| `quest` \| `region` \| `session-prep` \| `session` \| `recap` \| `work` |
| `reveal` | `unrevealed` \| `revealed` |
| `kind` | On `type: session-prep`: `hook` \| `development` \| `cliffhanger` \| `climax` \| `resolution` \| `session-plan` \| `encounter`. City pages stay `type: place` `kind: city`. |

Do not invent `type` values. Category is the top-level llm-wiki folder (`entities/`, `journal/`, …). `type` is the campaign kind — not a second category value (`category` stays `entities`, never `npc`).

**Entities path (depth 1):** live owner pages file at `wiki/entities/{type}/{Title}.md` using frontmatter `type` only (npc, pc, place, faction, item, creature, vehicle, spell, lore, quest, region, work). No deeper nests. No rarity/facet/synonym folders (`monster`, `inventory`, `rare`, …). Session-prep / session / recap stay under `wiki/journal/…`, not `entities/`. Redirect stubs with a typed target sit beside that type; typeless stubs may use `wiki/entities/_redirects/` only.

Redirect stubs with `redirects_to` omit campaign required fields (`sources`/`type`/`reveal`) from wiki-lint HARD `missing_frontmatter`.
Map early sample labels on file: `location`→`place`, `monster`→`creature`. Player characters use `type: pc` under `wiki/entities/pc/` — never `type: npc` / `entities/npc/`. PC identity signals: `role: PC` (any casing) or a `player:` frontmatter key. Do not file PCs as NPCs with a `pc` tag. World-truth notes use `type: lore`. Actual items stay `item`. Campaign situation pages use `type: quest`.
Canon follows the rule in [`llm-wiki`](../.agents/skills/llm-wiki/SKILL.md#canon). `visibility` defaults to `dm` and is distinct from `reveal`. `summary` is one sentence a DM can read in a list. Omit unused identity keys.


Work pages also set `grounded_in` and `invention` — see `docs/agents/work.md`.

Done when: required fields are present, body is complete sentences, related pages are `[[wikilinked]]`.

## Layout

Copy the matching `wiki/templates/` scaffold for the page's `type` (and `kind` for session-prep beats and city pages). The template is the one source of truth for the page: its headings, their order, and its callouts. The comment under a template heading starts with `Required.` when every page carries that section, `Required when <key> is <value>.` when the page's frontmatter decides, and `Free-form.` when the page shapes its own headings there; every other section is optional. The linter reads the same template, so changing a template changes what it checks. Keep the template's frontmatter keys; delete its comments and every body section you have no facts for.

**Fact-only.** Every line gives the DM a fact, ruling, or response they can use. A body section, glance bullet, table row, or callout with no fact stays off the page. Absence, uncertainty, and the source's silence are never written; where the table needs an answer and canon has none, decide it as a proposal (`docs/agents/table-ready.md` "Fill the silence"). Each fact appears once on the page. A stub is the lead sentence plus the glance bullets the source supports.

**Owner page anatomy** (every `entities/` type), in this order:

1. `# Title`, then optional overview art.
2. Header row (`col` codeblock): `## At a Glance` — one lead sentence on what the page is for at the table, then two to six `- **Label.** fact.` bullets — beside `> [!narration] Name`, the player-safe look.
3. The type's core section: `Statblock` (creature, vehicle, fighting NPC), `Sheet` (PC), `Properties` (item), `Effect` (spell), `Hazard` (flora hazard), `Ruling` (Rules), `Situation` (quest), or the type's own sections in its template. Lore shapes its body to fit the lore, with headings named for what they hold.
4. Shared sections, one meaning everywhere: `At the Table` (how to run it), `Secrets` (hidden truths and how each surfaces), `Connections` (`- [[page]] — what the tie does at the table`), `History` (past that changes a present choice), `Log` (newest first, one bullet per change play made), `Art`.

**Beat anatomy** (hook, development, cliffhanger, climax, resolution, session plan, session-prep, encounter): `At a Glance` (lead sentence, entry state, objective, ends when, next beat) → `> [!narration] Opening` → `Situation` → `Actors` → `Stage` → `Pressure` → `Handles` → `Checks` → `Clues` (truths) or `Leads` (routes onward) → `Outcomes` with carry-forward, plus the type's own sections in its template. `docs/agents/table-ready.md` is the completeness bar.

**Callouts.** `[!narration]` is the only callout: words the DM reads aloud, player-safe (no secrets, DCs, unearned names, or the At a Glance read). Mechanics and secrets are plain prose under their heading; the whole page is DM-facing. A page carries one narration block per moment the players live through — the look, a creature's or NPC's entrance, a revelation, the closing line — at the slot its template gives it; a line that belongs to one branch is an `_italic_` cell in the table's Narration column.

**Columns.** `col` / `col-md` codeblocks only, for two patterns: the owner-page header row, and a beat pair of two short same-moment blocks. Statblocks, wide tables, and long narration stay full width.

Layout kinds Encounters, Rules, Campaign State, and DM Intelligence copy `encounter.md`, `rules.md` (`type: lore` `kind: rules`), `campaign-state.md` (`type: lore` `kind: campaign-state`), and `dm-intelligence.md` (`type: work` `kind: dm-intelligence`). Flora hazards copy `hazard.md` (`type: item` `kind: flora hazard`). Cities copy `city.md` (`type: place` `kind: city`). `session-prep.md` is the run-guide cockpit; new beats and plans copy their typed template.

`wiki/_raw/` is evidence of facts, not a format to copy. Ingest maps foreign sources into the kind's template. Numbers live on one owner page; other pages link to it. Legacy pages move to the current template when next touched.

Done when: the template's required sections are present, every body line is fact-only, and the narration is player-safe.

Session home after ingest or accept: `wiki/journal/sessions/<campaign-slug>/<session-number>/` (Session 11 → `wiki/journal/sessions/shattered-sea/11/`; Session 01 → `…/01/`). Session plan `Session-<n>-00-<Title>.md`, numbered live beats `Session-<n>-<BB>-<Label>.md`, **post-play recaps**, and that night’s companion notes all live in the **same** session-number folder. Recap path: `wiki/journal/sessions/<campaign-slug>/<NN>/Session-<NN>-Recap.md` (`type: recap`, copy `wiki/templates/recap.md`). Do **not** park recaps at flat `wiki/journal/…`, spaced `Session NN - Recap.md`, or a parallel `recaps/` folder. Owner pages stay outside. `_raw/` is the ingest inbox. Two campaigns do not share a session-number folder. `type: session` remains legacy in the enum; new post-play logs are recaps. Do not file `{{title}} - B01 - Strong Start` names.

**Session evidence (post-play):** in the same session-number folder — `Session-<NN>-Recap.md` (summary), `Session-<NN>-Transcript.md` (text companion). Audio/video recording files use flat `wiki/attachments/session-<NN>-recording.{ext}` (role `recording`; kebab). Do not park transcripts/recordings under a parallel `recaps/` tree or repo-root folders. Raw dumps may land in `wiki/_raw/` then promote; archive evidence into `wiki/_archive/` after ingest.


## Page filenames

Wiki page `.md` **basenames** (not attachment images — those stay kebab `{slug}-{role}`).

**Rule (issue #80; amends #69/#70):** basename is a **space-free kebab slug** derived from the page’s display name. Frontmatter `title` keeps the human Obsidian display string (spaces/apostrophes OK). Filename stem and `title` are related by a deterministic slug function — they are not required to be identical strings.

**Slug function (mint / rename):**
1. Start from `title` (or the intended display name).
2. Strip leading legacy place-name prefixes (`Aruhe - `, `Aruhe -`, `Aruhe `) — content about the place stays in body/`title`; the prefix is dump legacy.
3. Strip leading `00` / `00-` / `00_` filename prefixes (including templates — e.g. `00-template` → `template`). **Banned** anywhere in the live vault.
4. Trim; replace each run of whitespace with a single `-`.
5. Remove apostrophes (`'` / `’`); keep existing hyphens that separate words.
6. Strip characters other than letters, digits, and `-` (no `/\:*?"<>|`, commas, etc.).
7. Collapse repeated `-`; trim leading/trailing `-`.
8. Result must contain **no spaces**. Prefer lowercase kebab for new mints (`hungry-isle.md`).

**Legacy = wrong:** current standards exclusively. Do not preserve spaced names, `Aruhe` place prefixes, or `00`/`00-` prefixes on mint or remorph.

Example: `title: Jean-Claude Tabarnack` → `wiki/entities/pc/jean-claude-tabarnack.md`. Example: `Aruhe - Hungry Isle.md` → `hungry-isle.md`. Example: `00-template.md` → `template.md`.


**Uniqueness:** vault-wide unique stem (no two live `.md` files share the same basename across folders). Prefer clearer titles/slugs over folder shadowing.

**Wikilinks:** bare `[[Display Title]]` resolves via `title` / `aliases` / path (lint already). Prefer putting the human name in `title` and former spaced stems in `aliases:` after rename. On rename: move the file to the new kebab stem and rewrite inbound wikilinks/embeds in the same pass so the old basename is gone. The old file is deleted in that pass, not kept as a `redirects_to` stub.

**Case-only rename** (`Bisou.md` → `bisou.md`; hit 2026-09-24). This volume is case-insensitive, so both spellings name one file: a Write to the lowercase path lands in the same inode and leaves the old spelling on disk, and a later `rm Bisou.md` takes the page with it. Move the file twice:

```bash
mv Bisou.md case-tmp.md && mv case-tmp.md bisou.md
```

Then re-point the index, which keeps the old spelling while `core.ignorecase = true`:

```bash
git rm --cached --quiet entities/npc/Bisou.md && git add entities/npc/bisou.md
```

Done when `ls` and `git ls-files` both print the kebab stem.

**Journal / session:** same session-number folder as today. Space-free forms:
- Plan: `Session-<n>-00-<kebab-title>.md`
- Beats: `Session-<n>-<BB>-<kebab-label>.md`
- Recaps: `Session-<NN>-Recap.md` (e.g. `Session-01-Recap.md`) — **not** `Session NN - Recap.md`
No separate `recaps/` tree; no flat `wiki/journal/Session-…`.

**Ingest minting:** `wiki/entities/{type}/{kebab-slug}.md` from `title` via the slug function above (depth 1). Do not mint spaced basenames. Manifest / qmd keys track vault-relative paths (prefer relative keys).

**Remorph apply greenlit 2026-09-14** (Nick): kebab (no spaces), strip `Aruhe` place prefixes, strip leading `00`/`00-` — run `./scripts/remorph-page-filename-kebab --dry-run` then `--apply` (GitHub PR diffs preferred). Other destructive consolidates stay gated. No lore invent.

Structural context waste (multi-H1 satellites, Foundry dump-copy beside Sheet, empty sections left in place) is a token bug — see `docs/agents/context-waste-method.md`. Not a prose-quality score.

Image assets use flat `wiki/attachments/{subject-slug}-{role}.{ext}` paths with roles `banner`\|`portrait`\|`token`\|`battlemap`\|`overview`\|`reference`\|`handout`\|`teaser`\|`recording`; see `wiki/attachments/README.md`. DM-visible labels use Title Case words (`One thing`, not `one_thing`); YAML keys may stay snake_case.

## Approval (FR-019)

Wiki facts the user said file immediately on the live path. Named ingest of those sources, and stubs for names those sources contain (including as links), file without a second chat step; a stub carries only the facts the source gives. Unsaid invented names are not canon. HARD entity-before-spoken files the owner page, then spoken.

Layout moves and structure-only template rewrites that keep facts and `type` unchanged proceed without waiting.

Done when: user-said facts are filed; layout and structure-only rewrites did not wait.
