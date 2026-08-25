---
updatedAt: 2026-07-13T23:00:19.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Displaying prices and information

## Asset details

Every asset on the DriveWealth platform has associated fundamental and general information data. These data points can allow investors to make more informed decisions, or help platforms ingest typical asset components such as a company logo.

<Callout icon="📘" theme="info">
  ### Data best practices

  Most fundamental data is updated on a daily basis and should be stored in cache to limit the total number of requests to the instrument's endpoint. General information such as logo and prospectus links that do not update frequently can be stored for longer.
</Callout>

Data is retrieved through the instruments endpoint, requiring an already stored `instrumentID`. Please note `instrumentID`’s are different between DriveWealth environments.

Upon a successful request, the API returns point in time quote information for the requested symbol. A client should expect the following data within a successful response:

```javascript
{
  "symbol": "AAPL",
  "reutersPrimaryRic": "AAPL.O",
  "name": "Apple, Inc.",
  "description": "Apple Inc. designs, manufactures and markets mobile communication and media devices, personal computers and portable digital music players. The Company sells a range of related software, services, accessories, networking solutions, and third-party digital content and applications. The Company's segments include the Americas, Europe, Greater China, Japan and Rest of Asia Pacific. The Americas segment includes both North and South America. The Europe segment includes European countries, India, the Middle East and Africa. The Greater China segment includes China, Hong Kong and Taiwan. The Rest of Asia Pacific segment includes Australia and the Asian countries not included in the Company's other operating segments. Its products and services include iPhone, iPad, Mac, iPod, Apple Watch, Apple TV, a portfolio of consumer and professional software applications, iPhone OS (iOS), OS X and watchOS operating systems, iCloud, Apple Pay and a range of accessory, service and support offerings.",
  "sector": "Technology",
  "longOnly": true,
  "orderSizeMax": 10000,
  "orderSizeMin": 1e-8,
  "orderSizeStep": 1e-8,
  "exchangeNickelSpread": false,
  "close": 0,
  "fundamentalDataModel": {
    "instrumentID": "a67422af-8504-43df-9e63-7361eb0bd99e",
    "symbol": "AAPL",
    "companyName": "APPLE INC",
    "openPrice": 207.86,
    "bidPrice": 204.74,
    "askPrice": 204.75,
    "lowPrice": 203.53,
    "highPrice": 208.55,
    "fiftyTwoWeekLowPrice": 142,
    "fiftyTwoWeekHighPrice": 233.47,
    "cumulativeVolume": 16934795,
    "marketCap": 915766600000,
    "peRatio": 17.9371,
    "dividendYield": 1.4916,
    "earningsPerShare": 11.5119,
    "dividend": 3.08,
    "sharesOutstanding": 4515829802,
    "timeLastUpdate": "19:37:00",
    "bookValuePerShare": "22.53361",
    "cashFlowPerShare": "14.38949",
    "operatingIncome": "72903000000",
    "pbRatio": "9.51980",
    "volumeMovingAverage10Day": 30891720,
    "volumeMovingAverage25Day": 31570250,
    "volumeMovingAverage50Day": 26449505,
    "priceMovingAverage50Day": 203.529,
    "priceMovingAverage150Day": 191.2912,
    "priceMovingAverage200Day": 185.6304,
    "roe": "0.5062"
  },
  "id": "a67422af-8504-43df-9e63-7361eb0bd99e",
  "type": "EQUITY",
  "exchange": "NSQ",
  "url": "http://investor.apple.com",
  "status": "ACTIVE",
  "exchangeThresholdOverride": null,
  "houseThresholdOverride": null,
  "closePrior": 206.49,
  "image": "http://syscdn.drivewealth.net/images/symbols/aapl.png"
}
```

Data that is returned varies based on the asset class. Refer to [Retrieve Instrument](https://developer.drivewealth.com/apis/reference/get_instruments-symbolorinstrumentid) for full details.

For assets such as Mutual Funds and ETFs certain data may be unavailable as they do not relate to funds. This could include `earningsPerShare` and `peRatio`.

Since options are a derivative product, they do not include all the same Instrument information that you may see for an Equity or ETF. Refer to the underlying instrument for more information.

<Callout icon="📘" theme="info">
  ### Logo query parameters

  Every logo allows for customization through hosting on [imgix](https://imgix.com). For example, to render a logo and adjust its size, it’s possible to add `/fit=crop&w=300&max-h=300` to the image URL.
</Callout>

## Quotes and prices

DriveWealth APIs carry pricing data for Equities, Mutual Funds, and Fixed Income securities.

Equities data is split into different data feeds for retrieving the prices of assets:

| Market data option         | Coverage                                              | Price                   | Typical use                                                                     |
| :------------------------- | :---------------------------------------------------- | :---------------------- | :------------------------------------------------------------------------------ |
| Referential Feed           | Equities (listed, core session, includes OTC), Crypto | Per customer, per month | Display data prior to and on execution for non-US Clients / Customers           |
| Consolidated Exchange Feed | Equities (listed, core+extended sessions)             | Per request             | Display data prior to a customer submitting a trade, and prior to its execution |
| 15 Minute Delayed Feed     | Equities (listed, core session)                       | Free                    | Watchlist and symbol searches                                                   |

A user must first be successfully created in order for a customer to be shown the market data. This is required because DriveWealth has a reporting requirement to the exchanges for who is accessing the data.

All market data endpoints require that the `userID` of the customer who is being provided the quote is passed as a parameter within the header of the API call being made; as shown below.

```javascript
GET /back-office/quotes/AAPL
dw-customer-user-id: {userID}
```

Upon a successful request, the API returns point in time quote information for the requested symbol.

```javascript
{
    "symbol": "AAPL",
    "bid": 208.94,
    "ask": 208.96,
    "lastTrade": 208.95,
    "change": 3.24,
    "open": 208.39,
    "high": 208.95,
    "low": 207.32,
    "close": 0,
    "priorClose": 205.7,
    "volume": 9663099,
    "marketCondition": "NORMAL",
    "dataProvider": "BATS"
}
```

<Callout icon="🚧" theme="warn">
  ### Storing data

  DriveWealth does not allow redistribution or non display of market data, meaning: clients may not store any data received for further use within their infrastructure.
</Callout>

You’ll notice above that there are multiple numbers that can be used to represent the single “price” of a security. For most assets, these 3 values are important in different contexts:

* `bid` — Shown at the time when a sale is being contemplated by customer
* `ask` — Shown at the time when a buy is being contemplated by the customer
* `lastTrade` — Displayed as a primary price of the asset elsewhere in the experience

US-regulated firms are required to show additional data points at certain points of the investing experience based on local regulations. Notice that when requesting a quote from the Consolidated Data Feed, additional values like the reporting exchanges and bid/ask volume are returned:

```javascript
{
    "symbol": "AAPL",
    "bid": 170.6,
    "ask": 170.62,
    "open": 170.4,
    "high": 170.95,
    "low": 169.16,
    "timeOffset": 1544627364231,
    "volume": 6259019,
    "askSize": 4,
    "bidSize": 3,
    "change": 1.99,
    "lastTradeExchange": "DA",
    "bestBidExchange": "Q",
    "bestAskExchange": "BT",
    "lastTrade": 170.62,
    "lastTradeSize": 100,
    "marketCondition": "NORMAL",
    "tradeCount": 39169,
    "close": 0,
    "priorClose": 168.63
}
```

<br />