# Edge Diagnostics Documentation

> Edge Diagnostics allows you to diagnose your server, DNS, and network problems from Akamai servers around the world.

Fetch the complete documentation index at: https://techdocs.akamai.com/edge-diagnostics/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: DIG
- [Get domain details with dig](https://techdocs.akamai.com/edge-diagnostics/reference/post-dig.md): Uses the `dig` command to provide DNS details for the location  of an edge server, a hostname or a domain name, or a GTM hostname. The results may help you diagnose issues with domain name resolutions.  You can run this operation either for a specific location or an edge IP. If you want to get the data for a location, you need to run the [List available edge server locations](ref:get-edge-locations) operation first to get `edgeLocationId`. To run this operation for an IP,  you may need to [verify an IP](ref:post-verify-edge-ip), if it belongs to an edge server. And to run this operation for a GTM hostname, you need to run the [List GTM properties](ref:get-gtm-properties) operation first. If you don't provide neither a location ID nor an edge server IP, then Edge Diagnostics runs the operation using a random edge server IP.
