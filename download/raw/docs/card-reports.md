---
updatedAt: 2025-09-05T18:29:10.000Z
---

Fetch the complete documentation index at: https://modulr.readme.io/llms.txt. Use this file to discover all available pages before exploring further. Append .md to any documentation page URL to get its markdown version.

# Card Reports

There are five card reports that are available to download:

* Daily Card Activity - Details about the previous day's activity including details of any controls that have been added to cards such as Custom Reference Fields
* Monthly Card Activity - Details of the previous month's activity including details of any controls that have been added to cards such as Custom Reference Fields
* Daily Account Funding - Details of the daily movements of money in and out of the account
* Monthly Account Funding - Details of the monthly movements of money in and out of the account
* Daily Auth Window - Details of future dated authorisation windows for cards on an account

> 📘 Daily Auth Window Reports
>
> Please note that its not possible to know exactly which transactions will come through in these windows so the detail is calculated based on the card limit available

## Being set up for reports

To ensure you are able to get reports in the first place you need to be enabled to access them, this is completed at the Onboarding and Implementation stage.

You will need to specify which reports you want access to and these will be enabled on your profile so that when you access the API's you will not be faced with an error.

## Reports available to download

To obtain the report details, which you will need to download the specific report, you will first need to make a call to [See Card Reports](https://modulr.readme.io/reference/searchreports) which will provide you a list of the reports that are available to download along with the respective ID's

```Text JSON
{
  "content": [
    {
      "id": "string",
      "reportSubjectId": "string",
      "reportDate": "2024-04-17",
      "reportType": "DAILY_CARD_ACTIVITY"
    }
  ],
  "size": 0,
  "totalSize": 0,
  "page": 0,
  "totalPages": 0
}
```

> 📘 Availability
>
> Please note that reports are held for 60 days before being archived, they will still be available to retrieve after this point as long as you know the specific report ID

## Downloading reports

Once you have the report ID's required you then need to make a call to [Get Card Reports](https://modulr.readme.io/reference/retrievereport) using the ID's provided to obtain the individual reports, these will be returned back in .csv format.

> 🚧 Report ID's
>
> You are only able to retrieve one report per call so if you have selected all five reports you will need to make five separate calls

<br />