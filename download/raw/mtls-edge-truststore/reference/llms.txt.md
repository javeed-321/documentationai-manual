# Mutual TLS Edge Truststore (Limited Availability) Documentation

> Mutual TLS Edge Truststore is a self-service application that supports the creation, management, and activation of certificate authority certificate sets (CA sets) needed to establish mutual authentication (mTLS) sessions between the client and the Akamai edge.

Fetch the complete documentation index at: https://techdocs.akamai.com/mtls-edge-truststore/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: API

- [API index](https://techdocs.akamai.com/mtls-edge-truststore/reference/api/llms.txt): full category index
- [mTLS Edge Truststore API v2](https://techdocs.akamai.com/mtls-edge-truststore/reference/api.md)
- [API summary](https://techdocs.akamai.com/mtls-edge-truststore/reference/api-summary.md)
- [Get started](https://techdocs.akamai.com/mtls-edge-truststore/reference/api-get-started.md)
- [API concepts](https://techdocs.akamai.com/mtls-edge-truststore/reference/api-concepts.md)
- [Rate and resource limiting](https://techdocs.akamai.com/mtls-edge-truststore/reference/rate-resource-limit.md)
- [API Hypermedia](https://techdocs.akamai.com/mtls-edge-truststore/reference/api-hypermedia.md)
- [Object versioning](https://techdocs.akamai.com/mtls-edge-truststore/reference/object-versioning.md)
- [Enumeration values](https://techdocs.akamai.com/mtls-edge-truststore/reference/enumeration-values.md)
- [API workflow](https://techdocs.akamai.com/mtls-edge-truststore/reference/api-workflow.md)
- [Errors](https://techdocs.akamai.com/mtls-edge-truststore/reference/errors.md)
- [400](https://techdocs.akamai.com/mtls-edge-truststore/reference/400.md)
- [401](https://techdocs.akamai.com/mtls-edge-truststore/reference/401.md)
- [403](https://techdocs.akamai.com/mtls-edge-truststore/reference/403.md)
- [404](https://techdocs.akamai.com/mtls-edge-truststore/reference/404.md)
- [405](https://techdocs.akamai.com/mtls-edge-truststore/reference/405.md)
- [406](https://techdocs.akamai.com/mtls-edge-truststore/reference/406.md)
- [409](https://techdocs.akamai.com/mtls-edge-truststore/reference/409.md)
- [415](https://techdocs.akamai.com/mtls-edge-truststore/reference/415.md)
- [422](https://techdocs.akamai.com/mtls-edge-truststore/reference/422.md)
- [429](https://techdocs.akamai.com/mtls-edge-truststore/reference/429.md)
- [500](https://techdocs.akamai.com/mtls-edge-truststore/reference/500.md)
- [503](https://techdocs.akamai.com/mtls-edge-truststore/reference/503.md)

## API Reference: CA sets

- [CA sets index](https://techdocs.akamai.com/mtls-edge-truststore/reference/ca-sets/llms.txt): full category index
- [Create a CA set](https://techdocs.akamai.com/mtls-edge-truststore/reference/post-ca-set.md): Create a CA set with the provided name.
- [List CA sets](https://techdocs.akamai.com/mtls-edge-truststore/reference/get-ca-sets.md): List CA sets created under the account.
- [Get a CA set](https://techdocs.akamai.com/mtls-edge-truststore/reference/get-ca-set.md): Get details of a CA set.
- [Delete a CA set](https://techdocs.akamai.com/mtls-edge-truststore/reference/delete-ca-set.md): Delete the CA set for given `caSetId`.
- [List CA set activations](https://techdocs.akamai.com/mtls-edge-truststore/reference/get-deployment-request-for-ca-set.md): List all activation and deactivation requests for the CA set.
- [List CA set activities](https://techdocs.akamai.com/mtls-edge-truststore/reference/get-ca-set-activities.md): List activities on the CA set, sorted reverse chronologically with recent activities first. Apply `start` and `end` parameters to specify a time range. Specify only `start` or `end` to include all activities after or before a given time.
- [Get CA set associations](https://techdocs.akamai.com/mtls-edge-truststore/reference/get-ca-set-associations.md): Get a CA set Associations.
- [Clone a CA set](https://techdocs.akamai.com/mtls-edge-truststore/reference/post-clone-ca-set.md): Clones a CA set. If you provide the optional cloneFromVersion parameter, the clone is created from that version; otherwise, it uses the latest version. The cloned set may include expired certificates from the source version.
- [Get CA set delete status](https://techdocs.akamai.com/mtls-edge-truststore/reference/get-deletion-request-for-ca-set.md): Retrieves the status of a CA set deletion request, including its progress, overall status, and any network-specific failures.

## API Reference: CA set versioning

- [CA set versioning index](https://techdocs.akamai.com/mtls-edge-truststore/reference/ca-set-versioning/llms.txt): full category index
- [Create a version](https://techdocs.akamai.com/mtls-edge-truststore/reference/post-ca-set-version.md): Create a new CA set version in the CA set specified by `caSetId`. When creating a new version, the API compares the certificates and SHA-1 provided in the request with the existing versions in the CA set. If another version exists with fingerprints for the same certificates, a 422 response provides a link to the version. If the `allowInsecureSha1` option differs between the versions with the same certificates, they're still considered the same CA set version. This prevents creating duplicate CA set versions.
- [List versions](https://techdocs.akamai.com/mtls-edge-truststore/reference/get-ca-set-versions.md): Versions of the CA set specified by `caSetId`.
- [Get a version](https://techdocs.akamai.com/mtls-edge-truststore/reference/get-ca-set-version.md): Get the CA set version details.
- [Update a version](https://techdocs.akamai.com/mtls-edge-truststore/reference/put-ca-set-version.md): Update all the certificates for the version, or the `allowInsecureSha1` that controls what type of certificates to allow.
- [Activate a version](https://techdocs.akamai.com/mtls-edge-truststore/reference/post-activate-ca-set-version.md): Activate the certificates for the version on the specified network.
- [Get version activations](https://techdocs.akamai.com/mtls-edge-truststore/reference/get-version-deployment-request-details.md): Get details of an activation or deactivation request by set ID and version number.
- [Get an activation](https://techdocs.akamai.com/mtls-edge-truststore/reference/get-deployment-request-details.md): Get details of an activation or deactivation request specified by `activationId`.
- [List certificates](https://techdocs.akamai.com/mtls-edge-truststore/reference/get-ca-set-version-certificates.md): List certificates for the specified version.
- [Clone a version](https://techdocs.akamai.com/mtls-edge-truststore/reference/post-clone-ca-set-version.md): Clone a version of the CA set from the CA set specified by `version`. Note that the clone may reflect expired certificates from the original.
- [Deactivate a version](https://techdocs.akamai.com/mtls-edge-truststore/reference/post-deactivate-ca-set-version.md): Deactivate the certificates for the version on the specified network.
- [Delete a version](https://techdocs.akamai.com/mtls-edge-truststore/reference/delete-ca-set-version.md): Marks the CA set version (`versionNumber`) in a specified CA set (`caSetId`) for future deletion without removing it from the system.  When you [Create a version](ref:post-ca-set-version), the new CA set version takes the subsequent `versionNumber` irregardless of earlier versions scheduled for deletion.

## API Reference: Certificates

- [Certificates index](https://techdocs.akamai.com/mtls-edge-truststore/reference/certificates/llms.txt): full category index
- [Validate certificates](https://techdocs.akamai.com/mtls-edge-truststore/reference/post-validate-certificates.md): Validates a list of certificates passed in PEM format and returns validation results for each certificate. The operation fails if any certificate is invalid.
