---
updatedAt: 2025-09-05T18:35:17.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Accounts

Accounts are required for customers to make and receive payments and are created via the [Create Account](https://modulr.readme.io/reference/createaccount) endpoint.

The following information is required to create an account:

| Field              | Description                                       |
| :----------------- | :------------------------------------------------ |
| Customer ID        | The ID of the customer the account will belong to |
| External Reference | A reference for you to identify the account       |
| Currency           | The required currency for the account             |
| Product Code       | **See below**                                     |

Successful creation of an account will return a unique account ID along with the information required for paying funds into the account, for example the Sort Code & Account Number for GBP accounts or an IBAN for EUR accounts.

### Product Codes

Product codes control how an account is configured. Those available to you depend on your agreement with us and will be provided during onboarding.

Some dummy examples showing their usage:

| Example Product Code | Example Usage                                                    |
| :------------------- | :--------------------------------------------------------------- |
| GBP-000001           | Connects GBP accounts to the UK payment schemes                  |
| EUR-000001           | Connects EUR accounts to SEPA and ensures a GB IBAN is assigned  |
| EUR-000002           | Connects EUR accounts to SEPA and ensures an NL IBAN is assigned |
| EUR-000003           | Connects EUR accounts to SEPA and ensures an IE IBAN is assigned |
| EUR-000004           | Connects EUR accounts to SEPA and ensures an ES IBAN is assigned |
| EUR-000005           | Connects EUR accounts to SEPA and ensures an FR IBAN is assigned |