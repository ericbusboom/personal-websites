#!/usr/bin/env python3
"""Write static redirect pages for a Hugo site hosted on GitHub Pages.

GitHub Pages cannot send real redirects, so each short link becomes
static/<path>/index.html with a meta refresh and a JavaScript redirect.
The list is a TSV file of `path<TAB>target` lines; lines starting with `#`
are comments.

    python3 _tools/redirect_pages.py www.sandiegodata.org/redirects.tsv www.sandiegodata.org/static
"""
import argparse
import html
from pathlib import Path

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Redirecting…</title>
<link rel="canonical" href="{url}">
<meta name="robots" content="noindex">
<meta http-equiv="refresh" content="0; url={url}">
<script>var t = {js}; location.replace(t.indexOf("#") < 0 ? t + location.hash : t)</script>
</head>
<body><p>This page has moved to <a href="{url}">{url}</a>.</p></body>
</html>
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("tsv", type=Path)
    ap.add_argument("static_dir", type=Path)
    args = ap.parse_args()

    count = 0
    for line in args.tsv.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        path, target = line.split("\t")
        out = args.static_dir / path.strip("/") / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        js = '"' + target.replace("\\", "\\\\").replace('"', '\\"') + '"'
        out.write_text(PAGE.format(url=html.escape(target, quote=True), js=js))
        count += 1
    print(f"wrote {count} redirect pages under {args.static_dir}")


if __name__ == "__main__":
    main()
