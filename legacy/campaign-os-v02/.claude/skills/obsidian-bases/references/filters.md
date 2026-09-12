# Filters

Filters select which notes appear. Applied globally or per-view.

```yaml
# Single string filter
filters: 'status == "canon"'

# AND: all must be true
filters:
  and:
    - 'status != "archived"'
    - file.inFolder("vault/campaigns/shattered-sea/npcs/")

# OR: any can be true
filters:
  or:
    - file.hasTag("intrigue")
    - file.hasTag("mystery")

# NOT: exclude matches
filters:
  not:
    - file.inFolder("vault/dashboards")

# Nested
filters:
  and:
    - file.inFolder("vault/")
    - or:
        - 'type == "npc"'
        - 'type == "faction"'
```

### Filter operators

`==` `!=` `>` `<` `>=` `<=`

### Useful filter functions

| Function | Example |
|----------|---------|
| `file.hasTag("x")` | Notes with tag `x` |
| `file.inFolder("path/")` | Notes in folder |
| `file.hasLink("Note")` | Notes linking to Note |
