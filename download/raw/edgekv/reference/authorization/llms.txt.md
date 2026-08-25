# EdgeKV Documentation

> Akamai's EdgeKV is a key-value store database at the edge. It enables you to build data-driven EdgeWorker applications that require fast, frequent reads and infrequent writes.

Fetch the complete documentation index at: https://techdocs.akamai.com/edgekv/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: Authorization
- [List permission groups](https://techdocs.akamai.com/edgekv/reference/get-groups.md): View a list of access groups and your associated permission capabilities, such as create a namespace or read data from a namespace.
- [Get a permission group](https://techdocs.akamai.com/edgekv/reference/get-group.md): View details permissions available within the specified access group, such as create a namespace or read data from a namespace.
- [Modify the default data access policy](https://techdocs.akamai.com/edgekv/reference/put-auth-database.md): Modify the default `dataAccessPolicy` setting that applies to new namespaces. The `restrictDataAccess` is `true` by default, and `allowNamespacePolicyOverride` is `false`.
- [Reauthorize a namespace](https://techdocs.akamai.com/edgekv/reference/reauthorize-namespace.md): Assign an existing namespace to a different Akamai access group.
