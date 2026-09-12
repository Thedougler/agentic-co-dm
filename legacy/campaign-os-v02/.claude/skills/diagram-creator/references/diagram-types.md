# Diagram Creator — Types & Rendering Reference

Detail behind `.claude/skills/diagram-creator/SKILL.md`'s workflow skeleton.

## Diagram Types

### Flowchart / Process Diagram

**Use for**: Business processes, decision trees, workflows.

```mermaid
flowchart TD
    A[Start] --> B{Decision?}
    B -->|Yes| C[Action 1]
    B -->|No| D[Action 2]
    C --> E[End]
    D --> E
```

### Sequence Diagram

**Use for**: API calls, user interactions, system communication.

```mermaid
sequenceDiagram
    participant U as User
    participant A as App
    participant S as Server
    participant D as Database

    U->>A: Click Login
    A->>S: POST /auth/login
    S->>D: Query user
    D-->>S: User data
    S-->>A: JWT token
    A-->>U: Redirect to dashboard
```

### Architecture Diagram

**Use for**: System design, infrastructure, component relationships.

```mermaid
flowchart TB
    subgraph Client
        A[Web App]
        B[Mobile App]
    end

    subgraph Backend
        C[API Gateway]
        D[Auth Service]
        E[User Service]
        F[Order Service]
    end

    subgraph Data
        G[(PostgreSQL)]
        H[(Redis)]
        I[(S3)]
    end

    A & B --> C
    C --> D & E & F
    D --> H
    E --> G
    F --> G & I
```

### Entity-Relationship Diagram

**Use for**: Database design, data models, wiki frontmatter schemas.

```mermaid
erDiagram
    CUSTOMER ||--o{ ORDER : places
    ORDER ||--|{ LINE_ITEM : contains
    PRODUCT ||--o{ LINE_ITEM : "ordered in"

    CUSTOMER {
        int id PK
        string name
        string email
    }
    ORDER {
        int id PK
        date created_at
        int customer_id FK
    }
```

### Class Diagram

**Use for**: OOP design, code structure.

```mermaid
classDiagram
    class Animal {
        +String name
        +int age
        +makeSound()
    }
    class Dog {
        +String breed
        +bark()
    }
    Animal <|-- Dog
```

### State Diagram

**Use for**: State machines, status workflows (e.g. a page's `status:` lifecycle).

```mermaid
stateDiagram-v2
    [*] --> Draft
    Draft --> Submitted: Submit
    Submitted --> InReview: Assign reviewer
    InReview --> Approved: Approve
    InReview --> Rejected: Reject
    Rejected --> Draft: Revise
    Approved --> [*]
```

### Gantt Chart

**Use for**: Project timelines, schedules.

```mermaid
gantt
    title Project Timeline
    dateFormat  YYYY-MM-DD

    section Planning
    Requirements    :a1, 2024-01-01, 14d
    Design          :a2, after a1, 21d

    section Development
    Backend         :b1, after a2, 30d
    Frontend        :b2, after a2, 30d
```

### Mind Map

**Use for**: Brainstorming, concept organization.

```mermaid
mindmap
    root((Project))
        Features
            Feature A
            Feature B
        Team
            Frontend
            Backend
```

### Git Graph

**Use for**: Branch visualization, git workflows.

```mermaid
gitGraph
    commit
    commit
    branch feature
    checkout feature
    commit
    checkout main
    merge feature
    commit
```

## PlantUML Examples

### Sequence Diagram (PlantUML)

```plantuml
@startuml
actor User
participant "Web App" as App
participant "API Server" as API
database "Database" as DB

User -> App: Login request
App -> API: POST /auth/login
API -> DB: SELECT user
DB --> API: User record
API --> App: JWT token
App --> User: Redirect to dashboard
@enduml
```

### Component Diagram

```plantuml
@startuml
package "Frontend" {
    [React App]
    [Mobile App]
}

package "Backend" {
    [API Gateway]
    [Auth Service]
}

database "PostgreSQL" as DB

[React App] --> [API Gateway]
[API Gateway] --> [Auth Service]
[Auth Service] --> DB
@enduml
```

## Customization

### Color Theme

Add to the beginning of a Mermaid block:
```
%%{init: {'theme':'forest'}}%%
```
Available themes: `default`, `forest`, `dark`, `neutral`.

### Direction

`TB` (top to bottom), `BT` (bottom to top), `LR` (left to right), `RL` (right to left).

### Tips

1. Keep it simple — don't overcrowd.
2. Use consistent, descriptive naming.
3. Group related items with subgraphs/packages.
4. Match diagram type to the concept being shown.
5. Use colors sparingly, for emphasis only.
6. Maintain a top-down or left-right hierarchy.

## Rendering Tools

| Tool | URL | Best For |
|------|-----|----------|
| Mermaid Live | mermaid.live | Quick editing |
| PlantUML Server | plantuml.com | PlantUML rendering |
| GitHub | — | Paste directly in markdown files |
| VS Code | — | Mermaid extension |

**Limitations**: cannot render raster images directly; complex layouts may need manual
adjustment; some diagram types aren't supported in every renderer.
