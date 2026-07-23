# Daily Routine — GetCodeFree Inbound Lead System

**Chrome profile**: Amitav (Default directory, logged in as pandaamitav01@gmail.com)
**All browser-use commands**: add `--profile Amitav` to every session command
**All tweet outputs**: must include full URL
**All drafts**: must include `image_prompt` (Gemini prompt) using brand system from getcodefree/brand/image-prompt-system.md

Start at 10:00 AM IST. Run each step. All steps draft only — review before posting.

---

## Weekly Content Mix (Choose Each Day)

| Day | Primary Content Type | Focus |
|---|---|---|
| Mon | Standard posts (authority) + Replies | Senior takes, contrarian opinions |
| Tue | Lead magnet posts + Threads | Framework reveal, client result with CTA |
| Wed | AI coding content (Skill 7) | Cursor, Claude, AI agents |
| Thu | Threads + Replies | Architecture deep-dive, build-in-public |
| Fri | Lead magnet posts + Article | Revenue breakdown, "How I" with lead CTA |
| Sat | AI coding content + Replies | Tool comparisons, tips |
| Sun | Off / Catch up | Review metrics, plan week |

**OR** customize daily: agent asks which mix you want before starting.

---

## Step 1: Top 10 Tweets + Best Article

**Auto prompt:**
```
Skill 1 + Skill 2 from getcodefree/agents/twitter/twitter-lead-agent.md.

Use browser-use --session gcf-twitter --profile Amitav.

Scrape my feed + competitor feeds for last 2 days.
Skill 1: Return top 10 tweets by views passing checklist. Every tweet MUST include full URL.
Skill 2: Return 1 best article matching dev agency/AI/tech domain.

Competitors: @kaif9998, @PrajwalTomar_, @askwhykartik, @Hartdrawss, @cremedgtl, @DeRonin_
My feed: @AmitavPanda99

Present with URLs and why_selected.
```

**Manual alternative**: "Here are tweets/articles I found: [paste URLs]. Score and rank them. Include URLs in output."

**Review**: Read results. Pick which to reply to and which to use for posts.

---

## Step 2: Draft Replies

**MUST draft in browser** — type each reply into X composer.

**Prompt:**
```
Skill 3 from getcodefree/agents/twitter/twitter-lead-agent.md.

Use the tweet URLs from Step 1.
For each: browser-use --session gcf-twitter --profile Amitav --headed open <url>, click reply textbox, type reply.

Guidelines: add value, share experience, no hard sell, 1-3 sentences.
Senior engineer tone. Draft in X browser. Do NOT post.
```

**OR manual**: "Here are URLs I want to reply to: [paste]. Draft replies."

**Review**: Edit if needed. Post manually.

---

## Step 3: Draft Posts (Content Type Based on Day)

**MUST draft in browser** — type each post into X composer. Clear composer between posts.

**Prompt (agent asks):**
```
Which content type today?
[1] Standard posts (authority, opinions)
[2] Lead magnet posts (value + reply CTA → DM capture)
[3] Threads (3-10 tweets, highest reach)
[4] AI coding content (Cursor, Claude, AI agents)
[5] Mix

Based on insights from today's top tweets, draft according to selected type.
For lead magnet: include "Reply KEYWORD and I'll DM you" CTA.
For threads: open composer, type Tweet 1, click "Add another tweet", type rest.
For each post/thread: browser-use --session gcf-twitter --profile Amitav --headed open https://x.com/compose/post, type draft.

Draft only. Do NOT publish until reviewed.
```

**Review**: Edit if needed. Post manually.

---

## Step 4: LinkedIn Cross-Post

**MUST draft in browser** — type into LinkedIn composer.

**⚠️ Full-time constraint:** Frame as senior engineer ("I"), not agency founder ("we"). See Skill 5 in agent for rules.

**Prompt:**
```
Skill 5 from getcodefree/agents/twitter/twitter-lead-agent.md.

Take best content from today and draft LinkedIn versions.

CRITICAL: "I" framing, not "we". Narrative paragraph format.
No agency language. No "book a call". No "GetCodeFree can help".
End with question to drive comments.

1 hashtag max. Open LinkedIn via browser-use --session gcf-linkedin --profile Amitav --headed.
Click "Start a post", type draft in text editor.
Draft. Do NOT publish.
```

**Review**: Edit if needed. Post manually.

---

## Step 5: Write X Article

**Prompt:**
```
Skill 6 from getcodefree/agents/twitter/twitter-lead-agent.md.

Based on today's top content, write 1 X Article (long-form, 800-1200 words).
Topic: AI/tech deep-dive, dev agency lesson, or building in public insight.

Open https://x.com/i/articles via browser-use --session gcf-twitter --profile Amitav.
Type title + body. Leave drafted. Do NOT publish.
```

**Review**: Edit if needed. Post manually.

---

## Step 6: Cleanup

```bash
browser-use close --all
```

---

## Standalone: Keyword Monitor

Run separately 1-2x/day. Not part of main routine.

**Prompt:**
```
Run getcodefree/agents/twitter/keyword-monitor-agent.md.

Search X + LinkedIn for these keywords:
"looking for a developer", "need help building", "build my MVP", "need a tech partner", "looking for dev agency"

Return prioritized list of reply opportunities. Include suggested reply for each.
```

**Best time:** 9 AM (catch overnight posts) + 3 PM (catch afternoon posts). 15 min each.

---

## Checklist

| # | Task | Mode | Time |
|---|---|---|---|
| 1 | Top 10 tweets + article | Auto scrape OR manual | 10:00 |
| 2 | Draft replies | From step 1 OR manual URLs | 10:20 |
| 3 | Draft posts (type-based on day) | Choose content type first | 10:35 |
| 4 | LinkedIn cross-post | From best content today | 10:50 |
| 5 | Write X Article | Long-form from today's insights | 11:00 |
| 6 | Review + post manually | You | 11:15 |
| 7 | Cleanup | Auto | 11:30 |
| 8 | **Keyword monitor (standalone)** | Separate run, 1-2x/day | 9 AM + 3 PM |
