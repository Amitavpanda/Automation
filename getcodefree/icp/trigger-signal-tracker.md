---
name: trigger-signal-tracker
description: Seven high-value trigger signals for GetCodeFree — funding announcements, job posts, social signals, Product Hunt launches, AI role hiring, conferences, and vendor-seeking posts with detection methods and response windows.
---

# ICP Trigger Signal Reference

## What is a Trigger Signal?

A trigger signal is an observable event that indicates a prospect is likely in an active buying window. Contacting someone during a trigger window increases conversion rate dramatically compared to cold outreach with no timing signal.

---

## High-Value Trigger Signals for GetCodeFree

### Signal 1: New Funding Announcement
**What it means:** Company just received capital and needs to ship fast
**Where to detect:** Crunchbase, TechCrunch, LinkedIn posts, Inc42 (India)
**Response window:** Contact within 7 days of announcement
**Offer to lead with:** MVP in 5 weeks / AI automation sprint

### Signal 2: Senior Engineering Job Post — Open 30+ Days
**What it means:** They need engineering capacity and can't find/afford full-time hires
**Where to detect:** LinkedIn Jobs, Wellfound, their careers page
**Response window:** Contact within 30–60 days of posting
**Offer to lead with:** Managed partner / specific workstream ownership

### Signal 3: Public Post About Shipping Speed or Bandwidth
**What it means:** Founder/CPO/CTO is frustrated and actively seeking solutions
**Where to detect:** LinkedIn posts, Twitter/X
**Response window:** Contact within 48 hours
**Offer to lead with:** Match to their stated problem exactly

### Signal 4: Product Hunt Launch in Last 90 Days
**What it means:** They shipped something and now need to scale/improve it
**Where to detect:** producthunt.com — sort by recent
**Response window:** 30–90 days post-launch
**Offer to lead with:** MVP to production / AI feature addition

### Signal 5: Hiring for AI/ML Roles with No Success
**What it means:** They want AI capability but can't hire for it — agency is the solution
**Where to detect:** LinkedIn Jobs — filter "AI engineer" + company size 10–50
**Response window:** Ongoing while position is open
**Offer to lead with:** AI automation sprint / AI product build

### Signal 6: Conference Speaker / Attendee
**What it means:** Active in the ecosystem, likely evaluating vendors
**Where to detect:** SaaStr, ProductCon, AI Engineer Summit, GITEX speaker lists
**Response window:** 2 weeks before or after event
**Offer to lead with:** Warm intro, not cold pitch

### Signal 7: LinkedIn Post Asking for Agency/Vendor Recommendations
**What it means:** In active vendor evaluation mode
**Where to detect:** LinkedIn search "looking for agency" / "recommend a dev team"
**Response window:** Within 6 hours
**Offer to lead with:** Direct, specific, no-fluff response

---

## Trigger Signal Monitoring Setup

### Manual (now):
- Check LinkedIn daily for posts matching Signal 3 and Signal 7
- Check Crunchbase weekly for Signal 1 in target ICPs
- Check Product Hunt weekly for Signal 4

### Automated (future agent):
- Crunchbase API → funding announcements → auto-enrich → route to outreach agent
- LinkedIn monitoring → keyword alerts → auto-qualify → route to copy agent
- Apify LinkedIn scraper → weekly job post scan → trigger signal detection

---
