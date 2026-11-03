#!/usr/bin/env python3
"""Build blog pages from markdown.

Usage (from the repo root):
    pip install markdown pyyaml
    python3 tools/build.py

Reads   content/posts/*.md   (front matter: title, date, permalink, tags)
Writes  posts/<slug>/index.html  for each post, and  posts/index.html  (the list).
The generated HTML is committed; GitHub Pages serves it as plain files.
"""
import html
import re
from pathlib import Path

import markdown
import yaml

ROOT = Path(__file__).resolve().parent.parent
POSTS_SRC = ROOT / "content" / "posts"
TEMPLATE = (ROOT / "tools" / "post_template.html").read_text(encoding="utf-8")

# $$...$$ first, then inline $...$ (not \$).
MATH_RE = re.compile(r"\$\$.+?\$\$|(?<![\\$])\$(?!\$).+?(?<!\\)\$", re.S)


def split_front_matter(text):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", text, re.S)
    if not m:
        raise ValueError("missing front matter")
    return yaml.safe_load(m.group(1)), m.group(2)


def render_markdown(body):
    """Convert markdown to HTML while leaving math untouched for KaTeX."""
    stash = []

    def keep(m):
        stash.append(m.group(0))
        return f"MATHTOKEN{len(stash) - 1}END"

    protected = MATH_RE.sub(keep, body)
    out = markdown.markdown(protected, extensions=["extra", "sane_lists"])
    return re.sub(r"MATHTOKEN(\d+)END", lambda m: html.escape(stash[int(m.group(1))], quote=False), out)


def page(title, body_html, description=""):
    return (TEMPLATE.replace("{{title}}", html.escape(title))
                    .replace("{{description}}", html.escape(description))
                    .replace("{{content}}", body_html))


def main():
    posts = []
    for src in sorted(POSTS_SRC.glob("*.md")):
        meta, body = split_front_matter(src.read_text(encoding="utf-8"))
        slug = meta["permalink"].strip("/").split("/")[-1]
        date = meta["date"]
        content = render_markdown(body)
        article = (f'<article class="post">\n<h1>{html.escape(meta["title"])}</h1>\n'
                   f'<p class="post-date"><time datetime="{date}">{date:%B %-d, %Y}</time></p>\n'
                   f"{content}\n</article>")
        out = ROOT / "posts" / slug / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page(meta["title"], article), encoding="utf-8")
        posts.append((date, meta["title"], f"/posts/{slug}/"))
        print(f"built {out.relative_to(ROOT)}")

    items = "\n".join(
        f'<li><time datetime="{d}">{d:%b %Y}</time> <a href="{url}">{html.escape(t)}</a></li>'
        for d, t, url in sorted(posts, reverse=True))
    index = ROOT / "posts" / "index.html"
    index.write_text(page("Blog", f'<h1>Blog</h1>\n<ul class="post-list">\n{items}\n</ul>'), encoding="utf-8")
    print(f"built {index.relative_to(ROOT)}  ({len(posts)} posts)")


if __name__ == "__main__":
    main()
