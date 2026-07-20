---
name: gcf-sales-ops
description: Orchestrates full sales pipeline — lead scraping, scoring, outreach queue, pipeline tracking
sessions: gcf-sales
---

# GetCodeFree Sales Ops Agent

Scrapes X, LinkedIn, Upwork, Crunchbase, Wellfound for ICP-matching leads.
Scores by fit, queues for outreach, tracks pipeline.

## ICP Filter (from `icp/definition.json`)

**Target**: US/EU funded founders, CTOs, CPOs needing MVP builds or AI features.
**Signals**: hiring posts, funding news, building-in-public, "need a dev" comments, tech stack matches.

## Workflow

1. **Scrape** — run all source agents in parallel via `browser-use --session gcf-sales`
   - X: search hiring/shipping/building posts
   - LinkedIn: search CTO/Founder posts with capacity signals
   - Crunchbase: recently funded Seed/Series A
   - Wellfound: startups hiring founding engineers
   - Upwork: open projects matching stack
2. **Score** — match against ICP definition, rank 0-10
3. **Queue** — write scored leads to `leads/inbox/`
4. **Alert** — present top 5 for manual review + DM

## Output

```json
{
  "agent": "gcf-sales-ops",
  "date": "2026-07-17",
  "sources_scraped": ["x", "linkedin", "crunchbase", "wellfound", "upwork"],
  "leads_found": 14,
  "top_5": [
    {
      "source": "https://x.com/...",
      "name": "Founder Name",
      "company": "Startup",
      "icp_match": "A1 — US Seed SaaS Founder",
      "score": 9,
      "signal": "Just raised $2M, posting about needing build help",
      "action": "DM — congrats + offer"
    }
  ]
}
```
