Fetch the complete documentation index at: https://developer.drivewealth.com/apis/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# API Release 1.18

## API Release 1.18

| Release Date | Status       |
| :----------- | :----------- |
| June 3, 2021 | **RELEASED** |

## IFA Restructure Events

For DriveWealth Partners who are implementing the new bulk deposit mechanism, new events have been created that will get triggered based upon report resource changes. At the end of each day a settlement report is generated and confirmed which triggers these new events. Once a bulk transfer has been received by DriveWealth the status is then modified to be successful.

Examples of the new event messages can be found below:

```json Settlements Created
{
  "id": "event_5c489c65-fd17-48f8-bfbf-146b46f01ee5",
  "type": "reports.instantFundingSettlement.created",
  "object": "INSTANT_FUNDING_SETTLEMENT_REPORT",
  "timestamp": "2021-05-25T19:27:00.231Z",
  "payload": {
    "settlementID": "1b06c469-9706-4ea0-90a6-9ad8f441d6ca_20210525",
    "settlementDate": "2021-05-25",
    "status": "PENDING",
    "statusComment": "Created from aggregator service",
    "totalAmount": 100,
    "depositsAmount": 100,
    "created": "2021-05-25T00:45:00.293Z",
    "updated": "2021-05-25T00:45:00.293Z",
    "updatedBy": "Instant Funding Aggregator Job"
  },
  "ibID": "1b06c469-9706-4ea0-90a6-9ad8f441d6ca"
}
```
```json Settlements Updated
{
  "id": "event_5c489c65-fd17-48f8-bfbf-146b46f01ee5",
  "type": "reports.instantFundingSettlement.updated",
  "object": "INSTANT_FUNDING_SETTLEMENT_REPORT",
  "timestamp": "2021-05-25T19:27:00.231Z",
  "payload": {
    "settlementID": "1b06c469-9706-4ea0-90a6-9ad8f441d6ca_20210525",
    "settlementDate": "2021-05-25",
    "status": "PENDING",
    "statusComment": "Created from aggregator service",
    "totalAmount": 100,
    "depositsAmount": 100,
    "created": "2021-05-25T00:45:00.293Z",
    "updated": "2021-05-25T19:27:00.223Z",
    "updatedBy": "Instant Funding Aggregator Job"
  },
  "ibID": "1b06c469-9706-4ea0-90a6-9ad8f441d6ca"
}
```

## New Field within GET /countries Endpoint

Attempting to identify countries that are acceptable values for citizenship during the onboarding process has always been difficult. In an effort to improve transparency around this DriveWealth is now releasing an additional boolean property within the `GET /countries` endpoint that is labeled: `expatsAllowed`.

`expatsAllowed` takes two forms:

* **`true`** - The country is available for users to select as their citizenship
* **`false`** - The country is NOT available for users to select as their citizenship

> 🚧 Country Status and Availability
>
> Not all countries will have an `expatsAllowed` property available. If a countries has `active : true` then by default `expatsAllowed` is assumed to be true.

```json
[
    {
        "id": "ALA",
        "name": "Aland Islands",
        "code2": "AX",
        "code3": "ALA",
        "active": true,
        "expatsAllowed": true
    },
    {
        "id": "ALB",
        "name": "Albania",
        "code2": "AL",
        "code3": "ALB",
        "active": true,
        "expatsAllowed": false
    }
]
```