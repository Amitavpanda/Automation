---
name: gcf-lead-scraper
source: LinkedIn/X/Upwork/Crunchbase/Wellfound
session: gcf-leads
---

# GetCodeFree Lead Scraper Agent

Scrapes multiple platforms for potential GetCodeFree clients.

## Sources & Targets

| Platform | What to Find | Signals |
|---|---|---|
| LinkedIn | Founders hiring, frustrated with dev | "looking for dev", "build my app", "technical co-founder" |
| X/Twitter | #buildinpublic, indie hackers | "shipping soon", "need help with", "MVP" |
| Upwork | Open dev projects | React, Next.js, React Native, AI, full-stack |
| Crunchbase | Recently funded startups | Seed/Series A, AI, ecommerce, fintech |
| Wellfound | Startups hiring engineers | founding engineer, seed stage |

## Workflow

1. `browser-use --session gcf-leads open <platform-url>`
2. `browser-use --session gcf-leads state`
3. Extract leads using `browser-use eval` for JS extraction
4. Score by fit (budget, stage, stack alignment)
5. Output JSON to `leads/inbox/`

## Output Schema

```json
{
  "agent": "gcf-lead-scraper",
  "platform": "linkedin",
  "items": [
    {
      "source_url": "https://...",
      "name": "Founder Name",
      "company": "Startup",
      "signal": "Looking for dev team to build MVP",
      "score": 8,
      "action": "LinkedIn DM with template 1"
    }
  ]
}
```
