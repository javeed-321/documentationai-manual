# CloudTest Documentation

> Using Akamai's CloudTest to optimize your approach to load testing with a scalable, global platform. CloudTest provides testing capabilities for web and mobile apps, APIs, databases, and web services. Realtime analytics and customizable dashboards provide actionable intelligence, allowing for root-cause analysis while tests run.

Fetch the complete documentation index at: https://techdocs.akamai.com/cloudtest/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: Compositions
- [Start or load a composition](https://techdocs.akamai.com/cloudtest/reference/post-composition.md): Start or load a test instance.
- [List active compositions](https://techdocs.akamai.com/cloudtest/reference/get-compositions.md): Get all instances that are in some type of active state. After tests are complete the instances are unloaded and the API can no longer return them, these are considered inactive. Because this call uses an asynchronous process to get the list of instances, if there are many load generators you should run a second call to ensure you get the most complete list of instances.
- [Get a composition](https://techdocs.akamai.com/cloudtest/reference/get-composition.md): Returns a single composition instance.
- [Composition commands](https://techdocs.akamai.com/cloudtest/reference/put-composition-action.md): The composition commands you use on a test instance are: play, stop, abort, pause, resume, unload. The return of the command doesn't imply that the action is complete. To get the current state of the instance, use the [Get a composition](ref:get-composition) command.
