# Headscale Setup — caddy droplet (143.110.228.9)

Headscale provides a self-hosted Tailscale-compatible VPN mesh.
The caddy droplet runs Headscale; all droplets and local machines join the same tailnet.

## Install Headscale on caddy

```bash
# SSH into caddy
ssh root@143.110.228.9

# Download Headscale (check https://github.com/juanfont/headscale/releases for latest)
HEADSCALE_VERSION="0.25.0"
ARCH=$(dpkg --print-architecture)
wget "https://github.com/juanfont/headscale/releases/download/v${HEADSCALE_VERSION}/headscale_${HEADSCALE_VERSION}_linux_${ARCH}.deb"
dpkg -i headscale_*.deb

# Configure
cat > /etc/headscale/config.yaml << 'EOF'
server_url: https://caddy.busboom.org:443
listen_addr: 0.0.0.0:8080
metrics_listen_addr: 127.0.0.1:9090
grpc_listen_addr: 0.0.0.0:50443
grpc_allow_insecure: false

noise:
  private_key_path: /var/lib/headscale/noise_private.key

ip_prefixes:
  - 100.64.0.0/10
  - fd7a:115c:a1e0::/48

derp:
  server:
    enabled: false
  urls: []
  paths: []
  auto_update_enabled: true
  update_frequency: 24h

disable_check_updates: false
ephemeral_node_inactivity_timeout: 30m

database:
  type: sqlite3
  sqlite:
    path: /var/lib/headscale/db.sqlite

acls: []
EOF

# Set up Caddy to proxy Headscale
# Add this to /etc/caddy/Caddyfile:
#
# headscale.busboom.org {
#     reverse_proxy localhost:8080
# }

# Start Headscale
systemctl enable headscale
systemctl start headscale
```

## Join docker1 to the tailnet

```bash
# On caddy, create a pre-auth key
headscale preauthkeys create --user default --reusable --expiration 24h

# On docker1, install and join
ssh root@10.124.0.2
curl -fsSL https://tailscale.com/install.sh | sh
tailscale up --login-server https://caddy.busboom.org:443 --authkey <preauth-key>
```

## Join local machine (gala)

```bash
# macOS — Tailscale client already installed
tailscale up --login-server https://caddy.busboom.org:443 --authkey <preauth-key>
```

After joining, docker1 gets a 100.64.x.x IP reachable from gala without the jump host.