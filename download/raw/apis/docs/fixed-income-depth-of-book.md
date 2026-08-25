---
updatedAt: 2025-08-20T23:29:58.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Depth of book

# Introduction

“Depth of book” for fixed income instruments refers to the display of buy and sell orders at various price levels in the order book. This concept provides market participants with transparency into the supply and demand dynamics for fixed income securities, such as bonds. By revealing the quantity of bonds available for purchase or sale at different price points, along with minimum quantity requirements to trade, the depth of book aids in assessing liquidity, price transparency, and market efficiency. Traders and investors can use this information to make informed decisions about executing trades, managing risk exposure, and determining the fair market value of a particular fixed income instrument.

> 🤔 Example
>
> Let's delve into a practical example to understand this concept. Below table shows the order book for a particular bond:
>
> | Qty (min) | Bid Price (Sell) | Ask Price (Buy) | Qty (min) |
> | :-------- | :--------------- | :-------------- | :-------- |
> | 300(75)   | 99.57            | 99.65           | 400(100)  |
> | 80(10)    | 99.50            | 99.70           | 70(10)    |
> |           |                  | 99.75           | 10(1)     |
>
> ‎
>
> We see that a dealer has 400 bonds (or $400,000 par value) available to buy at a price of 99.65% par value (i.e. $996.50 per bond). The dealer has also specified that a minimum\
> of 100 bonds (or $100,000 par value) must be purchased in order to buy at that price.
>
> Similarly, we see that a dealer has 300 bonds (or $300,000 par value) available for sale at a price of 99.57% par value (i.e. $995.70 per bond). The dealer has also specified that a minimum\
> of 75 bonds (or $75,000 par value) must be transacted in order to sell at that price.
>
> Both of these quotes are the best prices to buy and sell. Together, they are the best bid and best ask and they constitute the “top of book”, as shown below:
>
> | Qty(min) | Bid Price (Sell) | Ask Price (Buy) | Qty(min) |
> | :------- | :--------------- | :-------------- | :------- |
> | 300(75)  | 99.57            | 99.65           | 400(100) |
>
> ‏‏‎ ‎
>
> In the “depth of book” illustration, we see additional bids and asks at prices worse than the “top of book”. They also provide information on the quantities, prices and minimum quantities to trade for each bid/ask.
>
> By making the “depth of book” available, one can choose a price point at which one can meet the minimum quantity requirements for trading a bond. In this way, an investor can get a holistic view of the actual liquidity available for that instrument.
>
> “Depth of book” at times, may reflect price discounts for volume. As an analogy, one may purchase a single donut for a dollar, but could buy a dozen donuts for 10$. By buying the donuts in large quantities, the price per donut is less. Similarly, the best prices are normally available at the “top of book”, but one would have to trade larger quantities to avail of that price.
>
> In our example, if one wanted to only buy 10 bonds, they wouldn’t be able to interact with the best ask (i.e. 99.65). However, by paying 5c more, they could interact with the 99.70 ask and be able to purchase the 10 bonds.
>
> Also, in addition to prices, the dealers could also specify yields on the bid/ask quotes on the order book, as depicted below:
>
> | Bid Yield | Qty(min) | Bid Price(Sell) | Ask Price(Buy) | Qty(min) | Ask Yield |
> | :-------- | :------- | :-------------- | :------------- | :------- | :-------- |
> | 6.75      | 300(75)  | 99.57           | 99.65          | 400(100) | 6.72      |
> | 6.77      | 80(10)   | 99.50           | 99.70          | 70(10)   | 6.70      |
> |           |          |                 | 99.75          | 10(1)    | 6.68      |

<br />

## Retrieving depth of book

The “depth of book” is a new endpoint, exclusive to fixed income instruments. One can use the [GET /quotes/depth](https://developer.drivewealth.com/apis/reference/getquotedepth) endpoint.