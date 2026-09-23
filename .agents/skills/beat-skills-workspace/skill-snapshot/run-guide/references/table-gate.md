# Table Gate

One downward pass of the cockpit in Reading view. Every item holds, or the
draft is incomplete.

## Structure

- `## Scene ends when` is the first cockpit heading in Reading view; the end
  condition is the first line.
- Time budget present. Cut lines only when they change a pacing choice.
- One named *procedure*; Be ready for failures never also tick the clock. Be
  ready for is selective — no ordinary, boring, or redundant rows.
- Beat identity: filename number matches skeleton position; purpose, dramatis
  personae, and hand-off match the skeleton.
- This beat's opening follows from the previous beat's How the Scene Resolves —
  no state reset, teleport, or unexplained jump.
- The central element the table will ask about has an owner and appears on the
  card. Background detail may be marked unknown; the central element may not.
- `dnd5e-mechanics` was loaded for every check, save, DC, grapple, shove,
  attack, damage, quality ladder, or player action mapped to a roll.
- Every consequence is a *ruling* (see cockpit-rules.md § Ruling).
- Previous-session recap appears only on the first beat.

## Cockpit surface

- One cockpit per beat. No dual Now/Run-now pair, Scene menu, separate Ask
  callout, or peer round script.
- The only `> [!` on the card is `[!narration]`. Conditional spoken in
  Narration table columns is `==_italic_==`.
- Column layout uses `col` / `col-md` codeblock fences (not `[!col]`);
  `flexGrow` ratios match the layout table. Spoken `[!narration]` callouts,
  Zones, Be ready for, How the Scene Resolves, Backup, and Battlemap stay full
  width.
- Optional sections stay absent unless this beat spends them at the table.
- Secondary objective, How the Scene Resolves, Roster, and Backup use `##`
  headings.
- Existing overview or identity image embedded near the top when exact art
  exists.
- Battlemap art at the bottom when exact-scene art exists.
- Monster `![[Name#Statblock]]` rows: at most two columns.
- Travel omitted, or one inlined complication with a failure endpoint.

## Copy quality

- Hidden intent, opposition wants, and canon constraints live inline where the
  DM uses them.
- DM-facing text names people, places, and things plainly — no coy
  placeholders, mystery hedges, or "do not reveal this" notes.
- Every check names what success reveals or changes, what failure changes, and
  why the result matters now.
- Every DM-facing line is signal-only: it changes placement, a roll, spoken
  words, risk, route, clock, resource, or NPC response.
- No Partial lecture, 5e-default lecture, or writer note on the card.

## Pass-specific checks

- **Pass 1:** `dnd5e-mechanics` loaded; `writing-for-humans` and
  `theatre-of-the-mind` not loaded. Empty callout stubs and empty Narration
  cells at the TotM slots this beat uses. How the Scene Resolves is one
  unconditional stub plus an options table, not a stack of variant callouts.
  Each option hands off to a skeleton beat.
- **Pass 2:** `writing-for-humans` loaded after pass 1 completes;
  `theatre-of-the-mind` not loaded. DM-facing copy is usable and signal-only.
  Every `[!narration]` body and Narration cell is still empty.
- **Pass 3:** `theatre-of-the-mind` loaded after pass 2 completes. Initial
  Narration is the Layer 1 immediate frame — a stable shared picture and
  something live to respond to. Every stub is filled. Every spoken Narration
  cell is `==_italic_==`.
- **Pass 4:** Reading view checked top to bottom; no spoken slot is empty.
  Action cards sit near the procedure or ruling they support.

## Fun

Every ruling, DC, and design choice on this card serves **fun** first. Change
a DC, drop a constraint, or reshape a beat when the alternative is more fun —
consistency, symmetry, and prior-beat precedent yield to fun.
