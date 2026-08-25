# Edge Diagnostics Documentation

> Edge Diagnostics allows you to diagnose your server, DNS, and network problems from Akamai servers around the world.

Fetch the complete documentation index at: https://techdocs.akamai.com/edge-diagnostics/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: Content problems
- [Run the Content problems scenario](https://techdocs.akamai.com/edge-diagnostics/reference/post-content-problems.md): Launches an [asynchronous](ref:asynchronous-processes) request to simultaneously run [Launch a GREP request](ref:post-grep) and [Request content with cURL](ref:post-curl) operations for a URL. It may help you diagnose issues with slow download and high response time. Successful operations return fetched GREP and cURL data.
- [Get the Content problems scenario response](https://techdocs.akamai.com/edge-diagnostics/reference/get-content-problems.md): Returns the status of the [asynchronous](ref:asynchronous-processes) [Run the content problems scenario](ref:post-content-problems) request. Operations with the `SUCCESS` status include fetched GREP and cURL data.
