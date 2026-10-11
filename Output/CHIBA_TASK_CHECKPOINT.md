## Latest recovery entry — 2026-10-12 00:59 +08:00

### Completed

- Updated the shared Shopify localization control so mobile displays it directly below the header icon row; removed the drawer duplicate. Desktop selector remains in its existing header position.
- Updated unpublished preview theme [0m`chiba-mobile-language-preview-20261012-0044` (ID `190807703865`) with only the three task-scoped files.
- Browser-verified mobile CSS widths 320px and 390px: selector is visible in the header without opening the drawer, no drawer duplicate, and header rows remain 60px + ~49px.
- Browser-verified desktop CSS width 1280px: selector remains visible in the existing header. Switching zh-TW → English → zh-TW preserves `/products/chiba-3010524-cycling`.
- Theme Check: 367 files inspected, 0 errors, 20 warnings.

### Pending / blocker

- The preview is validated but has not been published. Publishing to the live theme requires explicit approval.

### Last known good build

- Unpublished preview theme `190807703865` with the mobile header selector; current live theme remains unchanged by this language-switch task.

### Next action

- Await explicit approval before publishing the validated language-switch change to the live Shopify theme.

## Latest recovery entry — 2026-10-12 00:35 +08:00

### Completed

- Published only `snippets/breadcrumbs.liquid` to live Shopify theme `chiba-shopify-theme-20261011-2228` (ID `190804492601`); no other live-theme file was replaced.
- Pulled the live file back from Shopify and confirmed its Home anchor now uses `{{ locale_prefix }}`.
- Verified collection and product breadcrumb Home links in English and Traditional Chinese at 390px and 1280px: `/en-tw/` and `/zh-tw/`, respectively.
- Theme Check on the current-live theme snapshot: 366 files inspected, 0 errors, 20 warnings. The timestamped ZIP passed archive integrity, root layout, and core-template checks.
- Theme ZIP: `CHIBA-Shopify-theme-20261012-0033.zip`, SHA-256 `c6a6e8fabd980fb38432628cbcf33eb064399fddca480bd26b1becbec0c6b318`; identical copies are in the project root, `Output/`, and `Downloads/`.

### Pending / blocker

- None for the locale-aware breadcrumb fix. Other storefront backlog and the separate cached `/admin/` issue were not changed by this task.

### Last known good build

- Live theme `190804492601` with the scoped breadcrumb update; Theme Check has 0 errors.

### Next action

- No further action required for this fix.

## Latest recovery entry — 2026-10-11 23:44 +08:00

### Completed

- Updated the Shopify breadcrumb home link to use the existing request-path-aware locale prefix, so English and Traditional Chinese breadcrumbs return to their matching locale root.
- Shopify Theme Check passed: 0 errors, 20 existing warnings; `git diff --check` passed.

### Pending / blocker

- The breadcrumb change is committed and pushed to official GitHub, but has not been uploaded or published as a Shopify theme. Production theme publication requires explicit approval.

### Next action

- After approval, create a timestamped theme ZIP, upload it as an unpublished draft, verify the breadcrumb links on English and Traditional Chinese collection/product pages, then ask before publishing.

## Latest recovery entry — 2026-10-11 15:32 +08:00

### Completed

- Fixed the remaining active desktop/mobile navigation outputs by routing `grandchildlink.url` and the generic menu block through `localized-link-url`.
- Theme Check passed with 0 errors and 21 existing warnings; `git diff --check` passed.
- Pushed official `main` commit `f3ecf94d686420754f4180cec1199076cf48e0c3`.
- Built and uploaded `CHIBA-Shopify-theme-20261011-2228.zip`.
- Published Shopify theme `chiba-shopify-theme-20261011-2228` (theme ID `190804492601`).
- Removed the unused test theme `chiba-shopify-theme-20261011-2216` and accidentally added/removed Horizon without publishing it.
- Live verification confirms all visible English category links remain under `/en-tw/`, all visible Traditional Chinese category links remain under `/zh-tw/`, and English click destinations preserve `/en-tw/`.

### Pending / blocker

- No blocker for the locale-navigation task. Shopify preview iframe checks may still report CSP `frame-ancestors 'none'`; public storefront verification is the authoritative check.

### Next action

- Monitor the published storefront for CDN propagation; no further code change is required unless another navigation surface is reported.

## Latest recovery entry — 2026-10-11 15:17 +08:00

### Completed

- Created a first silent vertical Cycling performance Reel using approved CHIBA product imagery.
- Output: `CHIBA-cycling-performance-reel-20261011-1513.mp4`, 9.00 seconds, 1080x1920, H.264, no audio track.
- Saved the deliverable to `Downloads/` and `Output/`; original image assets were not modified.

### Pending / blocker

- Music has not been added; a licensed or user-provided track is required before a music version is exported.

### Next action

- Review the silent cut and select a legal music direction before producing the final sound version.

## Latest recovery entry — 2026-10-10 19:50 +08:00

### Completed

- Added English-only footer translations for `Taiwan Official Exclusive Distributor`, `Business Registration No.`, and `Customer Service Email` in `theme/snippets/text.liquid`.
- Preserved the Traditional Chinese footer source in `theme/sections/footer-group.json`.
- Shopify Theme Check passed with 0 errors; `git diff --check` passed for the change.
- Generated and validated `CHIBA-Shopify-theme-20261010-1955.zip` with a flat Shopify theme root and copied it to the project root, `Output/`, and `Downloads/`.

### Pending / blocker

- The Shopify worktree contains unrelated pre-existing changes and generated files, so no commit, push, or live theme publish was performed.

### Next action

- Publish the isolated theme change through an approved clean deployment workflow, then verify the English footer live while confirming the Traditional Chinese footer is unchanged.

## Latest recovery entry — 2026-10-10 14:28 +08:00

### Completed
- Unified language switchers for Desktop and Mobile using segmented pill [ 🇹🇼 繁中 | 🇬🇧 EN ].
- Decommissioned legacy duplicate dropdown selector (show_language: false in header-group.json).
- Added comprehensive Liquid fallback translations for Homepage: Announcement Bar, Hero Headline, Hero CTA Button, Featured Products Title, and Collection Sorting options.
- Added strict Cross-Device (Mobile & Desktop) and Multi-Language Delivery Standards into AGENTS.md across both Chiba-Shopify and Chiba-AI.
- Theme Check passed with 0 errors.

### Artifacts
- ZIP package: /Users/SammyWang/Downloads/CHIBA-Shopify-theme-bilingual-pill-20261010.zip

# CHIBA Task Checkpoint

Updated: 2026-10-01 03:19 +08:00

## Latest recovery entry — 2026-10-10 13:10 +08:00

### Completed

- Crawled all 102 public English URLs from the Shopify sitemap and saved the deterministic audit to `Output/english-storefront-audit-20261010/pages.tsv`: 93 products, 6 collections, 1 page, 1 blog, and the homepage; all requests returned HTTP 200.
- Confirmed the live English crawl still contains Chinese text on all 102 URLs, including product data and collection/page metadata that cannot be safely replaced in theme Liquid.
- Added English-only fallbacks for mega-menu and mobile drawer series labels while retaining the Traditional Chinese fallback.
- Re-ran Shopify Theme Check with 0 errors and `git diff --check` passed.

### Pending / blocker

- Shopify Admin Translate & Adapt must create English translation records for the 93 product resources and the collection/page/blog resource fields; the theme repository cannot create those records without Shopify Admin access.
- The local theme remains unpublished because unrelated uncommitted files are present; no publish or commit was performed.

### Next action

- In Shopify Admin, run Translate & Adapt for the audited resource groups, then re-run `pages.tsv` audit and inspect all 102 English URLs for zero unintended Chinese customer-facing text.

## Latest recovery entry — 2026-10-10 13:10 +08:00
- Confirmed the English storefront route `/en` exists but still renders substantial Chinese content on navigation, collection, product, and custom-page surfaces.
- Added language-aware English fallbacks while preserving the existing Traditional Chinese branches in the category entrance, trust badges, technology spotlight, breadcrumbs, mobile drawer, product trust badges, glove size guide, cart free-shipping bar, and collection heading.
- Shopify Theme Check passed with 0 errors; existing warnings remain.
- `git diff --check` passed.
- Official `origin/main` was fetched and is aligned with local `HEAD`; no rebase was attempted because unrelated uncommitted work is present.

### Pending / blocker

- Product titles, descriptions, option values, collection names, and SEO fields for the 94 live products still require Shopify product translation records; theme Liquid cannot safely translate those stored product fields without changing the Traditional Chinese source.
- The live theme has not been published because the worktree contains unrelated uncommitted files and no approved isolated deployment boundary.
- English navigation/menu labels and remaining hardcoded template JSON content need a second audit after the product translation workflow is available.

### Next action

- Obtain an approved Shopify Admin translation workflow/token or a reviewed translation import artifact, then create English translations for all public products and pages and verify `/en` without modifying Traditional Chinese output.

## Latest recovery entry — 2026-10-10 09:02 +08:00

### Completed

- Audited the reorganized canonical Shopify CSV at `data/02_structured_data/CHIBA_Shopify_Full_Products_Fixed_20260930-0115.csv`: 93 products, 1,259 variants, 0 populated `Product Category` values, and 0 populated `Variant Barcodes` values.
- Probed the live UCP discovery and MCP catalog contract at `shop.chibataiwan.com`; `search_catalog` is the scanner-facing catalog tool.
- Ran a read-only live `search_catalog` request for `手套`; all 10 returned products had no `category`, `product_type`, `brand`, or `vendor` field in the response.
- Confirmed live `/llms.txt` and `/agents.md` already contain the custom CHIBA agent description; no `llms.txt` change is currently justified.

### Pending / blocker

- Build a deterministic 93-product category mapping and apply verified Shopify taxonomy categories through an approved Admin/CSV workflow.
- Re-run the live catalog scan after category updates and compare the exact response fields before considering the agent-catalog gate passed.
- Git sync is currently blocked by unrelated local uncommitted files; do not stash or overwrite them without approval.

### Next action

- Prepare a category-audit artifact from the reorganized canonical CSV only; do not invent GTIN/MPN values and do not modify live Shopify data until the taxonomy mapping is reviewed.

## Latest recovery entry — 2026-10-10 09:05 +08:00

### Completed

- Audited the reorganized `data/` sources without modifying product or live Shopify data.
- Verified `data/chiba_cycling_fitness_products_bilingual_front+Palm_thumbnails.xlsx` contains 93 product records with source handles matching all 93 handles in the canonical Shopify CSV.
- Verified the workbook's explicit source classification is complete: 38 `Cycling / 自行車` products and 55 `Fitness / 健身` products.
- Confirmed the workbook includes useful per-product fields for the next mapping phase: bilingual names and descriptions, source handle, SKU list, size/color data, price, inventory, publication state, and catalog status.
- Confirmed the existing structured importer in `data/00_uncategorized/import_sheets.py` uses a separate internal `cycling`/`fitness` content category; it is not a Shopify taxonomy mapping and must not be treated as one.

### Pending / blocker

- Map the workbook's 38/55 source categories and product semantics to Shopify's accepted taxonomy values or IDs. The workbook is authoritative for source grouping, but it does not itself provide Shopify taxonomy IDs.
- Do not overwrite the canonical CSV or live Shopify products until the taxonomy value format is confirmed.
- Git sync remains blocked by unrelated local uncommitted reorganized data; do not stash or overwrite it without approval.

### Next action

- Use the workbook as the join key and create a reviewable Handle-to-Shopify-taxonomy mapping. Start with the two clear top-level groups, then classify fitness accessories (belts, wraps, straps, grips, bags, and harnesses) separately from gloves.

## Latest recovery entry — 2026-10-10 09:08 +08:00

### Completed

- Created [CHIBA-product-category-review-20261010-0908.csv](./CHIBA-product-category-review-20261010-0908.csv) from the reorganized workbook and canonical CSV without changing either source.
- Validated 93 unique Handles, including 38 Cycling and 55 Fitness products.
- Classified the products into semantic groups: 38 cycling gloves, 19 fitness gloves, 6 grip aids, 3 wrist supports, 4 knee supports, 6 lifting straps, 11 weightlifting belts, and the remaining named training accessories.
- Added evidence, confidence, and review flags to every mapping row. Current result: 85 high-confidence and 8 medium-confidence candidates.
- Corrected the rule precedence so products explicitly named as gloves remain gloves even when they include wristguard or lifting-assistance features; Powerhook and Strongman Gripper remain grip aids.
- Confirmed the review artifact leaves `Current Product Category` blank for all rows; no Shopify taxonomy or live product data was changed.

### Pending / blocker

- Confirm the exact accepted Shopify taxonomy names or IDs for the candidate categories, especially grip aids, harnesses, loop accessories, and barbell pads.
- Human review is still required before changing the canonical CSV or Shopify Admin.

### Next action

- Review the eight medium-confidence rows and resolve the exact Shopify taxonomy IDs, then prepare a separate 43-column CSV patch only if the taxonomy values are confirmed.

## Latest recovery entry — 2026-10-10 09:10 +08:00

### Completed

- Resolved 89 of 93 review rows against Shopify's official `Shopify/product-taxonomy` distribution.
- Added official taxonomy GIDs and exact breadcrumb paths to [CHIBA-product-category-review-20261010-0908.csv](./CHIBA-product-category-review-20261010-0908.csv).
- Verified official mappings include bicycle gloves, weight lifting gloves, grip pads and hand grips, wrist wraps, weight lifting straps, weight lifting belts, barbell pads, knee braces, and elbow supports.
- Reduced unresolved rows to four: `chiba-40700-fitness` Head Harness, `chiba-40710-fitness` Arm Loops, `chiba-40720-fitness` Leg Loops, and `chiba-40755-fitness` Fitness Bag.
- Validation passed: 93 unique Handles, 89 official taxonomy IDs, 4 unresolved rows, and no source CSV or live Shopify changes.

### Pending / blocker

- Confirm the correct official leaf category for the four remaining training accessory/bag products; do not map them to a broad guessed category.
- After those four are resolved, generate a separate 43-column CSV patch from the canonical CSV and run the existing Shopify CSV gate before any import.

### Next action

- Obtain or confirm the four remaining taxonomy choices, then create the import patch and stop for explicit approval before changing live Shopify.

## Latest recovery entry — 2026-10-10 09:14 +08:00

### Completed

- Verified the four proposed mappings against Shopify's official taxonomy:
  - Head Harness, Arm Loops, and Leg Loops use the parent `sg-2-24` Weight Lifting category.
  - Fitness Bag uses the more specific official `lb-6-1` Gym Duffel Bags category, rather than the broader luggage parent.
- Updated [CHIBA-product-category-review-20261010-0908.csv](./CHIBA-product-category-review-20261010-0908.csv) with official GIDs for all 93 products.
- Generated [CHIBA_Shopify_Product_Category_Patch_20261010-0914.csv](./CHIBA_Shopify_Product_Category_Patch_20261010-0914.csv) from the canonical 43-column CSV without modifying the canonical source.
- Validation passed: UTF-8 BOM, 43 columns, 1,259 rows, 93 unique products, and one verified official category GID per product.

### Pending / blocker

- The category patch has not been imported into Shopify and no live data was changed.
- Explicit approval is required before any Shopify Admin import or live mutation.
- After import, re-run UCP `search_catalog` and the scanner to confirm that `category` is present in the live response.

### Next action

- Wait for approval to import [CHIBA_Shopify_Product_Category_Patch_20261010-0914.csv](./CHIBA_Shopify_Product_Category_Patch_20261010-0914.csv), then verify the live catalog response and scanner result.

## Latest recovery entry — 2026-10-10 09:26 +08:00

### Completed

- Created the three-product Shopify import test file [CHIBA_Shopify_Product_Category_Test_20261010-0926.csv](./CHIBA_Shopify_Product_Category_Test_20261010-0926.csv).
- Synchronized the same timestamped test file to `/Users/SammyWang/Downloads/`.
- Selected one cycling glove (`chiba-3030424-cycling`), one fitness glove (`chiba-42155-fitness`), and one fitness bag (`chiba-40755-fitness`) to exercise three taxonomy branches and the external-image case.
- Preserved the original 43-column schema, all 50 source rows/variants for those three products, UTF-8 BOM, SKUs, prices, images, and inventory fields.
- Validation passed: 50 rows, 43 columns, 3 unique products, and one official Product Category GID on each product's first row.
- The full category patch and canonical CSV were not changed.

### Pending / blocker

- Shopify Admin import preview/test upload has not been performed.
- After preview, inspect category acceptance, variant counts, image fetch results, prices, inventory, and product status before any full import.

### Next action

- Upload the test file only in Shopify Admin and stop at the preview screen unless the preview is clean and explicitly approved for import.

## Latest recovery entry — 2026-10-10 09:40 +08:00

### Completed

- Switched to the official local Chiba-AI workspace at `/Users/SammyWang/Chiba-AI`; confirmed it is the source for `www.chibataiwan.com`.
- Added `release-site/snapshot/llms.txt` with Traditional Chinese brand, product, service, and official Shopify links.
- Updated `release-site/release.json` with the SHA-256 binding and corrected `file_count` to 1,534.
- Ran `SITE_ENV=production python3 build.py`; production build passed and manifest/file hashes matched.
- Committed the scoped Chiba-AI change locally as `3214477` (`Add brand site llms.txt`) with the required Copilot co-author trailer.

### Pending / blocker

- Official `git pull --rebase origin main` and `git push origin main` could not authenticate in this environment (`fatal: unable to get password from user`).
- Live `https://www.chibataiwan.com/llms.txt` remains HTTP 404 because the commit has not reached the official remote/Cloudflare Pages deployment.
- No direct upload or DNS change was performed.

### Next action

- Authenticate GitHub for the official `archielin0725/Chiba-AI` remote, push commit `3214477`, wait for Cloudflare Pages Git deployment, then verify `/llms.txt` returns HTTP 200 with the committed content.

## Latest recovery entry — 2026-10-01 03:19 +08:00

### Completed

- Added `Credit Conservation & Input Ambiguity Pre-Warning Standard` (額度保護與模糊指令主動預警標準) as a permanent rule to `AGENTS.md`.
- Enshrined mandatory proactive braking: when user inputs are broad, ambiguous, or lack specific targets, AI is strictly required to pause, issue a high-cost warning, and suggest 1~3 specific scoping options before executing expensive queries.
- Synchronized `AGENTS.md` across `Chiba-Shopify` and `Chiba-AI`; executed `audit_md_health.py` and passed all governance assertions (210 lines, ~26KB, 100% byte-for-byte identical, symlinks valid).
- Committed and pushed to `archielin0725/Chiba-AI` and `archielin0725/Chiba-Shopify` `main`.

### Pending / blocker

- None. Permanent credit protection rule is active and enforceable immediately.

## Latest recovery entry — 2026-10-01 03:12 +08:00

### Completed

- Executed Change Request `CR-20261001-WASH-TRANSLATION` on `archielin0725/Chiba-AI` (`www.chibataiwan.com`).
- Identified and replaced residual German washing terms `MASCHINENWÄSCHE` and `Waschbar bis 30°C` in technology Section 3 (material feature 08):
  - In `zh-tw/technology/index.html` (dist & snapshot L248, L253):
    - Icon badge: `<span>30°C MASCHINENWÄSCHE</span>` ➔ `<span>可於 30°C 機洗</span>`
    - Card heading: `<h4>Waschbar bis 30°C 全手套可機洗</h4>` ➔ `<h4>30°C Machine Washable 可於 30°C 機洗</h4>`
  - In `en/technology/index.html` (dist & snapshot L217) & `scripts/build_english_site.py` (L427):
    - Icon badge: `<span>30°C MASCHINENWÄSCHE</span>` ➔ `<span>30°C MACHINE WASHABLE</span>`
  - In `scripts/enrich_shopify_csv.py`:
    - Updated internal references from `Maschinenwäsche` to `Machine Washable`.
- Re-computed snapshot file checksums in `release-site/release.json`.
- Verified 0 remaining occurrences of `MASCHINENWÄSCHE` and `Waschbar bis` in `release-site` and `scripts`.
- Committed and pushed to `archielin0725/Chiba-AI` `main` (`ecd8e44`).

### Pending / blocker

- None. Both BioXCell and washing label German strings have been completely cleared and localized.

## Latest recovery entry — 2026-10-01 02:55 +08:00

### Completed

- Executed Change Request `CR-20261001-TECH-TRANSLATION` on `archielin0725/Chiba-AI` (`www.chibataiwan.com`).
- Identified and replaced residual German string `Zweistufiger Aufbau` in BioXCell pillar 01 title with `Two-Stage Construction` across all tracked and build files:
  - `release-site/snapshot/zh-tw/technology/index.html` (L119)
  - `release-site/dist/zh-tw/technology/index.html` (L119)
  - `release-site/snapshot/en/technology/index.html` (L97)
  - `release-site/dist/en/technology/index.html` (L97)
  - `scripts/build_english_site.py` (L307)
  - `scratch/prototype_tech_desktop.html` (L406)
- Synchronized `release.json` with updated snapshot file checksums.
- Executed ripgrep search across `Chiba-AI`; verified 0 residual occurrences of `Zweistufiger Aufbau`.
- Committed and pushed to `archielin0725/Chiba-AI` `main` branch (`db9fd97fe4f8b683a8c39d58f26bffc8082886d4`).
- Theme performance & preview zip `CHIBA-Shopify-theme-20260930-0133.zip` remains packaged and verified for user preview.

### Pending / blocker

- None for website text translation. Production static site on `Chiba-AI` is clean and pushed.

## Latest recovery entry — 2026-09-30 01:15 +08:00

### Completed

- Performed a full HTTP status and integrity audit of all 434 unique product image URLs across all 93 products and 1,259 variants in the canonical Shopify master CSV.
- Detected that precisely 1 URL returned HTTP 404: `https://cdn.shopify.com/s/files/1/1015/5950/1113/files/fitness__40425__darkgrey-19__fd707c0881e3a416__40425-19-1.jpg?v=1790331652` for product `chiba-40425-fitness` (Air Performer 透氣機能訓練手套), while all other 433 URLs were 100% healthy (HTTP 200).
- Confirmed the user updated the image on live Shopify to `https://cdn.shopify.com/s/files/1/1015/5950/1113/files/CHIBA-40425-darkgray-front-20260930-0047.jpg?v=1790700613` (HTTP 200).
- Updated the canonical master CSV (`/Users/archie/Chiba-AI/data/canonical_shopify_products_master.csv`) by replacing the broken 404 URL in both `Image Src` (position 3) and `Variant Image` for all six `40425-DARKGREY19` variants (XS through XXL).
- Generated verified, timestamped milestone delivery files:
  - `/Users/archie/Downloads/CHIBA_Shopify_Full_Products_Fixed_20260930-0115.csv`
  - `/Users/archie/Chiba-Shopify/Output/CHIBA_Shopify_Full_Products_Fixed_20260930-0115.csv`
- Executed `python3 scripts/verify_shopify_csv_gate.py` on all copies; verified 100% pass across UTF-8 BOM, 43 columns, 93 canonical products, 0 duplicate variants, and 0 invalid categories.
- Re-tested image URLs for 40425; confirmed all 6 URLs return HTTP 200 with zero broken links.
- Synchronized `AGENTS.md` across `Chiba-Shopify` and `Chiba-AI`; passed `audit_md_health.py` with 0 issues.

### Pending / blocker

- None for product CSV. The live Shopify store and canonical product CSV are now 100% aligned.

## Latest recovery entry — 2026-09-30 00:55 +08:00

### Completed

- User approved updating the live Shopify product `chiba-40425-fitness`.
- Uploaded the verified official Air Performer deep-gray front/hand-back image (`40425-19-1.jpg`) as Shopify media.
- Assigned that image to all six `40425-DARKGREY19` variants and retained the existing deep-gray palm/grip image in the product gallery.
- Saved the product and verified the live product JSON contains six gallery images and all six deep-gray variants point to the newly uploaded front image.
- Verified the live product page with deep-gray XS selected; the gallery renders the CHIBA-logo hand-back image as its first image.
- The authoritative source image is already in official `archielin0725/Chiba-AI` `main` (`860f03e4dacba2ba487d0eae47f53e788d6c15aa`) and its SHA-256 matches the official release manifest.

### Pending / blocker

- No product code or canonical data files were changed; the approved update was made directly in Shopify product media and variant assignments.
- The earlier theme-announcement German emoji still requires uploading and publishing `CHIBA-Shopify-theme-20260929-2040.zip`.

## Latest recovery entry — 2026-09-30 00:47 +08:00

### Completed

- Confirmed the official `Chiba-AI` `main` includes the deep-gray front image for Air Performer SKU 40425: `fitness__40425__darkgrey-19__fd707c0881e3a416__40425-19-1.jpg`.
- Verified the image's SHA-256 against the official release manifest and visually confirmed it shows the CHIBA logo / hand-back side, unlike the palm-side `19-2` image currently used by Shopify.
- Shopify's public product JSON has five images and omits the `19-1` front image. The existing product-media records include dark-gray `19-2` but no dark-gray `19-1`.
- Prepared the verified official image in Downloads and `Output/` as `CHIBA-40425-darkgray-front-20260930-0047.jpg`; both copies match the official source checksum.
- No live Shopify product change has been made.

### Pending / blocker

- A production product-media change needs user approval. Proposed minimal fix: add the official `19-1` image to the Shopify gallery and assign it as the deep-gray variant's default image, retaining the existing `19-2` palm/grip image as a secondary gallery photo.
- Shopify Admin is accessible in the browser, but this change has not been saved. Once approved, update the product and verify all six deep-gray sizes display the correct image.
- Earlier flag task remains at a valid manual-upload stop: the announcement bar still renders an emoji unless the refreshed theme ZIP is uploaded and published.

## Latest recovery entry — 2026-09-30 00:27 +08:00

### Previous task valid stop before switching scope

- Live storefront check confirms the product-page German flag is an SVG, but the announcement bar still contains the German flag emoji. The user was given the verified alternative: upload `CHIBA-Shopify-theme-20260929-2040.zip` as a draft, preview, and publish; no new production upload is assumed.
- Official repository source was fetched before starting the new product-image investigation.

### New task — Air Performer dark-gray product image

- User reports the dark-gray gloves on `chiba-40425-fitness` do not show the correct front view. The supplied screenshot shows deep gray selected and the current gallery displaying the glove palm/grip side.
- Local product export includes inconsistent image URLs and variant-image associations for `40425-DARKGREY19`; determine the authoritative front-image asset before changing any product data.
- No product data or production listing has been changed.

## Latest recovery entry — 2026-09-29 21:26 +08:00

### Completed

- Clarified that official `archielin0725` GitHub repositories are the only source of truth for both Chiba websites, including `www.chibataiwan.com`.
- Replaced ambiguous dual-account pipeline language: `sammywanwan` repositories and local copies are downstream mirrors/workspaces only, never authority or mandatory sync hops.
- Confirmed current task branch was up to date with official `origin/main` before editing.

### Pending / blocker

- Validate and push this governance clarification to official `archielin0725` main; sync the personal mirror only afterward if applicable.
- The corrected 20:40 Shopify theme ZIP remains pending user upload/publish for the announcement-bar flag.

## Latest recovery entry — 2026-09-29 20:43 +08:00

### Completed

- Confirmed the official `archielin0725/Chiba-Shopify` and personal `sammywanwan/Chiba-Shopify` `main` branches both match `ac58278`, including the flag-fix source.
- Added an explicit standing rule to automatically sync validated changes to official `archielin0725` GitHub without requiring another prompt; the Sammy repository is a mirror only.

### Pending / blocker

- The 20:40 corrected full-theme ZIP still needs uploading as a Shopify draft and publishing to replace the remaining live announcement emoji. Official GitHub source is current, but production sync/deployment is not confirmed.

## Latest recovery entry — 2026-09-29 20:40 +08:00

### Completed

- Verified the live Lady Ibiza page now renders the German product trust flag from `flag-de.svg`; the CDN image loaded successfully at 24x16.
- Confirmed `archielin0725/Chiba-Shopify` `main` matched local commit `5f625ab774f570e26fadb36696175084093df546`, including the original six-file SVG fix.
- Detected one remaining German emoji in the live announcement bar, encoded in `sections/header-group.json`.
- Updated the announcement block to replace that legacy emoji with the German flag SVG at render time. Shopify Theme Check passed with 0 errors and 21 warnings; header JSON and whitespace checks passed.
- Created and verified corrected full-theme ZIP `CHIBA-Shopify-theme-20260929-2040.zip` in both `Output/` and `Downloads/`; copies have matching SHA-256.

### Pending / blocker

- The 20:40 ZIP has not been uploaded. The currently published theme still has the emoji in its announcement bar, although the product detail trust flag works. Upload the new ZIP as a draft, preview the announcement and product page, then publish to replace the live theme.
- Commit and push this last announcement fix to both official `origin/main` and Sammy's personal `sammy/main`; then confirm official main matches the final commit.
- Windows 11 rendering remains unverified; all flag surfaces should use the SVG after publishing the corrected ZIP.

## Latest recovery entry — 2026-09-29 20:31 +08:00

### Completed

- Recorded a standing standard to offer a safe, practical alternative with trade-offs and an exact next step as soon as a proposed route is blocked.
- Added Shopify deployment fallback guidance covering CLI authorization, draft ZIP upload, GitHub repository access/layout, and clear production verification.

### Pending / blocker

- The full theme ZIP is ready for user upload and preview; no production publish is confirmed.
- The rule updates are ready for validation and synchronization.

## Latest recovery entry — 2026-09-29 20:28 +08:00

### Completed

- Created a complete Shopify theme ZIP containing root-level theme folders and all current theme files, including the German flag SVG fix.
- Verified ZIP integrity, root structure, critical templates, and matching SHA-256 for the project and Downloads copies.
- Theme Check passed before packaging with 0 errors and 21 warnings.

### Pending / blocker

- The ZIP has not been uploaded to Shopify. Upload it through Online Store > Themes > Add theme > Upload ZIP to create a draft; preview before publishing.
- The GitHub theme-integration path is not viable through the account currently accessible to the user: Shopify documents that personal repositories where the user is a collaborator but not the owner aren't listed. The theme also lives inside the repository's `theme/` directory, while the integration expects Shopify theme files at repository root.
- The flag-fix commit is already on both GitHub `main` branches at `83e4ac7`; no production update is confirmed.
- ZIP files: `Output/CHIBA-Shopify-theme-20260929-2028.zip` and `/Users/SammyWang/Downloads/CHIBA-Shopify-theme-20260929-2028.zip`.

## Latest recovery entry — 2026-09-29 20:05 +08:00

### Completed

- Committed the six German-flag SVG fix files as `83e4ac7` and pushed the commit to `origin/main`. GitHub confirms the commit and exact six-file scope.
- Shopify Theme Check passed with 0 errors and 21 warnings; `git diff --check` passed.

### Pending / blocker

- The public Lady Ibiza product page still renders the German flag emoji after the push; the GitHub push has not been verified as synced to the live theme. Production has not been confirmed updated.
- Shopify's connected repository and branch could not be verified from the Admin page. Next action: confirm the repository/branch connection in Shopify Online Store > Themes, then trigger or wait for sync and verify the public storefront. If not connected to `origin/main`, use an authorized deployment path.
- The earlier staged checkpoint changes and the local patch ZIP remain uncommitted; neither was included in `83e4ac7`.

## Latest recovery entry — 2026-09-29 18:48 +08:00

### Completed

- Replaced every German flag emoji in the Shopify public theme with the official-site-matched German flag SVG asset in the product trust badges, header drawer, brand trust section, and glove size guide.
- Shopify Theme Check passed with 21 warnings and zero errors; SVG validation, `git diff --check`, and the flag-emoji scan passed.

### Pending / blocker

- Production publication was requested but is blocked: `shopify theme list --store shop.chibataiwan.com` reports the CLI is not authorized for `shop.chibataiwan.com.myshopify.com`.
- No production theme files were published. Live theme remains `190387093817`; rollback theme remains `190385455417`.
- Next action: complete Shopify Admin/CLI authorization, then publish only `assets/flag-de.svg`, `assets/base.css`, `sections/brand-trust-badges.liquid`, `snippets/glove-size-guide.liquid`, `snippets/header-drawer.liquid`, and `snippets/pdp-trust-badges.liquid`; verify storefront and flag rendering.

## Latest recovery entry — 2026-09-29 18:37 +08:00

### Completed

- Investigated Windows 11 rendering issue where the German flag emoji appears as the letters "DE".
- Confirmed the official static website renders flags as SVG image assets (`/assets/flags/tw.svg` and `/assets/flags/de.svg`), avoiding platform-dependent emoji rendering.
- Replaced all four German flag emoji uses in the Shopify theme with a local `flag-de.svg` asset: product trust badges, drawer brand badge, brand trust section, and glove size guide.
- Added explicit sizing/alignment for the image in each component. No publication, commit, or push was performed.

### Pending

- Shopify Theme Check passed with 21 existing warnings and zero errors; SVG XML validation, `git diff --check`, and a full flag-emoji scan passed.
- Verify the rendered theme in Windows 11 before any production rollout. No production publish, commit, or push has been performed.

## Latest recovery entry — 2026-09-29 01:20 +08:00

### Completed

- Production pagination deployment is complete on live theme `190387093817`; public `/collections/all?page=2` was verified with numbered pagination for pages 1–4.
- GitHub `origin/main` contains the pagination settings in `d38a72f7e886ce313610ffbe83ca8d9faf6f8aa2`.
- The temporary task branch was rebased onto `origin/main`; it now contains commit `d38a72f` and the duplicate local template edit has been removed.

### Pending

- None for this task.

## Current scope

Phase 2 Production Readiness — collection product pagination update; prior collection filter UX production rollout remains live.

## Completed

- Published `CHIBA Filter UX Review 20260928-2250` (theme ID `190387093817`) to production after explicit user approval.
- Verified Shopify reports theme `190387093817` as `[live]`, and the production storefront returns theme ID `190387093817` with role `main`.
- Confirmed the previous live theme `CHIBA Image Loading Preview 20260928-2200` (ID `190385455417`) is now unpublished and remains available as rollback.
- Verified production collection toolbar, category facet interaction, and that applying a category filter reduces the displayed count from 93 to 55.
- Corrected the collection filter UI: removed the guarantee card and duplicate drawer sorting; sorting stays in the toolbar.
- Corrected price filtering to display Taiwan retail currency as `NT$` without `.00`.
- In Shopify Search & Discovery, removed the Color criterion per user direction and saved a `分類` criterion from Product Type with localized values `自行車系列` and `健身重訓系列`. Size is not enabled. These storefront filter settings are shared with the live theme.
- Verified the live drawer shows only `價格` and `分類`, with the two requested localized category values; no Size, Color, guarantee card, or drawer sorting appears.
- Shopify Theme Check: 0 errors, 21 warnings. `git diff --check` and JavaScript syntax check passed.
- Configured collection listings to disable infinite scroll and show 24 products per page. Shopify Theme Check reported 0 errors and 21 warnings; collection JSON parsing and `git diff --check` passed. The change was published to live theme `190387093817`, verified on the public collection page, and committed to GitHub `main` as `d38a72f`.

## Pending / blockers

- The temporary task branch is aligned with `origin/main` at `d38a72f`. The previous GitHub synchronization blocker was resolved upstream.
- The current live Shopify theme remains `190387093817`; the rollback theme remains unpublished as `190385455417`.

## Last known good production

- Live theme ID: `190387093817` (`CHIBA Filter UX Review 20260928-2250`)
- Storefront: https://shop.chibataiwan.com/collections/all
- Rollback theme ID: `190385455417` (`CHIBA Image Loading Preview 20260928-2200`, unpublished)
- Theme Check: 0 errors, 21 warnings.
- Search & Discovery filters: Price + Category (Product Type); Size and Color are absent.

## Next action

No pending action for this pagination task.
