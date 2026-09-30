# magnusp

Source for [magnusp.is](https://magnusp.is), the portfolio of Magnús Pétursson. Built with [Zensical](https://zensical.org/) and deployed to GitHub Pages.

The site is bilingual: English at `/` and Icelandic at `/is/`.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt   # Zensical is pinned here
```

## Local development

```bash
source .venv/bin/activate
python preview.py    # both languages at http://localhost:8000 (Icelandic at /is/)
```

`preview.py` builds both languages into `site/`, serves the result, rebuilds when anything in `docs/`, `docs-is/` or the configs changes, and reloads open pages automatically.

## Build

```bash
zensical build --clean --strict                # English  → site/
zensical build --strict -f zensical.is.toml    # Icelandic → site/is/
```

Always build English first: it's the build that emits `CNAME`, the shared stylesheets and the images.

## Layout

| Path | Purpose |
|------|---------|
| `docs/` | English pages, plus the shared `stylesheets/`, `images/` and `CNAME` |
| `docs-is/` | Icelandic pages (same file names as `docs/`) |
| `zensical.toml` | English config |
| `zensical.is.toml` | Icelandic config; keep theme, features and palette in sync with `zensical.toml` |
| `requirements.txt` | Pinned Zensical version, also used by CI |

The Icelandic build loads its CSS and images by absolute URL (`/stylesheets/...`, `/images/...`) from the English build, so no files are duplicated. As a result, `zensical serve -f zensical.is.toml` on its own renders without custom styles. Use `python preview.py` for a full preview.

## Deploy

On every push to `main`, `.github/workflows/docs.yml` builds both languages and publishes `site/` to GitHub Pages. The custom domain is set by `docs/CNAME`. DNS for `magnusp.is` must point at GitHub Pages: A records `185.199.108.153`, `185.199.109.153`, `185.199.110.153` and `185.199.111.153`.
