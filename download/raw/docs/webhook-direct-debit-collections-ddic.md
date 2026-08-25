---
updatedAt: 2026-06-12T14:18:27.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Webhook - Direct Debit Collections Indemnity Claim (DDIC) 

A webhook notification raised whenever a Direct Debit Indemnity Claim (DDIC) has been received or changes status. This webhook enables Partners and Customers to receive real-time notifications when a new DDIC advice is received from Bacs, when a claim is cancelled following a successful challenge, or when a claim settles against a Collateral account.

This webhook is subscribed to at Customer level and fires for each status transition on an Indemnity Claim.

<Callout icon="📘" theme="info">
  This webhook is part of the DDIC Report Automation project and is available to subscribe from June 30' 2026. It replaces manual email notifications that were previously sent by Payment Operations. Partners who wish to receive real-time claim notifications must explicitly subscribe to this webhook.
</Callout>

## When Does This raised?

The webhook notification will be raised on each of the following status transitions:

| Status    | Circumstances                                                                                                                                             |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| NEW       | A new DDIC advice has been received from Bacs and processed by Direct Debit Service. A new Indemnity Claim record has been created.                       |
| CANCELLED | A cancellation advice has been received from Bacs. The DDIC was successfully challenged and the existing Indemnity Claim record has been cancelled.       |
| REJECTED  | The DDIC settlement transaction has been processed via STS transactional output. The claim amount has been debited from the Partner's Collateral account. |

<br />

## Webhook Parameters

| Parameter         | Type      | Description                                                                                                                                 |
| ----------------- | --------- | :------------------------------------------------------------------------------------------------------------------------------------------ |
| IndemnityClaimId  | String    | Unique ID for the Indemnity Claim. Prefix: ICC. Use this as the primary identifier for deduplication.                                       |
| DdicReference     | String    | DDIC reference received from Bacs. Always prefixed with DDIC. Note: a ddicReference is not unique and may be shared across multiple claims. |
| Reference         | String    | Service User Reference of the mandate associated with the claim. A mandate may have more than one claim at a time.                          |
| Amount            | Decimal   | Total amount for the DDIC advice. Expressed as a decimal with up to 2 decimal places (e.g. 20.02).                                          |
| ReasonCode        | String    | Reason code indicating why the indemnity claim was raised. Examples: INSTRUCTION\_CANCELLED\_BY\_PAYER, ADVANCE\_NOTICE\_DISPUTED.          |
| Status            | String    | Current status of the Indemnity Claim. Possible values: NEW \| CANCELLED \| SETTLED.                                                        |
| TotalDirectDebits | Integer   | Total number of direct debit collections included in the DDIC advice.                                                                       |
| CustomerId        | String    | The Customer ID being notified about the status change. Webhook is subscribed at this customer level.                                       |
| CollectionIds     | String\[] | Array of Modulr collection IDs that have been matched to the direct debits in this DDIC. May be empty if no match could be found.           |
| ChangeDate        | Date      | Date of the status change. Format: YYYY-MM-DD.                                                                                              |
| SchemeId          | String    | Scheme ID of the DDIC advice in Bacs service. Used for reconciliation with the settlement transaction.                                      |
| EventName         | String    | Name of the webhook event                                                                                                                   |
| EventId           | String    | ID of the webhook event                                                                                                                     |
| EventDateTime     | DateTime  | Date and time the event occurred. All timestamps are UTC. Format: ISO 8601 (e.g. 2025-01-03T09:15:00+0000).                                 |

<br />

## Duplication Check

When deduplicating incoming webhook notifications, use indemnityClaimId combined with status. This combination uniquely identifies a specific state transition for a given claim. The same indemnityClaimId will appear with different statuses as the claim progresses through its lifecycle (e.g. NEW → CANCELLED, or NEW → SETTLED).

This is important particularly if a webhook has failed and needs to be resent — ensure you do not process the same state transition twice.

<br />

## Example Webhook Payloads

<br />

```json NEW - New Indemnity Claim Received
{

  "IndemnityClaimId": "ICC3289458",
  "DdicReference": "DDIC-10223264",
  "Reference": "AA3473475",
  "Amount": 20.02,
  "ReasonCode": "INSTRUCTION_CANCELLED_BY_PAYER",
  "Status": "NEW",
  "TotalDirectDebits": 2,
  "CustomerId": "C2100004",
  "CollectionIds": ["K29758748", "K93474575"],
  "ChangeDate": "2025-01-03",
  "SchemeId": "S12345678",
  "EventName": "DD_INDEMNITY_CLAIM_STATUS",
  "EventId": "363f0ba4-a60f-40a9-a644-62fa6552c056",
  "EventDateTime": "2025-01-03T09:15:00+0000"
}

```
```json CANCELLED — Claim Successfully Challenged
{
  "IndemnityClaimId": "ICC3289458",
  "DdicReference": "DDIC-10223264",
  "Reference": "AA3473475",
  "Amount": 20.02,
  "ReasonCode": "INSTRUCTION_CANCELLED_BY_PAYER",
  "Status": "CANCELLED",
  "TotalDirectDebits": 2,
  "CustomerId": "C2100004",
  "CollectionIds": ["K29758748", "K93474575"],
  "ChangeDate": "2025-01-10",
  "SchemeId": "S12345679",
  "EventName": "DD_INDEMNITY_CLAIM_STATUS",
  "EventId": "363f0ba4-a60f-40a9-a644-62fa6552c056",
  "EventDateTime": "2025-01-10T11:32:00+0000"
}
```
```json SETTLED — Claim Settled Against Collateral Account
{
  "IndemnityClaimId": "ICC3289458",
  "DdicReference": "DDIC-10223264",
  "Reference": "AA3473475",
  "Amount": 20.02,
  "ReasonCode": "INSTRUCTION_CANCELLED_BY_PAYER",
  "Status": "SETTLED",
  "TotalDirectDebits": 2,
  "CustomerId": "C2100004",
  "CollectionIds": ["K29758748", "K93474575"],
  "ChangeDate": "2025-01-16",
  "SchemeId": "S12345680",
  "EventName": "DD_INDEMNITY_CLAIM_STATUS",
  "EventId": "363f0ba4-a60f-40a9-a644-62fa6552c056",
  "EventDateTime": "2025-01-16T08:00:00+0000"
}
```

<br />

## Retrieveing Claim Details

On receiving a DD\_INDEMNITY\_CLAIM\_STATUS webhook, Partners can use the indemnityClaimId to retrieve the full details of the claim via the API:

| Status | Circumstances                                                                         |
| ------ | ------------------------------------------------------------------------------------- |
| GET    | /direct-debit-service/indemnity-claims/{'{indemnityClaimId}'}                         |
| GET    | /direct-debit-service/indemnity-claims?accountId={'{accountId}'}\&status={'{status}'} |