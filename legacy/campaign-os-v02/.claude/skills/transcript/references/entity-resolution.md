Full entity-resolution algorithm (transcript-ingest/SKILL.md § What each fact
becomes), referenced from the condensed rule in core.

Resolution rule for any named entity — `grep -ril "<name>" vault/
vault/campaigns/shattered-sea/pcs/` (aliases resolve through each page's own `aliases:`
frontmatter, so this single grep catches a page's canonical name and any
listed alias alike):
- A hit on the entity's own page → target that page directly.
- A BODY hit on a different page means the entity may live as a sub-entry
  inside it (a Notable NPC on a settlement page, a crew member on a ship
  page): read that page; if it documents this entity, edit that page
  directly and flag a W9-near-miss for the human (promotion to its own page
  is their call), never create a duplicate `New` page.

A miss means `New` with a proposed template type. An ambiguous hit (name
could resolve to two distinct entities) means `Review` — leave a note where
you'd otherwise have edited, never a guess.

Parallel-dispatch caveat: sibling agents may land pages mid-run — re-run
`find vault -name "*.md"` immediately before each chunk's writes and
re-resolve any name that got a new page since the chunk started.

No line numbers on any citation: a wikilink doesn't rot when the transcript
is re-formatted; a cited line number does.
