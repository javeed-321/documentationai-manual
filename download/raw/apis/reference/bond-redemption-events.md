---
updatedAt: 2025-09-22T14:53:27.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Bond Redemption Events

Test Callable or redeemable bonds are bonds that can be redeemed or paid off by the issuer prior to the bonds' maturity date. When an issuer calls its bonds, it pays investors the call price (usually the face value of the bonds) together with accrued interest to date and, at that point, stops making interest payments.

## Partial Redemption Event

When a customer owns an instrument that is partially called, DriveWealth will create a new transaction in the customers account for the amount that was partially called. The instrument position will remain unchanged. For each partial call, DriveWealth provides information in regards to the partially called amount, and tax status of that transaction.

```json Created
{
    "id": "event_21b70415-e1bf-4df6-9e2b-a420647c93fd",
    "type": "transactions.created",
    "timestamp": "2023-08-02T07:02:31.963891677Z",
    "payload": {
        "accountID": "0dd1b08f-3668-440a-be18-131443d85a47.1551208006668",
        "accountNo": "DWUV000073",
        "userID": "0dd1b08f-3668-440a-be18-131443d85a47",
        "transaction": {
            "accountAmount": 300,
            "accountBalance": 4488.8,
            "comment": "Partially called 30% par value of 3456U123P for cash",
            "finTranID": "GH.356c7d5e-8671-42ed-8387-762960dc032e",
            "wlpFinTranTypeID": "b9d3f58c-da1a-47de-af78-fe59401f396b",
            "finTranTypeID": "PRCAL",
            "feeSec": 0,
            "feeTaf": 0,
            "feeBase": 0,
            "feeXtraShares": 0,
            "feeExchange": 0,
            "positionDelta": 0,
            "instrument": {
                "id": "5b85fabb-d57c-44e6-a7f6-a3efc760226c",
                "symbol": "US3456U123P0",
                "name": "Brookfield Property Partners L.P. 3.8% 2030/06/30"
            },
            "fiCall": {
                "type": "FI_PARTIAL_CALL",
                "callRate": 100,
                "accruedInterest": 3.20,
                "callFactor": 0.3,
                "principalFactor": 0.7
            }
        }
    }
}
```

## Full Redemption Event

When customer owns a instrument that is fully called, DriveWealth will create a new transaction in the customers account for the amount that was fully called. The instrument position will be zeroed. For each full call, DriveWealth provides information in regards to the called amount, and tax status of that transaction.

```json Created
{
    "id": "event_21b70415-e1bf-4df6-9e2b-a420647c93fd",
    "type": "transactions.created",
    "timestamp": "2023-08-02T07:02:31.963891677Z",
    "payload": {
        "accountID": "0dd1b08f-3668-440a-be18-131443d85a47.1551208006668",
        "accountNo": "DWUV000073",
        "userID": "0dd1b08f-3668-440a-be18-131443d85a47",
        "transaction": {
            "accountAmount": 3000,
            "accountBalance": 4488.8,
            "comment": "Fully called at 100% par value of 3456U123P for cash",
            "finTranID": "GH.356c7d5e-8671-42ed-8387-762960dc032e",
            "wlpFinTranTypeID": "b9d3f58c-da1a-47de-af78-fe59401f396b",
            "finTranTypeID": "FULCL",
            "feeSec": 0,
            "feeTaf": 0,
            "feeBase": 0,
            "feeXtraShares": 0,
            "feeExchange": 0,
            "positionDelta": -3,
            "instrument": {
                "id": "5b85fabb-d57c-44e6-a7f6-a3efc760226c",
                "symbol": "US3456U123P0",
                "name": "Brookfield Property Partners L.P. 3.8% 2030/06/30"
            },
            "fiCall": {
                "type": "FI_FULL_CALL",
                "accruedInterest": 3.20,
                "callRate": 100
            }
        }
    }
}
```

The position update event will be made for the removal of instrument that were previously held.

```json Updated
{
    "id": "event_5d5a4a88-fc05-4d53-b0bf-27801ef028c9",
    "type": "positions.updated",
    "timestamp": "2023-08-02T07:02:31.949597191Z",
    "payload": {
        "accountID": "0dd1b08f-3668-440a-be18-131443d85a47.1551208006668",
        "accountNo": "DWUV000073",
        "userID": "0dd1b08f-3668-440a-be18-131443d85a47",
        "updateReason": "FI_FULL_CALL",
        "previous": {
            "costBasis": 2700,
            "openQty": 3,
            "symbol": "US3456U123P0",
            "avgPrice": 900.00
        },
        "current": {
            "costBasis": 0,
            "openQty": 0,
            "symbol": "US3456U123P0"
        }
    }
}
```