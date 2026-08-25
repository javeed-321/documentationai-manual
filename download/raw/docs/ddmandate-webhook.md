---
updatedAt: 2026-05-07T08:01:36.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Webhook - Direct Debit Mandate Status

Applicable to the Direct Debit Outbound and Direct Debit Collections services

## Direct Debit Mandate Status

The `DDMANDATE` event is triggered when there is a status change to a Direct Debit Mandate for **both the Direct Debit Collections and Direct Debit Outbound services.**

## Example DDMANDATE Webhook

```json DDMANDATE Webhook Example
{
	"EventId": "3c4f3c54-b8e3-4a8b-a1f9-f68429c449c6",
	"AccountId": "A120C8D3",
	"EventName": "DDMANDATE",
  "EventTime": "2020-01-01T03:27:41+0000",  
  "CustomerId": "C130CYKD",
  "ExternalReference": "4F82222B86J99",
  "Reference": "GYM-8973XC",
  "MandateId": "M101BPSG",
  "NewStatus": "ACTIVE",
  "OldStatus": "SUBMITTED",
  "ReasonCode":"INSTRUCTION_CANCELLED_BY_PAYER",
  "ReasonMessage":"Instruction has been cancelled by Payer",
  "OldDueDate":"2021-05-04",
  "RequestedDueDate":"2021-05-14",
  "OldPaymentFrequency":"W",
  "RequestedPaymentFrequency":"M",
  "OldAmountOfPayment":"34.56",
  "RequestedAmountOfPayment":"35.78",
  "EffectivePaymentDate":"2021-05-14",
  "RequestedLastPaymentDate":"2022-05-14",
  "NewAccountName":"JOE BLOGGS",
  "NewAccountNumber":"11111111",
  "NewAccountSortCode":"010101",
  "OldAccountName":"JOE M BLOGGS",
  "OldAccountNumber":"12121212",
  "OldAccountSortCode":"020202"
}
```

**Please note that only non-null fields will be sent. If a field has no value, then it will not be part of the webhook.**

## Mandate Status

Mandates can have the following status during its lifecycle in the respective services. A `DDMANDATE` event is triggered on any progression between states, and the webhook will give the `OldStatus` and `NewStatus`

| Service                  | Status    | Meaning                                                                                                |
| :----------------------- | :-------- | :----------------------------------------------------------------------------------------------------- |
| Direct Debit Collections | Pending   | The Mandate has been created and has not yet been sent to BACS for processing                          |
| Direct Debit Collections | Submitted | The Mandate has been sent to BACS and waiting for the final decision                                   |
| Direct Debit Collections | Active    | The Mandate has successfully lodged.                                                                   |
| Direct Debit Collections | Rejected  | The mandate was rejected by the Payer's Bank. Modulr receives a BRAUDDIS file to explain the rejection |
| Direct Debit Collections | Cancelled | An existing mandate was cancelled                                                                      |
|                          |           |                                                                                                        |
| Direct Debit Outbound    | Active    | There is an active mandate lodged on our Partner's account                                             |
| Direct Debit Outbound    | Cancel    | An existing Mandate was cancelled by our Partner                                                       |
| Direct Debit Outbound    | Reject    | The Mandate was rejected during lodgement                                                              |
| Direct Debit Outbound    | Expire    | The Mandate has expired                                                                                |

## Webhook fields & old/new values

A list of all possible fields; please note that only non-null fields will be sent. If a field has no value, then it will not be part of the webhook. Where possible, old/new values showing the progression of fields are given.

| Parameter                 | Description                                                                        |
| :------------------------ | :--------------------------------------------------------------------------------- |
| EventId                   | Unique id for the webhook event. This can change if webhook needs to be resent.    |
| AccountId                 | Modulr Unique Account reference for the account that the mandate is linked to.     |
| EventName                 | Type of event: DDMANDATE - DD Mandate Status Update                                |
| EventTime                 | Date and Timestamp for the Event - All Dates and times are UTC based.              |
| CustomerId                | Modulr Unique Customer Reference for the customer that the mandate is linked to.   |
| ExternalReference         | This is the reference you can set on the mandate to correlate back to your system. |
| Reference                 | Reference of the mandate to match with the collections                             |
| MandateId                 | Modulr Unique Mandate reference.                                                   |
| NewStatus                 | Updated mandate status.                                                            |
| OldStatus                 | Previous mandate status.                                                           |
| ReasonCode                | Reason Code for any failed mandates                                                |
| ReasonMessage             | Reason Message for any failed mandates                                             |
| OldDueDate                | Collection due date before the change                                              |
| RequestedDueDate          | Collection due date after the change                                               |
| OldPaymentFrequency       | Collection frequency before the change                                             |
| RequestedPaymentFrequency | Collection frequency after the change                                              |
| OldAmountOfPayment        | Collection amount before the change                                                |
| RequestedAmountOfPayment  | Collection amount after the change                                                 |
| EffectivePaymentDate      | Date of the last collection before the change                                      |
| RequestedLastPaymentDate  | Date of the last collection after the change                                       |
| NewAccountName            | New account name of the customer                                                   |
| NewAccountNumber          | New account number of the customer                                                 |
| NewAccountSortCode        | New account sort code of the customer                                              |
| OldAccountName            | Old account name of the customer                                                   |
| OldAccountNumber          | Old account name of the customer                                                   |
| OldAccountSortCode        | Old account sort code of the customer                                              |

## ADDACS Reason Codes

A `DDMANDATE` event is triggered for the Direct Debit Collections service when Modulr receives an ADDACS (Automated Direct Debit Amendment and Cancellation Service) advice from a bank holding a Direct Debit Instruction (mandate) from you. The changes are automatically applied to the mandate held in the Modulr system, but you may want to also update any external system (for example when a payer changes bank account details).

The `ReasonCode` and `ReasonMessage` may be:

| Code | Reason                                                             |
| ---- | ------------------------------------------------------------------ |
| 0    | Instruction cancelled – Refer to payer                             |
| 1    | Instruction cancelled by payer                                     |
| 2    | Payer deceased                                                     |
| 3    | Account transferred to a new bank or building society              |
| B    | Account closed                                                     |
| C    | Account transferred to a different branch of bank/building society |
| D    | Advance notice disputed                                            |
| E    | Instruction amended                                                |
| R    | Instruction re-instated                                            |

## Bank Rejected AUDDIS reasons

A `DDMANDATE` event is also triggered in the DD Collections service when a Bank rejects a Direct Debit Instruction (Mandate) - in this case, the `ReasonCode` and `ReasonMessage` will be given alongside the status change to `REJECTED`

| Code | Reason                                                                 |
| ---- | ---------------------------------------------------------------------- |
| 1    | Instruction cancelled by payer                                         |
| 2    | Payer deceased                                                         |
| 3    | Account transferred                                                    |
| 5    | No account                                                             |
| 6    | No Instruction                                                         |
| 7    | DDI amount not zero                                                    |
| B    | Account closed                                                         |
| C    | Account transferred to a different branch of the bank/building society |
| F    | Invalid account type                                                   |
| G    | Bank will not accept Direct Debits on account                          |
| H    | Instruction has expired                                                |
| I    | Payer Reference is not unique                                          |
| K    | Instruction cancelled by paying PSP                                    |
| L    | Incorrect payer’s account details                                      |
| M    | Transaction code / user status incompatible                            |
| N    | Transaction disallowed at payer’s branch                               |
| O    | Invalid reference                                                      |
| P    | Payer’s name not present                                               |
| Q    | Service user’s name blank                                              |