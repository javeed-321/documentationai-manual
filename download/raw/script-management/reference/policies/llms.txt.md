# Script Management Documentation

> Akamai's Script Management is a suite of tools to help you minimize performance impacts from JavaScripts.

Fetch the complete documentation index at: https://techdocs.akamai.com/script-management/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: Policies
- [Get a policy](https://techdocs.akamai.com/script-management/reference/get-property-hostname-network-policies.md): Returns information about the latest version of a policy for the specified `property`, `hostname`, and `network`.
- [Create a policy](https://techdocs.akamai.com/script-management/reference/post-property-hostname-network-policy.md): Creates a new policy for the specified `propertyId`, `hostname`, and `network`. The policy request needs to include the `spofConfig` object or `scriptConfig` array item, but it can contain both. Only one policy can exist per `hostname`. A change to the `spofConfig` or `scriptConfig` overwrites the existing policy. If a policy already exists with the same `spofConfig` and `scriptConfig`, the API responds with a 409 error and displays the existing policy.
