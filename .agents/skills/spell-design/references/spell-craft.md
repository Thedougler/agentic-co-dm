# Spell craft

## Craft basis

Use the 2024 spell-entry shape: casting time, range, components, duration, then
effect. Prefer DM-facing craft that sharpens table utility: visible magic before
rules, compare against peer spells for level pressure, and keep prep runnable at
the table instead of exhaustively simulating edge cases.

Ground invention in wiki pages and 2024 spell patterns. When reskinning a close
peer, name the peer and write the effect in your own words; every change from
the peer is canon under the rule in `llm-wiki`.

## Section fill detail

### Narration

Theatre-of-the-mind casting portrait in complete sentences. Cover what a
bystander sees, hears, and feels. Keep secrets, save DCs, curse triggers, true
names, and unearned patron identities out of `[!narration]`; place them in
DM-facing body or notes so they remain recoverable without being read aloud.

### Classification and casting fields

Body line: `Level, School (Ritual when it is a ritual)`.

Fill with peer-usable substance (not blank labels):

- **Casting Time.** Action, Bonus Action, Reaction trigger, minute, hour, or
  special timing.
- **Range.** Distance, self, touch, area origin, and target count.
- **Components.** V, S, M, costly or consumed material, and focus limits.
- **Duration.** Instantaneous, fixed duration, Concentration duration, or until
  discharged.

### Effect block

One short block with every table consequence needed to run it: save or attack,
ability score, DC source, damage dice and type, healing, condition, movement,
object effect, area, target limits, repeated saves, Concentration breakpoints,
end condition, and scaling when it scales. Vague “protects X” fails — state what
sealing/hiding/marking does, how long, how it fails or ends, and any check/save.

### Discovery

Fill when the spell needs a scroll, book, teacher, patron, ritual site, faction
archive, bargain, or other source. State where it can be found, what access
costs, what clue points there, and what changes when the party gets it. Do not
treat item spell-scroll pages as the spell page itself.

### Lore

Fill when the spell needs history: old truth, who still cares, surviving
evidence, and how that history changes a present choice. Provenance the wiki
leaves silent is canon under the rule in `llm-wiki`, stated as world fact. Established lore keeps
its causes: a new spell explains nothing a lore page already explains
differently.

Discovery and Lore stay on the spell page. They are spell sections, not separate
`type: lore` notes.

### Rulings

The tricks players will try, each with one answer: targeting objects, allies,
or the caster; underwater, in darkness, through cover; stacking with common
spells; what it does to summoned or incorporeal creatures. Then counterplay
(save, cover, range, Concentration, *counterspell*, *dispel magic*, a
tradition's countermeasure) and how a named enemy opens with it.

## Peer anchoring and balance

Damage by spell level (single target / multiple targets, average-friendly
dice):

| Level | One target | Several targets |
|---|---|---|
| Cantrip | 1d10 | 1d6 |
| 1st | 2d10 | 2d6 |
| 2nd | 3d10 | 4d6 |
| 3rd | 5d10 | 6d6 |
| 4th | 6d10 | 7d6 |
| 5th | 8d10 | 8d6 |
| 6th | 10d10 | 11d6 |
| 7th | 11d10 | 12d6 |
| 8th | 12d10 | 13d6 |
| 9th | 15d10 | 14d6 |

A rider (a condition, forced movement, a disarm) costs roughly one damage die;
a save-for-half spell carries the full column, an attack spell that deals
nothing on a miss can carry a die more.

Compare against existing 2024 spells of the same level and role before locking
numbers. Cantrips stay cantrip-scoped; if the fantasy needs large damage,
no-save control, or extreme range, raise the level (or mark higher-level
invention) rather than stuffing nova into a cantrip. Climax-support spells may
grant info, leverage, or a risky gambit — never an automatic campaign win.

## Audit questions

- Does the identity sentence name level/school, table effect, signature, and
  player choice/pressure?
- Is narration sensory-only, with DCs/secrets/true names elsewhere?
- Are Casting Time/Range/Components/Duration concrete and peer-usable?
- Can the DM run the effect tonight (save/attack, targets, end, scaling)?
- What 2024 peers calibrate level and pressure?
- Does Discovery name a source page, a price, and who notices a casting?
- Do Rulings answer the likely tricks, counterplay, and enemy use?
- Is every invention canon under the rule in `llm-wiki`, stated as world fact and listed in the
  response?

## Failure modes

| Failure mode | Repair |
| --- | --- |
| Empty casting-field labels | Fill concrete 2024 values |
| Secrets/DCs in narration | Move to DM-facing sections |
| Silent canon / unmarked invention | `invention: true`; list the proposal in the response |
| Spell-scroll item as spell exemplar | Point to `type: spell` page / template only |
| Cantrip nova (huge dmg + no-save + mile range) | Raise level or cut axes to peer scope |
| Auto-win climax spell | Add cost, contest, failure, or choice |
| Verbatim PHB paste | SRD paraphrase, name-only ref, or homebrew |
| No source, or "found somewhere" | Named teacher, book, patron, or site with a price |
| Discovery/Lore spun into separate lore note | Keep sections on the spell page |
| One-off color forced into a spell page | Leave on beat/place/NPC/item until named |
