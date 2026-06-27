#!/usr/bin/env bash
# Environment setup script for the AI Pulse routine — installs Python deps the
# weekly run needs. Saved at Matthew's request, kept verbatim as provided.

pip install --quiet --upgrade --only-binary :all: feedparser youtube-transcript-api beautifulsoup4 requests || pip install --quiet --upgrade youtube-transcript-api beautifulsoup4 requests
pip install --quiet faster-whisper || echo "faster-whisper not installed; audio path disabled"

# ---------------------------------------------------------------------------
# NOTE (kept separate so the script above is untouched):
# - scripts/md_to_docx.py requires `python-docx` to render the Word doc, and it
#   is NOT installed above. So the weekly run installs it on the fly each time.
#   To pre-provision it, add `python-docx` to the first pip line.
# - `feedparser` and `faster-whisper` are not used by the current scripts
#   (no RSS parsing, no audio-transcription path), so they are optional.
# - The packages the code actually imports are: beautifulsoup4, python-docx,
#   youtube-transcript-api.
# ---------------------------------------------------------------------------
