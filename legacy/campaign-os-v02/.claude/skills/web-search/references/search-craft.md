# Web Search — Query, Engine & Source Craft

Detail behind `.claude/skills/web-search/SKILL.md`'s workflow skeleton.

## Query Optimization

### Search Operators

| Operator | Usage | Example |
|----------|-------|---------|
| `"exact phrase"` | Exact match | `"climate change policy"` |
| `site:` | Search within site | `site:reddit.com AI tools` |
| `filetype:` | Find specific files | `filetype:pdf annual report` |
| `-word` | Exclude term | `apple -fruit` |
| `OR` | Either term | `startup OR entrepreneur` |
| `intitle:` | Word in title | `intitle:guide python` |
| `inurl:` | Word in URL | `inurl:blog marketing` |
| `before:` | Before date | `AI before:2023-01-01` |
| `after:` | After date | `ChatGPT after:2024-01-01` |
| `*` | Wildcard | `"how to * in python"` |
| `related:` | Similar sites | `related:techcrunch.com` |

### Query Formulation Techniques

**Start broad, then narrow**
```
Broad: electric vehicles
Narrow: electric vehicle battery technology 2024
More narrow: solid-state battery EV range comparison 2024
```

**Use synonyms and variations**
```
Original: AI writing tools
Variations: artificial intelligence writing software, AI content generator,
machine learning writing assistant, GPT writing tool
```

**Question-based queries**
```
How: "how to implement SSO"
What: "what is zero trust security"
Why: "why companies use kubernetes"
Best: "best practices API design"
Compare: "AWS vs Azure vs GCP comparison"
```

**Source-specific queries**
```
Academic: site:edu OR site:ac.uk [topic]
Government: site:gov [topic]
News: [topic] site:reuters.com OR site:bbc.com
Forum: [topic] site:reddit.com OR site:stackoverflow.com
```

## Specialized Search Engines

| Search Engine | Best For | URL |
|---------------|----------|-----|
| Google Scholar | Academic papers | scholar.google.com |
| Semantic Scholar | AI-powered paper search | semanticscholar.org |
| PubMed | Medical/biomedical | pubmed.ncbi.nlm.nih.gov |
| arXiv | Preprints (CS, physics) | arxiv.org |
| Perplexity | AI-powered research | perplexity.ai |
| Wolfram Alpha | Computations, data | wolframalpha.com |
| Statista | Statistics | statista.com |
| Crunchbase | Company data | crunchbase.com |
| Product Hunt | New products | producthunt.com |
| GitHub | Code/projects | github.com |
| Stack Overflow | Programming Q&A | stackoverflow.com |

## Source Evaluation

### CRAAP Test

| Criterion | Questions to Ask |
|-----------|-----------------|
| **Currency** | When was it published? Updated? |
| **Relevance** | Does it relate to your topic? Audience? |
| **Authority** | Who is the author? Credentials? |
| **Accuracy** | Is it supported by evidence? Verifiable? |
| **Purpose** | Why was it written? Bias? |

### Source Reliability Tiers

| Tier | Source Type | Reliability |
|------|-------------|--------------|
| Tier 1 | Peer-reviewed journals, official statistics | Highest |
| Tier 2 | Quality news (Reuters, AP), industry reports | High |
| Tier 3 | Company blogs, trade publications | Medium |
| Tier 4 | Social media, forums, wikis | Verify required |
| Tier 5 | Anonymous sources, content farms | Low |

## Output Format & Examples

Strategy write-up template:

```markdown
# Web Search Strategy: [Topic]

**Information Need**: [What you're looking for]
**Search Date**: [Date]

## Recommended Search Queries

### Primary Query
[Optimized search query with operators]
**Rationale**: [Why this query works]

### Alternative Queries
1. `[Alternative query 1]` — Use when: [Scenario]
2. `[Alternative query 2]` — Use when: [Scenario]

## Recommended Search Engines

| Engine | Why | Query Modification |
|--------|-----|-------------------|
| [Engine 1] | [Reason] | [Any modifications] |

## Search Strategy

### Step 1: [First search approach]
- Query: `[query]`
- Expected results: [What to look for]

## Verification Strategy
1. [How to verify finding 1]

## Potential Challenges
- [Challenge 1]: [How to address]
```

### Worked Examples

**Recent statistics** — Need: latest global EV sales figures.
```
Query: global electric vehicle sales 2024 statistics
Operators: after:2024-01-01 (filetype:pdf OR site:statista.com)
Sources: IEA, Bloomberg NEF, industry reports
```

**Technical how-to** — Need: how to implement OAuth 2.0.
```
Query: "OAuth 2.0" implementation tutorial
Site-specific: site:stackoverflow.com OR site:auth0.com
Filter: Look for official docs, recent posts
```

**Competitive intelligence** — Need: information about a competitor's product.
```
Query: "[Company name]" product launch OR announcement
Sources: Press releases, news, Product Hunt
Social: site:twitter.com OR site:linkedin.com "[Company]"
```

### Tips

1. Start with the end in mind — know what type of answer you need.
2. Use quotes for exact phrases; combine operators for precision.
3. Try multiple query variations; check source dates — information expires.
4. Cross-reference findings across sources; use specialized engines for specific content types.
