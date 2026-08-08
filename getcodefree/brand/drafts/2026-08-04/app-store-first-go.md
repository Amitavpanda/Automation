# GetCodeFree Drafts — 2026-08-04

Mode: Manual. Source: user seed + research (app-store cluster, kaif9998 vibe-coding post).

## Piece 1 — ARTICLE: App Store first-go submission

**Title:** First-Go App Store Submission: Zero Rejections, One Process

Most App Store submissions get rejected. It is not close. Reviewers bounce apps for missing EULA links, unrecorded flows, outdated SDKs, and guidelines that changed while you were building.

A client came to us with an app headed for the App Store. It went through on the first submission. Zero rejections. No resubmission cycle. No waiting weeks for a second chance.

The whole process was executed by my web browser automation agent. After every phase it handed me the result and I verified and approved it before it moved on. The agent did the work; the senior judgment stayed with me.

First-go approval used to be a nice-to-have. In 2026 it is becoming a requirement, because the cost of rejection is climbing.

### Why this matters

The math on rejection is brutal. One missing EULA link cost a developer 16 days of waiting. Another spent three attempts over a deletion-flow recording. That is not a typo tax. That is a product launch slipping weeks, plus client burn while the clock runs.

Account-level risk is rising too. Since June 9, 2026, guideline 4.3(b) lets Apple reject and remove apps that are indistinguishable from existing ones. Saturation is now an enforcement lever, not a soft warning. Repeat rejections stack up against the account, not just the build.

The checklist changed under you. Xcode 26 and the iOS 26 SDK are mandatory for uploads since April 28, 2026. The age rating questionnaire now includes social media questions, required from September 2026. UGC and anonymous chat rules tightened under 1.2 back in February. Submitting against last year's checklist is how you get rejected this year.

### What we did

The result did not come from luck. It came from treating submission as part of the build, not an event after it. Here is the process. It is repeatable. Steps that depend on the specific app are marked CONFIRM so you can plug in your own specifics.

**Phase 1: Pre-submission audit**

Map the app against the current guidelines, not the ones you remember. Print the latest App Store Review Guidelines and walk every feature against them. CONFIRM: which guideline sections we flagged as highest risk for this app.

Audit the store listing: name, subtitle, keywords, description, screenshots. Reviewers read the store page before they open the binary. A listing that overpromises gets flagged before the code is touched. CONFIRM: what we changed in the listing before submission.

Audit permissions. Every permission prompt must map to a feature that visibly uses it. Unexplained permissions are one of the easiest rejections in the book. CONFIRM: permission prompts we added or removed.

**Phase 2: Compliance checklist**

Privacy policy reachable from inside the app and from the store page. EULA links where the app sells or subscribes. The single missing link that cost 16 days lives here.

Age rating questionnaire filled against actual app behavior, including the new social media questions if they apply. UGC and anonymous chat: report and block flows, content moderation, and a deletion flow. Recording the deletion flow on video is the proof reviewers ask for. Listed APIs and required reason APIs with approved reasons; Xcode surfaces these, read the warnings.

CONFIRM: the exact compliance items we verified or fixed for this client.

**Phase 3: AI-assisted review pass**

This is where AI earns its keep. We handed the latest guidelines plus the app's feature list to an LLM and asked it to find mismatches, the same pattern as the applecompliance.md files people share. It caught edge cases we had glossed over. CONFIRM: what the AI pass flagged that we had missed.

One rule: AI is the second reader, not the authority. Every finding gets verified against the actual guideline text and the app. Senior judgment is the difference between a useful flag and a confident hallucination.

**Phase 4: The submission itself**

Build with current tooling. Xcode 26 and the iOS 26 SDK, because anything older is rejected before a human sees it.

Test accounts and test data in the review notes, plus credentials that actually work. Review notes that pre-empt questions: explain unusual flows, state what you want reviewed, link the privacy policy. Reviewers approve faster when nothing surprises them. CONFIRM: what our review notes covered and how we set up test accounts.

**Phase 5: The human review**

After the machine gates, a person decides. Their job is to find a reason to say no. You win by giving them nothing to find: clear flows, recorded deletion, honest permissions, a store page that matches the app. First-go approval is what happens when the reviewer's questions are already answered.

### On the AI angle

We build with AI, and we say so. LLMs drafted parts of the review checklist and read guidelines against the feature list. What AI did not do: decide, verify, or take responsibility. The moat is knowing which AI output to trust and which to check, and that is senior judgment. Vibe-coded submissions get approved too, but approval is not the goal. Approval on the first try, with zero surprises, is.

### What first-go approval saved

The savings are concrete. No 16-day resubmission cycle. No third attempt over a recording. No developer hours re-reading rejection letters. Calendar time and client budget, spent on shipping instead of waiting. CONFIRM: the actual days saved for this client.

If you are shipping an app, do not submit against last year's rules. Audit, verify, record, pre-empt. If you want the checklist we run, comment CHECKLIST and I will DM it to you.

**Hooks:**
1. Most App Store submissions get rejected. Ours went through on the first submission.
2. One missing EULA link cost a developer 16 days. Here is the process that avoided all of that.
3. First-go App Store approval is rare and getting rarer. This is what made it happen.

**Image prompt hint:** clean editorial header: checklist document with 'FIRST GO' stamp on top of an App Store submission screen, teal #19d3c5 + blue #6f8cff accents, light background, dark slate #0f172a headline 'FIRST SUBMISSION. ZERO REJECTIONS.', no fake metrics or dollar amounts on the image.

**Lead magnet keyword:** CHECKLIST

### Article visual plan (one image per phase — engageable layout)

Cover + one visual per article section/phase. All: LIGHT theme, cartoonish flat, white bg, teal #19d3c5 + blue #6f8cff accents, dark slate #0f172a text. NO fake metrics, NO dollar amounts on any image. Real logos where tools are mentioned (Xcode/Apple, AI assistant chip). Inline size 1200×628, cover 1600×640.

- **COVER (1600×640):** split scene — left: app icon box labeled 'FIRST GO' stamp; right: submission status card 'APPROVED'. Headline: 'FIRST SUBMISSION. ZERO REJECTIONS.'
- **WHY THIS MATTERS (1200×628):** before/after split — left: dev at desk with calendar sliding backward, a document with a missing-link symbol, red X marks; right: calendar moving forward fast, green checkmarks. Headline: 'REJECTION COSTS WEEKS'. Small clock motif.
- **PHASE 1 — PRE-SUBMISSION AUDIT (1200×628):** cartoon dev with giant magnifying glass over a checklist + app icon; app store listing panel behind; permission prompts floating. Headline: 'AUDIT BEFORE YOU SUBMIT'.
- **PHASE 2 — COMPLIANCE CHECKLIST (1200×628):** big checklist card with checkboxes: privacy policy link, EULA, age rating, deletion flow, listed APIs. Green checks. Headline: 'NO SURPRISES, NO MISSING LINKS'.
- **PHASE 3 — AI-ASSISTED REVIEW (1200×628):** AI assistant chip + document reader scanning guidelines against app feature list; a human hand holding a 'VERIFY' stamp over one flag; robot + human side by side. Headline: 'AI FLAGS. HUMANS VERIFY.'
- **PHASE 4 — THE SUBMISSION (1200×628):** Xcode/Apple logo on build screen, test-account card, review notes sheet being handed to reviewer. Headline: 'PRE-EMPT THE QUESTIONS'.
- **PHASE 5 — THE HUMAN REVIEW (1200×628):** reviewer at desk, nothing on the app to flag — clean flows, honest permissions, matching store page; green 'APPROVED' stamp slam. Headline: 'GIVE THEM NOTHING TO FIND'.
- **AI ANGLE (1200×628):** robot + senior dev, robot hands a list to human, human reviews/decides — moat visual. Headline: 'SENIOR JUDGMENT IS THE MOAT'.
- **WHAT SAVED (1200×628):** calendar with skipped red-flag weeks, shipping rocket, dev smiling. Headline: 'WEEKS BACK. SHIPPING, NOT WAITING.'

**CONFIRM items before publishing:**
1. Client app name/vertical — do not publish without consent. Candidate proof asset: NativeNest (App Store live) — verify match.
2. Highest-risk guideline sections flagged
3. Store listing changes
4. Permission changes
5. Compliance items fixed (missing link, recorded flow, privacy policy)
6. What the AI review pass flagged
7. Review notes content + test account setup
8. Actual days saved / review turnaround

---

## Piece 2 — X POST: Vibe coding debate (kaif9998 echo)

Vibe coded became an insult. Dumb gatekeeping.

We ship client products this way. AI writes maybe 70%. The other 30% is knowing which 70% to trust. You can't prompt your way into that.

That's senior judgment. LLMs reward expertise.

Agree or disagree?

**Hooks:**
1. Vibe coded became an insult. Dumb gatekeeping.
2. AI writes 70% of our client code. The 30% that matters is deciding which 70% to trust.
3. Everyone laughs at vibe-coded apps. We ship them to paying clients.

**Image prompt hint:** split scene: senior engineer reviewing a large AI-generated code diff on screen, red 'VERIFY' tag on one block and green 'TRUST' tag on another, headline text 'KNOW WHICH 70% TO TRUST', teal #19d3c5 + blue #6f8cff accents, light background, dark slate #0f172a text, no logos.

---

## Piece 3 — X POST: Article promo (money framing)

Shipped a client's App Store app. First submission. Zero rejections.

The whole process ran on my web browser automation agent. After each phase, I verified and approved before it moved on.

Cost of the usual path: 16 days for one missing link. Three attempts for an unrecorded flow.

The math: fewer rejection cycles = shorter wait = lower burn.

Full breakdown → [article link]

**Hooks:**
1. First submission. Zero rejections. Here's the process.
2. App Store approval on the first try. Most apps never see it.
3. One missing link cost a dev 16 days. Our client's app passed on the first submission.

**Image prompt hint:** app store approval visual: green checkmark over submission status card reading 'APPROVED' with 'FIRST GO' ribbon, checklist motif behind it, teal #19d3c5 + blue #6f8cff accents, light background, dark slate #0f172a text, no download or revenue numbers.

**Lead magnet keyword:** CHECKLIST

---

## Piece 4 — X POST: Founder maintenance hell (replacement item, from @nico_jeannen signal)

90% of your time goes to bugs and tiny features. Marketing? Barely any.

You don't need a team. You need one senior who ships with AI.

One senior + AI clears the maintenance treadmill in hours. Back to growing.

Comment if this hits home.

**Hooks:**
1. 90% of your time goes to bugs and tiny features. Marketing? Barely any.
2. The founder tax: 90% maintenance, 0% growth. It does not have to be that way.
3. You do not need an org chart. You need one senior who ships with AI.

**Image prompt hint:** cartoonish flat scene, white background: stressed founder buried under a tall stack of bug-ticket papers and tiny feature icons on one side, confident senior engineer with laptop plus a friendly AI robot sweeping the pile away on the other side, headline text 'ONE SENIOR + AI', teal #19d3c5 + blue #6f8cff accents, dark slate #0f172a text, clean minimal, no logos, no dollar amounts, no price graphics.

**LinkedIn caption variant:** Founder maintenance hell is never fixed by headcount, it is fixed by one senior engineer who can look at AI output and know what is safe to ship, which is exactly the work I do every day. #AI

**Publish note:** Replacement for dropped kaif9998 vibe-coding item. Universal framing only: no @nico_jeannen mention, no direct quote, no invented metrics. Standalone post only; reply/DM to the original founder handled separately by engagement system. ~221 chars, 1 soft CTA.

---

## Alternates (not drafted, for next runs)

- @saen_dev (TODAY): cheap-model retry-cost lesson — thread "the cheapest model is the one that gets it right the first time"
- @OpenAI (YESTERDAY, 1.4M views): 10 open math problems solved for ~$2k tokens — cost-economics standard post
- @marclou (YESTERDAY, 30.6k views): $25K MRR, 7.12% churn, AI-proof pivot — metrics thread
- @mckaywrigley (TODAY): model routers / "era of model melding" — standard post
- @cursor_ai (YESTERDAY): Cursor agents across Google Workspace — automation standard post

---

## Pieces 5+6 — X POSTS: Cursor trending (https://x.com/i/trending/2084706171718697034)

Trend: "Cursor AI Editor Expands Beyond Coding to Everyday Work" (trending now, 99 posts). Anchor: @davep (Field CTO, Cursor) 4h ago, 39K views, 772 likes — "most of our use cases aren't coding at all: research, data analysis, bug triage, project management... coding agents are a pretty good foundation for all". Grok context: Google Workspace plugins early Aug 2026; PM ran all PM work in Cursor 6 months; $60/mo. Thread: @rawkode "Does anyone even still use Claude Code?", @kimmonismus "Codex is like macOS vs Windows", @utpalnadiger "coding agent harnesses as the brains".

### Piece 5 — X post: coding agent = general-purpose agent

Cursor's Field CTO just admitted the quiet part: most of their internal use of Cursor is not coding. Research. Bug triage. Project management.

The harness that made coding agents work, terminal, files, tools, a verification loop, is becoming the operating system for knowledge work.

Now Cursor can read and write your Gmail, Drive, and Docs. A product manager has run all PM work in Cursor for six months.

Coding was the training ground. Everything else is the real economy.

This is why AI-native agencies operate like software teams, not prompt shops. The harness plus senior judgment is what ships. That is how we run our own daily agents.

What is your agent handling this week?

**Hooks:**
1. Cursor's Field CTO says most of their internal use of Cursor is not coding. Research, bug triage, project management. The coding harness became the operating system for knowledge work.
2. The coding agent is becoming a general purpose agent. Cursor just plugged into Gmail and Google Drive. The terminal was the training ground. The office is the real economy.
3. A PM has run six months of project management inside Cursor. The agent harness stopped being a coding tool. It is becoming the operating system for knowledge work.

**Image prompt hint:** LIGHT theme. Cartoonish flat scene: one agent harness powering both a terminal window on the left and an office desk on the right (open email, calendar, docs, spreadsheet). Headline text 'FROM CODE TO EVERYDAY WORK'. White background, teal #19d3c5 + blue #6f8cff accents, dark slate #0f172a text. No real product logos. Clean, minimal, readable at thumbnail size.

**LinkedIn caption:** Cursor's field CTO admitted the obvious: most of their internal Cursor use is not coding. Research, bug triage, project management. The Google Workspace plugins let the agent read and write Gmail, Drive, and Docs. I run my marketing agents and my coding on the same harness. The terminal, the files, the verification loop. That loop is what makes an agent trustworthy, and it applies far beyond code. Coding was the training ground. The agent economy is everything else. I am more interested in who reviews the agent's output than which model wins the benchmark. #aiagents

**Publish note:** Post same day the trend is hot. Reply to @davep's thread after posting. One CTA only: the closing question. No invented metrics, no client counts. Quote the Field CTO title + the six-month PM fact accurately.

### Piece 6 — X post: tool-war pushback

Everyone is fighting the Cursor vs Claude Code vs Codex war.

A CoreWeave CTO asks who still uses Claude Code. Someone else says Codex is macOS vs Windows. It is a fun argument and it is the wrong one.

Any of these agents will ship if the loop around them is right. The real question is which harness fits your workflow, and who knows when the agent is wrong.

That judgment is the moat. Not the model.

One senior engineer with any agent beats a prompt crowd with the best agent. We see this on real client work.

The tool picks itself. The operator decides the outcome.

**Hooks:**
1. Everyone is arguing Cursor vs Claude Code vs Codex. Wrong fight. The moat is the operator who knows when the agent is wrong, not the model you picked.
2. One senior engineer with any agent beats a prompt crowd with the best agent. The tool war is a distraction from the only skill that matters: review.
3. CoreWeave's CTO asks who still uses Claude Code. Someone compares Codex to macOS vs Windows. Nobody is asking the question that matters: who catches the agent's mistakes?

**Image prompt hint:** LIGHT theme. Cartoonish flat scene: three robot mascots arguing over a trophy labeled 'BEST TOOL' while one senior dev calmly reviews output at a desk in the foreground. Headline text 'THE TOOL WAR IS THE WRONG FIGHT'. White background, teal #19d3c5 + blue #6f8cff accents, dark slate #0f172a text. No real product logos. Simple shapes, readable at thumbnail size.

**LinkedIn caption:** The tool war is the wrong fight. Cursor, Claude Code, Codex. Everyone is picking a camp and the camps get louder every week. What I have learned running agents daily: the harness matters, but the moat is knowing when the agent is wrong. One engineer who reads the output beats a team that pastes prompts into the best model. I have wasted more time trusting output than trusting tools. Pick any good agent. Then invest in the review loop. #ai

**Publish note:** Post 2-4 hours after post 1 to catch the same trend wave. Designed for replies: it contradicts the hot takes in the thread. Quote @rawkode and @kimmonismus posts accurately if replying. No CTA, the closer is the bookmark line. Keep 'real client work' qualitative, no counts.

---

## Piece 7 — X POST: Cursor Google Workspace release, personal usage (user request)

Cursor just plugged into Google Workspace. Agents can read and write Gmail, Drive, Calendar, Docs, Sheets.

Here is what I am going to run on it:

My daily brand agents already draft posts. Now they get to act on the results: log the week's analytics to Drive, draft replies from my inbox, queue the calendar, and keep the run book updated so nothing waits on me.

The agent goes from "writes the thing" to "runs the thing". That is the upgrade that matters.

First test this week: full daily run, zero copy-paste between apps.

What will you run on it first?

**Hooks:**
1. Cursor just plugged into Google Workspace. My agents go from writing the thing to running the thing.
2. Agents that draft are common. Agents that act on Gmail, Drive, and Calendar are new. Here is what I am testing this week.
3. Cursor now reads and writes your inbox, docs, and calendar. This is exactly what my daily brand agents were missing.

**Image prompt hint:** LIGHT theme, cartoonish flat scene: one robot agent in the center plugged into four app icons (mail, calendar, docs, drive) with arrows flowing, on one side a stack of drafted post cards going in, on the other side a completed weekly calendar going out. Headline text 'FROM DRAFTS TO DONE'. White background, teal #19d3c5 + blue #6f8cff accents, dark slate #0f172a text. No real product logos. Readable at thumbnail size.

**LinkedIn caption variant:** Cursor's new Google Workspace plugins mean my agents can read and write Gmail, Drive, Calendar, Docs, and Sheets. What that changes for me: my daily brand agents have always drafted the content. Now they can act on the output, log analytics to Drive, draft replies from my inbox, and keep the run book updated. The agent stops at the draft and starts running the operation. I am testing a full zero-copy-paste daily run this week. The interesting question is where the verification loop still needs a human. #aiagents
