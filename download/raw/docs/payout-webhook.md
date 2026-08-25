---
updatedAt: 2025-09-05T18:48:16.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Webhook - Outbound Payments

### Outbound Payment

The `PAYOUT` event is triggered when a Payment request reaches any [final status](https://modulr.readme.io/docs/payment-statuses) (*It doesn't trigger for payments that are rejected. To subscribe to Payment Approvel/Rejection notifications see our guide here:[Individual Payment Approval/Rejections](https://modulr.readme.io/docs/payment-approval-rejection-webhook)*) or a Settlement is processed in a card that's associated with one of your accounts

| Parameter            | Description                                                                                                                                                                                                        |
| :------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Amount               | Amount of the Payment.                                                                                                                                                                                             |
| Status               | Final status of the payment .                                                                                                                                                                                      |
| EventId              | Unique id for the webhook event. This can change if webhook needs to be resent.                                                                                                                                    |
| DateTime             | The Date and timestamp when the Payment was posted to Modulr - All Dates and times are UTC based.                                                                                                                  |
| AccountId            | Modulr Unique Account reference for the account that the payment was made from.                                                                                                                                    |
| EventName            | Type of event: PAYOUT - Payment has reached a final status.                                                                                                                                                        |
| EventTime            | Date and Timestamp for the Event - All Dates and times are UTC based.                                                                                                                                              |
| PaymentSubmittedTime | Date and Timestamp for when the payment has been sent externally from Modulr.                                                                                                                                      |
| PaymentId            | Modulr Unique Payment Reference for the payment sent.                                                                                                                                                              |
| Reference            | Reference to be used for the Payment. This will appear on the Account statement/the recipient's bank account.                                                                                                      |
| SchemeInfo           | Scheme information for the sent payment in this example this is a FPID and the response code from the Scheme.                                                                                                      |
| TransactionId        | Modulr Unique Transaction Reference for the payment sent. Transactions are only created when a payment is sent successfully in case of failed payment it is possible to receive a webhook without a TransactionId. |
| ExternalReference    | This is the reference you can set on the payment request to correlate back to your system.                                                                                                                         |

## Duplication Check

PaymentId should be used as your main duplication check, as there are times where the EventId could change or in the event of a failed payment the TransactionId would be empty. This is important particularly if a webhook has failed and needs to be resent.

## Example PAYOUT Webhook

### Internal Transfer Example

```json Payout Example
{
    "Amount": "19.28",
    "Status": "PROCESSED",
    "EventId": "a13bd641-4a19-4814-b121-2d58adc15623",
    "DateTime": "2024-02-02T02:02:022+0000",
    "AccountId": "A1201HT721",
    "EventName": "PAYOUT",
    "EventTime": "2024-02-02T02:02:024+0000",
    "PaymentId": "P120DD1AB2",
    "TransactionId": "T120A3VX22",
    "TransactionType": "INT_INTERC"
}
```

### Faster Payment Out Example

```json PAYOUT Example
{
    "Amount": "40",
    "Status": "PROCESSED",
    "EventId": "46915325-a6db-46c5-a3d8-606f35bde2ef",
    "DateTime": "2020-01-01T10:53:38+0000",
    "AccountId": "A120C8D3",
    "EventName": "PAYOUT",
    "EventTime": "2020-01-01T10:53:382+0000",
    "PaymentSubmittedTime": "2021-01-01T10:54:42.715+0000",
    "PaymentId": "P12000MWFB",
    "Reference": "Sent from Tony Stark",
    "SchemeInfo": {
        "Id": "MODULO00P12000MWFB020200101826040010",
        "ResponseCode": "0000"
    },
    "TransactionId": "T12000N5TN",
    "ExternalReference": "887adb57-9960-4a3d-bfa1-f0c6cacc7c97",
    "TransactionType": "PO_FAST"
}
```

### CHAPS Payment Out Example

```json CHAPS Webhook Example
{
    "Amount": "266726.74",
    "Status": "PROCESSED",
    "EventId": "f747b093-40f1-4438-b3a5-6ad3ce66f2dd",
    "DateTime": "2020-01-01T10:07:03+0000",
    "AccountId": "A120E8C3",
    "EventName": "PAYOUT",
    "EventTime": "2020-01-01T10:07:03+0000",
    "PaymentId": "P12000EWFQ",
    "Reference": "Hulk Smash",
    "SchemeInfo": {
        "Id": "+H4Bu6HbDww7jdgI",
        "Name": "CHAPS"
    },
    "TransactionId": "T12000N5GQ",
    "TransactionType": "PO_CHAPS"
}
```

### Direct Debit Out Payment Out Example

```json DD Out Webhook Example
{
    "Amount": "107.03",
    "Status": "PROCESSED",
    "EventId": "f3a48f9a-dd7a-42d2-b0de-87ed234f92ef",
    "DateTime": "2020-01-01T15:00:19+0000",
    "AccountId": "A120Q8Q3",
    "EventName": "PAYOUT",
    "EventTime": "2020-01-01T15:00:19+0000",
    "PaymentId": "D210NER0",
    "TransactionId": "T12000R5RQ",
    "TransactionType": "PO_DD"
}
```

### Direct Debit Internal Transfer Example

```Text Direct Debit Internal Transfer Example
{
  "Amount": "341.40",
  "Status": "PROCESSED",
  "EventId": "79e2926b-ccd2-40f8-82e5-868242ca4129",
  "DateTime": "2025-01-01T10:04:18+0000",
  "AccountId": "A2105JXXXX",
  "EventName": "PAYOUT",
  "EventTime": "2025-01-01T10:04:18+0000",
  "PaymentId": "K21004XXXX",
  "TransactionId": "T2117XXXXX",
  "TransactionType": "PO_DD_PEND"
}
```

<br />

### SEPA Credit Transfer Payment Out Example

```json SEPA Out Webhook Example
{
    "Amount": "100.0",
    "Status": "PROCESSED",
    "EventId": "4193b4d3-5dff-422c-be7e-66c79f69a10e",
    "DateTime": "2020-01-01T09:15:00+0000",
    "AccountId": "A120S8H3",
    "EventName": "PAYOUT",
    "EventTime": "2020-01-01T09:15:00+0000",
    "PaymentId": "P12000EWVV",
    "Reference": "JARVIS",
    "TransactionId": "T12000R5EE",
    "ExternalReference": "TYbJv7RRpDwHxmx",
    "TransactionType": "SEPA_SCT"
}
```

### Card Settlement Example

The PaymentId field contains the card activity BID which you can use to query additional details from the card [activities](https://modulr.readme.io/reference/getcardactivities) API

Some of our clients will also use the Order ID to match the settlement to the authorisation record as part of their internal reconciliation

```json
{
    "Amount": "107.03",
    "Status": "PROCESSED",
    "EventId": "f3a48f9a-dd7a-42d2-b0de-87ed234f92ef",
    "DateTime": "2020-01-01T15:00:19+0000",
    "AccountId": "A120Q8Q3",
    "EventName": "PAYOUT",
    "EventTime": "2020-01-01T15:00:19+0000",
    "PaymentId": "X11000DYTA", // Card Activity ID
    "ExternalReference": "10", // Order ID
    "TransactionId": "T12000R5RQ",
    "TransactionType": "PO_VISA"
}
```