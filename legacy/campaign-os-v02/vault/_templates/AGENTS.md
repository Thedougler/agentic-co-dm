### _templates/

These templates are the sole source of truth for how content is constructed
— frontmatter shape and required headings. A skill that needs one of these
facts points to the template instead of duplicating it; no other file owns
what a template provides itself.

A `_templates/<type>.md` (plus the files/skills it references) is all an
agent needs to construct that content type at the desired quality.

Templates are agent-consumed only. The Templater plugin is installed but
its automation (`folder_templates`, `trigger_on_file_creation`) stays off
by design: a template's `<!-- AGENT: ... -->` comments are instructions to
an LLM, not a human, so auto-inserting one into a hand-created note would
hand a person raw scaffolding with no agent there to fill it in.

#### Templates own layout only

No template carries a `<!-- AGENT: ... -->` comment — banned outright
(`CampaignOS.TemplateAgentComments`, `.vale-hard.ini`, error). A template
owns frontmatter shape, heading order, and each section's structural spec
(line counts, table columns, field types) as plain prose directly under
the heading — never wrapped in an HTML comment, never phrased as an
imperative to an agent.

That spec rides inside the `<…>` placeholder the author replaces, so the
angle brackets are what separates spec from content: replacing the
placeholder consumes the spec, and a spec left behind is a placeholder left
behind, which W48 fails on the instantiated page. Bare prose under a heading
is body content that ships verbatim onto every page made from the template
— write it only when every one of those pages should carry that sentence.

Build guidance — which skill to load, craft judgment calls, a prohibition
with its replacement and cited reason (`path/to/doc.md §N`) — lives in
that skill's own `.claude/skills/<skill-name>/SKILL.md` or a
`.claude/skills/<skill-name>/references/` file under it. A workflow
that coordinates more than one content type (e.g. "build the shop's NPC
page first, then link back") lives in a `vault/refs/runbook-<name>.md` page instead.
No template opens with a prose line naming its own target path or
purpose — that's self-evident from the file's own path and its `type:`/
`subtype:` frontmatter. The owning skill or drafting guide is named
exactly once, in frontmatter (`owner_skill:`, ADR-0040). A template's H1
is followed directly by its first real content block.

#### Ownership and containment (ADR-0040)

`owner_skill:` is required on every template file and carries through to
the page instantiated from it — it names the guide or skill that owns that
page's quality, and is as useful on the page as on the template. Its
trailing comment marks it `# OPTIONAL` so a page predating the key still
validates. `within:` is the one
containment relation — quoted always (an unquoted `[[<slug>]]` parses as
a nested array, not a string), full vault-relative path, no alias.

A key or heading is marked `# OPTIONAL` only when genuinely conditional on
something outside the author's control — never as a hedge against a case
that "might not apply." A fact the author can always supply (a location's
four compass neighbours, its `within:`) is required, full stop: marking it
optional teaches the model to skip it.

A template is grounded in its external reference wiki's genre conventions
first (e.g. Forgotten Realms Wiki for D&D locations and creatures) — this
vault's own real pages inform whether a genre-standard section earns its
keep for this campaign's play style, never the base shape.

An OPTIONAL heading states its own keep/delete condition in plain prose
directly under the heading (never a comment) — delete the heading outright
when the condition doesn't hold; never leave it empty (W38, error) or
filled with a placeholder line (W48, error).

Spoken player-facing prose is a sibling `type: narration` (or
`type: dialogue`) file. The parent template states only
`![[<slug>-narration-<role>]]` — no wrapping heading; the sibling's
standard callout title is the section. `writing-player-prose` owns how
to fill the sibling. `_templates/_performative/_narration.md` and
`_dialogue.md` are the shape.

Location is three genres, not one shape with six variants — governed-area
(`vault/_templates/_campaigns/_location/_location_settlement.md`, `vault/_templates/_campaigns/_location/_location_region.md`), site (`vault/_templates/_campaigns/_location/_location.md`,
`vault/_templates/_campaigns/_location/_location_shop.md`), dungeon (`vault/_templates/_campaigns/_location/_location_dungeon.md`) — each grounded in
its own external-wiki article type (ADR-0040). A district is
`subtype: settlement` nested `within:` a larger settlement; an island is
`subtype: region` nested `within:` a larger region or the sea. The shared
`## Notable NPCs` blocks and the compass-neighbour frontmatter
keys are identical across all five files by design — the same shape at
every genre and scale — and are not duplication to collapse. `## Loot` is
OPTIONAL, kept only when at least one `type: secret, subtype: cache` page's
`within:` resolves to that page.

The shared `## What Happened` + `## Consequences` blocks across the event
family (`vault/_templates/_campaigns/_events/_event.md` and its `vault/_templates/_campaigns/_events/_event_arrival.md`, `vault/_templates/_campaigns/_events/_event_battle.md`,
`vault/_templates/_campaigns/_events/_event_disappearance.md`, `vault/_templates/_campaigns/_events/_event_disaster.md`, `vault/_templates/_campaigns/_events/_event_festival.md`,
`vault/_templates/_campaigns/_events/_event_negotiation.md`, `vault/_templates/_campaigns/_events/_event_ritual.md` subtype forks) are identical by
design — every event, whatever its subtype, states its trigger/turn/outcome
and its aftermath the same way — and are not duplication to collapse. Each
subtype fork still needs its own template file: W54 discovers `type:` and
`subtype:` (and each one's required headings) per physical file in
`vault/_templates/`, so a subtype's middle section (Combatants, Cause, Parties &
Stakes, etc.) only registers as schema when it has a file of its own.

Monster is one template (`_srd/_monster.md`), not a fork between SRD and
homebrew (ADR-0040) — `statblock: inline
| transcluded` marks whether the stat block lives on the page itself or in
a separate `vault/_templates/_srd/_statblock.md` page. The `## Stats & Combat` heading
holds either form. No `vault/_templates/` fragment-transclusion mechanism covers
a plain heading + embed pair (only the `callout-*.md` files transclude,
and only for `> [!type]` callout boxes), so there is nothing to route the
transcluded case through instead.

`item` (`_srd/_item.md`) keeps its existing stat-line + `## Mechanics` +
`## Provenance` shape, grounded in the Forgotten
Realms Wiki's own item-article shape (infobox/stat-line, Powers,
ownership history). `spell` (`_srd/_spell.md`) is grounded in the 5e SRD
document itself, not an external wiki: its FR Wiki equivalent is in-world
lore prose, not the mechanical stat format this vault's spell pages
reproduce verbatim (`status: srd`, ADR-0014), so only the cross-cutting
`owner_skill:` convention applies to it, since a homebrew spell is `type: rule,
subtype: spell` (`rule-prep`) rather than an instance of this template.

`npc` (`_campaigns/_npcs/_npc.md`) is one shape regardless of `subtype:
major | minor | recurring`, grounded in the Forgotten
Realms Wiki's character-article genre (description, personality,
relationships, history), matching the read-aloud/Wants/Relationships/
Goals & Fronts shape already in play. The three pre-reorg drift forks
(_major_npc.md, _minor_npc.md, _hireling_npc.md) carried a different,
stale shape and are deleted.

`species` (`_srd/_species.md`) and `background` (`_srd/_background.md`)
are a second exception to external-wiki grounding, alongside `spell`:
their real standard is the 5e SRD's own mechanical species/background
format, not a narrative-wiki genre — this vault deliberately routes
cultural/narrative depth off both pages entirely (to `.claude/skills/draft-content/references/lore.md` or an
NPC's own page), so there is no FR Wiki article shape to ground against.
Both keep their existing shape; `subtype:` is free for a genuine shape
fork if one is ever needed.

`faction` (`_srd/_faction.md`) keeps its existing `## Members` +
`## Goals & Fronts` shape, grounded in the Forgotten
Realms Wiki's organization-article genre (description, membership,
activities, relations).

`quest` (`_srd/_quest.md`) is a third exception to external-wiki
grounding, alongside `spell`/`species`/`background`: the FR Wiki's
`Quest` namespace covers a spell, published game modules, and gamebooks
— no in-world "party's ongoing quest" article genre exists there. The
real external standard is GM-craft methodology this vault already cites
(the Alexandrian's Three-Clue Rule, Sly Flourish's LGMRD Secrets and
Clues) — the existing Secrets & Clues → Beats → Outcome shape holds.

`puzzle` (`_srd/_puzzle.md`) is a fourth exception, alongside `spell`/
`species`/`background`/`quest`: there is no FR Wiki "puzzle/trap
article" genre — the real standard is the 2024 DMG's own Trigger/
Effect/Countermeasures trap structure, extended by the
`writing-traps-trials` skill's craft methodology. The vault's
At a Glance→Surface (Immediate/Investigation/Mastery)→DM Truth→
Interaction→Consequences & Escalation→Bypasses & Exploits→Rewards &
Discoveries→Aftermath→Scaling Knobs shape maps onto the DMG core
while adding a mandatory no-roll bypass, escalation stages, world
aftermath, and scaling knobs as campaign-craft value beyond the DMG's
bare structure. `subtype:` (`puzzle | trap | hazard | trial |
composite`) classifies the dominant form.

`class`/`subclass` (`_srd/_class.md`, `_srd/_subclass.md`) are a fifth
exception: the 2024 SRD's own class-table format (Core Traits table,
Becoming a Class, a leveled Class Features table, per-level headings) is
the real standard, confirmed against a real 2024 SRD class entry —
matching the templates' existing shape exactly, down to heading names.
A homebrew class/subclass is `type: rule`
(`rule-prep`), a distinct, separately-scoped, currently thinner shape
not addressed by this pass.

`lore` (`vault/_templates/_srd/_lore.md`) is grounded in the Forgotten Realms Wiki's
history/legend article genre (prose, a History section; a genuine
`subtype: legend` carries multiple conflicting in-world accounts of the
same event, e.g. Asgorath's competing dragonborn-origin myths). The _lore_legend.md file was a dead 6-line
stub with no `type:`, no body, and no real content; deleted, with
`subtype: legend` folded into `vault/_templates/_srd/_lore.md` itself rather than kept as a
separate template.

`rumour` (`_campaigns/_lore/_lore_rumour.md`) is a sixth exception: not
an FR Wiki article genre, but the GM-craft rumour-table tradition
(Roleplaying Tips' column conventions, The Alexandrian's hexcrawl rumour
tables — a hook, a live question, a distortable true/false/
partially-true value) adapted into the vault's per-entity-page model.

`event` (`_campaigns/_events/_event*.md`, 9 files) splits: `battle`,
`disaster`, and `festival` are grounded in three genuinely distinct FR
Wiki article genres (Battle of Bones — combatant/casualty-shaped;
Spellplague — cause/effect-shaped; Shieldmeet — customs/attendee-shaped)
— real, structurally different exemplars, confirming these are genuine
forks, not drift. `arrival`, `negotiation`, `ritual`, and
`disappearance` did not surface as their own standalone FR Wiki article
genres in this pass; they remain distinct GM-craft functional shapes
(reception, stakes-and-terms, rite-and-effect, last-seen-and-leads) each
carrying real, non-overlapping structure, kept as their own templates
rather than collapsed into the base — a seventh exception shape, plural.
`war` is the ninth file: a war spans years, phases, and theatres, so it
separates who fought and led (`## Sides & Commanders`) from the war's
phased course (`## Campaigns & Phases`), grounded in World Anvil's
Conflict template, the FR Wiki's Blood War, and Wookieepedia's Galactic
Civil War. A single named engagement stays a `battle` page `within:` the
war.

`deity` (`_campaigns/_deity.md`) is grounded in the Forgotten Realms Wiki's
deity-article genre (Manifestations, Personality, Powers, Divine Realm,
Relationships, a Worshipers cluster of Dogma/Places of Worship/Rituals/
Holy Days/Notable Worshipers) plus the 2024 DMG's "Gods and Other Powers"
attribute set (Divine Rank, Home Plane, Provinces/Domains, Worshiper base,
Manifestation tendency), collapsed into this vault's existing lean
faction/npc shape (`## Portfolio & Presence`, `## Worship`). A church or
clergy with its own leadership is `type: faction`, linked by wikilink,
never absorbed; a myth or prophecy with no active-worship dimension stays
`type: lore`.

`culture` (`_campaigns/_culture/_culture.md`) is grounded in World Anvil's
Ethnicity and Tradition templates (cultural-trait drift, customs, beauty
ideals, festivals-as-institutions) and Patricia C. Wrede's Fantasy
Worldbuilding Questions "Peoples and Customs" section (birth/death customs,
greeting gestures, host/guest obligation, dress, manners). It never absorbs
a people's biology, which stays `type: species`, and never a single dated
happening, which stays `type: event` — a recurring institution (a festival
held every year) is written on the culture page itself, in
`## Customs & Traditions`.

`calendar` (`_campaigns/_calendar.md`) is grounded in Kanka's Calendar
entity (months/weekdays/current date required; moons, seasons, named
weeks, named years, intercalary months and leap years all optional) and
the Forgotten Realms Wiki's Calendar of Harptos (12 months of 3 tendays
each, 5 intercalary holidays including the quadrennial Shieldmeet leap
day). System, not sequence: `## Structure` states the recurring unit
shape a date is measured against; the actual chronological run of events
stays on a `lore` timeline page (`vault/campaigns/shattered-sea/lore/campaign-timeline.md`), never
duplicated here.

`threat` (`_campaigns/_threat.md`) is grounded in Dungeon World's Fronts
(Dangers, Grim Portents, Impending Doom, Stakes Questions), Fate Core's
Big Issues (Current vs. Impending), and the 2024 DMG's deliberately
minimalist Campaign Conflicts sheet. The Faction-vs-Threat boundary: a
danger with one clear organizational owner advancing it stays on that
faction's own `## Goals & Fronts`, never forked onto a `threat` page too;
a `threat` page exists only when the danger spans multiple factions or
NPCs, outlives whichever one started it, or has no organizational owner
at all — paired with "No Clock, No Threat" (`## Clock` is required) and
"Entangled, Not Owned" (`## Entangled Parties` never substitutes for an
owner).

`condition` (`_srd/_condition.md`) is grounded in World Anvil's Condition
template (diseases, mutations and transformations, phases of life, RPG
statuses, one flexible shape rather than a family) and the Forgotten
Realms Wiki's disease articles (transmission vectors — injury, ingestion,
inhalation, contact — and symptom timelines). The rule-vs-condition
boundary: `type: rule, subtype: condition` holds the numbers (DC, damage
dice, duration, RAW/homebrew precedent) with no in-world narrative;
`type: condition` holds the world-fact (what it is, how it spreads, what
it means) with no numbers, closing with a cross-link to its mechanical
counterpart page where one exists.

`document` (`_campaigns/_document.md`) is grounded in World Anvil's
Document template (books, letters, recordings, illustrations — anything
containing written or recorded content) and Call of Cthulhu's Mythos tome
convention (a tome as an in-world text with its own reading effect,
generalized here without importing Call of Cthulhu's own Sanity
mechanic). The Handout boundary: a `document` is the in-world text
itself, existing whether or not it's ever shown at the table; a `handout`
is that text staged as a physical table prop, transcluding
`![[<slug>#Text]]` from the document page rather than retyping it. A prop
invented purely for one scene, with no in-world history, stays a
`handout` alone.

`material` (`_srd/_material.md`) is grounded in World Anvil's Material
template (any substance or mixture something else is made out of, pure
or impure, living or non-living) and the Forgotten Realms Wiki's
substance articles (Mithral's ore-to-metal production process,
Belladonna's toxic reagent use, Elverquisst's per-unit trade price). Two
boundaries: a made, held, single thing is `item`; the substance it's made
from or out of, counted by weight or volume and traded as a commodity, is
`material`. For poison specifically, the tradeable good (dose, price,
application) is `material`; the effect on a victim is `condition`,
cross-linked rather than restated.

`profession` (`_srd/_profession.md`) is grounded in World Anvil's
Profession template (Workplace, Provided Services, Hazards, Career Path,
Compensation) and Title template (how a title is obtained, succession,
Accoutrements & Equipment, Removal or Dismissal), plus Wookieepedia's
Category:Occupations spanning honest trades to criminal and service work.
Two boundaries: "Job, Not Package" — `background` is the character-
creation mechanical package, a `profession` is the in-world job any
number of NPCs can hold; "Setting-Wide, Not Guild-Internal" — a rank
meaningful only inside one faction's own membership stays on that
faction's page, a `profession` page exists only for a trade or title
recognised beyond one organisation.

`route` (`_campaigns/_route.md`) is grounded in the 2024 DMG's Travel
Planner (terrain, pace, distance, encounter distance, forage/navigate/
search DCs), Traveller RPG's trade-route concept (transit points, ports,
dynamic routing), and the Alexandrian's hexcrawl wilderness-travel rules
(watch-based time tracking, known-trail vs. wilderness navigation DC
delta). Two boundaries: "Leg-vs-Place" — `location` owns a place stood
in, `route` owns the crossing between places; the Encounter-Table
boundary — `table` owns random encounter tables, `## Travel`/`## Hazards`
link to one by wikilink rather than restating its rows.

`culture:language` (`_campaigns/_culture/_culture_language.md`) is a
subtype fork off `culture`'s own spine, grounded in World Anvil's
Language template (a Structure/Common-usage split, geographic
distribution, name examples) and the Forgotten Realms Wiki's Elven-
language article (script — Espruar — plus named dialects such as Sea
Elvish and Sylvan Elvish). It forks `## Naming` outward into
`## Script & Speech`, `## Speakers & Dialects`, and
`## Sample Phrases & Names` while inheriting the parent's frontmatter
spine and `## The Language` framing unchanged, the same fixed-fork
convention as `vault/_templates/_campaigns/_events/_event_battle.md`'s siblings.

`ship` (`_srd/_ship.md`) is dual-grounded: a Forgotten Realms Wiki
vessel-biography genre (Sea Sprite — history, notable crew, final fate)
for its narrative shell, plus the real 2024 vehicle stat-block format
(D&D Beyond's Sailing Ship entry — component table of Hull/Helm/Sails/
weapons, each with its own AC/HP) for its `## Stats & Combat` body table
— confirmed against both real sources, matching the template's existing
two-genre split exactly.

`table` (`_refs/_table.md`) is grounded in the same SRD/DMG d100-table
format as its sibling exceptions — confirmed against the real SRD
trinkets table.

`statblock` (`_srd/_statblock.md`) is an eighth exception: its real
standard is the Fantasy Statblocks Obsidian plugin's own codeblock
schema (`vault/refs/vault/monster/references/statblock-format.md`), not the
2024 Monster Manual's redesigned layout (Initiative/Habitat/Treasure/
Gear/consolidated Immunity) confirmed via WotC's own preview post — the
plugin's fields predate that redesign but the guide already documents
2014/2024 grammar support inside `desc:` strings. It is the transcluded
form `_srd/_monster.md`'s `statblock: transcluded` case embeds via
`![[<slug>-statblock]]`, not a duplicate of it — pure mechanics only, no
read-aloud, no lore, no ecology.

`secret` (`_campaigns/_secret.md`, `_campaigns/_secret_cache.md`) is
grounded in World Anvil's Secrets entity — a discrete, reusable content
chunk created apart from the article it attaches to, carrying its own
reveal permission rather than living inline — which is why a concealment
earns a page of its own with a `within:` host rather than a paragraph on
the host page. Its `## Discovery` two-check shape is the 2024 rules'
secret-door structure: Perception finds that something is there (the thin
seams that betray a door), Investigation works out the trick that opens it,
the second check written only when defeating the concealment is a separate
act from spotting it. No Obsidian-vault template for a hidden feature
exists to reuse (obsidianttrpgtutorials.com's full world-building and
mechanical template lists carry none) — a genuine no-Obsidian-exemplar
case, same class as `season`. `subtype: cache` is the fixed fork for a
concealment that stores things, adding `contains:` and the requirement that
the Reveal box resolve to real item pages; it stays distinct from the DMG's
treasure/rarity roll tables (Random Treasure Hoard, Magic Item Rarities),
which generate a hoard's value and rarity when an encounter is defeated,
confirmed via the Alexandrian's "Rolling Treasure in 2024" as an
orthogonal concern, not a competing standard. The boundary against the
four other places secret-shaped content lives — `_srd/_quest.md`'s Secrets
& Clues, `_episodes/_session_run_guide.md`, `_campaigns/_reference_spoilers.md`,
and `lore`'s rumour subtype — is physical placement: only a `secret` page
has a concealment to defeat at a fixed location, so only it carries a
`## Discovery` check (`docs/rulings/0002-secret-subsumes-loot.md`).

`handout` (`_handouts/_handout.md`) is a ninth exception: not an FR Wiki
genre and no formal TTRPG-specific handout standard exists (Sly
Flourish's "Making Great Handouts," Forst Stories' letter/investigation-
document templates) — the real grounding is genre-of-real-document
convention, handled per-document by prose craft rather than page-schema.
A handout is never SRD content.

`encounter` (`_campaigns/_encounter.md`) is an eleventh exception: its
real standard is DMG 2024 encounter-building guidance plus Sly Flourish's
Lazy Encounter Benchmark (¼/½/¾/1× CR-vs-level formula) — confirmed
against real published sources, matching `encounter-prep`'s own already-
correct citations. Still owned directly by
`.claude/skills/encounter-prep/SKILL.md` (not yet migrated to a draft
guide — a real ADR-0031 candidate, deferred given its size, ~1300 lines
across 14 files).

`season` (`_episodes/_season.md`) is a twelfth exception, and the first
with genuinely no external genre at all: GM-craft literature names this
grouping "arc" (TTRPGList), "act" (The Alexandrian), or "episode" (Sly
Flourish) — never "season." Grounded honestly in that arc/front
methodology instead of a fabricated wiki or TV-season precedent.
`season-prep` migrated to
`.claude/skills/draft-content/references/season.md` (ADR-0031) and deleted.

`campaign` (`_campaigns/_campaign.md`, `_campaigns/_reference_spoilers.md`,
`_campaigns/_reference_threads.md`) is a thirteenth exception: Six Truths is Sly
Flourish's real, named technique (*Return of the Lazy Dungeon Master*
ch. 16, "six" a convention not a hard count) — already correctly cited
in-repo. Icons is a simplified, non-mechanical adaptation of 13th Age's
Icons concept (name/idea only, never its relationship-dice mechanic) —
now attributed. `campaign-prep` migrated to `.claude/skills/draft-content/references/campaign.md`
(ADR-0031) and deleted. `_campaigns/_reference_spoilers.md`/`_campaigns/_reference_threads.md`
stay owned directly by `world-update` (derived-index pages, not
drafted content).

`world` (`_world.md`) is grounded in the Forgotten Realms Wiki's
Toril/Abeir-Toril setting-index article genre (naming/identity →
geography index → cosmology/history) — confirmed against real fetched
content, matching the template's Overview→Geography→Cosmology &
Planes→History & Calendar shape exactly, including the "index, don't
detail" convention (a region with real detail gets its own location
page). `parent:` replaced with `within:`.

`pc-sheet` (`_campaigns/_pcs/_pc.md`, `_campaigns/_pcs/_pc_sheet.md`, `_campaigns/_pcs/_pc_interview.md`,
`_campaigns/_pcs/_player.md`) splits like `ship`: `_campaigns/_pcs/_pc.md`'s narrative hub is the same
FR Wiki character-article genre already confirmed for `npc` (a real
adventurer's FR Wiki article — Drizzt Do'Urden — gets identical
description/history/relationships treatment to any NPC), so `_campaigns/_pcs/_pc.md`
gains a `## Relationships` heading for parity with `_campaigns/_npcs/_npc.md`, previously
missing. `_campaigns/_pcs/_pc_sheet.md`'s mechanical fields are the SRD/2024-character-
sheet-format exception, same category as `species`/`background`.
`_campaigns/_pcs/_pc_interview.md`/`_campaigns/_pcs/_player.md` are process/roster artifacts, no genre.
`_campaigns/_pcs/_pc.md`/`_campaigns/_pcs/_pc_interview.md`/`_campaigns/_pcs/_player.md` owned directly by
`dnd5e-character-interview`, `_campaigns/_pcs/_pc_sheet.md` by `combat-profiles` — both
established, non-stale skills, not migrated.

`combat-profile` (`_campaigns/_pcs/_pc_combat_profile.md`,
`_campaigns/_pcs/_party_combat_profile.md`, plus satellite pages `_campaigns/_pcs/_pc_stats.md`,
`_campaigns/_pcs/_pc_abilities.md`, `_campaigns/_pcs/_pc_spells.md`, `_campaigns/_pcs/_pc_inventory.md`) is entirely this
repo's own methodology (DM ruling, 2026-08-07) — no external grounding
pass applies, unlike every other type above. The PC template collapsed from 8 sections to 5 (Fast Read, Combat Stats,
Counters & Synergy, Session Combat Log, Calibration) and the party
template from 8 to 5 (Fast Read, Combined Combat Table, Weakness Map,
Effective CR Band, Encounter Design Parameters) — folding Offensive/
Defensive/Resource-Economy into one table, Synergy Hooks into Counters,
Calibration Notes into one terse section — for an ultra-minimal,
agent-consumable data page over the prior prose-heavy shape. All six
files owned directly by `.claude/skills/combat-profiles/SKILL.md` (not
migrated — a derived-data producer, not a page-drafting guide, so
ADR-0031's skill-to-guide move doesn't apply here).

`_refs/*` (`_refs/_agent_guidance.md`, `_refs/_reference.md`, `_refs/_runbook.md`,
`_refs/_guide.md`, `_refs/_craft.md`) are the five agent-facing templates owned by
`writing-for-agents`, grounded against a Claude Code methodology rather
than a wiki genre or SRD/DMG source. Every one is nearly identical in
frontmatter (governed spine), differing only in subject (runbook = steps,
everything else = reference of a given kind). Each type has its own
dedicated template file (`_refs/_agent_guidance.md` for `type: agent-guidance`,
`_refs/_reference.md` for `type: reference`, etc.) — the `type:` values
(`agent-guidance`/`reference`/`runbook`/`guide`/`craft`) are preserved
across 235+ real pages and `w95-type-folder-placement`'s lint mapping.
`_refs/_ref.md` itself still exists as the governed-spine authority (W55,
`loadDefaultSpine` in `utils/wiki-cli/src/wiki_cli/rules/lib/templates.mjs`) but is
no longer the right file for a page author to instantiate. _subagent_ref.md
and _skill.md were not part of the split: the former's Claude-Code-native
frontmatter remains incompatible with the governed spine; the latter had zero
real usages repo-wide (skills are authored as `.claude/skills/*/SKILL.md`,
never instantiated from a template).

`_episodes/_session_*.md` (recap, world-turn, ingest-review, highlights,
fork, history, moment, run-guide) is the second phase-2 group: the
session pipeline's phase-artifact templates, each ground checked
independently rather than by analogy to a sibling. `recap`/`highlights`
(`recap-writer`) and `run-guide` (`draft-run-guide`) confirm against
Sly Flourish's real, named Eight Steps of Lazy RPG Prep and the TV-
episode "previously on" recap convention (Dungeon Solvers, The Angry
GM). `world-turn` (`world-update`) confirms against Dungeon World's real
"Front" mechanic (linked threats, off-screen advancement), previously
uncited in-repo. `moment` (`draft-moment`) and `fork` (`draft-fork`) checked against the
Alexandrian's node-based scenario design and found to genuinely diverge
from it (the Alexandrian explicitly argues against branching structures)
— a no-external-genre case, this repo's own methodology, same class as
`season`/`combat-profile`. `ingest-review` (`transcript-ingest`) and
`history` (`session-history-prep`) are pure internal artifacts (a
machine-ingest checkpoint, a read-derived compile) with no TTRPG or
GM-craft analog — also no-external-genre. All eight gain
`owner_skill:`; `history`'s stale `author: hb` key is removed, same
move `item`/`species`/`background` already made. The ninth file,
_session_prep.md, was a dead Obsidian-community-starter-kit stub
(Lorem ipsum body, wikilinks to a note that was never a real vault
page) superseded entirely by `run-guide`'s own real implementation of
the same Eight Steps — deleted, not migrated.

`_plugins/_callout_*.md` (dialogue, read-aloud, check, generic, mechanic,
spoiler) plus `_plugins/_leaflet.md` is the third phase-2 group: Obsidian-plugin
syntax fragments, grounded against the plugin's own real documentation
rather than a wiki genre. Every callout swap-type in `_plugins/_callout_generic.md`
is a real Obsidian built-in type or documented alias (obsidian.md/help/
callouts, fetched live); `check` is specifically a reserved alias of the
built-in `success` type, restyled via `custom-callouts.css` — a
documented naming collision, not a defect. The five custom types
(dialogue/read-aloud/mechanic/spoiler, plus `check`'s override) use
Obsidian's real `[!type]` extensibility mechanism, confirmed against
`vault/.obsidian/snippets/custom-callouts.css`'s `data-callout` rules —
not invented syntax. All six are owned by `callouts`
(`.claude/skills/callouts/SKILL.md`). `_plugins/_leaflet.md` is
grounded against the real `javalent/obsidian-leaflet` plugin's own
README (fetched) — every field it carries (id/image/bounds/height/
width/lat/long/minZoom/maxZoom/zoomDelta/defaultZoom/unit/scale) is
real and documented, none invented; a cosmetic `minZoom:5` spacing
drift (missing space, inconsistent with every sibling key) is fixed.
Owned by `obsidian-leaflet` (`.claude/skills/obsidian-leaflet/SKILL.md`).
All seven gain `owner_skill:`
frontmatter for the first time (none had any); each retires its old
opener-line prose naming the owning skill, moving that fact into
frontmatter per ADR-0040.

The fourth and final phase-2 group had no shared kinship — eight files
grouped only by "everything left," each grounded or resolved on its own
merits. _default.md (the former governed-spine authority template) is
deleted — DM ruling, follow-up to this pass. `_srd/_rule.md` is the named "largest
known real gap" — confirmed via a live 2024-DMG homebrew-spell-guidance
fetch (thegamer.com) that the real standard is materially richer
(explicit numeric ceiling, named RAW precedent) than the old two-heading
shape. Reshaped: `class`/`subclass`/`background`/`species`/`spell`
subtypes now route to their own already-real, already-dedicated
templates (`_srd/_class.md` etc. — DRY, not duplicated here); only
`feat`/`condition`/`subsystem` (genuinely no dedicated template exists)
keep the generic Mechanics/Provenance shape, thickened with the DMG's
numeric-ceiling-plus-precedent convention. Gains `owner_skill:`
(`rule-prep`); stale `author: hb` removed.
`_handouts/_va_script.md` confirms against the real VO-industry slate
convention (a spoken self-introduction opening a real audition, per
getcleveraboutvo.com/voquent.com) layered under this repo's own roast
structure. `_campaigns/_pcs/_pc-gallery.md` is a no-external-genre
case, same honest call as `season` — a personal photo gallery has no
TTRPG convention to ground against; `visual-aids`'s own placement
convention is the real internal standard. Both gain `owner_skill:`,
retiring their opener-line prose;
`_campaigns/_pcs/_pc-gallery.md`'s stale `author: hb` is removed the same way `history`'s
was.

_gallery.md is deleted, not migrated: an unowned, zero-instance
duplicate of `_campaigns/_pcs/_pc-gallery.md` (repo-wide grep found no real page using
it, and `visual-aids`'s own placement table has no generic-gallery row).

`_ideas/_idea.md` and `_stories/_story.md` are a fourteenth exception,
alongside `season`/`combat-profile`: no external genre grounds a
mid-development idea or a pre-canon draft chapter as a wiki-page type —
the real standard is the zettelkasten fleeting-note (atomic, unstructured,
append-only capture) and the novelist's raw-draft-before-outline
convention, both real, named, external practices distinct from this
vault's governed page schema. Both templates carry only an optional
`owner_skill:` key over three keys that are
required on every real page of either type: `type:` (`story` or
`idea`), `created:`, and `updated:`. Any further key is optional, matching
`draft-story` and `colab-on-idea` (`.claude/skills/draft-story/references/fragments.md`,
`.claude/skills/draft-story/references/hard-rules.md`). Owned directly by `draft-story` (`_stories/_story.md`) and `colab-on-idea`
(`_ideas/_idea.md`) — `draft-story`'s `.claude/skills/draft-story/references/fragments.md` still owns
the fragment-capture *format* both skills write to, since `draft-story`'s
own entry-points table reaches it too.

#### Session Log sections

No template scaffolds a `## Session Log` heading and no page carries one
until the entity actually appears in a session: the section is born when
the first real entry lands (transcript-ingest's write), one line per
session, most recent first. An absent section IS the record of "no
appearances yet" — never write a placeholder line to say so (W48, error).

#### Enum comments

A frontmatter key's trailing `#` comment defines its **closed enum** when,
after an optional `OPTIONAL —` prefix, the comment *begins* with a pipe
run of 2+ tokens (`a | b | c`; tokens may contain spaces). The enum ends
at the first `;`, ` — `, or `,` — prose may follow. `e.g.` before the
pipes marks an **open example list** (not validated); a comment with no
leading pipe run is prose (not validated). W54 reads every closed enum
from the templates at lint time and validates page frontmatter against it
— to add or change an allowed value, edit the template comment; no script
changes. Each per-type template owns its own enum comment on every key
it carries (`_srd/_ship.md`'s `tier` differs from every other type's). `status` and
`publish` are W2's (`STATUS_ENUM` in `wiki.toml` `[thresholds]`),
never enum-comment-validated.

#### Lint-rule constants

Vault-wide constants (status enum, page-length caps, term lists, callout
caps) live in `wiki.toml` `[thresholds]`, read by
`utils/wiki-cli/src/wiki_cli/rules/lib/templateConstants.mjs` at lint time — not
per-type content, so they're declared once there rather than duplicated
per template or hardcoded per rule.

**`CATALOG_EXCLUDED_TYPES` is currently empty** — no `type:` is exempt
from Wiki-catalog completeness (W24). `guide` and `table` pages are
vendored/generated reference material (5e SRD across
`vault/srd/monsters/`, `vault/srd/spells/`, `vault/campaigns/shattered-sea/items/`,
`vault/srd/classes/`, `vault/srd/feats/`, `vault/srd/species/`,
`vault/srd/backgrounds/`; craft guidance across `vault/refs/**` —
`vault/refs/stories/`, `vault/refs/ideas/`, per-type `vault/refs/vault/<type>/references/`, and
flat top-level files including `table-*.md`) with no page schema of their own — advisory, not
canon (`llm-wiki` skill) — but a hand-curated catalog for that tree would
track a third-party corpus the wiki does not author, not campaign content,
so DM ruling 2026-07-25 (`.claude/rules/external-guides.md`) put it in
scope like any other page instead of carving out a catalog exemption.
