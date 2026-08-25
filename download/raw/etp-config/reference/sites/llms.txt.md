# SIA Configuration API Documentation

> Akamai's Secure Internet Access (SIA) Configuration API offers a programmatic interface to manage policy settings to protect against enterprise security and acceptable user policy related events. A distributed configuration encapsulates all the rules for how to process DNS requests for your enterprise.

Fetch the complete documentation index at: https://techdocs.akamai.com/etp-config/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: Sites
- [List DNS VIPs](https://techdocs.akamai.com/etp-config/reference/get-dns-vips.md): Provides DNS virtual IP details.
- [Get global settings](https://techdocs.akamai.com/etp-config/reference/get-global-settings.md): Provides global settings details.
- [Update global settings](https://techdocs.akamai.com/etp-config/reference/put-global-settings.md): Updates the global settings.
- [Create a site](https://techdocs.akamai.com/etp-config/reference/post-sites.md): Creates a new site.
- [List sites](https://techdocs.akamai.com/etp-config/reference/get-sites.md): Returns all sites for a configuration.
- [Get site metadata](https://techdocs.akamai.com/etp-config/reference/get-sites-meta-info.md): Provides site meta info details.
- [Bulk create sites](https://techdocs.akamai.com/etp-config/reference/post-sites-bulk-upload.md): Uploads sites in bulk using a CSV file: - maximum of 100 sites per file - supports comma-delimited or tab-delimited files - must include all headers in the file.
- [Get a site](https://techdocs.akamai.com/etp-config/reference/get-site.md): Returns the details of a specific Site.
- [Update a site](https://techdocs.akamai.com/etp-config/reference/put-site.md): Modifies site details.
- [Assign a policy to a site](https://techdocs.akamai.com/etp-config/reference/post-sublocation-policy.md): Assigns a policy to the site.
- [Remove a site](https://techdocs.akamai.com/etp-config/reference/delete-site.md): Deletes a specific site. Add an `If-Match` header to prevent deleting any data another client has modified since you last accessed it.
- [Create a sublocation](https://techdocs.akamai.com/etp-config/reference/post-site-sublocation.md): Creates a sublocation.
- [List sublocations](https://techdocs.akamai.com/etp-config/reference/get-site-sublocations.md): Returns the list of sublocations for the site.
- [Get a sublocation](https://techdocs.akamai.com/etp-config/reference/get-site-sublocation.md): Returns a sublocation detail.
- [Update a sublocation](https://techdocs.akamai.com/etp-config/reference/put-site-sublocation.md): Updates the sublocation.
- [Remove a sublocation](https://techdocs.akamai.com/etp-config/reference/delete-site-sublocation.md): Deletes a specific sublocation. Add an `If-Match` header to prevent deleting any data another client has modified since you last accessed it.
