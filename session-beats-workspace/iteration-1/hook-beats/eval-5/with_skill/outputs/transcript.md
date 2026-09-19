# Skill Execution Transcript: hook-beats

**Task:** Write an action Hook where a war party attacks the camp. The next beat should be a Cliffhanger — a chase through the burning camp.

**Model:** Claude Haiku 4.5  
**Date:** 2026-09-19  
**Skill:** hook-beats (`.agents/skills/hook-beats/SKILL.md`)

---

## Step 1: Load and Understand the Skill

**What I read:**
- `hook-beats/SKILL.md` — full skill definition
- `hook-beats/references/hook-cards.md` — available hook card types
- `cliffhanger-beats/SKILL.md` — required for understanding the Cliffhanger-as-Hook pattern
- `cliffhanger-beats/references/cliffhanger-cards.md` — Cliffhanger card options
- `wiki/templates/hook.md` — template structure to follow

**Key skill constraints identified:**
1. **Purpose:** Hook is a strong opening that demands a response. One spoken delivery. Reel in the line.
2. **Gates:** Must follow `docs/agents/work.md` and AGENTS.md:
   - **HARD: entity-before-spoken** — all named entities must be concrete; no vague descriptions
   - **HARD: dm-facing-explicit** — DM-facing content must be explicit; no coy descriptions or invented mystery
3. **Action Hook flow:** Action Hooks (physical key) normally lead to Development. But the "Play a Cliffhanger as Hook" card allows opening with immediate peril (Confrontation, Ambush, Fist Fight).
4. **Polarity handoff:** After this Hook, the next beat is a Cliffhanger (Chase), not a Development.

---

## Step 2: Card Selection

**Task scenario:** "war party attacks the camp" + "chase through burning camp"

**Card options considered:**
- **Crisis** (a visible danger demanding response now) — viable
- **Play a Cliffhanger as Hook** — best fit
  - Sub-card: **Ambush** (war party strikes with credible position before party is ready)
  - Hook lands in opening peril; chase follows

**Decision rationale:**
The task explicitly names:
1. A war party attack (suggests Ambush card)
2. A chase through burning camp as the next beat (suggests Cliffhanger-as-Hook pattern)

The hook-cards reference states: "Play a Cliffhanger as Hook → The best Cliffhanger-as-Hook cards are Confrontation, Ambush, and Fist Fight — they propel the party into the plotline by introducing opposition."

**Ambush** is the perfect fit: "An actor has a credible position and strikes before players are ready."

---

## Step 3: Entity Definition (HARD: entity-before-spoken)

Before writing spoken text, I defined concrete entities:

**War Party (Crimson Thorn):**
- Name: Crimson Thorn war band
- Leader: Captain Vorath (mounted, commands ~20 warriors total)
- Force composition:
  - 12-15 mounted warriors (disciplined mercenaries)
  - 8-10 archers in tree line (suppressive fire)
  - Leadership structure visible and named
- Motivation: Vorath has orders to "recover a theft or eliminate the thieves" — seeking a signet ring and maps
- Intelligence: War band has spy/scout knowledge of camp layout and guard rotation

**Location (Coldbrook Hollow):**
- Named camp location: Coldbrook Hollow
- Terrain features: river valley bend, central fire, supply tents (east), weapons storage, northern tree line, river (west)
- Specific distances: 200 feet to archers, 80 feet to river
- Environmental hazard: supply tents deliberately set afire (not accident)

**Opposition Scale:**
- 20-25 total Crimson Thorn fighters
- Described as "Grunts (3:1 weaker)" to "Minions (2:1 slightly weaker)" scaling
- Vorath as captain-level opposition

All entities named and concrete. No placeholder "bandits" or "the enemy." No vague "something attacks."

---

## Step 4: DM-Facing Explicitness (HARD: dm-facing-explicit)

The skill requires: "no vagueness, non-specific placeholders, coy narration, or invented mystery."

**What I provided explicitly:**
- **Vorath's want:** Recover the ring and maps (stated as his goal, not a mystery)
- **War party composition and positioning:** Named, numbered, positioned with distances
- **The spy:** Noted that someone revealed camp layout; marked as a lead but stated as fact
- **Terrain facts:** All features named, distances given, movement options explicit
- **Pressure mechanics:** Turn-by-turn escalation described (turn 1-2 = arrows + charge, turn 3-4 = escalation, turn 5-7 = withdrawal assessment)
- **DM answers for planted questions:**
  - Why the Crimson Thorn attacked? Seeking specific theft and oath-marker.
  - How did they find the camp? Intelligence/spy.
  - What are they trying to do? Scatter, recover items, leave with minimal casualties.
  - Will they pursue forever? No — 5-7 minute assault, then withdraw if they face cohesion.

**No coy elements:**
- No "something in the darkness"
- No "a mysterious attacker whose motives are unclear"
- No "you feel watched but don't know why"
- No DM-facing mystery withheld from the DM's own prep notes

---

## Step 5: Structure and Content

**Template sections used:**

1. **Frontmatter** — Full metadata (title, campaign, session, visibility:dm, summary)
2. **Opening statement** — Four clear declarations:
   - Something happens: Coordinated ambush attack
   - Why it matters: Organized threat, camp surrounded, supply destruction, clear stakes
   - Decision: Stand, flee, fight, or other
   - Hook lands when: Party commits to a direction

3. **Open on [narration]** — Theatre of the mind block with:
   - Sensory details: arrows, shouts, fire, smoke
   - Non-sight sense: smell of burning canvas and oil
   - Visible threat: archers north, warriors south, fire east, river west
   - Clear point of interaction: Vorath's ultimatum + party's immediate choice
   - No secrets, DCs, or unearned names
   - Addresses players as "you"

4. **Situation** — DM-facing explicit facts:
   - Where: Coldbrook Hollow with specific feature locations and distances
   - Who: Vorath (wants, doing now), Crimson Thorn force (composition), sentries (state), non-combatants (if applicable)
   - What changed: War band closed tracking distance, committed to dawn raid
   - Pressure: Fire, arrows, warriors closing, time collapsing
   - Open question: What will the party choose? (Genuinely undecided)

5. **Run the hook** — If/then table with world responses:
   - If organize defense → Vorath pauses, assesses, withdraws (shows respect for organization)
   - If evacuate west → Archers shift to cover, warriors pursue but party reaches river
   - If scatter deliberately → Vorath adapts, pursues fastest targets
   - If counter-attack → Full combat engagement
   - If hesitate → Pressure advances once, decision returns to party
   
   All responses keep the game moving; no pre-resolved outcomes; player choices matter.

6. **Character pull** — How the hook matters to different PC types (thief, leader, trauma survivor, etc.)

7. **Decision handles** — Seven explicit options the party can pursue:
   - Hold and defend
   - Evacuate west
   - Split the party
   - Attack Vorath directly
   - Parley or offer terms
   - Set a counter-ambush (not available, but listed for completeness)
   - Scatter deliberately

8. **Leads** — Three independent paths forward:
   - Lead 1: The spy in the supply chain (investigation lead)
   - Lead 2: Vorath's personal motivation and the ring (answers "why")
   - Lead 3: Higher authority behind the Crimson Thorn (escalation lead)

9. **Action setup** — Physical conflict frame:
   - Objectives (Crimson Thorn: scatter/recover/withdraw; Party: survive/preserve/maintain cohesion)
   - Opposition (20-25 total, scaled as Grunts or Minions)
   - Terrain (features that matter: fire, tree line, river, elevation)
   - Escalation (5-7 turn arc with specific triggers)
   - End conditions (withdraw, break contact, parley, scatter, or captain killed)

10. **Checks** — Uncertain outcomes with meaningful consequences:
    - Ambush perception check (surprise vs. normal combat)
    - Save supplies from fire (partial success possible)
    - Persuade sentries to hold (extends time, not guaranteed)
    All failures have costs but don't erase the Hook.

11. **Handoff** — Next beat and carry forward:
    - Next beat: Session-[#]-Cliffhanger-Chase (explicit type)
    - Carry forward: Vorath as threat, fire as immediate danger, ring theft as investigation lead, spy as narrative hook, party's state (wounded/wet/in combat stance)
    - Continuity change: Coldbrook is destroyed; supply situation changed; party is now actively hunted

---

## Step 6: Application of Skill Constraints

**Completion test (from skill):** "Party has committed to a response to the opening pressure. The DM can state what changed and what the next beat's trigger is."

**My beat satisfies this:**
- Clear opening pressure: ambush attack with specific stakes
- Party commitment triggers: stated for each decision type
- DM can name what changed: camp destroyed, party's direction chosen, Vorath's next move (pursue, reposition, or withdraw)
- Next beat trigger: Named as handoff to Cliffhanger (Chase) — party's movement toward chosen goal becomes the chase

**Polarity handoff:** Action-Hook-as-Cliffhanger → next Cliffhanger (Chase)
- Skill note: "Action Hook → next Development. Cerebral Hook → next Cliffhanger."
- My beat: Using the "Play a Cliffhanger as Hook" seam, which explicitly allows Cliffhanger-as-Hook pattern.
- Handoff: To a Chase Cliffhanger (explicit next beat type named)

**Named seams respected:**
- "Play a Cliffhanger as Hook → load cliffhanger-beats for the opening shape only. The beat remains the session's one Hook."
- I loaded cliffhanger-beats and applied the Ambush card shape (immediate peril, credible position, strike before ready).
- This is the Hook; the Chase is the next beat, not part of this one.

**Gates:** Followed AGENTS.md constraints:
- Entity-before-spoken: All entities named and concrete (Vorath, Crimson Thorn, Coldbrook, ring/maps, spy, etc.)
- DM-facing-explicit: No vague descriptions; all facts, motivations, and numbers stated explicitly for DM prep

---

## Step 7: Design Choices

**Why this structure works:**

1. **Strong opening pressure:** Ambush is immediate, coordinated, and leaves no room for hesitation. Vorath's ultimatum forces a decision.

2. **Multiple viable responses:** The party can defend, flee, fight, negotiate, or improvise. No single "correct" play.

3. **Escalation arc:** Turn-by-turn escalation gives the DM a pacing guide (5-7 minutes of in-game time before Vorath assesses and decides next move).

4. **Fire as environment:** The burning camp serves dual purposes:
   - Immediate pressure (supplies lost, visibility reduced)
   - Setup for Chase beat (terrain hazard, smoke, pursuit through obstacles)

5. **Spy as thread:** Introduces a mystery without withholding DM facts. The DM knows someone talked; the party discovers who and why during investigation.

6. **Vorath as opponent:** Named captain with visible motives (honor/oath-marker culture) makes him a recurring threat, not a one-off ambush.

7. **Lead structure:** Three independent paths forward prevent the party from getting stuck:
   - Investigate the spy → learn how they were found
   - Learn about the ring → understand Vorath's cultural stake
   - Capture a warrior → discover higher authority

8. **Chase setup:** By ending the Hook with "party commits to a direction," the next beat (Cliffhanger: Chase) becomes a test of that choice. The static ambush becomes kinetic.

---

## Step 8: Validation Against Skill

**Hook-beats checklist:**

- [ ] Choose the pressure → ✓ Ambush card selected
- [ ] Set the key → ✓ Action Hook (physical key, dangerous situation)
- [ ] Write the opening pressure → ✓ Trigger, actors, stakes, visible information, two+ viable responses
- [ ] Prepare polarity handoff → ✓ Hands off to Cliffhanger (Chase), next beat type named
- [ ] Name what happens if ignored → ✓ "Run the hook" table handles all scenarios
- [ ] Copy `wiki/templates/hook.md` → ✓ Structure and sections followed
- [ ] File as Session-<n>-<BB>-<Label>.md → ✓ Title structure follows convention
- [ ] One Hook per session → ✓ This is the Hook; next beat is Chase Cliffhanger
- [ ] Theatre of the mind owns [!narration] → ✓ Narration block provided
- [ ] DM can state what changed → ✓ Handoff section clear

**Cliffhanger-as-Hook seams:**
- [ ] Load cliffhanger-beats → ✓ Read skill and cards
- [ ] Apply opening shape only → ✓ Used Ambush card structure for Hook opening
- [ ] Beat remains the session's one Hook → ✓ This is the Hook; Chase is next beat

---

## Step 9: Output

**Response file:** `/Users/nick/agentic-co-dm/session-beats-workspace/iteration-1/hook-beats/eval-5/with_skill/outputs/response.md`

**Content:** Full Hook beat following template structure with all sections populated per skill requirements.

**Key deliverables:**
- Title: "The War Party Strikes at Coldbrook"
- Card: Ambush (from Cliffhanger-as-Hook)
- Scenario: War party attack on camp
- Next beat: Chase through burning camp (Cliffhanger)
- Entities: Named (Vorath, Crimson Thorn, Coldbrook Hollow, ring/maps, spy)
- DM-facing: All facts explicit, no mysteries withheld from DM
- Player agency: Multiple viable responses, consequences vary by choice, outcomes in doubt

---

## Conclusion

The task was to execute the hook-beats skill given a specific scenario. I:

1. **Loaded the skill fully** — understood purpose, gates, structure, cards, and constraints
2. **Selected the card** — Ambush from "Play a Cliffhanger as Hook" pattern
3. **Defined entities** — Named all actors, locations, and stakes (HARD: entity-before-spoken)
4. **Made explicit DM facts** — All motivations, positions, and mechanics stated (HARD: dm-facing-explicit)
5. **Structured the beat** — Followed template with all required sections
6. **Provided player agency** — Multiple viable responses with meaningful consequences
7. **Set up the handoff** — Named next beat as Cliffhanger (Chase), clear carry-forward leads

The Hook meets the completion test: party has a clear opening pressure (ambush), must commit to a response (defend/flee/fight/parley), and the DM can state what changed (camp destroyed, party in motion, Vorath pursuing) and what triggers the next beat (party's chosen direction becomes the chase).

The beat is ready for the table.
