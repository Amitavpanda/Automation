---
name: gcf-keyword-monitor
source: X/Twitter + LinkedIn
session: gcf-keyword-monitor
profile: Default
email: pandaamitav01@gmail.com
purpose: Find real, today-only, low-competition inbound reply/DM opportunities. Validate each lead before surfacing. Extract direct contact points.
---

# Keyword Monitor Agent

**Chrome profile**: Amitav (Default directory — X, LinkedIn authenticated)
**All commands**: `--profile Amitav`

**Run 1-2x/day** (morning 9AM, evening 3PM). 15 min total.

**Goal**: Surface only posts where reply = high chance of response. No spam. No low-effort. No high-competition threads.

---

## Filtering Pipeline (Applied to Every Result)

Every post passes these checks before surfacing:

### Stage 1 — Legitimacy Check

| Signal | Pass | Fail |
|---|---|---|
| Account age | >30 days | <7 days (bot) |
| Follower count | >10 real followers | <5 followers (burner) |
| Posting history | Has 3+ original posts | Only reposts/likes |
| Bio | Has real bio, website, or location | Empty bio, NFT avatar, crypto keywords |
| Engagement on post | Has 0-5 replies (low competition) | Has 20+ replies (noise) |
| Language | Genuine need, specific context | Vague, "DM me for promo," copy-paste text |

**Auto-skip**: posts where author has crypto/NFT profile pic, bio says "promo" or "signal," account <7 days old, post is clearly marketing bait.

### Stage 2 — Intent Score (0-10)

| Score | Criteria |
|---|---|
| 9-10 | Explicitly hiring/needing dev. Specific project context. No replies yet. |
| 7-8 | Clearly looking for dev help. Some replies but <5. Has budget signals. |
| 5-6 | Evaluating options. Thinking about building. Low urgency but real. |
| 3-4 | Vague. "Anyone know a dev?" No specific need mentioned. |
| 0-2 | Skip. Spam, bot, troll, not relevant. |

### Stage 3 — Competition Check

- **Low competition** (0-3 replies) → Surface
- **Medium competition** (4-10 replies) → Surface if score 8+
- **High competition** (10+ replies) → Skip (your reply drowns)

### Stage 4 — Direct Reach Extraction

For every surfaced lead, extract from author profile:
- **Twitter handle** (always)
- **Website** (if in bio)
- **Email** (if in bio or website)
- **LinkedIn** (if in bio)
- **Location** (if in bio — useful for personalization)
- **DM open?** (can you DM directly?)

---

## Keywords (Refined)

### X — High-Signal (Today Only, `f=live`)

```
"looking for a developer" -crypto -nft -promo
"need help building" -crypto -nft -promo
"need a developer" -crypto -nft -promo
"build my MVP" -crypto -nft -promo
"looking for dev agency" -crypto
"need someone to build" -crypto -nft
"looking for react developer" -hiring -job
"need full stack developer" -hiring -job
"recommend an agency" -crypto
"anyone know a good developer"
"need a tech partner" -crypto
"who can build" MVP -crypto
"help me build" startup -crypto -nft
"need to build an app" -crypto -nft
"looking for technical cofounder" -crypto -nft
```

**Why these**: Direct need expression. Skip crypto/NFT noise. Skip job postings (those are HR, not founders).

### X — Mid-Signal (Only if time permits)

```
"thinking of building" startup
"evaluating agencies" development
"how much to build" app
"agency vs freelance" development
"should I build" MVP
```

### LinkedIn — High-Signal

```
"need a developer" -hiring -recruiter
"looking for technical cofounder"
"help with my startup" development
"recommend an agency" web
"need help building" app
```

---

## Workflow

### Step 1 — Search X

```bash
browser-use --session gcf-keyword-monitor --profile Amitav open "https://x.com/search?q=KEYWORD&src=typed_query&f=live"
```

For each keyword:
1. Open search with `f=live` (latest, today only)
2. `browser-use state` to get page state
3. Extract each tweet: text, author handle, timestamp, reply count
4. Apply **Stages 1-4** (legitimacy → intent → competition → reach extraction)
5. Collect passing results

### Step 2 — Validate Author Profile

For each passing tweet, open author profile:
```bash
browser-use --session gcf-keyword-monitor --profile Amitav open "https://x.com/HANDLE"
```

Extract from profile:
- Bio text
- Website link
- Follower count
- Account age
- Location
- Is DM button available?

### Step 3 — Score & Rank

Score = (Intent Score × 0.5) + (Low Competition × 0.3) + (Direct Reach Available × 0.2)

### Step 4 — Present Top 5 Only

Never return more than 5. Quality > quantity.

---

## Output Format (One-Go Response)

```json
{
  "agent": "gcf-keyword-monitor",
  "timestamp": "2026-07-23T10:00:00Z",
  "searches_performed": 12,
  "total_posts_scanned": 84,
  "passed_filter": 5,
  "results": [
    {
      "rank": 1,
      "score": 9.2,
      "post": {
        "url": "https://x.com/founder/status/123456",
        "text": "Need someone to build my MVP — React + Node. Have wireframes and funding. DM me.",
        "timestamp": "2026-07-23T08:15:00Z",
        "reply_count": 2
      },
      "author": {
        "handle": "@founderhandle",
        "profile_url": "https://x.com/founderhandle",
        "bio": "Building XYZ. Seeded by YC. Looking for dev partner.",
        "website": "https://startup.com",
        "email": null,
        "location": "San Francisco",
        "followers": 1200,
        "account_age_days": 340,
        "can_dm": true,
        "direct_reach": ["DM on X", "Website contact form"]
      },
      "validation": {
        "legitimate": true,
        "why": "Real YC founder, active account, specific project scope, low replies",
        "red_flags": []
      },
      "competition": {
        "replies_count": 2,
        "level": "low",
        "your_visibility": "High — early reply, low noise"
      },
      "action": {
        "best_channel": "DM on X",
        "suggested_reply": "Hey — saw you're building an MVP. I ship production-grade React/Node apps in ~3 weeks (just shipped an accounting AI MVP last month). Wireframes + funding == prime time to start. Want to chat about your scope?",
        "timing": "Reply within 1 hour for best response rate"
      }
    }
  ],
  "reply_recommendation": "Reply to top 3 within 1 hour. DM top 1 directly if DM is open. Quality responses only."
}
```

### Output Notes
- **Never return more than 5 results** — quality over volume
- **Every result includes** full validation, author profile, competition context, direct reach options, suggested reply
- **Why this will work** for each result explains the logic
- **Action field** tells the exact channel + reply to use

---

## Reply Guidelines (Updated)

### DM (Best — Private, No Competition)
```
Hey [name], saw your post about building [project]. I ship production-grade [stack] MVPs in ~3 weeks — just shipped [similar project] last month. Happy to share learnings or hop on a quick call no pressure.
```

### Public Reply (Second Best — Shows Expertise)
```
I recently built [similar project] for a client in [timeframe]. Key lesson: [specific insight]. Happy to share the full breakdown if helpful.
```

### Public Reply with CTA to DM
```
We ship production [stack] apps in 3 weeks. Just wrapped [similar project] — zero incidents in week one. DM me if you want to compare notes on your scope.
```

---

## Filtering Edge Cases

| Situation | Decision |
|---|---|
| Post has 15+ replies | Skip — too noisy |
| Author has 3 followers, account 2 days old | Skip — likely burner/bot |
| Post says "DM for promotion" | Skip — marketing bait |
| Author has website but no email | Check website for contact page |
| Author has email in bio | High priority — direct reach confirmed |
| Author is verified (blue check) | Higher priority — real person |
| Post mentions specific stack (React/Node/AI) | Higher priority — matches our expertise |
| Post mentions budget | Highest priority — qualified lead |
| LinkedIn post has recruiter keywords | Skip — not a founder need |
| Post in a language other than English | Skip — unless match is obvious |

---

## Notes

- Run 1-2x/day. 15 min total. Speed matters — first helpful reply wins.
- Track which keywords produce high-score leads. Drop low-performers weekly.
- Always `browser-use close --all` after.
- If no results pass filter, return empty set with "Nothing today — try again evening."
- Never surface more than 5 results. If you have 10 passing, pick the top 5 by score.
