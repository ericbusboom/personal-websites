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

The converted sites are served by GitHub Pages; each repo's workflow publishes
it on every push, and DNS points the domain at GitHub (October 2026).

| Domain | Served from | Notes |
|---|---|---|
| www.sandiegodata.org, sandiegodata.org | `www.sandiegodata.org` repo | WordPress blogs 6 + 7 merged |
| data.sandiegodata.org | ericbusboom/data.sandiegodata.org | Redirect-only: every path goes to www.sandiegodata.org |
| eric.busboom.org | `eric.busboom.org` repo | Blogs 9 + 12 merged |
| ericbusboom.com, www.ericbusboom.com | ericbusboom/ericbusboom.com | Redirect-only: to eric.busboom.org (`/` → `/professional/`) |
| max.busboom.org | `max.busboom.org` repo | |
| www.civicknowledge.com, civicknowledge.com | `www.civicknowledge.com` repo | |
| www.metatab.org, metatab.org | Metatab/www.metatab.org | Not the WordPress conversion; the `www.metatab.org` repo here is unused |
| www.lajollatroop506.com, lajollatroop506.com | troop506/www.lajollatroop506.com | Hugo rebuild of the troop WordPress site, edited with Sveltia CMS |

DNS for lajollatroop506.com and ericbusboom.com is at GoDaddy; the others are
at DNS Made Easy. Bare domains use GitHub's A records (185.199.108–111.153);
`www` and subdomains are CNAMEs to `ericbusboom.github.io`, `troop506.github.io`
or `metatab.github.io`.

**Still on the old WordPress server** (through the proxy): insights.sandiegodata.org,
tablecloth.civicknowledge.com, sdcta.civicknowledge.com, jenni.busboom.org,
www.busboom.org. Other blogs that were never converted: insights.civicknowledge.com
(blog 4), and blogs 13–17 (not.evenwrong.com, westerndissident.org, etc.).

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
