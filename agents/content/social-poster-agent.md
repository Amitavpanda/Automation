---
name: social-poster
source: LinkedIn/X
session: social
---

# Social Poster Agent

Posts curated content to LinkedIn and X using browser-use.

## Workflow

1. Read curated items from content-curator output
2. `browser-use --session social open <platform>`
3. Write post with extracted angle
4. Schedule or publish

## Output

```json
{
  "agent": "social-poster",
  "timestamp": "ISO-8601",
  "posted": [
    {
      "platform": "LinkedIn",
      "url": "https://linkedin.com/...",
      "status": "published"
    }
  ]
}
```
