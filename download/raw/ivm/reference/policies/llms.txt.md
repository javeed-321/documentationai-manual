# Image and Video Manager Documentation

> With more people using mobile devices and more ways to deliver content, dealing with your images and videos can be challenging. Akamai's Image and Video Manager gives you the control you need to expertly manage them and fully engage your web visitors.

Fetch the complete documentation index at: https://techdocs.akamai.com/ivm/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: Policies
- [List policies](https://techdocs.akamai.com/ivm/reference/get-policies.md): Returns a list of all policies belonging to the specified policy set.
- [Roll back a policy](https://techdocs.akamai.com/ivm/reference/put-rollback-policy.md): Use this operation to revert the previous version of the policy and deploy it to the network. Use this operation to stop and reverse a policy rollout.
- [Get a policy](https://techdocs.akamai.com/ivm/reference/get-policy.md): Returns a specific policy assigned to the specified policy set.
- [Create or modify a policy](https://techdocs.akamai.com/ivm/reference/put-policy.md): Run this operation to update an existing policy or create a new policy.  Run the [List policies](ref:get-policies) operation to get the list of existing policies and their policy IDs. Confirm the `policyId` doesn't already exist.
- [Remove a policy](https://techdocs.akamai.com/ivm/reference/delete-policy.md): Delete a specific policy.
- [Get policy history](https://techdocs.akamai.com/ivm/reference/get-policy-history.md): Returns the policy history by policy ID. This operation returns the full state of the policy at various points in time. Time stamps are in ISO 8601 extended notation format.
