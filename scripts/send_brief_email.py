#!/usr/bin/env python3
"""Email a finished brief (with the .docx attached) via SMTP.

Used by the weekly AI Pulse routine to deliver the brief to Matthew. All
credentials come from environment variables (set them in the Routine's
environment-variable vault — never commit them):

  BRIEF_SMTP_HOST   e.g. smtp.sendgrid.net / smtp.office365.com
  BRIEF_SMTP_PORT   usually 587 (STARTTLS)
  BRIEF_SMTP_USER   SMTP username (for SendGrid this is the literal "apikey")
  BRIEF_SMTP_PASS   SMTP password / API key
  BRIEF_EMAIL_FROM  verified sender address (e.g. msmith@jczmf.com)
  BRIEF_EMAIL_TO    recipient (defaults to BRIEF_EMAIL_FROM if unset)

Usage:
  python3 scripts/send_brief_email.py --docx briefs/ai-pulse-2026-06-24.docx \
      --md briefs/ai-pulse-2026-06-24.md --subject "AI Pulse Brief — week of June 24, 2026"

If --md is given, the brief's intro paragraph is used as a short email body and
the full markdown is included as plain text below it. The .docx is attached.
"""

import argparse
import os
import smtplib
import sys
from email.message import EmailMessage


def _require(name):
    val = os.environ.get(name)
    if not val:
        sys.exit(f"error: required environment variable {name} is not set")
    return val


def _intro_from_md(md_path):
    """Return the first real paragraph (the brief intro) for the email body."""
    if not md_path or not os.path.exists(md_path):
        return ""
    out = []
    for line in open(md_path, encoding="utf-8"):
        s = line.strip()
        if s.startswith("#") or s.startswith("*Week of") or not s:
            if out:  # stop at the first blank line after we've collected text
                break
            continue
        out.append(s)
        if len(out) >= 1:
            break
    return out[0] if out else ""


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--docx", required=True, help="path to the .docx to attach")
    ap.add_argument("--md", help="path to the markdown brief (for the email body)")
    ap.add_argument("--subject", required=True)
    args = ap.parse_args()

    host = _require("BRIEF_SMTP_HOST")
    port = int(os.environ.get("BRIEF_SMTP_PORT", "587"))
    user = _require("BRIEF_SMTP_USER")
    password = _require("BRIEF_SMTP_PASS")
    sender = _require("BRIEF_EMAIL_FROM")
    recipient = os.environ.get("BRIEF_EMAIL_TO", sender)

    if not os.path.exists(args.docx):
        sys.exit(f"error: docx not found: {args.docx}")

    msg = EmailMessage()
    msg["Subject"] = args.subject
    msg["From"] = sender
    msg["To"] = recipient

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

    with smtplib.SMTP(host, port, timeout=60) as server:
        server.starttls()
        server.login(user, password)
        server.send_message(msg)
    print(f"sent '{args.subject}' to {recipient} ({len(data)} bytes attached)")


if __name__ == "__main__":
    main()
