---
type: puzzle
status: draft
publish: false
aliases: []
summary: "The Blight's root network senses any creature that takes a living thing from Aruhe, turning the island's fauna hostile in escalating waves."
created: "2026-08-15"
updated: "2026-08-15"
owner_skill: ".claude/skills/draft-content/references/puzzle.md"
tags: [horror, survival]
tier: supporting
subtype: trial
severity: dangerous
campaigns: [Shattered Sea]
uid: 475c7f65-3ebc-4dc5-9b2b-eb4ce7c2c429
---

# The Taking Rule

*The island's guardian mechanism reads intent through its root network and punishes any creature that removes a living thing from Aruhe.*

## At a Glance

- **Type:** trial
- **Location:** [[aruhe|Aruhe]] (all zones)
- **Purpose:** the [[blight|Blight]]'s guardian mechanism protects Aruhe's bounty from invaders
- **Stakes:** island-wide fauna hostility, escalating with zone depth
- **Reward / Access:** safe passage through any zone while the rule is unbroken
- **Default State:** dormant. The island tolerates observation.

## Surface

### Immediate

- Fruit hangs heavy on feral terrace vines, unpicked and ripe
- [[sandro|Sandro]] and [[nino|Nino]] eat only from their own stores, never the island's
- No animal on the beach has attacked anyone who stood still and watched

### Investigation

Asking Sandro directly gets the rule stated plainly: take nothing, and the island lets you pass.

> [!check] Sandro and the fruit
>
> | Check | DC | Failure | Pass |
> |---|---|---|---|
> | [[wisdom\|Wisdom]] (Insight) | 13 | nothing unusual about their diet | they avoid the fruit deliberately, not from lack of hunger |
> | [[intelligence\|Intelligence]] (Nature) | 15 | wild plants, nothing more | feral cultivation, still tended by something |

### Mastery

The [[blight|Blight]] distinguishes passage from taking. Walking through plants costs nothing. Drinking from springs costs nothing, because water flows off the island on its own. Dead fallen wood has already left the tree. Only removing a living or growing thing triggers the rule.

> [!check] Black flowers and the root network
>
> | Check | DC | Failure | Pass |
> |---|---|---|---|
> | Arcana or Nature | 17 | the corruption's source is unclear | the protection is druidic, not divine, and the mechanism reads intent through the root network |

## DM Truth

> [!mechanic]
> **The Taking Rule.** The [[blight|Blight]] senses through its root network when any creature removes a living or growing thing from [[aruhe|Aruhe]]: fruit, fish, plants, trapped animals, firewood from living trees. Within 1 minute of the taking, fauna in the taker's current zone turn hostile toward that creature. Within 1 hour, fauna in adjacent zones join. Within 4 hours, all island fauna is hostile. Only the taker draws aggression at first, but the party joins the target list the moment it intervenes and the aggression does not fade while any taker remains on the island.
>
> **Exceptions.** Spring water, dead fallen wood, trampled plants underfoot, self-defense kills, and passage through already-cleared ground do not trigger the rule. The Blight attacks [[grung|Grung]] on sight regardless. That hatred predates the current mechanism.

Magic that creates food from nothing sidesteps the rule entirely.

> [!mechanic]
> **Conjured provisions.** [[goodberry|Goodberry]] and [[create-food-and-water|Create Food and Water]] do not trigger the rule because nothing leaves the island.

## Interaction

- **Avoid** — carry provisions, take nothing. The safest vector. The island tolerates indefinite observation.
- **Shield** — conjured food bypasses the rule entirely. [[goodberry|Goodberry]] and [[create-food-and-water|Create Food and Water]] both work.
- **Exchange** — leave a trade-worthy offering at a black-flower marker. A creature that places a worthy offering can take the same amount without triggering the rule.
- **Endure** — take what you need and accept island-wide hostility. The party fights through every zone with fauna turned against them.
- **Solve** — learn the Blight's story (from Sandro, from the ruins in [[aruhe-the-rot|the Rot]], from the graves in [[aruhe-the-hunger|the Hunger]]). A creature that understands the memorial's purpose and approaches the Death Bloom without taking can reach the grove without triggering any response, because intent matters to the original ritual.

> [!check] Black-flower markers
>
> | Check | DC | Failure | Pass |
> |---|---|---|---|
> | Insight | 15 | the flowers are decorative | the placement marks an exchange, leave something of value, take the same amount |

## Consequences & Escalation

| Stage | Timing | Effect |
|---|---|---|
| Local response | Within 1 minute | Fauna in the taker's zone turn hostile toward the taker |
| Adjacent response | Within 1 hour | Fauna in adjacent zones join; random encounters double in frequency |
| Island-wide response | Within 4 hours | All fauna hostile; the [[bear-elk\|bear-elk]] abandons its patrol to hunt the taker; [[corpsewood\|corpsewood]] walks toward the coast |

Escalation lasts the full visit and does not reset on return. The root network remembers the taker's scent.

## Bypasses & Exploits

- Conjured food is the cleanest bypass. It costs spell slots, not island hostility.
- A Ranger's Natural Explorer or similar survival feature lets a party forage without technically "taking" (adjudicate from the fiction: gathering windfall fruit vs. picking from a vine).
- [[druidcraft|Druidcraft]] to ripen fruit that then falls naturally is a creative use. Adjudicate as the Blight recognizing a druidic approach.
- A creature polymorphed into island fauna is not recognized as an invader and can eat freely. The Blight reads species, not identity.

> [!check] Druidcraft ripening
>
> | Check | DC | Failure | Pass |
> |---|---|---|---|
> | Nature | 14 | the Blight notices the interference | the fruit falls naturally, no trigger |

## Rewards & Discoveries

- Safe passage opens the island's deeper layers, from the terraces and ruins through the memorial grove to the Death Bloom itself
- Understanding the rule is the first step to understanding the Blight's motive — protection, not malice
- A party that reaches the Death Bloom without triggering the rule encounters the Blight in a calmer state (Stage 1, no preemptive aggression from fauna)

## Aftermath

- If the party never triggers the rule, the island remains as they found it — the memorial endures unchanged
- If triggered, the heightened aggression persists for 1d4 days after the party leaves, then the fauna return to baseline
- The Blight's awareness of the party persists regardless. It knows they came, whether they took

## Scaling Knobs

- Escalation timing:

| Pace | Local | Adjacent | Island-wide |
|---|---|---|---|
| Hard | instant | 10 minutes | 1 hour |
| Default | 1 minute | 1 hour | 4 hours |
| Forgiving | 1 hour | 4 hours | 1 day |

- The exchange DC can drop to 12 for a party that has seen the black flowers three or more times
- Remove the conjured food bypass entirely for a survival-horror table where the island recognizes all foreign magic
