#!/usr/bin/env python3
"""Send the weekly brief as a real email (Gmail app-password SMTP).

True send (no manual step), BCC to the recipient list, with the rendered .docx
attached. Used as the final step of the weekly AI Pulse routine.

Credentials and the recipient list come from environment variables — set them in
the Routine's environment-variable vault, never commit them:

  GMAIL_ADDRESS       the sending Gmail address (also the SMTP username and the
                      visible From/To)
  GMAIL_APP_PASSWORD  a Google App Password for that account (16 chars; requires
                      2-Step Verification). Only needed for an actual send.
  PULSE_RECIPIENTS    the distribution list, BCC'd. Separate addresses with
                      commas, semicolons, spaces, or newlines.

Optional overrides (default to Gmail):
  PULSE_SMTP_HOST     default smtp.gmail.com
  PULSE_SMTP_PORT     default 587 (STARTTLS)

The message is sent with From/To = GMAIL_ADDRESS and everyone in PULSE_RECIPIENTS
on Bcc, so recipients never see each other.

Usage:
  python3 scripts/mailer.py --docx briefs/ai-pulse-<date>.docx \
      --md briefs/ai-pulse-<date>.md \
      --subject "AI Pulse Brief — week of <date>"

  # dry run: build everything and report, but do NOT connect or send
  python3 scripts/mailer.py --docx ... --md ... --subject "..." --no-email
"""

import argparse
import os
import re
import smtplib
import sys
from email.message import EmailMessage


def _require(name):
    val = os.environ.get(name)
    if not val:
        sys.exit(f"error: required environment variable {name} is not set")
    return val


def _parse_recipients(raw):
    parts = [p.strip() for p in re.split(r"[,;\s]+", raw or "") if p.strip()]
    seen, out = set(), []
    for p in parts:
        key = p.lower()
        if key not in seen:
            seen.add(key)
            out.append(p)
    return out


def _intro_from_md(md_path):
    """Return the brief's first real paragraph for the email body."""
    if not md_path or not os.path.exists(md_path):
        return ""
    for line in open(md_path, encoding="utf-8"):
        s = line.strip()
        if not s or s.startswith("#") or s.startswith("*Week of"):
            continue
        return s
    return ""


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--docx", required=True, help="path to the rendered .docx to attach")
    ap.add_argument("--md", help="path to the markdown brief (for the email body)")
    ap.add_argument("--subject", required=True)
    ap.add_argument("--no-email", action="store_true",
                    help="dry run: build and report, but do not connect or send")
    args = ap.parse_args()

    if not os.path.exists(args.docx):
        sys.exit(f"error: docx not found: {args.docx}")

    sender = os.environ.get("GMAIL_ADDRESS") or os.environ.get("BRIEF_EMAIL_FROM")
    if not sender:
        sys.exit("error: GMAIL_ADDRESS is not set")
    recipients = _parse_recipients(os.environ.get("PULSE_RECIPIENTS", ""))
    if not recipients:
        sys.exit("error: PULSE_RECIPIENTS is empty — set the BCC distribution list")

    # build the message
    msg = EmailMessage()
    msg["Subject"] = args.subject
    msg["From"] = sender
    msg["To"] = sender                       # visible To is the sender
    msg["Bcc"] = ", ".join(recipients)       # everyone else BCC'd; send_message strips this header

    intro = _intro_from_md(args.md)
    body = (intro + "\n\n" if intro else "") + \
        "Your AI Pulse brief is attached as a Word document. The full text is below.\n"
    if args.md and os.path.exists(args.md):
        body += "\n" + "-" * 60 + "\n\n" + open(args.md, encoding="utf-8").read()
    msg.set_content(body)

    with open(args.docx, "rb") as f:
        data = f.read()
    msg.add_attachment(
        data,
        maintype="application",
        subtype="vnd.openxmlformats-officedocument.wordprocessingml.document",
        filename=os.path.basename(args.docx),
    )

    if args.no_email:
        print("DRY RUN (--no-email): not connecting or sending.")
        print(f"  subject:    {args.subject}")
        print(f"  from/to:    {sender}")
        print(f"  bcc ({len(recipients)}): {', '.join(recipients)}")
        print(f"  attachment: {os.path.basename(args.docx)} ({len(data)} bytes)")
        return

    host = os.environ.get("PULSE_SMTP_HOST", "smtp.gmail.com")
    port = int(os.environ.get("PULSE_SMTP_PORT", "587"))
    password = os.environ.get("GMAIL_APP_PASSWORD") or os.environ.get("BRIEF_SMTP_PASS")
    if not password:
        sys.exit("error: GMAIL_APP_PASSWORD is not set (needed to send)")

    with smtplib.SMTP(host, port, timeout=60) as server:
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)  # sends to To + Bcc; strips the Bcc header
    print(f"sent '{args.subject}' to {len(recipients)} BCC recipient(s); "
          f"{len(data)} bytes attached")


if __name__ == "__main__":
    main()
