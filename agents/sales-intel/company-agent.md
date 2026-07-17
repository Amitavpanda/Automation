---
name: company-agent
source: Wellfound/AngelList
session: company
---

# Company Agent

Scrapes Wellfound for startups hiring or building.

## Workflow

1. `browser-use --session company open https://wellfound.com/...`
2. Extract company profiles, open roles, tech stack, stage
3. Filter for seed/series A, AI, ecommerce, developer tools
4. Return with pitch angle

## Output

```json
{
  "agent": "company-agent",
  "items": [
    {
      "source": "https://wellfound.com/...",
      "title": "Y Startup — Building AI Commerce",
      "summary": "Seed stage, hiring founding engineer (React/Python)...",
      "signals": ["hiring", "seed", "founding-engineer", "ai"],
      "urgency": "high",
      "action": "pitch GetCodeFree / apply as founding engineer"
    }
  ]
}
```
