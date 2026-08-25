---
updatedAt: 2025-09-05T18:36:18.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Webhook - Direct Debit, Return Funds

The Returned Funds Notification is used to inform our Partner that the funds associated with an unpaid collections have been returned by the scheme and credited to the Partner's main account. Applicable only for Direct Debit Outbound service.

```json DD_FUNDS_RETURNED
{
 "EventName": "DD_FUNDS_RETURNED",
 "EventId": "c374a2e6-09d3-41b5-9172-57749fc48c37",
 "EventTime": "2019-01-11T16:54:57+0100",
 "ClaimId" : "C020005J",
 "SettlementDate": "2019-01-11T15:54:57.617+0000",
 "AccountId": "A020005E",
 "Amount": 100
}
```