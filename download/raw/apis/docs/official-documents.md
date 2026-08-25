---
updatedAt: 2025-08-20T23:30:37.000Z
---

Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Official documents

US regulators require all investors to receive certain documents pertaining to their Accounts. The documents must be made available to clients through your application. DriveWealth allows registered counter-parties to brand these documents with their logo and contact details.

> 🚧 UAT statement generation
>
> The sandbox does not automatically support the generation of statements. If you try to retrieve a statement in the UAT environment you will not get a response. Please contact DriveWealth to enable sandbox dummy statements for testing purposes.

## Trade confirmations

A Trade Confirmation is a required notification of a securities transaction. These are made available T+1. The customer must have access to this document prior to the completion of the settlement cycle (T+2).

<Image className="border" width="smart" border={true} src="https://files.readme.io/f295d3d-tradeconfirms.png" />

## Month-end account statements

The month-end account statement details a user's activity during a month and is uploaded to the user's accounts on the first weekend of every month; no later than the 10th of the month. Account Statements are typically available the first weekend, monthly.

<Image className="border" border={true} src="https://files.readme.io/996adca-accntstatement.png" />

<Image className="border" border={true} src="https://files.readme.io/5bcd8c0-accntStment2.png" />

## Tax documents

Read more about tax documents that are generated in the [Tax handling](https://developer.drivewealth.com/apis/docs/tax-handling) section.

## Retrieving documents

Fetching a list of documents available can be done via 3 APIs:

* [List Statements](https://developer.drivewealth.com/apis/reference/get_accounts-accountid-statements)
* [List Trade Confirms](https://developer.drivewealth.com/apis/reference/get_accounts-accountid-confirms)
* [List Tax Documents](https://developer.drivewealth.com/apis/reference/get_accounts-accountid-taxforms)

You can set the date range in the query params of the GET request to retrieve the statements for a given period of time. See the examples below:

```javascript
GET /back-office/accounts/{accountID}/statements?from=2023-01-01&to=2023-02-01
GET /back-office/accounts/{accountID}/confirms?from=2023-01-01&to=2023-02-01
```

In the above examples, the statements for January and February of 2023 will be returned. The response will contain a `displayName` and `fileKey`.

```javascript
Response:
[
  {
    "displayName": "Jun 02, 2017 Trade Confirm",
    "fileKey": "2017060201"
  },
  {
    "displayName": "Jun 26, 2017 Trade Confirm",
    "fileKey": "2017062601"
  }
]
```

Use the fileKey and accountID to fetch the individual statement URL from the [Statements Endpoint](https://developer.drivewealth.com/apis/reference/get_statements-accountid-filekey). The `url` field links the PDF version of the account statement; this is a temporary URL and will expire after 5 minutes.

```javascript
GET /back-office/statements/{accountID}/{fileKey}

Response:
{
  "accountID": "5a013513-8af1...",
  "url": "https://dzb6emi8pracf.cloudfront.net/5a013513...."
}
```

The above methodology works exactly the same for month-end statements, trade confirmations and tax forms.

## Document notifications

DriveWealth does not send out direct notifications to customers when these official documents are made available.

You can take advantage of the [Statement Events API](https://developer.drivewealth.com/apis/reference/statements-events) in order to receive a notification on your SQS queue when a new document has been made available. That Event can then be consumed and published back out through your platform in any way seen fit.

> 📘 Statement links
>
> Generally when sending a notification to a customer that their document has been made available (like over email), the physical document is not included in that notification to protect customer PII. Instead, a link to the reports section within the platform is given for customers to access.

## Hosted reports

DriveWealth additionally offers a Customer Reporting Portal that can be accessed directly through a DriveWealth hosted webpage. If a user were to close their account with you halfway through the year they could still retrieve their documents in the [Customer Reporting Portal](https://client.drivewealth.com/login).

Customers can also update their tax form information through the portal.