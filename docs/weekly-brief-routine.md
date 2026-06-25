# Weekly AI Pulse brief — automated routine setup

This sets up the AI Pulse brief to generate and email itself every Saturday
morning, with no prompt typing. It uses Claude Code on the web **Routines**
(https://code.claude.com/docs/en/routines).

You create the routine once in the web UI; everything it needs lives in this repo.

**Chosen email method: Gmail (draft).** The Gmail connector can compose a draft
(with the full brief in the body) but cannot send, and its attachments are "not
supported yet" — so each Saturday the routine drops a finished, readable brief
into your Gmail **Drafts**, with the Word doc linked from the repo. You read it in
Drafts, or one-click Send to move it to your inbox. No extra accounts, secrets, or
permission grants. Your only action item is creating the routine below and
including the Gmail connector.

## One-time setup at claude.ai/code/routines

1. **New routine.** Go to https://claude.ai/code/routines → **New routine**
   (Remote).
2. **Repository:** `mattsmith2004/ai-research-agent`.
3. **Environment / network access:** the brief scrapes the open web (podscripts,
   YouTube, aidailybrief, news sites), so the **Default "Trusted"** allowlist will
   block it with 403s. Set the routine's environment **Network access** to **Full**
   (or **Custom** with at least: podscripts.co, youtube.com, aidailybrief.ai,
   newsletter.semianalysis.com, and the news/primary domains the brief cites).
4. **Connectors:** include **Gmail** (for draft delivery). Remove connectors the
   routine doesn't need.
5. **Schedule trigger:** Weekly → Saturday → 9:00 AM, in your local (Eastern)
   timezone. (The UI converts local → UTC automatically.)
6. **Environment variables:** none needed for the Gmail-draft method. (Only the
   SMTP fallback below needs secrets.)
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
> 6. Deliver the brief by creating a Gmail draft with the `mcp__Gmail__create_draft`
>    tool: to msmith@jczmf.com, subject "AI Pulse Brief — week of <date>". Render
>    the FULL brief as the `htmlBody` (readable directly in the email) with a plain
>    -text version in `body`, and include a link to the pushed `.docx` on GitHub.
>    Do not rely on attachments (the tool does not support them). Confirm the draft
>    was created before finishing.
> 7. Refresh `templates/ai-pulse-format-reference.{md,docx}` from this brief only
>    if the format changed.

## Email step

**Chosen — Gmail draft (`mcp__Gmail__create_draft`).** Composes a fully readable
brief in your Gmail Drafts each Saturday; you read it there or one-click Send.
Step 6 of the prompt above uses it. No secrets or extra setup. Limits: the Gmail
connector cannot send (draft only) and does not support attachments, so the brief
goes in the body and the Word doc is linked from the repo.

**Fallback — true auto-send to inbox via `scripts/send_brief_email.py` (SMTP).**
Only if you later want the brief to land in your Inbox automatically with the
`.docx` attached (no manual Send). Switch step 6 to run the script and set these
environment variables in the routine vault (e.g. a free SendGrid account, sender
verified):
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
