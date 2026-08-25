---
updatedAt: 2026-03-13T16:03:39.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Webhook - Customer Status

For Partners, to be notified that a Customer is fully Approved as part of the KYC/KYB process.

## Customer Status

The `CUSTOMER_STATUS` event is triggered when a Partner's customer status is updated as the customer progresses through the KYC/KYB Process.

This notification type is available to all of Modulr's Partners, but not Direct Customers. It notifies you when a Customer has passed final Verification checks so that you can create Accounts.

| Parameter  | Description                                                                         |
| ---------- | ----------------------------------------------------------------------------------- |
| EventId    | Unique identifier for the webhook event. This may change if the webhook is re-sent. |
| EventName  | `CUSTOMER_STATUS`                                                                   |
| EventTime  | Date and timestamp of the event. All dates and times are UTC.                       |
| Status     | Updated status of the customer either `ACTIVE` or `BLOCKED`                         |
| CustomerId | Modulr unique customer reference for the impacted customer.                         |

## Example CUSTOMER\_STATUS Webhook

```json
{
  "EventId": "eb543484-0a6e-4e7f-8fe9-a2fec82e6d60",
  "EventName": "CUSTOMER_STATUS",
  "EventTime": "2025-10-01T21:37:28+0000",
  "Status": "BLOCKED",
  "CustomerId": "C2100001"
}
```