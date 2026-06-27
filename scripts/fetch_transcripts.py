#!/usr/bin/env python3
"""Fetch podcast and YouTube transcripts for the research-digest skill.

Two-stage design (see CLAUDE.md / topics config):

  Stage 1 - list candidates so the agent can pick the AI-relevant episodes:
      python3 scripts/fetch_transcripts.py list --days 7
      python3 scripts/fetch_transcripts.py list --show a16z --days 7

  Stage 2 - fetch full transcripts only for the episodes that matter:
      python3 scripts/fetch_transcripts.py fetch --show a16z --id <slug-or-url>
      python3 scripts/fetch_transcripts.py fetch --url <full-episode-url>
      python3 scripts/fetch_transcripts.py fetch --show dwarkesh --id <videoId>

Handlers:
  - podscripts : list from the show listing page (dates are inline), fetch the
                 transcript from the episode page. Covers a16z, Odd Lots,
                 In Good Company, Hard Fork.
  - youtube    : list recent videos by scraping the channel page, fetch captions
                 via youtube-transcript-api. Covers No Priors, Dwarkesh,
                 Greg Isenberg.
  - web        : date-addressed web editions (AI Daily Brief at /e/YYYY-MM-DD).

Design notes / known limits are at the bottom of this file.
"""

import argparse
import datetime as dt
import json
import re
import sys
import time
import urllib.request
import urllib.error

from bs4 import BeautifulSoup

UA = "Mozilla/5.0 (compatible; research-digest/1.0)"
TIMEOUT = 45        # seconds per attempt (podscripts.co can be slow)
RETRIES = 3         # transient timeouts / 5xx are common; retry before giving up


# --------------------------------------------------------------------------- #
# Show registry
# --------------------------------------------------------------------------- #
# type "podscripts": slug is the podscripts.co/podcasts/<slug> path segment.
# type "youtube":   handle is the @handle on youtube.com.
# type "web":       base is a date-addressed edition root.
SHOWS = {
    # --- AI-focused ---
    "ai-daily-brief": {"type": "web", "base": "https://aidailybrief.ai/e/", "name": "The AI Daily Brief", "md_suffix": ".md"},
    "no-priors":      {"type": "youtube", "handle": "@NoPriorsPodcast", "name": "No Priors"},
    "a16z":           {"type": "podscripts", "slug": "a16z-podcast", "name": "a16z Podcast"},
    "dwarkesh":       {"type": "youtube", "handle": "@DwarkeshPatel", "name": "Dwarkesh Podcast"},
    "greg-isenberg":  {"type": "youtube", "handle": "@GregIsenberg", "name": "Greg Isenberg"},
    "hard-fork":      {"type": "podscripts", "slug": "hard-fork", "name": "Hard Fork"},
    # --- Markets / finance / business ---
    "odd-lots":        {"type": "podscripts", "slug": "odd-lots", "name": "Odd Lots"},
    "in-good-company": {"type": "podscripts", "slug": "in-good-company-with-nicolai-tangen", "name": "In Good Company"},
}


def get(url):
    """Fetch a URL, retrying on transient failures (timeouts, 5xx, gateway
    errors) with backoff. podscripts.co intermittently times out or returns 502;
    a couple of retries recovers almost all of those. 4xx errors fail fast."""
    last = None
    for attempt in range(RETRIES):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
                return r.read().decode("utf-8", "ignore")
        except urllib.error.HTTPError as e:
            last = e
            if e.code < 500:      # 404 etc. won't fix themselves — stop now
                raise
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            last = e              # timeout / connection reset / DNS — retry
        if attempt < RETRIES - 1:
            time.sleep(2 * (attempt + 1))   # 2s, then 4s
    raise last


def in_window(date, days):
    if date is None:
        return True  # keep undated candidates; the agent can judge
    today = dt.date.today()
    return (today - date).days <= days >= 0


# --------------------------------------------------------------------------- #
# podscripts
# --------------------------------------------------------------------------- #
_MONTHS = {m: i for i, m in enumerate(
    ["January", "February", "March", "April", "May", "June", "July",
     "August", "September", "October", "November", "December"], 1)}


def _parse_episode_date(text):
    m = re.search(r"([A-Z][a-z]+)\s+(\d{1,2}),\s+(\d{4})", text)
    if not m:
        return None
    mon, day, year = m.group(1), int(m.group(2)), int(m.group(3))
    if mon not in _MONTHS:
        return None
    return dt.date(year, _MONTHS[mon], day)


def podscripts_list(slug, days):
    html = get(f"https://podscripts.co/podcasts/{slug}")
    soup = BeautifulSoup(html, "html.parser")
    out = []
    for span in soup.find_all("span", class_="episode_date"):
        date = _parse_episode_date(span.get_text(strip=True))
        # find the episode link near this date span
        link = None
        node = span
        for _ in range(6):
            node = node.find_parent()
            if node is None:
                break
            link = node.find("a", href=re.compile(rf"/podcasts/{re.escape(slug)}/[^/\"]+$"))
            if link:
                break
        if not link:
            continue
        ep_slug = link["href"].rstrip("/").split("/")[-1]
        title = ep_slug.replace("-", " ").title()
        if in_window(date, days):
            out.append({"id": ep_slug, "date": date.isoformat() if date else None,
                        "title": title, "url": f"https://podscripts.co{link['href']}"})
    # dedupe by id, preserve order
    seen, uniq = set(), []
    for e in out:
        if e["id"] in seen:
            continue
        seen.add(e["id"])
        uniq.append(e)
    return uniq


def podscripts_fetch(slug, ep_id):
    if ep_id.startswith("http"):
        url = ep_id
    else:
        url = f"https://podscripts.co/podcasts/{slug}/{ep_id}"
    html = get(url)
    soup = BeautifulSoup(html, "html.parser")
    node = soup.find(id="episodesingle") or soup
    text = node.get_text("\n", strip=True)
    # strip podscripts timestamp scaffolding and UI chrome
    lines = []
    for ln in text.split("\n"):
        if ln.startswith("Starting point is"):
            continue
        if ln in ("Transcript", "Discussion") or re.fullmatch(r"\(\d+\)", ln):
            continue
        if "comments yet for this episode" in ln:
            continue
        lines.append(ln)
    return "\n".join(lines).strip()


# --------------------------------------------------------------------------- #
# youtube
# --------------------------------------------------------------------------- #
def youtube_list(handle, days):
    html = get(f"https://www.youtube.com/{handle}/videos")
    m = re.search(r"var ytInitialData = (\{.*?\});</script>", html)
    if not m:
        return []
    data = json.loads(m.group(1))

    # Current YouTube layout: each video is a lockupViewModel with contentId
    # (the videoId) and a lockupMetadataViewModel holding title + a metadata row
    # whose parts include "<n> <unit> ago".
    lockups = []

    def walk(o):
        if isinstance(o, dict):
            if "lockupViewModel" in o and isinstance(o["lockupViewModel"], dict):
                lockups.append(o["lockupViewModel"])
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)

    walk(data)

    out, seen = [], set()
    for lk in lockups:
        vid = lk.get("contentId")
        if not vid or vid in seen:
            continue
        meta = lk.get("metadata", {}).get("lockupMetadataViewModel", {})
        title = meta.get("title", {}).get("content")
        if not vid or not title:
            continue
        # gather metadata text parts to find the "... ago" published string
        pub = None
        rows = (meta.get("metadata", {})
                    .get("contentMetadataViewModel", {})
                    .get("metadataRows", []))
        for row in rows:
            for part in row.get("metadataParts", []):
                txt = part.get("text", {}).get("content", "")
                if "ago" in txt or "Streamed" in txt:
                    pub = txt
        seen.add(vid)
        if _relative_in_window(pub, days):
            out.append({"id": vid, "date": pub, "title": title,
                        "url": f"https://www.youtube.com/watch?v={vid}"})
    return out


def _relative_in_window(pub, days):
    # pub like "2 days ago", "1 week ago", "3 hours ago", "Streamed 5 days ago"
    if not pub:
        return True
    p = pub.lower()
    if "hour" in p or "minute" in p or "today" in p or "yesterday" in p:
        return True
    m = re.search(r"(\d+)\s+(day|week|month|year)", p)
    if not m:
        return True
    n, unit = int(m.group(1)), m.group(2)
    mult = {"day": 1, "week": 7, "month": 30, "year": 365}[unit]
    return n * mult <= days


def youtube_fetch(vid):
    from youtube_transcript_api import YouTubeTranscriptApi
    api = YouTubeTranscriptApi()
    fetched = api.fetch(vid)
    return " ".join(snip.text for snip in fetched).strip()


# --------------------------------------------------------------------------- #
# web (AI Daily Brief date editions)
# --------------------------------------------------------------------------- #
def web_list(base, days):
    # AI Daily Brief homepage lists recent /e/YYYY-MM-DD editions
    root = base.rsplit("/e/", 1)[0] + "/"
    html = get(root)
    out, seen = [], set()
    for d in re.findall(r"/e/(\d{4}-\d{2}-\d{2})", html):
        if d in seen:
            continue
        seen.add(d)
        date = dt.date.fromisoformat(d)
        if in_window(date, days):
            out.append({"id": d, "date": d, "title": f"AI Daily Brief {d}",
                        "url": f"{base}{d}"})
    return out


def web_fetch(base, ep_id, md_suffix=None):
    # AI Daily Brief is a client-rendered SPA: the HTML page only contains the
    # first story. It publishes a clean per-edition markdown (e/<date>.md), so
    # use that when available.
    if md_suffix and not ep_id.startswith("http"):
        return get(f"{base}{ep_id}{md_suffix}").strip()
    url = ep_id if ep_id.startswith("http") else f"{base}{ep_id}"
    html = get(url)
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "nav", "footer", "header"]):
        tag.decompose()
    main = soup.find("article") or soup.find("main") or soup.body or soup
    return main.get_text("\n", strip=True)


# --------------------------------------------------------------------------- #
# dispatch
# --------------------------------------------------------------------------- #
def list_show(key, days):
    cfg = SHOWS[key]
    if cfg["type"] == "podscripts":
        return podscripts_list(cfg["slug"], days)
    if cfg["type"] == "youtube":
        return youtube_list(cfg["handle"], days)
    if cfg["type"] == "web":
        return web_list(cfg["base"], days)
    return []


def fetch_show(key, ep_id):
    cfg = SHOWS[key]
    if cfg["type"] == "podscripts":
        return podscripts_fetch(cfg["slug"], ep_id)
    if cfg["type"] == "youtube":
        return youtube_fetch(ep_id)
    if cfg["type"] == "web":
        return web_fetch(cfg["base"], ep_id, cfg.get("md_suffix"))
    return ""


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    pl = sub.add_parser("list", help="list candidate episodes in the window")
    pl.add_argument("--show", help="show key (default: all)")
    pl.add_argument("--days", type=int, default=7)
    pl.add_argument("--json", action="store_true")

    pf = sub.add_parser("fetch", help="fetch one transcript")
    pf.add_argument("--show", help="show key (required unless --url is a podscripts/web URL)")
    pf.add_argument("--id", help="episode slug / videoId / date")
    pf.add_argument("--url", help="full episode URL")

    sub.add_parser("shows", help="list configured shows")

    args = ap.parse_args()

    if args.cmd == "shows":
        for k, c in SHOWS.items():
            print(f"{k:16s} {c['type']:11s} {c['name']}")
        return

    if args.cmd == "list":
        keys = [args.show] if args.show else list(SHOWS)
        result = {}
        for k in keys:
            if k not in SHOWS:
                print(f"# unknown show: {k}", file=sys.stderr)
                continue
            try:
                eps = list_show(k, args.days)
                result[k] = eps
            except Exception as e:
                result[k] = {"error": f"{type(e).__name__}: {e}"}
                print(f"# {k}: ERROR {type(e).__name__}: {e}", file=sys.stderr)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            for k in keys:
                if k not in result:
                    continue
                eps = result[k]
                print(f"\n=== {k} ({SHOWS[k]['name']}) ===")
                if isinstance(eps, dict):
                    print(f"  ERROR: {eps['error']}")
                    continue
                if not eps:
                    print("  (no episodes in window)")
                for e in eps:
                    print(f"  [{e.get('date')}] {e['id']}")
                    print(f"       {e['title']}")
        return

    if args.cmd == "fetch":
        if args.url and not args.show:
            # infer handler from URL
            if "podscripts.co" in args.url:
                slug = args.url.split("/podcasts/")[1].split("/")[0]
                print(podscripts_fetch(slug, args.url))
            else:
                print(web_fetch("", args.url))
            return
        if not args.show:
            ap.error("fetch needs --show (or a recognizable --url)")
        ep = args.id or args.url
        if not ep:
            ap.error("fetch needs --id or --url")
        print(fetch_show(args.show, ep))
        return


if __name__ == "__main__":
    main()

# --------------------------------------------------------------------------- #
# Known limits / maintenance notes
# --------------------------------------------------------------------------- #
# - YouTube listing uses relative dates ("2 days ago") scraped from the channel
#   page, so window filtering is approximate near the boundary. The YouTube RSS
#   feed (videos.xml?channel_id=) would give exact timestamps but returns 404
#   through the current egress proxy.
# - YouTube captions can be auto-generated (lower fidelity) and rate-limited.
# - podscripts publishes a few days after an episode airs, so the most recent
#   1-2 days of a show may not have a transcript yet.
# - Stratechery, Odd Lots (Bloomberg site), WSJ, FT, NYT Hard Fork pages are
#   paywalled; podscripts covers Hard Fork/Odd Lots, the rest need WebFetch.
