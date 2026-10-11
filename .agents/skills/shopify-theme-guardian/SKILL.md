# Shopify Theme Guardian

## Official repository sync

- Treat the official `archielin0725` GitHub repository as the sole source of truth for both Chiba websites. After each requested theme change passes the required validation, commit only the task-scoped files, push to official `origin/main` without waiting for a separate reminder, and verify the remote commit SHA.
- `sammywanwan` repositories and local copies are downstream mirrors/workspaces only. Never treat them as authority or a required synchronization hop; update a mirror only after official sync when needed.
- A GitHub push is not proof of Shopify deployment. Verify the published storefront separately.

## When deployment is blocked

- State the exact blocker and what has or has not changed in production.
- Offer the simplest safe alternative immediately, with trade-offs and a concrete next action.
- For CLI authorization failures, a complete theme ZIP can be uploaded as an unpublished Shopify draft. Verify the ZIP, preview the draft, and publish only after explicit user approval.
- For GitHub integration, verify repository ownership/access and confirm the Shopify theme files are at the repository root; Shopify may not list personal repositories where the account is only a collaborator, and nested theme folders may not match the expected theme structure.
- Do not repeatedly ask the user to inspect settings or screenshots without explaining what evidence is needed and what decision it will resolve.
- Clearly distinguish a committed/pushed change from a verified Shopify sync or live production update.

## Bilingual storefront validation

- A working language selector does not prove that the storefront is translated. For each active locale, inspect rendered text and accessible image text on the target page at mobile and desktop widths, including the announcement bar, navigation/drawer, price labels, trust badges, calls to action, and recommendation headings.
- Confirm the selected locale and route after switching, then verify the page copy itself before calling the change complete.
- Before publishing a replacement theme, check whether Translate & Adapt theme-content translations need to be preserved or migrated; use only a Shopify-supported workflow and verify the candidate theme before publishing.
- When changing collection sort labels or filtering sort choices, inspect the actual `results.sort_options` values and test both the native select and custom list. Shopify may return `most-relevant`; keep the featured/relevance choice deduplicated.
