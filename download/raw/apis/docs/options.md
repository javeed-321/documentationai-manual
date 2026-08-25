---
updatedAt: 2026-07-13T22:54:02.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Options

An option is a derivative that gives the holder the right to purchase or sell an underlying security at a defined price (called the "strike price") through a defined date (called the “expiration date”). Typically 1 contract represents 100 shares of the underlying security.

## Types of options

* **Call options** allow the holder to *purchase* the underlying at the strike price, on or before the expiration date
* **Put options** allow the holder to *sell* the underlying at the strike price, on or before the expiration date

## Options Trading with DriveWealth

DriveWealth currently supports options trading on Equity and ETF underlyings in individual brokerage accounts.

There are two primary integration models for clients at DriveWealth, Fully Disclosed and Omnibus. Options Trading is currently available to Fully Disclosed Clients, and each user under a Fully Disclosed client must proceed through an options onboarding and approval process before their account can be enabled.

Different options trading strategies are grouped into levels based on their complexity and associated risks, and investors will be evaluated to see which level of options trading is appropriate for them based on a set of defined thresholds. DriveWealth currently supports Level 2 trading, which is the ability to Buy Calls and Buy Puts.

The below guide walks you through how to enable an end-to-end options trading experience.

## Step 1: Request DriveWealth Enablement

Please work with your Relationship Manager to ensure your client environment is enabled for options trading prior to proceeding.

## Step 2: Approving accounts to trade options

Options are complex instruments and thus, per FINRA Rule 2360, customer accounts must be approved for options trading before they can place their first options trade. In order to be evaluated for options trading, investors must provide certain personal information, including details about their trading history and risk profile. Customers must also acknowledge an Options Disclosure.

Once the <Anchor target="_blank" href="https://developer.drivewealth.com/apis/v1.83.0/docs/enabling-options-features">automated option approval process </Anchor>has been completed for a user and they’ve been approved for options trading, their account can be enabled for options trading.

## Step 3: Discovering an option contract to trade

<Image src="https://files.readme.io/65f8011-Discover-Bull2x.png" align="right" width="300px" wrap={true} />

DriveWealth supports options trading on Equity and ETF underlying. Equity & ETF options trade on public exchanges on trading days from 9:30am to 4pm ET. Options on a small subset of broad-based ETFs trade from 9:30am to 4:15pm ET. During trading hours, orders are accepted to buy and sell at a price specified by the customer.

The below guide walks you through how to enable an end-to-end options trading experience.

Typically, finding options to buy starts with picking an underlying security. Once a security is picked, an investor can narrow down the list of candidate option contracts by expiration date and strike price.

Learn more and review specific implementation details in <Anchor target="_blank" href="doc:filtering-options">Showing options chains</Anchor>.

## Step 4: Placing an option trade

DriveWealth currently supports Level 2 options trading, which means that investors have the ability to buy Call Options and Put Options, and then sell out of these positions.

DriveWealth clients can leverage the <Anchor target="_blank" href="https://developer.drivewealth.com/apis/reference/post_orders">Orders API</Anchor>  used for other asset classes to submit options orders. Additional order validations exist to ensure that appropriate options attributes are included in the order submission.

| Order Type |         Order Mode         | TIF | Slides Supported            |
| :--------- | :------------------------: | --: | :-------------------------- |
| Limit      | Whole  Contract (quantity) | Day | BUY\_OPEN,<br />SELL\_CLOSE |

Please refer to <Anchor target="_blank" href="https://developer.drivewealth.com/apis/docs/creating-an-order">Creating an Order</Anchor>  for implementation details and an example of placing an options order.

## Owning an option contract

Investors can check information about their open options positions alongside other asset class positions that they may hold with DriveWealth.

Please refer to <Anchor target="_blank" href="doc:getting-balances-and-positions">Getting balances and positions</Anchor> for more details on reviewing an account’s position summary, inclusive of options positions

### During corporate actions

Corporate actions that affect the underlying security (splits, dividends, mergers, etc.) typically also affect options. In most cases, the original option Instrument is marked INACTIVE, and a new option Instrument is created for existing positions.

Options corporate events consist of a bit more data because of updates that need to be made to the instrument and option positions. When an option corporate action event does occur there will be four (4) events created:

* Two instrument.updated events (expiring the pre-existing symbol, and setting the new symbol as active)
* Two positions.updated (removal of the position in pre-existing symbol and adding a position in the new one).

### On expiration day

Investors who hold an option contract may choose to exercise the option contract early, or submit a Do Not Exercise request.

On expiration day, the OCC may automatically exercise options positions that remain open after market close if they’re at least $0.01 in-the-money. Investors are expected to manage their options positions leading up to expiration and clients should remain oversight into this process and manage risk as necessary.

DriveWealth reserves the right to take action leading up to market close on expiration day in order to mitigate risk related to the exercise process.

If a position held in an account expires worthless and with no other activity, it will be removed from the account.

## Exercising an option

Contract holders can choose to exercise their right to purchase or to sell the underlying security based on the number of contracts they hold. This can be done up until the date of expiration.

* For a call option holder, the investor must have enough cash in their account to complete the purchase (typically, the number of contracts × the strike price × 100).
* For a put option holder, the investor must have enough shares in their account to complete the sale (typically, the number of contracts × 100).

Contract holders may also submit a “Do Not Exercise” request to prevent an ITM position from being exercised by The OCC on expiration day.  For more information see <Anchor target="_blank" href="https://developer.drivewealth.com/apis/v1.83.0/docs/exercising-contracts-managing-expiration">exercising contracts and managing expiration</Anchor>.

## Option Market Data

Please note that DriveWealth leverages 15-minute delayed market data for position display values. At this time, DriveWealth does not redistribute market data.