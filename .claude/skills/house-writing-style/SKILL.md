---
name: house-writing-style
description: >
  The house rules for how prose is built — voice, causal structure, jargon
  glossing, banned constructions, and attribution — for any writing in Matthew's
  name (the AI Pulse and other briefs, plus memos and drafts). Read and apply this
  before drafting any prose that should read in the house style. It governs the
  sentence-and-paragraph craft; the brief's structure lives in the topic config, and
  brief-level curation lives in the research-digest skill's "Writing and curation
  rules." [DRAFT — workshopped on claude/workshop; not yet live.]
---

# House Writing Style

How the prose itself is built, so everything reads as one publication. This is the
sentence-and-paragraph layer only. It does not define *what* a brief contains (topic
config) or *how a brief is curated* (research-digest's "Writing and curation rules")
— it governs *how the words go together*.

## Voice (the baseline)

- Neutral, third-person publication voice. No second-person "you," no "Matthew,"
  opener, no addressing any one reader. Editorial opinion is welcome but labeled and
  impersonal. (Canonical audience rule: CLAUDE.md "Audience and voice.")
- Direct, concrete, evidence-first. No fluff, no abstraction for its own sake.
- Em dashes are welcome. (Avoid them only in text drafted in Matthew's own voice to
  send to other people, where they read as AI.)

## 1. Causal chains, not lists

Connect points by cause and effect; do not lay them side by side as interchangeable
facts. The reader should be carried from one point to the next by "which means / which
is why / because," not by "and also."

- Weak: "The regime licenses releases. Enterprises are shifting to open models."
- Strong: "Because release timing is now an unlegislated regulatory variable,
  enterprises are hedging into open-weight models they can't have switched off."

Build significance as a single traced line — fact → what it causes → why that
matters — not a pile of true statements sitting next to each other.

## 2. Topic sentence first

Lead every paragraph with its point, then support it. Never bury the conclusion at
the end or make the reader assemble it. One paragraph, one idea; the first sentence
states it, the rest earns it.

- Weak: three sentences of setup, then finally the point.
- Strong: the point first, then the three sentences that back it.

## 3. Gloss the jargon, always

The first time a real technical term, benchmark, or tech-business buzzword appears,
gloss it in a few plain words — what it is and how to read it. Never let an
unexplained term carry the point, even in a one-line item.

- Benchmarks: say what the test measures and what a good score means, not just the
  number.
- Buzzwords ("industrialization of software," "legacy migration," "front door to
  computing") get a plain-words translation.
- Finance fundamentals (margins, valuation, multiples, run-rate) do NOT need
  glossing — Matthew knows them. A vague tech-business phrase built around them
  still does.

## 4. Banned constructions (the AI tells)

Cut these on sight; they read as machine-written or as filler:

- **Hedge/filler openers:** "It's worth noting that," "It's important to remember,"
  "Needless to say," "At the end of the day."
- **Inflated register:** "in the ever-evolving landscape," "in today's fast-paced
  world," "a testament to," "delve into," "tapestry," "realm," "navigate the
  complexities of."
- **Empty both-sidesing as a conclusion:** "only time will tell," "the possibilities
  are endless," "a double-edged sword."
- **Symmetry crutches:** reflexive "Not only X, but also Y," and rule-of-three lists
  that pad rather than build.
- **Throat-clearing:** restating the prompt or the section's own purpose before
  saying anything ("This section examines…").

Say the thing plainly instead. Test: if a sentence survives deletion of its first
few words, delete them.

## 5. Attribution discipline

- Separate fact from the writer's read. If a claim comes from a source, it is
  reported and cited; if it is the writer's synthesis or opinion, it is labeled as
  such. Never blur the two inside one sentence.
- Prefer primary sources, and attribute a claim to whoever actually made it — not to
  a secondhand write-up of it.
- When a named voice is used, keep the attribution honest about what they actually
  said versus how it is being framed.

(Brief-level rules — crediting every named person, a source link on every item,
restating a cross-referenced item before contrasting it — live in research-digest's
"Writing and curation rules," which sits on top of this skill.)

## Relationship to the other files

- `CLAUDE.md` holds identity, the lenses, and the canonical audience/voice rule;
  this skill is the prose-craft layer that operationalizes it. If they ever conflict,
  `CLAUDE.md` and `MEMORY.md` win per the precedence rule.
- `research-digest` reads this at step 7, then applies its brief-level "Writing and
  curation rules" on top.
- Keep this file to prose craft. Anything about *what to cover* or *brief structure*
  belongs in the topic config, not here.
