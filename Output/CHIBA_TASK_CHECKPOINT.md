# CHIBA Task Checkpoint

Updated: 2026-09-29 00:51:08 +08:00

## Current scope

Phase 2 Production Readiness — approved production publish of the collection filter UX theme.

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
- Configured collection listings to disable infinite scroll and show 24 products per page. Theme Check reports 0 errors and 21 warnings; collection JSON parsing, the required template-string scan, and `git diff --check` passed. This source change has not been published to Shopify production.

## Pending / blockers

- The previous GitHub synchronization blocker is resolved; `origin/main` includes `3d4ff34` and the follow-up commits through `3c2da19`.
- The current live Shopify theme remains `190387093817`; the 24-per-page collection change is source-only and is not live.

## Last known good production

- Live theme ID: `190387093817` (`CHIBA Filter UX Review 20260928-2250`)
- Storefront: https://shop.chibataiwan.com/collections/all
- Rollback theme ID: `190385455417` (`CHIBA Image Loading Preview 20260928-2200`, unpublished)
- Theme Check: 0 errors, 21 warnings.
- Search & Discovery filters: Price + Category (Product Type); Size and Color are absent.

## Next action

Obtain explicit approval before publishing the 24-per-page collection change to Shopify production. Do not perform a production publish without that approval.
