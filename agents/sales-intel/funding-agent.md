---
name: funding-agent
source: Crunchbase
session: funding
---

# Funding Agent

Scrapes Crunchbase for recently funded companies.

## Workflow

1. `browser-use --session funding open https://www.crunchbase.com/...`
2. Extract company name, funding amount, series, description
3. Filter for AI, ecommerce, dev-tools verticals
4. Return with outreach angle

## Output

```json
{
  "agent": "funding-agent",
  "items": [
    {
      "source": "https://www.crunchbase.com/...",
      "title": "X Corp raises $10M Series A",
      "summary": "AI-powered commerce platform...",
      "signals": ["funding", "series-a", "ai", "ecommerce"],
      "urgency": "high",
      "action": "outreach — they're building and hiring"
    }
  ]
}
```
