---
updatedAt: 2026-07-17T15:00:22.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Getting Sandbox Access

## Getting access to our Sandbox

To test out our API or Customer Portal you will need to register for access to our sandbox environment. To do so, complete the form [here](https://share.hsforms.com/1VPuWUUZPSSW4Npn-0BKqew1co3o).

## Sandbox default functionality

Your sandbox environment will be configured as a Direct Customer and you'll be provided with:

* API credentials
* Admin user credentials
* A single GBP account credited with £50,000 of fictitious money

Within the Sandbox environment, you can:

* Manage users
* Manage accounts
* Manage payment rules
* Manage beneficiaries
* Manage payments
* Credit your accounts with additional fictitious money via the Sandbox only [credit endpoint](https://modulr.readme.io/reference/createpayments)

## Sandbox functionality that can be enabled

We can configure the sandbox environment as a Partner such that you can:

* Manage customers

We can also enable the ability to:

* Create EUR (SEPA) accounts
* Manage Direct Debit collections
* Manage Virtual cards
* Manage payment approvals (including creating admin users with approval permissions)
* Allow waiting for funds before payments are made

## API Base URL

Within the Sandbox environment there are two authentication methods available:

If you are accessing our API directly from your code and have set-up HMAC [(Instructions here](https://modulr.readme.io/docs/authentication)) on how to calculate the hmac value are here: [Authentication](https://modulr.readme.io/docs/authentication)), the URL you should use for the Modulr API sandbox environment is:

* <https://api-sandbox.modulrfinance.com/api-sandbox/>

If you wish to try our API's **without** first setting up HMAC, you can use our token URL instead using your **API Key**:

* <https://api-sandbox.modulrfinance.com/api-sandbox-token/>

> ❗️ Authentication in Production
>
> HMAC is the only authentication method used in Production. Use of the token is only in our Sandbox environment.
>
> You will be provided with the production environment URL during onboarding to the production service.
>
> Failing to use the correct URLs may result in requests being rejected or silently ignored

There can be additional onboarding processes for certain functionality:\
[Getting started with DD collections →](https://modulr.readme.io/docs/what-is-dd-collections)\
[Getting started with Virtual Cards →](https://modulr.readme.io/docs/getting-started-with-virtual-cards)

<br />

## Sandbox Customer Portal Access

With your Sandbox account, you will have access to the Sandbox Modulr Portal. You can learn more about using this portal in our [Modulr Portal Knowledge Base here](https://knowledge.modulrfinance.com/knowledge-hub/using-the-modulr-portal).