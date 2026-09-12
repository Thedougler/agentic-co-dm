Full detail on the Gate check (transcript-ingest/SKILL.md § Gate check).

## Speaker-label grep

The gate's grep counts genuine `**Name:** ` lines regardless of what's in the
name — speaker names may contain spaces or parentheses, e.g. "Kaitlin (as
Catarina)", "Nick (DM)".

## Legacy prose-recap alternative gate

A written legacy session log (a prose recap that never passed through audio) is
ingestable when — and only when — `vault/episodes/NNN/transcript.md`'s FIRST line is:

```
LEGACY-SOURCE: <original path or provenance note> — prose recap, no audio
```

That header is the explicit opt-in: the speaker-label threshold is waived (prose
has no `**Name:**` lines and inventing them would fabricate attribution),
transcript-label is skipped entirely. Extraction, chunking, and the human-review
flow are all identical to speaker mode; citations still wikilink to the prose
file, no line numbers.
