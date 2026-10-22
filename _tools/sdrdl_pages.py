#!/usr/bin/env python3
"""Rebuild the pages of www.sandiegodata.org from both WordPress blogs.

The site merges blog 7 (www.sandiegodata.org) and blog 6, the data repository
(data.sandiegodata.org). wp2hugo.py wrote every page flat into content/, so
nested URLs were lost, pages with the same slug in both blogs overwrote each
other, and post lists became placeholder notes. This script regenerates the
pages only (posts and datasets are left alone):

  - each page keeps its WordPress URL via `url:` front matter
  - blog 7 home  -> content/_index.md       (site front page)
  - blog 7 blog  -> content/blog/_index.md  (list of all posts)
  - blog 6 home  -> content/dataset/_index.md (data repository front page)
  - other blog 6 pages keep their path, except where blog 7 has the same
    path (/about/), which move under /dataset/
  - [display-posts] shortcodes and advgb/recent-posts blocks become
    {{< post-list >}} shortcodes with the same filters

    uv run --with html2text --with python-dateutil \
        python3 _tools/sdrdl_pages.py _export www.sandiegodata.org/content
"""
import argparse
import html
import json
import re
import shlex
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import wp2hugo  # noqa: E402

NS = wp2hugo.NS
BLOGS = [
    (7, "www.sandiegodata.org", "blog7/sandiegoregionaldatalibrary.wordpress.2026-07-09.000.xml"),
    (6, "data.sandiegodata.org", "blog6/sdrdldatarepository.wordpress.2026-07-09.000.xml"),
]
SKIP_SLUGS = wp2hugo.SKIP_PAGES | {"posts"}  # blog 6 "posts" was its dataset index
# Tags named in post lists that the datasets actually carry under another name
TAG_ALIASES = {"homeless": "homelessness"}


def text(el, path):
    found = el.find(path, NS)
    return (found.text or "") if found is not None else ""


def load_blog(xml_path):
    root = ET.parse(xml_path).getroot()
    channel = root.find("channel")
    tags = {text(t, "wp:tag_slug"): html.unescape(text(t, "wp:tag_name"))
            for t in channel.findall("wp:tag", NS)}
    cats = {text(c, "wp:term_id"): html.unescape(text(c, "wp:cat_name"))
            for c in channel.findall("wp:category", NS)}
    cats_by_slug = {text(c, "wp:category_nicename"): html.unescape(text(c, "wp:cat_name"))
                    for c in channel.findall("wp:category", NS)}
    items = {}
    for it in channel.findall("item"):
        items[text(it, "wp:post_id")] = it
    return items, tags, cats, cats_by_slug


def url_path(link):
    return "/" + link.split("://", 1)[1].split("/", 1)[1] if "://" in link else link


def post_list_shortcode(args, tags, cats, cats_by_slug, items, section):
    """Translate display-posts / advgb settings into a post-list shortcode."""
    attrs = {"section": section}
    if "tag" in args:
        slugs = [s.strip() for s in re.split(r"[,+]", args["tag"]) if s.strip()]
        names = [tags.get(s, s) for s in slugs]
        names = [TAG_ALIASES.get(n, n) for n in names]
        attrs["tags"] = ",".join(names)
    if "category" in args:
        c = str(args["category"])
        attrs["category"] = cats.get(c) or cats_by_slug.get(c, c)
    if "id" in args:
        target = items.get(str(args["id"]))
        if target is not None:
            attrs["pages"] = url_path(target.find("link").text)
    if args.get("include_excerpt") == "true":
        attrs["excerpt"] = "true"
    inner = " ".join(f'{k}="{v}"' for k, v in attrs.items())
    return "{{< post-list " + inner + " >}}"


def replace_lists(content, tags, cats, cats_by_slug, items, section):
    """Swap post lists for tokens that survive HTML-to-Markdown conversion."""
    found = []

    def token(sc):
        found.append(sc)
        return f"\n\nPOSTLIST{len(found) - 1}TOKEN\n\n"

    def display_posts(m):
        args = dict(re.findall(r'(\w+)="([^"]*)"', m.group(0)))
        return token(post_list_shortcode(args, tags, cats, cats_by_slug, items, section))

    def advgb(m):
        args = json.loads(m.group(1))
        return token(post_list_shortcode(args, tags, cats, cats_by_slug, items, section))

    content = re.sub(r"\[display-posts[^\]]*\]", display_posts, content)
    content = re.sub(r"<!-- wp:advgb/recent-posts (\{.*?\}) /-->", advgb, content)
    return content, found


def frontmatter(fields):
    lines = ["---"]
    for k, v in fields.items():
        if v is None:
            continue
        if isinstance(v, list):
            lines.append(f"{k}: [{', '.join(json.dumps(x) for x in v)}]")
        elif isinstance(v, bool):
            lines.append(f"{k}: {str(v).lower()}")
        else:
            lines.append(f"{k}: {json.dumps(v)}")
    lines.append("---")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("export_dir", type=Path)
    ap.add_argument("content_dir", type=Path)
    args = ap.parse_args()
    content_dir = args.content_dir

    www_paths = set()
    pages = []
    for blog_id, host, xml in BLOGS:
        items, tags, cats, cats_by_slug = load_blog(args.export_dir / xml)
        for it in items.values():
            if text(it, "wp:post_type") != "page" or text(it, "wp:status") != "publish":
                continue
            slug = text(it, "wp:post_name")
            if slug in SKIP_SLUGS:
                continue
            path = url_path(it.find("link").text)
            if blog_id == 7:
                www_paths.add(path)
            pages.append((blog_id, host, it, slug, path, items, tags, cats, cats_by_slug))

    # Old flat page files from wp2hugo.py are replaced by this run.
    removed = [p for p in content_dir.glob("*.md") if p.name != "_index.md"]
    for p in removed:
        p.unlink()

    written = []
    for blog_id, host, it, slug, path, items, tags, cats, cats_by_slug in pages:
        section = "dataset" if blog_id == 6 else "post"
        fields = {
            "title": html.unescape(it.find("title").text or ""),
            "date": wp2hugo.dateparser.parse(text(it, "wp:post_date")).strftime("%Y-%m-%dT%H:%M:%S+00:00"),
            "draft": False,
            "author": text(it, "dc:creator") or None,
        }
        if blog_id == 7 and path == "/":
            out = content_dir / "_index.md"
        elif blog_id == 7 and slug == "blog":
            out = content_dir / "blog" / "_index.md"
        elif blog_id == 6 and path == "/":
            out = content_dir / "dataset" / "_index.md"
            fields["title"] = "Data Repository"
            fields["aliases"] = ["/posts/"]
        else:
            if blog_id == 6 and path in www_paths:
                path = "/dataset" + path
            fields["url"] = path
            name = slug if blog_id == 7 else f"data-{slug}"
            out = content_dir / f"{name}.md"

        raw = it.find("content:encoded", NS).text or ""
        raw, lists = replace_lists(raw, tags, cats, cats_by_slug, items, section)
        body = wp2hugo.convert_html_to_markdown(raw, blog_id)
        for i, sc in enumerate(lists):
            body = body.replace(f"POSTLIST{i}TOKEN", sc)
        if out.name == "_index.md" and out.parent == content_dir / "blog":
            body = ""

        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(frontmatter(fields) + "\n\n" + body + "\n")
        written.append((host + path, out.relative_to(content_dir)))

    print(f"removed {len(removed)} old page files, wrote {len(written)} pages")
    for url, out in sorted(written):
        print(f"  {url:75} {out}")


if __name__ == "__main__":
    main()
