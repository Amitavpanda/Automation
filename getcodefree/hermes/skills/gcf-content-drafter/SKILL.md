---
name: gcf-content-drafter
description: |
  Drafts cold emails, LinkedIn DMs, X/Twitter DMs, and social posts for GetCodeFree. Reads lead data from inbox/, selects best template, personalizes with lead context, and outputs draft to getcodefree/outreach/drafts/. Uses ICP segments for tone modulation. All output is markdown with {variable} placeholders filled from lead data.
allowed-tools:
  - Read
  - Write
  - Bash(cat *)
  - Bash(ls *)
  - Bash(jq *)
---

# GCF Content Drafter

Reads leads from inbox/ and drafts personalized outreach messages.

## Lead Classification

Read the lead JSON and classify:
- **ICP-A1**: Funded pre-seed/seed founder. Needs full MVP. Budget $5-15k. Tone: confident, founder-to-founder
- **ICP-A2**: Bootstrapped founder who raised $50k+. Needs dev team. Budget $3-8k. Tone: practical, ROI-focused
- **ICP-B1**: CTO at growing startup. Needs senior engineer. Budget $4-10k. Tone: technical, capability-focused

## Templates

### Template A: MVP Sprint (for ICP-A1)

```
Subject: {company}'s MVP — 3 weeks to ship

Hi {name},

Saw you're building {product}. Quick question — how's development going?

I run GetCodeFree, an AI-native dev studio. We ship production MVPs in ~3 weeks.

What makes us different:
- Senior-only engineers (I build everything myself)
- Founder-led — you talk to the person shipping code
- AI-assisted delivery (3x faster than traditional)

Shipped: NativeNest (React Native, App Store), EcomAI (AI commerce), InsureSarthi (fintech)

Want to chat about {company} this week?

Best,
Amitav
```

### Template B: AI Automation (for ICP-A2)

```
Subject: AI automation for {company}?

Hi {name},

Noticed {company} is in the {industry} space. Curious — have you looked into AI for {specific_pain}?

We build AI workflows in 5 days: lead gen, content automation, CRM sync, internal tools. Live, not vaporware.

Examples: EcomAI (AI commerce OS), AccounSaathi (AI accounting for wholesale).

Worth 15 min to see if this fits?

Amitav
GetCodeFree
```

### Template C: Senior Engineer (for ICP-B1)

```
Subject: Founding engineer for {company}?

Hi {name},

I'm a founding engineer at a US AI SaaS startup — building and scaling gen-AI from scratch with the CTO.

Also run GetCodeFree where we ship production apps (NativeNest on App Store, EcomAI, InsureSarthi).

If {company} needs senior full-stack/AI engineering, let's talk. I can commit 20-30 hrs/week.

Amitav
```

## LinkedIn DM Variants

Keep DMs to 2-3 lines. Lead with observation, offer value, CTA for call.

DM-A (ICP-A1):
"Hey {name}, saw you're building in the {space} space. We ship production MVPs in ~3 weeks — founder-led, senior-only. Want to compare notes?"

DM-B (ICP-B1):  
"Hey {name}, I'm a founding engineer at a US AI startup — also run a dev studio on the side. If {company} needs senior React/Node/AI help, happy to chat."

## Output

Write draft to `/Users/amitavpanda/Desktop/projects/Automation/getcodefree/outreach/drafts/{lead-name}-{template}.md`
Include:
- Selected template and why
- Filled draft with all variables
- Recommended send time
- Follow-up schedule (3 touches, 2 days apart)
