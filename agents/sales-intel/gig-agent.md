---
name: gig-agent
source: Upwork/Freelancer
session: gigs
---

# Gig Agent

Scrapes Upwork and Freelancer for open development gigs.

## Workflow

1. `browser-use --session gigs open <search-url>`
2. Inspect listings, extract title, budget, description, skills
3. Filter for relevant stack (AI, ecommerce, full-stack, mobile)
4. Return ranked gig list

## Output

```json
{
  "agent": "gig-agent",
  "items": [
    {
      "source": "https://www.upwork.com/...",
      "title": "Build Ecommerce Platform",
      "summary": "Looking for experienced full-stack dev...",
      "signals": ["ecommerce", "react", "node", "budget:5k+"],
      "urgency": "high",
      "action": "submit proposal"
    }
  ]
}
```
