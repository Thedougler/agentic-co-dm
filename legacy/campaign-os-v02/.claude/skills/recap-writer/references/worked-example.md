# Worked example (fixture — names below are placeholders, not real
campaign content)

Session `07-the-salt-road`. Gate check:

```
$ git log --oneline | grep "ingest(s07)"
a1b2c3d ingest(s07): the salt road
```

Pages the commit touched (query 2):

```
$ git show --stat a1b2c3d
 vault/campaigns/shattered-sea/npcs/example-quartermaster.md    | 6 +++++-
 vault/campaigns/shattered-sea/locations/example-harbor-town.md | 4 +++-
 vault/campaigns/shattered-sea/quests/example-salt-tithe.md     | 3 ++-
 vault/episodes/07/ingest-review.md | 8 ++++++++
```

Reading each touched page's own new content (each carries a wikilink back
to the transcript instead of a ledger line):

```
vault/campaigns/shattered-sea/npcs/example-quartermaster.md :: "Revealed as smuggling salt off
  the books ([[vault/episodes/07/transcript|transcript]])."
vault/campaigns/shattered-sea/locations/example-harbor-town.md :: "s07 — party first arrives at
  the harbor."
vault/campaigns/shattered-sea/quests/example-salt-tithe.md :: quest_status rumored → active.
```

Transcript excerpts around those passages, for color and exact wording:

```
L040: **DM:** A weathered sign creaks overhead: "Example Harbor — All Dues Paid at the Counting House."
L119: **Marcus (as Tobin):** These numbers don't add up. He's been skimming.
L120: **DM:** The quartermaster's face goes pale. "Fine. Fine! I've been moving salt off the books for years."
L148: **Kaila (as Sable):** We tell the harbor master everything.
```

`vault/episodes/NN-slug/recap.md` (`## Recap`, excerpt): *"The party's longboat put in at
[[example-harbor-town|Example Harbor]] beneath a sign promising all dues
paid at the Counting House — a promise the [[example-quartermaster|harbor
quartermaster]] hadn't been keeping. A quiet look through his books turned
up years of salt moved off the record. Confronted, he folded at once.
[[example-salt-tithe|The salt tithe dispute]] just went from rumor to
open case."* — every sentence traces to a page the commit touched
(quartermaster, harbor-town, salt-tithe) or the transcript color backing
it (L40, L119–120, L148); no line invents a fact none of those pages
carry.

`vault/episodes/NN-slug/highlights.md` (`## Quotes`, excerpt):

```
1. **[[example-npc-tobin|Tobin]]** (L119): "These numbers don't add up. He's been skimming."
2. **DM (as the quartermaster)** (L120): "Fine. Fine! I've been moving salt off the books for years."
```

**Failure case, same session.** A tempting highlight: *L145–147 is the
table arguing for two minutes about whether "skimming" is a bardic
insight check or just roleplay.* That's real-world rules meta with no
in-world action — it fails Hard Rule 7's in-world filter even though it
sits inside the same L-number neighborhood as a page the commit touched,
and it does not ship, no matter how lively the exchange was.
