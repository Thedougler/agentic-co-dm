# Statblock → Foundry field mapping

Vault statblocks use Obsidian Fantasy Statblocks YAML inside
` ```statblock ` fences. This reference maps each field to
`dnd5e-create-npc` parameters with concrete extraction patterns.

## Full example

Given this statblock YAML:

```yaml
name: River Otter
size: Small
type: beast
alignment: unaligned
ac: 12 (natural armor)
hp: 11 (2d6+4)
stats: [10, 15, 14, 4, 12, 6]
speed: 30 ft., swim 40 ft.
senses: darkvision 30 ft.
cr: 1/4
skillsaves:
  - perception: 3
  - stealth: 4
languages: "--"
traits:
  - name: Hold Breath
    desc: "Can hold its breath for 10 minutes."
actions:
  - name: Bite
    desc: "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4+2) piercing damage."
```

The `dnd5e-create-npc` call is:

```json
{
  "name": "River Otter",
  "creatureType": "beast",
  "size": "small",
  "alignment": "unaligned",
  "cr": "1/4",
  "hpAverage": 11,
  "hpFormula": "2d6+4",
  "acMode": "flat",
  "acValue": 12,
  "abilities": {"str": 10, "dex": 15, "con": 14, "int": 4, "wis": 12, "cha": 6},
  "walkSpeed": 30,
  "swimSpeed": 40,
  "darkvision": 30,
  "skills": [
    {"skill": "Perception", "proficiency": "proficient"},
    {"skill": "Stealth", "proficiency": "proficient"}
  ],
  "sourceRules": "2024"
}
```

## Extraction patterns

### AC — always use flat mode

`ac: 14 (natural armor)` → `acMode: "flat"`, `acValue: 14`

Parse the number before any parenthesized description. Always use
`acMode: "flat"` for creature imports.

### HP — split average from formula

`hp: 32 (5d8+10)` → `hpAverage: 32`, `hpFormula: "5d8+10"`

The number before parens is average. The string inside parens is formula.

### Ability scores — positional array

`stats: [STR, DEX, CON, INT, WIS, CHA]`

Index 0 = str, 1 = dex, 2 = con, 3 = int, 4 = wis, 5 = cha.

```json
"abilities": {"str": 16, "dex": 14, "con": 14, "int": 3, "wis": 12, "cha": 6}
```

### Speed — split on comma

`speed: 30 ft., fly 60 ft., swim 30 ft.`

- Bare number → `walkSpeed: 30`
- "fly N ft." → `flySpeed: 60`
- "swim N ft." → `swimSpeed: 30`
- "burrow N ft." → `burrowSpeed: N`
- "climb N ft." → `climbSpeed: N`

### Senses — split on comma, ignore passive Perception

`senses: darkvision 60 ft., passive Perception 14`

- "darkvision N ft." → `darkvision: 60`
- "blindsight N ft." → `blindsight: N`
- "tremorsense N ft." → `tremorsense: N`
- "truesight N ft." → `truesight: N`
- "passive Perception" → skip (derived from skills)

### Saves

`saves: [{ dex: 5 }, { wis: 3 }]`

Extract just the ability keys: `savingThrows: ["dex", "wis"]`

### Skills

`skillsaves: [{ perception: 3 }, { stealth: 4 }]`

Map to title case with proficiency level:

```json
"skills": [
  {"skill": "Perception", "proficiency": "proficient"},
  {"skill": "Stealth", "proficiency": "proficient"}
]
```

Use `"expert"` only when the modifier is significantly higher than
proficiency bonus + ability modifier would produce (roughly double
proficiency bonus).

### Damage/condition arrays

Direct pass-through as arrays of lowercase strings:

```json
"damageImmunities": ["fire", "poison"],
"damageResistances": ["bludgeoning"],
"damageVulnerabilities": ["cold"],
"conditionImmunities": ["poisoned", "frightened"]
```

### Languages

```json
"languages": ["Common", "Draconic"],
"languagesCustom": "telepathy 60 ft."
```

Split telepathy and other non-standard language entries into
`languagesCustom`. A `"--"` means no languages — omit the parameter.
