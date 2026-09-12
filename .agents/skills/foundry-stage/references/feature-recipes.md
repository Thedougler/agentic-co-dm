# Feature recipes

Exact `dnd5e-add-feature` call patterns for each feature type. Copy the
JSON shape, fill in the fields from the statblock description.

## How to pick the feature type

Read the action/trait description and match top-down (first match wins):

1. Contains "Weapon Attack:" AND "saving throw" → **attack-with-save**
2. Contains "Weapon Attack:" → **attack**
3. Contains "DC" and "saving throw", no attack roll → **save**
4. Everything else → **passive**

## Attack

Description pattern: `Melee Weapon Attack: +5 to hit, reach 5 ft., one
target. Hit: 8 (1d10+3) piercing damage.`

```json
{
  "featureType": "attack",
  "actorIdentifier": "Wolfrabbit",
  "featureName": "Bite",
  "attackType": "melee",
  "damageParts": [
    {"number": 1, "denomination": 10, "type": "piercing", "bonus": 3}
  ],
  "reachFt": 5,
  "description": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 8 (1d10+3) piercing damage."
}
```

Extraction:
- "Melee" → `attackType: "melee"` / "Ranged" → `attackType: "ranged"`
- "reach 5 ft." → `reachFt: 5`
- "range 30/120 ft." → `rangeFt: 30`, `longRangeFt: 120`
- "1d10+3 piercing" → `damageParts: [{number: 1, denomination: 10, type: "piercing", bonus: 3}]`
- Multiple damage types → multiple entries in `damageParts`

## Save

Description pattern: `Each creature in a 15-foot cone must make a DC 13
Dexterity saving throw, taking 14 (4d6) fire damage on a failed save, or
half as much on a successful one.`

```json
{
  "featureType": "save",
  "actorIdentifier": "Young Dragon",
  "featureName": "Breath Weapon",
  "saveAbility": "dex",
  "saveDC": 13,
  "damageParts": [
    {"number": 4, "denomination": 6, "type": "fire"}
  ],
  "halfOnSave": true,
  "areaType": "cone",
  "areaSize": 15,
  "activationType": "action",
  "description": "Each creature in a 15-foot cone must make a DC 13 Dexterity saving throw..."
}
```

Extraction:
- "DC 13" → `saveDC: 13`
- "Dexterity saving throw" → `saveAbility: "dex"`
- "half as much" → `halfOnSave: true`
- "15-foot cone" → `areaType: "cone"`, `areaSize: 15`
- "30-foot line" → `areaType: "line"`, `areaSize: 30`
- "10-foot-radius sphere" → `areaType: "sphere"`, `areaSize: 10`

## Attack-with-save

Description pattern: `Melee Weapon Attack: +5 to hit, reach 5 ft., one
target. Hit: 7 (1d6+4) piercing damage. The target must succeed on a
DC 12 Constitution saving throw or take 7 (2d6) poison damage.`

```json
{
  "featureType": "attack-with-save",
  "actorIdentifier": "Giant Spider",
  "featureName": "Bite",
  "attackType": "melee",
  "damageParts": [
    {"number": 1, "denomination": 6, "type": "piercing", "bonus": 4}
  ],
  "reachFt": 5,
  "saveAbility": "con",
  "saveDC": 12,
  "saveDamageParts": [
    {"number": 2, "denomination": 6, "type": "poison"}
  ],
  "description": "Melee Weapon Attack: +5 to hit, reach 5 ft..."
}
```

The attack damage goes in `damageParts`. The save damage goes in
`saveDamageParts`.

## Passive

For traits, Multiattack descriptions, and anything without a roll:

```json
{
  "featureType": "passive",
  "actorIdentifier": "Wolfrabbit",
  "featureName": "Pack Tactics",
  "description": "The wolfrabbit has advantage on an attack roll against a creature if at least one of the wolfrabbit's allies is within 5 feet of the creature and the ally isn't incapacitated."
}
```

### Action economy variants

Add `activationType` for non-standard action costs:

- Bonus action: `"activationType": "bonus"`
- Reaction: `"activationType": "reaction"`
- Legendary action: `"activationType": "legendary"`
- Lair action: `"activationType": "lair"`
- Multiattack: `"activationType": "action"` (it costs an action but
  describes the routine, not an individual attack)

## Spellcasting

Two separate calls. First set up the spellcasting feature:

```json
{
  "featureType": "spellcasting",
  "actorIdentifier": "Mage",
  "spellcastingAbility": "int",
  "spellcastingClass": "wizard",
  "spellcastingLevel": 9
}
```

Then import all named spells in one call:

```json
{
  "featureType": "spells",
  "actorIdentifier": "Mage",
  "spellNames": ["fire bolt", "shield", "misty step", "fireball", "counterspell"]
}
```

Spell names are case-insensitive. The tool matches against the D&D 5e
compendium and reports any unmatched names.

## Aura

Automatic area damage with no attack roll and no save (rare):

```json
{
  "featureType": "aura",
  "actorIdentifier": "Fire Elemental",
  "featureName": "Fire Form",
  "damageParts": [
    {"number": 1, "denomination": 10, "type": "fire"}
  ],
  "auraRadius": 5,
  "description": "A creature that touches the elemental or hits it with a melee attack while within 5 feet takes 5 (1d10) fire damage."
}
```
