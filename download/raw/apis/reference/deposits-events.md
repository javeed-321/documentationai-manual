---
updatedAt: 2026-08-22T01:44:42.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Deposit Events

## Deposit Created

A new deposit has been created for a user's account.

```json Created
{
    "id": "event_a296f5ba-3366-43dd-a0da-4e9a48ab7d57",
    "type": "deposits.created",
    "timestamp": "2019-09-23T07:08:14.121518146Z",
    "payload": {
        "paymentID": "DWTY000222-1569532743890-DXUCH",
        "category": "DEPOSIT",
        "type": "ACH",
        "amount": 1000,
        "currency": "USD",
        "status": 1,
        "statusMessage": "Pending",
        "statusComment": "",
        "created": "2019-09-26T21:19:03.890Z",
        "userID": "30b250c6-8e85-40e0-937f-0b0689691b38",
        "accountID": "30b250c6-8e85-40e0-937f-0b0689691b38.1569532274142",
        "transactionCode": "RECEIPT_IRA_ROLLOVER",
        "description": "Cash Receipt - Rollover IRA Contribution",
        "note": "Here's some money",
        "finTranRef": "GA.59ef9888-abb9-4b8d-95ce-e2a6cac7d576",
        "depositBuyingPowerHoldExpires": null,
        "seasoningPeriodExpires": null,
        "recurringDepositID": "DWTY000222-1349532743890-DXUHG",
        "failureReason": null,
        "metadata": {
            "clientDepositRef": "DEP-20260807-0042"
        }
    }
}
```

## Deposit Updated

A deposit has been updated.

```json Updated
{
    "id": "event_a296f5ba-3366-43dd-a0da-4e9a48ab7d57",
    "type": "deposits.updated",
    "timestamp": "2019-09-23T07:08:14.121518146Z",
    "payload": {
        "paymentID": "DWTY000222-1569532743890-DXUCH",
        "category": "DEPOSIT",
        "type": "ACH",
        "amount": 1000,
        "currency": "USD",
        "status": 2,
        "statusMessage": "Successful",
        "userID": "30b250c6-8e85-40e0-937f-0b0689691b38",
        "accountID": "30b250c6-8e85-40e0-937f-0b0689691b38.1569532274142",
        "finTranRef": "GA.59ef9888-abb9-4b8d-95ce-e2a6cac7d576",
        "failureReason": null,
        "transactionCode": "RECEIPT_IRA_ROLLOVER",
        "description": "Cash Receipt - Rollover IRA Contribution",
        "depositBuyingPowerHoldExpires": "2019-09-26T00:00:00Z",
        "seasoningPeriodExpires": "2019-09-27T00:00:00Z",
        "statusPhase": "BUYING_POWER_WITHHELD",
        "recurringDepositID": "DWTY000222-1349532743890-DXUHG",
        "note": "Here's some money",
        "metadata": {
            "clientDepositRef": "DEP-20260807-0042"
        }
    }
}
```
```json Updated [returned]
{
    "id": "event_2dc6fdd2-bb21-4ea4-8c03-f21a0f2976d3",
    "type": "deposits.updated",
    "timestamp": "2021-02-18T18:11:01.789491275Z",
    "payload": {
        "paymentID": "DWDF000107-1613671790556-D8XDS",
        "statusMessage": "RETURNED",
        "category": "DEPOSIT",
        "type": "ACH_MANUAL",
        "currency": "USD",
        "note": "Here's some money",
        "amount": 112,
        "status": 5,
        "accountID": "03bb51b9-64c9-40f7-8256-7bf8ab28c64a.1595613638739",
        "userID": "03bb51b9-64c9-40f7-8256-7bf8ab28c64a",
        "transactionCode": "RECEIPT_ACH_SVB",
        "description": "Cash Receipt - ACH",
        "metadata": {
            "clientDepositRef": "DEP-20260807-0042"
        }
    }
}
```
```json Updated [cash promotion]
{
    "id": "event_1b9bd3ff-702f-4528-9ebf-6aadd7aa9b31",
    "type": "deposits.updated",
    "timestamp": "2019-09-23T07:08:14.121518146Z",
    "payload": {
        "paymentID": "DWTX000087-1689769558412-DSHV7",
        "statusMessage": "Failed",
        "category": "DEPOSIT",
        "type": "CASH_PROMOTION",
        "currency": "USD",
        "note": "Here's some money",
        "amount": 100,
        "status": 3,
        "accountID": "e4a98fc4-bb75-4e1f-89b4-6d5447af5b06.1619547527786",
        "userID": "e4a98fc4-bb75-4e1f-89b4-6d5447af5b06",
        "transactionCode": "RECEIPT_CASH_PROMOTION",
        "description": "Cash Receipt - Cash Promotion",
        "failureReason": "Unable to create either deposit or redemption finTran",
        "metadata": {
            "clientDepositRef": "DEP-20260807-0042"
        }
    }
}
```