# Twitter Inbound Lead System — Prompts

**Chrome profile**: Amitav (Default directory, logged in as pandaamitav01@gmail.com)
**All browser-use commands must include**: `--profile Amitav`
**Every tweet output MUST include its full URL**
**Every draft MUST include `image_prompt`** (Gemini prompt using brand from getcodefree/brand/image-prompt-system.md)
**Every tweet output MUST include its full URL** (https://x.com/handle/status/id)

Two modes per skill: **auto** (agent scrapes) or **manual** (you provide URLs).

---

## Skill 1: Top 10 Tweets

**Auto:**
```
Skill 1 — Top 10 Tweets.

Use browser-use --session gcf-twitter --profile Amitav.
Scrape my feed + competitor feeds for last 2 days.
Find 10 tweets with highest views passing checklist.

CHECKLIST:
- Dev agency, building products, AI/tech, freelancing, SaaS, making money
- Shows authority, high engagement
- Not generic/guru content

FEEDS:
https://x.com/kaif9998
https://x.com/PrajwalTomar_
https://x.com/askwhykartik
https://x.com/Hartdrawss
https://x.com/cremedgtl
https://x.com/DeRonin_
https://x.com/AmitavPanda99

Return JSON with tweet URL (required), author, text, views, likes, why_selected.
```

**Manual:**
```
Skill 1 — Top 10 Tweets (manual).

Here are tweets I selected:
https://x.com/handle/status/...
https://x.com/handle/status/...

Score them against the checklist and return JSON with URLs, author, text, views, likes, why_selected.
```

---

## Skill 2: Best Article

**Auto:**
```
Skill 2 — Best Article.

From same feeds (use --profile Amitav), find 1 long-form post/article from last 2 days with high views.
Filter: dev agency, AI/tech, freelancing, startup/SaaS, senior engineer perspective.

Return JSON with URL (required), title, author, views, summary, why_relevant.
```

**Manual:**
```
Skill 2 — Best Article (manual).

Here's an article I found:
[paste URL]

Summarize it and tell me why it's relevant to GetCodeFree.
```

---

## Skill 3: Draft Replies

**Auto (from Skill 1 results):**
```
Skill 3 — Draft Replies (TYPE IN BROWSER).

Use the top 10 tweets from Skill 1 (each with URL).
For EACH tweet URL: browser-use --session gcf-twitter --profile Amitav --headed open <url>, click reply textbox, type reply.
CRITICAL: Actually type in browser. Do NOT just present text.

GUIDELINES:
- Add value, share experience, ask question
- No hard sell
- 1-3 sentences, senior engineer tone

Draft in X browser. Do NOT publish.
```

**Manual:**
```
Skill 3 — Draft Replies (manual).

Tweet URLs I selected:
https://x.com/handle/status/...
https://x.com/handle/status/...

Draft replies. Same guidelines. Draft in X browser. Do NOT publish.
```

---

## Skill 4: Draft Posts

**Auto (from scrape insights):**
```
Skill 4 — Draft Posts (TYPE IN BROWSER).

Based on insights from today's top tweets and articles, draft 1-3 posts.
Categories: building in public, senior takes, client results, lessons learned.

For EACH post: open X composer via browser-use --session gcf-twitter --profile Amitav --headed, clear composer, type post. One at a time.
CRITICAL: Actually type in browser. Do NOT just present text.
Do NOT publish.
```

**Manual:**
```
Skill 4 — Draft Posts (manual).

Topics I want to post about today:
1. [topic]
2. [topic]
3. [topic]

Open X composer, draft 1-3 posts. Do NOT publish.
```

---

## Skill 5: LinkedIn Cross-Post

```
Skill 5 — LinkedIn Cross-Post (TYPE IN BROWSER).

Take best content from today and draft LinkedIn versions.

ADAPTATION:
- Narrative format, paragraph-style
- More context, less jargon
- CTA for founders/CTOs
- 3-5 hashtags

Open LinkedIn via browser-use --session gcf-linkedin --profile Amitav --headed, click "Start a post", click editor, type draft.
CRITICAL: Actually type in browser. Do NOT just present text.
Do NOT publish.
```

---

## Full Daily Run

```
Run all 6 skills.

IMPORTANT: Use --profile Amitav for every browser-use command.
Logged in as pandaamitav01@gmail.com. Every tweet output MUST include full URL.

1. Skill 1 — Top 10 Tweets (scrape)
2. Skill 2 — Best Article (scrape)
3. Skill 3 — Draft Replies
4. Skill 4 — Draft Posts
5. Skill 5 — LinkedIn Cross-Post
6. Skill 6 — Write X Article (long-form, 800-1200 words)

Present results after each. Draft only. Never publish.
```
