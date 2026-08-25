---
updatedAt: 2026-07-13T23:01:17.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Fees, commissions, and markups

Various types of fees can be charged to customers for their trading activity.

## Commissions

The simplest way to charge a commission is by specifying an amount to charge on the Order object:

```javascript
POST /back-office/orders

{
  "accountNo": "DWPH000003",
  "orderType": "MARKET",
  "symbol": "ABCD",
  "side": "BUY",
  "quantity": 30.42,
  "commission": 4.99
}
```

This amount will be deducted from the Account once the Order is completed.

Rather than supplying this field with every Order, a Commission Schedule can be created instead. These schedules are defined by DriveWealth based on a few properties you dictate:

* A minimum amount to charge
* An amount per share executed
* An optional flat amount to charge instead for purchases of less than 1 share

<Callout icon="🚧" theme="warn">
  ###

  Commission Schedules are only supported for Equities orders. For all other asset classes, please refer to the above example of how to specify an amount on the Order object.
</Callout>

The Commission Schedules have a defined structure, and multiple can be configured for each client:

```javascript
{
        "active": true,
        "commissionID": "21c1bf22-9a36...",
        "description": "99 cents + Overages",
        "assignmentCriteria": {
            "wlpID": "ABCD",
            "country": null,
            "defaultStatus": true,
            "accountMgmtType": null
        },
        "rates": {
            "fractional": {
                "rate": 0.49,
                "passThroughFees": true,
                "shareAmountRounding": "CEIL",
                "minimumRate": 0.49
            },
            "default": {
                "rate": 0.0125,
                "passThroughFees": true,
                "shareAmountRounding": "NEAREST",
                "minimumRate": 0.99
            }
        }
}
```

The ID of each Commission Schedule can be assigned to an Account, either at its creation or later:

```javascript
PATCH /back-office/accounts/{accountID}

{
  "commissionID": "21c1bf22-9a36...",
}
```

Even while a Commission Schedule is assigned to an Account, the commission field on each Order creation can still be used to override that schedule for that specific trade. DriveWealth can also configure a Commission Schedule to be default for all Accounts created. Each country of residence can be assigned its own default.

## Regulatory fees

Some transaction incur government-mandated regulatory fees when they are traded. These fees can be invoiced to and paid for by the client, or they can be paid for by each customer at time of trade.

To charge these fees to a customer, the `passThroughFees` value in an assigned Commission Schedule must be true.

<Callout icon="🚧" theme="warn">
  ###

  If you override a Commission Schedule by passing a specific commission on an Order creation, DriveWealth will not pass through any additional regulatory fees to the customer. These will then be billed to you.
</Callout>

### SEC fee

The SEC fee, sometimes referred to as the “Section 31” fee is applicable of the following products:

* Sell-side executions of exchange-listed equities on national securities exchanges;
* Sell-side listed options trades; and
* Sales of security futures, where applicable.

Not subject to the SEC fee:

* Buys (purchases), mutual fund trades (unless sold via an exchange), bonds (corporate, muni, treasury), private placements, and internal firm transfers or proprietary trades not cleared through an exchange.
* The fee calculated as a percentage of the sale value.  The SEC fee is adjusted periodically. The amount of the current SEC fee can be found [here](https://legal.drivewealth.com/regulatory-fees).

### TAF fee

The Trading Activity Fee (TAF), lodged by FINRA, is applicable to all sale of the following products:

* All exchange registered securities wherever executed (except debt securities that are not TRACE-Eligible Securities);
* All other equity securities traded otherwise than on an exchange;
* All security futures wherever executed;
* All "TRACE-Eligible Securities" wherever executed, provided that the transaction also is a "Reportable TRACE Transaction," as these terms are defined in FINRA Rule 6710; and
* All municipal securities subject to MSRB reporting requirements.<br />According to FINRA Rule 0150(b) and FINRA Regulatory Notice 22-14, the following transactions are not subject to the Trading Activity Fee:
* IPOs as they are not considered secondary market transactions
* Proprietary Transactions by a Firm for its Own Account
* Transactions in Securities Issued by Open-End Mutual Funds or UITs
* Transactions by a Registered Options Market MakerTransactions Executed on a Foreign Exchange
* Transactions in Municipal Securities
* Private Placements
* Transactions in Government Securities
* Redemptions and Exercises
* Certain Transfers and Reorganizations

The TAF is calculated as a per-share fee on covered securities, with a maximum charge per trade. The TAF is adjusted periodically. The amount of the current TAF can be found [here](https://legal.drivewealth.com/regulatory-fees).

## Full Transaction example

A single Order can result in multiple fees being charged, as shown above. The following shows the resultant Transactions from a typical equity sale:

```javascript
{
    "accountAmount": 143,
    "accountBalance": 16951.58,
    "accountType": "LIVE",
    "comment": "ADJ  Sell 1 shares of AAPL at 143 FULL fill",
    "dnb": false,
    "finTranID": "KA.ac697309-e5ca-4c65-a9c7-26d30a9ca090",
    "finTranTypeID": "SSAL",
    "feeSec": 0,
    "feeTaf": 0,
    "feeBase": 0,
    "feeXtraShares": 0,
    "feeExchange": 0,
    "fillQty": 1,
    "fillPx": 143,
    "instrument": {
        "id": "a67422af-8504-43df-9e63-7361eb0bd99e",
        "symbol": "AAPL",
        "name": "Apple"
    },
    "orderID": "KA.b64a40d6-c7fe...",
    "orderNo": "KAGE004920",
    "tranAmount": 143,
    "tranSource": "EMS",
    "tranWhen": "2023-01-23T23:27:26.034Z",
}, {
    "accountAmount": -4.01,
    "accountBalance": 16947.57,
    "accountType": "LIVE",
    "comment": "COMM Sell AAPL base=3.99 secFee=0.01 tafFee=0.01",
    "dnb": false,
    "finTranID": "KA.6e2300f3-651c-4012-8b23-59b2a976ef41",
    "finTranTypeID": "COMM",
    "feeSec": 0.01,
    "feeTaf": 0.01,
    "feeBase": 3.99,
    "feeXtraShares": 0,
    "feeExchange": 0,
    "fillQty": 0,
    "fillPx": 0,
    "instrument": {
        "id": "a67422af-8504-43df-9e63-7361eb0bd99e",
        "symbol": "AAPL",
        "name": "Apple"
    },
    "orderID": "KA.b64a40d6-c7fe-46e5-9996-7a2b5b378035",
    "orderNo": "KAGE004920",
    "tranAmount": -4.01,
    "tranSource": "EMS",
    "tranWhen": "2023-01-23T23:27:26.104Z",
}
```

<br />