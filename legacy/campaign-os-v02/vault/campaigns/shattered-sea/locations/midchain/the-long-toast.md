---
type: location
status: draft
publish: false
title: "The Long Toast"
aliases: []
summary: "Stillmere's tavern, run by Ysolde, with the Widow's Toast and the wager slate where gossip about the recent draw-duel spreads before anything wrong becomes clear."
created: "2026-08-09"
updated: "2026-08-09"
tags: [mystery, horror]
tier: supporting
subtype: shop
within: "[[stillmere]]"
shopkeeper: "[[ysolde-sallow|Ysolde Sallow]]"
north_of: "[[nallowick]]"
east_of: "[[rasalgethi]]"
south_of: "[[rowans-hush]]"
west_of: "[[verdant-teeth]]"
geography: [coast]
campaigns: [Shattered Sea]
reference_image: ""
owner_skill: ".claude/skills/draft-content/references/location.md"
uid: af297e4c-94c3-4291-bd4b-27ed3f475028
---

# The Long Toast

> [!read-aloud]
> The low stone room runs long and close, driftwood beams strung with drying nets nobody has bothered to take down. Salt and dark rum sit thick over old woodsmoke. A dozen faces turn half a beat too slow when the door drags open: off-duty islanders hunched over their mugs, a couple of salt-crusted sailors still shaking off the crossing, every one of them quieter than a room this full should be. Behind the bar a lean woman wipes the same clean spot with a rag that stopped doing any real work an hour ago, one eyebrow already raised before you've said a word. A slate hangs at her shoulder, chalked WHO GOES DOWN FIRST over a column of names rewritten more times than anyone has bothered counting. She pours two glasses of [[widows-toast|Widow's Toast]] and sets them down unasked. "Or are you just here to listen?"

```meta-bind
VIEW[{reference_image}][image(class(reference-image-view))]
```

## Structure

The Long Toast occupies one of [[stillmere|Stillmere]]'s low stone houses. Its roof carries the same driftwood weight as every house around it, indistinguishable from a fisher's cottage outside, except for the noise leaking through the shutters after dark.

Inside, a single long room runs the depth of the building. A plank bar sits down one side. Mismatched tables and benches, worn smooth by generations of elbows, fill the rest of the floor. A low doorway at the back leads to the cellar, where Ysolde keeps her rum casks and the salted stock she trades on.

[[gerrit-sallow|Gerrit Sallow]]'s name comes up here more than his face does. Regulars trade the story of his latest offer to any outsider willing to try to finish him, half admiring and half tired of hearing it. A stranger crossing the threshold notices the wager slate first, chalked behind the bar, before anything else about the room.

| Field | Content |
|---|---|
| `verb` | Attract |
| `unstable_condition` | The wager slate behind the bar has run bets on "who goes down first" every night since the draw-duel two nights back, and the pot's grown too large for the tavern's usual joke to land the way it used to. |
| `consequence` | The next newcomer who wins big off the board starts asking why the losers keep walking back to their stools instead of a healer's table, and Ysolde runs out of ways to deflect it with a joke. |
| `link_of_relevance` | [[perrin-black-jaw\|Perrin Black-Jaw]] failed his Session 03 Arcana check (rolled 18, needed 22) identifying [[shepherd-grigori\|Shepherd Grigori]]'s necrotic healing magic and has suspected something's wrong ever since without knowing what. Ysolde watched the draw-duel firsthand and isn't bound by the rest of the village's practiced silence. A conversation with her at her own bar is where Perrin gets his first unvarnished account of what [[otel-karn\|Otel Karn]] actually is. |

## Atmosphere

Glass clinks on wood. Low laughter rolls under it, and a hush falls whenever someone new asks a straight question. Rum and brine dominate the air over old woodsmoke. A handful of oil lamps light the room and never reach its corners.

Ysolde runs the bar like she has done it a thousand times, because she has. A raised eyebrow stands in for sympathy, and a poured drink stands in for an answer. Whatever she is actually not saying gets left in the joke instead.

The regulars keep their own running tradition. They wager on who "goes down first" in the tavern's own brawls and scuffles, stakes that mean nothing since nobody here can really lose. That joke has stopped landing the way it used to since the draw-duel.

## Shopkeeper

![[ysolde-sallow]]

## Inventory

![[shop-inventory.base]]

## Hooks

If ignored, the wager board keeps paying out and Ysolde keeps pouring for both duelists in the same evening. Nothing here changes until a stranger presses her for a straight answer twice in the same conversation.

- **Moral**: Ysolde pours for both survivors of the draw-duel without missing a line. She shoulders what the rest of the village won't say out loud. A crew that spends real time in her chairs has to decide whether keeping the gallows humor running is mercy, or something closer to looking away.
- **Personal**: [[perrin-black-jaw|Perrin Black-Jaw]] gets his first unvarnished account of what happened on the Proving Ground here. Ysolde watched the draw-duel firsthand. She isn't bound by the rest of the village's practiced silence, so a straight question asked twice gets a straight answer nobody else on the island will give him.
- **Opportunistic**: the wager board pays out real coin on real bets. A stranger nobody's seen fight before draws the longest odds on the slate.
