# Image and Video Manager Documentation

> With more people using mobile devices and more ways to deliver content, dealing with your images and videos can be challenging. Akamai's Image and Video Manager gives you the control you need to expertly manage them and fully engage your web visitors.

Fetch the complete documentation index at: https://techdocs.akamai.com/ivm/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: API

- [API index](https://techdocs.akamai.com/ivm/reference/api/llms.txt): full category index
- [Image and Video Manager API v2](https://techdocs.akamai.com/ivm/reference/api.md)
- [API summary](https://techdocs.akamai.com/ivm/reference/api-summary.md)
- [Get started](https://techdocs.akamai.com/ivm/reference/get-started.md)
- [IVM Concepts](https://techdocs.akamai.com/ivm/reference/concepts.md)
- [Rate limits](https://techdocs.akamai.com/ivm/reference/rate-limits.md)
- [Test images on-demand](https://techdocs.akamai.com/ivm/reference/test-images-on-demand.md)
- [Transformation types](https://techdocs.akamai.com/ivm/reference/transformation-types.md)
- [Enumeration values](https://techdocs.akamai.com/ivm/reference/enum-values.md)
- [Workflow](https://techdocs.akamai.com/ivm/reference/workflow.md)
- [Errors](https://techdocs.akamai.com/ivm/reference/api-errors.md)
- [400](https://techdocs.akamai.com/ivm/reference/400.md)
- [404](https://techdocs.akamai.com/ivm/reference/404.md)

## API Reference: Images

- [Images index](https://techdocs.akamai.com/ivm/reference/images/llms.txt): full category index
- [List images](https://techdocs.akamai.com/ivm/reference/get-images.md): List a policy's images.
- [Get an image](https://techdocs.akamai.com/ivm/reference/get-image.md): Returns a specific image.

## API Reference: Policies

- [Policies index](https://techdocs.akamai.com/ivm/reference/policies/llms.txt): full category index
- [List policies](https://techdocs.akamai.com/ivm/reference/get-policies.md): Returns a list of all policies belonging to the specified policy set.
- [Roll back a policy](https://techdocs.akamai.com/ivm/reference/put-rollback-policy.md): Use this operation to revert the previous version of the policy and deploy it to the network. Use this operation to stop and reverse a policy rollout.
- [Get a policy](https://techdocs.akamai.com/ivm/reference/get-policy.md): Returns a specific policy assigned to the specified policy set.
- [Create or modify a policy](https://techdocs.akamai.com/ivm/reference/put-policy.md): Run this operation to update an existing policy or create a new policy.  Run the [List policies](ref:get-policies) operation to get the list of existing policies and their policy IDs. Confirm the `policyId` doesn't already exist.
- [Remove a policy](https://techdocs.akamai.com/ivm/reference/delete-policy.md): Delete a specific policy.
- [Get policy history](https://techdocs.akamai.com/ivm/reference/get-policy-history.md): Returns the policy history by policy ID. This operation returns the full state of the policy at various points in time. Time stamps are in ISO 8601 extended notation format.

## API Reference: Image & Video Manager policy sets

- [Image & Video Manager policy sets index](https://techdocs.akamai.com/ivm/reference/image-video-manager-policy-sets/llms.txt): full category index
- [Create a policy set](https://techdocs.akamai.com/ivm/reference/post-policyset.md): Create a new policy set for the contract on both networks.
- [List policy sets](https://techdocs.akamai.com/ivm/reference/get-policysets.md): Returns a list of all policy sets for a contract in production.
- [Get a policy set](https://techdocs.akamai.com/ivm/reference/get-policyset.md): View details for a specific policy set in production.
- [Update a policy set](https://techdocs.akamai.com/ivm/reference/put-policyset.md): Update the `name` or `region` of an existing policy set on both networks.
- [Delete a policy set](https://techdocs.akamai.com/ivm/reference/delete-policyset.md): Delete a policy set from a contract on both networks.

## API Reference: Log error details

- [Log error details index](https://techdocs.akamai.com/ivm/reference/log-error-details/llms.txt): full category index
- [List error details](https://techdocs.akamai.com/ivm/reference/get-errors.md): Returns a list of image or video errors for the transformations requested in the past three days.
- [List log details](https://techdocs.akamai.com/ivm/reference/get-logs.md): Returns a list of image or video logs for the transformations requested in the past three days.
