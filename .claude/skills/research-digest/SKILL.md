---
name: research-digest
description: >
  Produces a research brief on a topic by gathering recent developments,
  filtering and ranking them, and writing them up in my preferred brief format.
  Use this skill whenever I ask for a brief, digest, recap, roundup, or
  "what's new" on a topic, or when I name one of the topics under topics/
  (for example "run my AI weekly"). Also use it when I ask to catch up on a
  subject over a date range.
---

# Research Digest

Produce a brief on a single topic for a given time window. The topic specifics
live in a config file under `topics/`. This skill is the procedure; the config
is the subject matter. One skill, many topics.

## Inputs

- **Topic**: which config to use, e.g. `topics/ai-pulse.md`. If I do not name
  one, ask which topic, or infer it if it is obvious from what I said.
- **Window**: the time range to cover. Default to the cadence named in the topic
  config (for ai-pulse, the last 7 days). If I give a range, use that instead.

## Steps

1. **Read the context.** `CLAUDE.md` (the fixed foundation — who I am, the lenses,
   and the voice and sourcing rules) loads automatically at the start of the
   session, so it is already in context; apply it. Then read the **topic config**
   under `topics/` — the canonical template for this topic: the sources to
   prioritize, the subtopics to watch, what to flag, and the exact output shape —
   and `MEMORY.md`, which holds preferences learned from my past feedback, what I
   already know, and what has already been covered. Apply all of it. If the three
   ever conflict, follow the precedence rule in `CLAUDE.md`: never block the brief on
   a contradiction — `MEMORY.md` always takes precedence over everything, so apply
   its side and keep going, then note the contradiction at the bottom of the brief
   (the topic config's closing "Config notes" item) for me to resolve later.
   While reading, spot-check MEMORY's pointer bullets against their owner files.
   If MEMORY describes a rule differently than the file that owns it, follow the
   owner and note the mismatch in Config notes — a stale summary in MEMORY is a
   bug in MEMORY, not an override (see MEMORY's "write pointers, not copies").

2. **Gather the written sources.** Work through each written source listed in the
   config, and also search the open web broadly, with several focused searches
   across the subtopics rather than one query. The listed sources are the minimum
   to cover, not the limit: actively look beyond them, follow leads to sources not
   on the list, and pull in anything genuinely relevant wherever it comes from,
   including material tangential to AI that still connects to my interests. Open
   the actual source for anything promising rather than relying on a snippet.

3. **Work through the video and podcast sources. This pass is mandatory, not an
   optional extra, and web search does not substitute for it.** Go through every
   show listed in the config's video and podcast section, one at a time, and get
   its content for the window as text:
   - The AI Daily Brief: read the web editions at aidailybrief.ai directly (full
     text, no audio needed).
   - Shows that publish a transcript, episode page, show notes, or Substack post:
     fetch that page.
   - YouTube channels: pull the video's transcript (captions).
   - Freshness check (No Priors, Dwarkesh, Greg Isenberg — the shows rerouted
     to podscripts): the lister cross-checks each show's YouTube channel and
     marks any in-window episode not yet on podscripts as YouTube-only. Fetch
     those via captions. If captions are blocked this session (the fetch error
     says so plainly), use the episode's official description plus third-party
     recaps and record the gap in the coverage note.
   Cite the specific episode with a link. If you truly cannot get text for a given
   source this week, do not silently skip it. These shows are where the analysis
   and operator angles live, so they are not optional color.

4. **Filter to the window.** Drop anything older than the window unless it is
   clearly still the latest state of an ongoing story. Be strict about dates.

5. **Dedupe.** Collapse multiple write-ups of the same event into one item,
   keeping the most primary source.

6. **Rank by relevance to me.** Use the context file, the topic config, and
   `MEMORY.md` to judge what is genuinely new and material *to me*, not just
   generally popular. Demote anything I already know or that was already covered in
   a recent brief (both tracked in `MEMORY.md`).

7. **Synthesize.** Before drafting a single sentence, read the `house-writing-style`
   skill and apply every rule in it — it governs how the prose itself is built
   (causal chains, topic-sentence-first, jargon glossing, banned constructions, sourcing numbers with their limits). Then, for each item that makes the cut, write what
   happened and why it matters, judged through my lenses, in your own words and in
   the neutral voice set by `CLAUDE.md` and the topic config (not addressed to a
   reader). Do not reproduce source text. The "Writing and curation rules" section
   below adds brief-level enforcement on top of the house style.

   **The revision pass.** After drafting each item, run these four checks as
   separate acts, not as a drafting-time intention. Each is a thing you do and
   finish, in order:

   1. **Paragraphs.** Count the sentences in each paragraph. Split any past
      five at a natural seam. Count, then split — do not eyeball it.
   2. **Jargon, then companies.** For every term of art, ask whether the reader
      profiled in CLAUDE.md — finance-fluent, economics-solid, no technical
      background — already owns that word. Finance vocabulary passes unglossed.
      Any technical, AI, or industry term fails and gets a plain-language gloss
      on first use (house-writing-style rule 3). A term the drafter did not
      notice as jargon is the one most likely to fail — check nouns that would
      not appear in a finance textbook.

      Then, separately: **list every company named in this item, and for each
      one point to where its three parts appear** — what it sells, to whom, and
      why it is in this story. This is an enumeration, not a scan: an item names
      perhaps three to eight companies, and the check is finished when every one
      has been accounted for. Household names (Apple, Google, Amazon) are the
      only exemption. A company you cannot write the three parts for is one you
      do not understand well enough to have included — go find out or cut it.
      No script covers this; the enumeration IS the enforcement.
   3. **Causal chains.** Rebuild every causal claim and every relayed argument
      step by step: a, therefore b, therefore c (rule 1). If a middle step
      cannot be written down, find it in the source or cut the claim. A reader
      asking "why?" at a sentence marks exactly where this check was skipped.
   4. **Sentences.** Split any sentence that stacks a second idea onto a comma
      tail (rule 8). A labelled beat is not a licence for one long sentence —
      a "Both sides" bullet runs two to four short sentences per side.
   5. **Grammar.** Read every sentence for grammatical completeness. A sentence
      that cannot be read cleanly gets rewritten, not patched.
      BEFORE (week of Jul 25): "…the rest of the open-weight field is not as far
      ahead as it is being covered as catching up to." AFTER: "…the rest of the
      open-weight field may be less independently capable than its benchmark
      scores suggest."

   Then run the mechanical check over the whole draft, which catches what a
   read-through reliably misses:

       python3 scripts/check_prose.py briefs/<topic>-<date>.md

   It reports run-on sentences, over-long paragraphs, sections and Source lines
   carrying no hyperlinks, unglossed terms from the topic config's glossary
   roster, and banned constructions, each with a line number. Work the list: fix
   what it flags, and where a flag is a false positive, leave it and move on.
   The glossary check never asks you to drop a term — use the real word and
   gloss it, per CLAUDE.md's jargon rule; the flag means the explanation is
   missing, not the term. Two of its numbers are about the document rather than any one line
   — median sentence length and the share of sentences over rule 8's trigger.
   A median much above ~20 words, or a rate much above ~25%, means check 4 did
   not bind and the draft needs another pass, not a few spot fixes. (For scale:
   the Jul 25 brief ran a 29-word median with 53% over trigger.) The script
   flags; you judge.

8. **Produce the brief as a Word document.** Format it using the topic config's
   output shape as the canonical structure (for ai-pulse, the "Output shape"
   section). Save it as a `.docx` file to `briefs/<topic>-<YYYY-MM-DD>.docx`. (Keep a
   markdown copy alongside it if convenient, but the Word doc is the deliverable.)
   Run `scripts/check_prose.py` once more on the final markdown before
   rendering. Every flag must be RESOLVED before rendering — fixed, or judged a
   false positive on purpose. That is the gate: not a zero count, but no flag
   left unexamined. The script reports candidates; the judgment stays yours.
   Then give me the highlights inline.

9. **Report what you reached.** Before or with the highlights, tell me plainly
   which written sources, podcasts, and YouTube channels you actually pulled from
   this week, and name any from the config you could not reach. Also flag any
   strong source you found outside the config that I might want to add. This keeps
   the source coverage honest and visible rather than silently partial.

10. **Update memory and route feedback.** After the brief is done:
    - Update `MEMORY.md` with STATE only: add what you reported to the
      "recently covered" list and trim past ~4-6 weeks; update the model ledger
      if a covered release moved the standings; update the source-discovery
      ledger's hit/miss marks. Do not write style or structure rules here.
    - If I gave feedback this session, route it by kind:
      - Prose/writing-craft (how sentences are built, word choice, banned
        constructions, causal-chain or topic-sentence rules) → propose an edit
        to the `house-writing-style` skill.
      - Brief-shape or coverage (beats, sections, ordering, ranking, what to
        cover or exclude, sources, recurring voices) → propose an edit to the
        topic config.
      - Only durable cross-topic preferences that are neither → MEMORY.md.
    - For anything routed to a skill or config file, state the exact edit and
      where it goes, and output it as a paste-ready block rather than writing
      the file yourself. Record standing rules only, not one-offs; if a rule is
      ambiguous, confirm before saving.

## Writing and curation rules

The `house-writing-style` skill (read at step 7) governs the prose itself. These
rules sit on top of it and apply to every brief regardless of topic. Anything
topic-specific — per-section voice mapping, content exclusions, ranking priors —
lives in the topic config, not here.

- **Section headers bind to their object.** Any header that interrogates or
  qualifies something must name it. The header alone should tell me what is
  examined.
  - Before: `Does it hold up?`
  - After: `Does the 99% figure hold up?`

- **Every fact ties back to the item it lives in.** State the relevance in the
  same sentence or the next. If a fact belongs to a different item, move it; if
  it belongs nowhere, cut it.
  - Before (inside the Fable-ban story): "Anthropic shipped Claude Sonnet 5 the
    same day." — true, but the reader can't tell why it's in a story about the
    ban.
  - After: either cut it, or connect it — "Anthropic shipped Claude Sonnet 5 the
    same day, a sign it spent the shutdown building rather than stalling." If the
    only real home is a models-comparison item, move it there.

- **Bullets build, not enumerate.** If two bullets in a significance section
  share a causal link, connect them explicitly — one flowing into the next —
  rather than listing them as parallel, interchangeable points.
  - Before: one bullet says a licensing regime now exists with no law behind it;
    a separate bullet says enterprises are shifting spend to Chinese open-weight
    models. Presented as two unrelated facts.
  - After: make the causal line the spine — "Because release timing is now an
    unlegislated regulatory variable, enterprises are hedging: Coinbase already
    cut its AI bill in half by defaulting to open-weight models like GLM 5.2."
    The second point is the consequence of the first, not a neighbor to it.

- **Every item carries a source link**, including short skim-list items. No
  exceptions. A named source is a linked source: every primary document,
  letter, filing, edition, or episode named in the text gets its own
  hyperlink, at the point of naming or on the Source line, and "What people
  are saying" entries link the specific transcript or post actually read, not
  just the show's homepage.
  - Before: "Microsoft launched..." / "Meta barred its internal..." — stated flat
    with no link.
  - After: same claim, with the primary source linked inline. If no source can be
    found, the item doesn't run.

- **Credential every named person, every time — with enough to judge them by.**
  A credential names four things: the person's role, the organisation, what that
  organisation actually does, and what specifically qualifies them on this
  subject — prior roles, the work they are known for, or the institution's
  standing. A job title alone fails. "An economist" fails; "an economist at X"
  still fails. This holds on every mention, not just the first, whether or not
  they are quoted, and it includes podcast hosts, co-hosts, and guests —
  everyone named in a "What people are saying" entry.
  - Before: "Interconnects (Nathan Lambert, post-training researcher)"
  - After: "Nathan Lambert, a research scientist at the Allen Institute for AI —
    a nonprofit AI research lab — who specialises in how models are refined
    after their initial training and writes the Interconnects newsletter"
  - Before: "...as Dean Ball put it, 'this opacity will not lend itself well to a
    stable, investable industry.'"
  - After: "...as Dean Ball, OpenAI's policy lead and previously an AI policy
    advisor in the Trump administration, put it: 'this opacity will not lend
    itself well to a stable, investable industry.'"

  **Never an unnamed attribution.** No "one commentator," "an analyst," "some
  observers," or any claim attributed to a person who is not named. If the
  person cannot be named and credentialed, the claim does not run.

  Keep it to a clause or two, not a biography — a name recurring inside one item
  gets a light tag on later mentions, not the full treatment repeated. Pull
  standing wording from the topic config's recurring-voices roster where one
  exists, so the description stays consistent across weeks.

- **Cross-references restate before contrasting.** Referencing another item is
  encouraged, but restate what that item said in one clause before drawing the
  contrast — never assume I hold it in memory.
  - Before: "His price-reversal prediction is a direct, contrarian challenge to
    this week's Item 4 above — worth watching which read wins."
  - After: "Item 4 above argued memory prices will keep climbing on AI demand;
    his prediction is the opposite — that prices reverse as capacity catches up.
    Worth watching which read wins."
    
## Brief format

The brief's structure is defined by the **topic config**, not here. Follow its
"Output shape" section as the canonical template. Keep the format in one place — do not carry
a second, drifting copy in this file.

For a topic whose config does not define an output shape, fall back to a simple
structure: a "Top developments" list (3 to 6 items, each a headline in my words,
then what happened and why it matters, then a Source link), then "Worth a skim,"
then "On my radar."

If the window was quiet, a short brief is the right answer. Do not pad.

## Notes

- Honor every output preference in CLAUDE.md (plain and direct, always source,
  no invented sources, and the voice and tone rules — including that em dashes are
  welcome in the brief).
- This skill should work for any topic. If something here is AI-specific, it
  belongs in the topic config, not in this file.
