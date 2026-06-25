# Weekly AI Pulse brief — automated routine setup

This sets up the AI Pulse brief to generate and email itself every Saturday
morning, with no prompt typing. It uses Claude Code on the web **Routines**
(https://code.claude.com/docs/en/routines).

You create the routine once in the web UI; everything it needs lives in this repo.

**Email method: real send via Gmail app-password SMTP (`scripts/mailer.py`).**
Each Saturday the routine sends a true email (no manual click) to the
`PULSE_RECIPIENTS` distribution list as **Bcc**, with the rendered `.docx`
attached. No third-party signup — it uses your own Google account and a Google
App Password.

## One-time setup

### A. Create a Gmail App Password (once)

1. The sending Google account needs **2-Step Verification** enabled.
2. Create an App Password at https://myaccount.google.com/apppasswords (pick
   "Mail"). Google shows a 16-character password once — copy it. This is what
   `mailer.py` uses; it is not your normal Google password and can be revoked
   anytime.

### B. Create the routine at claude.ai/code/routines

1. **New routine** (Remote). **Repository:** `mattsmith2004/ai-research-agent`.
2. **Environment / network access:** the brief scrapes the open web (podscripts,
   YouTube, aidailybrief, news sites), so the **Default "Trusted"** allowlist will
   block it with 403s. Set the routine's environment **Network access** to **Full**
   (or **Custom** with at least: podscripts.co, youtube.com, aidailybrief.ai,
   newsletter.semianalysis.com, smtp.gmail.com, and the news/primary domains the
   brief cites). Note Gmail SMTP needs `smtp.gmail.com:587` reachable.
3. **Connectors:** none required for email (the send is a plain SMTP script). Keep
   only connectors the brief itself needs.
4. **Environment variables (vault):** set the three below. They never live in the
   repo.

   | Variable | Value |
   | --- | --- |
   | `GMAIL_ADDRESS` | the sending Gmail address (also the From/To) |
   | `GMAIL_APP_PASSWORD` | the 16-char App Password from step A |
   | `PULSE_RECIPIENTS` | the distribution list, Bcc'd — comma/space/semicolon separated |

5. **Schedule trigger:** Weekly → Saturday → 9:00 AM, in your local (Eastern)
   timezone. (The UI converts local → UTC automatically.)
6. Paste the **prompt** below, then **Create**. Use **Run now** once to test.

## The routine prompt (paste this)

> Generate this week's AI Pulse brief and email it to the distribution list.
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
> 6. Send the brief by running:
>    `python3 scripts/mailer.py --docx briefs/ai-pulse-<YYYY-MM-DD>.docx --md briefs/ai-pulse-<YYYY-MM-DD>.md --subject "AI Pulse Brief — week of <date>"`
>    This sends a real email, Bcc'd to the `PULSE_RECIPIENTS` list, with the
>    `.docx` attached. Confirm the script printed a success line before finishing.
> 7. Refresh `templates/ai-pulse-format-reference.{md,docx}` from this brief only
>    if the format changed.

## The sender — `scripts/mailer.py`

Real send via Gmail app-password SMTP. Behavior:

- Sends with From/To = `GMAIL_ADDRESS`; the whole `PULSE_RECIPIENTS` list goes on
  **Bcc**, so recipients never see each other.
- Attaches the rendered `.docx`; puts the brief's intro + full text in the body.
- Reads `GMAIL_ADDRESS`, `GMAIL_APP_PASSWORD`, `PULSE_RECIPIENTS` from the
  environment (optional `PULSE_SMTP_HOST` / `PULSE_SMTP_PORT`, default
  `smtp.gmail.com:587`).
- `--no-email` does a dry run: it builds the message and prints the subject,
  sender, recipient count/list, and attachment size, but does not connect or
  send. Use it to test the routine without spamming the list.

Test it (no send):

```
python3 scripts/mailer.py --docx briefs/ai-pulse-<date>.docx \
    --md briefs/ai-pulse-<date>.md \
    --subject "AI Pulse Brief — week of <date>" --no-email
```

## Notes

- Routines run autonomously (no approval prompts), draw on your subscription
  usage, and have a daily run cap — a weekly job is well within it.
- A run shows up as a normal session you can open to see exactly what it did.
- To change the time or pause it, edit the routine at claude.ai/code/routines.
- SendGrid alternative: `mailer.py` is plain SMTP, so it also works against any
  other provider by overriding `PULSE_SMTP_HOST`/`PORT` and using that provider's
  SMTP user/password in `GMAIL_ADDRESS`/`GMAIL_APP_PASSWORD`. Gmail app-password
  is the default and needs no third-party signup.
