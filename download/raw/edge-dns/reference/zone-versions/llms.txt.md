# Edge DNS Documentation

> Edge DNS is a cloud-based DNS solution that provides 24/7 DNS availability, improves DNS responsiveness, and has the resilience to defend against the largest DDoS attacks. Built on a globally distributed Anycast network, it can be implemented as a primary or secondary DNS service, replacing or augmenting existing DNS infrastructure as needed.

Fetch the complete documentation index at: https://techdocs.akamai.com/edge-dns/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: Zone versions
- [List a zone's versions](https://techdocs.akamai.com/edge-dns/reference/get-zone-versions.md): Shows the settings for current and prior versions of this Zone, in reverse chronological order of modification. Many versions in this list may look very similar because a new version is created every time the zone's settings or record sets are changed. This operation is [paginated](ref:use-pagination).
- [Show zone version differences](https://techdocs.akamai.com/edge-dns/reference/get-zone-versions-diff.md): Displays the difference between any two versions of a zone, as specified in the query parameters.
- [Get a zone version](https://techdocs.akamai.com/edge-dns/reference/get-zone-versions-uuid.md): Returns an image of the Zone from a previous version. Shows only zone settings, not record sets.
- [Get a version's record sets](https://techdocs.akamai.com/edge-dns/reference/get-zone-versions-recordsets.md): Lists all record sets for this zone. It works only for `PRIMARY` and `SECONDARY` zones. This operation [paginates](ref:use-pagination).
- [Reactivate a version](https://techdocs.akamai.com/edge-dns/reference/post-zones-zone-versions-uuid-recordsets-activate.md): Creates and activates a new version of the zone by copying the record sets from a prior version of this zone and reapplying them to the current version. The new version has a new, auto-incremented SOA serial number, and the zone's modification data is set to the current time and user. All other zone settings remain the same as the current version.
- [Get a version's master zone file](https://techdocs.akamai.com/edge-dns/reference/get-zones-zone-versions-uuid-zone-file.md): Downloads the record sets from a prior zone version in [master zone file](ref:get-zone-versions-uuid) format. This applies to primary and secondary zones.
