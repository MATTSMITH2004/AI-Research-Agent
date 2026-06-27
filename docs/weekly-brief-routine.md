# Weekly AI Pulse brief — automated routine setup

This sets up the AI Pulse brief to generate and email itself every Saturday
morning, with no prompt typing. It uses Claude Code on the web **Routines**
(https://code.claude.com/docs/en/routines).

You create the routine once in the web UI; everything it needs lives in this repo.

**Email method: real send via the SendGrid HTTPS API (`scripts/mailer.py`).**
Why SendGrid and not Gmail/Outlook SMTP: the Claude Code cloud environment blocks
outbound SMTP (ports 587/465) — only HTTP/HTTPS egress is allowed — so the send
must go through an HTTPS email API. (Confirmed: SMTP sockets fail; SendGrid's API
is reachable.) Microsoft 365 send is unavailable (the connector exposes no send),
and the Gmail connector can only draft. SendGrid sends a true email (no manual
click) to the `PULSE_RECIPIENTS` list as **Bcc**, with the rendered `.docx`
attached.

## One-time setup

### A. SendGrid (once, free)

1. Create a free account at https://sendgrid.com.
2. **Verify a sender:** Settings → Sender Authentication → **Single Sender
   Verification** → verify the address you want the brief to come *from* (e.g.
   msmith@jczmf.com). No domain ownership needed — just click the link SendGrid
   emails you.
3. **Create an API key:** Settings → API Keys → Create API Key → "Restricted
   Access" with **Mail Send** enabled (or Full Access). Copy the key once.

### B. Create the routine at claude.ai/code/routines

1. **New routine** (Remote). **Repository:** `mattsmith2004/ai-research-agent`.
2. **Environment / network access:** the brief scrapes the open web AND calls the
   SendGrid API, so the **Default "Trusted"** allowlist will block it. Set the
   environment **Network access** to **Full** (or **Custom** including at least:
   podscripts.co, youtube.com, aidailybrief.ai, newsletter.semianalysis.com,
   api.sendgrid.com, and the news/primary domains the brief cites).
3. **Connectors:** none required for email (SendGrid is a plain HTTPS call). Keep
   only connectors the brief itself needs.
3a. **Permissions:** leave **"Allow unrestricted branch pushes" OFF.** (Turning it
   on can block routine creation depending on the GitHub install.) Instead, the
   routine keeps its rolling state on the dedicated branch `claude/ai-pulse-weekly`
   — a `claude/`-prefixed branch the routine can always push to without that
   permission. Each week it checks out that branch (which carries the accumulated
   `MEMORY.md` and past briefs) and pushes its updates back there. That preserves
   the "recently covered" history week to week, which is what prevents repeats.
4. **Environment variables (vault):** set the three below. They never live in the
   repo.

   | Variable | Value |
   | --- | --- |
   | `SENDGRID_API_KEY` | the API key from step A.3 |
   | `SENDGRID_FROM` | your verified Single Sender address (the From/To) |
   | `PULSE_RECIPIENTS` | the distribution list, Bcc'd — comma/space/semicolon separated |

5. **Schedule trigger:** Weekly → Saturday → 9:00 AM, in your local (Eastern)
   timezone. (The UI converts local → UTC automatically.)
6. Paste the **prompt** below, then **Create**. Use **Run now** once to test.

## The routine prompt (paste this)

> Generate this week's AI Pulse brief and email it to the distribution list.
>
> 1. Switch to the weekly state branch: git fetch origin && git checkout claude/ai-pulse-weekly. This branch carries the rolling MEMORY.md and past briefs (plus all the skill, scripts, config, and format reference).
> 2. Read `CLAUDE.md`, `MEMORY.md`, and `topics/ai-pulse.md`, and apply all of it.
> 3. Run the `research-digest` skill for `topics/ai-pulse.md` over the past 7 days
>    (Saturday-to-Saturday: cover developments since last week's brief). Use
>    `MEMORY.md`'s "recently covered" list to skip anything already reported in a
>    prior brief — never repeat an item. Updating MEMORY in step 6 sets the
>    boundary so next week resumes exactly where this one stopped.
>    Follow the canonical format in `templates/ai-pulse-format-reference.docx` and
>    every rule in the config and MEMORY (structured deep items with the labeled
>    beats and "My read"; full "What people are saying" with podcast AND Substack
>    entries; the model-specs beat; the source-discovery + "New sources worth
>    adding" section; cite every source used; gloss all jargon/benchmarks; primary
>    sources first).
> 4. Pull podcast/YouTube transcripts with `scripts/fetch_transcripts.py` (two
>    stages: list candidates, then fetch the AI-relevant ones).
> 5. Save the brief to `briefs/ai-pulse-<YYYY-MM-DD>.md` (today's date) and render
>    the Word doc with
>    `python3 scripts/md_to_docx.py briefs/ai-pulse-<YYYY-MM-DD>.md briefs/ai-pulse-<YYYY-MM-DD>.docx`.
> 6. Add a row for this brief at the TOP of the table in `briefs/README.md` (the
>    archive index): the week-of date, and links to this brief's `.docx` and `.md`.
> 7. Update `MEMORY.md` (recently-covered + the source-discovery ledger hit/miss),
>    then commit and push the brief, the updated `briefs/README.md`, AND the
>    updated `MEMORY.md` to the branch `claude/ai-pulse-weekly`. Pushing MEMORY
>    there is essential — it is how next week (which checks out that same branch in
>    step 1) knows what was already covered and avoids repeats.
> 8. Send the brief by running:
>    `python3 scripts/mailer.py --docx briefs/ai-pulse-<YYYY-MM-DD>.docx --md briefs/ai-pulse-<YYYY-MM-DD>.md --subject "AI Pulse Brief — week of <date>"`
>    This sends a real email via SendGrid, Bcc'd to `PULSE_RECIPIENTS`, with the
>    `.docx` attached. Confirm the script printed a "sent ... via SendGrid" line
>    before finishing.
> 9. Refresh `templates/ai-pulse-format-reference.{md,docx}` from this brief only
>    if the format changed.

## The sender — `scripts/mailer.py`

Real send via the SendGrid HTTPS API. Behavior:

- From/To = `SENDGRID_FROM`; the whole `PULSE_RECIPIENTS` list is **Bcc**, so
  recipients never see each other.
- Attaches the rendered `.docx`; puts the brief's intro + full text in the body.
- Reads `SENDGRID_API_KEY`, `SENDGRID_FROM`, `PULSE_RECIPIENTS` from the
  environment.
- `--no-email` does a dry run: builds the payload and prints subject, sender,
  recipient count/list, and attachment size, without calling the API.

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
- The script also works with any other HTTPS email API by swapping the request in
  `mailer.py`; SendGrid is the default because its API is reachable here and its
  Single Sender verification needs no domain.
