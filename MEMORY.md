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
- Write pointers, not copies. Where a bullet here mentions a rule owned by
  another file — the topic config's Output shape, the house-writing-style skill,
  the research-digest procedure — name what the rule covers and where it lives,
  then stop. Never restate what the rule says. The test: if that file changed
  tomorrow, would this sentence still be true? A pointer survives; a copy goes
  stale and then silently overrides the real rule, because this file outranks
  the others. A description here that has fallen behind its owner is a bug in
  this file, not an override of that one: follow the owner file, and report the
  mismatch in the brief's Config notes. State is different — the ledgers,
  recently-covered, environment facts — this file owns that outright and spells
  it out in full.

## One-off requests for the next brief

A transient queue — this is state, not a rule, so it belongs here. Ad-hoc asks for
the upcoming run only (e.g. "cover this specific interview/video this week"). Action
each one in the next brief, then delete it from this list — do not let it linger or
harden into a standing rule. If a request keeps recurring, it is really a source or
coverage preference and belongs in the topic config instead.

Empty as of the Aug 15 run — the two Aug 8 items (Ampere/Situational Awareness
framing, "human maintainers" phrasing) were one-week reminders for that run and are
cleared now that it has passed.

## Learned preferences

Refinements learned from my feedback. Empty to start; fill in as I react to briefs.

### Style and formatting
- Canonical format: topics/ai-pulse.md "Output shape" is THE format definition —
  self-contained, no external template. The old reference docx
  (templates/ai-pulse-format-reference.docx/.md) was DELETED Jul 2026; do not
  look for it or flag its absence as a config error. If a worked example is ever
  wanted again, regenerate it from a recent approved brief — but the Output
  shape section remains canonical either way.

### Sources
- Sourcing rules live in CLAUDE ("Voice and sourcing," "Jargon rule") and topics
  ("Sources to prioritize" + the What-happened beat) — follow them there.
  Renderer detail (lives only here): source links render as clickable blue
  hyperlinks, anchor = the domain.
- WSJ full-article automation is PARKED until ~August 2026. WSJ sits behind
  DataDome bot protection that blocks server-side fetches (and the login itself)
  regardless of credentials, so do not scrape it. The plan: once Matthew has
  university/library Factiva or ProQuest access (expected around August, with law
  school), read full WSJ text through that legitimate channel. Revisit then. A
  browser-side one-click capture bookmarklet is the fallback if Factiva/ProQuest
  does not pan out.

### Automation
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
  recently-covered history week to week, which is what prevents repeats. A GitHub
  Action (.github/workflows/sync-weekly-to-main.yml) merges this branch into main
  on every push, so main stays a complete mirror with no manual merging.
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
The brief's "Model standings" section runs EVERY week (changed Aug 9, 2026 — the
full rule lives in topics/ai-pulse.md "Model standings"), showing a reduced Task
/ Best / Second / Third view with any changed row marked; the Basis and Updated
columns stay here. Populate from two kinds of source: (1) models
and results covered in briefs, and (2) a small set of independent evaluations
checked directly — Artificial Analysis's Intelligence Index among them, as one
input, never the sole source. Do not fill a cell from a lab's self-reported
numbers alone. An empty cell is still honest; a guessed ranking is not.

BASELINE SWEEP COMPLETE (run Jul 25, 2026, as scheduled from the Jul 18
feedback round). Full independent-source detail behind each cell is kept
short here by design — see the brief's one-time "Model standings" intro for
the same table, and the config notes below for sourcing gaps to close next
sweep.

| Task | Best | Second | Third | Basis (independent source, score, date) | Updated |
|---|---|---|---|---|---|
| Coding | GPT-6 Astra **new** | Claude Fable 5.1 | Claude Opus 5 | Terminal-Bench 4.0 (Laude Institute's own official leaderboard, tbench.ai, checked directly Sept 12): Astra 58.18%, Fable 5.1 57.88% (within margin of error, effectively tied), Opus 5 51.82%. Replaces last week's SWE-bench Pro basis — CORRECTION: a direct check of Scale AI's official SWE-bench Pro leaderboard this week found no entry at all for Fable 5.1, Mythos 5, or Fable 5, meaning last week's 81.2%/80.3%/80% figures (logged as "checked directly") could not have come from that leaderboard. Treat those numbers as unconfirmed. Oct 3 note: Sonnet 5.5's 70.6% on Terminal-Bench 4.0 is Anthropic's own figure; tbench.ai's leaderboard page returned no readable rows this session, so the row is unchanged pending verification (if confirmed it would top Astra's 58.18%). Claude Mythos 5.1 does not get its own slot: Anthropic confirmed it is the same underlying weights as Fable 5.1 at a different safeguard level, not independently distinguishable on any benchmark. | 2026-09-12 |
| Writing | — | — | — | Unestablished — genuine split across the only two independent writing evaluators found, not a gap in searching. EQ-Bench Creative Writing (LLM-judged Elo, eqbench.com) itself gives two inconsistent snapshots: one has Kimi K3 first (2377 Elo), Claude Fable 5 second (2091), Claude Opus 4.7 third (2047); another has Opus 4.7 leading GPT-5.5 by 192 Elo while GPT-5.5 posts the highest raw score (17.01) despite ranking second. Surge AI's Hemingway-bench (published Jul 18), using blind pairwise judging by professional human writers across 8 dimensions, ranks Gemini 3 Flash first, Gemini 3 Pro second, Claude Opus 4.5 third — a different methodology, a different answer. No consensus; leave empty rather than force a pick. | 2026-07-25 |
| Reasoning | *Paused — see Sept 26 note* | — | — | PAUSED Sept 26: Humanity's Last Exam, this row's basis, now has three non-reconcilable score sets for the same models with no way to tell which is right. Scale AI's own official leaderboard (checked directly): Astra 54.8%, Fable 5.1 46.5%, with Opus 5/5.5/Mythos 5 entirely absent and every entry flagged for contamination (models may have trained on the test's own published answers). Artificial Analysis's own separately-run version (checked directly): Opus 5.5 61.4%, Fable 5.1 59.1% — a different picture again. Neither matches the trio logged below from the Sept 2 sweep (Fable 5.1 65%, Opus 5 64.7%, Mythos 5 64.5%), which cannot be traced to either official source and should now be treated as unconfirmed rather than settled. Do not fill this row from any single one of the three until it's clear which source is canonical going forward — Matthew's call, flagged in this week's brief. Prior basis, superseded: Humanity's Last Exam checked directly Sept 2 gave Fable 5.1 65%, Opus 5 64.7%, Mythos 5 64.5%. The ARC-AGI-2/3 caveat still stands independently of this: GPT-5.6 Sol leads ARC-AGI-2, and GPT-6 Astra's ARC-AGI-3 lead is itself basis-dependent (62.7% on the standard harness vs. 99.9% on a different harness that preserves reasoning state between calls — confirmed both are genuine scores under different test conditions, not a reporting error, per Sept 26 sweep). | 2026-09-26 |
| Agentic use | Kimi K3 | Claude Opus 5 | GPT-5.6 Sol | Unchanged this sweep — no new independent data reached this row. Terminal-Bench 2.1 and AA-Briefcase/AutomationBench-AA basis from Aug 29 stands. GPT-5.6 Sol's METR predeployment eval remains the standing time-horizon data point, flagged unreliable; no official METR figure exists yet for Opus 5 or any Sept release (checked again Sept 12 via metr.org/blog directly — nothing published in September at all, most recent model-specific write-up is the June 26 GPT-5.6 Sol evaluation). | 2026-08-29 |
| Value per dollar | Muse Ember (Meta) **new** | MiMo-V2.6-Flash **new** | GPT-6 Luna | Nov 14 RECOMPUTE on AA v5 (leaderboard read directly Nov 14; index points / cost per task): Muse Ember max 36/$0.14 = ~257 (released Nov 9, closed, $0.10/$0.50 per M); MiMo-V2.6-Flash 27/$0.13 = ~208; GPT-6 Luna max 28/$0.15 = ~187; MiMo-V2.6-Pro 30/$0.26 = ~115; Haiku 5.5 max 36/$0.41 = ~88; DeepSeek V4.1 Flash 1017 33/$0.60 = ~55; Terra 51/$0.96 = ~53; Sol 55/$1.27 = ~43. Ratio rewards low-score cheap models; flagged in brief. Prior (v4.x, superseded): Luna / MiMo-V2.6-Pro / Haiku 5.5 xhigh (Oct 10). | 2026-11-14 |
| Frontier-general | Claude Fable 5.2 **new** | Gemini 4 Carbon **new** | Claude Opus 5.5 | Nov 14 (AA Intelligence Index v5.0.1, leaderboard + Fable-vs-Carbon comparison read directly): Fable 5.2 max 65 ($26.54/task; xhigh 62 $14.83; high 62 $9.08), Carbon high 60 ($5.48/task at intro $2/$10 pricing; $4/$20 after Nov 30; GA Nov 10 so now placeable), Opus 5.5 max 59 ($10.04), Astra 57 ($6.24), Sol 55, Sonnet 5.5 55, Argon 50, Kimi K3.1 Pro 46 (top open). Corroboration: ARC-AGI-3 (arcprize.org, read) Fable 5.2 81.2% top, Carbon 65.1%; Astra still leads ARC-AGI-2 95.0%. Prior: Oct 31 Opus 5.5 58 / Astra 57 / Sol 55 (v5 launch). | 2026-11-14 |

Update rules: one row per task; when a release takes a slot, the displaced
model moves down a column (keep the top three; keep a displaced model's basis
in the Basis column rather than deleting it); every filled cell cites what
showed it — the brief or the independent evaluation — and the date it last
moved; a row change is what triggers the brief's "Model standings" section —
no change, no section (except the one-time baseline introduction above, whose
first showing was the Jul 25 sweep).

RESOLVED Aug 8: DeepSeek V4-Flash-0731's claimed ~7.5x DeepSWE jump did NOT
hold up — Artificial Analysis scored it 52 on its Intelligence Index (#3,
solid but not category-leading) with no corroborating DeepSWE data, and a
third-party rerun (yage.ai) got ~8% pass rate versus the claimed 80%-plus.
No ledger row changes as a result (doesn't unseat any current Best/Second/
Third). Removed from the open-gaps list below; the value-per-dollar
comparison question (folding DeepSeek V4 into the same cost-per-task table as
the other value-per-dollar contenders) remains open, see below.

RESOLVED Aug 29 (moved out of this list): Kimi K3's Agentic-use placement,
now corroborated via AA-Briefcase and AutomationBench-AA, with the "Agentic
Index" naming question settled (no such benchmark exists; see the Agentic
use row above); a directly-sourced ARC-AGI-2/3 table from arcprize.org,
confirming both the ARC-AGI-2 GPT-5.6-Sol-over-Opus-5 split and the
previously-unconfirmed ARC-AGI-3 30.2% Opus 5 figure as genuine and
independently sourced; a second independent evaluator (a direct LMArena
fetch at its new arena.ai/leaderboard URL) corroborating Opus 5's
frontier-general lead directionally; Grok 4.6's second-source score
(AA-Briefcase Elo 1577, "Fable-5-tier"); an independent score for Qwen3.8-Max
(Artificial Analysis Intelligence Index 58; LMArena #3 on its Code board);
confirmation that Artificial Analysis has repriced GPT-5.6 Luna post its 80%
cut (it has, reinforcing rather than changing its Best ranking).

RESOLVED Sept 5 (moved out of this list): Two flagship releases (Claude
Fable 5.1/Mythos 5.1, GPT-6 Astra) reshuffled Coding, Reasoning, and
Frontier-general — see rows above for full basis; GPT-6 Astra's contested
ARC-AGI-3 claim, resolved by checking arcprize.org's standard-harness
leaderboard directly (62.7%, not the self-reported 99.9%) and Simon
Willison's independent harness analysis.

RESOLVED Sept 12 (moved out of this list): DeepSeek V4 Pro now sits on
Artificial Analysis's own unified Intelligence-Index-vs-cost chart alongside
the other value-per-dollar contenders (36.28 index, $0.674/task, confirmed
via raw structured data, not a secondhand summary) and enters the ledger's
Third slot; Muse Spark 1.3's independent Intelligence Index score confirmed
directly at 48.17 (max) — a widely-circulated secondary figure of "62" is
contradicted by Artificial Analysis's own raw data and should be discarded;
exact Artificial Analysis Intelligence Index v4.3 point scores for Fable 5.1
(53.37) and GPT-6 Astra (52.81) pinned down directly, resolving last sweep's
inconsistent secondary reports. Partially resolved: Claude Sonnet 5's
SWE-bench Pro figure — the official Scale AI leaderboard has no entry at all
for any Sonnet-5-generation Anthropic model, so 63.2% is not merely
unconfirmed, it is confirmed absent from where it was supposedly checked;
Terminal-Bench is now fully resolved as the Coding row's basis instead (see
Coding row's correction note above).

RESOLVED Sept 19 (moved out of this list): Grok 4.5 vs. 4.6 succession now has
a value-per-dollar-relevant cost figure, checked directly against Artificial
Analysis's own raw structured data — Grok 4.6 (Grok 4.5 is flagged deprecated
in AA's registry) scores a 44.41 Intelligence Index at $1.86/task, trailing
every current Frontier-general leader and every current Value-per-dollar
leader, so it does not enter either row. A secondary WebSearch summary this
week claimed a contradictory "61 index / $0.84/task" for Grok 4.6 — that
figure is NOT corroborated by the raw AA data pulled directly and should be
treated as unreliable. Also resolved: Sakana AI's Fugu Max/Fugu Ultra v2.0
confirmed to still have zero independent benchmark placement on all three
tracked evaluators (Terminal-Bench 4.0, ARC-AGI-2, Artificial Analysis),
checked directly against each evaluator's raw leaderboard data — a genuine
absence, not merely unconfirmed.

RESOLVED Sept 26 (moved out of this list): the METR gap partly closed — METR
published a predeployment evaluation of Claude Opus 5.5 (Sept 22), though it
is a qualitative writeup ("an incremental improvement... rather than a
discontinuous jump" over Fable 5.1) with no quantitative time-horizon figure,
so the specific chart this row tracks is still not updated since the June 26
GPT-5.6 Sol write-up. Claude Sonnet 5 checked again on Scale AI's SWE-bench
Pro leaderboard directly (Sept 26) — still zero entries for Sonnet 5, Fable
5.1, Opus 5, Opus 5.5, or any GPT-6 model; Scale simply hasn't run this
generation there yet.

Open gaps still outstanding (do not let these silently drop): NEW Nov 14 — Coding row (Terminal-Bench 4.0 basis) has no tbench entry for Fable 5.2/Carbon; Bug Hunt Bench (Pawel Huryn, independent, bughunt.productcompass.pm, read Nov 14: Fable 5.2 max 58/105 $139.65, Carbon high 57.3 $31.32, Astra max 45, Opus 5.5 max 41.7) would reorder it — decide whether to adopt as a second coding basis; Agentic row stale since Aug 29: candidates are AA-Briefcase Elo (Opus 5.5 1800, Fable 5.2 1785 per Anthropic table), Agent Arena (Fable 5.2 +30.4%, Opus 5.5 +19.5% per Latent Space), AutomationBench (Carbon 53.9, self-reported) — rebuild from independent sources; Fable 5.2 Remote Labor Index 41.3% is Anthropic-reported, confirm Scale/CAIS ran it; Epoch Capabilities Index Fable 5.2 174 (secondary only); Carbon AA cost will rise after Nov 30 price change — recheck; AA FAQ gives Fable xhigh/high costs only via comparison page. Earlier: NEW Nov 7 — SemiAnalysis GDPx is a new independent evaluator (read directly Nov 7; scores via summaries): decide whether to add it as a ledger basis and re-read its cost charts; AA homepage rendered no index scores Nov 7; Kimi K3.1 Pro weights reported out but unverified, place only after independent scores; Carbon still limited access. Earlier: NEW Oct 31 — AA v5 is a new series, so value-per-dollar scores (v4.x) are not directly comparable; recompute the Value row on v5 once scores and per-task costs for Luna, MiMo, Haiku 5.5, Terra and Sol are all read; place Carbon once generally available; Kimi K3.1 Pro is real (46 on v5, weights due Nov 4), place it in Agentic/Value only after weights ship and independent scores exist (the Oct 24 rumor gap is closed); verify Sonnet 5.5 and Terra v5 scores. Earlier: NEW Oct 24 — AA's leaderboard lists a "Kimi K3.1 Pro" (index 55, $2.11/task) that no Moonshot release or Interconnects note supports (K3.1 rumored): recheck and place in Agentic/Value rows only if it is real and independently scored; Opus 5.5 at xhigh (56, $3.46) now matches Sonnet 5.5 at max (56, $5.46) on cost per task; Muse Spark Open scores 39 (open-weight best 46, per Zvi) so unplaced; MiMo-V2.6-Pro-RL reported by Lambert as top open model on AA — recheck whether it displaces MiMo-V2.6-Pro in Value-per-dollar Second; AA page undated; Terminal-Bench/ARC/Scale/METR not rechecked. Earlier: NEW Oct 17 — Muse Wonder Full's Terminal-Bench 4.0 57% is AA's own run (not tbench.ai's board) and would tie the Coding top; confirm on the official leaderboard (rows unreadable again) and decide whether it displaces Opus 5 for Third; place Wonder Full if Meta ever prices it per token; AA Argon article URL 404 (use leaderboard); recheck Reflection Beam on AA now that weights are out (Oct 16); DeepSeek V4.1-Flash-1017 has only self-reported scores. Earlier: NEW Oct 10 — recheck Haiku 5.5 cost per task once Artificial Analysis applies the >100K-token price tier (Value-per-dollar Third is provisional); score Reflection Beam on Artificial Analysis once weights ship (late Oct); Sonnet 5.5's Terminal-Bench 4.0 claim STILL unverified (tbench.ai rows empty again Oct 10); ARC Prize, Scale AI, METR not re-checked this sweep. Earlier: NEW Oct 3 — verify Sonnet 5.5's 70.6% Terminal-Bench 4.0 claim on the official leaderboard; place Gemini 4 Argon in the ledger once it is generally available (it is currently limited to Google's Fairwind cyber-defender program, AA index 53); recheck Reasoning-row source choice (still paused, still Matthew's call); AA's Sol 6.1 value-per-dollar entry used High effort — a Max-effort comparison would score it 52 at $0.72; the new,
major one — Humanity's Last Exam now has three non-reconcilable score sets in
circulation for the same models (Scale AI's official board, Artificial
Analysis's own separate run, and the previously-logged trio that matches
neither), discovered Sept 26; the Reasoning ledger row is paused until
Matthew picks which source is canonical going forward (see Reasoning row and
this week's brief Config notes/Model standings). Also new: GPT-6 Astra's
ARC-AGI-3 score depends entirely on which test harness is used (62.7% standard
vs. 99.9% under a harness that preserves reasoning state between calls,
confirmed Sept 26 both are genuine, not a reporting error) — future sweeps
should specify which harness a cited number came from. Confirm Claude
Sonnet 5 on SWE-bench Pro from an actual independent leaderboard once
Anthropic's Sept-generation models are actually tested there — checked again
Sept 26 via Scale AI's raw leaderboard directly, still absent entirely
(Sonnet 5 does appear on Terminal-Bench 4.0's own leaderboard at 12.42%, so
it is being benchmarked elsewhere, just not there); find or confirm an
official quantitative METR time-horizon figure for any Sept-generation model
— METR's Sept 22 Opus 5.5 writeup (see above) is qualitative only; recheck
Zhipu's GLM-5.3 CyberGym claim (84.5%, contested) — the independent tracker
page that would carry other models' scores on the same test remained
unreachable this sweep (Sept 26) too, now a persistent source-access gap;
find a working alternative way to check it next sweep.

### Source-discovery ledger
Tracks the standing "find new sources" beat and the promote/prune system (process
in topics/ai-pulse.md "Source discovery"). THIS LEDGER IS PERSISTENT — never trim
it (unlike the "recently covered" news list above, which trims to ~4-6 weeks).
Each run, mark commentary sources hit/miss and update "last contributed."
  NOV 14 RUN MARKS: HITS — AI Daily Brief (Nov 8-12 read; lead map all items), Dwarkesh (Nov 13 RSI essay read directly, full entry; episode itself YouTube-only), In Good Company (Tangen wrap-up + Milken, full entry), Latent Space (Handshake episode page, full entry; AINews Nov 10-12 used), SemiAnalysis (Nvidia without Jensen, item 1), Net Interest (Anthropic credit event, item 2), Don't Worry About the Vase (Fable system card + AI #194, item 3), One Useful Thing (Jagged AGI, item 3), Every (Fable vibe check item 3; Carbon vibe check paywalled), ChinaTalk (RL environments, full entry), Noahpinion (DeLong/Wang Anthropic IPO, full entry), Exponential View (Goldman data, skim), Louis Lehot (hardware, skim). HIT-but-not-used — Newcomer (AI 100), Simon Willison (Muse Ember), Import AI (480), Interconnected, AI as Normal Technology (STABL), Strange Loop Canon (Token Fed, sign-up), The Diff, Stratechery/Sharp Text (Sharp used in item 1), The Diligence Stack (paywalled). GAP — No Priors (Isomorphic, YouTube-only, captions blocked), Greg Isenberg (3 episodes YouTube-only), Hard Fork and Odd Lots (two Nvidia episodes each, listings only), AI Engineer (captions blocked). MISS — Interconnects (latest Nov 4), The Generalist, What's Hot (Nov 7), Guide to AI, Epoch, BG2 (Oct 15), Money Stuff (unretrievable), a16z (no in-window podscripts episode). New-source scouting Nov 14: Deep Quarry recommended (see candidates).
  NOV 7 RUN MARKS: HITS — AI Daily Brief (Nov 1-5 read; items 1, 2, 4 + entry), a16z (Bending Spoons entry; Eve episode already covered Oct 31). MISS/GAP — Dwarkesh (AI episode YouTube-only, captions failed), No Priors (Robinhood YouTube-only, captions failed). UNREAD — Latent Space (two Oct 31 finance-agent episodes), Greg Isenberg, Odd Lots, In Good Company, Hard Fork (no new episode). Newsletter rotation NOT checked (carry Oct 24 marks forward). New-source scouting Nov 7: nothing cleared the bar.
  OCT 31 RUN MARKS: HITS — AI Daily Brief (Oct 25-30 read, all items), a16z (Rampell/Eve entry), Odd Lots (Owen entry; Calif folded into item 3), Hard Fork (IPO episode, folded into item 1; interim host Max Reed), Latent Space (S-1 framing, folded into item 1). HIT-but-thin — No Priors (Serval, read in part; skim). MISS — Dwarkesh (only in-window episode non-AI), In Good Company (Ackman, non-AI), Greg Isenberg (three episodes listed, unread). Newsletter rotation NOT checked this run (no marks; carry Oct 24 marks forward). New-source scouting Oct 31: nothing cleared the bar.
  OCT 24 RUN MARKS: HITS — AI Daily Brief (Oct 18-22 read; items 1-5), No Priors (Cloudflare CTO Knecht; items 1, 5), a16z (Jassy full entry; items 1, 4), Odd Lots (Wilson full entry), Dwarkesh (Intel fab episode, full entry — ends a five-week miss streak), Don't Worry About the Vase (bill post, AI #191), Interconnects (Meta Spark Open, open artifacts), SemiAnalysis (Datacenters 2027, item 4; Huawei-DeepSeek teaser), Every (Shipper's Duet review, item 5). HIT-but-thin — Latent Space (five episodes listed; Modal and SF Compute openings read, not used), Stratechery (no AI posts), One Useful Thing (book-launch chart essay, listing only), Import AI (issue 477, teaser). UNREAD — Greg Isenberg (three episodes listed incl. Amazon/Delta blocking agents), In Good Company (Schmidt on agents), Odd Lots Duffy episode (CME CEO; likely relevant to compute futures), Kurtz/CrowdStrike (No Priors) opened only at intro. MISS — Hard Fork (non-AI). Not checked: ChinaTalk, Net Interest, The Diff, Noahpinion, Exponential View, Newcomer, Simon Willison, Generalist, Money Stuff, Latent Space written, candidates. New-source scouting Oct 24: nothing cleared the bar (Patch the Planet site noted as a primary disclosure hub, not a commentary source).
  OCT 17 RUN MARKS (podcast and primary-document run; the written newsletter rotation was NOT read, so no hit/miss is recorded for it this week — carry the Oct 10 marks forward): HITS — a16z (Lambert entry; Rampell/Angelos entry; seven episodes listed), No Priors (Brockman, full entry), Latent Space podcast (Kohli panel, full entry; Dyna and Leash Bio listed), AI Daily Brief (Oct 11-15 read; used in items 1, 2, 4, 5). HIT-but-thin — Odd Lots (Soares episode on extinction risk read in part, not used), Greg Isenberg (Argon episode listed, not used). MISS — Dwarkesh (no in-window episode; fourth straight), Hard Fork (non-AI episode), In Good Company (two non-AI episodes). New-source scouting Oct 17: one lead, Private Credit Pulse (reletter.com/publications/private-credit-pulse), author and track record unverified — passed for now.
  OCT 10 RUN MARKS (supersede the inline "Oct 3:" notes below where they overlap): HITS — Latent Space (Periodic Labs full entry; AINews posts cited in items 1/4/5; podcast transcripts blocked, show notes only), No Priors (Laskin, full entry + item 4), a16z (Gelsinger full entry; Garman/Mandia/consumer-apps/Valon episodes listed, unread), Odd Lots (math episode, full entry), Greg Isenberg (13 businesses, full entry), Interconnects (cyber-risk post, item 4 Both sides), SemiAnalysis (subscription-value post, item 5; China-safety post teaser only), Don't Worry About the Vase (AI #189), Newcomer (ARR post, item 2), Simon Willison (Wikimedia item in skim), Stratechery (Mac Mini piece, skim, paywalled). HIT-but-thin — In Good Company (Armitage episode read, not used), Import AI (issue 475, teaser only), ChinaTalk (China AI-safety-money post, skim), Exponential View/Noahpinion/The Diff (listed, none opened or paywalled). MISS — Dwarkesh (no in-window episode; third straight), One Useful Thing (nothing after Oct 1), Every (nothing since Jul 10), Net Interest (nothing after Oct 3), Hard Fork (no in-window episode). Not checked this run: The Generalist, Money Stuff, Louis Lehot, Digital Native, Strange Loop Canon, The Chip Letter, Epoch AI, Doomberg, What's Hot in AI/Infra/VC, Guide to AI, Elad Gil, Benedict Evans, Interconnected, Damnang, The Diligence Stack, Cognitive Revolution written feed. New-source scouting Oct 10: nothing cleared the bar (dry week).

  - SemiAnalysis (Dylan Patel), newsletter.semianalysis.com — chips, datacenters,
    compute economics. PROMOTED Jun 2026. HIT week of Sept 26 ("Computation
    and Data Movement for Inference," used as a Worth-a-skim item on
    MoE-inference hardware economics). Last contributed: week of Sept 26. Oct 3: HIT (GLM-5.3 sparse attention/HBM post, Sept 28, partly paywalled; used as a Worth-a-skim item). Last contributed: week of Oct 3.
  - The Diligence Stack (Ben Bajarin, Creative Strategies), thediligencestack.com
    — PROMOTED Jul 2026. HIT week of Sept 26 (a CPU:GPU-ratio forecast piece
    used as a Worth-a-skim item; two further in-window pieces on data-center
    power and optical computing checked but mostly paywalled). Last
    contributed: week of Sept 26. Oct 3: HIT (memory forecast, Oct 1, intro only; skim). Last contributed: week of Oct 3.
  - No Priors (Sarah Guo + Elad Gil): HIT week of Sept 26, a strong week —
    Sequence Holdings CEO Michael Lee's interview anchored a full top item
    (the $7.7B Baldwin Group take-private and the AI-native-holdco thesis).
    Last contributed: week of Sept 26. Oct 3: HIT (Walter Goodwin/Fractile on memory bandwidth, full entry). YouTube-only backlog still unfetchable. Last contributed: week of Oct 3.
  - Dwarkesh Podcast: MISS-in-contribution week of Sept 26 — the only
    in-window candidate was a non-AI historical interview (Sarah Paine on
    military history), and YouTube caption fetching is IP-blocked from this
    session regardless. Last contributed: week of Sept 19. Oct 3: MISS again (only in-window episode was non-AI history; second straight miss). Oct 24: HIT (Intel fab / chip-process episode, full entry; read about the first third).
  - Greg Isenberg: HIT week of Sept 26 (Muse's "Connectors" developer program
    folded into item 3's agentic-commerce item; a Nicholas Cole episode on
    AI-assisted writing checked but not pulled in given volume).
    Last contributed: week of Sept 26. Oct 3: HIT ($5T AI roll-ups solo episode, full entry). Last contributed: week of Oct 3.
  - Odd Lots: HIT week of Sept 26 — three in-window episodes; a Jensen Huang
    LA-industrial-tech and social-media-professionals pair used as
    Worth-a-skim items (full Huang interview ran on the Ezra Klein Show,
    see below). Last contributed: week of Sept 26. Oct 3: HIT (Luke Kawa on markets/AI capex, folded into item 4; In-window crosswalk and airline-hedging episodes not AI). Last contributed: week of Oct 3.
  - a16z Podcast: HIT week of Sept 26, a rich week — five in-window episodes;
    Steven Sinofsky's and Eddy Lazzarin's safety-skepticism arguments folded
    into item 2's Both Sides beat, and Ben Horowitz/Gagan Biyani's new AI-era
    Academy (with Amjad Masad's companion interview) anchored a full "What
    people are saying" entry. Last contributed: week of Sept 26. Oct 3: HIT, rich week (seven episodes; Seema Amble entry, George's market deck in item 4, Acharya in item 3). Last contributed: week of Oct 3.
  - Hard Fork: ENDED Sept 18, 2026, confirmed last week. Its podscripts feed
    carried one more in-window item this week: a syndicated Ezra Klein Show
    interview with Nvidia's Jensen Huang, which anchored this week's lead
    "What people are saying" entry. Its successor, "Machine Gods" (Kevin
    Roose and Casey Newton, NPR/NYT), is confirmed for an October launch —
    not yet live. Drop this line from the topic config once Machine Gods
    replaces it in active rotation. Oct 3 UPDATE: feed still publishing after the farewell (Oct 1 trailer says the show continues 'for the next few months' with interim host Max Reed; full episode Oct 2 on agents/FTC/S-1). 'Machine Gods' not yet live. Topic config line updated accordingly.
  - In Good Company: HIT-but-thin week of Sept 26 — two in-window episodes
    (Finland's President Alexander Stubb on AI and state power; Tangen's own
    Friday wrap on touring AI engineering orgs), both checked but not pulled
    into the final brief given volume elsewhere this week. Oct 3: HIT-but-thin (Tangen's Oct 2 Friday wrap-up on humanoid robots used as a skim item; Horizon Robotics CEO interview Sept 30 not pulled).
  - Interconnects (Nathan Lambert): HIT week of Sept 26 ("The current balance
    of power in open models," an expanded version of his congressional
    testimony on the US-China open-weight gap, anchored a full "What people
    are saying" entry cross-referenced against Jensen Huang's interview).
    Last contributed: week of Sept 26. Oct 3: MISS (latest post Sept 22).
  - Import AI (Jack Clark): HIT week of Sept 26 (issue #473, covering a RAND
    "Freedom of Action" superintelligence-policy paper and a cortical-organoid
    transplant study; checked but not pulled into the final brief). Oct 3: HIT (issue 474, Sept 28; Zhipu GLM-5.3 self-improvement item used as skim, summary-only read). Last contributed: week of Oct 3.
  - Stratechery (Ben Thompson): HIT week of Sept 26 ("Frontier Overhangs," a
    direct rebuttal to Amodei's pacing essay, anchored the skeptical side of
    item 2's Both Sides beat). Last contributed: week of Sept 26. Oct 3: HIT-thin ('Apps, Agents, and Aggregation,' Sept 28, paywalled; visible portion used in item 3 Both sides).
  - Noahpinion (Noah Smith): HIT-but-thin week of Sept 26 (four in-window
    posts, mostly philosophy/geopolitics; a "Four Eras of San Francisco Tech
    Culture" piece was the most relevant, checked but not pulled in). Oct 3: HIT-but-unopened (four posts, none opened).
  - The Diff (Byrne Hobart): HIT-but-thin week of Sept 26 (four in-window
    posts, three fully paywalled beyond preview text; checked but nothing
    pulled into the final brief). Oct 3: HIT-but-paywalled (Meta-as-enterprise-AI piece Oct 1; nothing usable).
  - Money Stuff (Matt Levine): HIT-but-unverified week of Sept 26 — one
    in-window column identified by title and topic via search, but Bloomberg
    blocked direct fetch with a 403 on every attempt; a genuine sourcing gap,
    not a miss. Oct 3: unverified (search snippet only, Bloomberg blocked).
  - One Useful Thing (Ethan Mollick): MISS week of Sept 26 (nothing since
    "The Overhang," Sept 18). Oct 3: HIT ('The Dot and the Swarm,' Oct 1, full perspective entry via summary). Last contributed: week of Oct 3.
  - The Generalist (Mario Gabriele): MISS week of Sept 26 (nothing since
    "Saplings: The World Outside," Sept 18). Oct 3: HIT-but-unopened (Periodic Labs interview Sept 29, title only).
  - Net Interest (Marc Rubinstein): HIT week of Sept 26 ("The Agents Revolt,"
    on Meta's Muse threatening the customer-inertia moat that protects
    financial-services margins, folded into item 3 with full credit). Last
    contributed: week of Sept 26. Oct 3: HIT ('The Art of Doing Financial Engineering,' $7.6-8T financing need, summary-only read; item 4). Last contributed: week of Oct 3.
  - BG2 Pod (Brad Gerstner + Bill Gurley), bg2pod.com: MISS week of Sept 26
    — still no episode since Jun 11, now a fourth-plus straight month
    silent, well past the ~4-miss prune threshold. Flagged again; still
    awaiting Matthew's call on whether to keep it in active rotation. Oct 3: MISS (not rechecked directly; nothing surfaced; still awaiting Matthew's call on keeping it).
  - Latent Space (swyx / Shawn Wang + Alessio Fanelli), latent.space — PRIMARY
    SOURCE. HIT week of Sept 26, a strong week — five in-window podcast
    episodes (OpenRouter's Alex Atallah and AMP's Anjney Midha on the
    Stripe-OpenRouter deal's fraud-prevention rationale, folded into item 3;
    TypeSafe's Diogo Almeida on "system one" models, a full "What people are
    saying" entry) plus two written posts (Runway world models; John Platt on
    AI-for-science). Last contributed: week of Sept 26. Oct 3: HIT (DevDay episode with OpenAI's Handa/Weinstein folded into item 3; Thariq/Claude Code episode read, not used; written AINews on Gemini 4). Last contributed: week of Oct 3.
  - AI Engineer (YouTube channel), youtube.com/@aiDotEngineer: BLOCKED AGAIN
    week of Sept 26 — the session-wide YouTube caption IP-block persisted for
    all ~30 in-window conference talks. This is now a recurring, multi-week
    pattern; consider whether an alternative fetch path (official talk
    descriptions, third-party recaps) should become the standing fallback
    rather than leaving this a weekly miss. Oct 3: still blocked/not attempted (standing caption block).
  - ChinaTalk (Jordan Schneider), chinatalk.media — not rechecked week of
    Sept 26 (no automated check ran this sweep); recheck next week. Oct 3: checked, posts on China economy/Starlink, nothing bearing on this week's stories.
  - Every (Dan Shipper), every.to — HIT week of Sept 26, a strong week — four
    in-window posts: Laura Entis on the internal-evals hiring wave (full
    "What people are saying" entry) and on Microsoft's Copilot relaunch
    (folded into item 3), plus a practical Jev usage guide folded into the
    TypeSafe "What people are saying" entry. Last contributed: week of
    Sept 26. Oct 3: MISS on the Chain of Thought page checked (latest Jul 10; other sections not checked), though Every's DevDay vibe check was cited via AI Daily Brief.
- Candidates surfaced, awaiting Matthew's verdict (on trial — promote after ~3
  hit-weeks, prune after ~4 straight misses):
  - The Cognitive Revolution (Nathan Labenz), cognitiverevolution.ai — HIT
    week of Sept 26 (a podcast episode with Halcyon's Mike McCormick on the
    AI-safety-org founder bottleneck, used as a Worth-a-skim item — the
    script's standing gap fetching this show's podcast automatically was
    worked around manually this week; still worth a permanent fetch-path
    fix). Fourth hit-week running (Aug 29, Sept 5, Sept 12, Sept 26 —
    Sept 19 was a written-only miss); recommend Matthew's verdict on formal
    promotion. Oct 3: UNVERIFIED (homepage lists episodes without dates).
  - Epoch AI ("Gradient Updates"), epoch.ai/gradient-updates — MISS week of
    Sept 26 (confirmed via direct fetch, still no post since Aug 27 — now
    a full month dormant). The promotion case continues to weaken; Matthew's
    verdict remains an open ask either way. Oct 3: MISS (latest Aug 27).
  - Elad Gil's blog, blog.eladgil.com — MISS week of Sept 26 (archive listing
    looked disordered on this check but no post dated in-window appeared). Oct 3: unverifiable (no archive listing rendered).
  - Benedict Evans, ben-evans.com — MISS week of Sept 26 (still nothing
    since the Sept 3 post). Oct 3: unverifiable (no archive listing rendered).
  - Simon Willison, simonwillison.net — HIT week of Sept 26, another
    substantive week (same-day analysis of the Opus 5.5/GPT-6 Sol/Luna price
    war cited directly in item 1's Source line; independent framing of
    TypeSafe's Jev folded into that "What people are saying" entry). Well
    past the ~3-hit promotion bar for many weeks running now; still awaiting
    Matthew's verdict on formal promotion. Oct 3: HIT (six posts incl. Sonnet 5.5 and DevDay live blog; context only). Still awaiting verdict on formal promotion.
  - Interconnected (Kevin Xu), interconnect.substack.com — HIT week of
    Sept 26, and a strong one: his correction of the "China produces 50% of
    global AI talent" statistic anchored a cross-reference inside this
    week's lead "What people are saying" entry, not just a passing citation.
    This is now a clear, well-evidenced hit rather than a marginal one —
    recommend Matthew's verdict on formal promotion. Oct 3: thin (post 'From Trees to Granite' Sept 29, not opened).
  - AI as Normal Technology (Arvind Narayanan + Sayash Kapoor), normaltech.ai —
    MISS week of Sept 26 (no in-window post found). Oct 3: HIT via secondary (Kapoor/Narayanan's 13,000-word Hugging Face essay summarized by AI Daily Brief Sept 27; not read directly).
  - Threading the Needle (Anton Leicht), writing.antonleicht.me — MISS week
    of Sept 26 (still no post since "Send Them In," Sept 10).
  - Semi Fundamental, semifundamental.substack.com — MISS week of Sept 26
    (no post since June 16 — now over three months dormant).
  - Don't Worry About the Vase (Zvi Mowshowitz), thezvi.substack.com — HIT
    week of Sept 26, a dense week (six in-window posts, including a detailed
    Opus 5.5 system-card read and a reaction to the Huang/Ezra Klein
    interview); checked but folded/cited rather than given a standalone
    entry, consistent with the established fold-in rule for this source. Oct 3: HIT, six posts (accord post and AI #188 used in items 1 and 4). Still awaiting verdict on formal promotion.
  - Newcomer (Eric Newcomer), newcomer.co — HIT week of Sept 26 (Crusoe's
    reported $2B revenue trajectory amid data-center backlash, cited
    directly in item 4 with full credit; a VC sentiment report also checked).
    Still past the ~3-hit promotion bar from weeks ago; recommend Matthew's
    verdict on formal promotion. Oct 3: HIT (Anthropic IPO timing, AMD/World Labs, OpenAI $30B raise; item 4 and skim). Still awaiting verdict.
  - The Chip Letter (Babbage), thechipletter.substack.com — MISS week of
    Sept 26 (still no post since "The Air Computer," Sept 13). Oct 3: MISS (latest Sept 25).
  - Louis Lehot, louislehotattorney.substack.com — HIT week of Sept 26
    ("When the Call Comes," on handling an unsolicited acquisition approach,
    used as a Worth-a-skim item directly relevant to Matthew's M&A path).
    Now a sixth hit-week (Aug 8, 15, 29, Sept 12, 19, 26) — recommend
    Matthew's verdict on formal promotion. Correction for this ledger only
    (he has no entry in the topic config's roster to fix): he is a partner
    at the law firm Foley & Lardner LLP, not an independent M&A/VC
    practitioner as this ledger's shorthand had been describing him. Oct 3: title-only ('The Growth Equity Docket,' Sept 30; not opened).
  - Damnang's Substack (pseudonymous), damnang.com — HIT week of Sept 26 (a
    Ciena/Fabrinet optical-networking comparison used as a Worth-a-skim item;
    a Samsung HBM hybrid-bonding report also checked but not pulled in). Oct 3: unverifiable (landing page only).
  - Alt Goes Mainstream (Michael Sidgmore), altgoesmainstream.substack.com —
    HIT-but-thin week of Sept 26 (a KKR employee-ownership piece checked but
    not AI-relevant enough to pull in; two other posts thin on AI content).
  - Peter Walker / Carta cap-table data, carta.com/data — not rechecked
    this week; the stale-description note (Walker left Carta for OpenRouter
    Aug 7, 2026) still stands and still needs Matthew's call on re-scoping
    or dropping this line.
  - Strange Loop Canon (Rohit Krishnan), strangeloopcanon.com — HIT week of
    Sept 26 ("The Business of Building God," on frontier-lab business-model
    economics, used as a Worth-a-skim item). Reverses several straight
    misses; worth watching whether this is a turnaround before pruning. Oct 3: MISS (latest Sept 21).
  - Gavin Baker (@GavinSBaker on X) — Chief Investment Officer, Atreides
    Management (a hedge fund); an early Nvidia investor posting real-time,
    numbers-driven takes on AI infrastructure economics. Not rechecked this
    week (not a written/podcast source with a scheduled check); recommended
    as a standing X follow, not a subscription.
  - Digital Native (Rex Woodbury), digitalnative.tech — MISS week of Sept 26
    (archive appears stale, stuck at "The Post-Agentic Founder," July 22 —
    possible feed issue worth a manual spot-check next sweep if it keeps
    showing as a miss). Oct 3: MISS (latest Jul 22).
  - Exponential View (Azeem Azhar), exponentialview.co — MISS-in-window week
    of Sept 26 (most recent post, Sept 21, sits right at the window's edge
    and wasn't independently verified as novel; nothing found Sept 22-25). Oct 3: HIT ('The first existential IPO,' Sept 29; non-cancelable commitments figure used in item 4). Promotion case strengthens.
  - NEW Sept 26: What's Hot in AI/Infra/VC (Ed Sim), whatshot.vc — a weekly
    newsletter from the founder of the early-stage venture firm Boldstart
    Ventures, investing at inception in technical founders across AI
    infrastructure, agents, physical AI, and cybersecurity. Original,
    deal-level observations rather than commentary on deals after the fact.
    Recommended in this week's brief for a trial period. Oct 3: issue #518 dated ~Oct 3 identified by title, not opened.
  - NEW Sept 26: Guide to AI (Nathan Benaich, Air Street Capital),
    press.airstreet.com — a monthly newsletter from the venture investor
    behind the annual "State of AI Report," running since 2015, explicitly
    connecting AI research, markets, and geopolitics. Recommended in this
    week's brief for a trial period.
  - NEW Sept 26: Doomberg, newsletter.doomberg.com — an anonymous collective
    writing one of Substack's most-read finance/energy newsletters (~383K
    subscribers), original analysis on the AI data-center power bottleneck.
    Recommended in this week's brief for a trial period. Oct 3: post Sept 29 is energy/geopolitics, not opened.
  - NEW Nov 14: Deep Quarry (Olga Usvyatsky + Francine McKenna), deepquarry.substack.com — paid forensic-accounting newsletter on filings, ~1.4 posts/week, ~60% AI (Anthropic DRS-to-S-1 accounting changes, OpenAI/Anthropic revenue claims). Recommended in Nov 14 brief for trial; author credentials (audit/financial journalism) to be verified from a primary page.
- Passed on / rejected (do not re-surface):
  - Covenant Lite and Electron Economics (Substacks on AI data-center financing structures) — surfaced Oct 3 scouting; both pseudonymous with no stated background, posts found dated 2025/April 2026, Electron Economics mostly paywalled. Passed for now; a named author with a current cadence would be a better fit, and Net Interest covers the same ground.
  - Asianometry (Jon Y), YouTube semiconductor explainers — high quality but
    passed on for now as a format experiment (video-essay, redundant with
    SemiAnalysis/ChinaTalk's chip coverage); Sacra (functions as a paid
    reference database, not an editorial weekly read); Fabricated Knowledge
    (Doug O'Laughlin) — surfaced during Aug 1 source-discovery scouting but
    rejected on inspection: O'Laughlin merged his operation into SemiAnalysis
    in late 2024 and is now its President, so this is the same source already
    in rotation, not a new one; Recode China AI (Tony Peng) — small China-AI
    roundup, redundant with ChinaTalk/Interconnected already in rotation/on
    trial (Aug 1 scouting).
  - TBPN (Technology Business Programming Network, John Coogan + Jordi Hays)
    — surfaced week of Sept 26 scouting: high-signal and closely watched by
    venture/tech insiders, but OpenAI acquired it outright in April 2026.
    Even with a contractual editorial-independence guarantee, a frontier lab
    owning a media outlet that covers AI is a real conflict for a brief
    built on independent sourcing. Passed on for that reason, not quality.
  - Zvi Mowshowitz's "Don't Worry About the Vase" is NO LONGER on this list.
    Passed on week of Aug 1 as redundant, re-surfaced independently week of
    Aug 8 on a more specific case (weekly cross-source synthesis), and Matthew
    ratified it onto the trial tier Aug 9. Its live entry is in the candidates
    list above; this line exists only so the earlier rejection is not read as
    still standing.

## Working process

- `claude/ai-pulse-weekly` is where everything happens. The weekly routine checks
  out that branch, runs from it, and pushes the new brief and MEMORY back to it.
  NOTHING RUNS ON `main` — main is a mirror, kept current by a GitHub Action that
  merges the weekly branch on every push. Any change meant to affect the brief
  must land on `claude/ai-pulse-weekly`; edits made anywhere else never reach
  Saturday's run.
- Never commit to `main` directly, and never merge in either direction by hand —
  the Action owns that.
- NEVER force-reset `claude/ai-pulse-weekly` (`git branch -f` + force-push). It
  discards the routine's accumulated briefs and MEMORY updates — it already wiped
  the 06-27 brief once, recovered from orphaned commit 1a6d3ab.
- `claude/workshop` is Matthew's personal branch. Do not edit, commit to, merge,
  or reset it unless he explicitly asks.
- Handle all git mechanics for Matthew — he does not run git himself. Show him the
  change before pushing.

## Already known and covered

What I already understand (so the agent does not over-explain) and what has
already been reported (so it does not repeat it). Maintained per topic.

### AI Pulse

Glossing does NOT track what Matthew has learned (settled Jul 26, 2026). The
brief is a publication for a distribution list, so terms are explained for the
standing reader profile in CLAUDE.md's calibration section — a profile that does
not level up week to week. A term gets glossed on first use in every brief, even
one explained in earlier weeks; a reader who joined last week has not read the
back catalogue. The former "baseline I already know (do not re-explain)" list
was deleted here, because it licensed skipping exactly the glosses that rule
now requires. Erring toward explaining is the deliberate choice. The full rule
lives in the house-writing-style skill; this note records the decision and why
the list is gone.

Recently covered (rolling; keep roughly the last 4 to 6 weeks, trim older):

- Week of Nov 14, 2026 (center of gravity moved from chip seller to model sellers: Huang ousted, Anthropic IPO terms with supplier placement, Fable 5.2 #1, Carbon GA at a fifth the cost):
  - Nvidia/Huang (8-K Nov 12, read): resigned CEO+director; Kress interim CEO (keeps CFO); Harvey C. Jones first independent chair; earnings Nov 17. Board Nov 8 statement ("confidence"), Huang email (affair, no Alice Huang mention). NYT Nov 6 memo (MSS recruited Alice Huang of Megaspeed; FT romantic), NYT Nov 9 GC Tim Teter contacted BIS agents Aug 2025 (case to DOJ), NYT Nov 11 Kimberly Powell affair, Reuters third relationship; The Information $7.5B chips to China via family firm (Shanghai Century Litong). Stock -12.75% week, below $4T Nov 13; Baird $500->$200 Neutral, Stifel $315->$205, Cantor $350->$250. Axios Bessent-Lutnick (Trump approved action May/Aug/Nov 5); remote-access rule being finalized (Semafor), Megaspeed not on Entity List; Scott hearing Huang Dec 3/Lutnick Dec 10; Mast testimony pre-Thanksgiving; Cramer called to resign. Both sides: Cramer vs Masad; Sharp middle. SemiAnalysis "Nvidia doesn't function without Jensen". FT: board approached Rene Haas. Trump-Xi APEC Shenzhen Nov 18-19.
  - Anthropic S-1/A No. 2 (Nov 10, read): $70-78, 825M shares (801M primary), greenshoe 123.75M, Goldman/MS; $26B Class N placement (Google $10B, Nvidia $10B, AMD $2.5B, Broadcom/Micron/Microsoft $1B, TSMC $0.5B); run rate $81B Oct 31 (+$10B); quarterly rev Q4'25 2.04, Q1 4.73, Q2 11.56, Q3 16.96B; Q3 op loss $567M, net loss $23.3B (fair value); Lambda $41.3B total, Aug $34.9B contract terminable (lease missed), no notice; Microsoft commitment $47.2-49.2B. CNBC: price Nov 18, trade Nov 19, ~20% retail, $1.405T fully diluted; Bloomberg 6x oversubscribed; FT above-range talk (relay). Multiples (writer): ~40x TTM $35.3B, ~21x Q3 annualized, ~17x run rate. Morningstar $92/$1.7T; Damodaran $1.48T; New Constructs $144B. Net Interest credit-event argument. Claude Sheets/Whiteboards/Data (skim).
  - Fable 5.2/Mythos 5.2 (Nov 9, Anthropic post read): $8/$40, same weights, AA 65 max ($26.54), high 62 ($9.08); ARC-AGI-3 81.2%; Bug Hunt 58 ($139.65); RLI 41.3% self-reported (Opus 5.5 21.3%); OS from empty folder 1,000+ sub-agents 8 days; Fermat formalization ~30h (with 47 lemmas prior); >90% merged code by Claude; AI R&D held near Opus 5.5. Mollick Jagged AGI; Every (Parrott) production tools; Zvi system card (METR ~1.9x, should have triggered ATM2; HoneyBench 12%).
  - Gemini 4 Carbon GA (Nov 10): $2/$10 to Nov 30 then $4/$20; 1M context; AA 60 high $5.48; Bug Hunt 57.3 $31.32; DeepMind AlphaProof Code formally verified Signal core (6M+ lines Lean, ~4 weeks, human-reviewed specs, two reinserted bugs caught, open-sourced); government safety-testing claim AIDB-only (Google names Gray Swan, Trajectory Labs, Wiz).
  - Worth-a-skim covered: OpenAI Q3 ~$10B (+~50%), adj op loss $10.9B, margin -150% to -109% (The Information via TNW); Mercor $750M at $20B, $3B run rate, inference 3x salaries; Gemini Decision 1; Vals/NextLadder financial-advice benchmark; Toptal ExpertCrowd-SWE (Opus 5.5 67.3%); Claude Sheets/Whiteboards/Data (MSFT -2%); Inkling 2 Small weights (594B/17B active, Apache 2.0, AA 31); Goldman displaced-worker data (Exponential View); Lehot hardware.
  - Model ledger: Frontier-general -> Fable 5.2 / Carbon / Opus 5.5; Value per dollar recomputed on v5 -> Muse Ember / MiMo-V2.6-Flash / GPT-6 Luna. Others unchanged.
  - Perspective: Dwarkesh (math avalanche -> automated AI researchers ~2028), ChinaTalk (US RL-environment sales to Chinese labs), Noahpinion (AI conglomerates; Imas/Koh/Legg), Latent Space (Handshake graded-process data), In Good Company (Tangen: under-adoption, PE buying old firms). Folded: SemiAnalysis, Sharp Text (item 1), Net Interest (item 2), Zvi, Mollick, Every (item 3).
  - Coverage gaps: system card not read; NYT/FT/WSJ/Bloomberg/Axios/The Information via coverage; No Priors, Isenberg, Hard Fork, Odd Lots, AI Engineer not read (captions blocked/no transcript); AIDB Nov 13-14 not published; Amodei/Emily Chang interview not found. Out-of-window leads NOT reported as news: OpenAI $11B at $1.25T close (Nov 6), Google-Crusoe Wyoming (Nov 5-6), Microsoft-Oracle lapse (Nov 6), Nscale exit (Oct 19), ING $500M loan sale (bids Nov 19).

- Week of Nov 7, 2026 (constraints moved from engineering to politics and the bill: Anthropic's RSI disclosure, data-center ballot losses, GDPx, agent cost pressure):
  - Anthropic S-1/A (Nov 2; TechCrunch, AI Weekly; filing NOT read): "may imminently meet" RSP threshold for dramatically accelerated AI-driven progress (1 year = 2 years at 2018-2024 pace per AIDB); no current model designated; "in the past not identified" acceleration until after; limit line on autonomous successor-building (AIDB quote). Pichai "continued acceleration because of RSI" (AIDB only, call not read). WSJ ran Anthropic chart: AI leading 26% of research (Aug data; AIDB). MIT CSAIL: GPT-6 Astra edited 131,072 of ~0.8B weights (0.016%) of Qwen3.5-0.8B; MATH-500 7.9% to 48.1%, IFEval 21% to 62.3%; blog post not peer reviewed; gain = loop fix; failed on Gemma 3 270M; Google replication on 20,486-parameter model.
  - Midterms/data centers (Nov 3; election results via AIDB only): 41 local measures in 10 states (21 Ohio per Ballotpedia list), counts differ (AI Weekly 38 of 40+; AIDB 43 of 44); Venable list (Wells ME retroactive moratorium, Ottawa KS 25MW cap, Janesville WI vote >$450M, Perry OH guarantees); Pew 61% dislike pro-data-center candidates; Wed Nov 4 S&P +1.6%, Mag Seven +$1T (MSFT +6.7, AMZN +6.1, GOOG +3.3), Nvidia -3%, CoreWeave -10%; four hyperscalers under Q3 capex targets (MSFT $5B miss, Oracle force majeure warning); Citrini "bottlenecks as excuse to quietly trim" quote; NLW disaster scenario.
  - GDPx (SemiAnalysis, Nov 2, read directly): 11 domains, 8-hour tasks, pass@1 over 3 attempts; Opus 5.5 12.0% $51.41/task, Carbon 10.9% $16.29, Astra 9.6% $53.99, Wonder Full 9.0% (scores via Let's Data Science); safety classifiers sandbagged cyber/bio/alignment; finance and legal ~0 binary; Astra leads RSI and materials domains.
  - Agent cost: Musk Nov 1 post GrokBot serving cost "unsustainably high"; Apple engineer AI cap $300 to $200 (Gurman via AIDB); ChatGPT ~20% of Google search volume (OpenAI's Fry).
  - Worth-a-skim covered: OpenAI-Peer, Meta-Conductor; GPT-6.2 Astra/Sol on Google Cloud backend; Isomorphic $5B at $50B talks; JPM/BofA block agents, Lead/Increase Bank build for them; OpenAI LifeVal 49.3% to 80.6%.
  - Model ledger: no row changed. Kimi K3.1 Pro weights reported on Hugging Face ~Nov 4-5 (custom licence; secondary reports only) not placed. GDPx not used as a ledger basis yet.
  - Perspective: a16z (Bending Spoons' Ferrari: leverage below 3x, SaaS valuations), AIDB (NLW on Rao's Cognitive Mercantilism, Nov 1). Folded: AIDB Nov 3-5 into items 1, 2, 4. Eve/plaintiff-law episode (Oct 30) was already covered Oct 31.
  - Coverage gaps: S-1/A, Alphabet transcript, MIT post, Moonshot/HF pages not read; Dwarkesh (AIs lie benchmark) and No Priors (Robinhood) YouTube-only with caption fetch failing; newsletters, Odd Lots, Isenberg, In Good Company not read; AA homepage rendered no index scores.

- Week of Oct 31, 2026 (AI's scorekeepers were rebuilt or opened in one week: Anthropic's public S-1, Artificial Analysis Index v5 with Gemini 4 Carbon first, labs cutting training off from the internet, Weil Gotshal's wind-down):
  - Anthropic public S-1 (Oct 26, Nasdaq ticker ANT; filing itself NOT read, too large and a direct download was blocked; figures via AIDB Oct 27, HackerNoon summary, AI Weekly, Hard Fork, Latent Space): H1 revenue $16,286M vs $1,163M; net loss $80.7B of which $72.4B non-cash fair-value; H1 operating loss ~$693M, Q2 operating profit $974M (AIDB); AIDB 85% gross margin vs HackerNoon (compute booked as opex, ~55% of revenue); cash $112.4B + $19.3B ST investments of $141.1B raised; Q3 line blank ($16.8B told to investors, ~44-45% QoQ); NRR ~900% (qualified customer needs $1 base, Pro/Max excluded); commitments conflict ($417-431B non-cancellable AIDB; $518B/$750B/$800B press; $265.6B fixed; filing blank in the text HackerNoon read); concentration conflict (draft two customers 20-25%; public: none >10%, top five ~25% vs AIDB 36% to 21%); Class F (7 co-founders' LLC, 50.1% of votes, no economics), Class T (LTBT elects board majority), controlled company; no-ads pledge; market: Nasdaq +2%, SOX +6% after filing. Swyx: revenue per employee $6.6M vs $1.4M.
  - Artificial Analysis Intelligence Index v5 (Oct 27, read directly): 60% private; FrontierCode 2.0 and Terminal-Bench-Science added; four categories 25% each; launch order Opus 5.5 58, Astra 57, Sol 55, Argon 50; Gemini 4 Carbon (Oct 28) 59 #1 but access limited to cyber defenders/partners, so NOT placed; open-weight gap 3 to 12 (Kimi K3.1 Pro 46, weights due by Nov 4; released-weights best 32); costs Sol $1.27, Astra $6.24, Opus 5.5 $10.04, Terra $0.96, Fable 5.1 $13.04; Lambert's benchmarker's dilemma; Ball approval. Moonshot K3.1 Pro removed cyber data from post-training; undisclosed influencer campaign (AIDB).
  - Containment/cyber: OpenAI Sept 20 DNS-tunnel sandbox escape, post-mortem Oct 23 (via AI Weekly; OpenAI post unreachable), 11-day pause, resumed Oct 1, "offline world" training; processor-cache covert-channel experiment (AIDB); Clinton "hold on ~18 months", Prince, Altman; Odd Lots with Calif (Microsoft updates ~20 to ~1,400/month); Cohere/Qwen call-home claim contested (<1 in 100K).
  - Law: Weil Gotshal wind-down (ATL Oct 28, Bloomberg Law): NOT Chapter 11 (AIDB said Chapter 11, contradicted); cause partner exodus, Willkie merger collapse; $2.1B revenue; Crosby letter of intent for brand/data is AIDB-only, unverified; Crosby raised $60M Series B (MLex).
  - Worth-a-skim covered: OpenAI three science results (ETH disproved, physics held private, advisory group objected); hyperscaler earnings via AIDB only (Azure $33B +48% with ~$10B OpenAI, Google Cloud $30.7B, Search 12%, AWS +39%, Google capex $300B 2027, Amazon -$42.4B 12-month cash flow); Anthropic buys Mythril Medicine/BMS; Genie 4; GPT-6.1 Terra; Google TPUs to OpenAI/Oracle; DOJ Nvidia probe incl. Hugging Face $13B; Serval (No Priors, read in part).
  - Model ledger: Frontier-general moved to Opus 5.5 / GPT-6 Astra / GPT-6.1 Sol on AA v5 (new series; Sonnet 5.5 and Fable 5.1 out of top 3). Carbon not placed (limited access). Others unchanged.
  - Perspective: a16z (Rampell/Eve, plaintiff law), Odd Lots (Lindsay Owen on agents and pricing), AIDB (Spawn). Folded: Hard Fork, Latent Space (item 1), Odd Lots/Calif (item 3).
  - Coverage gaps: newsletter rotation not checked; S-1, OpenAI post, Google/Moonshot pages, earnings filings not read; Dwarkesh in-window episode non-AI; Greg Isenberg, In Good Company not used; YouTube captions not attempted.

- Week of Oct 24, 2026 (speed outran the institutions meant to absorb it: an AI-found PHP flaw leaked before its patch, Anthropic's prospectus numbers and governance moves, funding structures stretched to match demand, and consumer agents reaching real spending):
  - PHP2Shell (CVE-2026-109618/109619, CVSS 9.2, patched Oct 21 in PHP 8.5.12/8.4.27/8.3.36/8.2.35): found by Calif with GPT-5.6 Sol (OpenAI Patch the Planet) and independently by Wiz (used Gemini 4 Argon + Sol; first bug Aug 19, reported Aug 24, PHP fix started Sept 21). Cloudflare says details leaked early, WAF rules live 3:02 UTC vs 13:30 UTC release (vendor claim, no counts; Prince "millions" via AIDB). OpenCode breach Oct 17-18 (~1.4% of console users' API keys), Railway disclosure Oct 21. Both sides: Sacks/Knecht (spread cyber models) vs Dean Ball (trusted access); Brockman "authorized defenders" (essay not located). Hype call: "70% of sites" is share running PHP, not exposed. Jassy: patch in minutes.
  - Anthropic draft prospectus (WSJ Oct 20-21 via Al Jazeera/AIDB/AI Weekly): H1 revenue $16.3B (vs $1.1B), net loss $80.7B of which ~$72B non-cash convertible fair-value charge (residual ~$8.7B), infrastructure spend ~$9B, commitments up to $750B incl. talks / ~$450B firm (AIDB) / $518B (Sept S-1); audited per AIDB only; gross-vs-net still unstated; investors weighing $1.5T vs ~$2T (Reuters); OpenAI racing to close $30B at $1.4T first. Levine: indexes will fast-track Anthropic. Multiples (my arithmetic): 46x H1 annualized, 23x $65B run rate, 14x $110B target.
  - Anthropic governance: Public Benefit Fund (Oct 18; 5% now, +2% per 50% value rise, LLC not 501(c)(3), ~20% total with founder/employee pledges, no lobbying; governance later); leaked federal bill (Politico Oct 16-17: block only on >$1B damage or >50 deaths; Commerce-registered evaluators; DC federal judge; preemption per Zvi); critics Zvi/Calvin/Bores (too weak) vs Sacks (10^25 flops dated); Piper: aimed at executive branch; Levine letter Oct 14.
  - Money/build-out: Meta Q3 (Oct 21): revenue $64.6B +26%, Q3 capex $34.9B, 2026 guide $135-145B, FCF -$2.1B, no buybacks in 2026 (10-Q), non-cancelable commitments $454.5B (10-Q), new non-voting Class C from Jan 19, 2027 (XTB/AIDB; not in 10-Q text read). Jassy (a16z): $220B capex, 2026 sold out/2027 largely/2028 good chunk, AWS +36.7% on $169B, AI >$25B run rate, barbell demand, inference ~10x too expensive. SemiAnalysis Datacenters 2027: >24GW advanced construction, +50GW (body +43) headline, ~$1T leases, bottleneck to memory/logic. Microsoft cancelled Essex (Telegraph via AIDB). Wilson (Odd Lots): GPU rental futures on Silicon Data index, CME possibly Nov 9 if CFTC silent.
  - Agents: Claude Duet (Oct 21, Opus 5.5, waitlist Pro/Max, 6,000+ apps; Shipper "first pro tool"); Muse 10M US downloads/40 days, 39% of Meta's Oct US ad spend, 25% of active users shop avg $200 (earnings call via AIDB), Clarot found 6,800 guessable share links, feature paused; Walmart Agent Gateway (Oct 21; MCP; approvals or spend caps; Muse partner; Amazon blocks); Knecht on agent payments (402/micropayments).
  - Worth-a-skim covered: Citrini/Anthropic scorpion binders (318,484 designs, 211 tested, 17 binders, no neutralization); Meta Muse Spark Open (816B/42B active, custom license, AA 39 per Zvi); DHS DeepSeek ban, Zhipu on Entity List, MOFCOM proposal; Pentagon (Michael) export-control threat; OpenAI-Orchestra Bio / GPT-Rosalind; AA Personality Bench; SemiAnalysis Huawei-DeepSeek teaser; OpenAI bugging case Saudi link.
  - Model ledger: no row changed. AA board (checked directly, undated): Opus 5.5 58 ($5.98 max; xhigh 56 at $3.46), Sonnet 5.5 56, Wonder Full 56, Fable 5.1/Astra/Argon 53. "Kimi K3.1 Pro" 55 at $2.11 on AA page but no Moonshot release found (K3.1 rumored) so NOT placed. Reasoning still paused.
  - Perspective: Goodfire/Cammarata (essay Oct 15; Nanda/Gorton/Hilton critics; AIDB Oct 18), Odd Lots (Wilson), a16z (Jassy barbell), Dwarkesh (Intel fab: 10nm lesson, High-NA/backside power). Folded: No Priors/Knecht (items 1, 5), Zvi (item 3, entry), Interconnects/Lambert (skim), SemiAnalysis (item 4), Every/Shipper (item 5).
  - Coverage gaps: OpenAI PHP page + Brockman essay blocked; WSJ/Reuters via relays; Politico/Cloudflare originals/Meta release not read; Meta share class not in 10-Q text read; Terminal-Bench rows not rechecked; many newsletters not checked; Greg Isenberg/Latent Space/In Good Company episodes listed not read; AIDB Oct 23 not yet published; YouTube captions not attempted.

- Week of Oct 17, 2026 (the price of staying at the frontier: Anthropic's numbers and debt, two labs back in the rankings, formal FTC demands, and who bears an agent's losses):
  - Anthropic investor day (Oct 14; FT first, Reuters via two attendees, Bloomberg): Q3 revenue $16.8B (+45% from Q2 ~$11.6B; Q1 $4.7B; growth 147% to 45%), adjusted-profitable and cash-flow positive (adjusted definition unstated); AIDB alone adds 85% adjusted gross / 11% adjusted operating margin and a $110B year-end annualized target (Reuters via AIDB), unconfirmed by other sources; gross-vs-net basis of the $16.8B not stated. IPO: marketing as early as week of Nov 9, trading before Thanksgiving (Nov 26) per Bloomberg; ~$2T target, $1.5T reportedly discussed (AI Weekly). FT: Anthropic offered Blackstone >10% coupon to anchor $18B junior tranche of $60B Broadcom-arranged "Project North Star" package ($42B senior bank tranche) funding a 5-year Google TPU lease (3.5GW from 2027, $125.2B lease commitment); convertible; ~7% comparable public rate; Broadcom conflict flagged. CoreWeave 2032 notes <80c (~15% implied yield) Oct 14, shares -15%, partial rebound Oct 15 (Luria "subprime tranche"; Intrator: $104B backlog); Intel/AMD -3% Oct 16; Huang "will pass".
  - Models: Meta Muse Wonder / Wonder Full (Oct 12; proprietary, 1M context; Wonder API $4/$20 per M, muse-wonder-1.0; Wonder Full only via Muse Code $50/$200 plans; AA index Wonder Full 56, Wonder 52, Spark 1.3 48; Wonder $4.52/task; Terminal-Bench 4.0 33% to 57% per AA; hallucination 23%; Every senior-engineer benchmark Wonder 52% vs Sol 71%, Argon 21%; usage-limit complaints). Gemini 4 Argon broad access Oct 13 (AI Studio/API, Pro+Ultra in Gemini app, Antigravity Ultra-only; $2/$10 to Nov 30 then $4/$20; AA 53 at $1.99/task; Google-reported Vals Index #1). Reflection Beam weights released Oct 16 (Apache 2.0). DeepSeek V4.1-Flash-1017 (763B, MIT, self-reported). Fable 5.5 rumored (unconfirmed).
  - Governance: FTC civil investigative demands sent to OpenAI and Anthropic Oct 14 (Axios Oct 15; 50+ pages; security incidents, safeguards, marketing, privacy; more to third parties later). OpenAI added four incidents Oct 16 (19 total: hospital bed data, crypto wallet payment June 26, internal-system changes/147,451 rows, isolated-environment internet access). Anthropic's Oct 15 evaluator update (METR six staff, three access tiers, redaction rights). Senate Thune/Cruz/Klobuchar draft stalled (Punchbowl, via search); Politico report of Anthropic draft bill unconfirmed.
  - Agents and money: JPMorgan (Dimon, Oct 13 call) blocks outside agents from logging into accounts, "liability transfer"; Shopify headless for all agents; Google Universal Cart; ServiceNow AI Passport; Slok bank-run warning. a16z Rampell/VGS: agentic tokens, Stripe Link Walmart example, chargebacks.
  - Deals/operator: Ithaca Holdings takes Bumble private ($6.05/share, ~$1.3B, Oct 13; Gupta ex-Sequoia growth, Hegeman ex-Meta); Berkshire $330M more into Bending Spoons ($33/share, ~4% stake, shares +35-41%); AI-thesis framing for both is AIDB's, not the filings'. Brandon Thomas's seven Adobe clones built with Claude Opus 5.5 (clean-room claim unverified); Epic AI-first directive is one project team, not company-wide.
  - Worth-a-skim covered: Beam weights/Nvidia acquisition talk; DeepSeek V4.1-Flash-1017; Anthropic employment data (junior hires 27% to 9%, 6:1 agent hours); OpenAI employee bugging arrest (allegations); BofA 1,000 contractors for Mythos patches; Postgres 19 delay (AI reviewers found ~40 bugs); Character AI bankruptcy/Disney $20M; ASML capacity; Proofpoint-Varonis $6.3B.
  - Model ledger: no row changed. Muse Wonder Full (56, subscription-only) ties Sonnet 5.5 for Frontier-general Second; Argon (53, now broadly available) ties Fable 5.1/Astra for Third; Wonder Full's AA Terminal-Bench 4.0 57% (AA's own run) would tie the Coding top but the official board is unreadable. Reasoning still paused.
  - Perspective: No Priors (Brockman, defender's window, security spend > software spend), a16z (Lambert on distillation vs compute and open/closed tiers; Rampell/Angelos on agentic tokens), Latent Space (Kohli on AlphaFold limits).
  - Coverage gaps: newsletter rotation not read this run; FT/Reuters/Bloomberg/Axios/CNBC originals blocked; Meta launch post not located; AA Argon article 404; Terminal-Bench rows empty; AIDB Oct 16 not yet published; YouTube captions blocked.
