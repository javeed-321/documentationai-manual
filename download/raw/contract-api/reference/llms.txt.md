# Contract API Documentation

> The Contract API provides information about Akamai contracts as well as the products included in those contracts. With this API, you have the option of retrieving product information for a specified time frame by either contract ID or reporting group.

Fetch the complete documentation index at: https://techdocs.akamai.com/contract-api/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: API

- [API index](https://techdocs.akamai.com/contract-api/reference/api/llms.txt): full category index
- [Contract API](https://techdocs.akamai.com/contract-api/reference/api.md)
- [API summary](https://techdocs.akamai.com/contract-api/reference/api-summary.md)
- [Get started](https://techdocs.akamai.com/contract-api/reference/api-get-started.md)
- [API concepts](https://techdocs.akamai.com/contract-api/reference/concepts.md)
- [Rate limits](https://techdocs.akamai.com/contract-api/reference/rate-limits.md)
- [API workflow](https://techdocs.akamai.com/contract-api/reference/workflow.md)
- [Errors](https://techdocs.akamai.com/contract-api/reference/api-errors.md)
- [400](https://techdocs.akamai.com/contract-api/reference/400.md)
- [401](https://techdocs.akamai.com/contract-api/reference/401.md)
- [403](https://techdocs.akamai.com/contract-api/reference/403.md)
- [404](https://techdocs.akamai.com/contract-api/reference/404.md)

## API Reference: Contracts

- [Contracts index](https://techdocs.akamai.com/contract-api/reference/contracts/llms.txt): full category index
- [List contracts](https://techdocs.akamai.com/contract-api/reference/get-contract-ids.md): Get the list of contracts that a user has access to.
- [List products per contract](https://techdocs.akamai.com/contract-api/reference/get-contract-product-summaries.md): Get the IDs and names of the products associated with a contract for the time frame selected.

## API Reference: Reporting groups

- [Reporting groups index](https://techdocs.akamai.com/contract-api/reference/reporting-groups/llms.txt): full category index
- [List CP code reporting groups](https://techdocs.akamai.com/contract-api/reference/get-reporting-groups.md): Get the IDs of the Content Provider (CP) reporting groups that you have access to along with their names. To run this operation, your user account needs the CPCode Rep Group role. To add this role, use the [Identity and Access Management application](https://control.akamai.com/admin/?tab=CONFIGURE&type=context).
- [List CP code reporting group IDs](https://techdocs.akamai.com/contract-api/reference/get-group-ids.md): Get the IDs of the Content Provider (CP) reporting groups that you have access to. To run this operation, your user account needs the CPCode Rep Group role. To add this role, use the [Identity and Access Management application](https://control.akamai.com/admin/?tab=CONFIGURE&type=context).
- [List products per reporting group](https://techdocs.akamai.com/contract-api/reference/get-group-products-summaries.md): Get the IDs and names of the products associated with the reporting group for the time frame selected. To run this operation, your user account needs the CPCode Rep Group role. To add this role, use the [Identity and Access Management application](https://control.akamai.com/admin/?tab=CONFIGURE&type=context). When a request is successful, it may return either a 200 or a 300 response. The API returns a 200 (OK) response when the CP code reporting group is associated with only one contract. You'll receive a `300 Multiple Choices` response when the request returns a list of matching contracts because the CP code reporting group is associated with multiple contracts. To retrieve product information when you receive a 300 response code, make a new GET request to the hyperlinks provided in the response.
