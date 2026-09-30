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

`preview.py` builds both languages into `site/`, serves the result, rebuilds when anything in `docs/`, `docs-is/`, `overrides/` or the configs changes, and reloads open pages automatically.

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
| `overrides/` | Theme overrides shared by both builds: homepage, header, logo, 404 |
| `preview.py` | Local preview server for both languages |
| `zensical.toml` | English config |
| `zensical.is.toml` | Icelandic config; keep theme, features and palette in sync with `zensical.toml` |
| `requirements.txt` | Pinned Zensical version, also used by CI |

The Icelandic build loads its CSS and images by absolute URL (`/stylesheets/...`, `/images/...`) from the English build, so no files are duplicated. As a result, `zensical serve -f zensical.is.toml` on its own renders without custom styles. Use `python preview.py` for a full preview.

## Adding a project

1. Put images in `docs/images/<project>/` as WebP, at most ~1600 px wide. For example:
   `python3 -c "from PIL import Image; im=Image.open('in.jpg'); im.thumbnail((1600,1600)); im.save('out.webp', quality=82)"`
2. Copy an existing page such as `docs/projects/glasslight.md` to `docs/projects/<project>.md` and rewrite it: an H1, one lead paragraph, the `mp-facts` list, then sections.
3. Add the page to the `Projects` list in `nav` in both `zensical.toml` and `zensical.is.toml`.
4. Add a matching `docs-is/projects/<project>.md`. In Icelandic pages, write image paths as `/images/...`.
5. Optionally add it to `docs/projects/index.md` and the homepage (`docs/index.md`), plus their Icelandic twins.

## Email and contact form

The email address never appears in the HTML. `<span class="mp-email" data-e="...">` holds it base64-encoded and reversed, and `docs/javascripts/site.js` turns it into a link in the browser. To encode a new address:
`python3 -c "import base64; print(base64.b64encode(b'you@example.com').decode()[::-1])"`

The contact form (`overrides/contact.html`) posts to the service configured under `[project.extra.contact_form]` in both configs. Until `action` is set, the page shows a placeholder instead of the form.

## Analytics

GoatCounter is enabled by setting `goatcounter = "<site code>"` under `[project.extra]` in both configs. The script loads only when the code is set. `docs/javascripts/site.js` counts pages opened through instant navigation, which GoatCounter can't see on its own.

## Deploy

On every push to `main`, `.github/workflows/docs.yml` builds both languages and publishes `site/` to GitHub Pages. The custom domain is set by `docs/CNAME`. DNS for `magnusp.is` must point at GitHub Pages: A records `185.199.108.153`, `185.199.109.153`, `185.199.110.153` and `185.199.111.153`.
