---
name: ecomai-ig-lead-scraper
description: |
  Scrapes Instagram to find India businesses operating via Instagram or WhatsApp stores — fashion brands, ecommerce stores, jewellery, clothing (kapda), boutique, handmade — that need a complete commerce system (storefront + orders + invoices + WhatsApp + AI). QUALITY OVER QUANTITY: dedupes against EcomAI/leads/ledger.json, validates contacts (E.164/email/wa.me), enforces activity + website checks, classifies real businesses vs aggregators/influencers/non-India, deterministic scoring (cap 10, output ≥6), 4-5 runs/day via rotation + rate-limit abort. Runs inside hermes-agent. Pair with the opencode/claude version: EcomAI/agents/sales/ig-lead-scraper.md.
allowed-tools:
  - Bash(browser-use *)
  - Bash(ls *)
  - Bash(cat *)
  - Bash(jq *)
  - Write
---

# EcomAI — Instagram Lead Scraper (hermes skill)

Finds India businesses on Instagram — fashion, food/grocery, wholesalers/distributors, restaurants/cloud kitchens, retail — that run commerce manually (IG feed + DM + WhatsApp) and need EcomAI's complete system. Configurable per run: (category, location, slot). Dedupes against master ledger, validates contacts, outputs scored leads to `EcomAI/leads/inbox/`.

## Context (read first)

1. `EcomAI/PROFILE.md` — product, pricing, built vs planned
2. `EcomAI/icp/icp-definitions.md` — all ICPs + signals
3. `EcomAI/leads/ledger.json` — master lead ledger
4. `HUMAN.md` (Automation root) — operator profile

## Run Instruction (configurable each run)

Parse into (category, location, slot).

| Instruction | Category(s) | ICP |
|---|---|---|
| "find fashion brands and saree businesses" | fashion, saree | ICP 3 |
| "find grocery stores and food brands" | grocery, food | ICP 1 / 4 |
| "find wholesalers, retailers, distributors" | wholesale, retail, distributor | ICP 1 / 4 |
| "find cloud kitchens and restaurants in Bengaluru" | restaurant, cloud kitchen + Bengaluru | ICP 2 |
| "find local clothing stores across Odisha" | clothing, saree + Odisha | ICP 3 / 4 |

Slot (optional): morning | midday | evening, or 1–5. Derive from time if absent. Location appended to searches. No category → rotation fashion → grocery → wholesale → restaurant.

## Category → Search Map

**Rotate search pools — never reuse the previous 2 runs' tag set for the same category** (check `EcomAI/leads/inbox/`).

### Fashion / saree / clothing (ICP 3/4)
`explore/tags/fashionindia/`, `dressselling/`, `sarees/`, `sareelove/`, `boutiqueonline/`, `kurtisindia/`, `indianwear/`, `kapdastore/`, `handmadefashion/`
Keyword: `fashion store whatsapp`, `saree store`, `boutique order whatsapp`, `clothing brand dm order`

### Grocery / food brands / kirana (ICP 1/4)
`grocerystore/`, `kiranastore/`, `foodbusiness/`, `organicstore/`, `farmersmarket/`, `homemade/`
Keyword: `grocery whatsapp`, `kirana store`, `food brand order`, `homemade food delivery`

### Wholesalers / retailers / distributors (ICP 1/4)
`wholesalefashion/`, `wholesaleonly/`, `distributor/`, `bulkorder/`, `wholesalemarket/`, `traders/`
Keyword: `wholesaler whatsapp`, `bulk order`, `distributor order`, `wholesale dealer`

### Restaurants / cloud kitchens (ICP 2)
`cloudkitchen/`, `homechef/`, `restaurant/`, `streetfood/`, `fooddelivery/`, `catering/`
Keyword: `cloud kitchen order whatsapp`, `home chef`, `restaurant order`, `catering whatsapp`

### Jewellery / accessories (ICP 3)
`jewellerystore/`, `antitarnish/`, `handmadejewellery/`, `accessoriesindia/`

### Location suffix
`saree store bengaluru`, `fashion brand delhi`, `grocer odisha`. Try location hashtags: `#bengalurubusiness`, `#odishashopping`.

## What to Find

India businesses in category operating via IG/WhatsApp store with NO complete system. Target signals (bio/posts/highlights/link-in-bio):
- "DM to order" / "WhatsApp us" / "Inbox for price"
- WhatsApp number in bio
- Link-in-bio = WhatsApp/Google Form/nothing (NO proper store)
- Products but no checkout/cart, "Ship all India" / "COD available"
- No Shopify/app

## Lead Quality Gates (ALL mandatory — quality over quantity)

1. **Reachable, validated contact** — WhatsApp/phone/email visible AND valid (hard gate).
2. **ICP match** — fashion→3, food/grocery→1/4, wholesale/distributor→1, restaurant→2, offline→4.
3. **Real business** — passes classifier (not aggregator/influencer/personal/non-India).
4. **Active** — posts ≤30 days (≤7 preferred). Recorded on every lead.
5. **No working online store** — no functioning checkout/Shopify/app. Outdated = OK (rebuild).
6. **Reply-likely** — <10k followers preferred, "DM to order"/"WhatsApp us" language.

Lead missing any gate field (contact_validated, last_post, website_status, website_checked, follower_tier) = incomplete = do not output. When in doubt, leave it out.

## Contact Validation (MANDATORY)

**No usable contact, no lead.**

1. WhatsApp number in bio/highlights/link-in-bio (best)
2. Mobile number (second)
3. Email (last resort)

Validate, don't just collect:

| Rule | Check |
|---|---|
| India mobile | Exactly 10 digits (6–9 first digit) → `+91XXXXXXXXXX` |
| 91-prefixed | `91XXXXXXXXXX` → `+91XXXXXXXXXX` |
| Landline | `0` + 10 digits → `phone`, not whatsapp |
| Email | `name@domain.tld` regex, reject garbage |
| wa.me/wa.link | Resolve → extract number → normalize. Click-to-chat usable. |
| Truncated | Partial number (`889...`) → exclude from contacts, `contact_validated: false`, cap 4 |
| Non-India number | Not `91`/`0` start → keep as phone, `contact_validated: false` |

Store in `contacts: {whatsapp: [], phone: [], email: []}`. `contact_validated: true` only if ≥1 contact passes. **No WhatsApp, no mobile, no email → SKIP.** Never fabricate.

## Business-Type Classifier (MANDATORY)

| Type | Signals | Action |
|---|---|---|
| Aggregator/reseller | Reposts other brands, no own brand, "we supply"/"reseller available", middleman contact | SKIP `aggregator` |
| Influencer/personal | Lifestyle/meme/personal, no products/prices/orders | SKIP `influencer` |
| Non-India | Foreign currency ($/₺/€), foreign locations, foreign ship destinations | SKIP `non-india` |
| Big brand | 100k+ AND working site/app | SKIP `big-brand` |
| Working store | Own domain with functioning checkout/Shopify/app | SKIP `working-store` |
| Inactive | Last post >30d, no engagement | SKIP `inactive` |
| Duplicate | In ledger, last_seen ≤7d | SKIP `duplicate` |
| No usable contact | None valid | SKIP `no-contact` |
| Valid business | Real products, own brand, India, selling language, active | PROCEED |

India evidence: ₹, Hindi/regional, Indian cities, `.in` domain, Indian mobile. Ambiguous → non-India unless India evidence found.

## Activity + Website Check (MANDATORY — recorded on every lead)

### Activity
- Last post ≤7d = active; >30d = SKIP. 3+ posts/30d = active business.
- Engagement: open 1–2 recent posts → ≥50 likes or ≥10 comments = `high`; ≥5 = `medium`; near-zero = `none` (likely dead).
- "DM to order"/"WhatsApp us" in bio = `reply_signal: true`.

### Website
- No URL / link = WhatsApp/form/nothing → `none` (prime target).
- URL loads but old/broken/amateur/no checkout → `outdated` (rebuild, score 7–8).
- Working store (checkout/cart/Shopify/app) → SKIP.

Checklist when visiting: loads? / checkout? / modern or dated? / broken pages? / mobile-render? Record `website_checked: true`.

### Follower tier
- Small (<10k) = FIRST priority. Medium (10k–100k) = OK. Large (100k+) = deprioritize.

**Priority: active + small + no website + validated WA → active + no website + email → active + outdated-website → rest.**

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

- Hard gates (score 0, skip): no/validated-no contact, aggregator, non-India, influencer, inactive, working-store, big-brand.
- **Output threshold ≥6** (below → skipped `low-score`). Urgency: high ≥8, medium 6–7.

ICP map: fashion/saree/jewellery/boutique→`icp3`(or `icp4` local retail); grocery/kirana/food→`icp1`(or `icp4`); wholesaler/distributor→`icp1`; restaurant/cloud kitchen→`icp2`; offline→`icp4`. Shopify: skip.

## Ledger — Master State (MANDATORY)

`EcomAI/leads/ledger.json` = single source of truth. Key = `lead_id = platform | handle | primary_normalized_contact`. Runs upsert.

Load (create if missing):
```bash
[ -f EcomAI/leads/ledger.json ] || echo '{"version":1,"updated_at":null,"leads":{},"skipped":{},"blacklist":[]}' > EcomAI/leads/ledger.json
```

Dedupe check per candidate:
```bash
jq -r --arg id "<lead_id>" '.leads[$id].status // "none"' EcomAI/leads/ledger.json
jq -r --arg h "<handle>" --arg p "<phone>" --arg e "<email>" '.blacklist[] | select(. == $h or . == $p or . == $e)' EcomAI/leads/ledger.json
```

Rules: last_seen ≤7d → `duplicate` (update last_seen/seen_count only). >7d → requalify (refresh score/activity). In blacklist → skip `blacklisted`. New → first_seen=now, seen_count=1, status=new.

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

## Reliability (4–5 runs/day)

- No parallel runs on same platform. IG + FB may run concurrently.
- ≥3h between same-platform runs; never same platform+category within 6h.
- Rotate search pools each run. Candidate budget 10–15, hard cap 20, session <30 min.
- IG checkpoint/login wall → STOP, save partial, mark `run_status: aborted`, report. Fresh session after ≥30 min cooldown.
- Fresh session per run + `browser-use close --all`. Profile fails to load → skip + note.

## Output Schema

Write to `EcomAI/leads/inbox/ig-{timestamp}.json`:

```json
{
  "agent": "ecomai-ig-lead-scraper",
  "timestamp": "ISO-8601",
  "platform": "instagram",
  "icp_focus": ["icp3", "icp4"],
  "categories_scraped": ["fashion"],
  "slot": "morning|midday|evening",
  "run_status": "completed|aborted",
  "run_summary": {
    "candidates_seen": 18,
    "qualified_output": 5,
    "new_leads": 3,
    "updated_leads": 2,
    "skipped_total": 13,
    "skipped_by_reason": { "duplicate": 4, "no-contact": 5, "inactive": 2, "aggregator": 1, "non-india": 1 }
  },
  "items": [
    {
      "lead_id": "instagram|@handle|+919876543210",
      "timestamp": "ISO-8601",
      "platform": "instagram",
      "source_url": "https://instagram.com/handle",
      "handle": "@handle",
      "page_name": "Business Name",
      "category": "fashion|grocery|wholesale|restaurant|jewellery|retail|other",
      "icp": "icp3|icp4",
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
    { "handle": "@handle", "reason": "no-contact|inactive|aggregator|non-india|influencer|working-store|big-brand|duplicate|blacklisted|low-score" }
  ]
}
```

## Workflow

1. Parse instruction → category + location + slot. Pick rotated tags (avoid previous 2 runs' sets).
2. Load ledger. Verify no concurrent same-platform run.
3. `browser-use --session ecomai-ig --profile Amitav open <tag/search>`
4. `browser-use --session ecomai-ig state`
5. Collect 10–15 candidates (cap 20). Dedupe-check each handle before opening.
6. Open profiles: bio, followers (number, never null), link-in-bio.
7. Classify → skip non-leads with reason.
8. Contact validation → normalize; skip unreachable (`no-contact`).
9. Activity + website checks → record all fields.
10. Score (formula). Output ≥6. Sort desc.
11. Write run file with `run_summary`.
12. Merge into ledger (items + skipped). `updated_at`.
13. Report top 10 (handle + category + contact + score) = today's outreach priority.
14. `browser-use close --all`.

## Rules

- Never auto-DM/auto-send/auto-publish. Leads only.
- Contact gate: validated WhatsApp/phone/email required. No usable contact = skip. Never fabricate.
- Activity gate: posts ≤30d only. Inactive = skip. Prioritize ≤7d.
- Completeness gate: every lead records contact_validated, last_post, posting_cadence, engagement_tier, website_status, website_checked, follower_tier. Missing any = do not output.
- No-website priority: active + no-website + validated WA + small-following FIRST. Outdated = rebuild.
- Facts only from visible bio/posts. No guessing.
- Rate-limit/login wall: stop, report, don't hammer.
- `--profile Amitav`. Close all sessions. Normal English output.

## Tunables (defaults in bold)

Output threshold **≥6** · Top batch **10** · Dedupe window **7d** · Candidate cap **10–15/20** · Engagement: high ≥50 likes/≥10 comments, medium ≥5, else none