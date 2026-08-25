# CloudTest Documentation

> Using Akamai's CloudTest to optimize your approach to load testing with a scalable, global platform. CloudTest provides testing capabilities for web and mobile apps, APIs, databases, and web services. Realtime analytics and customizable dashboards provide actionable intelligence, allowing for root-cause analysis while tests run.

Fetch the complete documentation index at: https://techdocs.akamai.com/cloudtest/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: Results database
- [Get a results database](https://techdocs.akamai.com/cloudtest/reference/get-rsdb.md): Returns a single rsdb.  In order to interact with a result database you need the results database ID.  See [Get an object](https://techdocs.akamai.com/cloudtest/reference/get-object) for more information.
- [Start or stop a results database](https://techdocs.akamai.com/cloudtest/reference/post-action.md): Either `start`, `stop` or `terminate` a results database.  The `start` and `terminate` actions are asynchronous and return a 202.  A `stop` command is synchronous and returns a 200.  See [Asynchronous operations](ref:asynchronous-operations) for details.  In order to interact with a result database you need the results database ID.  See [Get an object](https://techdocs.akamai.com/cloudtest/reference/get-object) for more information.
