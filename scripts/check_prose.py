#!/usr/bin/env python3
"""Mechanical pre-flight check on a drafted brief (see research-digest step 7).

Reports what the house rules make checkable, with line numbers, so the
revision pass works from a list instead of from memory:

  - long sentences        house-writing-style rule 8 (one idea per sentence)
  - long paragraphs       topic config "Readability" (split past five sentences)
  - unlinked sections     research-digest "a named source is a linked source"
  - banned constructions  house-writing-style rule 5

It is a REPORTER, not an editor. It flags candidates; the writer judges each
one and fixes or deliberately keeps it. A clean run is not proof the prose is
good — only that these four mechanical traps are clear.

Usage:
    python3 scripts/check_prose.py briefs/ai-pulse-2026-07-25.md
    python3 scripts/check_prose.py <file> --quiet   # counts only
"""

import argparse
import re
import sys

# --------------------------------------------------------------------------- #
# Thresholds — keep in sync with the rules they enforce
# --------------------------------------------------------------------------- #
# Rule 8's audit trigger (3+ commas) is what a writer applies while writing.
# Applied to a finished brief it flags ~65% of sentences, which is a wall, not
# a worklist — so the report is tiered. SEVERE is the near-certain run-on and
# is listed in full; REVIEW is the rule's own trigger, counted and sampled.
SEVERE_WORDS = 50       # a sentence this long is a run-on almost regardless
SEVERE_COMMAS = 5       # ...or this comma-stacked, at moderate length
SEVERE_COMMA_WORDS = 35
WORKLIST = 25           # worst-first cap; the rate below carries the rest
MAX_COMMAS = 3          # house-writing-style rule 8 audit trigger
MAX_WORDS = 30          # "roughly thirty-plus words"
MAX_PARA_SENTENCES = 5  # topic config "Readability"

# house-writing-style rule 5. Word-boundary matched, case-insensitive.
BANNED = [
    r"closed the loop", r"come full circle", r"full circle",
    r"partial climbdown", r"\bsaga\b", r"\bdrama\b",
    r"last week's brief", r"this week's brief covered",
    r"it's not just .{1,40}?, it's", r"not just .{1,40}?, but rather",
    r"\bunderscores\b", r"\bhighlights\b(?! reel)", r"\bsignals\b",
    r"\bcements\b", r"marks a turning point",
    r", cementing", r", underscoring", r", highlighting", r", signaling",
    r"in recent developments", r"in a move that",
    r"\bQuotable\b",
]

SENTENCE_END = re.compile(r"(?<=[.!?])\s+")
# Abbreviations that must not end a sentence
ABBREV = re.compile(r"\b(?:e\.g|i\.e|vs|Mr|Ms|Dr|Inc|Corp|Co|St|No|approx|U\.S|U\.K)\.$",
                    re.IGNORECASE)


def is_skippable(line):
    """Table rows, headings, and code fences are not prose. Neither is a
    "Source:" line — it is a deliberate comma-separated list of citations, so
    the sentence rules would flag every one of them forever."""
    s = line.strip()
    return (not s or s.startswith("|") or s.startswith("#")
            or s.startswith("```") or s.startswith("---")
            or s.startswith("Source:") or s.startswith("**Source:"))


def is_bullet(line):
    return bool(re.match(r"\s*[-*+]\s", line))


def split_sentences(text):
    """Split on sentence enders, re-joining where the 'end' was an abbreviation
    or a decimal number ($1.7 billion, 62.1%)."""
    parts = SENTENCE_END.split(text)
    out = []
    for p in parts:
        if out and (ABBREV.search(out[-1]) or re.search(r"\d\.$", out[-1])):
            out[-1] = out[-1] + " " + p
        else:
            out.append(p)
    return [s for s in out if s.strip()]


def strip_markup(s):
    """Drop link URLs and bold/italic markers so word counts measure prose, not
    syntax. Keeps the link's anchor text."""
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)   # [anchor](url) -> anchor
    s = re.sub(r"[*_`]", "", s)
    return s


def check(path, quiet=False):
    lines = open(path, encoding="utf-8").read().split("\n")

    long_sentences, long_paras, banned_hits, all_lengths = [], [], [], []
    sections = []          # (line_no, title, has_link, body_lines)
    current = None

    para_buf, para_start = [], None

    def flush_para():
        nonlocal para_buf, para_start
        if para_buf:
            text = strip_markup(" ".join(para_buf))
            n = len(split_sentences(text))
            if n > MAX_PARA_SENTENCES:
                long_paras.append((para_start, n, text[:70]))
        para_buf, para_start = [], None

    for i, raw in enumerate(lines, 1):
        if raw.startswith("## "):
            flush_para()
            current = {"line": i, "title": raw[3:].strip(), "link": False}
            sections.append(current)
        if current and "](http" in raw:
            current["link"] = True

        if is_skippable(raw):
            flush_para()
            continue

        # each bullet is its own unit — consecutive bullets are a list, not one
        # dense paragraph, and merging them invents paragraph-length failures
        if is_bullet(raw):
            flush_para()

        para_buf.append(raw.strip())
        if para_start is None:
            para_start = i

        prose = strip_markup(raw)
        for s in split_sentences(prose):
            commas, words = s.count(","), len(s.split())
            all_lengths.append(words)
            if commas >= MAX_COMMAS or words >= MAX_WORDS:
                severe = words >= SEVERE_WORDS or (commas >= SEVERE_COMMAS
                                                   and words >= SEVERE_COMMA_WORDS)
                long_sentences.append((i, words, commas, s.strip()[:70], severe))

        if is_bullet(raw):
            flush_para()
        for pat in BANNED:
            for m in re.finditer(pat, prose, re.IGNORECASE):
                banned_hits.append((i, m.group(0)))
    flush_para()

    # Sections that legitimately carry no links: the standings table (a table of
    # model names) and the closing config-notes line.
    LINK_EXEMPT = ("config notes", "model standings")
    unlinked = [s for s in sections if not s["link"]
                and s["title"].lower() not in LINK_EXEMPT]

    if quiet:
        n_severe = sum(1 for s in long_sentences if s[4])
        print(f"{n_severe} run-ons ({len(long_sentences)} borderline) | "
              f"{len(long_paras)} long paragraphs | {len(unlinked)} unlinked "
              f"sections | {len(banned_hits)} banned constructions")
        return 1 if (n_severe or long_paras or unlinked or banned_hits) else 0

    def header(t, n):
        print(f"\n{'=' * 70}\n{t}: {n}\n{'=' * 70}")

    severe = [s for s in long_sentences if s[4]]
    n_sent = max(1, len(all_lengths))
    median = sorted(all_lengths)[len(all_lengths) // 2] if all_lengths else 0
    over_trigger = 100 * len(long_sentences) // n_sent

    header("SENTENCE LENGTH", f"median {median}w, {over_trigger}% over rule 8's "
           f"trigger")
    print("house-writing-style rule 8 — split unless it is genuinely one idea.")
    print(f"A median much above ~20w, or a rate much above ~25%, means the "
          f"split pass did not bind\nacross the document — not just in the "
          f"lines listed below.\n")
    print(f"Worst {min(WORKLIST, len(severe))} of {len(severe)} run-ons "
          f"(>={SEVERE_WORDS}w, or >={SEVERE_COMMAS} commas at "
          f">={SEVERE_COMMA_WORDS}w):")
    for ln, w, c, txt, _ in sorted(severe, key=lambda x: -x[1])[:WORKLIST]:
        print(f"  L{ln:<5} {w:>3}w {c}c  {txt}...")
    if len(severe) > WORKLIST:
        print(f"  … and {len(severe) - WORKLIST} more at or below "
              f"{sorted(severe, key=lambda x: -x[1])[WORKLIST][1]}w")

    header(f"LONG PARAGRAPHS (>{MAX_PARA_SENTENCES} sentences)", len(long_paras))
    print("topic config Readability — break at a natural seam.")
    for ln, n, txt in long_paras:
        print(f"  L{ln:<5} {n} sentences  {txt}...")

    header("SECTIONS WITH NO LINKS", len(unlinked))
    print("research-digest — a named source is a linked source.")
    for s in unlinked:
        print(f"  L{s['line']:<5} {s['title']}")

    header("BANNED CONSTRUCTIONS", len(banned_hits))
    print("house-writing-style rule 5.")
    for ln, hit in banned_hits:
        print(f"  L{ln:<5} \"{hit}\"")

    must_fix = len(severe) + len(long_paras) + len(unlinked) + len(banned_hits)
    print(f"\n{'=' * 70}\n{len(severe)} run-ons, {len(long_paras)} long "
          f"paragraphs, {len(unlinked)} unlinked sections, {len(banned_hits)} "
          f"banned constructions.\nFlags are candidates, not verdicts — judge "
          f"each one.\n{'=' * 70}")
    return 1 if must_fix else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file", help="the drafted brief (.md)")
    ap.add_argument("--quiet", action="store_true", help="counts only")
    args = ap.parse_args()
    sys.exit(check(args.file, args.quiet))


if __name__ == "__main__":
    main()
