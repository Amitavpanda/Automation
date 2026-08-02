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
- **High competition** (10+ replies) → Skip (your reply drowns) — BUT DM is still valid if Stage 5 passes

### Stage 4 — Direct Reach Extraction

For every surfaced lead, extract from author profile:
- **Twitter handle** (always)
- **Website** (if in bio)
- **Email** (if in bio or website)
- **LinkedIn** (if in bio)
- **Location** (if in bio — useful for personalization)
- **DM open?** (can you DM directly?)

### Stage 5 — Genuine Need vs Engagement Bait (RESPONSE LIKELIHOOD)

**This is the most important check.** Stages 1-4 validate the *account*; Stage 5 validates *whether the author will actually reply to you*. A real account can still post purely for reach and never respond — that wastes your time. Do these BEFORE surfacing:

**Check 5A — Does the author reply to comments on this post?**
- Open the post, expand replies, scroll.
- **PASS**: Author replied to 2+ commenters (evaluating, responsive, real need).
- **FAIL**: Author replied to 0 commenters despite many replies → posting for reach/leads, will ghost you. SKIP.
- **VERIFY WITH**: `browser-use eval` to count reply arrows from author within the thread.

**Check 5B — Specificity of need**
- **PASS**: Post names stack (React/Node/AI), budget, timeline, stage ("wireframes ready", "funding secured", "design done").
- **FAIL**: Vague — "anyone know a dev?", "DM me for details", "looking for someone to help". No specifics = low intent or fishing for portfolio work. SKIP or downgrade to 3-4 score.

**Check 5C — Posting history context**
- **PASS**: Account consistently posts about their own product/business/startup journey. This post fits their narrative.
- **FAIL**: One-off help-request post on an account that posts unrelated content → likely reach-bait or content-marketing trap. SKIP.

**Check 5D — Cross-platform footprint**
- **PASS**: Has website, LinkedIn, company page, or email. Real business behind the post.
- **FAIL**: Nothing but the X profile, no bio, no link. SKIP unless post is extremely specific.

**Auto-SKIP (bait patterns, 2026):**
- "Share your portfolio in comments" + author never replies to any portfolio drop → harvesting portfolios for their own pipeline
- Post asks "anyone know a good developer" but author is themselves a dev/agency/recruiter → fishing for referrals or competitor recon
- "DM me" with zero engagement on the post → gatekeeping reach, likely selling something
- Same help-request post repeated multiple times → aggregator/content strategy, not a real buyer
- Vague question + "I'll follow back" + no specifics → growth hacking, not hiring

### Stage 6 — Response Likelihood Score (add to final scoring)

Score = (Intent × 0.4) + (Low Competition × 0.2) + (Direct Reach × 0.2) + (Stage 5 Response Likelihood × 0.2)

**Stage 5 Response Likelihood value:**
- 1.0 — Author replied to comments + specific need + real business footprint
- 0.7 — Specific need, real account, unknown reply behavior
- 0.4 — Vague need, or no reply-to-comments observed
- 0.0 — Confirmed bait (author never replies, repeated posts, no footprint) → never surface

**New floor rule:** Any lead with Stage 5 likelihood < 0.5 is surfaced ONLY if it has a direct email/DM and a specific budget. Otherwise SKIP regardless of follower count or engagement.

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

### Step 2b — Verify Response Likelihood (Stage 5)

For each passing tweet, open the post and check whether the author actually replies to commenters:
```bash
browser-use --session gcf-keyword-monitor --profile Amitav open "https://x.com/HANDLE/status/ID"
```

Check:
1. Expand replies. Count commenters the author replied to (look for author's handle in reply chains).
2. If 79 replies but 0 author responses → bait, SKIP.
3. If 4 replies but 3 author responses → genuine evaluator, HIGH priority.
4. Assess specificity: stack named? budget? timeline? stage? If completely vague → downgrade.

### Step 3 — Score & Rank

Score = (Intent Score × 0.4) + (Low Competition × 0.2) + (Direct Reach Available × 0.2) + (Stage 5 Response Likelihood × 0.2)

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
      "response_likelihood": {
        "author_replied_to_comments": true,
        "replied_count": 3,
        "specificity": "high",
        "posting_history_fit": true,
        "cross_platform": ["website", "linkedin"],
        "bait_check": "pass",
        "why": "Author replied to 3 commenters asking scope questions, named React+Node stack + budget, active founder account"
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
| Post has 15+ replies | Skip — too noisy (unless DM open + Stage 5 passes) |
| Author has 3 followers, account 2 days old | Skip — likely burner/bot |
| Post says "DM for promotion" | Skip — marketing bait |
| Author has website but no email | Check website for contact page |
| Author has email in bio | High priority — direct reach confirmed |
| Author is verified (blue check) | Higher priority — real person |
| Post mentions specific stack (React/Node/AI) | Higher priority — matches our expertise |
| Post mentions budget | Highest priority — qualified lead |
| LinkedIn post has recruiter keywords | Skip — not a founder need |
| Post in a language other than English | Skip — unless match is obvious |
| 79 replies but author replied to ZERO commenters | SKIP — reach-bait, will ghost you |
| Author replied to commenters asking scope questions | HIGHEST priority — genuinely evaluating |
| Vague "anyone know a dev?", no stack/budget/timeline | Downgrade to 3-4, only surface with direct email |
| Author is themselves a dev/agency/recruiter asking for referrals | SKIP — competitor recon or referral fishing |
| Same help-request posted 3+ times | SKIP — content strategy, not a buyer |
| "Share portfolio in comments" + never replies to drops | SKIP — harvesting portfolios for their pipeline |
| Specific need + budget + responsive author | Surface immediately, top rank |

---

## Notes

- Run 1-2x/day. 15 min total. Speed matters — first helpful reply wins.
- Track which keywords produce high-score leads. Drop low-performers weekly.
- Always `browser-use close --all` after.
- If no results pass filter, return empty set with "Nothing today — try again evening."
- Never surface more than 5 results. If you have 10 passing, pick the top 5 by score.

### LinkedIn Outreach Rules

- **Never put URLs in connection request notes** — LinkedIn flags them as spam, request goes to Spam folder. Use only text.
- **Connection note max 300 chars** — who you are + what you do + why connect. No links.
- **Pitch flow**: Connection request (no link) → they accept → DM with full pitch + links
- **Preserve InMail credits** — only 45 available. Use connection request → DM flow instead. InMail only if they don't accept in 3 days.
- **Mention specific projects in connection notes** (without URLs): EcomAI, App Store product, accounting automation, GetCodeFree. These signal credibility. Example: "I run GetCodeFree — built EcomAI (e-commerce AI platform) and shipped a React Native app to App Store."

### Profile Summary (For Lead Outreach)

Amitav Panda — Senior Full-Stack & AI Engineer
- GetCodeFree (AI-native product engineering)
- 8+ yrs, Founding Engineer @ US AI SaaS startup
- Stack: React/Next.js/React Native/Node.js/Python/AI agents
- Proof: EcomAI, NativeNest (App Store), AccounSaathi (AI accounting automation)
- Website: getcodefreetech.com (only in DM, never in connection request)
