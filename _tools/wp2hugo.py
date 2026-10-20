#!/usr/bin/env python3
"""WordPress WXR XML → Hugo Markdown converter.

Usage:
  python3 wp2hugo.py <wxr-file.xml> <output-content-dir> --blog-id <id> --permalink <pattern> [--media-dir <dir>]

Examples:
  python3 wp2hugo.py blog9/ericbusboom.wordpress.2026-07-09.001.xml content --blog-id 9 --permalink '/%year%/%monthnum%/%day%/%postname%/' --media-dir static/uploads/9
"""

import argparse
import os
import re
import sys
import html
from datetime import datetime
from pathlib import Path

import xml.etree.ElementTree as ET
import html2text
from dateutil import parser as dateparser

# WXR namespace
NS = {
    'wp': 'http://wordpress.org/export/1.2/',
    'content': 'http://purl.org/rss/1.0/modules/content/',
    'dc': 'http://purl.org/dc/elements/1.1/',
    'excerpt': 'http://wordpress.org/export/1.2/excerpt/',
    'wfw': 'http://wellformedweb.org/CommentAPI/',
}

# Post types to skip entirely
SKIP_TYPES = {'revision', 'nav_menu_item', 'customize_changeset', 'oembed_cache',
              'wp_template', 'wp_template_part', 'wp_global_styles', 'wp_navigation',
              'et_pb_layout', 'custom_css', 'safecss', 'wp_block', 'wpforms',
              'fpf_fields', 'post_grid', 'rttpg', 'wplp-news-widget',
              'product', 'product_variation'}

# Custom post type mappings to Hugo content directories
CUSTOM_TYPE_MAP = {
    'dwqa-question': 'question',
    'dwqa-answer': 'answer',
}

# Default WordPress pages to skip (WooCommerce etc)
SKIP_PAGES = {'cart', 'checkout', 'my-account', 'shop', 'portfolio'}


def parse_wxr(xml_path):
    """Parse WXR XML, return list of post dicts."""
    tree = ET.parse(xml_path)
    root = tree.getroot()
    channel = root.find('channel')
    items = []
    for item in channel.findall('item'):
        post = {}
        # Title
        title_el = item.find('title')
        post['title'] = html.unescape(title_el.text or '') if title_el is not None else ''
        
        # Link (original URL)
        link_el = item.find('link')
        post['link'] = link_el.text or '' if link_el is not None else ''
        
        # Post type
        post_type_el = item.find('wp:post_type', NS)
        post['post_type'] = post_type_el.text or 'post' if post_type_el is not None else 'post'
        
        # Post status
        status_el = item.find('wp:status', NS)
        post['post_status'] = status_el.text or 'publish' if status_el is not None else 'publish'
        
        # Post name (slug)
        post_name_el = item.find('wp:post_name', NS)
        post['post_name'] = post_name_el.text or '' if post_name_el is not None else ''
        
        # Post date
        date_el = item.find('wp:post_date', NS)
        date_str = date_el.text if date_el is not None else ''
        try:
            post['post_date'] = dateparser.parse(date_str)
        except Exception:
            post['post_date'] = datetime.now()
        
        # Content
        content_el = item.find('content:encoded', NS)
        post['content'] = content_el.text or '' if content_el is not None else ''
        
        # Excerpt
        excerpt_el = item.find('excerpt:encoded', NS)
        post['excerpt'] = excerpt_el.text or '' if excerpt_el is not None else ''
        
        # Categories and tags
        post['categories'] = []
        post['tags'] = []
        for cat in item.findall('category'):
            domain = cat.get('domain', '')
            name = html.unescape(cat.text or '')
            if domain == 'category':
                post['categories'].append(name)
            elif domain == 'post_tag':
                post['tags'].append(name)
        
        # Author
        creator_el = item.find('dc:creator', NS)
        post['author'] = creator_el.text or '' if creator_el is not None else ''
        
        # Parent
        parent_el = item.find('wp:post_parent', NS)
        post['post_parent'] = int(parent_el.text or 0) if parent_el is not None else 0
        
        # Post ID
        post_id_el = item.find('wp:post_id', NS)
        post['post_id'] = int(post_id_el.text or 0) if post_id_el is not None else 0
        
        # Post meta (for featured image etc)
        post['meta'] = {}
        for pm in item.findall('wp:postmeta', NS):
            key_el = pm.find('wp:meta_key', NS)
            val_el = pm.find('wp:meta_value', NS)
            if key_el is not None and val_el is not None:
                post['meta'][key_el.text] = val_el.text or ''
        
        items.append(post)
    return items


def strip_shortcodes(content):
    """Handle WordPress shortcodes — strip them, keep inner content where possible."""
    # [caption ...]<img ...>[/caption] → just the img
    content = re.sub(r'\[caption[^\]]*\](.*?)\[/caption\]', r'\1', content, flags=re.DOTALL)
    
    # [gallery ...] → note
    content = re.sub(r'\[gallery[^\]]*\]', 
                     '> **Note:** This was a WordPress photo gallery.', content)
    
    # [display-posts ...] → note
    content = re.sub(r'\[display-posts[^\]]*\]',
                     '> **Note:** This was a dynamic WordPress post list.', content)
    
    # [contact-form-7 ...] → note
    content = re.sub(r'\[contact-form-7[^\]]*\]',
                     '> **Note:** This was a contact form.', content, flags=re.DOTALL)
    content = re.sub(r'\[/contact-form-7\]', '', content)
    
    # [et_pb_*] ... [/et_pb_*] — Divi builder shortcodes — strip, keep inner content
    content = re.sub(r'\[et_pb_[a-z_]+[^\]]*\]', '', content)
    content = re.sub(r'\[/et_pb_[a-z_]+\]', '', content)
    
    # [woocommerce_*] shortcodes
    content = re.sub(r'\[woocommerce[^\]]*\]', '', content)
    
    # Generic shortcode stripping: [shortcode ...] without closing tag → remove
    # But be careful not to strip [text] that looks like a shortcode but is content
    # Only strip known patterns
    
    return content


def rewrite_media_urls(content, blog_id):
    """Rewrite WordPress media URLs to local /uploads/{blog_id}/ paths."""
    # Pattern: https://domain/wp-content/uploads/sites/{id}/... → /uploads/{id}/...
    # Also http://, and domain-relative /wp-content/uploads/...
    
    # Match full URLs with sites/{id}/
    pattern = re.compile(
        r'https?://[^/]+/wp-content/uploads/sites/' + str(blog_id) + r'/([^\s"\'\)]+)',
        re.IGNORECASE
    )
    content = pattern.sub(r'/uploads/' + str(blog_id) + r'/\1', content)
    
    # Match domain-relative paths /wp-content/uploads/sites/{id}/
    pattern2 = re.compile(
        r'/wp-content/uploads/sites/' + str(blog_id) + r'/([^\s"\'\)]+)',
    )
    content = pattern2.sub(r'/uploads/' + str(blog_id) + r'/\1', content)
    
    # For blog 1 (root), uploads are at /wp-content/uploads/ (no /sites/)
    if blog_id == 1:
        pattern3 = re.compile(
            r'https?://[^/]+/wp-content/uploads/([^\s"\'\)]+)',
            re.IGNORECASE
        )
        content = pattern3.sub(r'/uploads/\1', content)
    
    return content


def convert_html_to_markdown(html_content, blog_id):
    """Convert WordPress HTML to Markdown, rewriting media URLs."""
    # First strip shortcodes
    content = strip_shortcodes(html_content)
    
    # Rewrite media URLs before conversion
    content = rewrite_media_urls(content, blog_id)
    
    # Configure html2text
    h = html2text.HTML2Text()
    h.body_width = 0  # No line wrapping
    h.unicode_snob = True
    h.protect_links = True
    h.wrap_links = False
    h.mark_code = True  # Preserve <code> blocks
    
    markdown = h.handle(content)
    
    # Clean up excessive blank lines
    markdown = re.sub(r'\n{4,}', '\n\n\n', markdown)
    
    return markdown.strip()


def determine_file_path(post, permalink_pattern, blog_id):
    """Determine Hugo content file path from WP permalink structure."""
    slug = post['post_name'] or slugify(post['title'])
    post_type = post['post_type']
    dt = post['post_date']
    
    # Skip unwanted post types
    if post_type in SKIP_TYPES:
        return None
    
    # Skip WooCommerce default pages
    if post_type == 'page' and slug in SKIP_PAGES:
        return None
    
    # Custom post types
    if post_type in CUSTOM_TYPE_MAP:
        section = CUSTOM_TYPE_MAP[post_type]
        return f"content/{section}/{slug}.md"
    
    if post_type == 'page':
        # Pages go at root of content/
        return f"content/{slug}.md"
    
    if post_type == 'post':
        # Generate path based on permalink pattern
        # Hugo URLs are derived from file path, so file path must match WP permalink
        pattern = permalink_pattern or '/%year%/%monthnum%/%day%/%postname%/'
        
        if '/%day%/' in pattern:
            # /%year%/%monthnum%/%day%/%postname%/ → {year}/{month}/{day}/{slug}.md
            return f"{dt.year}/{dt.month:02d}/{dt.day:02d}/{slug}.md"
        elif '/%monthnum%/' in pattern:
            # /%year%/%monthnum%/%postname%/ → {year}/{month}/{slug}.md
            return f"{dt.year}/{dt.month:02d}/{slug}.md"
        elif '/dataset/' in pattern and '/%postname%/' in pattern:
            # /dataset/%postname%/ → dataset/{slug}.md
            return f'dataset/{slug}.md'
        elif '/%postname%/' in pattern or pattern == '/%postname%/':
            # /%postname%/ → {slug}.md (at root, will be /{slug}/)
            return f"{slug}.md"
        else:
            return f"post/{slug}.md"
    
    # Dataset post type (blog 6 uses /dataset/%postname%/)
    if post_type == 'dataset':
        return f"dataset/{slug}.md"
    
    # Unknown type — put in {type}/
    return f"{post_type}/{slug}.md"


def generate_frontmatter(post):
    """Generate YAML frontmatter."""
    lines = ['---']
    lines.append(f'title: "{escape_yaml(post["title"])}"')
    lines.append(f'date: {post["post_date"].strftime("%Y-%m-%dT%H:%M:%S+00:00")}')
    
    if post['post_status'] != 'publish':
        lines.append(f'draft: true')
    else:
        lines.append(f'draft: false')
    
    if post['post_type'] != 'post' and post['post_type'] != 'page':
        lines.append(f'type: "{post["post_type"]}"')
    
    if post['categories']:
        cats = ', '.join(f'"{escape_yaml(c)}"' for c in post['categories'])
        lines.append(f'categories: [{cats}]')
    
    if post['tags']:
        tags = ', '.join(f'"{escape_yaml(t)}"' for t in post['tags'])
        lines.append(f'tags: [{tags}]')
    
    if post['author']:
        lines.append(f'author: "{escape_yaml(post["author"])}"')
    
    if post['excerpt']:
        lines.append(f'description: "{escape_yaml(post["excerpt"][:200])}"')
    
    lines.append('---')
    return '\n'.join(lines)


def escape_yaml(s):
    """Escape a string for YAML."""
    s = s.replace('"', '\\"')
    s = s.replace('\n', ' ')
    s = s.strip()
    return s


def slugify(s):
    """Generate a slug from a title."""
    s = s.lower().strip()
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'[\s_-]+', '-', s)
    s = s.strip('-')
    return s or 'untitled'


def generate_redirects(redirects_csv, output_path):
    """Generate a GitHub Pages _redirects file from Redirection plugin CSV."""
    if not os.path.exists(redirects_csv):
        return
    
    lines = []
    with open(redirects_csv, 'r') as f:
        next(f)  # skip header
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) >= 3:
                url, target, action_type = parts[0], parts[1], parts[2]
                if action_type == 'url':
                    # Internal redirect
                    if target.startswith('http'):
                        # External redirect — 301
                        lines.append(f"{url} {target} 301")
                    else:
                        # Internal path redirect — 301
                        lines.append(f"{url} {target} 301")
    
    with open(output_path, 'w') as f:
        f.write('\n'.join(lines) + '\n')
    print(f"  Redirects: {len(lines)} entries → {output_path}")


def main():
    parser = argparse.ArgumentParser(description='Convert WordPress WXR to Hugo Markdown')
    parser.add_argument('wxr_file', help='Path to WXR XML file')
    parser.add_argument('output_dir', help='Output directory for Hugo content')
    parser.add_argument('--blog-id', type=int, required=True, help='WordPress blog ID')
    parser.add_argument('--permalink', default='/%year%/%monthnum%/%day%/%postname%/',
                        help='WordPress permalink pattern')
    parser.add_argument('--media-dir', default=None,
                        help='Directory to copy media files to (optional)')
    parser.add_argument('--redirects-csv', default=None,
                        help='Path to Redirection plugin CSV for redirects')
    parser.add_argument('--skip-pages', action='store_true',
                        help='Skip WooCommerce default pages (cart, checkout, etc)')
    
    args = parser.parse_args()
    
    print(f"Parsing WXR: {args.wxr_file}")
    posts = parse_wxr(args.wxr_file)
    print(f"  Found {len(posts)} items")
    
    # Group by post type for reporting
    by_type = {}
    for p in posts:
        by_type.setdefault(p['post_type'], 0)
        by_type[p['post_type']] += 1
    for pt, cnt in sorted(by_type.items()):
        print(f"    {pt}: {cnt}")
    
    os.makedirs(args.output_dir, exist_ok=True)
    
    converted = 0
    skipped = 0
    
    for post in posts:
        if post['post_status'] not in ('publish',):
            skipped += 1
            continue
        
        file_path = determine_file_path(post, args.permalink, args.blog_id)
        if file_path is None:
            skipped += 1
            continue
        
        # Strip leading "content/" — the output_dir IS the content dir
        file_path = file_path.replace('content/', '', 1)
        
        full_path = os.path.join(args.output_dir, file_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        
        # Convert content
        markdown_content = convert_html_to_markdown(post['content'], args.blog_id)
        
        # Generate frontmatter
        frontmatter = generate_frontmatter(post)
        
        # Write file
        with open(full_path, 'w') as f:
            f.write(frontmatter)
            f.write('\n\n')
            f.write(markdown_content)
            f.write('\n')
        
        converted += 1
    
    print(f"  Converted: {converted}")
    print(f"  Skipped: {skipped}")
    
    # Generate redirects if provided
    if args.redirects_csv:
        redirects_path = os.path.join(args.output_dir, '..', 'static', '_redirects')
        os.makedirs(os.path.dirname(redirects_path), exist_ok=True)
        generate_redirects(args.redirects_csv, redirects_path)


if __name__ == '__main__':
    main()
