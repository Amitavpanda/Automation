# Daily Routine — GetCodeFree Inbound Lead System

**Chrome profile**: Amitav (Default directory, logged in as pandaamitav01@gmail.com)
**All browser-use commands**: add `--profile Amitav` to every session command
**All tweet outputs**: must include full URL
**All drafts**: must include `image_prompt` (Gemini prompt) using brand system from getcodefree/brand/image-prompt-system.md (https://x.com/handle/status/id)

Start at 10:00 AM IST. Run each step. All steps draft only — review before posting.

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

**Review**: Read results. Pick which to reply to and which to share.

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

## Step 3: Draft Posts

**MUST draft in browser** — type each post into X composer. Clear composer between posts.

**Prompt:**
```
Skill 4 from getcodefree/agents/twitter/twitter-lead-agent.md.

Based on insights from today's top tweets, draft 1-3 posts.
For each post: browser-use --session gcf-twitter --profile Amitav --headed open https://x.com/compose/post, clear composer, type post.
Draft 1 at a time. Do NOT publish until reviewed.
```

**OR manual**: "Topics I want to post about: [list]. Draft 1-3 posts."

**Review**: Edit if needed. Post manually.

---

## Step 4: LinkedIn Cross-Post

**MUST draft in browser** — type into LinkedIn composer.

**Prompt:**
```
Skill 5 from getcodefree/agents/twitter/twitter-lead-agent.md.

Take best content from today and draft LinkedIn versions.
Open LinkedIn via browser-use --session gcf-linkedin --profile Amitav --headed.
Click "Start a post", type draft in text editor.

Narrative format, CTA for founders/CTOs, 3-5 hashtags.
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

## Checklist

| # | Task | Mode | Time |
|---|---|---|---|
| 1 | Top 10 tweets + article | Auto scrape OR manual | 10:00 |
| 2 | Draft replies | From step 1 OR manual URLs | 10:20 |
| 3 | Draft posts | From insights OR manual topics | 10:35 |
| 4 | LinkedIn cross-post | From best content today | 10:50 |
| 5 | Write X Article | Long-form from today's insights | 11:00 |
| 6 | Review + post manually | You | 11:15 |
| 7 | Cleanup | Auto | 11:30 |
