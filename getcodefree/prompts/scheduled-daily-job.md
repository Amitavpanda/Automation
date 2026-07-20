# Daily Twitter Inbound Lead System — Scheduled Job

This prompt runs automatically via opencode-scheduler.

## Schedule

Daily at 8:00 AM IST (2:30 AM UTC)

## What It Does

1. **Skill 1** — Scrape X feed + competitor feeds for last 48h, return top 10 tweets by views
2. **Skill 2** — Find 1 high-views article matching dev agency/AI/tech domain
3. **Skill 3** — Draft replies to top 10 tweets
4. **Skill 4** — Draft 1-3 posts in X composer (no publish)
5. **Skill 5** — Draft LinkedIn versions of selected tweets (no publish)

## Execution

Load `agents/twitter/twitter-lead-agent.md` for full instructions.
Use `browser-use --session gcf-twitter` for all X operations.
Use `browser-use --session gcf-linkedin` for LinkedIn operations.

## Output

Present results in summary:
- Top 10 tweets (URLs + why selected)
- Best article (URL + summary)
- Draft replies (tweet URL + reply text)
- Draft posts (text only)
- LinkedIn drafts (text only)

## Post-Run

```bash
browser-use close --all
```
