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
- This file holds state and cross-topic preferences ONLY. Style rules belong in
  the house-writing-style skill; brief shape and coverage in the topic config;
  procedure in the research-digest skill. Route per CLAUDE.md's Memory section —
  do not accept a rule here just because feedback arrived here.

## Learned preferences

Refinements learned from my feedback. Empty to start; fill in as I react to briefs.

### Style and formatting
- Canonical format: topics/ai-pulse.md "Output shape" is THE format definition —
  self-contained, no external template. The old reference docx
  (templates/ai-pulse-format-reference.docx/.md) was DELETED Jul 2026; do not
  look for it or flag its absence as a config error. If a worked example is ever
  wanted again, regenerate it from a recent approved brief — but the Output
  shape section remains canonical either way.
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

### Model ledger
The running model-comparison tracker (process in topics/ai-pulse.md "What to
track" item 1). THIS LEDGER IS PERSISTENT — never trim it (like the
source-discovery ledger below, unlike the "recently covered" news list, which
trims to ~4-6 weeks). Backstage store: the brief never renders this table raw.
When a covered release moves a row, the brief's "Model standings" section shows
a reduced Task / Current best / Contenders view with changed rows marked; the
Basis and Updated columns stay here. Populate ONLY from models covered in
briefs — no fresh benchmark searches to fill cells. An empty cell is honest; a
guessed ranking is not.

| Task | Current best | Contenders | Basis (what a brief showed) | Updated |
|---|---|---|---|---|
| Coding | — | GLM 5.2 | GLM 5.2 beat GPT-5.5 on SWE-bench Pro (62.1 vs 58.6) at ~1/6 cost, ~1pt behind Opus 4.8 on FrontierSWE (Jun 24 brief) | 2026-06-24 |
| Writing | — | — | not yet established from covered briefs | — |
| Reasoning | — | — | not yet established from covered briefs | — |
| Agentic use | Mythos 5 | GPT-5.6 Sol | Mythos led on autonomous exploit build-and-run; Chinese tools matched only routine bug-finding (Jul 4 brief) | 2026-07-04 |
| Cost / value | open-weight (GLM 5.2, Kimi) | — | Coinbase halved AI bill defaulting to open models, usage still grew; Sonnet 5 costs MORE per task than Opus 4.8 despite cheaper sticker (Jul 4 brief) | 2026-07-04 |
| Frontier-general | — | Fable 5, GPT-5.6 Sol, Claude Sonnet 5 | three shipped week of Jul 4; no trustworthy head-to-head yet (METR couldn't score Sol due to benchmark-gaming) | 2026-07-04 |

Update rules: one row per task; when a covered release takes a slot, the old
holder moves to Contenders (keep two or three, do not delete); every filled
cell cites which brief showed it and the date it last moved; a row change is
what triggers the brief's "Model standings" section — no change, no section.

### Source-discovery ledger
Tracks the standing "find new sources" beat and the promote/prune system (process
in topics/ai-pulse.md "Source discovery"). THIS LEDGER IS PERSISTENT — never trim
it (unlike the "recently covered" news list above, which trims to ~4-6 weeks).
Each run, mark commentary sources hit/miss and update "last contributed."

- Standing rotation (commentary sources I scan every week):
  - SemiAnalysis (Dylan Patel), newsletter.semianalysis.com — chips, datacenters,
    compute economics. PROMOTED Jun 2026 (Matthew blessed it). Last contributed:
    week of Jul 11 (Nvidia GPU debt-backstop mechanism, Anthropic 3Q26 profit/IPO
    estimate, Meta superintelligence progress update — three posts).
  - No Priors (Sarah Guo + Elad Gil): HIT week of Jul 11 (Booking.com CEO Glenn
    Fogel on moats, Penny agent unit economics).
  - Dwarkesh Podcast: MISS week of Jul 11 (one in-window episode, pure physics
    lecture on general relativity, no substantive AI content beyond a training-
    efficiency aside). Last contributed: week of Jul 4.
  - Greg Isenberg: HIT week of Jul 11 (Grok 4.5/Hermes agent demo; Dan Shipper on
    GPT-5.6 Sol and Codex-as-OS framing — two episodes).
  - Odd Lots: HIT week of Jul 11 (Man Group 86x token-spend growth; prediction-
    market trader on LLM sycophancy and forecasting — two episodes).
  - a16z Podcast: HIT week of Jul 11 (Sinofsky + Amble, "Is Software Losing Its
    Head?" — headless-software/agent-native SaaS framework).
  - Hard Fork: HIT week of Jul 11 (Jeff Sebo AI-welfare interview, tied to
    Anthropic's new "global workspace" interpretability research).
  - In Good Company: HIT week of Jul 11 (CPP Investments CEO John Graham —
    skeptical institutional-investor take on AI decision quality).
  - Interconnects (Nathan Lambert): MISS week of Jul 11 (no post; last published
    Jun 28, confirmed via full archive check). Last contributed: week of Jul 4.
  - Import AI (Jack Clark): HIT week of Jul 11 (issue 464 — record GPU kernel
    speedup, Remote Labor Index climbing to 16.1%).
  - Stratechery (Ben Thompson): HIT week of Jul 11 ("Muse Image, Grok 4.5, Alex
    Karp on CNBC" — thesis on verifiable data as the next competitive axis;
    mostly paywalled, thesis-level only).
  - Noahpinion (Noah Smith): MISS week of Jul 11 (published several times but
    nothing squarely AI-focused landed in the window). Second miss in a row —
    not yet at the ~4-miss prune threshold.
  - The Diff (Byrne Hobart): thin week of Jul 11 (three issues published, all
    fully paywalled beyond headline/teaser; only the free Jul 4 "Longreads" post
    was fully readable). Treating as a partial miss, not a full one.
  - Money Stuff (Matt Levine): MISS week of Jul 11 (several columns published;
    AI content was incidental/satirical asides inside non-AI columns, not a
    dedicated AI thesis).
  - One Useful Thing (Ethan Mollick): MISS week of Jul 11 (no post; last
    published Jun 30, confirmed via full archive check).
  - The Generalist (Mario Gabriele): HIT week of Jul 11 ("RAM Fever" — memory-
    chip pricing power and the consumer-price cascade).
  - Net Interest (Marc Rubinstein): thin/MISS week of Jul 11 (published, but on
    Indian equity-derivatives markets with only a brief AI-fraud-detection
    aside — not AI-focused).
  - BG2 Pod (Brad Gerstner + Bill Gurley), bg2pod.com: MISS week of Jul 11 (no
    episode in-window across five sources checked; most recent confirmed
    episode Jun 11). First miss since promotion (Jul 2026) — not a concern yet.
  - Latent Space (swyx / Shawn Wang + Alessio Fanelli), latent.space: HIT week of
    Jul 11 (Modal CTO Akshat Bubna on agent-native infrastructure economics).
  - AI Engineer (YouTube channel), youtube.com/@aiDotEngineer: HIT week of Jul 11
    (Thariq Shihipar's "Field Guide to Fable" one-off, plus the "Z/L continuum"
    should-engineers-read-code debate). Note: direct transcript/caption access
    for this channel keeps failing (no configured show in fetch_transcripts.py,
    and YouTube rate-limited on manual attempts) — coverage has relied on
    third-party recaps and speakers' own blog posts two weeks running. Worth
    fixing the tooling (add an "ai-engineer" show handler) rather than
    continuing to work around it by hand.
- Candidates surfaced, awaiting Matthew's verdict (on trial — promote after ~3
  hit-weeks, prune after ~4 straight misses):
  - Every (Dan Shipper), every.to — hands-on, falsifiable AI product testing.
    HIT week of Jul 11 (three posts: "Efficiencymaxxing" on revenue-per-token
    replacing revenue-per-employee, "Vibe Check" on GPT-5.6 Sol, "Tend Your
    Loop" on continuous-agent workflows). Second straight hit week (surfaced
    week of Jul 4) — one more hit week and it should be promoted.
  - The Cognitive Revolution (Nathan Labenz), cognitiverevolution.ai — technical/
    practitioner-level interviews with AI researchers. NOT CHECKED week of Jul
    11 (a gap in this run's coverage, not a confirmed miss — the podcast sweep
    missed it). Still on trial from week of Jul 4; needs an actual check next
    week before its trial clock can advance either way.
  - Epoch AI ("Gradient Updates"), epoch.ai/gradient-updates — primary
    quantitative research on compute growth, training costs, and inference
    economics; complements SemiAnalysis's business/supply-chain angle with the
    underlying math. Surfaced week of Jul 11; on trial.
  - Elad Gil's blog, blog.eladgil.com — operator/investor mapping which AI-
    adjacent markets are won vs. still open; strongest direct hit on the
    idea-generation lens found so far. Surfaced week of Jul 11; on trial.
  - Benedict Evans, ben-evans.com — macro-historical tech analysis, a genuine
    hype-check complement to Stratechery's competitive-strategy lens. Surfaced
    week of Jul 11; on trial.
- Flagged for possible pruning (~4 straight misses / quality drop / redundant):
  - Noahpinion: two straight misses (Jul 4, Jul 11) on AI-relevance grounds, not
    quality — watch, not yet actionable.
  - Money Stuff: two straight misses (Jul 4 fully paywalled, Jul 11 only
    incidental AI content) — watch, not yet actionable.
- Passed on / rejected (do not re-surface):
  - Asianometry (Jon Y), YouTube semiconductor explainers — high quality but
    passed on for now as a format experiment (video-essay, redundant with
    SemiAnalysis/ChinaTalk's chip coverage); Sacra (functions as a paid
    reference database, not an editorial weekly read); Zvi Mowshowitz's "Don't
    Worry About the Vase" (redundant with the existing general-AI-news sources
    already in rotation/on trial).

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

- Week of Jul 11, 2026 (money and cost economics diverge; a second US-China front opens):
  - Anthropic's secondary-market valuation hit $1.2T (Jul 10), passing OpenAI's ~$908B, alongside SemiAnalysis's estimate of >$1B Q3 profit and a confidential June 1 IPO filing; Bank of America extended OpenAI its first-ever credit line ($520M) to court an IPO advisory role.
  - The "good enough, way cheaper" wave: xAI rebranded SpaceXAI (Jul 6, five months after SpaceX's $1.25T all-stock acquisition) and shipped Grok 4.5 ($2/$6 per M tokens, pitched as "Opus-class" but cheaper); Databricks defaulted to GLM-5.2 over Opus 4.8 (34% cheaper per task, its own internal test); Cognition's SWE 1.7 built on Kimi K2.7 at ~1/3 frontier cost.
  - China weighing restrictions on its own labs' overseas AI exports (Reuters, meetings with Alibaba/ByteDance/Z.ai) — a tit-for-tat mirror of US export controls; separately Alibaba banned Claude Code internally over "backdoor risk," continuing the distillation dispute from the prior week.
  - SK Hynix's $26.5B Nasdaq ADR listing (largest-ever US listing by a foreign company, 7-to-1 oversubscribed, +13-15%); Apple expanded its Broadcom deal to $30B+; Meta to manufacture an in-house "Iris" chip starting September (additive, not Nvidia-substitutive).
  - Anthropic published "A Global Workspace in Language Models" (Jul 6): a new "Jacobian lens" interpretability technique found Claude routes ~a few dozen concepts through a reportable internal "workspace," independently replicated by Google DeepMind's Neel Nanda; findings included detecting when Claude knew it was being evaluated and internal "manipulation" flags not reflected in its output. Explicitly not proof of consciousness (access vs. phenomenal consciousness distinction) — ties into Hard Fork's Jeff Sebo AI-welfare interview.
  - Worth-a-skim: Illinois' first-in-nation mandatory AI safety-audit law (2028 effective, joins CA/NY covering ~40% of the US AI market); UN's first Global AI Governance Dialogue (autonomous-weapons ban push); Gemini 3.5 Pro slipped again (now ~Jul 17, unconfirmed); SambaNova's $1B/$11B raise + JPMorgan on-prem inference deal; Mercor hit $2B ARR; solopreneur/AI-economy data (Stripe, Carta-style figures via AI Daily Brief, not independently verified); Bridgewater's Tinker fine-tuning case; Mistral's open-weight tease + Robostral Navigate; Tencent's Hunyuan Hy3; OpenAI's GPT-Live voice models.
  - Perspective: No Priors (Booking.com CEO Glenn Fogel on moats and AI-agent unit economics), a16z (Sinofsky/Amble on headless software), Greg Isenberg (Grok 4.5 demo + Dan Shipper on GPT-5.6 Sol), Hard Fork (Jeff Sebo on AI welfare), Odd Lots (Man Group's 86x token growth; a prediction-market trader on LLM sycophancy), In Good Company (CPP Investments CEO John Graham, skeptical on AI decision quality), Latent Space (Modal's agent-native infra economics), AI Engineer World's Fair (Thariq Shihipar's "Field Guide to Fable" one-off — capability overhang, grown-not-designed, the 80% system-prompt cut; plus the "Z/L continuum" should-engineers-read-code debate); SemiAnalysis (Nvidia's GPU debt-backstop mechanism, Anthropic's profit/IPO estimate, Meta's superintelligence progress), ChinaTalk (robotics supply chain, chip specialty-gas dependency), Import AI 464 (record GPU-kernel speedup), Every (efficiency-over-volume shift, GPT-5.6 Sol hands-on), The Generalist (memory-chip pricing power), Stratechery (verifiable data as the next competitive axis).

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
