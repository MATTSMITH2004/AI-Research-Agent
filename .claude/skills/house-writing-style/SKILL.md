---
name: house-writing-style
description: >
  Matthew's enforcement layer for analytical prose. Must apply whenever drafting
  any written deliverable — briefs, digests, memos, summaries, explanations.
  Read it before drafting, not after. CLAUDE.md sets the voice, calibration,
  and sourcing principles; this skill is the teeth: the specific constructions
  to avoid and the mechanical checks that make those principles actually bind.
  It governs written deliverables, not the agent's chat replies to Matthew.
---

# House writing style

CLAUDE.md already states the principles — gloss jargon once, explain in a
linear sequence, fact then proof then so-what, separate fact from read. Those
kept getting stated and violated anyway. This skill exists because a principle
without an enforcement check does not bind. Each rule below is a check with a
before/after, most drawn from real briefs. When a rule fights sounding
polished, follow the rule.

## 1. Show the transmission mechanism

Every causal claim walks each step: a → b → c. Never state a cause and a
downstream consequence with the middle cut out. Audit trigger: any sentence
using "meaning," "so," a colon, or an em-dash to carry causal weight — stop and
check the reader can rebuild every step.

BEFORE: "researchers found a jailbreak that could surface cyberattack-relevant
vulnerabilities — a shutdown that even blocked Anthropic's own foreign-national
employees."
(Jumps from the flaw to a consequence three steps downstream.)

AFTER: "Amazon researchers found a jailbreak: prompts that got the model to
reveal software flaws useful for planning cyberattacks. The government responded
by banning all foreign use of the model, out of fear that hostile actors would exploit that capability. That ban covered foreign nationals
working inside the US — including Anthropic's own employees — so the company
shut off access for everyone rather than police who could log in."

When relaying someone's argument, render it as an explicit chain (their claim
is a, therefore b, therefore c). If a step contradicts common intuition (e.g.
"demand is set by price"), explain what they actually mean before moving on.

## 2. Claim first, then evidence

Open every item and paragraph with a topic sentence stating the frame. The
reader knows what they are reading and why before any specifics land. Specs,
numbers, benchmarks, quotes follow the claim — never precede it.

BEFORE: an item that opens on Fable's return, drifts into Sonnet 5 specs, then
GPT-5.6 tiers, then Chinese benchmarks, with the point emerging only by
accumulation.

AFTER: "Three frontier models shipped this week — Fable 5 returned, Anthropic
released Claude Sonnet 5, and OpenAI previewed GPT-5.6 — and the benchmark
numbers deserve more skepticism than they got." Then the details, in that order.

## 3. Gloss jargon once; disambiguate names

No term the reader does not already own may carry the significance of a
sentence. Gloss on first use — one plain clause — then use it freely. A term is
worth keeping only if it recurs; otherwise use the plain version and drop it.
Company or product names that read as common nouns must be introduced so they
cannot be misparsed.

BEFORE: "Together AI raised an $800M Series C — a 'neocloud' renting compute for
open-source models without hyperscaler lock-in."
(Three unglossed terms; "Together AI" can read as "AI in general.")

AFTER: "Together AI, a startup that rents out GPU computing power for running
open-source models, raised an $800M Series C. Investors call this category
'neoclouds': cloud providers that, unlike Amazon or Microsoft, don't tie
customers into one company's ecosystem — the bundle of connected services like databases, storage, and security tools that your systems get built around, which is what makes a big provider like Amazon or Microsoft expensive to leave once you're in."

## 4. Every fact earns its place — visibly

State each fact's relevance to the point it serves, in the same sentence or the
next. A fact that is true, sourced, and interesting is still clutter if the
reader has to guess why it is here. If the tie-back can't be written, the fact
moves to where it belongs or gets cut.

BEFORE (inside the Fable-ban item): "Anthropic shipped Claude Sonnet 5 the same
day." (True, but why is it in a story about the ban?)

AFTER: either cut it, or connect it — "Anthropic shipped Claude Sonnet 5 the
same day, a sign it spent the shutdown building rather than stalling."

## 5. No idiom unless literally true; no self-narration

Test every idiom: is it literally true of the situation? "Closed the loop"
fails unless something loops. If it fails, say the plain thing. And the document
never narrates itself or its past editions ("last week's brief covered...") — if
prior context is needed, give the context; a pointer to earlier coverage goes in
a short parenthetical at the end of a sentence, never as the sentence's subject.

BEFORE: "This week closed the loop on the Fable saga. Last week's brief covered
the first climbdown."
AFTER: "Commerce fully lifted the export controls this week, and Anthropic
restored Fable worldwide (the first partial reprieve came a week earlier)."

Banned constructions (extend over time):
- "closed the loop" / "come full circle"
- editorializing event-shorthand: "partial climbdown," "saga," "drama"
- self-referential openers: "last week's brief covered..."
- "it's not just X, it's Y"
- significance-inflation verbs standing in for a claim: "underscores,"
  "highlights," "signals," "cements," "marks a turning point"
- participial significance-tails: ", cementing its position as..."
- throat-clearing openers: "in recent developments," "in a move that..."

## 6. Plain clauses over noun-piles; use the industry's own words

If a hyphenated compound can be a plain clause, make it a plain clause. Call
things what their field calls them. Cut modifiers that subtract meaning.

BEFORE: "cyberattack-relevant vulnerabilities" / "vendors" / "targeted gross
margin"
AFTER: "flaws that could help conduct cyberattacks" / "frontier labs" / "gross
margin"

## 7. A number carries its source and its limits

Self-reported figures and analytical proxies never stand alone as settled fact.
Say whose number it is, and in one clause what it assumes or leaves out. This is
not hedging — it is the difference between reporting a measurement and endorsing
a conclusion the measurement doesn't fully support.

BEFORE: "Q1 revenue exceeded depreciation for the first time — the industry is
now profitable."
AFTER: "Q1 revenue exceeded depreciation for the first time, per Exponential
View's estimate — though depreciation is a proxy for hardware cost, not the full
cost base, so 'profitable' overstates it."
