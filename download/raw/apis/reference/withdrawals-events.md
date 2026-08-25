---
updatedAt: 2026-08-13T02:07:54.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Withdrawal Events

> 👍 Withdrawals vs Redemptions
>
> Redemptions and withdrawals mean the same thing and are used throughout the guides and API reference interchangeably. So when you see redemptions think withdrawals and vice versa.

## Withdrawals Created

A new withdrawal has been created in a user's account.

```json Created
{
    "id": "event_a296f5ba-3366-43dd-a0da-4e9a48ab7d57",
    "type": "redemptions.created",
    "timestamp": "2019-09-23T07:08:14.121518146Z",
    "payload": {
        "paymentID": "DWTY000222-1569532743890-RXUCH",
        "category": "REDEMPTION",
        "type": "WIRE",
        "amount": -100.0,
        "currency": "USD",
        "status": 1,
        "statusMessage": "Pending",
        "userID": "30b250c6-8e85-40e0-937f-0b0689691b38",
        "accountID": "30b250c6-8e85-40e0-937f-0b0689691b38.1569532274142",
        "transactionCode": "RECEIPT_WIRE",
        "description": "Cash Disbursement - Wire",
        "note": "Here's some money",
        "metadata": {
            "clientWithdrawalRef": "WD-20260807-0043"
        }
    }
}
```

## Withdrawals Updated

A withdrawal has been updated.

```json Updated
{
    "id": "event_a296f5ba-3366-43dd-a0da-4e9a48ab7d57",
    "type": "redemptions.updated",
    "timestamp": "2019-09-23T07:08:14.121518146Z",
    "payload": {
        "paymentID": "DWTY000222-1569532743890-RXUCH",
        "category": "REDEMPTION",
        "type": "ACH",
        "amount": -100.0,
        "currency": "USD",
        "status": 2,
        "statusMessage": "Successful",
        "userID": "30b250c6-8e85-40e0-937f-0b0689691b38",
        "accountID": "30b250c6-8e85-40e0-937f-0b0689691b38.1569532274142",
        "finTranRef": "GA.59ef9888-abb9-4b8d-95ce-e2a6cac7d576",
        "transactionCode": "CSD",
        "description": "Cash Disbursement - Wire",
        "note": "Here's some money",
        "metadata": {
            "clientWithdrawalRef": "WD-20260807-0043"
        }
    }
}
```