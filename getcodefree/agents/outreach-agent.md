---
name: gcf-outreach
source: LinkedIn
session: gcf-outreach
---

# GetCodeFree Outreach Agent

Sends personalized outreach to qualified leads via LinkedIn.

## Workflow

1. Read leads from `leads/inbox/` (scored by lead-scraper)
2. `browser-use --session gcf-outreach open https://linkedin.com/messaging`
3. Compose and send DM using appropriate template
4. Log sent outreach to `leads/outreach-log.md`

## Templates

See `outreach/linkedin-dm.md` for templates.

## Priority

- Score 8-10: Immediate DM
- Score 5-7: Add to queue
- Score <5: Save for later
