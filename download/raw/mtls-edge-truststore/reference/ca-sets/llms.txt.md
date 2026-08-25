# Mutual TLS Edge Truststore (Limited Availability) Documentation

> Mutual TLS Edge Truststore is a self-service application that supports the creation, management, and activation of certificate authority certificate sets (CA sets) needed to establish mutual authentication (mTLS) sessions between the client and the Akamai edge.

Fetch the complete documentation index at: https://techdocs.akamai.com/mtls-edge-truststore/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: CA sets
- [Create a CA set](https://techdocs.akamai.com/mtls-edge-truststore/reference/post-ca-set.md): Create a CA set with the provided name.
- [List CA sets](https://techdocs.akamai.com/mtls-edge-truststore/reference/get-ca-sets.md): List CA sets created under the account.
- [Get a CA set](https://techdocs.akamai.com/mtls-edge-truststore/reference/get-ca-set.md): Get details of a CA set.
- [Delete a CA set](https://techdocs.akamai.com/mtls-edge-truststore/reference/delete-ca-set.md): Delete the CA set for given `caSetId`.
- [List CA set activations](https://techdocs.akamai.com/mtls-edge-truststore/reference/get-deployment-request-for-ca-set.md): List all activation and deactivation requests for the CA set.
- [List CA set activities](https://techdocs.akamai.com/mtls-edge-truststore/reference/get-ca-set-activities.md): List activities on the CA set, sorted reverse chronologically with recent activities first. Apply `start` and `end` parameters to specify a time range. Specify only `start` or `end` to include all activities after or before a given time.
- [Get CA set associations](https://techdocs.akamai.com/mtls-edge-truststore/reference/get-ca-set-associations.md): Get a CA set Associations.
- [Clone a CA set](https://techdocs.akamai.com/mtls-edge-truststore/reference/post-clone-ca-set.md): Clones a CA set. If you provide the optional cloneFromVersion parameter, the clone is created from that version; otherwise, it uses the latest version. The cloned set may include expired certificates from the source version.
- [Get CA set delete status](https://techdocs.akamai.com/mtls-edge-truststore/reference/get-deletion-request-for-ca-set.md): Retrieves the status of a CA set deletion request, including its progress, overall status, and any network-specific failures.
