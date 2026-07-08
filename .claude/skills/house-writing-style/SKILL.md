---
name: house-writing-style
description: Matthew's rules for analytical prose. Apply whenever drafting
  analytical writing of any kind — briefs, digests, memos, summaries,
  explanations of news or research. Read this before drafting, not after.
---

# House writing style

These rules were derived from line-level diagnosis of actual output, not
from abstract principles. Each has a before/after from a real brief.
When a rule conflicts with sounding polished, follow the rule.

## 1. Show the transmission mechanism

Every causal claim must walk the reader through each step: a → b → c.
Never state a cause and its distant consequence with the middle missing.
Audit trigger: any sentence using "meaning," "so," a colon, or an em-dash
to carry causal weight. Ask: can the reader reconstruct every step? If
not, unpack it into sequence — even at the cost of more words.

BEFORE: "researchers found a jailbreak that could surface
cyberattack-relevant vulnerabilities — a shutdown that even blocked
Anthropic's own foreign-national employees."
(Jumps from the flaw to a consequence three steps downstream.)

AFTER: "Amazon researchers found a jailbreak: prompts that got the model
to reveal software flaws useful for planning cyberattacks. The government
responded by banning all foreign use of the model. That ban covered
foreign nationals working inside the US — including Anthropic's own
employees — so the company shut off access for everyone rather than
police who could log in."

When relaying someone else's argument, render it as an explicit chain
(their claim is: a, therefore b, therefore c), and if a step contradicts
common intuition (e.g. "demand is set by price"), explain what they
actually mean before moving on.

## 2. Claim first, then evidence

Open every item and every paragraph with a topic sentence stating the
frame. The reader should know what they are about to read and why before
any specifics arrive. Specs, benchmarks, quotes, and numbers follow the
claim — never precede it.

BEFORE: an item that opens with Fable's return, drifts into Sonnet 5
specs, then GPT-5.6 tiers, then Chinese benchmarks, with the point
emerging only by accumulation.

AFTER: "Three frontier models shipped this week: Fable 5 returned,
Anthropic released Claude Sonnet 5, and OpenAI previewed GPT-5.6. Here is
how they compare — and why the benchmark numbers deserve skepticism."
Then the details, in that promised order.

## 3. Gloss jargon once; disambiguate names

No term the reader doesn't already own may carry the significance of a
sentence. Gloss on first use — one clause, plain words — then use the
term freely afterward. Company or product names that read as common nouns
("Together AI," "Exponential") must be introduced so they can't be
misparsed. A term is only worth retaining at all if it will recur;
otherwise use the plain-language version and drop the term.

BEFORE: "Together AI raised an $800M Series C — a 'neocloud' renting
compute for open-source models without hyperscaler lock-in."

AFTER: "Together AI, a startup that rents out GPU computing power for
running open-source models, raised an $800M Series C. Investors are
calling this category 'neoclouds': cloud providers that, unlike Amazon
or Microsoft, don't tie customers to one company's ecosystem."

## 4. Every fact must earn its place — visibly

State each fact's relevance to the point it serves, in the same sentence
or the one after. If the tie-back can't be written, the fact moves to
where it belongs or gets cut. A fact that is true, sourced, and
interesting is still clutter if the reader has to guess why it's here.

BEFORE: "Anthropic shipped Claude Sonnet 5 the same day." (In an item
about the Fable ban — connection never stated.)

AFTER: either cut it from this item, or: "Anthropic shipped Claude
Sonnet 5 the same day — a signal it spent the shutdown building rather
than stalling."

## 5. No idiom unless literally true; no self-narration

Test every idiom and stock phrase: is it literally true of the situation?
"Closed the loop" fails unless something actually loops. If it fails,
say the plain thing: "the situation was resolved."

The document never narrates itself or its predecessors ("last week's
brief covered..."). If prior context is needed, give the context itself;
a pointer to prior coverage goes in a short parenthetical at the end of
the sentence, never as the sentence's subject.

Banned constructions (grows over time):
- "closed the loop" / "come full circle"
- "partial climbdown" and similar editorializing shorthand for events
- "Last week's brief covered..." or any self-referential opener
- "it's not just X, it's Y"
- significance-inflation verbs doing a claim's work: "underscores,"
  "highlights," "signals," "cements," "marks a turning point"
- participial significance tails: ", cementing its position as..."
- "in recent developments" and all throat-clearing openers

## 6. Plain clauses over noun-piles; use the industry's own words

If a hyphenated compound can be replaced by a plain clause, replace it:
"cyberattack-relevant vulnerabilities" → "flaws that could help conduct
cyberattacks." Call things what their industry calls them: "frontier
labs," not "vendors." Cut modifiers that subtract meaning ("targeted
gross margin" → "gross margin").

## 7. Attribute contested facts; own your reads

Two kinds of claims, two treatments:
- Contested or self-reported facts and analytical framings (a company's
  own 99% figure; a revenue-vs-depreciation threshold) get attribution
  AND their limitations noted: whose claim, what it assumes, what it
  leaves out ("depreciation is a proxy for hardware cost, not the full
  cost base").
- Interpretive reads that follow from the analysis are stated flat, in
  the document's own voice, unattributed. Never borrow a quoted source's
  mouth for a conclusion you hold yourself. Quotes confirm points already
  made; they do not carry them.
