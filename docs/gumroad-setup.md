# Gumroad setup kit: Operation Pastorius dossier

Do these in order. Total time: about 30–40 minutes. The only waiting is Gumroad's payout verification.

## 1. Create the account (you must do this yourself)
1. Go to gumroad.com > Start selling. Sign up with yesmidealab.contact@gmail.com and verify the email.
2. Settings > Profile: name "Lives At WW2", username **yesmidealab** (this makes the link `yesmidealab.gumroad.com`), short bio, profile picture.

## 2. Payout details (Settings > Payments)
- Country: Bangladesh. Currency: USD (customers always pay in USD).
- Add your legal name, address, date of birth and a Bangladeshi bank account (bank name, branch, account number, SWIFT code) as Gumroad asks.
- If Gumroad asks for ID verification, upload it there. Payouts need a verified account.
- Expect: $100 minimum payout, a 7-day hold on new sales, then 2–7 bank days. Check current terms on Gumroad's own help pages.

## 3. Create the product (Products > New product)
| Field | Enter exactly |
| --- | --- |
| Type | Digital product |
| Name | Operation Pastorius: the case file (Mission Dossier No. 1) |
| Price | $7 (one-time, USD) |
| **URL slug** | **pastorius** (this must match the website buttons: `yesmidealab.gumroad.com/l/pastorius`) |
| Cover image | `site/assets/img/cover.jpg` |
| Thumbnail | `marketing/gumroad/pastorius-thumbnail-1200.jpg` (square, 1200×1200) |
| Files | Upload BOTH from `private/products/`: `..._Letter.pdf` and `..._A4.pdf` |

**Description** (paste):

> In June 1942, German submarines landed eight saboteurs on American beaches. Within sixteen days, every one of them was caught. This large-print dossier lets you follow the whole story at your own pace: the maps, the men, the night on the beach and the trial.
>
> • 15 pages in large, clear type
> • Prints on US Letter or A4 paper (both files included)
> • Maps and diagrams drawn for this edition
> • A minute-by-minute account of the night on the beach
> • A "record check" page showing where the sources disagree
>
> Digital download (PDF). Nothing is posted to you. 30-day money-back guarantee: email yesmidealab.contact@gmail.com.

**Receipt / "Content" page**: add the line "Thank you! Both paper sizes are below. Questions? yesmidealab.contact@gmail.com".

## 4. Settings to switch on
- Product > Share/Options: leave "Let customers pay more" off for now.
- Settings > Checkout: keep the email receipt on. Do not enable discount codes yet.
- Refund policy: Settings > Refund policy: 30 days (matches the website).

## 5. Publish and test
1. Click Publish. Open `https://yesmidealab.gumroad.com/l/pastorius`. It must load.
2. Test the full flow once: make a 100%-off discount code (Product > Discounts), buy with it from a second email address, and check that the receipt arrives and both PDFs download. Then delete the code.
3. Open the website's Buy button and confirm it lands on the same page.

## 6. After the first real sale
- Check Gumroad > Payouts shows the balance and status.
- Keep the receipt email format in mind for customer-support replies.

## If the link names change
Edit both Buy links in `site/index.html` (search for `gumroad.com/l/`), commit, push to main. The site redeploys itself.

---

# Product 2: The Pipes at Dawn, Complete Pack (main product on the website)

Create it the same way as step 3 above, with these values.

| Field | Enter exactly |
| --- | --- |
| Type | Digital product |
| Name | The Pipes at Dawn: Complete Pack (Mission Dossier No. 2) |
| Price | $10 (one-time, USD) |
| **URL slug** | **pipes-at-dawn** (must match the website: `yesmidealab.gumroad.com/l/pipes-at-dawn`) |
| Cover image | `marketing/gumroad/pipes-cover-1280x720.jpg` (1280×720; add `site/assets/img/pipes/pack-maps.jpg`, `pack-prints.jpg`, `pack-certificate.jpg` as extra preview images) |
| Thumbnail | `marketing/gumroad/pipes-thumbnail-photo-1200.jpg` (square, 1200×1200; the older `pipes-thumbnail-1200.jpg` is a spare) |
| Files | Upload all five PDFs from `private/products/pipes-at-dawn/` **and** `The-Pipes-at-Dawn_Complete-Pack.zip` (one-click download of everything) |

The five PDFs (all US Letter):
1. `Lives-At-WW2_Mission-Dossier-02_The-Pipes-at-Dawn_Letter.pdf` (27 pages)
2. `Lives-At-WW2_Pipes-at-Dawn_Map-Pack_Letter.pdf` (7 maps)
3. `Lives-At-WW2_Pipes-at-Dawn_Archive-Photo-Prints_Letter.pdf` (5 prints)
4. `Lives-At-WW2_Pipes-at-Dawn_Tribute-Poster-and-Certificate_Letter.pdf`
5. `Lives-At-WW2_Pipes-at-Dawn_Family-History-Workbook_Letter.pdf`

**Description** (paste):

> A man with no rifle, walking upright ahead of the attack, playing the bagpipes. Follow Scotland's battle pipers from the gas at Loos in 1915 to the minefields of El Alamein and Bill Millin on D-Day, and find out which famous stories are true and which are only legend.
>
> **What you get: five printable files**
> 1. The dossier, 27 large-print pages: the full story, a record check on every famous claim, four archive photographs with notes on what to look for, the Victoria Cross citation, the roll of named Alamein pipers, the tunes, a timeline and sources
> 2. Map pack: 7 large maps, one to a page (Loos, El Alamein, the night attack, Sicily, Sword Beach to Pegasus Bridge, and a visitor's map)
> 3. Archive photo prints: 5 public-domain wartime photographs to frame
> 4. Tribute posters and a Certificate of Remembrance to fill in with a family name
> 5. Family history workbook: "Was my grandfather a piper?" guide, questions to ask the family, a records log and a notes page
>
> All files are US Letter (on A4, choose "Fit to page").
> Goes with the documentary "What German Soldiers Said About the Scottish Highlanders' Bagpipes at Dawn" on Lives At WW2.
> Digital download. Nothing is posted to you. 30-day money-back guarantee: email yesmidealab.contact@gmail.com.

**Receipt / "Content" page:** "Thank you! Start with file 1, the dossier. Print at 100% on US Letter, or 'Fit to page' on A4. Questions? yesmidealab.contact@gmail.com"

**On YouTube:** put `https://shop.yesmedialab.com` (or the Gumroad link) in the video description and pinned comment of https://youtu.be/nQwC8NlTFeY.

**Rebuilding:** in `private/build`, run `python dossier_pipes.py` then `python pack_pipes.py`. Archive photos live in `private/photos/` (never commit them with the paid files; they are public domain, but the folder is private by design).

## Custom landing page for The Pipes at Dawn (Gumroad product ID `jnbhpje`)

`marketing/gumroad/landing-pipes.html` is a self-contained page (fonts and images inlined) that replaces the
default Gumroad product page. It has four `data-gumroad-action="buy"` buttons and live price/name fields.
Rebuild it after changing previews: `python marketing/gumroad/build_landing_pipes.py` (needs `private/photos/b5103.jpg`).

Run on your own computer (needs the Gumroad CLI and `gumroad auth login`):

```
cd marketing/gumroad
gumroad products page preview jnbhpje ./landing-pipes.html --json --no-input --non-interactive
```
Check `.sanitization_report` (no `<script>`, `data-gumroad-*` or `<button>` stripped) and that `.warning` is empty. Then:
```
gumroad products page publish jnbhpje ./landing-pipes.html --json --no-input --non-interactive
gumroad products page url jnbhpje --json --jq '.product.landing_url' --no-input --non-interactive
```
Open the live page and click "Get the complete pack" through to the checkout screen (don't pay).
To undo: `gumroad products page clear jnbhpje --yes --json --no-input --non-interactive`
