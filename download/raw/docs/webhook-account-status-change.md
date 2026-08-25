---
updatedAt: 2025-09-05T18:28:54.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Webhook - Account Status Change

The Account Status Change webhook is used to notify subscribed users that an account has changed status so may be blocked from making or receiving payments, or have been returned to being able to being available for payment processing.

```json ACCOUNT_STATUS_CHANGE
{
 "EventName": "ACCOUNTSTATUSCHANGE",
 "EventTime": "2023-02-02T02:02:02+0000",
 "AccountId" : "A210A21023",
 "CustomerId": "C210C21023",
 "OldStatus": "ACTIVE",
 "NewStatus": "BLOCKED"
}
```