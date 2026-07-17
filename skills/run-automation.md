# Run Automation Workflows

Trigger various multi-agent automation workflows.

## Available Workflows

| Command | Agents | What It Does |
|---|---|---|
| "run sales intel" | lead, gig, funding, company | Scrape LinkedIn, Upwork, Crunchbase, Wellfound |
| "run content" | curator, poster | Scrape X/Reddit for trends, post to LinkedIn/X |

## How to Run

```bash
# Load the relevant skill/agent files, then spawn agents via task tool
```

## Pattern

1. User says "run sales intel" / "run content" / "daily report"
2. Load the corresponding workflow config
3. Spawn subagents in parallel using `task` tool
4. Each agent runs browser-use in isolated `--session`
5. Collect results, deduplicate, rank, present to user

## Cleanup

Always after run:
```bash
browser-use close --all
```
