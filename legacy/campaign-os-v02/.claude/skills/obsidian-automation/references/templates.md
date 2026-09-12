# Obsidian Automation — Templates & Query Reference

Detail behind `.claude/skills/obsidian-automation/SKILL.md`'s workflow skeleton. All examples
target `inbox/` or other non-canon working space, never `vault/` (including its
`vault/campaigns/shattered-sea/pcs/` and `vault/episodes/` subtrees).

## Note Creation

```yaml
note_templates:
  daily_note:
    filename: "{{date:YYYY-MM-DD}}"
    folder: "inbox/Daily Notes"
    template: |
      # {{date:dddd, MMMM D, YYYY}}

      ## Morning Intentions
      - [ ]

      ## Tasks
      - [ ]

      ## Notes

      ## Evening Reflection

      ---
      [[{{date:YYYY-MM-DD|-1d}}|← Yesterday]] | [[{{date:YYYY-MM-DD|+1d}}|Tomorrow →]]

  meeting_note:
    filename: "Meeting - {{title}} - {{date}}"
    folder: "inbox/Meetings"
    template: |
      ---
      date: {{date}}
      attendees: {{attendees}}
      tags: meeting
      ---

      # {{title}}

      ## Agenda

      ## Notes

      ## Action Items
      - [ ]

      ## Follow-ups

      [[Meetings MOC]]

  zettelkasten:
    filename: "{{date:YYYYMMDDHHmmss}}"
    content: |
      ---
      id: {{date:YYYYMMDDHHmmss}}
      tags:
      links:
      ---

      # {{title}}

      ## Idea

      ## Source

      ## Connections
      - Related to:

      ## References

  book_note:
    filename: "Book - {{title}}"
    content: |
      ---
      author: {{author}}
      finished:
      rating:
      tags: book
      ---

      # {{title}}
      by {{author}}

      ## Summary

      ## Key Ideas

      ## Highlights

      ## My Thoughts

      ## Action Items
```

## Smart Linking

```yaml
auto_linking:
  rules:
    - pattern: "[[Person/{{name}}]]"
      trigger: "@{{name}}"
      create_if_missing: true

    - pattern: "[[Project/{{project}}]]"
      trigger: "#proj/{{project}}"

  backlink_suggestions:
    enabled: true
    min_mentions: 2

  alias_support:
    - "[[Machine Learning|ML]]"
    - "[[Artificial Intelligence|AI]]"
```

## Dataview Queries

```yaml
dataview_examples:
  tasks_due_today:
    query: |
      ```dataview
      TASK
      WHERE !completed AND due = date(today)
      SORT due ASC
      ```

  recent_meetings:
    query: |
      ```dataview
      TABLE date, attendees
      FROM "inbox/Meetings"
      WHERE date >= date(today) - dur(7 days)
      SORT date DESC
      LIMIT 10
      ```

  project_dashboard:
    query: |
      ```dataview
      TABLE status, due, priority
      FROM #project
      WHERE status != "completed"
      SORT priority ASC
      ```
```

## Workflow Automations

```yaml
web_clipper:
  trigger: browser_extension
  actions:
    - extract_content:
        title: "{{page.title}}"
        url: "{{page.url}}"
        content: "{{selection}}"
    - create_note:
        folder: "inbox/Clippings"
        template: web_clip
    - add_tags: ["web-clip", "{{domain}}"]

research_workflow:
  steps:
    - create_topic_note:
        filename: "Research - {{topic}}"
        folder: "inbox/Research"
    - gather_sources:
        search: "{{topic}}"
        link_to_note: true
    - generate_questions:
        based_on: sources
    - create_sub_notes:
        for_each: key_concept
```

## Graph Analysis

```yaml
graph_insights:
  orphan_notes:
    query: "notes without incoming links"
    action: suggest_connections

  clusters:
    identify: true
    visualize: true

  link_suggestions:
    based_on: content_similarity
    threshold: 0.7
```
