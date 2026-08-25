# EdgeWorkers Documentation

> Use Akamai's EdgeWorkers service to execute JavaScript functions at the edge and create customized web experiences based on geolocation, device characteristics, and more.

Fetch the complete documentation index at: https://techdocs.akamai.com/edgeworkers/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: API

- [API index](https://techdocs.akamai.com/edgeworkers/reference/api/llms.txt): full category index
- [EdgeWorkers API](https://techdocs.akamai.com/edgeworkers/reference/api.md)
- [API summary](https://techdocs.akamai.com/edgeworkers/reference/api-summary.md)
- [Get started](https://techdocs.akamai.com/edgeworkers/reference/api-get-started.md)
- [EdgeWorkers concepts](https://techdocs.akamai.com/edgeworkers/reference/edgeworker-concepts.md)
- [Rate and resource limiting](https://techdocs.akamai.com/edgeworkers/reference/resource-limiting.md)
- [Errors](https://techdocs.akamai.com/edgeworkers/reference/api-errors.md)
- [Validation types](https://techdocs.akamai.com/edgeworkers/reference/validation-types.md)
- [400](https://techdocs.akamai.com/edgeworkers/reference/400.md)
- [401](https://techdocs.akamai.com/edgeworkers/reference/401.md)
- [403](https://techdocs.akamai.com/edgeworkers/reference/403.md)
- [404](https://techdocs.akamai.com/edgeworkers/reference/404.md)
- [422](https://techdocs.akamai.com/edgeworkers/reference/422.md)
- [429](https://techdocs.akamai.com/edgeworkers/reference/429.md)
- [500](https://techdocs.akamai.com/edgeworkers/reference/500.md)
- [501](https://techdocs.akamai.com/edgeworkers/reference/501.md)
- [502](https://techdocs.akamai.com/edgeworkers/reference/502.md)
- [503](https://techdocs.akamai.com/edgeworkers/reference/503.md)

## API Reference: Groups

- [Groups index](https://techdocs.akamai.com/edgeworkers/reference/groups/llms.txt): full category index
- [List permission groups](https://techdocs.akamai.com/edgeworkers/reference/get-groups.md): View a list of groups and the associated permission capabilities, for example: activate a version or fetch an EdgeWorker ID.
- [Get a permission group](https://techdocs.akamai.com/edgeworkers/reference/get-group.md): View details on the capabilities enabled within a specified group, for example: activate a version or fetch an EdgeWorker ID.

## API Reference: Resource tiers

- [Resource tiers index](https://techdocs.akamai.com/edgeworkers/reference/resource-tiers/llms.txt): full category index
- [List resource tiers](https://techdocs.akamai.com/edgeworkers/reference/get-resource-tiers.md): View the list of available resource tiers for a specific contract ID. The resource tier defines the resource consumption limits for an EdgeWorker ID.

## API Reference: EdgeWorker IDs

- [EdgeWorker IDs index](https://techdocs.akamai.com/edgeworkers/reference/edgeworker-ids/llms.txt): full category index
- [Create a new EdgeWorker ID](https://techdocs.akamai.com/edgeworkers/reference/post-ids.md): Register a new EdgeWorker ID within a particular group.
- [List EdgeWorker IDs](https://techdocs.akamai.com/edgeworkers/reference/get-ids.md): View a list of EdgeWorker IDs created for your account. You can choose to specify the group and resource tier in the request to filter the response.
- [Get an EdgeWorker ID](https://techdocs.akamai.com/edgeworkers/reference/get-id.md): View details for a specific EdgeWorker.
- [Update an EdgeWorker ID](https://techdocs.akamai.com/edgeworkers/reference/put-id.md): Update the `name` or `groupId` of an existing EdgeWorker.
- [Delete an EdgeWorker ID](https://techdocs.akamai.com/edgeworkers/reference/delete-id.md): Delete a specific EdgeWorker ID.
- [Clone an EdgeWorker ID](https://techdocs.akamai.com/edgeworkers/reference/post-id-clone.md): Clone an EdgeWorker ID to change the resource tier.
- [Get the resource tier](https://techdocs.akamai.com/edgeworkers/reference/get-id-resource-tier.md): View the details of the resource tier assigned to the EdgeWorker ID.
- [Create a new version](https://techdocs.akamai.com/edgeworkers/reference/post-versions.md): Create a new version of an EdgeWorker. In order to run this operation you need to build an [EdgeWorkers code bundle](doc:create-a-code-bundle) and save it in GZIP format. You need to provide the GZIP binary file in the request body, with a `Content-Type` of `application/gzip`.
- [List versions](https://techdocs.akamai.com/edgeworkers/reference/get-versions.md): View a list of EdgeWorker versions.
- [Get version details](https://techdocs.akamai.com/edgeworkers/reference/get-version.md): View details for a specific version.
- [Delete version](https://techdocs.akamai.com/edgeworkers/reference/delete-version.md): Delete a specific version. You can't re-use a deleted EdgeWorker version. For instructions on how to create a new version, see [Create a code bundle](doc:create-a-code-bundle) in the EdgeWorkers guide.
- [Download an EdgeWorkers code bundle](https://techdocs.akamai.com/edgeworkers/reference/get-version-content.md): Download the bundle containing the code the EdgeWorker executes.
- [Activate an EdgeWorker version](https://techdocs.akamai.com/edgeworkers/reference/post-activations.md): Activate an existing EdgeWorker version on the Akamai network, either staging or production.
- [List activations](https://techdocs.akamai.com/edgeworkers/reference/get-activations.md): View the list of activations for an existing EdgeWorker based on ID. You can choose to specify the version in the request. The response filters the list of activations down by version number.
- [Roll back to the previous active EdgeWorker version](https://techdocs.akamai.com/edgeworkers/reference/post-rollback-to-previous-active-version.md): Reactivate the EdgeWorker version that was previously active on the Akamai network, either staging or production.
- [Get an activation](https://techdocs.akamai.com/edgeworkers/reference/get-activation.md): View details for a specific activation.
- [Cancel an activation](https://techdocs.akamai.com/edgeworkers/reference/delete-activation.md): Cancel an activation. You can cancel any activation whose `status` is still `PRESUBMIT`, `PENDING`, or `IN_PROGRESS`. Once complete, the activation status changes from `CANCELLING` to `CANCELLED`.
- [Deactivate an EdgeWorker version](https://techdocs.akamai.com/edgeworkers/reference/post-deactivations.md): Deactivate an existing EdgeWorker version on the Akamai network, either staging or production.
- [List deactivations](https://techdocs.akamai.com/edgeworkers/reference/get-deactivations.md): View the list of deactivations for an existing EdgeWorker. You can limit the results to a specific `version`.
- [Get a deactivation](https://techdocs.akamai.com/edgeworkers/reference/get-deactivation.md): View details for a specific deactivation.
- [List properties](https://techdocs.akamai.com/edgeworkers/reference/get-properties.md): View the list of properties using an existing EdgeWorker ID. You can limit the results to active properties.
- [List revisions](https://techdocs.akamai.com/edgeworkers/reference/get-revisions.md): View the list of revisions for an existing EdgeWorker based on ID. You can limit the results to a specific version or activation. To learn more about Flexible Composition, refer to the [EdgeWorkers guide](doc:flexible-composition).
- [Activate a fallback revision](https://techdocs.akamai.com/edgeworkers/reference/post-revision-activations.md): Reactivate a previously active revision on Akamai's staging or production network. To learn more about Flexible Composition, refer to the [EdgeWorkers guide](doc:flexible-composition).
- [List revision activations](https://techdocs.akamai.com/edgeworkers/reference/get-revision-activations.md): List activations for an existing EdgeWorker revision based on the EdgeWorker's ID. To learn more about Flexible Composition, refer to the [EdgeWorkers guide](doc:flexible-composition).
- [Get a revision](https://techdocs.akamai.com/edgeworkers/reference/get-revision.md): View details for a specific revision. To learn more about Flexible Composition, refer to the [EdgeWorkers guide](doc:flexible-composition).
- [Get a revision BOM](https://techdocs.akamai.com/edgeworkers/reference/get-revision-bom.md): View the Bill of Materials for a specific revision. To learn more about Flexible Composition, refer to the [EdgeWorkers guide](doc:flexible-composition).
- [Compare revisions](https://techdocs.akamai.com/edgeworkers/reference/post-revision-compare.md): View dependency differences between two revisions of the same EdgeWorker activation. To learn more about Flexible Composition, refer to the [EdgeWorkers guide](doc:flexible-composition).
- [Download the combined code bundle](https://techdocs.akamai.com/edgeworkers/reference/get-revision-content.md): Download the combined code bundle that contains the code and the dependencies that the EdgeWorker executes. To learn more about Flexible Composition, refer to the [EdgeWorkers guide](doc:flexible-composition).
- [Pin an active revision](https://techdocs.akamai.com/edgeworkers/reference/post-revision-pin.md): Disable dynamic activation for an EdgeWorker revision on Akamai's staging or production network. Note that you can't pin a revision unless it has a dependency. To learn more about Flexible Composition, refer to the [EdgeWorkers guide](doc:flexible-composition).
- [Unpin an active revision](https://techdocs.akamai.com/edgeworkers/reference/post-revision-unpin.md): Enable dynamic activation for an EdgeWorker revision on Akamai's staging or production network. Note that you can't unpin a revision unless it has a dependency. To learn more about Flexible Composition, refer to the [EdgeWorkers guide](doc:flexible-composition).

## API Reference: Validations

- [Validations index](https://techdocs.akamai.com/edgeworkers/reference/validations/llms.txt): full category index
- [Validate an EdgeWorkers code bundle](https://techdocs.akamai.com/edgeworkers/reference/post-validations.md): Return a list of errors and warnings containing details on how to fix your code bundle. See [Validation types](ref:validation-types). In order to run this operation you need to provide an EdgeWorkers code bundle as a GZIP binary file in the request body, with a `Content-Type` of `application/gzip`.

## API Reference: Contracts

- [Contracts index](https://techdocs.akamai.com/edgeworkers/reference/contracts/llms.txt): full category index
- [List contract IDs](https://techdocs.akamai.com/edgeworkers/reference/get-contracts.md): View the list of contract IDs that you can use to list resource tiers.

## API Reference: Reports

- [Reports index](https://techdocs.akamai.com/edgeworkers/reference/reports/llms.txt): full category index
- [List reports](https://techdocs.akamai.com/edgeworkers/reference/get-reports.md): View a list of available reports. The data in these reports is also available in the [EdgeWorkers Management application](doc:manage-report-data). Note that reports 2 and 4 have been deprecated.
- [Get an EdgeWorker report](https://techdocs.akamai.com/edgeworkers/reference/get-report.md): View a report for a set of EdgeWorkers. Note that reports 2 and 4 have been deprecated.

## API Reference: Secure Token

- [Secure Token index](https://techdocs.akamai.com/edgeworkers/reference/secure-token/llms.txt): full category index
- [Create a secure token](https://techdocs.akamai.com/edgeworkers/reference/post-secure-token.md): Generate a JWT authentication token to [enable enhanced debug headers](doc:enable-enhanced-debug-headers) for EdgeWorkers.
- [Get a secure token](https://techdocs.akamai.com/edgeworkers/reference/get-secure-token.md): __Deprecated__ Use the [Create a secure token](ref:post-secure-token) operation instead. This returns a generated authentication token, for use with enhanced debug headers for EdgeWorkers.

## API Reference: EdgeWorkers customer log delivery

- [EdgeWorkers customer log delivery index](https://techdocs.akamai.com/edgeworkers/reference/edgeworkers-customer-log-delivery/llms.txt): full category index
- [Create a new logging override](https://techdocs.akamai.com/edgeworkers/reference/post-override.md): Override the default JavaScript logging level for a specific EdgeWorker ID. By default, the log level for JavaScript logs is `ERROR`. For more information, go to the [Use DataStream 2 to deliver JavaScript logs](doc:ds2-javascript-logging) tutorial.
- [List logging overrides](https://techdocs.akamai.com/edgeworkers/reference/get-overrides.md): View a list of logging overrides created for your EdgeWorker ID. For more information, go to the [Use DataStream 2 to deliver JavaScript logs](doc:ds2-javascript-logging) tutorial.
- [Get logging override status](https://techdocs.akamai.com/edgeworkers/reference/get-override.md): Get status information about a specific logging override. For more information, go to the [Use DataStream 2 to deliver JavaScript logs](doc:ds2-javascript-logging) tutorial.

## API Reference: Limits

- [Limits index](https://techdocs.akamai.com/edgeworkers/reference/limits/llms.txt): full category index
- [List limits](https://techdocs.akamai.com/edgeworkers/reference/get-limits.md): View the various limits EdgeWorkers imposes on the number of activations, EdgeWorker IDs, and versions you can deploy.
