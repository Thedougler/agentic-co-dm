# Hook cards

Card shapes follow Mike Pondsmith, *Scripting the Game* (R. Talsorian, 2020;
transcription at `RTG-Scripting-the-Game-v1.2-agent-readable (2).md` in the repo
root), paraphrased for 5e play. Pick the card the current fiction calls for:

- What did last session's ending leave unresolved? A live threat or a scene
  cut mid-action usually selects the card (often **Play a Cliffhanger**).
- Which card lands on an active PC goal, bond, or fear? A Hook that touches
  what a player already cares about reels faster.
- Which key does the session want? Action cards (Kidnapped, Crisis, Play a
  Cliffhanger, False Accusation) open a physical key; cerebral cards
  (Discovery, Revelation, Murder, Looming Threat, Coronet Blue, Play a
  Development) open an informational key.

Each card: **Shape** — what the beat is; **Build** — what the page must
contain beyond the table-ready anatomy; **Pairs** — what it sets up;
**Fair play** — how the card keeps the players' grip on the outcome.

## Kidnapped
- **Shape:** The party, or someone they care about, is seized by a force that is mysterious and plainly stronger than they are. The abduction starts the game; it is not foiled inside the Hook.
- **Build:** The taker (owner page) and why they want this captive; how the seizure happens in front of the party, or the fresh aftermath they find; two or three concrete traces left behind; what happens to the captive and on what schedule.
- **Pairs:** Chase when the party gives pursuit; Clue or Warning Development when they arrive after.
- **Fair play:** The taker's edge is visible in the fiction — numbers, magic, a route the party cannot follow yet — so the thread outlives the Hook while the party chooses how to pursue, bargain, or investigate.

## Coronet Blue
- **Shape:** The characters wake in a dangerous or difficult situation with no memory of how they got there or who they are expected to be — while friends and enemies treat them as if they know everything.
- **Build:** The role everyone assumes they hold; who expects what from them in the next ten minutes; the danger; three clues to the truth on their persons or in the room.
- **Pairs:** Development (Clue, Lie Revealed, Mistaken Identity) as they piece it together.
- **Fair play:** Needs the players' buy-in for the memory gap; each player decides what their character makes of the role, and the truth is recoverable from the clues.

## Play a Cliffhanger
- **Shape:** Open in furious action. The best choices are **Confrontation**, **Ambush**, or **Fist Fight**. The fight throws the party straight into the plot by introducing the opposition or an ally.
- **Build:** Load `cliffhanger-beats` for the chosen card's shape; keep the fight short, with an objective besides killing everyone, and end it with the party committed.
- **Pairs:** Development next (action Hook).
- **Fair play:** The opening action has uncertain results; the party's choices in it decide the state the Development inherits.

## Play a Development
- **Shape:** Open on a Development — best as **Secret Meeting**, **Mistaken Identity**, **Romance**, or **Betrayal** (treachery). It pulls the party into the plot and introduces a major ally or opponent: a PC meets the ally-to-be, a friendly force turns on them, or they are en route to meet their enemy.
- **Build:** Load `development-beats` for the chosen card's shape; the turn lands inside the Hook's spoken opening or its first exchange.
- **Pairs:** Cliffhanger next (cerebral Hook).
- **Fair play:** The party chooses what to do with the meeting, the mistake, or the betrayal; the Hook ends on their commitment.

## Discovery
- **Shape:** The adventure starts with an important find — an invention, a relic, a document, a body of evidence. The find links directly to something the later game needs: it is the key to the curse, or the thing the villain is hunting.
- **Build:** The object (owner page) and what it visibly does or shows; who else wants it, and when they learn the party has it; two leads out of the Hook.
- **Pairs:** Cliffhanger next — often Ambush, Race, or Pursuit by whoever wants the find.
- **Fair play:** The party decides whether to keep, hide, use, sell, or surrender the find; each choice routes the next beat differently.

## Crisis
- **Shape:** The party walks into a disaster already in progress — an attack, a collapse, a plague, a fire — and it does not let up until they escape or set out to stop it. The crisis ties to the plot: the opposition caused it or rides it.
- **Build:** Three escalating crisis ticks with what each one destroys; named people in danger, with where they are; the first visible trace of the cause; the exits.
- **Pairs:** Development next (action Hook) — usually the Clue or Revelation that names the cause.
- **Fair play:** The party chooses whom to save, what to abandon, and whether to flee or push toward the cause; each choice leaves a different aftermath.

## Revelation
- **Shape:** A hidden fact dramatically changes a character's life — an inheritance, a secret past, a parentage, a curse — and links straight into the game.
- **Build:** The evidence or messenger; what the fact obliges, grants, or endangers; who else knows and what they will do about it.
- **Pairs:** Cliffhanger next (cerebral Hook) — someone moves on the new fact.
- **Fair play:** Agree backstory-changing revelations with the PC's player at prep time (`pc-interview` when needed); the player owns the character's reaction.

## Murder
- **Shape:** A friend, ally, or plainly innocent victim is killed near the party or found by them. The killer stays out of reach during the Hook — the murder exists to draw the party into the game.
- **Build:** The victim (owner page); how and where it happened; three clues; the killer (owner page) and the established means that put them beyond immediate reach — already gone, disguised, or protected; who blames whom.
- **Pairs:** Cliffhanger next (cerebral Hook) — the killer's allies clean up, or the party is blamed.
- **Fair play:** The killer's escape is part of the fiction the party walks into, not a rescue by the DM; every clue is real and leads toward the killer.

## False Accusation
- **Shape:** The party is accused of a crime they did not commit — the unpaid sword, the stranger pointing at them, the man who dies in a PC's arms. The pressure squeezes their options to a few hard ones: fight against bad odds, flee with everyone after them, or submit to a process stacked against them.
- **Build:** The accuser and their motive; the evidence and why it convinces; the authorities present, with numbers; the real culprit (owner page) and three clues to them.
- **Pairs:** Cliffhanger (Pursuit) next if they run; Development (Framed, Clue) if they submit.
- **Fair play:** Each hard option has a defined consequence and a path to clearing their names.

## Looming Threat
- **Shape:** Like a Crisis, but the danger has not broken yet: portents, dread in the air, the army massing, the first strange deaths. Everyone knows it is only a matter of time. The threat ties directly to the plot.
- **Build:** Three portents the party sees now; the clock to arrival, with its ticks; what preparation, warning, or action can change the threat's form or timing.
- **Pairs:** Cliffhanger next (cerebral Hook) — the threat's vanguard, or someone exploiting the fear.
- **Fair play:** The threat's arrival and form respond to what the party does before it lands.
