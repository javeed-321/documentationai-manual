---
updatedAt: 2026-03-01T18:58:15.000Z
---

Fetch the complete documentation index at: https://techdocs.akamai.com/adaptive-media-delivery/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Origin Characteristics

This behavior lets you set characteristics for your origin server to optimize access to it.

<div align=center>
<img src="https://techdocs.akamai.com/adaptive-media-delivery/img/amd-origin-char-v2.png" width="600"/>
</div>

# Authentication Method

Select the appropriate authentication method for use:

[block:parameters]
{
  "data": {
    "h-0": "Method",
    "h-1": "Description",
    "h-2": "Additional options",
    "0-0": "**​Akamai​ Origins - Auto, Others - None**",
    "0-1": "This is the default and applies to you if your origin server doesn't have any external authentication requirements, or if you're using NetStorage as your origin.",
    "0-2": "N/A",
    "1-0": "**​Akamai​ Signature Authentication**",
    "1-1": "Select this if your AMD property has been set up to use our shared certificate hostname for secure (HTTPS) delivery to your custom origin.",
    "1-2": "N/A",
    "2-0": "**​Akamai​ Media Services Live**",
    "2-1": "Select this if you're using this AMD property in association with the Media Services Live product to deliver live streaming media.",
    "2-2": "This is covered in the [Media Services Live user documentation](https://techdocs.akamai.com/msl/docs/setup-media-services-live-origin)",
    "3-0": "**Interoperability Google Cloud Platform**",
    "3-1": "Select this if you're authenticating with Google Cloud Storage (GCS) as your origin. Support is based on the GCS [V4 signing process](https://cloud.google.com/storage/docs/access-control/signing-urls-manually). Once selected, configure the additional options that are revealed.",
    "3-2": "<ul><li><strong>Access ID</strong>. Enter the identifier of the access key used to authenticate requests to your GCS instance.</li>  \n<li><strong>Secret</strong>. Enter the secret key value that is used to compute the signature.</li></ul>",
    "4-0": "**Amazon Web Services**",
    "4-1": "Select this if you're authenticating with Amazon Web Services (AWS) cloud provider as your origin. Support is based on the AWS [signature version 4 signing process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html). Once selected, configure the additional options that are revealed.",
    "4-2": "<ul>  \n<li><strong>Access Key ID</strong>. Enter the identifier of the access key used to authenticate requests to your AWS service.</li>  \n<li><strong>Secret Access Key</strong>. Enter the secret key value that is used to compute the signature.</li>  \n<li><strong>Region</strong>. Enter the AWS-specific region that houses your AWS instance.</li>  \n<li><strong>Endpoint Service</strong>. Enter the code of your AWS service. This is the segment or part of the segment that precedes `amazonaws.com` or the region code in the AWS hostname. For example, `s3` is the endpoint service for both `https://<account-id>.s3-control.eu-north-1.amazonaws.com` and `https://s3.us-east-2.amazonaws.com` hostnames. See the article, [Service endpoints and quotas in AWS](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) for more information.</li>  \n</ul>"
  },
  "cols": 3,
  "rows": 5,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]

## Additional considerations for GCS or AWS

Pay attention to these points when using GCS or AWS:

* **You can use Cloud Access Manager**. Use it to streamline the client authentication process. See [Cloud Access Manager & AMD](https://techdocs.akamai.com/adaptive-media-delivery/docs/add-cloud-access-manager) for complete details.

* **You can check your authentication details in the file you saved when creating your access key**. If you didn't download the file, or if you lost it, you may need to delete the existing access key and add a new one. See [Managing HMAC keys in GCS](https://cloud.google.com/storage/docs/authentication/managing-hmackeys#create) or [Managing Access Keys (console) in AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey).

* **Use a property with an akamaized hostname**. This lets you either retrieve objects from the origin, or for read-only bucket operations. This is because we're currently limited to storing cloud provider access keys in cleartext. This doesn't carry the level of protection you might expect for the transmission of personally identifiable information (PII).

* **Consider using two separate sets of cloud provider access keys**. Dedicate one to GET operations and another to POST, PUT, or DELETE operations. For all GET operations, set them up to use a property via Property Manager; for POST, PUT, and DELETE operations, you should use the APIs or SDKs offered by the associated cloud provider.

* **Regularly rotate the cloud provider access keys**. This reduces the likelihood of unauthorized diversion of confidential information.

* **Only the "Authorization" header is supported (AWS, only)**. If you're using query string parameters with this authentication, each query parameter in the incoming client request must be sorted alphabetically, and URL encoded.

# Origin Location

Select the appropriate location of the origin server, based on its **Origin Type**:

* **NetStorage**. Set this to **Unknown**.

* **Your Own Origin**. Select the geographical location of your origin server to optimize access to it. (Do this to implement what we consider "use case-based provisioning" for this behavior.) If you're not sure about your server location, select **Unknown**.

# Origin-specific best practices applied by default

To help optimize delivery, ​Akamai​ automatically sets various origin-related behaviors in the background of the Default Rule.

> 📘
>
> These automatic settings are what ​Akamai​ considers best practices to optimize delivery. However, you can manually add these behaviors to override these automatic settings.

## Origin Offload

These settings are automatically applied for this behavior in the background:

* **"1-Tier" Tiered Distribution is applied**. This lets AMD retrieve your cached content from another tier of ​Akamai​ edge servers that are closer to your origin server, rather than directly from your origin server. For cached content, the feature has significant advantages:

  * **The demand for bandwidth at the Origin Server is reduced**. This is often positive in itself and necessary to upscale applications.

  * **The time it takes for the product to retrieve content is reduced**. The tiered distribution parent servers are generally located close to the production servers that use them.

* **Hostname-based content sharding**. This is incorporated in the Tiered Distribution layer.

* **Multiple requests for the same object are queued to a single primary request.** If an error response is delivered to the primary request, it is delivered to all queued requests.

> 📘
>
> If you need to disable Tiered Distribution, you can add **Tiered Distribution** as an optional behavior and set **Enable** to **Off**. This will override the automatic best practices application.

## Origin Failure

These settings are automatically applied for this behavior in the background:

* **Origin Unresponsiveness**. The following are automatically set as best practices values for this scenario:

* **Connection Timeout**. Five seconds

* **HTTP Response Timeout**. Two minutes

* **Retry logic**. Retry once, and serve an error to the requesting client after retry failure.

* **Origin Server Error**. The following are automatically set as best practices values for this scenario:

* **Retry logic**. Retry once, and serve an error to the requesting client after retry failure.

* **Object Content Error**. An error is served to the requesting client.

## Origin Authentication

These settings are automatically applied for this behavior in the background:

* **If NetStorage is set as your origin**. **​Akamai​ Signature Header Verification Authentication** is applied by default.

* **For all other origin types**. Origin Authentication is *not* default applied. Use the [Authentication Method](#authentication-method) options in this behavior for your origin.

# Origin Characteristics and Mixed Mode Configuration

This is a "use case-based" behavior that's automatically included in the Default Rule and used to optimize delivery. You need to apply settings for this behavior in the Default Rule. However, with Mixed Mode Configuration for AMD (MMC), you can also include it in another rule and apply different match criteria to have separate requests use different origin characteristics optimizations. For more details, see [How to use Mixed Mode with AMD](https://techdocs.akamai.com/adaptive-media-delivery/docs/use-mixed-mode-amd).

# Sibling pages

* [Default optimizations](https://techdocs.akamai.com/adaptive-media-delivery/docs/best-practices-use-case-based-prov.md)
* [Origin Server](https://techdocs.akamai.com/adaptive-media-delivery/docs/origin-server-amd.md)
* [Content Provider Code](https://techdocs.akamai.com/adaptive-media-delivery/docs/content-provider-code-amd.md)
* [Segmented Media Delivery Mode](https://techdocs.akamai.com/adaptive-media-delivery/docs/segmented-media-deliv-mode-amd.md)
* [Content Characteristics](https://techdocs.akamai.com/adaptive-media-delivery/docs/content-charac-amd.md)
* [Client Characteristics](https://techdocs.akamai.com/adaptive-media-delivery/docs/client-charac-amd.md)
* [Cache Key Query Parameters](https://techdocs.akamai.com/adaptive-media-delivery/docs/cache-key-query-param-amd.md)
* [Tiered Distribution](https://techdocs.akamai.com/adaptive-media-delivery/docs/tiered-dist-amd.md)
* [Recommended behaviors in the Default Rule](https://techdocs.akamai.com/adaptive-media-delivery/docs/rcmd-behs-default-rule.md)
* [Optional behaviors in the Default Rule](https://techdocs.akamai.com/adaptive-media-delivery/docs/optal-behs-default-rule.md)
* [The Default CORS Policy Rule](https://techdocs.akamai.com/adaptive-media-delivery/docs/default-cors-policy-rule.md)
* [Add optional rules](https://techdocs.akamai.com/adaptive-media-delivery/docs/add-optal-rules.md)