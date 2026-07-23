# Daily Prompt — Copy & Paste This

Run this prompt in opencode at 10:00 AM IST. All skills execute sequentially. Draft only — nothing auto-posts.

**Chrome profile**: Amitav (Default directory, logged in as pandaamitav01@gmail.com)
**All browser-use commands use**: `--profile Amitav` (add `--headed` for draft steps)
**Every tweet output**: MUST include full URL (https://x.com/handle/status/id)

---

```
Run the full Twitter inbound lead system from getcodefree/agents/twitter/twitter-lead-agent.md.

IMPORTANT: Use --profile Amitav for ALL browser-use commands. Add --headed for Skills 3-5 (drafting). Logged in as pandaamitav01@gmail.com.
Every tweet output MUST include its full URL (https://x.com/handle/status/id).
Every draft (reply, post, article) MUST include image_prompt for Gemini (use getcodefree/brand/image-prompt-system.md).

BEFORE Skill 4, ask me: which content type today?
- Standard posts
- Lead magnet posts (value + reply CTA for DM capture)
- Threads (3-10 tweets)
- AI coding content (Cursor/Claude/Perplexity/agents)
- Mix

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

Also scrape AI/TECH feeds for potential Skill 7 content:
  - https://x.com/PrajwalTomar_         # Cursor MVP content
  - https://x.com/kaliiiiiiiiii          # AI/tooling takes
  - https://x.com/nickfloats             # AI dev insights
  - https://x.com/levelsio               # builds with AI, transparent revenue
  - https://x.com/mckaywrigley           # AI apps ship fast
  - https://x.com/dotey                  # AI agents
  - https://x.com/yoheinakajima          # AI agent frameworks

Checklist: relevant to dev agency, building products, AI/tech, freelancing, SaaS, making money. Shows authority. High engagement. Not generic.
Return JSON with URL (required), author, text, views, likes, type ("competitor" | "lead-rich" | "ai-tech"), why_selected.

IMPORTANT: Replies target lead-rich accounts (founder audience = potential clients). Posts/articles draw from competitor content (authority positioning).

2026 CONTENT PLAYBOOK — Use for Skills 4-7 drafting:
- Hook in first 100 chars (that's what shows before "Show more")
- Specific numbers always: "3 MVPs in 7 days" beats "some projects in a week"
- Images boost reposts 150% — include image_prompt for every post/article
- Best hook structures: contrarian take, uncomfortable truth, framework reveal, revenue breakdown, "How I [result] in [timeframe]"
- 70/30 split: 70% useful insights, 30% product updates
- Links go in first reply, not tweet body
- Threads get 54% more engagement — use for framework reveals
- Design for BOOKMARKS + REPLIES, not likes. Content that gets saved and discussed gets algorithm boost.
- Lead magnet posts: value content + "Reply KEYWORD and I'll DM you [template]"

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

[ASK ME: Which content type for today?]

SKILL 4 — Draft Posts (MUST type in browser, content type based on day):
Ask me: standard, lead magnet, thread, AI coding, or mix.

Based on insights from today's competitor content AND selected content type, draft 1-3 posts using best-performing 2026 formats:
- Contrarian take: "Everyone thinks X about dev agencies. They're wrong."
- Framework reveal: "The 5-step pipeline I use to ship MVPs in 7 days:"
- Revenue breakdown: "I made $X last month running AI pipelines. Here's how."
- Client result: "Shipped [result] for [client type] in [timeframe]."
- Uncomfortable truth: "Nobody talks about [unspoken reality of agency life]"
- Lead magnet: same formats + end with "Reply KEYWORD and I'll DM you [template]"
- Thread: hook tweet → 3-8 body tweets → summary/CTA tweet

Each post MUST: hook in first 100 chars, include specific numbers, include image_prompt.
For lead magnet posts: include reply CTA keyword.
For threads: open composer, type Tweet 1, find "Add another tweet" button via state, click, type next tweet.

For EACH post/thread: open https://x.com/compose/post via browser-use --session gcf-twitter --profile Amitav --headed, clear composer, type.
CRITICAL: Actually type in browser. Do NOT just present text.
Do NOT publish.

SKILL 5 — LinkedIn Cross-Post (MUST type in browser):
Take best content from today and draft LinkedIn versions.
⚠️ FULL-TIME CONSTRAINT: "I" framing, NOT "we". Senior engineer voice, NOT agency founder.
No: "we build", "GetCodeFree", "book a call", agency language.
Do: narrative paragraph, more context, less jargon, 1 hashtag max, end with question.
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
- Include lead magnet CTA if relevant
- MUST include image_prompt (2:1, 1600×800)

Topic: multi-agent systems shift, dev agency lessons, or building in public.
Open https://x.com/i/articles via browser-use --session gcf-twitter --profile Amitav, find write button, type title + body.
Leave drafted. Do NOT publish.

[OPTIONAL: Run Skill 7 — AI Coding Content]
If I say yes, run:
SKILL 7 — AI Coding Content:
Scrape AI/tech feeds (PrajwalTomar_, kaliiiiiiiiii, nickfloats, levelsio, mckaywrigley, dotey, yoheinakajima) for posts about Cursor, Claude, Perplexity, AI agents.
Draft 1-3 posts with image_prompt. Type in browser. Do NOT publish.

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

## Keyword Monitor (Standalone Run)

Run separately from main routine. 1-2x/day.

```
Run getcodefree/agents/twitter/keyword-monitor-agent.md.

Search X for: "looking for a developer", "need help building", "build my MVP", "need a tech partner", "looking for dev agency"
Search LinkedIn for: "need a developer", "looking for technical cofounder", "help with my startup"

Return prioritized list of posts to reply to. Include suggested reply for each.
Rank: high priority (explicitly hiring/needing) > medium (evaluating).
Top 5 only. Quality > quantity.
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
