---
name: brief-feedback
description: >
  Captures and routes Matthew's feedback on a delivered brief. Use this skill
  whenever Matthew reacts to, critiques, or requests a change to a brief he has
  received — its wording, structure, coverage, ranking, sources, recurring
  voices, or the digest procedure itself. It records the feedback and routes
  each point to the file that OWNS that kind of rule, per CLAUDE.md's Memory
  section, rather than dumping everything into MEMORY.md. Do not use it for
  generating a brief (that is research-digest) or for one-off asks about the
  next run (those go straight into MEMORY.md's one-off queue).
---

# Brief feedback

Turn a reaction to a brief into the right durable change. CLAUDE.md's "Memory"
section is the authority on where each kind of rule lives; this skill is the
procedure that applies it consistently every time feedback arrives, so a
preference lands in the file that owns it instead of defaulting to MEMORY.md.

## When this fires

Matthew has read a brief and said something about it — "this section ran long,"
"stop using that construction," "cover X every week," "the ranking was wrong,"
"drop that source." Anything that should change how future briefs are made.

Not this skill: a request to run a brief (use research-digest), or a one-off ask
scoped to the very next run only ("cover this interview this week") — that is
transient state and goes into MEMORY.md's "One-off requests" queue, not here.

## The routing rule (from CLAUDE.md)

Route each piece of feedback to the file that owns that kind of rule. Never
default to MEMORY.md.

- **Prose and writing craft** — how sentences are built, word choice, banned
  constructions, causal chains, paragraph length, jargon glossing → the
  `house-writing-style` skill.
- **Brief shape and coverage** — beats, sections, ordering, ranking, what to
  cover or exclude, sources, recurring voices → the topic config under `topics/`.
- **The digest procedure itself** — steps, gathering, memory updates, output
  mechanics → the `research-digest` skill.
- **Durable cross-topic preferences that fit none of the above, and STATE** —
  what's been covered, the ledgers, what Matthew already knows → `MEMORY.md`.

The test: rules go to the file that owns them; state goes to MEMORY.md. When
routing is ambiguous, say where it would go and why before making the edit.

## Procedure

1. **Separate durable from one-off.** A one-off ("make this week shorter") is
   state for the next run → MEMORY.md's one-off queue. A rule ("always lead with
   the money items") is durable → route it below. If unsure, state it back to
   Matthew before saving.
2. **Classify each point** against the routing rule above. One piece of feedback
   can produce more than one edit in more than one file.
3. **Edit in place.** Replace what the change supersedes rather than appending;
   record standing rules, not a history of edits.
4. **Flag conflicts, don't block.** If the feedback contradicts an existing rule
   in another file, resolve it (MEMORY.md wins by precedence) and note the
   contradiction so the files can be reconciled later.
5. **Confirm ambiguous routing** with Matthew before writing, per the rule above.

## Notes

- v1 scaffold — the routing rules mirror CLAUDE.md; refine the procedure here as
  the feedback loop is exercised. Confirm scope and triggers with Matthew.
