# Mutual TLS Origin Keystore Documentation

> Use Mutual TLS Origin Keystore to manage client certificates for mTLS authentication between the Akamai edge server and the origin.

Fetch the complete documentation index at: https://techdocs.akamai.com/mtls-origin-keystore/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: Client certificate versions
- [Rotate a client certificate](https://techdocs.akamai.com/mtls-origin-keystore/reference/post-client-cert-version.md): Create a new version in the client certificate specified by `certificateId`.
- [List client certificate versions](https://techdocs.akamai.com/mtls-origin-keystore/reference/get-client-cert-versions.md): Versions of the client certificate specified by `certificateId`.
- [Delete a client certificate version](https://techdocs.akamai.com/mtls-origin-keystore/reference/delete-client-certificate.md): Delete a client certificate version with the provided `certificateId` and `version`. [Learn more](doc:manage-client-certificates#delete-a-client-certificate-version).
- [Upload a signed client certificate](https://techdocs.akamai.com/mtls-origin-keystore/reference/post-cert-block.md): Upload a signed `THIRD_PARTY` client certificate with the `AWAITING_SIGNED_CERTIFICATE` status. [Learn more](https://techdocs.akamai.com/mtls-origin-keystore/docs/upload-cert).
