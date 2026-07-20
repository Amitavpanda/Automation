# Daily Prompt — Copy & Paste This

Run this prompt in opencode at 10:00 AM IST. All 5 skills execute sequentially. Draft only — nothing auto-posts.

**Chrome profile**: Amitav (Default directory, logged in as pandaamitav01@gmail.com)
**All browser-use commands use**: `--profile Amitav` (add `--headed` for draft steps)
**Every tweet output**: MUST include full URL (https://x.com/handle/status/id)

---

```
Run the full Twitter inbound lead system from getcodefree/agents/twitter/twitter-lead-agent.md.

IMPORTANT: Use --profile Amitav for ALL browser-use commands. Add --headed for Skills 3-5 (drafting). Logged in as pandaamitav01@gmail.com.
Every tweet output MUST include its full URL (https://x.com/handle/status/id).
Every draft (reply, post, article) MUST include image_prompt for Gemini (use getcodefree/brand/image-prompt-system.md).

Execute all 6 skills in sequence. Present results after each before moving to next.

SKILL 1 — Top 10 Tweets:
Use browser-use --session gcf-twitter --profile Amitav.
Scrape these X feeds for last 2 days and return 10 tweets with highest views that pass the checklist.

Two types of accounts:
- COMPETITORS (for content inspiration for posts/articles):
  - https://x.com/kaif9998
  - https://x.com/PrajwalTomar_
  - https://x.com/askwhykartik
  - https://x.com/Hartdrawss
  - https://x.com/cremedgtl
  - https://x.com/DeRonin_
  - https://x.com/AmitavPanda99
- LEAD-RICH (founders, startup builders — for reply targets):
  - Default set below (context: dev agency, building in public, AI/tech)
  - Swap targets for other contexts (company page, different niche, B2B SaaS, etc.)
  - https://x.com/levelsio
  - https://x.com/gregisenberg
  - https://x.com/SahilBloom
  - https://x.com/marclou
  - https://x.com/ShreyasDoshi
  - https://x.com/dvassallo
  - https://x.com/jackbutcher
  - https://x.com/thedankoe

Checklist: relevant to dev agency, building products, AI/tech, freelancing, SaaS, making money. Shows authority. High engagement. Not generic.
Return JSON with URL (required), author, text, views, likes, type ("competitor" | "lead-rich"), why_selected.

IMPORTANT: Replies target lead-rich accounts (founder audience = potential clients). Posts/articles draw from competitor content (authority positioning).

2026 VIRAL PLAYBOOK — Use for Skills 4-6 drafting:
- Hook in first 100 chars (that's what shows before "Show more")
- Specific numbers always: "3 MVPs in 7 days" beats "some projects in a week"
- Images boost reposts 150% — include image_prompt for every post/article
- Best hook structures: contrarian take, uncomfortable truth, framework reveal, revenue breakdown, "How I [result] in [timeframe]"
- 70/30 split: 70% useful insights, 30% product updates
- Links go in first reply, not tweet body
- Threads get 54% more engagement — use for framework reveals
- Engagement velocity in first 30 min = #1 algorithmic ranking factor

SKILL 2 — Best Article:
From competitor feeds only (not lead-rich accounts), find 1 long-form post from last 2 days with 100K+ views matching dev agency/AI/tech/freelancing domain.
Look for: AI pipeline insights, agency lessons, technical deep-dives, revenue transparency, building-in-public stories with specific numbers.
Return JSON with URL (required), title, author, views, summary, why_relevant.

[WAIT FOR MY REVIEW — I will pick which tweets to reply to and share]

SKILL 3 — Draft Replies (MUST type in browser):
For the top tweets I selected (use their URLs), draft thoughtful replies.
For EACH URL: browser-use --session gcf-twitter --profile Amitav --headed open <url>, click reply textbox, type reply.
CRITICAL: Actually type in browser. Do NOT just present text.

CMO REPLY STRATEGY:
- PRIORITY: Reply on lead-rich accounts (founders) — their audience = potential clients
- SECONDARY: Reply on competitors only when adding unique value that positions you as authority
- Every reply should make someone think "I need this person to build my MVP"
- Lead-gen messaging: focus on speed, outcomes, pipeline approach

Guidelines: add value, share experience, ask question, no hard sell, 1-3 sentences. Senior engineer who ships. Lead-gen mindset.
Do NOT post.

SKILL 4 — Draft Posts (MUST type in browser):
Based on insights from today's competitor content, draft 1-3 posts using best-performing 2026 formats:
- Contrarian take: "Everyone thinks X about dev agencies. They're wrong."
- Framework reveal: "The 5-step pipeline I use to ship MVPs in 7 days:"
- Revenue breakdown: "I made $X last month running AI pipelines. Here's how."
- Client result: "Shipped [result] for [client type] in [timeframe]."
- Uncomfortable truth: "Nobody talks about [unspoken reality of agency life]"

Each post MUST: hook in first 100 chars, include specific numbers, include image_prompt.
For EACH post: open https://x.com/compose/post via browser-use --session gcf-twitter --profile Amitav --headed, clear composer, type post. Draft one at a time.
CRITICAL: Actually type in browser. Do NOT just present text.
Do NOT publish.

SKILL 5 — LinkedIn Cross-Post (MUST type in browser):
Take best content from today and draft LinkedIn versions.
Adaptation: narrative paragraph format, more context, less jargon, CTA for founders/CTOs, 3-5 hashtags.
Open https://www.linkedin.com/feed/ via browser-use --session gcf-linkedin --profile Amitav --headed, click "Start a post", click editor, type draft.
CRITICAL: Actually type in browser. Do NOT just present text.
Do NOT publish.

SKILL 6 — Write X Article (long-form, in browser):
Based on competitor content insights, write 1 original X Article (800-1200 words).

Article format rules for 2026:
- Title: "How I [result] in [timeframe]" or "[Number] [topic] That [outcome]"
- Hook in first 2 sentences with specific claim + numbers
- Body: 5-7 clear sections with sub-headings
- Include real results/data points
- End with CTA (direct or implied)
- MUST include image_prompt (2:1, 1600×800)

Topic: multi-agent systems shift, dev agency lessons, or building in public.
Open https://x.com/i/articles via browser-use --session gcf-twitter --profile Amitav, find write button, type title + body.
Leave drafted. Do NOT publish.

After all skills: browser-use close --all
```

---

## Manual Alternative (No Scrape)

Replace Skill 1+2 with:

```
Skill 3+4+5 from getcodefree/agents/twitter/twitter-lead-agent.md — manual mode.

Use browser-use --profile Default for all commands.

Here are tweets I want to reply to (include URLs):
[URLs]

Here are topics I want to post about:
[topics]

Here is content to adapt for LinkedIn:
[text]

Draft replies, posts, and LinkedIn. Draft only. Do NOT publish.
```

---

## Company Page Posting Mode

When you provide pre-written content for company pages (not @AmitavPanda99 personal).

**Two sub-modes:**

```
COMPANY POST MODE — Format + Post

Company: [GetCodeFree / other name]
Platforms: [LinkedIn, Twitter, both]

Provide content. I'll:
1. Format for each platform (company voice: professional, outcome-focused, "we" not "I")
2. Generate image_prompt for each post
3. Open browser, type in composer
Leave drafted. Do NOT publish.
```

```
COMPANY POST MODE — Just Post

Platforms: [LinkedIn, Twitter]
Content per platform:
- LinkedIn: [paste exact content]
- Twitter: [paste exact content]

I'll open browsers and type exactly what you gave. No formatting changes.
```

**Browser sessions used:**
- Company Twitter: need separate session + profile (tell me which Chrome profile is logged into company X account)
- Company LinkedIn: need separate session + profile (tell me which Chrome profile is logged into company LinkedIn)
- Default: I'll use `--session gcf-company --profile <you-tell-me>`
