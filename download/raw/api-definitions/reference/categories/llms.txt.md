# API Definitions Documentation

> Akamai's API Definitions lets you register, manage, and deliver your APIs via Akamai in an efficient and secure manner.  Several products and features utilize API definitions, including: API Acceleration, API Discovery, API Gateway, Bot Manager, Kona Site Defender, and API protector with ASM module.

Fetch the complete documentation index at: https://techdocs.akamai.com/api-definitions/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: Categories
- [Create a category](https://techdocs.akamai.com/api-definitions/reference/post-category.md): Creates a category that you can use to tag endpoints. The request's `apiCategoryName` needs to be unique per account.
- [List categories](https://techdocs.akamai.com/api-definitions/reference/get-categories.md): Lists all categories available to tag endpoints and optionally indicates the number of endpoints tagged under each category.
- [Get a category](https://techdocs.akamai.com/api-definitions/reference/get-category.md): Returns a specific category that you can use to tag endpoints.
- [Edit a category](https://techdocs.akamai.com/api-definitions/reference/put-category.md): Updates a category's description or unique name.
- [Delete a category](https://techdocs.akamai.com/api-definitions/reference/delete-category.md): Removes an unassigned category. If you assigned the category to at least one endpoint, the operation returns a 403 error.
