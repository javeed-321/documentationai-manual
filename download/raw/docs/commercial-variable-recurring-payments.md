---
updatedAt: 2026-06-10T15:30:05.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Commercial Variable Recurring Payments

<br />

> 📘 Note
>
> Commercial VRP is available to customers who have been enabled for **Commercial VRP** on the Modulr platform. Please speak to your Modulr point of contact if you are unsure whether this applies to you.

Commercial Variable Recurring Payments (cVRP) allows you to set up recurring payments on behalf of your users that can vary in amount and frequency, all under a single consent. The user authenticates once, and subsequent payments can be initiated without them needing to re-authenticate with their bank each time, as long as payments remain within the agreed parameters of the consent.

> 📘 Terminology
>
> In these guides we use the term "bank" to generically refer to the organisation providing the payment account to the end user, also known as the "Account Servicing Payment Service Provider" (ASPSP). This includes non-banks such as e-money institutions and building societies.
>
> We use the term "consent" to refer to the VRP parameters that a user authenticates, under which cVRP payments are subsequently made.

## Is cVRP right for your use case?

cVRP is designed for **Me-to-them** payments, where the payer and the recipient are different people or businesses.

Currently eligible use cases include:

* Subscription or recurring billing for utility providers (e.g. electricity bills)
* Regulated financial services payments for account eligible for FSCS-protection, mortgage providers, pension schemes granted master trust authorisation
* Payments to government bodies or charities

If you are building for **Me-to-Me** payments -- where the same person or business entity owns both accounts -- Sweeping VRP is the correct product. See the [Variable Recurring Payments](https://modulr.readme.io/docs/variable-recurring-payments) section for details.

## Guides

Use these pages to build your integration:

* [Commercial cVRP Overview](https://modulr.readme.io/docs/commercial-vrp-overview)
* [Getting started with cVRP](https://modulr.readme.io/docs/getting-started-with-cvrp)
* [Creating a cVRP consent](https://modulr.readme.io/docs/creating-a-cvrp-consent)
* [Initiate a cVRP payment](https://modulr.readme.io/docs/creating-a-cvrp-payment)

<br />