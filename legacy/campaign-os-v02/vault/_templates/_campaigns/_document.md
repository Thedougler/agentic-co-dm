---
type: document
status: draft
publish: false
title: ""                      # OPTIONAL (display title if it differs from the H1 heading; absent, the H1 is the title, llm-wiki skill)
aliases: []
summary: ""                    # one sentence, ≤200 chars — cheap page preview, never empty
owner_skill: ".claude/skills/draft-content/references/document.md"   # OPTIONAL — the guide or skill that owns this page's quality
created: "{date}"
updated: "{date}"
tags: []
tier: supporting        # OPTIONAL — core | supporting | peripheral; absent ⇒ supporting (llm-wiki skill)
form: book              # book | tome | letter | treaty | contract | recording | inscription — this document's real-world genre; pick the closest, never invent a new one
author: ""              # OPTIONAL — wikilink to the NPC, faction, or deity that wrote or issued this document; free text only when genuinely anonymous or unattributed in-world
handout: ""              # OPTIONAL — quoted wikilink to the vault/campaigns/*/handouts/ page if this document was ever staged as a table prop; that page transcludes this page's ## Text, never retypes it
campaigns: []            # OPTIONAL — this page's campaign(s), if this repo runs more than one
uid: 5a6522bd-1d89-467d-8819-c3bcf37dc3d4
---

# <Name>

*One-line description: what this document is and why it matters.*

## Text

The document's own verbatim words, exactly as anyone reading it in-world
would encounter them, never a paraphrase or summary. Absorbs books,
tomes, letters, treaties, contracts, recordings, and inscriptions: any
in-world text that exists regardless of whether it's ever shown at the
table. If this text is ever staged as a table prop, the resulting handout
page transcludes this section (`![[<slug>#Text]]`) instead of retyping
it, so the words live here once, always. OPTIONAL only when nobody has
the text yet: it's destroyed, missing, or not yet drafted; state which,
plainly, instead of leaving the heading empty. Delete this condition and
fill the heading for real once the text exists.

## Origin

Who wrote or issued this document, when, and why it exists: the specific
in-world circumstance that produced it, stated plainly, point-first,
never a generic "ancient text" gesture.

## Effects Of Reading

OPTIONAL, delete outright if reading, studying, or carrying this document
does nothing beyond what its words say. What happens to whoever reads it,
whether it leaves them changed, saddled with a compulsion, or simply
holding a fact only they now know. A real numeric or mechanical effect
belongs on that effect's own `item` or `rule` page, linked here instead
of duplicated.
