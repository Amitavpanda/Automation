---
name: gcf-outreach
description: |
  Manages outreach pipeline for GetCodeFree. Reads drafts from outreach/drafts/, tracks send status, follow-ups. Uses browser-use to send DMs on LinkedIn/X. Maintains pipeline state in outreach/pipeline.json. High-score leads get manual review notification, others go automated.
allowed-tools:
  - Bash(browser-use *)
  - Read
  - Write
  - Bash(cat *)
  - Bash(ls *)
  - Bash(jq *)
---

# GCF Outreach

Sends and tracks outreach messages for GetCodeFree.

## Pipeline File

Pipeline state at `/Users/amitavpanda/Desktop/projects/Automation/getcodefree/outreach/pipeline.json`:

```json
{
  "leads": [
    {
      "id": "uuid",
      "name": "Lead Name",
      "company": "Startup",
      "score": 8,
      "status": "draft/sent/replied/closed",
      "touches": [
        {
          "channel": "linkedin/x/email",
          "template": "template-a",
          "sent_at": "ISO-8601",
          "response": null
        }
      ],
      "next_touch": "ISO-8601"
    }
  ]
}
```

## Workflow

1. Read inbox/ for new high-score leads (7+)
2. For score 9-10: flag for manual review, notify user
3. For score 7-8: use browser-use to send LinkedIn DM or X DM
4. Update pipeline.json with sent status
5. Check pipeline.json daily for follow-ups due
6. Send follow-up if 2+ days since last touch, max 3 touches total
7. If reply received, flag for manual handoff

## Notes

- Always close browser sessions after: `browser-use close --all`
- Never send more than 1 message per lead per day
- Do NOT send on weekends
- Log all sends to `/Users/amitavpanda/Desktop/projects/Automation/getcodefree/outreach/logs/{date}.json`
