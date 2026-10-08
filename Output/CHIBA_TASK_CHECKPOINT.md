# CHIBA Task Checkpoint

Updated: 2026-10-01 03:19 +08:00

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
