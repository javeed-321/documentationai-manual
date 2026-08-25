# Cloud Wrapper Documentation

> Akamai's Cloud Wrapper optimizes connectivity between cloud infrastructures and the Akamai Intelligent Edge. It uses custom caching to reduce origin requests and the cost to distribute content from the cloud. If you have a high volume of end-user requests, Cloud Wrapper can help provide consistent, high-quality experiences.

Fetch the complete documentation index at: https://techdocs.akamai.com/cloud-wrapper/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: API

- [API index](https://techdocs.akamai.com/cloud-wrapper/reference/api/llms.txt): full category index
- [Cloud Wrapper Configuration API](https://techdocs.akamai.com/cloud-wrapper/reference/api.md)
- [API summary](https://techdocs.akamai.com/cloud-wrapper/reference/api-summary.md)
- [Get started](https://techdocs.akamai.com/cloud-wrapper/reference/get-started-with-the-cloud-wrapper-configuration-api.md)
- [Concepts](https://techdocs.akamai.com/cloud-wrapper/reference/concepts.md)
- [Rate limiting](https://techdocs.akamai.com/cloud-wrapper/reference/rate-limiting.md)
- [API hypermedia](https://techdocs.akamai.com/cloud-wrapper/reference/api-hypermedia.md)
- [Errors](https://techdocs.akamai.com/cloud-wrapper/reference/errors.md)
- [400](https://techdocs.akamai.com/cloud-wrapper/reference/400.md)
- [401](https://techdocs.akamai.com/cloud-wrapper/reference/401.md)
- [403](https://techdocs.akamai.com/cloud-wrapper/reference/403.md)
- [404](https://techdocs.akamai.com/cloud-wrapper/reference/404.md)
- [405](https://techdocs.akamai.com/cloud-wrapper/reference/405.md)
- [415](https://techdocs.akamai.com/cloud-wrapper/reference/415.md)
- [429](https://techdocs.akamai.com/cloud-wrapper/reference/429.md)
- [500](https://techdocs.akamai.com/cloud-wrapper/reference/500.md)

## API Reference: Capacity

- [Capacity index](https://techdocs.akamai.com/cloud-wrapper/reference/capacity/llms.txt): full category index
- [List capacity](https://techdocs.akamai.com/cloud-wrapper/reference/get-capacity-inventory.md): View the capacities available for a given `contractId`.

## API Reference: Properties

- [Properties index](https://techdocs.akamai.com/cloud-wrapper/reference/properties/llms.txt): full category index
- [List properties](https://techdocs.akamai.com/cloud-wrapper/reference/get-properties.md): View a list of properties for delivery products that are eligible to enable Cloud Wrapper.
- [List origins](https://techdocs.akamai.com/cloud-wrapper/reference/get-origins.md): View a list of [origin](https://techdocs.akamai.com/property-mgr/reference/latest-origin) servers configured in eligible delivery properties. The API pulls response data from the property as it's shown in PAPI. At least one origin server entry is shown at the top-level for the `default` rule. If additional origin servers are set in child-level rules in the same property, they're revealed at a lower level.

## API Reference: Locations

- [Locations index](https://techdocs.akamai.com/cloud-wrapper/reference/locations/llms.txt): full category index
- [List locations](https://techdocs.akamai.com/cloud-wrapper/reference/get-locations.md): View the locations available to distribute your Cloud Wrapper capacity. This operation lists the available `trafficTypeId` values for use when creating configurations.

## API Reference: Configurations

- [Configurations index](https://techdocs.akamai.com/cloud-wrapper/reference/configurations/llms.txt): full category index
- [Create a configuration](https://techdocs.akamai.com/cloud-wrapper/reference/post-configuration.md): Create a Cloud Wrapper configuration. > 📘 > > You first need to work with your account team to include Cloud Wrapper locations and capacity on your contract. Verify your capacity by viewing your [capacity inventory](ref:get-capacity-inventory).
- [List configurations](https://techdocs.akamai.com/cloud-wrapper/reference/get-configurations.md): List all of the Cloud Wrapper configurations on your contract.
- [Activate a configuration](https://techdocs.akamai.com/cloud-wrapper/reference/post-configuration-activations.md): Activate a Cloud Wrapper configuration. It takes 3-4 hours for the configuration to complete. You can use the configuration's `configId` to run the [Get a configuration](ref:get-configuration) operation and review its `status`. Once it's `ACTIVE`, [enable the Cloud Wrapper behavior](https://techdocs.akamai.com/cloud-wrapper/docs/add-a-cloud-wrapper-behavior#enable-the-cloud-wrapper-behavior) in your property.  To deactivate a configuration, [update it](ref:put-configuration) and set the `activate` query string to `false`.
- [Get a configuration](https://techdocs.akamai.com/cloud-wrapper/reference/get-configuration.md): View a specific Cloud Wrapper configuration.
- [Update a configuration](https://techdocs.akamai.com/cloud-wrapper/reference/put-configuration.md): Update a saved or inactive configuration.
- [Delete a configuration](https://techdocs.akamai.com/cloud-wrapper/reference/delete-configuration.md): Delete a specific Cloud Wrapper configuration. The delete can take up to three hours to complete. You can use the configuration's `configId` to run the [Get a configuration](ref:get-configuration) operation to check the status. `DELETE_IN_PROGRESS` indicates the API accepted the request and it's processing the delete. A 404 response indicates the API has deleted the configuration.  > 🚧 Before you delete a configuration: > > Ensure that all the properties that use it have the [`cloudWrapper`](https://techdocs.akamai.com/property-mgr/reference/latest-cloud-wrapper) behavior disabled. Then [update](ref:put-configuration) the configuration to deactivate it by setting the `activate` query string to `false`.

## API Reference: Multi-CDN

- [Multi-CDN index](https://techdocs.akamai.com/cloud-wrapper/reference/multi-cdn/llms.txt): full category index
- [List auth keys](https://techdocs.akamai.com/cloud-wrapper/reference/get-auth-keys.md): This operation shows the `cdnAuthKeys` for a specific Akamai `contractId` and specific third-party CDN (`cdnCode`). Use [auth keys](ref:concepts) (`cdnAuthKeys`) to generate the header that authenticates a request between a third-party CDN and your Cloud Wrapper cache, on the Akamai CDN.
- [Get origin hostnames for a configuration](https://techdocs.akamai.com/cloud-wrapper/reference/get-origin-hostnames.md): View the origin hostnames for a specific configuration.
- [List CDN providers](https://techdocs.akamai.com/cloud-wrapper/reference/get-providers.md): View a list of CDN providers.
