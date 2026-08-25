# Adaptive Media Delivery Documentation

> Delivers streaming video and a quality viewing experience anywhere by adapting real-time to available bandwidth. To meet consumer expectations in a hyperconnected world, content providers need a high-performance streaming media delivery solution like Akamai’s Adaptive Media Delivery. Optimized for Adaptive Bitrate (ABR) streaming, it provides a high-quality viewing experience across the broad variety of network types, fixed or mobile, at varying connection speeds. Because it’s built on the Akamai Intelligent Platform, Adaptive Media Delivery provides superior scalability, reliability, and availability.

Fetch the complete documentation index at: https://techdocs.akamai.com/adaptive-media-delivery/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: Welcome

- [Welcome index](https://techdocs.akamai.com/adaptive-media-delivery/reference/welcome/llms.txt): full category index
- [Adaptive Media Delivery APIs](https://techdocs.akamai.com/adaptive-media-delivery/reference/adaptive-media-apis.md)

## API Reference: AMD's Access Revocation API

- [AMD's Access Revocation API index](https://techdocs.akamai.com/adaptive-media-delivery/reference/amds-access-revocation-api/llms.txt): full category index
- [Access Revocation API](https://techdocs.akamai.com/adaptive-media-delivery/reference/api.md)
- [API summary](https://techdocs.akamai.com/adaptive-media-delivery/reference/api-summary.md)
- [Get started](https://techdocs.akamai.com/adaptive-media-delivery/reference/get-started.md)
- [Concepts](https://techdocs.akamai.com/adaptive-media-delivery/reference/concepts.md)
- [API workflow](https://techdocs.akamai.com/adaptive-media-delivery/reference/api-workflow.md)
- [Rate limiting](https://techdocs.akamai.com/adaptive-media-delivery/reference/rate-limiting.md)
- [Errors](https://techdocs.akamai.com/adaptive-media-delivery/reference/api-errors.md)
- [400](https://techdocs.akamai.com/adaptive-media-delivery/reference/400.md)
- [401](https://techdocs.akamai.com/adaptive-media-delivery/reference/401.md)
- [403](https://techdocs.akamai.com/adaptive-media-delivery/reference/403.md)
- [404](https://techdocs.akamai.com/adaptive-media-delivery/reference/404.md)
- [405](https://techdocs.akamai.com/adaptive-media-delivery/reference/405.md)
- [415](https://techdocs.akamai.com/adaptive-media-delivery/reference/415.md)
- [429](https://techdocs.akamai.com/adaptive-media-delivery/reference/429.md)
- [500](https://techdocs.akamai.com/adaptive-media-delivery/reference/500.md)

## API Reference: Access Revocation

- [Access Revocation index](https://techdocs.akamai.com/adaptive-media-delivery/reference/access-revocation/llms.txt): full category index
- [Add a revocation list](https://techdocs.akamai.com/adaptive-media-delivery/reference/post-revocation-list.md): Add a new list to house token identifiers that you want revoked from access. You can have a total of 10 revocation lists. You can't modify these settings for a revocation list, so be sure you provide the proper details when adding one. However, you can [revoke](ref:post-revocation-list-ids) or [unrevoke](ref:post-unrevoke-revocation-list-ids) token identifiers from each revocation list, as necessary.
- [List revocation lists](https://techdocs.akamai.com/adaptive-media-delivery/reference/get-revocation-lists.md): List all of your revocation lists and view details about them.
- [Delete a revocation list](https://techdocs.akamai.com/adaptive-media-delivery/reference/delete-revocation-list.md): Delete a specific revocation list. This removes support for Access Revocation in any AMD property that may have this revocation list currently selected for use.
- [List identifiers](https://techdocs.akamai.com/adaptive-media-delivery/reference/get-revocation-list-ids.md): List all identifiers for a specific revocation list to review their details.
- [Revoke tokens](https://techdocs.akamai.com/adaptive-media-delivery/reference/post-revocation-list-ids.md): Add a set of token identifiers to a revocation list to revoke them. Add up to 5,000 token identifiers in a single operation.
- [Unrevoke tokens](https://techdocs.akamai.com/adaptive-media-delivery/reference/post-unrevoke-revocation-list-ids.md): Remove token identifiers from a revocation list.
- [Get an identifier](https://techdocs.akamai.com/adaptive-media-delivery/reference/get-revocation-list-token.md): Get a specific identifier that belongs to a revocation list and review its details.
- [Get a revocation list's identifier count](https://techdocs.akamai.com/adaptive-media-delivery/reference/get-revocation-list-meta.md): Get the current count and maximum number of identifiers allowed in the revocation list.
- [List revocation list ARL properties](https://techdocs.akamai.com/adaptive-media-delivery/reference/get-revocation-list-properties.md): Get Property Manager-specific information for AMD properties that use this revocation list.
