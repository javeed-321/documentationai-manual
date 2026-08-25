# GTM Load Feedback API Documentation

> Akamai's Global Traffic Management Load Feedback API allows users to submit load data for a GTM domain in either JSON or XML format via POST, and to fetch the current load state via GET.

Fetch the complete documentation index at: https://techdocs.akamai.com/gtm-load-feedback/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: Global Traffic Management Load Feedback API
- [Submit load data](https://techdocs.akamai.com/gtm-load-feedback/reference/post-domain-resource.md): Use this action to submit load data. The URL specifies the `domain`, `resource`, and `datacenterId` of the instance to which the load data pertains. The data may be submitted in either XML or JSON format. To support legacy clients, we allow `region` as an alias for `datacenterId`. The timestamp string should be in XSD format.
- [Get load data](https://techdocs.akamai.com/gtm-load-feedback/reference/get-domain-resource.md): Use this action to fetch the load data for a resource instance. The URL format is the same as the POST action. The API returns either XML or JSON, depending on your `Accept` header. If both are specified, or there is no `Accept` header, the default is JSON. In this sample data, we're fetching load for a resource called `connections` in datacenter 100, in the `example.akadns.net` domain.
