# Network Lists API Documentation

> Manage common sets of lists used by various Akamai security products and features.

Fetch the complete documentation index at: https://techdocs.akamai.com/network-lists/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: API

- [API index](https://techdocs.akamai.com/network-lists/reference/api/llms.txt): full category index
- [Network Lists API](https://techdocs.akamai.com/network-lists/reference/api.md)
- [API summary](https://techdocs.akamai.com/network-lists/reference/api-summary.md)
- [Get started](https://techdocs.akamai.com/network-lists/reference/api-get-started.md)
- [Concurrency control](https://techdocs.akamai.com/network-lists/reference/concurrency-control.md)
- [Partial GET and PUT options](https://techdocs.akamai.com/network-lists/reference/partial-get-and-put-options.md)
- [API hypermedia](https://techdocs.akamai.com/network-lists/reference/api-hypermedia.md)
- [Rate limits](https://techdocs.akamai.com/network-lists/reference/rate-limits.md)
- [Activation states](https://techdocs.akamai.com/network-lists/reference/activation-states.md)
- [Errors](https://techdocs.akamai.com/network-lists/reference/api-errors.md)
- [400](https://techdocs.akamai.com/network-lists/reference/400.md)
- [401](https://techdocs.akamai.com/network-lists/reference/401.md)
- [403](https://techdocs.akamai.com/network-lists/reference/403.md)
- [404](https://techdocs.akamai.com/network-lists/reference/404.md)
- [409](https://techdocs.akamai.com/network-lists/reference/409.md)
- [500](https://techdocs.akamai.com/network-lists/reference/500.md)

## API Reference: Network Lists

- [Network Lists index](https://techdocs.akamai.com/network-lists/reference/network-lists/llms.txt): full category index
- [List network lists](https://techdocs.akamai.com/network-lists/reference/get-network-lists.md): List all network lists available for an authenticated user who belongs to a group, optionally filtered by `listType` or based on a `search` string. Results appear within the `networkLists` array, which might be empty if no network lists are available to the client.
- [Create a new network list](https://techdocs.akamai.com/network-lists/reference/post-network-lists.md): Creates a new network list.
- [Delete a network list](https://techdocs.akamai.com/network-lists/reference/delete-network-list.md): Removes a network list. You can only remove network lists that never activated. To deactivate a list, you can empty out its `list` of elements.
- [Get a network list](https://techdocs.akamai.com/network-lists/reference/get-network-list.md): Gets a network list's most recent `syncPoint` version.
- [Update a network list](https://techdocs.akamai.com/network-lists/reference/put-network-list.md): Modify the network list items and properties. Allows you to set the name, description and set of network list items to the resource. The current state of the list will be replaced with the properties and items you provide. The type cannot be changed.
- [Append elements to a network list](https://techdocs.akamai.com/network-lists/reference/post-network-list-append.md): Appends a set of elements to a network list.  If the networks list's `type` is `IP`, the submitted `list` is a series of IP addresses or CIDR blocks.  If the type is `GEO`, it's a set of two-character country codes. (See the [EdgeScape Documentation](https://control.akamai.com/apps/download-center/#/products/3;name=EdgeScape) for more information. For a list of countries, go to __Data Codes__ &rArr; __Country Code__.)
- [Update network list details](https://techdocs.akamai.com/network-lists/reference/put-network-list-details.md): Update a network list's name or description.
- [Remove an element](https://techdocs.akamai.com/network-lists/reference/delete-network-list-elements.md): Removes the specified `element` from the list.  If the network list's `type` is `IP`, the value is a URL-encoded IP address or CIDR block. If the type is `GEO`, it's a two-character country code.
- [Add an element](https://techdocs.akamai.com/network-lists/reference/put-network-list-elements.md): Adds the specified `element` to the list.  If the network list's `type` is `IP`, the value needs to be a URL-encoded IP address or CIDR block. If the type is `GEO`, it's a two-character country code. (See the [EdgeScape Documentation](https://control.akamai.com/apps/download-center/#/products/3;name=EdgeScape)) for more information. For a list of countries, go to __Data Codes__ &rArr; __Country Code__.)
- [Activate a network list](https://techdocs.akamai.com/network-lists/reference/post-network-list-activate.md): Activate the most recent `syncPoint` version of a network list in either the `STAGING` or `PRODUCTION` environment.
- [Get activation status](https://techdocs.akamai.com/network-lists/reference/get-network-list-status.md): Shows a network list's activation status on either the `STAGING` or `PRODUCTION` environment. The response reflects standard activation status. For fast activation status, see [Get activation details](ref:get-activation).
- [Get an activation's snapshot](https://techdocs.akamai.com/network-lists/reference/get-network-list-history.md): Gets a version of a network list in its state when activated, with each version identified by its `syncPoint` value.  You can only get `syncPoint` versions that have been activated.

## API Reference: Activations

- [Activations index](https://techdocs.akamai.com/network-lists/reference/activations/llms.txt): full category index
- [Get activation details](https://techdocs.akamai.com/network-lists/reference/get-activation.md): Provides detailed status for a given activation, including progress on _fast_ activation and other audit information, in addition to information ordinarily available from the [Get activation status](ref:get-network-list-status) operation.

## API Reference: Notifications

- [Notifications index](https://techdocs.akamai.com/network-lists/reference/notifications/llms.txt): full category index
- [Subscribe to network lists](https://techdocs.akamai.com/network-lists/reference/post-notifications-subscribe.md): Specifies a set of email addresses to inform Control Center account recipients about changes to a set of network lists.
- [Unsubscribe to network lists](https://techdocs.akamai.com/network-lists/reference/post-notifications-unsubscribe.md): Unsubscribes the listed users from a set of network lists.
