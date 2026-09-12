# Player boundary

The owning parent and current table state supply the world. This skill decides
which part of that world the player can receive through the current surface.
It does not invent a second world inside player-facing prose. Read this file
whenever a scene contains hidden truth, automatic knowledge, a specific
interaction, a creature effect, or an unresolved player choice.

## Evidence-of-access gate

Before putting a detail on the player-facing page, name its legitimate channel:

1. **Current sensory access:** a character can see, hear, smell, touch, or
   otherwise sense it from the current position, angle, and state.
2. **Established automatic knowledge:** the character's known expertise,
   culture, background, magic, or prior experience supports recognition. Do not
   invent a specialty to make a detail convenient.
3. **Declared and resolved interaction:** the player declared an action and the
   fiction or mechanic resolved it. Describe only what that result exposed.
4. **Earned public canon:** the parent or prior play has already made the fact
   public and relevant. Preserve its certainty and ownership.

If no channel applies, cut the detail and stop or route to the owning
content-stock skill. An uncertainty marker does not create access: an inference
is permissible only when it follows from named perceivable evidence or
established knowledge. Source silence cannot be filled with a genre default.
Recheck the object's interaction state: visible, held/inspected,
recognized/used, or recurrent/intelligent. A character holding an intact
stonepear can receive its established exterior and weight; holding it does not
reveal the inside, underside, function, history, contents, taste, temperature,
texture, or magic. Do not write “skin barely yields,” “grit under the skin,” or
equivalent interior information until the surface is actually exposed and the
result is resolved.

Current sensory access also has a boundary. A sightline does not expose the
far side; a hand on a handle does not inspect the room beyond a door; a sound
does not identify its source without evidence. Questions and player actions
earn closer detail. Mechanics can establish an effect, but do not backfill
unresolved fiction with its likely explanation.

## Fresh phrasing gate

The parent and references provide facts and technique, not wording or
architecture to repeat. Make a terse fact inventory in fragmentary keywords
with provenance and access; never copy source sentences into that inventory.
For a standalone portrait, use the target portrait contract to make a private,
unordered coverage checklist; it is an audit, not an outline. Set the source
aside and discard its headings, order, and clause grouping. Choose the portrait's
organizing spine independently of both source order and checklist order — a
dominant supported relationship, contrast, or use when the facts support one —
and compose around it. Do not default to checklist sequence, a universal
whole-to-detail order, or arbitrary shuffling. Recompose around that spine,
materially changing the grammatical subject and attention order, fact grouping,
and sentence boundaries or clause dependencies; relocate or change comparisons
when the facts include them. This is a structural break check, not a style
formula: sparse facts may leave an unavoidable relationship or sentence shape,
and accuracy always wins over artificial variation.

After writing, check off the unordered coverage checklist; do not reorder the
draft to match it. Then compare the result with the polished parent and every
read expert excerpt for phrase or sentence overlap, distinctive metaphors,
callouts, and recognizable architecture: the same sequence or section
progression, fact grouping, or clause dependencies. If the architecture is
still recognizable, rebuild from the fact inventory rather than swapping
synonyms. Preserve proper names, necessary measurements, and irreducible game
terms when changing them would alter identity or accuracy. “Copy the move,
leave the setting” means copy the technique, never the words. The sole narrow
exception is an established in-world quotation, inscription, or document the
user explicitly requests verbatim; identify its owner and quotation. Expert
table lines in `experts.md` are instructional analysis, not player-facing text
to echo.

## Standalone knowledge scope

Unless the user explicitly asks for identified or player-known properties, a
standalone portrait is a cold player-appearance and observable-state layer.
Parent audience labels such as `[agent, dm]` do not grant player knowledge.
Include all established descriptive states needed to recognize the subject,
including state-qualified physical views such as a cut cross-section, but keep
exact effects, durations, speeds, actions, DCs, rarity, attunement, curses,
private biology or history, tactics, hidden causes, learned route rules, and
secret identities out. Render a separately requested mechanics layer only after
the description and only within the explicitly granted knowledge state.
Complete means complete for the target portrait contract, never every parent
heading.

## Manifestation, inference, mechanics

Keep these layers separate, especially for creatures, auras, hazards, magic,
and illusions:

- **Visible manifestation:** body, posture, behavior, buildup, and sensory or
  physical effects the characters actually experience now.
- **Permissible inference:** a character's qualified reading of named
  perceivable evidence or established knowledge (“it may be warded,” “the air
  seems to thin”). “May” or “seems” cannot rescue a detail with no evidence;
  players still decide what it means. Do not turn mood into certainty.
- **Mechanic or secret:** exact radius, DC, condition, HP, damage, save,
  recharge, hidden ability, source, or true consequence. Keep these in
  `[!mechanic]` or collapsed `[!secret]-` until the parent, character
  knowledge, earned public canon, or a resolved interaction makes them public.

On a first look at a monster, expose only body, visible behavior, posture, and
sensory effects actually experienced. Do not announce an exact 30-foot aura or
suffocation before contact merely because the stat block contains them.
Telegraph danger with an observable buildup — breath frosting, moths dropping,
grass paling, a hanging line snapping taut, a cough after someone enters —
then resolve the mechanic when the table acts. Do not resolve Hookline/Reel,
grab, bite, or haul on the first look. A later public reveal may state the rule
in the appropriate wrapper.

## Creature response state

For a cold standalone creature response, use the terminal pattern
`observable stimulus → observable response → stop`. If useful, lead with
“Evidence, not explanation:” and name only what the creature does when the
stimulus occurs. Do not append an unseen actor, cause, direction, meaning,
threat, or tactical interpretation, even as “may,” “seems,” or another hedge.
Keep the creature's stable body, habitat, and ordinary behavior in the portrait
contract; this stopping rule governs the response state and does not replace
that coverage.

## Player agency

Never write what a PC thinks, feels, wants, decides, intends, remembers
incorrectly, concludes, or chooses to investigate. Do not narrate a route,
trust, surrender, victory, death, or other unresolved outcome. Show the
stimulus and leave the response to the player.

**Freeze-frame fail:** do not continue past the reaction point on a first look
— no ankle/boot already seized, feet already leaving the ground, body already
hauled aloft, or other completed contact/injury before the table can act.

**Remote-control cognition fail:** do not narrate table understanding or PC
awareness as prose payload (`before anyone understands`, `you realize too late`,
`nobody notices until…`). Show the observable telegraph; let players react.

**Unearned campaign-rule fail:** do not put Hunger / possession frameworks,
claim/unclaimed metaphysics, or other private campaign rules into Appearance or
cold place portraits. Keep them in DM sections / `[!secret]-`.

**Invented event fail:** do not narrate a perceivable one-shot event (shadow
turns then still, something flees then vanishes) that the parent did not
establish as stable public appearance or that current table state did not
supply. Cold portraits stay on durable geography.

NPC and faction behavior may pursue established goals. The world may change
because of a resolved mechanic or an established pressure. A player-facing
surface stops at the next meaningful decision; do not append an “if they hold”
or “if anyone touches it” branch to spoken text.

If a description gives the table a false mental model, correct it directly.
Communication must not become a hidden challenge. Do not hide obvious geometry,
conspicuous danger, or normal expertise to manufacture mystery.
DM-facing notes do not need coy fog. Name the fact for the DM, and withhold it
only from player-facing prose until the table earns it. Do not write vague
placeholders such as "someone may be there" when the source identifies the
actor, and do not add "do not reveal this" reminders as spoken or table-facing
content.

## Parent, canon, and stock

Read the owning parent before drafting. Established and locked facts remain the
authority. Preserve beliefs as beliefs; do not promote a possibility to canon
because it makes a cleaner image.

If the parent lacks a signature, first-sight facts, and one usable property,
invoke `fleshing-out-content` before this prose pass. Select only facts that
pass the access gate. The stock pass may add reversible texture, but may not
decide hidden truth, player action, or an unresolved consequence. Keep hidden
truth in `[!secret]-`.
