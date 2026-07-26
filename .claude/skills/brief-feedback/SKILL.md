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

## Step 0 — Audit the previous round

Before reading a single new comment, verify the last round actually landed.
This runs first because its findings change how the new comments are read: a
complaint that repeats last round's is not a new rule, it is evidence the last
fix did not bind.

1. Read the most recent `feedback/*-ratified.md` record.
2. For each item, check the file it landed in — confirm the ratified wording
   is still there and has not been overwritten by a later edit.
3. For each item with an observable check, examine the brief now under comment
   and mark it **applied**, **partially applied**, **not applied**, or **not
   yet testable** (no occasion arose this week — carry it forward, never score
   it as a pass). An item may only be marked applied on MECHANICAL evidence: a
   grep, a count, a named line quoted from the brief. Where no mechanical check
   exists, mark it **unverified** — never applied — and carry it forward.
   Run `scripts/check_prose.py` on the brief as part of this step; it covers
   sentence length, links, glossing, and banned constructions directly.
   This rule exists because the Jul 25 audit marked three items "applied
   (qualitative)" on a skim and all three had failed: the causal-chain rule
   (five reader complaints), the gloss rule (Databricks, the rule's own worked
   example, unglossed), and the stand-in-words rule. A spot-check is not an
   audit.
4. For anything not applied, diagnose why before proposing anything. Known
   causes, in order of likelihood: a stale copy of the old rule survives in a
   higher-precedence file (the Jul 25 failure — the topic config had the new
   spec, MEMORY still described the old one); the rule reads as an aspiration
   rather than a checkable act; it landed in a file the drafting step does not
   read at the right moment; or it conflicts with another rule that won.
   Re-ratifying the same words fixes none of these.
5. Look for clustering. Several failures in one section of the brief usually
   means one shared cause, not several independent ones — in the Jul 25 audit
   a single stale note suppressed three separate ratified changes, all inside
   "What people are saying."
6. Write the results into the memo's first group, and fill in the Result
   column of that round's record.

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

Archive the upload. Copy the document to `feedback/` as
`ai-pulse-<YYYY-MM-DD>-feedback.docx`, dated for the brief it comments on
(matching that brief's filename in `briefs/`), so the raw input behind every
rule change stays traceable. It gets committed in Step 6 alongside whatever
was ratified — including a round where Matthew rejects everything, since the
document is the record either way. Its companion
`ai-pulse-<YYYY-MM-DD>-ratified.md` record is written in Step 6, once the
verdicts are in.

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

**Sweep every rule file, not just the destination.** Before proposing an edit,
search all four — `CLAUDE.md`, `topics/*.md`, `house-writing-style`,
`research-digest` — plus `MEMORY.md`, for any passage describing the same rule,
using the rule's distinctive words (a beat label, a section name, a format
term). Editing the owner file while a second file still describes the old
version does not produce a visible conflict; it produces a silent override,
since MEMORY outranks the others and the two files never look like they
disagree. Every stale copy found is part of the proposed edit — deleted, or
reduced to a pointer — and is listed in the memo under the item that supersedes
it, so what gets ratified is the whole change, not just its best-known half.
Two real cases: the Jul 18 round moved "What people are saying" to three-layer
entries in the topic config while MEMORY kept describing the two-layer form,
and the next brief silently used the old format; the same round rewrote the
model-ledger sourcing rule in MEMORY while the topic config kept the superseded
"briefs only, no fresh searches" wording.

## Step 5 — The proposal memo, then STOP

One memo, grouped in this order:
1. Last round's audit (Step 0) — what was ratified, what landed, what did
   not, and for each failure the diagnosis plus a proposed fix aimed at the
   cause rather than a restatement of the rule. Items still not yet testable
   carry forward, named.
2. Decisions needed — conflicts, ambiguous classifications, design
   questions, and any proposed new categories. Options, not a single
   recommendation.
3. Enforcement failures — the failed rule, the evidence (comment + anchor),
   and the drafted sharpening. Dual-classified one-offs appear here as
   evidence lines even when no sharpening is proposed yet.
4. New standing rules — each with source comment, destination, and the exact
   paste-ready edit, written in the house register: a check with an audit
   trigger and a before/after where possible. A rule that cannot be checked
   will not bind.
5. One-offs and curation — one line each.
6. Positive signals — what to protect.

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

Then verify, in two separate passes. They catch different things, and running
only the first is how the Jul 26 round shipped four conflicts.

**Pass 1 — no superseded copy survives.** Re-search the rule files for the
distinctive wording of each ratified change and confirm the old version is gone
everywhere. A ratified edit is not applied until it is the only version in the
repo.

**Pass 2 — the new rules do not contradict the old ones.** Pass 1 only proves
the text you replaced is gone; it says nothing about whether what you wrote can
coexist with rules you never touched. For each newly written rule, find every
existing rule that governs the same object — the same beat, section, artifact,
or term — read them together, and ask whether a run obeying both could satisfy
both. Four shapes to look for, each drawn from a real conflict this pass caught
on Jul 26:

- **A cap the new rule exceeds.** The recurring-voices roster said to write a
  credential "as a clause" while the new credential rule required four
  components. Fix: the lookup defers to the rule for depth instead of setting a
  length itself.
- **A prohibition the new rule requires you to break.** "Do not compress any
  perspective source" read as forbidding the new fold-a-source-into-an-item
  rule. Fix: scope them — one governs depth of an entry that earned its slot,
  the other governs selection.
- **A spec that never mentions the new rule's subject.** The sentence-length
  rule for "Both sides" landed in two skills but not in the beat's own spec,
  where the section is built. Fix: put it where the thing is made.
- **The same check described with different force in two files.** Step 8 called
  the prose checker's output "gates," the script called them "candidates." Fix:
  say once what binding means — here, every flag resolved, not a zero count.

Anything found in pass 2 gets fixed before committing, and named in the closing
summary — a conflict introduced while fixing feedback is still a conflict
Matthew has to live with next Saturday.

Commit the archived feedback document from Step 1 with those edits, and add
its row to `feedback/README.md`: the brief commented on, the file, the
comment count, and a one-line outcome (what was ratified and where, how much
was deferred).

Write this round's record to `feedback/ai-pulse-<YYYY-MM-DD>-ratified.md`,
following the format of the existing records: one row per ratified item —
item, change, destination file, the observable check to run against the next
brief, and an empty Result column for the next round's Step 0 to fill. An
observable check must be something a later run can actually look at ("no
occurrence of X," "every entry in section Y has Z"), not a restatement of the
rule. Where a rule has no observable signature, say so in the row rather than
inventing one. Close the record with the round's deferred items, so nothing
approved-adjacent goes missing between rounds.

Close with a two-line summary: last round's audit result (N of N landed), then
N comments → N one-offs queued, N sharpenings and N rules landed (by file), N
design items open.

## Boundaries

- This skill never edits CLAUDE.md — foundation changes are always a direct
  conversation, not a feedback-routing outcome.
- It never resolves a rule conflict on its own authority, and never infers a
  standing rule from tone alone.
- If the uploaded document has no comments, say so and stop — do not infer
  feedback from the skill text itself.
