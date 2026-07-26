# Brief feedback — Archive

Every commented brief Matthew uploads, newest first. These are the marked-up Word
documents his margin comments live in — the raw input the `brief-feedback` skill
reads, kept so the reasoning behind a rule change stays traceable to the comment
that prompted it.

Naming: `ai-pulse-<YYYY-MM-DD>-feedback.docx`, where the date is the brief being
commented on (matching its filename in [`briefs/`](../briefs/)), not the date the
comments were written.

Each round also gets a `-ratified.md` record listing every approved change and
the observable check for whether it actually landed. The next round's audit
(brief-feedback Step 0) reads that record, tests each item against the newest
brief, and fills in the Result column — so a change that quietly fails to bind
is caught within a week instead of drifting.

| Brief commented on | Feedback doc | Comments | Ratified record | Outcome |
| --- | --- | --- | --- | --- |
| July 11–18, 2026 | [ai-pulse-2026-07-18-feedback.docx](ai-pulse-2026-07-18-feedback.docx) | 41 | [record](ai-pulse-2026-07-18-ratified.md) | 15 ratified Jul 20, 8 deferred. Audited against the Jul 25 brief: 12 applied, 1 failed (three-layer perspective entries), 2 partial (transcript links, sentence length) — all three traced to one stale note in `MEMORY.md`, since removed |

The `brief-feedback` skill adds a row here each time a feedback round is
processed.
