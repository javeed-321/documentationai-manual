# Edge Diagnostics Documentation

> Edge Diagnostics allows you to diagnose your server, DNS, and network problems from Akamai servers around the world.

Fetch the complete documentation index at: https://techdocs.akamai.com/edge-diagnostics/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: GTM properties
- [List GTM properties](https://techdocs.akamai.com/edge-diagnostics/reference/get-gtm-properties.md): Lists GTM properties you have access to. You can use the returned `hostname` values to run [Test network connectivity with MTR](ref:post-mtr) and [Get domain details with dig](ref:post-dig) operations for a GTM hostname. Note, that the [Test network connectivity with MTR](ref:post-mtr) operation requires also hostname's test and target IP values, that you can get with the [List test and target IPs for a GTM hostname](ref:get-gtm-property-domain-gtm-property-ips) operation.
- [List test and target IPs for a GTM hostname](https://techdocs.akamai.com/edge-diagnostics/reference/get-gtm-property-domain-gtm-property-ips.md): Lists test and target IPs for a GTM property. You can use the returned data to run the [Test network connectivity with MTR](ref:post-mtr) operation for a GTM hostname. To get the data necessary for this request, run the [List GTM properties](ref:get-gtm-properties) operation first.
