# SIA Configuration API Documentation

> Akamai's Secure Internet Access (SIA) Configuration API offers a programmatic interface to manage policy settings to protect against enterprise security and acceptable user policy related events. A distributed configuration encapsulates all the rules for how to process DNS requests for your enterprise.

Fetch the complete documentation index at: https://techdocs.akamai.com/etp-config/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: Security connectors
- [Create a security connector](https://techdocs.akamai.com/etp-config/reference/post-security-connector.md): Creates a security connector.
- [List security connectors](https://techdocs.akamai.com/etp-config/reference/get-security-connectors.md): Returns security connectors.
- [List the current security connector versions](https://techdocs.akamai.com/etp-config/reference/get-security-connectors-latest-version.md): Provides the current version of the security connectors.
- [Get the security connector's latest available version](https://techdocs.akamai.com/etp-config/reference/get-security-connector-latest-versions.md): Provides the latest available version for the security connector.
- [Get a security connector](https://techdocs.akamai.com/etp-config/reference/get-security-connector.md): Returns the details of a specific security connector.
- [Delete a security connector](https://techdocs.akamai.com/etp-config/reference/delete-security-connector.md): Deletes the specified security connector. Add an `If-Match` header to prevent deleting any data another client has modified since you last accessed it.
- [Change a local security connector password](https://techdocs.akamai.com/etp-config/reference/post-security-connector-change-local-password.md): Changes the local password for the specified security connector.
- [Generate an activation code for a security connector](https://techdocs.akamai.com/etp-config/reference/post-security-connector-generate-activation-code.md): Generates the activation code for a security connector.
- [Upgrade a security connector](https://techdocs.akamai.com/etp-config/reference/post-security-connector-upgrade.md): Upgrades software of a specific security connector.
- [Update a security connector](https://techdocs.akamai.com/etp-config/reference/put-security-connector.md): Modifies details of the current security connector.
