# `[!read-aloud]` — boxed text the DM performs

**Role:** the only block on a page spoken to the players, verbatim. Everything else serves
the DM's eyes; this box is the table's ears. It exists so the DM never improvises an entry
moment cold.

Its two jobs at the table are **orient** and **direct**: put the players inside the scene
knowing where they stand, then point them at the thing they now have to answer.

## Use when

- A scene, room, arrival, or reveal has an entry moment the DM should deliver, not improvise.
- An appearance paragraph — NPC first impression, item in hand, creature emerging, location
  first sight.
- A session's strong start or recap opener.
- A document/letter/inscription performed aloud in full (a single spoken line is `[!dialogue]`).

## Never for → use instead

- Mechanics, DCs, dice, conditions → `[!mechanic]` or `[!check]`, placed after the box. The
  box stays pure performance.
- DM-only information → plain prose (`[!dm]` is retired, `.claude/skills/callouts/SKILL.md`).
- One NPC's spoken line → `[!dialogue]`.
- Conditional text ("If the party succeeded...") → two boxes, or DM prose before the box. A
  bracketed conditional read aloud breaks the performance.

## Prose contract

- The box is laid out like a screenplay page, not a paragraph: the GM performs it at a
  glance, eyes up. Its parts, in order:
  1. **Beats.** Each beat is one breath-unit — one image or action, 1–2 short sentences —
     on its own quoted line. A lone `>` line separates beats (never a naked blank line —
     that ends the callout; `obsidian-markdown` references/callouts-syntax.md). The GM
     breathes at every gap.
  2. **Delivery cues (optional, sparse).** An italic parenthetical opening a beat —
     `*(low)*`, `*(beat)*`, `*(building)*`. Cues direct the voice only; they carry no
     scene content and are never spoken.
  3. **Speaker lines.** Anything a character says is its own beat, prefixed with the
     speaker: `*Fioravante*: You have come in on precisely the wrong afternoon.` The
     form — no quotation marks, no dialogue tag, where the delivery cue sits — is
     specified once in `vault/refs/stories/prose-and-character-craft.md` § Dialogue.
     A lone `>` separates it from the narration beat above, same as any other beat.
     This is the sole page-only markup the box permits besides the delivery cues: the
     GM reads the text after the colon and never the name.
  4. **The closing beat** stands alone: the live element, then an open action question
     asking what the players do about it — "What do you do?", "How do you get past it?",
     "How do you stay ahead of it?" (`dnd5e-scene-narration` Hard Rule 7). General enough to
     hold any response: never a binary "or" menu, never an abstract question about nerve or
     willpower, never one that names the check's own mechanical solution. The question is
     its own sentence after the live element, not folded into it. The one exception: a box
     reproducing a document verbatim — a letter, proclamation, or inscription — ends where
     the prop's own text ends.
- Present tense, second person implied. Never tells players what they feel or decide.
- Nothing inside that only makes sense on the page — no bracketed content directions, no
  "see below". The italic delivery cues and the speaker prefixes above are the only
  exceptions; cues direct voice, prefixes name who is talking, and neither is spoken. Numbers players would hear ("the ledge is thirty feet up") belong
  in the box; numbers only the DM uses (DCs, damage) never do.
- Title optional; add one when a page carries several boxes (`[!read-aloud] Mercatura`).
- Drafting the paragraph itself: load `dnd5e-scene-narration` while writing, not as an
  audit afterward (PROJECT.md PJ10). This file owns the container; that skill owns the
  sentences.

### Two modes — position decides which

**Establishing** — the first box on a page, and the first box after any `[!read-aloud]
Transition` (a transition carries the party through time or place, so the frame it lands in
is new). It builds the whole frame from nothing: the players picture their own character
standing in this scene from this box alone, with no memory of an earlier box and no setup
line before it (`vault/refs/theater-of-the-mind-abbreviated.md`,
`vault/refs/theater-of-the-mind-extended.md`). All of:

- a physical anchor for the place, and its rough spatial layout — where things stand
  relative to each other; when a fight can start here, distances in feet (default 25 ft
  when unsure);
- who is present and how they're arranged (front line, scattered, behind cover);
- what is *moving*;
- at least one non-visual sense;
- at least one feature players can *use* — cover, elevation, a hanging, burning, or
  breakable thing (every detail is a toy).

**Continuing** — a box inside a frame an establishing box already built. It carries **what
changed**, in the scene's own terms: what entered, moved, broke, spoke, or stopped since the
table last heard from the box. Detail is the focus control — spend it on the change the
players must act on, let the standing frame stand, and name anything else in a clause or not
at all. Re-describing the whole room here buries the one thing they were meant to react to.

**Same bar, smaller scope.** The two modes differ in what the box covers, never in how well
it's written. A continuing box is shorter because it has less to cover — the frame already
stands — not because it's allowed to be flatter: `dnd5e-scene-narration`'s checklist (senses,
concrete imagery, no vague words, a story turn, ends on the live element) binds a 3-sentence
continuing box exactly as hard as a 6-sentence establishing one. A continuing box that reads
thin because it named the change and stopped, with no sense beyond sight or no specific image,
fails the same way a flat establishing box does — being short is not an excuse.

**Seed the menu.** A box that opens a beat is the only place the players hear the situation
whatever follows it acts on — so every interactable the beat needs them to reach for has its
subject standing in the box: the enemy a listed attack swings at, the notation an
Investigation reads, the crowd an Intimidation works, the door a getaway runs for, the lever
a `[!mechanic]` note assumes they've already found. This covers every check, branch point, or
fight below the box, and any other toy named only in a `[!mechanic]` block or DM-only prose —
not just a check's DC line. A subject that never appears in the box is one the players cannot
see to reach for, and it leaves the DM building the fiction it needs on the spot, mid-beat.
Write the box long enough to hand the table everything the beat asks them to touch.

Sentence budget across all beats: **establishing 4–6** (first arrival), **5–8** for a
combat or scene opening where action can start here (the theater-of-the-mind situation
report needs the extra room); **continuing 3–6**, and 2–3 for a lite establishing box
(revisit, minor sub-location) — the modes `.claude/skills/draft-content/references/location.md` uses. These are working ranges, not
ceilings to squeeze under: a beat whose menu genuinely needs more subjects on the table gets
the sentences to put them there. Cut for repetition and for detail that provokes nothing,
never for length alone.

## Examples

Establishing — page-first box, whole frame built, closing on the thing the table answers:

```markdown
> [!read-aloud] Mercatura
> The smell hits before the sound does. Salt, wet rope, and something frying in oil no one
> will name.
>
> Stall awnings crack in the harbour wind while porters thread the crowd with crates held
> overhead, shouting a rhythm that never quite becomes a song.
>
> At the fish rows a woman guts silverfins without looking down, eyes already pricing you.
>
> *(dry)* She sets the knife down when the crowd puts you in front of her stall, and waits.
>
> What do you say to her?
```

Continuing — same frame, only the change, still landing on a live element:

```markdown
> [!read-aloud]
> The knife comes back up, and this time it is pointed past your shoulder at the awning rope.
>
> Both porters behind you have stopped walking. The crates are still on their shoulders.
>
> What do you do?
```

## Conversion table — misuses found in this vault

| Found | Fix |
|---|---|
| `[!READ-ALOUD]` uppercase | lowercase (W22 auto-fixes) |
| A DC or roll inside the box | move it to a `[!check]` directly below the box |
| "It feels ominous" / told emotion | rewrite via `dnd5e-scene-narration` — show the source of the feeling |
| An establishing box (page-first, or first after a Transition) that only works if an earlier box was just read | rebuild the frame inside it: place anchor and layout, who is present, what is moving |
| A continuing box that re-describes the standing frame | cut it back to what changed since the last box; the frame is already up |
| A box that ends on scenery, mood, or a closed moment | end on the live element, then an open action question — "What do you do?", "How do you get past it?" |
| A box that ends on a statement with no closing question | add one: general, never a binary "or" menu, never naming the check's own solution |
| A `*Set the scene:*` setup line before the box (enforced: W29) | fold anything load-bearing into the box; delete the line |
| A combat that opens with no situation description | add an opening box: layout, distances in feet, arrangement, usable features |
| A box with nothing players can act on (pure mood) | add a usable feature and the spatial layout — every detail is a toy |
| A check menu whose subjects (the target, the notation, the door, the crowd) never appear in the box above it | put each one in the box; the DM should never have to invent the fiction a listed check acts on |
| A single dense block paragraph | split into beat lines with blank `>` lines between (screenplay layout above) |
| Quoted dialogue inside the box (enforced: `CampaignLiterary.DialogueInQuotesBox`) | give the line its own beat as `*Name*: text`, quotes and tag dropped |

## CSS

```css
/* boxed-text identity per the published exemplars (A Most Potent Brew's italic read-aloud, Wild Sheep Chase's shaded boxes) — the read-aloud box must read as a different voice at a glance */
.callout[data-callout="read-aloud"] {
  --callout-color: 201, 162, 74;
  --callout-icon: lucide-scroll-text;
  background-color: rgba(201, 162, 74, 0.07);
  border-left: 4px solid rgb(var(--callout-color));
}
.callout[data-callout="read-aloud"] .callout-content {
  font-style: italic;
  font-size: 1.05em;
  padding: 0.75em 1em;
}
```
