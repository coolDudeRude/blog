#!/usr/bin/env python3
"""Create a new Jekyll post and its per-post asset folder."""

import argparse
import re
import sys
from datetime import date
from pathlib import Path

# script lives in `_scripts/` so root is one dir above.
ROOT = Path(__file__).resolve().parent.parent

TEMPLATE = """---
layout: post
title: '{title}'
tags: [{tags}]
---

Write the intro here. This first paragraph becomes the homepage excerpt.

{{% assign dir = '/assets/posts/' | append: page.slug %}}

"""


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("name", help="post name without the date")
    p.add_argument("-t", "--tags", nargs="*", default=[], help="tags (lowercase)")
    p.add_argument(
        "-d",
        "--date",
        default=date.today().isoformat(),
        help="YYYY-MM-DD (default: today)",
    )
    args = p.parse_args()

    slug = slugify(args.name)
    if not slug:
        print("error: name has no usable characters", file=sys.stderr)
        return 1
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", args.date):
        print("error: date must be YYYY-MM-DD", file=sys.stderr)
        return 1

    post = ROOT / "_posts" / f"{args.date}-{slug}.md"
    assets = ROOT / "assets" / "posts" / slug

    if post.exists():
        print(f"error: {post.relative_to(ROOT)} already exists", file=sys.stderr)
        return 1

    title = slug.replace("-", " ").capitalize().replace("'", "''")
    tags = ", ".join(slugify(t.lower()) for t in args.tags)

    post.parent.mkdir(exist_ok=True)
    post.write_text(TEMPLATE.format(title=title, tags=tags), encoding="utf-8")

    assets.mkdir(parents=True, exist_ok=True)

    (assets / ".gitkeep").touch()

    print(f"created {post.relative_to(ROOT)}")
    print(f"created {assets.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
