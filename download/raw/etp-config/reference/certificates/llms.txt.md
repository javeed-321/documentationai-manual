# SIA Configuration API Documentation

> Akamai's Secure Internet Access (SIA) Configuration API offers a programmatic interface to manage policy settings to protect against enterprise security and acceptable user policy related events. A distributed configuration encapsulates all the rules for how to process DNS requests for your enterprise.

Fetch the complete documentation index at: https://techdocs.akamai.com/etp-config/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: Certificates
- [Create a new proxy certificate](https://techdocs.akamai.com/etp-config/reference/post-customers-certificate.md): Creates a new proxy certificate.
- [List proxy certificates](https://techdocs.akamai.com/etp-config/reference/get-customers-certificates.md): Returns a list of all available proxy certificates.
- [Get a proxy certificate](https://techdocs.akamai.com/etp-config/reference/get-customers-certificate.md): Returns the details of the specified proxy certificate.
- [Modify a proxy certificate](https://techdocs.akamai.com/etp-config/reference/put-customers-certificate.md): Updates the value of a proxy certificate.
- [Activate a proxy certificate](https://techdocs.akamai.com/etp-config/reference/post-customers-certificate-activate.md): Transitions the proxy certificate's state from `PENDING_ACTIVATION` to `ACTIVE`.
- [Confirm a proxy certificate's distribution](https://techdocs.akamai.com/etp-config/reference/post-certificate-confirm-distribution.md): Transitions the certificate's state from `PENDING_DISTRIBUTION` to `PENDING_ACTIVATION`. Only perform this operation  after distributing the proxy certificates to relevant enterprise devices.
- [Confirm a proxy certificate's download](https://techdocs.akamai.com/etp-config/reference/post-certificate-confirm-download.md): Transitions the certificate's state from `PENDING_DOWNLOAD` to `PENDING_ACTIVATION` or `INCOMPLETE`.
- [Deactivate a proxy certificate](https://techdocs.akamai.com/etp-config/reference/post-certificate-deactivate.md): Transitions the proxy certificate's state from any state to `DEACTIVATING`.
- [Create a new proxy certificate](https://techdocs.akamai.com/etp-config/reference/post-customers-certificate-1.md): Creates a new proxy certificate.
- [List proxy certificates](https://techdocs.akamai.com/etp-config/reference/get-customers-certificates-1.md): Returns all available proxy certificates.
- [Get a proxy certificate](https://techdocs.akamai.com/etp-config/reference/get-customers-certificate-1.md): Returns the details of the specified proxy certificate.
- [Modify a proxy certificate](https://techdocs.akamai.com/etp-config/reference/put-customers-certificate-1.md): Updates the value of a proxy certificate.
- [Activate a proxy certificate](https://techdocs.akamai.com/etp-config/reference/post-customers-certificate-activate-1.md): Transitions the proxy certificate's state from `PENDING_ACTIVATION` to `ACTIVE`.
- [Confirm a proxy certificate's distribution](https://techdocs.akamai.com/etp-config/reference/post-certificate-confirm-distribution-1.md): Transitions the certificate's state from `PENDING_DISTRIBUTION` to `PENDING_ACTIVATION`. Only perform this operation  after distributing the proxy certificates to relevant enterprise devices.
- [Confirm a proxy certificate's download](https://techdocs.akamai.com/etp-config/reference/post-certificate-confirm-download-1.md): Transitions the certificate's state from `PENDING_DOWNLOAD` to `PENDING_ACTIVATION` or `INCOMPLETE`.
- [Deactivate a proxy certificate](https://techdocs.akamai.com/etp-config/reference/post-certificate-deactivate-1.md): Transitions the proxy certificate's state from any state to `DEACTIVATING`.
