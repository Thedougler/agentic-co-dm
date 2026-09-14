# Campaign wiki

Owner conventions for this vault. Load before every write to `wiki/`. Overrides llm-wiki defaults for campaign pages.

## Prose

Write **complete-sentence human prose**. A DM reads this without decoding agent shorthand. Telegram stubs, slash-stacks, and AI note-speak are invalid (FR-018).

Classify each write against the stack table in `AGENTS.md`. Vault is `true` on wiki vault notes. Mixed documents classify per passage, then apply vault format to the whole note.

Spoken player text is `[!narration]` only.

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
`lifecycle` defaults to `proposed` until the DM accepts. `visibility` defaults to `dm` and is distinct from `reveal`. `summary` is one sentence a DM can read in a list. Omit unused identity keys.


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

Session home after ingest or accept: `wiki/journal/sessions/<campaign-slug>/<session-number>/` (Session 11 → `wiki/journal/sessions/shattered-sea/11/`; Session 01 → `…/01/`). Session plan `Session-<n>-00-<Title>.md`, numbered live beats `Session-<n>-<BB>-<Label>.md`, **post-play recaps**, and that night’s companion notes all live in the **same** session-number folder. Recap path: `wiki/journal/sessions/<campaign-slug>/<NN>/Session NN - Recap.md` (`type: recap`, copy `wiki/templates/recap.md`). Do **not** park recaps at flat `wiki/journal/Session NN - Recap.md` or a parallel `recaps/` folder. Owner pages stay outside. `_raw/` is staging. Two campaigns do not share a session-number folder. `wiki/templates/session.md` is deprecated as copy-start; `type: session` remains legacy in the enum. Do not file `{{title}} - B01 - Strong Start` names.


## Shared grammar

## Page filenames

Wiki page `.md` **basenames** (not attachment images — those stay kebab `{slug}-{role}`).

**Rule:** filename stem **equals** frontmatter `title` (Unicode, Title Case / display casing as spoken). Spaces and apostrophes are allowed. Example: `wiki/entities/npc/Jean-Claude Tabarnack.md` with `title: Jean-Claude Tabarnack`.

**Why:** Obsidian graph nodes and bare `[[wikilinks]]` use the note name. Agents need one deterministic key — the same string as `title` — not a parallel kebab slug. Attachment kebab does **not** apply to pages.

**Uniqueness:** vault-wide unique stem (no two live `.md` files share the same basename, even across `entities/{type}/`). Prefer fixing collisions with a clearer title, not folder shadowing.

**Forbidden in basenames:** `/\:*?"<>|`, leading/trailing whitespace, control characters, consecutive spaces. Do not use snake_case or kebab-case page files for owner pages.

**Wikilinks:** prefer `[[Title]]` matching the stem. Path-qualified links (`[[entities/npc/Title]]`) are optional hardening; display aliases use `[[Title|short]]`. On rename: update `title` + filename together; leave a `redirects_to` stub at the old stem when inbound links may linger; put alternate names in `aliases:` when useful.

**Journal / session:** under `wiki/journal/sessions/<campaign-slug>/<session-number>/` keep `Session-<n>-00-<Title>.md`, beats `Session-<n>-<BB>-<Label>.md`, and recaps `Session NN - Recap.md` (same folder as that night’s plan when present). Companion notes that night only. Do not invent `Title - B01 - …` forms; do not use a separate `recaps/` tree.

**Ingest minting:** new owner page path = `wiki/entities/{type}/{title}.md` (depth 1). Refuse inventing a different slug file while `title` stays human. Manifest / qmd keys should track the vault-relative path; prefer relative keys over absolute machine paths when rewriting.

**No mass rename** until Nick greenlights after this standard lands. Lint/remorph are ATE follow-on (issue #69).

Structural context waste (multi-H1 satellites, Foundry dump-copy beside Sheet, empty sections left in place) is a token bug — see `docs/agents/context-waste-method.md`. Not a prose-quality score.

Cross-kind DM-usability rules for templates and filed pages: frontmatter core, shared Title Case headings (`At a Glance`, `At the Table`, `Connections`, `Secrets`, `Provenance`, `Art`), callout surfaces, omit-empty, and no synonym headings for the same job. Full text: `wiki/templates/00-shared-grammar.md`. Image assets: flat `wiki/attachments/{subject-slug}-{role}.{ext}` with roles `banner`\|`portrait`\|`token`\|`battlemap`\|`overview`\|`reference`\|`handout`\|`teaser` (see shared grammar Attachment filenames).

When a shared job appears, use the shared heading name. DM-visible labels use Title Case / spaced words — never snake_case in body or table Field columns (`One thing`, not `one_thing`); YAML keys may stay snake_case. Kind-specific job blocks keep their own names. `Relationships` is not a Connections synonym — use `## Connections`. Recap/session/run spoken surfaces use only `[!narration]`; owner pages may add `[!mechanic]` / `[!secret]`.

## Approval (FR-019)

Wiki facts change only after the DM accepts. Named ingest of approved sources, and thin complete-sentence stubs for names those sources contain (including as links), may file without a second accept. Invented names not in the source are Work — chat proposal first. Rejected proposals leave no page.

Layout moves and structure-only template rewrites that keep facts and `type` unchanged proceed without waiting.

Done when: fact writes waited on accept; layout and structure-only rewrites did not.
