---
updatedAt: 2026-07-13T22:52:14.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Mutual Funds

Mutual funds are professionally managed investments that pool investor money to invest in a portfolio of securities, like stocks or bonds. When you invest in a mutual fund, you're buying a share of the fund, equal to a portion of ownership in its holdings. As the fund's total value changes over time, the value of your investment also goes up or down. If the underlying stocks or bonds pay dividends or income, you receive that too.

## Types of mutual funds

DriveWealth divides its available mutual funds list into two categories:

1. US Mutual Funds - funds available to client firms incorporated within the US
2. Global Mutual Funds - funds available to client firms incorporated outside the US

Both categories are implemented using the same API calls. The only difference between them is the use of an International Securities Identification Number (ISIN) for global funds instead of a traditional ticker symbol when querying for information or initiating a transaction.

## Buying a mutual fund

Mutual funds accept orders for processing once per business day. Each fund issues a new Net Asset Value (NAV) at the end of every trading day. NAVs behave similarly to prices for equities, the main difference being that they do not change throughout the day.
Unlike equities, mutual funds often have minimum investment amounts. As long as this minimum is met, any dollar amount can be invested.
Some mutual funds charge a percent of each purchase as a fee, often called a “front-end load” charge.

## Owning a mutual fund

Owners of mutual funds receive ongoing dividends and cash distributions as they are collected and distributed by the fund.<br />Global Mutual Fund clients sometimes benefit from selecting “accumulation” share classes. These types of share classes ensure that cash income is not disbursed causing unwanted or unexpected tax events.<br />Some mutual funds charge a 12b-1 fee which behaves similarly to a management fee, collecting up to 1% (typically between .25% - .75%) in the value of held shares, often monthly. Fee schedules differ from fund to fund.

## Selling a mutual fund

Some mutual funds charge a fee when positions are sold called a “back-load” fee. Many back-load fees can be avoided by holding positions for a predetermined amount of time before selling, often 1 year or more.

<br />