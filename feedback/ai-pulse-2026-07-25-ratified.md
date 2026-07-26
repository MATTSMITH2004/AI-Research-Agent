# Ratified changes — feedback round on the July 18–25, 2026 brief

Source doc: [ai-pulse-2026-07-25-feedback.docx](ai-pulse-2026-07-25-feedback.docx)
(44 comments). Ratified Jul 26, 2026.

Audit target: the **week of Aug 1, 2026 brief** — the first produced after these
changes land. Results below to be filled by the next round's Step 0.

Standing rule from this round (F7): an item may be marked **applied** only on
mechanical evidence — a grep, a count, a named line quoted from the brief.
Anything without a mechanical check is marked **unverified**, never applied.

| # | Change | File | Observable check in the next brief | Result |
|---|---|---|---|---|
| D1 | Combined overall top-5, as two lists (best regardless of cost / best per dollar), added below the unchanged per-task table | topics | Model standings contains both lists, five entries each, and the per-task table is still present | |
| D2 | Name how many independent evaluators fed the standings, and which | topics | A closing line under the standings names the count and the evaluators | |
| D3 | Empty cells carry a stated reason | topics | No empty standings cell without an explanation in that closing line | |
| D4 | AI Daily Brief gets a full entry only when NLW makes a substantive argument; cite it on the Source line wherever it surfaced a lead | topics | Any ADB entry carries an NLW argument, not a recap; ADB appears on Source lines of items it surfaced | |
| D5 | One entry per argument, not per source; a source arguing one side of a "Both sides" beat belongs inside the item | topics | No perspective entry restates a top development without adding a separable argument | |
| F1 | Glossary roster in the topic config + mechanical gloss check | topics + script | `check_prose.py` reports 0 unglossed terms | |
| F2 | A sentence asserting a mechanism is followed by the mechanism in plain words | house-writing-style §1 | No "creates/leads to/risks/favors" sentence followed by a topic change (qualitative — mark unverified if not mechanically checkable) | |
| F3 | Every named source on a Source line carries its own hyperlink | topics + script | `check_prose.py` reports 0 unlinked Source lines | |
| F4 | Credentials name role, organisation, what it does, and what qualifies them; never an unnamed attribution | research-digest | No bare job-title credentials; zero occurrences of "one commentator," "an analyst," "some observers" | |
| F5 | Sentence length binds; a labelled beat is not a licence for one long sentence | house-writing-style §8 | `check_prose.py`: median sentence ≤ ~20w and run-ons materially below the Jul 25 baseline of 56 | |
| F6 | Grammar check added as revision-pass check 5 | research-digest §7 | No ungrammatical fragments (qualitative) | |
| F7 | Audit marks require mechanical evidence | brief-feedback Step 0 | Next audit contains no "applied (qualitative)" marks | |
| R1 | Company explanations say what it sells, to whom, and why it is in the story — parenthetical or its own sentence | house-writing-style §3 | Companies on the glossary roster carry a real explanation on first use | |
| R2 | Hyperlinks in both the inline tag and the Source line | topics | Inline bracketed tags contain links | |
| R4 | "Why it matters" traces two steps out, states the premise it contests, may run multiple paragraphs | topics | No why-it-matters that only restates the item's significance | |
| P1 | Praised sandbox gloss harvested as a worked example | house-writing-style §3 | (protection, not a check) | |
| P2 | Inline bracketed-tag format marked confirmed working | topics | (protection, not a check) | |

## Baseline for next week's comparison

Measured on the Jul 25 brief with `scripts/check_prose.py`:

- 56 run-ons, 126 borderline sentences, median 29 words, 53% over rule 8's trigger
- 1 over-long paragraph
- 4 unlinked sections, 5 Source lines missing links
- 20 unglossed terms
- 1 banned construction

## Carried forward from the Jul 18 round

D5 (three-layer perspective entries), E4 (linked sources) and R1 (sentence
length) all failed in the Jul 25 brief and their fixes post-date it, so they
remain untested. They carry into the next audit alongside the items above.

## Corrections to the Jul 18 record

That record claimed 12 of 15 applied. Re-checked against this round's comments,
the real figure is 6. E1 (causal chains), E2a (glossing) and R2 (stand-in words)
were marked "applied (qualitative)" on a skim and had all failed; E3
(credentials) and E2b (benchmark glossing) were partial rather than applied; E4
failed more broadly than recorded, covering Source lines as well as the
perspective section. F7 exists to prevent a repeat.

## Deferred / not ratified this round

None — every item was verdicted. Still open from the Jul 18 round: O1 TSMC
concentration risk; O2 safety-index ranking; O3 NYT-sanctions re-explain; O4
Apple chip-deal motive; C1 Lambert roster credential (now resolved by F4's
roster entry); C2 add Xu / Sheehan / Chow to the roster; P2 from that round
(confirmed-working line for the What happened → Does it hold up pairing).
