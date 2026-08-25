---
updatedAt: 2025-09-22T15:01:33.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Spinoff Events

A Spinoff relates to when a single company is split into a new company, creating a new CUSIP and symbol traded entity. It is typical that the spinoffs also contain a share conversion.

```json Updated
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