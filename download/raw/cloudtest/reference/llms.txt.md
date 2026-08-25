# CloudTest Documentation

> Using Akamai's CloudTest to optimize your approach to load testing with a scalable, global platform. CloudTest provides testing capabilities for web and mobile apps, APIs, databases, and web services. Realtime analytics and customizable dashboards provide actionable intelligence, allowing for root-cause analysis while tests run.

Fetch the complete documentation index at: https://techdocs.akamai.com/cloudtest/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: API

- [API index](https://techdocs.akamai.com/cloudtest/reference/api/llms.txt): full category index
- [CloudTest API](https://techdocs.akamai.com/cloudtest/reference/api.md)
- [API summary](https://techdocs.akamai.com/cloudtest/reference/api-summary.md)
- [Get started](https://techdocs.akamai.com/cloudtest/reference/get-started.md)
- [API concepts](https://techdocs.akamai.com/cloudtest/reference/api-concepts.md)
- [Rate limiting](https://techdocs.akamai.com/cloudtest/reference/rate-limiting.md)
- [Asynchronous operations](https://techdocs.akamai.com/cloudtest/reference/asynchronous-operations.md)
- [Errors](https://techdocs.akamai.com/cloudtest/reference/errors.md)
- [400](https://techdocs.akamai.com/cloudtest/reference/400.md)
- [401](https://techdocs.akamai.com/cloudtest/reference/401.md)
- [403](https://techdocs.akamai.com/cloudtest/reference/403.md)
- [404](https://techdocs.akamai.com/cloudtest/reference/404.md)
- [405](https://techdocs.akamai.com/cloudtest/reference/405.md)
- [429](https://techdocs.akamai.com/cloudtest/reference/429.md)
- [500](https://techdocs.akamai.com/cloudtest/reference/500.md)

## API Reference: Cloud servers

- [Cloud servers index](https://techdocs.akamai.com/cloudtest/reference/cloud-servers/llms.txt): full category index
- [List cloud servers](https://techdocs.akamai.com/cloudtest/reference/get-cloud-servers.md): Returns an array of cloud servers.
- [Get a cloud server](https://techdocs.akamai.com/cloudtest/reference/get-cloud-server.md): Returns a single cloud server.
- [Restart or terminate a cloud server](https://techdocs.akamai.com/cloudtest/reference/post-cloud-server-action.md): Either `restart` or `terminate` a cloud server. The operation responds asynchronously with 202. See [Asynchronous operations](ref:asynchronous-operations) for details.

## API Reference: Test environments

- [Test environments index](https://techdocs.akamai.com/cloudtest/reference/test-environments/llms.txt): full category index
- [Get a test environment](https://techdocs.akamai.com/cloudtest/reference/get-environment.md): Returns a single test environment.
- [Start or stop a test environment](https://techdocs.akamai.com/cloudtest/reference/post-environment-action.md): Either `start` or `stop` a test environment. The operation responds either synchronously with a 200 code, or asynchronously with 202. See [Asynchronous operations](ref:asynchronous-operations) for details.

## API Reference: Grid provisioning

- [Grid provisioning index](https://techdocs.akamai.com/cloudtest/reference/grid-provisioning/llms.txt): full category index
- [List grids](https://techdocs.akamai.com/cloudtest/reference/get-grids.md): Returns an array of grids. Retrieves a list of Grids that have been started. It may include `TERMINATED` grids.  It doesn't return grids that exist in the repository but are inactive.
- [Get a grid](https://techdocs.akamai.com/cloudtest/reference/get-grid.md): Returns information about a single grid.
- [Start or stop a grid](https://techdocs.akamai.com/cloudtest/reference/post-grid-action.md): Start or stop a grid. The operation responds either synchronously with a 200 code, or asynchronously with 202. See [Asynchronous operations](ref:asynchronous-operations) for details.

## API Reference: Compositions

- [Compositions index](https://techdocs.akamai.com/cloudtest/reference/compositions/llms.txt): full category index
- [Start or load a composition](https://techdocs.akamai.com/cloudtest/reference/post-composition.md): Start or load a test instance.
- [List active compositions](https://techdocs.akamai.com/cloudtest/reference/get-compositions.md): Get all instances that are in some type of active state. After tests are complete the instances are unloaded and the API can no longer return them, these are considered inactive. Because this call uses an asynchronous process to get the list of instances, if there are many load generators you should run a second call to ensure you get the most complete list of instances.
- [Get a composition](https://techdocs.akamai.com/cloudtest/reference/get-composition.md): Returns a single composition instance.
- [Composition commands](https://techdocs.akamai.com/cloudtest/reference/put-composition-action.md): The composition commands you use on a test instance are: play, stop, abort, pause, resume, unload. The return of the command doesn't imply that the action is complete. To get the current state of the instance, use the [Get a composition](ref:get-composition) command.

## API Reference: Objects

- [Objects index](https://techdocs.akamai.com/cloudtest/reference/objects/llms.txt): full category index
- [List objects](https://techdocs.akamai.com/cloudtest/reference/get-objects-attribute.md): Gets a list of repository objects, filtered by attributes.
- [Create an object](https://techdocs.akamai.com/cloudtest/reference/put-object.md): Creates an object.
- [Update an object](https://techdocs.akamai.com/cloudtest/reference/post-objects.md): Update a repository object.
- [Get an object](https://techdocs.akamai.com/cloudtest/reference/get-object.md): Gets a repository object by type and ID.
- [Delete an object](https://techdocs.akamai.com/cloudtest/reference/delete-objects.md): Delete a repository object.
- [Transfer object ownership](https://techdocs.akamai.com/cloudtest/reference/post-mass-change-owner.md): Transfers the owner status for all entities within the Mains and CloudTest Manager (CTM) environments between users.

## API Reference: Results management

- [Results management index](https://techdocs.akamai.com/cloudtest/reference/results-management/llms.txt): full category index
- [Request a delete of test results](https://techdocs.akamai.com/cloudtest/reference/post-result-delete.md): This action submits a background task to delete results. It returns a jobId.  Use the jobId to make subsequent calls to track the status of the task.
- [List results management tasks](https://techdocs.akamai.com/cloudtest/reference/get-management-tasks.md): Get a list of all tasks.
- [Get a results management task](https://techdocs.akamai.com/cloudtest/reference/get-mgmt-task.md): Returns task info for the specified task.
- [Stop a results management task](https://techdocs.akamai.com/cloudtest/reference/delete-mgmt-task.md): Attempts to stop a task.  Stopping a task doesn't undo any deleted results. It just tells the task to stop as quickly as it can. A status of `STOPPED` means that the task was stopped before it completed. A status of `COMPLETED` means that the task completed before it received the stop command.

## API Reference: Query results

- [Query results index](https://techdocs.akamai.com/cloudtest/reference/query-results/llms.txt): full category index
- [List results](https://techdocs.akamai.com/cloudtest/reference/get-results.md): Get a list of all results that satisfy the query.
- [Get a result](https://techdocs.akamai.com/cloudtest/reference/get-result.md): Returns summary info for the specified result.
- [Get ramp and marker data](https://techdocs.akamai.com/cloudtest/reference/get-ramp-info-by-resultid.md): Get the Ramp/Marker Information for each result.
- [Get aggregate action data](https://techdocs.akamai.com/cloudtest/reference/get-clip-element-metrics.md): Queries action-related metrics (such as HTTP messages or database actions) from a result with grouping/aggregation by location, time in seconds or minutes, network profile, element type, or element name. Use this to get the number of HTTP 404 errors or compute the average response time or determine which assets contained the largest number of bytes.
- [Get aggregate collection data](https://techdocs.akamai.com/cloudtest/reference/get-collection-metrics.md): Queries collection related metrics (such as pages or transactions) from a result with grouping/aggregation by location, time in seconds or minutes, network profile, element type, or element name. Use this to determine page load time or transactions per second (tps) or get the 90th percentile for a transaction.
- [List load generators](https://techdocs.akamai.com/cloudtest/reference/get-load-generator-info-by-resultid.md): Get the load generators and the location for each result.
- [Get virtual user count](https://techdocs.akamai.com/cloudtest/reference/get-virtual-users-metrics.md): Get the number of virtual users for each minute of the test.
- [Get a virtual user count time series](https://techdocs.akamai.com/cloudtest/reference/get-virtual-users-metrics-by-interval.md): Get the number of virtual users and peak virtual users within the requested interval (second/minute/hour).

## API Reference: Results database

- [Results database index](https://techdocs.akamai.com/cloudtest/reference/results-database/llms.txt): full category index
- [Get a results database](https://techdocs.akamai.com/cloudtest/reference/get-rsdb.md): Returns a single rsdb.  In order to interact with a result database you need the results database ID.  See [Get an object](https://techdocs.akamai.com/cloudtest/reference/get-object) for more information.
- [Start or stop a results database](https://techdocs.akamai.com/cloudtest/reference/post-action.md): Either `start`, `stop` or `terminate` a results database.  The `start` and `terminate` actions are asynchronous and return a 202.  A `stop` command is synchronous and returns a 200.  See [Asynchronous operations](ref:asynchronous-operations) for details.  In order to interact with a result database you need the results database ID.  See [Get an object](https://techdocs.akamai.com/cloudtest/reference/get-object) for more information.

## API Reference: Seed data

- [Seed data index](https://techdocs.akamai.com/cloudtest/reference/seed-data/llms.txt): full category index
- [Append seed data](https://techdocs.akamai.com/cloudtest/reference/post-seed-data.md): Appends CSV content to existing seed data.  The `.csv` file is sent as a part of the request payload.
- [Get seed data](https://techdocs.akamai.com/cloudtest/reference/get-seed-data.md): Returns seed data content as CSV.
- [Delete seed data](https://techdocs.akamai.com/cloudtest/reference/delete-seed-data.md): Removes seed data from the repository.

## API Reference: Server management

- [Server management index](https://techdocs.akamai.com/cloudtest/reference/server-management/llms.txt): full category index
- [List servers](https://techdocs.akamai.com/cloudtest/reference/get-servers.md): Get a list of all servers listed in the server list.  You need to have server access privileges to access this operation.
- [Get a server](https://techdocs.akamai.com/cloudtest/reference/get-server.md): Returns server info for the specified server. You need to have server access privileges to access this operation.

## API Reference: Tenant management

- [Tenant management index](https://techdocs.akamai.com/cloudtest/reference/tenant-management/llms.txt): full category index
- [Initiate tenant sub-data deletion](https://techdocs.akamai.com/cloudtest/reference/post-tenant-subdata-delete.md): This action submits a background task to delete results and monitors under given tenant for passed auth token. It returns a jobId.  Use the jobId to make subsequent calls to track the status of the task.
- [List tenant management tasks](https://techdocs.akamai.com/cloudtest/reference/get-tenant-mgmt-tasks.md): Get a list of all tasks.
- [Get a tenant management task](https://techdocs.akamai.com/cloudtest/reference/get-tenant-mgmt-task.md): Returns a specific task.
- [Stop a tenant management task](https://techdocs.akamai.com/cloudtest/reference/delete-tenant-mgmt-task.md): Attempts to stop a task.  Stopping a task doesn't undo any deleted results but stops the task as quickly as possible. A status of `STOPPED` means that the task was stopped before it completed. A status of `COMPLETED` means that the task completed before it received the instruction to stop.

## API Reference: Tokens

- [Tokens index](https://techdocs.akamai.com/cloudtest/reference/tokens/llms.txt): full category index
- [Generate a token](https://techdocs.akamai.com/cloudtest/reference/put-token.md): Authenticates and generates a token. The security token expires after five hours of inactivity.
- [Delete a token](https://techdocs.akamai.com/cloudtest/reference/delete-token.md): Delete a token so it can no longer be used for authentication with the API.
