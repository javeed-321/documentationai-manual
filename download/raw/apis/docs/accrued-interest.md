---
updatedAt: 2026-07-13T22:58:33.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Accrued interest

# Introduction

In fixed income trading, one crucial concept that both buyers and sellers must understand is 'accrued interest.' Accrued interest plays a vital role in ensuring a fair distribution of interest earnings between the two parties involved in a bond transaction. In simple words, it represents the interest that has accumulated on a bond between the last interest payment date and the date ownership actually changes.

To illustrate this, consider a scenario where an investor wishes to buy a corporate bond with a specified coupon rate. If this purchase occurs between interest payment dates, the buyer compensates the seller for the interest that has accrued but not yet been paid. Accrued interest serves as a means to ensure that both the buyer and the seller receive their rightful share of the next scheduled interest payment.

<Callout icon="🤔" theme="default">
  ### Example

  Let's delve into a practical example to understand how accrued interest is calculated and what the seller of the bond will receive.

  Suppose you're interested in purchasing a corporate bond with a face value of $1,000 that carries a 6% annual coupon rate and settles the next day. This bond pays interest on February 15 and August 15 each year and has a 30/360 day count accrual basis. You decide to buy the bond on July 12. Here's how accrued interest is calculated:

  - #### Calculate the annual interest
    - Annual Interest = Face Value \* Annual Coupon Rate
    - Annual Interest = $1,000 \* 6% = $60
  - #### Determine the number of days between the last interest payment date (February 15) and your purchase date (July 12)
    - Days Accrued = 147 days (February has 15 days, March to June each have 30 days, and July has 12 days in 30/360 day count convention)
  - #### Calculate the daily interest rate
    - Daily Interest Rate = Annual Interest / 360 days (using the 30/360 day-count convention)
    - Daily Interest Rate = $60 / 360 = $0.1667 (rounded to four decimal places)
  - #### Calculate the accrued interest
    - Accrued Interest = Daily Interest Rate \* Days Accrued
    - Accrued Interest = $0.1667 \* 147 = $24.50 (rounded to two decimal places)

  If you buy the bond on July 12, the seller of the bond will receive the accrued interest, which is $24.50. On the next coupon payment date (Aug 15), you will receive $30 in interest. But since you paid $24.50 as accrued interest when you bought the bond, you receive a net interest of $5.50 ($30 - $24.50). This is the exact interest you would have received for owning the bond for 33 days (July 12 to August 15). In this way, accrued interest serves to maintain fairness and transparency in bond trading.
</Callout>

<br />

## Contrast with equity dividends

In equities, stocks provide periodic payments in the form of dividends, which are a portion of a company's profits distributed to shareholders, while, in fixed income, bonds pay periodic interest based on their coupon rates.

In fixed income, accrued interest for bonds ensures that both buyers and sellers are compensated fairly for the interest that has accumulated since the last payment date. This compensation is prorated according to the number of days each party holds the bond, guaranteeing that they receive their rightful share of the next scheduled interest payment. In contrast, in equities, when a stock pays dividends, the seller of the stock doesn't receive any portion of the dividend if they sell the stock before the ex-dividend date.

This distinction highlights the unique role of accrued interest in fixed income, which strives to provide equitable treatment to both parties involved in a transaction, regardless of when the trade occurs.

## Retrieving accrued interest

The accrued interest is available in the instrument level reference data endpoint. The accrued interest is reported for a single bond, with current date as the trading date. Use [GET /instruments/:instrumentID](https://developer.drivewealth.com/apis/reference/get_instruments-symbolorinstrumentid) to get the accrued interest.

As this accrued interest is available at an instrument level, when placing orders, the accrued interest for the order can be computed by taking the total number of bonds for that order. Accrued interest for an order = Accrued interest \* Number of bonds for that order.

For a buy order, the accrued interest is added to the traded order value. For a sell order, the accrued interest will be subtracted from the traded order value. This can be displayed on the order ticket on the client app.

After an order has been created, the accrued interest for that order can be obtained when the user queries for the status of the order. Use [GET orders/:orderID](https://developer.drivewealth.com/apis/reference/get_orders-orderid) to get the accrued interest at an order level.

## Journal entries

For a Fixed Income (FI) order, at a minimum, there are 3 Transactions that will be created in an Account. These are detailed as follows:

* Trade Notional: This is equal to trade price times the number of bonds transacted.
* Fees: This is the sum of fees like commission/markup.
* Accrued Interest: This is the accrued interest (as explained in this article) since the last interest payment date and date of change of ownership (i.e. one day less than settlement date).

From a client perspective, for the client account, following are the entries for a buy/sell FI transaction:

| Entry Type       | Buy FI Order          | Sell FI Order          |
| :--------------- | :-------------------- | :--------------------- |
| Trades Notional  | Debit account balance | Credit account balance |
| Fees             | Debit account balance | Debit account balance  |
| Accrued Interest | Debit account balance | Credit account balance |

<br />