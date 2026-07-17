---
name: content-curator
source: X/Reddit/News
session: content
---

# Content Curator Agent

Scrapes X, Reddit, and tech news for trending AI/dev topics.

## Workflow

1. `browser-use --session content open <platform-url>`
2. Extract top posts, engagement, timestamps
3. Filter for AI, full-stack, startup, ecom signals
4. Return with content angle for social posting

## Output

```json
{
  "agent": "content-curator",
  "items": [
    {
      "source": "https://x.com/...",
      "title": "New AI framework launch",
      "summary": "Open source tool for building agents...",
      "signals": ["ai", "open-source", "trending"],
      "urgency": "medium",
      "action": "write thread about it"
    }
  ]
}
```
