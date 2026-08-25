# CloudTest Documentation

> Using Akamai's CloudTest to optimize your approach to load testing with a scalable, global platform. CloudTest provides testing capabilities for web and mobile apps, APIs, databases, and web services. Realtime analytics and customizable dashboards provide actionable intelligence, allowing for root-cause analysis while tests run.

Fetch the complete documentation index at: https://techdocs.akamai.com/cloudtest/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: Query results
- [List results](https://techdocs.akamai.com/cloudtest/reference/get-results.md): Get a list of all results that satisfy the query.
- [Get a result](https://techdocs.akamai.com/cloudtest/reference/get-result.md): Returns summary info for the specified result.
- [Get ramp and marker data](https://techdocs.akamai.com/cloudtest/reference/get-ramp-info-by-resultid.md): Get the Ramp/Marker Information for each result.
- [Get aggregate action data](https://techdocs.akamai.com/cloudtest/reference/get-clip-element-metrics.md): Queries action-related metrics (such as HTTP messages or database actions) from a result with grouping/aggregation by location, time in seconds or minutes, network profile, element type, or element name. Use this to get the number of HTTP 404 errors or compute the average response time or determine which assets contained the largest number of bytes.
- [Get aggregate collection data](https://techdocs.akamai.com/cloudtest/reference/get-collection-metrics.md): Queries collection related metrics (such as pages or transactions) from a result with grouping/aggregation by location, time in seconds or minutes, network profile, element type, or element name. Use this to determine page load time or transactions per second (tps) or get the 90th percentile for a transaction.
- [List load generators](https://techdocs.akamai.com/cloudtest/reference/get-load-generator-info-by-resultid.md): Get the load generators and the location for each result.
- [Get virtual user count](https://techdocs.akamai.com/cloudtest/reference/get-virtual-users-metrics.md): Get the number of virtual users for each minute of the test.
- [Get a virtual user count time series](https://techdocs.akamai.com/cloudtest/reference/get-virtual-users-metrics-by-interval.md): Get the number of virtual users and peak virtual users within the requested interval (second/minute/hour).
