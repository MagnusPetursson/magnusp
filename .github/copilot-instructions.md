# Project Guidelines

## What This Is

The personal portfolio site of Magnús Pétursson (magnusp.is), built with [Zensical](https://zensical.org/), a static site generator from the creators of Material for MkDocs. It is bilingual: English at `/` and Icelandic at `/is/`.

## Build & Dev

```bash
source .venv/bin/activate
pip install -r requirements.txt               # Zensical version is pinned

python preview.py                             # both languages, http://localhost:8000, live reload
zensical build --clean --strict               # English  → site/
zensical build --strict -f zensical.is.toml   # Icelandic → site/is/ (must run after English)
```

`site/` is gitignored. `.github/workflows/docs.yml` builds both languages and deploys to GitHub Pages on push to `main`. Builds run with `--strict`, so fix every warning.

## Architecture

```
docs/                  # English pages + shared assets
  index.md             # Homepage (template: home.html; layout built with md_in_html divs)
  projects/            # Projects section: index.md overview + one page per project
  about.md, contact.md
  stylesheets/extra.css  # The whole visual design (shared with the Icelandic build)
  images/              # Shared images (WebP, max ~1600 px wide); og.jpg = link preview
  fonts/               # Self-hosted WOFF2 fonts (Latin subset) + OFL licences
  javascripts/site.js  # Email reveal + contact form; re-runs on instant navigation via document$
  CNAME                # Custom domain for GitHub Pages
docs-is/               # Icelandic pages, same file names as docs/
overrides/             # Theme overrides (custom_dir), used by both builds
  main.html            # Drops the tab bar, adds Open Graph tags
  home.html            # Full-width homepage without sidebars
  404.html             # Bilingual 404 (GitHub Pages only serves the root one)
  contact.html         # Contact page: Markdown + form posting to [project.extra.contact_form]
  partials/header.html # Header: brand, section links, language link, theme toggle
  partials/logo.html   # Pixel "M" logo (inline SVG; the red pixel is the compass needle)
preview.py             # Local preview server
zensical.toml          # English config (nav, theme, features)
zensical.is.toml       # Icelandic config; mirror shared settings from zensical.toml
requirements.txt       # Pinned Zensical version
```

- Zensical's TOML config has no inheritance, so theme, features, palette and font settings are duplicated across both config files. Change them in both.
- The language link in the header goes to the same page in the other language (`alt.link` + `page.url`), so page paths must match across `docs/` and `docs-is/`.
- The Icelandic build references CSS and images by absolute path (`/stylesheets/...`, `/images/...`) so they aren't duplicated. In `docs-is/` pages, reference images as `/images/<file>`.
- Every English page in `docs/` has an Icelandic counterpart in `docs-is/` with the same file name. Add or rename both together, and update both `nav` lists.

## Content Conventions

Every page starts with YAML frontmatter:

```yaml
---
title: Page title
description: One sentence, used for search engines and link previews.
hide:
  - toc            # all pages hide the table of contents
  - navigation     # pages outside the Projects section hide the sidebar
---
```

Quote a `description` that contains a colon. Project pages open with an H1, a lead paragraph, then a `<dl class="mp-facts">` of key facts. Renders on white backgrounds get `class="mp-render"` (dimmed in dark mode). In raw HTML, English pages use relative image paths; Icelandic pages use `/images/...`.

Buttons use Material attribute syntax:
```markdown
[Label](page.md){ .md-button .md-button--primary }
```

Privacy rules, from the site owner:
- Never write the email address in plain text or as a `mailto:` link in source or config; use the `mp-email` span (see README).
- Never name employers, and never mention the owner's home server, game servers or agent setup.
- Only circuit-board renders of McCompass may be shown; the McCompass source is private, so don't link it.
- Nothing loads from third-party servers except the contact form service and analytics.

Never invent biographical facts. Draft content is marked with `<!-- DRAFT: ... -->` comments naming the open question. Write in first person, sentence case, plain and specific. Use a non-breaking hyphen in "Wi‑Fi".

## Styling

Direction: precise, calm, handmade. All styles live in `docs/stylesheets/extra.css`, built on tokens defined per colour scheme:

- `--mp-paper` bench-grey background, `--mp-ink` text, `--mp-ink-soft` secondary text, `--mp-rule` lines, `--mp-plate` image and code backgrounds
- `--mp-mask` solder-mask green for links and primary buttons
- `--mp-needle` compass-needle red, used only in the logo

Type: Bricolage Grotesque (`--mp-display`) for headings and UI, Source Serif 4 for body text, JetBrains Mono for code only. Sentence case everywhere; no all-caps labels. Don't add inline styles to Markdown.
