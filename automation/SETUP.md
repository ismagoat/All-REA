# All-REA automated catalog

This package adds an automated *daily discovery and ranking pipeline* to All-REA.
It updates only the two marked regions in the README. Everything else is yours to edit.

## Installation

1. Upload all supplied files to your repository **preserving their paths**, including `.github/workflows/update-catalog.yml`.
2. Go to GitHub **Settings → Actions → General → Workflow permissions**. Allow **GitHub Actions to create and approve pull requests**. The workflow explicitly requests `contents: write` and `pull-requests: write`.
3. Go to **Actions → Discover and refresh All-REA → Run workflow** to trigger the first scan.
4. Review the PR named **chore: update All-REA directory**; merge if the suggested projects and ranking are appropriate.
5. The action runs automatically **every day at 06:37 UTC**. No separate token, hosting, database, or paid service is necessary.

## How it works

- `automation/catalog.json` = hand-curated, useful featured tools. Raise an item's `priority` (integer) to promote it. Live GitHub stars break ties.
- `automation/update_catalog.py` = GitHub API client, ranking, README updater, discovery + documentation reference check.
- `automation/candidates.json` = persistent queue, reviewed in pull requests.
- README markers = delimit exactly where the bot is allowed to write.
- GitHub Actions = daily scheduling and PR creation.

### Add an approved project

If you have reviewed a candidate and confirmed its use, add a new item to `automation/catalog.json` with the correct `relation`, `title`, `utility`, `category`, and `priority`. Add it to the appropriate permanent README section. **Then remove it from `candidates.json`.** The bot does not grant itself authority to call a discovery 'verified'.

### A few limitations

- GitHub repository search is imperfect and misses projects that do not mention REA clearly.
- A README linking to REA is **not proof** that it actually used REA.
- GitHub rate limits apply; the script uses authenticated API requests with a small built-in delay.
- Featured order is based on **editorial utility tier first, stars second**, rather than falsely presenting a quality/performance leaderboard.
- The daily workflow might be delayed by GitHub's scheduler. PRs need human review.
- For an empty repository, use the included README as a starting point. For an existing customized README, copy the two AUTO marker pairs and their sections into that README, rather than replacing your changes.
