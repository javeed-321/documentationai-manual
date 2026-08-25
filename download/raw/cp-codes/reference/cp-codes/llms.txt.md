# CP Codes and Reporting Groups Tool Documentation

> Akamai's CP Codes and Reporting Groups tool lets you create, edit, view, and delete reporting groups. You can get access to detailed information about CP codes, edit their parameters, and group them for billing purposes.

Fetch the complete documentation index at: https://techdocs.akamai.com/cp-codes/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: CP Codes
- [List CP codes](https://techdocs.akamai.com/cp-codes/reference/get-cpcodes.md): Lists detailed information about CP codes available within your account and contract.
- [Get a CP code](https://techdocs.akamai.com/cp-codes/reference/get-cpcode.md): Get detailed information about a specific CP code. The details include the CP code type, name, time zone, as well as the account, contracts, and products it's assigned to. This operation also lists the access control group the CP code belongs to.
- [Update a CP code](https://techdocs.akamai.com/cp-codes/reference/put-cpcode.md): Modifies a specific CP code. After running the [GET a CP code](ref:get-cpcode) operation, use the response to build a request body. You can only modify a CP code's name, time zone, and purgeable member.
- [Get a water-mark limit](https://techdocs.akamai.com/cp-codes/reference/get-cpcodes-watermark-limits.md): Get a watermark limit for CP codes for the account associated within a specific contract. For more details, see [Rate and resource limiting](ref:rate-and-resource-limiting).
