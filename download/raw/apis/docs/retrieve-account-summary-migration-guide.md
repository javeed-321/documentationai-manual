---
updatedAt: 2026-07-13T18:38:46.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Retrieve Account Summary Migration Guide

## Overview

The endpoint `GET /accounts/{accountID}/summary` is deprecated.

To migrate, call the supported endpoints below and compose your own summary response object.

## Endpoint Replacement Matrix

| Deprecated endpoint                 | Replacement endpoint(s)                       | Notes                                                                  |
| :---------------------------------- | :-------------------------------------------- | :--------------------------------------------------------------------- |
| `GET /accounts/{accountID}/summary` | `GET /accounts/{accountID}/summary/money`     | Source of `cash` values and account-level money metadata.              |
| `GET /accounts/{accountID}/summary` | `GET /accounts/{accountID}/summary/margin`    | Source of margin fields.                                               |
| `GET /accounts/{accountID}/summary` | `GET /accounts/{accountID}/summary/positions` | Source of equity positions and valuation fields.                       |
| `GET /accounts/{accountID}/summary` | `GET /accounts/{accountID}/summary/orders`    | Source of currently resting (pending) orders.                          |
| `GET /accounts/{accountID}/summary` | `GET /accounts/{accountID}/transactions`      | Source of historical transaction activity (date-range query required). |
| `GET /accounts/{accountID}/summary` | `GET /accounts/{accountID}`                   | Source of canonical account identity and account metadata.             |

## Field Mapping

Use this mapping if your client currently expects the deprecated `SummaryRes` shape.

### accountSummary

| Deprecated field             | Replacement source                                                   |
| :--------------------------- | :------------------------------------------------------------------- |
| `accountSummary.accountID`   | `summary/money.accountID` (or `summary/positions.accountID`)         |
| `accountSummary.accountNo`   | `summary/money.accountNo` (or `summary/positions.accountNo`)         |
| `accountSummary.tradingType` | `summary/money.tradingType` (or `summary/positions.tradingType`)     |
| `accountSummary.lastUpdated` | `summary/money.updated` (closest equivalent to legacy `lastUpdated`) |
| `accountSummary.cash`        | `summary/money.cash`                                                 |

### margin

| Deprecated field | Replacement source      |
| :--------------- | :---------------------- |
| `margin`         | `summary/margin.margin` |

### equity

| Deprecated field         | Replacement source                  |
| :----------------------- | :---------------------------------- |
| `equity.equityValue`     | `summary/positions.equityValue`     |
| `equity.equityPositions` | `summary/positions.equityPositions` |

### orders

| Deprecated field | Replacement source      |
| :--------------- | :---------------------- |
| `orders`         | `summary/orders.orders` |

`summary/orders` returns only resting (pending) orders, which aligns with legacy summary behavior.

### transactions

| Deprecated field | Replacement source              |
| :--------------- | :------------------------------ |
| `transactions`   | `transactions` response payload |

Legacy `transactions` in the deprecated summary used `transactionSumObj`; `GET /accounts/{accountID}/transactions` returns `transactionObj` with overlapping but not identical field names.

Key normalization differences to handle in client code:

* `orderID` (legacy) vs `orderId` (transactions endpoint)
* `commissions` (legacy) vs `commission` (transactions endpoint)
* `GET /accounts/{accountID}/transactions` requires `from` and `to` query parameters

## Recommended Orchestration Pattern

1. Call these endpoints in parallel:
   * `GET /accounts/{accountID}/summary/money`
   * `GET /accounts/{accountID}/summary/margin`
   * `GET /accounts/{accountID}/summary/positions`
   * `GET /accounts/{accountID}/summary/orders`
2. Call `GET /accounts/{accountID}/transactions?from={fromISODate}&to={toISODate}` for transaction history window needed by your product.
3. Optionally call `GET /accounts/{accountID}` if your UI also depends on additional account metadata outside the legacy summary payload.
4. Build a compatibility object for downstream consumers.

## Compatibility Object Example

```json
{
  "accountSummary": {
    "accountID": "<from money.accountID>",
    "accountNo": "<from money.accountNo>",
    "tradingType": "<from money.tradingType>",
    "lastUpdated": "<from money.updated>",
    "cash": "<from money.cash>"
  },
  "margin": "<from margin.margin>",
  "equity": {
    "equityValue": "<from positions.equityValue>",
    "equityPositions": "<from positions.equityPositions>"
  },
  "orders": "<from orders.orders>",
  "transactions": "<from transactions endpoint payload>"
}
```

## Migration Checklist

* Replace all direct calls to `GET /accounts/{accountID}/summary`.
* Add aggregation logic that composes the replacement payload.
* Normalize transaction field names where needed (`orderId`/`orderID`, `commission`/`commissions`).
* Add integration tests for:
  * cash and buying power values,
  * margin values,
  * positions valuation,
  * pending orders,
  * transactions date-window behavior.
* Remove deprecated response-type dependencies from client models.

<br />