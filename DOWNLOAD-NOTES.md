# Wholechain docs — local mirror

Read-only snapshot of the Wholechain Documentation.AI repo (deployment branch `main`),
pulled via the authoring MCP on 2026-08-26. Structure mirrors the repo exactly, with
two unavoidable filesystem adaptations:

1. `update-a-location-/-trade-object.mdx` — the repo filename contains a literal `/`,
   which a filesystem cannot represent. Stored here URL-encoded as
   `update-a-location-%2F-trade-object.mdx`. (This `/` is itself one of the repo's anomalies.)
2. `scripts/Helpscout Beacon.js` — the MCP `get_page` returned no content for this file
   (empty on the repo side); stored here as an empty file.

Source of truth for the two large files:
- `documentation.json` — byte-identical to the live `get_site_config`.
- `api-reference/wholechain-openapi.json.json` — the full 195 KB spec (note the doubled
  `.json.json` extension is the real repo filename).
