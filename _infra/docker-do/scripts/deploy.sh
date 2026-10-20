#!/bin/bash
# Deploy helper for docker-do
# Usage: ./scripts/deploy.sh [site-name]
#   No args: deploy everything
#   site-name: deploy just that site

set -euo pipefail

REPO_DIR="/opt/docker-do"
CADDY_HOST="root@143.110.228.9"
DOCKER_HOST="root@10.124.0.2"

SITE="${1:-}"

echo "=== docker-do deploy ==="

# Build Hugo sites
if [ -z "$SITE" ] || [ "$SITE" = "garage" ]; then
    echo "→ Building garage site..."
    cd sites/garage && hugo --minify && cd -
fi

# Push to docker1
echo "→ Pulling on docker1..."
ssh "$DOCKER_HOST" "cd $REPO_DIR && git pull"

# Rebuild containers
echo "→ Restarting containers..."
if [ -z "$SITE" ]; then
    ssh "$DOCKER_HOST" "cd $REPO_DIR && docker compose up -d --force-recreate"
else
    ssh "$DOCKER_HOST" "cd $REPO_DIR && docker compose up -d --force-recreate $SITE"
fi

# Reload Caddy
echo "→ Reloading Caddy..."
scp caddy/Caddyfile "$CADDY_HOST:/etc/caddy/Caddyfile"
ssh "$CADDY_HOST" 'caddy reload --config /etc/caddy/Caddyfile'

# Verify
sleep 2
echo "→ Verifying..."
curl -sI https://garage.busboom.org/ 2>/dev/null | head -3 || echo "⚠ Could not reach garage.busboom.org"

echo "✓ Deploy complete"