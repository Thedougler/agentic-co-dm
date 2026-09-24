---
name: npc-design
description: >-
  Design, revise, and file NPCs and villains for D&D 5.5e (2024 rules):
  incidental extras, scene NPCs, recurring allies, patrons, rivals, faction
  faces, villains, and lieutenants. Use when creating or improving a
  `type: npc` page or any part of one (want, secret, look, voice, ties,
  Influence play, villain plan, combat forms), or when a beat needs a new
  speaker minted. Monsters without a personal identity go to monster-design;
  player characters go elsewhere.
---

# NPC design

An NPC is a person who **wants something now** and does something about it.
Players remember three things about them: their **face** (the few details they
can picture again), their **voice** (how they talk, and one line they would
repeat), and what they **want** from the party. Everything the NPC hides (a
secret, a debt, a divided loyalty) leaves a **tell** in their face or habits
that a sharp player can notice; the DM page states the truth behind it.

File what constitution X makes canon. Follow `docs/agents/work.md`.

## Boundary contract

- **Input:** A named NPC (existing page or one to mint), the caller's
  objective and brief, `wiki/templates/npc.md`, and the vault canon the person
  touches.
- **Work:** The steps below at the prep scale this NPC needs.
- **Done:** Every item in `## Done` holds for the reported page path.
- **Capability Handoff:** The portrait and voice lines go to
  `theatre-of-the-mind` with the packet from step 6. Combat forms go to
  `monster-design`, which tunes them against the live party and returns the
  statblocks and encounter rule for the Combat section. A faction the NPC
  fronts goes to `faction-design`; a home or workplace to `place-design`. A
  named owner the NPC needs and the vault lacks is minted first by its owner
  skill (AGENTS.md **HARD: entity-before-spoken**). Each child returns its page
  path or result; resume at the step that waited on it, or report the named
  gap.

## Page rules

- **Canon.** User-said facts file immediately on the live path. Whatever the
  page needs that canon leaves silent, records as unknown, or contradicts,
  decide now as a **canon proposal** (`docs/agents/table-ready.md` § Fill the
  silence): one concrete answer, stated on the page as world fact where the DM
  uses it, with the page marked `invention: true`. The response lists each
  proposal with the `[[pages]]` it grows from; a proposal that settles a
  contradiction names the sources and the reading it chose, so the DM picks the
  winner.
- **Preserve.** Improving an existing page keeps every established fact and
  the NPC's existing face words; add only what changed.
- **Bar.** Existing vault pages are canon to keep, never a quality model; many
  predate this skill. The bar is the steps and `## Done` below.
- **Role.** Frontmatter `role` is exactly `rival`, `patron`, or `contact`,
  chosen from how the NPC stands toward the party. Their job (gatekeeper,
  informant, smith) goes in Nature.
- **One callout.** `[!narration] {Name}` is the only callout. Secrets and
  truths are plain complete sentences in At a Glance, Running, or Connections.
- **Explicit DM layer** (AGENTS.md **HARD: dm-facing-explicit**). Every tell
  has its truth on the page, by name: what they hide, from whom, and what
  happens if it comes out.
- **Process stays off the page.** The inventory, concept notes, and packet are
  working notes.

## Prep scale

Pick the scale from the NPC's importance at the table. It decides which steps
run.

| Scale | Page carries | Steps |
|---|---|---|
| Incidental | Face, want, one line, exit | 1 (canon only); Want from 2; Face and Voice from 3; 6; 7 |
| Scene | Face, voice, want, leverage, limit, one secret or contradiction | All steps |
| Recurring | Scene, plus ties to every relevant PC, faction, and place, a next move, and an activity log | All steps |
| Villain or faction face | Recurring, plus a front from [references/villain-front.md](references/villain-front.md) | All steps |

## Steps

[references/example.md](references/example.md) takes one NPC through every
step; read it before step 3.

### 1. Read the canon and the party

Retrieve before inventing (constitution XII), using QMD per AGENTS.md § Vault
retrieval.

1. Read the NPC page if it exists and every page that links to it:
   `grep -rliF "[[<name>" wiki/entities` for the slug, title, and each alias.
2. Read their home place, their faction, and every person they are tied to.
   Search QMD for the name, their job in that place, and session recaps that
   mention them. `qmd get` every hit you will use.
3. Read each PC page in `wiki/entities/pc/` (At a Glance, Connections, Session
   Log) for backstory threads, debts, rivals, and goals this NPC could touch.

Write the **canon inventory** in working notes: `[[slug]]` · kind · the fact
that ties it to this NPC. Add one line per PC: the thread this NPC could pull.

Done when every backlink and relevant hit is in the inventory or dropped with a
reason, and every PC has a line (or "no thread").

### 2. Build what drives them

- **Want:** concrete, present tense, able to change the next scene.
- **Leverage:** what they can grant, deny, expose, or mobilise, and what using
  it costs them.
- **Need or fear:** what they lack or dread losing.
- **Limit:** the line, oath, resource, or fear that blocks an easy win.
- **Contradiction:** two true pressures that can collide in play.
- **Secret:** what they hide, from whom, why, and what happens if it comes
  out. Give it about three discovery paths (a statement, a trace, a witness, a
  document, a consequence).
- **What they know:** the facts they carry, which they share freely, which
  they sell, and which they lie about.
- **Open questions:** every question their page raises (a missing crew, a
  rumour, a debt), with the DM answer: what actually happened, even when the
  NPC does not know it. The page states the truth and, separately, how much of
  it they know.
- **If ignored:** what they do next without the party.
- **PC threads:** one optional reason for each relevant PC to engage, drawn
  from step 1. An invitation, never a forced bond.

Done when every field is concrete enough to change a choice, the secret has
its truth, its stakes, and its discovery paths, and every open question has
its DM answer written as one concrete fact.

### 3. Make them this person and no other

Read [references/concept.md](references/concept.md) for diversity axes, face
and voice craft, and weak-to-strong examples.

1. **Stock version.** One line: "gruff dwarf smith", "mysterious hooded
   stranger", "jolly innkeeper". Everything it predicts is the default.
2. **Twist.** Tie their work, body, or history to campaign canon so the
   stock version breaks: a smith who forges only from wreck iron because the
   Crown taxes ore; a harbour clerk who can recite every ship lost in forty
   years.
3. **Face.** Two or three specific visual details, one sound or smell with its
   source, and what they are usually doing with their hands. These words are
   reused every time they appear.
4. **Voice.** Word choice, rhythm, one verbal habit, and a subject they avoid.
   Voice comes from what they care about, never from an accent or a gag.
5. **Tells.** For the secret, the contradiction, and any hidden leverage, one
   detail in the face or a habit that points at it: the wedding ring worn on a
   cord under the collar, ink under the fingernails of a man who claims he
   cannot read.
6. **Swap test.** Put another NPC from the same place or faction in their
   place. Replace every line that stays true.

Done when the twist, face, and voice fail the swap test and every hidden truth
has a tell.

### 4. Plan how they run

- **First meeting:** where they are, what they are doing, their opening move,
  and what they want from the party.
- **Attitude and request:** starting Attitude (Friendly, Indifferent, Hostile)
  and, separately, how they meet the party's likely requests (Willing,
  Hesitant, Unwilling).
- **Posture changes:** what opens them up, what closes the door, and what
  takes priority over the party.
- **Influence:** the approaches that fit their need and limit, each roll as
  Ability (Skill) and DC from `dnd5e-mechanics`, and what a success or miss
  moves. Procedure: [references/social.md](references/social.md).
- **Likely moves:** each thing the party will plausibly ask of or try on
  them, drawn from the brief, the PC threads, and what they guard (buy,
  haggle, beg, threaten, steal, set free), with their answer, its price, and
  the roll when the outcome is uncertain.
- **Next move and activity log** (recurring and villain): what they do between
  appearances; one log line per appearance with what play changed.
- **Villain or faction face:** build the front in
  [references/villain-front.md](references/villain-front.md): an active plan
  with visible, interruptible steps and several possible endings.
- **Allies:** capable, limited, and player-directed; they have a want and a
  cost and leave the central problem to the party.

Done when the DM could run the first five minutes of the meeting, the moment
the NPC's posture changes, and every likely move from the page alone.

### 5. Arm everyone in reach

A likely move that goes wrong ends in a fight: anyone the party could attack,
rob, or arrest can fight back, and so can whatever the NPC would loose or call
(guards, beasts, a crew). Each of them carries compact numbers in the Combat
section: AC, HP, Speed, the attacks or save DCs the DM will roll, and what they
do when violence starts (fight, flee, call the watch, loose the animals). A
standard statblock used unchanged needs no custom features: name it and copy
those numbers. New or changed combat forms come from `monster-design`, given
the NPC's concept, face, tells, and brief; it returns statblocks tuned to the
live party and an encounter rule (the fiction that picks a form).

Done when every fighter the page puts in the party's reach carries numbers,
the NPC included: someone who flees can still be grabbed, chased, or struck.

### 6. Hand the look and voice to theatre-of-the-mind

Build the **packet** as fragments, each with its source:

- **Body:** build, age, and height against something familiar.
- **Face:** the details from step 3, word for word.
- **Clothing and gear:** what they wear and carry, and its wear.
- **Senses:** one sound or smell with its source.
- **At rest:** what their hands do when nothing is happening.
- **Tells:** every tell from step 3, as plain appearance, never its meaning.
- **Voice:** the voice notes from step 3 and what they want from the party.
- **Leave out:** the secret, the DM thesis, mechanics, and names the players
  have not earned.

Load `.agents/skills/theatre-of-the-mind` and give it the packet twice: in
portrait mode, person recipe, for the `[!narration] {Name}` block; and in the
dialogue recipe, for three sample lines (the ask, the refusal, the line under
pressure).

Done when the portrait passes theatre-of-the-mind's final check and carries the
face and every tell, and the three lines sound like one person.

### 7. File the page

Copy `wiki/templates/npc.md` and fill the person jobs from `wiki/AGENTS.md`
Layout. Omit empty sections, write complete sentences, and wikilink every
owner page.

| Section | Carries |
|---|---|
| At a Glance | Role, Nature (job and what they are like), Home, Wants; rows for Secret, Leverage, or Limit when they change how the DM runs them; the one-sentence DM thesis |
| Narration | The portrait from step 6 |
| First meeting | Opening move and one sample line |
| When posture changes | What opens them, what closes the door, what takes priority, what they will and will not share, and the truth behind each open question |
| Voice | Voice notes and the three sample lines |
| Connections | Each tie by wikilink and what it does at the table, including each PC thread; a PC with no thread stays in the working notes |
| Combat | Numbers for every fighter in reach from step 5, and the encounter rule for custom forms |

Run `wiki lint <path>`, then `wiki lint fix <path>`, and rerun until green.

Then **audit**: for each item in `## Done`, write in the working notes the page
line that satisfies it, and fix the page wherever no line does. For the item
that keeps established canon, copy every sentence, list item, and table row of
the old page into the notes as its own line, and beside each write the new
line that carries it; a line with nothing beside it goes back on the page.

## Done

- The prep scale matches their importance; the page carries what that scale
  lists.
- The canon inventory is complete, and every relevant PC has a thread or a
  "no thread".
- Want, leverage, limit, contradiction, and secret are concrete; the secret
  has its truth, stakes, and discovery paths.
- The twist, face, and voice fail the swap test; every hidden truth has a
  tell.
- The portrait and three sample lines came from theatre-of-the-mind and pass
  its final check; the portrait keeps every face word the old page had.
- A villain has an active, interruptible front and several possible endings.
- Every question the page raises has its DM answer; every likely move has
  an answer, a price, and a roll where the outcome is uncertain.
- Each new mint names, in the response, the candidates considered and why none
  fit (`docs/agents/table-ready.md` § Cast before minting).
- Every page filed passes the world-voice search (`docs/agents/table-ready.md` §
  Fill the silence).
- Each new owner page came from its owner skill, loaded and followed.
- Every fighter in reach carries compact numbers, the NPC included; custom
  forms came from `monster-design`.
- `role` is rival, patron, or contact; `[!narration]` is the only callout.
- User-said canon is filed; every invention is a canon proposal, marked on the
  page and listed in the response.
- `wiki lint <path>` is green, and one done-summary names the page and what
  changed.
