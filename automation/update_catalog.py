#!/usr/bin/env python3
"""Refresh All-REA's featured projects and discover REA-related candidates.

Requires Python 3.11+ and GITHUB_TOKEN for API access. Standard library only.
Only the marked/generated README sections are edited; other sections survive.
New projects are *candidates*, never automatically labeled verified REA usage.
"""

from __future__ import annotations

import argparse
import base64
import datetime as dt
import json
import math
import os
from pathlib import Path
import re
import sys
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, quote
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
CFG_PATH = ROOT / "automation" / "catalog.json"
CANDIDATES_PATH = ROOT / "automation" / "candidates.json"
README_PATH = ROOT / "README.md"
FEATURE_START = "<!-- ALL-REA:FEATURED:START -->"
FEATURE_END = "<!-- ALL-REA:FEATURED:END -->"
DISCOVER_START = "<!-- ALL-REA:DISCOVERED:START -->"
DISCOVER_END = "<!-- ALL-REA:DISCOVERED:END -->"
API_BASE = "https://api.github.com"
REPO_PATTERN = re.compile(r"(?i)(?:https?://)?github\.com/([a-z\d-]+)/([a-z\d._-]+)")
EXPLICIT_REA_PATTERN = re.compile(
    r"(?i)(?:https?://(?:www\.)?github\.com/morluto/rea(?:[\s/#?)\]\"'`]|$)|"
    r"https?://(?:www\.)?rea\.tools(?:[/\s\]\)'\"`]|$))"
)


def safe_text(value: str, max_length: int = 110) -> str:
    """Escape untrusted metadata for a Markdown table; don't allow HTML."""
    value = re.sub(r"<[^>]*>", "", str(value or ""))
    value = re.sub(r"[\r\n\t|<>]", " ", value)
    value = re.sub(r"\s+", " ", value).strip()
    value = value.replace("[", "\\[").replace("]", "\\]")
    return value[:max_length].rstrip()


def repo_key(name: str) -> str:
    return name.strip().lower()


def replace_between(text: str, start: str, end: str, replacement: str) -> str:
    if text.count(start) != 1 or text.count(end) != 1:
        raise ValueError(f"Missing or duplicate markers: {start} / {end}")
    prefix, rest = text.split(start, 1)
    _, suffix = rest.split(end, 1)
    return prefix + start + "\n" + replacement.rstrip() + "\n" + end + suffix


class GitHub:
    def __init__(self, token: str, request_delay: float = 0.45):
        if not token:
            raise ValueError("GITHUB_TOKEN is required. Use the automatic workflow.")
        self.token = token
        self.request_delay = request_delay

    def get(self, path: str, *, query: dict | None = None) -> dict:
        url = API_BASE + path + (("?" + urlencode(query)) if query else "")
        headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {self.token}",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "All-REA-catalog-bot",
        }
        for attempt in range(3):
            try:
                with urlopen(Request(url, headers=headers), timeout=18) as response:
                    result = json.load(response)
                time.sleep(self.request_delay)
                return result
            except HTTPError as exc:
                if exc.code in (403, 429, 502, 503) and attempt < 2:
                    wait = min(30, max(3, int(exc.headers.get("Retry-After", 4))))
                    time.sleep(wait)
                    continue
                raise RuntimeError(f"GitHub API {exc.code}: {path}") from exc
            except (URLError, TimeoutError) as exc:
                if attempt < 2:
                    time.sleep(2 + attempt * 2)
                    continue
                raise RuntimeError(f"GitHub API unavailable: {path}") from exc
        raise RuntimeError(f"GitHub API request failed: {path}")

    def repo(self, name: str) -> dict:
        owner, repo = name.split("/", 1)
        return self.get(f"/repos/{quote(owner)}/{quote(repo)}")

    def search(self, query: str, per_page: int = 25) -> list[dict]:
        data = self.get("/search/repositories", query={
            "q": query, "sort": "updated", "order": "desc", "per_page": min(per_page, 50)
        })
        return data.get("items", [])

    def readme(self, full_name: str) -> str:
        owner, repo = full_name.split("/", 1)
        data = self.get(f"/repos/{quote(owner)}/{quote(repo)}/readme")
        if data.get("encoding") != "base64":
            return ""
        return base64.b64decode(data.get("content", "")).decode("utf-8", errors="replace")


def activity_score(repo: dict, today: dt.date) -> int:
    """Small tie-breaker; stars and editor-assigned utility priority matter most."""
    stamp = (repo.get("pushed_at") or "")[:10]
    try:
        age = (today - dt.date.fromisoformat(stamp)).days
    except ValueError:
        return 0
    return 2 if age <= 14 else (1 if age <= 60 else 0)


def rank_featured(entries: list[dict], metadata: dict[str, dict], today: dt.date):
    def sort_key(entry):
        repo = metadata.get(repo_key(entry["repo"]), {})
        stars = max(0, int(repo.get("stargazers_count") or 0))
        # Utility priority dominates. Stars are popularity signal within a tier.
        return (int(entry.get("priority", 3)), math.log10(stars + 1), activity_score(repo, today))
    return sorted(entries, key=sort_key, reverse=True)


def render_featured(entries: list[dict], metadata: dict[str, dict], today: dt.date) -> str:
    rows = [
        "**Ordered by editorial usefulness first, then GitHub popularity.** "
        "This is not a quality guarantee. Star badges are live; app maturity varies.",
        "",
        "| Project | What can I do with it? | Type | REA relationship | Stars |",
        "| --- | --- | --- | --- | --- |",
    ]
    for entry in rank_featured(entries, metadata, today):
        full_name = entry["repo"]
        title = safe_text(entry["title"])
        utility = safe_text(entry["utility"])
        category = safe_text(entry["category"])
        relation = safe_text(entry["relation"])
        url = f"https://github.com/{full_name}"
        badge = f"![Stars](https://img.shields.io/github/stars/{full_name}?style=flat-square)"
        rows.append(f"| **[{title}]({url})** | {utility} | {category} | {relation} | {badge} |")
    return "\n".join(rows)


def links_in_readme(markdown: str) -> set[str]:
    results = set()
    for owner, repo in REPO_PATTERN.findall(markdown):
        repo = re.sub(r"\.git$", "", repo, flags=re.I)
        results.add(repo_key(f"{owner}/{repo}"))
    return results


def discover(gh: GitHub, config: dict, old_candidates: list[dict], readme: str, today: dt.date):
    known = links_in_readme(readme)
    known.update(repo_key(item["repo"]) for item in config["featured"])
    known.update(repo_key(x) for x in config.get("excluded_repositories", []))
    known.update(repo_key(item["repo"]) for item in old_candidates)
    pool: dict[str, dict] = {}
    for query in config["search_queries"]:
        print("Search:", query)
        for repo in gh.search(query, int(config.get("search_results_per_query", 25))):
            full = repo.get("full_name", "")
            if not full or "/" not in full or repo.get("fork") or repo.get("archived"):
                continue
            key = repo_key(full)
            if key in known or key == "morluto/rea":
                continue
            pool[key] = repo

    # Search is only a lead. Documentation must reference the real REA project.
    # Even then, it is a candidate for human review, NOT a verified REA project.
    selected = sorted(pool.values(), key=lambda r: (
        int(r.get("stargazers_count") or 0), r.get("pushed_at") or ""
    ), reverse=True)
    # Rotate through candidates across days: otherwise the same popular false
    # positives could consume the limited README checks indefinitely.
    check_limit = int(config.get("readme_checks_per_run", 18))
    if selected and check_limit > 0:
        pages = max(1, math.ceil(len(selected) / check_limit))
        offset = (today.toordinal() % pages) * check_limit
        selected = selected[offset:] + selected[:offset]
    added = []
    checks = 0
    for repo in selected:
        if checks >= check_limit:
            break
        checks += 1
        name = repo["full_name"]
        try:
            doc = gh.readme(name)
        except RuntimeError as exc:
            print(f"Skipped README for {name}: {exc}")
            continue
        if not EXPLICIT_REA_PATTERN.search(doc):
            continue
        added.append({
            "repo": name,
            "description": safe_text(repo.get("description") or "No description supplied", 125),
            "stars_at_discovery": int(repo.get("stargazers_count") or 0),
            "first_seen": today.isoformat(),
            "status": "Needs review — README mentions REA",
        })
        if len(added) >= 8:
            break
    # Keep a small rolling queue; submissions are proposed in a PR.
    combined = old_candidates + added
    combined.sort(key=lambda x: (x.get("first_seen", ""), x.get("stars_at_discovery", 0)), reverse=True)
    combined = combined[:int(config.get("candidates_limit", 15))]
    return combined, added


def render_candidates(candidates: list[dict]) -> str:
    lines = [
        "> [!CAUTION]",
        "> **Unverified discoveries.** The linked repositories mention REA, but this does **not** prove REA was used to build their software. Review their evidence, source, and license before recommending them.",
        "",
    ]
    if not candidates:
        return "No new candidates in the review queue."
    lines.extend([
        "| Repository | What it claims to do | Discovered | Verification |",
        "| --- | --- | --- | --- |",
    ])
    for item in candidates:
        name = safe_text(item["repo"], 95)
        description = safe_text(item["description"], 125)
        first = safe_text(item.get("first_seen", ""), 20)
        lines.append(f"| [{name}](https://github.com/{name}) | {description} | {first} | Needs review |")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-discovery", action="store_true", help="Only refresh featured order")
    args = ap.parse_args()
    config = json.loads(CFG_PATH.read_text(encoding="utf-8"))
    existing = README_PATH.read_text(encoding="utf-8")
    old_candidates = json.loads(CANDIDATES_PATH.read_text(encoding="utf-8"))
    today = dt.datetime.now(dt.timezone.utc).date()
    gh = GitHub(os.environ.get("GITHUB_TOKEN", ""))

    meta: dict[str, dict] = {}
    for entry in config["featured"]:
        name = entry["repo"]
        try:
            r = gh.repo(name)
        except RuntimeError as exc:
            print(f"Unable to refresh featured project {name}: {exc}", file=sys.stderr)
            # Avoid deleting or de-ranking known projects during API failures.
            raise
        meta[repo_key(name)] = r

    updated = replace_between(existing, FEATURE_START, FEATURE_END,
                              render_featured(config["featured"][:int(config.get("featured_limit", 11))], meta, today))
    if args.no_discovery:
        candidates, added = old_candidates, []
    else:
        candidates, added = discover(gh, config, old_candidates, updated, today)
    updated = replace_between(updated, DISCOVER_START, DISCOVER_END,
                              render_candidates(candidates))
    if updated != existing:
        README_PATH.write_text(updated, encoding="utf-8")
        print("README.md updated")
    else:
        print("README.md unchanged")
    if candidates != old_candidates:
        CANDIDATES_PATH.write_text(json.dumps(candidates, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"New candidates: {len(added)}; queued: {len(candidates)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
