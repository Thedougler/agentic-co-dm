---
name: writing-cold-opens
description: >-
  Write or revise a cold open in a Campaign OS vault: a cinematic pre-Hook
  prelude the table plays from a borrowed NPC, ally, rival, or villain POV. Use
  when prepping a session opener that runs before the PCs' own Hook, a
  temporary-NPC-control scene, an alternate-POV or villain-POV opener, events
  elsewhere in the world, or when auditing an existing cold open against its
  handoff, ratchet, timebox, and hard-cut gates.
---

# Cold Opens

Write a **directed, interactive prelude** that energizes the table, dramatizes
events outside the PCs' viewpoint, and hands momentum into the main session.

A cold open is **one Hook Beat**, not a miniature adventure. The narration,
checks, obstacles, reversals, and final image are movements inside that Beat.
The main session keeps its own Beat Chart and opens on its own Hook afterward.

Default shape:

> alternate POV → immediate situation → escalating checks → striking payoff →
> hard cut → main PCs

Target **20–30 minutes** of table time and **five group checks or saves**
unless the request establishes another count.

## Reference

| Read | When |
|---|---|
| `references/cold-open-method.md` | choosing the handoff; fixing the trajectory while leaving outcomes variable; selecting and briefing the POV; separating player knowledge from PC knowledge; protecting the timebox; writing for spoken delivery; leaving runtime state unresolved |
| `references/cold-open-patterns.md` | selecting an archetype; running the five-check ratchet; writing a hostile or villain POV; picking consequence dimensions and failure patterns; running one character with the whole table; choosing an ending shape and a hard cut |
| `references/cold-open-page.md` | the page skeleton, the repo's beat-page integration (group check, picture-then-check steps, labeled landings), and wiki conventions |
| `references/cold-open-gates.md` | the completion gate every finished cold open passes |

Sibling authorities: `writing-hook-beats` owns Hook beats the party plays as
themselves; `composing-beats` owns the main session's Beat Chart;
`writing-player-prose` owns every read-aloud paragraph this skill produces.

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

Use the campaign's established group-check procedure
(`references/cold-open-page.md` § Repo integration) rather than inventing a
replacement resolution system.

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

Chain-load `writing-player-prose` for the read-aloud text. Narration is written
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

Instantiate the page per `references/cold-open-page.md`. Run
`npm run lint -- <path>` and fix findings. Run every item of
`references/cold-open-gates.md`.

**Complete when:** lint is clean and every gate passes.
