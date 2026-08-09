# Ratified changes — feedback round on the August 1–8, 2026 brief

Source doc: [ai-pulse-2026-08-08-feedback.docx](ai-pulse-2026-08-08-feedback.docx)
(32 comments). Ratified Aug 9, 2026.

Audit target: the **week of Aug 15, 2026 brief**. Results below to be filled by
the next round's Step 0. Per F7, an item is marked applied only on mechanical
evidence; anything without a mechanical check is marked **unverified**.

| # | Change | File | Observable check in the next brief | Result |
|---|---|---|---|---|
| D1 | Length target 15–18 pages, soft; over-length prompts trimming the perspective section by depth-over-coverage, never the top developments | topics | Brief is near 15–18 rendered pages, or says in one line why it ran over | |
| D2 | Model standings run EVERY week, with a line saying what moved or that nothing did | topics + MEMORY | A "## Model standings" section is present | |
| D3 | "On my radar" sits directly after "Worth a skim," before "What people are saying" | topics | Section order matches | |
| D4 | Zvi Mowshowitz ledger conflict resolved — on trial, removed from the passed-on list | MEMORY | Zvi appears in exactly one tier of the ledger | |
| D5 | One-off: do not repeat the "coverage volume shows market intent" framing | MEMORY one-offs | No market-intent claim resting on how many outlets covered something | |
| F1 | Inline bracketed source tags carry hyperlinks, same as the Source line | topics + script | `check_prose.py` reports 0 inline tags missing links (Aug 8 baseline: 19) | |
| F2 | Credentials extended: publications and shows get a blurb; hosts get why-listen context; guest hosts credentialed per episode; sitting CEOs of named companies exempt | research-digest + script | `check_prose.py` reports 0 roster names missing a credential (Aug 8 baseline: 7); "Money Stuff" and "Hard Fork" carry blurbs | |
| F3 | Superseded by D1's restructure — the perspective "Why it matters" beat is removed, not deepened | topics | No "Why it matters:" label appears in the perspective section | |
| F4 | Perspective headers state the argument, not the topic | topics | Every perspective header reads as a claim, like a top-development heading | |
| F5 | Glossary roster grows every run with terms the brief introduced | topics + research-digest | Roster gained entries this week; 0 unglossed terms | |
| F6 | Every paragraph in a perspective entry earns its place (revision-pass check 5) | research-digest | No digressions of the Lucent / researchers-marriage kind | |
| F7 | Bullet-marker consistency within a section | script | `check_prose.py` reports 0 mixed-bullet sections | |
| R1 | Depth over coverage in perspective entries: one or two topics explained properly — what it is, why it is relevant, how it connects — with concrete processes walked step by step | topics | No entry surveys five topics at a paragraph each | |
| R3 | "Issues" replaced by weaknesses / limits / failures where that is the real word | house-writing-style §9 | No capability-limit finding described as an "issue" | |
| L6 | Perspective entries restructured to four layers: claim header, italic credential line, body, unlabelled closing paragraph tying to the rest of the brief. No writer's own verdict in this section | topics | Entries show four distinct layers; the closing paragraph makes a connection to another item or a running thread | |
| P1 | Falsifiable capability-limit findings are a protected recurring beat, actively hunted | topics "What to track" | Such a finding appears when one exists in-window | |
| P2 | Hands-on product/implementation deep-dives earn extra weight in Pulse | topics "What to track" | (protection, not a check) | |

## Baseline for next week's comparison

Measured on the Aug 8 brief with `scripts/check_prose.py`:

- 38 run-ons, 177 borderline, median 27 words, 46% over rule 8's trigger
- 9 long paragraphs (regressed from 1 on Jul 25; was 20 on Aug 1)
- 0 unlinked sections, 0 unlinked Source lines, 0 unglossed roster terms
- **19 inline source tags missing links** (new check)
- **7 roster names missing a credential** (new check)
- ~10,500 words

## Carried forward

D1/D2/D3 from the Jul 25 round (model standings) were never testable because no
standings section ran for two weeks; D2 above fixes the cause. F2 (causal
chains), F6 (grammar) and F1b (company three parts) from that round remain
**unverified** — no mechanical check exists for them.

## Rejected this round

R2 (no market-level inference from coverage volume) — Matthew wants market
inference kept as a tool; the Aug 8 instance is queued as a one-off correction
instead.

## Not actioned

c7 ("This is nnew," anchored to the operator/legal due-diligence passage) —
disregarded at Matthew's instruction. c11 (more DeepMind backstory) — explicitly
not queued.
