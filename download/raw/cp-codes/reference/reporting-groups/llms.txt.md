# CP Codes and Reporting Groups Tool Documentation

> Akamai's CP Codes and Reporting Groups tool lets you create, edit, view, and delete reporting groups. You can get access to detailed information about CP codes, edit their parameters, and group them for billing purposes.

Fetch the complete documentation index at: https://techdocs.akamai.com/cp-codes/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: Reporting Groups
- [Create a reporting group](https://techdocs.akamai.com/cp-codes/reference/post-reporting-groups.md): Creates a reporting group. Make sure the reporting group's name is unique within an account. The `location` header in the response provides a relative path to the created reporting group.
- [List reporting groups](https://techdocs.akamai.com/cp-codes/reference/get-reporting-groups.md): Lists detailed information about reporting groups available for your account and contract.
- [Get a reporting group](https://techdocs.akamai.com/cp-codes/reference/get-reporting-group.md): Get detailed information about a specific reporting group. The details include the reporting group name and the access control group that it belongs to. This operations also lists the contracts and CP codes assigned to the reporting group.
- [Update a reporting group](https://techdocs.akamai.com/cp-codes/reference/put-reporting-group.md): Modifies a specific reporting group. You should only modify a reporting group's name and assigned CP codes.
- [Delete a reporting group](https://techdocs.akamai.com/cp-codes/reference/delete-reporting-group.md): Deletes a specific reporting group.
- [Get a water-mark limit for reporting groups](https://techdocs.akamai.com/cp-codes/reference/get-reporting-groups-watermark-limits.md): Get a watermark limit for CP reporting groups for the account associated within a specific contract. For more details, see [Rate and resource limiting](ref:rate-and-resource-limiting).
- [List products within a reporting group](https://techdocs.akamai.com/cp-codes/reference/get-reporting-group-products.md): Lists products and services assigned to a specific reporting group.
