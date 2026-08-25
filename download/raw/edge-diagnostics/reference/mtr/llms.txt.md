# Edge Diagnostics Documentation

> Edge Diagnostics allows you to diagnose your server, DNS, and network problems from Akamai servers around the world.

Fetch the complete documentation index at: https://techdocs.akamai.com/edge-diagnostics/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: MTR
- [Test network connectivity with MTR](https://techdocs.akamai.com/edge-diagnostics/reference/post-mtr.md): Uses MTR to provide information about packet loss and latency between an edge server IP, location, or Site Shield map and a remote destination. To run this operation for an IP, you may need to [verify an IP](ref:post-verify-edge-ip) if it belongs to an edge server. To run this operation for a GTM hostname, run [List GTM properties](ref:get-gtm-properties) and [List test and target IPs for a GTM hostname](ref:get-gtm-property-domain-gtm-property-ips) operations first to get the test and target IPs for the hostname.
