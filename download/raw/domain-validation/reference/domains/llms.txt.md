# Domain Ownership Manager Documentation

> Domain Ownership Manager (DOM) is a service that prevents unauthorized use of hostnames on the Akamai network and strengthens security. Use the UI or API to prove domain ownership before you onboard new domains and hostnames to Akamai.

Fetch the complete documentation index at: https://techdocs.akamai.com/domain-validation/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: Domains
- [List domains](https://techdocs.akamai.com/domain-validation/reference/get-domains.md): Returns the list of available domains. By default, the results are paginated. You can disable pagination to retrieve all domains at once, but if the number of domains exceeds the allowed limit, the request returns a 409 Conflict error. In that case, use the pagination parameters to retrieve the full set of results.
- [Add domains](https://techdocs.akamai.com/domain-validation/reference/post-domains.md): Add domains to validate.
- [Get a domain](https://techdocs.akamai.com/domain-validation/reference/get-domain.md): Returns a domain.
- [Validate pending domains](https://techdocs.akamai.com/domain-validation/reference/post-validate-domains.md): Immediately validates the domains using the DNS CNAME, DNS TXT, and HTTP methods. Use this operation when you've already updated your DNS or HTTP server and want to skip the standard queue to start the validation now.
- [Invalidate a domain](https://techdocs.akamai.com/domain-validation/reference/post-invalidate-domain.md): Invalidates the specified domain. When you invalidate a domain, Akamai doesn't recognize you as its owner. The domain is then automatically deleted as part of a cleanup procedure. You can also [delete it manually](ref:delete-domain).
- [Invalidate domains](https://techdocs.akamai.com/domain-validation/reference/post-invalidate-domains.md): Invalidates the specified domains. When you invalidate a domain, Akamai doesn't recognize you as its owner. The domain is then automatically deleted as part of a cleanup procedure. You can also [delete it manually](ref:delete-domain).
- [Delete a domain](https://techdocs.akamai.com/domain-validation/reference/delete-domain.md): Deletes a domain validation. You can only delete a domain that is invalidated or has an expired token. When you delete a domain, Akamai doesn't recognize you as its owner. To revalidate a deleted domain, submit it for validation again.
- [Batch-delete domains](https://techdocs.akamai.com/domain-validation/reference/delete-domains.md): Deletes the specified domains. You can only delete domains that are invalidated or have expired tokens. When you delete domains, Akamai doesn't recognize you as their owner. To revalidate deleted domains, submit them for validation again.
- [Search for domains](https://techdocs.akamai.com/domain-validation/reference/post-search-domains.md): Returns the status of specified domains. For any nonexistent domains, the API returns the closest matching domain status.
