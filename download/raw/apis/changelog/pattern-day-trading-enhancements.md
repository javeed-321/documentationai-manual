Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Pattern Day Trading Enhancements

## Pattern Day Trading

Enhancements are being made to how we handle accounts that are classified as Pattern Day Traders and below the FINRA-required $25k minimum equity to day trade.\
Instead of restricting customers to liquidating transactions only after their 4th day trade and when the account is below $25K, we will continue to allow the customer to buy and sell as long as they do not perform another day trade. In addition, we will provide daily reports to help you easily identify accounts which became Pattern Day Traders or had a Pattern Day Trade restriction removed. More details of the change can be found in the “What Will Change” section below.

<br />

#### Why?

We are making our restriction logic more flexible in order to impact fewer of your accounts and provide a more seamless customer experience. The new logic will allow your customers who don’t intend to day trade further the opportunity to continue to trade as normal.

<br />

#### What Will Change?

##### Trading Restriction Methodology

* If customers are under $25K in equity they will be able to Buy and Sell as normal. However, they are not permitted to day trade. If they day trade, their account status will be set to liquidating orders only for 90 days and will be classified as PDT Restricted. This will happen in real time.
* If the account equity goes above $25k at the end of day, the liquidating orders only restriction and PDT restricted designation will be removed even if the 90 days has not passed.
* After 90 days have passed since the PDT restriction, the liquidating orders only restriction and PDT restricted designation will be removed.

<br />

##### SQS Events

Events will be sent out for any of the following changes:

* account classified as a Pattern Day Trader
* account becomes PDT Restricted
* account no longer a Pattern Day Trader
* account no longer PDT Restricted

Sample Event:

```Text Sample Event- Account is no longer a pattern day trader or PDT Restricted
{
  "id": "event_4b8e2d66-badc-4101-bd12-c16b2adff105",
  "type": "accounts.updated",
  "timestamp": "2022-11-08T19:00:55.982991901Z",
  "payload": {
    "previous": {
      "status": {
        "name": "OPEN",
        "description": "Open"
      },
      "pdt": {
        "pdtRestricted": true,
        "patternDayTrader": true,
        "pdtRestrictedWhen": "2022-10-31T18:51:37.605Z"
      }
    },
    "current": {
      "status": {
        "name": "OPEN",
        "description": "Open"
      },
      "pdt": {
        "pdtRestricted": false,
        "patternDayTrader": false,
        "pdtRestrictedWhen": "2022-10-31T18:51:37.605Z"
      }
    },
    "accountID": "03bb51b9-64c9-40f7-8256-7bf8ab28c64a.1667240300776",
    "accountNo": "DWHA000069",
    "userID": "03bb51b9-64c9-40f7-8256-7bf8ab28c64a"
  }
}

```

<br />

##### DriveHub

* On the Account Details screen in DriveHub you will now be able to see if an account is classified as a Pattern Day Trader or is PDT restricted.
* Any time the pattern day trade status or pattern day trade restricted status changes, a note will be logged to you and viewable in DriveHub.
* A new pattern day trade report will be created showing the below data:
  * Timestamp restriction set/removed
  * Account Number
  * One of following 5 event types:
    * account becomes PDT
    * account becomes PDT Restricted because they are classified as a pattern day trader without $25k equity in the account
    * account no longer PDT Restricted at eod because their equity is $25k
    * account is manually cleared of being PDT Restricted and a Pattern Day Trader
    * account is manually cleared of being PDT Restricted
    * PDT Restricted cleared because it's greater than 90 days since last day trade.
  * Person (or system) which set restriction

![](https://files.readme.io/d945417-image.png)