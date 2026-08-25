---
updatedAt: 2025-11-05T10:07:43.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Channel Manager - Notifications

Notifications enable your platform to find out about events as they happen, these will be supplied in the form of webhooks.

These will be for customers that are shared between the Modulr platform and the Channel Manager platform.

<Callout icon="🚧">
  You will need to build a listener to look out for webhooks
</Callout>

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Notification Type
      </th>

      <th>
        Description
      </th>

      <th>
        Subscription Level
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Card Authorisation - CARDAUTH 
      </td>

      <td>
        A notification to alert you that there has been a new or updated card authorisation
      </td>

      <td>
        Channel Manager
      </td>
    </tr>

    <tr>
      <td>
        Offline Card Authorisation – CARDAUTHOFFLINE
      </td>

      <td>
        A notification to alert that the card has been used for an authorisation offline, this means that there will be no other corresponding authorisation but just a settlement.

        This is advice only and does not instruct any money movements

      </td>

      <td>
        Channel Manager
      </td>
    </tr>

    <tr>
      <td>
        Card Refund – PAYIN
      </td>

      <td>
        When there's a new refund in a card that's associated with one of your accounts
      </td>

      <td>
        Channel Manager
      </td>
    </tr>

    <tr>
      <td>
        Card Settlement - PAYOUT
      </td>

      <td>
        When there's a new settlement in a card that's associated with one of your accounts
      </td>

      <td>
        Channel Manager
      </td>
    </tr>
  </tbody>
</Table>

<br />

## Webhooks - An Introduction

A Webhook, in simple terms, is a user-defined HTTP callback. It is a mechanism for the system to notify you about an event. How does it notify you? By doing an HTTP POST to the Webhook (i.e. the Web URL that you define). In terms of implementation, you can write an API endpoint that is capable of receiving an HTTP POST in an application stack of your choice.

Remember in live this must be reliable and resilient if you are to depend on it for information.

The advantage of a Webhook is that there is no persistent open connection to the system where you keep filtering for events that you are interested in. It is an asynchronous mechanism where you will wait for the system to notify you. The HTTP POST payload will contain the details of the event.

<br />

## Webhook security

We sign the POST request with an HMAC digest, using a secret that you provide. This can be set when registering the endpoint for the webhook type of notification. It is required that you validate this signature, particularly if you are acting upon these events to authorise actions in your system. The method of calculation of the hmac signature is the same as in HMAC Signatures / Authorisation header calculation

For webhook requests that are sent from us to you, we use the webhook id as the key and the secret you have provided when creating the webhook to sign the webhook.

<br />

<br />