# Edge DNS Documentation

> Edge DNS is a cloud-based DNS solution that provides 24/7 DNS availability, improves DNS responsiveness, and has the resilience to defend against the largest DDoS attacks. Built on a globally distributed Anycast network, it can be implemented as a primary or secondary DNS service, replacing or augmenting existing DNS infrastructure as needed.

Fetch the complete documentation index at: https://techdocs.akamai.com/edge-dns/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: API

- [API index](https://techdocs.akamai.com/edge-dns/reference/api/llms.txt): full category index
- [Edge DNS API v2](https://techdocs.akamai.com/edge-dns/reference/edge-dns-api.md)
- [API summary](https://techdocs.akamai.com/edge-dns/reference/api-summary.md)
- [Get started](https://techdocs.akamai.com/edge-dns/reference/get-started.md)
- [Use pagination](https://techdocs.akamai.com/edge-dns/reference/use-pagination.md)
- [Group IDs and access level](https://techdocs.akamai.com/edge-dns/reference/group-ids-access-level.md)
- [Supported DNS resource record types](https://techdocs.akamai.com/edge-dns/reference/supported-dns-resource-record-types.md)
- [Use change lists](https://techdocs.akamai.com/edge-dns/reference/use-change-lists.md)
- [Example: Create a new primary zone](https://techdocs.akamai.com/edge-dns/reference/example-create-new-primary-zone.md)
- [Zone create failure states](https://techdocs.akamai.com/edge-dns/reference/zone-create-failure-vals.md)
- [Subzone grants](https://techdocs.akamai.com/edge-dns/reference/subzone-grants.md)
- [Definitions of the activationState](https://techdocs.akamai.com/edge-dns/reference/activation-state-definitions.md)
- [Edge DNS API Troubleshooting](https://techdocs.akamai.com/edge-dns/reference/edns-api-troubleshooting.md)
- [Errors](https://techdocs.akamai.com/edge-dns/reference/api-errors.md)
- [304](https://techdocs.akamai.com/edge-dns/reference/304.md)
- [400](https://techdocs.akamai.com/edge-dns/reference/400.md): Bad request
- [401](https://techdocs.akamai.com/edge-dns/reference/401.md): API authentication error
- [403](https://techdocs.akamai.com/edge-dns/reference/403.md): Forbidden
- [404](https://techdocs.akamai.com/edge-dns/reference/404.md): Not found
- [405](https://techdocs.akamai.com/edge-dns/reference/405.md): Method Not Allowed
- [409](https://techdocs.akamai.com/edge-dns/reference/409.md): Conflict
- [415](https://techdocs.akamai.com/edge-dns/reference/415.md): Unsupported Media Type
- [503](https://techdocs.akamai.com/edge-dns/reference/503.md): Service Unavailable

## API Reference: Zones

- [Zones index](https://techdocs.akamai.com/edge-dns/reference/zones/llms.txt): full category index
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

## API Reference: Zone versions

- [Zone versions index](https://techdocs.akamai.com/edge-dns/reference/zone-versions/llms.txt): full category index
- [List a zone's versions](https://techdocs.akamai.com/edge-dns/reference/get-zone-versions.md): Shows the settings for current and prior versions of this Zone, in reverse chronological order of modification. Many versions in this list may look very similar because a new version is created every time the zone's settings or record sets are changed. This operation is [paginated](ref:use-pagination).
- [Show zone version differences](https://techdocs.akamai.com/edge-dns/reference/get-zone-versions-diff.md): Displays the difference between any two versions of a zone, as specified in the query parameters.
- [Get a zone version](https://techdocs.akamai.com/edge-dns/reference/get-zone-versions-uuid.md): Returns an image of the Zone from a previous version. Shows only zone settings, not record sets.
- [Get a version's record sets](https://techdocs.akamai.com/edge-dns/reference/get-zone-versions-recordsets.md): Lists all record sets for this zone. It works only for `PRIMARY` and `SECONDARY` zones. This operation [paginates](ref:use-pagination).
- [Reactivate a version](https://techdocs.akamai.com/edge-dns/reference/post-zones-zone-versions-uuid-recordsets-activate.md): Creates and activates a new version of the zone by copying the record sets from a prior version of this zone and reapplying them to the current version. The new version has a new, auto-incremented SOA serial number, and the zone's modification data is set to the current time and user. All other zone settings remain the same as the current version.
- [Get a version's master zone file](https://techdocs.akamai.com/edge-dns/reference/get-zones-zone-versions-uuid-zone-file.md): Downloads the record sets from a prior zone version in [master zone file](ref:get-zone-versions-uuid) format. This applies to primary and secondary zones.

## API Reference: Change lists

- [Change lists index](https://techdocs.akamai.com/edge-dns/reference/change-lists/llms.txt): full category index
- [Create a change list](https://techdocs.akamai.com/edge-dns/reference/post-changelists.md): Creates a new change list based on the most recent version of a zone. No POST body is needed, since the object is read-only.
- [List user's change lists](https://techdocs.akamai.com/edge-dns/reference/get-changelists.md): Retrieves the change lists that you created. Otherwise, displays both stale change lists and change lists for zones you can no longer access.
- [Search for change lists](https://techdocs.akamai.com/edge-dns/reference/post-changelists-search.md): Retrieves the change lists that you've created for the specified zone names. If the input list is empty, the response doesn't return any change lists. Note that it's possible to own a change list on a zone that you're no longer allowed to access.
- [Get a change list](https://techdocs.akamai.com/edge-dns/reference/get-changelists-zone.md): Describes a change list, showing its base zone version, last modified time, and current change tag.
- [Delete a change list](https://techdocs.akamai.com/edge-dns/reference/delete-changelists-zone.md): Removes an unneeded change list.
- [Show changes](https://techdocs.akamai.com/edge-dns/reference/get-changelists-zone-diff.md): Show [differences](ref:get-zone-versions-diff) between this change list and its base version.
- [List record set names for a change list](https://techdocs.akamai.com/edge-dns/reference/get-changelists-zone-names.md): Retrieves existing record names on this zone, based on the change list. If a record is deleted in the change list, it doesn't appear on the records returned. If no record sets exist within the change list, this operation returns an empty list.
- [Submit a change list](https://techdocs.akamai.com/edge-dns/reference/post-changelists-zone-submit.md): Applies all of the changes in this change list to the current zone. This operation fails if the change list has become stale.
- [Get change list settings](https://techdocs.akamai.com/edge-dns/reference/get-changelists-zone-settings.md): Retrieves the zone's settings based on the selected change list. Zone settings include metadata about the zone, but not the record sets. The data returned reflects the zone setting changes included in the change list. This call works even if the change list is stale.
- [Update change list settings](https://techdocs.akamai.com/edge-dns/reference/put-changelists-zone-settings.md): Updates the change list with new Zone settings. The entire Zone object is needed no matter how many fields you're updating.
- [List record set types for name and change list](https://techdocs.akamai.com/edge-dns/reference/get-changelists-zone-names-name-types.md): Retrieves existing record set types for a given name based on the selected change list. The record sets returned reflect the changes added to the change list. Records deleted in this change list don't appear. If the name doesn't exist within the change list, returns an empty list.
- [Get a record set for a change list](https://techdocs.akamai.com/edge-dns/reference/get-changelists-zone-names-name-types-type.md): Returns an individual record set based on the selected change list. The record sets returned reflects any changes added to this change list. Record sets are annotated with the related change as clean, modified, new, or deleted. This call works even if the change list is stale.
- [Upload a master zone file to a change list](https://techdocs.akamai.com/edge-dns/reference/post-changelists-zone-recordsets.md): Replaces your change list's record sets with the contents of a master zone file.
- [List record sets for a change list](https://techdocs.akamai.com/edge-dns/reference/get-changelists-zone-recordsets.md): Retrieves the current record sets based on the selected change list. The record sets returned reflect any Changes added to this change list. This call works even if the change list is stale. This operation is (paginated](ref:use-pagination).
- [Modify record set for a change list](https://techdocs.akamai.com/edge-dns/reference/post-changelists-zone-recordsets-add-change.md): Adds a record set change to this change list. Each change is an operation that affects a single record set: `ADD`, `EDIT`, or `DELETE`.

## API Reference: Data services

- [Data services index](https://techdocs.akamai.com/edge-dns/reference/data-services/llms.txt): full category index
- [List authoritative name servers](https://techdocs.akamai.com/edge-dns/reference/get-data-authorities.md): Retrieves the currently assigned Akamai authoritative name servers for one or more contracts.
- [List contracts](https://techdocs.akamai.com/edge-dns/reference/get-data-contracts.md): Lists the contracts accessible to the current user. Each contract includes the features and permissions that are available to you on that contract.
- [List DNSSEC algorithms](https://techdocs.akamai.com/edge-dns/reference/get-data-dns-sec-algorithms.md): Retrieves DNSSEC algorithm names.
- [List edge hostnames](https://techdocs.akamai.com/edge-dns/reference/get-data-edgehostnames.md): Displays Edge hostnames that have been configured for the current customer.
- [List groups](https://techdocs.akamai.com/edge-dns/reference/get-data-groups.md): Lists the groups accessible to the current user. Each group includes the contracts related to that group, as well as your permissions of `READ`, `WRITE`, `ADD`, or `DELETE` zone on that group.
- [List TSIG key algorithms](https://techdocs.akamai.com/edge-dns/reference/get-data-tsig-algorithms.md): Retrieves TSIG algorithm names.
- [List record types](https://techdocs.akamai.com/edge-dns/reference/get-record-set-types.md): Retrieves record types you can add to the requested zone. Record types depend on both the zone type and the available contract features.

## API Reference: Bulk zones

- [Bulk zones index](https://techdocs.akamai.com/edge-dns/reference/bulk-zones/llms.txt): full category index
- [Submit a bulk zone create request](https://techdocs.akamai.com/edge-dns/reference/post-zones-create-requests.md): Submits a request to create one or more new Zones asynchronously. The request body contains a JSON array. Each object in the array contains the data necessary to create a zone. All zones are created on the same contract and group.  An offline task creates the new zones. You can use the response's `requestId` to check the task's status and view its results once it completes.
- [Check bulk zone create status](https://techdocs.akamai.com/edge-dns/reference/get-zones-create-requests-requestid.md): Retrieves the current status of a running or completed request. The `requestId` was returned when the create request was initiated.
- [Get bulk zone create results](https://techdocs.akamai.com/edge-dns/reference/get-zones-create-requests-requestid-result.md): Retrieves the results from a completed request.
- [Search bulk zone convert requests](https://techdocs.akamai.com/edge-dns/reference/get-zones-convert-requests.md): Search convert requests.
- [Submit a bulk zone convert alias request](https://techdocs.akamai.com/edge-dns/reference/post-zones-convert-alias-requests.md): Submits a request to convert one or more zones to alias asynchronously. The request body contains a JSON array. Each object in the array contains the data necessary to convert to an alias zone. All zones are converted on the same contract and group.  An offline task converts the zones. You can use the response's `requestId` to check the task's status and view its results once it completes.
- [Submit a bulk zone convert primary request](https://techdocs.akamai.com/edge-dns/reference/post-zones-convert-primary-requests.md): Submits an asynchronous request to convert one or more DNS zones to primary. The request body must be a JSON array, where each object provides the required data for converting a zone. All zones included in the request must belong to the same contract and group. The conversion is performed as an offline task. Use the requestId returned in the response to track the task’s progress and retrieve the results upon completion.
- [Submit a bulk zone convert secondary request](https://techdocs.akamai.com/edge-dns/reference/post-zones-convert-secondary-requests.md): Submits an asynchronous request to convert one or more DNS zones to secondary. The request body must be a JSON array, with each object containing the required data for the conversion. All zones must belong to the same contract and group. The conversion is handled by an offline task. Use the `requestId` returned in the response to monitor the task's progress and retrieve the results when complete.
- [List SOA serials for secondary zones](https://techdocs.akamai.com/edge-dns/reference/post-zones-convert-serials-requests.md): Submits a request to retrieve SOA serial numbers for secondary zones only. If a serial number cannot be retrieved from the back end for a given zone, the corresponding zone/soaSerialLock object will be omitted from the response list.
- [Check bulk zone convert status](https://techdocs.akamai.com/edge-dns/reference/get-zones-convert-requests-requestid.md): Retrieves the current status of a running or completed zone conversion request. The `requestId` is returned when the conversion request is initiated.
- [Get bulk zone convert results](https://techdocs.akamai.com/edge-dns/reference/get-zones-convert-requests-requestid-result.md): Retrieves the results from a completed request.
- [Submit a bulk zone delete request](https://techdocs.akamai.com/edge-dns/reference/post-zones-delete-requests.md): Submits a request to delete one or more new Zones asynchronously. The request body contains a JSON array. Each element in the array is the name of a zone to be deleted.  Before deleting a zone from the Edge DNS system, the API makes sure Akamai servers aren't receiving DNS requests for that zone. It also checks that the zone isn't currently delegated to Akamai's name servers.  An offline task deletes the new zones. The result of this operation is a `requestId`, which you can use to check the task's status and view its results once it completes.
- [Check bulk zone delete status](https://techdocs.akamai.com/edge-dns/reference/get-zones-delete-requests-requestid.md): Retrieves the current status of a running or completed request. The `requestId` was returned when the delete request was initiated.
- [Get bulk zone delete results](https://techdocs.akamai.com/edge-dns/reference/get-zones-delete-requests-requestid-result.md): Retrieves the `results` from a completed request.

## API Reference: TSIG keys

- [TSIG keys index](https://techdocs.akamai.com/edge-dns/reference/tsig-keys/llms.txt): full category index
- [List TSIG keys](https://techdocs.akamai.com/edge-dns/reference/get-keys.md): Get the TSIG keys used by zones that you're allowed to manage.
- [Update a TSIG key across zones](https://techdocs.akamai.com/edge-dns/reference/post-keys-bulk-update.md): This updates the key data for multiple zones at once. Keep in mind that this operation can only add zones to a TSIG key, not remove them. To safely remove the association between a zone and a TSIG key, update the zone to its new TSIG key or remove the key from the zone if you're sure it's no longer needed.
- [List zones using TSIG key](https://techdocs.akamai.com/edge-dns/reference/post-keys-used-by.md): Returns zone names that use the given TSIG key and for which the current user has READ access. If the zones returned is empty, it's possible that the given key is in use by other zones but the current user doesn't have permission to view those zones.
- [Zones to contract using TSIG key](https://techdocs.akamai.com/edge-dns/reference/post-keys-used-by-zone-contract-map.md): Zone names within a contract that use the given TSIG key for which the current user has READ access. If the list returned is empty, it's possible that the given key is in use by other zones but the current user doesn't have permission to view those zones.
- [Get a zone's TSIG key](https://techdocs.akamai.com/edge-dns/reference/get-zones-zone-key.md): Retrieves the TSIG Key data for this zone. Includes a count of zones that use this key. Returns a 404 error if the zone doesn't have a TSIG key.
- [Update a zone's TSIG key](https://techdocs.akamai.com/edge-dns/reference/put-zones-zone-key.md): Creates or replaces the current TSIG Key for this zone. If other zones use the same key, doesn't modify those zones.
- [Delete a zone's TSIG key](https://techdocs.akamai.com/edge-dns/reference/delete-zones-zone-key.md): Removes the TSIG Key for this zone. This action doesn't affect any other zone, even if they share the same TSIG key as this zone. If the zone doesn't currently have a key, no actions are taken and no error is thrown.
- [List users of a zone's TSIG key](https://techdocs.akamai.com/edge-dns/reference/get-zones-zone-key-used-by.md): Lists the Zones that use the same TSIG key as this zone.

## API Reference: Shield NS53

- [Shield NS53 index](https://techdocs.akamai.com/edge-dns/reference/shield-ns53/llms.txt): full category index
- [Create a proxy](https://techdocs.akamai.com/edge-dns/reference/post-proxy.md): Creates a new proxy.
- [List proxies](https://techdocs.akamai.com/edge-dns/reference/get-proxy.md): Get all proxies that the current user has access to manage.
- [List valid proxy health check record set types](https://techdocs.akamai.com/edge-dns/reference/get-proxy-healthcheck-recordset-types.md): Lists the valid proxy health check record set types.
- [Get a proxy](https://techdocs.akamai.com/edge-dns/reference/get-proxy-id.md): Get the proxy that the current user has access to manage.
- [Update a proxy](https://techdocs.akamai.com/edge-dns/reference/put-proxy.md): Updates the proxy.
- [Delete a proxy](https://techdocs.akamai.com/edge-dns/reference/delete-proxy.md): Delete the proxy as an asynchronous operation.  Your proxy will continue to show with a `DELETED` status and continue to count against your maximum proxy cap until permanently removed.
- [List proxy zones](https://techdocs.akamai.com/edge-dns/reference/get-proxy-zones.md): Get all proxy zones that the current user has access to manage.
- [List proxy zone keys](https://techdocs.akamai.com/edge-dns/reference/get-proxy-zone-keys.md): Get all proxy zones keys that the current user has access to manage.
- [Get a proxy zone by name](https://techdocs.akamai.com/edge-dns/reference/get-proxy-zones-name.md): Get a proxy zone that the current user has access to manage by proxy zone name.
- [Save the apex alias for a proxy zone](https://techdocs.akamai.com/edge-dns/reference/put-proxy-zone-apex-alias.md): Save the apex alias for a proxy zone.
- [Delete apex alias for a proxy zone](https://techdocs.akamai.com/edge-dns/reference/delete-proxy-zone-apex-alias.md): Delete the apex alias for a proxy zone.
- [Get a proxy zone TSIG key by name](https://techdocs.akamai.com/edge-dns/reference/get-proxy-zones-name-key.md): Get a TSIG key for a proxy zone that the current user has access to manage by proxy zone name.
- [Update a proxy zone TSIG key by name](https://techdocs.akamai.com/edge-dns/reference/put-proxy-zones-name-key.md): Update the proxy zone.
- [Delete a proxy zone TSIG key by name](https://techdocs.akamai.com/edge-dns/reference/delete-proxy-zones-name-key.md): Delete a TSIG key for a proxy zone that the current user has access to manage by proxy zone name.
- [List proxies for a TSIG key](https://techdocs.akamai.com/edge-dns/reference/get-proxies-key-used-by.md): List proxies that use a TSIG key.
- [Get a manual filter report](https://techdocs.akamai.com/edge-dns/reference/get-proxy-zone-manual-filter-report.md): Get manual filter report for a  proxy zone that the current user has access to manage.
- [Manage manual filter names](https://techdocs.akamai.com/edge-dns/reference/post-proxy-zone-manual-filter-names.md): Manage manual filter entries for a proxy zone that the current user has access to manage.
- [Initialize manual filter names with a zone file](https://techdocs.akamai.com/edge-dns/reference/post-proxy-zone-manual-filter-names-file.md): Initializes manual filter names for a proxy zone. Use [Manage manual filter names operation](ref:post-proxy-zone-manual-filter-names) to update a proxy zone.
- [Convert a proxy zone filter mode to all](https://techdocs.akamai.com/edge-dns/reference/post-proxy-zone-manual-filter-mode-convert-all.md): Converts a proxy zone filter mode to all.
- [Convert a proxy zone filter mode to automatic](https://techdocs.akamai.com/edge-dns/reference/post-proxy-zone-manual-filter-mode-convert-automatic.md): Converts a proxy zone filter mode to automatic.
- [Convert a proxy zone filter mode to manual](https://techdocs.akamai.com/edge-dns/reference/post-proxy-zone-manual-filter-mode-convert-manual.md): Converts a proxy zone filter mode to manual.
- [Convert a proxy zone filter mode to none](https://techdocs.akamai.com/edge-dns/reference/post-proxy-zone-manual-filter-mode-convert-none.md): Converts a proxy zone filter mode to none.
- [Run existing proxy health check](https://techdocs.akamai.com/edge-dns/reference/post-run-proxy-healthcheck.md): Runs the health check currently defined on the proxy.
- [Run proposed proxy health check for origin name servers](https://techdocs.akamai.com/edge-dns/reference/post-run-proposed-proxy-healthcheck.md): Runs a proposed health check on the proxy.
- [Submit a bulk proxy zone create request](https://techdocs.akamai.com/edge-dns/reference/post-proxy-zones-create-requests.md): Submits a request to create one or more new Proxy Zones asynchronously. The request body contains a JSON array. Each object in the array contains the data necessary to create a proxy zone. All proxy zones are created on the same contract and group.  An offline task creates the new proxy zones. You can use the response's `requestId` to check the task's status and view its results once it completes.
- [Get a bulk proxy zone create results for a proxy](https://techdocs.akamai.com/edge-dns/reference/get-proxy-zones-create-requests-result.md): Retrieves the results of requests for a given proxy.
- [Check bulk proxy zone create status](https://techdocs.akamai.com/edge-dns/reference/get-proxy-zones-create-requests-requestid.md): Retrieves the current status of a running or completed request. The `requestId` was returned when the create request was initiated.
- [Get a bulk proxy zone create result](https://techdocs.akamai.com/edge-dns/reference/get-proxy-zones-create-requests-requestid-result.md): Retrieves the results from a completed request.
- [Submit a bulk proxy zone delete request](https://techdocs.akamai.com/edge-dns/reference/post-proxy-zones-delete-requests.md): Submits a request to delete one or more proxy zones asynchronously. Each element in the response array is the name of a proxy zone to be deleted.  Before deleting a zone from the Edge DNS system, the API makes sure Akamai servers aren't receiving DNS requests for that proxy zone. It also checks that the proxy zone isn't currently delegated to Akamai's name servers.  An offline task deletes the proxy zones. The result of this operation is a `requestId`, which you can use to check the task's status and view its results once it completes.
- [Get all bulk proxy zone delete results](https://techdocs.akamai.com/edge-dns/reference/get-proxy-zones-delete-requests-result.md): Retrieves the results for all requests for a given proxy.
- [Check bulk proxy zone delete status](https://techdocs.akamai.com/edge-dns/reference/get-proxy-zones-delete-requests-requestid.md): Retrieves the current status of a running or completed request. The `requestId` was returned when the delete request was initiated.
- [Get a bulk proxy zone delete result](https://techdocs.akamai.com/edge-dns/reference/get-proxy-zones-delete-requests-requestid-result.md): Retrieves the result from a completed request.

## API Reference: Record sets

- [Record sets index](https://techdocs.akamai.com/edge-dns/reference/record-sets/llms.txt): full category index
- [List record set names for a zone](https://techdocs.akamai.com/edge-dns/reference/get-zone-names.md): Retrieves record set names for a zone.
- [Upload a master zone file](https://techdocs.akamai.com/edge-dns/reference/post-zones-zone-zone-file.md): Upload new record set data for this zone in master zone file format. Replaces any existing record sets. This operation applies to primary zones and secondary zones. See [RFC 1035](http://tools.ietf.org/html/rfc1035) section 5 and [RFC 1034](http://tools.ietf.org/html/rfc1034) section 3.6.1 for more information.  Zone files can contain only US-ASCII characters 0&ndash;127. Where allowed, you can encode high-order ASCII characters, 128+, with a backslash plus a three-digit decimal number representing the byte value. For example, `\233` instead of `&eacute;`.  `AKAMAICDN` and `AKAMAITLC` records can't be represented in this format. Uploading a zone file doesn't affect these records.
- [Get a master zone file](https://techdocs.akamai.com/edge-dns/reference/get-zones-zone-zone-file.md): Download this zone's record set data in master zone file format. Use the recipe below to get the master zone file. This operation applies to primary zones and secondary zones. See [RFC 1035](http://tools.ietf.org/html/rfc1035) section 5 and [RFC 1034](http://tools.ietf.org/html/rfc1034) section 3.6.1 for more information.  `AKAMAICDN` and `AKAMAITLC` records can't be represented in this format, so they're displayed as comment lines.
- [List record set types for name and zone](https://techdocs.akamai.com/edge-dns/reference/get-zone-name-types.md): Lists all *existing* record set types for this name. The types are available at [List record types](ref:get-record-set-types). If the name doesn't exist within the zone, an empty list is returned.
- [Create a record set](https://techdocs.akamai.com/edge-dns/reference/post-zones-zone-names-name-types-type.md): Creates a new Record set with the specified name and type.
- [Get a record set](https://techdocs.akamai.com/edge-dns/reference/get-zone-name-type.md): Retrieves a single record set for the zone, record name, and record type specified in the URL.
- [Replace a record set](https://techdocs.akamai.com/edge-dns/reference/put-zones-zone-names-name-types-type.md): Replaces an existing Record set with the request body. The `name` and `type` need to match the existing record.
- [Delete a record set](https://techdocs.akamai.com/edge-dns/reference/delete-zone-name-type.md): Removes an existing record set.
- [Create record sets](https://techdocs.akamai.com/edge-dns/reference/post-zones-zone-recordsets.md): Creates multiple new record sets on this Zone. If any record set fails to create, for example, because a record set with that name and type already exists, the entire operation fails.
- [Get a zone's record sets](https://techdocs.akamai.com/edge-dns/reference/get-zones-zone-recordsets.md): Lists all record sets for this Zone. It works only for `PRIMARY` and `SECONDARY` zones. This operation is [paginated](ref:use-pagination).
- [Replace record sets](https://techdocs.akamai.com/edge-dns/reference/put-zones-zone-recordsets.md): Replaces all record sets that currently exist with the list provided.
