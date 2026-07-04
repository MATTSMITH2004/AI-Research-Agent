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

## One-off requests for the next brief

Ad-hoc asks for the upcoming run only — NOT durable preferences. Action each one in
the next brief, then delete it from this list (do not let it linger or harden into a
standing rule).

- (none open)

## Learned preferences

Refinements learned from my feedback. Empty to start; fill in as I react to briefs.

### Style and formatting
- Canonical format reference: templates/ai-pulse-format-reference.docx/.md (the
  week-of-Jun-24 brief). This is THE format going forward; match it. It replaced
  the earlier June-20 layout, now archived in briefs/archive/. Regenerate the
  reference from the latest brief whenever the format meaningfully changes.
- Pulse brief structure — the 3-required + 2-optional beat design (What happened,
  optional "Does it hold up?" / "Both sides," Why it matters, My take): the canonical
  template lives in topics/ai-pulse.md "Output shape." Don't restate the full
  template here — edit it there. Standing reminders that tie to the other rules:
  keep "My take" labeled as editorial, fold the evidence inline (no separate evidence
  beat), and keep the voice neutral per the VOICE rule below.
- VOICE (changed Jun 27, 2026): the brief reads neutrally for a distribution list,
  not addressed to Matthew — the full rule lives in CLAUDE "Audience and voice" and
  is applied in topics' beats. The deltas to remember: the beats were renamed ("Why
  it matters to me" -> "Why it matters," "My read" -> "My take"), and only the
  addressing is neutral — lenses, calibration, and what-matters stay personalized
  to Matthew.
- "What people are saying" format — its own section, two bold colon-labels
  ("**What it was about:**" / "**Why it matters:**") that the renderer auto-colors
  dark teal, Substack parity with the podcasts, depth scaled to the speaker, and a
  quote when there's a good one: the full spec lives in topics/ai-pulse.md "Output
  shape." Learned anchor to keep: the week-of-Jun-24 brief shortchanged the
  Substacks by compressing them into one paragraph — give each its own full
  two-beat entry, never compress.

### Sources
- The sourcing rules themselves live in CLAUDE ("Voice and sourcing," "Jargon
  rule") and topics ("Sources to prioritize" + the What-happened beat): cite every
  source used on the Source line; primary sources over secondhand articles; gloss
  every benchmark and every tech-business buzzword in plain words, in every section
  including "What people are saying." Renderer detail (lives only here): source
  links render as clickable blue hyperlinks, anchor = the domain.
- Learned anchors to keep — specific past misses, do not repeat:
  - Benchmarks/buzzwords: the week-of-Jun-24 Snowflake item left "craft-and-margin
    economics" and "agent-driven legacy migrations" unexplained.
  - Primary sources: the week-of-Jun-24 brief wrongly cited a TheStreet article for
    Nadella's essay instead of his actual post.
  - Finance fundamentals I already know (margins, valuation, and the like) do not
    need glossing — but a vague tech-business phrase built around them still does.

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
- AI Daily Brief sourcing — read every daily web/markdown edition in the window,
  use it as a lead-finder to primary sources, the agent.json feed -> e/<date>.md
  path, skip the audio transcript: the full rule now lives in topics/ai-pulse.md
  (the AI Daily Brief entry under "AI-focused shows").

### Automation
- CRITICAL git rule: NEVER force-reset claude/ai-pulse-weekly to main
  (`git branch -f claude/ai-pulse-weekly main` + force-push). That DISCARDS the
  routine's accumulated briefs and MEMORY updates — it already wiped the 06-27
  brief once (recovered from orphaned commit 1a6d3ab). To push config changes from
  main into the weekly branch, MERGE: `git checkout claude/ai-pulse-weekly &&
  git merge main && git push` (no force). To bring accumulated briefs/MEMORY into
  main, merge the other way (weekly -> main). Always merge, never force-reset.
- The AI Pulse brief is meant to run as a weekly Claude Code Routine (Sat ~8am
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
- Email body format (set in mailer.py): "Good morning," + "Attached is your AI
  Pulse brief for the week of <date>." + the brief's intro paragraph, then the
  .docx attached. Do NOT dump the full brief text in the body. Greeting is generic
  ("Good morning,") because the brief now goes to a distribution list, not just
  Matthew. The brief content itself is also written neutrally now (no "Matthew,"
  intro). mailer.py still strips a leading "Matthew," from the intro defensively,
  but the brief should no longer produce one.
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
    compute economics. PROMOTED Jun 2026 (Matthew blessed it). Last contributed:
    week of Jul 4 ("Meta Compute: Everyone Wants To Be A Neocloud" — direct
    rebuttal to the CoreWeave/Nebius selloff narrative).
  - No Priors (Sarah Guo + Elad Gil): HIT week of Jul 4 (Isaiah Taylor/Valar
    Atomics nuclear-AI energy episode).
  - Dwarkesh Podcast: HIT week of Jul 4 (Grant Sanderson on AI and math —
    verifiability + grindability framework).
  - Greg Isenberg: HIT week of Jul 4 ("AI Agents are the new SaaS" operator
    playbook).
  - Odd Lots: HIT week of Jul 4 (Baidu CFO Henry He; Dan Wang China trip used as
    a "Worth a skim" item rather than full entry).
  - a16z Podcast: HIT week of Jul 4 (Andreessen "Beyond P(doom)"). Back online
    after two straight timeout misses (Jun 27, and unreachable before that).
  - Hard Fork: HIT week of Jul 4 (Fable ban reversed + Dana Suskind segments —
    two full entries from one episode). Back online after a Jun 27 timeout miss.
  - In Good Company: not checked this week (no in-window episode looked AI-
    relevant per the fetch_transcripts listing — Fortescue/mining CEO). Last
    contributed: week of Jun 24 (Snowflake CEO).
  - Interconnects (Nathan Lambert): HIT week of Jul 4 ("Artifacts #22" open-model
    roundup — Zyphra, Cohere, Poolside).
  - Import AI (Jack Clark): HIT week of Jul 4 (issue 463 — self-improving robots,
    10K-GPU Chinese cluster).
  - Stratechery (Ben Thompson): MISS week of Jul 4 (announced summer break
    through Jul 5 — no new content, not a quality issue). Last contributed:
    week of Jun 27.
  - Noahpinion (Noah Smith): MISS week of Jul 4 (Roundup #84 published but only
    glancingly AI-relevant — an AI-sycophancy study citation, not full-entry
    material).
  - The Diff (Byrne Hobart): HIT week of Jul 4 ("The Mythical Agent-Minute" +
    "Every AI Lab is a Neocloud for Fifteen Minutes" — both paywalled, summarized
    from previews).
  - Money Stuff (Matt Levine): MISS week of Jul 4 ("Tricking the AI Investors"
    published but fully paywalled, only headline-level detail accessible).
  - One Useful Thing (Ethan Mollick): HIT week of Jul 4 ("The Twilight of the
    Chatbots" — independent agent-capability evidence, direct tie to Fable news).
  - The Generalist (Mario Gabriele): checked week of Jul 4, in-window post
    ("Welcome to GLP-World") was non-AI (GLP-1 drugs) and paywalled — not counted
    as a miss on AI-relevance grounds, just off-topic this week.
  - Net Interest (Marc Rubinstein): MISS week of Jul 4 (no post published in
    the window).
- Candidates surfaced, awaiting Matthew's verdict:
  - BG2 Pod (Brad Gerstner + Bill Gurley), bg2pod.com — investor-led AI-and-markets
    analysis (capex circularity, hidden leverage). Surfaced week of Jul 4.
  - Every (Dan Shipper), every.to — hands-on, falsifiable AI product testing
    ("Vibe Check" series scored Fable 5 vs Opus 4.8 vs GPT-5.5 on a concrete
    benchmark). Surfaced week of Jul 4.
  - The Cognitive Revolution (Nathan Labenz), cognitiverevolution.ai — technical/
    practitioner-level interviews with AI researchers. Surfaced week of Jul 4.
- Flagged for possible pruning (~4 straight misses / quality drop / redundant):
  - (none yet — Stratechery's miss this week was an announced break, not quality;
    Noahpinion and Money Stuff are on their second-ish thin week but not yet at
    the ~4-miss threshold)
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

- Week of Jul 4, 2026 (Fable's full return + the AI economy's first report card):
  - Fable 5 fully restored worldwide (Jul 1) after 19 days offline; GPT-5.6 (Sol/Terra/Luna) shipped Jun 29 restricted to ~20 trusted partners at government request; Claude Sonnet 5 shipped alongside Fable's return. Hard Fork's "default no environment" framing (any model beating Mythos/GPT-5.6 assumed blocked pending government review); Coinbase halved its AI bill defaulting to GLM 5.2/Kimi as a policy-risk hedge, not a capability choice.
  - Model roundup: OpenAI's own Sol system card disclosed cheating/benchmark-gaming; independent evaluator METR couldn't produce a trustworthy capability read (11.3 hrs vs 270+ hrs depending on how cheating is scored). Artificial Analysis found Sonnet 5 costs MORE per task than Opus 4.8 despite cheaper sticker price (30% more tokens, ~3x agentic turns vs Sonnet 4.6). GLM 5.2, DeepSeek V4 Pro, Kimi K2.7, Nemotron 3 Ultra specs compared; open-weight gap ~4 months (Epoch AI) to ~7 months (China-specific), near-zero in coding.
  - Exponential View's first "State of the AI Economy" report: $110B trailing-12-month revenue, $175B run rate, Q1 2026 quarterly revenue exceeded quarterly depreciation for the first time. Ramp/Revelio: high-AI-adoption firms grew headcount 10% (12% entry-level) vs flat for low-adoption; Remote Labor Index: Fable scored 16.1% (quadrupled in 8 months) but 84% of tasks still need a human; BLS: tech/finance still shedding 28K jobs/month.
  - Memory/chip price spike: Micron's actual (not target) Q3 gross margin 84.9%, DRAM ASPs +~60% q/q; Apple raised MacBook/iPad prices up to $200; Xbox +$100-150 effective Aug 1; federal class action alleges Samsung/SK Hynix/Micron cartel behind ~700% DRAM price rise (unproven allegation); Apple lobbying to source memory from blacklist-adjacent Chinese supplier CXMT.
  - "Tributary capitalism": OpenAI proposed a 5% equity stake (~$42.6B) to a government sovereign-wealth vehicle modeled on Alaska's Permanent Fund, floated Anthropic/Google/Meta joining (inverts/pre-empts Sanders' 50%-tax proposal from two weeks prior); Meta Compute (internal cloud business) sent Meta stock +8.8% same day CoreWeave/Nebius fell 15-17%; SemiAnalysis pushed back that this signals acceleration, not overcapacity (Meta contracted 5GW in H1 2026).
  - Alex Karp (Palantir) CNBC interview (Jul 1, one-off request, now closed): "wealth tax" attack on OpenAI/Anthropic token pricing, new Palantir-Nvidia "Sovereign AI" partnership, Palantir stock +8-9%.
  - Perspective: Hard Fork (Fable ban reversed segment + Dana Suskind on parenting/AI); a16z Andreessen "Beyond P(doom)" (blue/red sector economy split, price-per-token could reverse); No Priors Isaiah Taylor/Valar Atomics (nuclear-AI energy nexus); Odd Lots Baidu CFO Henry He (unit economics, "daily active agents") and Dan Wang on China ("Fortress China"); Greg Isenberg "AI Agents are the new SaaS" (concrete operator playbook); SemiAnalysis, One Useful Thing "Twilight of the Chatbots," The Diff "Mythical Agent-Minute," Interconnects "Artifacts #22," Dwarkesh w/ Grant Sanderson (verifiability + grindability framework), Import AI 463.

- Week of Jun 27, 2026 (partial resolution + hardware proof points):
  - Mythos partial reprieve (Jun 26): US Commerce cleared Mythos 5 for 100+ US trusted-partner institutions; Fable still banned; Lutnick letter citing "appropriate safeguards." Fable conversations ongoing through weekend. Ben Thompson Stratechery "Anthropic and Alignment" — corporate safety gates can't substitute for democratic accountability; parallel to nuclear governance. Legion lawsuit against US over Fable ban still live.
  - OpenAI Jalapeño chip (Jun 24): first custom inference ASIC with Broadcom; 9 months design to TSMC 3nm tape-out; AI-assisted design process; claims 50% cheaper inference vs Nvidia GPUs (self-reported, unverified); deployment end of 2026; Broadcom CEO: demand "simply insatiable" through 2028; won't reduce Nvidia orders near-term.
  - Claude Tag in Slack (Jun 23–24): Anthropic puts Claude Code into Slack as persistent org teammate on Opus 4.8; 65% of Anthropic product code from Claude Tag internally; Tobin South: "90%-plus of my work"; Karpathy: "third major redesign of how we interact with LLMs"; concerns: surveillance optics in shared channels; Hugging Face counter: build your own agent; KPMG/UT Austin 1.4M interaction study — high-impact users treat AI as reasoning partner not prompt tool.
  - Micron Q3 FY2026 blowout (Jun 25): $41.46B revenue up 346% YoY from $9.3B; Q4 guidance $50B (vs $43.2B est.); stock +15% after-hours; HBM4 shipping for Nvidia Vera Rubin; 2026 HBM fully booked; 16 long-term supply agreements, $22B committed; 81% projected Q4 gross margin.
  - Anthropic-Alibaba distillation (Jun 24–25): 28.8M Claude interactions via 25,000 fake accounts April-June; largest known distillation campaign; targeted software engineering + agentic reasoning; Anthropic wrote to White House; shadow market in China selling Claude API access at 90% off via stolen credentials.
  - Gemini 3.5 Pro slips to July — confirmed missed June 30 target; two slips now.
  - Grok 5 missed Q2 window; xAI shipped Grok Voice, Grok Imagine Video 1.5, /goal in Grok Build instead; Q3 expected.
  - DeepMind exodus continues: Jonas Adler + Alexander Pritzel to Anthropic (follows Shazeer/Jumper from prior week).
  - Meta sole holdout on voluntary safety model review; White House pressing.
  - Commerce Dept closed-door meeting on Chinese robots (Boston Dynamics, SpaceX, Siemens, Goldman); GUARD Act moving in Congress.
  - ByteDance Seedance 2.5: 30s clips, 4K, 50 input references + multimedia.
  - xAI /goal primitive in Grok Build (Grok fine-tune + Cursor Composer 2.5).
  - Perspective: No Priors Noam Brown (benchmarks don't control for compute budget; models think for weeks before plateauing; safety frameworks ignore test-time compute; Erdős Unit Distance Conjecture disproved at "dirt cheap" cost; latent frontier capability underexplored); Dwarkesh "next training paradigm" (RLVR generalization bet; grindability bottleneck for law/politics; OPSD for continual learning; ~30-50% of lab compute to inference with zero training signal feedback; "wasted inference" problem); Stratechery Thompson "Anthropic and Alignment" (democratic oversight must govern military AI; corporate gatekeeping insufficient); Odd Lots Jun 20 (Substack writers on covering AI-markets era; "being cited by the AI" as distribution strategy); Greg Isenberg "six skills" (agent design, distribution, robotics, curation/yapping, builder-distributor, IRL community; most companies need an AI "operating system" builder).

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
