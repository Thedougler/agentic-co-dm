# Shattered Sea Dashboard Templates

Worked recipes matching the real `.base` files in `vault/dashboards/`
(global reference) and `vault/campaigns/shattered-sea/dashboards/`
(per-campaign live state) — read one there before writing a new dashboard;
these show the pattern, not a fixed catalog.

### Full content dashboard (all governed pages)

```yaml
filters:
  and:
    - file.inFolder("vault/")
    - not:
        - file.inFolder("vault/dashboards")

formulas:
  age: '(now() - file.ctime).days.round(0)'

properties:
  formula.age:
    displayName: "Age (days)"

views:
  - type: table
    name: "All Content Pages"
    order:
      - file.name
      - type
      - status
      - touched
      - formula.age
    groupBy:
      property: type
      direction: ASC
```

### NPC tracker with a villains sub-view

Matches `vault/campaigns/shattered-sea/dashboards/npcs.base` — a base
file's `views:` list can carry more than one view, each with its own
`filters:` layered on top of the root filter. The `or:` block is the
per-campaign scoping clause (§ Where to Save in the main SKILL.md): most
pages omit `campaigns:` entirely and default to every campaign.

```yaml
filters:
  and:
    - file.inFolder("vault/campaigns/shattered-sea/npcs/")
    - 'type == "npc"'
    - or:
        - 'campaigns.isEmpty()'
        - 'campaigns.contains("Shattered Sea")'

views:
  - type: table
    name: "NPCs"
    order:
      - file.name
      - location
      - role
      - status
      - tags
      - touched
    groupBy:
      property: location
      direction: ASC
  - type: table
    name: "Villains"
    filters:
      and:
        - 'role.contains("villain")'
    order:
      - file.name
      - location
      - status
      - touched
```

### Quest tracker grouped by quest state

Matches `vault/campaigns/shattered-sea/dashboards/quests.base` —
`quest_status` (in-progress, complete, failed) is a distinct field from the
page-lifecycle `status` (draft, pending, canon):

```yaml
filters:
  and:
    - file.inFolder("vault/campaigns/shattered-sea/quests/")
    - 'type == "quest"'
    - or:
        - 'campaigns.isEmpty()'
        - 'campaigns.contains("Shattered Sea")'

views:
  - type: table
    name: "Quests"
    order:
      - file.name
      - quest_status
      - status
      - touched
    groupBy:
      property: quest_status
      direction: ASC
```

### Prep queue (cross-type, filters on `status` alone)

Matches `vault/campaigns/shattered-sea/dashboards/prep-queue.base` — no
`file.inFolder()` clause, so it spans every content type at once by
filtering on a shared frontmatter value instead of a path:

```yaml
filters:
  and:
    - 'status == "pending"'
    - or:
        - 'campaigns.isEmpty()'
        - 'campaigns.contains("Shattered Sea")'

views:
  - type: table
    name: "Prep Queue"
    order:
      - file.name
      - type
      - touched
    groupBy:
      property: type
      direction: ASC
```
