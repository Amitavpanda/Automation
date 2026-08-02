---
name: gcf-pipeline-view
description: |
  Generates a pipeline dashboard summary for GetCodeFree. Reads all leads from inbox/, pipeline state from pipeline.json, and outputs a formatted markdown report with counts by score, stage, source, and next actions. Use this to get a quick daily snapshot of lead pipeline health.
allowed-tools:
  - Read
  - Bash(cat *)
  - Bash(ls *)
  - Bash(jq *)
---

# GCF Pipeline View

Reads all lead and pipeline data and produces a summary.

## Read these files:

- `/Users/amitavpanda/Desktop/projects/Automation/getcodefree/leads/inbox/` — all lead JSON files
- `/Users/amitavpanda/Desktop/projects/Automation/getcodefree/outreach/pipeline.json` — current pipeline

## Produce Report

```markdown
# GCF Pipeline — {date}

## Summary
- New leads today: {count}
- Total in pipeline: {count}
- Sent: {count}
- Replied: {count}
- Closed/won: {count}

## By Score
- Hot (9-10): {count}
- Warm (7-8): {count}  
- Cold (1-6): {count}

## By Source
- X/Twitter: {count}
- LinkedIn: {count}

## Next Actions
1. Review hot leads and send DMs
2. Follow up on {n} leads due today
3. Reply to {n} new responses
```

## Save

Save to `/Users/amitavpanda/Desktop/projects/Automation/getcodefree/hermes/reports/pipeline-{date}.md`
