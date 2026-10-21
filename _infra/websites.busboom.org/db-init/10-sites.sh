#!/bin/sh
# Runs once, when the db volume is first created: one database and user per
# WordPress site, loaded from the site's clean dump if it is mounted.
set -eu

site() {  # site NAME PASSWORD DUMP
    mariadb -uroot -p"$MARIADB_ROOT_PASSWORD" <<SQL
CREATE DATABASE IF NOT EXISTS \`$1\`;
CREATE USER IF NOT EXISTS '$1'@'%' IDENTIFIED BY '$2';
GRANT ALL ON \`$1\`.* TO '$1'@'%';
SQL
    if [ -f "$3" ]; then
        echo "Loading $3 into $1"
        zcat "$3" | mariadb -uroot -p"$MARIADB_ROOT_PASSWORD" "$1"
    fi
}

site troop506 "$TROOP506_DB_PASSWORD" /seed/troop506/troop506-clean.sql.gz
