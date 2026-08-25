---
updatedAt: 2025-09-22T15:01:32.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Merger & Acquisitions Events

M\&A corporate events consist of a bit more data because of updates that need to be made to cash and share positions. When an M\&A event does occur there will be four (4) events created; Two `transaction.created` (changes in cash), and two `positions.updated` (removal of one symbol and addition of another). The sequence of events you would see are the following:

## First Transaction Event\*\*

* The first transaction event will be the addition of the acquirers shares as part of the merger or acquisition.

```json Created
{
    "id": "event_ff31400a-565a-4c35-9782-279313f18521",
    "type": "transactions.created",
    "timestamp": "2019-08-02T07:02:31.858026996Z",
    "payload": {
        "accountID": "0dd1b08f-3668-440a-be18-131443d85a47.1551208006668",
        "accountNo": "DWUV000073",
        "userID": "0dd1b08f-3668-440a-be18-131443d85a47",
        "transaction": {
            "accountAmount": 0,
            "accountBalance": 3616.2,
            "comment": "Added 5.51 shares of FB (part of merger/acquisition of TWTR by FB)",
            "finTranID": "GH.081b1011-7923-49fe-9144-aa1b555f0873",
            "wlpFinTranTypeID": "b9d3f58c-da1a-47de-af78-fe59401f396b",
            "finTranTypeID": "MERGER_ACQUISITION",
            "feeSec": 0,
            "feeTaf": 0,
            "feeBase": 0,
            "feeXtraShares": 0,
            "feeExchange": 0,
            "positionDelta": 5.51,
            "instrument": {
                "id": "4312a85c-b50d-4adb-93ba-cc7973243a53",
                "symbol": "FB",
                "name": "Facebook, Inc."
            },
            "mergerAcquisition": {
                "type": "ADD_SHARES",
                "acquirer": {
                    "id": "4312a85c-b50d-4adb-93ba-cc7973243a53",
                    "symbol": "FB",
                    "name": "Facebook, Inc."
                },
                "acquiree": {
                    "id": "bf4fc752-a5f4-4801-a416-0d75087c9779",
                    "symbol": "TWTR",
                    "name": "Twitter, Inc."
                }
            }
        }
    }
}
```

In this example we see that Facebook bought Twitter, and so we `ADD_SHARES` to the customers account. In this case 5.51 shares of FB were added (`positionDelta`).

## Second Transaction Event

The second transaction event will be the removal of the acquiree's shares and addition of any cash as a result of the merger or acquisition.

```json Created
{
    "id": "event_88602b5d-a189-4a0a-b4f7-941ad9a2fb4a",
    "type": "transactions.created",
    "timestamp": "2019-08-02T07:02:31.844056197Z",
    "payload": {
        "accountID": "0dd1b08f-3668-440a-be18-131443d85a47.1551208006668",
        "accountNo": "DWUV000073",
        "userID": "0dd1b08f-3668-440a-be18-131443d85a47",
        "transaction": {
            "accountAmount": 122.320596405,
            "accountBalance": 3616.2,
            "comment": "Removed 11.64958061 shares of TWTR (part of merger/acquisition of TWTR by FB)",
            "finTranID": "GH.b06c05f5-e1da-4989-9f4d-fbe5d8be4ac1",
            "wlpFinTranTypeID": "b9d3f58c-da1a-47de-af78-fe59401f396b",
            "finTranTypeID": "MERGER_ACQUISITION",
            "feeSec": 0,
            "feeTaf": 0,
            "feeBase": 0,
            "feeXtraShares": 0,
            "feeExchange": 0,
            "positionDelta": -11.64958061,
            "instrument": {
                "id": "bf4fc752-a5f4-4801-a416-0d75087c9779",
                "symbol": "TWTR",
                "name": "Twitter, Inc."
            },
            "mergerAcquisition": {
                "type": "REMOVE_SHARES_ADD_CASH",
                "acquirer": {
                    "id": "4312a85c-b50d-4adb-93ba-cc7973243a53",
                    "symbol": "FB",
                    "name": "Facebook, Inc."
                },
                "acquiree": {
                    "id": "bf4fc752-a5f4-4801-a416-0d75087c9779",
                    "symbol": "TWTR",
                    "name": "Twitter, Inc."
                }
            }
        }
    }
}
```

In this example we see that we removed the existing position of TWTR, and added the cash due to the customer.

## First Position Update Event

* The first position update will be for the addition of the acquiring company's shares.

```json Updated
{
    "id": "event_fc0df771-084b-4d4c-b1b4-2f5cb5b86ad7",
    "type": "positions.updated",
    "timestamp": "2019-08-02T07:02:31.827375527Z",
    "payload": {
        "accountID": "0dd1b08f-3668-440a-be18-131443d85a47.1551208006668",
        "accountNo": "DWUV000073",
        "userID": "0dd1b08f-3668-440a-be18-131443d85a47",
        "updateReason": "MERGER_AND_ACQUISITION",
        "previous": {
            "costBasis": 500,
            "openQty": 11.64958061,
            "symbol": "TWTR",
            "avgPrice": 42.92
        },
        "current": {
            "costBasis": 0,
            "openQty": 0,
            "symbol": "TWTR"
        }
    }
}
```

In this example we can see that we removed all shares of TWTR as a part of the merger or acquisition.