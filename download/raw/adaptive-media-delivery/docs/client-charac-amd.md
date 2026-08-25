---
updatedAt: 2026-03-01T18:58:15.000Z
---

Fetch the complete documentation index at: https://techdocs.akamai.com/adaptive-media-delivery/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Client Characteristics

This behavior incorporates use case-based provisioning to optimize delivery to requesting clients.

<div align=center>
<img src="https://techdocs.akamai.com/adaptive-media-delivery/img/amd-client-char-v2.png" width="500" />
</div>

# Client Location

Select a location that is *geographically closest* to the clients accessing content through this property configuration, to optimize the delivery. If you set a region that is closer to your clients, delivery is typically faster.

> 📘
>
> If you're unsure, leave this set to **Unknown**. If you select an inappropriate geographic region, it could negatively affect delivery.

# About mixed-mode configuration

This is a "use case-based" behavior that's used to optimize delivery. You need to keep this behavior in the Default Rule and apply settings. But, with mixed mode configuration for AMD, you can also include it in a child rule and apply different match criteria to have separate requests use different client characteristics optimizations. For more details, see [Mixed Mode & AMD](https://techdocs.akamai.com/adaptive-media-delivery/docs/use-mixed-mode-amd).

# Sibling pages

* [Default optimizations](https://techdocs.akamai.com/adaptive-media-delivery/docs/best-practices-use-case-based-prov.md)
* [Origin Server](https://techdocs.akamai.com/adaptive-media-delivery/docs/origin-server-amd.md)
* [Content Provider Code](https://techdocs.akamai.com/adaptive-media-delivery/docs/content-provider-code-amd.md)
* [Segmented Media Delivery Mode](https://techdocs.akamai.com/adaptive-media-delivery/docs/segmented-media-deliv-mode-amd.md)
* [Origin Characteristics](https://techdocs.akamai.com/adaptive-media-delivery/docs/origin-charac-amd.md)
* [Content Characteristics](https://techdocs.akamai.com/adaptive-media-delivery/docs/content-charac-amd.md)
* [Cache Key Query Parameters](https://techdocs.akamai.com/adaptive-media-delivery/docs/cache-key-query-param-amd.md)
* [Tiered Distribution](https://techdocs.akamai.com/adaptive-media-delivery/docs/tiered-dist-amd.md)
* [Recommended behaviors in the Default Rule](https://techdocs.akamai.com/adaptive-media-delivery/docs/rcmd-behs-default-rule.md)
* [Optional behaviors in the Default Rule](https://techdocs.akamai.com/adaptive-media-delivery/docs/optal-behs-default-rule.md)
* [The Default CORS Policy Rule](https://techdocs.akamai.com/adaptive-media-delivery/docs/default-cors-policy-rule.md)
* [Add optional rules](https://techdocs.akamai.com/adaptive-media-delivery/docs/add-optal-rules.md)