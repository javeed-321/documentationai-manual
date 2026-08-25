# Akamai MFA OIDC API Documentation

> Akamai MFA OIDC API lets you integrate multi-factor authentication (MFA) into OpenID Connect (OIDC) authentication flows using Pushed Authorization Requests (PAR).

Fetch the complete documentation index at: https://techdocs.akamai.com/mfa-oidc/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: Akamai MFA OIDC
- [Get an authorization code](https://techdocs.akamai.com/mfa-oidc/reference/get-authorize.md): This operation authenticates and authorizes the user. You need to make this request from the browser.
- [Submit an authorization request](https://techdocs.akamai.com/mfa-oidc/reference/post-par.md): This operation returns a short-lived, one-time use reference to the stored authorization request.
- [Create an ID token](https://techdocs.akamai.com/mfa-oidc/reference/post-token.md): This operation exchanges an [authorization code](ref:get-authorize) for ID token.
