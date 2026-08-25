# Purge Cache Documentation

> Akamai’s Purge Cache web interface on Control Center lets you refresh specific cached objects or remove all objects across Akamai’s edge network in just a few seconds. You can filter objects by URLs, Content Provider (CP) codes, or cache tags. Removing cached objects allows you to quickly correct mistakes in your published content.

Fetch the complete documentation index at: https://techdocs.akamai.com/purge-cache/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: API

- [API index](https://techdocs.akamai.com/purge-cache/reference/api/llms.txt): full category index
- [Fast Purge API v3](https://techdocs.akamai.com/purge-cache/reference/api.md)
- [API summary](https://techdocs.akamai.com/purge-cache/reference/api-summary.md)
- [Get started](https://techdocs.akamai.com/purge-cache/reference/api-get-started.md)
- [Rate limiting](https://techdocs.akamai.com/purge-cache/reference/rate-limiting.md)
- [Rate limit response examples](https://techdocs.akamai.com/purge-cache/reference/rate-limit-response-examples.md)
- [Errors](https://techdocs.akamai.com/purge-cache/reference/api-errors.md)
- [400](https://techdocs.akamai.com/purge-cache/reference/400.md)
- [401](https://techdocs.akamai.com/purge-cache/reference/401.md)
- [403](https://techdocs.akamai.com/purge-cache/reference/403.md)
- [404](https://techdocs.akamai.com/purge-cache/reference/404.md)
- [405](https://techdocs.akamai.com/purge-cache/reference/405.md)
- [408](https://techdocs.akamai.com/purge-cache/reference/408.md)
- [410](https://techdocs.akamai.com/purge-cache/reference/410.md)
- [411](https://techdocs.akamai.com/purge-cache/reference/411.md)
- [413](https://techdocs.akamai.com/purge-cache/reference/413.md)
- [415](https://techdocs.akamai.com/purge-cache/reference/415.md)
- [429](https://techdocs.akamai.com/purge-cache/reference/429.md)
- [500](https://techdocs.akamai.com/purge-cache/reference/500.md)
- [503](https://techdocs.akamai.com/purge-cache/reference/503.md)
- [504](https://techdocs.akamai.com/purge-cache/reference/504.md)
- [507](https://techdocs.akamai.com/purge-cache/reference/507.md)

## API Reference: Invalidations

- [Invalidations index](https://techdocs.akamai.com/purge-cache/reference/invalidations/llms.txt): full category index
- [Invalidate by CP code](https://techdocs.akamai.com/purge-cache/reference/post-invalidate-cpcode.md): Invalidates content on the selected CP code for the selected `network`. You should consider invalidating content by default. This keeps each object in cache until the version on your origin server is newer. Deletion retrieves the object regardless, which can dramatically increase the load on your origin server and would prevent Akamai from serving the old content if your origin is unreachable.
- [Invalidate by cache tag](https://techdocs.akamai.com/purge-cache/reference/post-invalidate-tag.md): Invalidates content on the selected set of cache tags for the selected `network`. You should consider invalidating content by default. This keeps each object in cache until the version on your origin server is newer. Deletion retrieves the object regardless, which can dramatically increase the load on your origin server and would prevent Akamai from serving the old content if your origin is unreachable.
- [Invalidate by URL or ARL](https://techdocs.akamai.com/purge-cache/reference/post-invalidate-url.md): Invalidates content on the selected URL or ARL for the selected `network`. You should consider invalidating content by default. This keeps each object in cache until the version on your origin server is newer. Deletion retrieves the object regardless, which can dramatically increase the load on your origin server and would prevent Akamai from serving the old content if your origin is unreachable. URLs and ARLs can be submitted in the same request.

## API Reference: Deletions

- [Deletions index](https://techdocs.akamai.com/purge-cache/reference/deletions/llms.txt): full category index
- [Delete by cache tag](https://techdocs.akamai.com/purge-cache/reference/post-delete-tag.md): Deletes content on the selected set of cache tags for the selected `network`. In most cases, you should [invalidate](ref:post-invalidate-tag) rather than delete content. Invalidation keeps each object in cache until the version on your origin server is newer. Deletion retrieves the object regardless, which can dramatically increase the load on your origin server and would prevent Akamai from serving the old content if your origin is unreachable.
- [Delete by URL or ARL](https://techdocs.akamai.com/purge-cache/reference/post-delete-url.md): Deletes content on the selected URL or ARL  for the selected `network`.  URLs and ARLs can be submitted in the same request. In most cases, you should [invalidate](ref:post-invalidate-url) rather than delete content. Invalidation keeps each object in cache until the version on your origin server is newer. Deletion retrieves the object regardless, which can dramatically increase the load on your origin server and would prevent Akamai from serving the old content if your origin is unreachable.
- [Delete by CP code](https://techdocs.akamai.com/purge-cache/reference/post-delete-cpcode.md): Deletes content on the selected CP code for the selected `network`. In most cases, you should [invalidate](ref:post-invalidate-cpcode) rather than delete content. Invalidation keeps each object in cache until the version on your origin server is newer. Deletion retrieves the object regardless, which can dramatically increase the load on your origin server and would prevent Akamai from serving the old content if your origin is unreachable.

## API Reference: Rate limit status

- [Rate limit status index](https://techdocs.akamai.com/purge-cache/reference/rate-limit-status/llms.txt): full category index
- [Check rate and object limit statuses](https://techdocs.akamai.com/purge-cache/reference/post-rate-limit-status.md): The Fast Purge API uses a token bucket model for [rate limiting](ref:rate-limiting) to protect itself from inadvertent or malicious overuse. For each Akamai account, there's a rate limit shared by all object types (CP codes, cache tags, and URL/ARLs), and three separate resource limits for each object type. Each purge request uses one rate limit token from the requests bucket. Each purge object in a request takes up a token from the resource bucket. This operation fetches information on the remaining number of requests and objects for a specific account. You can use these details to monitor the request consumption or throttle requests to prevent exceeding the limits, which results in the [429](ref:429) error.
