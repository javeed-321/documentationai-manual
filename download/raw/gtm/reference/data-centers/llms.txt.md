# Global Traffic Management Documentation

> Akamai's Global Traffic Management (GTM) helps Internet users access your website or IP applications with greater reliability. It applies an Internet-centric approach to global load balancing to increase site availability and responsiveness to online user requests. Unlike traditional hardware-based solutions that reside within data centers, the fault-tolerant Global Traffic Management service makes intelligent routing decisions. These are based on real-time data center performance health and on global Internet conditions. They transport user requests to the appropriate data center based on the best Internet route for that user at that moment.

Fetch the complete documentation index at: https://techdocs.akamai.com/gtm/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

## API Reference: Data centers
- [Create a data center](https://techdocs.akamai.com/gtm/reference/post-datacenter.md): This operation creates a specific data center.
- [List data centers](https://techdocs.akamai.com/gtm/reference/get-datacenters.md): This operation returns a list of data centers.
- [Create an IPv4 data center for ip-version-selector](https://techdocs.akamai.com/gtm/reference/post-datacenter-for-ipv.md): This operation creates a data center which is solely reserved for use by properties of the IP Version Selector type `qtr`. The data center created by this resource  is assigned the `datacenterId` 5401, which is interpreted as the target for `A` record requests.
- [Create an IPv6 data center for ip-version-selector](https://techdocs.akamai.com/gtm/reference/post-datacenter-for-ipv6.md): This operation creates a data center which is solely reserved for use by properties of type `qtr` (IP Version Selector). The data center created by this resource  is assigned the `datacenterId` 5402, which is interpreted as the target for `AAAA` record requests.
- [Create a default data center](https://techdocs.akamai.com/gtm/reference/post-default-datacenter-for-maps.md): This operation creates a data center for use by the map-type properties CIDR, Geographic or AS mapping as the default data center.
- [Get a data center](https://techdocs.akamai.com/gtm/reference/get-datacenter.md): This operation returns information for a specific data center.
- [Update a data center](https://techdocs.akamai.com/gtm/reference/put-datacenter.md): This operation updates a specific data center.
- [Remove a data center](https://techdocs.akamai.com/gtm/reference/delete-datacenter.md): Remove a data center: This operation removes a data center. You can only remove a data center when no properties or resources are assigned to it.
