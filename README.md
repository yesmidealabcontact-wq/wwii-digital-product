# Lives At WW2 Shop

Website and products for Lives At WW2's printable, large-print history dossiers.
Website: **https://shop.yesmidealab.com**, hosted on AWS (S3 + CloudFront).

> **Keep this repo private.** `private/` holds the paid PDFs.

## Layout

| Path | What it is | Public? |
| --- | --- | --- |
| `site/` | The website. The only folder ever uploaded to AWS | Yes, once deployed |
| `site/index.html` | Shop page for Mission Dossier No. 1: Operation Pastorius | Yes |
| `site/policies.html`, `site/404.html` | Refunds and privacy; "page not found" | Yes |
| `site/assets/` | Styles, fonts (SIL Open Font License, licence files included), preview images | Yes |
| `site/free/pastorius-free-sample.pdf` | Free 3-page sample | Yes |
| `private/products/` | Paid PDFs (US Letter + A4). Upload these to Gumroad | **No** |
| `private/build/` | Python scripts that build the dossier PDF and maps | **No** |
| `.github/workflows/deploy.yml` | Uploads `site/` to S3 and refreshes CloudFront on each push to `main` | n/a |

## Hosting on AWS (one-time setup)

1. **Certificate:** in AWS Certificate Manager, region **us-east-1** (CloudFront requires it), request a public certificate for `shop.yesmidealab.com`. Validate it by adding the CNAME record it shows to your DNS.
2. **Bucket:** create an S3 bucket (e.g. `shop.yesmidealab.com`). Keep **Block all public access ON**: CloudFront reads it privately.
3. **CloudFront distribution:**
   - Origin: the bucket, with **Origin access control (OAC)**; let CloudFront update the bucket policy.
   - Viewer protocol policy: **Redirect HTTP to HTTPS**. Default root object: `index.html`.
   - Alternate domain name: `shop.yesmidealab.com`, with the certificate from step 1.
   - Custom error responses: 403 and 404 → `/404.html`, response code 404.
4. **DNS:** add a record for `shop` pointing to the distribution's `dxxxx.cloudfront.net` domain (CNAME, or an alias A/AAAA record if the domain is in Route 53).
5. **Let GitHub deploy:**
   - IAM > Identity providers: add OpenID Connect provider `https://token.actions.githubusercontent.com`, audience `sts.amazonaws.com`.
   - Create a role trusted by that provider, limited to `repo:yesmidealabcontact-wq/wwii-digital-product:ref:refs/heads/main`, with permission to `s3:ListBucket` on the bucket, `s3:PutObject`/`s3:DeleteObject` on `bucket/*`, and `cloudfront:CreateInvalidation` on the distribution.
   - In GitHub, **Settings > Secrets and variables > Actions**: secret `AWS_ROLE_ARN`; variables `AWS_REGION`, `S3_BUCKET`, `CLOUDFRONT_DISTRIBUTION_ID`.
6. Push a change under `site/` (or run the workflow from the **Actions** tab). The site updates within a few minutes.

## Before launch

- Buy buttons point to `https://yesmidealab.gumroad.com/l/pastorius`. Create that Gumroad product, or change both links in `site/index.html`.
- The YouTube button points to https://www.youtube.com/@LivesatWW2.

## Rebuilding the dossier PDF

`private/build/dossier_pastorius.py` needs Python with Playwright, plus two downloads not stored here:
Natural Earth GeoJSON (`github.com/nvkelso/natural-earth-vector`, folder `geojson/`) and the
Google Fonts files for Source Serif 4, IBM Plex Sans and Courier Prime. Edit the `NE` and `G`
paths at the top of `geo.py` and `dossier_pastorius.py` to point to them.

## Licence

Website code: MIT (see `LICENSE`). Dossier text, maps and images: © 2026 Lives At WW2, all rights reserved.
