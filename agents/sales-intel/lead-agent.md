---
name: lead-agent
source: LinkedIn
session: leads
---

# Lead Agent

Scrapes LinkedIn for people hiring developers or seeking tech help.

## Workflow

1. `browser-use --session leads open https://www.linkedin.com`
2. `browser-use --session leads state` — get element indices
3. Search for hiring posts, use `browser-use eval` for JS extraction
4. Extract: profile URLs, post text, engagement, hiring signals
5. Output JSON with scored leads

## Signals

- "hiring" / "looking for" / "we're building" / "need a dev"
- Technical stack mentions (React, Python, AI, Node, etc.)
- Ecommerce, SaaS, AI startup keywords

## Output

```json
{
  "agent": "lead-agent",
  "items": [
    {
      "source": "https://www.linkedin.com/...",
      "title": "Hiring Senior Engineer",
      "summary": "We're looking for a full-stack engineer...",
      "signals": ["hiring", "full-stack", "react"],
      "urgency": "high",
      "action": "DM or connect"
    }
  ]
}
```
