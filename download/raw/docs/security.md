---
updatedAt: 2025-09-05T18:45:44.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Security

Access to the Modulr API must be over HTTPS in all environments.

HMAC is used to authenticate API calls. As such, you are required to calculate a signature which must be included in the authorization header when making requests.

The signature will be unique per API request and will include:

* Your **API Key** (Sometimes referred to as your **token**)
* Your **API HMAC secret** (Sometimes referred to as your **HMAC** or **Secret**)

For Production: these will be provided during onboarding.

For Sandbox: these will be provided when you create your Sandbox Account.

Keys and secrets must be kept secure as they authenticate all requests as being approved by your organisation. Instructions on creating the signature are detailed here: [Authentication](https://modulr.readme.io/docs/authentication).

Access to the API in the live environment is restricted by IP address. Your IP addresses will be requested during onboarding.

Note that sandbox keys may be time limited to 1 month to allow evaluation. Should you require an extension please contact us.