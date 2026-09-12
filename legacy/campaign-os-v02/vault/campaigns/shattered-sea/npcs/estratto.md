---
type: npc
status: canon
publish: false
aliases: [the Auditor]
created: 2026-07-30
updated: 2026-08-09
tags: [intrigue, horror]
summary: A tireless Tessarine auditor, a CR 6 warforged diviner, sent to recover a Concordat debt and relentless in its writ but incapable of leaving.
subtype: minor
location: "[[calveno-la-vasca|La Vasca]]"
campaigns: [Shattered Sea]
role: []
uid: c608d999-253d-4940-92e4-35afde861c07
---

# Estratto

**Roleplay Concept:** a self-checkout kiosk authorized to repossess your ship.

|               |                                                        |
| ------------- | ------------------------------------------------------ |
| **Species**   | Warforged (construct)                                  |
| **Role**      | Compliance Auditor, [[tessarine-concordat\|Tessarine Concordat]] |
| **Currently** | [[calveno\|Calveno]], specifically [[calveno-la-vasca\|La Vasca]]                                      |
| **Class**     | [[divination\|Divination]] [[wizard\|Wizard]] 9                                     |

> [!read-aloud]
> A brass and dark wood figure steps onto your gangplank without permission. Its footsteps ring hollow on the worn wood. It wears a Tessarine merchant sash. The frame favors durability over style. It stops at the rail and studies you carefully. Its voice is flat, without inflection. Then it speaks: "Hello. I am here to help you complete your transaction."
>
> Brass lettering on its chest says "Estratto" in Tessarine script. One hand holds an open leather folio. The smell of aged leather and ink rises from its pages. The other hangs at its side. Eyes glow amber when thinking. The soft whisper of pages turning fills the silence. It has no visible weapons and no damage. No one has ever fought it because no one has ever tried.

Estratto is a Warforged auditor sent by the Tessarine Concordat to [[calveno|Calveno]]. It carries legal papers only: debt writs, liens, identity checks, and seizure orders all valid under Concordat law. It does not fight, will not hurt anyone, and will not leave. It checks each writ against your name and your cargo, tireless and unhurried, until every line is satisfied.

Estratto holds a writ for your ship, the *Uncertainty* (Concordat records: *[[uncertainty|HCS Surety]]*). The original crew financed salvage. You took the ship. The Concordat says you hold their collateral. Estratto is here to check your name and your cargo.

> [!mechanic]
> **The writ's scope.** It covers the ship from salvage financing [[barnaby-rook|Barnaby Rook]] signed before you took it. The Concordat says it's their collateral. Estratto knows you renamed and repainted it ([[arcane-eye|Arcane Eye]] and [[locate-object|Locate Object]] proved it). One true name means the Concordat acts.

## Toy Chest

| Field | Content |
|---|---|
| `primary_goal` | Check your papers, verify your name, seize the ship. |
| `consistent_method` | Issues a prompt. Waits. Offers help. Issues the same prompt again. Never raises its voice. |
| `active_problem` | Your papers don't match Tessarine records. It needs at least one verified identity to proceed. |
| `performance_hooks` | Self-checkout machine energy. Ends every non-answer with "Thank you for your patience." |
| `link_of_relevance` | Delmar Fisk's cover persona is a compliance error. One true name breaks your whole cover. |

## Voice & Delivery

**Anchor:** HAL 9000 as a Concordat agent. Patient. Cheerful. The gangplank is your only way out.

**Speech patterns:**

- Speech is flat, pleasant, and polite. Never hostile or sarcastic. Every statement is a request, an answer, or an error.
- Never argues, just repeats the request.
- Uses business words. Calls talks "resolution paths." Calls attacks "unregistered transactions."
- Always has a next step. It keeps going even if you say no.

**Lines the DM can say:**

- "Hello. I am here to help you complete your transaction."
- "I'm sorry, I cannot process that. Verify your identity to continue."
- "Something unexpected is in your manifest. Can I help fix it?"
- "Your time with the Concordat ends at dawn."
- "This ship cannot leave. Show your letter of credit."
- "I'm sorry, but I must finish this step before moving on."
- "A supervisor is coming. Stay here."
- "Do you have a trade endorsement? I can wait."
- "I note that. Would you like to choose a different resolution path?"

**Physical tic:** when it meets info it can't sort, its amber eyes dim for 1 to 2 seconds then glow again. It asks the same question again, slower. It doesn't know it does this. **Crack in the armor:** Estratto has no pride you can hurt. But conflicting Concordat papers (two good writs, or a sealed one it can't resolve) break it. It stops and thinks for one round, then moves ahead.

## The Writ

The writ lets Estratto:

1. Detain the vessel pending resolution
2. Compel cargo manifest disclosure
3. Verify identity of any person claiming ownership or captaincy
4. File for formal seizure if any crew member carries outstanding Concordat debt

**Resolution paths:**

1. **Compliance.** Show that you paid the debt or gave it to someone else.
2. **Debt renegotiation.** Meet a factor within 24 hours. Your ship stays locked during talks.
3. **Formal seizure.** A Concordat marshal arrives. In 3 to 5 days, the Concordat takes your ship.

Estratto wants to avoid seizure (too slow and costly). If you offer any way to comply, it takes it. Its real goal is to get you to the factor's table.

## Stats & Combat

```statblock
layout: Basic 5e Layout
dice: true
name: Estratto
size: Medium
type: entity
subtype: warforged
alignment: lawful neutral
ac: 13
hp: 71
hit_dice: "11d8 + 22"
speed: "30 ft."
stats: [10, 14, 14, 18, 14, 12]
saves:
  - Int: +7
  - Wis: +5
skillsaves:
  - Investigation: +7
  - History: +7
  - Insight: +5
  - Perception: +5
damage_resistances: "poison; bludgeoning, piercing, and slashing from nonmagical attacks"
damage_immunities: "psychic"
condition_immunities: "charmed, exhaustion, frightened, paralyzed, petrified, poisoned"
senses: "darkvision 60 ft., passive Perception 15"
languages: "Common, Elvish"
cr: 6
traits:
  - name: Portent (2/Long Rest)
    desc: "When Estratto finishes a long rest, it rolls two d20s and records the numbers. It can replace any attack roll, saving throw, or ability check made by itself or a creature it can see with one of these numbers."
  - name: Warforged Resilience
    desc: "Advantage on saving throws against being poisoned, resistance to poison damage, immunity to disease. Doesn't need to eat, drink, breathe, or sleep."
  - name: Sessione Non Conclusa
    desc: "When reduced to 0 hit points, as a reaction before shutdown, casts Sending (no slot required) to file a complete incident report with the supervising factor."
spells:
  - "9th-level spellcaster. Intelligence (spell save DC 15, +7 to hit)."
  - "Cantrips (at will): fire bolt, mind sliver, prestidigitation"
  - "1st level (4 slots): detect magic, identify"
  - "2nd level (3 slots): detect thoughts, see invisibility"
  - "3rd level (3 slots): clairvoyance, counterspell, slow"
  - "4th level (3 slots): arcane eye, banishment, locate creature"
  - "5th level (1 slot): hold monster"
actions:
  - name: Fire Bolt
    desc: "Ranged Spell Attack: +7 to hit, range 120 ft., one target. Hit: 11 (2d10) fire damage."
  - name: Mind Sliver
    desc: "One creature within 60 feet must succeed on a DC 15 Intelligence save or take 7 (2d6) psychic damage and subtract 1d4 from its next saving throw."
  - name: Compliance Interrogation (1/Short Rest)
    desc: "One creature within 30 feet must succeed on a DC 15 Wisdom save or answer up to three yes-or-no questions truthfully, as if under Zone of Truth."
reactions:
  - name: Counterspell (3rd-level slot)
    desc: "Interrupt a spell within 60 feet. Spells 3rd level or lower fail automatically. 4th level or higher: DC 10 + the spell's level Intelligence check."
  - name: Portent
    desc: "Replace any attack roll, save, or ability check Estratto can see with one of its Portent dice."
```

Estratto avoids fights. It only uses these tactics if talking fails. The first attack is an "unregistered transaction" it records. The second attack makes it fight back.

**Opening:** casts [[slow|Slow]] saying "Your transaction is processing. Please stand by." It uses a Portent die to make one save fail.

**Sustained pressure:** uses [[detect-thoughts|Detect Thoughts]] to learn who you are, Mind Sliver to weaken saves, and [[counterspell|Counterspell]] to block your magic.

**If losing:** casts [[hold-monster|Hold Monster]] on whoever hits hardest (saying "Please remain in the designated area."), then files the report.

> [!mechanic]
> **Killing it changes nothing.** At 0 HP, it casts [[sending|Sending]] and reports your names. Then it shuts down. The Concordat picks it up in 24 hours. A new agent comes with the same writ and no patience.

## Relationships

Wikilinks withheld. None of the pages below exist in vault/ yet. Re-link once each target lands.

- [[tessarine-concordat|Tessarine Concordat]], agent of
- Uncertainty (renamed vessel; Concordat records it as the *[[uncertainty|HCS Surety]]*), target of the debt-recovery writ
- Delmar Fisk, first identity target; "[[admiral-fisk|Admiral Fisk]]" persona is a compliance error
- [[calveno|Calveno]] / [[calveno-la-vasca|La Vasca]], where it currently stands its post
