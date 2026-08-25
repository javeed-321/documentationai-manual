# Certificate Provisioning System Documentation

> Akamai’s Certificate Provisioning System (CPS) allows you to self-provision and manage your Secure Sockets Layer (SSL) and Transport Layer Security (TLS) certificates. It supports all certificate options, including third party.

Fetch the complete documentation index at: https://techdocs.akamai.com/cps/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: API

- [API index](https://techdocs.akamai.com/cps/reference/api/llms.txt): full category index
- [Certificate Provisioning System API v2](https://techdocs.akamai.com/cps/reference/api.md)
- [API summary](https://techdocs.akamai.com/cps/reference/api-summary.md)
- [Get started](https://techdocs.akamai.com/cps/reference/get-started.md)
- [API concepts](https://techdocs.akamai.com/cps/reference/api-concepts.md)
- [X509 certificates](https://techdocs.akamai.com/cps/reference/x509-certificates.md)
- [Certificate authorities](https://techdocs.akamai.com/cps/reference/certificate-authorities.md)
- [Validation](https://techdocs.akamai.com/cps/reference/validation.md)
- [Enrollments](https://techdocs.akamai.com/cps/reference/enrollments-ref.md)
- [Resources related to enrollments](https://techdocs.akamai.com/cps/reference/resources-related-to-enrollments.md)
- [Certificate pinning](https://techdocs.akamai.com/cps/reference/certificate-pinning.md)
- [API workflow](https://techdocs.akamai.com/cps/reference/about-the-cps-workflow.md)
- [Create a domain-validated certificate](https://techdocs.akamai.com/cps/reference/create-a-domain-validated-cert.md)
- [Change control](https://techdocs.akamai.com/cps/reference/change-input-content-type-mapping.md)
- [Change management](https://techdocs.akamai.com/cps/reference/change-mgmt.md)
- [Pre and Post-verification warnings](https://techdocs.akamai.com/cps/reference/pre-post-verification-warnings.md)
- [Let's Encrypt challenges](https://techdocs.akamai.com/cps/reference/lets-encrypt-challenges.md)
- [Third-party](https://techdocs.akamai.com/cps/reference/third-party.md)
- [Object versioning](https://techdocs.akamai.com/cps/reference/internal-versioning.md)
- [Acknowledgement object](https://techdocs.akamai.com/cps/reference/acknowledgement.md)
- [Certificate object](https://techdocs.akamai.com/cps/reference/certificate.md)
- [CertificateHistory object](https://techdocs.akamai.com/cps/reference/certificate-history.md)
- [Change object](https://techdocs.akamai.com/cps/reference/change.md)
- [ChangeHistory object](https://techdocs.akamai.com/cps/reference/change-history.md)
- [ChangeManagement object](https://techdocs.akamai.com/cps/reference/change-management.md)
- [CSR object](https://techdocs.akamai.com/cps/reference/csr.md)
- [Deployment object](https://techdocs.akamai.com/cps/reference/deployment.md)
- [DeploymentSchedule object](https://techdocs.akamai.com/cps/reference/deployment-schedule.md)
- [DvChallenges object](https://techdocs.akamai.com/cps/reference/dvchallenges.md)
- [DvHistory object](https://techdocs.akamai.com/cps/reference/dv-history.md)
- [Enrollment object](https://techdocs.akamai.com/cps/reference/enrollment-object.md)
- [Organization object](https://techdocs.akamai.com/cps/reference/organization.md)
- [TrustChains object](https://techdocs.akamai.com/cps/reference/trust-chains.md)
- [Rate limiting](https://techdocs.akamai.com/cps/reference/rate-limiting.md)
- [Status values](https://techdocs.akamai.com/cps/reference/status-values-and-descriptions.md)
- [Errors](https://techdocs.akamai.com/cps/reference/api-errors.md)
- [400](https://techdocs.akamai.com/cps/reference/400.md)
- [409](https://techdocs.akamai.com/cps/reference/409.md)
- [429](https://techdocs.akamai.com/cps/reference/429.md)
- [500](https://techdocs.akamai.com/cps/reference/500.md)

## API Reference: Enrollments

- [Enrollments index](https://techdocs.akamai.com/cps/reference/enrollments/llms.txt): full category index
- [Create an enrollment](https://techdocs.akamai.com/cps/reference/post-enrollment.md): Creates an enrollment that contains all the information about the process that your certificate goes through from the time you request it, through renewal, and as you obtain subsequent versions. To select a Client TLS Renegotiation option, use the CPS user interface. For details, see [Edit deployment settings](doc:view-edit-network-deploy-settings). Note that you can create one certificate every five minutes, per account. Creating a certificate for the same contract within the five-minute interval results in a 409 response.
- [List enrollments](https://techdocs.akamai.com/cps/reference/get-enrollments.md): A list of the names of each enrollment.
- [Get an enrollment](https://techdocs.akamai.com/cps/reference/get-enrollment.md): Gets an enrollment.
- [Update an enrollment](https://techdocs.akamai.com/cps/reference/put-enrollment.md): Updates an enrollment with changes. Response type varies depending on the type and impact of change. For example, changing SANs list may return HTTP 202 Accepted since the operation requires a new certificate and network deployment operations, and thus can't be completed without a change. On the contrary, for example a Technical Contact name change may return HTTP 200 OK assuming there are no active change and when the operation does not require a new certificate.  Note that `fipsMode` requires that TLS 1.2, TLS 1.3, or both are enabled on the certificate. You can’t list these TLS versions as disabled in the `disallowedTlsVersions` deployment object. When `fipsMode` is enabled, you need to use an active (non-deprecated) cipher profile for both `mustHaveCiphers` and `preferredCiphers`. For details, see [Update SSL/TLS cipher profiles](doc:cipher-profiles).
- [Remove an enrollment](https://techdocs.akamai.com/cps/reference/delete-enrollment.md): Removes an enrollment from CPS. The response code varies depending on the state of the enrollment. Deleting an enrollment in the future, or deleting when the enrollment has a certificate deployed to the network, may result in a 202 response. Deleting an enrollment that hasn't yet deployed any certificate to the network responds immediately with a 200 code.
- [Get DV history](https://techdocs.akamai.com/cps/reference/get-dv-history.md): Domain name Validation history for the enrollment.
- [Get certificate history](https://techdocs.akamai.com/cps/reference/get-history-certificates.md): View the certificate history. To view deployed certificates and their expiration dates, run the [Get production deployment](ref:get-deployments-production) operation. Note that for enrollments with six certificates or fewer, the response yields up to twelve years of data per certificate. If there are more than six certificates in the enrollment, the response shows a truncated set. To view all changes or certificates, use the `includeAll=true` query parameter in the request.
- [Update a deployment schedule](https://techdocs.akamai.com/cps/reference/put-change-deployment-schedule.md): Updates the current deployment schedule.
- [List deployments](https://techdocs.akamai.com/cps/reference/get-deployments.md): Lists the deployments for an enrollment.
- [Get production deployment](https://techdocs.akamai.com/cps/reference/get-deployments-production.md): Gets the enrollments deployed on the production network.
- [Get staging deployment](https://techdocs.akamai.com/cps/reference/get-deployment-staging.md): Gets the enrollments deployed on the staging network.
- [Get change status](https://techdocs.akamai.com/cps/reference/get-enrollment-change.md): Gets the status of a pending change.
- [Cancel a change](https://techdocs.akamai.com/cps/reference/delete-enrollment-change.md): Cancels a pending change. This cancels the entire change. You can cancel any pending change you previously made to a certificate.
- [Get a deployment schedule](https://techdocs.akamai.com/cps/reference/get-change-deployment-schedule.md): Gets the current deployment schedule settings describing when a change deploys to the network.
- [Get a change](https://techdocs.akamai.com/cps/reference/get-change-allowed-input-param.md): Get detailed information of a pending change. Below is a sample where `allowedInput[].type` has the value `third-party-csr`. The acceptable `Accept` header depends on the value of the `allowedInput.type` for the Change instance. See [Change control](ref:change-input-content-type-mapping) for details.
- [Update a change](https://techdocs.akamai.com/cps/reference/post-change-allowed-input-param.md): Updates a pending change. Below is a sample where `allowedInput[].type` has the value `third-party-cert-and-trust-chain`. The acceptable `Content-Type` and `Accept` headers depends on the value of the `allowedInput.type` for the Change instance. See [Change control](ref:change-input-content-type-mapping) for details.
- [Get change history](https://techdocs.akamai.com/cps/reference/get-history-changes.md): Change history of an enrollment.
- [List active certificates](https://techdocs.akamai.com/cps/reference/get-active-certificates.md): Lists enrollments with active certificates. Note that the rate limit for this operation is 10 requests per minute per account. For details, see [Rate limiting](ref:rate-limiting).
