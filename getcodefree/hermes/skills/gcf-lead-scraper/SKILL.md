---
name: gcf-lead-scraper
description: |
  Daily lead scraping for GetCodeFree agency. Scrapes X/Twitter and LinkedIn for founders hiring developers, posting about needing technical help, or building MVPs. Scores leads by fit, outputs structured lead JSON to getcodefree/leads/inbox/. Targets ICP-A1 (funded pre-seed/seed founders, $5-15k budget), ICP-A2 (bootstrapped founders who raised $50k+), ICP-B1 (CTOs at growing startups).
allowed-tools:
  - Bash(browser-use *)
  - Bash(ls *)
  - Bash(cat *)
  - Bash(jq *)
  - Write
---

# GCF Lead Scraper

Scrapes X/Twitter and LinkedIn for potential GetCodeFree clients.

## Platform: X/Twitter

Search for these signals using browser-use:
- "looking for developer" OR "need a developer" OR "need help building"
- "building my MVP" OR "build my app" OR "looking for technical co-founder"
- "shipping soon" OR "almost ready to launch"
- "stuck on development" OR "need dev help"

## Platform: LinkedIn

Search for:
- Posts from founders: "hiring developer", "build my team", "technical co-founder"
- People with "CTO" or "Founder" title at seed-stage startups

## Scoring

Score each lead 1-10 based on:
- 8-10: Funded founder, needs full MVP, budget $5k+
- 5-7: Early-stage founder, building something, potential retainer
- 1-4: Low urgency, not a fit, just gathering info

## Output Schema

Write each lead to `/Users/amitavpanda/Desktop/projects/Automation/getcodefree/leads/inbox/{timestamp}-{platform}-{score}.json`:

```json
{
  "agent": "gcf-lead-scraper",
  "timestamp": "ISO-8601",
  "platform": "x/linkedin",
  "items": [
    {
      "source_url": "https://...",
      "name": "Founder Name",
      "company": "Startup",
      "role": "CEO/CTO/Founder",
      "signal": "original post text",
      "score": 8,
      "urgency": "high/medium/low",
      "action": "LinkedIn DM with template outreach-1"
    }
  ]
}
```

## Workflow

1. Open X/Twitter search for each signal query using browser-use
2. Extract posts from last 24h
3. Score each lead
4. Open LinkedIn, search for matching profiles
5. Cross-reference
6. Write scored leads to inbox/
7. Report summary back
