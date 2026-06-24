#!/usr/bin/env python3
"""Render a research-digest brief (markdown) to a styled .docx.

Usage: python3 scripts/md_to_docx.py <input.md> <output.docx>

Handles the subset of markdown the briefs use: # / ## headings, **bold**,
*italic*, "- " bullets, "Source:" lines, and --- rules. URLs are left as
visible text so every claim stays traceable on the page.
"""

import re
import sys

from docx import Document
from docx.shared import Pt


INLINE = re.compile(r"(\*\*.+?\*\*|\*.+?\*)")


def add_inline(paragraph, text):
    """Add text to a paragraph, honoring **bold** and *italic* spans."""
    for part in INLINE.split(text):
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            run = paragraph.add_run(part[2:-2])
            run.bold = True
        elif part.startswith("*") and part.endswith("*"):
            run = paragraph.add_run(part[1:-1])
            run.italic = True
        else:
            paragraph.add_run(part)


def main():
    src, dst = sys.argv[1], sys.argv[2]
    lines = open(src, encoding="utf-8").read().split("\n")

    doc = Document()
    style = doc.styles["Normal"]
    style.font.name = "Calibri"
    style.font.size = Pt(11)

    for raw in lines:
        line = raw.rstrip()
        if not line.strip():
            continue
        if line.strip() == "---":
            continue
        if line.startswith("# "):
            doc.add_heading(line[2:].strip(), level=0)
        elif line.startswith("## "):
            doc.add_heading(line[3:].strip(), level=1)
        elif line.startswith("- "):
            p = doc.add_paragraph(style="List Bullet")
            add_inline(p, line[2:].strip())
        elif line.startswith("Source:"):
            p = doc.add_paragraph()
            run = p.add_run("Source: ")
            run.bold = True
            run.font.size = Pt(9)
            r2 = p.add_run(line[len("Source:"):].strip())
            r2.font.size = Pt(9)
            r2.italic = True
        else:
            p = doc.add_paragraph()
            # whole-line italics (e.g. the coverage note)
            if line.startswith("*") and line.endswith("*") and not line.startswith("**"):
                run = p.add_run(line[1:-1])
                run.italic = True
            else:
                add_inline(p, line)

    doc.save(dst)
    print("wrote", dst)


if __name__ == "__main__":
    main()
