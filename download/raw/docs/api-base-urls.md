---
updatedAt: 2025-09-05T18:54:40.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# API Base URLs and Authentication Methods

Learn about the different Base URL options for use in the Modulr Sandbox

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