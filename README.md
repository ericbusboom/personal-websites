# personal-websites

Content and config for personal websites. One directory per website.

## Structure

```
personal-websites/
├── eric.busboom.org/          # Hugo static site
├── max.busboom.org/           # Hugo static site
├── www.metatab.org/           # Hugo static site
├── www.civicknowledge.com/    # Hugo static site
├── www.sandiegodata.org/      # Hugo static site
├── explainers/                # Hugo static site
├── lajollatroop506.com/       # WordPress site (not yet converted)
│   ├── www.lajollatroop506.com/  # Docker/WordPress config
│   ├── troop506-theme/           # WordPress theme
│   └── google-connector/         # G Suite integration scripts
├── localhost/                 # Local dev stack: Caddy proxy + every site in its own container (`just up`)
├── _infra/
│   ├── proxy.do.cnshost.net/ # Caddy reverse proxy config
│   └── docker-do/             # Docker hosting config
├── _tools/
│   ├── wp2hugo.py             # WordPress WXR → Hugo Markdown converter
│   └── wp-static-theme/       # Custom Hugo theme approximating original WordPress designs
└── _export/                   # WXR XML exports + media from the WordPress multisite (not in git — too large)
```

## Background

These sites were originally a WordPress multisite on DigitalOcean droplet `wp2.do.cnshost.net` (137.184.39.244). The multisite had 17 blogs across multiple domains. In July 2026, the server was compromised with malware; the database content was clean but the PHP files were infected.

7 of the 17 blogs were converted to Hugo static sites and deployed to GitHub Pages:

| Blog ID | Domain | Converted To | Status |
|---------|--------|---------------|--------|
| 9 + 12 | eric.busboom.org, ericbusboom.com | `eric.busboom.org` repo | ✅ Live on GitHub Pages |
| 10 | max.busboom.org | `max.busboom.org` repo | ✅ Live on GitHub Pages |
| 2 | www.metatab.org | `www.metatab.org` repo | ✅ Live on GitHub Pages |
| 3 | www.civicknowledge.com | `www.civicknowledge.com` repo | ✅ Live on GitHub Pages |
| 6 + 7 | www.sandiegodata.org, data.sandiegodata.org | `www.sandiegodata.org` repo | ✅ Live on GitHub Pages |

**Not yet converted:**

| Blog ID | Domain | Notes |
|---------|--------|-------|
| 8 | www.lajollatroop506.com | 25 pages, 17 posts, WooCommerce products — needs migration plan |
| 4 | insights.civicknowledge.com | 8 posts |
| 5 | tablecloth.civicknowledge.com | 11 posts |
| 11 | jenni.busboom.org | 1 post |
| 13-17 | Various small sites | not.evenwrong.com, westerndissident.org, etc. |

## WordPress Server

The original WordPress multisite is still running at `wp2.do.cnshost.net` (137.184.39.244), proxied through `proxy.do.cnshost.net` (137.184.225.100) via Caddy.

## Running everything locally

```bash
cd localhost && just up        # http://localhost:8000/ — index of all sites
just wp                        # also run Troop 506 WordPress at http://troop506.localhost:8000/
```

Each site gets its own `*.localhost` hostname (no /etc/hosts edits needed) and runs
`hugo server` with live reload in its own container. Port and domain are set in `localhost/.env`.

## Submodules

Each site and infra directory is a git submodule with its own repo; that repo
is where the site's content lives. Clone with `git clone --recursive`, or run
`git submodule update --init` after cloning.

| Directory | Repo |
|---|---|
| `_infra/docker-do` | [ericbusboom/docker-do](https://github.com/ericbusboom/docker-do) |
| `_infra/proxy.do.cnshost.net` | [ericbusboom/proxy-do-cnshost-net](https://github.com/ericbusboom/proxy-do-cnshost-net) |
| `eric.busboom.org` | [ericbusboom/eric.busboom.org](https://github.com/ericbusboom/eric.busboom.org) |
| `explainers` | [ericbusboom/explainers](https://github.com/ericbusboom/explainers) |
| `lajollatroop506.com/google-connector` | [troop506/google-connector](https://github.com/troop506/google-connector) |
| `lajollatroop506.com/troop506-theme` | [troop506/troop506-theme](https://github.com/troop506/troop506-theme) |
| `max.busboom.org` | [ericbusboom/max.busboom.org](https://github.com/ericbusboom/max.busboom.org) |
| `www.civicknowledge.com` | [ericbusboom/www.civicknowledge.com](https://github.com/ericbusboom/www.civicknowledge.com) |
| `www.metatab.org` | [ericbusboom/www.metatab.org](https://github.com/ericbusboom/www.metatab.org) |
| `www.sandiegodata.org` | [ericbusboom/www.sandiegodata.org](https://github.com/ericbusboom/www.sandiegodata.org) |

To change a site: commit and push inside its directory, then commit the new
submodule pointer here.

From 2026-10-19 to 2026-10-21 these were plain directories in this repo; the
changes made then were pushed to each repo before it became a submodule again.

`lajollatroop506.com/www.lajollatroop506.com` (the troop WordPress Docker
setup) stays a plain directory. Its old repo, troop506/www.lajollatroop506.com,
is now the Hugo rebuild of the troop site, checked out next to this repo.
