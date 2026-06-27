#!/usr/bin/env bash
# Environment setup script for the AI Pulse routine — installs Python deps the
# weekly run needs. Mirrors the script set in the routine's environment settings.

pip install --quiet --upgrade --only-binary :all: feedparser youtube-transcript-api beautifulsoup4 requests || pip install --quiet --upgrade youtube-transcript-api beautifulsoup4 requests
pip install --quiet faster-whisper || echo "faster-whisper not installed; audio path disabled"
pip install --quiet python-docx

# ---------------------------------------------------------------------------
# Notes:
# - python-docx (last line) is what renders the Word doc (scripts/md_to_docx.py).
# - The packages the code actually imports are: beautifulsoup4, python-docx,
#   youtube-transcript-api. feedparser and faster-whisper are unused by the
#   current scripts (no RSS parsing, no audio path) and are optional.
# ---------------------------------------------------------------------------
