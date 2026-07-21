---
name: brief-feedback
description: >
  Processes Matthew's commented feedback on a brief. Use whenever Matthew
  uploads a Word document containing margin comments on a past brief, or asks
  to process, ingest, or apply his brief feedback. Extracts every comment,
  classifies and routes it under CLAUDE.md's routing doctrine, checks proposed
  rules against existing ones, and presents a proposal memo for Matthew to
  ratify. NEVER edits a rule file before ratification.
---

# Brief feedback

Turn margin comments on a brief into correctly-routed, conflict-checked
changes — with Matthew as the ratification step. The failure mode this skill
exists to prevent is silent rule-drift: a misread comment hardening into a
standing rule that quietly degrades every future brief. So the procedure is
extract → classify → route → conflict-check → propose → STOP for verdicts →
apply only what was approved.

## Step 1 — Extract every comment with its anchored text

Comments live in the docx XML, not the visible text. Unzip the .docx and
parse:
- `word/comments.xml` — comment id, author, text.
- `word/document.xml` — for each id, collect the text between its
  `commentRangeStart` and `commentRangeEnd` markers. That anchored text is
  what the comment is about; a comment without its anchor is ambiguous.

Produce a numbered list: comment text + anchored passage + which brief
section it sits in. Process every comment — never sample or skip. If a
comment anchors to a point rather than a range, note the surrounding
paragraph.

## Step 2 — Classify each comment

Seven kinds. When genuinely torn between two, mark it ambiguous and ask in
the memo rather than guessing.

1. **One-off fix** — about this brief only. No rule implied.
   Example: "We should also mention the risk of this revenue concentration"
   (anchored to a chips-revenue stat). The fix is one-off; note it also
   dual-classifies as evidence against the walk-the-full-chain rule (see
   boundary note below).

2. **Violation of an existing rule** — the comment describes a failure a
   standing rule already prohibits. This is NOT a duplicate to ignore; it is
   evidence the rule did not bind, and the proposal is an ENFORCEMENT
   SHARPENING: an audit trigger, a revision-pass check, or a named example
   added to the rule — following the house pattern that a rule must be a
   checkable act, not an aspiration.
   Example: "What are parameters" anchored to "a 2.8-trillion-parameter
   model" — the gloss-jargon rule exists and failed. Propose sharpening
   (e.g., a post-draft jargon sweep), not a new rule.
   Example: "I always want credentials on people" / "Even guests on a show" —
   the credential rule exists; the sharpening names guests explicitly.

3. **New standing rule** — a generalizable instruction no current rule
   covers. The tell: "always," "never," "every time," a self-generalization,
   or the same complaint anchored in 2+ places.
   Example: "I feel a general trend of sentences being too long, almost run
   ons" — self-generalized; no sentence-length rule exists; draft one for
   house-writing-style with a check and a before/after.

4. **Feature request or design question** — asks for new capability,
   persistent structure, or a format change that alters how the whole brief
   renders. Not a rule; route to a design conversation. Never draft these as
   file edits.
   Example: "This is terrible... maybe best, second best, third best... we
   need to discuss this part further" (Model standings) — explicit design
   flag.
   Example: "Should we use Artificial Analysis going forward for the model
   table" — a question about method and sources; design conversation.
   Example: a request that every sentence visibly correspond to its source —
   changes the rendering of every item; design conversation, not a routed
   rule.

5. **Curation/state** — coverage, ranking, sources, or what Matthew already
   knows. Example: "This one should be lower regardless" (ranking, one-off);
   "cut this kind of story" (standing, topic config).

6. 6. **Positive signal** — something that worked. Do not let praise die in the
   memo; convert it into durable reinforcement:
   - If the praised passage exemplifies a specific rule, propose harvesting
     it (trimmed to 1-3 sentences) as a real-brief AFTER example under that
     rule in house-writing-style — praised output from actual briefs
     outranks synthetic examples.
   - If the praise is structural (a beat, a sequence, a format choice),
     propose a "confirmed working" line in the topic config so the choice is
     protected against later restructuring.
   - If the praise attaches to no existing rule, surface it in the memo as a
     possible unarticulated rule — praise without a rule is sometimes the
     first sighting of one.
   - Never collect praised passages into a free-floating exemplar gallery;
     a positive example only teaches when attached to the rule it
     demonstrates.
   As before: if a proposed rule from the same doc would undermine a praised
   behavior, surface the tension.
   Example: "Very good what happened and does it hold up section" → propose
   harvesting two sentences of that item as an AFTER under the claim-first
   rule, plus a confirmed-working line for the beat sequence in the topic
   config.

7. **Unclassifiable** — the comment fits none of the kinds above. Do not
   force-fit it into the nearest kind. Put it in the memo's decisions-needed
   group with a proposed NEW category (name, definition, routing, and how it
   would have classified this comment). If Matthew ratifies the category, add
   it to this skill file as part of applying the verdicts — the taxonomy
   grows, but only through ratification.

Classification notes:
- A margin QUESTION ("Cement what?", "What is a stopgap release?") is
  confusion evidence: the brief failed the reader at that spot. Classify by
  what failed (usually a rule violation — unglossed term, broken chain,
  vague referent). Do not treat it as a question to answer in the memo.
- Before finalizing a one-off, check whether an existing rule, generously
  read, already prohibits the failure (e.g., "mention the risk of this
  concentration" is a one-off fix AND a miss against CLAUDE.md's
  every-item-carries-its-significance / walk-the-full-chain rule). If so,
  dual-classify: route the fix as a one-off, and record the item under
  enforcement failures as evidence against that rule — without proposing a
  sharpening unless the same rule has failed on multiple anchors.
- "I don't love X" about a word or phrase is a one-off unless the same
  species of complaint anchors in 2+ places, in which case propose a
  banned-constructions addition or a specificity rule.
- A jargon complaint is a gloss failure, not a word ban: the term stays, the
  explanation was missing. Never propose adding domain terms to the banned
  list — banned constructions are for phrases Matthew never wants (dead
  idioms, self-narration), not vocabulary that needed teaching.
- A single complaint about a single passage stays a one-off unless the
  comment itself generalizes. Do not promote irritation into permanent rules.

## Step 3 — Route per CLAUDE.md's routing doctrine

- Prose/writing craft → `house-writing-style` skill.
- Brief shape, beats, coverage, ranking, sources, recurring voices → the
  topic config under `topics/`.
- Digest procedure (steps, gathering, output mechanics) → `research-digest`.
- One-off fixes → MEMORY.md's "One-off requests for the next brief" section
  (its action-then-delete discipline handles expiry).
- Curation/state and cross-topic preferences fitting nothing above →
  MEMORY.md.
- Feature requests and design questions → no file; flag for a design
  conversation with Matthew.
- Enforcement sharpenings route to wherever the failed rule lives — and if
  the sharpening is a revision-pass check, it lands in research-digest step 7
  alongside the paragraph and jargon checks, since that is where post-draft
  enforcement runs.

## Step 4 — Conflict-check before proposing

For every proposed rule or sharpening, read the destination file and check:
- **Duplicate**: an existing rule already fully covers it and the brief
  complied → propose nothing. (If the brief did NOT comply, it is a
  violation — kind 2 — and gets a sharpening, not silence.)
- **Conflict**: it contradicts an existing rule in any file → do not pick a
  winner. Present both, name the tension, offer options. Apparent conflicts
  are often scope splits (principle in one file, enforcement in another);
  propose the split where it fits.
- **Supersession**: it replaces an existing rule → propose replace-not-
  append, quoting what it would remove.

## Step 5 — The proposal memo, then STOP

One memo, grouped in this order:
1. Decisions needed — conflicts, ambiguous classifications, design
   questions, and any proposed new categories. Options, not a single
   recommendation.
2. Enforcement failures — the failed rule, the evidence (comment + anchor),
   and the drafted sharpening. Dual-classified one-offs appear here as
   evidence lines even when no sharpening is proposed yet.
3. New standing rules — each with source comment, destination, and the exact
   paste-ready edit, written in the house register: a check with an audit
   trigger and a before/after where possible. A rule that cannot be checked
   will not bind.
4. One-offs and curation — one line each.
5. Positive signals — what to protect.

Presentation rules for every memo item (added Jul 2026 after Matthew had to
ask for both — the memo must answer these in place, not on request):
- Ground every item in the brief itself. Quote the actual passage the
  comment anchored to (the BEFORE), then show what that same passage would
  look like under the proposal (the AFTER). For a design question, mock each
  option on that passage so the choices are visible, not abstract. Never
  present a proposal as a label plus a classification — if Matthew would
  need to ask "what do you mean, give me an example," the item is not done.
- Name the destination precisely. Every proposed edit states the file AND
  the section or anchor within it ("topics/ai-pulse.md, the Intro bullet
  under Output shape") so the where gets ratified along with the what, and
  no follow-up "where is this going" round is needed.

Then stop. Ask Matthew to verdict each item: approve / edit / reject /
defer. Apply nothing — including "obvious" one-offs — before verdicts.

## Step 6 — Apply only what was ratified

Apply approved edits exactly as ratified, on a `claude/`-prefixed branch per
the standing git rules, replacing what each edit supersedes rather than
appending. Rejected items are dropped without residue. Deferred items and
design flags get one line in the closing summary so they are findable — they
are NOT written into any rule file as pending.

Close with a two-line summary: N comments → N one-offs queued, N sharpenings
and N rules landed (by file), N design items open.

## Boundaries

- This skill never edits CLAUDE.md — foundation changes are always a direct
  conversation, not a feedback-routing outcome.
- It never resolves a rule conflict on its own authority, and never infers a
  standing rule from tone alone.
- If the uploaded document has no comments, say so and stop — do not infer
  feedback from the skill text itself.
