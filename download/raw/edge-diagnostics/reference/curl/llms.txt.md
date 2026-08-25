# Edge Diagnostics Documentation

> Edge Diagnostics allows you to diagnose your server, DNS, and network problems from Akamai servers around the world.

Fetch the complete documentation index at: https://techdocs.akamai.com/edge-diagnostics/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: CURL
- [Request content with cURL](https://techdocs.akamai.com/edge-diagnostics/reference/post-curl.md): Requests content using the `curl` command to provide the raw HTML for a URL, including request headers. You can run this operation for a specific location, an edge server IP, or a Site Shield map. If you want to get the data for a location, you need to run the [List available edge server locations](ref:get-edge-locations) operation first to get `edgeLocationId`. And if you want to run this operation for an IP,  you may need to [verify an IP](ref:post-verify-edge-ip) to check if it belongs to an edge server. If you provide neither a location nor an edge server IP, then Edge Diagnostics runs the operation using a random edge server IP.
