# www.sandiegodata.org

The San Diego Regional Data Library: a Hugo site made from two WordPress
blogs, the main site (blog 7, www.sandiegodata.org) and the data repository
(blog 6, data.sandiegodata.org).

| Content | Where | URL |
|---|---|---|
| Blog posts | `content/YYYY/MM/` | `/YYYY/MM/slug/`, as on WordPress |
| Datasets | `content/dataset/` | `/dataset/slug/`, as on data.sandiegodata.org |
| Pages | `content/*.md` | their WordPress path, set by `url:` |
| Collections | `content/data-*.md` | `/collections/slug/` |

Data files are not in this repo. They are in the public S3 bucket
`library-metatab-org`, copied from the archived `library.metatab.org`,
`cde.metatab.org` and `ds.civicknowledge.org` buckets.

## Development

```bash
just dev    # or: hugo server --buildDrafts
just build  # or: hugo --minify --buildDrafts
```

## Hosting

Served by the `websites.busboom.org` stack
([_infra/websites.busboom.org](../_infra/websites.busboom.org/README.md)).
Short-link redirects and the `data.sandiegodata.org` → www redirects are in
[sandiegodata.caddy](../_infra/websites.busboom.org/sandiegodata.caddy).

## How the content was made

From the repo root, in this order. Each step edits `content/` in place;
rerunning step 1 throws away the later fixes to pages, so rerun the rest
after it.

```bash
# 1. pages from both blogs, at their WordPress URLs, with post lists
uv run --with html2text --with python-dateutil \
    python3 _tools/sdrdl_pages.py _export www.sandiegodata.org/content
# 2. data file links -> library-metatab-org bucket
python3 _tools/relink_data_files.py www.sandiegodata.org/content
# 3. links to the old www./data. hosts -> site-relative links
python3 _tools/sdrdl_links.py www.sandiegodata.org
# 4. image and file links that point at missing uploads
aws s3 ls --recursive s3://library-metatab-org/ | awk '{$1=$2=$3=""; sub(/^ +/,""); print}' > /tmp/keys.txt
python3 _tools/sdrdl_media.py www.sandiegodata.org /tmp/keys.txt
# 5. WordPress leftovers: tab bars, [code] blocks, buttons
python3 _tools/sdrdl_cleanup.py www.sandiegodata.org/content
```

Files that could not be found anywhere are marked "(no longer available)"
in the pages that listed them.
