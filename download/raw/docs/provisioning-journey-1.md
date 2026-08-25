---
updatedAt: 2025-09-05T18:57:02.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Provisioning Journey

## Wallet Based Provisioning

Below are the steps that are undertaken in Wallet Based Provisioning attempts:

1. The cardholder opens the Wallet app on their device and will be asked to add a new card to the wallet
2. The cardholder will then be asked to use their camera to scan the card details (which will be the PAN, CVV, expiry and name) or they can choose to manually add the card details
3. The wallet provider will perform some initial checks to validate the request, if the checks do not pass the wallet provider will inform the cardholder that the provisioning attempt has failed
4. If the initial checks pass, the wallet provider sends a request to the card network for them to convert the card into a token. The request will also contain the request to authenticate via an OTP (One Time Passcode) if the risk assessment has passed (see below)
5. If authentication passes the card will be converted to the token and passed back through to the wallet

## OTP Management

To ensure that you as a card program will get notification of events for tokenisation then you will need to be subscribed to webhooks.

The webhook that you will first receive is CARD\_TOKEN\_PROVISIONING which will outline the details in the provisioning journey the cardholder is as well as provide the details of the token which will be needed to obtain the OTP, it will also state when the journey is complete and the card has been tokenised.

```text JSON
{
  "EventName":"CARDTOKENPROVISIONING",
  "CardId":"Vxxxxxxxxx",
  "DeviceId":"Dxxxxxxxxx",
  "Status":"OTP_AVAILABLE",
  "CardTokenId":"TXXXXXXXXX"
}
```

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Name
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        EventName
      </td>

      <td>
        CARDTOKENPROVISIONING
      </td>
    </tr>

    <tr>
      <td>
        CardId
      </td>

      <td>
        Card ID
      </td>
    </tr>

    <tr>
      <td>
        DeviceId
      </td>

      <td>
        Device ID
      </td>
    </tr>

    <tr>
      <td>
        Status
      </td>

      <td>
        One of:  

        COMPLETED  

        OTP\_AVAILABLE  

        ACTIVATION\_CODE\_EXPIRED  

        INVALID\_ACTIVATION\_CODE  

        ACTIVATION\_ATTEMPTS\_EXCEEDED
      </td>
    </tr>

    <tr>
      <td>
        CardTokeId
      </td>

      <td>
        Card Token ID
      </td>
    </tr>
  </tbody>
</Table>

The cardholder has two options available to them for authentication of the card, SMS or Email.

For SMS, this is all handled between scheme and processor who will generate the OTP and send to the cardholder on the mobile number specified in the provisioning journey in the wallet, you will get updates via the above webhook when this has been completed but there is nothing for you to do extra in this journey.

If the cardholder has selected Email then you will be notified by the above webhook at which point you will need to extract the OTP to add to an email template (you will need to create this on your own email headers).

To retrieve the OTP you will need to make a call to endpoint <https://modulr.readme.io/reference/getotpdetails> which will respond with the following:

```text JSON
{
   "activationCode": "123456",
   "expiry": "<date>",
   "deliveryMethod": "EMAIL",
   "deliveryDetails": "mail@domain.com"
}
```

> 👍 OTP Email Message Description
>
> Example wording for the email template:
>
> **Email** - To activate XXXXX Pay, open the Wallet app, tap your card, tap Enter Code and enter p, tap y.  This will expire in e and enter  and is for card ending ire in. If you did not initiate this request, please contact us at \[contact info] \*

## Push Provisioning

Unlike with Wallet based provisioning, there is more development work required to be undertaken by yourselves to enable Push Provisioning and all the documentation will be sent to you upon acceptance of the T\&C's (Apple Pay) and the signing of the NDA (Google Pay).

All documentation on the development of Push Provisioning will be sent to the card program upon meeting the token providers requirements.

### Apple Pay

For Apple Pay, you will need to complete a request to [GET/cards/\{id}/in-app-provisioning/apple](https://modulr.readme.io/reference/getinappprovisioningforapple) supplying the following information obtained from the Apple Servers:

```text JSON
{
  "leafCertificate": "string",
  "additionalCertificates": [
    "string"
  ],
  "nonce": "string",
  "nonceSignature": "string"
}
```

Modulr will then respond with the encrypted payload which will be forwarded on to the payment network via the app, the response will be the following:

```text JSON
{
  "ephemeralPublicKey": "string",
  "encryptedPassData": "string",
  "activationData": "string"
}
```

The response will need to be passed through the app to the payment network who will then decrypt the payload and tokenise the card before pushing back to the wallet ready for use.

All documentation on how to build the connections will be provided upon completion of the terms & conditions.

### Google Pay

For Google Pay, you will need to complete a request to GET/cards/\{id}/in-app-provisioning/google when required to obtain the encrypted card data.  The request should be as follows:

```text JSON
{
  "walletId": "string",
  "deviceId": "string"
}
```

Modulr will then respond with an OPC (Opaque Payment Card) which will need to be passed to the payment network via the app, the request will be as follows:

```text JSON
{
  "opaquePaymentCard": "string"
}
```

Once this is returned to the payment network, they will tokenise the card and push back through to the wallet app.

> ❗️ Google Pay Push Provisioning
>
> This is currently not available and only Wallet Provisioning is available for Google, this feature is coming soon