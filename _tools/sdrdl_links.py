#!/usr/bin/env python3
"""Turn links to the old WordPress hosts into site-relative links.

www.sandiegodata.org and data.sandiegodata.org are now one Hugo site. Links
to either host are rewritten to the matching page's path. The list of real
pages comes from `hugo list all`. A link whose path is not a page is matched
by its last path segment (WordPress redirected old slugs the same way);
anything still unresolved is reported and left absolute.

    python3 _tools/sdrdl_links.py www.sandiegodata.org [--dry-run]
"""
import argparse
import csv
import io
import re
import subprocess
from collections import Counter, defaultdict
from pathlib import Path

LINK = re.compile(r"https?://(?:(www|data)\.)?sandiegodata\.org(/[^\s)\"'<>\]]*)?")

# data.sandiegodata.org paths that moved when the two sites were merged
DATA_PATHS = {
    "/": "/dataset/",
    "/about/": "/dataset/about/",
    "/posts/": "/dataset/",
    "/dataset": "/dataset/",
    "/datasets/": "/dataset/",
    "/organization/": "/dataset/",
    "/dataset/category/dataset/": "/dataset/",
    "/homelessness/": "/collections/homelessness/",
}

# Old www.sandiegodata.org sections, by path prefix. The Q&A forum
# (/question/...) was not exported; its service page is the closest match.
WWW_PREFIXES = {
    "/projects/": "/get-data/projects/",
    "/question/": "/get-data/insights/",
}


def tag_names(site):
    names = set()
    for md in (site / "content").rglob("*.md"):
        m = re.search(r"^tags: \[(.*)\]$", md.read_text(), re.M)
        if m:
            names |= {t.lower() for t in re.findall(r'"([^"]+)"', m.group(1))}
    return names


def site_paths(site):
    out = subprocess.run(["hugo", "list", "all", "-s", str(site)],
                         capture_output=True, text=True, check=True).stdout
    # `hugo list` covers regular pages only; add the list pages
    paths = {"/", "/blog/", "/dataset/", "/categories/", "/tags/"}
    paths |= {f"/tags/{t}/" for t in tag_names(site)}
    for row in csv.DictReader(io.StringIO(out)):
        path = re.sub(r"^https?://[^/]+", "", row["permalink"])
        paths.add(path)
    return paths


def norm_slug(slug):
    """Slug with version and CKAN-era suffixes removed, for fuzzy matching."""
    slug = re.sub(r"[_.]", "-", slug.lower())
    slug = re.sub(r"-(extract|rev-\d+|casnd-[0-9a-f]+)$", "", slug)
    slug = re.sub(r"-casnd-[0-9a-f]+", "", slug)
    return re.sub(r"(-\d+)+$", "", slug)


def load_redirects(site):
    redirects = {}
    path = site / "static" / "_redirects"
    if path.exists():
        for line in path.read_text().splitlines():
            parts = line.split()
            if len(parts) >= 2:
                redirects[parts[0].rstrip("/") or "/"] = parts[1]
    return redirects


def find_page(path, paths, by_slug, by_norm):
    if path in paths:
        return path
    slug = path.rstrip("/").rsplit("/", 1)[-1]
    for hits in (by_slug.get(slug, []), by_norm.get(norm_slug(slug), [])):
        if len(hits) == 1:
            return hits[0]
    # Attachment pages and CKAN resources sit under their page: use that page
    parent = path.rstrip("/").rsplit("/", 1)[0] + "/"
    while parent != "/":
        if parent in paths:
            return parent
        parent = parent.rstrip("/").rsplit("/", 1)[0] + "/"
    return None


def resolve(host, path, paths, by_slug, by_norm, redirects):
    path = path or "/"
    path, _, frag = path.partition("#")
    path, _, query = path.partition("?")
    if host == "data":
        if query and path.rstrip("/") == "/dataset":
            query = ""  # CKAN-era searches, e.g. /dataset?groups=crime
        path = DATA_PATHS.get(path, DATA_PATHS.get(path + "/", path))
    if path.startswith("/wp-content/uploads/sites/"):
        new = re.sub(r"^/wp-content/uploads/sites/", "/uploads/", path)
    elif path.startswith("/uploads/") or re.search(r"\.[a-z0-9]{2,4}$", path, re.I):
        new = path
    else:
        path = path.rstrip(".")
        target = redirects.get(path.rstrip("/") or "/")
        if target and target.startswith("http"):
            return target
        if target:
            path = target
        if not path.endswith("/"):
            path += "/"
        new = find_page(path, paths, by_slug, by_norm)
        if new is None and host == "www":
            new = next((t for pre, t in WWW_PREFIXES.items() if path.startswith(pre)), None)
        if new is None and host == "www" and path.startswith("/tag/"):
            new = find_page("/tags/" + path[5:], paths, by_slug, by_norm)
        if new is None:
            return None
    if query:
        new += "?" + query
    if frag:
        new += "#" + frag
    return new


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("site", type=Path)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    paths = site_paths(args.site)
    by_slug, by_norm = defaultdict(list), defaultdict(list)
    for p in paths:
        slug = p.rstrip("/").rsplit("/", 1)[-1]
        by_slug[slug].append(p)
        by_norm[norm_slug(slug)].append(p)
    redirects = load_redirects(args.site)

    total, unresolved = 0, Counter()
    for md in sorted((args.site / "content").rglob("*.md")):
        old = md.read_text()

        def sub(m):
            nonlocal total
            new = resolve(m.group(1) or "www", m.group(2), paths, by_slug, by_norm, redirects)
            if new is None:
                unresolved[m.group(0)] += 1
                return m.group(0)
            total += 1
            return new

        new = LINK.sub(sub, old)
        if new != old and not args.dry_run:
            md.write_text(new)

    print(f"{'would rewrite' if args.dry_run else 'rewrote'} {total} links; "
          f"{sum(unresolved.values())} left unresolved")
    for url, n in unresolved.most_common():
        print(f"  {n:3}  {url}")


if __name__ == "__main__":
    main()
