---
updatedAt: 2025-08-20T23:30:36.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Showing historical transactions

All activity that occurs in an Account—whether deposits, withdrawals, trades, corporate actions, or others—are journaled via Transaction objects. These can be listed for any date range to show the historical activity in an Account.

For example, a purchase of an equity would result in the following Transaction:

```javascript
{
      "orderId": "IC.4c108af2-3c65-4215-84f6-b9b338528096",
      "orderNo": "ICPB023294",
      "symbol": "AAPL",
      "cumQty": 1,
      "orderStatus": "2",
      "orderType": "1",
      "orderQty": 1,
      "limitPrice": 0,
      "stopPrice": 0,
      "executedPrice": 122.47,
      "side": "B",
      "createdWhen": "2021-03-22T15:23:21.100Z",
      "updatedWhen": "2021-03-22T15:23:21.102Z",
      "updatedReason": "market_order-buy-filled",
      "commission": 0,
      "commissionDesc": "Standard Commission",
      "isoTimeRestingOrderExpires": "2021-03-22T20:00:00.000Z",
      "executedWhen": "2021-03-22T15:23:21.102Z",
      "realizedPL": null,
      "orderCashAmt": 0
}
```

View the [List Transactions by Account](https://developer.drivewealth.com/apis/reference/get_accounts-accountid-transactions) API to learn more about each field returned.

Generally, each Transaction manipulates cash, a single asset position, or both. Some actions, which result in multiple positions being adjusted, can result in multiple Transactions being created. You can see examples of these in [Creating an order](https://developer.drivewealth.com/apis/docs/creating-an-order) and in the API Reference for [Corporate action Events](https://developer.drivewealth.com/apis/reference/stock-splits).

## List of Transaction types

Each Transaction has a `finTranTypeID` which informs the overall type of journal that took place.

| Transaction type    | Description                                                                                            |                                               |
| ------------------- | ------------------------------------------------------------------------------------------------------ | --------------------------------------------- |
| CSR                 | A deposit                                                                                              |                                               |
| CSD                 | A withdrawal                                                                                           |                                               |
| FEE                 | A fee was deducted from the account. Fee types can include AUM and withdrawal fees                     |                                               |
| JNLC                | A cash journal was made from one account to another                                                    |                                               |
| CADJ                | "A credit adjustment was made                                                                          | generally used for returned ACH transactions" |
| INT                 | An interest adjustment                                                                                 |                                               |
| SPUR                | A security (stock/ETF/ADR) was bought                                                                  |                                               |
| SSAL                | A security (stock/ETF/ADR) was sold                                                                    |                                               |
| MERGER\_ACQUISITION | A merger or acquisition has taken place                                                                |                                               |
| DIV                 | A dividend payment                                                                                     |                                               |
| DIVTAX              | A tax withholding on a dividend                                                                        |                                               |
| DIVNRA              | A tax withholding on a dividend for a non-resident alien                                               |                                               |
| STCK                | A stock price adjustment                                                                               |                                               |
| COMM                | A commission                                                                                           |                                               |
| SPINOFF             | Stock spinoff                                                                                          |                                               |
| STOCK\_SPLIT        | Stock split/reverse stock split                                                                        |                                               |
| ACATS\_CASH         | ACATS cash delivery or receive                                                                         |                                               |
| ACATS\_STOCK        | ACATS stock delivery or receive                                                                        |                                               |
| CCPUR               | Crypto Currency Purchase                                                                               |                                               |
| CCSAL               | Crypto Currency Sale                                                                                   |                                               |
| SLIP                | An interest payment for security lending rebates                                                       |                                               |
| DIVM                | A dividend that is received when shares are on loan as part of the fully paid security lending program |                                               |