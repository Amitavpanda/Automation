# GetCodeFree Automation Runner

Run lead scraping + outreach for GetCodeFree.

## Commands

| Command | What It Does |
|---|---|
| "find GCF leads" | Run lead-scraper across all platforms |
| "send outreach" | Run outreach-agent for top leads |
| "GCF daily report" | Full: scrape → score → send → report |
| "show GCF pipeline" | List current leads by stage |

## Pattern

1. Spawn `gcf-lead-scraper` agent via task tool — scrapes all platforms in parallel
2. Score results and write to `leads/inbox/`
3. Spawn `gcf-outreach` agent for high-scored leads
4. Log all results

## Cleanup

```bash
browser-use close --all
```
