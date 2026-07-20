---
name: gcf-twitter-lead
source: X/Twitter
session: gcf-twitter
profile: Default
email: pandaamitav01@gmail.com
purpose: Inbound lead system — scrape OR manual input → drafts replies & posts for GetCodeFree
---

# Twitter Inbound Lead Agent

**Chrome profile**: Amitav (Default directory, logged in as pandaamitav01@gmail.com — X, LinkedIn all authenticated)
**All browser-use commands must use**: `--profile Amitav`

Two modes:
- **Auto**: agent scrapes X feed + competitor feeds, finds top content
- **Manual**: you provide tweet/article URLs directly

Either way → agent drafts replies, posts, LinkedIn cross-posts, X Articles. **Every draft includes image_prompt** for Gemini image generation. Draft only — you review before posting.

## Goal

Grow @AmitavPanda from 284 → 50k followers in 3 months. Generate inbound client leads for GetCodeFree.

## CMO Strategy — Reply vs Post Targeting

| Activity | Target Accounts | Why |
|---|---|---|
| **Replies** (Skill 3) | Lead-rich accounts — founders, startup builders, investors (@levelsio, @gregisenberg, @SahilBloom, @marclou, @ShreyasDoshi) | Visibility in front of potential clients. Every reply = lead signal. |
| **Posts** (Skill 4) | Draw from competitor content insights | Establish authority. Show expertise. Drive followers. |
| **LinkedIn** (Skill 5) | Cross-post from competitor-inspired content | Reach professional/founder audience in a different channel. |
| **Articles** (Skill 6) | Draw from competitor content | Deep authority + long-form reach. Appear in follower feeds. |

**Gold Rule:** Reply where clients hang out. Post what makes you look like the expert. Both matter, but replies on lead-rich accounts drive direct inbound.

---

## 2026 Viral Content Playbook — What Agent Looks For

### What Makes a Tweet Go Viral in 2026

Research-backed patterns (from 847+ tweet analysis, Buffer 45M+ post study, forkoff 140-campaign data):

| Structure | Hook Pattern | Why It Works |
|---|---|---|
| Contrarian take | "Everyone thinks X. They're wrong." | Debate drives reply depth (strongest algosignal) |
| Uncomfortable truth | "Nobody talks about [unspoken reality]" | Recognition drives shares + saves |
| Framework reveal | "The system that [result] in [timeframe]:" | Utility drives bookmarks (top quality signal) |
| Bold prediction | "[Prediction] will happen by [date]." | Controversy drives reply speed (velocity = reach) |
| How I thread | "How I [result] in [timeframe]:" | Narrative keeps dwell time high |
| Revenue breakdown | "I made $X last month. Here's how:" | Numbers + transparency = compound engagement |
| Client result | "Shipped [result] for [client type] in [time]." | Social proof + specificity = lead generation |

### Algorithm Priority Signals (X in 2026):
1. **Engagement velocity** — replies/reposts in first 30 minutes is #1 ranking factor
2. **Reply depth** — multi-level conversation threads beat single reactions
3. **Bookmark rate** — highest quality signal (user wants to return)
4. **Dwell time** — how long people pause before scrolling
5. **Creator authority** — account-level credibility score

### Content Type — What Agent Targets

| Content | Source Accounts | What to Extract | Hook Style to Draft | Goal |
|---|---|---|---|---|
| **Replies** (Skill 3) | Lead-rich only (levelsio, gregisenberg, SahilBloom, marclou, etc.) | Tweets with 50K+ views where your expertise adds value. Look for: founder questions, tech debates, revenue discussions, hiring complaints | Add specific number/result. "I do X and Y happened." 1-3 sentences. No soft praise. | Visibility in front of potential clients. Reply = lead signal. |
| **Posts** (Skill 4) | Competitors + your own insights | Topics trending in dev/AI/agency space. High-engagement posts about: building with AI, agency models, shipping fast, revenue transparency | Contrarian take, framework reveal, or revenue breakdown. Must include specific numbers. | Follower growth. Authority positioning. |
| **LinkedIn** (Skill 5) | Repurpose best post from Skill 4 | Same topic as best-performing post idea | Narrative paragraph format. More context. CTA for founders/CTOs. | Reach professional audience. Lead gen. |
| **Articles** (Skill 6) | Competitors only (kaif9998, DeRonin_, askwhykartik, etc.) | Long-form posts with 100K+ views matching GetCodeFree domain. Look for: AI pipeline insights, agency lessons, technical deep-dives | How I / Framework reveal. 800-1200 words with: hook → insight/body → CTA | Deep authority. Appear in follower feeds. SEO reach. |

### Build-in-Public Rule: 70/30 Split
- **70%** of posts = insights and observations useful to anyone (even non-clients)
- **30%** = direct updates about your product/agency progress
- Flip this ratio and you're a newsletter, not a personal brand.

### Format Rules for Maximum Reach:
- **Hook in first 100 chars** — that's what shows before "Show more"
- **Specific numbers always** — "3 MVPs in 7 days" beats "some projects in a week"
- **Images boost reposts 150%** — include tweet image for every post
- **Threads get 54% more engagement** — use for frameworks/reveals
- **Links go in first reply, not tweet body** — algorithm penalizes link-in-tweet

## Skill 1: Top 10 Tweets (Last 2 Days)

Scrape own feed + competitor feeds + lead-rich accounts for last 2 days. Return 10 tweets with highest views that pass checklist.

**Goal:** 2 types of tweets needed:
- **Competitors/peers** (from competitor feeds) — for content inspiration, articles, posts
- **Lead-rich accounts** (founders, startup builders, people who hire dev agencies) — for reply targets. Replies on these tweets get visibility in front of potential clients.

**Checklist:**
- Relevant to: dev agency, building products, AI/tech, freelancing, SaaS, making money
- Shows authority (senior dev insight, real experience, contrarian take)
- High engagement (views, likes, replies, bookmarks)
- Not generic/guru content — specific, actionable, opinionated
- For LEAD-RICH account tweets: prioritise those where a reply from @AmitavPanda adds value AND gets visibility in front of the account's founder/startup audience
- For COMPETITOR tweets: prioritise content usable as post/article inspiration — frameworks, revenue numbers, contrarian takes, client results

**Competitor feeds (for content + article inspiration):**
```yaml
- https://x.com/kaif9998
- https://x.com/PrajwalTomar_
- https://x.com/askwhykartik
- https://x.com/Hartdrawss
- https://x.com/cremedgtl
- https://x.com/DeRonin_
- https://x.com/AmitavPanda99
```

**Lead-rich accounts (for reply targets — founders, investors, startup audience):**
Default context: dev agency, building in public, AI/tech. Swap targets for other contexts (company page, different niche, B2B SaaS).
```yaml
- https://x.com/levelsio
- https://x.com/gregisenberg
- https://x.com/SahilBloom
- https://x.com/marclou
- https://x.com/ShreyasDoshi
- https://x.com/dvassallo
- https://x.com/jackbutcher
- https://x.com/thedankoe
```

**Workflow:**
1. `browser-use --session gcf-twitter --profile Amitav open <feed-url>`
2. Scroll to load last 2 days
3. `browser-use eval` to extract tweet text, views, likes, timestamp, URL
4. Filter last 48h, score against checklist
5. Return top 10 — **mix of competitor tweets (for posts/articles) and lead-rich tweets (for replies)**. Every tweet MUST include its full URL.

**Or manual**: you pass URLs directly instead.

**Output:**
```json
{
  "skill": "top-10-tweets",
  "source": "scrape",
  "tweets": [
    {
      "url": "https://x.com/handle/status/...",
      "author": "handle",
      "text": "tweet content",
      "views": 50000,
      "likes": 1200,
      "type": "competitor | lead-rich",
      "why_selected": "specific insight"
    }
  ]
}
```

---

## Skill 2: Best Article (Last 2 Days)

From same feeds, find 1 article/post with high views matching GetCodeFree domain.

**Filter:** dev agency, AI/tech, freelancing, money online, startup/SaaS, senior engineer perspective.

**Or manual**: you provide article URLs directly.

**Output:**
```json
{
  "skill": "best-article",
  "url": "https://x.com/...",
  "title": "article title",
  "author": "handle",
  "views": 494800,
  "summary": "key takeaways",
  "why_relevant": "matches GetCodeFree positioning"
}
```

---

## Skill 3: Draft Replies

Takes tweets (from Skill 1 scrape OR URLs you provide) and drafts replies. **MUST type each reply in browser composer.**

**CRITICAL — Reply Targeting Strategy:**
- **PRIORITY: Lead-rich accounts** (founders, startup builders, investors) — replies on these tweets get visibility in front of potential clients who need dev agency services. Think: @levelsio, @gregisenberg, @SahilBloom, @marclou, @ShreyasDoshi
- **SECONDARY: Competitors** — only reply if you can add unique value that positions you as an authority. Avoid fanboy replies. Add insight.
- **NEVER reply to competitors just to be seen.** Every reply must generate a lead signal (visibility in front of the right audience) or position you as an authority.
- CMO mindset: "Will this reply make someone think 'I need this person to build my app'?"

**Usage:**
```
Skill 3 — Draft Replies.

Sources:
- From Skill 1 top 10 (if scrape was run)
- OR manual URLs: [paste URLs]

Draft thoughtful replies in browser. Type each one, do NOT just present text.
```

**Guidelines:** add value, share experience, no hard sell, 1-3 sentences. Senior engineer tone. Lead-gen mindset.

**Workflow:**
For each tweet:
1. `browser-use --session gcf-twitter --profile Amitav --headed open <tweet-url>`
2. `browser-use state` to find reply textbox element index
3. `browser-use click <index>` to focus
4. `browser-use type "<reply>"` to type reply in composer
5. Leave drafted. Do NOT post.

**Also generate** `image_prompt` for each reply (Gemini prompt for the tweet's visual). Use brand system from `getcodefree/brand/image-prompt-system.md`.

**Output:**
```json
{
  "skill": "draft-replies",
  "replies": [
    {
      "tweet_url": "https://x.com/...",
      "draft_reply": "reply text",
      "intent": "add value / share experience",
      "image_prompt": "Image prompt for Gemini: Style: ..."
    }
  ]
}
```

---

## Skill 4: Draft Posts

Open X composer, draft 1-3 posts based on **competitor content insights** OR your topics. **MUST type each post in browser composer.**

**Source:** Pull insights from competitor tweets/articles. Do NOT draw from lead-rich accounts for post content — those are for reply targets only.

**Categories:** building in public, senior takes, client results, lessons learned.

**Usage (auto):** "Draft posts based on insights from today's top tweets."
**Usage (manual):** "Draft posts about these topics: [list]"

**Workflow:**
For each post:
1. `browser-use --session gcf-twitter --profile Amitav --headed open https://x.com/compose/post`
2. `browser-use eval` to clear composer: `document.querySelector('div[aria-label="Post text"]').innerHTML = ''`
3. `browser-use type "<post-text>"` (use single quotes in shell for $ signs)
4. Leave drafted. You click "Post" manually. One post at a time.

**Also generate** `image_prompt` per post (1:1 square 1080×1080). Use brand system.

**Output:**
```json
{
  "skill": "draft-posts",
  "posts": [
    {
      "text": "post content",
      "category": "senior takes",
      "image_prompt": "Image prompt for Gemini: Style: ..."
    }
  ]
}
```

---

## Skill 5: Cross-Post to LinkedIn

Take best content from Skills 1-4 and draft equivalent LinkedIn posts. **MUST type in browser composer.**

**Adaptation rules:**
- LinkedIn: narrative, paragraph-style, more context, less jargon
- CTA for founders/CTOs
- 3-5 relevant hashtags

**Workflow:**
1. `browser-use --session gcf-linkedin --profile Amitav --headed open https://www.linkedin.com/feed/`
2. `browser-use state` to find "Start a post" button
3. `browser-use click <index>` to open composer
4. `browser-use state` to find text editor element
5. `browser-use click <index>` to focus
6. `browser-use type "<content>"` (use single quotes for $ signs)
7. Leave drafted. You click "Post" manually.

---

## Skill 6: Write X Article (Long-Form)

Write 1 original X Article per run based on **competitor content insights**. X Articles are long-form (500-1500 words), appear in followers' feeds, drive high engagement.

**Source:** Pull topic and framing from competitor tweets/articles. Do NOT use lead-rich accounts for article inspiration — those are for reply targets only.

**Categories:** AI/tech deep-dive, dev agency lessons, building in public, senior engineer perspective.

**Workflow:**
1. Pick 1 topic from today's competitor tweets + articles
2. Write 800-1200 word article with: hook, insight/body, CTA
3. `browser-use --session gcf-twitter --profile Amitav open https://x.com/i/articles`
4. Find "Write" or compose button, click
5. Type title + body
6. Leave drafted. Do NOT publish.

**Also generate** `image_prompt` for the article cover (2:1 format, 1600×800). Use brand system.

**Output:**
```json
{
  "skill": "write-article",
  "topic": "article topic",
  "title": "article title",
  "word_count": 850,
  "why_topic": "inspired by today's top content",
  "image_prompt": "Image prompt for Gemini: Style: ..."
}
```

---

## Company Page Posting Mode

For pre-written content posted to company pages (not @AmitavPanda99 personal).

**When you say:** "I have content to post to company [LinkedIn/Twitter]"

**Branch to:**

```
### Mode A — You provide raw content
You give topic/idea/text → I format for each platform → open browser → type

Company voice: professional, outcome-focused, "we" not "I", shorter sentences, CTA for founders/CTOs
Include image_prompt per post

### Mode B — You provide fully formatted copy
You paste exact text per platform → I open browser → type exactly what you gave
No formatting changes. Just typing.

### Mode C — You provide text + I tailor for platforms
You give one version → I adapt for LinkedIn (narrative, hashtags) + Twitter (shorter, hook-first)
```

**Browser sessions for company accounts (separate from personal):**
- Company X: `--session gcf-company-x --profile <profile-name>` (you tell me which profile)
- Company LinkedIn: `--session gcf-company-li --profile <profile-name>` (you tell me which profile)

**Workflow:**
1. You flag you have company content + specify which mode
2. You provide content (raw idea or formatted copy or both)
3. I format/tailor per platform (if Mode A or C)
4. I open browser via `--headed`, type content in composer
5. Leave drafted. You review and post.

---

## Notes

- Chrome profile: `Amitav` (Default directory, logged in as pandaamitav01@gmail.com)
- Sessions: `--session gcf-twitter` and `--session gcf-linkedin`
- Every command: `browser-use --session <name> --profile Amitav`
- Always include full tweet URLs in all outputs
- Every draft includes `image_prompt` field (uses getcodefree/brand/image-prompt-system.md)
- Always `browser-use close --all` after
- Never auto-publish. Draft + present for review.
