# Client Access Control Documentation

> Manage access between your web assets and the edge servers on the Akamai network. With Client Access Control you can retrieve information about the CIDR blocks that currently connect your content to the Akamai network. When Akamai updates the CIDR blocks used for access, use Client Access Control to review the changes and send an acknowledgement to Akamai once you update your Access Control List.

Fetch the complete documentation index at: https://techdocs.akamai.com/client-access-control/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: Configurations
- [List CAC configurations](https://techdocs.akamai.com/client-access-control/reference/get-configurations.md): Lists all Client Access Control (CAC) configurations you can access.
- [Get a CAC configuration](https://techdocs.akamai.com/client-access-control/reference/get-configuration.md): Returns the Client Access Control (CAC) configuration for a specific `configurationId`.
- [Acknowledge proposed CIDR blocks](https://techdocs.akamai.com/client-access-control/reference/put-configuration-acknowledge-version.md): Acknowledges the change. Use it once you review the `proposedCidrs` from Akamai and update your Access Control List (ACL) accordingly.
