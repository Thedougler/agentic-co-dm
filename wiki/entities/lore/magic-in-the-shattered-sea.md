---
title: "Magic in the Shattered Sea"
aliases:
  - Magic in the Shattered Sea
category: entities
tags: [shattered-sea, lore]
sources:
  - "campaign-os:magic-in-the-shattered-sea.md"
created: 2026-09-13
updated: 2026-09-13
type: lore
lifecycle: proposed
lifecycle_changed: "2026-09-13"
reveal: unrevealed
campaign: shattered-sea
visibility: dm
summary: "Arcane, Divine, and Primal tradition rulings for Detect Magic, Counterspell, and Dispel Magic across every supernatural system in the Shattered Sea."
provenance:
  extracted: 0.85
  inferred: 0.10
  ambiguous: 0.05
base_confidence: 0.55
tier: supporting
---
# Magic in the Shattered Sea

*Arcane, Divine, and Primal sit above the spell schools, governing how player spells interact with every supernatural effect in this campaign.*

## The Fact

This page is world-texture with no single PC thread owning it. Every Grung encounter, Maw conduit interaction, and Tithe item question pulls on it through its own thread.

Magic in the Shattered Sea runs on three source traditions: Arcane, Divine, and Primal. These sit above the eight spell schools as a table-level classification governing how Detect Magic, Counterspell, and Dispel Magic interact with every supernatural effect in the world. The answer to "what does Detect Magic show?" and "can I Counterspell this?" always depends on tradition first, school second.

### Tradition Profiles

**Arcane** magic operates through study and technique. A practitioner learns it, and trained casters can teach it or steal it. Every arcane effect carries a school. Detect Magic returns tradition and school. Counterspell intercepts any arcane cast, and Dispel Magic suppresses it.

**Divine** magic flows through a patron relationship or through sincere collective worship (mortal faith feeding a deity or hierarchy, compressed or expanded by the relationship's shape). It always has a school. Detect Magic identifies tradition and school. Counterspell can intercept individual divine spells. Dispel Magic suppresses most divine effects, though effects with a divine release condition may reassert after suppression ends.

**Primal** magic runs biological, environmental, and creature-native. A creature carries it as part of its nature, not through learning or casting. Primal base traits register nothing on Detect Magic. Counterspell and Dispel Magic have no effect on them.

> [!mechanic]
> **Player spell interactions (tradition summary).**
> **Detect Magic:** Arcane and Divine return tradition + school, plus one sensory impression. Primal base traits return nothing.
> **Counterspell:** intercepts arcane and divine cast spells. Primal traits and conduit effects (an entity's influence flowing through a vessel with no discrete cast event) fall outside its reach.
> **Dispel Magic:** suppresses arcane and divine effects. Primal magic resists it. Effects with an external divine release condition may return after suppression ends.

### The Grung Three-Layer System

[[Grung]] magic runs three simultaneous layers, each a distinct tradition with no mechanical interaction between them.

**Layer 1 (Primal, species-wide).** Toxic secretion, diet-driven color shift, standing leap, sticky tongue: all biological traits with no spell school attached. Detect Magic returns nothing on them, Counterspell has no application, and Dispel Magic has no effect.

**Layer 2 (Arcane): the [[Ossketh]] (Gold monopoly, now stolen).** The color-sealing rite operates in the Transmutation school, designed to permanently reorder another Grung's caste color. When a second caster completes the rite on another Grung, the effect holds permanently with neither concentration nor a duration limit. Self-cast, the rite never completes: it becomes an unstable, ongoing transmutation requiring periodic external arcane maintenance from a skilled caster to prevent collapse. [[Ozzeth the Twiceborn]] and [[simone-tabarnack]] independently discovered and misapplied it. Gold chose reputation censure over direct force to avoid confirming the rite exists.

> [!mechanic]
> **Detect Magic (sealed Grung, Ossketh properly completed by a second caster):** Arcane transmutation, a change locked in place, holding.
> **Detect Magic (self-cast Ossketh holder, rite incomplete, requiring maintenance):** Arcane transmutation in progress, like a spell caught mid-execution and never completed.
> **Counterspell:** yes, can target the ongoing transmutation. **Dispel Magic:** suppresses; if external maintenance is then interrupted, the effect collapses.

**Layer 3 (Divine): the certainty-tap (Gold leaders only).** Lower-caste Grung hold sincere religious certainty that Gold are literal living gods. That sincere worship generates real divine power for Gold leaders (the same mechanism as mortal faith feeding a deity, compressed into a species hierarchy). Gold leaders at full tap have near-unlimited divine spellcasting. Belief sustains it moment-to-moment (shatter lower-caste certainty and it drains in real time), while proximity feeds it over distance (cut off from believers, it starves within hours). Gold engineered these conditions through the Ossketh: locking caste color creates the evidence of divine immutability that sustains the belief. The most effective player lever is exposing the Ossketh as arcane trickery, because lower-caste belief shatters when the cosmology it rests on is publicly disproved.

> [!mechanic]
> **Detect Magic near a Gold leader at full tap:** Divine (intense, sustained, like standing in front of a waterfall). It isn't coming from them; it's flowing through them.
> **Counterspell:** targets individual divine spells the leader casts. The tap itself has no discrete cast event to intercept.
> **Dispel Magic:** suppresses individual cast effects. The tap lies beyond its reach. Only severing belief or proximity drains it.

### The Maw Entity

An entity on the far side of the [[drowned-maw]] fissure is actively ripping reality. Its influence reaches the surface through conduits; [[Toby]] and [[Frankie]] are accidental conduits, not independent casters. The entity's effects fall outside the three-tradition taxonomy entirely, originating beyond the planar structure it maps.

> [!mechanic]
> **Detect Magic near a conduit (Toby or Frankie):** No school registers. The air feels like it's under strain (wrong pressure, something pushing through from somewhere else). Arcana check: planar contamination, not a cast spell.
> **Counterspell:** not applicable. No discrete cast event exists to intercept. The entity's declarations constitute direct influence on reality, outside the spell framework.
> Closing the fissure or addressing the entity is the only remedy. The children are keys, but the power source lies elsewhere. Harming the children has no effect on the source.

### Umberlee's Tithe

The curse that falls on every piece of the [[Tithe]] is divine. [[Umberlee]] maintains active divine attention on each piece; the curse is her attention, not a cast spell.

> [!mechanic]
> **Tradition:** Divine. **School:** Necromancy.
> **Detect Magic:** Divine necromancy. The curse reads as old and deliberate, carrying the weight of something that has never let go.
> **Remove Curse:** fails. The curse is divine in origin. Only the divine release condition lifts it: the item touching saltwater.
> **Dispel Magic:** suppresses for 1 minute, after which Umberlee's attention reasserts.
> **Counterspell:** not applicable (not a cast spell, an ongoing divine imposition).
> The curse falls on the object, not the bearer. Transfer, sale, or gifting moves the curse with the item.

### Sin and Sanctuary

The cosmological law governing fiend incursion, hallowed ground, and the demon's/devil's kiss maps to existing SRD spells without homebrew additions. See [[sin-and-sanctuary]] for the full lore.

> [!mechanic]
> **Hallowed ground (Hallow, Evocation, Divine).** Maintained by active patron attention. Lapses without the patron's ongoing claim. No visible sign marks when a patron withdraws. Detect Magic: Divine evocation, a claim being actively held.
>
> **The demon's/devil's kiss (Bestow Curse, Necromancy, Divine).** Permanent, patron-sanctioned. The receiving fiend is the instrument, not the caster. Detect Magic: Divine necromancy, a mark that remembers the moment of recognition. Counterspell: not applicable. The patron sanctions the kiss directly, and no mortal cast event occurs to intercept.
>
> **Fiend/celestial soul-reading (Detect Evil and Good, Divination, Divine).** Always-on and passive, requiring neither a cast event nor concentration. All fiends and celestials read mortal souls this way innately. Counterspell: not applicable.
