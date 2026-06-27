# Memory

This file is the agent's evolving memory. `CLAUDE.md` is the fixed foundation and
is not edited. This file is the layer the agent maintains from my feedback and
from what it has already reported, so the briefs keep getting more on-target and
stop repeating themselves.

How to maintain this file:

- Read it at the start of every run, alongside `CLAUDE.md`, and apply it.
- Update it in place. Replace outdated entries, do not just append to the bottom.
  The file should always reflect the current state, not a history of edits.
- Record only durable preferences, not one-offs. "Make this week shorter" is a
  one-off; "always lead with the money items" is a rule. If a rule is ambiguous,
  state it back to me before saving it.
- Keep it lean. Trim anything stale.

## Learned preferences

Refinements learned from my feedback. Empty to start; fill in as I react to briefs.

### Style and formatting
- Canonical format reference: templates/ai-pulse-format-reference.docx/.md (the
  week-of-Jun-24 brief). This is THE format going forward; match it. It replaced
  the earlier June-20 layout, now archived in briefs/archive/. Regenerate the
  reference from the latest brief whenever the format meaningfully changes.
- Pulse brief structure: Title + "Week of" line, short intro, then Top
  developments as numbered claim-sentence headings. Each top item is broken into
  labeled beats — What happened / The evidence / Why it matters to me, traced out
  (use an indented bullet list when there are multiple reasons) / My read. Always
  keep "My read" explicitly labeled as my own opinion, separated from the facts.
  Full template lives in topics/ai-pulse.md "Output shape."
- Keep "What people are saying" as its own section (do not fold the perspective
  takes into the items). Write each take as two beats opened with literal bold
  labels — "**What it was about:**" and "**Why it matters:**". These labels are
  keys and must stand out: the Word renderer auto-colors any bold colon-terminated
  label in a distinct accent (dark teal), so always write them in that exact form.
- Substacks get FULL parity with the podcasts in that section — each its own
  labeled two-beat entry at the same depth, never compressed into one summary
  paragraph. They are a top-tier perspective source. (Week-of-Jun-24 brief first
  shortchanged them in one paragraph; corrected.) Give more depth for high-signal speakers (major
  CEOs, frontier-lab leaders, serious investors) — more on what was actually
  said, not a one-liner. Include a good quote when there is one; do not force a
  quote every time.

### Sources
- Cite every source actually used in an item, not just the strongest one. List
  them all on the Source line, each with a few words on what it supports. In the
  Word doc, render source links as clickable blue hyperlinks (anchor = domain).
- Always explain benchmarks in plain language — what the test measures and how to
  read the score (higher is better, what counts as good, what it means in
  practice) — never just drop a benchmark name or number. I do not know the
  benchmarks. Same for jargon like parameters, context window, license: gloss on
  first use.
- This applies to ALL sections (including "What people are saying"), and to
  business/tech buzzwords, not just hard technical terms. Never let an unexplained
  buzzy phrase carry the point. Things like "industrialization of software,"
  "craft-and-margin economics," "legacy migration," "data pipeline," "front door
  to computing" must be glossed in plain words I already have. Finance
  fundamentals I know (margins, valuation, etc.) do not need spelling out, but a
  vague tech-business phrase built around them still does. (Critique on the
  week-of-Jun-24 Snowflake item: "craft-and-margin economics" and "agent-driven
  legacy migrations" went unexplained — do not repeat that.)
- Primary sources first, always. When someone posts a specific thing (essay,
  blog, filing, paper, model card, X/LinkedIn post), read and cite that primary
  directly — never a secondhand article about it. Secondary only supplements the
  primary or fills in when no primary exists. (The week-of-Jun-24 brief wrongly
  cited a TheStreet article for Nadella's essay instead of his actual post — do
  not repeat that.)

### Emphasis
- Keep the lens mix balanced for now; do not tilt the whole brief toward any one
  angle. The three I care about roughly equally: operator / idea-generation,
  finance, and the technical apparatus.
- The technical interest is genuine, not just background. I want to track how the
  technology, the companies, and the people are advancing and what is changing —
  and especially the different models and the specs and trade-offs between them.
  When a model is material, give the concrete comparison (context window, price,
  benchmarks, speed, strengths/weaknesses), pitched for fluency, not engineering.
- Standing "models and their specs" beat, including open-weight and Chinese models
  (GLM, DeepSeek, Kimi, Qwen, etc.) — see topics/ai-pulse.md "What to track" #1.

### Sources, kept and dropped
- WSJ: keep as a written/journalism source for article research, NOT as a podcast.
  Read headlines/snippets via search and cite; full articles are paywalled and I
  cannot legitimately get past it with these tools — no paywall-bypass mirrors, no
  stored login. If a WSJ article is load-bearing, flag it and Matthew pastes the
  text.
- WSJ full-article automation is PARKED until ~August 2026. WSJ sits behind
  DataDome bot protection that blocks server-side fetches (and the login itself)
  regardless of credentials, so do not scrape it. The plan: once Matthew has
  university/library Factiva or ProQuest access (expected around August, with law
  school), read full WSJ text through that legitimate channel. Revisit then. A
  browser-side one-click capture bookmarklet is the fallback if Factiva/ProQuest
  does not pan out.
- Dropped from the weekly podcast scan: WSJ What's News, FT News Briefing, and
  Bloomberg Talks.
- AI Daily Brief: pull the published web/markdown edition per day (via the
  agent.json feed -> e/<date>.md), not the verbatim audio transcript. It is NLW's
  own structured write-up, so it is denser and cleaner AND fewer tokens — the best
  version, not a lossy shortcut. Skip the separate transcript.md.

### Automation
- The AI Pulse brief is meant to run as a weekly Claude Code Routine (Sat ~9am
  Eastern) that generates the brief and delivers it to Matthew. Setup guide and
  the ready-to-paste routine prompt: docs/weekly-brief-routine.md. The routine
  environment needs Full/Custom network access (the brief scrapes the open web).
- State branch: the routine runs on the dedicated branch `claude/ai-pulse-weekly`,
  NOT main. It checks out that branch at the start (it carries the rolling
  MEMORY.md + past briefs) and pushes the new brief + MEMORY back to it each week.
  Reason: enabling "Allow unrestricted branch pushes" (needed to push to main)
  breaks routine creation on Matthew's GitHub install, but `claude/`-prefixed
  branches are always pushable. Keeping state on this branch preserves the
  recently-covered history week to week, which is what prevents repeats. (To fold
  the accumulated briefs into main, merge claude/ai-pulse-weekly -> main manually.)
- Delivery: REAL SEND via scripts/mailer.py using the SendGrid HTTPS API. The
  digest goes to MULTIPLE recipients, so it must be a true sent email (no manual
  click), Bcc'd to the PULSE_RECIPIENTS list, with the rendered .docx attached.
  Env vars (routine vault): SENDGRID_API_KEY, SENDGRID_FROM (verified Single
  Sender), PULSE_RECIPIENTS. mailer.py supports --no-email for a dry run.
- Email body format (set in mailer.py): "Hi Matthew," + "Attached is your AI Pulse
  brief for the week of <date>." + the brief's intro paragraph, then the .docx
  attached. Do NOT dump the full brief text in the body.
- Deliverability note: sending from a free gmail.com From lands in Junk on
  corporate M365 (DMARC mismatch). It delivers, just to Junk. The durable fix for
  inbox delivery is a domain Matthew controls, authenticated (SPF/DKIM) in
  SendGrid — parked until he has a domain.
- IMPORTANT environment fact: the cloud env BLOCKS outbound SMTP (ports 587/465) —
  only HTTP/HTTPS egress works — so SMTP senders (Gmail app-password, Outlook
  SMTP) cannot connect. That is why we use an HTTPS email API. Microsoft 365 send
  is unavailable (connector exposes no send option), and the Gmail connector can
  only draft (no send, no attachments). SendGrid HTTPS API confirmed reachable.

### Source-discovery ledger
Tracks the standing "find new sources" beat and the promote/prune system (process
in topics/ai-pulse.md "Source discovery"). THIS LEDGER IS PERSISTENT — never trim
it (unlike the "recently covered" news list above, which trims to ~4-6 weeks).
Each run, mark commentary sources hit/miss and update "last contributed."

- Standing rotation (commentary sources I scan every week):
  - SemiAnalysis (Dylan Patel), newsletter.semianalysis.com — chips, datacenters,
    compute economics. PROMOTED Jun 2026 (Matthew blessed it). Also added to the
    topics/ai-pulse.md Substack list. Last contributed: week of Jun 24 (surfaced
    as the find that promoted it).
  - The other baseline podcasts/Substacks in topics/ai-pulse.md are the rest of
    the rotation; start logging hit/miss for them as runs accumulate.
- Candidates surfaced, awaiting Matthew's verdict:
  - (none open)
- Flagged for possible pruning (~4 straight misses / quality drop / redundant):
  - (none yet)
- Passed on / rejected (do not re-surface):
  - (none yet)

## Working process

- For any change Matthew requests, always work on a branch first, show him the
  change, and only merge to `main` after he approves. Handle all the git mechanics
  for him — he does not run git himself. Exception: for tiny, obvious fixes he says
  "just push," commit straight to `main`.
- `main` is the live version the weekly Routine runs from, so any change meant to
  affect the automated brief must end up merged to `main`.

## Already known and covered

What I already understand (so the agent does not over-explain) and what has
already been reported (so it does not repeat it). Maintained per topic.

### AI Pulse

Baseline I already know (do not re-explain):

- The basics of how agents are wired up: skills, context files, MCP.

Recently covered (rolling; keep roughly the last 4 to 6 weeks, trim older):

- Week of Jun 24, 2026 (loud week; competition reordering the board):
  - GLM 5.2 "DeepSeek moment": Z.ai open-weight model (released Jun 16) did NOT fade after a weekend of use; ranks #1 on Design Arena for websites (ahead of Fable 5); 62.1 SWE-bench Pro vs GPT-5.5 58.6, within ~1pt of Opus 4.8 on FrontierSWE; ~3.6x/5.7x cheaper than Opus but emits ~25% more code and ~2x slower (Theo: not actually cheaper). NLW: "two-horse race has been broken." Don't buy 8 H200s (~$400K / $20K/mo) — use a router.
  - Google/DeepMind talent crisis: Noam Shazeer -> OpenAI (Jun 18), Nobel laureate John Jumper (AlphaFold) -> Anthropic (Jun 19); Alphabet -7.2% Mon Jun 22 (~$200-250B wiped). Gemini 3.5 Pro slipped to ~Jun 30; internal "not the step change we need." Luria: "losing the war for talent." NLW counter: "peak Google is done for" has always been wrong.
  - Nadella essay "A Frontier Without an Ecosystem Is Not Stable" (~Jun 12-15, went viral this week, 65M reads): human capital x scaffolding x feedback = "token capital"; build a model-agnostic learning system you own, not an AI strategy. Private evals + RL environments + knowledge base = "hill-climbing machine." Suleyman's Frontier Tuning (launched Build, Jun 2). Operator-central.
  - Fable/Mythos ban -> truce: White House-Anthropic talks thawing toward a security-flaw severity framework (Levie: preview of a slower, more-reviewed release regime); Trump conciliatory on Axios. "Mythos hacked the NSA in hours" claim retracted (was a controlled red-team exercise). OpenAI countered with Daybreak + GPT-5.5 Cyber (claims 85.6% vs Mythos 83.8% CyberGym - its own framing while Mythos is offline) + Patch the Planet w/ Trail of Bits.
  - Bernie Sanders $7T AI sovereign wealth fund (Jun 18): one-time 50% equity tax on AI cos >$200M sales, voting shares, ~$1,000+/yr dividend. NLW: de facto nationalization. Vance likes the stake idea but pivots to unions. Left-right lines scrambled.
  - Skims: Accenture -18% Jun 18 (worst day in ~decade, AI-disruption fear + Iran/bookings); SpaceX-Reflection AI $6.3B Colossus deal (vs ~$1B/mo Anthropic & Google each), SpaceX-Cursor $60B (Jun 16); MS testing DeepSeek V4 fine-tune for Copilot; OpenRouter Fusion model panels + Harvey worker/advisor (smart routing as edge); Trump quantum EOs; Five Eyes AI cyber alert; data-center backlash bipartisan + water/electricity myths debunked (Louisiana $50K teacher bonuses); Coinbase ANTHROPIC-PERP/OPENAI-PERP pre-IPO perps.
  - Perspective: Odd Lots (Grace Shao on China AI economics/hybrid stacks; Jack Clark + McCrory ~1.8pp productivity, 8x code, barbell hiring; Grantham "dogfight of seven ditches" bubble); Hard Fork (Kokotajlo vs Kapoor AI-2027-vs-normal-tech; Dylan Field on taste/average); a16z Andreessen/Horowitz "new rules of media"; In Good Company Snowflake (coding agents = "front door to computing"); Dwarkesh "data black hole" (why open lags ~4mo); No Priors Intel Lip-Bu Tan (CPU:GPU 1:8->1:4, memory bottleneck); Interconnects (GLM step change + "banning open source a mistake"); Stratechery (memory-chip cartel + MS->Chinese models); ChinaTalk (datacenter NIMBY = underpaying communities, not China); Noahpinion ("writing for the AIs"); Import AI (AI super-persuasion study).

- Week of Jun 21, 2026 (quieter week; governance-led):
  - G7 summit, Evian-les-Bains, Jun 17: Amodei + Hassabis + Altman closed-door lunch w/ Trump; called for US-led AI coalition, "structured access" to frontier models, China-excluding chip/component trade, cyber/bio cooperation. G7 pushed US to share access; Macron promised Western-democracies platform within a month, meet again Sept. (Next chapter of last week's Fable export ban + G7 access debate.)
  - OpenAI Jun 18 health/science push: health intelligence in ChatGPT, rare genetic disease diagnosis tool for physicians, near-autonomous "AI chemist."
  - Gemini 3.5 Pro still not shipped mid-June (Pichai promised "next month" at I/O May 19); Flash shipped on time, Pro slipping. 2M context, Deep Think, ~$15/$60 per M tokens.
  - Skims (mostly running context, some predate strict window): OpenAI + Anthropic IPO race (Anthropic S-1 Jun 1 ~$965B/$30B run-rate; OpenAI confidential ~$730-850B, Sept target, ~$27B burn vs ~$25B rev); Anthropic Project Glasswing (Mythos cyber model) 50->150 orgs; Microsoft "Autopilots"/Scout agent; JPMorgan $19.8B tech budget, ~2000 AI staff, ~$2B savings, 10-11% productivity.
  - Perspective: Stratechery "Agents Over Bubbles" (Thompson anti-bubble thesis); ChinaTalk "AI attention war"; ADB Jun 20 G7 framing; Interconnects open-model pressure.

- Week of Jun 13-20, 2026:
  - US govt (Commerce) export-control directive forcing Anthropic to suspend Fable 5 + Mythos 5 worldwide (Jun 12); first govt "kill switch" on a frontier model; G7 access debate; legal theory seen as constitutionally shaky.
  - SpaceX IPO (Jun 11, ~$75B raised, largest ever), +49% to ~$2.6T by Jun 16, Musk first trillionaire; SpaceX as AI neo-cloud story; acquired Cursor for $60B.
  - Bezos's Project Prometheus out of stealth: $12B at $41B valuation, "artificial general engineer" for the physical economy.
  - Z.ai GLM-5.2 open-weight model (Jun 16, MIT, 753B, 1M context) at ~1/6 cost; open models as access/cost hedge after the Fable ban.
  - Skims: OpenAI leaked financials ($38.5B loss mostly one-time PBC charge; profitable on inference; $73B cash); Noam Shazeer Google->OpenAI (Jun 18); Anthropic regulated-industry deals (TCS, DXC); Anthropic Seoul office + NVIDIA Korea buildout; DOJ defends xAI Colossus II turbines; OpenAI Codex expansion.
