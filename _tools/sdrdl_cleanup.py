#!/usr/bin/env python3
"""Clean WordPress leftovers out of www.sandiegodata.org content.

  - the "Resources | Packages | Documentation| ..." tab bar on dataset
    pages (its links were JavaScript tabs and did nothing once converted)
  - html2text [code] ... [/code] blocks -> fenced code blocks
  - [button link="..."]Text[/button] -> a Markdown link
  - [box ...] [/box], [icon ...], [rp_register_widget ...] -> removed

    python3 _tools/sdrdl_cleanup.py www.sandiegodata.org/content
"""
import argparse
import re
from collections import Counter
from pathlib import Path

TAB_BAR = re.compile(r"^Resources ?\| ?Packages ?\|.*\n", re.M)
CODE = re.compile(r"\[code\] *\n?(.*?)\n?[ \t]*\[/code\]", re.S)
BUTTON = re.compile(r'\[button link="([^"]+)"[^\]]*\]\s*(.*?)\s*\[/button\]', re.S)
STRIP = re.compile(r"\[/?box[^\]]*\]|\[icon [^\]]*\]|\[rp_register_widget[^\]]*\]")


def fence(m):
    lines = m.group(1).split("\n")
    lines = [l[4:] if l.startswith("    ") else l for l in lines]
    return "```\n" + "\n".join(lines).rstrip() + "\n```"


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("content_dir", type=Path)
    args = ap.parse_args()

    stats = Counter()
    for md in sorted(args.content_dir.rglob("*.md")):
        old = md.read_text()
        new = old
        for name, pattern, repl in (
            ("tab bars", TAB_BAR, ""),
            ("code blocks", CODE, fence),
            ("buttons", BUTTON, r"[\2](<\1>)"),
            ("other shortcodes", STRIP, ""),
        ):
            new, n = pattern.subn(repl, new)
            stats[name] += n
        if new != old:
            md.write_text(new)
    print(", ".join(f"{k}: {v}" for k, v in stats.items()))


if __name__ == "__main__":
    main()
