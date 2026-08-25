# API Keys and Traffic Management Documentation

> Akamai's API Keys and Traffic Management lets you create and manage API keys that serve as unique identifiers for API consumers. API keys exist inside top-level units called key collections. At the key collection level, you can set a quota limit for the number of successful requests that individual API clients can make. You can also edit access control lists (ACLs) associated with your API endpoints and resources. Together with the API Endpoint Definition API, you can use this API to programmatically deploy your APIs on the Akamai network.

Fetch the complete documentation index at: https://techdocs.akamai.com/key-traffic-mgmt/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: Keys
- [Create keys](https://techdocs.akamai.com/key-traffic-mgmt/reference/post-keys.md): Creates a collection of keys with unassigned values. To generate keys with assigned values, use the [Generate keys](ref:post-keys-generate) operation.
- [List keys](https://techdocs.akamai.com/key-traffic-mgmt/reference/get-keys.md): Returns keys included in a collection based on the specified criteria.
- [Assign keys](https://techdocs.akamai.com/key-traffic-mgmt/reference/post-keys-assign.md): Assigns keys to collections.
- [Export keys](https://techdocs.akamai.com/key-traffic-mgmt/reference/get-export-keys.md): Returns information about all available keys in the JSON, XML, or CSV format.
- [Generate keys](https://techdocs.akamai.com/key-traffic-mgmt/reference/post-keys-generate.md): Creates a collection of keys with assigned values. To create keys and assign your own values, use the [Create keys](ref:post-keys) operation.
- [Move keys](https://techdocs.akamai.com/key-traffic-mgmt/reference/post-keys-move.md): "Moves keys from one collection to another, either an existing one or a new one. If you specify a `destinationCollectionId` in the request, the operation moves the keys to the existing collection. \n"
- [Restore revoked keys](https://techdocs.akamai.com/key-traffic-mgmt/reference/post-keys-restore.md): Restores previously revoked keys in a collection. This operation is only available in the 120 days following the revocation.
- [Revoke keys](https://techdocs.akamai.com/key-traffic-mgmt/reference/post-keys-revoke.md): Revokes keys in a collection and marks them as revoked. You can restore the revoked keys within the next 120 days, after which they're deleted.
- [Unassign keys](https://techdocs.akamai.com/key-traffic-mgmt/reference/post-keys-unassign.md): Unassigns keys from collections.
- [Get a key](https://techdocs.akamai.com/key-traffic-mgmt/reference/get-key.md): Returns information about a key.
- [Edit a key](https://techdocs.akamai.com/key-traffic-mgmt/reference/put-key.md): Updates information about a key.
- [Reset key quota](https://techdocs.akamai.com/key-traffic-mgmt/reference/post-keys-quota-reset.md): Resets the quota limit for selected keys.
