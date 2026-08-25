---
updatedAt: 2026-03-01T18:58:06.000Z
---

Fetch the complete documentation index at: https://techdocs.akamai.com/adaptive-media-delivery/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Understand the request flow

To start, you should have a basic understanding of the flow of a request and how the ​Akamai​ content delivery network (CDN) fits in.

[block:callout]
{
  "type": "info",
  "body": "Secure hypertext transfer protocol (HTTPS) has become the standard for access on the Internet. All processes covered here assume you're using this security to deliver your content via the ​Akamai​ network. While non-secure HTTP is still supported, it's not recommended."
}
[/block]

# The stages of a request

There are two connections involved in a request using the ​​Akamai​ platform:

1. **The client to the ​Akamai​ edge server**. This is the initial connection between the end user's browser or application and an edge server in the ​Akamai​ network. The request is resolved to an edge hostname that you assign to your actual hostname. The edge hostname directs the request to your property, which is read to determine how to deliver content to the end user. To secure the connection, you'll need to use an "edge certificate" that's verified between the client and the edge server.

<div align=center>
<img src="https://techdocs.akamai.com/property-manager/img/user-to-edge-server-v1.png"/>
</div>

2. **The ​Akamai​ edge server to origin**. This is the connection between the edge server and your designated origin, where the requested content is hosted. You'll use various behaviors in your property to set up your origin. Depending on your selected origin type, you may need to create a separate secure certificate and apply it on your origin.

<div align=center>
<img src="https://techdocs.akamai.com/property-manager/img/edge-server-to-origin-v1.png"/>
</div>

# Understand secure connections

HTTPS embodies security on the web. When end users make an HTTPS request to your site or application, they expect that their request and the response are encrypted and trusted, end to end.

At its base, HTTPS (also known as Secure Sockets Layer, `SSL` or Transport Layer Security, `TLS`) compares a pair of encryption keys, one `public` and one `private`, to allow access. When an HTTPS connection is established, the server sends the requesting client a certificate with:

* the public key
* a list of sites on which the cert is valid, referred to as a `SAN`
* an expiration date for the cert
* a signature from a Certificate Authority that proves that the key is legitimate for a SAN listed in the cert

The client checks whether:

* [x] the signature matches the cert.
* [x] the cert came from a Certificate Authority it trusts.
* [x] the cert is actually for the site it requested.
* [x] the cert hasn't expired.

If those checks succeed, the client encrypts this information using the public key, and sends it to the server, establishing a shared key for the session. Only a server that holds the corresponding private key can decrypt the information, read the shared key, and ultimately prove its identity to the requesting client.

# Sibling pages

* [Delivery concepts and terms](https://techdocs.akamai.com/adaptive-media-delivery/docs/key-concepts-and-terms.md)
* [Review supported media formats](https://techdocs.akamai.com/adaptive-media-delivery/docs/supported-media-formats.md)
* [Get your unique information](https://techdocs.akamai.com/adaptive-media-delivery/docs/get-environ-info.md)
* [Prepare your environment](https://techdocs.akamai.com/adaptive-media-delivery/docs/prepare-your-environment.md)