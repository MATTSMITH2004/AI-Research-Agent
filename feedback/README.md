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
| July 18–25, 2026 | [ai-pulse-2026-07-25-feedback.docx](ai-pulse-2026-07-25-feedback.docx) | 44 | [record](ai-pulse-2026-07-25-ratified.md) | 17 ratified Jul 26, 0 deferred. Adds a glossary roster with a mechanical gloss check, Source-line link enforcement, deeper credentials, a combined model ranking, and the one-entry-per-argument rule |
| July 11–18, 2026 | [ai-pulse-2026-07-18-feedback.docx](ai-pulse-2026-07-18-feedback.docx) | 41 | [record](ai-pulse-2026-07-18-ratified.md) | 15 ratified Jul 20, 8 deferred. Audited against the Jul 25 brief: **6 applied, not the 12 first recorded** — three items were marked applied on a skim and had failed. Corrections in that record; brief-feedback Step 0 now requires mechanical evidence |

The `brief-feedback` skill adds a row here each time a feedback round is
processed.
