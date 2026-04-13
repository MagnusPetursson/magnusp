# Project Guidelines

## What This Is

A personal portfolio site built with [Zensical](https://zensical.org/) (a Material-for-MkDocs-based static site generator). Content lives in `docs/` as Markdown; `zensical build` compiles it to `site/`. Configuration is in `zensical.toml`.

## Build & Dev

```bash
# Activate the local venv first
source .venv/bin/activate

# Live preview with hot reload (http://localhost:8000)
zensical serve

# Production build (output → site/)
zensical build --clean
```

`site/` is gitignored — it's auto-deployed to GitHub Pages via `.github/workflows/docs.yml` on push to `main`/`master`.

## Architecture

```
docs/           # All content (edit here)
  *.md          # Pages — one per nav item
  stylesheets/extra.css  # Brand styles (FabLab Ísland color system)
  images/       # Static assets
site/           # Generated output (do not edit)
zensical.toml   # Site config, nav, theme, features
```

Navigation order is defined explicitly in `zensical.toml` under `nav`.

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

Collapsible FAQ blocks:
```markdown
??? question "Question text"
    Answer content
```

Use `---` horizontal rules to separate content sections (renders as a brand-color gradient).

## Styling

Custom styles are in `docs/stylesheets/extra.css`. Brand color variables are defined on `:root`:
- `--brand-red: #E03A3F` — primary accent, links hover, list bullets, H1 underline
- `--brand-green: #009967` — code block borders, blockquote accents
- `--brand-blue: #1245DE` — links, scrollbar, button backgrounds
- Additional: pink `#E94C8D`, orange `#F2822E`, yellow `#F2BE32`

Light/dark schemes each have their own variable overrides. Edit `extra.css` for any visual changes — do not add inline styles to Markdown.
