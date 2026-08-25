---
updatedAt: 2025-09-22T15:01:34.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Stock Split Events

A stock split is a decision made by a company's board of directors to increase or decrease the number of shares that are outstanding. When a stock split happens, we will provide an updated `openQty` and `avgPrice`.

```json Updated
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
            "openQty": 2,
            "symbol": "CPLP",
            "avgPrice": 1.4
        }
    }
}
```

In this example there was a 2:1 stock split where the customers `openQty` and `avgPrice` was adjusted to match this split.