# Ratified changes — feedback round on the July 11–18, 2026 brief

Source doc: [ai-pulse-2026-07-18-feedback.docx](ai-pulse-2026-07-18-feedback.docx)
(41 comments). Ratified Jul 20, 2026. Applied in commit `0ceec20`.

Audited against the **July 18–25, 2026 brief** on Jul 25, 2026 — the first brief
produced after these changes landed.

**Result: 12 of 15 applied, 1 failed, 2 partially applied.**

| # | Change | File | Observable check in the next brief | Result |
|---|---|---|---|---|
| D1a | Inline bracketed source tags after each claim-cluster | topics | `[Source]` tags appear inline in item bodies | **Applied** — e.g. `[OpenAI; Hugging Face]`, `[CNBC]` throughout the top developments |
| D2 | Model standings as Best / Second / Third + value-per-dollar row; one-time baseline sweep | topics + MEMORY | Standings table has three ranked columns and a value-per-dollar row | **Applied** — sweep ran Jul 25, full table published |
| D3 | Ledger populated from brief coverage **plus** independent evaluations, Artificial Analysis as one input among several | MEMORY | Basis column cites more than one independent evaluator | **Applied** — cites AA, Epoch, SWE-bench Pro, METR, Terminal-Bench, EQ-Bench, Surge |
| D4 | "Does it hold up?" label names its object | topics | No bare generic label | **Applied** — "Does the 'isolated incident' framing hold up?" |
| D5 | Three-layer perspective entries (claim-style header → credential sub-header → two beats) | topics | Every "What people are saying" entry has a claim-style header with the credential on its own line beneath | **FAILED** — every entry used the superseded two-layer form. Cause: a stale copy of the old format survived in MEMORY, which outranks the topic config, so the routine built the section from the old spec. Fixed Jul 25 (`f1146af`) by deleting the stale copy and adding MEMORY's "write pointers, not copies" rule |
| E1 | Rebuild every causal claim and relayed argument step by step | research-digest §7 | No asserted conclusions with the middle steps missing | **Applied** (qualitative) — chains in items 1–3 walk each step |
| E2a | A gloss must differentiate, not categorize | house-writing-style §3 | Company glosses say what the company sells and to whom | **Applied** (qualitative) |
| E2b | Benchmarks **and indexes/rankings** glossed, including who measures | topics | Every benchmark or index named is explained in plain words | **Applied** — e.g. "a benchmark called 'Exploit Gym,' which measures a model's ability to find and use software security flaws" |
| E3 | Credentials on everyone, including podcast hosts and guests | research-digest | No bare names in perspective entries | **Applied** — e.g. "Mark Gurman, Managing Editor of Consumer Tech, Bloomberg"; "Boris Cherny, head of Claude Code at Anthropic" |
| E4 | A named source is a linked source, including the specific transcript or post read | research-digest | Named documents/episodes carry hyperlinks, in every section | **PARTIAL** — top developments and Worth-a-skim link correctly, but the entire "What people are saying" section contains **zero** hyperlinks; episodes are cited by name and date only. This is the clause added specifically from comment 25 ("R we able to link the transcripts in the source below") |
| R1 | One idea per sentence; commas are not glue | house-writing-style §8 + research-digest §7 | No sentence stacking a second idea off a comma tail | **PARTIAL** — 83 of 199 sentences carry three or more commas, and the longest runs 130 words. Shorter than the Jul 18 brief in places, but the split pass plainly did not bind. Worst offenders sit in "What people are saying" (110w, 96w) |
| R2 | Name the thing — no stand-in words at the verdict | house-writing-style §9 | Conclusion sentences carry concrete load-bearing words | **Applied** (qualitative) |
| R3 | Intro opens on the week's theme, then the examples | topics | First sentence is the through-line, not the lead story | **Applied** — "This week, the industry's own worst-case warnings started showing up as news rather than research papers." |
| R4 | Quotes woven in with attribution; never a bare "Quotable:" label | topics | Zero occurrences of "Quotable" | **Applied** — 0 occurrences |
| R5 | One entry per topic, not per source | topics | A source contributing two unrelated topics gets two entries | **Applied** — Odd Lots ×2, Greg Isenberg ×2 |

## Diagnosis

All three misses land in the same section. D5 failed outright there, E4's
transcript-linking clause failed there and nowhere else, and R1's worst
sentences are there too. The most likely single cause is the one already
confirmed for D5: MEMORY's stale description of "What people are saying" was
the operative spec for that section, so the section was built from the old
note and the newly ratified rules that touched it were never brought to bear.
One stale copy suppressed three changes, not one.

The stale copy is gone (`f1146af`), so the next brief is the real test of
whether E4 and R1 bind there. Both carry forward to the next round's audit.

## Deferred from this round (not ratified, recorded so they stay findable)

O1 TSMC concentration risk; O2 safety-index ranking; O3 NYT-sanctions
re-explain; O4 Apple chip-deal motive; C1 Lambert roster credential; C2 add
Xu / Sheehan / Chow to the roster; P1 harvest the praised Anthropic-IPO
sentences as a rule example; P2 "confirmed working" line for the What
happened → Does it hold up pairing.
