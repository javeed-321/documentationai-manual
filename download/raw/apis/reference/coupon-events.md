---
updatedAt: 2025-09-22T15:01:27.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Coupon Events

When a customer owns a security that pays a coupon, DriveWealth will create a new transaction in the customers account for the amount owed. For each coupon, DriveWealth provides information in regards to the type of coupon, the amount, and tax status of that coupon.

```json Created
{
    "id": "event_a1acdf71-17d2-4e38-81ce-871a86374b40",
    "type": "transactions.created",
    "timestamp": "2024-04-05T19:25:14.711707573Z",
    "payload": {
        "accountID": "b25f0d36-b4e4-41f8-b3d9-9249e46402cd.1491330741850",
        "accountNo": "DWEF000010",
        "userID": "b25f0d36-b4e4-41f8-b3d9-9249e46402cd",
        "transaction": {
            "accountAmount": 76.000,
            "accountBalance": 128195.27,
            "comment": "BPY coupon, $38.00/bond",
            "finTranID": "GF.861e931d-e7aa-47c8-b87a-b1e55acf3862",
            "wlpFinTranTypeID": "e8ff5103-ad40-4ed9-b2ee-fd96826bf935",
            "finTranTypeID": "FI_COUP",
            "feeSec": 0,
            "feeTaf": 0,
            "feeBase": 0,
            "feeXtraShares": 0,
            "feeExchange": 0,
            "instrument": {
                "id": "476b40ee-3ff9-46af-85af-fec572d13d23",
                "symbol": "US3456U123P0",
                "name": "Brookfield Property Partners L.P. 3.8% 2030/06/30"
            },
            "coupon": {
                "type": "CASH",
                "amountPerBond": 38.00,
                "taxCode": "NON_TAXABLE"
            }
        }
    }
}
```