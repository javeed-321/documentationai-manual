# API Keys and Traffic Management Documentation

> Akamai's API Keys and Traffic Management lets you create and manage API keys that serve as unique identifiers for API consumers. API keys exist inside top-level units called key collections. At the key collection level, you can set a quota limit for the number of successful requests that individual API clients can make. You can also edit access control lists (ACLs) associated with your API endpoints and resources. Together with the API Endpoint Definition API, you can use this API to programmatically deploy your APIs on the Akamai network.

Fetch the complete documentation index at: https://techdocs.akamai.com/key-traffic-mgmt/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: Key collections
- [Create a key collection](https://techdocs.akamai.com/key-traffic-mgmt/reference/post-collection.md): Creates an empty collection under the selected contract and group.
- [List key collections](https://techdocs.akamai.com/key-traffic-mgmt/reference/get-collections.md): Returns information about all collections available for the current contract and group.
- [Get a key collection](https://techdocs.akamai.com/key-traffic-mgmt/reference/get-collection.md): Returns information about a collection.
- [Edit a key collection](https://techdocs.akamai.com/key-traffic-mgmt/reference/put-collection.md): Updates a collection.
- [Delete a key collection](https://techdocs.akamai.com/key-traffic-mgmt/reference/delete-collection.md): Deletes a collection and any keys the collection includes that aren't assigned to other collections.
- [Get an ACL](https://techdocs.akamai.com/key-traffic-mgmt/reference/get-collection-acl-entries.md): Returns the access control list of a collection.
- [Edit an ACL](https://techdocs.akamai.com/key-traffic-mgmt/reference/put-collection-acl-entries.md): Updates the access control list of a collection by adding or removing endpoint, resource, and HTTP method information from the ACL.
- [List collection endpoints](https://techdocs.akamai.com/key-traffic-mgmt/reference/get-collection-endpoints.md): Lists all endpoints assigned to the contract and group where you created the collection. The [API Endpoints API](https://techdocs.akamai.com/api-gateway/reference/api) manages this operation's response data format.
- [Import keys](https://techdocs.akamai.com/key-traffic-mgmt/reference/post-collection-import-keys.md): Imports keys from a CSV, XML, or JSON file to a collection. When making a request to import keys, embed the data structure that defines the contents of the import file in a JSON object. See the [examples of the files](doc:key-op#import-keys).
- [Returns collection keys in JSON, XML or CSV format](https://techdocs.akamai.com/key-traffic-mgmt/reference/get-export-collection-keys.md): Returns information about all collection keys in the JSON, XML or CSV format.
- [Get quota settings](https://techdocs.akamai.com/key-traffic-mgmt/reference/get-collection-quota-config.md): Returns information about the quota settings in a collection.
- [Edit quota settings](https://techdocs.akamai.com/key-traffic-mgmt/reference/put-collection-quota-config.md): Updates the quota settings in a collection.
- [Reset collection key quota](https://techdocs.akamai.com/key-traffic-mgmt/reference/post-collections-quota-reset.md): Resets the quota limit for selected keys in this particular collection.
