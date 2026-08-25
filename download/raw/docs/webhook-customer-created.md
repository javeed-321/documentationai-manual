---
updatedAt: 2026-06-11T09:56:38.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Webhook - Customer Created

Modulr sends this webhook once a customer's application has been approved and their record has been created on the Modulr platform. This is the signal that the customer is ready to have their first payment account created.

***

## When it fires

After an application reaches `APPROVED` status, following completion of CDD review.

***

## Payload

```json
{
  "eventDateTime": "2026-04-27T13:19:34.457092669Z",
  "eventName": "CUSTOMER_CREATED",
  "applicationId": "APP21000MG",
  "customerId": "C210000A"
}
```

### Fields

| Field           | Type              | Description                                           |
| --------------- | ----------------- | ----------------------------------------------------- |
| `eventDateTime` | string (ISO 8601) | Timestamp of customer creation.                       |
| `eventName`     | string            | Always `CUSTOMER_CREATED`.                            |
| `applicationId` | string            | The application ID that was approved.                 |
| `customerId`    | string            | The newly created customer ID on the Modulr platform. |

***

## What to do

1. **Store the `customerId`** against your customer record and maintain its association with the `applicationId`.
2. **Proceed with account creation** using the `customerId` in subsequent Account Creation API calls.

***

## Implementation notes

* Your handler must be idempotent - the same event may be delivered more than once.
* Respond with `HTTP 200` to acknowledge receipt. Modulr will retry on failure.
* The `customerId` remains constant across the customer's lifetime on Modulr, even when new Application IDs are generated for CDD refresh cycles.

***

## Related

* [Webhook - Application Status Change](https://modulr.readme.io/docs/webhook-application-status-change)
* [Webhook - Customer Status Change](https://modulr.readme.io/docs/customer-status)
* [Integration Guide](https://modulr.readme.io/docs/customer-verification-integration-guide)