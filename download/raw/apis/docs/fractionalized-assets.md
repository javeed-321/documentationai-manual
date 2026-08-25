---
updatedAt: 2025-08-20T23:55:25.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Fractionalized assets

Equities and Mutual Funds on DriveWealth’s platform can support fractional purchases, sales, and holdings.

## Determining fractional support

To verify that an asset is supported fractionally, refer to its Instrument details:

```javascript
GET /back-office/instruments/AAPL
{
  "symbol": "AAPL",
  "name": "Apple, Inc.",
  "sector": "Technology",
  "longOnly": true,
  "orderSizeMax": 10000,
  "orderSizeMin": 0.00000001,
  "orderSizeStep": 0.00000001,
  "id": "a67422af-8504-43df-9e63-7361eb0bd99e",
  "type": "EQUITY",
  ...
}
```

This equity asset can be traded in increments of 0.00000001 share. This is common across nearly all equities on the platform, though in very rare circumstances, an equity asset may need to be disabled for fractional trading by updating these values.

Note that some assets, like mutual funds, have a minimum purchase amount. These can still be traded fractionally, but the Order will need to meet the minimum requirement.

## Trading fractionally

Order creation allows for two fields to specify an amount:

* **quantity** — An exact number of units to buy or sell
* **amountCash** — An exact amount of USD to buy or sell

Choose one based on the intended experience. For example:

> The last price of ABCD was $40/share. Andre places an order to purchase 3 shares. The Order is completed, and Andre receives exactly 3 shares, but pays $122.94, since the price of ABCD changed while the Order was being submitted.
>
> The last price of WXYZ was $20/share. Joseph places an order to purchase $1,000 worth of stock. The Order is completed, and Joseph receives exactly $1,000 worth of shares, which is equal to 50.0531 shares by the time the Order is completed.

When a customer is selling stock, be cautious of submitting cash-denominated trades that are very close to their total position. For example:

> The last price of EFGH was $10/share. Isaiah holds 5 shares, worth $50, and submits an order to sell $50 worth of stock. When the order is completed, Isaiah receives $50 in cash, but still has $0.01 worth of stock left in his account, because the price changed while the order was being placed.

To avoid this edge case, it is common for an implementation to switch an Order’s definition to being denominated in a quantity before being sent to DriveWealth, if the customer is clearly intending to sell their entire position.