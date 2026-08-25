---
updatedAt: 2025-09-30T09:33:00.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Fundamentals

Improving your integration to Modulr

## Modulr API

Modulr is an API first company and all data is available from Modulr API calls for 6 months. Therefore, we recommend that you store all available data from our API responses and Webhooks. Please refer to our [Developer Centre](https://modulr.readme.io/) for full details. For details about access via the Modulr Portal, please refer to our [Knowledge Hub](https://knowledge.modulrfinance.com/knowledge-hub). We strongly recommend that you test via our Sandbox because this will improve your integration as a whole and is free to use.

We will set you up either as a Partner or Direct client depending on your proposition and requirements from Modulr’s e-money and payment services with the appropriate permissions and functionality, securely identifying you via your connection. In simple terms:

* A Partner will be able to Create Customers, then Accounts, then Payments and/or Cards.
* A Direct will be able to Create Accounts, then Payments and/or Cards (there is no create customer functionality).

## Modulr References

These are Modulr specific alphanumeric references and essential items to store and when raising queries with Modulr. They are provided in the API responses to Create Customer, Create Account, etc and are needed for subsequent calls, e.g. the CustomerID is needed to create an account for that customer. They are often referred to with the starting letter and “Bid”, examples as follows:

* Customer (CBid) - Unique identifier for a Customer. Begins with 'C'
* Accounts (ABid)
* Payments (PBid)
* Transactions (TBid)
* Card (VBid)

## The Modulr Platform has a simple entity hierarchy

<Image align="center" className="border" border={true} src="https://files.readme.io/5506f39e0fa8311f917e43bb5c44335c2e3b3edfc59f08ad4870960387581a2d-image.png" />