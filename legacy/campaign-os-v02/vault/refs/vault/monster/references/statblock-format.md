---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "Fantasy Statblocks codeblock syntax for Obsidian: required/optional fields, SRD wording patterns enforced by dndsim lint, the sim: extension namespace for combat simulation, bestiary recall, and plugin gotchas."
created: "2026-08-03"
updated: "2026-08-10"
tags: [combat]
uid: 2cb66c75-ec98-489c-a26c-57d0fa766beb
---

# Stat block format (Fantasy Statblocks plugin)

Load when writing or fixing an actual `statblock` codeblock — the syntax
that renders as a playable stat block in Obsidian.

This vault has the **Fantasy Statblocks** community plugin
(`obsidian-5e-statblocks`) installed, confirmed via
`.obsidian/community-plugins.json`.

General plugin mechanics beyond this creature-scoped schema — config keys,
layouts, and how the bestiary actually gets populated — live in the
`obsidian-fantasy-statblocks` skill instead.

---

## Where it lives on the page

A `type: monster` page (`.claude/skills/draft-content/references/monster.md`) is always
inline: the codeblock is written directly on the creature page itself,
under `## Statblock`, no separate page. An NPC or encounter page's stat
block is always its own separate page instead, embedded via a bare-slug
`![[<slug>-statblock]]` (Obsidian resolves by basename, no directory
prefix):

- **Named NPC with combat stats** → a statblock page, embedded under
  `## Stats & Combat` on the NPC's own page (`.claude/skills/draft-content/references/npc.md`
  owns NPC page creation; this file only covers the codeblock syntax
  itself).
- **One-off creature for a single encounter** →
  `vault/campaigns/shattered-sea/monsters/<slug>-statblock.md`, embedded
  on that encounter page's own Enemy Roster / Stats & Combat section.

A `vault/_templates/_srd/_statblock.md` page is pure mechanics — no read-aloud, no lore, no
ecology; that content stays on the creature/NPC page that embeds it.

## Minimal viable 5e stat block

```statblock
layout: Basic 5e Layout
name: Goblin Scout
size: Small
type: humanoid
alignment: neutral evil
ac: 15
hp: 7
hit_dice: 2d6
speed: "30 ft."
stats: [8, 14, 10, 10, 8, 8]
cr: 1/4
actions:
  - name: Scimitar
    desc: "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) slashing damage."
```

`stats:` is `[STR, DEX, CON, INT, WIS, CHA]` in that fixed order.

## Required fields

| Field | Example |
|---|---|
| `name` | `"Ancient Red Dragon"` |
| `size` | `Tiny`/`Small`/`Medium`/`Large`/`Huge`/`Gargantuan` |
| `type` | `humanoid`, `beast`, `monstrosity`, `undead`, `fiend`, `celestial`, `dragon`, `elemental`, `fey`, `giant`, `construct`, `ooze`, `plant`, `aberration` |
| `alignment` | `"neutral evil"` |
| `ac` | `15` or `"15 (natural armor)"` |
| `hp` | `136` |
| `hit_dice` | `"16d10 + 48"` |
| `speed` | `"30 ft., fly 60 ft."` — always quote |
| `stats` | `[20, 10, 16, 12, 14, 16]` |
| `cr` | `5` or `"1/2"` — quote fractions |

## Common optional fields

```yaml
saves:
  - Dex: +5
skillsaves:
  - Perception: +7
damage_resistances: "cold; bludgeoning, piercing, and slashing from nonmagical attacks"
damage_immunities: "poison, psychic"
condition_immunities: "charmed, frightened, poisoned"
senses: "darkvision 60 ft., passive Perception 17"   # always include passive Perception
languages: "Common, Goblin"
traits:
  - name: "Pack Tactics"
    desc: "..."
actions:
  - name: Multiattack
    desc: "..."
  - name: Fire Breath
    desc: "..."
    usage: { times: 1, per: day }
bonus_actions: [...]
reactions: [...]
legendary_actions:
  - name: ""
    desc: "The creature can take 3 legendary actions..."   # first entry = blank-name preamble
  - name: "Detect"
    desc: "..."
lair_actions:
  - desc: "On initiative count 20 (losing initiative ties)..."
```

## WotC wording patterns — keep them exact

Official phrasing is unambiguous under 5e rules; an improvised rewording
routinely introduces a rules question mid-combat (does this crit? does it
stack?) that the canonical phrasing already answers. It also keeps the
sim parseable: action `desc` strings must keep the SRD attack grammar
("+X to hit … Hit: N (XdY+Z) type damage"), enforced by `dndsim lint`'s
`W-statblock-simulatable` rule (`utils/dndsim/src/dndsim/lint/rules.py`)
on every edit (reactions exempt — prose there is encoded via
`creature_overrides` at sim time).

**Melee attack:**
> Claws. Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 13
> (2d8 + 4) slashing damage.

**With a rider:**
> Bite. Melee Weapon Attack: +9 to hit, reach 5 ft., one creature. Hit: 18
> (3d8 + 5) piercing damage, and the target is [[grappled|grappled]] (escape DC 17).
> Until this grapple ends, the target is [[restrained|restrained]], and the [name] can't
> bite another target.

**Save-based cone/sphere:**
> Acid Breath (Recharge 5–6). The [name] exhales acid in a 30-foot cone.
> Each creature in that area must make a DC 14 [[dexterity|Dexterity]] saving throw,
> taking 49 (11d8) acid damage on a failed save, or half as much damage on
> a successful one.

**Save-or-suffer, no damage:**
> Paralyzing Gaze. The [name] targets one creature it can see within 30
> feet. The target must succeed on a DC 14 [[wisdom|Wisdom]] saving throw or be
> [[paralyzed|paralyzed]] until the end of the [name]'s next turn. The target can
> repeat the saving throw at the end of each of its turns, ending the
> effect on itself on a success.

**Pack Tactics:**
> Pack Tactics. The [name] has advantage on an attack roll against a
> creature if at least one of the [name]'s allies is within 5 feet of the
> creature and the ally isn't [[incapacitated|incapacitated]].

**Regeneration:** `Regeneration. The [name] regains [X] hit points at the
start of its turn. If the [name] takes [acid or fire] damage, this trait
doesn't function at the start of the [name]'s next turn. The [name] dies
only if it starts its turn with 0 hit points and doesn't regenerate.`

## The `sim:` extension namespace

dndsim reads one custom key the Fantasy Statblocks plugin
itself ignores (safe to add — the plugin already tolerates unknown keys
like `dice:`/`bestiary:` alongside creature data): `sim:`, at the top level
and per-action.

Top-level `sim:` carries what the native fence vocabulary can't: `side:
party | enemy` (required on a PC page — this is what makes a page a PC
rather than a monster; absent on a creature/NPC page defaults to
`enemy`), `resources:` (recharge pools), `abilities:` (always-available
capabilities in the loadout-modifier vocabulary — Hex, GWM, Pack Tactics
reactions...), `save_advantage:`, `concentration_save:`, `initiative:`,
`crit_range:`, `routine:` (turn preference order).

Per-action `sim:` (on any `actions:`/`bonus_actions:`/`reactions:`/
`legendary_actions:` entry) carries `id` (a stable ref for `routine:`/
reaction lookups), `cost`, `concentration`, `on_success`/`on_fail`
(replaces — never merges with — the prose-parsed outcome, for a rider the
SRD grammar can't express), a `heal: { dice }` (routes the entry to heals
instead of actions), and reaction mechanics (`kind`, `die`, `attack`,
`bonus`, `trigger`).

Full schema and worked example: `utils/dndsim/CLAUDE.md`. `utils/dndsim/`'s
importer reads the identical fence and `sim:` namespace; its docs
are the source of truth for its CLI, not the schema (the
fence stays the one authored artifact both engines compile from —
`docs/adr/0009`).

**Both 2014 and 2024 SRD attack/save grammar parse** — `Melee Weapon
Attack: +X to hit ... Hit: N (dice) type damage` (2014) and `Melee Attack
Roll: +X, reach ... N (dice) Type damage` / `<Ability> Saving Throw: DC N
... Failure: ... Success: ...` (2024) are both permanently supported,
auto-detected per action — write whichever phrasing matches the source
you're transcribing (a reskinned SRD 2024 monster, homebrew in traditional
2014 phrasing).

## Codeblock config keys (rendering, not creature data)

```yaml
layout: Basic 5e Layout   # exact string match required — see landmine below
dice: true                # clickable dice rollers
columns: 2                 # split into columns; add forceColumns: true for big blocks
bestiary: true              # false = exclude from bestiary/Initiative Tracker
```

## Bestiary wiring

```yaml
---
statblock: inline
name: Goblin Shaman   # MUST match the codeblock name: exactly
---
```

Every `vault/srd/monsters/` or `vault/campaigns/shattered-sea/monsters/` statblock page carries
this — `statblock: inline` in frontmatter
registers the note's first `statblock` codeblock in the plugin's bestiary, making it
recallable by name in any other note (`monster: Goblin Shaman`). Registration
mechanics beyond this (recall, the plugin's bundled 5e SRD, alternate creation
methods) live in `.claude/skills/obsidian-fantasy-statblocks/references/bestiary-and-recall.md`.

**Recall + override** (SRD or a previously-registered homebrew creature):

```statblock
layout: Basic 5e Layout
monster: Goblin
name: "Goblin Boss"
hp: 21
cr: 1
traits+:
  - name: "Redirect Attack"
    desc: "When targeted by an attack, the boss redirects it to an adjacent goblin."
```

`traits+:` / `actions+:` **append** to the inherited list; a bare
`traits:` / `actions:` **replaces** the entire inherited list — this is
the plugin's single biggest silent-failure trap. Remove a specific
inherited entry by name with `actions-:` (`- name: Scimitar`).

## Plugin landmines (fail silently, no error shown)

- **`layout:` is case-and-space exact.** `"Basic 5e Layout"` typo'd any
  way silently falls back to the default layout. Verify against Settings →
  Statblock Layouts before trusting it.
- **`extends:`/`monster:` + a bare list field replaces, doesn't merge**
  (see above) — the #1 "my inherited actions disappeared" bug.
- **Unquoted colon inside a string breaks YAML parsing** — `desc: Melee
  Attack: +4` is invalid; quote the whole value.
- **Frontmatter `name:` must exactly match codeblock `name:`** or bestiary
  registration silently fails.

## Recall vs. write from scratch

| Situation | Approach |
|---|---|
| SRD creature, changes are <50% of fields | `monster: <SRD Name>` + override changed fields |
| Homebrew with no SRD analog | Write full stat block from scratch |
| SRD base but >50% of fields differ | Write from scratch — recall noise outweighs value |
| Reskin (same math, new flavor) | `monster:` recall, override `name`/`desc` flavor text only, keep numbers |
| No SRD analog, but a variant/template fits | `vault/refs/vault/monster/references/reskin-templates.md` — elemental/dire/fiendish/spell-infused/undead templates, or a general-use base block (Minion CR 1/8–Champion CR 15) |

**Reskin bias.** Prefer a published creature reskinned over inventing new
math: a pirate enforcer is a [[bandit-captain|Bandit Captain]], a sea-hag cult leader is a
[[sea-hag|Sea Hag]]. Only write a full custom stat block (`vault/refs/vault/monster/references/cr-design.md`) when
the mechanical concept genuinely doesn't exist in print.
