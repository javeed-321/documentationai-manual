# Enhanced Content Control Utility API Documentation

> The Enhanced Content Control Utility (ECCU) is one of several supported Akamai purge interfaces. Use ECCU to specify the set of files to refresh on the edge network. Specify directories, file extensions, certain types of HTTP request, or response properties to refine the set of content to refresh. For example, you can refresh specific parts of a library or the complete cache repository for many domains. The ECCU only invalidates content. It does not remove content from cache.

Fetch the complete documentation index at: https://techdocs.akamai.com/eccu/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: Permissions
- [List permissions](https://techdocs.akamai.com/eccu/reference/get-permissions.md): Returns the ECCU permissions. If the response's `submitEccuRequest` member is enabled, you can run the [Create an ECCU request](ref:post-request) operation to invalidate content.
