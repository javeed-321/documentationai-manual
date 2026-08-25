---
updatedAt: 2025-08-20T23:55:44.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Getting balances and positions

Real-time APIs are updated as transactions occur to reflect a comprehensive view of a customer’s investments and the performance of their portfolio.

## Cash balances

Use the [Money Endpoint](https://developer.drivewealth.com/apis/reference/get_accounts-accountid-summary-money) to access realtime snapshots of an account's cash balance.

```javascript
GET /back-office/accounts/{accountID}/summary/money

{
  "accountID": "35fae684-4a96...",
  "accountNo": "ABCD000040",
  "tradingType": "CASH",
  "updated": "2021-04-23T18:41:32.440Z",
  "cash": {
    "cashAvailableForTrade": 400,
    "cashAvailableForWithdrawal": 100,
    "cashBalance": 500,
    "noBuyingPowerReason": null,
    "cashSettlement": [
      {
        "utcTime": "2021-04-27T13:30:00.001Z",
        "cash": 300
      }
    ],
    "pendingPaymentsAmount": 0
  },
  ...
}
```

There are multiple types of cash balances shown above, all of which you’ll want to use differently:

* **Buying Power** (`cashAvailableForTrade`) — This represents the amount of cash a user can use to buy securities. The customer above can place $400 worth of buy trades right now.
* **Available for withdrawal** (`cashAvailableForWithdrawal`) — The amount of money that can be withdrawn from the Account. This customer can only withdraw $100 today. This is due to $300 that is not yet settled (likely from a recent sale), and displayed in the cashSettlement array.
* **Cash Balance** (`cashBalance`) — The amount of cash this customer owns. This customer holds $500, but can only invest $400. This is likely due to an outstanding buy order that has not yet been completed.

## Asset positions

The [Positions Endpoint](https://developer.drivewealth.com/apis/reference/get_accounts-accountid-summary-positions) will return a list of held Positions in an Account.

```javascript
GET /back-office/accounts/{accountID}/summary/positions

Response:
{
	"accountID": "cc07f91b-7ee1-4868-b8fc-823c70a1b932.1407775317759",
	"accountNo": "DWBG000052",
	"tradingType": "CASH",
	"updated": "2017-06-16T15:35:30.617Z",
	"equityValue": 34275565.44,
	"optionsValue": 12345.67,
	"positionsValue": 34287911.11,
	"equityPositions": [
		{
			"symbol": "MS",
			"instrumentID": "3fb1e8a9-f7d5-4d90-95e2-43e7326b5636",
			"openQty": 31.65120151,
			"availableForWithdrawalQty": null,
			"costBasis": 975.98,
			"marketValue": 4540.36,
			"side": "B",
			"priorClose": 144.29,
			"availableForTradingQty": 31.65120151,
			"avgPrice": 30.84,
			"mktPrice": 143.45,
			"unrealizedPL": 3564.38,
			"unrealizedDayPLPercent": -0.58,
			"unrealizedDayPL": -26.59
		}
	],
	"optionPositions": [
		{
			"symbol": "AAPL210331C00300000",
			"instrumentID": "2cbd5648-7afa-4347-8c82-743fd74a123a",
			"openQty": 5,
			"availableForWithdrawalQty": null,
			"costBasis": 4300.12,
			"marketValue": 4400.12,
			"side": "B",
			"priorClose": 400.53,
			"availableForTradingQty": 5,
			"avgPrice": 330.07,
			"mktPrice": 440.75,
			"unrealizedPL": 14.24,
			"unrealizedDayPLPercent": 1.65,
			"unrealizedDayPL": 0.54
		}
	]
}
```

A full description of properties can be found in the API specification. As an example, for this customer:

* $4540.36 worth of Equity MS is owned
  * A total of $975.98 was invested into ABCD, meaning a total profit of $3564.38
  * All 31.65120151 held shares are available to be sold
* $4400.12 worth of Option AAPL210331C00300000 is owned
  * A total of $4300.12 was invested into AAPL210331C00300000, meaning a total profit of $14.24
  * All 5 held contracts are available to be sold

## Account performance

At the end of each trading day, DriveWealth captures several metrics for each Account. These metrics can be used to show a change in value over time, and include the following:

* **Realized P/L** – The actual (realized) profit or loss.
* **Unrealized Day P/L** – The daily, uncaptured, profit or loss on open positions
* **Cumulative Realized P/L** – The aggregate realized P/L from inception of the account (each day adds to previous days)
* **Equity** – The total invested equity (excluding cash)
* **Cash** – The total cash balance (settled and unsettled)
* **Deposits** – The cumulative amount in deposits since inception
* **Withdrawals** – The cumulative amount in withdrawals since inception
* **Fees** – Total dollar amount of fees calculated from 4pm ET of previous day until current time.

Access these metrics via the [Performance Endpoint](https://developer.drivewealth.com/apis/reference/get_accounts-accountid-performance):

```javascript
GET /back-office/accounts/{accountID}/performance

{
  "accountID": "cc07f91b-7ee1...",
  "accountNo": "ABCD000040",
  "startDate": "2018-09-18",
  "endDate": "2018-09-18",
  "lastUpdated": "2018-09-18T17:34:00.370Z",
  "performance": [
    {
      "realizedDayPL": 0,
      "unrealizedDayPL": 13.11,
      "cumRealizedPL": 0,
      "date": "2018-09-18",
      "equity": 9941.59,
      "cash": 2698.49,
      "deposits": 100,
      "withdrawals": 0,
      "fees": 0
    }
  ]
}
```

The “performance” array will hold a performance object based on the date range or period set in the query parameters. For example, if you want to retrieve the performance metrics from January to April:

```javascript
GET /back-office/accounts/{accountID}/performance?from=2023-01-01&to=2023-04-30
```

Likewise, if you want to retrieve the performance for a specific period (e.g 2 weeks, 1 month, 10 days) from the current day then you can make the following type of  request:

```javascript
GET /back-office/accounts/{accountID}/performance?period=2w
```

## Margin details

Customers trading with leverage have additional balances they need to monitor in addition to the other metrics shown above. Read [Enabling leverage](https://developer.drivewealth.com/apis/docs/enabling-leverage) to learn how to create an Account that tracks these values.

```javascript
GET /back-office/accounts/{accountID}/summary/margin
{
  "accountID": "35fae684-4a96-424d-add0-d235d7b1e6d2.1445614025578",
  "accountNo": "DWHM000040",
  "tradingType": "CASH",
  "updated": "2021-04-23T18:41:32.440Z",
  "margin": {
        "marginRequirement": 0.5,
        "longMarketValue": 9000,
        "debitBalance": -1000,
        "equity": 4000,
        "equityFraction": 1,
        "equityRequired": 3500,
        "accruedInterest": 0,
        "patternDayTrader": false,
        "restricted": false,
        "daySMA": 3335.66,
        "rtExcessEquity": 1500,
        "effectiveSMA": 3335.66,
        "noBuyingPowerReason": null,
        "marginCall": null,
        "restingOrders": 0
    }

}
```

For this Account, there are some prudent details important to show to a customer:

* **longMarketValue** –  The real time dollar value of the current holdings in the margin account.
* **debitBalance** – This represents the real time value of debt in the margin account. A positive number is a debit balance while a negative amount is a credit balance. A customer will pay interest on any debit balance amount.
* **equity** – The amount of equity the user holds based on their contributions to the account.
* **equityRequired** – Minimum equity required to stay above a DriveWealth house margin call. If the account is in a margin call (house or exchange) this field will also appear in the `marginCall` object.
* **rtExcessEquity** – Equity in excess of equityRequired calculated in real time (more is good).

Trading on margin refers to the practice of borrowing money from a broker (DriveWealth) to trade securities. This allows traders to potentially increase their returns by leveraging their capital, but it also increases the risk of losses. The borrowed money is known as a margin loan, and the trader is required to maintain a minimum level of equity in their account, known as the minimum margin (`equityRequired`), to cover potential losses. A margin call occurs when the value of a trader's securities in a margin account drops to a level where the equity falls below the minimum margin requirement set by the broker.

> John purchases $10,000 worth of stock using a 2:1 margin loan. This means John contributed $5,000 of his own money and borrowed an additional $5,000 on margin. DriveWealth requires a minimum margin of 30-35%, so John must maintain at least $3,500 in equity in the account. If the value of the stock (`longMarketValue`) drops to $8,000, John's equity would fall to $3,000 ($8,000 value of stock - $5,000 margin loan), which is below the minimum margin requirement (`equityRequired`). This would trigger a margin call, and John would be required to deposit additional funds or securities into the account to bring the equity back up to the minimum level.

It's important to note that if a customer is unable to meet a margin call, DriveWealth can sell securities in the account to bring the equity back up to the minimum level, which could result in significant realized losses for the customer.

If a customer is issued a margin call because they haven’t contributed enough equity to the Account, you’ll see additional data in that same API:

```javascript
GET /back-office/accounts/{accountID}/summary/margin
{
  "accountID": "35fae684-4a96-424d-add0-d235d7b1e6d2.1445614025578",
  "accountNo": "DWHM000040",
  "tradingType": "CASH",
  "updated": "2021-04-23T18:41:32.440Z",
  "margin": {
    "marginRequirement": .5,
    "longMarketValue": 8000,
    "debitBalance": -2000,
    "equity": 3000,
    "equityFraction": 1,
    "equityRequired": 3500,
    "accruedInterest": 0,
    "patternDayTrader": false,
    "restricted": false,
    "daySMA": 0,
    "rtExcessEquity": 0,
    "effectiveSMA": 0,
    "noBuyingPowerReason": null,
    "marginCall":{
      "marginCallType": "HOUSE",
      "equityRequired": 500,
      "callAmount": 500
    }
    "restingOrders": 0
  }
}
```

This customer must deposit $500 to clear the margin call.