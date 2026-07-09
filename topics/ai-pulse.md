# Topic: AI Pulse

The stay-informed-and-connect-dots brief for AI. This is the Pulse job: situational
awareness of the space, tied back to money, markets, technology, and my own ideas. The
research-digest skill reads this to know what to gather and how to judge relevance
for AI. Edit it freely as my interests shift. This is the cheap, frequently-changed
file. The skill itself stays put.

## Scope

AI-centered, but not AI-only. The aperture is AI and its orbit: the technology
itself, plus how it moves money, markets, technology, labor, and business, plus genuinely
adjacent or tangential developments that matter to an operator with my interests
(finance, deals, starting and buying businesses). If something is not strictly an
AI story but connects to AI or to where I am headed, it belongs. Do not filter it
out just because it is not labeled "AI."

## Cadence

Weekly. Default window is the last 7 days.

## Output shape

Build the Pulse brief in this exact structure every week. The canonical example of
the format — match its structure, sectioning, and styling — is
`templates/ai-pulse-format-reference.docx` (and the `.md` beside it), built from
the week-of-Jun-24 brief. It supersedes the earlier June-20 layout (now in
`briefs/archive/`); when in doubt about format, follow the reference file. (The
Playbook config overrides this with a reading-queue shape; this section governs
Pulse only.)

- **Title block.** "AI Pulse Brief" and a "Week of <date range>" line.
- **Intro.** Two to four sentences on the week: name the single biggest story and
  the through-line that connects the rest. Direct, no throat-clearing. Write it as
  a neutral publication opener — do not address a reader by name or open with a
  greeting ("Matthew," / "Good morning,").
- **Top developments (3 to 5).** Each item is a numbered heading written as a
  full claim sentence, not a short label. The heading should state what happened
  and signal why it is the story. Inside each item, walk the chain with these
  labeled beats, each label in bold. Three beats are required and appear in every
  item; two are optional and fire only when the story earns them:
  - **What happened.** *(required)* The facts, with the date, told as one picture.
    Weave the supporting proof, corroboration, caveats, and any glossary asides
    INLINE, next to the claim they qualify — there is no separate "evidence" beat
    (it only re-narrated the event). Prefer the primary source; cite every source
    actually drawn on for the item, not just the best one, on the Source line
    below. If a claim has no source, do not make it.
    Benchmarks and jargon: never drop a benchmark name or score without explaining,
    in plain words, what the test measures and how to read the number (what counts
    as good, what it means in practice). I do not know the benchmarks. Same for
    terms like parameters, context window, or license — gloss them the first time.
  - **Does it hold up?** *(optional)* Include only when the item rests on a
    self-reported or contestable claim worth stress-testing — a vendor's own
    benchmark, a striking growth number, an unverified capability. State plainly
    what is actually proven versus what is self-reported or unverified. Skip it
    when the facts are not in dispute.
  - **Both sides.** *(optional)* Include only when there is a genuine interpretive
    disagreement about what the news means (not a manufactured one). Open with one
    framing line naming the axis of dispute, then one bullet per side, each giving
    the strongest version of that side and attributed where possible, then an
    optional closing line only if there is a real synthesis to name. If it would
    collapse to "the obvious view plus a token objection," cut the beat — a forced
    debate is worse than none.
  - **Why it matters.** *(required)* The so-what chain, step by step, traced
    through my standing lenses (technical, finance, operator) as general
    significance — neutral voice, not addressed to a reader. When there are several
    distinct reasons, use an indented bullet list, each bullet led by a short bold
    phrase.
  - **My take.** *(required)* The writer's own opinion, clearly labeled as
    editorial and separated from the facts above, including the signal-versus-hype
    call. It is the writer's voice, not a note addressed to any one reader. When a
    "Both sides" beat ran, adjudicate between the reads here rather than restating
    them — land where the weight falls and why.

  End each item with a "Source:" line listing every source used, each tagged with
  a few words on what it supports. The standing beat order is fixed — What happened,
  then the optional Does it hold up? and/or Both sides, then Why it matters, then
  My take — and the optionals always sit between What happened and Why it matters.
  The three required beats appear every time; wording inside a beat can flex to the
  story, but keep that spine and always keep My take labeled. Most items run three
  beats; four when one optional fires; five is rare, only when an item genuinely
  has both a contestable claim and a live debate.

  Readability — keep paragraphs short. A beat is not required to be a single
  paragraph. When a beat's prose runs long (more than about four or five sentences),
  break it into two or three shorter paragraphs at natural seams rather than one
  dense block — the first paragraph carries the bold beat label, the continuation
  paragraphs do not repeat it. This holds for every section, including the longer
  "What people are saying" entries, not just the top items. Dense walls of text are
  the thing to avoid.
  
- **Worth a skim.** Shorter items that are relevant but not urgent. One bullet
  each: a bold lead-in sentence, a one-line why, and a link.
- **What people are saying.** The perspective layer from the podcasts and
  Substacks, kept as its own section (do not fold it into the items). For each
  show or writer worth surfacing, write two beats, each opened with a literal
  bold label: "**What it was about:**" then "**Why it matters:**". These two
  labels are keys that should stand out — in the Word doc they render bold in a
  distinct accent color (any bold label ending in a colon is auto-colored by the
  renderer), so always write them exactly as those two bold, colon-terminated
  labels. Two more rules:
  - Scale the depth to the speaker. When it is a high-signal voice (a major CEO,
    a frontier-lab leader, a serious investor), give more on what was actually
    said, not a single line.
  - Use a quote when there is a genuinely good one. Not every show needs a quote,
    but a sharp line beats a paraphrase. Cite the specific episode or post.
  - Gloss the jargon here too. Buzzy business or tech phrases a guest uses
    ("industrialization of software," "legacy migration," "data pipeline," and the
    like) must be explained in plain words — this section is not exempt from the
    no-unexplained-term rule.
  - Every perspective source gets the same full treatment — podcast, YouTube
    channel, or Substack alike. Give each one worth surfacing its own labeled
    two-beat entry at full depth; do not compress any of them into a summary
    paragraph or bury them as a footnote. (Substacks were the ones shortchanged
    before, so watch them especially, but the rule is medium-neutral.)
- **New sources worth adding.** The output of the standing source-discovery beat
  (see "Source discovery" below). One to three newly found high-signal sources
  this week — Substacks, podcasts, YouTube channels, analysts, sites — each with a
  short "**What it is:**" / "**Why it fits:**" write-up and a clear recommendation
  to add it or pass. Skip the section only in a week where nothing good turned up,
  and say so if so. When I bless one, promote it into the standing source list.
- **On my radar.** Things that have not landed yet, open questions, threads to
  follow next week. Bullets.
- **Source coverage this week.** A short closing section: what was pulled
  (primary and verification), what could not be reached, and any strong new
  source worth adding.
- **Config notes.** The very last line of the brief: a one-line report on whether
  any contradiction between the config files (CLAUDE.md, this topic config, and
  MEMORY.md) turned up during the run. If none, say so in a few words ("Config
  notes: no contradictions this run."). If one did, name it in a sentence or two —
  what conflicted and which way it was resolved — noting that MEMORY.md always wins
  by rule, and flag a major contradiction clearly so it can be fixed in the files
  later. This is a report only; it never blocks or delays the brief.

Length follows substance. A quiet week is short; a rich week can run long. Never
pad, and never compress something worth teaching just to stay short.

## Lens weighting for this topic

AI reads through three core lenses kept in rough balance — the technical apparatus,
finance and economics (where is the money, who wins), and idea generation (operator
angles) — with no standing tilt toward any one. Apply whichever genuinely fit an
item and lead with the most material. Two things hold regardless of weighting:
always teach the technical layer when it appears (how it works, what is different,
where things are heading, pitched for fluency — never skip or shrink it), and run
the standing "models and their specs" sweep every week. The situational lenses,
market structure, legal, and cross-domain ripple, come in only when an item
genuinely has that angle.

## Source discovery (standing beat)

The listed sources are a baseline, not a cage. Every run, actively hunt for new
high-signal sources beyond the list — Substacks, podcasts, YouTube channels,
independent analysts, interesting sites, sharp people on X worth following. Do not
treat this as optional color; it is a real job each week. How it works:

- Scout. While researching the week, notice who keeps producing genuinely good
  work that is not already in my rotation, and run a deliberate search or two for
  new voices in AI, AI-and-finance, compute and chips, and the operator/idea
  angle.
- Vet. Only surface sources that clear a real bar: original analysis, primary
  reporting, or a perspective I am not already getting. Skip SEO content farms,
  rehashers, and hype accounts. Quality over volume — one strong find beats five
  weak ones, and a dry week is fine to report as dry.
- Surface. Put the best one to three in the brief's "New sources worth adding"
  section with a short what-it-is / why-it-fits and a clear recommendation.
- Promote and prune. Track everything in MEMORY.md (the source-discovery ledger).
  When I bless a candidate, add it to the standing source list here and give it
  normal weight in future briefs. A source that earns its place should start
  showing up as a regular, cited voice, not just a suggestion.

The promote/prune system (keep it lightweight):

- Two kinds of memory, do not confuse them. The "recently covered" news list in
  MEMORY.md trims to ~4-6 weeks on purpose (old news should fall off). The
  source-discovery ledger is PERSISTENT and never trimmed — it is the long-horizon
  memory that makes promote/prune possible. No need to extend the news window for
  this; the ledger lives in a committed file and persists on its own.
- Promote (candidate -> rotation): when Matthew blesses it, or when I have
  recommended it and it has delivered brief-worthy material across ~3 separate
  weeks and he confirms. On promotion, add it to the source list above and to the
  ledger's rotation bucket.
- Track hits and misses. Each run, in the ledger, mark every commentary source
  (podcasts, Substacks, YouTube channels) as a hit (it contributed to the brief)
  or a miss (checked, nothing worth pulling), and note when it last contributed.
  This is cheap — the coverage section already records reached vs not-reached.
- Prune (rotation -> dropped): when a commentary source hits ~4 consecutive
  misses, or its quality clearly drops, or a stronger source now covers the same
  beat, flag it for me in the brief ("consider dropping X — N weeks without a
  contribution") and let me decide. Never silently drop a source I chose. This
  applies only to the commentary rotation, where a slot has real cost — not to
  news sources (lab blogs, wires), which are simply checked as needed.

## What to track (rough priority)

1. Models and their specs (a standing beat — sweep this every week, even a quiet
   one). What shipped or changed across the major labs AND the open-weight and
   Chinese world (GLM, DeepSeek, Kimi, Qwen, and peers — the part most likely to
   get skipped, so check it deliberately). When a release is material, lay out
   what is actually different in concrete terms: context window, price per token,
   benchmarks, speed, and what it is good and bad at. I want to understand the
   models and the trade-offs between them, pitched for fluency, not engineering.
   Include what people are saying about it.
2. The money. Funding rounds, infrastructure and data-center spend, big commercial
   deals, valuations. Where capital is flowing and what it implies.
3. Agents and agent tooling at the news level. Notable launches and what companies
   are doing with agents. (The deeper "here is how to build it" material lives in
   the Playbook, not here.)
4. Infrastructure and market structure. Compute, chips, who is building which layer
   of the stack, and shifts in how the pieces fit together.
5. Applied AI in finance, law, and professional services. Real deployments, not
   press releases.
6. Regulation and policy when it actually lands. Rules, liability, IP, anything
   that changes the playing field, with a bias toward the business and
   transactional angle.
7. Adjacent and tangential developments. The second-order stuff: AI's effect on the
   broader economy and labor, notable moves in markets and business that connect
   back to AI or to operating, and the occasional non-AI development that is simply
   worth an operator's attention. Use judgment, but err toward including a strong
   tangential item over forcing a weak pure-AI one.

## Sources to prioritize

Lead with primary sources, and mean it. When a person or company posts a
specific thing — an essay, a blog post, a filing, a paper, a model card, an X or
LinkedIn post — go find and read that primary source and cite it directly. Do not
cite a secondhand article about it (a Fortune or TheStreet write-up of Satya
Nadella's essay is the anti-pattern). Secondary coverage is only for supplementing
the primary or for when no primary exists. If the primary cannot be found, say so
rather than passing off the secondhand version as the source.

Starter set, refine as I learn which ones earn it:

- Major lab newsrooms and blogs: Anthropic, OpenAI, Google DeepMind, Meta AI,
  Mistral, and peers.
- Official blogs for the big infrastructure players: Nvidia and the major cloud
  providers.
- For the money: reputable deal and funding coverage (The Wall Street Journal,
  The Information, Bloomberg, Reuters, CNBC) plus primary filings where they exist.
  WSJ note: I can read WSJ headlines and snippets via search and cite them, but
  full articles sit behind a paywall I cannot legitimately get past with these
  tools — do not use paywall-bypass mirrors, and do not store my login. When a
  specific WSJ article is load-bearing for an item, flag it and I will paste the
  text; otherwise cite from the search snippet and note the limit.
- High-signal Substacks and independent analysts. AI and ecosystem: Interconnects
  (Nathan Lambert) for the model and open-weight scene, ChinaTalk (Jordan
  Schneider) for US-China AI and chips, Import AI (Jack Clark) for frontier and
  policy, SemiAnalysis (Dylan Patel) for chips, datacenters, and compute economics
  (promoted Jun 2026 — the money-and-engineering read on the AI supply chain),
  One Useful Thing (Ethan Mollick) for practical, operator-level AI use, and Every
  (Dan Shipper, https://every.to) for hands-on, first-hand, falsifiable testing of
  AI tools and models rather than secondhand commentary.
  Finance and the tech-finance seam (the tangential angle I want): The Diff (Byrne
  Hobart) for the finance-meets-strategy intersection, The Generalist (Mario
  Gabriele) for deep dives on companies and business models, Net Interest (Marc
  Rubinstein) for financial-sector plumbing, Money Stuff (Matt Levine) for markets
  with everything connected, Noahpinion (Noah Smith) for economics and policy.
  Stratechery (Ben Thompson) sits across both. Prune this list as I learn which
  ones earn their place.

Treat social posts and aggregators as leads to verify, not as sources to quote.

The lists here are a floor, not a ceiling. Cover all of them, but do not stop
there: research the open web freely, follow leads to sources not on these lists,
and surface anything genuinely relevant wherever it comes from. If you keep
finding a strong source that is not listed, flag it so I can add it.

Special weight on the perspective layer — Substacks, podcasts, and YouTube alike.
These are where writers and speakers spell out what they are actually seeing, and
they are co-equal top-tier sources for the brief: no medium ranks above the others.
Substacks are the written analysis; podcasts and YouTube are the interviews and
discussion. All of them belong in every brief, not as occasional links. Scan the
listed ones every week without fail, and keep hunting for strong new ones beyond the
list. Their takes belong in the brief's "What people are saying" section, each
summarized with a point of view and given real depth, not buried as a passing
citation.

### Video and podcast sources

These are the commentary layer, not a headline feed. Their value is not breaking
news (the articles, Substacks, and AI Daily Brief cover that). It is what people
are saying: the themes, the arguments, the interview takeaways, the context around
the week's events. Scan them every week even when nothing "breaks" from them. The
last run skipped this entirely because the news was already covered elsewhere, and
that is exactly the mistake to avoid: the point of these is perspective, not events.

How to use them:

- Scan each show's episodes inside the window. Several (especially the markets
  shows) cover plenty that is not about AI; pull the AI-relevant or
  operator-relevant discussions and skip the rest, but actually look at each one.
- For anything worth surfacing, give me the take: "On [show], [person] argued X,"
  with a sentence or two of what they said and why it adds context. Cite the
  episode. These belong in the "What people are saying" section of the brief.
- Read them via transcript, and prefer a transcript site over YouTube captions,
  which are unreliable to fetch. Check podscripts.co first (URL pattern
  podscripts.co/podcasts/<show-slug>), with Tapesearch or Metacast as backups, plus
  the AI Daily Brief web editions and any transcript a show publishes itself. Look
  the show up, find the in-window episodes, and read those transcript pages. If a
  show genuinely had nothing relevant, or you could not find a transcript this
  week, say so in the coverage note rather than skipping silently.

AI-focused shows:

- The AI Daily Brief (Nathaniel Whittemore), https://aidailybrief.ai and
  https://www.youtube.com/@AIDailyBrief : daily AI news plus analysis, and one of
  the best secondary maps of the week. Read EVERY daily edition in the window — one
  per day, do not sample just a few — and read the web/markdown edition (NLW's own
  structured write-up, via the agent.json feed -> e/<date>.md), not the audio
  transcript; the web edition is denser, cleaner, and fewer tokens. Use it as a
  lead-finder: it tells you much of what happened across the week, so for stories it
  surfaces that earn a place in the brief, go find the PRIMARY source (or other
  independent coverage) and build the item off that where one exists. Two caveats,
  both important: it is NOT the only map — cross-check it against the other
  discovery sources (WSJ and other headlines, the Substacks, YouTube, and the
  podcasts) so a story it misses does not slip through. And the AI Daily Brief is
  itself a good, citable secondary source — cite it on the Source line where it
  backs a point or for NLW's own analysis; prefer the primary when one exists, but
  sourcing the AI Daily Brief is fully allowed and encouraged.
- No Priors (Sarah Guo and Elad Gil), https://www.youtube.com/@NoPriorsPodcast :
  investor and founder lens, where AI is headed and how it reshapes businesses.
- a16z Podcast (Andreessen Horowitz), https://www.youtube.com/@a16z, transcripts at
  https://podscripts.co/podcasts/a16z-podcast : venture and operator view on AI and
  tech, and where the firm thinks value is forming.
- Dwarkesh Podcast (Dwarkesh Patel), https://www.youtube.com/@DwarkeshPatel : long,
  deep interviews with frontier-lab leaders. Mine it for understanding what the
  technology is and where it is going.
- Greg Isenberg, https://www.youtube.com/@GregIsenberg : startup ideas and using
  AI to build and grow a business. Strongest feed for the idea-generation and
  operator lens.
- Hard Fork (New York Times), https://www.nytimes.com/column/hard-fork : weekly,
  accessible, ties AI to the broader news cycle. NYT publishes transcripts.
- Stratechery / Sharp Tech (Ben Thompson), https://stratechery.com : strategy,
  platform economics, and market structure.
- The Cognitive Revolution (Nathan Labenz), https://www.cognitiverevolution.ai :
  technical interviews with AI researchers and builders at the frontier, hosted by a
  practitioner who runs his own AI company. Strongest for the build-real-fluency
  mandate — how the technology actually works, not just product news.
- Latent Space (swyx / Shawn Wang and Alessio Fanelli), https://www.latent.space :
  AI engineering at the practitioner level. Pull its AI-market, model, and
  builder-trend discussions (leave the deep how-to-build tutorials to the Playbook).
- AI Engineer (YouTube channel), https://www.youtube.com/@aiDotEngineer : talks and
  keynotes from the AI Engineer World's Fair and Summit, where practitioners present
  how they actually build with AI (e.g. the "Field Guide to Fable" talk). Pull the
  transcript of any in-window talk worth surfacing.

Markets, finance, and business shows (the tangential and cross-domain angle; not
every episode is about AI, so pull the ones that are or that touch operating):

- Odd Lots (Bloomberg, Joe Weisenthal and Tracy Alloway),
  https://www.bloomberg.com/oddlots : deep dives on markets and how things work.
  Strong for the economics-ripple lens. Bloomberg publishes transcripts.
- In Good Company (Nicolai Tangen, Norges Bank Investment Management), transcripts
  at https://podscripts.co/podcasts/in-good-company-with-nicolai-tangen : interviews
  with CEOs and investors on how big businesses and markets work.
- BG2 Pod (Brad Gerstner of Altimeter Capital and Bill Gurley of Benchmark),
  https://www.bg2pod.com : biweekly, numbers-driven analysis at the AI-and-markets
  intersection from two working investors who actually allocate capital. Strong for
  the finance lens — AI capex, circular-revenue and hidden-leverage scrutiny.
Dropped from the weekly podcast scan: WSJ What's News, FT News Briefing, and
Bloomberg Talks. The WSJ daily-news podcast is short headline audio and not worth
the tokens for a weekly brief. WSJ still counts as a written/journalism source for
article research (see "Sources to prioritize" above) — just not as a podcast.

Optional and heavier: Acquired for occasional company deep dives, All-In for
markets and venture chatter (more punditry, lower signal-to-noise).

Latent Space is now part of the Pulse rotation (listed under AI-focused shows
above). Its deep build-tutorials still belong to the Playbook; here, pull its
AI-market, model, and practitioner-trend discussions.

## What I already know and have covered

Tracked in `MEMORY.md`, not here, since it changes from week to week. The agent
reads it to avoid re-explaining what I understand and repeating what it already
reported, and updates it after each run. Keep this config to what to look at; let
`MEMORY.md` hold what I have already got.

## Flag for me

- Anything that changes how I should think about starting, buying, or running a
  business, or about bringing AI into one.
- Anything sitting at the intersection of AI and finance or law.
- Clear hype or overclaiming. Call it out rather than passing it on.
