# Lives At WW2 Shop

Website for Lives At WW2's printable, large-print history dossiers.
Website: **https://shop.yesmidealab.com**, hosted free on GitHub Pages.

> **The paid PDFs are NOT in this repo.** They live only on your own computer (in `private/`, which git ignores) and on Gumroad, where buyers download them.

## Layout

| Path | What it is | In this repo? |
| --- | --- | --- |
| `site/` | The website. The only folder GitHub Pages publishes | Yes (public) |
| `site/index.html` | Shop page for Mission Dossier No. 1: Operation Pastorius | Yes |
| `site/policies.html`, `site/404.html` | Refunds and privacy; "page not found" | Yes |
| `site/assets/` | Styles, fonts (SIL Open Font License, licence files included), preview images | Yes |
| `site/free/pastorius-free-sample.pdf` | Free 3-page sample (pages 1, 5 and 7) | Yes |
| `marketing/` | Gumroad thumbnail, Gumroad custom landing page, share-image source | Yes |
| `docs/gumroad-setup.md` | Step-by-step Gumroad product setup | Yes |
| `private/products/` | Paid PDFs (US Letter + A4). Upload these to Gumroad | **No: your computer only** |
| `private/build/` | Python scripts that build the dossier PDF and maps | **No: your computer only** |
| `.github/workflows/deploy.yml` | Publishes `site/` to GitHub Pages on each push to `main` | Yes |

## Hosting on GitHub Pages (one-time setup)

1. Repo **Settings > Pages > Build and deployment > Source**: choose **GitHub Actions**.
2. Push any change under `site/` (or run "Deploy site to GitHub Pages" from the **Actions** tab). It deploys in about a minute.
3. **Custom domain:** in your DNS for `yesmidealab.com`, add a **CNAME** record: name `shop`, value `yesmidealabcontact-wq.github.io`.
4. **Settings > Pages > Custom domain**: enter `shop.yesmidealab.com`, save, wait for the DNS check, then tick **Enforce HTTPS**.
5. Recommended: **Settings > Pages > Verify** the domain `yesmidealab.com` so nobody else can claim your subdomain on GitHub.

## Before launch

- Buy buttons point to `https://yesmidealab.gumroad.com/l/pastorius`. Create that Gumroad product (see `docs/gumroad-setup.md`), or change both links in `site/index.html`.
- The YouTube button points to https://www.youtube.com/@LivesatWW2.

## Rebuilding the dossier PDF

The build scripts live in `private/build/` on your computer. They need Python with Playwright, plus
Natural Earth GeoJSON (`github.com/nvkelso/natural-earth-vector`, folder `geojson/`) and the
Google Fonts files for Source Serif 4, IBM Plex Sans and Courier Prime. Edit the `NE` and `G`
paths at the top of `geo.py` and `dossier_pastorius.py` to point to them.

## Licence

Website code: MIT (see `LICENSE`). Dossier text, maps and images: © 2026 Lives At WW2, all rights reserved.
