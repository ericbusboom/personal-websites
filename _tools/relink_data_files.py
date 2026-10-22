#!/usr/bin/env python3
"""Point data-file links at the library-metatab-org S3 bucket.

The old buckets (library.metatab.org, cde.metatab.org, ds.civicknowledge.org)
are disabled. Their files were copied to s3://library-metatab-org:
library.metatab.org objects at the bucket root, the other two under a folder
named after the old host.

    python3 _tools/relink_data_files.py www.sandiegodata.org/content [--dry-run]
"""
import argparse
import pathlib
import re

BASE = "https://library-metatab-org.s3.amazonaws.com/"

# Every way the old hosts were written, mapped to the prefix in the new bucket.
OLD_HOSTS = [
    (r"https?://s3\.amazonaws\.com/library\.metatab\.org/", ""),
    (r"https?://library\.metatab\.org\.s3\.amazonaws\.com/", ""),
    (r"https?://library\.metatab\.org/", ""),
    (r"https?://s3\.amazonaws\.com/cde\.metatab\.org/", "cde.metatab.org/"),
    (r"https?://cde\.metatab\.org/", "cde.metatab.org/"),
    (r"https?://s3\.amazonaws\.com/ds\.civicknowledge\.org/", "ds.civicknowledge.org/"),
    (r"https?://ds\.civicknowledge\.org\.s3\.amazonaws\.com/", "ds.civicknowledge.org/"),
    (r"https?://ds\.civicknowledge\.org/", "ds.civicknowledge.org/"),
]

# Files that only exist under a newer version.
RENAMES = {
    "sandiegodata.org-planning-tracts-1.zip": "sandiegodata.org-planning-tracts-2.zip",
}


def relink(text):
    count = 0
    for pattern, prefix in OLD_HOSTS:
        text, n = re.subn(pattern, BASE + prefix, text)
        count += n
    for old, new in RENAMES.items():
        text = text.replace(BASE + old, BASE + new)
    return text, count


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("content_dir", type=pathlib.Path)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    total = files = 0
    for path in sorted(args.content_dir.rglob("*.md")):
        old = path.read_text()
        new, n = relink(old)
        if n:
            files += 1
            total += n
            if not args.dry_run:
                path.write_text(new)
    print(f"{'would rewrite' if args.dry_run else 'rewrote'} {total} links in {files} files")


if __name__ == "__main__":
    main()
