# Automation — Multi-Agent AI System

See `HUMAN.md` for operator profile (Amitav Panda).

## Automation System

Multi-agent AI system using **browser-use CLI** for web scraping + **opencode** with deepseek v4 flash free model. Agents run in parallel for daily tasks.

### Structure

```
Automation/
├── CLAUDE.md          ← This file (profile + system context)
├── agents/            ← Individual agent definitions
│   ├── sales-intel/   ← Lead gen, competitor tracking, gigs, funding
│   └── content/       ← Content & social media automation
├── workflows/         ← Composed multi-agent workflows
├── skills/            ← Custom automation skills
└── config/            ← Agent configurations
```

### Core Principles

1. **browser-use CLI** — primary scraping tool, isolated `--session` per agent
2. **Parallel execution** — spawn agents via `task` tool, run concurrently
3. **Structured output** — all agents return JSON with consistent schema
4. **Session isolation** — each agent gets `browser-use --session <name>`
5. **Cleanup always** — `browser-use close --all` after runs

### Browser-Use Best Practices

| Practice | Why |
|---|---|
| `browser-use state` first | Get element indices before interacting |
| `--session NAME` per agent | Isolated parallel scraping |
| `--headed` for debug | Visual feedback during development |
| Chain with `&&` | Efficient for multi-step flows |
| `browser-use close` on failure | Clear broken sessions before retry |
| Use `browser-use eval` for JS extraction | Fast structured data |
| Cloud connect for heavy tasks | Offload browser to cloud |

### Quick Commands

```bash
browser-use doctor                          # Verify installation
browser-use --session sales open <url>      # Isolated session
browser-use close --all                     # Cleanup all sessions
```

## Daily Automations

| Workflow | Agents | Frequency |
|---|---|---|
| Sales intel | Lead, Content, Gig, Funding, Company | Daily |
| Content & social | Content-curator, Social-poster | Daily/Weekly |

## Agent Output Schema

All agents produce:

```json
{
  "agent": "agent-name",
  "workflow": "workflow-name",
  "timestamp": "ISO-8601",
  "items": [
    {
      "source": "platform-url",
      "url": "https://...",
      "title": "item title",
      "summary": "extracted text",
      "signals": ["tag1", "tag2"],
      "urgency": "high/medium/low",
      "action": "suggested next step"
    }
  ]
}
```
