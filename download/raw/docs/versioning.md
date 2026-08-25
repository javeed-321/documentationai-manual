---
updatedAt: 2025-09-05T18:35:08.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Versioning

You should insert a header in your api calls with the version of the Modulr api. This allows us to manage our clients' compatibility if we introduce any breaking changes in the api (which is rare).

To do this insert a header `x-mod-version` with a single integer version number as the value

Example: `x-mod-version: 1`

Only the major version number should be sent (so send 1 rather than 1.0.1)