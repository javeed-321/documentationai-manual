# SIA Configuration API Documentation

> Akamai's Secure Internet Access (SIA) Configuration API offers a programmatic interface to manage policy settings to protect against enterprise security and acceptable user policy related events. A distributed configuration encapsulates all the rules for how to process DNS requests for your enterprise.

Fetch the complete documentation index at: https://techdocs.akamai.com/etp-config/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: Lists
- [Create a list](https://techdocs.akamai.com/etp-config/reference/post-list.md): Creates a new list.
- [List all lists](https://techdocs.akamai.com/etp-config/reference/get-lists.md): Returns all available custom security lists.
- [List global list quotas](https://techdocs.akamai.com/etp-config/reference/get-lists-quota.md): Returns the remaining list item quota for all lists globally.
- [Get details of a list](https://techdocs.akamai.com/etp-config/reference/get-list.md): Returns the details of a specific list.
- [Update a list](https://techdocs.akamai.com/etp-config/reference/put-config-list.md): Modifies list properties and all items for a specific list. Full update only.
- [Remove a list](https://techdocs.akamai.com/etp-config/reference/delete-config-list.md): Deletes a specific list.
- [Search in a list](https://techdocs.akamai.com/etp-config/reference/get-config-lists-items.md): Filters items in a list by search parameters.
- [Modify list items](https://techdocs.akamai.com/etp-config/reference/put-config-lists-items.md): Updates list items (overwrite).
- [Patch a list](https://techdocs.akamai.com/etp-config/reference/patch-config-list.md): Modifies individual list items entries. Add or delete only.
- [List all Akamai built-in security lists](https://techdocs.akamai.com/etp-config/reference/get-akamai-lists.md): Returns all available Akamai built-in lists.
- [Clear the DNS cache](https://techdocs.akamai.com/etp-config/reference/post-dns-cache.md): Clears the DNS cache for the specified domain.
