# Project Guidelines

## What This Is

The personal portfolio site of Magnús Pétursson (magnusp.is), built with [Zensical](https://zensical.org/), a static site generator from the creators of Material for MkDocs. It is bilingual: English at `/` and Icelandic at `/is/`.

## Build & Dev

```bash
source .venv/bin/activate
pip install -r requirements.txt               # Zensical version is pinned

zensical serve                                # English preview, http://localhost:8000
zensical build --clean --strict               # English  → site/
zensical build --strict -f zensical.is.toml   # Icelandic → site/is/ (must run after English)
```

`site/` is gitignored. `.github/workflows/docs.yml` builds both languages and deploys to GitHub Pages on push to `main`. Builds run with `--strict`, so fix every warning.

## Architecture

```
docs/                  # English pages + shared assets
  *.md                 # One page per nav item
  stylesheets/         # Shared CSS (also used by the Icelandic build)
  images/              # Shared images
  CNAME                # Custom domain for GitHub Pages
docs-is/               # Icelandic pages, same file names as docs/
zensical.toml          # English config (nav, theme, features)
zensical.is.toml       # Icelandic config; mirror shared settings from zensical.toml
requirements.txt       # Pinned Zensical version
```

- Zensical's TOML config has no inheritance, so theme, features, palette and font settings are duplicated across both config files. Change them in both.
- The language switcher is `[[project.extra.alternate]]`, which appears in both configs.
- The Icelandic build references CSS and images by absolute path (`/stylesheets/...`, `/images/...`) so they aren't duplicated. In `docs-is/` pages, reference images as `/images/<file>`.
- Every English page in `docs/` has an Icelandic counterpart in `docs-is/` with the same file name. Add or rename both together, and update both `nav` lists.

## Content Conventions

Every page starts with YAML frontmatter for its sidebar icon:

```yaml
---
icon: lucide/rocket
---
```

Buttons use Material attribute syntax:
```markdown
[Label](page.md){ .md-button .md-button--primary }
```

Never invent biographical facts. Unfinished content is marked with `<!-- TODO -->` comments.

## Styling

The visual design is being redesigned; the previous FabLab Ísland brand is being retired. Custom styles live in `docs/stylesheets/extra.css`. Don't add inline styles to Markdown.
