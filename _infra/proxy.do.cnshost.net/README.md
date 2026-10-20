# proxy.do.cnshost.net — Caddy reverse proxy

Production Caddy reverse proxy on DigitalOcean droplet `proxy.do.cnshost.net` (137.184.225.100).

Routes TLS-terminated traffic to backend WordPress server `wp2` (137.184.39.244) and Docker host `docker1` (146.190.130.5).

## Domains served

| Domain | Backend |
|---|---|
| busboom.org, www.busboom.org | wp2:80 |
| eric.busboom.org, max.busboom.org, jenni.busboom.org | wp2:80 |
| wordpress.busboom.org | wp2:80 |
| ericbusboom.com | wp2:80 |
| civicknowledge.com, www.civicknowledge.com | wp2:80 |
| sandiegodata.org, www.sandiegodata.org | wp2:80 |
| data.sandiegodata.org, insights.sandiegodata.org | wp2:80 |
| metatab.org, www.metatab.org | wp2:80 |
| lajollatroop506.com, www.lajollatroop506.com | wp2:80 |
| sdcta.civicknowledge.com | wp2:80 |
| tablecloth.civicknowledge.com | wp2:80 |
| phpmyadmin.busboom.org | 161.35.239.192:80 |
| garage.busboom.org | docker1:80 |
| proxy.do.cnshost.net | responds "hello" (health check) |

## TLS

ZeroSSL via ACME. Certificates auto-renewed by Caddy.

## Deploy

```bash
scp Caddyfile root@proxy.do.cnshost.net:/etc/caddy/Caddyfile
ssh root@proxy.do.cnshost.net 'systemctl reload caddy'
```