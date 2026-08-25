---
updatedAt: 2026-03-01T18:58:11.000Z
---

Fetch the complete documentation index at: https://techdocs.akamai.com/adaptive-media-delivery/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Define property configuration settings

The Property Configuration Settings content panel contains the rules for your property. Rules consist of match criteria and behaviors. If a request meets the conditions in a rule's match criteria, the behaviors in that rule are applied.

When you select a **Rule**, its match criteria and behaviors are displayed. Click each rule to view and manage its settings.

# Understand property rule and behavior logic

Property Manager applies a specific logic with the application of rules and the behaviors they contain. When setting up rules, remember these points:

* **The Default Rule is required and applies to all requests**. However, if you set up the same behavior in an optional rule, and that rule's match criteria is met, *that* behavior's settings are used, rather than what's in the Default Rule.

* **Rule logic "trickles down"**. More specific rule wins over a less specific one. In other words, child settings win over parent settings.

* **Several of the behaviors in the Default Rule are required**. You can't delete certain behaviors from the Default Rule, and you have to configure them. If you want certain requests to use different settings for these behaviors, you can include them in an optional rule and set up different match criteria for these requests.

For more details on how business rules execute, see [Property Configuration logic](https://techdocs.akamai.com/property-mgr/docs/config-best-practices).

# Sub pages

* [Default optimizations](https://techdocs.akamai.com/adaptive-media-delivery/docs/best-practices-use-case-based-prov.md)
* [Origin Server](https://techdocs.akamai.com/adaptive-media-delivery/docs/origin-server-amd.md)
* [Content Provider Code](https://techdocs.akamai.com/adaptive-media-delivery/docs/content-provider-code-amd.md)
* [Segmented Media Delivery Mode](https://techdocs.akamai.com/adaptive-media-delivery/docs/segmented-media-deliv-mode-amd.md)
* [Origin Characteristics](https://techdocs.akamai.com/adaptive-media-delivery/docs/origin-charac-amd.md)
* [Content Characteristics](https://techdocs.akamai.com/adaptive-media-delivery/docs/content-charac-amd.md)
* [Client Characteristics](https://techdocs.akamai.com/adaptive-media-delivery/docs/client-charac-amd.md)
* [Cache Key Query Parameters](https://techdocs.akamai.com/adaptive-media-delivery/docs/cache-key-query-param-amd.md)
* [Tiered Distribution](https://techdocs.akamai.com/adaptive-media-delivery/docs/tiered-dist-amd.md)
* [Recommended behaviors in the Default Rule](https://techdocs.akamai.com/adaptive-media-delivery/docs/rcmd-behs-default-rule.md)
* [Optional behaviors in the Default Rule](https://techdocs.akamai.com/adaptive-media-delivery/docs/optal-behs-default-rule.md)
* [The Default CORS Policy Rule](https://techdocs.akamai.com/adaptive-media-delivery/docs/default-cors-policy-rule.md)
* [Add optional rules](https://techdocs.akamai.com/adaptive-media-delivery/docs/add-optal-rules.md)

# Sibling pages

* [Create a new AMD property](https://techdocs.akamai.com/adaptive-media-delivery/docs/create-new-prop.md)
* [Define property hostnames](https://techdocs.akamai.com/adaptive-media-delivery/docs/define-prop-hn.md)
* [Define property variables (optional)](https://techdocs.akamai.com/adaptive-media-delivery/docs/define-prop-vars-optal.md)
* [Finalize your AMD property](https://techdocs.akamai.com/adaptive-media-delivery/docs/finalize-amd-prop.md)
* [Test your AMD property](https://techdocs.akamai.com/adaptive-media-delivery/docs/test-amd-prop.md)
* [Go live with AMD](https://techdocs.akamai.com/adaptive-media-delivery/docs/go-live.md)