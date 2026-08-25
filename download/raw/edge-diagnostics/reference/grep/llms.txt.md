# Edge Diagnostics Documentation

> Edge Diagnostics allows you to diagnose your server, DNS, and network problems from Akamai servers around the world.

Fetch the complete documentation index at: https://techdocs.akamai.com/edge-diagnostics/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: GREP
- [Launch a GREP request](https://techdocs.akamai.com/edge-diagnostics/reference/post-grep.md): Launches an [asynchronous](ref:asynchronous-processes) request to fetch logs for an edge server IP address using the `grep` command.  To verify if an IP belongs to an edge server, run the [Verify an IP](ref:post-verify-edge-ip) operation first. If you known the exact values to filter the logs by and you want to get the data directly, run the synchronous [Get specific logs](ref:get-grep) operation.
- [Get specific logs](https://techdocs.akamai.com/edge-diagnostics/reference/get-grep.md): Using the `grep` command, returns logs that match the query parameters. This operation gets the data  directly. If you don't have detailed information about the logs or you want to avoid latency, run the [Launch a GREP request](ref:post-grep) operation. If you provide request parameters  for which Edge Diagnostics doesn't find logs, you get the validation error.
- [Check a GREP request status](https://techdocs.akamai.com/edge-diagnostics/reference/get-grep-request.md): Returns the status of the [asynchronous](ref:asynchronous-processes) [Launch a GREP request](ref:post-grep) request.  Operations with the `SUCCESS` status include also the `grep` logs.
