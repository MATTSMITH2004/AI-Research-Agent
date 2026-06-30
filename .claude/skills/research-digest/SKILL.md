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

7. **Synthesize.** For each item that makes the cut, write what happened and why
   it matters, judged through my lenses, in your own words and in the neutral voice
   set by `CLAUDE.md` and the topic config (not addressed to a reader). Do not
   reproduce source text.

8. **Produce the brief as a Word document.** Format it using the topic config's
   output shape as the canonical structure (for ai-pulse, the "Output shape"
   section, and match the worked example in `templates/` if the topic provides
   one). Save it as a `.docx` file to `briefs/<topic>-<YYYY-MM-DD>.docx`. (Keep a
   markdown copy alongside it if convenient, but the Word doc is the deliverable.)
   Then give me the highlights inline.

9. **Report what you reached.** Before or with the highlights, tell me plainly
   which written sources, podcasts, and YouTube channels you actually pulled from
   this week, and name any from the config you could not reach. Also flag any
   strong source you found outside the config that I might want to add. This keeps
   the source coverage honest and visible rather than silently partial.

10. **Update memory.** After the brief is done, update `MEMORY.md` in place:
    - Add the items you just reported to the "recently covered" list for this
      topic, and trim entries older than roughly the last 4 to 6 weeks.
    - If I gave feedback this session (on style, sources, emphasis, or what I
      already understand), fold it into the right section as a durable rule.
      Replace any entry it supersedes rather than appending a new one. Record only
      standing preferences, not one-offs, and if a rule is ambiguous, state it
      back to me before saving it.

## Brief format

The brief's structure is defined by the **topic config**, not here. Follow its
"Output shape" section as the canonical template, and match the worked example in
`templates/` if the topic provides one. Keep the format in one place — do not carry
a second, drifting copy in this file.

For a topic whose config does not define an output shape, fall back to a simple
structure: a "Top developments" list (3 to 5 items, each a headline in my words,
then what happened and why it matters, then a Source link), then "Worth a skim,"
then "On my radar."

If the window was quiet, a short brief is the right answer. Do not pad.

## Notes

- Honor every output preference in CLAUDE.md (plain and direct, always source,
  no invented sources, and the voice and tone rules — including that em dashes are
  welcome in the brief).
- This skill should work for any topic. If something here is AI-specific, it
  belongs in the topic config, not in this file.
