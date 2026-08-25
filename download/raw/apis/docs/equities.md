---
updatedAt: 2025-08-20T23:54:49.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Equities

An equity is a security that represents the ownership of a fraction of a corporation or other asset. This entitles the owner of the stock to a proportion of the corporation's assets and profits equal to how much stock they own.

## Types of equities

* **Stocks** represent ownership of a company
* **ETFs** (Exchange Traded Funds) represent ownership of many securities, all rolled into one
* **ADRs** (American Depositary Receipts) are stocks of international companies that have been listed for trading in the US

The end-to-end experience for interacting with all of these assets is extremely consistent.

> 🚧
>
> Some types of equities cannot be offered in certain countries, or to certain investors. For example, the UK and EU do not allow for the sale of US-traded ETF products.
>
> Within these categories, there may be additional considerations to take on each asset. Some ETFs, for example, are leveraged, meaning the price movement of the underlying assets are multiplied for holders of the ETF. These instruments often should not be sold to investors with little investing experience.

> 🚧
>
> Some types of equities can incur fees for the shareholder while they are owned. These include ADRs and stocks issued by FPIs (**Foreign Private Issuers**: international companies listing their own stock in the US). These fees are typically a few cents per year and cover FX conversion, custody, or similar concerns, and are described in each security’s prospectus or filing documents.

## Buying an equity

Equities trade on all public exchanges on most business days from 9:30am to 4pm ET. During this time, orders are accepted to buy and sell at either the best available price, or at a price specified by the customer. The price of every equity updates every few milliseconds to represent the last trades that took place.

### Buying equities after hours

Although the US equity market is primarily open from 9:30 to 4, some exchanges and off-exchange networks allow for the transacting of equities outside of these hours. This is referred to as “after hours trading.” DriveWealth supports trading equities from 4:00am to 8:00pm ET, though not all securities will have much liquidity during this window. This could result in orders failing to fill, or filling with a price far away from the anticipated execution price.

Learn more in [Creating an order](https://developer.drivewealth.com/apis/docs/creating-an-order).

### Buying equities Over-the-Counter

Some equities are registered for sale in the US, but don’t trade on exchanges. Many can be traded on DriveWealth like any other equity, but often have limited liquidity and wide spreads.

## Owning an equity

Owners of equity are entitled to receive certain compensation and adjustments as determined by the corporation. These adjustments occur automatically and can include scenarios like:

* Receiving cash as a dividend
* Receiving more shares as a dividend
* Exchanging shares for cash (like if the corporation gets purchased)

Other events are not mandatory and allow each shareholder to participate only if he or she chooses. These are often referred to as “voluntary actions” and include:

* Voting on a proposal from the corporation
* Agreeing to accept a public cash offer for one’s shares (a “tender offer”)

Learn more in the [Corporate actions](https://developer.drivewealth.com/apis/docs/corporate-actions) section.