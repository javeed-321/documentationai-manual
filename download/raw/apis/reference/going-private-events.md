---
updatedAt: 2025-09-22T15:01:29.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Going Private Events

In the event that a company goes private, there will be one `transactions.create` event and one `positions.updated` event.

## Transaction Created

* The transaction created event is going to be the exchange of cash for shares held in the company going private

```json Created
{
    "id": "event_21b70415-e1bf-4df6-9e2b-a420647c93fd",
    "type": "transactions.created",
    "timestamp": "2019-08-02T07:02:31.963891677Z",
    "payload": {
        "accountID": "0dd1b08f-3668-440a-be18-131443d85a47.1551208006668",
        "accountNo": "DWUV000073",
        "userID": "0dd1b08f-3668-440a-be18-131443d85a47",
        "transaction": {
            "accountAmount": 872.6003454,
            "accountBalance": 4488.8,
            "comment": "Exchanged 2.07761987 shares of TSLA for cash (merger/acquisition)",
            "finTranID": "GH.356c7d5e-8671-42ed-8387-762960dc032e",
            "wlpFinTranTypeID": "b9d3f58c-da1a-47de-af78-fe59401f396b",
            "finTranTypeID": "MERGER_ACQUISITION",
            "feeSec": 0,
            "feeTaf": 0,
            "feeBase": 0,
            "feeXtraShares": 0,
            "feeExchange": 0,
            "positionDelta": -2.07761987,
            "instrument": {
                "id": "5b85fabb-d57c-44e6-a7f6-a3efc760226c",
                "symbol": "TSLA",
                "name": "Tesla Motors, Inc."
            },
            "mergerAcquisition": {
                "type": "EXCHANGE_STOCK_CASH",
                "acquirer": {
                    "id": "5b85fabb-d57c-44e6-a7f6-a3efc760226c",
                    "symbol": "TSLA",
                    "name": "Tesla Motors, Inc."
                },
                "acquiree": {
                    "id": "5b85fabb-d57c-44e6-a7f6-a3efc760226c",
                    "symbol": "TSLA",
                    "name": "Tesla Motors, Inc."
                }
            }
        }
    }
}
```

## Position Updated

* The position update event will be made for the removal of shares that were previously held in the security

```json Updated
{
    "id": "event_5d5a4a88-fc05-4d53-b0bf-27801ef028c9",
    "type": "positions.updated",
    "timestamp": "2019-08-02T07:02:31.949597191Z",
    "payload": {
        "accountID": "0dd1b08f-3668-440a-be18-131443d85a47.1551208006668",
        "accountNo": "DWUV000073",
        "userID": "0dd1b08f-3668-440a-be18-131443d85a47",
        "updateReason": "MERGER_AND_ACQUISITION",
        "previous": {
            "costBasis": 500,
            "openQty": 2.07761987,
            "symbol": "TSLA",
            "avgPrice": 240.66
        },
        "current": {
            "costBasis": 0,
            "openQty": 0,
            "symbol": "TSLA"
        }
    }
}
```