# Shopify Theme Guardian

## When deployment is blocked

- State the exact blocker and what has or has not changed in production.
- Offer the simplest safe alternative immediately, with trade-offs and a concrete next action.
- For CLI authorization failures, a complete theme ZIP can be uploaded as an unpublished Shopify draft. Verify the ZIP, preview the draft, and publish only after explicit user approval.
- For GitHub integration, verify repository ownership/access and confirm the Shopify theme files are at the repository root; Shopify may not list personal repositories where the account is only a collaborator, and nested theme folders may not match the expected theme structure.
- Do not repeatedly ask the user to inspect settings or screenshots without explaining what evidence is needed and what decision it will resolve.
- Clearly distinguish a committed/pushed change from a verified Shopify sync or live production update.
