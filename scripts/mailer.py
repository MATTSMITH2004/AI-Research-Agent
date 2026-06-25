#!/usr/bin/env python3
"""Send the weekly brief as a real email via the SendGrid HTTPS API.

Why not SMTP: the Claude Code cloud environment blocks outbound SMTP (ports
587/465) — only HTTP/HTTPS egress is allowed — so the brief must be sent through
an HTTPS email API. SendGrid's API works here; raw smtplib does not.

True send (no manual step), BCC to the recipient list, with the rendered .docx
attached. Credentials and the recipient list come from environment variables —
set them in the Routine's environment-variable vault, never commit them:

  SENDGRID_API_KEY  a SendGrid API key with Mail Send permission
  SENDGRID_FROM     the verified sender address (SendGrid Single Sender), also
                    the visible From/To
  PULSE_RECIPIENTS  the distribution list, BCC'd. Separate addresses with
                    commas, semicolons, spaces, or newlines.

Usage:
  python3 scripts/mailer.py --docx briefs/ai-pulse-<date>.docx \
      --md briefs/ai-pulse-<date>.md \
      --subject "AI Pulse Brief — week of <date>"

  # dry run: build the payload and report, but do NOT call the API
  python3 scripts/mailer.py --docx ... --md ... --subject "..." --no-email
"""

import argparse
import base64
import json
import os
import re
import ssl
import sys
import urllib.request
import urllib.error

SENDGRID_URL = "https://api.sendgrid.com/v3/mail/send"
PROXY_CA = "/root/.ccr/ca-bundle.crt"


def _parse_recipients(raw):
    parts = [p.strip() for p in re.split(r"[,;\s]+", raw or "") if p.strip()]
    seen, out = set(), []
    for p in parts:
        if p.lower() not in seen:
            seen.add(p.lower())
            out.append(p)
    return out


def _intro_from_md(md_path):
    if not md_path or not os.path.exists(md_path):
        return ""
    for line in open(md_path, encoding="utf-8"):
        s = line.strip()
        if not s or s.startswith("#") or s.startswith("*Week of"):
            continue
        return s
    return ""


def _ssl_context():
    ctx = ssl.create_default_context()
    if os.path.exists(PROXY_CA):  # trust the environment's egress proxy CA
        try:
            ctx.load_verify_locations(PROXY_CA)
        except Exception:
            pass
    return ctx


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--docx", required=True, help="path to the rendered .docx to attach")
    ap.add_argument("--md", help="path to the markdown brief (for the email body)")
    ap.add_argument("--subject", required=True)
    ap.add_argument("--no-email", action="store_true",
                    help="dry run: build the payload and report, but do not call the API")
    args = ap.parse_args()

    if not os.path.exists(args.docx):
        sys.exit(f"error: docx not found: {args.docx}")

    sender = os.environ.get("SENDGRID_FROM") or os.environ.get("BRIEF_EMAIL_FROM")
    if not sender:
        sys.exit("error: SENDGRID_FROM is not set (your verified Single Sender address)")
    recipients = _parse_recipients(os.environ.get("PULSE_RECIPIENTS", ""))
    if not recipients:
        sys.exit("error: PULSE_RECIPIENTS is empty — set the BCC distribution list")

    intro = _intro_from_md(args.md)
    body = (intro + "\n\n" if intro else "") + \
        "Your AI Pulse brief is attached as a Word document. The full text is below.\n"
    if args.md and os.path.exists(args.md):
        body += "\n" + "-" * 60 + "\n\n" + open(args.md, encoding="utf-8").read()

    with open(args.docx, "rb") as f:
        docx_b64 = base64.b64encode(f.read()).decode("ascii")

    payload = {
        # visible To is the sender; the whole list is Bcc so recipients don't see each other
        "personalizations": [{
            "to": [{"email": sender}],
            "bcc": [{"email": r} for r in recipients],
        }],
        "from": {"email": sender},
        "subject": args.subject,
        "content": [{"type": "text/plain", "value": body}],
        "attachments": [{
            "content": docx_b64,
            "type": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            "filename": os.path.basename(args.docx),
            "disposition": "attachment",
        }],
    }

    if args.no_email:
        print("DRY RUN (--no-email): payload built, not calling the API.")
        print(f"  subject:    {args.subject}")
        print(f"  from/to:    {sender}")
        print(f"  bcc ({len(recipients)}): {', '.join(recipients)}")
        print(f"  attachment: {os.path.basename(args.docx)} "
              f"({len(docx_b64)} b64 chars)")
        return

    api_key = os.environ.get("SENDGRID_API_KEY")
    if not api_key:
        sys.exit("error: SENDGRID_API_KEY is not set (needed to send)")

    req = urllib.request.Request(
        SENDGRID_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Authorization": f"Bearer {api_key}",
                 "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=60, context=_ssl_context()) as resp:
            code = resp.getcode()
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "ignore")[:500]
        sys.exit(f"error: SendGrid returned HTTP {e.code}: {detail}")
    except urllib.error.URLError as e:
        sys.exit(f"error: could not reach SendGrid: {e.reason}")

    # SendGrid returns 202 Accepted on success
    print(f"sent '{args.subject}' to {len(recipients)} BCC recipient(s) "
          f"via SendGrid (HTTP {code})")


if __name__ == "__main__":
    main()
