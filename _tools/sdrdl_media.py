#!/usr/bin/env python3
"""Fix /uploads/ links on www.sandiegodata.org that point at missing files.

Posts copied between the WordPress blogs kept the other blog's media paths
(/uploads/12/..., /uploads/2018/...). For each /uploads/ link whose file is
not in static/, this script tries, in order:

  1. the same file under another blog's folder in static/uploads/
  2. a file with the same name in the library-metatab-org bucket
     (package docs, e.g. codebooks), given as a key listing
  3. otherwise the link is removed: link text stays, marked unavailable;
     images are dropped

    aws s3 ls --recursive s3://library-metatab-org/ | ... > keys.txt
    python3 _tools/sdrdl_media.py www.sandiegodata.org keys.txt [--dry-run]
"""
import argparse
import re
from collections import Counter, defaultdict
from pathlib import Path

BASE = "https://library-metatab-org.s3.amazonaws.com/"
UPLOAD = re.compile(r"/uploads/[^\s)\"'<>#]+")
IMAGE = re.compile(r"!\[[^\]]*\]\(<?(/uploads/[^)>]+)>?\)")
# Absolute WordPress upload URLs on any of the old hosts
ABSOLUTE = re.compile(r"https?://[^/\s)>]+/wp-content/uploads/(?:sites/)?")
# A link whose only content was a removed image
EMPTY = re.compile(r"(?<!!)\[\]\((<?https?://[^)]+>?)\)")
# html2text wrapped some long upload URLs across lines
SPLIT = re.compile(r"(\(<?/uploads/[^\s)>]*)\n([^\s)>]+)")
LINK = re.compile(r"\[(?P<text>[^\]]*)\]\(<?(?P<url>/uploads/[^)>]+|/storage/[^)>]+)>?\)")


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("site", type=Path)
    ap.add_argument("bucket_keys", type=Path)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    static = args.site / "static"
    by_rest = defaultdict(list)  # "2013/01/x.png" -> ["/uploads/7/2013/01/x.png"]
    by_name = defaultdict(list)
    for f in (static / "uploads").rglob("*"):
        if f.is_file():
            url = "/" + str(f.relative_to(static))
            by_rest[re.sub(r"^/uploads/(\d+/)?", "", url)].append(url)
            by_name[f.name].append(url)
    keys = defaultdict(list)
    for key in args.bucket_keys.read_text().splitlines():
        keys[key.rsplit("/", 1)[-1]].append(key)

    def fix(url):
        if (static / url.lstrip("/")).is_file():
            return url
        rest = re.sub(r"^/uploads/(\d+/)?", "", url)
        name = url.rsplit("/", 1)[-1]
        for hits in (by_rest.get(rest, []), by_name.get(name, [])):
            if len(set(hits)) == 1:
                return hits[0]
        if len(keys.get(name, [])) >= 1:
            # same document in several package versions: take the newest
            return BASE + sorted(keys[name])[-1]
        return None

    stats = Counter()
    for md in sorted((args.site / "content").rglob("*.md")):
        old = md.read_text()

        def image(m):
            if fix(m.group(1).split("#")[0]) is None:
                stats["image removed"] += 1
                return ""
            return m.group(0)

        def link(m):
            url = m.group("url")
            path, hash_, frag = url.partition("#")
            if url.startswith("/storage/") or fix(path) is None:
                stats["link removed"] += 1
                return f"{m.group('text')} (no longer available)"
            return m.group(0)

        def remap(m):
            new = fix(m.group(0))
            if new and new != m.group(0):
                stats["link moved"] += 1
                return new
            return m.group(0)

        new = old
        while SPLIT.search(new):
            new = SPLIT.sub(r"\1\2", new)
        new = ABSOLUTE.sub("/uploads/", new)
        new = IMAGE.sub(image, new)
        new = EMPTY.sub(r"[link](\1)", new)
        new = LINK.sub(link, new)
        new = UPLOAD.sub(remap, new)
        if new != old and not args.dry_run:
            md.write_text(new)

    print(", ".join(f"{k}: {v}" for k, v in sorted(stats.items())) or "nothing to fix")


if __name__ == "__main__":
    main()
