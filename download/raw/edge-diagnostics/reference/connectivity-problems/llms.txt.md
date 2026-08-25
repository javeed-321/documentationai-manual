# Edge Diagnostics Documentation

> Edge Diagnostics allows you to diagnose your server, DNS, and network problems from Akamai servers around the world.

Fetch the complete documentation index at: https://techdocs.akamai.com/edge-diagnostics/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: Connectivity problems
- [Run the Connectivity problems scenario](https://techdocs.akamai.com/edge-diagnostics/reference/post-connectivity-problems.md): Launches an [asynchronous](ref:asynchronous-processes) request to simultaneously run [Launch a GREP request](ref:post-grep), [Request content with cURL](ref:post-curl), and [Test network connectivity with MTR](ref:post-mtr) operations for a URL. It may help you diagnose issues with slow download and high response time. Successful operations return fetched GREP, cURL, and MTR data.
- [Get the Connectivity problems scenario response](https://techdocs.akamai.com/edge-diagnostics/reference/get-connectivity-problems-request.md): Returns the status of the [asynchronous](ref:asynchronous-processes) [Run the connectivity problems scenario](ref:post-connectivity-problems) request. Operations with the `SUCCESS` status include also fetched GREP, cURL, and MTR data.
