# Edge DNS Documentation

> Edge DNS is a cloud-based DNS solution that provides 24/7 DNS availability, improves DNS responsiveness, and has the resilience to defend against the largest DDoS attacks. Built on a globally distributed Anycast network, it can be implemented as a primary or secondary DNS service, replacing or augmenting existing DNS infrastructure as needed.

Fetch the complete documentation index at: https://techdocs.akamai.com/edge-dns/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: Zones
- [Get a zone's DNSSEC status](https://techdocs.akamai.com/edge-dns/reference/post-zones-dns-sec-status.md): Returns the current DNSSEC status for one or more zones.
- [Get a zone's DNSSEC DNSKEY records](https://techdocs.akamai.com/edge-dns/reference/get-zone-dnskeys.md): Get the current DNSSEC DNSKEY records for a zone.
- [Get matching DS record key tags](https://techdocs.akamai.com/edge-dns/reference/get-zones-zone-matching-ds-record-key-tags.md): Returns the key tag values from DS records in the parent zone that match the zone's current DNSKEY records. Use this to verify DS delegation is correctly configured.
- [Get secondary zones transfer status](https://techdocs.akamai.com/edge-dns/reference/post-zones-zone-transfer-status.md): Returns the results of the most recent zone transfer attempts for one or more zones.  When you configure a `SECONDARY` zone, several Akamai name servers known as zone transfer agents perform zone transfer requests to fetch the record data from the zone's configured master name servers. The data returned by this operation describes the results of those zone transfers.
- [Get a zone's contract](https://techdocs.akamai.com/edge-dns/reference/get-zone-contract.md): Show data about the contract to which this zone belongs.
- [Create a zone](https://techdocs.akamai.com/edge-dns/reference/post-zone.md): Creates a new zone. Carefully review the documentation for which fields are relevant to the type of zone you're creating.
- [List zones](https://techdocs.akamai.com/edge-dns/reference/get-zones.md): All zones that the current user has access to manage. The response is [paginated](ref:use-pagination).
- [Bulk edit secondary zones](https://techdocs.akamai.com/edge-dns/reference/post-zones-edit-secondary-zones.md): Updates settings for one or more secondary zones in a single operation.
- [Get zone propagation status](https://techdocs.akamai.com/edge-dns/reference/post-zones-propagation-status.md): Returns the current propagation status for one or more zones, showing what percentage of name servers have received the latest zone data.
- [Get a zone's settings](https://techdocs.akamai.com/edge-dns/reference/get-zone.md): Retrieves the metadata for this zone. Does not include record sets.
- [Update a zone's settings](https://techdocs.akamai.com/edge-dns/reference/put-zone.md): Modifies a zone's settings. You can't change the zone `type` with this operation.
- [Get a zone's aliases](https://techdocs.akamai.com/edge-dns/reference/get-zone-aliases.md): Show all zones that alias to this zone.
- [Schedule an immediate zone transfer](https://techdocs.akamai.com/edge-dns/reference/put-zones-zone-schedule-immediate-transfer.md): Schedules an immediate zone transfer for the specified secondary zone, bypassing any pending transfer delays.
