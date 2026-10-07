# Gumroad setup kit: Operation Pastorius dossier

Do these in order. Total time: about 30–40 minutes. The only waiting is Gumroad's payout verification.

## 1. Create the account (you must do this yourself)
1. Go to gumroad.com > Start selling. Sign up with yesmidealab.contact@gmail.com and verify the email.
2. Settings > Profile: name "WWII Insider", username **yesmidealab** (this makes the link `yesmidealab.gumroad.com`), short bio, profile picture.

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
| Thumbnail | same image |
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
