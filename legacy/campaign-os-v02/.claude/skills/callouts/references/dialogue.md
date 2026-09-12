# `[!dialogue]` — performed NPC speech, one line or an exchange

**Role:** every piece of NPC speech the DM performs in character, from a single signature
line to a back-and-forth between two or more parties. Replaces `[!quote]` — retired, same
reason `[!dm]` was: a narrower type superseded by a more capable one.

## Use when

- A signature line that establishes an NPC's voice on first meeting.
- A pre-written response the scene will likely need ("if pressed about the table: ...").
- A short overheard line — a shout from the crowd, a whisper through the door.
- A scripted exchange between two or more NPCs, or an NPC and the party, where the back-and-forth
  itself is the content — a confrontation, a negotiation, a possession scene.

## Never for → use instead

- Scene description or narration around the speech → `[!read-aloud]`; a `[!dialogue]` box carries
  no narration, only lines.
- A full letter, speech, or inscription performed aloud → `[!read-aloud]`.
- Delivery instructions (tone, when to use it) → the line before the callout, or plain prose —
  never inside the box itself.
- Quoting a source text on a docs/meta page → generic `[!quote]` semantics apply there
  (see generic-types.md) — unaffected by this retirement, it's a different type on a different
  page class.

## Two forms

**Single line** — one NPC, no exchange:

- **No custom title.** Bare `[!dialogue]` so Obsidian shows the standard
  type name.
- The spoken line uses `*Name*: text`. No quotation marks.

**Exchange** — two or more speakers trading lines:

- Bare `[!dialogue]`. No speaker in the callout title.
- Every line is its own speaker cue in **bold**, `**Name**: text`, one per beat, separated by a
  lone `>` the same way a read-aloud beat is. Bold, not italic, is deliberate here: a multi-party
  exchange reads as a script, and the bold cue is scannable as a label at a glance across many
  turns — the sole place in the vault bold means dialogue rather than a label prefix
  (`vault/refs/stories/prose-and-character-craft.md` § Dialogue). Consecutive lines by one speaker
  still collapse into one.
- No quotation marks, no dialogue tag — same rules as any speaker line. The lint checks anchored
  on the italic speaker-line shape (`CampaignLiterary.SpeakerLineQuoteMarks`,
  `RedundantDialogueTag`, `DialogueSelfDelivery`, `CampaignDiegesis.MechanicsInDialogue`,
  `DiceInDialogue`) do not yet cover the bold form — widening them collides with unrelated
  `**Success:**`/`**Failure:**` outcome labels elsewhere in the vault — so hold this line to the
  same discipline by eye until they're rescoped.
- A delivery cue may open a line the same way: `**Ashe**: *(pleading)* You cannot enter the house
  of Tyr!`

## Prose contract

- Player-facing register: evocative, in-voice, concrete — this is performance text, same bar
  as a read-aloud box.
- Cut to the spoken words. Anything that isn't a line one of the parties says belongs outside
  the box, in plain prose or a `[!read-aloud]` beat.

## Examples

Single line:

```markdown
> [!dialogue]
> *Nona Black-Jaw*: You sat at my table once. That buys you the truth said slow — it does not buy it twice.
```

Exchange:

```markdown
> [!dialogue]
> **Corven Ashe**: You cannot enter the house of Tyr!
>
> **The Shape**: Tyr is not here. This is an empty box.
>
> **Corven Ashe**: Tyr is in all his temples.
>
> **The Shape**: Your God's love is not unconditional. He does not love us, and he does not love you.
```

## Conversion table — misuses found in this vault

| Found | Fix |
|---|---|
| `[!QUOTE]` / `[!DIALOGUE]` uppercase | lowercase (W22 auto-fixes) |
| `[!quote]` (retired) | rename to `[!dialogue]`; single-line form is otherwise unchanged |
| A quote block carrying scene description | `[!read-aloud]` |
| Delivery notes inside the box | move above the callout or into plain prose |
| An exchange written as a `[!read-aloud]` box with `*Name*:` italic beats | convert to `[!dialogue]` with bold `**Name**:` cues when the box is pure back-and-forth with no narration between lines; keep `[!read-aloud]` when narration beats sit between the lines |

## CSS

```css
.callout[data-callout="dialogue"] {
  --callout-color: 196, 108, 74;
  --callout-icon: lucide-message-circle;
  background-color: rgba(196, 108, 74, 0.08);
  border-left: 4px solid rgb(var(--callout-color));
}
.callout[data-callout="dialogue"] .callout-title {
  font-size: 0.95em;
  letter-spacing: 0.02em;
}
.callout[data-callout="dialogue"] .callout-content {
  font-style: normal;
  font-size: 1.08em;
  line-height: 1.5;
  padding: 0.85em 1.1em 1em;
}
```
