# ProofShot Post Set — 2026-08-08 — EDUCATIONAL VERSION (what it is → how we use it)

Grounding: EcomAI `nextjs-app/proofshot-artifacts/` — 7 real verification runs on 2026-08-08. Real flows: login, dashboard, aging (AR 90+, suppliers AP), retailer search "Naidu" + ledger, back-dated invoice (2026-04-30, ~100 days), order fill, credit overdue, GST reports, GSTR-1 CSV export, HSN summary, analysis reports, intra/inter-state invoices. Real artifact bundle: session.webm, viewer.html, SUMMARY.md, step screenshots, console-output.log, session-log.json, metadata.json (branch main, commit sha 86c59783).

Tool facts (from repo README, verified): open-source, MIT, agent-agnostic CLI. Works with Claude Code, Cursor, Codex, OpenCode, Gemini CLI, Windsurf, GitHub Copilot. Sits on top of vercel-labs/agent-browser. Commands: `proofshot start`, agent drives browser, `proofshot stop`, `proofshot pr`, `proofshot diff`. 846 stars. Repo: https://github.com/AmElmo/proofshot

---

## 1. X post — LARGE slot (280 chars, no URL — URL goes in first reply comment)

```
ProofShot is an open-source CLI that gives AI agents eyes: records the browser while your agent works, grabs screenshots + errors, bundles it for review.

We use it in EcomAI: agent runs a flow, ProofShot records, we watch before approving.

Agent builds. ProofShot proves. We verify.
```

**First reply (adds the link + one concrete use):**
```
github.com/AmElmo/proofshot

Example from this morning in EcomAI: our agent created a back-dated invoice (100 days old), ran aging, searched a retailer, filled an order. ProofShot recorded all of it, 12 screenshots, console log included.
```

## 2. Thread option — educational, more room

```
Tweet 1:
ProofShot is an open-source CLI that gives AI coding agents eyes.

Your agent builds a feature. ProofShot records it working in a real browser, captures screenshots and console errors, and bundles everything into files a human can review.

Works with Claude Code, Cursor, Codex, OpenCode, any agent that runs shell commands.

Tweet 2:
How it works:
- proofshot start: browser opens, recording starts, server logs captured
- your agent drives the browser
- proofshot stop: video + screenshots + console log + server log + action timeline, all synced
- proofshot pr: uploads the whole bundle to the PR as a comment

Tweet 3:
How we use it in EcomAI:
Our agent runs a flow, ProofShot records it, we watch the recording before we approve anything. Seven verification sessions today alone: login, aging reports, retailer search, back-dated invoice entry, order fill, credit overdue, GST reports.

Tweet 4:
Why it matters: an agent can tell you it worked. ProofShot shows you. The video and the console log are the difference between "trust me" and "watch it."

We don't approve agent work from summaries anymore. We approve it from proof.

Tweet 5:
Open source, agent-agnostic, sits on vercel/agent-browser. No vendor lock-in.

Agent builds. ProofShot proves. We verify. github.com/AmElmo/proofshot
```

## 3. LinkedIn variant — educational, senior "I", 1 hashtag, no agency sell
Gate: plan says no LI post Day 2 (every-other-day). Recommended Sunday 2026-08-09 18:30 IST unless user overrides.

```
ProofShot is an open-source CLI that gives AI coding agents eyes.

What it does: your agent builds a feature, and ProofShot records it working in a real browser — video, screenshots of key steps, console errors, server logs, all synced to an action timeline. It runs on top of agent-browser and works with any agent that can run a shell command: Claude Code, Cursor, Codex, OpenCode, and the rest.

How we use it in EcomAI: our agent runs a flow and ProofShot records it. We watch the recording before we approve anything. Seven verification sessions this morning — login, aging reports, retailer search, back-dated invoice entry, order fill, credit overdue, GST reports. Each one produced a video, screenshots, and logs we could review in minutes instead of re-testing manually. The bundle can even be posted to the PR as a comment, so reviewers see the proof, not a summary.

The principle behind it is simple and it is the same one we use everywhere: agents execute, humans verify. The tool gives the agent eyes; the senior engineer still gives the judgment.

Open source, MIT, agent-agnostic. github.com/AmElmo/proofshot

What does your agent show you before you approve its work?

#AI
```

## 4. Image prompt (LIGHT theme, cartoonish)

```
Image prompt for Gemini:
Style: Bright flat digital illustration, cartoonish, playful, clean minimal, LIGHT theme (NOT dark).
Colors: White background (#ffffff), teal (#19d3c5) accents, blue (#6f8cff) highlights, dark slate text (#0f172a). No fake numbers, no dollar amounts, no metric claims.
Mood: Energetic, trustworthy, tech-forward, friendly.
Composition: Center: a cartoonish developer character (generic, no photo available) holding a clipboard, watching a big browser window with a red REC dot, a play button over a video frame, and a stack of artifact files (folder, screenshots, checklist with checkmarks, timeline). Small terminal shows "$ proofshot stop".
Subject: Cartoon style. No photorealism.
Typography: Bold rounded sans-serif headline "AGENT BUILDS. PROOFSHOT PROVES." in teal/blue gradient, "WE VERIFY." in dark slate.
Details: Soft pastel teal glow, subtle floating shapes, white cards with soft shadow.
Text to include: "AGENT BUILDS. PROOFSHOT PROVES. WE VERIFY."
Size: 1080x1080px square.
```

## 5. Reply / quote-tweet angle — Anthropic Claude Code cross-session news

Context (verified): Claude Code v2.1.224 (Aug 7) adds cross-session messaging on macOS/Linux. Sessions discover peers via `ListAgents`, send text via `SendMessage`. Text only, no history/files/permissions transfer. Official post: https://x.com/ClaudeDevs/status/2085817074816070014 / docs: https://code.claude.com/docs/en/cross-session-messaging

Draft reply (engagement, NOT a post):
```
Sessions can talk to each other now. Fine.
What did they actually do while talking? That's the part nobody's asking.

Every workflow we ship ends in a proof bundle, not a summary. Video, screenshots, console logs, PR comment. The human reviews the artifact.

Coordination without verification is just optimistic concurrency.
```

Reply target: the ClaudeDevs post, or Anthropic's own announcement handle. Send within 48h window (post is Aug 7, in window until Aug 9).

## Facts discipline
- No invented metrics, error counts, or time savings. Only: 7 sessions today, flows listed, artifact bundle contents, repo facts from README.
- Token/cost estimates in SUMMARY.md left OUT of posts — estimated by tool, not a claim worth making.
- The React key warning detail is real but deliberately left out of the educational version (user preference: explain what it is + how we use it, not bug-stories).
