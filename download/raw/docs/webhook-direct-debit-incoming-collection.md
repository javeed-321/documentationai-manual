---
updatedAt: 2025-09-05T18:48:37.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Webhook - Direct Debit, Incoming Collection

Applicable only for Direct Debit Outbound service.

The Incoming Collection Notification is used to inform our partner that a collection has been received, accepted or rejected and if accepted, that a debit of the customer's account will follow in the scheme pre-defined time period. Applicable only for Direct Debit Outbound service.

```json DD_INCOMING_DEBIT
{
  "Amount": "10.00",
  "ClaimId": "D110P5YY",
  "EventId": "ff62f4d1-a59a-47b0-819f-a3da7a890df0",
  "AccountId": "A1100FTQW6",
  "EventName": "DDINCOMINGDEBIT",
  "EventTime": "2022-07-28T09:56:53+0000",
  "MandateId": "M1101WN3",
  "MerchantName": "Modulr Customer 01",
  "MerchantNumber": "123456",
  "SettlementDate": "2022-07-29T00:00:00.000+0000",
  "MerchantReference": "DDOSAUTOMATEDTEST",
  "Status": "REJECTED",
  "RejectionCode": "B"
}
```

## Status & Rejection codes

A status of `REJECTED` means that the incoming Direct Debit immediately been identified for a reason that would prevent the application of the Direct Debit. These Direct Debits will have ARUDD generated so the payer bank returns the Direct Debit unpaid, and will not attempt to be applied to the account.  The `RejectionCode` values indicating ARUDD generation at this stage are:

| Code | Reason                             | Circumstances                                                                                                                                                                                 |
| :--- | :--------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0    | Refer to payer                     | The paying PSP is not in a position to pay the Direct Debit; e.g. account is blocked                                                                                                          |
| 1    | Instruction cancelled              | Instruction cancelled by payer or his bank                                                                                                                                                    |
| 2    | Payer deceased                     | Payer deceased                                                                                                                                                                                |
| 3    | Account transferred                | Account transferred to a new bank or building society                                                                                                                                         |
| 5    | No account (OR wrong account type) | Account Number is not recognised at the paying bank                                                                                                                                           |
| 6    | No Instruction                     | No Instruction held with paying PSP                                                                                                                                                           |
| 8    | Amount not yet due                 | Payer states date of debiting is in advance of the due date specified in the advance notice to the payer. AUDDIS service users only – It is less than 2 working days since the DDI was lodged |
| A    | Service user differs               | Identity of service user differs from DDI                                                                                                                                                     |
| B    | Account closed                     | Payer has closed their account for an unknown reason                                                                                                                                          |

A status of `ACCEPTED` means that the incoming Direct Debit has been accepted as eligible to be applied to the account.   The application may still result in ARUDD generation, e.g. insufficient balance on account after the initial debit and retry attempt will generate a Reason Code 0 (Refer to Payer) return.

As ARUDD returns are generated on Day 3 of the Direct Debit cycle, the[ Unpaid Collection](https://dash.readme.com/project/modulr/v2.2/docs/webhook-direct-debit-unpaid-collection) webhook will be triggered for each unpaid collection