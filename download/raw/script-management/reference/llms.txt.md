# Script Management Documentation

> Akamai's Script Management is a suite of tools to help you minimize performance impacts from JavaScripts.

Fetch the complete documentation index at: https://techdocs.akamai.com/script-management/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: API

- [API index](https://techdocs.akamai.com/script-management/reference/api/llms.txt): full category index
- [Script Management API](https://techdocs.akamai.com/script-management/reference/api.md)
- [API summary](https://techdocs.akamai.com/script-management/reference/api-summary.md)
- [Get started](https://techdocs.akamai.com/script-management/reference/get-started.md)
- [Script Management concepts](https://techdocs.akamai.com/script-management/reference/script-mgmt-concepts.md)
- [Rate limiting](https://techdocs.akamai.com/script-management/reference/rate-limiting.md)
- [Errors](https://techdocs.akamai.com/script-management/reference/errors.md)
- [400](https://techdocs.akamai.com/script-management/reference/400.md)
- [401](https://techdocs.akamai.com/script-management/reference/401.md)
- [403](https://techdocs.akamai.com/script-management/reference/403.md)
- [404](https://techdocs.akamai.com/script-management/reference/404.md)
- [409](https://techdocs.akamai.com/script-management/reference/409.md)
- [500](https://techdocs.akamai.com/script-management/reference/500.md)

## API Reference: Insights

- [Insights index](https://techdocs.akamai.com/script-management/reference/insights/llms.txt): full category index
- [Get insights](https://techdocs.akamai.com/script-management/reference/get-property-hostname-network-insights.md): Returns script performance information for the specified `propertyId`, `hostname`, and `network`.

## API Reference: Policies

- [Policies index](https://techdocs.akamai.com/script-management/reference/policies/llms.txt): full category index
- [Get a policy](https://techdocs.akamai.com/script-management/reference/get-property-hostname-network-policies.md): Returns information about the latest version of a policy for the specified `property`, `hostname`, and `network`.
- [Create a policy](https://techdocs.akamai.com/script-management/reference/post-property-hostname-network-policy.md): Creates a new policy for the specified `propertyId`, `hostname`, and `network`. The policy request needs to include the `spofConfig` object or `scriptConfig` array item, but it can contain both. Only one policy can exist per `hostname`. A change to the `spofConfig` or `scriptConfig` overwrites the existing policy. If a policy already exists with the same `spofConfig` and `scriptConfig`, the API responds with a 409 error and displays the existing policy.
