---
updatedAt: 2026-06-30T08:31:29.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Commercial VRP Overview

## Overview

Commercial Variable Recurring Payments (cVRP) lets a user authorise a trusted third party to initiate recurring payments on their behalf, with each payment varying in amount and timing but always within pre-agreed limits set at the point of consent. The user authenticates once, subsequent payments can be made without the user needing to re-authenticate with their bank, as long as each payment stays within those limits.

cVRP is a **Me-to-Them** payment type, meaning the payer and the recipient are different people or organisations. If you are building for **Me-to-Me** payments -- where the same person or entity owns both accounts -- see [Sweeping VRP](https://modulr.readme.io/docs/variable-recurring-payments) instead.

> 🚧 cVRP restrictions
>
> cVRP payments can only be made between two UK accounts
>
> cVRP payments can only be made in GBP
>
> All cVRP payments are made via the Faster Payments (FPS) rail

## cVRP consent types

The cVRP specification defines multiple consent types. **Modulr currently supports CVRP1**, which covers the Wave 1 roll-out of cVRP in the UK. Support for additional consent types will be added in future and this page will be updated accordingly.

## Eligible use cases (CVRP1)

Commercial VRP is currently scoped to a defined set of low-risk sectors as part of the initial Wave 1 roll-out.

Your use case must fall within one of the following categories to be eligible:

* Energy, Utilities and Telecoms
* Regulated financial services firms (i.e. accounts with FSCS protection)
* E-money institutions (EMIs)
* Local and central government
* Charities

If you are unsure whether your use case is in scope, speak to your Modulr point of contact before starting your integration.

## Banks supporting cVRP

cVRP is currently available with the following banks in the UK. This list will be updated as more banks are onboarded.

| Banks                                            |
| :----------------------------------------------- |
| Barclays                                         |
| HSBC                                             |
| Lloyds                                           |
| NatWest                                          |
| Santander                                        |
| Nationwide (available from 24 July 2026 onwards) |

## High-level customer journey

Setting up a cVRP follows the same two-stage flow as Sweeping VRP: the user first authorises a consent, then payments can be initiated against that consent without further authentication.

The journey breaks down as follows:

1. **Select bank** – the user selects their bank so they can be directed to the correct authentication URL. Only banks with the `COMMERCIAL_VRP` capability enabled should be presented in your customer journey.
2. **Create a cVRP consent** – you submit a consent request to Modulr specifying the destination account and the payment limits. The user is redirected to their bank to review and authorise the consent.
3. **User authorises** – the user logs in to their bank and approves the consent parameters. They are redirected back to your application.
4. **Initiate payments** – once the consent is authorised, you can initiate payments against it at any time, without any further action from the user, provided each payment falls within the consent limits.
5. **Get payment status** – receive the status of a payment using the payment ID returned at initiation.
6. **Revoke consent** – the user or you can revoke the consent at any time. Revoked consents cannot be reinstated.

> 📘 Consent vs payment
>
> The consent is the agreement between the end user and you that defines what payments are permitted. The consent ID generated at authorisation is then used to initiate individual payments. If no consent exists, no payments can be made.

<br />