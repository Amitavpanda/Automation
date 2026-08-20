# Hermes + Qwen + Telegram — CEO-Console Marketing Automation (Research & Plan)

> Status: **RESEARCH COMPLETE — NOT DEPLOYED**. Plan approved for later build.
> Created: 2026-08-15. Source: research session (opencode, websearch, live runtime checks).
> Goal: automate sales/marketing + content creation from phone, like a CEO instructing employees. Free as possible.

## The Idea

Run the Hermes agent (Nous Research) as an always-on marketing automation brain, connected to Telegram/Discord so Amitav can command it from his phone. Brain = Qwen open-source models. Deploy free (Oracle Cloud or local Mac). Agents (gcf-lead-scraper, content drafter, outreach, pipeline) run as hermes skills/cron.

```
[PHONE]  Telegram/Discord app
   │
   ├──► hermes gateway  (Telegram bot + Discord bot, native, free)
   │         │
   │         ├── hermes agent (brain) → gcf skills, cron, memory
   │         └── model backend:
   │               ├── OpenRouter qwen/qwen3-coder:free   ($0, 50-1000 req/day)
   │               └── Ollama qwen3-coder:14b local        ($0, ~9GB, best that fits 18GB Mac)
   │
   └──► agents: browser-use scraping, gcf-lead-scraper, gcf-content-drafter, gcf-pipeline-view
```

## What's Already Installed & Working

| Component | Status | Notes |
|---|---|---|
| Hermes (Nous Research agent) | ✅ installed, `~/.hermes` | agent-first, persistent memory, learning loop, skills, cron. Currently `deepseek/deepseek-chat` via OpenRouter (key set) |
| Hermes messaging gateway | ✅ native | `hermes gateway setup` — Telegram, Discord, WhatsApp, Slack, Signal, Teams. **Telegram = 2-min setup, no approval. Discord = needs bot app creation** |
| opencode | ✅ installed | headless server mode (`opencode serve` port 4096) + `opencode web` UI. Ready-made Telegram bridges: `grinev/opencode-telegram-bot`, `doughknee/opencode-telegram` |
| Ollama | ✅ running (0.32.9) | local models: `qwen3-coder:30b` (18GB, pulled), `gemma4:e4b` (9.6GB) |
| GCF automation stack | ✅ wired into hermes skills | gcf-lead-scraper, gcf-content-drafter, gcf-outreach, gcf-pipeline-view |
| browser-use | ✅ working | CLI scraping, `--profile Amitav` Chrome profile for X/LinkedIn/IG logins |

## Qwen Model Reality Check (2026-08-15)

**qwen.ai/home model = Qwen3.8-Max — CANNOT self-host on free tier.** 2.4T-parameter MoE (~95B active), needs ~2,400GB FP8 weights, minimum 24x H200 GPUs or multi-node B300. Proprietary/API-only anyway.

| Model | Params | Weights | Fits Oracle free (2/12)? | License |
|---|---|---|---|---|
| Qwen3.8-Max (qwen.ai/home) | 2.4T MoE | ~2,400GB FP8 | ❌ GPU cluster | Proprietary (API) |
| Qwen3.8-2.4T-A95B (base, Aug 12) | 2.4T | still 2.4T | ❌ same | Custom |
| Qwen3.8-27B (dense, Aug 15) | 27B | Q4_K_M 17.1GB | ⚠️ 9GB quant fits RAM but CPU-only ~2-4 tok/s | Apache-2.0 |
| Qwen3.5-9B / Qwen3-8B | 8-9B | Q4 ~5.5GB | ✅ fits, ~5-10 tok/s, weak for agents | Apache-2.0 |

**Free Qwen OAuth is DEAD**: free hosted OAuth quota cut 1000→100/day on 2026-04-13, discontinued entirely 2026-04-15. Surviving free paths:
1. **OpenRouter `qwen/qwen3-coder:free`** — $0, 480B-A35B MoE, 1M context. ~50 req/day default, **1000/day after one-time $10 credit** (never expires). Best value.
2. **Local Ollama** — $0, unlimited, needs RAM.
3. Alibaba Model Studio API (region-specific keys) / $50/mo Coding Plan.

## Oracle Free Tier Reality (2026)

**Halved 2026-06-15**: Ampere A1 = **2 OCPU / 12GB** (was 4/24). 200GB storage unchanged. Consequences:
- 12GB RAM → only small models fit (~qwen3:8b, not 30B).
- **Idle reclamation**: Oracle kills instances idle 7 days (<20% CPU/net/mem).
- "Out of capacity" lottery on launch (scripts exist, finicky).
- 10TB egress/mo, free forever, $0 bill.

## LIVE TEST RESULT — 30B on M3 Pro HANGS

Proven 2026-08-15 on Mac (Apple M3 Pro, 18GB RAM):

```
ollama list          → qwen3-coder:30b 18GB present
curl generate 30 tok → timed out at 120s, ZERO output
vm.swapusage         → total 24GB, USED 20.3GB
```

**Root cause**: 18GB model working set on 18GB RAM = 0 headroom → infinite swap thrash → system hang. Swap exhausted (20.3/24GB). **30B is a non-starter on this Mac.** Recovery: `ollama stop qwen3-coder:30b` (worked, CPU back to 0%).

## What Fits Locally (M3 Pro 18GB)

| Model | Q4 size | Free RAM after load | Verdict |
|---|---|---|---|
| qwen3-coder:30b | 18GB | ~0 | ❌ hang (proven) |
| **qwen3-coder:14b** | ~9GB | ~9GB | ✅ best local pick, decent coding |
| qwen3:8b | ~5GB | ~13GB | ✅ comfortable, weaker |
| qwen3.5:9b | ~5.5GB | ~12GB | ✅ comfortable |

## Recommended Architecture (approve → build later)

**Path 1 — RECOMMENDED: Oracle VM + cloud Qwen (flagship quality, $0)**
- Oracle free VM (2/12): run hermes + Telegram gateway (hermes is lightweight, 12GB plenty).
- Model = OpenRouter `qwen/qwen3-coder:free` (480B, Opus-4.5-class). 50 req/day default; 1000/day after one-time $10 credit.
- Flagship Qwen quality without hardware. Phone control via hermes+Telegram.
- Caveat: browser-use scraping needs the local Amitav Chrome profile — scraping stays on Mac, or re-login on VM. Flagged, not blocking.

**Path 3 — Local Mac (strongest self-hosted, but Mac must stay on)**
- M3 Pro + Ollama `qwen3-coder:14b` (NOT 30b — hangs).
- Hermes → `http://localhost:11434`.
- 14B < 30B quality, no hang, no API.

**Path 2 — Oracle VM + small local Qwen (fully local, weaker)** — fallback if API refused entirely.

## Build Order (when approved)

1. `hermes gateway setup` → add Telegram bot (2 min) → test reply-from-phone.
2. Point hermes model to `qwen/qwen3-coder:free` via OpenRouter, fallback chain → deepseek-chat → Ollama local.
3. `hermes gateway install` → 24/7 launchd service on Mac (Path 3) OR deploy to Oracle VM (Path 1).
4. Wire gcf cron jobs → deliver summaries to Telegram (CEO briefing).
5. Discord bot (second channel).
6. Optional: Oracle VM move (needs $0 hosting win + re-login scraping).

## Cost Math

| Layer | Cost |
|---|---|
| Hermes + gateway | $0 |
| Telegram/Discord bots | $0 |
| Oracle free tier | $0 (2/12, capacity lottery) |
| Qwen via OpenRouter free | $0 (or one-time $10 → 1000 req/day forever) |
| Qwen local (Ollama 14b, your Mac) | $0 |
| **Total** | **$0/month**, $10 optional unlock |

## Decision Points Locked

- ✅ Research complete, plan approved to note. NOT building now.
- ✅ Qwen3.8-Max (qwen.ai/home) ruled out for self-host (2.4T).
- ✅ qwen3-coder:30b on M3 Pro ruled out (hang proven, swap thrash).
- ✅ Telegram-first (fastest, no approval), Discord second.
- ✅ OpenRouter qwen3-coder:free = primary free model; deepseek-chat fallback; Ollama 14b local fallback.
- ⏳ Brain host: Mac (Path 3) vs Oracle (Path 1) — decide at build time. Oracle preferred for 24/7 Mac-free.

## Sources

- opencode server docs: https://opencode.ai/docs/server/ (serve mode, basic auth, port 4096)
- opencode Telegram bots: github.com/doughknee/opencode-telegram, github.com/grinev/opencode-telegram-bot
- OpenClaw (alternative platform, self-hosted, MIT, 20+ channels): github.com/openclaw/openclaw
- Qwen free tier shutdown: QwenLM/qwen-code issues #3203, #3267 (2026-04-13/15)
- OpenRouter free Qwen3-Coder: `qwen/qwen3-coder:free` 480B-A35B, 50 req/day, 1000/day after $10 credit
- Oracle free tier halving: Oracle Always Free docs (2026-06-12/15), InfoQ 2026-07
- Qwen3.8-27B specs (Apache-2.0, Aug 15 2026): Q4_K_M 17.1GB, IQ4_XS 15.7GB, UD-Q3_K_XL 13.4GB
- Qwen3.8-Max specs: 2.4T MoE, 95B active, 1M ctx, needs 24x H200 / 2x B300 nodes
- Hermes agent (Nous Research): agent-first, persistent memory, learning loop, gateway, cron