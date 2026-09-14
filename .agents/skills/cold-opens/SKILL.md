---
name: cold-opens
description: >-
  Write or revise a cold open in this ai-co-dm vault: a cinematic pre-Hook
  prelude the table plays from a borrowed NPC, ally, rival, or villain POV. Use
  when prepping a session opener that runs before the PCs' own Hook, a
  temporary-NPC-control scene, an alternate-POV or villain-POV opener, events
  elsewhere in the world, or when auditing an existing cold open against its
  handoff, ratchet, timebox, and hard-cut gates.
---

# Cold Opens
## Work gate

Prep only. Follow `docs/agents/work.md`.

Show a chat proposal; write a campaign wiki page only after DM accept (FR-019). Reject leaves no page. Invention is required when the wiki lacks the fact: set `invention: true` and ground in wiki pages and/or D&D 5e rules. Cite `[[pages]]` for wiki claims. Show the DM any contradiction with an existing page. Never present invention as a wiki fact. Never write silent canon. A craft `type` becomes `canon` only after DM accept.

Players see nothing until the DM accepts and presents.

Done when: the page is inspectable Work, `lifecycle: proposed`, invention flagged, grounding named.

Remap durable output paths from `campaigns/<slug>/` to `wiki/` (entities/journal as appropriate). Templates live in `wiki/templates/`. Replace knowledge-bank terminology with wiki terminology, but do not change geographic river-bank language. Point at `docs/agents/work.md` rather than restating the glossary.


Write a **directed, interactive prelude** that energizes the table, dramatizes
events outside the PCs' viewpoint, and hands momentum into the main session.

A cold open is **one Hook beat** with `framing: borrowed-pov`, not a
miniature adventure and not a new kind. Recap, Strong Start, and cold
open stay three different openers. Knowledge uses `audience` and
`reveals:` — no third secrecy model. Table math is the campaign's
existing procedure; do not invent a five-d20 house rule here.

Default shape:

> alternate POV → immediate situation → escalating checks → striking payoff →
> hard cut → main PCs

Target **20–30 minutes** of table time and **five group checks or saves**
unless the request establishes another count.


## HARD: entity-before-spoken

Follow AGENTS.md **HARD: entity-before-spoken** (Nick 2026-09-14). Mint/file required owner pages (kebab + templates; stage when `WIKI_STAGED_WRITES=true`) **before** filling this beat's spoken/`[!narration]`/action-card text. Vague stand-ins for missing entities = critical error — do not ship.

## HARD: dm-facing-explicit

Follow AGENTS.md **HARD: dm-facing-explicit** (Nick 2026-09-14) together with **entity-before-spoken**. DM layers (action cards, Be ready for, secrets, situation facts) state who/what/where/why concretely — no coy placeholders. Player `[!narration]` may withhold from players but stays grounded in named owners.

## Reference

| Read | When |
|---|---|
| `references/cold-open-method.md` | choosing the handoff; fixing the trajectory while leaving outcomes variable; selecting and briefing the POV; separating player knowledge from PC knowledge; protecting the timebox; writing for spoken delivery; leaving runtime state unresolved |
| `references/cold-open-patterns.md` | selecting an archetype; running the five-check ratchet; writing a hostile or villain POV; picking consequence dimensions and failure patterns; running one character with the whole table; choosing an ending shape and a hard cut |
| `references/cold-open-page.md` | the page skeleton, the repo's beat-page integration (group check, picture-then-check steps, labeled landings), and wiki conventions |
| `references/cold-open-gates.md` | the completion gate every finished cold open passes |

Sibling authorities: `hook-beats` owns Hook beats the party plays as
themselves; `session-beats` owns the main session's Beat Chart;
`theatre-of-the-mind` owns every player-facing paragraph this skill produces.

## Workflow

### 1. Establish the handoff

Read enough campaign and session context to answer:

1. Why show this instead of leaving it offscreen?
2. Why show it **now**?
3. What should the players feel, know, suspect, or anticipate at the cut?
4. What should the PCs themselves know afterward?

Write the answers as one purpose statement and one knowledge statement. The
handoff menu is in `references/cold-open-method.md` § Handoff.

**Complete when:** the cold open has one identifiable handoff, and the split
between player knowledge and PC knowledge is explicit.

### 2. Choose and brief the POV

Default to a **known friendly NPC** — a familiar character lowers setup cost
and reaches meaningful action fast. The whole table shares control of one
character or one NPC group unless the request establishes another structure.

Other viewpoints, the player brief's contents, and the hostile-POV test are in
`references/cold-open-method.md` § POV and
`references/cold-open-patterns.md` § Hostile POV.

**Complete when:** a player can state who they are, what they want **right
now**, and what is happening, within a minute of introduction.

### 3. Set the knowledge firewall

Separate POV knowledge, player knowledge, and PC knowledge. Use dramatic irony
deliberately; show effects, symbols, behavior, or consequences where naming the
underlying explanation would collapse a live mystery. Procedure:
`references/cold-open-method.md` § Knowledge firewall.

**Complete when:** every revelation in the cold open carries an explicit answer
to "do the main PCs know this?"

### 4. Build the trajectory

Write the sequence as:

1. **Opening frame**
2. **Check 1 — Orientation**
3. **Check 2 — Pressure**
4. **Check 3 — Complication**
5. **Check 4 — Crisis**
6. **Check 5 — Payoff**
7. **Final image**
8. **Hard cut**

These are dramatic functions, not a mechanical formula — keep an established
structure when the DM supplies one. Each check arises from the fiction the
previous result created. Each function's job:
`references/cold-open-patterns.md` § Five-check ratchet.

Predetermine the **trajectory**, not the **outcome**: fix where the scene
begins, the problem confronting the POV, the order of major pressures, the
threshold it moves toward, and where the camera cuts. Leave injuries,
resources, collateral, information, survival, exposure, and position variable —
the full split is in `references/cold-open-method.md` § Directed trajectory.

**Complete when:** the scene has a fixed start, a fixed order of pressures, and
a fixed cut point, with every listed variable still open.

### 5. Ratchet the checks

Every check leaves the situation changed and raises pressure, significance, or
understanding. For each check define:

- **Prompt** — what is happening now?
- **Resolution** — which group check, save, or established campaign mechanic
  resolves it?
- **Success** — what changes on success?
- **Failure** — what changes on failure?
- **Advance** — what happens next regardless?

Success and failure must differ meaningfully, and failure usually imposes a
cost rather than halting the sequence. Consequence dimensions and failure
patterns: `references/cold-open-patterns.md`.

Use the campaign's established group-check or table procedure. If no
an existing ruling note exists for this, name the check the fiction demands and
leave the math to the DM.

**Complete when:** every check advances the fiction, every result changes at
least one fictional state, and no failed roll can strand the scene.

### 6. Protect the timebox

Design for **20–30 minutes**. Favor immediate situations, compressed travel,
short exchanges, one-roll obstacles, consequential decisions with few options,
and narration that bridges straight into the next interactive moment. Abstract
pursuit, battle, escape, boarding, disaster, infiltration, or survival through
checks; enter full encounter procedure only when the DM wants the budget spent
there. Introduce a proper noun only when the players need it now. Tactics:
`references/cold-open-method.md` § Timebox.

**Complete when:** every element establishes the POV, creates a decision or
check, communicates the handoff, escalates, or lands the ending.

### 7. Write for spoken delivery

If the POV, place, or threat still has no pictureable facts, invoke
`flesh-out` on that parent first. Then chain-load
`theatre-of-the-mind` for the read-aloud text. Narration is written
for the DM to **say**: concrete sensory information, active events, short
paragraphs, visible threats, one strong image over several decorative details,
in the order the character perceives it. Between checks, narrate the
consequence and move to the next pressure. Give dialogue as compact intent plus
strong lines, never a scripted exchange whose timing depends on the players.

**Complete when:** the DM can move narration → roll → consequence without
reading around explanatory prose.

### 8. Land the final image and cut

The ending opens a question rather than closing the larger story:

> final image → one beat of silence → main PCs

Ending shapes and hard-cut patterns are in
`references/cold-open-patterns.md`. The main session supplies the next Hook.

**Complete when:** the DM holds an exact final image and an exact destination
for the cut.

### 9. Preserve unresolved state

Preparation describes possibilities; play establishes history. Leave every
variable result unresolved in prep — transcript ingest and the repo's canon
update decide which branch happened. Detail:
`references/cold-open-method.md` § Unresolved state.

**Complete when:** fixed setting facts and unresolved runtime outcomes are
distinguishable on the page.

### 10. Write the page and pass the gate

Instantiate `templates/Session prep.md` with `subtype: hook` and
`framing: borrowed-pov`. Put spoken text in `[!narration]`. Follow
from `scripts/`. Run `references/cold-open-gates.md`.

**Complete when:** doctor is clean and every gate passes.

## Strong-start gate

The opener must be purposeful, not merely cinematic: connect it to the
cliffhanger or agreed plan, make the immediate situation actionable, and hand a
changed pressure into the main PCs. It is one modular Hook in the session
skeleton, not a plotted prelude. Keep a fallback parachute file for an off-map
one-shot if the party's chosen direction makes the prepared opener irrelevant.

## Tone and energy gate

Confirm the session's agreed tone before choosing the cold open's register. Make
the start purposeful and visibly energetic through one striking, supported
image and an actionable pressure, not an inventory of cinematic details. Keep
secrets, DCs, and hidden mechanics outside `[!narration]`; dramatic framing may
show effects and choices without exposing the answer.
