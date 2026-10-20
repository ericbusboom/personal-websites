# docker-do — DigitalOcean Docker Hosting

Project for hosting websites and services on DigitalOcean droplets.
Architecture: public Caddy reverse proxy → private Docker host on VPC network.

## Agent instructions (for Hermes / Claude Code / Codex)

### Architecture

```
Internet → caddy (143.110.228.9, public) → docker1 (10.124.0.2, VPC-only)
              │                                  │
              │ Let's Encrypt TLS                │ Docker Compose
              │ Caddy reverse proxy              │ nginx per site
              │ Headscale VPN                    │ Static sites / apps
```

### Droplets

| Name | Public IP | Private IP | Size | Role |
|---|---|---|---|---|
| caddy | 143.110.228.9 | 10.124.0.3 | 512MB | Reverse proxy, TLS, Headscale |
| docker1 | — | 10.124.0.2 | 1GB | Docker host, all services |

Both in VPC: `6b61cced-6113-4e0b-a1ca-cdcc2b0505d8` (default-sfo3, My Team account)

### DNS

- `caddy.busboom.org` → 143.110.228.9
- `*.busboom.org` → CNAME to `caddy.busboom.org`

### Accessing the droplets

**Caddy droplet:**
```bash
ssh root@143.110.228.9   # or via Headscale once set up
```

**Docker1 (VPC-only, via caddy jump host):**
```bash
ssh -J root@143.110.228.9 root@10.124.0.2
# or via Headscale: ssh root@<headscale-ip>
```

### Adding a new site

1. **Create content** in `sites/<name>/` (Hugo site, static HTML, or app)
2. **Add Docker Compose service** for the site (or reuse existing nginx)
3. **Add Caddy route** in `caddy/Caddyfile`:
   ```
   <name>.busboom.org {
       reverse_proxy 10.124.0.2:<port>
   }
   ```
4. **Deploy to docker1**: `git pull && docker compose up -d`
5. **Reload Caddy**: `ssh root@143.110.228.9 'caddy reload --config /etc/caddy/Caddyfile'`

### Deploy workflow

```bash
# Build the Hugo site
cd sites/garage && hugo --minify

# Push to GitHub
cd /Users/eric/proj/docker/docker-do
git add -A && git commit -m "update" && git push

# Deploy to docker1 (via Headscale or jump host)
ssh root@<docker1> 'cd /opt/docker-do && git pull && docker compose up -d --force-recreate'

# Verify
curl -sI https://garage.busboom.org | head -5
```

### Caddy config management

The Caddyfile lives at `caddy/Caddyfile` in this repo. On the caddy droplet, it's deployed to `/etc/caddy/Caddyfile`.

```bash
# Copy Caddyfile to caddy droplet
scp caddy/Caddyfile root@143.110.228.9:/etc/caddy/Caddyfile

# Reload
ssh root@143.110.228.9 'caddy reload --config /etc/caddy/Caddyfile'

# Check status
ssh root@143.110.228.9 'systemctl status caddy'
```

### Headscale

Headscale runs on the caddy droplet. This provides a Tailscale-compatible VPN mesh:
- All droplets + local machines join the same tailnet
- Deploy directly to docker1's Headscale IP instead of going through the jump host
- Caddy on the public droplet serves as both the reverse proxy and the Headscale coordinator

Setup: see `headscale/setup.md`.

### Monitoring

```bash
# Check docker1 services
ssh root@10.124.0.2 'docker compose ps && docker stats --no-stream'

# Check Caddy
ssh root@143.110.228.9 'systemctl status caddy && caddy version'

# Check disk (512MB droplet is tight!)
ssh root@143.110.228.9 'df -h /'
```

### Pitfalls

- **docker1 is VPC-only** — no public IP. All inbound traffic goes through caddy.
- **No swap on small droplets** — the 512MB caddy droplet may struggle under memory pressure. Add swap file if needed.
- **GitHub repo is private** — use SSH keys or token for git operations on droplets.
- **DO token**: `DIGITALOCEAN_ACCESS_TOKEN` in `~/.zshenv`. This is the "My Team" account (eric@civicknowledge.com).
- **SSH keys**: Droplets were created without SSH keys. Password reset was used for initial access. After gaining root, add `~/.ssh/id_rsa.pub` from gala to `authorized_keys`.
- **31MB GLB file**: The backyard-current.glb is large but under GitHub's 100MB limit. It's served as a static asset by nginx.
- **Caddy wildcard TLS**: `*.busboom.org` is a CNAME to `caddy.busboom.org`. Each new subdomain gets auto-TLS from Let's Encrypt.