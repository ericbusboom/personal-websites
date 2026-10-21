# websites.busboom.org

One Docker Compose stack that runs every site in this repo on the
`websites.busboom.org` droplet. It replaces the old WordPress multisite
(`wp2`, 137.184.39.244) one site at a time.

```
browser ──https──▶ proxy.do.cnshost.net ──http──▶ websites droplet :80
                   (public Caddy, TLS)            web (Caddy) ─┬─ Hugo sites (static, in the image)
                                                               └─ troop506 (WordPress) ── db (MariaDB)
```

## Hostnames

Every site answers to two names: a **test URL**, linked from the index page,
and its **real domain**, which is the name of its directory in this repo.

| Site | Test URL | Real domain(s) |
|---|---|---|
| index | https://websites.busboom.org/ | — |
| eric.busboom.org | https://eric.websites.busboom.org/ | eric.busboom.org |
| max.busboom.org | https://max.websites.busboom.org/ | max.busboom.org |
| www.metatab.org | https://metatab.websites.busboom.org/ | www.metatab.org, metatab.org → www |
| www.civicknowledge.com | https://civicknowledge.websites.busboom.org/ | www.civicknowledge.com, civicknowledge.com → www |
| www.sandiegodata.org | https://sandiegodata.websites.busboom.org/ | www.sandiegodata.org, sandiegodata.org → www |
| explainers | https://explainers.websites.busboom.org/ | none (production is GitHub Pages) |
| www.lajollatroop506.com | https://troop506.websites.busboom.org/ | www.lajollatroop506.com, lajollatroop506.com → www |
| static.lajollatroop506.com | https://static.websites.busboom.org/ | none — Hugo rebuild of the troop site, from the separate `www.lajollatroop506.com` repo next to this one; production will be GitHub Pages |

Hugo sites are built twice into the image (see [sites.Dockerfile](sites.Dockerfile)),
once per name, so links stay on the name you are viewing. WordPress stores
only its real URL; the [alt-host mu-plugin](../../lajollatroop506.com/www.lajollatroop506.com/wordpress/mu-plugins/alt-host.php)
rewrites it when viewed on the test URL.

## Testing a site, then cutting it over

1. **Test URL.** Open https://websites.busboom.org/ and follow the link.
2. **Real domain, privately.** Point the domain at the droplet in `/etc/hosts`:
   ```
   <droplet IP>  www.civicknowledge.com civicknowledge.com
   ```
   The droplet serves real domains over https with a self-signed certificate
   (Caddy `tls internal`), so expect a certificate warning. Remove the line
   when done.
3. **Cut over.** For domains already on the public proxy, change their
   `reverse_proxy` in [../proxy.do.cnshost.net/Caddyfile](../proxy.do.cnshost.net/Caddyfile)
   from `137.184.39.244:80` (wp2) to the droplet and reload Caddy. Domains
   whose DNS is elsewhere (www.metatab.org on GitHub Pages, sandiegodata.org,
   metatab.org) first need their DNS pointed at the proxy.

## Running it

```bash
just new-env   # once: writes .env with DB passwords and WordPress salts; set DEPLOY_HOST
just local     # whole stack on this machine: http://websites.localhost:8090/
just seed      # once: copy troop506 uploads + DB dump (gitignored) to the droplet
just deploy    # rsync the repo + .env to the droplet, rebuild and restart there
```

On first start, [db-init/10-sites.sh](db-init/10-sites.sh) creates a database
and user per WordPress site and loads its clean dump. It runs only when the
`db` volume is new; to add a WordPress site later, add a `site` line there
and create the database by hand on the running server.
