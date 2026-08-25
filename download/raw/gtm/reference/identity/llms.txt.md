# Global Traffic Management Documentation

> Akamai's Global Traffic Management (GTM) helps Internet users access your website or IP applications with greater reliability. It applies an Internet-centric approach to global load balancing to increase site availability and responsiveness to online user requests. Unlike traditional hardware-based solutions that reside within data centers, the fault-tolerant Global Traffic Management service makes intelligent routing decisions. These are based on real-time data center performance health and on global Internet conditions. They transport user requests to the appropriate data center based on the best Internet route for that user at that moment.

Fetch the complete documentation index at: https://techdocs.akamai.com/gtm/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: Identity
- [Get identity](https://techdocs.akamai.com/gtm/reference/get-identity.md): This operation returns information about the API client. Run this operation for details on the API client contract such as available load balancing `features` and `permissions` the client has on the domains tied to the contract.
- [List contracts](https://techdocs.akamai.com/gtm/reference/get-identity-contracts.md): This operation returns a list of API client `contracts`. When you [Create a domain](ref:post-domain), you may need a `contractId` under certain circumstances. Run this operation to view available values.
- [List groups](https://techdocs.akamai.com/gtm/reference/get-identity-groups.md): This operation returns a list of API client `groups` and their parameters.  When you [Create a domain](ref:post-domain), you may need a `groupId` under certain circumstances. Run this operation to view available values.
