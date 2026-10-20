# docker-do

Docker-based hosting on DigitalOcean droplets.

## Architecture

```
Internet
  │
  ▼
caddy.busboom.org (143.110.228.9)  ← public, Let's Encrypt TLS
  │
  │  VPC network (10.124.0.0/20)
  ▼
docker1 (10.124.0.2)               ← private, Docker Compose
  ├── garage (nginx, port 8080)    → garage.busboom.org
  └── ... (future services)
```

## Sites

| Domain | Description | Backend |
|---|---|---|
| [garage.busboom.org](https://garage.busboom.org) | Garage rebuild project: 3D model, report, cost estimate | nginx (Hugo static) |

## Quick start

```bash
# Build and serve locally
cd sites/garage && hugo server

# Deploy
git push
ssh docker1 'cd /opt/docker-do && git pull && docker compose up -d'
```

## Directory structure

```
docker-do/
├── AGENTS.md              # Agent instructions (for Hermes/Claude/Codex)
├── README.md              # This file
├── docker-compose.yml     # Docker Compose for docker1
├── nginx-garage.conf      # nginx config for garage site
├── caddy/
│   └── Caddyfile          # Caddy reverse proxy config
├── headscale/
│   └── setup.md           # Headscale VPN setup
├── config/                # dotconfig environment config
├── sites/
│   └── garage/            # Hugo site for garage.busboom.org
│       ├── content/       # Markdown content
│       ├── static/        # 3D model, JS, images
│       └── themes/        # Custom dark theme
└── scripts/
    └── deploy.sh          # Deployment helper
```

## Droplet inventory

See `AGENTS.md` for full details and operational instructions.