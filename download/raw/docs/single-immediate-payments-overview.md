---
updatedAt: 2026-08-17T10:19:33.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Single Immediate Payments

This page provides guidance on using the Payment Initiation Service to initiate **single immediate payments** using Faster Payments and describes how to:

* List the banks that are supported by the service.
* Request a new single immediate payment initiation.
* Redirect the end-user to their bank to authenticate and approve the required payment.
* Return the end-user back to your website or application.
* Retrieve the status of the payment initiation.

## Step 1: Listing available banks

The first step is to present the end-user with a list of banks from which they can select their provider. Use the [GET ASPSPs API](https://modulr.readme.io/reference/getaspsproviders) to fetch the latest list of supported institutions and their capabilities.

This list may change from time-to-time, as we add new banks or change their supported capabilities, so you must ensure that your application can handle changes dynamically.

Only institutions that support the capability type **SINGLE\_IMMEDIATE** should be offered to the end-user.

<Callout icon="📘" theme="info">
  ### Capability Status

  The `status` field gives you the operational status of a capability and we strongly recommend that you query this endpoint every time that you intend to use the Payment Initiation Service.

  You should only make those banks that are **enabled** available for selection by the end-user.  Disabled capabilities are usually temporarily unavailable and indicate a technical issue at the bank.
</Callout>

```json
[
  {
    "id": "H120000002",
    "name": "Test Bank",
    "capabilities": [
      {
        "type": "SINGLE_IMMEDIATE",
        "status": "ENABLED"
      },
      {
        "type": "STANDING_ORDER",
        "status": "DISABLED"
      }
    ]
  }
]
```

## Step 2: Initiating a new payment

When the end-user has selected their ban&#x6B;*(from step one)* you can initiate a new payment using the [\[POST /payment-initiations API\]](https://modulr.readme.io/reference/createpaymentinitiation).

You will need to provide details of the payment to be made, including the destination account that will receive it.

```json
{  
  "destination": {  
    "id": "A1234567",  
    "type": "ACCOUNT"  
  },  
  "paymentAmount": {  
    "currency": "GBP",  
    "value": 1 
  },  
  "aspspId": "H120000002",  
  "paymentReference": "Top Up RB1382731",  
  "paymentContext": {  
    "paymentContextCode": "PARTYTOPARTY"  
  }  

```

<Callout icon="📘" theme="info">
  ### Payment Reference

  Using a unique and meaningful `paymentReference` will make it easy to reconcile payments received as this reference is used as the incoming payment reference.
</Callout>

## Step 3: Redirecting the end-user to their online banking service

The response to the API call in the previous step will return a unique payment initiation ID and redirect URL to the end-user’s online banking service.

**You must immediately redirect the end-user to their bank using the redirect URL provided so that they can authenticate and authorise the payment initiation.**

The redirect URL is valid for 5 minutes. If the end-user does not complete bank authentication and payment approval in this time, the payment initiation request will be expired and will have the status ER\_EXPIRED.

<Callout icon="🚧" theme="warn">
  Whilst the redirect URL does not contain any sensitive information that could be used maliciously in isolation, it does contain data that might facilitate malicious use when paired with information gained elsewhere.

  **The redirect URL must not be distributed or used in ways where it can be easily inspected (such as via e-mail).**
</Callout>

If the end-user is using a mobile device which has their bank’s mobile app installed, the redirect URL may open the online banking app rather than the online banking website. This is generally the desired user experience and provides the best conversion. If the bank’s mobile app is not installed or is not correctly setup to open the URL, it will open in a web browser page.

Whether the online banking app or website opens is a feature of the mobile device *(known as "deep linking")* and is not influenced by the Modulr Payment Initiation Service.

When the end-user has authenticated with their bank and approved the payment, Modulr will finalise the payment initiation and will then redirect the end-user back to your application using the redirect URL provided by you during onboarding.

## Step 4: Returning the end-user back to your site or application

When the end-user has approved the payment initiation, they are redirected back to your application using your redirect URL. The URL will contain the payment initiation identifier and will also contain a parameter to indicate success or failure of the payment.

The purpose of this indication is so that you can display an initial message to the end-user but you **must not** rely on this as a definitive status, as it could have been tampered with by a malicious user or third party.

## Step 5: Retrieving the status of the payment initiation

To retrieve the status of the payment initiation, you must use the [GET /payment-initiations/\{paymentInitiationId} API](https://modulr.readme.io/reference/getpaymentinitiation).

The response will contain the **status of the payment initiation** and the **payment status** as provided to Modulr by the bank.

```json
{
    "id": "I123456789",
    "status": "EXECUTED",
    "paymentAmount": {
        "currency": "GBP",
        "value": 1.00
    },
    "paymentReference": "Top Up RB1382731",
    "destination": {
        "type": "ACCOUNT",
        "id": "A1234567"
    },
    "aspspId": "H120000002",
    "aspspPaymentStatus": "AcceptedSettlementCompleted"
}
```

#### Payment Initiation Status

<Image src="https://files.readme.io/c2c6224-StateDiagram2.png" alt="Payment Initiation Status Model (`status`)" align="center" />

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Status
      </th>

      <th>
        Comment
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        AWAITING_CONSENT
      </td>

      <td>
        Waiting for the end-user to approve the payment initiation at their bank. If not approved/rejected within a certain timeframe, the payment initiation will move to ER_EXPIRED. Otherwise it will move to EXECUTED or any of the other error statuses.
      </td>
    </tr>

    <tr>
      <td>
        CONSENT_REJECTED
      </td>

      <td>
        The end-user or bank has rejected the payment initiation.
      </td>
    </tr>

    <tr>
      <td>
        EXECUTED
      </td>

      <td>
        The payment initiation has been accepted by the bank and it is with them to execute.

        Note that the bank may still on rare occasions have problems fulfilling the payment and fail at the time of execution. You should not assume that the payment has been successful until you check the status of field aspspPaymentStatus.

        Alternatively you can check if funds have been received into the destination account.
      </td>
    </tr>

    <tr>
      <td>
        ER_EXTSYS
      </td>

      <td>
        The payment initiation failed because there was a problem communicating with the bank’s systems.
      </td>
    </tr>

    <tr>
      <td>
        ER_EXPIRED
      </td>

      <td>
        The end-user did not approve or reject the payment initiation within a certain timeframe, for example, by not even logging into their banking app.
      </td>
    </tr>

    <tr>
      <td>
        ER_GENERAL
      </td>

      <td>
        Generic error occurred when processing the payment initiation.
      </td>
    </tr>
  </tbody>
</Table>

#### Payment Status

<Image src="https://files.readme.io/a90741f-StateDiagram1.png" alt="Payment Status Model (aspspPaymentStatus)" align="center" />

| Status                            | ISO 20022 Code | Payment Status Description                                                                                                                                                        |
| --------------------------------- | -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Pending                           | PDNG           | Payment initiation or individual transaction included in the payment initiation is pending. Further checks and status update will be performed.                                   |
| Rejected                          | RJCT           | Payment initiation or individual transaction included in the payment initiation has been rejected.                                                                                |
| AcceptedSettlementInProcess       | ACSP           | All preceding checks such as technical validation and customer profile were successful and therefore the payment initiation has been accepted for execution.                      |
| AcceptedSettlementCompleted       | ACSC           | Settlement on the payer's account has been completed.                                                                                                                             |
| AcceptedWithoutPosting            | ACWP           | Payment instruction included in the credit transfer is accepted without being posted to the payee's customer's account. **Note that most banks do not provide this information.** |
| AcceptedCreditSettlementCompleted | ACCC           | Settlement on the payee's account has been completed. **Note that most banks do not provide this information.**                                                                   |

You should always check the `aspspPaymentStatus` field as the payment could, on rare occasions, fail after the payment initiation has been executed if the bank has stopped it for risk/ fraud purposes.

<Callout icon="👍" theme="okay">
  ### When initiating payments into a Modulr account

  For absolute certainty, use the [PAYIN webhook](https://modulr.readme.io/docs/payin-webhook) to be notified of inbound payments to a Modulr account, the payment initiation reference will be used as the Faster Payment reference.
</Callout>

## High level end-to-end flow

![](https://files.readme.io/38ffb3f-PISPFlow.jpg "PISPFlow.jpg")