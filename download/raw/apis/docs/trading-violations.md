---
updatedAt: 2026-06-03T22:53:16.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Trading violations

> ## 📋 Regulatory update: Pattern day trading rule changes
>
> **Effective June 4, 2026** — [FINRA Regulatory Notice 26-10](https://us.list-manage.com/S4IFLOPKsEJ?e=7f7ca5a638\&c2id=b54217449f03970bad1aa4800cfacc5f)

As a result of FINRA Regulatory Notice 26-10, the monitoring and restricting of pattern day trading will be retired. These changes are effective **June 4, 2026** and include the following:

| What's Changing       | Details                                                                                      |
| --------------------- | -------------------------------------------------------------------------------------------- |
| **$25,000 Minimum**   | The hard equity gate required to day trade is being removed                                  |
| **Trade Counters**    | The "4 trades in 5 days" logic is now obsolete                                               |
| **Account Flagging**  | Accounts will no longer be labeled "Pattern Day Trader" or restricted from day trading       |
| **Day Trading Calls** | The day trading leverage calculation is replaced by standard maintenance margin requirements |

***

## What's new: Intraday margin

While the old "day trade count" is gone, the focus shifts to a more dynamic metric called the **Intraday Margin Level (IML)**. Instead of checking account balances solely at end of day, the new rule requires monitoring of a customer account's highest margin deficiency reached **during** the trading day.

| Concept                         | Definition                                                                                                                    |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **Standardized Minimum Equity** | All margin accounts are subject to a **$2,000 minimum equity requirement** (or 100% of the purchase price, whichever is less) |
| **Intraday Margin Level (IML)** | The amount of cash a customer could withdraw while still maintaining required maintenance margin                              |
| **Intraday Margin Deficit**     | Occurs when the IML becomes a **negative number** due to IML-reducing transactions                                            |

***

## Trade violation types

When placing trades, customers may incur violations depending on account type:

| Violation                      | Account Type    | Description                                                          |
| ------------------------------ | --------------- | -------------------------------------------------------------------- |
| **Good Faith Violation (GFV)** | Cash accounts   | Occurs when unsettled funds are used to purchase and sell securities |
| **Pattern Day Trader (PDT)**   | Margin accounts | Triggered by intraday margin deficit conditions                      |

> 📘 **Note:** PDT account flagging and restrictions are being retired as part of this regulatory change. The PDT violation type above refers to **intraday margin violations** under the new framework, not the legacy day trade counting logic.

When placing trades in a brokerage account, customers may incur two types of violations depending on the account type:

* Good Faith Violation (GFV): Applicable to **Cash** accounts
* Pattern Day Trader (PDT): Applicable to **Margin** accounts

## Pattern day trader

A user is marked as a Pattern Day Trader when they execute four or more day trades within a **rolling** five business day period in a margin account. Once marked as a PDT, the account must maintain a minimum equity balance of $25,000. If the equity falls below this threshold, any further attempts to day trade will be blocked until the required balance is restored.

An account that has been marked as a pattern day trader, will be restricted from day trading in the following scenarios:

1. If the account equity balance falls below $25K the account will be restricted at the end of the trading day
2. If a day trade is attempted and the equity balance is below $25K the account will be restricted immediately

An account that has been marked as a pattern day trader, will be allowed to continue or resume day trading in the following scenarios:

1. If the account equity balance exceeds $25K, the account will be unrestricted after market close and able to day trade the next trading day

A day trade is defined as buying, then selling the same security within the same trading day. When an account's day trade counter changes, a violations event is triggered:

```json Increment
{
  "id": "event_51486507-b649-4112-8dc1-13ba94dad33f",
  "type": "violations.created",
  "timestamp": "2025-05-08T13:39:56.173620357Z",
  "payload": {
    "accountID": "4fc53560-15a5-4597-9574-395978e4c813.1704939817537",
    "accountNo": "DJEF034684",
    "currentViolations": {
      "patternDayTrades": {
        "count": 3
      }
    }
  }
}
```
```json Decrement
{
  "id": "event_10486507-b649-4112-8dc1-13ba94dad33f",
  "type": "violations.removed",
  "timestamp": "2025-05-08T13:39:56.173620357Z",
  "payload": {
    "accountID": "4fc53560-15a5-4597-9574-395978e4c813.1704939817537",
    "accountNo": "DJEF034684",
    "currentViolations": {
      "patternDayTrades": {
        "count": 1
      }
    }
  }
}
```

To retrieve details about the underlying trades contributing to the current day trade count, use the []()[Violations](https://developer.drivewealth.com/apis/reference/get_accounts-accountid-violations) endpoint.

When an account is marked as a PDT or is restricted from day trading due to insufficient equity, an accounts event is triggered. A PDT-restricted account remains **open** and can still engage in non-day trading activities.

```json
{
  "id": "event_fa1a7849-aad1-4128-bedc-08012396ff5b",
  "type": "accounts.updated",
  "timestamp": "2025-05-07T14:12:05.538Z",
  "payload": {
    "previous": {
      "pdt": {
        "patternDayTrader": false,
        "pdtRestricted": false,
        "pdtRestrictedWhen": "NO-RESTRICTION"
      }
    },
    "current": {
      "pdt": {
        "patternDayTrader": true,
        "pdtRestricted": true,
        "pdtRestrictedWhen": "2025-05-07T14:07:05.506Z"
      }
    },
    "accountEquityBreakdown": {
      "longMarketValue": 0,
      "debitBalance": 0,
      "accountEquity": 12.32
    },
    "accountID": "89ba405d-3faf-41e5-a103-df73a48df144.1745332377758",
    "accountNo": "JIWE000108",
    "userID": "89ba405d-3faf-41e5-a103-df73a48df144"
  }
}

```

### Day trade examples

Example A: 09:30 Buy 250 ABC 09:31 Buy 250 ABC 13:00 Sell 500 ABC The customer has executed one day trade.

Example B: 09:30 Buy 100 ABC 09:31 Sell 100 ABC 09:32 Buy 100 ABC 13:00 Sell 100 ABC The customer has executed two day trades.

Example C: 09:30 Buy 500 ABC 13:00 Sell 100 ABC 13:01 Sell 100 ABC 13:03 Sell 300 ABC The customer has executed one day trade.

Example D: 09:30 Buy 250 ABC 09:31 Buy 300 ABC 13:01 Buy 100 ABC 13:02 Sell 150 ABC 13:03 Sell 175 ABC The customer has executed one day trade.

Example E: 09:30 Buy 199 ABC 09:31 Buy 142 ABC 13:00 Sell 1 ABC 13:01 Buy 45 ABC 13:02 Sell 100 ABC 13:03 Sell 200 ABC The customer has executed two day trades.

Example F: 09:30 Buy 200 ABC 09:30 Buy 100 XYZ 13:00 Sell 100 ABC 13:00 Sell 100 XYZ The customer has executed two day trades

A sale of a security followed by a buy of that security is not considered a day trade.

### Impact of day trading restriction

If an account is restricted from day trading, orders will be rejected to prevent additional day trades from occurring.

For example, if the account already purchased TSLA today, any new sell order of TSLA (market, limit, stop, etc.) will be rejected.

```json
GET /back-office/orders/{{orderID}} 
{
    "id": "ME.677d34fd-fc32-4b75-83c9-c7760fbee05c",
    "orderNo": "MEMN000012",
    "type": "MARKET",
    "side": "SELL",
    "status": "REJECTED",
    "statusMessage": {
        "errorCode": "O624",
        "message": "Day Trade Rejection"
    },
    "symbol": "TSLA",
    "averagePrice": 0,
    "averagePriceRaw": 0,
    "totalOrderAmount": 0,
    "cumulativeQuantity": 0,
    "quantity": 1,
    "fees": 0,
    "orderExpires": "2025-05-06T20:00:00.000Z",
    "createdBy": "6dfb1271-917b-4e25-bc6e-89e5dc8e7f09",
    "userID": "6dfb1271-917b-4e25-bc6e-89e5dc8e7f09",
    "accountID": "6dfb1271-917b-4e25-bc6e-89e5dc8e7f09.1746557469043",
    "accountNo": "FHMF000013",
    "created": "2025-05-06T18:52:08.539Z",
    "extendedHours": false,
    "preventQueuing": false
}
```

Here's how the `orders.completed` event would look like:

```json orders.completed
{
    "id": "event_a5859ce6-7c4d-4514-af40-23a1473ceb60",
    "type": "orders.completed",
    "timestamp": "2025-05-06T18:52:11.841989687Z",
    "payload": {
        "id": "ME.677d34fd-fc32-4b75-83c9-c7760fbee05c",
        "orderNo": "MEMN000012",
        "type": "MARKET",
        "side": "SELL",
        "status": "REJECTED",
        "statusMessage": {
            "errorCode": "O624",
            "message": "Day Trade Rejection"
        },
        "symbol": "TSLA",
        "averagePrice": 0,
        "cumulativeQuantity": 0,
        "openQuantity": 0,
        "availableForTradingQuantity": 1,
        "quantity": 1,
        "fees": 0,
        "orderExpires": "2025-05-06T20:00:00.000Z",
        "createdBy": "6dfb1271-917b-4e25-bc6e-89e5dc8e7f09",
        "userID": "6dfb1271-917b-4e25-bc6e-89e5dc8e7f09",
        "accountID": "6dfb1271-917b-4e25-bc6e-89e5dc8e7f09.1746557469043",
        "accountNo": "FHMF000013",
        "created": "2025-05-06T18:52:08.539Z"
    }
}
```

Additionally, restricted accounts cannot have pending orders for the same symbol on opposite sides. For example, if an account has a pending sell limit order of ABC, any new buy order of ABC will be rejected, until the pending sell order has either been canceled or filled.

> ❗️ Market risk in restricted accounts
>
> For accounts flagged as PDT with an equity balance below $25,000, same-day exits of newly established long positions are not permitted. To help customers avoid unintended market exposure and potential losses, it is recommended to issue a prompt or warning before a new purchase, since that instrument will be prohibited from sales for the remainder of the day.

## Good faith violations

In a cash Account, a customer can reinvest funds immediately after a sale. For example, imagine a customer has no cash in their Account, and then sells their stock:

```json
POST /back-office/orders 
{
  "accountNo": "DWPH000003",
  "orderType": "MARKET",
  "symbol": "AAPL",
  "side": "SELL",
  "clientNotes": "Manual limit order",
  "amountCash": 400,
}
```

This Account now has cash available to trade, but not to withdraw, and cash is pending settlement from this stock sale:

```json
GET /back-office/accounts/{accountID}/summary/money
{
  "accountID": "35fae684-4a96...",
  "accountNo": "ABCD000040",
  "tradingType": "CASH",
  "updated": "2021-04-23T18:41:32.440Z",
  "cash": {
    "cashAvailableForTrade": 400,
    "cashAvailableForWithdrawal": 0,
    "cashBalance": 400,
    "noBuyingPowerReason": null,
    "cashSettlement": [
      {
        "utcTime": "2021-04-27T13:30:00.001Z",
        "cash": 400
      }
    ],
    "pendingPaymentsAmount": 0
  },
  ...
}
```

Every asset settles with a different time period. Equity sales, for example, settle 1 business day after the trade is executed.

By default, this customer is allowed to purchase more stock with this cash, even though it is pending settlement. However, if they do so, they may not sell the new Position before this cash settles. Doing so would be a Good Faith Violation and would be listed in the Violations endpoint:

```json
{
    "goodFaithViolations": [
        {
            "id": "KA.6ce5e920-b1cc-4c82-bc45-1a6b1d5b8301",
            "symbol": "AAPL",
            "qty": 0.70802817,
            "amount": 100.54,
            "side": "BUY",
            "createdWhen": "2023-01-23T23:26:52.049Z",
            "orderID": "KA.6ce5e920-b1cc-4c82-bc45-1a6b1d5b8301",
            "orderNo": "KAXA004278",
            "violatingSells": [
                {
                    "side": "SELL",
                    "qty": 0.70802817,
                    "amount": 100.54,
                    "createdWhen": "2023-01-23T23:27:26.050Z",
                    "orderID": "KA.b64a40d6-c7fe-46e5-9996-7a2b5b378035",
                    "orderNo": "KAGE004920"
                }
            ]
        }
    ],
    "patternDayTrades": null,
    ...
}
```

An Account that commits Good Faith Violations will no longer be able to reinvest funds from sales until the sale settles. A special restricted flag will be set to true on the Account indicating this behavior.