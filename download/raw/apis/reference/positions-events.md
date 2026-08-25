---
updatedAt: 2025-09-22T15:02:01.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Position Events

## Positions Updated

A user's account positions has been updated by DriveWealth operations staff or by a corporate action like a stock split, stock dividend or a symbol change.

```json Updated [manual]
{
    "id": "event_704378d9-8c3c-4b38-9230-181aa53791cd",
    "type": "positions.updated",
    "timestamp": "2019-03-28T23:10:45.779100609Z",
    "payload": {
        "accountID": "b25f0d36-b4e4-41f8-b3d9-9249e46402cd.1403540676095",
        "accountNo": "DWZR000001",
        "userID": "b25f0d36-b4e4-41f8-b3d9-9249e46402cd",
        "updateReason": "MANUAL",
        "previous": {
            "costBasis": 23.94,
            "openQty": 1.944,
            "symbol": "AAON",
            "avgPrice": 12.32
        },
        "current": {
            "costBasis": 23.9436,
            "openQty": 1.9436,
            "symbol": "AAON",
            "avgPrice": 12.32
        }
    }
}
```
```json Updated [spinoff]
{
    "id": "event_22f840b1-80c8-4d72-9f10-07315ffd30fb",
    "type": "positions.updated",
    "timestamp": "2019-03-29T07:02:33.200962333Z",
    "payload": {
        "accountID": "272472de-6522-41be-85a6-31af662251dc.1520386265152",
        "accountNo": "DWFE000039",
        "userID": "272472de-6522-41be-85a6-31af662251dc",
        "updateReason": "SPINOFF",
        "spinoff": {
            "parentCompanySymbol": "CLEG"
        },
        "previous": {
            "openQty": 0,
            "symbol": "BMY.RT"
        },
        "current": {
            "openQty": 0.00915499,
            "symbol": "BMY.RT"
        }
    }
}
```
```json Updated [stock split]
{
    "id": "event_c4b2c210-ce32-41d4-a9a1-cfad4fdf191c",
    "type": "positions.updated",
    "timestamp": "2019-03-29T07:02:33.200962333Z",
    "payload": {
        "accountID": "272472de-6522-41be-85a6-31af662251dc.1520386265152",
        "accountNo": "DWFE000039",
        "userID": "272472de-6522-41be-85a6-31af662251dc",
        "updateReason": "STOCK_SPLIT",
        "previous": {
            "costBasis": 2.8,
            "openQty": 1,
            "symbol": "CPLP",
            "avgPrice": 2.8
        },
        "current": {
            "costBasis": 2.8,
            "openQty": 0.14286,
            "symbol": "CPLP",
            "avgPrice": 19.6
        }
    }
}
```
```json Updated [ACATs inbound]
{
    "id": "event_faecc66d-5d15-4698-8967-30744f1f2d14",
    "type": "positions.updated",
    "timestamp": "2019-09-27T11:54:47.752978141Z",
    "payload": {
        "accountID": "b2124bd2-467d-4a5e-8864-7b8b9f5809aa.1552418271646",
        "accountNo": "DWBG000076",
        "userID": "b2124bd2-467d-4a5e-8864-7b8b9f5809aa",
        "updateReason": "ACATS_STOCK",
        "acats": {
            "type": "INCOMING",
            "brokerDTCNo": "524",
            "referenceNo": "ACAT21182",
            "controlNo": "20192560028977"
        },
        "previous": {
            "openQty": 0,
            "symbol": "NVDA"
        },
        "current": {
            "openQty": 80,
            "symbol": "NVDA"
        }
    }
}
```
```json Updated [ACATs outbound]
{
  "id": "event_faecc66d-5d15-4698-8967-30744f1f2d14",
  "type": "positions.updated",
  "timestamp": "2019-09-27T11:54:47.752978141Z",
  "payload": {
    "accountID": "b2124bd2-467d-4a5e-8864-7b8b9f5809aa.1552418271646",
    "accountNo": "DWBG000076",
    "userID": "b2124bd2-467d-4a5e-8864-7b8b9f5809aa",
    "updateReason": "ACATS_STOCK",
    "acats": {
      "type":"OUTGOING",
      "brokerDTCNo": "524",
      "referenceNo":"ACAT21182",
      "controlNo":"20192560028977"
    },
    "previous": {
      "openQty": 80,
      "costBasis":11,425
      "symbol": "NVDA"
    },
    "current": {
      "openQty": 0,
      "symbol": "NVDA"
    }
  }
}
```
```json Updated [option ca]
{
  "id": "event_37dd24e5-06b5-4258-9845-48747a3ca431",
  "type": "positions.updated",
  "timestamp": "2023-11-29T00:24:46.974213515Z",
  "payload": {
    "accountID": "c92f59dc-3780-4be4-bec8-4228b6187502.1691043473709",
    "accountNo": "DPBN000043",
    "userID": "c92f59dc-3780-4be4-bec8-4228b6187502",
    "updateReason": "OPTION_CA",
    "from": {
      "symbol": "AAPL231110C00250000",
      "instrumentID": "6563cbf2-0ae2-4782-a6b4-80b07ba1ce8d",
      "previous": {
        "costBasis": 421.52,
        "openQty": 88,
        "avgPrice": 5
      },
      "current": {
        "costBasis": 421.52,
        "openQty": 0
      }
    },
    "to": {
      "symbol": "AAPL231110C00265000",
      "instrumentID": "d0082eac-d89c-4354-ae04-0ddf385d04d7",
      "previous": {
        "costBasis": 0,
        "openQty": 0
      },
      "current": {
        "costBasis": 421.52,
        "openQty": 88,
        "avgPrice": 4.79
      }
    }
  }
}
```
```json Updated [options exercise]
{
  "id": "event_b6635686-b4b1-4ba9-a028-b1c074e8a25b",
  "type": "positions.updated",
  "timestamp": "2023-11-20T17:37:34.663503168Z",
  "payload": {
    "accountID": "c92f59dc-3780-4be4-bec8-4228b6187502.1691043473709",
    "accountNo": "DPBN000043",
    "userID": "c92f59dc-3780-4be4-bec8-4228b6187502",
    "updateReason": "EXERCISE",
    "current": {
      "costBasis": 0,
      "openQty": 0,
      "symbol": "AAPL231110P00175000"
    },
    "previous": {
      "costBasis": 250,
      "openQty": 50,
      "symbol": "AAPL231110P00175000",
      "avgPrice": 5
    }
  }
}
```
```json Updated [options expiration]
{
  "id": "event_b6635686-b4b1-4ba9-a028-b1c074e8a25b",
  "type": "positions.updated",
  "timestamp": "2023-11-20T17:37:34.663503168Z",
  "payload": {
    "accountID": "c92f59dc-3780-4be4-bec8-4228b6187502.1691043473709",
    "accountNo": "DPBN000043",
    "userID": "c92f59dc-3780-4be4-bec8-4228b6187502",
    "updateReason": "EXPIRED",
    "current": {
      "costBasis": 0,
      "openQty": 0,
      "symbol": "AAPL231110P00175000"
    },
    "previous": {
      "costBasis": 250,
      "openQty": 50,
      "symbol": "AAPL231110P00175000",
      "avgPrice": 5
    }
  }
}
```
```json Updated [options assignment]
{
  "id": "event_b6635686-b4b1-4ba9-a028-b1c074e8a25b",
  "type": "positions.updated",
  "timestamp": "2023-11-20T17:37:34.663503168Z",
  "payload": {
    "accountID": "c92f59dc-3780-4be4-bec8-4228b6187502.1691043473709",
    "accountNo": "DPBN000043",
    "userID": "c92f59dc-3780-4be4-bec8-4228b6187502",
    "updateReason": "ASSIGNMENT",
    "current": {
      "costBasis": 0,
      "openQty": 0,
      "symbol": "AAPL231110P00175000"
    },
    "previous": {
      "costBasis": 250,
      "openQty": 50,
      "symbol": "AAPL231110P00175000",
      "avgPrice": 5
    }
  }
}
```