---
name: ecomai-fb-lead-scraper
description: |
  Scrapes Facebook to find India businesses running commerce via FB page + WhatsApp — wholesalers, grocery stores, food brands, distributors, saree shops, fashion, retailers, restaurants — that need a complete commerce system (storefront + orders + invoices + WhatsApp + AI). QUALITY OVER QUANTITY: dedupes against EcomAI/leads/ledger.json, validates contacts (E.164/email), classifies business pages vs personal/aggregator/influencer/non-India, enforces activity + website checks, deterministic scoring (cap 10, output ≥6), capped at 2 runs/day for FB reliability. Runs inside hermes-agent. Pair with opencode/claude version: EcomAI/agents/sales/fb-lead-scraper.md.
allowed-tools:
  - Bash(browser-use *)
  - Bash(ls *)
  - Bash(cat *)
  - Bash(jq *)
  - Write
---

# EcomAI — Facebook Lead Scraper (hermes skill)

Finds India businesses on Facebook — wholesalers, grocery, food brands, distributors, saree shops, fashion, retail, restaurants — that run commerce manually (FB page + WhatsApp) and need EcomAI's complete system. Configurable per run: (category, location, slot). Dedupes against master ledger, validates contacts, outputs scored leads to `EcomAI/leads/inbox/`. FB strength: more wholesalers/grocery/food/distributors than IG.

## Prerequisite: One-time Facebook login

FB requires a logged-in session. Run once headed first:
```bash
browser-use --session ecomai-fb --profile Amitav --headed open "https://www.facebook.com/"
```
Log in manually, verify home loads, close. If FB shows login wall during a run, STOP and report.

## Context (read first)

1. `EcomAI/PROFILE.md` — product, pricing, built vs planned
2. `EcomAI/icp/icp-definitions.md` — all ICPs + signals
3. `EcomAI/leads/ledger.json` — master lead ledger
4. `HUMAN.md` (Automation root) — operator profile

## Run Instruction (configurable each run)

Parse into (category, location, slot).

| Instruction | Category(s) | ICP |
|---|---|---|
| "find wholesalers, distributors in Odisha" | wholesale, distributor + Odisha | ICP 1 / 4 |
| "find grocery stores and food brands" | grocery, food | ICP 1 / 4 |
| "find fashion stores and saree shops" | fashion, saree, retail | ICP 3 / 4 |
| "find restaurants and cloud kitchens in Bengaluru" | restaurant, cloud kitchen + Bengaluru | ICP 2 |
| "find local retailers across Delhi" | retail + Delhi | ICP 4 |

Slot (optional): morning | midday | evening, or 1–5. Location appended. No category → rotation wholesale → grocery → fashion → restaurant.

## Category → Search Map (FB)

**Rotate — never reuse the previous 2 runs' query set for the same category** (check `EcomAI/leads/inbox/`).

### Wholesalers / distributors (ICP 1/4) — FB's strength
`wholesaler`, `wholesale distributor`, `wholesale supplier`, `bulk supplier`, `dealer`, `trader`, `stockist`

### Grocery / food brands / kirana (ICP 1/4) — FB's strength
`grocery store`, `kirana`, `supermarket`, `food products`, `food manufacturer`, `organic store`, `spices`, `rice mill`, `provisions store`

### Fashion / saree / clothing / retail (ICP 3/4)
`saree shop`, `fashion store`, `boutique`, `clothing store`, `textile shop`, `garment shop`, `ladies wear`

### Restaurants / cloud kitchens (ICP 2)
`restaurant`, `cloud kitchen`, `home chef`, `catering`, `fast food`

### Jewellery / accessories (ICP 3)
`jewellery shop`, `jewellers`, `accessories shop`

### Location suffix
`wholesale distributor odisha`, `grocery store bengaluru`, `saree shop delhi`.

## Lead Quality Gates (ALL mandatory — quality over quantity)

1. **Reachable, validated contact** — phone/WhatsApp/email in page About + validated (hard gate).
2. **ICP match** — wholesale/distributor→1, food/grocery→1/4, fashion/retail→3/4, restaurant→2, offline→4.
3. **Real business** — business page (NOT personal profile), passes classifier.
4. **Active** — posts ≤30 days (≤7 preferred). Recorded on every lead.
5. **No working online store** — no functioning checkout. Outdated website = OK (rebuild).
6. **Reply-likely** — <10k page following preferred, "WhatsApp us"/"DM for price" language.

Lead missing any gate field (contact_validated, last_post, website_status, website_checked, follower_tier) = incomplete = do not output. When in doubt, leave it out.

## Contact Validation (MANDATORY)

**No usable contact, no lead.**

1. WhatsApp number in page info (best)
2. Phone in About → Contact info
3. Email in About → Contact info (last resort)

Also check page **Call-to-Action button** (WhatsApp / Call Now / Send Message / Email) — validated contacts FB shows.

| Rule | Check |
|---|---|
| India mobile | Exactly 10 digits (6–9 first digit) → `+91XXXXXXXXXX` |
| 91-prefixed | `91XXXXXXXXXX` → `+91XXXXXXXXXX` |
| Landline | `0` + 10 digits → `phone`, not whatsapp |
| Email | `name@domain.tld` regex, reject garbage |
| wa.me/wa.link | Resolve → extract → normalize. Click-to-chat usable. |
| Truncated | Partial number → exclude from contacts, `contact_validated: false`, cap 4 |
| Non-India number | Not `91`/`0` start → keep as phone, `contact_validated: false` |

Store in `contacts: {whatsapp: [], phone: [], email: []}`. `contact_validated: true` only if ≥1 passes. **No phone, no WhatsApp, no email → SKIP.** Never fabricate.

## Business-Type Classifier (MANDATORY)

| Type | Signals | Action |
|---|---|---|
| Personal profile | Not a page (no Local Business category, individual profile) | SKIP `personal-profile` |
| Aggregator/reseller | Reposts other brands, no own brand, "we supply"/"reseller available", middleman contact | SKIP `aggregator` |
| Influencer/personal | Lifestyle/meme/personal, no products/prices/orders | SKIP `influencer` |
| Non-India | Foreign currency, foreign locations, foreign ship destinations | SKIP `non-india` |
| Big brand | 100k+ AND working site/store | SKIP `big-brand` |
| Working store | Own domain, functioning checkout/Shopify/ecommerce site | SKIP `working-store` |
| Inactive | Last post >30d, no engagement | SKIP `inactive` |
| Duplicate | In ledger, last_seen ≤7d | SKIP `duplicate` |
| No usable contact | None valid | SKIP `no-contact` |
| Valid business | Real products, own brand, India, selling language, active page | PROCEED |

India evidence: ₹, Hindi/regional, Indian cities, `.in` domain, Indian mobile. Ambiguous → non-India.

## Activity + Website + Follower Check (MANDATORY — recorded on every lead)

### Activity
- Last post ≤7d = active; >30d = SKIP. 3+ posts/30d = active business.
- Engagement: 1–2 recent posts → ≥50 likes or ≥10 comments = `high`; ≥5 = `medium`; near-zero = `none`.
- "WhatsApp us"/"DM for price"/"Call us" = `reply_signal: true`.

### Website
- No website in page info → `none` (prime target).
- URL loads but old/broken/amateur/no checkout → `outdated` (rebuild, score 7–8).
- Working online store → SKIP.

Checklist when visiting: loads? / checkout? / modern or dated? / broken pages? / mobile-render? Record `website_checked: true`.

### Follower tier
- Small (<10k) = FIRST priority. Medium (10k–100k) = OK. Large (100k+) = deprioritize.

**Priority: active + small + no website + validated phone/WA → active + no website + email → active + outdated-website → rest.**

## Scoring (deterministic — cap 10)

```
score = ICP(icp1=2|icp2=1.5|icp3=1|icp4=0.5)
      + contact(whatsapp=2.5|phone=2|email=1) +0.5 if validated
      + activity(≤7d=2|≤30d=1)
      + website(none=2|outdated=1)
      + follower(small=1|medium=0.5|large=0)
      + engagement(high=0.5|medium=0.25|none=0)
      + reply_signal(+0.5)
Cap 10. contact_validated=false → cap 4.
```

- Hard gates (score 0, skip): no/validated-no contact, personal-profile, aggregator, non-India, influencer, inactive, working-store, big-brand.
- **Output threshold ≥6** (below → skipped `low-score`). Urgency: high ≥8, medium 6–7.

ICP map: wholesaler/distributor→`icp1`; grocery/kirana/food→`icp1`(or `icp4`); fashion/saree/retail→`icp3`(or `icp4`); restaurant/cloud kitchen→`icp2`; offline→`icp4`. Shopify/ecommerce-store: skip.

## Ledger — Master State (MANDATORY)

`EcomAI/leads/ledger.json` = single source of truth. Key = `lead_id = platform | handle_or_page | primary_normalized_contact`. Runs upsert.

Load (create if missing):
```bash
[ -f EcomAI/leads/ledger.json ] || echo '{"version":1,"updated_at":null,"leads":{},"skipped":{},"blacklist":[]}' > EcomAI/leads/ledger.json
```

Dedupe check per candidate:
```bash
jq -r --arg id "<lead_id>" '.leads[$id].status // "none"' EcomAI/leads/ledger.json
jq -r --arg h "<page_or_handle>" --arg p "<phone>" --arg e "<email>" '.blacklist[] | select(. == $h or . == $p or . == $e)' EcomAI/leads/ledger.json
```

Rules: last_seen ≤7d → `duplicate` (update last_seen/seen_count only). >7d → requalify. In blacklist → skip `blacklisted`. New → first_seen=now, seen_count=1, status=new.

Update skipped:
```bash
jq --slurpfile run EcomAI/leads/inbox/<run>.json '
  ($run[0].timestamp) as $ts |
  reduce $run[0].skipped[] as $s (.;
    .skipped[$s.handle] = {reason: $s.reason, first_seen: (.skipped[$s.handle].first_seen // $ts), last_seen: $ts, seen_count: ((.skipped[$s.handle].seen_count // 0)+1)})
' EcomAI/leads/ledger.json > /tmp/ledger.tmp && mv /tmp/ledger.tmp EcomAI/leads/ledger.json
```

Merge items into ledger:
```bash
jq --slurpfile run EcomAI/leads/inbox/<run>.json '
  ($run[0].timestamp) as $ts |
  reduce $run[0].items[] as $it (.;
    .leads[$it.lead_id] as $old |
    .leads[$it.lead_id] = {
      lead_id: $it.lead_id, platform: $it.platform, handle: $it.handle,
      page_name: ($it.page_name // $it.business_name), category: $it.category,
      icp: $it.icp, location: ($it.location // null), contacts: $it.contacts,
      contact_validated: $it.contact_validated, website_status: $it.website_status,
      website_checked: $it.website_checked, followers: $it.followers,
      follower_tier: $it.follower_tier, last_post: $it.last_post,
      posting_cadence: $it.posting_cadence, engagement_tier: $it.engagement_tier,
      reply_signal: $it.reply_signal, score: $it.score,
      status: ($old.status // "new"), first_seen: ($old.first_seen // $ts),
      last_seen: $ts, seen_count: (($old.seen_count // 0)+1),
      source_url: $it.source_url, offer_angle: $it.offer_angle,
      outreach_channel: $it.outreach_channel, notes: ($old.notes // null)
    })
' EcomAI/leads/ledger.json > /tmp/ledger.tmp && mv /tmp/ledger.tmp EcomAI/leads/ledger.json
```

Set `updated_at` to now after merge.

## Reliability (2 runs/day FB cap)

- **FB run cap: ≤2/day, ≥6h apart. Do not exceed** (FB is the most lockout-prone platform).
- No parallel runs on same platform. IG + FB may run concurrently.
- Rotate search pools each run. Candidate budget 10–15, hard cap 20, session <30 min.
- Login wall / "Temporarily Blocked" → STOP, save partial, mark `run_status: aborted`, report. Fresh session after ≥60 min cooldown.
- Fresh session per run + `browser-use close --all`. Page fails to load → skip + note.

## Output Schema

Write to `EcomAI/leads/inbox/fb-{timestamp}.json`:

```json
{
  "agent": "ecomai-fb-lead-scraper",
  "timestamp": "ISO-8601",
  "platform": "facebook",
  "icp_focus": ["icp1", "icp4"],
  "categories_scraped": ["wholesale"],
  "slot": "morning|midday|evening",
  "run_status": "completed|aborted",
  "run_summary": {
    "candidates_seen": 15,
    "qualified_output": 4,
    "new_leads": 2,
    "updated_leads": 2,
    "skipped_total": 11,
    "skipped_by_reason": { "duplicate": 3, "no-contact": 4, "inactive": 2, "personal-profile": 1, "non-india": 1 }
  },
  "items": [
    {
      "lead_id": "facebook|pagename|+919876543210",
      "timestamp": "ISO-8601",
      "platform": "facebook",
      "source_url": "https://facebook.com/pagename",
      "handle": "pagename",
      "page_name": "Business Name",
      "category": "wholesale|grocery|fashion|restaurant|jewellery|retail",
      "icp": "icp1|icp2|icp3|icp4",
      "location": "if-any",
      "contacts": { "whatsapp": ["+919876543210"], "phone": [], "email": [] },
      "contact_validated": true,
      "website_status": "none|outdated|working-store",
      "website_checked": true,
      "followers": 1234,
      "follower_tier": "small|medium|large",
      "last_post": "days-ago-or-ISO",
      "posting_cadence": "3+/month|slow|none",
      "engagement_tier": "high|medium|none",
      "reply_signal": true,
      "score": 8,
      "urgency": "high|medium",
      "offer_angle": "storefront + WhatsApp order flow + invoices + AI",
      "outreach_channel": "whatsapp|phone|email"
    }
  ],
  "skipped": [
    { "handle": "pagename", "reason": "no-contact|inactive|personal-profile|aggregator|non-india|influencer|working-store|big-brand|duplicate|blacklisted|low-score" }
  ]
}
```

## Workflow

1. Parse instruction → category + location + slot. Pick rotated queries (avoid previous 2 runs' sets).
2. Load ledger. Verify no concurrent same-platform run + FB run-cap (≤2/day).
3. `browser-use --session ecomai-fb --profile Amitav open <search-url or FB home>`
4. `browser-use --session ecomai-fb state`
5. Collect 10–15 candidate pages (cap 20). Dedupe-check each page before opening.
6. Open pages: About (contact, website, category) + followers + last post + CTA button.
7. Classify → skip non-leads with reason.
8. Contact validation → normalize; skip unreachable (`no-contact`).
9. Activity + website checks → record all fields.
10. Score (formula). Output ≥6. Sort desc.
11. Write run file with `run_summary`.
12. Merge into ledger (items + skipped). `updated_at`.
13. Report top 10 (page + category + contact + score) = today's outreach priority.
14. `browser-use close --all`.

## Rules

- Never auto-DM/auto-send/auto-publish. Leads only.
- Contact gate: validated phone/WhatsApp/email required. No usable contact = skip. Never fabricate.
- Activity gate: posts ≤30d only. Inactive = skip. Prioritize ≤7d.
- Completeness gate: every lead records contact_validated, last_post, posting_cadence, engagement_tier, website_status, website_checked, follower_tier. Missing any = do not output.
- No-website priority: active + no-website + validated phone/WA + small-following FIRST. Outdated = rebuild.
- Facts only from visible page content. No guessing.
- Login wall / block: stop, report, don't hammer.
- **FB run cap ≤2/day.** `--profile Amitav`. Close all sessions. Normal English output.

## Tunables (defaults in bold)

Output threshold **≥6** · Top batch **10** · Dedupe window **7d** · Candidate cap **10–15/20** · FB run cap **2/day** · Engagement: high ≥50 likes/≥10 comments, medium ≥5, else none