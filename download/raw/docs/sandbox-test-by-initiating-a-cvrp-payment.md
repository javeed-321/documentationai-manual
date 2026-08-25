---
updatedAt: 2026-08-12T08:54:15.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Sandbox: Initiating a cVRP payment

## Payment initiation request

1. **Initiate the payment** – `POST /vrp` returns a `vrpId` (as `id` in the response). The status will always return `RECEIVED`.

   Please use the same `consentId` that you have created under /POST `vrp-consents`&#x20;

```json Initiate payment – request
{
  "consentId": "E210000BUJ",
  "payment": {
    "amount": "1.00",
    "currency": "GBP",
    "reference": "GWE-VRP-001"
  },
  "interactionType": "IN_SESSION"
}
```
```json Initiate payment – response
{
  "id": "V21000074D",
  "status": "RECEIVED"
}
```

2. **Check the payment status** – `GET /vrp/{id}` returns the payment status, which will always be `ACCEPTEDSETTLEMENTCOMPLETEDDEBITORACCOUNT`.

```json Get payment status – response
{
  "consentId": "E210000BUJ",
  "payment": {
    "currency": "GBP",
    "amount": 1.00,
    "reference": "GWE-VRP-001"
  },
  "status": "ACCEPTEDSETTLEMENTCOMPLETEDDEBITORACCOUNT",
  "interactionType": "IN_SESSION"
}
```

***

If you would like to test some payment error scenarios - below are some examples. You may also wish to test your own error scenarios.&#x20;

## Error scenario 1: Consent expired

To simulate a rejection caused by an expired consent, submit a payment against a consent whose `validToDate` has elapsed.

```json Expired consent payment request
{
  "consentId": "I000000002",
  "payment": {
    "currency": "GBP",
    "amount": 50,
    "reference": "GWE-VRP-002"
  },
  "interactionType": "OffSession",
  "risk": {
    "merchantCategoryCode": "4900",
    "merchantCustomerIdentification": "CUST-001",
    "contractPresentIndicator": true,
    "beneficiaryPrepopulatedIndicator": true,
    "paymentPurposeCode": "BKDF",
    "categoryPurposeCode": "BONU"
  }
}
```
```json Expired consent payment response
{
  "field": "consentId",
  "code": "INVALID",
  "message": "Consent has expired and cannot be used to initiate payments"
}
```

## Error scenario 2: Individual payment limit exceeded

To simulate a per-payment limit breach, submit a payment where `amount` exceeds the `maximumIndividualAmount` set on the consent. For example, if the consent allows a maximum of £250 per payment, submit a payment of £300.

```json Individual limit exceeded request
{
  "consentId": "I000000001",
  "payment": {
    "currency": "GBP",
    "amount": 300,
    "reference": "GWE-VRP-001"
  },
  "interactionType": "OffSession",
  "risk": {
    "merchantCategoryCode": "4900",
    "merchantCustomerIdentification": "CUST-001",
    "contractPresentIndicator": true,
    "beneficiaryPrepopulatedIndicator": true,
    "paymentPurposeCode": "BKDF",
    "categoryPurposeCode": "BONU"
  }
}
```
```json Individual limit exceeded response
{
  "field": "payment.amount",
  "code": "INVALID",
  "message": "Payment amount exceeds the maximumIndividualAmount permitted by the consent"
}
```

##