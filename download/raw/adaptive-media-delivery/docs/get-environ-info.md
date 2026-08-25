---
updatedAt: 2026-03-01T18:58:05.000Z
---

Fetch the complete documentation index at: https://techdocs.akamai.com/adaptive-media-delivery/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Get your unique information

You need to review your environment and gather some specific pieces of information before creating your Adaptive Media Delivery (AMD) property.

# Get your account information

Within five days of your service contract submission, you should receive your account information. You need this information to activate your property for use with Adaptive Media Delivery.  If you haven't received it, or you don't have it, contact your ​Akamai​ account representative.

You should receive the following information:

* **Your account name and ID**. This is the unique name for your account and its unique identifier. This is not your login information.

* **Content provider (CP) codes**. These are used for reporting and billing. You'll use this value when setting up your Adaptive Media Delivery property. If you need access to more CP codes for granularity in reporting and billing, talk to your account team. You'll either be given more individual CP codes for use, or you'll be given access to create more using Property Manager.

* **An administrator login**. This is used to access the following:

  * **​Akamai Control Center​**. This is ​Akamai​'s user interface portal.

  * **Content storage servers**. This applies if you've included NetStorage in your service package, for use as the origin to store your content for delivery.

## You can create more administrator accounts

An administrator account for ​Akamai Control Center​ is provided to you in your account information after you initially provision Adaptive Media Delivery. As an administrator, you can create additional accounts with this same level or lesser access. Creating additional administrator-level accounts makes it possible for multiple people to log on and perform administrator-level tasks.

See the [Identity and Access Management documentation](https://techdocs.akamai.com/iam/docs/manage-users-admin) for instructions on adding new users.

# Additional items you'll need

In addition to the information ​Akamai​ gives you, you need these items, some of which are gathered during the processes discussed in this documentation.

* **Your domain**. This is the hostname that end users are using to access your site or application. This is used to create a property hostname.

* **The origin server hostname**. This applies if you're housing deliverable content on a custom origin—you're not using ​Akamai​ NetStorage as your origin server. ​Akamai​ edge servers need this value to fetch target content for a request.

# Multiple origin servers

If you're using multiple origin servers, your overall configuration might be impacted. You should contact your account representative before creating a property for Adaptive Media Delivery. Explain the use and purpose of the various origin servers. For example, assume origin server center "A" is active, and origin server center "P" is passive, to be used only when required by heavy traffic or failover. If this is the case, you can set up multiple rules in your Adaptive Media Delivery property to accommodate them, using different match criteria for requests. See [Mixed Mode & AMD](https://techdocs.akamai.com/adaptive-media-delivery/docs/use-mixed-mode-amd) for details on this process. However, you can also reach out to your account representative for additional tips, or for assistance in setting this up.

There are some other ways that multiple origin servers can affect your configuration:

* When using SureRoute, ​Akamai Technologies, Inc.​ edge servers race test objects to determine the optimal edge-to-origin routes. By default, the assumption is that only one origin server location needs to be evaluated.

* When configuring cacheable objects, there are ways to avoid caching multiple instances of the same object that may be obtained from different origin servers.

# Sibling pages

* [Delivery concepts and terms](https://techdocs.akamai.com/adaptive-media-delivery/docs/key-concepts-and-terms.md)
* [Review supported media formats](https://techdocs.akamai.com/adaptive-media-delivery/docs/supported-media-formats.md)
* [Understand the request flow](https://techdocs.akamai.com/adaptive-media-delivery/docs/understand-the-request-flow.md)
* [Prepare your environment](https://techdocs.akamai.com/adaptive-media-delivery/docs/prepare-your-environment.md)