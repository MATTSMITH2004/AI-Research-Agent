# Weekly AI Pulse brief — automated routine setup

This sets up the AI Pulse brief to generate and email itself every Saturday
morning, with no prompt typing. It uses Claude Code on the web **Routines**
(https://code.claude.com/docs/en/routines).

You create the routine once in the web UI; everything it needs lives in this repo.

## One-time setup at claude.ai/code/routines

1. **New routine.** Go to https://claude.ai/code/routines → **New routine**
   (Remote).
2. **Repository:** `mattsmith2004/ai-research-agent`.
3. **Environment / network access:** the brief scrapes the open web (podscripts,
   YouTube, aidailybrief, news sites), so the **Default "Trusted"** allowlist will
   block it with 403s. Set the routine's environment **Network access** to **Full**
   (or **Custom** with at least: podscripts.co, youtube.com, aidailybrief.ai,
   newsletter.semianalysis.com, and the news/primary domains the brief cites).
4. **Connectors:** include **Microsoft 365** only if you go with email Option A
   below. Remove connectors the routine doesn't need.
5. **Schedule trigger:** Weekly → Saturday → 9:00 AM, in your local (Eastern)
   timezone. (The UI converts local → UTC automatically.)
6. **Environment variables (only for email Option B):** add the SMTP secrets
   listed below. These live in the routine's vault, never in this repo.
7. Paste the **prompt** below, then **Create**. Use **Run now** once to test.

## The routine prompt (paste this)

> Generate this week's AI Pulse brief and email it to me.
>
> 1. Read `CLAUDE.md`, `MEMORY.md`, and `topics/ai-pulse.md`, and apply all of it.
> 2. Run the `research-digest` skill for `topics/ai-pulse.md` over the past 7 days.
>    Follow the canonical format in `templates/ai-pulse-format-reference.docx` and
>    every rule in the config and MEMORY (structured deep items with the labeled
>    beats and "My read"; full "What people are saying" section with podcast AND
>    Substack entries; the model-specs beat; the source-discovery + "New sources
>    worth adding" section; cite every source used; gloss all jargon/benchmarks;
>    primary sources first).
> 3. Pull podcast/YouTube transcripts with `scripts/fetch_transcripts.py` (two
>    stages: list candidates, then fetch the AI-relevant ones).
> 4. Save the brief to `briefs/ai-pulse-<YYYY-MM-DD>.md` (use today's date) and
>    render the Word doc with
>    `python3 scripts/md_to_docx.py briefs/ai-pulse-<YYYY-MM-DD>.md briefs/ai-pulse-<YYYY-MM-DD>.docx`.
> 5. Update `MEMORY.md` (recently-covered + the source-discovery ledger hit/miss),
>    then commit and push the brief and memory to a `claude/` branch.
> 6. Email the brief to msmith@jczmf.com — see the email step for your chosen
>    method — with the `.docx` attached and the subject
>    "AI Pulse Brief — week of <date>".
> 7. Refresh `templates/ai-pulse-format-reference.{md,docx}` from this brief only
>    if the format changed.

## Email step — pick ONE and keep it in the prompt

**Option A — Microsoft 365 connector (send from your own Outlook).**
Requires the Microsoft 365 connector to have **send / Mail.Send** permission
(the current connection is read-only — reconnect it granting send). Then add to
the prompt's step 6: "Send the email using the Microsoft 365 send-mail tool,
attaching the .docx." No script or secrets needed.

**Option B — SMTP via `scripts/send_brief_email.py` (no connector changes).**
Add these environment variables to the routine (vault), then add to step 6:
"Send the email by running `python3 scripts/send_brief_email.py --docx <docx>
--md <md> --subject '<subject>'`."

| Variable | Value |
| --- | --- |
| `BRIEF_SMTP_HOST` | e.g. `smtp.sendgrid.net` |
| `BRIEF_SMTP_PORT` | `587` |
| `BRIEF_SMTP_USER` | SMTP user (for SendGrid, the literal `apikey`) |
| `BRIEF_SMTP_PASS` | the API key / SMTP password |
| `BRIEF_EMAIL_FROM` | a verified sender, e.g. `msmith@jczmf.com` |
| `BRIEF_EMAIL_TO` | `msmith@jczmf.com` |

With SendGrid (free tier), verify `msmith@jczmf.com` as a Single Sender so you
don't need to own a domain. The same script works with any SMTP provider.

## Notes

- Routines run autonomously (no approval prompts), draw on your subscription
  usage, and have a daily run cap — a weekly job is well within it.
- A run shows up as a normal session you can open to see exactly what it did.
- To change the time or pause it, edit the routine at claude.ai/code/routines.
