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

## 3 Content Types — You Choose Daily

Before drafting, agent asks which mix:

```
Which content type(s) today?
[1] Standard posts (authority, opinions, insights)
[2] Lead magnet posts (value post → reply CTA → DM lead capture)
[3] AI coding content (Cursor, Claude, Perplexity, AI agents)
[4] Threads (3-10 tweet sequence, highest reach)
[5] All of the above
[6] Custom mix (tell me)
```

Agent generates posts per selected type. Each includes `image_prompt`.

## Core Flow

Two modes:
- **Auto**: agent scrapes X feed + competitor feeds, finds top content
- **Manual**: you provide tweet/article URLs directly

Either way → agent drafts content per your chosen types. Draft only — you review before posting.

---

## Goal

Grow @AmitavPanda from 284 → 50k followers in 3 months. Generate inbound client leads for GetCodeFree.

---

## CMO Strategy — Reply vs Post Targeting

| Activity | Target Accounts | Why |
|---|---|---|
| **Replies** (Skill 3) | Lead-rich accounts — founders, startup builders, investors (@levelsio, @gregisenberg, @SahilBloom, @marclou, @ShreyasDoshi) | Visibility in front of potential clients. Every reply = lead signal. |
| **Posts** (Skill 4) | Draw from competitor content insights | Establish authority. Show expertise. Drive followers. |
| **LinkedIn** (Skill 5) | Cross-post from competitor-inspired content | Reach professional/founder audience in a different channel. |
| **Articles** (Skill 6) | Draw from competitor content | Deep authority + long-form reach. Appear in follower feeds. |

**Gold Rule:** Reply where clients hang out. Post what makes you look like the expert. Both matter, but replies on lead-rich accounts drive direct inbound.

---

## 2026 Algorithm Priority Signals

1. **Engagement velocity** — replies/reposts in first 30 minutes
2. **Bookmark rate** — highest quality signal (user wants to return)
3. **Reply depth** — multi-level conversation threads
4. **Dwell time** — how long people pause before scrolling

**Design for bookmarks + replies, not likes.** Content that gets saved and discussed gets algorithm boost.

---

## Skill 1: Top 10 Tweets (Last 2 Days)

Scrape own feed + competitor feeds + lead-rich accounts for last 2 days. Return 10 tweets with highest views that pass checklist.

**Goal:** 2 types of tweets needed:
- **Competitors/peers** — for content inspiration, articles, posts
- **Lead-rich accounts** — for reply targets. Replies on these get visibility in front of potential clients.

**Checklist:**
- Relevant to: dev agency, building products, AI/tech, freelancing, SaaS, making money
- Shows authority (senior dev insight, real experience, contrarian take)
- High engagement (views, likes, replies, bookmarks)
- Not generic/guru content — specific, actionable, opinionated
- For LEAD-RICH account tweets: prioritise those where a reply from @AmitavPanda99 adds value AND gets visibility in front of the account's founder/startup audience
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
Default context: dev agency, building in public, AI/tech. Swap targets for other contexts.
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

**AI/Tech feeds (for Skill 7 — AI coding content):**
```yaml
- https://x.com/PrajwalTomar_         # Cursor MVP content
- https://x.com/kaliiiiiiiiii          # AI/tooling takes
- https://x.com/nickfloats             # AI dev insights
- https://x.com/levelsio               # builds with AI, transparent revenue
- https://x.com/mckaywrigley           # AI apps ship fast
- https://x.com/dotey                  # AI agents
- https://x.com/yoheinakajima          # AI agent frameworks
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
- **PRIORITY: Lead-rich accounts** (founders, startup builders, investors) — replies on these tweets get visibility in front of potential clients who need dev agency services.
- **SECONDARY: Competitors** — only reply if you can add unique value that positions you as an authority.
- Every reply must generate a lead signal (visibility in front of the right audience) or position you as an authority.

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

**Also generate** `image_prompt` for each reply (Gemini prompt for the tweet's visual). Use brand system.

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

## Skill 4: Draft Posts (Standard + Lead Magnet + Threads)

Open X composer, draft 1-3 posts based on **competitor content insights** OR your topics. **MUST type each post in browser composer.**

### Format Options (Agent asks which):

```
Post format?
[1] Single post (standard)
[2] Lead magnet post (value + reply CTA for DM capture)
[3] Thread (3-10 tweets, highest reach)
[4] Mix
```

### Lead Magnet Posts

Structure:
```
Tweet 1-3: Value content (insight, framework, client result, take)
Last tweet: CTA → "Reply KEYWORD and I'll DM you [free template/resource]"
```

Lead magnet CTAs work for:
- "Reply BLUEPRINT and I'll DM you our 7-Day MVP Blueprint template"
- "Reply AUDIT and I'll DM you our Startup Tech Stack Audit"
- "Reply CHECKLIST and I'll DM you our production deployment checklist"
- "Reply SCOPING and I'll DM you our MVP scoping template"

**Why this works:** X algorithm boosts replies. You capture warm leads in DMs. Low friction.

### Threads

Thread = 3-10 connected tweets. 54% more engagement than single posts.

Structure:
```
Tweet 1: Hook (contrarian take, specific claim, or question)
Tweet 2-8: Body (one idea per tweet, build the case)
Tweet 9 (optional): Summary / key takeaway
Tweet 10 (optional): Lead magnet CTA (if lead magnet mode)
```

**Algorithm benefit:** Threads get high bookmark rate + reply depth — two top ranking signals.

**Workflow for thread:**
1. `browser-use --session gcf-twitter --profile Amitav --headed open https://x.com/compose/post`
2. Type Tweet 1
3. Click "Add another tweet" button (find via `browser-use state`)
4. Type Tweet 2
5. Repeat for remaining tweets
6. Leave drafted. Do NOT publish.

**Categories:** building in public, senior takes, client results, lessons learned, AI coding.

### Source:** Pull insights from competitor tweets/articles and AI/tech feeds. Do NOT draw from lead-rich accounts for post content — those are for reply targets only.

**Usage:**
```
Skill 4 — Draft Posts.

Sources: competitor insights + AI coding feeds.
Format: [single | lead magnet | thread | mix]
Topics from today's top 10 tweets.

Draft in browser. Do NOT publish.
```

**Workflow for single/lead magnet post:**
For each post:
1. `browser-use --session gcf-twitter --profile Amitav --headed open https://x.com/compose/post`
2. `browser-use eval` to clear composer: `document.querySelector('div[aria-label="Post text"]').innerHTML = ''`
3. `browser-use type "<post-text>"` (use single quotes in shell for $ signs)
4. Leave drafted. You click "Post" manually. One post at a time.

**Also generate** `image_prompt` per post (1:1 square 1080×1080). For threads, generate 1 image prompt for the thread cover.

**Output:**
```json
{
  "skill": "draft-posts",
  "format": "single | lead-magnet | thread",
  "posts": [
    {
      "text": "post content (first tweet if thread)",
      "thread_tweets": ["tweet 1", "tweet 2", "..."],
      "category": "senior takes",
      "lead_magnet_keyword": "BLUEPRINT",
      "image_prompt": "Image prompt for Gemini: Style: ..."
    }
  ]
}
```

---

## Skill 5: Cross-Post to LinkedIn

Take best content from Skills 1-4 and draft equivalent LinkedIn posts. **MUST type in browser composer.**

**⚠️ CRITICAL — Full-Time Constraint Strategy**

Amitav is full-time employed. LinkedIn content must position him as a senior engineer sharing knowledge, NOT as a dev agency founder selling services.

| ✅ Post This (Safe) | ❌ Avoid This (Risky) |
|---|---|
| Architecture deep-dives: "How I approach X" | "We build apps for startups" |
| AI coding workflows: "My Cursor/Claude setup" | "GetCodeFree can help you build" |
| Client result: "Helped a startup friend build X" | Pricing, packages, "book a call" |
| Engineering opinions: "What production-grade means" | "We're a dev agency" language |
| "I" framing (individual practitioner) | "We" framing (agency/organization) |

**Pipeline:**
```
LinkedIn post (personal, senior engineer voice)
  → DMs asking "how can I build this?"
  → "I help startups with this on the side. Happy to chat."
  → Qualified? → Share GetCodeFree company page
```

**Adaptation rules (X → LinkedIn):**
- X: punchy, casual, "we/our" (agency voice is fine on X)
- LinkedIn: narrative, paragraph-style, **"I" not "we"**, more context
- End with question or discussion prompt (not hard CTA)
- 1 hashtag max (3+ triggers spam filters in 2026)
- Same content as X, different framing

**Workflow:**
1. `browser-use --session gcf-linkedin --profile Amitav --headed open https://www.linkedin.com/feed/`
2. `browser-use state` to find "Start a post" button
3. `browser-use click <index>` to open composer
4. `browser-use state` to find text editor element
5. `browser-use click <index>` to focus
6. `browser-use type "<content>"` (use single quotes for $ signs)
7. Leave drafted. You click "Post" manually.

**Output:**
```json
{
  "skill": "linkedin-crosspost",
  "framing": "senior-engineer",
  "post": {
    "text": "LinkedIn post content (I framing, narrative, 1 hashtag max)",
    "x_source": "link to original X post",
    "adaptation_notes": "changed we→I, removed agency language, added question at end"
  }
}
```

---

## Skill 6: Write X Article (Long-Form)

Write 1 original X Article per run based on **competitor content insights**. X Articles are long-form (500-1500 words), appear in followers' feeds, drive high engagement.

**Source:** Pull topic and framing from competitor tweets/articles. Do NOT use lead-rich accounts for article inspiration — those are for reply targets only.

**Categories:** AI/tech deep-dive, dev agency lessons, building in public, senior engineer perspective, AI coding deep-dive (Cursor, agents, tooling).

### ⚠️ Draft.js Formatting Limitation

X Articles uses Draft.js rich text editor. Only `type` input persists. No eval/execCommand/innerHTML/toolbar-click formatting works — Draft.js reverts all DOM changes.

**Bold headings** — use unicode Mathematical Bold characters when typing via `type`:
- `𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙`
- `𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳`
- `𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗`
Example heading: `𝐓𝐡𝐞 𝐅𝐫𝐚𝐦𝐞𝐰𝐨𝐫𝐤`, `𝐏𝐡𝐚𝐬𝐞 𝟏: 𝐀𝐫𝐜𝐡𝐢𝐭𝐞𝐜𝐭𝐮𝐫𝐞`

**After typing**, user must manually apply bold/italic via browser toolbar.

### Image Placeholders

Include `[Image: description]` text typed inline between sections. Use `keys "Enter"` + `type` to add new paragraphs. Placeholders positioned at article end can be cut/pasted by user.

### Writing Workflow

1. `browser-use --session gcf-article --profile Amitav open https://x.com/compose/articles`
2. Click draft or create new, click body editor
3. `browser-use type "<text>"` for body paragraphs
4. `browser-use keys "Enter"` between paragraphs
5. For headings, use Mathematical Bold unicode in the type string
6. For image placeholders, type `[Image: description]` at target positions
7. Leave drafted. User manually bolds/italics and adds images in browser.

### Article Promotion Post

When article is published, draft a tweet to share it. Options by goal:

| Goal | Hook |
|---|---|
| Reach | Result/stat opener. "Shipped X in Y weeks. Here's how." |
| Engagement | Question. "What's your non-negotiable step when building with AI?" |
| Bookmark | List-style. "The 5-phase framework for..." |
| Clicks | Money/ROI framing. "Cost client what 2 weeks of discovery alone would." |

Money framing template:
```
Shipped [result] in [timeframe]. Cost [money reference].

The math: shorter build = lower burn = faster revenue.

Full breakdown → [article link]
```

### Image Prompts

Generate 5 image prompts per article using `getcodefree/brand/image-prompt-system.md`:
- Cover (5:2, 1600×640)
- 4 inline: one per relevant section, matching the surrounding content's visual subject

**Output:**
```json
{
  "skill": "write-article",
  "topic": "article topic",
  "title": "article title",
  "word_count": 850,
  "why_topic": "inspired by today's top content",
  "promotion_post": "draft tweet to share article",
  "image_prompts": [
    {"position": "cover", "prompt": "Gemini prompt..."},
    {"position": "section-1", "prompt": "Gemini prompt..."}
  ]
}
```

---

## Skill 7: AI Coding Content (Cursor / Claude / Perplexity / AI Agents)

Dedicated skill for fetching + drafting content about AI coding tools. Runs alongside Skills 1-6 or standalone.

**Sources:** Scrape AI/tech feeds (defined in Skill 1) for posts about:
- Cursor (composer, agent, rules, workflows)
- Claude Code
- Perplexity (as dev tool)
- AI agents (autonomous coding, agent pipelines)
- Kimi K3, Copilot, Cline, Bolt, Lovable
- AI vs traditional dev debates
- Vibe coding techniques
- MCP (Model Context Protocol) servers

**Workflow:**
1. `browser-use --session gcf-twitter --profile Amitav open <feed-url>`
2. Scrape AI/tech feeds (PrajwalTomar_, kaliiiiiiiiii, nickfloats, levelsio, mckaywrigley, dotey, yoheinakajima)
3. Extract posts mentioning: Cursor, Claude, Perplexity, AI agents, AI coding, vibe coding
4. Draft 1-3 posts using these formats:
   - "My [tool] workflow for [task]"
   - "Where [tool] fails for production (and what I use instead)"
   - "Comparison: [tool A] vs [tool B] for [use case]"
   - "Tip: [specific technique] in [tool] that most people don't know"
5. Include `image_prompt` per post

**Usage:**
```
Skill 7 — AI Coding Content.

Scrape AI/tech feeds for Cursor/Claude/Perplexity/AI agent posts.
Draft 1-3 posts from insights.

Type in browser. Do NOT publish.
```

**Output:**
```json
{
  "skill": "ai-coding-content",
  "source": "scrape | manual",
  "feeds_scraped": ["PrajwalTomar_", "levelsio", "mckaywrigley"],
  "posts": [
    {
      "text": "post text",
      "category": "cursor-workflow | ai-coding-tip | comparison",
      "tool_mentioned": "Cursor",
      "image_prompt": "Image prompt for Gemini: Style: ..."
    }
  ]
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
- Before Skill 4, ask user: standard post, lead magnet post, or thread? Default = all 3
- Threads = 54% more engagement. Lead magnet = capture warm leads in DMs.
- Always `browser-use close --all` after
- Never auto-publish. Draft + present for review.

### Technical Findings

- **X Articles (Draft.js)**: Only `type` input persists. eval/execCommand/innerHTML/DOM-insert all reverted by Draft.js internal state. `keys "Meta+B"` and toolbar clicks via eval also blocked.
- **Contenteditable structure**: `contenteditable > div > div[blocks] > .longform-unstyled > .public-DraftStyleDefault-block > span[data-offset-key] > span[data-text="true"]`
- **eval returning `None`**: When eval sets `innerHTML` or performs DOM mutations, the return value is swallowed. Check for `<strong>` via `indexOf('strong')>=0` on innerHTML to verify.
- **Article URL format**: `https://x.com/compose/articles/edit/<id>` not `https://x.com/i/articles`
- **All content types daily**: User wants standard + lead magnet + thread + AI coding content each run.
