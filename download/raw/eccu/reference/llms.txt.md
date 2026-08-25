# Enhanced Content Control Utility API Documentation

> The Enhanced Content Control Utility (ECCU) is one of several supported Akamai purge interfaces. Use ECCU to specify the set of files to refresh on the edge network. Specify directories, file extensions, certain types of HTTP request, or response properties to refine the set of content to refresh. For example, you can refresh specific parts of a library or the complete cache repository for many domains. The ECCU only invalidates content. It does not remove content from cache.

Fetch the complete documentation index at: https://techdocs.akamai.com/eccu/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: API

- [API index](https://techdocs.akamai.com/eccu/reference/api/llms.txt): full category index
- [Enhanced Content Control Utility (ECCU) API](https://techdocs.akamai.com/eccu/reference/api.md)
- [API summary](https://techdocs.akamai.com/eccu/reference/api-summary.md)
- [Get started](https://techdocs.akamai.com/eccu/reference/get-started.md)
- [Rate limits](https://techdocs.akamai.com/eccu/reference/rate-limits.md)
- [API workflow](https://techdocs.akamai.com/eccu/reference/api-workflow.md)
- [Errors](https://techdocs.akamai.com/eccu/reference/errors.md)
- [400](https://techdocs.akamai.com/eccu/reference/400-1.md)
- [401](https://techdocs.akamai.com/eccu/reference/401.md)
- [403](https://techdocs.akamai.com/eccu/reference/403.md)
- [404](https://techdocs.akamai.com/eccu/reference/404.md)
- [405](https://techdocs.akamai.com/eccu/reference/405.md)
- [408](https://techdocs.akamai.com/eccu/reference/408.md)
- [415](https://techdocs.akamai.com/eccu/reference/415.md)
- [500](https://techdocs.akamai.com/eccu/reference/500.md)
- [503](https://techdocs.akamai.com/eccu/reference/503.md)

## API Reference: Permissions

- [Permissions index](https://techdocs.akamai.com/eccu/reference/permissions/llms.txt): full category index
- [List permissions](https://techdocs.akamai.com/eccu/reference/get-permissions.md): Returns the ECCU permissions. If the response's `submitEccuRequest` member is enabled, you can run the [Create an ECCU request](ref:post-request) operation to invalidate content.

## API Reference: Properties

- [Properties index](https://techdocs.akamai.com/eccu/reference/properties/llms.txt): full category index
- [List properties](https://techdocs.akamai.com/eccu/reference/get-properties.md): Returns the digital properties that you can apply ECCU refresh requests to.

## API Reference: Requests

- [Requests index](https://techdocs.akamai.com/eccu/reference/requests/llms.txt): full category index
- [Create an ECCU request](https://techdocs.akamai.com/eccu/reference/post-request.md): Creates a new ECCU refresh request.
- [List ECCU requests](https://techdocs.akamai.com/eccu/reference/get-requests.md): Returns a summary of submitted  ECCU refresh requests under your account. Use this to view the `status` of all refresh requests.
- [Get an ECCU request](https://techdocs.akamai.com/eccu/reference/get-request.md): Returns a submitted refresh request. Run this operation if you want details on the request's `metadata`. Otherwise, you can run [List ECCU requests](ref:get-requests) to check the `status` of all refresh requests.
- [Remove an ECCU request](https://techdocs.akamai.com/eccu/reference/delete-request.md): Removes the refresh request from the  list of submitted requests only. This operation doesn't stop the refresh request from being processed.
