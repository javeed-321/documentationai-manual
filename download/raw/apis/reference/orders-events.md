---
updatedAt: 2025-09-22T15:02:00.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Order Events

## Order Created

A new order has been created, and provides the full details of the order.

```json Created
{
    "id": "event_dcadb7df-a677-4ba6-8a06-15005d4a491d",
    "type": "orders.created",
    "timestamp": "2019-03-28T22:40:03.260922189Z",
    "extendedHours": false,
    "timeInForce": "",
    "payload": {
        "id": "GC.f7590a52-75c7-4f3a-92c7-6b03e02dc44f",
        "orderNo": "GCWS000039",
        "type": "MARKET",
        "side": "BUY",
        "status": "NEW",
        "symbol": "AAPL",
        "averagePrice": 0,
        "cumulativeQuantity": 0,
        "openQuantity": 1,
        "availableForTradingQuantity": 7,
        "quantity": 1,
        "fees": 0,
        "orderExpires": "2019-03-29T20:00:00.000Z",
        "createdBy": "b25f0d36-b4e4-41f8-b3d9-9249e46402cd",
        "userID": "b25f0d36-b4e4-41f8-b3d9-9249e46402cd",
        "accountID": "b25f0d36-b4e4-41f8-b3d9-9249e46402cd.1403540676095",
        "accountNo": "DWZR000001",
        "created": "2019-03-28T22:40:03.240Z"
    }
}
```
```json Created [options]
{
  "id": "event_f61ee39e-7a34-4cd8-86cc-9c9744f3fbeb",
  "type": "orders.created",
  "timestamp": "2023-12-15T14:09:38.158174290Z",
  "payload": {
    "id": "KL.5820763e-5647-4d77-b1b6-409d14d0839b",
    "orderNo": "KLRM000636",
    "type": "LIMIT",
    "side": "BUY_OPEN",
    "status": "NEW",
    "symbol": "AMZN240119C00265000",
    "averagePrice": 0,
    "averagePriceRaw": 0,
    "totalOrderAmount": 0,
    "price": 2,
    "cumulativeQuantity": 0,
    "quantity": 1,
    "fees": 0,
    "orderExpires": "2023-12-15T21:00:00.000Z",
    "createdBy": "9abd520e-550b-4278-b09a-3dd1aa483265",
    "userID": "9abd520e-550b-4278-b09a-3dd1aa483265",
    "accountID": "9abd520e-550b-4278-b09a-3dd1aa483265.1594660375409",
    "accountNo": "KRFZ000001",
    "created": "2023-12-15T14:09:38.069Z",
    "timeInForce": "DAY",
    "specialHandlingInstructions": {
      "tradeInstruction": "UNSOLICITED"
    }
  }
}
```

## Order Updated

The status of the order has been updated, contains details of the order in its current state.

```json Updated
{
    "id": "event_4da42927-77f5-4308-a6bf-60c1ed0a4b24",
    "type": "orders.updated",
    "timestamp": "2019-01-09T12:14:44.155187291Z",
    "payload": {
        "id": "GA.021be353-1f63-4540-aeeb-8a11b1f5a189",
        "orderNo": "GAFZ000003",
        "type": "MARKET",
        "side": "BUY",
        "status": "PARTIAL_FILL",
        "symbol": "BABA",
        "averagePrice": 134.42,
        "cumulativeQuantity": 12,
        "quantity": 1000,
        "lastShares": 6,
        "lastPrice": 134.11,
        "createdBy": "cc07f91b-7ee1-4868-b8fc-823c70a1b932",
        "lastExecuted": "2019-01-04T14:36:17.378Z",
        "userID": "cc07f91b-7ee1-4868-b8fc-823c70a1b932",
        "accountID": "cc07f91b-7ee1-4868-b8fc-823c70a1b932.1407775317759",
        "accountNo": "DPKU000001",
        "created": "2019-01-04T14:36:17.378Z"
    }
}
```

## Order Completed

The order has been completed, contains details of the full order that was executed or rejected.

```json Completed
{
    "id": "event_ddb09679-2f16-4440-9ef1-4bd209dfba26",
    "type": "orders.completed",
    "timestamp": "2019-03-28T22:40:03.267813768Z",
    "payload": {
        "id": "GC.f7590a52-75c7-4f3a-92c7-6b03e02dc44f",
        "orderNo": "GCWS000039",
        "type": "MARKET",
        "side": "BUY",
        "status": "FILLED",
        "symbol": "AAPL",
        "averagePrice": 188.72,
        "totalOrderAmount": 188.72,
        "cumulativeQuantity": 1,
        "openQuantity": 0,
        "availableForTradingQuantity": 7,
        "quantity": 1,
        "fees": 0,
        "orderExpires": "2019-03-29T20:00:00.000Z",
        "lastExecuted": "2019-01-04T14:36:17.378Z",
        "createdBy": "b25f0d36-b4e4-41f8-b3d9-9249e46402cd",
        "userID": "b25f0d36-b4e4-41f8-b3d9-9249e46402cd",
        "accountID": "b25f0d36-b4e4-41f8-b3d9-9249e46402cd.1403540676095",
        "accountNo": "DWZR000001",
        "created": "2019-03-28T22:40:03.240Z",
        "lastPrice": 60.34,
        "lastShares": 0.31908104,
        "lastMarket": "DRVW"
    }
}
```
```json Completed [rejected]
{
    "id": "event_a5859ce6-7c4d-4514-af40-23a1473ceb60",
    "type": "orders.completed",
    "timestamp": "2019-03-29T22:11:37.841989687Z",
    "payload": {
        "id": "GC.f39b4618-a2fb-4fa2-808e-b956059a79c8",
        "orderNo": "GCWS000054",
        "type": "MARKET",
        "side": "SELL",
        "status": "REJECTED",
        "statusMessage": {
            "errorCode": "O105",
            "message": "Order quantity exceeds quantity available for sale.  Cannot SELL SHORT.  [orderNo=GCWS000054] [orderqty=10000.0] [openQty=20.9873] [sellingInMarket=0] [restingOrderSummary=]"
        },
        "symbol": "AMZN",
        "averagePrice": 0,
        "cumulativeQuantity": 0,
        "openQuantity": 0,
        "availableForTradingQuantity": 7,
        "quantity": 10000,
        "fees": 0,
        "orderExpires": "2019-04-01T20:00:00.000Z",
        "createdBy": "b25f0d36-b4e4-41f8-b3d9-9249e46402cd",
        "userID": "b25f0d36-b4e4-41f8-b3d9-9249e46402cd",
        "accountID": "b25f0d36-b4e4-41f8-b3d9-9249e46402cd.1403540676095",
        "accountNo": "DWZR000001",
        "created": "2019-03-29T22:02:12.818Z"
    }
}
```
```json Completed [options]
{
  "id": "event_a5859ce6-7c4d-4514-af40-23a1473ceb60",
  "type": "orders.completed",
  "timestamp": "2019-03-29T22:11:37.841989687Z",
  "payload": {
    "id": "KL.5820763e-5647-4d77-b1b6-409d14d0839b",
    "orderNo": "KLRM000636",
    "type": "LIMIT",
    "side": "BUY_OPEN",
    "status": "FILLED",
    "symbol": "TSLA240315P00158330",
    "averagePrice": 2.00,
    "averagePriceRaw": 2,
    "totalOrderAmount": 200,
    "price": 2,
    "cumulativeQuantity": 1,
    "quantity": 1,
    "fees": 0.04,
    "orderExpires": "2023-12-15T21:00:00.000Z",
    "createdBy": "9abd520e-550b-4278-b09a-3dd1aa483265",
    "userID": "9abd520e-550b-4278-b09a-3dd1aa483265",
    "accountID": "9abd520e-550b-4278-b09a-3dd1aa483265.1594660375409",
    "accountNo": "KRFZ000001",
    "created": "2023-12-15T14:09:38.069Z",
    "lastExecuted": "2023-12-15T14:09:38.396Z",
    "timeInForce": "DAY",
    "specialHandlingInstructions": {
      "tradeInstruction": "UNSOLICITED"
    },
    "lastPrice": 2,
    "lastShares": 0
  }
}
```
```json Completed [options rejected]
{
  "id": "event_a5859ce6-7c4d-4514-af40-23a1473ceb60",
  "type": "orders.completed",
  "timestamp": "2019-03-29T22:11:37.841989687Z",
  "payload": {
    "id": "KL.a1ce2ef9-655e-488c-ba57-ad581d999cf4",
    "orderNo": "KLRM000637",
    "type": "LIMIT",
    "side": "BUY_OPEN",
    "status": "REJECTED",
    "statusMessage": {
      "errorCode": "O125",
      "message": "Order quantity or notional higher than allowed max. orderQty=10000000000000000000, maxmaxAllowedOrderQty=50000"
    },
    "symbol": "TSLA240315P00158330",
    "averagePrice": 0,
    "averagePriceRaw": 0,
    "totalOrderAmount": 0,
    "price": 2,
    "cumulativeQuantity": 0,
    "quantity": 0,
    "fees": 0,
    "orderExpires": "2023-12-15T21:00:00.000Z",
    "createdBy": "9abd520e-550b-4278-b09a-3dd1aa483265",
    "userID": "9abd520e-550b-4278-b09a-3dd1aa483265",
    "accountID": "9abd520e-550b-4278-b09a-3dd1aa483265.1594660375409",
    "accountNo": "KRFZ000001",
    "created": "2023-12-15T14:10:34.250Z",
    "timeInForce": "DAY",
    "specialHandlingInstructions": {
      "tradeInstruction": "UNSOLICITED"
    }
  }
}
```
```json Completed [options canceled]
{
  "id": "event_a5859ce6-7c4d-4514-af40-23a1473ceb60",
  "type": "orders.completed",
  "timestamp": "2019-03-29T22:11:37.841989687Z",
  "payload": {
    "id": "KL.3d7fae88-2ee4-4ac4-988f-87560f43f0bb",
    "orderNo": "KLRM000639",
    "type": "LIMIT",
    "side": "BUY_OPEN",
    "status": "CANCELED",
    "symbol": "AMZN240119C00265000",
    "averagePrice": 0,
    "averagePriceRaw": 0,
    "totalOrderAmount": 0,
    "price": 2,
    "cumulativeQuantity": 0,
    "quantity": 1,
    "fees": 0,
    "orderExpires": "2023-12-15T21:00:00.000Z",
    "createdBy": "9abd520e-550b-4278-b09a-3dd1aa483265",
    "userID": "9abd520e-550b-4278-b09a-3dd1aa483265",
    "accountID": "9abd520e-550b-4278-b09a-3dd1aa483265.1594660375409",
    "accountNo": "KRFZ000001",
    "created": "2023-12-15T14:17:45.442Z",
    "timeInForce": "DAY",
    "specialHandlingInstructions": {
      "tradeInstruction": "UNSOLICITED"
    },
    "lastPrice": 2,
    "lastShares": 0
  }
}
```