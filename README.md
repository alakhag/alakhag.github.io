# alakhag.github.io

Personal site of Alakh Aggarwal, built with [Hugo](https://gohugo.io) and the [Blowfish](https://blowfish.page) theme (pinned as a git submodule in `themes/blowfish`).

- Home page text: `content/_index.md`
- Blog posts: `content/posts/*.md` (add `{{< katex >}}` to a post that uses `$...$` math)
- Research pages: `content/research/`
- Site settings: `config/_default/`
- Preview locally: `hugo server`, then open http://localhost:1313
- Publishing: every push to `master` is built and deployed by `.github/workflows/hugo.yml`.
