---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "Region-by-region ecology profiles for placing SRD and homebrew monsters thematically across the Shattered Sea via found_at:."
created: "2026-08-06"
updated: "2026-08-06"
tags: [nature, maritime]
tier: supporting
uid: 8dc9b562-47fc-4f19-bd27-cebe31ac802f
---

# Monster ecology

Region-scale ecology profiles for setting a monster page's `found_at:`
frontmatter (`vault/_templates/_srd/_monster.md`).
Thematic fit governs, not CR or level — a region hosts threats across the
whole power range, and populating it with one monster never excludes
another. Reuse a region across as many monsters as genuinely fit it.

## How to use this

1. Read the monster's own type (aberration, beast, construct, dragon,
   elemental, fey, fiend, giant, humanoid, monstrosity, ooze, plant,
   undead) and whatever flavor cues its SRD text or homebrew concept
   already carries.
2. Pick at least 2 region-scale locations (`subtype: region` or `island`)
   below whose profile resonates thematically. A generic reef- or
   open-water-flavored monster with no strong draw falls back to
   [The Shattered Sea](vault/campaigns/shattered-sea/locations/shattered-sea.md)'s
   baseline; a monster with a real draw (fire, decay, deep-sea horror,
   jungle ambush, etc.) reaches for whichever region's profile names that
   draw, not the baseline.
3. `found_at:` may point to any location subtype once a specific site is
   warranted — a particular island, settlement, dungeon, or building
   beneath a fitting region — not only the region page itself. The region
   profile is the anchor for that judgment call, not the only legal target.
4. [Midchain](vault/campaigns/shattered-sea/locations/midchain.md) and
   [Verdant Scatter](vault/campaigns/shattered-sea/locations/verdant-scatter.md)
   are umbrella/index pages with no ecology of their own — route to their
   child regions instead (Midchain East/North/South/West;
   Crown Islands/Midchain). Midchain's four sub-regions are dense tropical
   island chain by default, but treat that as a baseline, not a rule: a
   single island within any of them can diverge sharply where local
   weather isolates it — a storm-locked cove, a persistent fog bank, a
   rain-shadow dry stretch, a wind-scoured bald outcrop. A monster whose
   flavor doesn't read as tropical isn't excluded from Midchain on that
   basis alone; it may fit one specific island's local anomaly rather
   than its sub-region's general character, and `found_at:` should name
   that island directly rather than the sub-region page.
5. Fiends (`type: fiend` — demons and devils) are the one exception to
   terrain-matching above: per
   [Sin and Sanctuary](vault/campaigns/shattered-sea/lore/sin-and-sanctuary.md), a fiend goes where sin has
   mass, not where the biome fits. It walks boldly in a place steeped in
   real cruelty and skulks at the margins of clean or hallowed ground,
   regardless of that place's terrain. Set a fiend's `found_at:` on
   specific sites with documented corruption, crime, or a fallen/contested
   patron's claim (a corrupt port authority, a black market, a shrine a
   god has stopped actively holding) rather than a region profile below —
   the region's terrain flavor doesn't apply to this type.

## Region profiles

### The Shattered Sea (baseline)

Reef, deep channel, coast, open water generally — the fallback for a
monster whose theme is straightforwardly maritime with no sharper regional
draw: pelagic predators, reef-dwellers, general aquatic aberrations and
monstrosities.

### [Ashwall Islands](vault/campaigns/shattered-sea/locations/ashwall-islands.md)

Ash-choked volcanic spires at [the Galewall](vault/campaigns/shattered-sea/locations/galewall.md)'s edge — thin cold air, sulfur
vents, sheer cliffs. Fits fire- or ash-adapted beasts, venomous or armored
crawlers, cliff-nesting aerial predators and scavengers, and lesser
elemental or draconic presences drawn to the vents.

### [Calder's Tooth](vault/campaigns/shattered-sea/locations/calders-tooth.md)

A Dravosi inspection port cut into cliff, facing mudflat villages the
Crown barely polices — a place monsters pass through more than lair in.
Fits mudflat/burrowing scavengers and vermin drawn to a working port more
than apex predators; humanoid threats outnumber monstrous ones here.

### [Central Strait](vault/campaigns/shattered-sea/locations/central-strait.md)

Open shipping channel, heavily patrolled, current-driven. Fits ambush
predators that prey on passing shipping and territorial aquatic creatures
contesting the current — subtle, submerged, or fast-fleeing, since nothing
survives sustained naval attention here.

### [Crown Islands](vault/campaigns/shattered-sea/locations/crown-islands.md)

Fortified, reef-fringed, the strongest Dravosi authority in the Sea — and
still hiding an unacknowledged dragon behind three generations of bad
charts. Fits apex reef predators and dragons content to stay hidden, and
monstrous allies of the smuggling trade the authorities quietly tolerate.

### [Doldrums](vault/campaigns/shattered-sea/locations/doldrums.md)

A windless, drifting band where voices carry a quarter mile and a black
dragon works the still channels. Fits stealth/silence hunters that exploit
becalmed ships, acid- or decay-themed threats, and stagnant-water
aberrations.

### [Midchain East](vault/campaigns/shattered-sea/locations/midchain-east.md)

The chain's older, stranger end — small islands scattered wide over pale
reef, charts turning vague, a drowned city beneath. Fits aberrations and
ruin-guardians tied to what's sunken there, reef creatures adapted to
bleached coral, and anything that resists being charted (illusion,
camouflage).

### [Midchain North](vault/campaigns/shattered-sea/locations/midchain-north.md)

A dense, defended coastal strip watching two ways — Crown patrols north,
[Grung](vault/campaigns/shattered-sea/factions/grung-clans.md) raids from the south. Fits territorial or raiding creatures aligned
with or against the Grung incursions and coastal-cover ambush predators;
nothing that draws direct Crown naval attention.

### [Midchain South](vault/campaigns/shattered-sea/locations/midchain-south.md)

The chain's smallest region — steep volcanic terraces, rich soil, almost
no flat ground, hostile to outsiders. Fits territorial ground or burrow
predators suited to steep terrain, plant-creatures thriving in volcanic
soil, and isolationist guardians matching the region's settled hostility.

### [Midchain West](vault/campaigns/shattered-sea/locations/midchain-west.md)

The chain's biggest land and western end — dense forest over a shallow
shelf, wide channels no frigate runs without a pilot, and Kalowe's
lawless free port. Fits forest ambush predators, shallow-water creatures
that snag unwary hulls in the wide channels, and scavengers drawn to a
lawless port's traffic.

### [Outer Reach](vault/campaigns/shattered-sea/locations/outer-reach.md)

Water past the Maw, beyond any flag or resupply, worked only by salvagers,
scholars, pilgrims, and the pirates content to sit this far out. Fits
deep-ocean apex predators and isolation-adapted aberrations — anything too
dangerous or strange for charted waters to tolerate.

### [Overland Track](vault/campaigns/shattered-sea/locations/overland-track.md)

A muddy switchback toll road through Calder's Tooth. Fits ambush predators
suited to a narrow travel corridor and bandit-adjacent humanoid threats —
low-tier nuisances fitting a road, not a wild.

### [Redwind Isles](vault/campaigns/shattered-sea/locations/redwind-isles.md)

Under-charted islands where a hot, dry wind blows off bare rock and the
few charts that exist disagree on how many islands there even are. Fits
heat- or wind-adapted creatures, rock-dwelling ambush predators, and
creatures whose numbers or presence are themselves unreliable — migratory
swarms, shapeshifters, illusion.

### [Orak](vault/campaigns/shattered-sea/locations/orak.md)

A low, wet island of the Verdant Teeth, shadowed and thick with predators
and Grung scouts. Fits amphibious or reptilian predators and dense-canopy
ambush hunters that pair naturally with Grung scouting parties.

### [Shelfworks](vault/campaigns/shattered-sea/locations/shelfworks.md)

An Antheri salvage field forty feet down, dive lines crowding the upper
ruins, and a drop-off nobody works any more. Fits Antheri construct or
guardian remnants and aquatic scavengers drawn to the salvage — and, at
the drop-off specifically, whatever it was that made the crews stop.

### [Sunken Crown](vault/campaigns/shattered-sea/locations/sunken-crown.md)

Low islands ringing a Blue Hole no sounding line has reached, held by
[Tabaxi](vault/campaigns/shattered-sea/species/tabaxi.md) who were here before the
charts were, whose water has lately started behaving wrong. Fits
deep-water aberrations tied to the Blue Hole's wrongness and guardian
creatures the Tabaxi already have a working relationship with — not
hostile by default.

### [Tail](vault/campaigns/shattered-sea/locations/tail.md)

Where the Scatter's two arcs converge into cliff-walled channels that
everything bound for the Maw funnels through. Fits ambush predators
positioned to exploit the bottleneck and territorial creatures contesting
the funnel point — the danger a chart can't warn a pilot about.

### [The Drowned Maw](vault/campaigns/shattered-sea/locations/the-drowned-maw.md)

The bottomless trench walling the Scatter's eastern edge, crossed fast and
by starlight, with a salvage rush working its western rim. Fits deep-sea
horrors, undead-of-the-deep, and salvage-guardian creatures contesting the
rush on the rim.

### [Verdant Teeth](vault/campaigns/shattered-sea/locations/verdant-teeth.md)

Five reef-fringed, Grung-held islands with dense rainforest interiors,
strict trade protocols, and lethal boundaries. Fits amphibious reptilian
creatures, dense-jungle ambush predators, giant insects and
plant-creatures inland, and boundary-guardians as lethal as the region's
own reputation.
