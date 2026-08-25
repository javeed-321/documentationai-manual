---
updatedAt: 2026-03-01T18:58:05.000Z
---

Fetch the complete documentation index at: https://techdocs.akamai.com/adaptive-media-delivery/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Review supported media formats

Adaptive Media Delivery (AMD) reliably delivers prepared, pre-segmented HTTP-based live and on-demand streaming media.

This includes support for the following formats:

* **HTTP Live Streaming (HLS)**. This is supported for iOS devices, browsers running HTML5, and more.

* **HTTP Dynamic Streaming (HDS)**. This is supported for devices running the Adobe Flash and AIR runtimes.

* **Microsoft Smooth Streaming (MSS)**. This is supported for devices running Microsoft Silverlight.

* **Dynamic Adaptive Streaming over HTTP (MPEG-DASH)**

* **Common Media Application Format (CMAF)**.

AMD is both workflow and origin server storage agnostic. However, you can combine AMD with our complementary Media Services and NetStorage products for an efficient, high-quality streaming media solution.

# Additional points regarding format support

* CMAF support requires that you package your media as CMAF and select HLS, DASH, or both when defining Content Characteristics in your AMD property.

* Various behaviors may be limited to specific media formats, beyond what is listed above. When applicable, this is called out in the description of the behavior.

* With the exception of integration of a Media Services Live origin within a AMD property, this guide is not generally intended for users of the Media Services Live or Media Services On Demand products.

# Sibling pages

* [Delivery concepts and terms](https://techdocs.akamai.com/adaptive-media-delivery/docs/key-concepts-and-terms.md)
* [Get your unique information](https://techdocs.akamai.com/adaptive-media-delivery/docs/get-environ-info.md)
* [Understand the request flow](https://techdocs.akamai.com/adaptive-media-delivery/docs/understand-the-request-flow.md)
* [Prepare your environment](https://techdocs.akamai.com/adaptive-media-delivery/docs/prepare-your-environment.md)