---
updatedAt: 2025-08-20T23:41:37.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Bond Maturity Events

When a customer holds a bond that reaches its maturity date, DriveWealth automatically processes the return of the bond's principal amount. This event is recorded as a transaction in the customer's account, reflecting the repayment of the bond's face value.

## Maturity Event Details

Upon maturity of a bond, DriveWealth executes the following actions:

* Generates a transaction in the customer's account for the principal amount of the matured bond.
* Updates the account balance to reflect the returned principal.
* Closes out the bond position, reducing the holding quantity to zero.

```json Created
{
    "id": "event_a1acdf71-17d2-4e38-81ce-871a86374b40",
    "type": "transactions.created",
    "timestamp": "2024-04-05T19:25:14.711707573Z",
    "payload": {
       "accountID": "73b54qwe-55a1-43cb-9bb5-8ccc571e8ff1.1733350177233",
       "accountNo": "JKLM000007",
       "userID": "73qwerty-55a1-43cb-9bb5-8ccc571e8ff1",
       "transaction": {
           "accountAmount": 4000,
           "accountBalance": 17046576.51,
           "comment": "US912797NC79 - Maturity @ 100.00",
           "finTranID": "MD.159d8a41-9bd1-461f-8068-1cb33cefc71f",
           "wlpFinTranTypeID": "b293d057-d1c7-4a8f-a090-9cf5d5225a8d",
           "finTranTypeID": "FIMAT",
           "feeSec": 0,
           "feeTaf": 0,
           "feeBase": 0,
           "feeXtraShares": 0,
           "feeExchange": 0,
           "instrument": {
               "id": "12345568-98d5-4b57-83f3-50c014078a86",
               "symbol": "US912797NC79",
               "name": "United States Treasury Bills"
           },
      "fiMaturity": {
           "accruedInterest": "0",
           "tag": "fiMaturity",
           "type": "FI_MATURITY"
       }
     }
  }
}
```

The `positions.updated` event will be made for the removal of instrument that were previously held.

```json Updated
{
    "id": "event_5d5a4a88-fc05-4d53-b0bf-27801ef028c9",
    "type": "positions.updated",
    "timestamp": "2023-08-02T07:02:31.949597191Z",
    "payload": {
        "accountID": "0dd1b08f-3668-440a-be18-131443d85a47.1551208006668",
        "accountNo": "DWUV000073",
        "userID": "0dd1b08f-3668-440a-be18-131443d85a47",
        "updateReason": "FI_MATURITY",
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