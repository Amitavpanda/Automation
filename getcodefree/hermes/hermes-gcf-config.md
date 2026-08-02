# Hermes Agent — GCF Setup

## 1. Set OpenRouter API Key

```bash
echo 'OPENROUTER_API_KEY=sk-or-v1-xxxxxxxx' >> ~/.hermes/.env
```

## 2. Configure Model

```bash
hermes model
# Select: openrouter → deepseek/deepseek-v4-flash:free
```

## 3. Enable Tools

```bash
hermes tools
# Enable: browser, cronjob, file, terminal, web
```

## 4. Run First Skill (Manual Test)

```bash
hermes --skills gcf-lead-scraper "Scrape X/Twitter for founders looking for developers. Focus on posts from last 24h."
```

## 5. Schedule Daily Automation

Once test passes, create cron jobs:

```bash
# Daily at 7am — scrape leads
hermes cron create "0 7 * * *" \
  "Scrape X/Twitter and LinkedIn for founder leads. Score each 1-10. Write to inbox/. Start with X search: 'looking for developer', 'need help building MVP', 'building my app'. Then check LinkedIn." \
  --skill gcf-lead-scraper \
  --name "gcf-daily-leads" \
  --deliver local

# Daily at 8am — draft outreach for new hot leads
hermes cron create "0 8 * * *" \
  "Read inbox/ for new leads scored 7+. For each, pick best template from gcf-content-drafter, personalize, and write draft to outreach/drafts/." \
  --skill gcf-content-drafter \
  --name "gcf-daily-drafts" \
  --deliver local

# Daily at 5pm — pipeline summary
hermes cron create "0 17 * * *" \
  "Read all lead data and pipeline state. Produce a summary report. Save to hermes/reports/." \
  --skill gcf-pipeline-view \
  --name "gcf-evening-report" \
  --deliver local
```

## 6. Start Gateway (for cron)

```bash
hermes gateway install    # install as service
hermes gateway            # or run in foreground
```

## 7. Install ripgrep (Optional, for faster file search)

Homebrew is broken on macOS 26.4.1. Install via:
```bash
curl -LO https://github.com/BurntSushi/ripgrep/releases/download/14.1.1/ripgrep-14.1.1-aarch64-apple-darwin.tar.gz
tar xzf ripgrep-14.1.1-aarch64-apple-darwin.tar.gz
sudo cp ripgrep-14.1.1-aarch64-apple-darwin/rg /usr/local/bin/
rm -rf ripgrep-14.1.1-aarch64-apple-darwin*
```

## Skills Created

| Skill | What it does | Output |
|---|---|---|
| `gcf-lead-scraper` | Scrapes X/LinkedIn for founder leads | `leads/inbox/{ts}-{platform}.json` |
| `gcf-content-drafter` | Reads leads, drafts personalized DMs | `outreach/drafts/{name}-{template}.md` |
| `gcf-outreach` | Sends DMs via browser, tracks pipeline | `outreach/pipeline.json` |
| `gcf-pipeline-view` | Generates daily pipeline summary | `hermes/reports/pipeline-{date}.md` |
