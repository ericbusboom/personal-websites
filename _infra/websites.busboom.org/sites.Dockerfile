# syntax=docker/dockerfile:1
#
# Front-door image for websites.busboom.org: builds every Hugo site in this
# repo and serves them with Caddy, which also routes to WordPress.
#
# Build context is the repo root (see compose.yaml). Each site is built twice:
#   /srv/sites/<name>/prod   baseURL = its real domain
#   /srv/sites/<name>/test   baseURL = TEST_SCHEME://<name>.TEST_HOST[TEST_PORT]/
# so links stay on whichever hostname you are viewing.

FROM ghcr.io/gohugoio/hugo:v0.157.0 AS hugo
USER root
ARG TEST_SCHEME=https
ARG TEST_HOST=websites.busboom.org
# e.g. ":8080" when testing locally on a non-standard port
ARG TEST_PORT=
COPY . /src
WORKDIR /src
# name  directory  production baseURL ("-" = no production domain)
RUN set -eu; \
    while read -r name dir url; do \
        [ "$url" = "-" ] || hugo --quiet --minify --buildDrafts -s "$dir" -d "/out/$name/prod" -b "$url"; \
        hugo --quiet --minify --buildDrafts -s "$dir" -d "/out/$name/test" -b "$TEST_SCHEME://$name.$TEST_HOST$TEST_PORT/"; \
    done <<'EOF'
eric            eric.busboom.org        https://eric.busboom.org/
max             max.busboom.org         https://max.busboom.org/
metatab         www.metatab.org         https://www.metatab.org/
civicknowledge  www.civicknowledge.com  https://www.civicknowledge.com/
sandiegodata    www.sandiegodata.org    https://www.sandiegodata.org/
explainers      explainers              -
EOF

# The Hugo rebuild of www.lajollatroop506.com lives in its own repo (build
# context "troop506static"). Test URL only; production is GitHub Pages.
COPY --from=troop506static . /src-static
RUN hugo --quiet -s /src-static -d /out/static/test -b "$TEST_SCHEME://static.$TEST_HOST$TEST_PORT/"

FROM caddy:2.10-alpine
COPY --from=hugo /out /srv/sites
COPY _infra/websites.busboom.org/www /srv/index
COPY _infra/websites.busboom.org/Caddyfile /etc/caddy/Caddyfile
