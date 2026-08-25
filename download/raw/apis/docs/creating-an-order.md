---
updatedAt: 2026-07-13T23:01:00.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Creating an order

To place an order, an Account must first be set up and approved to trade. If you are using the [Account Management](https://developer.drivewealth.com/apis/docs/choosing-your-integration-model) product, the Account can be owned by any customer. Otherwise, the Account should be your firm’s trading Account set up by DriveWealth.

Generally, Accounts need funds to buy assets. Refer to [Getting balances and positions](https://developer.drivewealth.com/apis/docs/getting-balances-and-positions) to verify how much cash can be spent in an Order, or refer to [Depositing](https://developer.drivewealth.com/apis/docs/depositing)  to learn how to get funds into an account.

Immediately before placing an Order, you probably want to show a customer information about the asset and its current price. Refer to [Displaying prices and information](https://developer.drivewealth.com/apis/docs/displaying-prices-and-information)  if that’s the case.

When you’re ready to create an Order, provide the instructions specified by the customer:

```javascript
POST /back-office/orders
{
  "accountNo": "DWPH000003",
  "orderType": "LIMIT",
  "symbol": "AAPL",
  "side": "BUY",
  "quantity": 10,
  "price": 160
}
```

You’ll receive an Order ID and human-readable Order number as a response.

```json
{
      "orderId": "EF.418a5506-256c-4c3c-9d4d-f491522cf7f2",
      "orderNo": "EFXM000103"
}
```

### Placing an Options order

See [Enabling options access](https://developer.drivewealth.com/apis/docs/enabling-options-features) for prerequisite steps before orders for options will be accepted.

To place on options order, use the same [Orders endpoint](https://developer.drivewealth.com/apis/reference/post_orders) as for other asset classes, with some minor modifications.

<br />

Please note:

* The orderType must be Limit
* Only single leg options orders are allowed at this time
* The side must be BUY\_OPEN or SELL\_CLOSE as DriveWealth currently supports Level 2 trading
* Dollar-based orders are not accepted
* Time in Force DAY will be accepted

Below is an example of placing an options order:

```shell
POST /back-office/orders

{
      "accountNo": "DWPH000003",
      "orderType": "LIMIT",
      "timeInForce" : "DAY"   
      "symbol": "AAPL2305210C00013500",
      "side": "BUY_OPEN",
      "quantity": 1,
      "price": 3.42
}
```

## Receiving updates to the Order

You’ll notice the Order creation does not return any details about the processing of the Order. This processing takes time, even while the market is open. To check if an Order has been completed or updated:

```javascript
GET /back-office/orders/:orderID
{
  "id": "GB.70359e38-fe9a-412d-ab8f-364bd7e910f0",
  "orderNo": "GBPT000048",
  "type": "LIMIT",
  "side": "BUY",
  "status": "FILLED",
  "symbol": "AAPL",
  "averagePrice": 155,
  "totalOrderAmount": 1550,
  "cumulativeQuantity": 10,
  "quantity": 10,
  "amountCash": 1550,
  "fees": 1,
  "createdBy": "cc07f91b-7ee1-4868-b8fc-823c70a1b932",
  "userID": "cc07f91b-7ee1-4868-b8fc-823c70a1b932",
  "accountID": "cc07f91b-7ee1-4868-b8fc-823c70a1b932.1407776996299",
  "accountNo": "DWPH000003",
  "created": "2019-02-14T18:56:07.411Z"
}
```

This order has been completed, and the customer has purchased 10 shares at a price of $155.00 per share.

## General Order workflow

There are 3 statuses that DriveWealth considers immutable:

* `CANCELED`
* `REJECTED`
* `FILLED`

When an order is submitted it will be returned with a status of `NEW`. From here, the status can be updated to any of the following: `PARTIAL_FILL`, `CANCELLED`, `REJECTED`, `FILLED`.

A `PARTIAL_FILL` will **only** transition to `FILLED` or `CANCELED`.

On fractional orders that are < 1 share you may receive a `PARTIAL_FILL` status. For orders that are fractional but > 1 shares (eg. 5.12580012), you may receive a `PARTIAL_FILL` status prior to the order being updated to `FILLED`; however, in most cases the order will be filled in a single execution.

For partially filled orders that wind up being canceled, it's possible to determine the executed amount prior to the order cancellation using the `cumulativeQuantity` in the response. The cumulative quantity is the total amount that has been filled, where the `quantity` of an order is the amount that was requested.

<Callout icon="📘" theme="info">
  ###

  Orders for Crypto and Mutual Funds will never be partially filled.
</Callout>

In some cases, such as the [Retrieve all Orders by Account](https://developer.drivewealth.com/apis/reference/get_accounts-accountid-reports-order-history)  endpoint, you will receive a number for the orderStatus field. Refer to the table below for the number status pairs.

| orderStatus | Status Name      | Description                                                                                                                                                                                                 |
| :---------- | :--------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0           | New              | A status of NEW will persist until DriveWealth OMS receives the order. This should happen within milliseconds.                                                                                              |
| 1           | Partially filled | An order that is partially filled.                                                                                                                                                                          |
| 2           | Filled           | The order has been filled.                                                                                                                                                                                  |
| 4           | Canceled         | The order was canceled.                                                                                                                                                                                     |
| 6           | Pending Canceled | An attempt to cancel an order but the order has already been sent to the street for execution. DriveWealth can not guarantee cancellation at this point. However, most Pending Canceled orders will cancel. |
| 8           | Rejected         | Order is rejected by DriveWealth systems. For example, there is not enough buying power in a user's account. Rejected orders do not reach DriveWealth's OMS.                                                |

## Manually canceling an Order

Once an Order is created, it can be canceled manually by the customer. This applies to all types of Orders, like a limit Order to buy at a certain price or an Order to purchase stock overnight, or for asset classes other than Equities.

However, in some cases—like a market order for an equity placed during the day—there may not be any reasonable time for a customer to cancel an Order once it’s placed. For this reason, Order cancellations are by request, and may be unsuccessful.

Placing a request to cancel requires an edit to the Order:

```javascript
PATCH /back-office/orders/{orderID}
{
  "method": "CANCEL"
}
```

A response does not indicate that the cancellation has been successful, only that the request was received. If the cancellation goes through the Order will update and Events will be received:

```javascript
{
  "id": "event_a5859ce6-7c4d...",
  "type": "orders.completed",
  "timestamp": "2019-03-29T22:11:37.841989687Z",
  "payload": {
    "id": "GC.82079a33-ae23...",
    "orderNo": "GCZZ000027",
    "type": "STOP",
    "side": "SELL",
    "status": "CANCELED",
    "symbol": "AMZN",
    "triggerPrice": 100,
    "averagePrice": 0,
    "cumulativeQuantity": 0,
    "quantity": 5,
    "fees": 0,
    "createdBy": "b25f0d36-b4e4...",
    "userID": "b25f0d36-b4e4...",
    "accountID": "b25f0d36-b4e4...",
    "accountNo": "DWZR000001",
    "created": "2019-03-29T22:11:24.013Z"
  }
}
```

## Choosing an Order type

Most assets support multiple types of orders depending on the desired style of execution. The different types of orders are explained below.

### Market

Market orders are accepted for: **Equities, Mutual Funds**

Market orders are submitted immediately to execution venues (assuming the security is actively trading) and carry the highest priority. Provided there is sufficient liquidity to fill the order, customers can expect very fast execution, but without any guarantee of price.

The bid or ask the customer sees when placing the trade is an indicative price only, and due to the fast-moving nature of the market, the actual executed price may differ.

### Limit

Limit orders are accepted for: **Equities, Fixed Income, Options**

Unlike market orders, limit orders have a guarantee of price if filled. To achieve this, an order for a quantity and specified price is sent to an exchange or market maker to be later paired with a buyer or seller also willing to transact at that price. There is no guarantee that the order will be executed—for example: if a customer wants to purchase stock at $100/share, they may not ever receive a fill if the security continues to trade around $120/share.

Buy orders are created with a price below the current ask, and sell orders are created with a price above the current bid. It is possible for the customer to receive a price better than requested. Limit orders can also be set to expire up to 90 days from the date of creation.

Because limit orders need to rest in an order book at a market maker, **limit orders accept whole-share quantities only**.

### Stop & Market if Touched

Stop & Market if Touched orders are accepted for: **Equities**

Stop Orders and market-if-touched orders have very similar functions: they both create market orders when a condition has been reached.

Like limit orders, these Order types require both a quantity (or dollar amount) and a price. Unlike limit orders, this price is not a guarantee. Instead, it is a triggering price which, upon the security trading at, dispatches a market order to buy or sell the requested amount.

Trigger prices should be set according to the following:

* Buy stop: If lastTrade >= trigger price
* Buy market-if-touched: If ask >= trigger price
* Sell stop: If lastTrade <= trigger price
* Sell market-if-touched: If bid <= trigger price

Market-if-touched orders share the same side of the current price as limit orders. Because of this, they may be considered an alternative to limit orders when fractional orders are desired (keeping in mind the lack of guaranteed price).

To provide a simplified approach to choosing an appropriate order type, consider a workflow that guides the customer similar to the below:

* Buy now — (market order)
* Buy if price goes up — (stop order)
* Buy if price goes down — (market-if-touched order)

## Queuing orders for later

Some assets, like equities, trade only during certain hours. By default, orders placed outside of these hours are queued for execution during the next trading window.

DriveWealth will accept equities orders that are placed after market close, and will hold them overnight to release on market open the following business day.

If you specifically do not want an Order to be queued for the next open, use the `preventQueuing` parameter when [creating the order](https://developer.drivewealth.com/apis/reference/create-manual-order). By sending the order request with this parameter set to true, the order will be rejected if received after 4:00pm ET. This may be helpful if you think the customer is expecting an immediate execution.

To help determine whether an order will be executed immediately or queued for the next market session, there is an `orderExpires` attribute in the Order status response. For example, an order submitted after hours will have an `orderExpires` set to 4:00pm ET of the following market session.

Market orders for equities that are submitted overnight are sent to DriveWealth's executing brokers at 9:05am ET and will generally be part of the opening auction. Orders cannot be canceled after these times for the following exchanges:

* NASDAQ-listed equities — 9:28am ET
* NYSE ARCA-listed equities — 9:29am ET
* NYSE American-listed equities — 9:29am ET
* BATS Names-listed equities — 9:28am ET
* IEX Names-listed equities — 9:28am ET
* NYSE Names-listed equities — Open Time

Orders that are submitted after 9:28am ET will not be part of the opening auction.

## Security halts

Sometimes, specific securities are halted from trading by an exchange or by regulators. Derivative securities like options are halted if the underlying security is halted.

DriveWealth processes security halts differently for fractional and whole share orders.

* **Whole Share** orders that are submitted during a security halt are left in a `PENDING` state, and will be processed once the halt has been lifted.
* **Fractional Share** orders, e.g. 0.555555 shares, that are submitted during a security halt are immediately `REJECTED`.

When a security halt does occur, clients are provided an [instrument updated](https://developer.drivewealth.com/apis/reference/instrument-updated) event that would be structured as the following:

```javascript
{
    "id": "event_17913550-6db0-4086-9137-3fd728bd6821",
    "type": "instruments.updated",
    "timestamp": "2019-08-21T16:41:53.938331938Z",
    "payload": {
        "instrumentID": "26fa9515-d1c6-44ce-93b2-b94430451508",
        "previous": {
            "status": "ACTIVE"
        },
        "current": {
            "status": "HALTED"
        }
    }
}
```

<br />