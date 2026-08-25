# Edge Diagnostics Documentation

> Edge Diagnostics allows you to diagnose your server, DNS, and network problems from Akamai servers around the world.

Fetch the complete documentation index at: https://techdocs.akamai.com/edge-diagnostics/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: URL Health Check
- [Run the URL health check](https://techdocs.akamai.com/edge-diagnostics/reference/post-url-health-check.md): Launches an [asynchronous](ref:asynchronous-processes) request to simultaneously run [Launch a GREP request](ref:post-grep), [Get domain details with dig](ref:post-dig), [Request content with cURL](ref:post-curl), [Test network connectivity with MTR](ref:post-mtr) and [Translate an Akamaized URL](ref:post-translated-url) operations for a URL. Successful operations return fetched GREP, dig, cURL, and MTR data and [Akamaized URL (ARL)](doc:arl-syntax) details.
- [Get a URL health check response](https://techdocs.akamai.com/edge-diagnostics/reference/get-url-health-check-requests.md): Returns the status of the [asynchronous](ref:asynchronous-processes) [Run the URL health check](ref:post-url-health-check) request. Operations with the `SUCCESS` status include also fetched GREP, dig, cURL, and MTR data.
