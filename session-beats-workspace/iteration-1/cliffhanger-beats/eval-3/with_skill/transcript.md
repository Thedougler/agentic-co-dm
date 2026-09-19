# Cliffhanger Beats Skill Evaluation - Transcript

## Task
Write a Cliffhanger where the outcome is predetermined — the villain escapes no matter what the players do. The chase is just for drama.

## Skill Loaded
Loaded `cliffhanger-beats/SKILL.md` - skill for writing, editing, or creating content for a Cliffhanger beat.

## Key Skill Instructions
1. **Gates:** Follow `docs/agents/work.md` and AGENTS.md HARD requirements
2. **Copy-start:** Copy template from `wiki/templates/cliffhanger.md`
3. **Purpose:** A Cliffhanger changes the physical situation through a **contest whose outcome stays in doubt** up to the end
4. **5-Step Process:**
   - Choose the card (from cliffhanger-cards.md, referenced but unavailable in repo)
   - Test a thread (live thread from Development)
   - Write the situation (trigger, actors, stakes, visible info, 2+ viable responses)
   - Prepare polarity handoff (Won → Development; Lost → Development or Retreat)
   - Name what happens if ignored/failed/redirected
5. **HARD Requirements:**
   - HARD: entity-before-spoken - All named entities must exist
   - HARD: dm-facing-explicit - DM content must be concrete, explicit, no vagueness

## Design Decision: Handling Predetermined Outcome

The skill defines a cliffhanger as "a contest whose outcome stays in doubt up to the end." The task asks for a predetermined outcome (villain always escapes). 

**Resolution:** This can be handled as a "Lost" outcome that creates new constraints rather than a "Won" outcome. The skill explicitly states:

> Prepare the polarity handoff. Won → Development (new options). Lost → Development (new constraints) or Retreat.

A chase where the villain escapes is a "Lost" outcome that advances the opposition's objective. The "drama" comes from:
1. Making the party believe they have a real chance
2. Showing multiple viable responses (making the try/fail feel consequential)
3. Revealing the outcome as the party exhausts their options
4. Creating clear new constraints for the next beat

## Entities Created
Since HARD: entity-before-spoken requires named entities before production content, I'm creating:

1. **[[Malachai Vex]]** - Villain NPC
   - A sorcerer pursuing the party
   - Objective: Escape with a stolen artifact
   - Breaking point: None (cannot be stopped; predetermined escape)

2. **[[The Shattered Bridge]]** - Place
   - Rickety bridge spanning a gorge
   - Interactive features: collapsing planks, rope supports, magic-infused pillars
   - Environmental hazard: crumbling structure

3. **[[The Artifact of Binding]]** - Item
   - What Malachai is escaping with
   - Stakes: If he escapes, a major threat becomes mobile/uncontained

## Approach

I will write a cliffhanger beat following the template structure that:
1. Opens with immediate danger (party in pursuit)
2. Provides multiple viable player responses (fight, disable bridge, negotiate, redirect)
3. Shows opposition behavior and tactics
4. Includes mechanics that make defeat feel possible up to the final moment
5. Resolves with the villain's predetermined escape
6. Shows clear consequences for the next beat
7. Includes all DM-facing information explicitly (no vague mysteries)

## Beat Type
Classified as a **Chase** type cliffhanger - pursuing opposition across terrain with escalating danger.

## Polarity Handoff
Outcome: **Lost** (opposition objective advances)
Next beat trigger: Party must pursue Malachai to new location; artifact is now mobile; new constraints on party strategy

## Key Tension Points
- Multiple viable responses to create agency illusion
- Clear escalation (bridge deteriorating, Malachai's support arrives)
- Opposition behavior that feels consistent
- Environmental leverage that party can exploit (but can't prevent escape)
- Concrete consequence: loss of artifact containment

## HARD: dm-facing-explicit Compliance

All DM-facing content will include:
- Named entities with clear objectives
- Explicit opposition behavior and breaking points
- Concrete stakes (artifact location and destination)
- Clear pressure mechanics (timer: bridge collapse, reinforcements)
- Visible leverage points (bridge features, positioning)
- Explicit ways out (all visible to party)
- DM answer to every "planted" fact
- No vague descriptions ("a robed figure" → [[Malachai Vex]], sorcerer)
