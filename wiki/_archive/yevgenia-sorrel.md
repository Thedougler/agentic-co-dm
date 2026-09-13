---
type: npc
status: draft
publish: false
aliases: []
created: "2026-08-10"
updated: "2026-08-10"
tags: [maritime, intrigue]
summary: "Runs Sunkline General Store at Fathomrush, matching Voyvode General Store shelf for shelf while despising its shopkeeper personally."
owner_skill: ".claude/skills/draft-content/references/npc.md"
subtype: minor
location: "[[fathomrush]]"
role: []
has_active_front: false
campaigns: []
reference_image: ""
voice_id: ""
voice: ""
voice_actor: ""
uid: 9065fd2e-8165-4317-9748-9609c2226e03
---

# Yevgenia Sorrel

**Wants:** to match Voyvode General Store shelf for shelf, rope for rope, price to the copper, and this week Sunkline repriced its rope again, leaving her nothing to show for it but another identical aisle.

> [!read-aloud]
> Sunkline-blue apron, sleeves rolled past the elbow, the same practiced smile the company drills into every clerk. She's straightening a shelf of rope coils that don't need straightening.

*Yevgenia Sorrel*: Everything here's cut to match what's across the water, down to the apron. Don't tell me hers smiles better.

Company-store customer-service voice, drilled flat, cracking on one word, Marta. Underneath the uniform she's sharper with scavenged [[antheri|Antheri]] parts than the job lets her show, patching broken stock with scrap the catalog doesn't cover, and [[catarina-davirelli|Catarina Da'Virelli]] is the one customer who'd actually clock that the fix wasn't off any shelf.

**Runs Sunkline General Store** at Fathomrush's Sunkline pier, stocking [[rope|rope]], tools, rations, and diving sundries repriced daily to match [[marta-kessler|Marta Kessler]]'s ledger across the harbor, item for item. **Despises Marta personally**, not just professionally: the two shops read as interchangeable from the dock, and that reading is what cracks her company patter.

| Field | Detail |
|---|---|
| `primary_goal` | Out-price and out-stock Voyvode General Store's shelf, item for item, so neither company blinks first. |
| `consistent_method` | Recites the company script until "Voyvode" comes up, then drops it mid-sentence for a real jab. |
| `active_problem` | Sunkline just repriced its rope to match Voyvode's again, and she has to restock and reprice with nothing to show for it but another identical aisle. |
| `performance_hooks` | The identikit company clerk drilled into cheerful sameness. Straightens the same shelf-row twice while she talks, like the aisle itself needs correcting. |
| `link_of_relevance` | [[catarina-davirelli\|Catarina Da'Virelli]]: Yevgenia jury-rigs broken stock with scavenged Antheri scrap faster and better than the company catalog allows, and Catarina is the one customer sharp enough to notice the fix wasn't off any shelf. |

Voice & delivery: clipped, company-trained cadence, every line sized for a transaction.

*Yevgenia Sorrel*: This coil's rated for shelf work, cut this morning, priced to the copper Voyvode's charging. Go check, if you don't believe me.

*Yevgenia Sorrel*: *(flat, then sharper)* We match Voyvode on everything but the smile. Mine's real.

```meta-bind
VIEW[{reference_image}][image(class(reference-image-view))]
```

## Relationships

- [[sunkline-company|Sunkline Company]]: employer; the source of the identical apron, patter, and price sheet.
- [[marta-kessler|Marta Kessler]]: rival counterpart at Voyvode General Store, the one person Yevgenia's company sameness can't cover.
- [[catarina-davirelli|Catarina Da'Virelli]]: the customer sharp enough to notice her scavenged fixes for what they are.
