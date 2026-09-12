# Contradictions

A transcript fact beats stale prose. When a page's existing text (prep
guesswork, an earlier assumption, a "not yet encountered" placeholder) is
contradicted by what the transcript shows actually happened, correct the
page directly — rewrite the false line, cite the transcript, done. That's
a `Fact` edit, not a `Review`; the transcript is play, the old line was a
guess, and guesses lose.

The only genuine contradiction left is transcript vs. transcript: two
different sessions' recorded play disagreeing with each other (a retcon,
a player misremembering out loud, a DM ruling that changed between
sessions). That's a real human call — never pick a winner between two
pieces of actual play. Append a CONTRADICTION block to the page instead of
editing past it:

```markdown
> [!warning] CONTRADICTION
> [[vault/episodes/004/transcript]]: "Otar has never left the Shattered Sea."
> Conflicts with: [[vault/episodes/012/transcript]] —
> "back when I sailed the southern reach"
> Detected during: INGEST s12
```

`canon-review` resolves it with the human later; nothing else to write,
the block itself is the flag.
