# CloudTest Documentation

> Using Akamai's CloudTest to optimize your approach to load testing with a scalable, global platform. CloudTest provides testing capabilities for web and mobile apps, APIs, databases, and web services. Realtime analytics and customizable dashboards provide actionable intelligence, allowing for root-cause analysis while tests run.

Fetch the complete documentation index at: https://techdocs.akamai.com/cloudtest/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: Grid provisioning
- [List grids](https://techdocs.akamai.com/cloudtest/reference/get-grids.md): Returns an array of grids. Retrieves a list of Grids that have been started. It may include `TERMINATED` grids.  It doesn't return grids that exist in the repository but are inactive.
- [Get a grid](https://techdocs.akamai.com/cloudtest/reference/get-grid.md): Returns information about a single grid.
- [Start or stop a grid](https://techdocs.akamai.com/cloudtest/reference/post-grid-action.md): Start or stop a grid. The operation responds either synchronously with a 200 code, or asynchronously with 202. See [Asynchronous operations](ref:asynchronous-operations) for details.
