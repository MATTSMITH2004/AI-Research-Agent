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

- **Topic**: which config to use, e.g. `topics/ai-weekly.md`. If I do not name
  one, ask which topic, or infer it if it is obvious from what I said.
- **Window**: the time range to cover. Default to the cadence named in the topic
  config (for ai-weekly, the last 7 days). If I give a range, use that instead.

## Steps

1. **Read the topic config** under `topics/`. It tells you the sources to
   prioritize, the keywords and subtopics to watch, and what to flag. Treat it as
   the brief on what I care about for this topic. Also read `MEMORY.md`: it holds
   preferences learned from my past feedback, what I already know, and what has
   already been covered. Apply all of it.

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
   it matters to me, in my own-words summary. Do not reproduce source text.

8. **Produce the brief as a Word document.** Format using the template below and
   save it as a `.docx` file to `briefs/<topic>-<YYYY-MM-DD>.docx`. (Keep a
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

```
# <Topic> brief — week of <date>

## Top developments
For each (aim for 3 to 5):
- **<Headline in my words>**
  What happened, then why it matters to me. 2 to 4 sentences.
  Source: <link>

## Worth a skim
Shorter items that are relevant but not urgent. One line each, with a link.

## On my radar
Things to watch that have not landed yet, open questions, or threads to follow
next week.
```

If the window was quiet, a short brief with only a Top developments section is
the right answer. Do not pad.

## Notes

- Honor every output preference in CLAUDE.md (plain and direct, no em dashes,
  source links, no invented sources).
- This skill should work for any topic. If something here is AI-specific, it
  belongs in the topic config, not in this file.
