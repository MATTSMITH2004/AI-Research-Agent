# Sandbox — scratch copies, safe to edit

This folder is a **playground**. The files here are copies of the real config that
shapes the weekly brief. Edit them all you want — **nothing in here affects the
brief.** The weekly routine never reads this folder; it only reads the real files
at the top of the repo.

## What's in here (copies of the live files)

| Sandbox copy | The real file it mirrors |
| --- | --- |
| `sandbox/CLAUDE.md` | `CLAUDE.md` (who I am, lenses, how briefs read, tone) |
| `sandbox/MEMORY.md` | `MEMORY.md` (learned preferences, what's been covered) |
| `sandbox/topics/ai-pulse.md` | `topics/ai-pulse.md` (the AI brief's structure and sources) |
| `sandbox/templates/ai-pulse-format-reference.md` | `templates/ai-pulse-format-reference.md` (the format exemplar) |

## How to use it

1. Edit any file under `sandbox/` — try out new wording, a new section, a different
   tone. Commit freely. The live brief keeps running on the real files, untouched.
2. When you're happy with a change and want it to go live, tell Claude
   "promote the sandbox change to the real file" (or copy it over yourself). Only
   then does it start affecting the brief.

## Keeping it fresh

These copies are a snapshot from when the folder was created, so over time the real
files will drift ahead (the routine updates `MEMORY.md` every week, for instance).
If you want a clean copy to start tinkering from again, ask Claude to "refresh the
sandbox from the live files."
