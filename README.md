# WWII Insider Shop

The website for WWII Insider's printable, large-print history dossiers.
Live at **https://shop.yesmidealab.com** (GitHub Pages).

## What's here

| Path | What it is |
| --- | --- |
| `index.html` | Shop page for Mission Dossier No. 1: Operation Pastorius |
| `policies.html` | Refunds and privacy |
| `404.html` | "Page not found" page |
| `assets/site.css` | All styles (large type, high contrast, big buttons) |
| `assets/fonts/` | Source Serif 4, IBM Plex Sans, Courier Prime (SIL Open Font License, licence files included) |
| `assets/img/` | Page previews, cover and social-share image (`og.jpg`) |
| `free/pastorius-free-sample.pdf` | Free 3-page sample offered on the site |
| `CNAME` | Custom domain: `shop.yesmidealab.com` |
| `.nojekyll` | Tells GitHub Pages to serve files as they are |

## What's deliberately NOT here

The full paid PDFs and the scripts that build them live in `private/` on your
computer, which `.gitignore` keeps out of this public repo. Buyers get the PDFs
from Gumroad after paying. Never commit them here.

## Publishing

1. Repo **Settings > Pages**: Source **Deploy from a branch**, branch **main**, folder **/ (root)**.
2. DNS for yesmidealab.com: `CNAME` record, name `shop`, value `yesmidealabcontact-wq.github.io`.
3. **Settings > Pages > Custom domain** `shop.yesmidealab.com`, then tick **Enforce HTTPS**.

Any change pushed to `main` goes live within a few minutes.

## Before launch

- Buy buttons point to `https://yesmidealab.gumroad.com/l/pastorius`. Create that Gumroad product, or change both links in `index.html`.
- The YouTube button points to channel `UCKcqq-MwhD2JaGe_MjMvO0A`. Confirm it is yours.

## Licence

Website code: MIT (see `LICENSE`). Dossier text, maps and images: © 2026 WWII Insider, all rights reserved.
