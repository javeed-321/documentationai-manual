---
updatedAt: 2025-09-05T18:48:44.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Third Party Providers

Information regarding PSD2

We allow Third Party Providers (“TPPs”) to:

* Get access to an end user’s account information
* Trigger a one-off payment

In order gain access the TPP will need to:

* Hold a valid eIDAS / OBWAC certificate that Modulr can verify
* Register with Modulr as a TPP
* Get consent from the end user

## How does this work?

Please contact Modulr at [openbanking@modulrfinance.com](openbanking@modulrfinance.com), indicating the certificate you intend to use for mutual TLS. Once we confirm this has been received, you can then register using the endpoint `<baseurl>/register`.  You will need:

* An eIDAS certificate that has been obtained from one of the Qualified Trusted Service Providers. A list of QTSPs can be found here: <https://www.openbankingeurope.eu/qtsps-and-eidas/>
* Or an OBWAC certificate that has been obtained from Open banking UK.

> 📘 Base URLs
>
> Production: <https://openbanking.modulrfinance.com>\
> Sandbox: <https://openbanking-sandbox.modulrfinance.com>

### You will need to provide the following details:

```json
{
  "redirect_uris": ["http://www.test.com"],
  "client_name": "testClient",
  "client_legal_name": "testClientLegal",
  "client_org_id": "999543",
  "client_description": "test description",
  "address": "testAddress",
  "contacts": [
  	{
     "first_name": "testFirstname-1",
     "last_name": "testLastname-1",
     "telephone": "111111",
     "email": "abc1@aaa.com",
     "job_role": "testRole-1",
     "role_type": "Technical"
    }, 
    {
     "first_name": "testFirstname-2",
     "last_name": "testLastname-2",
     "telephone": "222222",
     "email": "abc2@aaa.com",
     "job_role": "testRole-2",
     "role_type": "Business"
	}
  ],
  "scope": "AISP PISP",
  "client_uri": "http://www.test.com/info",
  "tos_uri": "http://www.test.com/tos",
  "policy_uri": "http://www.test.com/policy",
  "logo_uri": "http://www.test.com/logo"
}
```

### The response will include:

```json
{
    "client_id": "8b7b1bdbcb9242b6bdf249cb6e04ef7c",
    "secret": "NWQ2YTg4NmItODdlNi00OWM2LTk1YzktNDk0N2MwMTMxMTlm",
    "grant_type": [
        "authorization_code", "refresh_token"
    ],
    "provider_id": "ProviderIdForModulr",
    "provider_display_name": "DisplayNameForModulr",
    "redirect_uris" : ["http://www.test.com"]
}
```

Then you can list Modulr as an Account Service & Payment Service Provider in your application.

Once a user has selected Modulr in your application you need to use the `<baseurl>/consent` endpoint to get a redirect URL, using this URL to redirect the user to Modulr so they can sign in.

The end user will:

* Sign in as they usually would for Modulr.
* Consent (or not) to give you access.
* Note: for Payments, the consent can be used only once within one hour. For Account Services, consent duration can be null. There is no limit on maximum consent duration.

They will then be redirected back to you. If they have consented you will be provided with an authorization code.

Using the authorization code you can get an access token via the `<baseurl>/oauth/token` endpoint, which you then use to access the specific action you have gained consent for.

For account information access you can go back to the token endpoint to get a refreshed access token.

To fetch account information use the endpoint `<baseurl>/accounts`.  The request is a GET with the headers: `X-CLIENT-SSL-CERT`, with your eIDAS/OBWAC certificate and `x-mod-consent-id` with the consent token.

To make a payment, use the endpoint `<baseurl>/payments`. The request is a POST with the headers: `X-CLIENT-SSL-CERT`, with your eIDAS/OBWAC certificate and `x-mod-consent-id` with the consent token.