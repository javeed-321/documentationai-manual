---
updatedAt: 2026-03-01T18:58:13.000Z
---

Fetch the complete documentation index at: https://techdocs.akamai.com/adaptive-media-delivery/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Segmented Media Delivery Mode

Set the delivery mode for your content to optimize the property to deliver for that specific mode: **On Demand** or **Live**.

# Select the Mode

Set the appropriate delivery Mode:

* **On Demand**. This adjusts the Time-to-Live (TTL) of the manifests if no specific caching rules are defined. Also, ​Akamai​ automatically applies [best practices and use case-based provisioning](https://techdocs.akamai.com/adaptive-media-delivery/docs/best-practices-use-case-based-prov) to optimize the delivery of content.

* **Live**. This also adjusts the TTL of the manifests if no specific caching rules are defined. With live media, it assigns a very short TTL to the stream manifest file so that updates to it are retrieved in a timely manner. The best practices and use case-based provisioning that are applied for On Demand media aren't applied for Live mode. Use the additional options that are revealed to fine-tune delivery.

# Enable ULL Streaming for "Live" Mode

If you've selected **Live** as the Mode, you can add support for low latency streaming for both DASH and HLS format live streams. Low latency streaming reduces latency and decreases the overall transfer time of your live streams. Configuration for low latency support varies, based on your live stream format:

* [DASH live streams](https://techdocs.akamai.com/adaptive-media-delivery/docs/dash-and-msl-origin). We recommend that you use Media Services Live (MSL), and set it as your origin in your AMD property.

* [HLS live streams](https://techdocs.akamai.com/adaptive-media-delivery/docs/hls-and-third-party-origin). You need to incorporate a third-party origin.

<div align=center>
<img src="https://techdocs.akamai.com/adaptive-media-delivery/img/amd-seg-del-mode-enable-v2.png" />
</div>

# Show Advanced Options for "Live" Mode

If you've selected **Live** as the Mode, the Show Advanced Option slider can be set to "**Yes**" to reveal additional options. These are used when configuring Media Services Live as your origin with AMD.

<div align=center>
<img src="https://techdocs.akamai.com/adaptive-media-delivery/img/amd-seg-media-behavior-live-v2.png" />
</div>

## Live Type

Select from two modes:

* **Linear**. Once you activate your Adaptive Media Delivery property in production ([Go live](https://techdocs.akamai.com/adaptive-media-delivery/docs/go-live)), the TTL optimization will be applied to requests for your live streams, with no specific end date.

* **Event**. This tells your AMD property to anticipate requests for your live stream during a specific range of time. During this time, the optimization discussed above is applied to requests for live streams. Times are represented in GMT, so be sure to take your required timezone into consideration.

## Segment Access Time Mode (and Segment Access Time)

Select from these options:

* **Configurable**. Select this if you want to apply a time to live (TTL) for your segments for requesting clients. Use the **Segment Access Time** to set this duration. This can potentially optimize delivery, because AMD won't need to read the manifest to get the segment access time.

* **Unknown**. Select this if you don't know of a specific availability time, or if there isn't one. Your AMD  property will look to your manifest to determine a segment access time, if applicable.

<div><p></p></div>

> 🚧
>
> This also applies to DVR access to your live segments. If you set too low of a TTL, this can overwhelm your origin with DVR access requests for your segments. Consider an adequate amount of time customers may need to access your content for DVR viewing.

# Media Delivery Type Mapping Solution and Mixed Mode Configuration

If you're adding either of these services to your AMD property configuration, the following apply:

* **Media Delivery Type Mapping Solution**. During the creation of your property hostname to edge hostname association, if you've set the Media Delivery Type setting to either **Live** or **On Demand**, you need to match that setting here. The complete setup is discussed in [Media Delivery Type & AMD](https://techdocs.akamai.com/adaptive-media-delivery/docs/add-use-case-based-edge-mapping).

* **Mixed Mode Configuration for AMD**. This lets you include use case-based behaviors like Segmented Media Delivery Mode in rules outside the Default Rule, in order to optimize delivery for unique requests using specific match criteria. If you're including this behavior in multiple rules, ensure that it's set to match the applicable delivery mode for each rule. See [Mixed Mode & AMD](https://techdocs.akamai.com/adaptive-media-delivery/docs/use-mixed-mode-amd) for more details.

# Sibling pages

* [Default optimizations](https://techdocs.akamai.com/adaptive-media-delivery/docs/best-practices-use-case-based-prov.md)
* [Origin Server](https://techdocs.akamai.com/adaptive-media-delivery/docs/origin-server-amd.md)
* [Content Provider Code](https://techdocs.akamai.com/adaptive-media-delivery/docs/content-provider-code-amd.md)
* [Origin Characteristics](https://techdocs.akamai.com/adaptive-media-delivery/docs/origin-charac-amd.md)
* [Content Characteristics](https://techdocs.akamai.com/adaptive-media-delivery/docs/content-charac-amd.md)
* [Client Characteristics](https://techdocs.akamai.com/adaptive-media-delivery/docs/client-charac-amd.md)
* [Cache Key Query Parameters](https://techdocs.akamai.com/adaptive-media-delivery/docs/cache-key-query-param-amd.md)
* [Tiered Distribution](https://techdocs.akamai.com/adaptive-media-delivery/docs/tiered-dist-amd.md)
* [Recommended behaviors in the Default Rule](https://techdocs.akamai.com/adaptive-media-delivery/docs/rcmd-behs-default-rule.md)
* [Optional behaviors in the Default Rule](https://techdocs.akamai.com/adaptive-media-delivery/docs/optal-behs-default-rule.md)
* [The Default CORS Policy Rule](https://techdocs.akamai.com/adaptive-media-delivery/docs/default-cors-policy-rule.md)
* [Add optional rules](https://techdocs.akamai.com/adaptive-media-delivery/docs/add-optal-rules.md)