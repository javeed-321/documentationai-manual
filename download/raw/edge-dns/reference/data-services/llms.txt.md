# Edge DNS Documentation

> Edge DNS is a cloud-based DNS solution that provides 24/7 DNS availability, improves DNS responsiveness, and has the resilience to defend against the largest DDoS attacks. Built on a globally distributed Anycast network, it can be implemented as a primary or secondary DNS service, replacing or augmenting existing DNS infrastructure as needed.

Fetch the complete documentation index at: https://techdocs.akamai.com/edge-dns/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: Data services
- [List authoritative name servers](https://techdocs.akamai.com/edge-dns/reference/get-data-authorities.md): Retrieves the currently assigned Akamai authoritative name servers for one or more contracts.
- [List contracts](https://techdocs.akamai.com/edge-dns/reference/get-data-contracts.md): Lists the contracts accessible to the current user. Each contract includes the features and permissions that are available to you on that contract.
- [List DNSSEC algorithms](https://techdocs.akamai.com/edge-dns/reference/get-data-dns-sec-algorithms.md): Retrieves DNSSEC algorithm names.
- [List edge hostnames](https://techdocs.akamai.com/edge-dns/reference/get-data-edgehostnames.md): Displays Edge hostnames that have been configured for the current customer.
- [List groups](https://techdocs.akamai.com/edge-dns/reference/get-data-groups.md): Lists the groups accessible to the current user. Each group includes the contracts related to that group, as well as your permissions of `READ`, `WRITE`, `ADD`, or `DELETE` zone on that group.
- [List TSIG key algorithms](https://techdocs.akamai.com/edge-dns/reference/get-data-tsig-algorithms.md): Retrieves TSIG algorithm names.
- [List record types](https://techdocs.akamai.com/edge-dns/reference/get-record-set-types.md): Retrieves record types you can add to the requested zone. Record types depend on both the zone type and the available contract features.
