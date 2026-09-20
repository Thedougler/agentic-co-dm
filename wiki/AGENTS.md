# Campaign wiki

Owner conventions for this vault. Load before every write to `wiki/`. Overrides llm-wiki defaults for campaign pages.

## Prose

Write **complete-sentence human prose**. A DM reads this without decoding agent shorthand. Telegram stubs, slash-stacks, and AI note-speak are invalid (FR-018).

**HARD (Nick 2026-09-14):** Production session-prep / TotM / spoken text that names or requires an entity MUST have that owner page filed first (kebab + template, live path). Vague stand-ins for missing entities do not ship — see root `AGENTS.md` entity-before-spoken. **DM-facing layers** (action cards, Be ready for, secrets, Wiki facts, owner pages): no coy/vague placeholders — see root `AGENTS.md` dm-facing-explicit.

Classify each write against the stack table in `AGENTS.md`. Vault is `true` on wiki vault notes. Mixed documents classify per passage, then apply vault format to the whole note.

Spoken player text is `[!narration]` only.
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
| `lifecycle` | `draft` \| `proposed` \| `accepted` \| `rejected` \| `canon` |
| `reveal` | `unrevealed` \| `revealed` |
| `kind` | On `type: session-prep`: `hook` \| `development` \| `cliffhanger` \| `climax` \| `resolution` \| `session-plan`. City pages stay `type: place` `kind: city`. |

Do not invent `type` values. Category is the top-level llm-wiki folder (`entities/`, `journal/`, …). `type` is the campaign kind — not a second category value (`category` stays `entities`, never `npc`).

**Entities path (depth 1):** live owner pages file at `wiki/entities/{type}/{Title}.md` using frontmatter `type` only (npc, pc, place, faction, item, creature, vehicle, spell, lore, quest, region, work). No deeper nests. No rarity/facet/synonym folders (`monster`, `inventory`, `rare`, …). Session-prep / session / recap stay under `wiki/journal/…`, not `entities/`. Redirect stubs with a typed target sit beside that type; typeless stubs may use `wiki/entities/_redirects/` only.

Redirect stubs with `redirects_to` omit campaign required fields (`sources`/`type`/`lifecycle`/`reveal`) from wiki-lint HARD `missing_frontmatter`.
Map early sample labels on file: `location`→`place`, `monster`→`creature`. Player characters use `type: pc` under `wiki/entities/pc/` — never `type: npc` / `entities/npc/`. PC identity signals: `role: PC` (any casing) or a `player:` frontmatter key. Do not file PCs as NPCs with a `pc` tag. World-truth notes use `type: lore`. Actual items stay `item`. Campaign situation pages use `type: quest`.
`lifecycle` defaults to `accepted` when the user said the fact; use `proposed` only when the user asked to park it. `visibility` defaults to `dm` and is distinct from `reveal`. `summary` is one sentence a DM can read in a list. Omit unused identity keys.


Work pages also set `grounded_in` and `invention` — see `docs/agents/work.md`.

Done when: required fields are present, body is complete sentences, related pages are `[[wikilinked]]`.

## Layout

Copy the matching `wiki/templates/` scaffold for the campaign `type` (and `kind` when the page is a session-prep beat). Session-prep beats copy `wiki/templates/hook.md`, `development.md`, `cliffhanger.md`, `climax.md`, `resolution.md`, or `session-plan.md`. Do not copy-start `wiki/templates/session-prep.md` for new beats or plans. Layout kinds Encounters, Rules, Campaign State, and DM Intelligence copy `wiki/templates/encounter.md`, `rules.md`, `campaign-state.md`, and `dm-intelligence.md`. Those names are not campaign `type` values. Do not add `type: encounter` or `type: rules`. Omit empty sections. Pass is run jobs, not heading-order match.

`wiki/_raw/` illustrates quality. It is not a clone target. Incoming ingest files are evidence of facts, not exemplary format. Filed pages are judged against the kinds and jobs in this file.

| Kind | Jobs |
|---|---|
| Place | Look; situation now; moves that change the scene; presence or sign of absence; table objects; connections; purpose |
| Consumable | Portrait; classification; one runnable effect; then stop. Copy `wiki/templates/item.md` with `kind: consumable`. |
| Flora hazard | Look; start; notice; contact cost; careful passage; honest counterplay. `type: item` `kind: flora hazard`. Copy `wiki/templates/hazard.md`. Pass is those jobs. |
| Magic / Plot / Durable item | Portrait; classification; runnable effect; then omit-empty At a Glance / At the Table / Connections / Secrets / Provenance / Art. `type: item` with `kind: magic` \| `plot` \| `durable`. Copy `wiki/templates/item.md`. Pass is those jobs. |
| Recap | Cold open optional; player-safe `[!narration] Recap`; Wiki facts. `type: recap`. Copy `wiki/templates/recap.md`. Pass is those jobs. |
| Creature | Look; runnable sheet; life (habitat, habits, diet, social); hunt (signs, instincts, opening, shut-down, aftermath) |
| Person | Who and want; look; first minutes and posture change; named ties; combat only if they can fight |
| PC | Spoken look; At a Glance (class/level/player/home ship + play-pattern thesis); Connections; Sheet + Combat Profile; Abilities; Spells when caster; Inventory; Session Log; Voice; Art. Single H1 only — flatten satellites; forbid nested `# Title — Facet` dumps. `type: pc`. Copy `wiki/templates/pc.md`. Pass is those jobs. |
| Session plan | Compass; beat map; floating beats; pressure; PC touchpoints. `type: session-prep` `kind: session-plan`. Copy `wiki/templates/session-plan.md`. File `Session-<n>-00-<Title>.md`. Pass is those jobs. |
| Hook | At the table; Open on; Situation; Run the hook; Decision handles; Handoff. `type: session-prep` `kind: hook`. Copy `wiki/templates/hook.md`. File `Session-<n>-<BB>-<Label>.md`. Pass is those jobs. |
| Development | Abstract; Opening; Run the beat; Situation; Revelations; Exits. `type: session-prep` `kind: development`. Copy `wiki/templates/development.md`. File `Session-<n>-<BB>-<Label>.md`. Pass is those jobs. |
| Cliffhanger | At a Glance; Open on Action; Run the beat; Opposition; Pressure; Resolution; Handoff. `type: session-prep` `kind: cliffhanger`. Copy `wiki/templates/cliffhanger.md`. File `Session-<n>-<BB>-<Label>.md`. Pass is those jobs. |
| Climax | Run this; Opening image; Situation; Visible levers; Pressure; Opposition; Outcome. `type: session-prep` `kind: climax`. Copy `wiki/templates/climax.md`. File `Session-<n>-<BB>-<Label>.md`. Pass is those jobs. |
| Resolution | Abstract; Run the beat; Closing image; What is true now; Consequences. `type: session-prep` `kind: resolution`. Copy `wiki/templates/resolution.md`. File `Session-<n>-<BB>-<Label>.md`. Pass is those jobs. |
| Vehicle | Look; sheet; components; crew stations; handling; combat; then omit-empty At a Glance / Secrets / Connections / At the Table / Provenance / Art. Copy `wiki/templates/vehicle.md`. Pass is those jobs. |
| Spell | Look of the casting; classification; runnable 2024 effect; Discovery when placement needed; Lore when history needed. Pass is those jobs. |
| Faction | Public face; DM thesis; current state; one active agenda; table-relevant assets, people, places, and relationships; faction-turn log. Pass is those jobs. |
| Lore | One durable question; At a Glance (core truth + why it matters); Current Truth; At the Table (notice / explains / enables / warns). Pass is those jobs. |
| Quest | Summary (objective, why now, deadline); Situation; Stakes including walk-away; World in motion (driver and next move if uninterrupted); at least two independent leads. Resolution omitted while unresolved. Pass is those jobs. |
| City | Arrival; At a glance including current pressure; Orientation (districts and getting around); Gazetteer enough to intentionally seek a place; rules that matter at the table; at least one active situation with if-nobody-intervenes. Page is `type: place` with `kind: city`. Site places keep using `wiki/templates/place.md` and existing Place jobs. Pass is those jobs. |
| Region | Spoken look; At a glance; Current state; geography/travel enough to choose a route; active powers; change log. Pass is those jobs. |
| Encounter | Situation; Opening pressure; Opposition; Choice surface; If ignored; Handoff. `type: session-prep`. Copy `wiki/templates/encounter.md`. Pass is those jobs. |
| Rules | At a Glance; Current Truth; At the Table. `type: lore`. Copy `wiki/templates/rules.md`. Pass is those jobs. |
| Campaign State | Table aim on the campaign hub; Live state; Index. `type: lore`. Copy `wiki/templates/campaign-state.md`. Pass is those jobs. |
| DM Intelligence | Table analysis; Grounding; Decision. `type: work`. Copy `wiki/templates/dm-intelligence.md`. DM Intelligence is not the aim. Pass is those jobs. |

Spoken look is theatre of the mind: no secrets, DCs, unearned names, author thesis.

Ingest of campaign-shaped `type: place` keeps required treatments (including `[!narration]`); it does not distill. Foreign sources map into the kind. Session-prep pages are `type: session-prep` with a matching `kind`.

Numbers live on one owner page. Other sample pages wikilink; they do not copy the effect, save, or sheet.

Consumable, flora hazard, and magic/plot/durable items all use `type: item`; they differ by `kind` and jobs. Flora hazards copy `wiki/templates/hazard.md`; other item kinds copy `wiki/templates/item.md`.

Legacy pages are out of scope. Wrapup MUST NOT convert a legacy page into a sample.

Done when: the kind's jobs are answered, empty sections are omitted, spoken look is player-safe.

Session home after ingest or accept: `wiki/journal/sessions/<campaign-slug>/<session-number>/` (Session 11 → `wiki/journal/sessions/shattered-sea/11/`; Session 01 → `…/01/`). Session plan `Session-<n>-00-<Title>.md`, numbered live beats `Session-<n>-<BB>-<Label>.md`, **post-play recaps**, and that night’s companion notes all live in the **same** session-number folder. Recap path: `wiki/journal/sessions/<campaign-slug>/<NN>/Session-<NN>-Recap.md` (`type: recap`, copy `wiki/templates/recap.md`). Do **not** park recaps at flat `wiki/journal/…`, spaced `Session NN - Recap.md`, or a parallel `recaps/` folder. Owner pages stay outside. `_raw/` is the ingest inbox. Two campaigns do not share a session-number folder. `wiki/templates/session.md` is deprecated as copy-start; `type: session` remains legacy in the enum. Do not file `{{title}} - B01 - Strong Start` names.

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

**Journal / session:** same session-number folder as today. Space-free forms:
- Plan: `Session-<n>-00-<kebab-title>.md`
- Beats: `Session-<n>-<BB>-<kebab-label>.md`
- Recaps: `Session-<NN>-Recap.md` (e.g. `Session-01-Recap.md`) — **not** `Session NN - Recap.md`
No separate `recaps/` tree; no flat `wiki/journal/Session-…`.

**Ingest minting:** `wiki/entities/{type}/{kebab-slug}.md` from `title` via the slug function above (depth 1). Do not mint spaced basenames. Manifest / qmd keys track vault-relative paths (prefer relative keys).

**Remorph apply greenlit 2026-09-14** (Nick): kebab (no spaces), strip `Aruhe` place prefixes, strip leading `00`/`00-` — run `./scripts/remorph-page-filename-kebab --dry-run` then `--apply` (GitHub PR diffs preferred). Other destructive consolidates stay gated. No lore invent.

Structural context waste (multi-H1 satellites, Foundry dump-copy beside Sheet, empty sections left in place) is a token bug — see `docs/agents/context-waste-method.md`. Not a prose-quality score.

Cross-kind DM-usability rules for templates and filed pages: use the frontmatter core, shared Title Case headings (`At a Glance`, `At the Table`, `Connections`, `Secrets`, `Provenance`, `Art`), correct callout surfaces, omit-empty sections, and no synonym headings for the same job. Image assets use flat `wiki/attachments/{subject-slug}-{role}.{ext}` paths with roles `banner`\|`portrait`\|`token`\|`battlemap`\|`overview`\|`reference`\|`handout`\|`teaser`\|`recording`; see `wiki/attachments/README.md`.

When a shared job appears, use the shared heading name. DM-visible labels use Title Case / spaced words — never snake_case in body or table Field columns (`One thing`, not `one_thing`); YAML keys may stay snake_case. Kind-specific job blocks keep their own names. `Relationships` is not a Connections synonym — use `## Connections`. Recap/session/run spoken surfaces use only `[!narration]`; owner pages may add `[!mechanic]` / `[!secret]`.

## Approval (FR-019)

Wiki facts the user said file immediately on the live path. Named ingest of those sources, and thin complete-sentence stubs for names those sources contain (including as links), file without a second chat step. Unsaid invented names are not canon. HARD entity-before-spoken files the owner page, then spoken.

Layout moves and structure-only template rewrites that keep facts and `type` unchanged proceed without waiting.

Done when: user-said facts are filed; layout and structure-only rewrites did not wait.
