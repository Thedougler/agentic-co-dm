# View Types

### Table
```yaml
views:
  - type: table
    name: "Wiki Index"
    limit: 100
    order:
      - file.name
      - type
      - status
      - touched
      - formula.age_days
    groupBy:
      property: type
      direction: ASC
```

Omit the grouped property from `order:` — it becomes the group header row, and duplication breaks the view if it's also listed as a column.

### Cards
```yaml
views:
  - type: cards
    name: "Gallery"
    order:
      - file.name
      - tags
      - status
```

### List
```yaml
views:
  - type: list
    name: "Quick List"
    order:
      - file.name
      - status
```
